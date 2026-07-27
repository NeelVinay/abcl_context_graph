"""Phase 2: train the distilled student model on Claude's gold labels.

Features per turn (all local, no API):
  - sentence embedding of the turn text        (meaning)
  - sentence embedding of the PREVIOUS turn     (context: disambiguates short acks)
  - speaker (agent/customer)                    (different intent distributions)
  - normalized position in the call             (greeting early, transfer late)

A scikit-learn LogisticRegression learns base_intent from these. We measure with
GroupKFold (split by CALL, so turns from one call never span train+test -> honest),
then train a final model on ALL data and save it.

  python -m src.distill eval    # grouped CV, print metrics vs gold (the 'after')
  python -m src.distill train   # train final model on all gold, save to data/models/
"""
from __future__ import annotations

import json
import pickle

import numpy as np

import config
from src.evaluate import GOLD_PATH, load_gold, score_intents
from src.extract import EMBED_MODEL

MODELS_DIR = config.CACHE_DIR.parent / "models"
MODEL_PATH = MODELS_DIR / "intent_clf.pkl"

# intfloat/multilingual-e5-* models were trained expecting a "query: " prefix on
# every encoded text (both sides — there's no asymmetric query/passage split for a
# classification-style use like this). Measured in scripts/_generic_embed_model_eval.py:
# a genuinely different/more modern embedder (not just a bigger one — a same-family
# bigger model showed no gain) gave a real cross-domain accuracy jump (+6 to +9 points)
# on the `generic` domain. Applied ONLY there — ABCL/JustDial keep their existing
# MiniLM model rather than force a retrain of something already working.
def embed_prefix_for(embed_model: str) -> str:
    return "query: " if embed_model.startswith("intfloat/multilingual-e5") else ""


GENERIC_EMBED_MODEL = "intfloat/multilingual-e5-base"

# Domain -> (gold labels path, model output path). ABCL is the default/back-compat.
DOMAINS = {
    "abcl": {"gold": GOLD_PATH, "model": MODEL_PATH, "embed_model": EMBED_MODEL},
    "justdial": {"gold": config.DATA / "gold_justdial" / "labels.jsonl",
                 "model": MODELS_DIR / "justdial_clf.pkl", "embed_model": EMBED_MODEL},
    "justdial_coarse": {"gold": config.DATA / "gold_justdial" / "labels_coarse.jsonl",
                        "model": MODELS_DIR / "justdial_clf.pkl", "embed_model": EMBED_MODEL},
    # Cross-client broad-bucket model — trained on whatever clients have been dropped
    # into data/generic_transcripts/ (GEN-<client>-<id> naming) and labeled via
    # src/generic_taxonomy.py. This is the model that tests generalization.
    "generic": {"gold": config.DATA / "gold_generic" / "labels.jsonl",
                "model": MODELS_DIR / "generic_clf.pkl", "embed_model": GENERIC_EMBED_MODEL},
}


def load_dataset(gold_path=None) -> list[dict]:
    """Join gold labels with the cached turn text; add previous-turn context.
    Only calls present in the gold set are used, so mixing ABCL + JD caches is safe.

    Some calls were cached twice under different filenames (e.g. a full-uuid
    "...-transcript.json" and a short-hash "<hex8>.json" from separate extraction
    runs) with identical content — `seen_call_ids` keeps the first and skips the
    duplicate so those calls aren't double-counted in the eval/training set."""
    gold = load_gold(gold_path)
    samples = []
    seen_call_ids: set = set()
    for f in sorted(config.CACHE_DIR.glob("*.json")):
        c = json.loads(f.read_text())
        if c["call_id"] in seen_call_ids:
            continue
        seen_call_ids.add(c["call_id"])
        turns = c["turns"]
        n = len(turns)
        for i, t in enumerate(turns):
            key = (c["call_id"], t["index"])
            if key not in gold:
                continue
            samples.append({
                "call_id": c["call_id"], "index": t["index"],
                "speaker": t["speaker"], "text": t["text"],
                "prev_text": turns[i - 1]["text"] if i > 0 else "",
                "pos": t["index"] / max(n - 1, 1),
                "label": gold[key]["base_intent"],
            })
    return samples


def _embed(texts, model, prefix=""):
    if prefix:
        texts = [prefix + t for t in texts]
    return model.encode(texts, normalize_embeddings=True, batch_size=64,
                        show_progress_bar=False)


