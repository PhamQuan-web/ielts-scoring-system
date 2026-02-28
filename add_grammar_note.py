import os
import json

def add_grammar_note_to_files(directories):
    for directory in directories:
        if not os.path.exists(directory):
            print(f"Directory not found: {directory}")
            continue

        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                filepath = os.path.join(directory, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    modified = False
                    if "words" in data:
                        for word in data["words"]:
                            if "grammar_note" not in word:
                                word["grammar_note"] = ""
                                modified = True

                    if modified:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            json.dump(data, f, indent=4, ensure_ascii=False)
                        print(f"Updated: {filepath}")
                    else:
                        print(f"No changes needed: {filepath}")

                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    directories_to_process = [
        "output/cambridge_13",
        "output/cambridge_14",
        "output/cambridge_15"
    ]
    add_grammar_note_to_files(directories_to_process)
