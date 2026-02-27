import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_12.jsonl"

def fix_duplicates_again(file_path):
    updated_samples = []
    seen_questions = set()

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            sample = json.loads(line)
            q = sample["question"]

            if q in seen_questions:
                if q == "Describe a festival you want to attend.":
                    sample["question"] = "Describe a cultural event you are interested in."
                elif q == "Describe a natural place you want to visit.":
                    sample["question"] = "Describe a scenic spot you wish to see."

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
    fix_duplicates_again(OUTPUT_FILE)
    print(f"Fixed duplicates again in {OUTPUT_FILE}")
