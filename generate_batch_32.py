import json
from generate_batch_02 import make_samples, samples
samples.clear()

# Batch 32: V8/G6(10) V9/G7(10) V4/G6(5) V5/G4(5) (Total 30)
make_samples(1551, 8, 6, 10)
make_samples(1561, 9, 7, 10)
make_samples(1571, 4, 6, 5)
make_samples(1576, 5, 4, 5)

with open("ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_32.jsonl", 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
