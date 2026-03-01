import json
from generate_batch_02 import make_samples, samples
samples.clear()

# Batch 05: V4/G4(10) V4/G5(10) V5/G4(10) V5/G5(10) V5/G6(10) (Samples 0201-0250)
make_samples(201, 4, 4, 10)
make_samples(211, 4, 5, 10)
make_samples(221, 5, 4, 10)
make_samples(231, 5, 5, 10)
make_samples(241, 5, 6, 10)

with open("ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_05.jsonl", 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
