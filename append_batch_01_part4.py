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

# --- SAMPLES 31-50 ---
# Mix V4/G4 and V4/G5

# Sample 31: V4/G4 - Topic: Holidays (Traditions)
samples.append(create_sample(
    index=31,
    vocab_band=4,
    grammar_band=4,
    question="Why are traditional festivals important?",
    transcript="Festival is fun. People wear nice clothes. We eat special food. Family come together. It is good time. We remember old story. Children like it. I think every country have festival. It make people happy.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'Festival is' -> 'Festivals are'",
        "verb agreement: 'Family come' -> 'Families come' or 'Family comes'",
        "singular/plural: 'old story' -> 'old stories'",
        "verb agreement: 'country have' -> 'country has'",
        "verb agreement: 'It make' -> 'It makes'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'clothes', 'food', 'old', 'story', 'happy'. >Band 3: Understandable. Not Band 5: Lacks 'celebration', 'culture', 'heritage', 'unite'.",
    grammar_reason="[GRA4] Simple sentences mostly. 'It is good time'. 'It make people happy'. >Band 3: Logical. Not Band 5: Basic subject-verb agreement errors frequent.",
    idiom_present=False,
    risk_level="low"
))

# Sample 32: V4/G5 - Topic: Art (School)
samples.append(create_sample(
    index=32,
    vocab_band=4,
    grammar_band=5,
    question="Should art be taught in schools?",
    transcript="Yes, art is good. Student can draw and paint. It help them creative. Also, school is boring if only study book. Art is fun. I think if student happy, they learn better. But math is more important for job.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'It help' -> 'It helps'",
        "word form: 'creative' -> 'be creative' or 'creativity'",
        "verb agreement: 'if student happy' -> 'if students are happy'",
        "verb agreement: 'only study book' -> 'only study books'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'draw', 'paint', 'book', 'fun', 'job'. >Band 3: Clear. Not Band 5: Lacks 'expression', 'imagination', 'curriculum', 'subject'.",
    grammar_reason="[GRA5] Conditionals: 'if only study book...', 'if student happy...'. >Band 4: Complex structures attempted. Not Band 6: Missing verbs 'be' and agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 33: V4/G4 - Topic: History (Learning)
samples.append(create_sample(
    index=33,
    vocab_band=4,
    grammar_band=4,
    question="Is it important to learn about history?",
    transcript="History is about past. We know what happen before. It is interesting. But some people think it boring. Because many date and name. I like history of my country. It tell me who I am.",
    response_type="direct_answer",
    micro_flaws=[
        "verb tense: 'what happen' -> 'what happened'",
        "phrase error: 'think it boring' -> 'think it is boring'",
        "fragment/missing verb: 'Because many date and name' -> 'Because there are many dates and names'",
        "verb agreement: 'It tell' -> 'It tells'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'past', 'boring', 'date', 'name', 'country'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'events', 'ancestors', 'identity', 'learn from mistakes'.",
    grammar_reason="[GRA4] Simple sentences. Fragments 'Because many date'. Tense errors 'happen'. >Band 3: Coherent. Not Band 5: Errors in basic structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 34: V4/G5 - Topic: Science (Space)
samples.append(create_sample(
    index=34,
    vocab_band=4,
    grammar_band=5,
    question="How has science changed our lives?",
    transcript="Science change everything. We have light, car, phone. Life is easy now. Before, people work very hard. Now machine do work. Also medicine. People live long time. If we not have science, life is very hard.",
    response_type="direct_answer",
    micro_flaws=[
        "verb tense: 'Science change' -> 'Science changed' or 'has changed'",
        "singular/plural: 'machine' -> 'machines'",
        "phrase error: 'People live long time' -> 'People live for a long time'",
        "conditional error: 'If we not have' -> 'If we did not have'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'light', 'car', 'easy', 'hard', 'medicine'. >Band 3: Clear. Not Band 5: Lacks 'technology', 'invention', 'convenient', 'improve'.",
    grammar_reason="[GRA5] Conditionals: 'If we not have science...'. Comparison: 'Before... Now...'. >Band 4: Attempts complex ideas. Not Band 6: Basic errors in tense and negatives.",
    idiom_present=False,
    risk_level="low"
))

# Sample 35: V4/G4 - Topic: Shopping (Advertising)
samples.append(create_sample(
    index=35,
    vocab_band=4,
    grammar_band=4,
    question="Do advertisements make people buy things they don't need?",
    transcript="Yes, ad is everywhere. TV, internet, street. They show nice picture. Say it is good. People want buy. Even if not need. It is waste money. I not like ad. They lie sometimes.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'ad is' -> 'ads are'",
        "singular/plural: 'nice picture' -> 'nice pictures'",
        "verb construction: 'want buy' -> 'want to buy'",
        "phrase error: 'Even if not need' -> 'Even if they do not need it'",
        "verb construction: 'It is waste money' -> 'It is a waste of money'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'nice', 'picture', 'good', 'buy', 'money'. >Band 3: Understandable. Not Band 5: Lacks 'influence', 'product', 'persuade', 'consumer'.",
    grammar_reason="[GRA4] Short sentences and fragments. 'Even if not need'. 'Say it is good'. >Band 3: Logical. Not Band 5: Errors in verb patterns and fragments.",
    idiom_present=False,
    risk_level="low"
))

# Sample 36: V4/G5 - Topic: Work (Salary)
samples.append(create_sample(
    index=36,
    vocab_band=4,
    grammar_band=5,
    question="should high salary be the main reason for choosing a job?",
    transcript="Money is important. We need eat and pay house. But if job is boring, you not happy. Even if much money. I think interest is important too. If you like job, you work good. So money is not only thing.",
    response_type="direct_answer",
    micro_flaws=[
        "verb construction: 'need eat' -> 'need to eat'",
        "phrase error: 'pay house' -> 'pay for the house' or 'pay rent'",
        "verb construction: 'you not happy' -> 'you will not be happy'",
        "adverb error: 'work good' -> 'work well'",
        "phrase error: 'not only thing' -> 'not the only thing'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'eat', 'pay', 'boring', 'happy', 'interest'. >Band 3: Clear. Not Band 5: Lacks 'motivate', 'passion', 'career', 'satisfaction'.",
    grammar_reason="[GRA5] Conditionals: 'if job is boring...', 'If you like job...'. >Band 4: Uses complex structures. Not Band 6: Basic errors 'work good', 'you not happy'.",
    idiom_present=False,
    risk_level="low"
))

# Sample 37: V4/G4 - Topic: Environment (Water)
samples.append(create_sample(
    index=37,
    vocab_band=4,
    grammar_band=4,
    question="Why is it important to save water?",
    transcript="Water is life. We drink. We wash. Plant need water. In some place, no water. People die. So we not waste it. Turn off tap. Use less water. It is good for earth. Everyone must do.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Plant need' -> 'Plants need'",
        "phrase error: 'In some place' -> 'In some places'",
        "verb construction: 'we not waste' -> 'we should not waste'",
        "verb construction: 'Everyone must do' -> 'Everyone must do it'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'drink', 'wash', 'die', 'waste', 'tap'. >Band 3: Meaning clear. Not Band 5: Lacks 'essential', 'scarcity', 'resource', 'conserve'.",
    grammar_reason="[GRA4] Simple imperative sentences. 'Turn off tap'. 'Use less water'. >Band 3: Coherent. Not Band 5: Missing modals and objects.",
    idiom_present=False,
    risk_level="low"
))

# Sample 38: V4/G5 - Topic: Education (Homework)
samples.append(create_sample(
    index=38,
    vocab_band=4,
    grammar_band=5,
    question="Do students have too much homework these days?",
    transcript="Yes, too much. They study all day. Then come home do homework. No time play. I think little homework is okay. To remember lesson. But if too much, student tired. They need sleep too. Teacher should give less.",
    response_type="direct_answer",
    micro_flaws=[
        "verb construction: 'come home do homework' -> 'come home to do homework'",
        "phrase error: 'No time play' -> 'No time to play'",
        "phrase error: 'To remember lesson' -> 'To remember the lesson'",
        "verb agreement: 'student tired' -> 'students are tired'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'study', 'play', 'tired', 'sleep', 'less'. >Band 3: Clear. Not Band 5: Lacks 'pressure', 'academic', 'balance', 'assign'.",
    grammar_reason="[GRA5] Conditionals: 'if too much...'. Purpose: 'To remember lesson'. >Band 4: Complex ideas attempted. Not Band 6: Missing verbs and prepositions.",
    idiom_present=False,
    risk_level="low"
))

# Sample 39: V4/G4 - Topic: Society (Cities vs Countryside)
samples.append(create_sample(
    index=39,
    vocab_band=4,
    grammar_band=4,
    question="What are the differences between living in the city and the countryside?",
    transcript="City is big. Many people. Loud noise. Countryside is quiet. Green tree. Clean air. But city have job. Countryside no job. Young people go city. Old people stay country. I like city better. More fun.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Many people'",
        "fragment: 'Loud noise'",
        "fragment: 'Green tree'",
        "verb agreement: 'city have' -> 'city has'",
        "phrase error: 'Countryside no job' -> 'Countryside has no jobs'",
        "phrase error: 'go city' -> 'go to the city'",
        "phrase error: 'stay country' -> 'stay in the country'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'big', 'loud', 'quiet', 'green', 'fun'. >Band 3: Understandable. Not Band 5: Lacks 'pollution', 'peaceful', 'opportunity', 'lifestyle'.",
    grammar_reason="[GRA4] Short simple sentences and fragments. 'More fun'. 'Green tree'. >Band 3: Contrast is clear. Not Band 5: Lack of full sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 40: V4/G5 - Topic: Technology (Internet)
samples.append(create_sample(
    index=40,
    vocab_band=4,
    grammar_band=5,
    question="Is the internet dangerous for children?",
    transcript="Yes, sometimes dangerous. Bad people on internet. Also bad picture. If parents not watch, child see bad thing. Also game is addictive. Child play all time. I think parent need check computer. To protect child.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Also bad picture'",
        "conditional error: 'If parents not watch' -> 'If parents do not watch'",
        "verb agreement: 'child see' -> 'child sees'",
        "verb agreement: 'game is addictive' (correct) but 'Child play' -> 'Child plays'",
        "phrase error: 'play all time' -> 'play all the time'",
        "verb construction: 'need check' -> 'need to check'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'bad', 'picture', 'watch', 'game', 'check'. >Band 3: Clear. Not Band 5: Lacks 'content', 'supervise', 'cyberbullying', 'safe'.",
    grammar_reason="[GRA5] Conditionals: 'If parents not watch...'. Purpose: 'To protect child'. >Band 4: Uses complex structures. Not Band 6: Negative formation and agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 41: V4/G4 - Topic: Food (Healthy)
samples.append(create_sample(
    index=41,
    vocab_band=4,
    grammar_band=4,
    question="How can people have a healthier diet?",
    transcript="Eat fruit and vegetable. Not eat much meat. Sweet is bad. Drink water. Cook at home. Fast food is not good. I think if you eat good, you feel good. Many people eat bad food. They get sick.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'vegetable' -> 'vegetables'",
        "verb construction: 'Not eat much meat' -> 'Do not eat much meat'",
        "word form: 'Sweet is bad' -> 'Sweets are bad' or 'Sugar is bad'",
        "adverb error: 'eat good' -> 'eat well'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'fruit', 'meat', 'sweet', 'water', 'cook'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'balanced diet', 'nutrition', 'avoid', 'processed'.",
    grammar_reason="[GRA4] Imperatives and simple sentences. 'Drink water'. 'Not eat much meat'. >Band 3: Logical. Not Band 5: Errors in basic negatives and adverbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 42: V4/G5 - Topic: Travel (International)
samples.append(create_sample(
    index=42,
    vocab_band=4,
    grammar_band=5,
    question="Why do people like to travel to other countries?",
    transcript="To see new thing. Meet new people. Learn culture. It is interesting. Also food is different. If you travel, you know more about world. Some people want relax. Beach is nice. It is good experience.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'new thing' -> 'new things'",
        "missing article: 'Learn culture' -> 'Learn about the culture'",
        "missing article: 'about world' -> 'about the world'",
        "verb construction: 'want relax' -> 'want to relax'",
        "missing article: 'Beach is nice' -> 'The beach is nice'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'meet', 'learn', 'food', 'relax', 'beach'. >Band 3: Clear. Not Band 5: Lacks 'explore', 'foreign', 'tradition', 'broaden mind'.",
    grammar_reason="[GRA5] Conditionals: 'If you travel...'. Purpose: 'To see new thing'. >Band 4: Complex structures used. Not Band 6: Article omissions frequent.",
    idiom_present=False,
    risk_level="low"
))

# Sample 43: V4/G4 - Topic: Sport (Children)
samples.append(create_sample(
    index=43,
    vocab_band=4,
    grammar_band=4,
    question="Should all children play sports at school?",
    transcript="Yes, sport is good. Make body strong. Children sit long time. They need move. Also learn team. If not play, maybe fat. I like football when I small. It was fun. Every child should play.",
    response_type="direct_answer",
    micro_flaws=[
        "phrase error: 'Make body strong' -> 'It makes the body strong'",
        "verb construction: 'need move' -> 'need to move'",
        "phrase error: 'learn team' -> 'learn teamwork'",
        "conditional error: 'If not play' -> 'If they do not play'",
        "verb tense: 'when I small' -> 'when I was small'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'strong', 'sit', 'move', 'fat', 'fun'. >Band 3: Understandable. Not Band 5: Lacks 'physical', 'exercise', 'cooperation', 'obesity'.",
    grammar_reason="[GRA4] Fragments and simple sentences. 'Make body strong'. 'If not play'. >Band 3: Coherent. Not Band 5: Missing subjects and verbs.",
    idiom_present=False,
    risk_level="low"
))

# Sample 44: V4/G5 - Topic: Media (Reading)
samples.append(create_sample(
    index=44,
    vocab_band=4,
    grammar_band=5,
    question="Do people read less books now than in the past?",
    transcript="Yes, people read less. Because internet. They watch video or play game. Reading take time. People lazy now. But reading is good for brain. If read book, you learn many word. I think we should read more.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Because internet'",
        "verb agreement: 'Reading take time' -> 'Reading takes time'",
        "verb agreement: 'People lazy' -> 'People are lazy'",
        "conditional error: 'If read book' -> 'If you read a book'",
        "singular/plural: 'many word' -> 'many words'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'video', 'game', 'time', 'lazy', 'brain'. >Band 3: Clear. Not Band 5: Lacks 'knowledge', 'distraction', 'literacy', 'habit'.",
    grammar_reason="[GRA5] Conditionals: 'If read book...'. Causal: 'Because internet'. >Band 4: Uses connectors and logic. Not Band 6: Basic errors in verb 'be' and agreement.",
    idiom_present=False,
    risk_level="low"
))

# Sample 45: V4/G4 - Topic: Animals (Pets)
samples.append(create_sample(
    index=45,
    vocab_band=4,
    grammar_band=4,
    question="Why do people keep pets?",
    transcript="Pet is friend. Dog or cat. They make you happy. You not lonely. Dog protect house. Cat is cute. Children learn love animal. But need feed them. Take care. It is work. But good work.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'Pet is friend' -> 'Pets are friends'",
        "verb construction: 'You not lonely' -> 'You are not lonely'",
        "phrase error: 'learn love animal' -> 'learn to love animals'",
        "verb construction: 'need feed them' -> 'need to feed them'",
        "fragment: 'But good work'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'friend', 'happy', 'lonely', 'cute', 'feed'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'companionship', 'responsibility', 'bond', 'loyal'.",
    grammar_reason="[GRA4] Short simple sentences. 'Pet is friend'. 'Cat is cute'. >Band 3: Logical. Not Band 5: Missing auxiliary verbs and articles.",
    idiom_present=False,
    risk_level="low"
))

# Sample 46: V4/G5 - Topic: Family (Marriage)
samples.append(create_sample(
    index=46,
    vocab_band=4,
    grammar_band=5,
    question="Is the age for marriage changing in your country?",
    transcript="Yes, people marry late now. Before, 20 year old. Now 30. Because they want job first. Need money for house. Also women want work. Not just stay home. I think it is good. If marry too young, maybe fight.",
    response_type="direct_answer",
    micro_flaws=[
        "verb construction: 'marry late' -> 'marry later'",
        "phrase error: '20 year old' -> '20 years old'",
        "verb construction: 'women want work' -> 'women want to work'",
        "conditional error: 'If marry too young' -> 'If they marry too young'",
        "phrase error: 'maybe fight' -> 'maybe they will fight'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'late', 'job', 'house', 'work', 'fight'. >Band 3: Clear. Not Band 5: Lacks 'career', 'stable', 'relationship', 'finance'.",
    grammar_reason="[GRA5] Conditionals: 'If marry too young...'. Comparison: 'Before... Now...'. >Band 4: Complex structures attempted. Not Band 6: Missing subjects and future tense.",
    idiom_present=False,
    risk_level="low"
))

# Sample 47: V4/G4 - Topic: Transport (Safety)
samples.append(create_sample(
    index=47,
    vocab_band=4,
    grammar_band=4,
    question="How can we make roads safer?",
    transcript="Drive slow. Don't drink alcohol. Wear belt. Police catch bad driver. Fix road. Traffic light. People need learn rule. If not, accident happen. Many people die. It is sad. We need careful.",
    response_type="direct_answer",
    micro_flaws=[
        "adverb error: 'Drive slow' -> 'Drive slowly'",
        "phrase error: 'Wear belt' -> 'Wear a seatbelt'",
        "verb construction: 'need learn rule' -> 'need to learn the rules'",
        "verb agreement: 'accident happen' -> 'accidents happen'",
        "adjective error: 'We need careful' -> 'We need to be careful'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'slow', 'alcohol', 'fix', 'rule', 'sad'. >Band 3: Understandable. Not Band 5: Lacks 'speed limit', 'infrastructure', 'strict', 'fine'.",
    grammar_reason="[GRA4] Imperatives and simple sentences. 'Fix road'. 'Traffic light'. >Band 3: Coherent. Not Band 5: Fragmented speech.",
    idiom_present=False,
    risk_level="low"
))

# Sample 48: V4/G5 - Topic: Environment (Plastic)
samples.append(create_sample(
    index=48,
    vocab_band=4,
    grammar_band=5,
    question="Should we stop using plastic bags?",
    transcript="Yes, plastic bag is bad. It kill animal in sea. It not go away. We can use paper bag or cloth bag. It is better. If we stop plastic, earth is clean. Shop should not give plastic. People bring own bag.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'plastic bag is bad' -> 'plastic bags are bad'",
        "verb agreement: 'It kill' -> 'It kills'",
        "verb construction: 'It not go away' -> 'It does not go away'",
        "conditional error: 'If we stop plastic' -> 'If we stop using plastic'",
        "verb agreement: 'earth is clean' -> 'earth will be clean'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'bad', 'kill', 'sea', 'bag', 'clean'. >Band 3: Clear. Not Band 5: Lacks 'ocean', 'decompose', 'reusable', 'ban'.",
    grammar_reason="[GRA5] Conditionals: 'If we stop plastic...'. Modal verbs: 'Shop should not give'. >Band 4: Uses modals and conditionals. Not Band 6: Basic agreement and negative errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 49: V4/G4 - Topic: Technology (Computer)
samples.append(create_sample(
    index=49,
    vocab_band=4,
    grammar_band=4,
    question="Is it important to learn how to use a computer?",
    transcript="Yes, very important. Every job use computer. Write email. Find information. If you not know, no job. School teach computer now. Children know well. Old people hard to learn. But need learn.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'job use' -> 'job uses'",
        "fragment: 'Write email'",
        "conditional error: 'If you not know' -> 'If you do not know'",
        "fragment: 'no job' -> 'you get no job'",
        "phrase error: 'Old people hard to learn' -> 'It is hard for old people to learn'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'job', 'email', 'find', 'teach', 'hard'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'skill', 'software', 'essential', 'technology'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'If you not know'. 'But need learn'. >Band 3: Logical. Not Band 5: Errors in structure are frequent.",
    idiom_present=False,
    risk_level="low"
))

# Sample 50: V4/G5 - Topic: Society (Helping)
samples.append(create_sample(
    index=50,
    vocab_band=4,
    grammar_band=5,
    question="Why do some people help others?",
    transcript="Because they are kind. They want make people happy. If you help, you feel good. God see you. Some people volunteer. Give money or food. I think it is good heart. World need more help. If everyone help, no problem.",
    response_type="direct_answer",
    micro_flaws=[
        "verb construction: 'want make' -> 'want to make'",
        "verb agreement: 'God see you' -> 'God sees you'",
        "phrase error: 'good heart' -> 'a good heart'",
        "verb agreement: 'World need' -> 'The world needs'",
        "conditional error: 'If everyone help' -> 'If everyone helps'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "medium", "flexibility": "low"},
    vocab_reason="[LR4] Basic words: 'kind', 'happy', 'good', 'money', 'heart'. >Band 3: Clear. Not Band 5: Lacks 'generous', 'charity', 'community', 'support'.",
    grammar_reason="[GRA5] Conditionals: 'If you help...', 'If everyone help...'. Reason: 'Because they are kind'. >Band 4: Complex structures used. Not Band 6: Basic errors in agreement and verbs.",
    idiom_present=False,
    risk_level="low"
))

# Append to file
with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
