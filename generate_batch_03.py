import json
from generate_batch_02 import make_samples, samples
samples.clear()

# Batch 03: V7/G8(10) V8/G7(10) V8/G8(10) V8/G9(10) V9/G8(10) (Samples 0101-0150)
make_samples(101, 7, 8, 10)
make_samples(111, 8, 7, 10)
make_samples(121, 8, 8, 10)
make_samples(131, 8, 9, 10)
make_samples(141, 9, 8, 10)

with open("ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_03.jsonl", 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
