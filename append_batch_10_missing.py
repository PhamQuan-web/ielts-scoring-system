import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch10.jsonl")

def create_sample(index, vocab_band, grammar_band, question, transcript, response_type,
                  micro_flaws, grammar_profile, vocab_reason, grammar_reason,
                  idiom_present, risk_level):

    sample_id = f"syn_p3_v{vocab_band}_g{grammar_band}_{index:03d}"
    word_count = len(transcript.split())

    input_text = (
        f"Part: 3\n"
        f"Question: {question}\n\n"
        f"Transcript: {transcript}\n\n"
        f"Word Count: {word_count} words\n"
        f"Response Type: {response_type}"
    )

    output_text = (
        f"## Vocabulary (Lexical Resource): Band {vocab_band}\n\n"
        f"**Reasoning:** {vocab_reason}\n\n"
        f"**Idiom present:** {'Yes' if idiom_present else 'No'}\n"
        f"**Risk level:** {risk_level.capitalize()}\n\n"
        f"---\n\n"
        f"## Grammar (Grammatical Range & Accuracy): Band {grammar_band}\n\n"
        f"**Reasoning:** {grammar_reason}\n\n"
        f"**Micro flaws identified:**\n" +
        "\n".join([f"- {flaw}" for flaw in micro_flaws])
    )

    return {
        "sample_id": sample_id,
        "video_id": "synthetic",
        "part": 3,
        "question": question,
        "transcript_cleaned": transcript,
        "word_count": word_count,
        "response_type": response_type,
        "micro_flaws": micro_flaws,
        "grammar_profile": grammar_profile,
        "vocab_reason": vocab_reason,
        "grammar_reason": grammar_reason,
        "vocabulary": vocab_band,
        "grammar": grammar_band,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": idiom_present,
        "risk_level": risk_level,
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": input_text,
        "output": output_text
    }

samples = []

# --- BATCH 10 SUPPLEMENT: SAMPLES 871-880 (10 Total) ---
# Combo: V9/G9

missing_topics = [
    ("Society", "Community", "Why is community important?", "It is the bedrock of human existence. We are inherently social creatures, biologically wired for connection. A strong community provides a safety net during crises and amplifies joy during celebrations. It fosters a sense of belonging that is vital for mental health. In an increasingly atomized world, rebuilding communal bonds is an urgent imperative."),
    ("Work", "Future", "Will AI replace all jobs?", "While AI will undoubtedly disrupt the labor market, total replacement is unlikely. AI excels at optimization and data processing, but it lacks the nuance of human creativity and emotional intelligence. We will likely see a symbiosis where AI augments human capabilities. The challenge lies in adapting our education systems to prepare for this hybrid future."),
    ("Culture", "Art", "Is art essential?", "Absolutely. Art is the highest expression of the human spirit. It transcends language and culture, communicating universal truths. It challenges the status quo and provokes introspection. A society that neglects art is spiritually impoverished. It is not a luxury, but a fundamental necessity for a vibrant, reflective civilization."),
    ("Environment", "Climate", "Can we reverse climate change?", "The window of opportunity is narrowing, but it is not shut. We possess the technological solutions, from renewable energy to carbon capture. What is lacking is the political will to implement them at scale. It requires a radical transformation of our economic systems. If we act with urgency and unity, we can avert the worst potential outcomes."),
    ("Technology", "Privacy", "Is privacy dead?", "It is certainly under siege. In the age of surveillance capitalism, our data is harvested and monetized with impunity. The notion of privacy has been eroded by the convenience of digital services. However, a pushback is emerging. Regulatory frameworks and encryption technologies offer a path to reclaiming our digital sovereignty. It is a battle worth fighting."),
    ("Education", "Learning", "Is lifelong learning important?", "In a rapidly evolving world, it is indispensable. The skills we learn in school are becoming obsolete faster than ever. Continuous upskilling is necessary to remain relevant in the workforce. Moreover, learning keeps the mind sharp and fosters intellectual curiosity. It is a journey of self-improvement that should never end."),
    ("Health", "Mental", "How to improve mental health?", "We must destigmatize mental illness. Open dialogue is the first step towards healing. Access to affordable care is also crucial. Furthermore, we need to address the root causes of stress in our society, such as economic insecurity and social isolation. Promoting a culture of empathy and support is essential for collective well-being."),
    ("Transport", "Cities", "How to fix traffic?", "A multi-modal approach is required. We must prioritize public transport and active travel over private cars. Congestion pricing can deter unnecessary driving. Smart traffic management systems can optimize flow. Ultimately, we need to redesign our cities to reduce the need for travel, creating '15-minute cities' where amenities are local."),
    ("Society", "Inequality", "Is inequality inevitable?", "To some degree, perhaps, but the current levels are grotesque. Extreme wealth concentration distorts democracy and stifles opportunity. It is a policy choice, not a law of nature. Through progressive taxation and investment in public services, we can reduce the gap. A more egalitarian society is not only fairer but also more stable and prosperous."),
    ("Culture", "Tradition", "Should we keep traditions?", "Traditions are the anchors of identity. They connect us to our past and provide a sense of continuity. However, they should not be static. Traditions must evolve to remain relevant. We should cherish those that foster connection and discard those that perpetuate prejudice. It is about honoring the spirit of the past while embracing the future.")
]

start_index = 871
for i, topic in enumerate(missing_topics):
    samples.append(create_sample(
        index=start_index + i,
        vocab_band=9,
        grammar_band=9,
        question=topic[2],
        transcript=topic[3],
        response_type="extended",
        micro_flaws=[],
        grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
        vocab_reason="[LR9] Demonstrates full flexibility and precision. Uses idiomatic language naturally. >Band 8: Near-native proficiency.",
        grammar_reason="[GRA9] Uses a full range of structures naturally and appropriately. Produces consistently error-free sentences. >Band 8: Complete control.",
        idiom_present=True,
        risk_level="high"
    ))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
