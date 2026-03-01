import json
from generate_batch_02 import make_samples, samples
samples.clear()

# Batch 31: V8/G7(10) V4/G5(10) V5/G7(10) V7/G5(10) V6/G8(10)
make_samples(1501, 8, 7, 10)
make_samples(1511, 4, 5, 10)
make_samples(1521, 5, 7, 10)
make_samples(1531, 7, 5, 10)
make_samples(1541, 6, 8, 10)

with open("ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_31.jsonl", 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
