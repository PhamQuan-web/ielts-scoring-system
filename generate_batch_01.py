import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch01.jsonl")

# Helper to format the final JSON object
def create_sample(index, vocab_band, grammar_band, question, transcript, response_type,
                  micro_flaws, grammar_profile, vocab_reason, grammar_reason,
                  idiom_present, risk_level):

    sample_id = f"syn_p3_v{vocab_band}_g{grammar_band}_{index:03d}"
    word_count = len(transcript.split())

    # Input field formatting
    input_text = (
        f"Part: 3\n"
        f"Question: {question}\n\n"
        f"Transcript: {transcript}\n\n"
        f"Word Count: {word_count} words\n"
        f"Response Type: {response_type}"
    )

    # Output field formatting
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

# --- BATCH 01 SAMPLES (50 Total) ---
# Mix of V4/G4 and V4/G5
# Topics: Society, Education, Technology, Environment, Work, Health, Culture, Ethics

# Sample 1: V4/G4 - Topic: Technology (Simple opinion)
samples.append(create_sample(
    index=1,
    vocab_band=4,
    grammar_band=4,
    question="Do you think technology helps students learn better?",
    transcript="I think technology is good for student. They can use internet for study. But sometimes it is bad because they play game too much. In my country, many student have computer. It help them do homework. So I think it is helpful.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'student' should be 'students'",
        "article missing: 'use internet' should be 'use the internet'",
        "verb agreement: 'it help' should be 'it helps'",
        "simple sentence structure only",
        "repetition of 'I think'",
        "limited vocabulary: 'good', 'bad', 'helpful'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic vocabulary used repetitively: 'good', 'bad', 'student', 'study'. >Band 3: Can convey meaning about familiar topic. Not Band 5: Lacks sufficient range to avoid repetition and discuss abstractly.",
    grammar_reason="[GRA4] Very simple sentence forms used. Frequent errors: 'it help', 'student have'. >Band 3: Subordinate clauses are attempted ('because...'). Not Band 5: Errors are frequent and structures are mainly simple.",
    idiom_present=False,
    risk_level="low"
))

