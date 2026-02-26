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

# --- BATCH 03 PART 1: SAMPLES 151-175 (25 Total) ---
# Combo: V5/G6 (Modest Vocab, Competent Grammar)

# Sample 151: V5/G6 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=151,
    vocab_band=5,
    grammar_band=6,
    question="Why do some people not recycle?",
    transcript="I think there are a few reasons. Firstly, some people are lazy. They don't want to separate their trash because it takes time. Secondly, maybe they don't know how to recycle correctly. The rules can be confusing. Also, in some places, there are no bins nearby. If the government made it easier, more people would do it.",
    response_type="extended",
    micro_flaws=[
        "singular/plural: 'there are no bins' (correct) but 'trash' is general",
        "phrase error: 'rules can be confusing' (good grammar)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'separate', 'trash', 'bins', 'recycle', 'government'. >Band 4: Uses relevant terms. Not Band 6: Lacks 'inconvenient', 'facilities', 'incentive', 'awareness'.",
    grammar_reason="[GRA6] Mix of simple and complex structures. 'Because it takes time' (reason). 'If the government made it easier...' (conditional). >Band 5: Good control of complex sentences. Not Band 7: Structures are relatively simple though accurate.",
    idiom_present=False,
    risk_level="low"
))

# Sample 152: V5/G6 - Topic: Technology (Social Media)
samples.append(create_sample(
    index=152,
    vocab_band=5,
    grammar_band=6,
    question="Is social media a waste of time?",
    transcript="It depends on how you use it. For some people, it is very useful. They can talk to friends and find information. But for others, it is bad. They spend hours looking at photos. They don't do their work. I think we need to balance it. If we use it too much, we will have problems.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'balance it' (correct)",
        "verb construction: 'spend hours looking' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'useful', 'information', 'photos', 'balance', 'problems'. >Band 4: Clear meaning. Not Band 6: Lacks 'platform', 'content', 'addiction', 'productivity'.",
    grammar_reason="[GRA6] Uses complex structures: 'It depends on how...', 'If we use it too much...'. >Band 5: Frequent error-free sentences. Not Band 7: Range is somewhat limited.",
    idiom_present=False,
    risk_level="low"
))

