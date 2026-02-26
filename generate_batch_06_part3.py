import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch06.jsonl")

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

# --- BATCH 06 PART 3: SAMPLES 501-525 (25 Total) ---
# Combo: V7/G7

# Sample 501: V7/G7 - Topic: Culture (Art)
samples.append(create_sample(
    index=501,
    vocab_band=7,
    grammar_band=7,
    question="Why is public art important?",
    transcript="It makes cities more vibrant and interesting. Art accessible to everyone democratizes culture. It sparks conversation and debate. Murals and sculptures can transform a dull space into a landmark. It also fosters a sense of community pride. When people see their culture represented, they feel connected. Public art is an expression of our collective identity.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'vibrant', 'democratizes', 'sparks', 'murals', 'transform', 'landmark', 'fosters', 'collective identity'. >Band 6: Sophisticated vocabulary. Not Band 8: Lacks idiomatic flow.",
    grammar_reason="[GRA7] Time clause: 'When people see...'. Relative clause implied. >Band 6: Frequent error-free sentences. Not Band 8: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 502: V7/G7 - Topic: Technology (Robots)
samples.append(create_sample(
    index=502,
    vocab_band=7,
    grammar_band=7,
    question="Will robots take over the world?",
    transcript="That is a popular science fiction trope, but it is unlikely. Robots are tools created by humans. They lack consciousness and desire. They only do what they are programmed to do. However, if we give them too much autonomy, accidents could happen. We need strict safety protocols. The real danger is not robot rebellion, but human misuse of technology.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'trope', 'unlikely', 'consciousness', 'desire', 'programmed', 'autonomy', 'protocols', 'rebellion', 'misuse'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'sentience', 'singularity'.",
    grammar_reason="[GRA7] Contrast: 'but it is unlikely'. Conditionals: 'if we give them...'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 503: V7/G7 - Topic: Health (Diet)
samples.append(create_sample(
    index=503,
    vocab_band=7,
    grammar_band=7,
    question="Why is breakfast the most important meal?",
    transcript="It kick-starts your metabolism. After sleeping for hours, your body needs fuel. Eating a nutritious breakfast improves concentration and energy levels. Studies show that people who eat breakfast perform better at work and school. It prevents overeating later in the day. Skipping it can lead to weight gain and fatigue. It sets the tone for the rest of the day.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'sets the tone' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'kick-starts', 'metabolism', 'fuel', 'nutritious', 'concentration', 'overeating', 'fatigue'. Idiom: 'sets the tone'. >Band 6: Precise terms. Not Band 8: Slightly robotic.",
    grammar_reason="[GRA7] Time clause: 'After sleeping...'. Relative clause: 'people who eat...'. >Band 6: Good control. Not Band 8: Structure is functional.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 504: V7/G7 - Topic: Work (Remote)
samples.append(create_sample(
    index=504,
    vocab_band=7,
    grammar_band=7,
    question="How can remote workers stay motivated?",
    transcript="Self-discipline is crucial. Setting a strict routine helps. Wake up at the same time and dress for work. This puts you in the right mindset. Creating a dedicated workspace is also important. It separates professional and personal life. Regular breaks prevent burnout. Staying connected with colleagues through video calls combats isolation. Motivation comes from within, but structure helps.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'crucial', 'routine', 'mindset', 'dedicated workspace', 'separates', 'burnout', 'combats', 'isolation'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'intrinsic', 'accountability'.",
    grammar_reason="[GRA7] Reason: 'This puts you...'. Contrast: 'Motivation comes from within, but...'. >Band 6: Accurate complex sentences. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 505: V7/G7 - Topic: Society (Cities)
samples.append(create_sample(
    index=505,
    vocab_band=7,
    grammar_band=7,
    question="How can we make cities safer?",
    transcript="Better urban planning can help. Well-lit streets deter criminals. Public spaces should be open and visible. Community policing is effective too. When police build trust with residents, crime goes down. Addressing social issues like poverty and unemployment is the long-term solution. Desperate people commit crimes. If we improve living standards, safety will naturally follow.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'urban planning', 'deter', 'visible', 'policing', 'residents', 'addressing', 'living standards'. >Band 6: Good range. Not Band 8: Lacks 'surveillance', 'intervention', 'root cause'.",
    grammar_reason="[GRA7] Time clause: 'When police build trust'. Conditionals: 'If we improve...'. >Band 6: Frequent error-free sentences. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 506: V7/G7 - Topic: Environment (Global Warming)
samples.append(create_sample(
    index=506,
    vocab_band=7,
    grammar_band=7,
    question="What is the impact of melting glaciers?",
    transcript="It contributes to rising sea levels. This threatens coastal cities and island nations. Millions of people could be displaced. Also, glaciers are a source of fresh water for many rivers. If they disappear, water scarcity will become a crisis. It affects agriculture and drinking water. The ecosystem is delicate. One change triggers a chain reaction.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'chain reaction' (collocation)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'contributes', 'threatens', 'displaced', 'source', 'scarcity', 'crisis', 'delicate', 'triggers'. Collocation: 'chain reaction'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA7] Conditionals: 'If they disappear...'. Relative clause implied. >Band 6: Good control. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 507: V7/G7 - Topic: Transport (Flying)
samples.append(create_sample(
    index=507,
    vocab_band=7,
    grammar_band=7,
    question="Why is air travel so popular?",
    transcript="Speed is the main factor. You can cross oceans in hours. It makes the world smaller. Also, affordability has increased. Budget airlines make travel accessible to more people. It connects families and businesses globally. Despite the environmental cost, the convenience is undeniable. People value time, and flying saves a lot of it.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'factor', 'affordability', 'budget airlines', 'accessible', 'connects', 'globally', 'undeniable'. >Band 6: Relevant terms. Not Band 8: Lacks 'globalization', 'connectivity'.",
    grammar_reason="[GRA7] Contrast: 'Despite the environmental cost'. Reason: 'Speed is the main factor'. >Band 6: Accurate grammar. Not Band 8: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 508: V7/G7 - Topic: Education (Reading)
samples.append(create_sample(
    index=508,
    vocab_band=7,
    grammar_band=7,
    question="Do e-books have advantages over paper books?",
    transcript="Yes, they are portable. You can carry a library in your pocket. They are often cheaper and instant to download. You can adjust the font size, which is good for people with vision problems. However, some people miss the tactile experience of paper. The smell of a new book. E-books need batteries, which is a drawback. Both formats have their place.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'portable', 'instant', 'adjust', 'vision problems', 'tactile', 'drawback', 'formats'. >Band 6: Precise vocabulary. Not Band 8: Lacks 'sensory', 'convenience', 'preference'.",
    grammar_reason="[GRA7] Relative clause: 'which is good', 'which is a drawback'. Contrast: 'However'. >Band 6: Frequent error-free sentences. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 509: V7/G7 - Topic: Culture (Tradition)
samples.append(create_sample(
    index=509,
    vocab_band=7,
    grammar_band=7,
    question="Why are weddings important?",
    transcript="They are a rite of passage. A public declaration of commitment. Weddings bring families together to celebrate love. It strengthens social bonds. Also, they are steeped in tradition. Rituals and customs connect us to our ancestors. While some think they are expensive parties, for many, the symbolism is profound. It marks the start of a new chapter in life.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'rite of passage' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'declaration', 'commitment', 'strengthens', 'bonds', 'steeped in', 'rituals', 'ancestors', 'symbolism', 'profound'. Idiom: 'rite of passage'. >Band 6: Sophisticated terms. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA7] Contrast: 'While some think...'. Relative clause implied. >Band 6: Good control. Not Band 8: Limited complexity.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 510: V7/G7 - Topic: Technology (Internet)
samples.append(create_sample(
    index=510,
    vocab_band=7,
    grammar_band=7,
    question="Has the internet made us impatient?",
    transcript="I think so. We are used to instant gratification. We want answers now. If a video buffers for five seconds, we get annoyed. We have lost the art of waiting. This affects our attention span. We scan text instead of reading deeply. We expect everything to be fast. It is harder to focus on long-term goals.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'instant gratification' (collocation)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'gratification', 'buffers', 'annoyed', 'attention span', 'scan', 'deeply', 'expect'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'tolerance', 'immediate', 'consequence'.",
    grammar_reason="[GRA7] Conditionals: 'If a video buffers...'. Contrast implied. >Band 6: Accurate grammar. Not Band 8: Sentences are somewhat short.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 511: V7/G7 - Topic: Work (Career)
samples.append(create_sample(
    index=511,
    vocab_band=7,
    grammar_band=7,
    question="Should we choose a career based on money or passion?",
    transcript="Ideally, a mix of both. Passion gives you motivation. If you love your work, you will excel. However, bills must be paid. Financial stability is crucial for a stress-free life. Choosing a job only for money can lead to burnout. Choosing only for passion might lead to poverty. A pragmatic approach is best. Find something you like that also pays the bills.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'ideally', 'motivation', 'excel', 'stability', 'crucial', 'burnout', 'poverty', 'pragmatic'. >Band 6: Good range. Not Band 8: Lacks 'fulfillment', 'sustain', 'compromise'.",
    grammar_reason="[GRA7] Conditionals: 'If you love your work...'. Contrast: 'However'. >Band 6: Frequent error-free sentences. Not Band 8: Structure is standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 512: V7/G7 - Topic: Society (Friendship)
samples.append(create_sample(
    index=512,
    vocab_band=7,
    grammar_band=7,
    question="Why do friends drift apart?",
    transcript="Life circumstances change. People move to different cities for work. Physical distance creates emotional distance. Also, priorities shift. When people get married and have children, they have less time for friends. Interests change too. You might not have anything in common anymore. It is natural. Not all friendships are meant to last forever.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'drift apart' (phrasal verb)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'circumstances', 'physical distance', 'emotional', 'priorities', 'shift', 'in common', 'natural'. Phrasal verb: 'drift apart'. >Band 6: Clear meaning. Not Band 8: Lacks 'evolution', 'diverge', 'mutual'.",
    grammar_reason="[GRA7] Time clause: 'When people get married'. Reason: 'Because life circumstances change' (implied). >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 513: V7/G7 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=513,
    vocab_band=7,
    grammar_band=7,
    question="Should recycling be mandatory?",
    transcript="I believe it should. Voluntary recycling is not enough. Too much waste still goes to landfill. If it were law, people would take it seriously. Fines could enforce it. It forces people to be responsible for their consumption. Some might complain about the inconvenience, but the environmental benefit outweighs the cost. We need drastic measures to save the planet.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'voluntary', 'landfill', 'enforce', 'responsible', 'consumption', 'inconvenience', 'outweighs', 'drastic'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA7] Conditionals: 'If it were law...'. Contrast: 'but the environmental benefit...'. >Band 6: Good control. Not Band 8: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 514: V7/G7 - Topic: Culture (Global)
samples.append(create_sample(
    index=514,
    vocab_band=7,
    grammar_band=7,
    question="How does travel affect prejudice?",
    transcript="It destroys it. Prejudice often comes from ignorance. When you travel, you meet real people, not stereotypes. You realize that we all have similar hopes and fears. Sharing a meal or a conversation breaks down barriers. You see the humanity in others. It makes you more open-minded and tolerant. Travel is the enemy of bigotry.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'breaks down barriers' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'destroys', 'prejudice', 'ignorance', 'stereotypes', 'humanity', 'open-minded', 'tolerant', 'bigotry'. Idiom: 'breaks down barriers'. >Band 6: Advanced vocabulary. Not Band 8: Lacks 'misconception', 'perspective', 'empathy'.",
    grammar_reason="[GRA7] Time clause: 'When you travel'. Reason: 'Prejudice often comes...'. >Band 6: Accurate grammar. Not Band 8: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 515: V7/G7 - Topic: Education (University)
samples.append(create_sample(
    index=515,
    vocab_band=7,
    grammar_band=7,
    question="What is the role of universities in society?",
    transcript="They are centers of knowledge and innovation. Universities research solutions to global problems, like climate change or disease. They educate the future workforce, providing skilled professionals. Also, they are places of debate and critical thinking. They challenge established ideas. A society without universities would stagnate. They drive progress and social mobility.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'centers', 'innovation', 'workforce', 'skilled professionals', 'debate', 'critical thinking', 'established', 'stagnate', 'social mobility'. >Band 6: Sophisticated terms. Not Band 8: Slightly academic.",
    grammar_reason="[GRA7] Conditionals: 'without universities would...'. Relative clause implied. >Band 6: Frequent error-free sentences. Not Band 8: Structure is functional.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 516: V7/G7 - Topic: Technology (Games)
samples.append(create_sample(
    index=516,
    vocab_band=7,
    grammar_band=7,
    question="Why are esports becoming popular?",
    transcript="It is the competitive nature. Just like traditional sports, people love to see skill and strategy. The players are professionals who train hard. Also, technology makes it accessible. You can watch tournaments online from anywhere. It has a massive community. Young people identify with gamers more than athletes. It is a digital evolution of sport.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'competitive', 'nature', 'strategy', 'professionals', 'accessible', 'tournaments', 'massive', 'identify with', 'evolution'. >Band 6: Good range. Not Band 8: Lacks 'spectator', 'entertainment', 'phenomenon'.",
    grammar_reason="[GRA7] Comparison: 'more than athletes'. Reason: 'Just like traditional sports...'. >Band 6: Accurate grammar. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 517: V7/G7 - Topic: Health (Sleep)
samples.append(create_sample(
    index=517,
    vocab_band=7,
    grammar_band=7,
    question="Does technology affect our sleep?",
    transcript="Yes, negatively. The blue light from screens suppresses melatonin, the sleep hormone. It tricks the brain into thinking it is day. Also, social media is addictive. We scroll for hours instead of sleeping. The constant flow of information keeps our minds active. We cannot switch off. To sleep better, we need digital detox before bed.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'switch off' (phrasal verb)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'negatively', 'suppresses', 'melatonin', 'hormone', 'tricks', 'addictive', 'scroll', 'active', 'digital detox'. >Band 6: Scientific/modern vocabulary. Not Band 8: Lacks 'insomnia', 'disrupt', 'cycle'.",
    grammar_reason="[GRA7] Reason: 'Because the blue light...'. Gerund: 'instead of sleeping'. >Band 6: Good control. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 518: V7/G7 - Topic: Transport (Cars)
samples.append(create_sample(
    index=518,
    vocab_band=7,
    grammar_band=7,
    question="Why are SUVs popular?",
    transcript="They offer a sense of safety. They are big and heavy, so drivers feel protected. Also, the high driving position gives a better view of the road. They are practical for families, with lots of space. However, they are bad for the environment. They consume more fuel and take up more space. It is a choice of comfort over conscience.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'comfort over conscience' (idiomatic)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'protected', 'position', 'practical', 'consume', 'conscience'. >Band 6: Clear meaning. Not Band 8: Lacks 'status symbol', 'utility', 'efficiency'.",
    grammar_reason="[GRA7] Reason: 'so drivers feel protected'. Contrast: 'However'. >Band 6: Accurate grammar. Not Band 8: Sentences are somewhat standard.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 519: V7/G7 - Topic: Society (Consumerism)
samples.append(create_sample(
    index=519,
    vocab_band=7,
    grammar_band=7,
    question="How can we stop overconsumption?",
    transcript="We need a cultural shift. We must value experiences over things. Minimalism is a growing trend. People realize that having less stuff leads to less stress. We should also repair things, not replace them. Companies need to stop making disposable products. If we are content with what we have, we won't need to buy constantly.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'cultural shift', 'minimalism', 'trend', 'realize', 'disposable', 'content', 'constantly'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'materialism', 'sustainability', 'marketing'.",
    grammar_reason="[GRA7] Conditionals: 'If we are content...'. Modal: 'Need to stop'. >Band 6: Frequent error-free sentences. Not Band 8: Simple sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 520: V7/G7 - Topic: Environment (Trees)
samples.append(create_sample(
    index=520,
    vocab_band=7,
    grammar_band=7,
    question="Why do we need more parks in cities?",
    transcript="Parks are the lungs of the city. They improve air quality and reduce heat. They provide a space for recreation and relaxation. People can exercise or meet friends. It improves mental health to be near nature. Also, parks support wildlife. Birds and insects need a home too. A city without parks is just a concrete jungle.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'concrete jungle' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'lungs', 'recreation', 'relaxation', 'mental health', 'wildlife', 'concrete jungle'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'urban planning', 'biodiversity', 'amenity'.",
    grammar_reason="[GRA7] Reason: 'to be near nature'. List structure. >Band 6: Accurate grammar. Not Band 8: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 521: V7/G7 - Topic: Work (Job Satisfaction)
samples.append(create_sample(
    index=521,
    vocab_band=7,
    grammar_band=7,
    question="Is salary the most important part of a job?",
    transcript="It is important, but not the most important. You need money to live, of course. But job satisfaction comes from other things. Like good colleagues and a nice boss. Also, the work itself must be interesting. If you are bored every day, no amount of money will make you happy. Purpose is more valuable than pay.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'satisfaction', 'colleagues', 'amount', 'purpose', 'valuable'. >Band 6: Clear meaning. Not Band 8: Lacks 'compensation', 'fulfillment', 'motivation'.",
    grammar_reason="[GRA7] Contrast: 'But job satisfaction...'. Conditionals: 'If you are bored...'. >Band 6: Good control. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="low"
))

# Sample 522: V7/G7 - Topic: Culture (Language)
samples.append(create_sample(
    index=522,
    vocab_band=7,
    grammar_band=7,
    question="Why is English the global language?",
    transcript="It is due to history and power. The British Empire spread the language everywhere. Then, American cultural dominance kept it there. Hollywood, music, and the internet are mostly English. It is the language of business and science. It is useful to have one common language. It makes communication easier. However, we should not let it kill other languages.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'empire', 'spread', 'dominance', 'communication', 'kill'. >Band 6: Relevant terms. Not Band 8: Lacks 'colonialism', 'lingua franca', 'hegemony'.",
    grammar_reason="[GRA7] Reason: 'Due to history'. Contrast: 'However'. >Band 6: Accurate grammar. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 523: V7/G7 - Topic: Society (Crime)
samples.append(create_sample(
    index=523,
    vocab_band=7,
    grammar_band=7,
    question="Why do people break the law?",
    transcript="There are many reasons. Poverty is a big one. If people cannot feed their families, they might steal. Addiction is another cause. Drugs make people do desperate things. Also, some people have no moral compass. They don't care about others. Peer pressure affects young people. Understanding the cause helps us find the solution.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'moral compass' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'poverty', 'addiction', 'desperate', 'moral compass', 'peer pressure'. >Band 6: Good range. Not Band 8: Lacks 'socioeconomic', 'psychological', 'deterrent'.",
    grammar_reason="[GRA7] Conditionals: 'If people cannot...'. Reason: 'Understanding the cause helps...'. >Band 6: Accurate complex sentences. Not Band 8: Limited complexity.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 524: V7/G7 - Topic: Technology (AI)
samples.append(create_sample(
    index=524,
    vocab_band=7,
    grammar_band=7,
    question="Will AI improve education?",
    transcript="It has great potential. AI can personalize learning. It adapts to the student's speed and level. If a student struggles, AI can explain it differently. It frees up teachers to focus on mentoring. However, AI cannot replace the human connection. Encouragement and empathy must come from a person. It should be a tool, not a teacher.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'potential', 'personalize', 'adapts', 'struggles', 'frees up', 'mentoring', 'encouragement', 'empathy'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'curriculum', 'pedagogy', 'supplement'.",
    grammar_reason="[GRA7] Conditionals: 'If a student struggles...'. Contrast: 'However'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 525: V7/G7 - Topic: Transport (Safety)
samples.append(create_sample(
    index=525,
    vocab_band=7,
    grammar_band=7,
    question="Is driving getting safer?",
    transcript="Yes, cars are safer now. They have airbags, sensors, and cameras. Technology helps prevent accidents. Also, roads are better designed. However, drivers are more distracted. Phones are a huge problem. Texting while driving causes many crashes. So, while the cars are safer, human behavior is still a risk. We need to be more responsible behind the wheel.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'behind the wheel' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'sensors', 'prevent', 'designed', 'distracted', 'crashes', 'behavior', 'responsible'. Idiom: 'behind the wheel'. >Band 6: Good topic words. Not Band 8: Lacks 'autonomous', 'regulation', 'fatality'.",
    grammar_reason="[GRA7] Contrast: 'However', 'So, while...'. Gerund: 'Texting while driving'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
