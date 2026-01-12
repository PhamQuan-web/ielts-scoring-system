import json
import re

INPUT_FILE = "output/samples_verified.json"
OUTPUT_FILE = "output/samples_verified.json" # Overwrite

# Additional strong patterns to scrub from end of Valid samples
# These are specific leftovers found during inspection
TRAILING_SCRUB_PATTERNS = [
    r"Okay, I am going to stop you there.*$",
    r"I am going to stop you there.*$",
    r"Thank you very very much.*$",
    r"So, we have been talking there about.*$",
    r"All right\.$", # Catch isolated "All right."
    r"Great\.$",
    r"Thank you\.$"
]

def scrub_trailing_examiner(text):
    cleaned = text
    # Apply regex scrubs for specific known leaks
    for pattern in TRAILING_SCRUB_PATTERNS:
        # Check if pattern exists at the end of text
        # Using re.search with $ anchor inside the pattern
        match = re.search(pattern, cleaned, re.IGNORECASE | re.DOTALL)
        if match:
            # Cut text at the start of the match
            cleaned = cleaned[:match.start()].strip()

    return cleaned

def main():
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    samples = data["samples"]
    count = 0

    for sample in samples:
        original_clean = sample["transcript_cleaned"]
        new_clean = scrub_trailing_examiner(original_clean)

        if new_clean != original_clean:
            sample["transcript_cleaned"] = new_clean
            count += 1

    # Save back
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Post-scrubbed {count} samples.")

if __name__ == "__main__":
    main()
