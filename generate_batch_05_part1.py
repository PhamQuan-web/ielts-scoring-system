import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch05.jsonl")

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

# --- BATCH 05 PART 1: SAMPLES 351-375 (25 Total) ---
# Combo: V6/G7 (Competent Vocab, Good Grammar)

# Sample 351: V6/G7 - Topic: Environment (Climate Change)
samples.append(create_sample(
    index=351,
    vocab_band=6,
    grammar_band=7,
    question="How can international cooperation help with environmental issues?",
    transcript="It is absolutely essential because environmental problems do not respect borders. Pollution from one country can easily affect its neighbors. Therefore, countries need to work together to create treaties and set targets for reducing emissions. If nations cooperate, they can share technology and resources, which makes the process more efficient. Without a unified global effort, it will be impossible to solve a crisis like climate change.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'essential', 'borders', 'treaties', 'targets', 'emissions', 'unified', 'crisis'. >Band 5: Precise vocabulary. Not Band 7: Lacks idiomatic expressions.",
    grammar_reason="[GRA7] Uses a variety of complex structures: 'because...', 'If nations cooperate...', 'which makes...'. Produces frequent error-free sentences. >Band 6: Better control and accuracy. Not Band 8: Range is good but not fully flexible.",
    idiom_present=False,
    risk_level="low"
))

# Sample 352: V6/G7 - Topic: Technology (Privacy)
samples.append(create_sample(
    index=352,
    vocab_band=6,
    grammar_band=7,
    question="Do you think people share too much personal information online?",
    transcript="Yes, I definitely think so. Many people seem to forget that the internet is a public space. They post details about their daily lives, their location, and even their children, without thinking about the consequences. This behavior can be dangerous because it exposes them to identity theft or stalking. While sharing can be fun, we should be more cautious about what we make public.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'public space', 'consequences', 'exposes', 'identity theft', 'stalking', 'cautious'. >Band 5: Relevant terms. Not Band 7: Lacks natural collocations.",
    grammar_reason="[GRA7] Frequent error-free sentences. Uses 'seem to forget', 'without thinking', 'because it exposes'. >Band 6: Good control of grammar. Not Band 8: Some structures are slightly repetitive.",
    idiom_present=False,
    risk_level="low"
))

# Sample 353: V6/G7 - Topic: Education (University)
samples.append(create_sample(
    index=353,
    vocab_band=6,
    grammar_band=7,
    question="What are the benefits of studying at a university?",
    transcript="Studying at university offers numerous advantages. Firstly, it provides students with specialized knowledge in their chosen field, which is crucial for their future careers. Secondly, it is a place where young people learn independence and critical thinking skills. They have to manage their own time and money. Furthermore, the social aspect is important as they meet people from diverse backgrounds.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'numerous', 'specialized', 'crucial', 'independence', 'critical thinking', 'diverse backgrounds'. >Band 5: Strong vocabulary. Not Band 7: Lacks stylistic flair.",
    grammar_reason="[GRA7] Uses a variety of complex structures: 'provides... with...', 'which is crucial', 'where young people learn'. >Band 6: Sentences are accurate and well-structured. Not Band 8: Could be more varied.",
    idiom_present=False,
    risk_level="low"
))

# Sample 354: V6/G7 - Topic: Work (Job Satisfaction)
samples.append(create_sample(
    index=354,
    vocab_band=6,
    grammar_band=7,
    question="Is it important to enjoy your job?",
    transcript="I believe it is vital. We spend a significant portion of our lives working, so if we hate our job, it will negatively affect our mental health. Enjoying what you do brings a sense of fulfillment and motivation. When people are happy at work, they are generally more productive and creative. Therefore, job satisfaction should be a priority for everyone.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'vital', 'significant portion', 'negatively affect', 'fulfillment', 'motivation', 'productive', 'priority'. >Band 5: Good range. Not Band 7: Lacks idiomatic flow.",
    grammar_reason="[GRA7] Frequent error-free sentences. Uses 'so if we hate...', 'When people are happy...'. >Band 6: Good control. Not Band 8: Occasional rigidity.",
    idiom_present=False,
    risk_level="low"
))