def featurize(samples, model, prefix=""):
    cur = _embed([s["text"] for s in samples], model, prefix)
    prev = _embed([s["prev_text"] or "" for s in samples], model, prefix)
    spk = np.array([[1.0 if s["speaker"] == "agent" else 0.0] for s in samples])
    pos = np.array([[s["pos"]] for s in samples])
    X = np.hstack([cur, prev, spk, pos])
    y = np.array([s["label"] for s in samples])
    groups = np.array([s["call_id"] for s in samples])
    return X, y, groups


def _make_clf():
    from sklearn.linear_model import LogisticRegression
    return LogisticRegression(max_iter=2000, C=10.0, class_weight="balanced")


# ---------- sequence smoothing (Viterbi over learned intent transitions) ----------
def learn_transitions(label_seqs, classes, smooth=0.5):
    """Log transition matrix + log initial distribution from gold label sequences."""
    idx = {c: i for i, c in enumerate(classes)}
    S = len(classes)
    A = np.full((S, S), smooth)
    pi = np.full(S, smooth)
    for seq in label_seqs:
        seq = [s for s in seq if s in idx]
        if not seq:
            continue
        pi[idx[seq[0]]] += 1
        for a, b in zip(seq, seq[1:]):
            A[idx[a], idx[b]] += 1
    A = A / A.sum(axis=1, keepdims=True)
    pi = pi / pi.sum()
    return np.log(A), np.log(pi)


def viterbi(emis_log, logA, logpi):
    """Best state path given log emission (T,S), log transitions (S,S), log init (S,)."""
    T, S = emis_log.shape
    dp = np.full((T, S), -np.inf)
    bp = np.zeros((T, S), dtype=int)
    dp[0] = logpi + emis_log[0]
    for t in range(1, T):
        scores = dp[t - 1][:, None] + logA
        bp[t] = np.argmax(scores, axis=0)
        dp[t] = scores[bp[t], np.arange(S)] + emis_log[t]
    path = np.zeros(T, dtype=int)
    path[-1] = int(np.argmax(dp[-1]))
    for t in range(T - 2, -1, -1):
        path[t] = bp[t + 1, path[t + 1]]
    return path


def _emission_log(clf, X, alpha):
    """alpha scales the emission vs. transition strength (lower alpha = trust order more)."""
    proba = clf.predict_proba(X)
    return alpha * np.log(np.clip(proba, 1e-9, 1.0))


def _call_groups(samples, indices):
    """Group sample indices by call_id, preserving turn order."""
    from collections import defaultdict, OrderedDict
    g = OrderedDict()
    for i in indices:
        g.setdefault(samples[i]["call_id"], []).append(i)
    return g


def cv_eval(gold_path=None, embed_model=None):
    from sklearn.model_selection import GroupKFold
    from sentence_transformers import SentenceTransformer
    embed_model = embed_model or EMBED_MODEL
    prefix = embed_prefix_for(embed_model)
    print(f"loading embedding model ({embed_model}) + dataset ...")
    model = SentenceTransformer(embed_model)
    samples = load_dataset(gold_path)
    X, y, groups = featurize(samples, model, prefix)
    print(f"{len(samples)} samples, {X.shape[1]} features, {len(set(y))} classes")

    alphas = [0.3, 0.5, 0.8, 1.0]
    gkf = GroupKFold(n_splits=5)
    oof_raw = {}
    oof_sm = {a: {} for a in alphas}
    for fold, (tr, te) in enumerate(gkf.split(X, y, groups)):
        clf = _make_clf()
        clf.fit(X[tr], y[tr])
        classes = list(clf.classes_)
        # raw per-turn predictions
        for idx, p in zip(te, clf.predict(X[te])):
            s = samples[idx]
            oof_raw[(s["call_id"], s["index"])] = {"base_intent": p, "keywords": []}
        # smoothed: learn transitions on TRAIN, Viterbi-decode each TEST call
        train_seqs = [[samples[i]["label"] for i in idxs]
                      for idxs in _call_groups(samples, tr).values()]
        logA, logpi = learn_transitions(train_seqs, classes)
        for a in alphas:
            for cid, idxs in _call_groups(samples, te).items():
                Xc = X[idxs]
                path = viterbi(_emission_log(clf, Xc, a), logA, logpi)
                for i, st in zip(idxs, path):
                    s = samples[i]
                    oof_sm[a][(s["call_id"], s["index"])] = {
                        "base_intent": classes[st], "keywords": []}
        print(f"  fold {fold}: train={len(tr)} test={len(te)}")

    gold = load_gold(gold_path)
    raw = score_intents(gold, oof_raw)
    print(f"\n===== 5-fold grouped CV vs Claude gold =====")
    print(f"RAW (per-turn)      accuracy={raw['accuracy']:.3f}  macro-F1={raw['macro_f1']:.3f}")
    best_a, best = None, raw
    for a in alphas:
        s = score_intents(gold, oof_sm[a])
        mark = ""
        if s["accuracy"] > best["accuracy"]:
            best, best_a = s, a
        print(f"SMOOTHED (alpha={a})  accuracy={s['accuracy']:.3f}  macro-F1={s['macro_f1']:.3f}")
    print(f"\nBEST: {'smoothed alpha='+str(best_a) if best_a else 'raw'}  "
          f"accuracy={best['accuracy']:.3f}  macro-F1={best['macro_f1']:.3f}")
    print("\nstill-worst intents (F1, n>=10):")
    worst = sorted([(lab, *v) for lab, v in best["per_class"].items() if v[3] >= 10],
                   key=lambda x: x[3])
    for lab, prec, rec, f1, nn in worst[:10]:
        print(f"  {f1:.2f} F1  (p={prec:.2f} r={rec:.2f}, n={nn:>4})  {lab}")
    return best_a


