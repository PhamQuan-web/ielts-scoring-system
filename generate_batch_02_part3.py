import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch02.jsonl")

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

# --- BATCH 02 PART 3: SAMPLES 101-125 (25 Total) ---
# Combo: V5/G5 (Modest Vocab, Modest Grammar)

# Sample 101: V5/G5 - Topic: Education (University)
samples.append(create_sample(
    index=101,
    vocab_band=5,
    grammar_band=5,
    question="Why do many students want to study abroad?",
    transcript="I think they want to improve their language. English is international language. Also, foreign university have better facility. They can learn new culture and make friend. It is good experience for future job. If they study hard, they will success. But it is expensive for parents.",
    response_type="extended",
    micro_flaws=[
        "singular/plural: 'foreign university have' -> 'foreign universities have'",
        "singular/plural: 'better facility' -> 'better facilities'",
        "singular/plural: 'make friend' -> 'make friends'",
        "word form: 'they will success' -> 'they will succeed'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'improve', 'international', 'facility', 'culture', 'experience', 'success'. >Band 4: Uses relevant terms. Not Band 6: Lacks 'academic', 'prestigious', 'broaden horizons', 'career'.",
    grammar_reason="[GRA5] Attempts complex sentences. 'If they study hard, they will success'. 'I think they want...'. >Band 4: Uses subordinate clauses. Not Band 6: Frequent errors in basic agreement and word forms.",
    idiom_present=False,
    risk_level="low"
))

# Sample 102: V5/G5 - Topic: Technology (Robots)
samples.append(create_sample(
    index=102,
    vocab_band=5,
    grammar_band=5,
    question="Will robots replace humans in jobs?",
    transcript="Maybe in some job. Factory work is dangerous so robot is better. They not tired. But creative job need human. Robot cannot think like us. Also, robot is expensive to buy. If company use robot, many people lose job. This is big problem for society.",
    response_type="extended",
    micro_flaws=[
        "singular/plural: 'some job' -> 'some jobs'",
        "verb construction: 'They not tired' -> 'They do not get tired' or 'are not tired'",
        "verb agreement: 'creative job need' -> 'creative jobs need'",
        "conditional error: 'If company use robot' -> 'If companies use robots'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'dangerous', 'creative', 'society', 'replace'. >Band 4: Clear meaning. Not Band 6: Lacks 'artificial intelligence', 'automate', 'unemployment'.",
    grammar_reason="[GRA5] Uses conditionals: 'If company use robot...'. Contrast: 'But creative job need human'. >Band 4: Complex structures attempted. Not Band 6: Errors in subject-verb agreement persist.",
    idiom_present=False,
    risk_level="low"
))

# Sample 103: V5/G5 - Topic: Environment (Pollution)
samples.append(create_sample(
    index=103,
    vocab_band=5,
    grammar_band=5,
    question="What can we do to reduce air pollution?",
    transcript="We should use public transport more. Bus and train reduce car on road. Also, government should control factory smoke. It is main cause of pollution. We can plant more tree in city. Tree give fresh air. If everyone do this, the air will clean.",
    response_type="extended",
    micro_flaws=[
        "singular/plural: 'reduce car' -> 'reduce cars'",
        "singular/plural: 'plant more tree' -> 'plant more trees'",
        "verb agreement: 'Tree give' -> 'Trees give'",
        "conditional error: 'If everyone do this' -> 'If everyone does this'",
        "adjective error: 'air will clean' -> 'air will be clean'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'public transport', 'factory', 'smoke', 'pollution', 'fresh air'. >Band 4: Relevant vocabulary. Not Band 6: Lacks 'emissions', 'carbon footprint', 'environmentally friendly'.",
    grammar_reason="[GRA5] Conditionals: 'If everyone do this...'. Modals: 'should use', 'should control'. >Band 4: Uses range of structures. Not Band 6: Basic errors in agreement and verb 'be'.",
    idiom_present=False,
    risk_level="low"
))

# Sample 104: V5/G5 - Topic: Work (Salary)
samples.append(create_sample(
    index=104,
    vocab_band=5,
    grammar_band=5,
    question="Is salary the most important factor in a job?",
    transcript="Money is important but not everything. We need money for life. But if you hate your job, you will stress. Happiness is important too. Also colleague. Good friend at work make you happy. So I think salary is one factor, but environment is also important.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'money for life' -> 'money to live'",
        "word form: 'you will stress' -> 'you will be stressed'",
        "singular/plural: 'colleague' -> 'colleagues'",
        "verb agreement: 'Good friend... make' -> 'Good friends... make'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'stress', 'happiness', 'colleague', 'environment', 'factor'. >Band 4: Specific terms. Not Band 6: Lacks 'satisfaction', 'atmosphere', 'motivation'.",
    grammar_reason="[GRA5] Conditionals: 'if you hate your job...'. Comparison: 'not everything'. >Band 4: Complex sentences used correctly at times. Not Band 6: Word form errors (stress/stressed).",
    idiom_present=False,
    risk_level="low"
))

# Sample 105: V5/G5 - Topic: Society (Crime)
samples.append(create_sample(
    index=105,
    vocab_band=5,
    grammar_band=5,
    question="How can technology help reduce crime?",
    transcript="Camera is everywhere now. CCTV help police catch bad people. If criminal know camera is there, they scare. Also, computer analyze data. Find where crime happen. But privacy is problem. Some people not like camera. Government need balance safety and privacy.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'CCTV help' -> 'CCTV helps'",
        "verb agreement: 'criminal know' -> 'criminals know'",
        "adjective error: 'they scare' -> 'they are scared'",
        "verb agreement: 'crime happen' -> 'crime happens'",
        "verb construction: 'people not like' -> 'people do not like'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'CCTV', 'criminal', 'analyze', 'data', 'privacy', 'balance'. >Band 4: Good range. Not Band 6: Lacks 'surveillance', 'deterrent', 'identify', 'rights'.",
    grammar_reason="[GRA5] Conditionals: 'If criminal know...'. Contrast: 'But privacy is problem'. >Band 4: Uses connectors and complex forms. Not Band 6: Missing auxiliary verbs and agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 106: V5/G5 - Topic: Health (Fast Food)
samples.append(create_sample(
    index=106,
    vocab_band=5,
    grammar_band=5,
    question="Why is fast food so popular?",
    transcript="Because it is fast and cheap. People are busy with work. No time to cook. Fast food taste good. Have much sugar and fat. But it is unhealthy. If eat every day, people get fat. Obesity is big problem in many country.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Fast food taste' -> 'Fast food tastes'",
        "missing subject: 'Have much sugar' -> 'It has much sugar'",
        "conditional error: 'If eat every day' -> 'If people eat every day'",
        "singular/plural: 'many country' -> 'many countries'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'unhealthy', 'fat', 'sugar', 'obesity', 'popular'. >Band 4: Relevant vocabulary. Not Band 6: Lacks 'convenient', 'nutritious', 'calories', 'processed'.",
    grammar_reason="[GRA5] Conditionals: 'If eat every day...'. Causal: 'Because it is fast'. >Band 4: Structure variety. Not Band 6: Missing subjects and basic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 107: V5/G5 - Topic: Culture (Language)
samples.append(create_sample(
    index=107,
    vocab_band=5,
    grammar_band=5,
    question="Is it difficult to learn a foreign language?",
    transcript="Yes, grammar is hard. Vocabulary is many. You need practice every day. If you not speak, you forget. Learning method is important. Watch movie or listen music help. Some people have talent for language. But for me, it take long time.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Vocabulary is many' -> 'There is a lot of vocabulary'",
        "verb construction: 'need practice' -> 'need to practice'",
        "conditional error: 'If you not speak' -> 'If you do not speak'",
        "verb agreement: 'music help' -> 'music helps'",
        "verb agreement: 'it take' -> 'it takes'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'grammar', 'vocabulary', 'practice', 'method', 'talent'. >Band 4: Specific terms. Not Band 6: Lacks 'fluency', 'pronunciation', 'acquire', 'native speaker'.",
    grammar_reason="[GRA5] Conditionals: 'If you not speak...'. Gerunds: 'Learning method', 'Watch movie'. >Band 4: Complex attempts. Not Band 6: Negative formation errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 108: V5/G5 - Topic: Travel (Tourism)
samples.append(create_sample(
    index=108,
    vocab_band=5,
    grammar_band=5,
    question="What are the benefits of tourism for a country?",
    transcript="Tourism bring money. Hotel and restaurant make profit. Also create job for local people. Tourist buy souvenir. It help economy. But too many tourist is bad. Environment damage. Noise and trash. So government should manage tourism carefully.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Tourism bring' -> 'Tourism brings'",
        "verb agreement: 'restaurant make' -> 'restaurants make'",
        "verb agreement: 'It help' -> 'It helps'",
        "verb agreement: 'tourist is bad' -> 'tourists are bad'",
        "phrase error: 'Environment damage' -> 'Environmental damage' or 'Damage to the environment'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'profit', 'local people', 'souvenir', 'economy', 'damage', 'manage'. >Band 4: Good range. Not Band 6: Lacks 'revenue', 'infrastructure', 'preservation', 'industry'.",
    grammar_reason="[GRA5] Modals: 'should manage'. Contrast: 'But too many tourist is bad'. >Band 4: Logical connection. Not Band 6: Frequent agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 109: V5/G5 - Topic: Family (Elders)
samples.append(create_sample(
    index=109,
    vocab_band=5,
    grammar_band=5,
    question="Should young people look after old people?",
    transcript="Yes, it is responsibility. Parents take care us when small. So we take care them when old. In my country, family live together. But now, young people busy. Work in city. Old people lonely. Nursing home is option, but family is better.",
    response_type="extended",
    micro_flaws=[
        "missing preposition: 'take care us' -> 'take care of us'",
        "missing preposition: 'take care them' -> 'take care of them'",
        "verb agreement: 'family live' -> 'families live'",
        "missing verb: 'young people busy' -> 'young people are busy'",
        "missing verb: 'Old people lonely' -> 'Old people are lonely'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'responsibility', 'nursing home', 'lonely', 'option'. >Band 4: Relevant words. Not Band 6: Lacks 'obligation', 'support', 'generation gap', 'caregiver'.",
    grammar_reason="[GRA5] Comparison: 'Nursing home is option, but family is better'. Time clauses: 'when small', 'when old'. >Band 4: Structure variety. Not Band 6: Missing prepositions and verbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 110: V5/G5 - Topic: Media (News)
samples.append(create_sample(
    index=110,
    vocab_band=5,
    grammar_band=5,
    question="How do people get news today?",
    transcript="Most people use internet. Smartphone is convenient. Social media like Facebook. It is fast. But sometimes fake news. Not true information. Old people watch TV or read newspaper. Young people not like read. I think internet is main source now.",
    response_type="extended",
    micro_flaws=[
        "fragment: 'Social media like Facebook'",
        "fragment: 'But sometimes fake news'",
        "verb construction: 'not like read' -> 'do not like reading'",
        "missing article: 'read newspaper' -> 'read newspapers'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'social media', 'fake news', 'information', 'source', 'convenient'. >Band 4: Specific terms. Not Band 6: Lacks 'platform', 'unreliable', 'broadcast', 'update'.",
    grammar_reason="[GRA5] Contrast: 'But sometimes fake news'. Comparison: 'Old people... Young people...'. >Band 4: Clear structure. Not Band 6: Fragments and verb pattern errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 111: V5/G5 - Topic: Work (Retirement)
samples.append(create_sample(
    index=111,
    vocab_band=5,
    grammar_band=5,
    question="At what age should people retire?",
    transcript="I think 60 is good. People work long time. They tired. Need rest and enjoy life. Travel or hobby. But some people healthy. Want work more. If stop work, they boring. So government should let people choose. Flexible age is better.",
    response_type="extended",
    micro_flaws=[
        "missing verb: 'They tired' -> 'They are tired'",
        "verb construction: 'Want work more' -> 'Want to work more'",
        "adjective error: 'they boring' -> 'they are bored'",
        "fragment: 'Travel or hobby'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'retire', 'hobby', 'healthy', 'choose', 'flexible'. >Band 4: Relevant vocabulary. Not Band 6: Lacks 'pension', 'contribute', 'workforce', 'mandatory'.",
    grammar_reason="[GRA5] Conditionals: 'If stop work...'. Modals: 'Should let people choose'. >Band 4: Uses complex forms. Not Band 6: Adjective confusion (boring/bored) and missing verbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 112: V5/G5 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=112,
    vocab_band=5,
    grammar_band=5,
    question="Is recycling important?",
    transcript="Yes, very important. We produce trash every day. Plastic take long time to disappear. If we recycle, we save resource. Also save energy. But recycling process is expensive. People need separate trash. Paper, glass, plastic. Education is need to teach people.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Plastic take' -> 'Plastic takes'",
        "singular/plural: 'resource' -> 'resources'",
        "verb construction: 'Education is need' -> 'Education is needed'",
        "verb construction: 'People need separate' -> 'People need to separate'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'trash', 'produce', 'disappear', 'resource', 'process', 'separate'. >Band 4: Good range. Not Band 6: Lacks 'decompose', 'waste management', 'material', 'environment'.",
    grammar_reason="[GRA5] Conditionals: 'If we recycle...'. Passive attempt: 'Education is need'. >Band 4: Complex structures attempted. Not Band 6: Passive voice error.",
    idiom_present=False,
    risk_level="low"
))

# Sample 113: V5/G5 - Topic: Society (City Life)
samples.append(create_sample(
    index=113,
    vocab_band=5,
    grammar_band=5,
    question="What are the disadvantages of living in a city?",
    transcript="City is crowded. Too many people and car. Traffic jam is terrible. Waste time on road. Also air pollution. Smoke from vehicle. Housing is expensive. Rent high price. People stress. Countryside is quiet and clean. Better for health.",
    response_type="extended",
    micro_flaws=[
        "singular/plural: 'car' -> 'cars'",
        "singular/plural: 'vehicle' -> 'vehicles'",
        "phrase error: 'Rent high price' -> 'Rent is a high price' or 'Rent is high'",
        "word form: 'People stress' -> 'People are stressed'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'crowded', 'traffic jam', 'pollution', 'vehicle', 'housing', 'rent'. >Band 4: Specific terms. Not Band 6: Lacks 'congestion', 'urban', 'cost of living', 'resident'.",
    grammar_reason="[GRA5] Comparison implied. Reason: 'Smoke from vehicle'. >Band 4: Logical flow. Not Band 6: Word form errors (stress/stressed) and plurals.",
    idiom_present=False,
    risk_level="low"
))

# Sample 114: V5/G5 - Topic: Technology (Games)
samples.append(create_sample(
    index=114,
    vocab_band=5,
    grammar_band=5,
    question="Are video games bad for children?",
    transcript="Not always bad. Game can teach skill. Problem solving and reaction. But too much is bad. Addiction happen. Children not do homework. Eye problem. Violence game make child aggressive. Parents must control time. 1 hour per day is enough.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Game can teach' -> 'Games can teach'",
        "verb agreement: 'Addiction happen' -> 'Addiction happens'",
        "phrase error: 'Violence game' -> 'Violent games'",
        "verb agreement: 'make child aggressive' -> 'make children aggressive'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'skill', 'problem solving', 'addiction', 'violence', 'aggressive', 'reaction'. >Band 4: Good range. Not Band 6: Lacks 'cognitive', 'strategy', 'behavior', 'supervise'.",
    grammar_reason="[GRA5] Contrast: 'But too much is bad'. Modals: 'Parents must control'. >Band 4: Variety of structures. Not Band 6: Adjective/Noun confusion (Violence/Violent).",
    idiom_present=False,
    risk_level="low"
))

# Sample 115: V5/G5 - Topic: Work (Gender)
samples.append(create_sample(
    index=115,
    vocab_band=5,
    grammar_band=5,
    question="Why are there fewer women in some professions?",
    transcript="Maybe tradition. In past, women stay home. Cook and clean. Men work outside. Now change, but slow. Some job like engineer, mostly men. People think heavy work is for men. But women is smart. Can do anything. Education encourage girl now.",
    response_type="extended",
    micro_flaws=[
        "verb tense: 'women stay home' -> 'women stayed home'",
        "verb tense: 'Men work outside' -> 'Men worked outside'",
        "verb agreement: 'women is smart' -> 'women are smart'",
        "verb agreement: 'Education encourage' -> 'Education encourages'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'tradition', 'profession', 'engineer', 'heavy work', 'encourage'. >Band 4: Relevant vocabulary. Not Band 6: Lacks 'stereotype', 'gender role', 'male-dominated', 'opportunity'.",
    grammar_reason="[GRA5] Comparison: 'In past... Now...'. Contrast: 'But women is smart'. >Band 4: Complex time comparisons. Not Band 6: Tense consistency errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 116: V5/G5 - Topic: Education (Online)
samples.append(create_sample(
    index=116,
    vocab_band=5,
    grammar_band=5,
    question="What are the advantages of online learning?",
    transcript="It is convenient. Study anywhere. Home or cafe. Save time travel. Also cheap. Course on internet is free sometimes. You can replay video. Understand better. But self-discipline is hard. No teacher push you. Some student lazy and stop.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Save time travel' -> 'Save travel time' or 'Save time traveling'",
        "fragment: 'Home or cafe'",
        "missing verb: 'Some student lazy' -> 'Some students are lazy'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'convenient', 'replay', 'self-discipline', 'course', 'cheap'. >Band 4: Specific terms. Not Band 6: Lacks 'flexible', 'accessible', 'interaction', 'motivate'.",
    grammar_reason="[GRA5] Contrast: 'But self-discipline is hard'. Reason: 'No teacher push you'. >Band 4: Logical connectors. Not Band 6: Fragments and phrase errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 117: V5/G5 - Topic: Society (History)
samples.append(create_sample(
    index=117,
    vocab_band=5,
    grammar_band=5,
    question="Why is it important to learn history?",
    transcript="History teach us mistake. We not repeat bad thing. War or disaster. Also know our culture. Where we come from. Hero in past. I think history is boring in school. Memorize date. But actually interesting. Visit museum is good way to learn.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'History teach' -> 'History teaches'",
        "verb construction: 'We not repeat' -> 'We do not repeat'",
        "fragment: 'Hero in past'",
        "verb construction: 'Memorize date' -> 'Memorizing dates'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'mistake', 'repeat', 'war', 'culture', 'hero', 'memorize'. >Band 4: Relevant terms. Not Band 6: Lacks 'avoid', 'ancestors', 'heritage', 'identity'.",
    grammar_reason="[GRA5] Purpose: 'We not repeat bad thing'. Contrast: 'But actually interesting'. >Band 4: Complex ideas. Not Band 6: Missing auxiliary verbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 118: V5/G5 - Topic: Transport (Cars)
samples.append(create_sample(
    index=118,
    vocab_band=5,
    grammar_band=5,
    question="Why do people prefer private cars?",
    transcript="Car is comfortable. Personal space. You can go any time. Not wait bus. Listen music. AC is good. Public transport is crowded. Dirty and smell. But car is expensive. Gas and insurance. Traffic jam is stressful. But still people like car.",
    response_type="extended",
    micro_flaws=[
        "verb construction: 'Not wait bus' -> 'Do not have to wait for the bus'",
        "phrase error: 'Dirty and smell' -> 'Dirty and smelly'",
        "fragment: 'Gas and insurance'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'comfortable', 'personal space', 'crowded', 'insurance', 'stressful'. >Band 4: Good range. Not Band 6: Lacks 'convenience', 'freedom', 'maintenance', 'pollution'.",
    grammar_reason="[GRA5] Comparison implied. Contrast: 'But car is expensive'. >Band 4: Logical flow. Not Band 6: Adjective/verb confusion (smell/smelly).",
    idiom_present=False,
    risk_level="low"
))

# Sample 119: V5/G5 - Topic: Environment (Global Warming)
samples.append(create_sample(
    index=119,
    vocab_band=5,
    grammar_band=5,
    question="What causes global warming?",
    transcript="Main cause is greenhouse gas. CO2 from car and factory. Burning coal and oil. Also deforestation. Cut tree in forest. Earth become hot. Ice melt. Sea level rise. Weather change crazy. Storm and flood. Human activity is reason.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Earth become hot' -> 'Earth becomes hot'",
        "verb agreement: 'Ice melt' -> 'Ice melts'",
        "verb agreement: 'Weather change' -> 'Weather changes'",
        "adjective error: 'Weather change crazy' -> 'Weather changes crazily' or 'is crazy'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'greenhouse gas', 'coal', 'oil', 'deforestation', 'flood', 'human activity'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'fossil fuels', 'atmosphere', 'consequence', 'emission'.",
    grammar_reason="[GRA5] Cause and Effect structure. 'Earth become hot'. 'Ice melt'. >Band 4: Logical sequence. Not Band 6: Subject-verb agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 120: V5/G5 - Topic: Health (Children)
samples.append(create_sample(
    index=120,
    vocab_band=5,
    grammar_band=5,
    question="Why are children less healthy today?",
    transcript="They eat bad food. Junk food like burger and chips. Sweet drink. Also not exercise. Play video game inside. Not go outside. Technology make them lazy. In past, children play sport. Run in park. Now obesity is problem. Parents should cook healthy.",
    response_type="extended",
    micro_flaws=[
        "fragment: 'Sweet drink'",
        "verb construction: 'Not exercise' -> 'Do not exercise'",
        "verb agreement: 'Technology make' -> 'Technology makes'",
        "verb tense: 'In past, children play' -> 'In the past, children played'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'junk food', 'exercise', 'lazy', 'obesity', 'technology'. >Band 4: Relevant terms. Not Band 6: Lacks 'sedentary', 'diet', 'nutrition', 'lifestyle'.",
    grammar_reason="[GRA5] Comparison: 'In past... Now...'. Modals: 'Parents should cook'. >Band 4: Complex time comparison. Not Band 6: Tense errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 121: V5/G5 - Topic: Society (Advertising)
samples.append(create_sample(
    index=121,
    vocab_band=5,
    grammar_band=5,
    question="Does advertising have a bad influence on children?",
    transcript="Yes, children believe everything. Ad show toy or candy. Make it look perfect. Child want it. Ask parents buy. If parents say no, child cry. Advertising manipulate mind. Create desire. Government should ban ad for kids. It is unethical.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Ad show' -> 'Ads show'",
        "verb agreement: 'Child want' -> 'The child wants'",
        "verb construction: 'Ask parents buy' -> 'Ask parents to buy'",
        "phrase error: 'ban ad' -> 'ban ads'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'influence', 'perfect', 'desire', 'manipulate', 'unethical', 'ban'. >Band 4: Good range. Not Band 6: Lacks 'persuade', 'consumer', 'commercial', 'impact'.",
    grammar_reason="[GRA5] Conditionals: 'If parents say no...'. Modals: 'Should ban'. >Band 4: Uses complex structures. Not Band 6: Agreement and infinitive errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 122: V5/G5 - Topic: Work (Teamwork)
samples.append(create_sample(
    index=122,
    vocab_band=5,
    grammar_band=5,
    question="Is teamwork important in the workplace?",
    transcript="Yes, very important. One person cannot do big project. Need help. Teamwork share idea. Solve problem fast. Support each other. If work alone, maybe mistake happen. Stressful. But teamwork need good leader. Sometimes conflict happen. Need compromise.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Teamwork share' -> 'The team shares' or 'Teamwork involves sharing'",
        "verb agreement: 'mistake happen' -> 'mistakes happen'",
        "fragment: 'Stressful'",
        "verb agreement: 'conflict happen' -> 'conflicts happen'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'project', 'support', 'mistake', 'conflict', 'compromise', 'leader'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'collaborate', 'efficiency', 'diverse', 'resolution'.",
    grammar_reason="[GRA5] Conditionals: 'If work alone...'. Contrast: 'But teamwork need...'. >Band 4: Logical flow. Not Band 6: Subject-verb agreement.",
    idiom_present=False,
    risk_level="low"
))

# Sample 123: V5/G5 - Topic: Culture (Globalization)
samples.append(create_sample(
    index=123,
    vocab_band=5,
    grammar_band=5,
    question="Does globalization mean we are losing our local culture?",
    transcript="A little bit yes. Western culture is strong. Hollywood movie and music. Young people like American style. Fast food. English language. Local tradition become weak. Wear jean not traditional cloth. But we can keep both. Celebrate festival. Teach history. Balance is key.",
    response_type="extended",
    micro_flaws=[
        "fragment: 'Hollywood movie and music'",
        "verb agreement: 'tradition become' -> 'traditions become'",
        "verb construction: 'Wear jean' -> 'They wear jeans'",
        "singular/plural: 'cloth' -> 'clothes'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'western', 'style', 'traditional', 'festival', 'balance', 'weak'. >Band 4: Relevant terms. Not Band 6: Lacks 'dominate', 'preserve', 'identity', 'integration'.",
    grammar_reason="[GRA5] Contrast: 'But we can keep both'. List: 'Celebration festival. Teach history'. >Band 4: Coherent. Not Band 6: Fragments and agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 124: V5/G5 - Topic: Technology (Communication)
samples.append(create_sample(
    index=124,
    vocab_band=5,
    grammar_band=5,
    question="Has technology improved communication?",
    transcript="Yes, it improve a lot. We can talk to anyone anywhere. Video call is great. See face. Email is fast for work. No need write letter. Wait long time. But negative side too. People text, not talk. Face-to-face is important. Feeling is lost in text.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'it improve' -> 'it improves' or 'has improved'",
        "verb construction: 'No need write' -> 'No need to write'",
        "fragment: 'Wait long time'",
        "verb agreement: 'Feeling is lost' -> 'Feelings are lost'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'video call', 'email', 'negative side', 'text', 'face-to-face', 'feeling'. >Band 4: Good range. Not Band 6: Lacks 'instant', 'connect', 'relationship', 'emotion'.",
    grammar_reason="[GRA5] Contrast: 'But negative side too'. Comparison implied. >Band 4: Structure variety. Not Band 6: Basic verb errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 125: V5/G5 - Topic: Society (Shopping)
samples.append(create_sample(
    index=125,
    vocab_band=5,
    grammar_band=5,
    question="Why is online shopping so popular?",
    transcript="It is convenient. You can buy at home. 24 hour open. Compare price easy. Cheaper than shop. Delivery to door. But problem is size. Cannot try on. Maybe material is bad. Return is difficult. I still like shop in mall. Can touch product.",
    response_type="extended",
    micro_flaws=[
        "phrase error: '24 hour open' -> 'Open 24 hours'",
        "phrase error: 'Compare price easy' -> 'Comparing prices is easy'",
        "fragment: 'Cheaper than shop'",
        "fragment: 'Delivery to door'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'compare', 'delivery', 'size', 'material', 'return', 'product'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'variety', 'quality', 'browse', 'experience'.",
    grammar_reason="[GRA5] Contrast: 'But problem is size'. Reason: 'It is convenient'. >Band 4: Logical connectors. Not Band 6: Fragments and phrase structure errors.",
    idiom_present=False,
    risk_level="low"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
