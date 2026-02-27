import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_07.jsonl"

def update_word_counts(file_path):
    updated_samples = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            sample = json.loads(line)
            transcript = sample.get("transcript_cleaned", "")
            word_count = len(transcript.split())
            sample["word_count"] = word_count

            # Update input field to match new word count
            input_text = sample.get("input", "")
            if "Word Count:" in input_text:
                import re
                input_text = re.sub(r"Word Count: \d+ words", f"Word Count: {word_count} words", input_text)
                sample["input"] = input_text

            updated_samples.append(sample)

    with open(file_path, 'w', encoding='utf-8') as f:
        for sample in updated_samples:
            f.write(json.dumps(sample) + '\n')

if __name__ == "__main__":
    update_word_counts(OUTPUT_FILE)
    print(f"Updated word counts in {OUTPUT_FILE}")
