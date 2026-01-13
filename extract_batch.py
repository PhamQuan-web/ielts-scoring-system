import json

try:
    with open('training_samples_normalized.json', 'r') as f:
        data = json.load(f)

    samples_list = data.get('samples', [])

    start_idx = 260
    end_idx = 280 # Exclusive, 260-279

    batch = samples_list[start_idx:end_idx]

    print(f"Total samples available: {len(samples_list)}")
    print(f"Extracting batch: {start_idx} to {end_idx-1}")

    print(json.dumps(batch, indent=2))

except Exception as e:
    print(f"Error: {e}")
