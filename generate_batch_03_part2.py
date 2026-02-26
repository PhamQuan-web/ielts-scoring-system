import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch03.jsonl")

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

# --- BATCH 03 PART 2: SAMPLES 176-200 (25 Total) ---
# Combo: V5/G6

# Sample 176: V5/G6 - Topic: Society (Community)
samples.append(create_sample(
    index=176,
    vocab_band=5,
    grammar_band=6,
    question="What makes a good neighbor?",
    transcript="A good neighbor is someone who is friendly. They help you when you need it. They are quiet at night. They don't make loud noise. Also, they are clean. They don't throw trash on the street. If you go on holiday, they watch your house. It is important to trust them.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'go on holiday' (correct)",
        "phrase error: 'throw trash' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'friendly', 'help', 'quiet', 'noise', 'clean', 'trust'. >Band 4: Relevant terms. Not Band 6: Lacks 'considerate', 'community', 'respectful', 'relationship'.",
    grammar_reason="[GRA6] Relative clause: 'Someone who is friendly'. Conditionals: 'If you go...'. >Band 5: Accurate grammar. Not Band 7: Simple vocabulary limits structure.",
    idiom_present=False,
    risk_level="low"
))

# Sample 177: V5/G6 - Topic: Technology (Computer)
samples.append(create_sample(
    index=177,
    vocab_band=5,
    grammar_band=6,
    question="Why is it important to learn computer skills?",
    transcript="Because computers are everywhere. We use them for work and study. If you don't know how to use a computer, you cannot get a good job. Everything is online now. Banking, shopping, news. It is a basic skill. Like reading and writing. Everyone needs it.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'basic skill' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'everywhere', 'work', 'study', 'online', 'banking', 'basic'. >Band 4: Specific words. Not Band 6: Lacks 'essential', 'digital', 'technology', 'access'.",
    grammar_reason="[GRA6] Conditionals: 'If you don't know...'. Reason: 'Because computers are...'. >Band 5: Good control. Not Band 7: Short simple sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 178: V5/G6 - Topic: Health (Mental)
samples.append(create_sample(
    index=178,
    vocab_band=5,
    grammar_band=6,
    question="Why is mental health important?",
    transcript="The mind controls the body. If you are stressed, your body feels sick. You cannot sleep or eat well. Many people work too hard today. They are tired and unhappy. This is a big problem. We need to relax more. Talk to friends or family. It helps you feel better.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'mind controls the body' (simple)",
        "phrase error: 'big problem' (simple)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'mind', 'body', 'stressed', 'sick', 'tired', 'relax'. >Band 4: Good range. Not Band 6: Lacks 'psychological', 'well-being', 'anxiety', 'balance'.",
    grammar_reason="[GRA6] Conditionals: 'If you are stressed...'. Modals: 'Need to relax'. >Band 5: Clear and correct. Not Band 7: Repetitive structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 179: V5/G6 - Topic: Work (Gender)
samples.append(create_sample(
    index=179,
    vocab_band=5,
    grammar_band=6,
    question="Should men and women get paid the same?",
    transcript="Of course. If they do the same job, the pay should be equal. It is not fair if men get more money. Women work hard too. They have the same skills. In the past, men were the bosses. But now, women are leaders too. Companies must be fair to everyone.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'bosses' (correct)",
        "phrase error: 'fair to everyone' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'equal', 'fair', 'money', 'skills', 'leaders', 'companies'. >Band 4: Relevant terms. Not Band 6: Lacks 'salary', 'gender gap', 'discrimination', 'opportunity'.",
    grammar_reason="[GRA6] Conditionals: 'If they do the same job...'. Comparison: 'In the past...'. >Band 5: Accurate grammar. Not Band 7: Simple connectors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 180: V5/G6 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=180,
    vocab_band=5,
    grammar_band=6,
    question="Why are zoos controversial?",
    transcript="Some people like zoos. They can see animals from other countries. It is educational for children. But other people hate zoos. They think it is cruel. Animals are in cages. They cannot run free. They look sad. I think wild animals belong in the wild. Not in a city.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'belong in the wild' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'animals', 'countries', 'educational', 'cruel', 'cages', 'wild'. >Band 4: Clear meaning. Not Band 6: Lacks 'captivity', 'natural habitat', 'conservation', 'ethical'.",
    grammar_reason="[GRA6] Contrast: 'But other people hate zoos'. Reason: 'They think it is cruel'. >Band 5: Error-free sentences. Not Band 7: Very simple structure.",
    idiom_present=False,
    risk_level="low"
))

# Sample 181: V5/G6 - Topic: Education (Homework)
samples.append(create_sample(
    index=181,
    vocab_band=5,
    grammar_band=6,
    question="Is homework necessary?",
    transcript="I think a little is okay. It helps students remember the lesson. They practice at home. But too much is bad. Children need time to play. They are tired after school. If they do homework all night, they don't sleep enough. Teachers should give less work.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'give less work' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'remember', 'lesson', 'practice', 'play', 'tired', 'sleep'. >Band 4: Relevant terms. Not Band 6: Lacks 'reinforce', 'academic', 'pressure', 'balance'.",
    grammar_reason="[GRA6] Conditionals: 'If they do homework...'. Contrast: 'But too much is bad'. >Band 5: Accurate grammar. Not Band 7: Limited complexity.",
    idiom_present=False,
    risk_level="low"
))

# Sample 182: V5/G6 - Topic: Transport (Public)
samples.append(create_sample(
    index=182,
    vocab_band=5,
    grammar_band=6,
    question="Why don't more people use public transport?",
    transcript="Because it is not convenient. Buses are often late. You have to wait a long time. Also, they are crowded. You have no seat. In summer, it is hot and smelly. Cars are more comfortable. You have music and AC. People want comfort.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'hot and smelly' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'convenient', 'late', 'wait', 'crowded', 'seat', 'comfortable'. >Band 4: Specific words. Not Band 6: Lacks 'reliable', 'efficient', 'schedule', 'personal space'.",
    grammar_reason="[GRA6] Reason: 'Because it is not convenient'. Comparison implied. >Band 5: Correct structures. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 183: V5/G6 - Topic: Culture (Food)
samples.append(create_sample(
    index=183,
    vocab_band=5,
    grammar_band=6,
    question="Is food an important part of culture?",
    transcript="Yes, definitely. Every country has special food. It tells us about the history. For example, in my country, we eat rice every day. It is our tradition. When we have a festival, we cook special dishes. Food brings people together. We share it with family and friends.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'special dishes' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'special', 'history', 'rice', 'tradition', 'festival', 'share'. >Band 4: Good range. Not Band 6: Lacks 'cuisine', 'ingredients', 'identity', 'celebration'.",
    grammar_reason="[GRA6] Time clause: 'When we have a festival...'. >Band 5: Error-free grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="low"
))

# Sample 184: V5/G6 - Topic: Society (Cities)
samples.append(create_sample(
    index=184,
    vocab_band=5,
    grammar_band=6,
    question="Why do young people move to cities?",
    transcript="They move for jobs. There are more companies in the city. The salary is higher. Also, for education. Universities are in big cities. Life is more exciting there. There are shops, cinemas, and clubs. Villages are quiet and boring for young people. They want a modern life.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'modern life' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'companies', 'salary', 'universities', 'exciting', 'shops', 'modern'. >Band 4: Relevant terms. Not Band 6: Lacks 'opportunity', 'career', 'entertainment', 'urban'.",
    grammar_reason="[GRA6] Comparison: 'Life is more exciting'. Contrast implied. >Band 5: Accurate grammar. Not Band 7: Repetitive 'There are...'.",
    idiom_present=False,
    risk_level="low"
))

# Sample 185: V5/G6 - Topic: Technology (Phones)
samples.append(create_sample(
    index=185,
    vocab_band=5,
    grammar_band=6,
    question="Do people rely too much on their phones?",
    transcript="Yes, too much. We use phones for everything. Calling, messaging, map, camera. If we lose our phone, we panic. We cannot do anything. People check their phones every minute. Even when talking to friends. It is a bad habit. We need to look up sometimes.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'look up' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'messaging', 'map', 'panic', 'check', 'habit', 'look up'. >Band 4: Specific words. Not Band 6: Lacks 'dependent', 'device', 'addicted', 'communicate'.",
    grammar_reason="[GRA6] Conditionals: 'If we lose our phone...'. Reason: 'We cannot do anything'. >Band 5: Good control. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 186: V5/G6 - Topic: Environment (Energy)
samples.append(create_sample(
    index=186,
    vocab_band=5,
    grammar_band=6,
    question="How can we save energy at home?",
    transcript="There are many simple ways. Turn off the lights when you leave a room. Don't leave the TV on. Use less water. Hot water uses energy. Also, buy good machines. Like a fridge that saves power. If everyone does a little bit, it helps the world.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'good machines' (simple for appliances)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'simple', 'lights', 'water', 'power', 'world', 'turn off'. >Band 4: Clear instructions. Not Band 6: Lacks 'efficient', 'electricity', 'conserve', 'reduce'.",
    grammar_reason="[GRA6] Conditionals: 'If everyone does...'. Time clause: 'When you leave...'. >Band 5: Accurate grammar. Not Band 7: Imperatives mostly.",
    idiom_present=False,
    risk_level="low"
))

# Sample 187: V5/G6 - Topic: Work (Team)
samples.append(create_sample(
    index=187,
    vocab_band=5,
    grammar_band=6,
    question="What are the disadvantages of working in a team?",
    transcript="Sometimes it is slow. You have to wait for other people. Everyone has a different idea. So you argue. Decision making takes time. Also, some people are lazy. They don't do their work. You have to do it for them. This makes you angry.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'decision making' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'slow', 'wait', 'idea', 'argue', 'lazy', 'angry'. >Band 4: Relevant terms. Not Band 6: Lacks 'conflict', 'compromise', 'efficient', 'productive'.",
    grammar_reason="[GRA6] Reason: 'So you argue'. Contrast: 'Also, some people...'. >Band 5: Error-free sentences. Not Band 7: Simple sentence structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 188: V5/G6 - Topic: Education (Teacher)
samples.append(create_sample(
    index=188,
    vocab_band=5,
    grammar_band=6,
    question="Can computers replace teachers?",
    transcript="No, never. Computers are smart, but they have no feelings. A teacher cares about the student. They understand if a student is sad or tired. A computer cannot do that. Also, a teacher can explain things in different ways. Computers just give answers. We need human connection.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'human connection' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'smart', 'feelings', 'cares', 'explain', 'answers', 'connection'. >Band 4: Good range. Not Band 6: Lacks 'empathy', 'adapt', 'guide', 'interact'.",
    grammar_reason="[GRA6] Contrast: 'But they have no feelings'. Conditionals: 'If a student is sad...'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="low"
))

# Sample 189: V5/G6 - Topic: Culture (Global)
samples.append(create_sample(
    index=189,
    vocab_band=5,
    grammar_band=6,
    question="Is it good to have a global culture?",
    transcript="It has good and bad points. Good point is we understand each other. Less fighting. Bad point is we lose local tradition. Everyone wears the same clothes. Eats the same food. The world becomes boring. I think we should keep our own culture, but respect others.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'good point is' (simple)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'understand', 'fighting', 'tradition', 'boring', 'respect', 'own'. >Band 4: Clear meaning. Not Band 6: Lacks 'unique', 'diversity', 'homogenous', 'identity'.",
    grammar_reason="[GRA6] Contrast: 'But respect others'. Comparison: 'Same clothes... Same food'. >Band 5: Correct grammar. Not Band 7: Repetitive structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 190: V5/G6 - Topic: Society (Media)
samples.append(create_sample(
    index=190,
    vocab_band=5,
    grammar_band=6,
    question="Should the government control the media?",
    transcript="This is dangerous. If government controls news, we don't know the truth. They only show good things. Hide bad things. This is not democracy. People need to know what is happening. But media should not tell lies. Fake news is bad. So maybe some rules are needed.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'hide bad things' (simple)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'dangerous', 'news', 'truth', 'democracy', 'lies', 'rules'. >Band 4: Specific terms. Not Band 6: Lacks 'censorship', 'freedom of speech', 'unbiased', 'regulate'.",
    grammar_reason="[GRA6] Conditionals: 'If government controls news...'. Contrast: 'But media should not...'. >Band 5: Good control. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 191: V5/G6 - Topic: Health (Sleep)
samples.append(create_sample(
    index=191,
    vocab_band=5,
    grammar_band=6,
    question="Do people sleep enough these days?",
    transcript="No, they don't. People are very busy. They work late. Also, technology stops them sleeping. Phones and computers have blue light. It wakes up the brain. So people sleep late. In the morning, they are tired. This is bad for health. We need more rest.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'wakes up the brain' (simple)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'busy', 'technology', 'blue light', 'brain', 'tired', 'rest'. >Band 4: Relevant vocabulary. Not Band 6: Lacks 'deprivation', 'insomnia', 'schedule', 'recover'.",
    grammar_reason="[GRA6] Reason: 'So people sleep late'. Description: 'It wakes up the brain'. >Band 5: Error-free sentences. Not Band 7: Simple phrasing.",
    idiom_present=False,
    risk_level="low"
))

# Sample 192: V5/G6 - Topic: Environment (Plastic)
samples.append(create_sample(
    index=192,
    vocab_band=5,
    grammar_band=6,
    question="Should we ban plastic bags?",
    transcript="Yes, I think so. Plastic bags are terrible for nature. Animals eat them and die. They stay in the ground for a long time. Paper bags are better. Or bring your own bag. Many countries already banned them. It is a small change, but it helps a lot.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'stay in the ground' (simple)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'nature', 'animals', 'die', 'ground', 'better', 'change'. >Band 4: Clear meaning. Not Band 6: Lacks 'decompose', 'pollution', 'environment', 'alternative'.",
    grammar_reason="[GRA6] Contrast: 'But it helps a lot'. Comparison: 'Paper bags are better'. >Band 5: Accurate grammar. Not Band 7: Limited complexity.",
    idiom_present=False,
    risk_level="low"
))

# Sample 193: V5/G6 - Topic: Travel (Adventure)
samples.append(create_sample(
    index=193,
    vocab_band=5,
    grammar_band=6,
    question="Why do people like adventure holidays?",
    transcript="Because they are boring with normal life. They want excitement. Climbing mountains or diving in the sea. It makes them feel alive. Also, they want to test themselves. See how strong they are. It is dangerous, but that is the fun part. Good story to tell friends.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'boring with normal life' -> 'bored with normal life'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'excitement', 'climbing', 'diving', 'alive', 'test', 'dangerous'. >Band 4: Specific words. Not Band 6: Lacks 'challenge', 'adrenaline', 'experience', 'routine'.",
    grammar_reason="[GRA6] Reason: 'Because they are...'. Contrast: 'But that is the fun part'. >Band 5: Good structure. Not Band 7: Adjective error (boring/bored).",
    idiom_present=False,
    risk_level="low"
))

# Sample 194: V5/G6 - Topic: Work (Robots)
samples.append(create_sample(
    index=194,
    vocab_band=5,
    grammar_band=6,
    question="Will robots make us lazy?",
    transcript="Maybe yes. If robots do everything, we do nothing. We don't clean or cook. We don't walk. Just sit. Our bodies will get weak. Our brains will get slow. Technology should help us, not replace us. We must stay active. Use robots, but do work too.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'get weak' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'lazy', 'clean', 'cook', 'weak', 'slow', 'active'. >Band 4: Relevant terms. Not Band 6: Lacks 'dependent', 'sedentary', 'mental', 'physical'.",
    grammar_reason="[GRA6] Conditionals: 'If robots do everything...'. Modals: 'Must stay active'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 195: V5/G6 - Topic: Education (Art)
samples.append(create_sample(
    index=195,
    vocab_band=5,
    grammar_band=6,
    question="Is art class important?",
    transcript="Yes, it is. School is not just about facts. Art helps children be creative. They can express their feelings. Draw or paint. It is relaxing. Also, some children are good at art, not math. They need a chance to shine. Art makes school fun.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'chance to shine' (idiomatic)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'facts', 'creative', 'express', 'relaxing', 'shine', 'fun'. >Band 4: Good range. Not Band 6: Lacks 'imagination', 'talent', 'curriculum', 'subject'.",
    grammar_reason="[GRA6] Reason: 'Art helps children...'. Contrast: 'Not math'. >Band 5: Correct grammar. Not Band 7: Simple sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 196: V5/G6 - Topic: Society (Rich and Poor)
samples.append(create_sample(
    index=196,
    vocab_band=5,
    grammar_band=6,
    question="Why is there a gap between rich and poor?",
    transcript="This is a complex problem. Some people are born rich. They have good education and connections. Poor people have no chance. They work hard but get low pay. Also, the system is not fair. Rich people keep money. Poor people pay tax. Government should help the poor more.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'keep money' (simple)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'complex', 'connections', 'chance', 'pay', 'system', 'tax'. >Band 4: Relevant vocabulary. Not Band 6: Lacks 'inequality', 'opportunity', 'wealth', 'distribute'.",
    grammar_reason="[GRA6] Contrast: 'They work hard but get low pay'. Modals: 'Government should help'. >Band 5: Accurate structure. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="low"
))

# Sample 197: V5/G6 - Topic: Technology (Space)
samples.append(create_sample(
    index=197,
    vocab_band=5,
    grammar_band=6,
    question="Is space exploration a waste of money?",
    transcript="Many people say yes. We have problems on Earth. Hunger and poverty. We should spend money here. But space is important too. We learn new things. Maybe find a new home. Also technology from space helps us. Satellite and GPS. So it is not a total waste.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'find a new home' (simple)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'hunger', 'poverty', 'spend', 'new home', 'satellite', 'GPS'. >Band 4: Specific terms. Not Band 6: Lacks 'investment', 'scientific', 'benefit', 'research'.",
    grammar_reason="[GRA6] Contrast: 'But space is important'. Reason: 'So it is not a total waste'. >Band 5: Good grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="low"
))

# Sample 198: V5/G6 - Topic: Culture (Fashion)
samples.append(create_sample(
    index=198,
    vocab_band=5,
    grammar_band=6,
    question="Why does fashion change so quickly?",
    transcript="Because companies want money. If fashion stays the same, we don't buy new clothes. They make new styles every season. Also, people get bored. They want to look different. Look cool. Famous people wear new things, and we copy them. It is a cycle.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'look cool' (simple)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'companies', 'season', 'bored', 'styles', 'famous', 'copy'. >Band 4: Clear meaning. Not Band 6: Lacks 'industry', 'trend', 'consumer', 'influence'.",
    grammar_reason="[GRA6] Conditionals: 'If fashion stays the same...'. Reason: 'Because companies want money'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 199: V5/G6 - Topic: Transport (Cities)
samples.append(create_sample(
    index=199,
    vocab_band=5,
    grammar_band=6,
    question="Should cars be banned from city centers?",
    transcript="I agree with this. City centers are too crowded. Dangerous for walking. If we ban cars, air will be clean. People can walk and shop. Shops will make more money. We can use buses or trams. It is better for everyone. Quiet and safe.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'make more money' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'crowded', 'dangerous', 'ban', 'clean', 'trams', 'quiet'. >Band 4: Relevant terms. Not Band 6: Lacks 'pedestrian', 'zone', 'pollution', 'environment'.",
    grammar_reason="[GRA6] Conditionals: 'If we ban cars...'. Reason: 'It is better for everyone'. >Band 5: Correct grammar. Not Band 7: Simple structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 200: V5/G6 - Topic: Society (Success)
samples.append(create_sample(
    index=200,
    vocab_band=5,
    grammar_band=6,
    question="How do you define success?",
    transcript="Money is not success. Rich people can be sad. Success is being happy. Doing what you love. Having a good family and friends. Also health. If you are sick, money is useless. I think if you feel good about your life, you are successful.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'money is useless' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'rich', 'sad', 'happy', 'love', 'useless', 'successful'. >Band 4: Clear meaning. Not Band 6: Lacks 'fulfillment', 'achieve', 'content', 'wealth'.",
    grammar_reason="[GRA6] Conditionals: 'If you are sick...', 'If you feel good...'. >Band 5: Accurate complex sentences. Not Band 7: Repetitive sentence patterns.",
    idiom_present=False,
    risk_level="low"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
