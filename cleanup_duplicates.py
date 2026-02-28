import os
import json

def cleanup_duplicates(directories):
    for directory in directories:
        if not os.path.exists(directory):
            continue

        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                filepath = os.path.join(directory, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    if "words" in data:
                        unique_words = []
                        seen_words = set()
                        for word_obj in data["words"]:
                            word_str = word_obj.get("word", "").lower()
                            if word_str not in seen_words:
                                seen_words.add(word_str)
                                unique_words.append(word_obj)

                        if len(unique_words) != len(data["words"]):
                            data["words"] = unique_words
                            data["wordCount"] = len(unique_words)

                            with open(filepath, 'w', encoding='utf-8') as f:
                                json.dump(data, f, indent=4, ensure_ascii=False)
                            print(f"Cleaned up {filepath}. New count: {data['wordCount']}")

                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    directories_to_process = [
        "output/cambridge_10",
        "output/cambridge_11",
        "output/cambridge_12",
        "output/cambridge_13",
        "output/cambridge_14",
        "output/cambridge_15"
    ]
    cleanup_duplicates(directories_to_process)
