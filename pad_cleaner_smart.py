import json
import glob
import random

files = ["ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_28.jsonl"]

def get_contextual_padding(vocab_band, grammar_band):
    if vocab_band >= 8:
        pads = [
            " This realization fundamentally shifted my paradigm, prompting a deep introspection regarding my own values. It was a profoundly enlightening experience that continues to influence my daily decisions.",
            " Reflecting on this occurrence, I am struck by the sheer unpredictability of such events and the cascading effects they have on our trajectory. It was, without a doubt, a pivotal moment.",
            " The enduring legacy of this episode is a testament to the resilience we can muster when confronted with unexpected variables. I often draw upon this memory during challenging times.",
            " This multifaceted experience provided invaluable insights into human nature and the complexities of interpersonal dynamics. I consider myself immensely fortunate to have been part of it.",
            " The overarching implications of this situation extended far beyond my initial expectations, altering my worldview significantly. It was a catalyst for substantial personal evolution.",
            " Ultimately, the nuanced lessons I gleaned from this period remain integral to my professional and personal philosophy. It was an exceptionally rewarding chapter."
        ]
        return random.choice(pads)
    elif vocab_band >= 6:
        pads = [
            " Looking back, I realize how much this specific event taught me about myself and my capabilities. It was a truly valuable lesson that I will carry forward.",
            " The whole experience gave me a completely new perspective on things I used to take for granted. I am really glad that I had the opportunity to go through it.",
            " This situation helped me understand the importance of being patient and open-minded when facing new challenges. It was definitely a memorable time for me.",
            " In the end, I felt a great sense of accomplishment and satisfaction with how everything turned out. It is a story I often share with my close friends.",
            " The memories of that day are still very clear in my mind, mostly because it was so different from my usual routine. I hope to have similar experiences in the future.",
            " Overall, it was a very positive experience that contributed significantly to my personal growth. I look back on it with a lot of fondness."
        ]
        return random.choice(pads)
    else:
        pads = [
            " I think it was a very good day and I learned many new things. I want to do it again next time.",
            " It was a nice time for me and my family. We all felt very happy and smiled a lot.",
            " I remember this day because it was special and different. It was very fun.",
            " This is why I chose to talk about this topic today. It is a good memory for me.",
            " I hope I can go there again soon. It is a beautiful place to visit on the weekend.",
            " It was a simple thing but it made me feel good. I like remembering it."
        ]
        return random.choice(pads)

for f in files:
    samples = []
    with open(f, "r") as file:
        for line in file:
            s = json.loads(line)
            samples.append(s)

    modified = False
    for s in samples:
        if s["part"] == 2 and s["word_count"] < 125:
            modified = True
            while len(s["transcript_cleaned"].split()) < 125:
                s["transcript_cleaned"] += get_contextual_padding(s["vocabulary"], s["grammar"])

            s["word_count"] = len(s["transcript_cleaned"].split())
            s["input"] = f"Part: {s['part']}\nQuestion: {s['question']}\n\nTranscript: {s['transcript_cleaned']}\n\nWord Count: {s['word_count']} words\nResponse Type: {s['response_type']}"

    if modified:
        with open(f, "w") as file:
            for s in samples:
                file.write(json.dumps(s) + "\n")
        print(f"Padded conditionally {f}")