# Sample 355: V6/G7 - Topic: Society (Cities)
samples.append(create_sample(
    index=355,
    vocab_band=6,
    grammar_band=7,
    question="Why do cities need public parks?",
    transcript="Public parks are essential for several reasons. Primarily, they provide a green space where people can relax and escape the noise of the city. This is beneficial for mental well-being. Additionally, parks are places for community interaction. Families can play there, and neighbors can meet. They also help to reduce pollution and improve air quality, making the city more livable.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'essential', 'green space', 'beneficial', 'well-being', 'interaction', 'pollution', 'livable'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'urban oasis', 'respite'.",
    grammar_reason="[GRA7] Uses complex structures: 'where people can relax', 'making the city more livable'. >Band 6: Accurate and varied. Not Band 8: Could be more sophisticated.",
    idiom_present=False,
    risk_level="low"
))

# Sample 356: V6/G7 - Topic: Culture (Food)
samples.append(create_sample(
    index=356,
    vocab_band=6,
    grammar_band=7,
    question="Has fast food changed people's eating habits?",
    transcript="Undoubtedly, it has had a major influence. In the past, people used to cook meals at home using fresh ingredients. However, nowadays, many individuals prefer fast food because it is convenient and cheap. This shift has led to an increase in health problems, such as obesity. While fast food saves time, it has unfortunately made our diets less nutritious.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'undoubtedly', 'influence', 'ingredients', 'convenient', 'shift', 'obesity', 'nutritious'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'dietary', 'consumption'.",
    grammar_reason="[GRA7] Uses 'used to cook', 'has led to', 'While fast food saves time'. >Band 6: Good control of tenses and complex forms. Not Band 8: Structure is a bit predictable.",
    idiom_present=False,
    risk_level="low"
))

# Sample 357: V6/G7 - Topic: Transport (Electric Cars)
samples.append(create_sample(
    index=357,
    vocab_band=6,
    grammar_band=7,
    question="Will electric cars solve pollution problems?",
    transcript="They will certainly help, but they are not the complete solution. Electric cars produce zero emissions while driving, which is great for air quality in cities. However, the electricity they use must also be clean. If it comes from burning coal, then we are just moving the pollution elsewhere. We need a comprehensive approach that includes renewable energy sources.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'complete solution', 'zero emissions', 'air quality', 'comprehensive approach', 'renewable energy'. >Band 5: Advanced terms. Not Band 7: Lacks 'holistic', 'mitigate'.",
    grammar_reason="[GRA7] Uses 'while driving', 'which is great', 'If it comes...'. >Band 6: Accurate complex sentences. Not Band 8: Limited flexibility.",
    idiom_present=False,
    risk_level="low"
))

# Sample 358: V6/G7 - Topic: Technology (Communication)
samples.append(create_sample(
    index=358,
    vocab_band=6,
    grammar_band=7,
    question="Has technology made communication better or worse?",
    transcript="I would say it has made it faster and easier, but not necessarily better. We can contact anyone instantly, which is amazing. However, the quality of conversation has declined. Text messages are often short and lack emotion. We are losing the art of face-to-face conversation. So, while technology connects us, it can also create a distance between people.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'necessarily', 'instantly', 'quality', 'declined', 'lack emotion', 'connects', 'distance'. >Band 5: Clear meaning. Not Band 7: Lacks 'superficial', 'nuance'.",
    grammar_reason="[GRA7] Contrast: 'but not necessarily better'. Relative clause: 'which is amazing'. >Band 6: Good control. Not Band 8: Sentences are competent but standard.",
    idiom_present=False,
    risk_level="low"
))

# Sample 359: V6/G7 - Topic: Society (Consumerism)
samples.append(create_sample(
    index=359,
    vocab_band=6,
    grammar_band=7,
    question="Why do brands use celebrities in advertisements?",
    transcript="They do it because it works. Celebrities have a huge influence on their fans. When a famous person promotes a product, people trust it more. They want to be like their idols. This creates a desire to buy the product. It is a powerful marketing strategy. Even if we know it is an ad, we are still affected by the celebrity's image.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'influence', 'promotes', 'trust', 'idols', 'desire', 'marketing strategy', 'affected'. >Band 5: Relevant terms. Not Band 7: Lacks 'endorsement', 'persuasive'.",
    grammar_reason="[GRA7] Time clause: 'When a famous person...'. Contrast: 'Even if we know...'. >Band 6: Accurate structures. Not Band 8: Limited range.",
    idiom_present=False,
    risk_level="low"
))

