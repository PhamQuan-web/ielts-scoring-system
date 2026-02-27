import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_14.jsonl"

def fix_batch_14_v2(file_path):
    updated_samples = []
    seen_questions = set()

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            sample = json.loads(line)
            q = sample["question"]

            # Fix duplicate question
            if q == "Describe an antique in your possession.":
                if q in seen_questions:
                    sample["question"] = "Describe a vintage item you keep."

            seen_questions.add(sample["question"])

            # Recalculate input field just in case
            transcript = sample.get("transcript_cleaned", "")
            word_count = sample.get("word_count", 0)
            new_input = f"Part: {sample['part']}\nQuestion: {sample['question']}\n\nTranscript: {transcript}\n\nWord Count: {word_count} words\nResponse Type: {sample['response_type']}"
            sample["input"] = new_input

            updated_samples.append(sample)

    with open(file_path, 'w', encoding='utf-8') as f:
        for sample in updated_samples:
            f.write(json.dumps(sample) + '\n')

if __name__ == "__main__":
    fix_batch_14_v2(OUTPUT_FILE)
    print(f"Fixed duplicates again in {OUTPUT_FILE}")