def train_final(gold_path=None, model_path=None, embed_model=None):
    from sentence_transformers import SentenceTransformer
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    embed_model = embed_model or EMBED_MODEL
    prefix = embed_prefix_for(embed_model)
    model = SentenceTransformer(embed_model)
    samples = load_dataset(gold_path)
    X, y, _ = featurize(samples, model, prefix)
    clf = _make_clf()
    clf.fit(X, y)
    out = model_path or MODEL_PATH
    with open(out, "wb") as fh:
        pickle.dump({"clf": clf, "embed_model": embed_model, "embed_prefix": prefix}, fh)
    print(f"trained on {len(samples)} samples (embed_model={embed_model}) -> saved {out}")


# ---------- inference (used by extract.py as the classification backend) ----------
_PRED: dict = {}   # keyed by model path -> {clf, model}


def load_predictor(model_path=None):
    """Load (and cache) a distilled model. Defaults to the ABCL model; pass a path
    (e.g. the JustDial or generic model) to use a different one. Embedder is shared
    across models trained on the SAME embed_model id. embed_prefix (e.g. e5's
    "query: ") is read back from the pickle so inference matches training exactly —
    defaults to "" for older pickles saved before this field existed."""
    from sentence_transformers import SentenceTransformer
    path = model_path or MODEL_PATH
    key = str(path)
    if key not in _PRED:
        with open(path, "rb") as fh:
            d = pickle.load(fh)
        # reuse an already-loaded embedder if the model id matches
        emb = next((p["model"] for p in _PRED.values()
                    if p.get("embed_id") == d["embed_model"]), None)
        emb = emb or SentenceTransformer(d["embed_model"])
        _PRED[key] = {"clf": d["clf"], "model": emb, "embed_id": d["embed_model"],
                      "embed_prefix": d.get("embed_prefix", "")}
    return _PRED[key]


def predict_bases(turns: list[dict], model_path=None) -> list[str]:
    """turns: ordered list of {speaker, text}. Returns base_intent per turn, using
    the SAME features as training (current+prev embedding, speaker, position)."""
    if not turns:
        return []
    p = load_predictor(model_path)
    model, clf, prefix = p["model"], p["clf"], p.get("embed_prefix", "")
    n = len(turns)
    cur = _embed([t["text"] for t in turns], model, prefix)
    prev = _embed([turns[i - 1]["text"] if i > 0 else "" for i in range(n)], model, prefix)
    spk = np.array([[1.0 if t["speaker"] == "agent" else 0.0] for t in turns])
    pos = np.array([[i / max(n - 1, 1)] for i in range(n)])
    X = np.hstack([cur, prev, spk, pos])
    return [str(x) for x in clf.predict(X)]


if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "eval"
    dom = sys.argv[2] if len(sys.argv) > 2 else "abcl"
    d = DOMAINS[dom]
    print(f"[domain: {dom}]  gold={d['gold'].name}  model={d['model'].name}  "
          f"embed_model={d['embed_model']}")
    if cmd == "eval":
        cv_eval(d["gold"], d["embed_model"])
    elif cmd == "train":
        train_final(d["gold"], d["model"], d["embed_model"])
