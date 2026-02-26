import json
import collections

FILEPATH = "ielts-data/phase3/v76_review_output/jules3/agent_3_samples.jsonl"

def audit():
    try:
        with open(FILEPATH, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {FILEPATH}")
        return

    total_samples = len(lines)
    print(f"Total samples: {total_samples}")
    if total_samples != 372:
        print("FAIL: Total samples must be 372.")

    vocab_dist = collections.defaultdict(int)
    grammar_dist = collections.defaultdict(int)
    questions = set()
    short_transcripts = 0
    word_counts = []

    for line in lines:
        try:
            data = json.loads(line)
            v = data.get('vocabulary')
            g = data.get('grammar')
            q = data.get('question')
            t = data.get('transcript_cleaned', "")
            wc = len(t.split())

            vocab_dist[v] += 1
            grammar_dist[g] += 1
            questions.add(q)
            word_counts.append(wc)

            if wc < 120 or wc > 200:
                short_transcripts += 1

        except json.JSONDecodeError:
            print("FAIL: Invalid JSON line.")
            return

    print("\nVocabulary Distribution (Target: V4=20, V5=60, V6=70, V7=80, V8=80, V9=62):")
    for v, count in sorted(vocab_dist.items()):
        print(f"  V{v}: {count}")

    print("\nGrammar Distribution (Target: G5=90, G6=90, G7=67, G8=62, G9=63):")
    for g, count in sorted(grammar_dist.items()):
        print(f"  G{g}: {count}")

    print(f"\nUnique Questions: {len(questions)} / {total_samples}")
    if len(questions) != total_samples:
        print("FAIL: Questions are not unique.")

    print(f"\nTranscripts < 120 or > 200 words: {short_transcripts}")
    if short_transcripts > 0:
        print("FAIL: Some transcripts are out of length range (120-200).")

    avg_wc = sum(word_counts) / len(word_counts) if word_counts else 0
    print(f"Average Word Count: {avg_wc:.1f}")

if __name__ == "__main__":
    audit()
