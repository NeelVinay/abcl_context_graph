"""Hindi + Hinglish + English stopwords for DATA-DRIVEN keyword extraction.

Used only to filter the auto-derived keyword vocabulary (function words, pronouns,
postpositions, and the common conjugations of होना/करना/जाना/देना/लेना/रहना that carry
no topical signal). Curated intent keywords are matched separately and are NOT affected
by this list — so a word like "कैसे" can be a stopword here yet still match the
ask_question intent.
"""

# Devanagari function words + very common verb conjugations
_HINDI = {
    # pronouns / determiners
    "मैं", "मैने", "मैंने", "तुम", "तू", "आप", "वह", "यह", "हम", "ये", "वो", "उस", "इस",
    "उन", "इन", "उन्हें", "इन्हें", "उसे", "इसे", "मुझे", "मुझको", "हमें", "तुम्हें",
    "मेरा", "मेरी", "मेरे", "तेरा", "तेरी", "आपका", "आपकी", "आपके", "आपको", "आपने",
    "हमारा", "हमारी", "हमारे", "उनका", "उनकी", "उनके", "इनका", "इसका", "इसकी", "इसके",
    "उसका", "उसकी", "उसके", "किसी", "किसे", "कोई", "कुछ", "सब", "सभी", "सारे", "सारा",
    "सारी", "खुद", "अपना", "अपनी", "अपने", "जिस", "जिसे", "जिन", "वही", "यही",
    # postpositions / particles / conjunctions
    "का", "की", "के", "को", "में", "से", "पर", "तक", "ने", "और", "या", "भी", "ही",
    "तो", "न", "ना", "नहीं", "नही", "मत", "कि", "जो", "जब", "तब", "अब", "अगर", "तभी",
    "लेकिन", "मगर", "पर", "फिर", "इसलिए", "क्योंकि", "वरना", "बल्कि", "जैसे", "वैसे",
    # adverbs / fillers
    "अभी", "यहाँ", "यहां", "वहाँ", "वहां", "जहाँ", "कहाँ", "कहां", "क्यों", "कैसे",
    "कब", "क्या", "कौन", "बहुत", "थोड़ा", "थोड़ी", "ज़्यादा", "ज्यादा", "सिर्फ", "बस",
    "ओके", "अच्छा", "अच्छे", "हाँ", "हां", "जी", "मतलब", "वाला", "वाली", "वाले",
    "साथ", "बार", "दिन", "चीज़", "चीज", "तरह", "बात", "लोग", "नाम",
    # होना
    "है", "हैं", "था", "थी", "थे", "हूँ", "हूं", "हो", "होता", "होती", "होते", "होना",
    "होने", "होगा", "होगी", "होंगे", "हुआ", "हुई", "हुए", "है।", "हैं।",
    # रहना
    "रहा", "रही", "रहे", "रहता", "रहती", "रहते", "रहना", "रहने", "रहेगा", "रहेंगे",
    # करना
    "कर", "करता", "करती", "करते", "करना", "करने", "करूं", "करूँ", "किया", "करो",
    "करें", "करेगा", "करेगी", "करेंगे", "करके",
    # जाना
    "जा", "जाता", "जाती", "जाते", "जाना", "जाने", "गया", "गई", "गए", "जाएगा", "जाएगी",
    "जाएंगे", "जाऊं",
    # आना
    "आ", "आता", "आती", "आते", "आना", "आने", "आया", "आई", "आए", "आएगा", "आएगी", "आएंगे",
    # बताना / कहना
    "बता", "बताता", "बताती", "बताते", "बताना", "बताओ", "बताइए", "बताया", "कह", "कहा",
    "कहता", "कहती", "कहना", "बारे", "कभी", "वगैरा", "रेज",
    # देना / लेना
    "दे", "दिया", "देना", "देता", "देती", "देंगे", "दीजिए", "ले", "लिया", "लेना",
    "लेता", "लेती", "लीजिए",
    # modals / misc
    "चाहिए", "चाहूं", "चाहूँ", "सकता", "सकती", "सकते", "पड़ा", "पड़ता", "वगैरह",
    "एक", "दो", "तीन", "लिए", "हमने", "इससे", "इसमें", "इसपर", "पहले", "बाद", "पास",
}