# Sample 360: V6/G7 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=360,
    vocab_band=6,
    grammar_band=7,
    question="Should we try to bring back extinct animals?",
    transcript="That is a fascinating idea, but I have doubts. On the positive side, it could help restore ecosystems. However, there are ethical questions. Is it right to bring an animal back into a world that has changed? They might not have a suitable habitat anymore. Also, it would be extremely expensive. We should focus our resources on saving the animals that are still alive.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'fascinating', 'doubts', 'restore ecosystems', 'ethical', 'suitable habitat', 'resources'. >Band 5: Good vocabulary. Not Band 7: Lacks 'resurrect', 'moral implication'.",
    grammar_reason="[GRA7] Contrast: 'However', 'But'. Conditionals implied. Relative clause: 'that has changed'. >Band 6: Frequent error-free sentences. Not Band 8: Could be more varied.",
    idiom_present=False,
    risk_level="low"
))

# Sample 361: V6/G7 - Topic: Health (Sleep)
samples.append(create_sample(
    index=361,
    vocab_band=6,
    grammar_band=7,
    question="Why do people have trouble sleeping?",
    transcript="There are several factors. Stress is a major cause. When people are worried about work or money, they cannot relax. Technology is another culprit. The blue light from screens keeps our brains awake. We should avoid using phones before bed. Also, irregular schedules can disrupt our body clock. To sleep better, we need to establish a consistent routine.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'factors', 'culprit', 'irregular schedules', 'disrupt', 'body clock', 'consistent routine'. >Band 5: Specific terms. Not Band 7: Lacks 'insomnia', 'circadian rhythm'.",
    grammar_reason="[GRA7] Time clause: 'When people are worried'. Modals: 'Should avoid', 'Need to establish'. >Band 6: Good control. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="low"
))

# Sample 362: V6/G7 - Topic: Education (Art)
samples.append(create_sample(
    index=362,
    vocab_band=6,
    grammar_band=7,
    question="Is art education important for children?",
    transcript="Yes, it is very significant. Art encourages creativity and imagination, which are important skills for any job. It allows children to express themselves in ways that words cannot. Furthermore, art classes can be a relief from academic pressure. They help students relax and enjoy school. Therefore, removing art from the curriculum would be a mistake.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'significant', 'encourages', 'imagination', 'express themselves', 'relief', 'academic pressure', 'curriculum'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'foster', 'outlet'.",
    grammar_reason="[GRA7] Relative clause: 'which are important skills'. Conditionals: 'would be a mistake'. >Band 6: Accurate grammar. Not Band 8: Limited flexibility.",
    idiom_present=False,
    risk_level="low"
))

# Sample 363: V6/G7 - Topic: Work (Retirement)
samples.append(create_sample(
    index=363,
    vocab_band=6,
    grammar_band=7,
    question="How should people prepare for retirement?",
    transcript="Financial planning is the most important step. People need to save money early so they can live comfortably later. They should also think about their health. Staying active is crucial for a happy retirement. Moreover, they need hobbies. If they don't have interests outside of work, they might get bored. Preparing mentally is just as important as saving money.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'financial planning', 'comfortably', 'crucial', 'hobbies', 'interests', 'mentally'. >Band 5: Relevant terms. Not Band 7: Lacks 'pension', 'investment', 'fulfillment'.",
    grammar_reason="[GRA7] Purpose: 'so they can live'. Conditionals: 'If they don't have...'. >Band 6: Frequent error-free sentences. Not Band 8: Structure is a bit repetitive.",
    idiom_present=False,
    risk_level="low"
))

# Sample 364: V6/G7 - Topic: Society (Friendship)
samples.append(create_sample(
    index=364,
    vocab_band=6,
    grammar_band=7,
    question="How do friendships change as we get older?",
    transcript="As we age, our friendships tend to change. In school, we have many friends because we see them every day. But as adults, we are busy with work and family. We have less time to socialize. Consequently, our circle of friends becomes smaller. However, the friendships that remain are usually deeper and more meaningful. Quality becomes more important than quantity.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'tend to', 'socialize', 'circle of friends', 'meaningful', 'quality', 'quantity'. >Band 5: Good range. Not Band 7: Lacks 'intimacy', 'drift apart', 'bond'.",
    grammar_reason="[GRA7] Time clause: 'As we age'. Reason: 'because we see them'. Contrast: 'However'. >Band 6: Accurate and varied. Not Band 8: Could be more complex.",
    idiom_present=False,
    risk_level="low"
))

