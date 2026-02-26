import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch04.jsonl")

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

# --- BATCH 04 PART 4: SAMPLES 326-350 (25 Total) ---
# Combo: V6/G6

# Sample 326: V6/G6 - Topic: Culture (Language)
samples.append(create_sample(
    index=326,
    vocab_band=6,
    grammar_band=6,
    question="Why do some people learn dead languages?",
    transcript="It is for academic interest. Languages like Latin or Ancient Greek. They help us understand history. You can read old texts. Also, it helps with other languages. Many English words come from Latin. It is a mental challenge. Like a puzzle. It keeps the brain active. It is not useful for travel, but good for knowledge.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'academic interest' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'academic', 'interest', 'texts', 'mental challenge', 'puzzle', 'active', 'knowledge'. >Band 5: Precise vocabulary. Not Band 7: Lacks 'etymology', 'derivative', 'cognitive', 'intellectual'.",
    grammar_reason="[GRA6] Contrast: 'It is not useful..., but good...'. Reason: 'It helps with...'. >Band 5: Accurate grammar. Not Band 7: Simple sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 327: V6/G6 - Topic: Society (Cities)
samples.append(create_sample(
    index=327,
    vocab_band=6,
    grammar_band=6,
    question="What makes a city safe?",
    transcript="Good lighting is important. Dark streets are scary. Also, police presence. If people see police, they feel safe. Community is key too. If neighbors know each other, they look out for each other. Low crime rate. Jobs are also important. If people have money, they don't steal. A safe city is a happy city.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'look out for each other' (phrasal verb)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'lighting', 'presence', 'community', 'look out for', 'crime rate', 'steal'. >Band 5: Relevant terms. Not Band 7: Lacks 'surveillance', 'prevention', 'poverty', 'employment'.",
    grammar_reason="[GRA6] Conditionals: 'If people see police...', 'If people have money...'. >Band 5: Accurate grammar. Not Band 7: Repetitive 'If...' structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 328: V6/G6 - Topic: Technology (Computer)
samples.append(create_sample(
    index=328,
    vocab_band=6,
    grammar_band=6,
    question="Will computers ever be smarter than humans?",
    transcript="They are already faster. They can calculate huge numbers in a second. They remember everything. But 'smart' is different. Humans have creativity and feelings. We can imagine new things. Computers only follow code. Maybe one day AI will learn to think. That is called Singularity. But for now, the human brain is still unique.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Singularity' (advanced term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'calculate', 'huge', 'creativity', 'imagine', 'code', 'Singularity', 'unique'. >Band 5: Good range. Not Band 7: Lacks 'consciousness', 'intuition', 'emotional intelligence', 'superior'.",
    grammar_reason="[GRA6] Contrast: 'But smart is different'. Comparison: 'They are already faster'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 329: V6/G6 - Topic: Work (Leadership)
samples.append(create_sample(
    index=329,
    vocab_band=6,
    grammar_band=6,
    question="How do leaders influence people?",
    transcript="By example. If a leader works hard, the team works hard. They set the standard. Also, by communication. A leader must speak clearly and inspire people. They give a vision. If people believe in the vision, they follow. Good leaders also listen. They care about their staff. Influence comes from respect, not fear.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'set the standard' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'example', 'standard', 'communication', 'inspire', 'vision', 'follow', 'respect'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'motivate', 'delegate', 'integrity', 'authority'.",
    grammar_reason="[GRA6] Conditionals: 'If a leader works hard...'. Contrast: 'respect, not fear'. >Band 5: Accurate grammar. Not Band 7: Simple phrasing.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 330: V6/G6 - Topic: Environment (Climate Change)
samples.append(create_sample(
    index=330,
    vocab_band=6,
    grammar_band=6,
    question="Are individuals responsible for climate change?",
    transcript="We all contribute to it. We drive cars, use electricity, and buy plastic. Our lifestyle causes carbon emissions. So yes, we are responsible. But big companies are worse. They pollute much more than one person. Governments must make rules for them. Individuals can help, but we need systemic change to save the planet.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'systemic change' (advanced term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'contribute', 'lifestyle', 'emissions', 'pollute', 'systemic change', 'planet'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'consumption', 'industrial', 'regulation', 'collective'.",
    grammar_reason="[GRA6] Contrast: 'But big companies are worse'. Comparison: 'much more than'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 331: V6/G6 - Topic: Health (Diet)
samples.append(create_sample(
    index=331,
    vocab_band=6,
    grammar_band=6,
    question="What is the role of diet in health?",
    transcript="It is the foundation. You are what you eat. If you eat junk food, your body gets weak. You get sick easily. A balanced diet gives you energy. Vitamins and minerals are important for the immune system. Food affects your mood too. Sugar makes you tired later. Healthy food makes you strong and happy.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'foundation' (metaphor)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'foundation', 'junk food', 'balanced diet', 'vitamins', 'minerals', 'immune system', 'mood'. >Band 5: Specific terms. Not Band 7: Lacks 'nutrition', 'metabolism', 'impact', 'preventative'.",
    grammar_reason="[GRA6] Conditionals: 'If you eat junk food...'. Reason: 'Food affects your mood'. >Band 5: Accurate grammar. Not Band 7: Simple sentence structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 332: V6/G6 - Topic: Transport (Public)
samples.append(create_sample(
    index=332,
    vocab_band=6,
    grammar_band=6,
    question="How can we improve bus services?",
    transcript="They need to be reliable. People hate waiting. If the bus is late, they drive next time. Dedicated bus lanes help. The bus doesn't get stuck in traffic. Also, comfort. Clean seats and AC. The price should be low. If it is cheap and fast, everyone will use it. It is good for the city.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'stuck in traffic' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'reliable', 'dedicated', 'lanes', 'stuck', 'traffic', 'comfort', 'AC'. >Band 5: Relevant words. Not Band 7: Lacks 'punctual', 'efficient', 'infrastructure', 'incentive'.",
    grammar_reason="[GRA6] Conditionals: 'If the bus is late...', 'If it is cheap...'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 333: V6/G6 - Topic: Culture (Global)
samples.append(create_sample(
    index=333,
    vocab_band=6,
    grammar_band=6,
    question="Why is it important to learn about other cultures?",
    transcript="To avoid prejudice. If you don't know a culture, you might fear it. Learning brings understanding. It promotes peace. Also, it is interesting. Different food, music, and art. It enriches your life. The world is a big place. We should be open-minded. Tolerance is key in a global society.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'prejudice' (advanced word)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'prejudice', 'fear', 'promotes', 'peace', 'enriches', 'open-minded', 'tolerance'. >Band 5: Advanced vocabulary. Not Band 7: Lacks 'diversity', 'perspective', 'stereotype', 'harmony'.",
    grammar_reason="[GRA6] Conditionals: 'If you don't know...'. Reason: 'To avoid prejudice'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 334: V6/G6 - Topic: Education (Skills)
samples.append(create_sample(
    index=334,
    vocab_band=6,
    grammar_band=6,
    question="Should schools teach practical skills?",
    transcript="Yes, definitely. Academic subjects are important, but not enough. Students need life skills. How to cook, how to manage money, how to fix things. These are useful every day. Many graduates know history but cannot pay taxes. Schools should prepare students for real life. Practical skills give confidence and independence.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'manage money' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'academic', 'life skills', 'manage money', 'graduates', 'taxes', 'prepare', 'independence'. >Band 5: Good range. Not Band 7: Lacks 'vocational', 'competence', 'curriculum', 'essential'.",
    grammar_reason="[GRA6] Contrast: 'know history but cannot pay taxes'. Modals: 'Should prepare'. >Band 5: Accurate grammar. Not Band 7: Simple phrasing.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 335: V6/G6 - Topic: Society (Friendship)
samples.append(create_sample(
    index=335,
    vocab_band=6,
    grammar_band=6,
    question="Is it better to have many friends or a few close ones?",
    transcript="A few close friends is better. Quality over quantity. You can have fun with many people, but trust is rare. Close friends help you in trouble. They know you well. Shallow friendships fade away. It takes energy to maintain friendship. Focusing on a few good people is more rewarding. They are like family.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Quality over quantity' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'quantity', 'trust', 'rare', 'shallow', 'fade away', 'maintain', 'rewarding'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'bond', 'intimacy', 'superficial', 'support system'.",
    grammar_reason="[GRA6] Contrast: 'but trust is rare'. Comparison implied. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 336: V6/G6 - Topic: Technology (Games)
samples.append(create_sample(
    index=336,
    vocab_band=6,
    grammar_band=6,
    question="Are video games a waste of time?",
    transcript="Not always. They are entertainment, like watching a movie. People need to relax. Some games are social. You play with friends online. It is a hobby. However, addiction is real. If you play for 10 hours, it is a waste. You ignore real life. Moderation is the answer. Enjoy it, but don't let it control you.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Moderation is the answer' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'entertainment', 'relax', 'social', 'hobby', 'addiction', 'ignore', 'moderation', 'control'. >Band 5: Relevant terms. Not Band 7: Lacks 'leisure', 'excessive', 'escapism', 'virtual'.",
    grammar_reason="[GRA6] Conditionals: 'If you play...'. Contrast: 'However'. >Band 5: Accurate grammar. Not Band 7: Simple sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 337: V6/G6 - Topic: Work (Gender)
samples.append(create_sample(
    index=337,
    vocab_band=6,
    grammar_band=6,
    question="Why are some jobs dominated by one gender?",
    transcript="It is tradition and culture. Nurses are often women because they are seen as caring. Construction workers are men because of physical strength. But this is changing. Stereotypes are breaking. Women can be engineers. Men can be nurses. It is about ability, not gender. We should encourage people to follow their passion, not society's rules.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Stereotypes are breaking' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'dominated', 'tradition', 'caring', 'physical strength', 'stereotypes', 'ability', 'encourage', 'passion'. >Band 5: Good topic words. Not Band 7: Lacks 'bias', 'perception', 'equality', 'barrier'.",
    grammar_reason="[GRA6] Reason: 'because they are seen as caring'. Contrast: 'But this is changing'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 338: V6/G6 - Topic: Environment (Energy)
samples.append(create_sample(
    index=338,
    vocab_band=6,
    grammar_band=6,
    question="What is the future of energy?",
    transcript="We must move to renewable energy. Fossil fuels will run out. Solar and wind are the future. Technology is improving. Batteries are getting better. We can store energy now. Nuclear power is also an option, but people are scared of it. Clean energy is essential to stop climate change. It will be cheaper in the long run.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'in the long run' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'renewable', 'fossil fuels', 'run out', 'batteries', 'store', 'nuclear power', 'essential', 'cheaper'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'sustainable', 'emissions', 'alternative', 'efficiency'.",
    grammar_reason="[GRA6] Contrast: 'but people are scared'. Future forms: 'Will run out', 'Will be'. >Band 5: Accurate grammar. Not Band 7: Simple phrasing.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 339: V6/G6 - Topic: Transport (Cars)
samples.append(create_sample(
    index=339,
    vocab_band=6,
    grammar_band=6,
    question="Should we encourage carpooling?",
    transcript="Yes, it is a great idea. It reduces the number of cars on the road. Less traffic and less pollution. It also saves money. You share the cost of gas. It can be social too. You talk to people on the way to work. Companies should reward carpooling. Give special parking spots. It is a simple way to help the environment.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'special parking spots' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'carpooling', 'reduces', 'traffic', 'pollution', 'share', 'cost', 'reward', 'environment'. >Band 5: Specific terms. Not Band 7: Lacks 'commute', 'initiative', 'incentive', 'emissions'.",
    grammar_reason="[GRA6] Reason: 'It reduces the number...'. Modals: 'Should reward'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 340: V6/G6 - Topic: Society (Shopping)
samples.append(create_sample(
    index=340,
    vocab_band=6,
    grammar_band=6,
    question="Is shopping a hobby?",
    transcript="For many people, yes. It is called retail therapy. Buying new things makes them happy. It is exciting to find a bargain. Walking in the mall is exercise too. But it can be a bad hobby. You spend too much money. You buy things you don't need. It creates waste. I think hobbies should be creative, like painting or cooking.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'retail therapy' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'retail therapy', 'exciting', 'bargain', 'mall', 'waste', 'creative'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'consumerism', 'materialistic', 'leisure', 'debt'.",
    grammar_reason="[GRA6] Contrast: 'But it can be...'. Reason: 'It creates waste'. >Band 5: Accurate grammar. Not Band 7: Simple sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 341: V6/G6 - Topic: Culture (Tradition)
samples.append(create_sample(
    index=341,
    vocab_band=6,
    grammar_band=6,
    question="How do traditions affect young people?",
    transcript="Some young people find them boring. They want to be modern. They reject old customs. But others value them. Traditions give a sense of belonging. Knowing your roots is important. It gives confidence. I think we need to make traditions relevant. Adapt them for the new generation. If we don't, they will die out.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'sense of belonging' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'boring', 'modern', 'reject', 'customs', 'value', 'belonging', 'roots', 'relevant', 'adapt', 'die out'. >Band 5: Good range. Not Band 7: Lacks 'identity', 'heritage', 'continuity', 'perspectives'.",
    grammar_reason="[GRA6] Conditionals: 'If we don't...'. Contrast: 'But others value them'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 342: V6/G6 - Topic: Education (University)
samples.append(create_sample(
    index=342,
    vocab_band=6,
    grammar_band=6,
    question="Why do students study abroad?",
    transcript="To get a better education. Some universities abroad are famous. Also, to learn a language. Immersion is the best way. It is an adventure. You meet people from all over the world. You learn independence. Living alone in a foreign country is hard but rewarding. It looks good on a CV. Employers like international experience.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'looks good on a CV' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'abroad', 'famous', 'immersion', 'adventure', 'independence', 'foreign', 'rewarding', 'CV', 'employers'. >Band 5: Relevant terms. Not Band 7: Lacks 'prestige', 'cultural exchange', 'perspective', 'career'.",
    grammar_reason="[GRA6] Contrast: 'hard but rewarding'. Reason: 'To get a better education'. >Band 5: Accurate grammar. Not Band 7: Simple phrasing.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 343: V6/G6 - Topic: Health (Mental)
samples.append(create_sample(
    index=343,
    vocab_band=6,
    grammar_band=6,
    question="How can we help people with mental health issues?",
    transcript="First, we need to talk about it. Remove the stigma. It is okay not to be okay. We should listen to them without judgment. Professional help is important. Therapy and counseling. Governments should fund mental health services. Make it free or cheap. Friends and family support is key. Just being there for someone can save a life.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Remove the stigma' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'stigma', 'judgment', 'professional', 'therapy', 'counseling', 'fund', 'services', 'support'. >Band 5: Advanced vocabulary. Not Band 7: Lacks 'awareness', 'psychological', 'treatment', 'resources'.",
    grammar_reason="[GRA6] Modals: 'Should listen', 'Should fund'. Purpose: 'To talk about it'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 344: V6/G6 - Topic: Transport (Flying)
samples.append(create_sample(
    index=344,
    vocab_band=6,
    grammar_band=6,
    question="Why is flying stressful?",
    transcript="Airports are crowded and noisy. There are long queues for security. You have to take off your shoes and belt. It is annoying. Then, the plane is small. Legroom is tight. You cannot move. Delays happen often. Missing a connection is a nightmare. Also, some people are afraid of flying. Turbulence scares them. It is not a relaxing experience.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'nightmare' (metaphor)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'crowded', 'queues', 'security', 'annoying', 'legroom', 'tight', 'delays', 'connection', 'nightmare', 'turbulence'. >Band 5: Specific terms. Not Band 7: Lacks 'claustrophobic', 'anxiety', 'procedure', 'inconvenience'.",
    grammar_reason="[GRA6] Sequencing: 'Then, the plane...'. Reason: 'It is annoying'. >Band 5: Accurate grammar. Not Band 7: Simple sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 345: V6/G6 - Topic: Society (Cities)
samples.append(create_sample(
    index=345,
    vocab_band=6,
    grammar_band=6,
    question="What makes a city livable?",
    transcript="Green spaces are number one. Parks and trees improve the air and mood. Also, good public transport. You need to get around easily. Safety is crucial. Low crime rates. Affordable housing is also key. If rent is too high, people are stressed. Culture and entertainment make a city fun. A mix of work and play.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'get around' (phrasal verb)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'livable', 'improve', 'mood', 'public transport', 'crucial', 'crime rates', 'affordable', 'entertainment'. >Band 5: Good range. Not Band 7: Lacks 'infrastructure', 'amenities', 'resident', 'environment'.",
    grammar_reason="[GRA6] Conditionals: 'If rent is too high...'. Reason: 'You need to get around'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 346: V6/G6 - Topic: Technology (Data)
samples.append(create_sample(
    index=346,
    vocab_band=6,
    grammar_band=6,
    question="Is data the new oil?",
    transcript="Yes, it is very valuable. Companies use data to sell things. They know what we like and what we do. This information is power. Google and Facebook are rich because of data. It fuels the digital economy. But unlike oil, data is infinite. We create more every day. We need to protect it, or it will be used against us.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'fuels the digital economy' (metaphor)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'valuable', 'information', 'power', 'fuels', 'digital economy', 'infinite', 'create', 'protect'. >Band 5: Advanced vocabulary. Not Band 7: Lacks 'resource', 'commodity', 'exploit', 'regulation'.",
    grammar_reason="[GRA6] Contrast: 'But unlike oil...'. Reason: 'because of data'. >Band 5: Accurate grammar. Not Band 7: Simple structure.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 347: V6/G6 - Topic: Work (Job)
samples.append(create_sample(
    index=347,
    vocab_band=6,
    grammar_band=6,
    question="Why is it hard to find a job?",
    transcript="Competition is high. There are many graduates for one position. Companies want experience, but young people don't have it. It is a cycle. Also, technology changes fast. Skills become old quickly. You need to keep learning. Networking is important too. Many jobs are not advertised. You need to know someone. It takes patience and persistence.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'It is a cycle' (referring to vicious cycle)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'competition', 'graduates', 'position', 'experience', 'networking', 'advertised', 'patience', 'persistence'. >Band 5: Good topic words. Not Band 7: Lacks 'market', 'qualification', 'obsolete', 'adapt'.",
    grammar_reason="[GRA6] Contrast: 'Companies want..., but...'. Reason: 'There are many...'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 348: V6/G6 - Topic: Culture (Art)
samples.append(create_sample(
    index=348,
    vocab_band=6,
    grammar_band=6,
    question="Is graffiti art or vandalism?",
    transcript="It depends on the context. If it is a beautiful picture on a legal wall, it is art. It takes skill and talent. Banksy is a famous artist. But if it is just a tag on a private house, it is vandalism. It looks messy and costs money to clean. Street art can improve a city, but tagging destroys it.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'tag' (correct slang)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'context', 'legal', 'skill', 'talent', 'tag', 'vandalism', 'messy', 'improve', 'destroys'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'expression', 'property', 'permission', 'aesthetic'.",
    grammar_reason="[GRA6] Conditionals: 'If it is...', 'But if it is...'. Contrast: 'Street art can..., but...'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 349: V6/G6 - Topic: Environment (Climate)
samples.append(create_sample(
    index=349,
    vocab_band=6,
    grammar_band=6,
    question="Will we solve climate change?",
    transcript="I am hopeful but worried. We have the technology. Solar, wind, electric cars. But we lack political will. Leaders talk but don't act. Money is still more important than nature. People are waking up, though. Young people are protesting. If we act fast, we can save the planet. If we wait, it will be too late.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'political will' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'hopeful', 'technology', 'lack', 'political will', 'nature', 'waking up', 'protesting', 'planet'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'commitment', 'crisis', 'consequences', 'urgent'.",
    grammar_reason="[GRA6] Conditionals: 'If we act fast...', 'If we wait...'. Contrast: 'But we lack...'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 350: V6/G6 - Topic: Education (Teacher)
samples.append(create_sample(
    index=350,
    vocab_band=6,
    grammar_band=6,
    question="Should teachers be paid more?",
    transcript="Yes, absolutely. Teaching is a hard job. They shape the future generation. They work long hours, marking papers and planning lessons. But their salary is often low. This is unfair. If we want good teachers, we must pay them well. Otherwise, smart people will choose other jobs. Education is the most important investment for a country.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'shape the future' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'shape', 'generation', 'marking', 'salary', 'unfair', 'choose', 'investment'. >Band 5: Good range. Not Band 7: Lacks 'profession', 'responsibility', 'undervalued', 'incentive'.",
    grammar_reason="[GRA6] Conditionals: 'If we want good teachers...'. Reason: 'This is unfair'. >Band 5: Accurate grammar. Not Band 7: Simple structure.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
