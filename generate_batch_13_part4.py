import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch13.jsonl")

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
        f"## Grammar (Grammatical Range and Accuracy): Band {grammar_band}\n\n"
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

# --- BATCH 13 PART 4: SAMPLES 1141-1160 (20 Total) ---
# Combo: V7/G4 (Good Vocab, Limited Grammar)

# Sample 1141: V7/G4 - Topic: Environment
samples.append(create_sample(
    index=1141,
    vocab_band=7,
    grammar_band=4,
    question="Why preserve wildlife?",
    transcript="It is crucial to preserve the biodiversity because animals is important. The ecosystem rely on distinct species. If we destroyed the habitat, the consequences is severe. I believe that conservation efforts is paramount. People has to took responsibility for the environment.",
    response_type="extended",
    micro_flaws=["Subject-verb agreement error: 'animals is'", "Tense error: 'If we destroyed'", "Subject-verb agreement error: 'consequences is'", "Verb form error: 'has to took'"],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Good range: 'biodiversity', 'distinct species', 'conservation efforts', 'paramount'. >Band 6: Uses less common items. Not Band 8: Some precision issues.",
    grammar_reason="[GRA4] Limited range with frequent errors: 'animals is' (S-V), 'rely' (S-V), 'destroyed' (tense), 'consequences is' (S-V), 'has to took' (form). >Band 3: Meaning generally clear. Not Band 5: Errors are very frequent.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1142: V7/G4 - Topic: Technology
samples.append(create_sample(
    index=1142,
    vocab_band=7,
    grammar_band=4,
    question="Is AI beneficial?",
    transcript="AI is a groundbreaking innovation that transform our lives. The sophisticated algorithms helps us solving complex problems. However, there is ethical implications what we must considers. I thinks that artificial intelligence have immense potential but we must regulated it meticulously.",
    response_type="extended",
    micro_flaws=["Subject-verb agreement error: 'innovation that transform'", "Verb form error: 'helps us solving'", "Relative pronoun error: 'what we must'", "Subject-verb agreement error: 'I thinks'", "Subject-verb agreement error: 'intelligence have'"],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Lexical items: 'groundbreaking innovation', 'sophisticated algorithms', 'ethical implications', 'immense potential', 'meticulously'. >Band 6: Good collocations. Not Band 8: Slightly repetitive.",
    grammar_reason="[GRA4] Frequent errors: 'transform' (S-V), 'solving' (form), 'what' (relative), 'considers' (form), 'thinks' (S-V), 'have' (S-V). >Band 3: Sentences attempted. Not Band 5: Basic errors persist.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1143: V7/G4 - Topic: Education
samples.append(create_sample(
    index=1143,
    vocab_band=7,
    grammar_band=4,
    question="Is university necessary?",
    transcript="Higher education provides academic excellence and career prospects. Many student wants to acquire specialized knowledge. The curriculum are rigorous and demanding. I believes that university foster intellectual growth. But some people thinks vocational training is viable alternative.",
    response_type="extended",
    micro_flaws=["Subject-verb agreement error: 'student wants'", "Subject-verb agreement error: 'curriculum are'", "Subject-verb agreement error: 'I believes'", "Subject-verb agreement error: 'foster'", "Subject-verb agreement error: 'people thinks'"],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Vocabulary: 'academic excellence', 'career prospects', 'specialized knowledge', 'rigorous', 'intellectual growth', 'viable alternative'. >Band 6: Precise terms. Not Band 8: Lacks flexibility.",
    grammar_reason="[GRA4] Errors dominate: 'student wants', 'curriculum are', 'I believes', 'foster', 'people thinks'. >Band 3: Communicates ideas. Not Band 5: High error density.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1144: V7/G4 - Topic: Work
samples.append(create_sample(
    index=1144,
    vocab_band=7,
    grammar_band=4,
    question="Is job satisfaction important?",
    transcript="Job satisfaction is integral for professional fulfillment. If employees is motivated, they works efficiently. A conducive environment enhance productivity significantly. I feels that remuneration is secondary to passion. People who pursues their dreams is usually more content.",
    response_type="extended",
    micro_flaws=["Subject-verb agreement error: 'employees is'", "Subject-verb agreement error: 'they works'", "Subject-verb agreement error: 'environment enhance'", "Subject-verb agreement error: 'I feels'", "Subject-verb agreement error: 'People... is'"],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Good range: 'integral', 'professional fulfillment', 'conducive environment', 'remuneration', 'productivity'. >Band 6: Uses less common items. Not Band 8: Style slightly rigid.",
    grammar_reason="[GRA4] Basic errors: 'employees is', 'they works', 'enhance', 'I feels', 'People... is'. >Band 3: Meaning clear despite errors. Not Band 5: Errors in simple sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1145: V7/G4 - Topic: Society
samples.append(create_sample(
    index=1145,
    vocab_band=7,
    grammar_band=4,
    question="Why volunteer?",
    transcript="Volunteering foster community cohesion and altruism. It allow individuals to contributes to society. The philanthropic activities is beneficial for everyone. I has participated in charitable initiatives last year. It gave me a sense of purpose and fulfillment.",
    response_type="extended",
    micro_flaws=["Subject-verb agreement error: 'foster'", "Subject-verb agreement error: 'allow'", "Verb form error: 'to contributes'", "Subject-verb agreement error: 'activities is'", "Tense/Form error: 'I has participated... last year'"],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Vocab: 'community cohesion', 'altruism', 'philanthropic activities', 'charitable initiatives', 'fulfillment'. >Band 6: Good range. Not Band 8: Use is functional.",
    grammar_reason="[GRA4] Frequent errors: 'foster', 'allow', 'to contributes', 'activities is', 'I has participated' (wrong tense/auxiliary). >Band 3: Understandable. Not Band 5: Systematic errors.",
    idiom_present=False,
    risk_level="medium"
))

# Generating 1146-1160 with explicit reasoning
topics_13_4 = [
    {
        "question": "Is stress bad?",
        "transcript": "Chronic stress have detrimental effects on mental well-being. It can caused anxiety and depression. We must prioritizes psychological health. I thinks that meditation alleviate the symptoms effectively.",
        "micro_flaws": ["Subject-verb agreement error: 'stress have'", "Verb form error: 'can caused'", "Subject-verb agreement error: 'must prioritizes'", "Subject-verb agreement error: 'I thinks'", "Subject-verb agreement error: 'meditation alleviate'"],
        "vocab_reason": "[LR7] Vocab: 'chronic stress', 'detrimental effects', 'mental well-being', 'anxiety', 'psychological health', 'alleviate'. >Band 6: Precise terms. Not Band 8: Some repetition.",
        "grammar_reason": "[GRA4] Frequent errors: 'stress have' (S-V), 'can caused' (modal+V3), 'prioritizes' (after must), 'I thinks' (S-V). >Band 3: Meaning clear. Not Band 5: Basic errors throughout."
    },
    {
        "question": "Is it efficient?",
        "transcript": "The infrastructure is inadequate for the population. Commuters faces congestion daily. The rapid transit system need substantial investment. I suggests that government allocates funds for improvement.",
        "micro_flaws": ["Subject-verb agreement error: 'Commuters faces'", "Subject-verb agreement error: 'system need'", "Subject-verb agreement error: 'I suggests'", "Subject-verb agreement error: 'government allocates'"],
        "vocab_reason": "[LR7] Vocab: 'infrastructure', 'inadequate', 'commuters', 'congestion', 'rapid transit', 'substantial investment'. >Band 6: Good range. Not Band 8: Lacks nuance.",
        "grammar_reason": "[GRA4] Errors: 'faces' (S-V), 'need' (S-V), 'suggests' (S-V), 'allocates' (subjunctive expected). >Band 3: Communicates ideas. Not Band 5: Errors are systematic."
    },
    {
        "question": "Why keep traditions?",
        "transcript": "Cultural heritage define our national identity. It preserve the customs of our ancestors. If we forgets our roots, we loses our history. Traditional festivals plays a vital role in society.",
        "micro_flaws": ["Subject-verb agreement error: 'heritage define'", "Subject-verb agreement error: 'preserve'", "Subject-verb agreement error: 'we forgets'", "Subject-verb agreement error: 'we loses'", "Subject-verb agreement error: 'festivals plays'"],
        "vocab_reason": "[LR7] Vocab: 'cultural heritage', 'national identity', 'customs', 'ancestors', 'vital role'. >Band 6: Collocations used well. Not Band 8: A bit formulaic.",
        "grammar_reason": "[GRA4] Basic S-V errors: 'define', 'preserve', 'forgets', 'loses', 'plays'. >Band 3: Meaning clear. Not Band 5: Errors in almost every sentence."
    },
    {
        "question": "Is it addictive?",
        "transcript": "Social media platforms induces addictive behavior. Users consumes content excessively. The algorithm manipulate our preferences. I believes that digital detox is essential for mental clarity.",
        "micro_flaws": ["Subject-verb agreement error: 'platforms induces'", "Subject-verb agreement error: 'Users consumes'", "Subject-verb agreement error: 'algorithm manipulate'", "Subject-verb agreement error: 'I believes'"],
        "vocab_reason": "[LR7] Vocab: 'induces', 'addictive behavior', 'excessively', 'algorithm', 'digital detox', 'mental clarity'. >Band 6: Good topic vocab. Not Band 8: Slightly repetitive.",
        "grammar_reason": "[GRA4] Frequent S-V errors: 'induces', 'consumes', 'manipulate', 'believes'. >Band 3: Understandable. Not Band 5: High error density."
    },
    {
        "question": "Is it real?",
        "transcript": "Global warming pose a catastrophic threat to humanity. The carbon emissions has increased drastically. We must implements sustainable practices immediately. Future generations suffers if we ignores the warning signs.",
        "micro_flaws": ["Subject-verb agreement error: 'warming pose'", "Subject-verb agreement error: 'emissions has'", "Verb form error: 'must implements'", "Subject-verb agreement error: 'generations suffers'", "Subject-verb agreement error: 'we ignores'"],
        "vocab_reason": "[LR7] Vocab: 'global warming', 'catastrophic threat', 'carbon emissions', 'sustainable practices', 'drastically'. >Band 6: Precise. Not Band 8: Less flexible.",
        "grammar_reason": "[GRA4] Errors: 'pose' (S-V), 'has' (plural subject), 'implements' (after modal), 'suffers' (S-V), 'ignores' (S-V). >Band 3: Meaning conveyed. Not Band 5: Basic errors."
    },
    {
        "question": "Is it important?",
        "transcript": "Gender equality is fundamental human right. Discrimination hinder social progress. Everyone deserve equal opportunities in workplace. I supports policies that promotes inclusivity and diversity.",
        "micro_flaws": ["Missing article: 'fundamental human right'", "Subject-verb agreement error: 'Discrimination hinder'", "Subject-verb agreement error: 'Everyone deserve'", "Subject-verb agreement error: 'I supports'", "Subject-verb agreement error: 'policies that promotes'"],
        "vocab_reason": "[LR7] Vocab: 'fundamental human right', 'discrimination', 'social progress', 'inclusivity', 'diversity'. >Band 6: Good range. Not Band 8: Lacks idiomatic flow.",
        "grammar_reason": "[GRA4] Errors: 'hinder' (S-V), 'deserve' (S-V), 'I supports' (S-V), 'promotes' (antecedent policies). >Band 3: Clear. Not Band 5: Errors impede flow."
    },
    {
        "question": "Is it good?",
        "transcript": "Telecommuting offer flexibility and autonomy. Employees maintains work-life balance. However, isolation affect collaboration negatively. I prefers hybrid model which combine best of both worlds.",
        "micro_flaws": ["Subject-verb agreement error: 'Telecommuting offer'", "Subject-verb agreement error: 'Employees maintains'", "Subject-verb agreement error: 'isolation affect'", "Subject-verb agreement error: 'I prefers'", "Subject-verb agreement error: 'model which combine'"],
        "vocab_reason": "[LR7] Vocab: 'telecommuting', 'flexibility', 'autonomy', 'work-life balance', 'isolation', 'hybrid model'. >Band 6: Specific terms. Not Band 8: Functional use.",
        "grammar_reason": "[GRA4] Errors: 'offer', 'maintains', 'affect', 'prefers', 'combine'. >Band 3: Meaning generally clear. Not Band 5: Persistent S-V errors."
    },
    {
        "question": "Is it effective?",
        "transcript": "E-learning provides accessible education globally. Students interacts with diverse resources. But technical issues disrupts the learning process. I feels that face-to-face interaction is indispensable.",
        "micro_flaws": ["Subject-verb agreement error: 'Students interacts'", "Subject-verb agreement error: 'issues disrupts'", "Subject-verb agreement error: 'I feels'"],
        "vocab_reason": "[LR7] Vocab: 'accessible education', 'diverse resources', 'technical issues', 'indispensable', 'interaction'. >Band 6: Good range. Not Band 8: Lacks sophistication.",
        "grammar_reason": "[GRA4] Errors: 'interacts' (S-V), 'disrupts' (S-V), 'I feels' (S-V). >Band 3: Understandable. Not Band 5: Systematic errors."
    },
    {
        "question": "Are they better?",
        "transcript": "Electric vehicles reduces carbon footprint significantly. The renewable energy source is eco-friendly. However, charging stations is scarce in some areas. I thinks adoption rate depend on government incentives.",
        "micro_flaws": ["Subject-verb agreement error: 'vehicles reduces'", "Subject-verb agreement error: 'stations is'", "Subject-verb agreement error: 'I thinks'", "Subject-verb agreement error: 'rate depend'"],
        "vocab_reason": "[LR7] Vocab: 'electric vehicles', 'carbon footprint', 'renewable energy', 'eco-friendly', 'government incentives'. >Band 6: Precise. Not Band 8: Formulaic.",
        "grammar_reason": "[GRA4] Errors: 'reduces' (S-V), 'stations is' (S-V), 'I thinks' (S-V), 'depend' (S-V). >Band 3: Meaning clear. Not Band 5: Frequent basic errors."
    },
    {
        "question": "Is fast food bad?",
        "transcript": "Processed food contain harmful additives and preservatives. Obesity rates has risen alarmingly. A balanced diet ensure physical vitality. People should consumes organic produce for better health.",
        "micro_flaws": ["Subject-verb agreement error: 'food contain'", "Subject-verb agreement error: 'rates has'", "Subject-verb agreement error: 'diet ensure'", "Verb form error: 'should consumes'"],
        "vocab_reason": "[LR7] Vocab: 'processed food', 'additives', 'preservatives', 'obesity rates', 'balanced diet', 'organic produce'. >Band 6: Good topic vocab. Not Band 8: Lacks flair.",
        "grammar_reason": "[GRA4] Errors: 'contain' (S-V), 'has' (plural subject), 'ensure' (S-V), 'should consumes' (modal+V3). >Band 3: Clear. Not Band 5: High error frequency."
    },
    {
        "question": "Will they replace us?",
        "transcript": "Automation threaten manual labor jobs. Artificial intelligence exceed human capabilities in some tasks. But creativity and empathy is unique to humans. I doubts that robots replaces us completely.",
        "micro_flaws": ["Subject-verb agreement error: 'Automation threaten'", "Subject-verb agreement error: 'intelligence exceed'", "Subject-verb agreement error: 'empathy is'", "Subject-verb agreement error: 'I doubts'", "Subject-verb agreement error: 'robots replaces'"],
        "vocab_reason": "[LR7] Vocab: 'automation', 'manual labor', 'artificial intelligence', 'capabilities', 'creativity', 'empathy'. >Band 6: Precise. Not Band 8: Functional.",
        "grammar_reason": "[GRA4] Errors: 'threaten', 'exceed', 'is' (compound subject), 'doubts', 'replaces'. >Band 3: Meaning clear. Not Band 5: Errors dominate."
    },
    {
        "question": "Why ban plastic?",
        "transcript": "Single-use plastics pollutes the oceans severely. Marine life is endangered by waste. We must adopts biodegradable alternatives. Legislation play a crucial role in waste management.",
        "micro_flaws": ["Subject-verb agreement error: 'plastics pollutes'", "Verb form error: 'must adopts'", "Subject-verb agreement error: 'Legislation play'"],
        "vocab_reason": "[LR7] Vocab: 'single-use plastics', 'marine life', 'endangered', 'biodegradable alternatives', 'legislation', 'waste management'. >Band 6: Good range. Not Band 8: Slightly repetitive.",
        "grammar_reason": "[GRA4] Errors: 'pollutes' (S-V), 'adopts' (after modal), 'play' (S-V). >Band 3: Understandable. Not Band 5: Basic errors."
    },
    {
        "question": "Is it good?",
        "transcript": "Urban migration cause overcrowding in cities. The infrastructure strain under pressure. However, economic opportunities attracts people. I believe that rural development prevent excessive migration.",
        "micro_flaws": ["Subject-verb agreement error: 'migration cause'", "Subject-verb agreement error: 'infrastructure strain'", "Subject-verb agreement error: 'opportunities attracts'", "Subject-verb agreement error: 'development prevent'"],
        "vocab_reason": "[LR7] Vocab: 'urban migration', 'overcrowding', 'infrastructure', 'economic opportunities', 'rural development'. >Band 6: Specific terms. Not Band 8: Lacks nuance.",
        "grammar_reason": "[GRA4] Errors: 'cause', 'strain', 'attracts', 'prevent'. >Band 3: Meaning clear. Not Band 5: Systematic S-V errors."
    },
    {
        "question": "Why learn languages?",
        "transcript": "Linguistic proficiency enhance cognitive abilities. It facilitate cross-cultural communication. Being bilingual open doors to opportunities. I has learned English since five years.",
        "micro_flaws": ["Subject-verb agreement error: 'proficiency enhance'", "Subject-verb agreement error: 'It facilitate'", "Subject-verb agreement error: 'bilingual open'", "Tense/Form error: 'I has learned... since'"],
        "vocab_reason": "[LR7] Vocab: 'linguistic proficiency', 'cognitive abilities', 'cross-cultural communication', 'bilingual'. >Band 6: High-level items. Not Band 8: Slightly rigid.",
        "grammar_reason": "[GRA4] Errors: 'enhance', 'facilitate', 'open', 'I has learned' (wrong aux/tense). >Band 3: Clear. Not Band 5: Errors persist."
    },
    {
        "question": "When to retire?",
        "transcript": "Retirement age depend on physical capability. Financial security is prerequisites for retiring. Elderly people contributes wisdom to society. I thinks that voluntary retirement is preferable.",
        "micro_flaws": ["Subject-verb agreement error: 'age depend'", "Subject-verb agreement error: 'security is prerequisites' (number)", "Subject-verb agreement error: 'people contributes'", "Subject-verb agreement error: 'I thinks'"],
        "vocab_reason": "[LR7] Vocab: 'retirement age', 'physical capability', 'financial security', 'prerequisites', 'voluntary retirement'. >Band 6: Good range. Not Band 8: Lacks flexibility.",
        "grammar_reason": "[GRA4] Errors: 'depend' (S-V), 'is prerequisites' (S-V/number), 'contributes' (S-V), 'I thinks' (S-V). >Band 3: Meaning clear. Not Band 5: Basic errors."
    }
]

start_index = 1146
for i, item in enumerate(topics_13_4):
    samples.append(create_sample(
        index=start_index + i,
        vocab_band=7,
        grammar_band=4,
        question=item["question"],
        transcript=item["transcript"],
        response_type="extended",
        micro_flaws=item["micro_flaws"],
        grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
        vocab_reason=item["vocab_reason"],
        grammar_reason=item["grammar_reason"],
        idiom_present=False,
        risk_level="medium"
    ))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
