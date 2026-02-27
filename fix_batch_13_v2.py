import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_13.jsonl"

def fix_batch_13_v2(file_path):
    updated_samples = []
    seen_questions = set()

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            sample = json.loads(line)
            q = sample["question"]

            if q in seen_questions:
                if q == "Describe a friend you like.":
                    sample["question"] = "Describe a close friend."
                elif q == "Describe a piece of technology you use.":
                    sample["question"] = "Describe a gadget you own."
            seen_questions.add(sample["question"])

            # Recalculate input (transcript and word count are fine from prev fix)
            transcript = sample.get("transcript_cleaned", "")
            word_count = sample.get("word_count", 0)
            new_input = f"Part: {sample['part']}\nQuestion: {sample['question']}\n\nTranscript: {transcript}\n\nWord Count: {word_count} words\nResponse Type: {sample['response_type']}"
            sample["input"] = new_input

            updated_samples.append(sample)

    with open(file_path, 'w', encoding='utf-8') as f:
        for sample in updated_samples:
            f.write(json.dumps(sample) + '\n')

if __name__ == "__main__":
    fix_batch_13_v2(OUTPUT_FILE)
    print(f"Fixed duplicates again in {OUTPUT_FILE}")