# Sample 365: V6/G7 - Topic: Technology (Internet)
samples.append(create_sample(
    index=365,
    vocab_band=6,
    grammar_band=7,
    question="Does the internet make people smarter?",
    transcript="It gives us access to information, but that doesn't necessarily mean we are smarter. We can find answers quickly without thinking. This might make us lazy. True intelligence involves analyzing information, not just finding it. However, the internet is a great tool for learning if used correctly. Online courses allow people to learn new skills easily.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'access', 'necessarily', 'analyzing', 'tool', 'online courses'. >Band 5: Clear meaning. Not Band 7: Lacks 'cognitive', 'critical thinking', 'resource'.",
    grammar_reason="[GRA7] Contrast: 'but that doesn't necessarily...'. Conditionals: 'if used correctly'. >Band 6: Good control. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="low"
))

# Sample 366: V6/G7 - Topic: Environment (Energy)
samples.append(create_sample(
    index=366,
    vocab_band=6,
    grammar_band=7,
    question="Why is renewable energy important?",
    transcript="Because fossil fuels are finite and damaging. Burning oil and coal causes pollution and climate change. Renewable energy, like solar and wind, is clean and infinite. It does not harm the planet. Transitioning to green energy is essential for our survival. Although it is expensive to build the infrastructure, it will pay off in the future.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'finite', 'damaging', 'infinite', 'transitioning', 'green energy', 'essential', 'infrastructure', 'pay off'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'sustainable', 'emissions', 'investment'.",
    grammar_reason="[GRA7] Contrast: 'Although it is expensive'. Relative clause implied. >Band 6: Frequent error-free sentences. Not Band 8: Standard structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 367: V6/G7 - Topic: Culture (Fashion)
samples.append(create_sample(
    index=367,
    vocab_band=6,
    grammar_band=7,
    question="Does fashion reflect society?",
    transcript="Yes, I think it does. Fashion shows what people value. For example, nowadays, people prefer comfortable clothes because our lives are busy. In the past, clothes were more formal to show status. Also, fashion can show political views. People wear certain colors to support a cause. So, clothes are not just material; they are a message.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'reflect', 'value', 'prefer', 'formal', 'status', 'political views', 'support a cause', 'material'. >Band 5: Good topic words. Not Band 7: Lacks 'expression', 'trend', 'societal'.",
    grammar_reason="[GRA7] Reason: 'because our lives are busy'. Infinitive of purpose: 'to show status'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="low"
))

# Sample 368: V6/G7 - Topic: Society (Housing)
samples.append(create_sample(
    index=368,
    vocab_band=6,
    grammar_band=7,
    question="How can we solve the housing crisis?",
    transcript="The government needs to build more affordable homes. There is a shortage of houses, which drives prices up. Private companies only build expensive apartments for profit. We need social housing for low-income families. Also, we should improve transport links. If people can travel easily, they can live outside the city where it is cheaper.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'affordable', 'shortage', 'drives prices up', 'profit', 'social housing', 'low-income', 'transport links'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'incentivize', 'urban planning', 'rent control'.",
    grammar_reason="[GRA7] Relative clause: 'which drives prices up'. Conditionals: 'If people can travel...'. >Band 6: Frequent error-free sentences. Not Band 8: Structure is standard.",
    idiom_present=False,
    risk_level="low"
))

# Sample 369: V6/G7 - Topic: Transport (Cars)
samples.append(create_sample(
    index=369,
    vocab_band=6,
    grammar_band=7,
    question="Should we ban cars from city centers?",
    transcript="It is a radical idea, but it has merits. City centers are often polluted and noisy because of cars. If we ban them, the air would be cleaner. It would be safer for pedestrians and cyclists. However, we need to provide good alternatives. Public transport must be excellent. If not, businesses in the center might suffer.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'radical', 'merits', 'polluted', 'pedestrians', 'cyclists', 'alternatives'. >Band 5: Advanced terms. Not Band 7: Lacks 'congestion', 'pedestrianize', 'zone'.",
    grammar_reason="[GRA7] Conditionals: 'If we ban them...', 'If not...'. Contrast: 'However'. >Band 6: Good control. Not Band 8: Sentences are somewhat short.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 370: V6/G7 - Topic: Education (Teacher)
samples.append(create_sample(
    index=370,
    vocab_band=6,
    grammar_band=7,
    question="What makes a good teacher?",
    transcript="A good teacher needs to be patient and knowledgeable. They should understand their subject well. But more importantly, they must be able to explain things clearly. Inspiring students is also key. If a teacher is passionate, the students will be interested. They should care about the students' progress, not just their grades.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'knowledgeable', 'inspiring', 'passionate', 'progress'. >Band 5: Clear meaning. Not Band 7: Lacks 'engaging', 'methodology', 'empathetic'.",
    grammar_reason="[GRA7] Conditionals: 'If a teacher is passionate...'. Contrast: 'But more importantly'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="low"
))

# Sample 371: V6/G7 - Topic: Society (Crime)
samples.append(create_sample(
    index=371,
    vocab_band=6,
    grammar_band=7,
    question="Is rehabilitation better than punishment?",
    transcript="I think so. Punishment alone does not change behavior. If criminals go to prison and learn nothing, they will reoffend when they leave. Rehabilitation focuses on the cause of the crime. It teaches skills and provides therapy. This gives people a second chance. While serious crimes need punishment, our goal should be a safer society, not just revenge.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'behavior', 'reoffend', 'focuses on', 'therapy', 'revenge'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'reintegration', 'deterrent', 'correctional'.",
    grammar_reason="[GRA7] Conditionals: 'If criminals go to prison...'. Contrast: 'While serious crimes...'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 372: V6/G7 - Topic: Technology (Phones)
samples.append(create_sample(
    index=372,
    vocab_band=6,
    grammar_band=7,
    question="How have smartphones changed our lives?",
    transcript="They have changed everything. We have the world in our pockets. We can find information instantly and talk to anyone. It is very convenient. However, there are downsides. We are addicted to our screens. Face-to-face communication has decreased. We are always distracted. Smartphones are useful tools, but we must control how we use them.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'instantly', 'convenient', 'downsides', 'addicted', 'decreased', 'distracted'. >Band 5: Relevant terms. Not Band 7: Lacks 'dependency', 'virtual', 'interaction'.",
    grammar_reason="[GRA7] Contrast: 'However', 'but we must control'. Present perfect: 'have changed', 'has decreased'. >Band 6: Accurate grammar. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 373: V6/G7 - Topic: Culture (Travel)
samples.append(create_sample(
    index=373,
    vocab_band=6,
    grammar_band=7,
    question="What are the benefits of traveling alone?",
    transcript="Traveling alone gives you total freedom. You can do what you want, when you want. You don't have to compromise with others. It also forces you to meet new people. You become more independent and confident. It can be scary at first, but it is a great way to grow as a person.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'freedom', 'compromise', 'forces', 'independent', 'confident', 'scary'. >Band 5: Clear meaning. Not Band 7: Lacks 'autonomy', 'self-discovery', 'itinerary'.",
    grammar_reason="[GRA7] Reason: 'Because you don't have to...'. Contrast: 'but it is a great way'. >Band 6: Frequent error-free sentences. Not Band 8: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 374: V6/G7 - Topic: Work (Teamwork)
samples.append(create_sample(
    index=374,
    vocab_band=6,
    grammar_band=7,
    question="Why is teamwork important in the workplace?",
    transcript="Because no one can do everything alone. Companies have complex problems that need different skills. When people work together, they can share ideas and find better solutions. It also builds morale. People feel supported. However, teamwork requires good communication. If people don't get along, it can be a disaster.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'complex', 'solutions', 'morale', 'supported', 'requires', 'disaster'. >Band 5: Good topic words. Not Band 7: Lacks 'collaborate', 'synergy', 'conflict resolution'.",
    grammar_reason="[GRA7] Time clause: 'When people work together'. Conditionals: 'If people don't get along...'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 375: V6/G7 - Topic: Environment (Water)
samples.append(create_sample(
    index=375,
    vocab_band=6,
    grammar_band=7,
    question="Why should we save water?",
    transcript="Water is a precious resource. Although the Earth has a lot of water, most of it is salty. Fresh water is limited. With climate change, droughts are becoming common. If we waste water, we might face shortages in the future. We need to be responsible. Simple actions like fixing leaks can make a difference.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'precious resource', 'salty', 'limited', 'droughts', 'shortages', 'responsible', 'leaks'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'scarcity', 'conservation', 'vital'.",
    grammar_reason="[GRA7] Contrast: 'Although the Earth...'. Conditionals: 'If we waste water...'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structures.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Generated {len(samples)} samples in {OUTPUT_FILE}")
