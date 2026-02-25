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

# --- BATCH 02 PART 4: SAMPLES 126-150 (25 Total) ---
# Combo: V5/G5

# Sample 126: V5/G5 - Topic: Health (Sleep)
samples.append(create_sample(
    index=126,
    vocab_band=5,
    grammar_band=5,
    question="Why is sleep important for health?",
    transcript="Sleep helps body recover. If not sleep enough, you tired. Brain not work good. Cannot focus study or work. Immune system become weak. Easy get sick. People need 8 hour sleep. Avoid phone before bed. Relax is important.",
    response_type="extended",
    micro_flaws=[
        "verb construction: 'helps body recover' -> 'helps the body to recover'",
        "conditional error: 'If not sleep enough' -> 'If you do not sleep enough'",
        "verb agreement: 'Brain not work' -> 'The brain does not work'",
        "verb agreement: 'Immune system become' -> 'The immune system becomes'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'recover', 'immune system', 'focus', 'weak', 'relax'. >Band 4: Relevant terms. Not Band 6: Lacks 'regenerate', 'cognitive', 'deprivation', 'insomnia'.",
    grammar_reason="[GRA5] Conditionals: 'If not sleep enough...'. Reason: 'Sleep helps...'. >Band 4: Logical structure. Not Band 6: Missing articles and auxiliary verbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 127: V5/G5 - Topic: Environment (Renewable Energy)
samples.append(create_sample(
    index=127,
    vocab_band=5,
    grammar_band=5,
    question="Why should countries use renewable energy?",
    transcript="Fossil fuel is dirty. Coal and oil cause pollution. Renewable energy is clean. Solar and wind power. It is infinite. Not run out. Protect environment. Reduce global warming. It is expensive to build, but cheap to run. Good for future.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Fossil fuel is' -> 'Fossil fuels are'",
        "verb construction: 'Not run out' -> 'It does not run out'",
        "verb construction: 'Protect environment' -> 'It protects the environment'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'fossil fuel', 'coal', 'solar', 'wind', 'infinite', 'global warming'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'sustainable', 'emission', 'investment', 'alternative'.",
    grammar_reason="[GRA5] Contrast: 'But cheap to run'. Reason: 'Fossil fuel is dirty'. >Band 4: Coherent. Not Band 6: Fragments and verb agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 128: V5/G5 - Topic: Work (Job Security)
samples.append(create_sample(
    index=128,
    vocab_band=5,
    grammar_band=5,
    question="Is job security important to employees?",
    transcript="Yes, very important. People worry about money. Need pay bill and rent. If lose job, big problem. Stable job make you relax. Can plan future. Buy house or car. Freelance is popular but risky. No guarantee income. Security is better.",
    response_type="extended",
    micro_flaws=[
        "verb construction: 'Need pay bill' -> 'Need to pay bills'",
        "conditional error: 'If lose job' -> 'If you lose your job'",
        "verb agreement: 'Stable job make' -> 'A stable job makes'",
        "phrase error: 'No guarantee income' -> 'No guaranteed income'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'bill', 'rent', 'stable', 'freelance', 'risky', 'guarantee'. >Band 4: Good range. Not Band 6: Lacks 'financial', 'uncertainty', 'contract', 'permanent'.",
    grammar_reason="[GRA5] Conditionals: 'If lose job...'. Contrast: 'Freelance is popular but risky'. >Band 4: Complex ideas. Not Band 6: Missing subjects and verbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 129: V5/G5 - Topic: Society (Volunteer)
samples.append(create_sample(
    index=129,
    vocab_band=5,
    grammar_band=5,
    question="What are the benefits of volunteering?",
    transcript="Helping other people make you happy. You feel useful. Meet new friend. Learn skill. It is good for CV. Experience is important. Also community become strong. Reduce problem. Young people should try. Not always about money.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Helping... make' -> 'Helping... makes'",
        "singular/plural: 'friend' -> 'friends'",
        "singular/plural: 'skill' -> 'skills'",
        "verb agreement: 'community become' -> 'the community becomes'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'useful', 'CV', 'community', 'experience', 'skill'. >Band 4: Relevant terms. Not Band 6: Lacks 'charity', 'contribute', 'social', 'generosity'.",
    grammar_reason="[GRA5] Gerund subject: 'Helping other people make you happy'. Modals: 'Should try'. >Band 4: Varied structures. Not Band 6: Agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 130: V5/G5 - Topic: Technology (Art)
samples.append(create_sample(
    index=130,
    vocab_band=5,
    grammar_band=5,
    question="Can computers create art?",
    transcript="Yes, AI can draw picture. Write poem too. It is amazing. But is it real art? Computer just copy data. No emotion. No soul. Human art express feeling. Unique style. Computer is tool. Maybe help artist, but not replace artist.",
    response_type="extended",
    micro_flaws=[
        "singular/plural: 'draw picture' -> 'draw pictures'",
        "phrase error: 'But is it real art?' (question word order correct)",
        "verb agreement: 'Human art express' -> 'Human art expresses'",
        "phrase error: 'Not replace artist' -> 'It cannot replace the artist'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'poem', 'amazing', 'copy', 'data', 'soul', 'unique'. >Band 4: Good vocabulary. Not Band 6: Lacks 'creativity', 'originality', 'inspiration', 'masterpiece'.",
    grammar_reason="[GRA5] Contrast: 'But not replace artist'. Comparison implied. >Band 4: Coherent. Not Band 6: Fragments and agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 131: V5/G5 - Topic: Education (Music)
samples.append(create_sample(
    index=131,
    vocab_band=5,
    grammar_band=5,
    question="Should music be taught in schools?",
    transcript="Yes, music is good for brain. Relax student. Study math and science is stressful. Music class is fun. Creative thinking. Also learn teamwork. Play in band. Some student have talent. School should support them. Not waste talent.",
    response_type="extended",
    micro_flaws=[
        "verb construction: 'Relax student' -> 'It relaxes students'",
        "gerund error: 'Study math... is stressful' -> 'Studying math... is stressful'",
        "verb agreement: 'Some student have' -> 'Some students have'",
        "verb construction: 'Not waste talent' -> 'Do not waste talent'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'relax', 'stressful', 'creative', 'band', 'talent', 'support'. >Band 4: Relevant terms. Not Band 6: Lacks 'curriculum', 'instrument', 'expression', 'academic'.",
    grammar_reason="[GRA5] Reason: 'Music is good for brain'. Modals: 'School should support'. >Band 4: Logical flow. Not Band 6: Gerund errors and missing verbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 132: V5/G5 - Topic: Transport (Bicycles)
samples.append(create_sample(
    index=132,
    vocab_band=5,
    grammar_band=5,
    question="How can we encourage people to cycle more?",
    transcript="Build safe lane. Many people afraid car. If road is safe, they cycle. Also bike sharing system. Rent bike cheap. Place near station. Good for health and environment. Government can give reward. Tax reduce for cyclist. Make it popular.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'afraid car' -> 'afraid of cars'",
        "conditional error: 'If road is safe' -> 'If the road is safe'",
        "verb construction: 'Rent bike cheap' -> 'Rent bikes cheaply'",
        "phrase error: 'Tax reduce' -> 'Tax reduction' or 'Reduce tax'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'lane', 'sharing system', 'rent', 'station', 'reward', 'tax'. >Band 4: Specific terms. Not Band 6: Lacks 'infrastructure', 'promote', 'traffic', 'incentive'.",
    grammar_reason="[GRA5] Conditionals: 'If road is safe...'. Modals: 'Can give reward'. >Band 4: Complex structures attempted. Not Band 6: Preposition and phrase errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 133: V5/G5 - Topic: Society (Happiness)
samples.append(create_sample(
    index=133,
    vocab_band=5,
    grammar_band=5,
    question="What makes people happy?",
    transcript="Different for everyone. Some like money. Buy expensive thing. Some like family. Spend time together. Health is important too. If sick, not happy. Freedom to do what you want. Travel world. Simple life is best for me. No stress.",
    response_type="extended",
    micro_flaws=[
        "fragment: 'Different for everyone'",
        "singular/plural: 'expensive thing' -> 'expensive things'",
        "conditional error: 'If sick, not happy' -> 'If you are sick, you are not happy'",
        "fragment: 'Travel world' -> 'Traveling the world'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'expensive', 'spend time', 'freedom', 'simple life', 'stress'. >Band 4: Good range. Not Band 6: Lacks 'contentment', 'fulfillment', 'relationship', 'material'.",
    grammar_reason="[GRA5] Comparison implied. Conditionals: 'If sick, not happy'. >Band 4: Logical structure. Not Band 6: Fragments and missing verbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 134: V5/G5 - Topic: Work (Robots)
samples.append(create_sample(
    index=134,
    vocab_band=5,
    grammar_band=5,
    question="Will we work fewer hours in the future?",
    transcript="Maybe yes. Robot do hard work. Computer do calculation. Human only supervise. So we have free time. Work 4 day a week. Enjoy life. But maybe pay is less. If work less, earn less. Companies want profit. So it is not sure.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Robot do' -> 'Robots do'",
        "verb agreement: 'Computer do' -> 'Computers do'",
        "phrase error: 'Work 4 day' -> 'Work 4 days'",
        "conditional error: 'If work less' -> 'If we work less'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'calculation', 'supervise', 'profit', 'earn', 'sure'. >Band 4: Relevant vocabulary. Not Band 6: Lacks 'efficiency', 'productivity', 'leisure', 'salary'.",
    grammar_reason="[GRA5] Cause and Effect: 'So we have free time'. Conditionals: 'If work less...'. >Band 4: Connectors used well. Not Band 6: Subject-verb agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 135: V5/G5 - Topic: Culture (Food)
samples.append(create_sample(
    index=135,
    vocab_band=5,
    grammar_band=5,
    question="Why is trying traditional food important for tourists?",
    transcript="Food is part of culture. Taste tell history. Ingredients from local area. If you eat local food, you understand people. Connect with them. International food is boring. Same everywhere. Trying new flavor is adventure. Good memory for trip.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Taste tell' -> 'Taste tells'",
        "fragment: 'Ingredients from local area'",
        "phrase error: 'International food is boring' (ok)",
        "fragment: 'Same everywhere'",
        "fragment: 'Good memory for trip'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'ingredient', 'local area', 'flavor', 'adventure', 'memory'. >Band 4: Specific terms. Not Band 6: Lacks 'cuisine', 'authentic', 'culinary', 'experience'.",
    grammar_reason="[GRA5] Conditionals: 'If you eat local food...'. Contrast: 'International food is boring'. >Band 4: Logical flow. Not Band 6: Fragments and agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 136: V5/G5 - Topic: Technology (Space)
samples.append(create_sample(
    index=136,
    vocab_band=5,
    grammar_band=5,
    question="Should governments spend money on finding life on other planets?",
    transcript="It is exciting idea. Are we alone? But Earth have many problem. Poverty and disease. We need fix here first. Space travel is very expensive. Waste of resource. Maybe in future, when we rich. But now, help poor people is better.",
    response_type="extended",
    micro_flaws=[
        "missing article: 'exciting idea' -> 'an exciting idea'",
        "verb agreement: 'Earth have' -> 'Earth has'",
        "singular/plural: 'many problem' -> 'many problems'",
        "verb construction: 'need fix' -> 'need to fix'",
        "phrase error: 'when we rich' -> 'when we are rich'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'alone', 'poverty', 'disease', 'resource', 'expensive'. >Band 4: Relevant terms. Not Band 6: Lacks 'extraterrestrial', 'exploration', 'priority', 'investment'.",
    grammar_reason="[GRA5] Contrast: 'But Earth have many problem'. Comparison: 'Help poor people is better'. >Band 4: Clear structure. Not Band 6: Missing verbs and agreement.",
    idiom_present=False,
    risk_level="low"
))

# Sample 137: V5/G5 - Topic: Education (Reading)
samples.append(create_sample(
    index=137,
    vocab_band=5,
    grammar_band=5,
    question="How can we encourage children to read more?",
    transcript="Parents should read to child. Bedtime story. Make it habit. School should have good library. Interesting book. Not just textbook. Also limit TV and game. If child bore, they read. Reading is fun if book is good. Imagination grow.",
    response_type="extended",
    micro_flaws=[
        "fragment: 'Bedtime story'",
        "verb construction: 'Make it habit' -> 'Make it a habit'",
        "singular/plural: 'Interesting book' -> 'Interesting books'",
        "adjective error: 'If child bore' -> 'If the child is bored'",
        "verb agreement: 'Imagination grow' -> 'Imagination grows'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'habit', 'library', 'textbook', 'limit', 'imagination'. >Band 4: Good range. Not Band 6: Lacks 'literacy', 'engage', 'fiction', 'vocabulary'.",
    grammar_reason="[GRA5] Conditionals: 'If child bore...'. Modals: 'Parents should read'. >Band 4: Complex structures attempted. Not Band 6: Adjective/verb confusion.",
    idiom_present=False,
    risk_level="low"
))

# Sample 138: V5/G5 - Topic: Environment (Plastic)
samples.append(create_sample(
    index=138,
    vocab_band=5,
    grammar_band=5,
    question="Why is plastic pollution a problem?",
    transcript="Plastic is everywhere. Ocean and land. Animal eat it and die. It not disappear. Stay forever. Microplastic in water. We drink it. Bad for health. We use too much plastic bag and bottle. Need stop. Use paper or glass instead.",
    response_type="extended",
    micro_flaws=[
        "fragment: 'Ocean and land'",
        "verb agreement: 'Animal eat' -> 'Animals eat'",
        "verb construction: 'It not disappear' -> 'It does not disappear'",
        "fragment: 'Bad for health'",
        "verb construction: 'Need stop' -> 'Need to stop'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'ocean', 'disappear', 'microplastic', 'health', 'instead'. >Band 4: Specific terms. Not Band 6: Lacks 'biodegradable', 'toxic', 'consumption', 'recycle'.",
    grammar_reason="[GRA5] Cause and Effect: 'Animal eat it and die'. List: 'Paper, glass...'. >Band 4: Coherent. Not Band 6: Negative formation errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 139: V5/G5 - Topic: Society (Celebrities)
samples.append(create_sample(
    index=139,
    vocab_band=5,
    grammar_band=5,
    question="Why are people interested in the lives of celebrities?",
    transcript="Celebrity life is glamorous. Rich and famous. Beautiful clothes and house. People want escape reality. Dream about that life. Also gossip is fun. Talk with friend. Media show them everyday. We feel we know them. But it is fake image.",
    response_type="extended",
    micro_flaws=[
        "fragment: 'Rich and famous'",
        "fragment: 'Beautiful clothes and house'",
        "verb construction: 'want escape' -> 'want to escape'",
        "fragment: 'Talk with friend'",
        "phrase error: 'everyday' (adjective) -> 'every day' (adverb)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'glamorous', 'reality', 'dream', 'gossip', 'image'. >Band 4: Good range. Not Band 6: Lacks 'fascination', 'lifestyle', 'privacy', 'idol'.",
    grammar_reason="[GRA5] Reason: 'People want escape'. Contrast: 'But it is fake image'. >Band 4: Logical flow. Not Band 6: Fragments and missing verbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 140: V5/G5 - Topic: Transport (Traffic)
samples.append(create_sample(
    index=140,
    vocab_band=5,
    grammar_band=5,
    question="What problems does traffic congestion cause?",
    transcript="First is time. We waste time in car. Late for work. Second is stress. Driver get angry. Road rage. Third is pollution. Car engine run but not move. Smoke go in air. Bad for lung. City become noisy and ugly.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Driver get' -> 'Drivers get'",
        "verb agreement: 'engine run' -> 'engines run'",
        "verb agreement: 'Smoke go' -> 'Smoke goes'",
        "singular/plural: 'lung' -> 'lungs'",
        "verb agreement: 'City become' -> 'The city becomes'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'waste time', 'stress', 'road rage', 'engine', 'lung', 'ugly'. >Band 4: Specific terms. Not Band 6: Lacks 'productivity', 'frustration', 'exhaust fumes', 'environment'.",
    grammar_reason="[GRA5] Sequencing: 'First... Second... Third...'. >Band 4: Clear structure. Not Band 6: Subject-verb agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 141: V5/G5 - Topic: Work (Environment)
samples.append(create_sample(
    index=141,
    vocab_band=5,
    grammar_band=5,
    question="What makes a good working environment?",
    transcript="Friendly people is number one. If colleague help you, you happy. Boss should be nice. Not shout. Clean office. Good computer. Also salary. But atmosphere is key. If stress high, people quit. Teamwork make work easy. Fun place is best.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Friendly people is' -> 'Friendly people are'",
        "conditional error: 'If colleague help you, you happy' -> 'If colleagues help you, you are happy'",
        "fragment: 'Clean office'",
        "fragment: 'Also salary'",
        "verb agreement: 'Teamwork make' -> 'Teamwork makes'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'colleague', 'boss', 'atmosphere', 'quit', 'teamwork'. >Band 4: Relevant terms. Not Band 6: Lacks 'supportive', 'facility', 'morale', 'productive'.",
    grammar_reason="[GRA5] Conditionals: 'If colleague help you...'. Modals: 'Boss should be nice'. >Band 4: Complex structures attempted. Not Band 6: Agreement and verb 'be' errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 142: V5/G5 - Topic: Technology (AI)
samples.append(create_sample(
    index=142,
    vocab_band=5,
    grammar_band=5,
    question="Is artificial intelligence dangerous?",
    transcript="Maybe in future. Now it is helpful. Search engine and phone. But if AI become smart than human, problem. It can control us. Robot war. Also job loss. AI do work cheap. People have no money. We need rule to control AI.",
    response_type="extended",
    micro_flaws=[
        "fragment: 'Search engine and phone'",
        "comparison error: 'smart than' -> 'smarter than'",
        "fragment: 'Robot war'",
        "phrase error: 'AI do work cheap' -> 'AI does work cheaply'",
        "phrase error: 'rule to control' -> 'rules to control'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'search engine', 'control', 'war', 'job loss', 'rule'. >Band 4: Good range. Not Band 6: Lacks 'superior', 'threat', 'regulate', 'ethics'.",
    grammar_reason="[GRA5] Conditionals: 'If AI become...'. Contrast: 'But if...'. >Band 4: Uses connectors. Not Band 6: Comparison and agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 143: V5/G5 - Topic: Culture (Museums)
samples.append(create_sample(
    index=143,
    vocab_band=5,
    grammar_band=5,
    question="Should museums be free?",
    transcript="Yes, education for everyone. Poor people can visit. Learn history and art. If ticket expensive, only rich go. Museum is public place. Tax money pay for it. But museum need money for maintain. Cleaning and staff. Maybe donation is better way.",
    response_type="extended",
    micro_flaws=[
        "fragment: 'Learn history and art'",
        "conditional error: 'If ticket expensive' -> 'If the ticket is expensive'",
        "fragment: 'Tax money pay for it' -> 'Tax money pays for it'",
        "verb construction: 'need money for maintain' -> 'needs money for maintenance'",
        "fragment: 'Cleaning and staff'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'public place', 'tax', 'maintain', 'staff', 'donation'. >Band 4: Relevant terms. Not Band 6: Lacks 'accessible', 'funding', 'operate', 'admission'.",
    grammar_reason="[GRA5] Conditionals: 'If ticket expensive...'. Contrast: 'But museum need money'. >Band 4: Logical flow. Not Band 6: Missing verbs and word form errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 144: V5/G5 - Topic: Health (Sport)
samples.append(create_sample(
    index=144,
    vocab_band=5,
    grammar_band=5,
    question="Why are team sports good for children?",
    transcript="Learn to work with other. Cooperation. Not selfish. Also make friend. Fun to play together. Learn to win and lose. Respect rule. Physical health too. Run and jump. Strong body. Computer game is bad. Sport is better for character.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'work with other' -> 'work with others'",
        "fragment: 'Cooperation'",
        "fragment: 'Not selfish'",
        "fragment: 'Respect rule' -> 'Respect rules'",
        "fragment: 'Run and jump'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'cooperation', 'selfish', 'rule', 'physical', 'character'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'social skills', 'discipline', 'competition', 'sportsmanship'.",
    grammar_reason="[GRA5] Comparison: 'Sport is better'. Reason: 'Fun to play'. >Band 4: Clear ideas. Not Band 6: Heavy reliance on fragments.",
    idiom_present=False,
    risk_level="low"
))

# Sample 145: V5/G5 - Topic: Society (City)
samples.append(create_sample(
    index=145,
    vocab_band=5,
    grammar_band=5,
    question="How can we solve housing problems in cities?",
    transcript="Build more apartment. High building. Save space. Government should build cheap house. For poor people. Also improve transport. People can live far and travel. Work in city, live in village. Rent control is idea. Landlord cannot increase price too much.",
    response_type="extended",
    micro_flaws=[
        "singular/plural: 'apartment' -> 'apartments'",
        "fragment: 'High building'",
        "phrase error: 'cheap house' -> 'cheap houses'",
        "phrase error: 'Rent control is idea' -> 'Rent control is an idea'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'apartment', 'transport', 'village', 'rent control', 'landlord'. >Band 4: Good range. Not Band 6: Lacks 'skyscraper', 'suburb', 'commute', 'affordable'.",
    grammar_reason="[GRA5] Modals: 'Should build'. Solution structure. >Band 4: Logical. Not Band 6: Fragments and article errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 146: V5/G5 - Topic: Education (Science)
samples.append(create_sample(
    index=146,
    vocab_band=5,
    grammar_band=5,
    question="Is science the most important subject in school?",
    transcript="Science is important. Understand world. Technology come from science. But art and language also important. Creativity and communication. We need balance. If everyone is scientist, boring world. We need artist and writer too. Education should wide. Not just one subject.",
    response_type="extended",
    micro_flaws=[
        "missing article: 'Understand world' -> 'Understand the world'",
        "verb agreement: 'Technology come' -> 'Technology comes'",
        "fragment: 'Creativity and communication'",
        "fragment: 'Boring world'",
        "phrase error: 'Education should wide' -> 'Education should be wide/broad'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'technology', 'creativity', 'communication', 'scientist', 'artist'. >Band 4: Relevant terms. Not Band 6: Lacks 'innovation', 'humanities', 'curriculum', 'perspective'.",
    grammar_reason="[GRA5] Contrast: 'But art...'. Conditionals: 'If everyone is scientist...'. >Band 4: Complex structures attempted. Not Band 6: Missing verbs and articles.",
    idiom_present=False,
    risk_level="low"
))

# Sample 147: V5/G5 - Topic: Environment (Animals)
samples.append(create_sample(
    index=147,
    vocab_band=5,
    grammar_band=5,
    question="Why should we protect endangered species?",
    transcript="Every animal have purpose. Ecosystem balance. If one animal die, other affect. Tiger or whale. They are beautiful. Future generation should see them. If we kill all, we alone. Nature is connect. Protect animal is protect us.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'animal have' -> 'animal has'",
        "fragment: 'Ecosystem balance'",
        "verb construction: 'other affect' -> 'others are affected'",
        "conditional error: 'If we kill all' -> 'If we kill them all'",
        "verb construction: 'Nature is connect' -> 'Nature is connected'",
        "phrase error: 'Protect animal is protect us' -> 'Protecting animals is protecting us'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'purpose', 'balance', 'generation', 'nature', 'connect'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'biodiversity', 'extinction', 'chain reaction', 'habitat'.",
    grammar_reason="[GRA5] Conditionals: 'If one animal die...'. Reason: 'Nature is connect'. >Band 4: Clear reasoning. Not Band 6: Passive voice and gerund errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 148: V5/G5 - Topic: Technology (Internet)
samples.append(create_sample(
    index=148,
    vocab_band=5,
    grammar_band=5,
    question="How has the internet changed the way we work?",
    transcript="Work is faster now. Email and chat. Send file easy. Also work from home. Remote work. No need office. Save money. But work time is long. Boss call anytime. Cannot relax. Internet make work stress. Always online.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Send file easy' -> 'Sending files is easy'",
        "fragment: 'Remote work'",
        "fragment: 'No need office'",
        "verb agreement: 'Internet make' -> 'Internet makes'",
        "fragment: 'Always online'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'file', 'remote work', 'office', 'relax', 'stress', 'online'. >Band 4: Relevant terms. Not Band 6: Lacks 'efficiency', 'collaboration', 'boundary', 'flexible'.",
    grammar_reason="[GRA5] Contrast: 'But work time is long'. Comparison: 'Faster now'. >Band 4: Logical. Not Band 6: Fragments and agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 149: V5/G5 - Topic: Culture (Festivals)
samples.append(create_sample(
    index=149,
    vocab_band=5,
    grammar_band=5,
    question="Are traditional festivals becoming commercialized?",
    transcript="Yes, business use festival. Sell gift and food. Christmas is shopping day. Not religious. People spend much money. Forget meaning. But it help economy. Shop make profit. I think balance is need. Keep tradition but also fun.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'business use' -> 'businesses use'",
        "fragment: 'Sell gift and food'",
        "fragment: 'Not religious'",
        "verb agreement: 'Shop make' -> 'Shops make'",
        "verb construction: 'balance is need' -> 'balance is needed'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'commercialized' (in prompt), 'religious', 'spend', 'profit', 'balance'. >Band 4: Specific terms. Not Band 6: Lacks 'consumerism', 'spiritual', 'marketing', 'significance'.",
    grammar_reason="[GRA5] Contrast: 'But it help economy'. Opinion: 'I think balance is need'. >Band 4: Coherent. Not Band 6: Passive voice and agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 150: V5/G5 - Topic: Society (Change)
samples.append(create_sample(
    index=150,
    vocab_band=5,
    grammar_band=5,
    question="Is change always a good thing?",
    transcript="Not always. Some change is bad. For example, pollution. Climate change. But technology change is good. Make life easy. Change is difficult for old people. They like old way. Young people like new thing. We must adapt to change. Cannot stop it.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'technology change' -> 'technological change'",
        "phrase error: 'old way' -> 'the old way'",
        "singular/plural: 'new thing' -> 'new things'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'pollution', 'technology', 'difficult', 'adapt', 'stop'. >Band 4: Clear meaning. Not Band 6: Lacks 'progress', 'inevitable', 'resistance', 'benefit'.",
    grammar_reason="[GRA5] Contrast: 'But technology change is good'. Comparison: 'Old people... Young people...'. >Band 4: Structure variety. Not Band 6: Phrase errors.",
    idiom_present=False,
    risk_level="low"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