_ENGLISH = {
    "the", "a", "an", "this", "that", "these", "those", "you", "your", "yours", "i",
    "me", "my", "we", "our", "he", "she", "it", "they", "them", "his", "her", "is",
    "am", "are", "was", "were", "be", "been", "being", "do", "does", "did", "have",
    "has", "had", "will", "would", "can", "could", "should", "may", "might", "must",
    "to", "of", "in", "on", "for", "with", "at", "by", "from", "up", "and", "or",
    "but", "so", "if", "then", "than", "as", "not", "no", "yes", "ok", "okay", "yeah",
    "hi", "hello", "ya", "na", "ji", "haan", "hmm", "uh", "um",
}

# Hinglish (Latin-spelled Hindi) function words
_HINGLISH = {
    "hai", "hain", "tha", "thi", "the", "hoon", "hun", "ho", "hota", "hoti", "hote",
    "kar", "karta", "karti", "karte", "karna", "kiya", "karo", "karenge", "raha",
    "rahi", "rahe", "gaya", "gayi", "jana", "jata", "diya", "lena", "liya", "main",
    "mein", "aap", "apko", "aapko", "hum", "ye", "wo", "yeh", "woh", "ka", "ki", "ke",
    "ko", "se", "par", "aur", "ya", "bhi", "hi", "to", "nahi", "nahin", "kya", "kyun",
    "kaise", "kab", "kahan", "matlab", "bahut", "thoda", "sab", "kuch", "koi", "acha",
    "accha", "sir", "madam", "maam",
}

# Common Indian first names — agents recur across many calls, so their names would
# survive the >=2-call PII guard and leak as "keywords". This blocks the frequent ones.
# (Customer names are call-specific and already filtered by the >=2-call rule.)
_NAMES = {
    # Latin
    "priya", "pooja", "puja", "neha", "anjali", "kavita", "sunita", "rekha", "deepa",
    "ritu", "swati", "shreya", "sneha", "divya", "preeti", "preeti", "komal", "nisha",
    "aarti", "arti", "manisha", "seema", "geeta", "meena", "radha", "sapna", "payal",
    "amit", "rahul", "raj", "ravi", "vijay", "vikas", "vikram", "rohit", "rohan",
    "sandeep", "sanjay", "suresh", "ramesh", "rajesh", "mahesh", "dinesh", "naresh",
    "ankit", "ashish", "abhishek", "deepak", "manoj", "anil", "sunil", "arun", "varun",
    "gaurav", "saurabh", "nitin", "pankaj", "prakash", "mohit", "karan", "aakash",
    "akash", "salman", "imran", "faisal", "arjun", "aman", "kunal", "yash", "harsh",
    "shivam", "shubham", "siddharth", "kartik", "nandu", "anaya", "ananya",
    # Devanagari
    "प्रिया", "पूजा", "नेहा", "अंजली", "कविता", "सुनीता", "रेखा", "दीपा", "रितु",
    "अमित", "राहुल", "राज", "रवि", "विजय", "विकास", "विक्रम", "रोहित", "रोहन",
    "संदीप", "संजय", "सुरेश", "रमेश", "राजेश", "महेश", "दिनेश", "अंकित", "आशीष",
    "दीपक", "मनोज", "अनिल", "सुनील", "अरुण", "वरुण", "गौरव", "सौरभ", "नितिन",
    "प्रकाश", "मोहित", "करण", "आकाश", "अर्जुन", "अमन", "कुनाल", "नंदू",
    # common Indian surnames (recur across calls as agent/customer names -> leak as keywords)
    "yadav", "kumar", "sharma", "singh", "verma", "gupta", "patel", "devi", "khan",
    "reddy", "rao", "das", "shah", "jain", "mishra", "pandey", "chauhan", "tiwari",
    "यादव", "कुमार", "शर्मा", "सिंह", "वर्मा", "गुप्ता", "पटेल", "देवी", "खान",
    "रेड्डी", "राव", "दास", "शाह", "जैन", "मिश्रा", "पांडे", "चौहान", "तिवारी",
}

# system / DSL markers that leak from the agent transcripts (e.g. <chd>, <EOC/>)
_SYSTEM = {"chd", "eoc", "eoc/", "chd/"}

STOPWORDS = _HINDI | _ENGLISH | _HINGLISH | _NAMES | _SYSTEM
