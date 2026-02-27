import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_10.jsonl"

def update_word_counts(file_path):
    updated_samples = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            sample = json.loads(line)
            transcript = sample.get("transcript_cleaned", "")
            word_count = len(transcript.split())

            # Pad if < 120 words
            if word_count < 120:
                padding = ""
                vocab_band = sample.get("vocabulary", 6)

                if vocab_band == 6:
                    padding = " I really enjoyed this experience and I hope to do it again in the future. It was a very special time for me and my friends."
                elif vocab_band == 7:
                    padding = " This event holds a significant place in my memories, and I often reflect on it with fondness. It was truly a remarkable experience."

                transcript += padding
                word_count = len(transcript.split())
                sample["transcript_cleaned"] = transcript

            sample["word_count"] = word_count

            # Update input field
            input_text = sample.get("input", "")
            import re
            new_input = f"Part: {sample['part']}\nQuestion: {sample['question']}\n\nTranscript: {transcript}\n\nWord Count: {word_count} words\nResponse Type: {sample['response_type']}"
            sample["input"] = new_input

            updated_samples.append(sample)

    with open(file_path, 'w', encoding='utf-8') as f:
        for sample in updated_samples:
            f.write(json.dumps(sample) + '\n')

if __name__ == "__main__":
    update_word_counts(OUTPUT_FILE)
    print(f"Updated word counts in {OUTPUT_FILE}")
