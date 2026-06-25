# ABCL Overlapping Context Graphs (POC)

Turns call-center **voice-call transcripts** into **overlapping context graphs**: each
transcript becomes a small graph of intents/entities/flow, and all of them are merged
into one **weighted master graph** that shows the common conversation paths, branch
points, and drop-offs.

## How it's split (important mental model)
- **The LLM (Claude)** does the *understanding*: it reads each messy transcript and emits
  structured JSON (turns -> intents -> entities -> outcome).
- **Deterministic Python** does the *assembly*: it merges all the per-call JSON into one
  weighted graph, exactly and reproducibly (counting, aligning, drawing).

## Pipeline (stages)
0. **Data prep**        — drop transcripts in `data/transcripts/`
1. **Taxonomy**         — `src/taxonomy.py`  discover the intent set (LLM)
2. **Extract**          — `src/extract.py`   per-call JSON via Claude (schema-enforced)
3. **Canonicalize**     — `src/canonicalize.py`  fold synonymous intents into one node
4. **Merge**            — `src/merge.py`     build the weighted master DiGraph
5. **Analyze**          — `src/analyze.py`   variants / happy path / drop-offs
6. **Visualize**        — `src/visualize.py` Graphviz / text summary
7. **Output**           — `data/output/`     master_graph.json + image

## Standard adopted
Labeled Property Graph (LPG), held in NetworkX for the POC, serialized as JSON node-link.
Conversation/intent graph modeled as a process-mining "directly-follows graph".
Designed to graduate to Neo4j / Graphiti for production with no remodeling.

## Setup
```bash
cd abcl-context-graph
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt        # for the mock run you only need networkx
```

## Run the mock demo (works today, no API key, no transcripts)
```bash
python run.py --mock
```
This builds the overlapping graph from fake calls in `tests/mock_data.py` and writes
`data/output/master_graph.json` (+ an image if Graphviz is installed).

## Next steps
- Wire `src/extract.py` to Claude (see the `claude-api` reference) + add a real transcript.
- Then run the full pipeline on real ABCL transcripts.
