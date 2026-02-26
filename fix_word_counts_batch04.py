import json

FILEPATH = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch04.jsonl'

def fix_word_counts():
    updated_lines = []
    with open(FILEPATH, 'r') as f:
        for line in f:
            try:
                sample = json.loads(line)
                transcript = sample.get('transcript_cleaned', '')
                actual_wc = len(transcript.split())

                if sample['word_count'] != actual_wc:
                    print(f"Updating {sample['sample_id']}: {sample['word_count']} -> {actual_wc}")
                    sample['word_count'] = actual_wc

                    if 'input' in sample:
                        import re
                        sample['input'] = re.sub(r'Word Count: \d+ words', f'Word Count: {actual_wc} words', sample['input'])

                updated_lines.append(json.dumps(sample))
            except json.JSONDecodeError:
                print("Skipping invalid JSON line")
                continue

    with open(FILEPATH, 'w') as f:
        for line in updated_lines:
            f.write(line + '\n')

    print("Word counts updated.")

if __name__ == "__main__":
    fix_word_counts()
