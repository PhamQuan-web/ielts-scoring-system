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

# --- SAMPLES 11-30 ---
# Mix V4/G4 and V4/G5

# Sample 11: V4/G4 - Topic: Food (Restaurants)
samples.append(create_sample(
    index=11,
    vocab_band=4,
    grammar_band=4,
    question="Do people in your country prefer eating out or cooking at home?",
    transcript="Many people like eat out. Because restaurant have good food. And they not need cook. But some people cook at home. It is cheap. Also, healthy. I think young people like eat out more. Old people like cook.",
    response_type="direct_answer",
    micro_flaws=[
        "verb construction: 'like eat' -> 'like eating' or 'like to eat'",
        "verb agreement: 'restaurant have' -> 'restaurants have'",
        "verb construction: 'not need cook' -> 'do not need to cook'",
        "adjective/noun confusion: 'Also, healthy' -> 'Also, it is healthy'",
        "verb construction: 'like cook' -> 'like cooking'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic vocabulary: 'eat out', 'restaurant', 'good', 'cook', 'cheap'. >Band 3: Meaning conveyed. Not Band 5: Repetitive use of 'cook', 'eat'. Lacks 'cuisine', 'ingredients', 'convenience'.",
    grammar_reason="[GRA4] Simple sentences mostly. 'Also, healthy' is a fragment. Errors in verb patterns 'like eat' are frequent. >Band 3: Logical sequence. Not Band 5: Systematic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 12: V4/G5 - Topic: Travel (Tourism)
samples.append(create_sample(
    index=12,
    vocab_band=4,
    grammar_band=5,
    question="How does tourism help a country's economy?",
    transcript="Tourist bring money. They stay in hotel and eat food. This help business. Also, people get job. If more tourist come, the country will rich. I think tourism is very important. But sometimes too many people is bad.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Tourist bring' -> 'Tourists bring'",
        "singular/plural: 'stay in hotel' -> 'stay in hotels'",
        "verb agreement: 'This help' -> 'This helps'",
        "singular/plural: 'get job' -> 'get jobs'",
        "singular/plural: 'more tourist' -> 'more tourists'",
        "adjective confusion: 'country will rich' -> 'country will be rich'",
        "verb agreement: 'people is bad' -> 'people are bad'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'money', 'hotel', 'food', 'business', 'job'. >Band 3: Understandable. Not Band 5: Lacks 'revenue', 'employment', 'sector', 'infrastructure'.",
    grammar_reason="[GRA5] Conditionals: 'If more tourist come...'. Connectors: 'Also', 'But'. >Band 4: Some complex attempts succeed. Not Band 6: Basic errors 'This help', 'will rich' persist.",
    idiom_present=False,
    risk_level="low"
))

# Sample 13: V4/G4 - Topic: Sport (Team vs Individual)
samples.append(create_sample(
    index=13,
    vocab_band=4,
    grammar_band=4,
    question="Is it better to play team sports or individual sports?",
    transcript="Team sport is good for friend. You can play together. Like football. But individual sport is good too. You can do what you want. Like running. I like team sport more. Because it is fun. And I make friend.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'Team sport' -> 'Team sports'",
        "singular/plural: 'friend' -> 'friends'",
        "sentence fragment: 'Like football' (acceptable in speech but frequent use implies limited structure)",
        "sentence fragment: 'Like running'",
        "singular/plural: 'make friend' -> 'make friends'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Limited vocabulary: 'good', 'friend', 'play', 'fun'. Repetition of 'sport'. >Band 3: Communicates preference. Not Band 5: Lacks 'cooperation', 'discipline', 'independent'.",
    grammar_reason="[GRA4] Very simple sentences. Fragments 'Like football'. Errors in plurals. >Band 3: Coherent. Not Band 5: Errors are noticeable and structures are simple.",
    idiom_present=False,
    risk_level="low"
))

# Sample 14: V4/G5 - Topic: Media (News)
samples.append(create_sample(
    index=14,
    vocab_band=4,
    grammar_band=5,
    question="Do young people watch the news on TV?",
    transcript="No, young people use phone. They see news on internet. TV is for old people. I check news on Facebook. It is fast. If something happen, I know quick. But TV news is sometimes better because it is true.",
    response_type="direct_answer",
    micro_flaws=[
        "missing article: 'use phone' -> 'use phones' or 'their phones'",
        "missing article: 'on internet' -> 'on the internet'",
        "verb agreement: 'something happen' -> 'something happens'",
        "adjective/adverb: 'know quick' -> 'know quickly'",
        "limited vocabulary: 'old', 'fast', 'true', 'better'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic vocabulary: 'phone', 'internet', 'old', 'fast', 'true'. >Band 3: clear. Not Band 5: Lacks 'social media', 'reliable', 'source', 'broadcast'.",
    grammar_reason="[GRA5] Complex sentence attempt: 'If something happen, I know quick'. Causal clause: 'because it is true'. >Band 4: Uses complex structures to explain. Not Band 6: Errors in agreement and word forms.",
    idiom_present=False,
    risk_level="low"
))

# Sample 15: V4/G4 - Topic: Animals (Zoos)
samples.append(create_sample(
    index=15,
    vocab_band=4,
    grammar_band=4,
    question="Should wild animals be kept in zoos?",
    transcript="Zoo is good for see animal. But animal not happy. Cage is small. They want run free. Some zoo is good. They help sick animal. But I think animal should live in forest. It is better for them.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'Zoo is' -> 'Zoos are'",
        "verb form: 'for see animal' -> 'for seeing animals'",
        "missing verb: 'animal not happy' -> 'animals are not happy'",
        "missing article: 'Cage is small' -> 'The cage is small' or 'Cages are small'",
        "verb form: 'want run' -> 'want to run'",
        "singular/plural: 'sick animal' -> 'sick animals'",
        "missing article: 'in forest' -> 'in the forest'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'happy', 'small', 'free', 'sick', 'forest'. >Band 3: Intelligible. Not Band 5: Lacks 'captivity', 'natural habitat', 'conserve'.",
    grammar_reason="[GRA4] Simple sentences often lacking verbs or articles. 'But animal not happy'. >Band 3: Logical connection. Not Band 5: Omission of auxiliary verbs is systematic.",
    idiom_present=False,
    risk_level="low"
))

# Sample 16: V4/G5 - Topic: Family (Size)
samples.append(create_sample(
    index=16,
    vocab_band=4,
    grammar_band=5,
    question="Why are families becoming smaller in many countries?",
    transcript="Before, family is big. Many children. But now, life is expensive. To raise child cost money. Parents work hard. They not have time. If have many children, it is difficult. So small family is better now.",
    response_type="direct_answer",
    micro_flaws=[
        "verb tense: 'family is big' -> 'families were big'",
        "sentence fragment: 'Many children' (acceptable emphasis)",
        "phrase error: 'raise child cost money' -> 'raising a child costs money'",
        "verb construction: 'not have time' -> 'do not have time'",
        "conditional error: 'If have many children' -> 'If they have many children'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Simple vocabulary: 'big', 'expensive', 'money', 'hard', 'time'. >Band 3: clear meaning. Not Band 5: Lacks 'cost of living', 'expenses', 'career', 'responsibility'.",
    grammar_reason="[GRA5] Uses conditionals 'If have many children...'. Reason clauses imply 'because'. >Band 4: Some control of complex ideas. Not Band 6: Missing subjects and auxiliary verbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 17: V4/G4 - Topic: Transport (Public Transport)
samples.append(create_sample(
    index=17,
    vocab_band=4,
    grammar_band=4,
    question="What are the benefits of using public transport?",
    transcript="Public transport is cheap. Bus and train. You can sleep on bus. Not drive. It is good for air. Car make pollution. But bus is slow sometimes. People not like wait. I use bus every day.",
    response_type="direct_answer",
    micro_flaws=[
        "sentence fragment: 'Bus and train'",
        "verb form: 'Not drive' -> 'You do not have to drive'",
        "singular/plural: 'Car make' -> 'Cars make'",
        "verb construction: 'not like wait' -> 'do not like waiting'",
        "missing article: 'on bus' -> 'on the bus'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Limited vocabulary: 'cheap', 'sleep', 'air', 'slow', 'wait'. >Band 3: Understandable. Not Band 5: Lacks 'affordable', 'convenient', 'environmentally friendly'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'Not drive'. 'People not like wait'. >Band 3: Coherent ideas. Not Band 5: Errors in basic verb patterns.",
    idiom_present=False,
    risk_level="low"
))

# Sample 18: V4/G5 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=18,
    vocab_band=4,
    grammar_band=5,
    question="Is recycling important for protecting the environment?",
    transcript="Yes, recycling is very important. We make too much trash. If we recycle, we save the earth. Plastic is bad. It stay long time. I think everyone should recycle. If not, the world will dirty.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'trash' (uncountable, correct)",
        "verb agreement: 'It stay' -> 'It stays'",
        "phrase error: 'stay long time' -> 'stays for a long time'",
        "adjective confusion: 'world will dirty' -> 'world will be dirty'",
        "conditional error: 'If not' (acceptable but simple)"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'trash', 'save', 'earth', 'bad', 'dirty'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'waste', 'pollution', 'decompose', 'landfill'.",
    grammar_reason="[GRA5] Conditionals: 'If we recycle...', 'If not...'. >Band 4: Uses complex structures to support opinion. Not Band 6: Basic errors 'It stay', 'will dirty' are frequent.",
    idiom_present=False,
    risk_level="low"
))

# Sample 19: V4/G4 - Topic: Technology (Children)
samples.append(create_sample(
    index=19,
    vocab_band=4,
    grammar_band=4,
    question="At what age should children be allowed to have their own phone?",
    transcript="I think 12 year old. Phone is good for call parent. But children play game too much. It is bad for eye. Small children not need phone. They break it. So wait until they big.",
    response_type="direct_answer",
    micro_flaws=[
        "plural: '12 year old' -> '12 years old'",
        "verb form: 'good for call' -> 'good for calling'",
        "singular/plural: 'parent' -> 'parents'",
        "singular/plural: 'game' -> 'games'",
        "singular/plural: 'eye' -> 'eyes'",
        "verb construction: 'not need phone' -> 'do not need a phone'",
        "phrase error: 'until they big' -> 'until they are big'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Repetitive basic words: 'good', 'bad', 'big', 'break'. >Band 3: Intelligible. Not Band 5: Lacks 'responsibility', 'supervision', 'distraction'.",
    grammar_reason="[GRA4] Simple sentences with frequent omissions. 'Phone is good for call'. 'They big'. >Band 3: Logical flow. Not Band 5: Auxiliary verbs frequently missing.",
    idiom_present=False,
    risk_level="low"
))

# Sample 20: V4/G5 - Topic: Work (Retirement)
samples.append(create_sample(
    index=20,
    vocab_band=4,
    grammar_band=5,
    question="What is the best age for people to retire?",
    transcript="Maybe 60 or 65. If people work too long, they get tired. Old people need rest. But some people like work. If they healthy, they can work more. I think it depend on the person. But government give money is important.",
    response_type="direct_answer",
    micro_flaws=[
        "adjective confusion: 'If they healthy' -> 'If they are healthy'",
        "verb agreement: 'it depend' -> 'it depends'",
        "phrase error: 'government give money is important' -> 'the government giving money is important' or 'it is important that the government gives money'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic vocabulary: 'tired', 'rest', 'healthy', 'money'. >Band 3: Clear. Not Band 5: Lacks 'pension', 'contribute', 'workforce', 'energy'.",
    grammar_reason="[GRA5] Conditionals: 'If people work...', 'If they healthy...'. >Band 4: Complex structures attempted. Not Band 6: Errors in basic agreement and verb 'be' omission.",
    idiom_present=False,
    risk_level="low"
))

# Append to file
with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