# Sample 2: V4/G5 - Topic: Environment (Pollution)
samples.append(create_sample(
    index=2,
    vocab_band=4,
    grammar_band=5,
    question="What can people do to reduce pollution in cities?",
    transcript="People should use bus or train more. If they drive car, the air is dirty. Also, we can plant more tree. I think government need to make rule about this. It is important for our health because pollution is dangerous.",
    response_type="direct_answer",
    micro_flaws=[
        "article missing: 'use bus' -> 'use the bus'",
        "singular/plural: 'drive car' -> 'drive cars'",
        "singular/plural: 'plant more tree' -> 'plant more trees'",
        "verb agreement: 'government need' -> 'government needs'",
        "limited vocabulary: 'dirty', 'rule', 'dangerous'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Vocabulary is limited to basic items: 'bus', 'train', 'dirty', 'tree', 'rule'. >Band 3: sufficient for the task. Not Band 5: Lacks less common items; 'pollution' is from the prompt.",
    grammar_reason="[GRA5] Attempts complex sentences: 'If they drive car...', 'because pollution is dangerous'. >Band 4: Uses some complex structures (conditionals, reasons) with reasonable accuracy. Not Band 6: Mistakes still frequent in basic structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 3: V4/G4 - Topic: Shopping (Online vs In-store)
samples.append(create_sample(
    index=3,
    vocab_band=4,
    grammar_band=4,
    question="Why do some people prefer shopping online?",
    transcript="Some people like shop online because it is easy. They not need go out. But I like go to shop. I can see the thing I buy. Online shop sometimes have problem. The size is wrong. So I think shop is better.",
    response_type="direct_answer",
    micro_flaws=[
        "verb form: 'like shop' -> 'like shopping' or 'like to shop'",
        "verb construction: 'They not need' -> 'They do not need'",
        "verb form: 'like go' -> 'like going'",
        "missing relative pronoun: 'thing I buy' -> 'thing that I buy' (acceptable but simple)",
        "article/plural: 'Online shop' -> 'Online shops' or 'Online shopping'",
        "verb agreement: 'have problem' -> 'has problems'",
        "repetitive vocabulary: 'shop', 'like', 'buy'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Uses only basic words: 'easy', 'shop', 'size', 'wrong'. Repetitive use of 'shop'. >Band 3: Can communicate simple ideas. Not Band 5: Cannot paraphrase or use more precise language.",
    grammar_reason="[GRA4] mainly simple sentences. Frequent errors: 'They not need', 'Online shop have'. >Band 3: Connectors 'because' and 'but' are used. Not Band 5: Grammatical errors are systematic and cause some strain.",
    idiom_present=False,
    risk_level="low"
))

# Sample 4: V4/G5 - Topic: Work (Job satisfaction)
samples.append(create_sample(
    index=4,
    vocab_band=4,
    grammar_band=5,
    question="Is money the most important factor when choosing a job?",
    transcript="I think money is important but not most important. We need money for life. But if you do not like job, you will be sad. I believe happy is more important. Also, friend at work is good too. If we have good friend, we can work better.",
    response_type="direct_answer",
    micro_flaws=[
        "missing article: 'most important' -> 'the most important'",
        "wrong word form: 'happy is more important' -> 'happiness is more important'",
        "singular/plural: 'friend at work' -> 'friends at work'",
        "singular/plural: 'good friend' -> 'good friends'",
        "limited vocabulary: 'sad', 'happy', 'good', 'friend'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic vocabulary: 'money', 'life', 'job', 'sad', 'happy'. Wrong word form 'happy' (adjective) instead of 'happiness' (noun). >Band 3: intelligible. Not Band 5: Lacks vocabulary to express 'satisfaction', 'colleagues', 'environment'.",
    grammar_reason="[GRA5] Attempts complex sentences with 'but' and 'if'. 'If you do not like job, you will be sad' is a correct conditional structure. >Band 4: Better control of sentence structures. Not Band 6: Still relies on simple connectors and has basic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 5: V4/G4 - Topic: Transport (Traffic congestion)
samples.append(create_sample(
    index=5,
    vocab_band=4,
    grammar_band=4,
    question="Why is traffic congestion a problem in many big cities?",
    transcript="Many car in the city. The road is small. People go to work same time. It make traffic jam. I think government should make more road. Or people take bus. It is bad for air too. The car smoke make people sick.",
    response_type="direct_answer",
    micro_flaws=[
        "sentence fragment/missing verb: 'Many car in the city' -> 'There are many cars...'",
        "singular/plural: 'Many car' -> 'Many cars'",
        "missing preposition: 'work same time' -> 'work at the same time'",
        "verb agreement: 'It make' -> 'It makes'",
        "singular/plural: 'more road' -> 'more roads'",
        "article missing: 'take bus' -> 'take the bus'",
        "word choice: 'car smoke' -> 'exhaust fumes' (expected for higher band)",
        "verb agreement: 'smoke make' -> 'smoke makes'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Vocabulary is limited and repetitive: 'car', 'road', 'work', 'bad', 'sick'. 'Car smoke' shows lack of precise vocabulary. >Band 3: Meaning is clear. Not Band 5: Cannot discuss the topic with appropriate terms like 'congestion', 'commute', 'pollution'.",
    grammar_reason="[GRA4] Simple sentences predominant. Frequent basic errors: 'It make', 'The car smoke make'. >Band 3: Logical flow with 'Or' and 'It is'. Not Band 5: Errors in basic subject-verb agreement are frequent.",
    idiom_present=False,
    risk_level="low"
))

# Sample 6: V4/G5 - Topic: Education (Teacher's role)
samples.append(create_sample(
    index=6,
    vocab_band=4,
    grammar_band=5,
    question="How has the role of teachers changed in recent years?",
    transcript="In the past, teacher just talk and student listen. Now, teacher help student to learn by self. I think it is better. Because student can think more. Also, teacher use computer in class. This make the class interesting.",
    response_type="direct_answer",
    micro_flaws=[
        "verb tense: 'teacher just talk' -> 'teachers just talked'",
        "singular/plural: 'student listen' -> 'students listened'",
        "phrase error: 'learn by self' -> 'learn by themselves'",
        "verb agreement: 'This make' -> 'This makes'",
        "limited vocabulary: 'talk', 'listen', 'help', 'think', 'interesting'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Very basic vocabulary: 'talk', 'listen', 'help', 'think'. >Band 3: Communicates ideas. Not Band 5: Lacks terms like 'guidance', 'facilitator', 'independent learning'.",
    grammar_reason="[GRA5] mix of simple and complex. 'Because student can think more' is a dependent clause used as a sentence (common spoken feature). Tense consistency is an issue (using present for past). >Band 4: Some correct complex attempts. Not Band 6: Basic errors persist.",
    idiom_present=False,
    risk_level="low"
))

# Sample 7: V4/G4 - Topic: Culture (Museums)
samples.append(create_sample(
    index=7,
    vocab_band=4,
    grammar_band=4,
    question="Do you think museums are important for education?",
    transcript="Yes, museum is important. We can see old thing there. Children learn history. It is good place for family go weekend. But some museum is boring. Just look at picture. I think museum need more fun thing.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'museum is' -> 'museums are'",
        "word choice: 'old thing' -> 'old things' or 'artifacts'",
        "missing preposition/article: 'family go weekend' -> 'families to go to on the weekend'",
        "singular/plural: 'some museum is' -> 'some museums are'",
        "singular/plural: 'look at picture' -> 'look at pictures'",
        "verb agreement: 'museum need' -> 'museums need'",
        "word choice: 'fun thing' -> 'fun things' or 'interactive exhibits'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Limited vocabulary: 'old thing', 'good place', 'boring', 'picture', 'fun thing'. >Band 3: Meaning conveyed. Not Band 5: Lacks specific vocabulary like 'artifacts', 'exhibitions', 'interactive'.",
    grammar_reason="[GRA4] mainly simple sentences. 'Just look at picture' is a fragment. Errors in plurals and verbs are frequent. >Band 3: Some coherence. Not Band 5: frequent errors impede flow slightly.",
    idiom_present=False,
    risk_level="low"
))

# Sample 8: V4/G5 - Topic: Health (Exercise)
samples.append(create_sample(
    index=8,
    vocab_band=4,
    grammar_band=5,
    question="Why do many people find it difficult to exercise regularly?",
    transcript="People is busy with work. They come home late and tired. So they not want exercise. Also, gym is expensive. Some people not have money. I think if work is less time, people will exercise more.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'People is' -> 'People are'",
        "missing verb: 'late and tired' -> 'late and are tired'",
        "verb construction: 'not want exercise' -> 'do not want to exercise'",
        "missing article: 'gym is' -> 'the gym is'",
        "verb construction: 'not have money' -> 'do not have money'",
        "phrase error: 'work is less time' -> 'work takes less time' or 'working hours are shorter'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'busy', 'work', 'tired', 'expensive', 'money'. >Band 3: clear meaning. Not Band 5: repetition of 'exercise', lacks 'sedentary', 'commit', 'afford'.",
    grammar_reason="[GRA5] Uses conditionals: 'If work is less time...'. Connectors 'So', 'Also' used correctly. >Band 4: Some successful complex structures. Not Band 6: Basic errors 'People is', 'not have' are too frequent.",
    idiom_present=False,
    risk_level="low"
))

# Sample 9: V4/G4 - Topic: Technology (Robots)
samples.append(create_sample(
    index=9,
    vocab_band=4,
    grammar_band=4,
    question="Will robots replace humans in the workplace in the future?",
    transcript="Maybe robot do some job. Like make car or clean house. But robot cannot think like human. Human have feeling. Robot not have. So for some job, we need human. But simple job, maybe robot do better.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'Maybe robot' -> 'Maybe robots'",
        "singular/plural: 'do some job' -> 'will do some jobs'",
        "verb agreement: 'Human have' -> 'Humans have'",
        "verb construction: 'Robot not have' -> 'Robots do not have'",
        "missing article/plural: 'But simple job' -> 'But for simple jobs'",
        "verb agreement: 'robot do better' -> 'robots will do better'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] repetitive use of 'robot', 'human', 'job'. Basic verbs 'do', 'make', 'think', 'have'. >Band 3: Intelligible. Not Band 5: Lacks 'automate', 'artificial intelligence', 'emotion'.",
    grammar_reason="[GRA4] mostly simple sentences. 'Like make car...' is a fragment. Negative form 'Robot not have' is incorrect. >Band 3: Can link ideas. Not Band 5: Errors are systematic.",
    idiom_present=False,
    risk_level="low"
))

# Sample 10: V4/G5 - Topic: Society (Community)
samples.append(create_sample(
    index=10,
    vocab_band=4,
    grammar_band=5,
    question="What makes a neighborhood a good place to live?",
    transcript="A good place need safe. People should friendly. If neighbor help each other, it is good. Also, need store and park near house. I like place where is quiet. If too much noise, I cannot sleep.",
    response_type="direct_answer",
    micro_flaws=[
        "word form: 'need safe' -> 'needs to be safe' or 'needs safety'",
        "missing verb: 'People should friendly' -> 'People should be friendly'",
        "singular/plural: 'neighbor' -> 'neighbors'",
        "missing article/plural: 'need store' -> 'need stores'",
        "relative clause error: 'place where is quiet' -> 'a place that is quiet' or 'where it is quiet'",
        "phrase error: 'If too much noise' -> 'If there is too much noise'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic adjectives: 'good', 'safe', 'friendly', 'quiet'. >Band 3: Understandable. Not Band 5: Lacks 'facilities', 'amenities', 'atmosphere', 'community'.",
    grammar_reason="[GRA5] Uses conditionals 'If neighbor help...', 'If too much noise...'. Relative clause attempted 'place where is quiet'. >Band 4: Attempt at complex structures is clear. Not Band 6: Missing verbs and articles are frequent.",
    idiom_present=False,
    risk_level="low"
))

# Writing to file
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Generated {len(samples)} samples in {OUTPUT_FILE}")
