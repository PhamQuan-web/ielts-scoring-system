import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch01.jsonl")

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

# --- SAMPLES 21-30 ---
# Mix V4/G4 and V4/G5

# Sample 21: V4/G4 - Topic: Culture (Language)
samples.append(create_sample(
    index=21,
    vocab_band=4,
    grammar_band=4,
    question="Is learning a foreign language difficult?",
    transcript="Yes, very hard. English is difficult for me. Grammar is hard. Words are many. I learn 5 year but I speak bad. Some people learn fast. But I am slow. I think need practice every day.",
    response_type="direct_answer",
    micro_flaws=[
        "word order: 'Words are many' -> 'There are many words'",
        "verb tense: 'learn 5 year' -> 'have learned for 5 years'",
        "adjective/adverb: 'speak bad' -> 'speak badly'",
        "verb construction: 'need practice' -> 'need to practice'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Simple adjectives: 'hard', 'difficult', 'bad', 'fast', 'slow'. >Band 3: Basic meaning. Not Band 5: Lacks 'complicated', 'fluency', 'acquire'.",
    grammar_reason="[GRA4] Short simple sentences. 'Words are many'. 'I learn 5 year'. >Band 3: Logical. Not Band 5: Tense errors and word order issues are frequent.",
    idiom_present=False,
    risk_level="low"
))

# Sample 22: V4/G5 - Topic: Health (Fast Food)
samples.append(create_sample(
    index=22,
    vocab_band=4,
    grammar_band=5,
    question="Why is fast food so popular these days?",
    transcript="Fast food is cheap and quick. People busy so they buy it. It taste good. But it is not healthy. Too much fat. If eat every day, you get fat. I think people know it bad but they still eat.",
    response_type="direct_answer",
    micro_flaws=[
        "missing verb: 'People busy' -> 'People are busy'",
        "verb agreement: 'It taste' -> 'It tastes'",
        "missing subject/verb: 'Too much fat' -> 'There is too much fat'",
        "conditional error: 'If eat every day' -> 'If you eat every day'",
        "phrase error: 'know it bad' -> 'know it is bad'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'cheap', 'quick', 'fat', 'bad', 'eat'. >Band 3: Clear. Not Band 5: Lacks 'convenient', 'nutrition', 'obesity', 'ingredients'.",
    grammar_reason="[GRA5] Uses conditionals: 'If eat every day...'. Connectors: 'So', 'But'. >Band 4: Complex attempts. Not Band 6: Basic errors 'It taste', 'People busy'.",
    idiom_present=False,
    risk_level="low"
))

# Sample 23: V4/G4 - Topic: Technology (Space)
samples.append(create_sample(
    index=23,
    vocab_band=4,
    grammar_band=4,
    question="Should governments spend money on space exploration?",
    transcript="Space is interesting. But cost many money. We have problem on earth. Poor people need food. So I think stop go to space. Maybe in future is okay. Now is too expensive.",
    response_type="direct_answer",
    micro_flaws=[
        "phrase error: 'cost many money' -> 'costs a lot of money'",
        "singular/plural: 'have problem' -> 'have problems'",
        "phrase error: 'stop go to space' -> 'stop going to space'",
        "missing subject: 'in future is okay' -> 'in the future it is okay'",
        "missing subject: 'Now is too expensive' -> 'Now it is too expensive'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'money', 'problem', 'food', 'future', 'expensive'. >Band 3: Understandable. Not Band 5: Lacks 'investment', 'resources', 'priority', 'universe'.",
    grammar_reason="[GRA4] Simple sentences with missing subjects. 'Now is too expensive'. 'Cost many money'. >Band 3: Coherent. Not Band 5: Basic sentence structure errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 24: V4/G5 - Topic: Society (Crime)
samples.append(create_sample(
    index=24,
    vocab_band=4,
    grammar_band=5,
    question="How can we reduce crime in big cities?",
    transcript="Police is important. If more police on street, bad people scared. Also, camera is good. They see everything. I think if people have job, they not steal. So government should give job. Education is help too.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Police is' -> 'Police are'",
        "missing verb: 'more police on street' -> 'there are more police on the street'",
        "missing verb: 'bad people scared' -> 'bad people will be scared'",
        "singular/plural: 'camera' -> 'cameras'",
        "verb construction: 'not steal' -> 'will not steal'",
        "phrase error: 'Education is help' -> 'Education helps'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic vocabulary: 'police', 'bad', 'scared', 'job', 'steal'. >Band 3: Clear. Not Band 5: Lacks 'prevention', 'security', 'unemployment', 'poverty'.",
    grammar_reason="[GRA5] Conditionals: 'If more police...', 'If people have job...'. >Band 4: Uses complex structures to explain solutions. Not Band 6: Basic agreement errors and missing verbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 25: V4/G4 - Topic: Education (University)
samples.append(create_sample(
    index=25,
    vocab_band=4,
    grammar_band=4,
    question="Is a university degree necessary for success?",
    transcript="University is good. But not for everyone. Some job not need degree. Like chef or artist. They need skill. But doctor need degree. I think success is happy. Not just money.",
    response_type="direct_answer",
    micro_flaws=[
        "verb construction: 'job not need' -> 'jobs do not need'",
        "missing article: 'Like chef' -> 'Like a chef'",
        "verb agreement: 'doctor need' -> 'doctors need'",
        "word form: 'success is happy' -> 'success is happiness'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'good', 'job', 'skill', 'happy', 'money'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'qualification', 'career path', 'vocational', 'essential'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'Like chef or artist'. 'Not just money'. >Band 3: Logical. Not Band 5: Errors in basic structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 26: V4/G5 - Topic: Work (Robots)
samples.append(create_sample(
    index=26,
    vocab_band=4,
    grammar_band=5,
    question="What jobs will robots do in the future?",
    transcript="Robots will do many thing. Clean house, drive car, cook food. It is good because people can rest. But if robot take all job, people have no money. This is big problem. I think we need control robot.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'many thing' -> 'many things'",
        "sentence fragment: 'Clean house, drive car...'",
        "singular/plural: 'robot take all job' -> 'robots take all the jobs'",
        "verb construction: 'need control robot' -> 'need to control robots'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Repetitive basic words: 'robot', 'job', 'money', 'problem'. >Band 3: Clear. Not Band 5: Lacks 'automate', 'replace', 'workforce', 'regulate'.",
    grammar_reason="[GRA5] Conditionals: 'if robot take all job...'. Causal: 'because people can rest'. >Band 4: Complex reasoning attempted. Not Band 6: Basic errors in plurals and verb forms.",
    idiom_present=False,
    risk_level="low"
))

# Sample 27: V4/G4 - Topic: Environment (Climate Change)
samples.append(create_sample(
    index=27,
    vocab_band=4,
    grammar_band=4,
    question="Is climate change a serious problem?",
    transcript="Yes, very serious. The weather is hot. Ice is melt. Animal die. We need stop pollution. If not, maybe we die too. It is scary. People use too much car. And factory smoke.",
    response_type="direct_answer",
    micro_flaws=[
        "verb form: 'Ice is melt' -> 'Ice is melting'",
        "verb agreement: 'Animal die' -> 'Animals are dying'",
        "verb construction: 'need stop' -> 'need to stop'",
        "verb agreement: 'People use too much car' -> 'People use cars too much'",
        "sentence fragment: 'And factory smoke'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'hot', 'melt', 'die', 'stop', 'scary'. >Band 3: Understandable. Not Band 5: Lacks 'global warming', 'temperature', 'extinction', 'emissions'.",
    grammar_reason="[GRA4] Short simple sentences. 'Ice is melt'. 'And factory smoke'. >Band 3: Coherent. Not Band 5: Wrong verb forms are frequent.",
    idiom_present=False,
    risk_level="low"
))

# Sample 28: V4/G5 - Topic: Transport (Bicycles)
samples.append(create_sample(
    index=28,
    vocab_band=4,
    grammar_band=5,
    question="Why should people use bicycles more often?",
    transcript="Bicycle is good for health. You exercise when go work. Also, no pollution. It is cheap. If everyone use bicycle, the air is clean. But city need safe road for bike. Now it is dangerous because many car.",
    response_type="direct_answer",
    micro_flaws=[
        "missing article: 'Bicycle is' -> 'Bicycles are' or 'The bicycle is'",
        "phrase error: 'when go work' -> 'when going to work'",
        "verb agreement: 'everyone use' -> 'everyone uses'",
        "adjective confusion: 'air is clean' -> 'air will be clean'",
        "verb agreement: 'city need' -> 'the city needs'",
        "phrase error: 'because many car' -> 'because there are many cars'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'health', 'work', 'cheap', 'clean', 'safe'. >Band 3: Clear. Not Band 5: Lacks 'environment', 'fitness', 'congestion', 'lane'.",
    grammar_reason="[GRA5] Conditionals: 'If everyone use bicycle...'. Reason: 'because many car'. >Band 4: Uses complex structures. Not Band 6: Frequent errors in articles and verb tenses.",
    idiom_present=False,
    risk_level="low"
))

# Sample 29: V4/G4 - Topic: Family (Elders)
samples.append(create_sample(
    index=29,
    vocab_band=4,
    grammar_band=4,
    question="Who should take care of elderly people?",
    transcript="Family should take care. Children help parents. It is tradition. But if busy, maybe nursing home. But nursing home is expensive. And lonely. I think stay with family is best. We love them.",
    response_type="direct_answer",
    micro_flaws=[
        "missing subject: 'But if busy' -> 'But if they are busy'",
        "sentence fragment: 'And lonely' (acceptable)",
        "phrase error: 'stay with family' -> 'staying with family'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'care', 'help', 'busy', 'expensive', 'lonely'. >Band 3: Meaning clear. Not Band 5: Lacks 'responsibility', 'support', 'facility', 'generation'.",
    grammar_reason="[GRA4] Simple sentences. 'But if busy' is a fragment. 'Children help parents'. >Band 3: Logical. Not Band 5: Errors in structure.",
    idiom_present=False,
    risk_level="low"
))

# Sample 30: V4/G5 - Topic: Media (Fame)
samples.append(create_sample(
    index=30,
    vocab_band=4,
    grammar_band=5,
    question="Is it good to be famous?",
    transcript="Being famous have good and bad. Good is money. Everyone know you. Bad is no privacy. People follow you everywhere. If I famous, I not like it. I want normal life. So I think being famous is hard.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Being famous have' -> 'Being famous has'",
        "phrase error: 'Good is money' -> 'The good thing is money'",
        "verb agreement: 'Everyone know' -> 'Everyone knows'",
        "phrase error: 'Bad is no privacy' -> 'The bad thing is no privacy'",
        "conditional error: 'If I famous' -> 'If I were famous'",
        "verb construction: 'I not like it' -> 'I would not like it'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'good', 'bad', 'money', 'know', 'hard'. >Band 3: Intelligible. Not Band 5: Lacks 'celebrity', 'attention', 'disadvantage', 'private life'.",
    grammar_reason="[GRA5] Conditionals: 'If I famous, I not like it'. Contrast: 'Good is... Bad is...'. >Band 4: Attempts complex comparisons. Not Band 6: Basic verb errors 'have', 'know'.",
    idiom_present=False,
    risk_level="low"
))

# Append to file
with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