# Sample 153: V5/G6 - Topic: Education (University)
samples.append(create_sample(
    index=153,
    vocab_band=5,
    grammar_band=6,
    question="Should university be free?",
    transcript="This is a difficult question. On one hand, education is important for everyone. If it is free, poor students can study. This is good for society. On the other hand, universities need money. Teachers need salary. If government pays everything, tax will be high. So maybe low cost is better than free.",
    response_type="extended",
    micro_flaws=[
        "singular/plural: 'tax will be high' -> 'taxes will be high'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'education', 'society', 'salary', 'tax', 'cost'. >Band 4: Specific terms. Not Band 6: Lacks 'funding', 'tuition', 'opportunity', 'investment'.",
    grammar_reason="[GRA6] Uses connectors: 'On one hand... On the other hand'. Conditionals: 'If government pays...'. >Band 5: Good control. Not Band 7: Some minor errors or simple phrasing.",
    idiom_present=False,
    risk_level="low"
))

# Sample 154: V5/G6 - Topic: Work (Remote)
samples.append(create_sample(
    index=154,
    vocab_band=5,
    grammar_band=6,
    question="Is working from home better than working in an office?",
    transcript="I prefer working from home. It is more comfortable. I don't need to travel, so I save time. Also, I can wear casual clothes. But the office has benefits too. You can see your colleagues. It is easier to talk. Sometimes at home, I feel lonely. So both have good points.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'save time' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'comfortable', 'travel', 'casual clothes', 'colleagues', 'lonely'. >Band 4: Relevant words. Not Band 6: Lacks 'environment', 'commute', 'socialize', 'flexibility'.",
    grammar_reason="[GRA6] Mix of simple and complex. 'I don't need to travel, so I save time'. 'It is easier to talk'. >Band 5: Accurate use of basic complex forms. Not Band 7: Lacks sophistication.",
    idiom_present=False,
    risk_level="low"
))

# Sample 155: V5/G6 - Topic: Health (Exercise)
samples.append(create_sample(
    index=155,
    vocab_band=5,
    grammar_band=6,
    question="How can people stay healthy?",
    transcript="The most important thing is exercise. We should do sport like running or swimming. It makes our body strong. Also, food is important. We need to eat fruit and vegetable. Not too much sugar. Drinking water helps too. If we have a healthy lifestyle, we will not get sick easily.",
    response_type="extended",
    micro_flaws=[
        "singular/plural: 'fruit and vegetable' -> 'fruit and vegetables'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'sport', 'strong', 'sugar', 'lifestyle', 'sick'. >Band 4: Good range. Not Band 6: Lacks 'nutritious', 'diet', 'fitness', 'maintain'.",
    grammar_reason="[GRA6] Modals: 'should do'. Conditionals: 'If we have...'. >Band 5: Error-free sentences are frequent. Not Band 7: Vocabulary limits the complexity of grammar used.",
    idiom_present=False,
    risk_level="low"
))

# Sample 156: V5/G6 - Topic: Society (Crime)
samples.append(create_sample(
    index=156,
    vocab_band=5,
    grammar_band=6,
    question="How can we stop crime?",
    transcript="I think education is the key. If people have good jobs, they don't need to steal. So schools should teach skills. Also, police are important. If there are more police on the street, criminals will be scared. Punishment should be strict too. People need to know that crime is bad.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'police are' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'steal', 'skills', 'criminals', 'scared', 'punishment', 'strict'. >Band 4: Relevant terms. Not Band 6: Lacks 'prevention', 'opportunity', 'deterrent', 'consequence'.",
    grammar_reason="[GRA6] Conditionals: 'If people have...', 'If there are more police...'. >Band 5: Complex structures used correctly. Not Band 7: Repetitive sentence patterns.",
    idiom_present=False,
    risk_level="low"
))

# Sample 157: V5/G6 - Topic: Culture (Language)
samples.append(create_sample(
    index=157,
    vocab_band=5,
    grammar_band=6,
    question="Why do people learn foreign languages?",
    transcript="There are many reasons. Some people want to travel. If they speak the language, it is easy to travel. Others need it for work. English is useful for business. Also, some people like culture. They want to understand movies or songs. Learning a language opens new doors for them.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'opens new doors' (idiomatic but common)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'travel', 'business', 'culture', 'understand', 'useful'. >Band 4: Clear meaning. Not Band 6: Lacks 'communicate', 'career', 'opportunity', 'fluency'.",
    grammar_reason="[GRA6] Conditionals: 'If they speak...'. Reason: 'Others need it for work'. >Band 5: Accurate basic complex structures. Not Band 7: Sentences are not very long or varied.",
    idiom_present=False,
    risk_level="low"
))

# Sample 158: V5/G6 - Topic: Transport (Cars)
samples.append(create_sample(
    index=158,
    vocab_band=5,
    grammar_band=6,
    question="What are the problems with private cars?",
    transcript="The main problem is traffic. There are too many cars in the city. This causes jams every day. Another problem is pollution. Cars make the air dirty. This is bad for our health. Also, cars are expensive to buy and fix. Public transport is a better choice for many people.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'make the air dirty' (simple)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'traffic', 'jams', 'pollution', 'dirty', 'expensive', 'fix'. >Band 4: Specific terms. Not Band 6: Lacks 'congestion', 'emission', 'maintenance', 'alternative'.",
    grammar_reason="[GRA6] Sequencing: 'The main problem...', 'Another problem...'. >Band 5: Clear organization with accurate grammar. Not Band 7: Limited range of complex features.",
    idiom_present=False,
    risk_level="low"
))

# Sample 159: V5/G6 - Topic: Environment (Global Warming)
samples.append(create_sample(
    index=159,
    vocab_band=5,
    grammar_band=6,
    question="Is global warming real?",
    transcript="Yes, definitely. The weather is changing. Summers are hotter than before. We can see ice melting in the north. This is because of human activity. We burn oil and coal. If we don't stop, it will get worse. We need to protect our planet for the future.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'in the north' (referring to Arctic)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'weather', 'hotter', 'melting', 'human activity', 'burn', 'planet'. >Band 4: Relevant vocabulary. Not Band 6: Lacks 'evidence', 'temperature', 'fossil fuels', 'severe'.",
    grammar_reason="[GRA6] Comparison: 'Summers are hotter'. Conditionals: 'If we don't stop...'. >Band 5: Good control. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="low"
))

# Sample 160: V5/G6 - Topic: Society (Children)
samples.append(create_sample(
    index=160,
    vocab_band=5,
    grammar_band=6,
    question="Do children have too much freedom today?",
    transcript="I think so. Parents let them do what they want. They play games all day. They don't help in the house. In the past, children had rules. They respected older people. Now, children argue a lot. I believe discipline is important. Parents should be stricter.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'help in the house' (common)",
        "phrase error: 'old people' -> 'older people' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'freedom', 'rules', 'respect', 'argue', 'discipline', 'strict'. >Band 4: Specific terms. Not Band 6: Lacks 'independence', 'responsibility', 'behavior', 'lenient'.",
    grammar_reason="[GRA6] Comparison: 'In the past... Now...'. Modals: 'Parents should be stricter'. >Band 5: Clear time frames. Not Band 7: Short sentences mostly.",
    idiom_present=False,
    risk_level="low"
))

# Sample 161: V5/G6 - Topic: Technology (Robots)
samples.append(create_sample(
    index=161,
    vocab_band=5,
    grammar_band=6,
    question="What jobs will robots do in the future?",
    transcript="Robots will do many jobs. Especially dangerous jobs. For example, working in fire or deep sea. They can also do boring jobs. Like in a factory. This is good because humans can do creative work. However, some people might lose their jobs. We need to be careful about this.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'working in fire' -> 'fighting fires'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'dangerous', 'factory', 'creative', 'lose their jobs', 'careful'. >Band 4: Good range. Not Band 6: Lacks 'repetitive', 'manual labor', 'replace', 'artificial intelligence'.",
    grammar_reason="[GRA6] Future tense: 'Robots will do'. Contrast: 'However, some people...'. >Band 5: Accurate structure. Not Band 7: Simple connectors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 162: V5/G6 - Topic: Education (Online)
samples.append(create_sample(
    index=162,
    vocab_band=5,
    grammar_band=6,
    question="Is it better to study online or in a classroom?",
    transcript="I think the classroom is better. You can see the teacher. If you have a question, you ask immediately. Also, you learn with other students. It is more fun. Online study is lonely. You just look at a screen. Maybe for adults it is okay, but for children, school is best.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'ask immediately' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'classroom', 'immediately', 'lonely', 'screen', 'adults'. >Band 4: Clear meaning. Not Band 6: Lacks 'interaction', 'environment', 'socialize', 'independent'.",
    grammar_reason="[GRA6] Conditionals: 'If you have a question...'. Comparison: 'Classroom is better'. >Band 5: Error-free sentences. Not Band 7: Basic complex structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 163: V5/G6 - Topic: Work (Salary)
samples.append(create_sample(
    index=163,
    vocab_band=5,
    grammar_band=6,
    question="Why do some jobs pay more than others?",
    transcript="It depends on the skill. If a job is difficult, the pay is high. For example, doctors study for many years. Their job is important. They save lives. But cleaners do simple work. Anyone can do it. So the salary is low. I think this is fair.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'pay is high' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'skill', 'difficult', 'pay', 'cleaners', 'salary', 'fair'. >Band 4: Relevant terms. Not Band 6: Lacks 'qualification', 'responsibility', 'demand', 'profession'.",
    grammar_reason="[GRA6] Conditionals: 'If a job is difficult...'. Reason: 'So the salary is low'. >Band 5: Logical connections. Not Band 7: Repetitive structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 164: V5/G6 - Topic: Culture (Festivals)
samples.append(create_sample(
    index=164,
    vocab_band=5,
    grammar_band=6,
    question="Are festivals important for a country?",
    transcript="Yes, very important. They show our history and culture. People come together to celebrate. It is a happy time. Also, tourists like festivals. They come to watch and spend money. This helps the economy. Without festivals, life would be boring. We need to keep our traditions alive.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'keep our traditions alive' (idiomatic)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'history', 'celebrate', 'tourists', 'economy', 'boring', 'traditions'. >Band 4: Good range. Not Band 6: Lacks 'heritage', 'unite', 'identity', 'preserve'.",
    grammar_reason="[GRA6] Conditionals: 'Without festivals...'. Purpose: 'Come to watch'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 165: V5/G6 - Topic: Society (Shopping)
samples.append(create_sample(
    index=165,
    vocab_band=5,
    grammar_band=6,
    question="Why do people like buying brand name products?",
    transcript="I think it is about status. If you have a famous brand, people think you are rich. It makes you feel good. Also, the quality is usually better. It lasts longer. But sometimes, it is just a waste of money. You pay for the name, not the product.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'waste of money' (common)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'status', 'brand', 'rich', 'quality', 'waste of money'. >Band 4: Specific terms. Not Band 6: Lacks 'image', 'reputation', 'expensive', 'materialistic'.",
    grammar_reason="[GRA6] Conditionals: 'If you have...'. Contrast: 'But sometimes...'. >Band 5: Good control. Not Band 7: Limited flexibility.",
    idiom_present=False,
    risk_level="low"
))

# Sample 166: V5/G6 - Topic: Environment (City)
samples.append(create_sample(
    index=166,
    vocab_band=5,
    grammar_band=6,
    question="How can we make cities better places to live?",
    transcript="We need more green spaces. Parks are good for relaxing. Also, we should reduce traffic. Too many cars make noise and dirt. Public transport should be better. Cheap and fast. If the city is clean and quiet, people will be happier. The government must plan this well.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'dirt' (simple for pollution)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'green spaces', 'relaxing', 'traffic', 'noise', 'public transport', 'government'. >Band 4: Relevant vocabulary. Not Band 6: Lacks 'environment', 'pollution', 'facilities', 'infrastructure'.",
    grammar_reason="[GRA6] Modals: 'We should reduce', 'Must plan'. Conditionals: 'If the city is clean...'. >Band 5: Accurate complex forms. Not Band 7: Simple vocabulary limits grammar range.",
    idiom_present=False,
    risk_level="low"
))

# Sample 167: V5/G6 - Topic: Health (Diet)
samples.append(create_sample(
    index=167,
    vocab_band=5,
    grammar_band=6,
    question="Why is it hard for some people to lose weight?",
    transcript="Because there is too much delicious food. Fast food is everywhere. It is cheap and easy to buy. Also, people are lazy. They don't want to exercise. They sit in offices all day. Losing weight takes hard work. You need to be strong in your mind.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'strong in your mind' (simple for willpower)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'delicious', 'fast food', 'lazy', 'exercise', 'hard work'. >Band 4: Clear meaning. Not Band 6: Lacks 'temptation', 'unhealthy', 'sedentary', 'discipline'.",
    grammar_reason="[GRA6] Reason: 'Because there is...'. Description: 'It is cheap and easy'. >Band 5: Error-free sentences. Not Band 7: Repetitive 'They...' subjects.",
    idiom_present=False,
    risk_level="low"
))

# Sample 168: V5/G6 - Topic: Technology (Games)
samples.append(create_sample(
    index=168,
    vocab_band=5,
    grammar_band=6,
    question="Do video games help children learn?",
    transcript="Some games are educational. They teach math or language. Also, games help with reactions. You have to think fast. But many games are just violent. Fighting and killing. This is not good for children. Parents should check what their kids play. Balance is important.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'reactions' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'educational', 'math', 'violent', 'fighting', 'balance'. >Band 4: Specific terms. Not Band 6: Lacks 'cognitive skills', 'strategy', 'problem solving', 'monitor'.",
    grammar_reason="[GRA6] Contrast: 'But many games...'. Modals: 'Parents should check'. >Band 5: Accurate grammar. Not Band 7: Simple sentence structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 169: V5/G6 - Topic: Society (Old People)
samples.append(create_sample(
    index=169,
    vocab_band=5,
    grammar_band=6,
    question="How should we treat old people?",
    transcript="We should treat them with respect. They have a lot of experience. They worked hard for us. In my country, families look after old parents. It is our duty. We should listen to their stories. But now, some people put them in homes. I think that is sad.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'put them in homes' (referring to nursing homes)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'respect', 'experience', 'duty', 'stories', 'sad'. >Band 4: Good range. Not Band 6: Lacks 'wisdom', 'elderly', 'care', 'generation'.",
    grammar_reason="[GRA6] Modals: 'We should treat', 'We should listen'. Contrast: 'But now...'. >Band 5: Correct grammar. Not Band 7: Limited complexity.",
    idiom_present=False,
    risk_level="low"
))

# Sample 170: V5/G6 - Topic: Travel (Space)
samples.append(create_sample(
    index=170,
    vocab_band=5,
    grammar_band=6,
    question="Will people live on other planets in the future?",
    transcript="Maybe, but not soon. It is very difficult. Space is dangerous and cold. We need air and water. Technology must improve a lot. Also, it is very expensive. Only rich people might go. I think we should fix Earth first. This is our home.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'not soon' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'dangerous', 'technology', 'expensive', 'rich', 'fix'. >Band 4: Relevant terms. Not Band 6: Lacks 'survival', 'environment', 'colonize', 'resource'.",
    grammar_reason="[GRA6] Modals: 'Must improve', 'Might go', 'Should fix'. >Band 5: Good range of modals. Not Band 7: Sentences are short.",
    idiom_present=False,
    risk_level="low"
))

# Sample 171: V5/G6 - Topic: Work (Leadership)
samples.append(create_sample(
    index=171,
    vocab_band=5,
    grammar_band=6,
    question="What makes a good leader?",
    transcript="A good leader must be calm. They shouldn't get angry easily. Also, they need to listen to their team. If there is a problem, they solve it. They must be fair to everyone. Experience is also important. If a leader knows the job, people will respect them.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'There is a problem' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'calm', 'angry', 'team', 'fair', 'respect'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'decisive', 'motivate', 'communicate', 'guidance'.",
    grammar_reason="[GRA6] Conditionals: 'If there is a problem...', 'If a leader knows...'. Modals: 'Must be', 'Need to'. >Band 5: Accurate complex sentences. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="low"
))

# Sample 172: V5/G6 - Topic: Education (Exams)
samples.append(create_sample(
    index=172,
    vocab_band=5,
    grammar_band=6,
    question="Are exams a fair way to test students?",
    transcript="I don't think so. Exams only test memory. If you remember facts, you pass. But some students are smart but nervous. They fail because of stress. This is not fair. Schools should look at work during the year. Projects and homework are better ways to test.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'look at work' (simple)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'memory', 'facts', 'nervous', 'stress', 'fair', 'projects'. >Band 4: Good range. Not Band 6: Lacks 'assess', 'evaluate', 'pressure', 'performance'.",
    grammar_reason="[GRA6] Conditionals: 'If you remember facts...'. Contrast: 'But some students...'. >Band 5: Good control. Not Band 7: Basic connectors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 173: V5/G6 - Topic: Culture (Museums)
samples.append(create_sample(
    index=173,
    vocab_band=5,
    grammar_band=6,
    question="Why do some people find museums boring?",
    transcript="Maybe they are not interested in history. They think old things are dull. Also, some museums are not fun. You just look and read. You cannot touch anything. Young people like action. If museums had interactive things, maybe they would like it more.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'interactive things' (simple)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'interested', 'history', 'dull', 'touch', 'action'. >Band 4: Clear meaning. Not Band 6: Lacks 'exhibit', 'engage', 'display', 'modern'.",
    grammar_reason="[GRA6] Conditionals: 'If museums had interactive things...'. Reason: 'They think old things are dull'. >Band 5: Accurate grammar. Not Band 7: Simple vocabulary limits complexity.",
    idiom_present=False,
    risk_level="low"
))

# Sample 174: V5/G6 - Topic: Transport (Safety)
samples.append(create_sample(
    index=174,
    vocab_band=5,
    grammar_band=6,
    question="How can we make roads safer?",
    transcript="We need stricter rules. Police should stop speeding cars. Drivers who drink alcohol should go to jail. It is very dangerous. Also, we need better roads. Fix the holes. Pedestrians need safe places to walk. If everyone follows the rules, accidents will go down.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'go down' (simple for decrease)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'stricter', 'speeding', 'jail', 'dangerous', 'pedestrians', 'accidents'. >Band 4: Relevant terms. Not Band 6: Lacks 'enforce', 'penalty', 'infrastructure', 'reduce'.",
    grammar_reason="[GRA6] Relative clause: 'Drivers who drink alcohol'. Conditionals: 'If everyone follows...'. >Band 5: Good use of complex features. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 175: V5/G6 - Topic: Environment (Water)
samples.append(create_sample(
    index=175,
    vocab_band=5,
    grammar_band=6,
    question="Why is water important?",
    transcript="Water is life. We cannot live without it. We drink it and clean with it. Farmers need water for food. If there is no water, plants die. Animals die too. We must save water. Don't waste it. It is the most important resource on Earth.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Water is life' (cliché but correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Topic words: 'live', 'clean', 'farmers', 'plants', 'save', 'resource'. >Band 4: Specific words. Not Band 6: Lacks 'essential', 'survive', 'agriculture', 'shortage'.",
    grammar_reason="[GRA6] Conditionals: 'If there is no water...'. Modals: 'Must save'. >Band 5: Accurate grammar. Not Band 7: Very simple sentences.",
    idiom_present=False,
    risk_level="low"
))

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Generated {len(samples)} samples in {OUTPUT_FILE}")
