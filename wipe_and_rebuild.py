import json
import random

def reset_and_clean(fn):
    samples = []
    with open(fn, "r", encoding="utf-8") as f:
        for line in f:
            samples.append(json.loads(line))

    # Remove ANY scripted endings from ALL files that might have been added by fix_lengths_part2.py
    # I will strip them off completely.
    bad_phrases = [
        "Marketers carefully analyze these specific consumer behaviors to maximize their corporate profits.",
        "The long-term stability of ", "definitely requires immediate, comprehensive government intervention.",
        "Ultimately, acquiring this specific physical ability guarantees personal safety in unpredictable aquatic environments.",
        "These profound digital transformations continue to redefine our basic relationship with",
        "We must prioritize the ecological preservation of these magnificent natural habitats immediately.",
        "Consequently, interacting directly with", "broadens our fundamental understanding of humanity.",
        "Developing such robust leadership skills is practically essential for maintaining long-term organizational success.",
        "Therefore, exploring these massive cosmic frontiers requires unprecedented levels of international funding.",
        "The continuous evolution of digital", "is absolutely transforming the modern classroom experience.",
        "Prioritizing the mindful development of these urban", "drastically improves collective civic happiness.",
        "Expanding these vital municipal services significantly enhances the overall quality of urban living.",
        "Managing the complex socioeconomic impacts of", "remains an incredibly daunting global challenge.",
        "Addressing this profound psychological burden is critical for maintaining a truly healthy modern workforce.",
        "Regulating the rapid proliferation of autonomous", "systems will dominate future political debates.",
        "Resolving these complex issues surrounding", "effectively demands our full, undivided attention today."
    ]

    for s in samples:
        t = s["transcript_cleaned"]
        for phrase in bad_phrases:
            if phrase in t:
                # Strip it out carefully
                t = t.split(" " + phrase)[0]
                t = t.split(phrase)[0]

        s["transcript_cleaned"] = t
        wc = len(t.split())
        s["word_count"] = wc

    with open(fn, "w", encoding="utf-8") as f:
        for s in samples:
            f.write(json.dumps(s) + "\n")

reset_and_clean("ielts-data/phase3/v76_review_output/synthetic_batches/batch_p3_22.jsonl")
reset_and_clean("ielts-data/phase3/v76_review_output/synthetic_batches/batch_p3_23.jsonl")
reset_and_clean("ielts-data/phase3/v76_review_output/synthetic_batches/batch_p3_24.jsonl")
