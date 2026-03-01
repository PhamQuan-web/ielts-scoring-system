import json
from generate_batch_02 import make_samples, samples
samples.clear()

# Batch 06: V6/G5(10) V6/G6(10) V6/G7(10) V7/G6(10) V7/G7(10) (Samples 0251-0300)
make_samples(251, 6, 5, 10)
make_samples(261, 6, 6, 10)
make_samples(271, 6, 7, 10)
make_samples(281, 7, 6, 10)
make_samples(291, 7, 7, 10)

with open("ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_06.jsonl", 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
