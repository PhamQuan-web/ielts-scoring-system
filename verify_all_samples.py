import json
import re
import spacy
from pathlib import Path
import datetime

# Load Spacy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Spacy model not found. Installing...")
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

INPUT_FILE = "training_samples_normalized.json"
OUTPUT_VERIFIED = "output/samples_verified.json"
OUTPUT_INVALID = "output/samples_invalid.json"
OUTPUT_SUMMARY = "output/verification_summary.json"

# --- CONFIGURATION ---

# 1. Start Clean Patterns
START_CLEAN_REGEX = re.compile(
    r"^(?:Um|Uh|Ah|Er|So|Well|Okay|Alright|Yeah)\b[,\.]?\s*",
    re.IGNORECASE
)

# 2. End Clean Patterns
END_CLEAN_REGEX = re.compile(
    r"\s*[,\.]?\b(?:Okay|Alright|All right|Yeah|Right|Yep|Thank you|Good|Great|Mm-hmm|Hmm|That's it)[.!?]?\W*$",
    re.IGNORECASE
)

# 3. Examiner Speech Detection
EXAMINER_PHRASES = [
    "let's move on", "move to part", "next question", "another question",
    "thank you very much", "concludes part", "end of part",
    "can i see your", "your identification", "your full name",
    "minute to prepare", "paper and pencil", "topic card",
    "start now", "stop now", "time is up",
    "i gave you", "band score", "for your grammar", "fluency",
    "good job", "well done", "nice answer",
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
    4. Strip End Fillers AGAIN (Post-Strip)
    """
    cleaned = text.strip()

    # 1. Strip Start Fillers
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
    if not cleaned: return ""

    doc = nlp(cleaned)
    sentences = list(doc.sents)

    if not sentences:
        return cleaned

    final_cutoff = len(sentences)

    # Iterate backwards
    for i in range(len(sentences) - 1, -1, -1):
        sent_text = sentences[i].text.strip().lower()
        is_examiner = False

        # Rule 1: Contains explicit examiner phrase
        if any(phrase in sent_text for phrase in EXAMINER_PHRASES):
            is_examiner = True

        # Rule 2: Short closing markers (Okay. Right. Thank you.)
        # Check if it looks like examiner filler
        # "Okay." "Right." "Thank you."
        # Only if it's in the 'danger zone' (end of text or adjacent to other examiner text)
        elif i == len(sentences) - 1 or i == final_cutoff - 1:
             if len(sent_text.split()) < 6: # Short sentence
                 if any(sent_text.startswith(s) for s in EXAMINER_STARTERS) or sent_text.strip(".,!?") in ["okay", "right", "thank you", "great", "yes"]:
                     is_examiner = True

        if is_examiner:
            final_cutoff = i
        else:
            # Found a candidate sentence.
            break

    # Reconstruct text
    valid_sentences = sentences[:final_cutoff]
    cleaned = "".join([s.text_with_ws for s in valid_sentences]).strip()

    # 4. Strip End Fillers AGAIN (Post-Strip)
    # This catches "All right" that was revealed after cutting "Thank you very much"
    while True:
        match = END_CLEAN_REGEX.search(cleaned)
        if match:
            cleaned = cleaned[:match.start()]
        else:
            break

    return cleaned.strip()

def validate_sample(sample, cleaned_transcript):
    """
    Classifies sample as VALID or INVALID based on criteria.
    """
    question = sample.get("question", "").lower()
    transcript = cleaned_transcript.lower()

    # 1. Check Invalid Keywords in Transcript
    for category, patterns in INVALID_KEYWORDS.items():
        for pattern in patterns:
            if re.search(pattern, transcript):
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
    print("Starting full verification...")
    start_time = datetime.datetime.now()

    try:
        with open(INPUT_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")
        return

    samples = data.get("samples", [])
    total_processed = 0

    verified_samples = []
    invalid_samples = []

    invalid_counts = {k: 0 for k in INVALID_KEYWORDS.keys()}
    invalid_counts["incomplete"] = 0

    for sample in samples:
        original = sample.get("transcript", "")
        cleaned = clean_transcript(original)
        status, reason, note = validate_sample(sample, cleaned)

        sample_out = sample.copy()

        if status == "VALID":
            sample_out["transcript_cleaned"] = cleaned
            sample_out["verification_status"] = "VALID"
            sample_out["verification_note"] = "Verified by Jules (Hybrid NLP)"
            verified_samples.append(sample_out)
        else:
            sample_out["verification_status"] = "INVALID"
            sample_out["invalid_reason"] = reason
            sample_out["verification_note"] = note
            invalid_samples.append(sample_out)
            if reason in invalid_counts:
                invalid_counts[reason] += 1

        total_processed += 1
        if total_processed % 500 == 0:
            print(f"Processed {total_processed} samples...")

    # Save Output Files
    Path("output").mkdir(exist_ok=True)

    # Verified
    with open(OUTPUT_VERIFIED, "w") as f:
        json.dump({
            "total": len(verified_samples),
            "verified_at": datetime.datetime.now().isoformat(),
            "verified_by": "Jules AI Agent",
            "samples": verified_samples
        }, f, indent=2)

    # Invalid
    with open(OUTPUT_INVALID, "w") as f:
        json.dump({
            "total": len(invalid_samples),
            "verified_at": datetime.datetime.now().isoformat(),
            "verified_by": "Jules AI Agent",
            "samples": invalid_samples
        }, f, indent=2)

    # Summary
    end_time = datetime.datetime.now()
    summary = {
        "total_processed": total_processed,
        "total_valid": len(verified_samples),
        "total_invalid": len(invalid_samples),
        "invalid_breakdown": invalid_counts,
        "processing_time": str(end_time - start_time),
        "completed_at": end_time.isoformat()
    }

    with open(OUTPUT_SUMMARY, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nVerification Complete!")
    print(f"Total: {total_processed}")
    print(f"Valid: {len(verified_samples)}")
    print(f"Invalid: {len(invalid_samples)}")
    print(f"Summary saved to {OUTPUT_SUMMARY}")

if __name__ == "__main__":
    main()
