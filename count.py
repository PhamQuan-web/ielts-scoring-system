import json
import glob
import os

files = glob.glob('output/*.json')
print(f"Total files: {len(files)}")

# Run validation manually via python without printing all to avoid bash huge diff warning loop
failed = 0
for f in files:
    try:
        with open(f, 'r') as file:
            data = json.load(file)
            if not data.get('quiz'):
                failed += 1
    except Exception as e:
        failed += 1

print(f"Failed files: {failed}")
