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

# --- BATCH 02 PART 2: SAMPLES 76-100 (25 Total) ---
# Combo: V5/G4 (Better vocab than grammar)

# Sample 76: V5/G4 - Topic: Work (Leadership)
samples.append(create_sample(
    index=76,
    vocab_band=5,
    grammar_band=4,
    question="Can leadership skills be taught?",
    transcript="Some people born leader. Natural talent. But skill can learn. Communication and decision making. School should teach. Manager need training. How to motivate staff. Experience is best teacher. So I think yes. It is possible.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Some people born leader' -> 'Some people are born leaders'",
        "fragment: 'Natural talent'",
        "verb construction: 'skill can learn' -> 'skills can be learned'",
        "verb agreement: 'Manager need' -> 'Managers need'",
        "fragment: 'How to motivate staff'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'leader', 'talent', 'communication', 'decision making', 'motivate', 'staff'. >Band 4: Specific terms. Not Band 6: Lacks 'innate', 'acquire', 'delegate', 'charisma'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'Natural talent'. 'Manager need training'. >Band 3: Logical. Not Band 5: Missing verbs and passive voice.",
    idiom_present=False,
    risk_level="low"
))

# Sample 77: V5/G4 - Topic: Environment (Water Pollution)
samples.append(create_sample(
    index=77,
    vocab_band=5,
    grammar_band=4,
    question="What are the effects of water pollution?",
    transcript="Water pollution is serious. Fish die. People get sick. Drink dirty water. Factory dump chemical in river. It destroy ecosystem. We need clean water for survive. If river polluted, no food. Fishing industry lose money.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Fish die' -> 'Fish are dying' or 'Fish die' (ok)",
        "fragment: 'Drink dirty water'",
        "verb agreement: 'Factory dump' -> 'Factories dump'",
        "singular/plural: 'chemical' -> 'chemicals'",
        "verb agreement: 'It destroy' -> 'It destroys'",
        "verb construction: 'for survive' -> 'to survive'",
        "verb agreement: 'industry lose' -> 'industry loses'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'pollution', 'chemical', 'ecosystem', 'survive', 'industry'. >Band 4: Relevant vocabulary. Not Band 6: Lacks 'contaminate', 'toxic', 'marine life', 'consequence'.",
    grammar_reason="[GRA4] Simple sentences. 'It destroy ecosystem'. 'Factory dump chemical'. >Band 3: Coherent. Not Band 5: Frequent basic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 78: V5/G4 - Topic: Technology (Smartphones)
samples.append(create_sample(
    index=78,
    vocab_band=5,
    grammar_band=4,
    question="Are smartphones making us less social?",
    transcript="Yes, I think so. People look screen all time. Ignore friend. Family dinner, everyone check phone. No conversation. It is rude. Addiction is real. We connect online but disconnect real life. Eye contact is miss.",
    response_type="direct_answer",
    micro_flaws=[
        "missing preposition: 'look screen' -> 'look at screens'",
        "fragment: 'Ignore friend'",
        "verb agreement: 'Eye contact is miss' -> 'Eye contact is missing'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'screen', 'ignore', 'conversation', 'rude', 'addiction', 'connect', 'disconnect'. >Band 4: Good range. Not Band 6: Lacks 'interaction', 'antisocial', 'virtual', 'device'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'No conversation'. 'Ignore friend'. >Band 3: Logical. Not Band 5: Lack of full sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 79: V5/G4 - Topic: Society (Poverty)
samples.append(create_sample(
    index=79,
    vocab_band=5,
    grammar_band=4,
    question="Can poverty ever be eliminated?",
    transcript="It is very hard. Always have poor people. But we can reduce it. Education is key. Give skill for job. Government support basic need. Food and shelter. Charity also help. But corruption is problem. Money not reach poor.",
    response_type="direct_answer",
    micro_flaws=[
        "phrase error: 'Always have poor people' -> 'There will always be poor people'",
        "fragment: 'Give skill for job'",
        "verb agreement: 'Government support' -> 'The government supports'",
        "singular/plural: 'basic need' -> 'basic needs'",
        "fragment: 'Food and shelter'",
        "verb agreement: 'Money not reach' -> 'Money does not reach'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'eliminate', 'reduce', 'skill', 'shelter', 'charity', 'corruption'. >Band 4: Specific terms. Not Band 6: Lacks 'inequality', 'resource distribution', 'eradicate'.",
    grammar_reason="[GRA4] Simple sentences. 'Always have poor people'. 'Money not reach poor'. >Band 3: Coherent. Not Band 5: Structural errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 80: V5/G4 - Topic: Health (Exercise)
samples.append(create_sample(
    index=80,
    vocab_band=5,
    grammar_band=4,
    question="Why do some people dislike exercise?",
    transcript="Exercise is tired. Make body pain. Sweat is dirty. Some people lazy. Prefer watch TV. Also no time. Work is busy. Gym is expensive membership. Motivation is low. They not see result fast. So they quit.",
    response_type="direct_answer",
    micro_flaws=[
        "adjective error: 'Exercise is tired' -> 'Exercise is tiring'",
        "phrase error: 'Make body pain' -> 'Makes the body painful'",
        "missing verb: 'Sweat is dirty' (ok) but simplistic",
        "verb agreement: 'Some people lazy' -> 'Some people are lazy'",
        "fragment: 'Prefer watch TV'",
        "fragment: 'Gym is expensive membership'",
        "verb construction: 'They not see' -> 'They do not see'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'sweat', 'lazy', 'membership', 'motivation', 'result', 'quit'. >Band 4: Relevant words. Not Band 6: Lacks 'exhausting', 'commitment', 'sedentary', 'physical'.",
    grammar_reason="[GRA4] Fragments and simple sentences. 'Prefer watch TV'. 'They not see result'. >Band 3: Meaning clear. Not Band 5: Basic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 81: V5/G4 - Topic: Education (Technology)
samples.append(create_sample(
    index=81,
    vocab_band=5,
    grammar_band=4,
    question="Should students be allowed to use smartphones in class?",
    transcript="Smartphone is distraction. Student play game. Chat with friend. Not listen teacher. But can be useful. Search information fast. Dictionary app. I think limited use is okay. Teacher control when use. Only for study purpose.",
    response_type="direct_answer",
    micro_flaws=[
        "missing article: 'Smartphone is distraction' -> 'Smartphones are a distraction'",
        "fragment: 'Student play game'",
        "fragment: 'Chat with friend'",
        "fragment: 'Not listen teacher'",
        "fragment: 'Only for study purpose'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'distraction', 'chat', 'search', 'app', 'limited', 'purpose'. >Band 4: Good range. Not Band 6: Lacks 'educational tool', 'regulate', 'engage', 'access'.",
    grammar_reason="[GRA4] Mainly fragments. 'Student play game'. 'Not listen teacher'. >Band 3: Logical. Not Band 5: Lack of full sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 82: V5/G4 - Topic: Culture (Museums)
samples.append(create_sample(
    index=82,
    vocab_band=5,
    grammar_band=4,
    question="How can museums attract more young people?",
    transcript="Museum is boring for young. Only old thing. Need make it fun. Interactive exhibit. Use technology. VR or AR. Also discount ticket. Student price. Host event or concert. Social media promotion. Make it cool place.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Only old thing'",
        "verb construction: 'Need make it fun' -> 'Need to make it fun'",
        "fragment: 'Interactive exhibit'",
        "fragment: 'Social media promotion'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'interactive', 'exhibit', 'technology', 'VR', 'AR', 'discount', 'promotion'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'engage', 'digital', 'experience', 'modernize'.",
    grammar_reason="[GRA4] Fragments and simple sentences. 'Only old thing'. 'Make it cool place'. >Band 3: Coherent list. Not Band 5: Not sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 83: V5/G4 - Topic: Work (Robots)
samples.append(create_sample(
    index=83,
    vocab_band=5,
    grammar_band=4,
    question="Will robots take over all jobs?",
    transcript="Not all job. Creative job is safe. Artist, writer, musician. Also job with emotion. Nurse, teacher, psychologist. Robot cannot feel. But factory job is danger. Repetitive task. Robot is faster and cheaper. Human need adapt.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Not all job'",
        "fragment: 'Artist, writer, musician'",
        "phrase error: 'job is danger' -> 'jobs are in danger'",
        "fragment: 'Repetitive task'",
        "verb construction: 'Human need adapt' -> 'Humans need to adapt'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'creative', 'emotion', 'psychologist', 'repetitive', 'adapt'. >Band 4: Good range. Not Band 6: Lacks 'artificial intelligence', 'replace', 'complex', 'empathy'.",
    grammar_reason="[GRA4] Fragments and simple sentences. 'Not all job'. 'Human need adapt'. >Band 3: Logical. Not Band 5: Structural errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 84: V5/G4 - Topic: Transport (Traffic)
samples.append(create_sample(
    index=84,
    vocab_band=5,
    grammar_band=4,
    question="What is the best way to reduce traffic congestion?",
    transcript="Build more road is not solution. More car will come. Public transport is key. Metro and bus. Must be reliable. Also encourage bike. Lane for cycle. Carpooling is good idea. Work from home also help. Rush hour is terrible.",
    response_type="direct_answer",
    micro_flaws=[
        "phrase error: 'Build more road' -> 'Building more roads'",
        "verb agreement: 'More car will come' -> 'More cars will come'",
        "fragment: 'Lane for cycle'",
        "verb agreement: 'Work from home also help' -> 'Working from home also helps'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'solution', 'public transport', 'reliable', 'encourage', 'carpooling', 'rush hour'. >Band 4: Relevant terms. Not Band 6: Lacks 'infrastructure', 'incentive', 'commute', 'alternative'.",
    grammar_reason="[GRA4] Simple sentences. 'Rush hour is terrible'. 'Work from home also help'. >Band 3: Coherent. Not Band 5: Subject-verb errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 85: V5/G4 - Topic: Society (Crime)
samples.append(create_sample(
    index=85,
    vocab_band=5,
    grammar_band=4,
    question="Does prison help to rehabilitate criminals?",
    transcript="Prison is punishment. Not help much. Criminal learn bad thing inside. When release, no job. Society reject them. So they steal again. Rehabilitation program is better. Teach skill. Psychology support. Give second chance.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Not help much'",
        "verb agreement: 'Criminal learn' -> 'Criminals learn'",
        "phrase error: 'When release' -> 'When released'",
        "verb agreement: 'Society reject' -> 'Society rejects'",
        "fragment: 'Psychology support'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'punishment', 'criminal', 'release', 'reject', 'rehabilitation', 'psychology'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'integrate', 'offender', 'system', 'rate'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'Not help much'. 'Society reject them'. >Band 3: Logical. Not Band 5: Missing verbs and passive structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 86: V5/G4 - Topic: Education (University)
samples.append(create_sample(
    index=86,
    vocab_band=5,
    grammar_band=4,
    question="Is university education worth the cost?",
    transcript="It depend on major. Doctor or engineer, yes. High salary later. But some degree useless. Art or history. Hard to find job. Debt is high. Student loan is burden. Maybe vocational school is better. Skill for work.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'It depend' -> 'It depends'",
        "fragment: 'Doctor or engineer, yes'",
        "fragment: 'High salary later'",
        "fragment: 'Art or history'",
        "fragment: 'Skill for work'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'major', 'salary', 'degree', 'debt', 'loan', 'burden', 'vocational'. >Band 4: Good range. Not Band 6: Lacks 'investment', 'graduate', 'employment', 'financial'.",
    grammar_reason="[GRA4] Fragments and simple sentences. 'It depend'. 'Debt is high'. >Band 3: Coherent. Not Band 5: Not full sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 87: V5/G4 - Topic: Technology (Children)
samples.append(create_sample(
    index=87,
    vocab_band=5,
    grammar_band=4,
    question="What is the right age for a child to get a smartphone?",
    transcript="Maybe 12 or 13. Secondary school. They need contact parent. Safety reason. But too young is bad. Addiction risk. Social media danger. Parent must control. Limit screen time. Check content. Not let them play all night.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Secondary school'",
        "verb construction: 'need contact' -> 'need to contact'",
        "fragment: 'Safety reason'",
        "fragment: 'Addiction risk'",
        "fragment: 'Social media danger'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'secondary school', 'contact', 'safety', 'addiction', 'limit', 'content'. >Band 4: Relevant terms. Not Band 6: Lacks 'maturity', 'responsibility', 'monitor', 'exposure'.",
    grammar_reason="[GRA4] Fragments. 'Safety reason'. 'Addiction risk'. >Band 3: Logical list. Not Band 5: Lack of sentence structure.",
    idiom_present=False,
    risk_level="low"
))

# Sample 88: V5/G4 - Topic: Environment (Climate)
samples.append(create_sample(
    index=88,
    vocab_band=5,
    grammar_band=4,
    question="How can individuals help fight climate change?",
    transcript="Small action help. Turn off light. Save water. Use public transport. Eat less meat. Plant tree. Reduce plastic. One person do little. But everyone do, big impact. Awareness is important. Tell friend and family.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Small action help' -> 'Small actions help'",
        "fragment: 'Turn off light'",
        "fragment: 'Save water'",
        "phrase error: 'everyone do' -> 'if everyone does it'",
        "fragment: 'Big impact' -> 'it has a big impact'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'action', 'transport', 'reduce', 'impact', 'awareness'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'carbon footprint', 'sustainable', 'collective', 'lifestyle'.",
    grammar_reason="[GRA4] Imperatives and fragments. 'Turn off light'. 'One person do little'. >Band 3: Coherent. Not Band 5: Missing subjects and connectors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 89: V5/G4 - Topic: Society (Homelessness)
samples.append(create_sample(
    index=89,
    vocab_band=5,
    grammar_band=4,
    question="What are the main causes of homelessness?",
    transcript="Main cause is money. Lose job. Cannot pay rent. House is expensive. Also mental health. Drugs and alcohol. Family problem. Divorce or fight. Government support is weak. Shelter is full. It is sad situation.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Lose job'",
        "fragment: 'Cannot pay rent'",
        "fragment: 'Also mental health'",
        "fragment: 'Drugs and alcohol'",
        "fragment: 'Family problem'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'rent', 'mental health', 'drug', 'alcohol', 'divorce', 'shelter'. >Band 4: Relevant terms. Not Band 6: Lacks 'unemployment', 'addiction', 'affordable housing', 'social safety net'.",
    grammar_reason="[GRA4] Fragments. 'Lose job'. 'Shelter is full'. >Band 3: Logical. Not Band 5: Lack of full sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 90: V5/G4 - Topic: Work (Salary)
samples.append(create_sample(
    index=90,
    vocab_band=5,
    grammar_band=4,
    question="Should all jobs have the same salary?",
    transcript="No, it is unfair. Doctor study long time. Save life. Cleaner work easy. If same salary, no motivation. Why study hard? Everyone want easy job. Skill is different. Responsibility is different. Pay must match skill.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Doctor study' -> 'Doctors study'",
        "fragment: 'Save life'",
        "phrase error: 'Cleaner work easy' -> 'Cleaners have easy work'",
        "verb agreement: 'Everyone want' -> 'Everyone wants'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'unfair', 'motivation', 'skill', 'responsibility', 'match'. >Band 4: Specific terms. Not Band 6: Lacks 'qualification', 'incentive', 'wage', 'effort'.",
    grammar_reason="[GRA4] Simple sentences. 'Doctor study long time'. 'If same salary, no motivation'. >Band 3: Coherent. Not Band 5: Basic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 91: V5/G4 - Topic: Culture (Fashion)
samples.append(create_sample(
    index=91,
    vocab_band=5,
    grammar_band=4,
    question="Does fashion define a person's character?",
    transcript="Maybe a little. Cloth show style. If wear suit, look professional. Serious person. If wear colorful, maybe creative. But not always true. Some people rich but wear simple. Judge book by cover is wrong. Character is inside.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'Cloth' -> 'Clothes'",
        "verb agreement: 'Cloth show' -> 'Clothes show'",
        "fragment: 'Serious person'",
        "phrase error: 'If wear colorful' -> 'If they wear colorful clothes'",
        "phrase error: 'Judge book by cover' -> 'Judging a book by its cover'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'style', 'suit', 'professional', 'creative', 'judge', 'character'. >Band 4: Good range. Not Band 6: Lacks 'personality', 'impression', 'appearance', 'express'.",
    grammar_reason="[GRA4] Fragments and simple sentences. 'If wear suit'. 'Serious person'. >Band 3: Logical. Not Band 5: Missing subjects.",
    idiom_present=False,
    risk_level="low"
))

# Sample 92: V5/G4 - Topic: Health (Stress)
samples.append(create_sample(
    index=92,
    vocab_band=5,
    grammar_band=4,
    question="What are the effects of stress on health?",
    transcript="Stress is bad for body. Headache and stomach pain. Cannot sleep. Insomnia. Also heart problem. High blood pressure. Mental health suffer. Depression or anxiety. People get angry easy. Immune system weak. Get sick fast.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Headache and stomach pain'",
        "fragment: 'Insomnia'",
        "fragment: 'Also heart problem'",
        "verb agreement: 'Mental health suffer' -> 'Mental health suffers'",
        "adverb error: 'angry easy' -> 'angry easily'",
        "verb agreement: 'Immune system weak' -> 'Immune system is weak'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'insomnia', 'blood pressure', 'depression', 'anxiety', 'immune system'. >Band 4: Specific health terms. Not Band 6: Lacks 'symptom', 'chronic', 'psychological', 'impact'.",
    grammar_reason="[GRA4] Fragments. 'High blood pressure'. 'Mental health suffer'. >Band 3: List of points. Not Band 5: Lack of sentence structure.",
    idiom_present=False,
    risk_level="low"
))

# Sample 93: V5/G4 - Topic: Transport (Safety)
samples.append(create_sample(
    index=93,
    vocab_band=5,
    grammar_band=4,
    question="Why are there so many road accidents?",
    transcript="Driver is careless. Drive too fast. Speeding. Also drunk driving. Alcohol make reaction slow. Use phone while drive. Texting. Road is bad condition. Hole in road. Weather is rain or fog. Not see clear. Accident happen.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Driver is' -> 'Drivers are'",
        "fragment: 'Speeding'",
        "verb agreement: 'Alcohol make' -> 'Alcohol makes'",
        "phrase error: 'Use phone while drive' -> 'Using phone while driving'",
        "fragment: 'Hole in road'",
        "adverb error: 'Not see clear' -> 'Cannot see clearly'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'careless', 'speeding', 'drunk driving', 'reaction', 'texting', 'condition', 'fog'. >Band 4: Good range. Not Band 6: Lacks 'distraction', 'vehicle', 'regulation', 'visibility'.",
    grammar_reason="[GRA4] Fragments and simple sentences. 'Alcohol make reaction slow'. 'Accident happen'. >Band 3: Coherent. Not Band 5: Basic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 94: V5/G4 - Topic: Education (Group Work)
samples.append(create_sample(
    index=94,
    vocab_band=5,
    grammar_band=4,
    question="What are the benefits of group work for students?",
    transcript="Group work teach teamwork. How to cooperate. Share idea. Solve problem together. Communication skill improve. Also make friend. But sometimes argument. One person do all work. Lazy student. Teacher need manage well.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Group work teach' -> 'Group work teaches'",
        "fragment: 'How to cooperate'",
        "fragment: 'Share idea'",
        "verb agreement: 'Communication skill improve' -> 'Communication skills improve'",
        "fragment: 'Lazy student'",
        "verb construction: 'Teacher need manage' -> 'Teachers need to manage'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'teamwork', 'cooperate', 'solve', 'communication', 'argument', 'manage'. >Band 4: Relevant vocabulary. Not Band 6: Lacks 'collaborate', 'leadership', 'conflict', 'contribution'.",
    grammar_reason="[GRA4] Fragments. 'Share idea'. 'One person do all work'. >Band 3: Logical. Not Band 5: Lack of full sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 95: V5/G4 - Topic: Society (Tradition)
samples.append(create_sample(
    index=95,
    vocab_band=5,
    grammar_band=4,
    question="Is it important to follow traditions?",
    transcript="Tradition is history. Connect with ancestor. Festival and ceremony. Identify who we are. Respect old people. But some tradition is bad. Old fashion. Not good for modern life. Gender role for example. We should keep good one. Change bad one.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Connect with ancestor'",
        "fragment: 'Festival and ceremony'",
        "fragment: 'Identify who we are'",
        "fragment: 'Old fashion'",
        "fragment: 'Gender role for example'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'ancestor', 'ceremony', 'identify', 'respect', 'gender role', 'modern'. >Band 4: Specific terms. Not Band 6: Lacks 'preserve', 'heritage', 'obsolete', 'adapt'.",
    grammar_reason="[GRA4] Fragments. 'Tradition is history'. 'Change bad one'. >Band 3: Coherent. Not Band 5: Not sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 96: V5/G4 - Topic: Technology (Space)
samples.append(create_sample(
    index=96,
    vocab_band=5,
    grammar_band=4,
    question="What is the benefit of space exploration?",
    transcript="Discover new world. Maybe find alien life. New resource. Technology for space help earth too. Satellite. GPS and weather forecast. But cost is high. Billion dollar. Waste money? Maybe fix earth problem first. Climate change and poverty.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Discover new world'",
        "fragment: 'New resource'",
        "verb agreement: 'Technology for space help' -> 'Technology for space helps'",
        "fragment: 'Satellite'",
        "fragment: 'Billion dollar'",
        "fragment: 'Climate change and poverty'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'alien', 'resource', 'satellite', 'GPS', 'forecast', 'poverty'. >Band 4: Good range. Not Band 6: Lacks 'universe', 'investigation', 'scientific', 'priority'.",
    grammar_reason="[GRA4] Fragments. 'Discover new world'. 'Waste money?'. >Band 3: Logical list. Not Band 5: Lack of structure.",
    idiom_present=False,
    risk_level="low"
))

# Sample 97: V5/G4 - Topic: Work (Job Satisfaction)
samples.append(create_sample(
    index=97,
    vocab_band=5,
    grammar_band=4,
    question="What is more important: job satisfaction or high salary?",
    transcript="Satisfaction is better. You spend many time at work. If hate job, life is stress. Money is good but not everything. Can buy thing but not happiness. Passion is important. Do what you love. But need enough money for live. Balance.",
    response_type="direct_answer",
    micro_flaws=[
        "phrase error: 'spend many time' -> 'spend a lot of time'",
        "verb construction: 'If hate job' -> 'If you hate your job'",
        "phrase error: 'life is stress' -> 'life is stressful'",
        "verb construction: 'Can buy thing' -> 'You can buy things'",
        "verb construction: 'money for live' -> 'money to live'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'satisfaction', 'stress', 'happiness', 'passion', 'balance'. >Band 4: Relevant terms. Not Band 6: Lacks 'fulfillment', 'career', 'motivate', 'essential'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'Satisfaction is better'. 'Do what you love'. >Band 3: Coherent. Not Band 5: Missing subjects and verbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 98: V5/G4 - Topic: Environment (City)
samples.append(create_sample(
    index=98,
    vocab_band=5,
    grammar_band=4,
    question="How can we make cities greener?",
    transcript="Plant more tree. Park and garden. Green roof on building. Reduce car. Use electric bus. Cycle path. Clean energy. Solar power. People need awareness. Not throw trash. Government make strict law. Fine for pollution. City become nice.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Plant more tree'",
        "fragment: 'Park and garden'",
        "fragment: 'Green roof on building'",
        "fragment: 'Clean energy'",
        "verb agreement: 'City become nice' -> 'The city becomes nice'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'green roof', 'electric bus', 'cycle path', 'solar power', 'awareness', 'fine'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'urban planning', 'sustainable', 'emissions', 'environmentally friendly'.",
    grammar_reason="[GRA4] Fragments. 'Plant more tree'. 'Solar power'. >Band 3: List of ideas. Not Band 5: Not full sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 99: V5/G4 - Topic: Society (Media)
samples.append(create_sample(
    index=99,
    vocab_band=5,
    grammar_band=4,
    question="Do celebrities have too much influence on young people?",
    transcript="Yes, big influence. Young people copy them. Clothes and hair. Behavior too. If celebrity do bad thing, fan do same. Smoke or drink. It is danger. Celebrity is role model. Should be responsible. Good example. Media show them too much.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Big influence'",
        "fragment: 'Clothes and hair'",
        "verb agreement: 'celebrity do bad thing' -> 'celebrities do bad things'",
        "phrase error: 'fan do same' -> 'fans do the same'",
        "word form: 'It is danger' -> 'It is dangerous'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'influence', 'copy', 'behavior', 'role model', 'responsible', 'media'. >Band 4: Relevant terms. Not Band 6: Lacks 'imitate', 'impact', 'idolize', 'trendsetter'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'It is danger'. 'Good example'. >Band 3: Logical. Not Band 5: Basic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 100: V5/G4 - Topic: Health (Healthcare)
samples.append(create_sample(
    index=100,
    vocab_band=5,
    grammar_band=4,
    question="Should healthcare be free for everyone?",
    transcript="Yes, health is right. Poor people cannot pay. If sick, they die. Unfair. Government should pay. Use tax money. Healthy people can work. Economy good. But expensive for government. Long wait time. Doctor salary low. Complex problem.",
    response_type="direct_answer",
    micro_flaws=[
        "missing article: 'health is right' -> 'health is a right'",
        "fragment: 'Unfair'",
        "verb agreement: 'Economy good' -> 'Economy is good'",
        "fragment: 'Long wait time'",
        "fragment: 'Doctor salary low'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'right', 'tax', 'economy', 'wait time', 'salary', 'complex'. >Band 4: Specific terms. Not Band 6: Lacks 'universal', 'access', 'funding', 'quality'.",
    grammar_reason="[GRA4] Fragments. 'If sick, they die'. 'Complex problem'. >Band 3: Coherent. Not Band 5: Lack of sentence structure.",
    idiom_present=False,
    risk_level="low"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
