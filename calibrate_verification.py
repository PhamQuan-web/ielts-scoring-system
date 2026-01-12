import json
import re
import spacy
from pathlib import Path

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

INPUT_FILE = "training_samples_normalized.json"
OUTPUT_FILE = "output/calibration_results.json"

# --- CONFIGURATION ---

# 1. Start Clean Patterns
START_CLEAN_REGEX = re.compile(
    r"^(?:Um|Uh|Ah|Er|So|Well|Okay|Alright|Yeah)\b[,\.]?\s*",
    re.IGNORECASE
)

# 2. End Clean Patterns
# Note: Added \W* to handle potential punctuation like "Okay." or "Right?"
END_CLEAN_REGEX = re.compile(
    r"\s*[,\.]?\b(?:Okay|Alright|All right|Yeah|Right|Yep|Thank you|Good|Great|Mm-hmm|Hmm|That's it)[.!?]?\W*$",
    re.IGNORECASE
)

# 3. Examiner Speech Detection (for Trailing Strip & Invalid Classification)
EXAMINER_PHRASES = [
    "let's move on", "move to part", "next question", "another question",
    "thank you very much", "concludes part", "end of part",
    "can i see your", "your identification", "your full name",
    "minute to prepare", "paper and pencil", "topic card",
    "start now", "stop now", "time is up",
    "i gave you", "band score", "for your grammar", "fluency",
    "good job", "well done", "nice answer",
    # ADDED
    "move on", "stop you there", "ask some questions", "related to that",
    "talking about", "ask you about", "part two", "part one", "part three",
    "going to give you", "talk about the topic", "take some paper"
]

EXAMINER_STARTERS = ["okay", "alright", "right", "so", "thank you", "good", "great", "now"]

# Invalid Classification Keywords
INVALID_KEYWORDS = {
    "examiner_feedback": [
        r"\bscore\b", r"\bband\b", r"\bgrammar\b", r"\bvocabulary\b",
        r"\bfluency\b", r"\bpronunciation\b", r"\bgive you a (nine|eight|seven|six|five)\b",
        r"\bdid a (good|great) job\b"
    ],
    "instructions": [
        r"\bpart (one|two|three|1|2|3)\b", r"\bminute to prepare\b",
        r"\btake notes\b", r"\bpaper and (pen|pencil)\b", r"\btopic card\b",
        r"\bstart speaking\b", r"\btime is up\b"
    ],
    "greeting": [
        r"^(hello|hi|good morning|good afternoon|good evening)\b",
        r"\bhow are you\b"
    ],
    "meta_communication": [
        r"\bsee your (id|identification|passport)\b", r"\bfull name\b",
        r"\bwhat should i call you\b", r"\brecording\b", r"\bthis is the speaking test\b"
    ]
}


def clean_transcript(text):
    """
    Applies the cleaning rules:
    1. Strip Start Fillers (recursive)
    2. Strip End Fillers (recursive)
    3. Detect and Strip Trailing Examiner Speech
    """
    cleaned = text.strip()

    # 1. Strip Start Fillers (Iterative to catch "Um, so, well...")
    while True:
        match = START_CLEAN_REGEX.match(cleaned)
        if match:
            cleaned = cleaned[match.end():]
        else:
            break

    # 2. Strip End Fillers
    while True:
        match = END_CLEAN_REGEX.search(cleaned)
        if match:
            cleaned = cleaned[:match.start()]
        else:
            break

    # 3. Strip Trailing Examiner Speech
    # Use Spacy to split sentences
    doc = nlp(cleaned)
    sentences = list(doc.sents)

    if not sentences:
        return cleaned

    final_cutoff = len(sentences)

    # Iterate backwards to find the start of the "Examiner Block" at the end
    # We allow the block to grow backwards as long as sentences look like examiner speech
    for i in range(len(sentences) - 1, -1, -1):
        sent_text = sentences[i].text.strip().lower()
        is_examiner = False

        # Rule 1: Contains explicit examiner phrase
        if any(phrase in sent_text for phrase in EXAMINER_PHRASES):
            is_examiner = True

        # Rule 2: Short closing markers (Okay. Right. Thank you.)
        # Only if it's the very last sentence or follows another examiner sentence
        elif i == len(sentences) - 1 or i == final_cutoff - 1:
             if len(sent_text.split()) < 5: # Short sentence
                 if any(sent_text.startswith(s) for s in EXAMINER_STARTERS) or sent_text in ["okay.", "right.", "thank you.", "great."]:
                     is_examiner = True

        if is_examiner:
            final_cutoff = i
        else:
            # Found a clear candidate sentence (or at least not clearly examiner).
            # Stop stripping here.
            break

    # Reconstruct text
    valid_sentences = sentences[:final_cutoff]
    cleaned = "".join([s.text_with_ws for s in valid_sentences]).strip()

    # Post-clean: Strip end fillers again just in case the sentence split left some
    while True:
        match = END_CLEAN_REGEX.search(cleaned)
        if match:
            cleaned = cleaned[:match.start()]
        else:
            break

    return cleaned

def validate_sample(sample, cleaned_transcript):
    """
    Classifies sample as VALID or INVALID based on criteria.
    """
    question = sample.get("question", "").lower()
    transcript = cleaned_transcript.lower()

    # 1. Check Invalid Keywords in Transcript (Examiner Feedback mixed in)
    for category, patterns in INVALID_KEYWORDS.items():
        for pattern in patterns:
            if re.search(pattern, transcript):
                # Context check: ignore if "part one" is "part of one" (false positive check)
                return "INVALID", category, f"Match: {pattern}"

    # 2. Check Question validity
    for category, patterns in INVALID_KEYWORDS.items():
        for pattern in patterns:
            if re.search(pattern, question):
                return "INVALID", category, f"Question Match: {pattern}"

    # 3. Check for Empty/Too Short
    if len(cleaned_transcript.split()) < 3:
        return "INVALID", "incomplete", "Too short"

    return "VALID", None, None


def main():
    try:
        with open(INPUT_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")
        return

    samples = data.get("samples", [])
    results = []

    # Process first 50 samples
    for sample in samples[:50]:
        original = sample.get("transcript", "")
        cleaned = clean_transcript(original)
        status, reason, note = validate_sample(sample, cleaned)

        results.append({
            "sample_id": sample.get("sample_id"),
            "question": sample.get("question"),
            "original": original,
            "cleaned": cleaned,
            "status": status,
            "reason": reason,
            "note": note
        })

    # Save results
    Path("output").mkdir(exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Calibration complete. Processed {len(results)} samples.")

if __name__ == "__main__":
    main()
