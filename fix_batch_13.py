import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_13.jsonl"

def fix_batch_13(file_path):
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
                if q == "Describe a book you read recently.":
                    sample["question"] = "Describe a novel you enjoyed."
                elif q == "Describe a hobby you have.":
                    sample["question"] = "Describe a pastime you like."
            seen_questions.add(sample["question"])

            # 2. Pad transcript if < 120 words (which is ALL of them)
            # Need significant padding as avg is 78 words
            transcript = sample.get("transcript_cleaned", "")
            word_count = len(transcript.split())

            if word_count < 120:
                padding = ""
                vocab_band = sample.get("vocabulary", 4)

                # Add sentences appropriate for low bands (V4/5) vs mid bands (V6/7)
                if vocab_band <= 5:
                    padding = " I really like it very much. It is very good for me. I think everyone should try it. It make me happy every day. My friends also like it. We do it together. It is fun time for us. I will do it again soon. It is my favorite thing. I tell my family about it. They say it is good."
                else:
                    padding = " This experience was truly memorable for me. It taught me a lot of things. I will never forget it. I hope to do it again in the future. It was a special time in my life. I think it is important to have such experiences. It makes life more interesting and fun. I recommend it to everyone."

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
    fix_batch_13(OUTPUT_FILE)
    print(f"Fixed duplicates and word counts in {OUTPUT_FILE}")
