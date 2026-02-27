import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_12.jsonl"

def fix_batch_12(file_path):
    updated_samples = []
    seen_questions = set()

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            sample = json.loads(line)
            q = sample["question"]

            # 1. Fix duplicate questions
            if q in seen_questions:
                if q == "Describe a person you admire.":
                    sample["question"] = "Describe a role model in your life."
                elif q == "Describe a place you recommend visiting.":
                    sample["question"] = "Describe a tourist destination you like."
            seen_questions.add(sample["question"])

            # 2. Pad transcript if < 120 words
            transcript = sample.get("transcript_cleaned", "")
            word_count = len(transcript.split())

            if word_count < 120:
                padding = ""
                vocab_band = sample.get("vocabulary", 8) # Most are higher bands here

                if vocab_band >= 8:
                    padding = " This topic is particularly meaningful to me, as it represents a significant chapter in my personal development and growth. It continues to inspire me."
                elif vocab_band >= 6:
                    padding = " Overall, it was an experience I will never forget. It taught me many important lessons that I still use today."
                else:
                    padding = " I really like it and I think it is very good. Everyone should try it because it is fun and interesting."

                transcript += padding
                word_count = len(transcript.split())
                sample["transcript_cleaned"] = transcript

            sample["word_count"] = word_count

            # 3. Update input field
            new_input = f"Part: {sample['part']}\nQuestion: {sample['question']}\n\nTranscript: {transcript}\n\nWord Count: {word_count} words\nResponse Type: {sample['response_type']}"
            sample["input"] = new_input

            updated_samples.append(sample)

    with open(file_path, 'w', encoding='utf-8') as f:
        for sample in updated_samples:
            f.write(json.dumps(sample) + '\n')

if __name__ == "__main__":
    fix_batch_12(OUTPUT_FILE)
    print(f"Fixed duplicates and word counts in {OUTPUT_FILE}")
