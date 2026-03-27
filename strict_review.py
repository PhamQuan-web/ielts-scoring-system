import json, sys
from collections import Counter
import re

def review_file(filepath):
    print(f"--- Strict Review: {filepath} ---")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    transcripts = []
    endings = []

    for i, line in enumerate(lines, 1):
        if not line.strip(): continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            print(f"Line {i}: Invalid JSON")
            return False

        t = data.get("transcript_cleaned", "")
        transcripts.append(t)

        # Check for banned programmatic references
        if re.search(r'\(Ref \d+\)', t):
            print(f"FAIL L{i}: Found programmatic reference tag '(Ref X)'")
            return False

        if "I really like it very much" in t or "This is just my perspective." in t:
             print(f"FAIL L{i}: Found banned generic padding.")
             return False

        # Check endings (last 30 chars or last sentence)
        sentences = re.split(r'[.!?]\s+', t)
        if len(sentences) > 1:
             endings.append(sentences[-2] if not sentences[-1] else sentences[-1]) # rudimentary check

    # Ensure 100% transcript uniqueness
    if len(set(transcripts)) != len(transcripts):
        print("FAIL: Duplicate transcripts found in batch!")
        return False

    print("PASS: No generic padding or programmatic artifacts detected. Transcripts are unique.")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        success = review_file(sys.argv[1])
        sys.exit(0 if success else 1)
