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

# --- BATCH 05 PART 2: SAMPLES 376-400 (25 Total) ---
# Combo: V6/G7

# Sample 376: V6/G7 - Topic: Transport (Public)
samples.append(create_sample(
    index=376,
    vocab_band=6,
    grammar_band=7,
    question="Why do people prefer cars over buses?",
    transcript="It is mainly about convenience. A car takes you from door to door. You don't have to walk to a bus stop or wait in the rain. Also, cars offer privacy. You can listen to your own music and control the temperature. Buses are often crowded and noisy. Although cars are expensive, the comfort they provide is worth it for many people.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'convenience', 'privacy', 'control', 'temperature', 'crowded', 'comfort'. >Band 5: Clear meaning. Not Band 7: Lacks 'flexibility', 'autonomy', 'personal space'.",
    grammar_reason="[GRA7] Contrast: 'Although cars are expensive'. Reason: 'It is mainly about...'. >Band 6: Frequent error-free sentences. Not Band 8: Limited range of complex structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 377: V6/G7 - Topic: Health (Diet)
samples.append(create_sample(
    index=377,
    vocab_band=6,
    grammar_band=7,
    question="Should government tax unhealthy food?",
    transcript="This is a controversial topic. Some people say yes, because it would reduce consumption. If sugar is expensive, people will buy less of it. This could lower obesity rates. However, others argue that it is unfair to the poor. Healthy food is already pricey. A tax would hurt those with low incomes. I think education is a better solution than taxation.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'controversial', 'reduce consumption', 'obesity rates', 'unfair', 'pricey', 'incomes', 'taxation'. >Band 5: Advanced vocabulary. Not Band 7: Lacks 'regressive', 'deterrent', 'policy'.",
    grammar_reason="[GRA7] Conditionals: 'If sugar is expensive...'. Comparison: 'better solution than'. >Band 6: Good control. Not Band 8: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 378: V6/G7 - Topic: Society (Media)
samples.append(create_sample(
    index=378,
    vocab_band=6,
    grammar_band=7,
    question="Is news on social media reliable?",
    transcript="Not always. Social media is full of opinions, not just facts. Anyone can post a story, even if it is not true. This leads to the spread of fake news. People often share headlines without reading the article. Traditional news organizations are usually more trustworthy because they check their sources. We need to be critical of what we read online.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'opinions', 'fake news', 'headlines', 'organizations', 'trustworthy', 'sources', 'critical'. >Band 5: Relevant terms. Not Band 7: Lacks 'verify', 'misinformation', 'bias'.",
    grammar_reason="[GRA7] Reason: 'because they check'. Concession: 'even if it is not true'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 379: V6/G7 - Topic: Culture (Language)
samples.append(create_sample(
    index=379,
    vocab_band=6,
    grammar_band=7,
    question="Does language define a person's identity?",
    transcript="To a large extent, yes. Language is how we express our thoughts and feelings. It connects us to our culture and history. When you speak your native language, you feel at home. However, many people are bilingual. They have two identities. They can switch between cultures easily. So, while language is important, it is not the only thing that defines us.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'extent', 'express', 'connects', 'native', 'bilingual', 'identities', 'switch'. >Band 5: Clear meaning. Not Band 7: Lacks 'integral', 'heritage', 'nuance'.",
    grammar_reason="[GRA7] Time clause: 'When you speak...'. Contrast: 'So, while language is important...'. >Band 6: Frequent error-free sentences. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="low"
))

# Sample 380: V6/G7 - Topic: Education (Skills)
samples.append(create_sample(
    index=380,
    vocab_band=6,
    grammar_band=7,
    question="Are practical skills more important than academic ones?",
    transcript="Both are necessary. Academic skills teach us how to think and analyze. They are important for fields like science and law. But practical skills are essential for daily life. We need to know how to fix things, cook, and manage money. In the modern world, employers value people who can do things, not just know things. A balance is best.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'necessary', 'analyze', 'fields', 'essential', 'manage money', 'employers', 'value'. >Band 5: Good range. Not Band 7: Lacks 'theoretical', 'competency', 'vocational'.",
    grammar_reason="[GRA7] Reason: 'Because both are...'. Relative clause: 'people who can do things'. >Band 6: Accurate structures. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 381: V6/G7 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=381,
    vocab_band=6,
    grammar_band=7,
    question="Why do some people hunt animals?",
    transcript="For some, it is a sport. They enjoy the challenge and the thrill of the chase. In some cultures, it is a tradition passed down through generations. However, others hunt for food. In remote areas, it is necessary for survival. There is also illegal hunting, or poaching, which is done for money. People sell parts of rare animals. This is very wrong.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'challenge', 'thrill', 'chase', 'tradition', 'passed down', 'remote', 'survival', 'illegal', 'poaching', 'rare'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'sustenance', 'ethical', 'trophy hunting'.",
    grammar_reason="[GRA7] Relative clause: 'which is done for money'. Passive: 'is passed down'. >Band 6: Frequent error-free sentences. Not Band 8: Standard forms.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 382: V6/G7 - Topic: Technology (Robots)
samples.append(create_sample(
    index=382,
    vocab_band=6,
    grammar_band=7,
    question="Will robots make humans lazy?",
    transcript="There is a risk of that. If machines do all the hard work, we might become physically weak. We won't need to clean or cook. Also, if computers do our thinking, our brains might get lazy too. We won't need to remember anything. However, robots also give us free time. We can use that time to be creative or exercise. It is our choice.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'risk', 'physically weak', 'creative', 'choice'. >Band 5: Clear meaning. Not Band 7: Lacks 'dependent', 'sedentary', 'cognitive'.",
    grammar_reason="[GRA7] Conditionals: 'If machines do...', 'if computers do...'. >Band 6: Good control. Not Band 8: Repetitive 'If' structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 383: V6/G7 - Topic: Work (Job)
samples.append(create_sample(
    index=383,
    vocab_band=6,
    grammar_band=7,
    question="What makes a job stressful?",
    transcript="High workload is a common cause. When you have too much to do and not enough time, you feel pressure. Also, bad management. If your boss is not supportive or is always angry, it creates a toxic environment. Uncertainty is another factor. If you are afraid of losing your job, you will be anxious. Stress can damage your health.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'workload', 'pressure', 'management', 'supportive', 'toxic environment', 'uncertainty', 'factor', 'anxious'. >Band 5: Specific terms. Not Band 7: Lacks 'deadline', 'micromanagement', 'insecurity'.",
    grammar_reason="[GRA7] Conditionals: 'If your boss is...', 'If you are afraid...'. >Band 6: Accurate grammar. Not Band 8: Repetitive structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 384: V6/G7 - Topic: Society (Friendship)
samples.append(create_sample(
    index=384,
    vocab_band=6,
    grammar_band=7,
    question="Can men and women be just friends?",
    transcript="Yes, I believe they can. Friendship is based on shared interests and trust, not gender. Many people have close friends of the opposite sex without any romantic feelings. It is healthy to have different perspectives. However, sometimes feelings can change. One person might fall in love. That makes things complicated. But in general, platonic friendship is definitely possible.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'shared interests', 'gender', 'opposite sex', 'romantic', 'perspectives', 'complicated', 'platonic'. >Band 5: Advanced terms. Not Band 7: Lacks 'attraction', 'boundary', 'relationship'.",
    grammar_reason="[GRA7] Contrast: 'But in general'. Reason: 'Friendship is based on...'. >Band 6: Frequent error-free sentences. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 385: V6/G7 - Topic: Culture (Art)
samples.append(create_sample(
    index=385,
    vocab_band=6,
    grammar_band=7,
    question="Is street art real art?",
    transcript="I think it depends on the intention. If it is just a tag or a mess, it is vandalism. But many street artists are very talented. They create beautiful murals that improve the city. Their work has a message. It makes people think. Banksy is a great example. His art is famous worldwide. So yes, street art can be real art.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'intention', 'tag', 'mess', 'vandalism', 'talented', 'murals', 'improve', 'worldwide'. >Band 5: Good range. Not Band 7: Lacks 'expression', 'aesthetic', 'public space'.",
    grammar_reason="[GRA7] Conditionals: 'If it is just a tag...'. >Band 6: Accurate grammar. Not Band 8: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 386: V6/G7 - Topic: Transport (Flying)
samples.append(create_sample(
    index=386,
    vocab_band=6,
    grammar_band=7,
    question="Should we fly less to save the planet?",
    transcript="Ideally, yes. Flying produces a lot of carbon emissions. It is bad for the climate. If we take trains or buses, it is much greener. However, sometimes flying is the only option. For long distances, like going to another continent, you cannot take a train. We need better technology. Cleaner planes are the answer, not just stopping travel.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'ideally', 'emissions', 'climate', 'greener', 'option', 'continent'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'aviation', 'footprint', 'sustainable'.",
    grammar_reason="[GRA7] Conditionals: 'If we take trains...'. Contrast: 'However'. >Band 6: Good control. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 387: V6/G7 - Topic: Education (University)
samples.append(create_sample(
    index=387,
    vocab_band=6,
    grammar_band=7,
    question="Do you think university prepares students for work?",
    transcript="It provides knowledge, but maybe not practical skills. You learn a lot of theory in class. You write essays and take exams. But the real world is different. Jobs require teamwork and problem-solving. University doesn't always teach this. That is why internships are important. They give students a taste of real work before they graduate.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'practical skills', 'theory', 'essays', 'real world', 'require', 'problem-solving', 'internships', 'graduate'. >Band 5: Specific terms. Not Band 7: Lacks 'academic', 'competence', 'workplace'.",
    grammar_reason="[GRA7] Contrast: 'It provides..., but...'. Reason: 'That is why...'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 388: V6/G7 - Topic: Society (Cities)
samples.append(create_sample(
    index=388,
    vocab_band=6,
    grammar_band=7,
    question="Why do cities have traffic problems?",
    transcript="Because there are too many people and not enough space. Everyone wants to drive their own car. It is convenient. But the roads were built a long time ago. They are too narrow for modern traffic. Also, public transport is sometimes poor. If the bus is slow or dirty, people won't use it. We need to invest in better systems.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'convenient', 'narrow', 'modern', 'public transport', 'invest', 'systems'. >Band 5: Clear meaning. Not Band 7: Lacks 'infrastructure', 'congestion', 'population density'.",
    grammar_reason="[GRA7] Reason: 'Because there are...'. Conditionals: 'If the bus is slow...'. >Band 6: Frequent error-free sentences. Not Band 8: Short sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 389: V6/G7 - Topic: Health (Exercise)
samples.append(create_sample(
    index=389,
    vocab_band=6,
    grammar_band=7,
    question="Is walking a good form of exercise?",
    transcript="Yes, it is excellent. It is easy and free. You don't need special equipment. Anyone can do it, young or old. Walking is good for the heart and legs. It also clears the mind. It reduces stress. If you walk every day, you will feel healthier. It is not intense like running, but it is effective.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'excellent', 'equipment', 'clears the mind', 'reduces', 'intense', 'effective'. >Band 5: Good range. Not Band 7: Lacks 'cardiovascular', 'low-impact', 'stamina'.",
    grammar_reason="[GRA7] Conditionals: 'If you walk every day...'. Contrast: 'It is not intense..., but...'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="low"
))

# Sample 390: V6/G7 - Topic: Technology (AI)
samples.append(create_sample(
    index=390,
    vocab_band=6,
    grammar_band=7,
    question="What are the dangers of AI?",
    transcript="One danger is job loss. Machines can do work faster and cheaper than humans. Many people might become unemployed. Another risk is privacy. AI can collect data about us without us knowing. It can track our movements. Also, we might rely on it too much. If the system fails, we won't know what to do. We need to be careful.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'job loss', 'unemployed', 'privacy', 'collect data', 'track', 'rely on', 'fails'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'automation', 'surveillance', 'dependency'.",
    grammar_reason="[GRA7] Conditionals: 'If the system fails...'. Comparison: 'faster and cheaper'. >Band 6: Frequent error-free sentences. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 391: V6/G7 - Topic: Culture (Global)
samples.append(create_sample(
    index=391,
    vocab_band=6,
    grammar_band=7,
    question="How can we protect local culture?",
    transcript="We need to value our traditions. Parents should teach their children about their history and customs. Language is also important. We must keep speaking our native language. Festivals are a good way to celebrate culture. They bring people together. The government can help by funding museums and cultural events. If we don't act, globalization might erase our unique identity.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'value', 'traditions', 'customs', 'native', 'celebrate', 'funding', 'globalization', 'erase', 'unique identity'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'preserve', 'heritage', 'diversity'.",
    grammar_reason="[GRA7] Conditionals: 'If we don't act...'. Modals: 'Should teach', 'Must keep'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 392: V6/G7 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=392,
    vocab_band=6,
    grammar_band=7,
    question="Why is it hard to recycle?",
    transcript="It can be confusing. There are many different types of plastic and paper. People don't know which bin to use. If they make a mistake, the whole bin is contaminated. Also, it takes effort. You have to wash the trash and separate it. Some people are too lazy. We need clearer rules and better facilities to make it easier.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'confusing', 'contaminated', 'effort', 'separate', 'facilities'. >Band 5: Specific terms. Not Band 7: Lacks 'incentive', 'guidelines', 'waste management'.",
    grammar_reason="[GRA7] Conditionals: 'If they make a mistake...'. Passive: 'is contaminated'. >Band 6: Accurate grammar. Not Band 8: Simple sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 393: V6/G7 - Topic: Society (Friendship)
samples.append(create_sample(
    index=393,
    vocab_band=6,
    grammar_band=7,
    question="What qualities are important in a friend?",
    transcript="Trust is the most important. You need to know they will keep your secrets. Also, kindness and support. A good friend helps you when you are sad. They are happy for your success. Humor is good too. It is fun to laugh together. Finally, honesty. A friend should tell you the truth, even if it is hard to hear.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'trust', 'secrets', 'kindness', 'support', 'success', 'humor', 'honesty'. >Band 5: Good topic words. Not Band 7: Lacks 'loyalty', 'reliable', 'genuine'.",
    grammar_reason="[GRA7] Conditionals: 'even if it is hard...'. Time clause: 'when you are sad'. >Band 6: Accurate grammar. Not Band 8: Short sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 394: V6/G7 - Topic: Work (Remote)
samples.append(create_sample(
    index=394,
    vocab_band=6,
    grammar_band=7,
    question="Does working from home affect productivity?",
    transcript="It depends on the person. For some, it increases productivity. There are no distractions from colleagues. No time wasted on commuting. They can focus better. But for others, it is harder. They might watch TV or do housework instead of working. They need discipline. So, it can be good or bad depending on your personality.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'productivity', 'distractions', 'colleagues', 'wasted', 'commuting', 'focus', 'discipline', 'personality'. >Band 5: Relevant terms. Not Band 7: Lacks 'efficiency', 'environment', 'motivated'.",
    grammar_reason="[GRA7] Contrast: 'But for others'. Reason: 'depending on your personality'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structure.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 395: V6/G7 - Topic: Education (Reading)
samples.append(create_sample(
    index=395,
    vocab_band=6,
    grammar_band=7,
    question="Why don't people read books anymore?",
    transcript="Because we have the internet. Information is instant. Videos and social media are more exciting. They grab our attention quickly. Reading a book takes time and patience. Modern life is fast, so people don't have time to sit and read. Also, books can be expensive. However, reading is still the best way to improve your mind and vocabulary.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'instant', 'grab', 'attention', 'patience', 'expensive', 'improve', 'mind'. >Band 5: Clear meaning. Not Band 7: Lacks 'concentration', 'literacy', 'accessible'.",
    grammar_reason="[GRA7] Reason: 'Because we have...'. Contrast: 'However'. >Band 6: Accurate grammar. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 396: V6/G7 - Topic: Technology (Data)
samples.append(create_sample(
    index=396,
    vocab_band=6,
    grammar_band=7,
    question="Should we be worried about data privacy?",
    transcript="Yes, definitely. Our data is very valuable. Companies buy and sell it. They know everything about us. Where we go, what we buy. This can be used to manipulate us. Also, data leaks happen. Hackers can steal your identity. We need better laws to protect our information. We should be careful about what we share online.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'valuable', 'manipulate', 'leaks', 'hackers', 'steal', 'identity', 'protect'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'surveillance', 'regulation', 'security', 'breach'.",
    grammar_reason="[GRA7] Passive: 'can be used'. Modals: 'Need to', 'Should be'. >Band 6: Accurate grammar. Not Band 8: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 397: V6/G7 - Topic: Society (Family)
samples.append(create_sample(
    index=397,
    vocab_band=6,
    grammar_band=7,
    question="Is it better to grow up in a big family?",
    transcript="There are advantages. You are never lonely. You have brothers and sisters to play with. You learn to share and compromise. It is a lively environment. But there are downsides. It is expensive for parents. There is less privacy and space. A small family is quieter and maybe richer. Both have good points.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'advantages', 'lonely', 'compromise', 'lively', 'environment', 'downsides', 'privacy'. >Band 5: Good range. Not Band 7: Lacks 'support network', 'chaos', 'attention'.",
    grammar_reason="[GRA7] Contrast: 'But there are downsides'. Comparison: 'quieter and maybe richer'. >Band 6: Frequent error-free sentences. Not Band 8: Simple structure.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 398: V6/G7 - Topic: Culture (Fashion)
samples.append(create_sample(
    index=398,
    vocab_band=6,
    grammar_band=7,
    question="Is it important to dress well?",
    transcript="It depends on the situation. For a job interview or a wedding, yes. It shows respect. It gives a good first impression. People judge you by your clothes. If you look smart, they trust you more. But in free time, comfort is key. You should wear what makes you happy. Fashion is a way to express yourself.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'situation', 'respect', 'impression', 'judge', 'smart', 'comfort', 'express yourself'. >Band 5: Relevant words. Not Band 7: Lacks 'professionalism', 'appropriately', 'image'.",
    grammar_reason="[GRA7] Conditionals: 'If you look smart...'. Reason: 'It shows respect'. >Band 6: Accurate grammar. Not Band 8: Sentences are somewhat short.",
    idiom_present=False,
    risk_level="low"
))

# Sample 399: V6/G7 - Topic: Transport (Safety)
samples.append(create_sample(
    index=399,
    vocab_band=6,
    grammar_band=7,
    question="Why are young drivers more likely to have accidents?",
    transcript="They lack experience. They don't know how to react in dangerous situations. Also, they are often overconfident. They drive too fast and take risks. They might use their phones while driving. Peer pressure is another factor. If friends are in the car, they might show off. Older drivers are more careful and patient.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'lack', 'react', 'dangerous', 'overconfident', 'risks', 'peer pressure', 'factor', 'show off', 'patient'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'judgment', 'reckless', 'distraction'.",
    grammar_reason="[GRA7] Conditionals: 'If friends are in the car...'. Comparison: 'Older drivers are more careful'. >Band 6: Frequent error-free sentences. Not Band 8: Standard forms.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 400: V6/G7 - Topic: Environment (Trees)
samples.append(create_sample(
    index=400,
    vocab_band=6,
    grammar_band=7,
    question="Should we plant more trees in cities?",
    transcript="Definitely. Trees make the city look beautiful. But more importantly, they improve air quality. They absorb pollution and give oxygen. They also provide shade, which cools the streets in summer. Trees are good for mental health too. Seeing green nature makes people calm. A concrete city is depressing. We need nature in our lives.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'improve', 'quality', 'absorb', 'pollution', 'oxygen', 'shade', 'cools', 'mental health', 'concrete', 'depressing'. >Band 5: Advanced terms. Not Band 7: Lacks 'aesthetic', 'temperature', 'environment'.",
    grammar_reason="[GRA7] Relative clause: 'which cools the streets'. Contrast: 'But more importantly'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
