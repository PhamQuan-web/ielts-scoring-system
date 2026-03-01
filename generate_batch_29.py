import json
from generate_batch_02 import make_samples, samples
samples.clear()

# Batch 29: V9/G9(10) V4/G4(10) V5/G5(10) V6/G7(10) V7/G8(10)
make_samples(1401, 9, 9, 10)
make_samples(1411, 4, 4, 10)
make_samples(1421, 5, 5, 10)
make_samples(1431, 6, 7, 10)
make_samples(1441, 7, 8, 10)

with open("ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_29.jsonl", 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
