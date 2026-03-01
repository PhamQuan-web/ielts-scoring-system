import json
from generate_batch_02 import make_samples, samples
samples.clear()

# Batch 04: V9/G9(10) V5/G7(10) V7/G5(10) V6/G8(10) V8/G6(10) (Samples 0151-0200)
make_samples(151, 9, 9, 10)
make_samples(161, 5, 7, 10)
make_samples(171, 7, 5, 10)
make_samples(181, 6, 8, 10)
make_samples(191, 8, 6, 10)

with open("ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_04.jsonl", 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
