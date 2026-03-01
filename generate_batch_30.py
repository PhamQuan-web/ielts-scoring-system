import json
from generate_batch_02 import make_samples, samples
samples.clear()

# Batch 30: V8/G9(10) V9/G8(10) V5/G6(10) V6/G5(10) V7/G6(10)
make_samples(1451, 8, 9, 10)
make_samples(1461, 9, 8, 10)
make_samples(1471, 5, 6, 10)
make_samples(1481, 6, 5, 10)
make_samples(1491, 7, 6, 10)

with open("ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_30.jsonl", 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
