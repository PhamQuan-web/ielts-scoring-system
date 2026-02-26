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

# --- BATCH 04 PART 2: SAMPLES 276-300 (25 Total) ---
# Combo: V6/G6

# Sample 276: V6/G6 - Topic: Work (Leadership)
samples.append(create_sample(
    index=276,
    vocab_band=6,
    grammar_band=6,
    question="Can anyone become a leader?",
    transcript="I think most people can learn leadership skills. It is not just a talent you are born with. You can learn how to communicate and organize people. However, some personalities are better suited. If you are shy, it is harder. A leader needs confidence. But with practice, even a shy person can lead. It takes time and effort.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'better suited' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'leadership skills', 'talent', 'communicate', 'organize', 'personalities', 'suited', 'confidence'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'innate', 'acquire', 'charisma'.",
    grammar_reason="[GRA6] Contrast: 'However', 'But'. Conditionals: 'If you are shy...'. >Band 5: Accurate grammar. Not Band 7: Simple sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 277: V6/G6 - Topic: Transport (Cars)
samples.append(create_sample(
    index=277,
    vocab_band=6,
    grammar_band=6,
    question="Why do people like fast cars?",
    transcript="It gives them a thrill. Driving fast is exciting. It pumps adrenaline. Also, fast cars are often expensive and stylish. They are a status symbol. People want to show off. It makes them feel powerful. But it is dangerous. Speeding causes many accidents. We should enjoy cars responsibly.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'pumps adrenaline' (idiomatic usage)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'thrill', 'adrenaline', 'stylish', 'status symbol', 'show off', 'speeding', 'responsibly'. >Band 5: Good range. Not Band 7: Lacks 'prestige', 'performance', 'reckless'.",
    grammar_reason="[GRA6] Reason: 'It gives them a thrill'. Contrast: 'But it is dangerous'. >Band 5: Error-free sentences. Not Band 7: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 278: V6/G6 - Topic: Environment (Climate)
samples.append(create_sample(
    index=278,
    vocab_band=6,
    grammar_band=6,
    question="What can governments do about climate change?",
    transcript="They have the power to make big changes. They can pass laws to limit pollution. For example, taxing carbon emissions. They can also invest in renewable energy. Solar and wind power farms. Education is important too. Governments should tell people how to live green. International cooperation is needed. One country cannot solve it alone.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'live green' (informal but correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'pass laws', 'pollution', 'taxing', 'carbon emissions', 'invest', 'renewable energy', 'cooperation'. >Band 5: Specific terms. Not Band 7: Lacks 'legislation', 'incentivize', 'sustainable'.",
    grammar_reason="[GRA6] Modals: 'Can pass', 'Should tell'. Gerund: 'taxing carbon emissions'. >Band 5: Accurate grammar. Not Band 7: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 279: V6/G6 - Topic: Society (Poverty)
samples.append(create_sample(
    index=279,
    vocab_band=6,
    grammar_band=6,
    question="How can we help poor people?",
    transcript="Giving money is a short-term fix. It helps for a day. But education is the long-term solution. If people learn skills, they can get jobs. Then they can support themselves. We should also provide healthcare. If people are sick, they cannot work. Creating opportunities is better than just giving charity. We need to empower them.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'short-term fix' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'short-term fix', 'solution', 'skills', 'support themselves', 'healthcare', 'opportunities', 'charity', 'empower'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'sustainable', 'alleviate', 'cycle of poverty'.",
    grammar_reason="[GRA6] Contrast: 'But education is...'. Conditionals: 'If people learn...'. >Band 5: Good control. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 280: V6/G6 - Topic: Technology (Social Media)
samples.append(create_sample(
    index=280,
    vocab_band=6,
    grammar_band=6,
    question="Why is cyberbullying a problem?",
    transcript="Because it is easy to be mean online. You can hide behind a screen. You don't see the person's face. So you don't feel guilty. Cyberbullying hurts feelings deeply. It can lead to depression. Especially for teenagers. It is hard to escape because the internet is everywhere. We need to report bullies and support victims.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'hide behind a screen' (idiomatic)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'mean', 'guilty', 'depression', 'teenagers', 'escape', 'report', 'bullies', 'victims'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'anonymity', 'harassment', 'consequences'.",
    grammar_reason="[GRA6] Reason: 'Because it is easy'. Result: 'So you don't feel'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 281: V6/G6 - Topic: Culture (Art)
samples.append(create_sample(
    index=281,
    vocab_band=6,
    grammar_band=6,
    question="Why do people collect art?",
    transcript="For some, it is an investment. Art can become very valuable over time. They buy it to sell later. For others, it is about passion. They love the beauty of the painting. It makes them feel happy. Also, it can show status. Having expensive art on the wall impresses guests. It is a mix of money and emotion.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'mix of money and emotion' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'investment', 'valuable', 'passion', 'beauty', 'status', 'impresses', 'emotion'. >Band 5: Good topic words. Not Band 7: Lacks 'appreciation', 'aesthetic', 'prestige'.",
    grammar_reason="[GRA6] Reason: 'They buy it to sell'. Purpose implied. >Band 5: Error-free sentences. Not Band 7: Simple phrasing.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 282: V6/G6 - Topic: Health (Food)
samples.append(create_sample(
    index=282,
    vocab_band=6,
    grammar_band=6,
    question="Is organic food better?",
    transcript="Many people think so. It is grown without chemicals. No pesticides. So it might be healthier. It tastes better too. More natural. However, it is expensive. Not everyone can afford it. Also, regular food is safe if you wash it. I think organic is good, but not necessary for everyone. A balanced diet is more important.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'grown without chemicals' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'chemicals', 'pesticides', 'healthier', 'natural', 'afford', 'regular', 'necessary', 'balanced diet'. >Band 5: Relevant terms. Not Band 7: Lacks 'nutritional value', 'cultivation', 'preservatives'.",
    grammar_reason="[GRA6] Contrast: 'However'. Conditionals: 'if you wash it'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 283: V6/G6 - Topic: Transport (Traffic)
samples.append(create_sample(
    index=283,
    vocab_band=6,
    grammar_band=6,
    question="How does traffic affect the economy?",
    transcript="It costs money. When people sit in traffic, they are not working. Delivery trucks are late. This slows down business. Also, fuel is wasted. This is bad for the economy. Pollution from traffic causes health problems. Sick people cannot work. So, congestion is very expensive for a country. Efficient transport is key to a strong economy.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'slows down business' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'delivery trucks', 'wasted', 'pollution', 'congestion', 'efficient', 'key'. >Band 5: Specific terms. Not Band 7: Lacks 'productivity', 'logistics', 'impact', 'infrastructure'.",
    grammar_reason="[GRA6] Time clause: 'When people sit...'. Result: 'This slows down...'. >Band 5: Good control. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 284: V6/G6 - Topic: Education (University)
samples.append(create_sample(
    index=284,
    vocab_band=6,
    grammar_band=6,
    question="What makes a university good?",
    transcript="Good teachers are essential. They should be experts in their subject. Also, facilities matter. A good library, labs, and computers. The atmosphere is important too. Students should feel safe and inspired. A good university helps students find jobs. They have connections with companies. It prepares you for the real world.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'real world' (idiomatic)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'essential', 'experts', 'facilities', 'labs', 'atmosphere', 'inspired', 'connections', 'prepares'. >Band 5: Good range. Not Band 7: Lacks 'academic reputation', 'research', 'campus'.",
    grammar_reason="[GRA6] Modals: 'Should be', 'Should feel'. List structure. >Band 5: Accurate grammar. Not Band 7: Simple sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 285: V6/G6 - Topic: Society (Crime)
samples.append(create_sample(
    index=285,
    vocab_band=6,
    grammar_band=6,
    question="Should criminals be given a second chance?",
    transcript="It depends on the crime. If it is minor, like stealing food, yes. Everyone makes mistakes. Prison should help them change. Teach them a job. But for violent crimes, it is hard. Murderers might be dangerous forever. We need to protect society first. But forgiveness is a good value. Rehabilitation works for many people.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'violent crimes' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'minor', 'stealing', 'mistakes', 'violent', 'murderers', 'society', 'forgiveness', 'value', 'rehabilitation'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'offense', 'reintegration', 'justice'.",
    grammar_reason="[GRA6] Conditionals: 'If it is minor...'. Contrast: 'But for violent crimes'. >Band 5: Good structure. Not Band 7: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 286: V6/G6 - Topic: Work (Job)
samples.append(create_sample(
    index=286,
    vocab_band=6,
    grammar_band=6,
    question="Is it better to work for a big company or a small one?",
    transcript="Both have pros and cons. Big companies offer stability. The salary is usually good. You can move up the ladder. But you might feel like a number. Small companies are friendlier. You know everyone. Your work is noticed more. But there is less security. It might go bankrupt. It depends on what you want from your career.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'move up the ladder' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'pros and cons', 'stability', 'ladder', 'noticed', 'security', 'bankrupt', 'career'. >Band 5: Relevant terms. Not Band 7: Lacks 'corporate', 'environment', 'promotion', 'flexible'.",
    grammar_reason="[GRA6] Contrast: 'But you might feel...'. Comparison implied. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 287: V6/G6 - Topic: Technology (Robots)
samples.append(create_sample(
    index=287,
    vocab_band=6,
    grammar_band=6,
    question="How do robots help us in daily life?",
    transcript="We have robot vacuums now. They clean the floor automatically. It saves time. Also, kitchen machines. Smart homes use technology to control lights and heat. In the future, we might have robot assistants. They could cook or look after children. This makes life easier. But we might become lazy if we rely on them too much.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'robot assistants' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'vacuums', 'automatically', 'smart homes', 'control', 'assistants', 'rely on'. >Band 5: Good topic words. Not Band 7: Lacks 'appliance', 'convenience', 'artificial intelligence'.",
    grammar_reason="[GRA6] Conditionals: 'if we rely on them...'. Future possibility: 'might have'. >Band 5: Accurate grammar. Not Band 7: Simple phrasing.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 288: V6/G6 - Topic: Culture (Music)
samples.append(create_sample(
    index=288,
    vocab_band=6,
    grammar_band=6,
    question="Why is music popular around the world?",
    transcript="Because it is a universal language. You don't need to understand the words to enjoy the melody. It expresses emotions. Happiness, sadness, love. Music connects people. Concerts are a shared experience. Also, music helps us relax. It changes our mood. Every culture has music. It is part of being human.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'universal language' (common idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'universal', 'melody', 'expresses', 'emotions', 'connects', 'shared experience', 'mood'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'rhythm', 'genre', 'transcend', 'lyrics'.",
    grammar_reason="[GRA6] Reason: 'Because it is...'. Purpose: 'to enjoy the melody'. >Band 5: Correct grammar. Not Band 7: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 289: V6/G6 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=289,
    vocab_band=6,
    grammar_band=6,
    question="Why is it important to teach children about the environment?",
    transcript="They are the future. If they learn to respect nature now, they will protect it later. We need to teach them about recycling and pollution. Schools should have green projects. Planting trees or cleaning parks. This creates good habits. If children care, they can influence their parents. Education is the best way to change the world.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'green projects' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'respect', 'nature', 'protect', 'recycling', 'pollution', 'habits', 'influence'. >Band 5: Clear meaning. Not Band 7: Lacks 'sustainability', 'awareness', 'generation', 'conserve'.",
    grammar_reason="[GRA6] Conditionals: 'If they learn...', 'If children care...'. >Band 5: Good structure. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 290: V6/G6 - Topic: Society (Urbanization)
samples.append(create_sample(
    index=290,
    vocab_band=6,
    grammar_band=6,
    question="What are the effects of urbanization?",
    transcript="Cities are getting bigger. This creates jobs and wealth. But it also causes problems. Overcrowding is a big issue. Housing becomes expensive. Slums appear. Pollution increases because of cars and factories. People lose connection with nature. Village life destroys. I think we need to plan cities better. To make them green and livable.",
    response_type="extended",
    micro_flaws=[
        "verb voice: 'Village life destroys' -> 'Village life is destroyed'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'wealth', 'overcrowding', 'slums', 'connection', 'plan', 'livable'. >Band 5: Specific terms. Not Band 7: Lacks 'infrastructure', 'migration', 'development', 'sustainability'.",
    grammar_reason="[GRA6] Contrast: 'But it also causes...'. Passive voice error 'Village life destroys'. >Band 5: Mostly accurate. Not Band 7: Basic error present.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 291: V6/G6 - Topic: Travel (Tourism)
samples.append(create_sample(
    index=291,
    vocab_band=6,
    grammar_band=6,
    question="Can tourism damage a country?",
    transcript="Yes, it can. Too many tourists cause overcrowding. They can damage historical sites by walking on them. Also, they produce trash. Pollution increases. Local culture can change to please tourists. It becomes fake. Prices go up for local people. However, tourism brings money. We need sustainable tourism. Managing the numbers is key.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Managing the numbers' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'overcrowding', 'historical sites', 'produce', 'pollution', 'please', 'fake', 'sustainable'. >Band 5: Good range. Not Band 7: Lacks 'erosion', 'commercialize', 'economy', 'heritage'.",
    grammar_reason="[GRA6] Contrast: 'However'. Gerund: 'Managing the numbers'. >Band 5: Accurate grammar. Not Band 7: Simple sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 292: V6/G6 - Topic: Health (Stress)
samples.append(create_sample(
    index=292,
    vocab_band=6,
    grammar_band=6,
    question="How does stress affect work performance?",
    transcript="It has a negative effect. If you are stressed, you cannot focus. You make mistakes. Productivity goes down. You might argue with colleagues. Also, stress causes health issues. You take more sick days. This costs the company money. A happy worker is a good worker. Employers should try to reduce stress in the office.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'sick days' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'negative effect', 'focus', 'productivity', 'colleagues', 'issues', 'reduce'. >Band 5: Relevant terms. Not Band 7: Lacks 'concentration', 'efficiency', 'burnout', 'impact'.",
    grammar_reason="[GRA6] Conditionals: 'If you are stressed...'. Modals: 'Should try'. >Band 5: Accurate grammar. Not Band 7: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 293: V6/G6 - Topic: Education (Technology)
samples.append(create_sample(
    index=293,
    vocab_band=6,
    grammar_band=6,
    question="Should tablets be used in primary schools?",
    transcript="I think so. Children love technology. It makes learning fun. Interactive apps can teach reading and math. It prepares them for the future digital world. However, screen time must be limited. Too much is bad for eyes. Also, they need to learn to write by hand. Tablets are a tool, not a teacher.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'digital world' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'technology', 'interactive', 'apps', 'prepares', 'digital world', 'screen time', 'limited'. >Band 5: Good range. Not Band 7: Lacks 'engagement', 'educational', 'device', 'supplement'.",
    grammar_reason="[GRA6] Contrast: 'However'. Modals: 'Must be limited'. >Band 5: Correct grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 294: V6/G6 - Topic: Society (Family)
samples.append(create_sample(
    index=294,
    vocab_band=6,
    grammar_band=6,
    question="How has family life changed?",
    transcript="It has changed a lot. In the past, families were big. Grandparents lived with children. Now, families are smaller. Usually just parents and kids. Also, both parents work now. They have less time for children. Family dinners are rare. Technology also affects us. We look at phones instead of talking. We are less connected.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'less connected' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'grandparents', 'rare', 'affects', 'instead of', 'connected'. >Band 5: Clear meaning. Not Band 7: Lacks 'extended family', 'nuclear family', 'household', 'quality time'.",
    grammar_reason="[GRA6] Comparison: 'In the past... Now...'. Gerund: 'instead of talking'. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 295: V6/G6 - Topic: Culture (Global)
samples.append(create_sample(
    index=295,
    vocab_band=6,
    grammar_band=6,
    question="What is the impact of western culture?",
    transcript="It is everywhere. Movies, music, and fashion. Western brands are famous globally. It brings modern ideas. Like democracy and individual freedom. But it can damage local traditions. People stop wearing traditional clothes. They eat fast food. It is a mix of good and bad. We should accept the good but keep our own identity.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'mix of good and bad' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'globally', 'modern', 'democracy', 'freedom', 'damage', 'traditional', 'identity'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'dominance', 'influence', 'values', 'heritage'.",
    grammar_reason="[GRA6] Contrast: 'But it can damage'. Modals: 'Should accept'. >Band 5: Accurate structure. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 296: V6/G6 - Topic: Work (Job)
samples.append(create_sample(
    index=296,
    vocab_band=6,
    grammar_band=6,
    question="What is the most important quality for an employee?",
    transcript="I think it is reliability. The boss needs to trust you. If you say you will do something, you must do it. Also, being on time is important. Hard work is good, but teamwork is better. You need to get along with colleagues. Skills can be learned, but attitude is hard to change. A positive attitude is key.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'get along with' (phrasal verb)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'reliability', 'trust', 'colleagues', 'attitude', 'positive'. >Band 5: Good topic words. Not Band 7: Lacks 'competence', 'punctuality', 'adaptable', 'professionalism'.",
    grammar_reason="[GRA6] Conditionals: 'If you say...'. Contrast: 'Hard work is good, but...'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 297: V6/G6 - Topic: Technology (AI)
samples.append(create_sample(
    index=297,
    vocab_band=6,
    grammar_band=6,
    question="Will AI ever have emotions?",
    transcript="It is hard to say. Computers are becoming very smart. They can copy human behavior. They can speak like us. But emotion is biological. It comes from the heart and brain chemistry. A machine is just code. It can fake emotion, but not feel it. Maybe in the far future, but not now. It is a scary thought.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'scary thought' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'copy', 'behavior', 'biological', 'chemistry', 'code', 'fake'. >Band 5: Specific terms. Not Band 7: Lacks 'simulate', 'consciousness', 'artificial', 'complexity'.",
    grammar_reason="[GRA6] Contrast: 'But emotion is...'. Comparison implied. >Band 5: Good control. Not Band 7: Simple sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 298: V6/G6 - Topic: Environment (Trees)
samples.append(create_sample(
    index=298,
    vocab_band=6,
    grammar_band=6,
    question="Why are trees important for cities?",
    transcript="They are the lungs of the city. They clean the air by absorbing CO2. They give oxygen. Also, they provide shade. In summer, cities are hot. Trees make them cooler. They are beautiful too. Green spaces help people relax. A city without trees is ugly and unhealthy. We should plant more trees on every street.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'lungs of the city' (metaphor)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'lungs', 'absorbing', 'oxygen', 'shade', 'cooler', 'unhealthy'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'filter', 'temperature', 'aesthetic', 'urban'.",
    grammar_reason="[GRA6] Reason: 'by absorbing CO2'. Conditionals implied. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 299: V6/G6 - Topic: Society (Friendship)
samples.append(create_sample(
    index=299,
    vocab_band=6,
    grammar_band=6,
    question="What is a true friend?",
    transcript="A true friend is someone who is always there. In good times and bad times. They listen to you. They don't judge you. You can trust them with your secrets. They tell you the truth, even if it hurts. It is hard to find a true friend. Most people are just acquaintances. Friendship takes time and effort to build.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'acquaintances' (advanced word)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'judge', 'secrets', 'truth', 'hurts', 'acquaintances', 'effort'. >Band 5: Good range. Not Band 7: Lacks 'loyalty', 'supportive', 'bond', 'reliable'.",
    grammar_reason="[GRA6] Relative clause: 'someone who is...'. Conditionals: 'even if it hurts'. >Band 5: Accurate grammar. Not Band 7: Simple structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 300: V6/G6 - Topic: Transport (Flying)
samples.append(create_sample(
    index=300,
    vocab_band=6,
    grammar_band=6,
    question="Is air travel good for the world?",
    transcript="It connects the world. We can travel anywhere quickly. It helps business and tourism. People learn about other cultures. But it is bad for the environment. Planes produce a lot of pollution. Carbon footprint is high. Also, airports are noisy. We need greener planes. Electric planes maybe. Until then, we should fly less.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'greener planes' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'connects', 'tourism', 'produce', 'pollution', 'carbon footprint', 'noisy', 'greener'. >Band 5: Relevant terms. Not Band 7: Lacks 'aviation', 'emissions', 'global', 'sustainable'.",
    grammar_reason="[GRA6] Contrast: 'But it is bad'. Modals: 'Should fly'. >Band 5: Good control. Not Band 7: Sentences are somewhat short.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
