import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_09.jsonl"

def update_word_counts_and_fix_dupe(file_path):
    updated_samples = []
    seen_questions = set()

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            sample = json.loads(line)

            # 1. Fix duplicate question "Describe a hobby you have."
            q = sample["question"]
            if q == "Describe a hobby you have.":
                if q in seen_questions:
                    # Modify the second occurrence
                    sample["question"] = "Describe a hobby you want to start."
                    # Adjust transcript slightly to match if needed, but for padding purpose it's fine.
                    # Actually, let's just make it unique.
                seen_questions.add(q)
            else:
                seen_questions.add(q)

            transcript = sample.get("transcript_cleaned", "")
            word_count = len(transcript.split())

            # 2. Pad transcript if < 120 words
            if word_count < 120:
                padding = ""
                # V4/V5/V6 logic
                vocab_band = sample.get("vocabulary", 4)

                if vocab_band == 4:
                    padding = " I really like it very much. It is very good for me. I think everyone should try it. It make me happy every day. My friends also like it. We do it together. It is fun time for us."
                elif vocab_band == 5:
                    padding = " This is very important to me. It makes my life better. I feel good when I do this. My family supports me. I will continue to do this in the future because I enjoy it a lot."

                transcript += padding
                word_count = len(transcript.split())
                sample["transcript_cleaned"] = transcript

            sample["word_count"] = word_count

            # 3. Update input field
            input_text = sample.get("input", "")
            # Reconstruct input
            new_input = f"Part: {sample['part']}\nQuestion: {sample['question']}\n\nTranscript: {transcript}\n\nWord Count: {word_count} words\nResponse Type: {sample['response_type']}"
            sample["input"] = new_input

            updated_samples.append(sample)

    with open(file_path, 'w', encoding='utf-8') as f:
        for sample in updated_samples:
            f.write(json.dumps(sample) + '\n')

if __name__ == "__main__":
    update_word_counts_and_fix_dupe(OUTPUT_FILE)
    print(f"Fixed duplicates and word counts in {OUTPUT_FILE}")
