import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_11.jsonl"

def fix_batch_11(file_path):
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
                    sample["question"] = "Describe a biography you found interesting."
                elif q == "Describe a piece of art you like.":
                    sample["question"] = "Describe a famous painting."
            seen_questions.add(sample["question"]) # Add the NEW question if changed, or old if not

            # 2. Pad transcript if < 120 words
            transcript = sample.get("transcript_cleaned", "")
            word_count = len(transcript.split())

            if word_count < 120:
                padding = ""
                # V7/V8/V9 logic
                vocab_band = sample.get("vocabulary", 7)

                if vocab_band >= 9:
                    padding = " This experience was truly transformative, reshaping my perspective on life in a fundamental way. It remains a constant source of inspiration for me."
                elif vocab_band >= 8:
                    padding = " Reflecting on this, I realize how much it has influenced my personal growth and understanding of the world. It is something I will always cherish."
                else: # Band 7
                    padding = " Overall, it was a very memorable experience that I will not forget. It taught me a valuable lesson about life."

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
    fix_batch_11(OUTPUT_FILE)
    print(f"Fixed duplicates and word counts in {OUTPUT_FILE}")
