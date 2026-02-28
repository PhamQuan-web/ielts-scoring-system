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

# --- BATCH 04 PART 1: SAMPLES 251-275 (25 Total) ---
# Combo: V6/G6 (Competent Vocab, Competent Grammar)

# Sample 251: V6/G6 - Topic: Environment (Climate Change)
samples.append(create_sample(
    index=251,
    vocab_band=6,
    grammar_band=6,
    question="How does climate change affect people's lives?",
    transcript="It has a significant impact. Firstly, the weather patterns are changing. We see more storms and floods, which destroy homes. Secondly, it affects agriculture. Farmers struggle to grow crops because of drought. This leads to higher food prices. Also, there are health risks. Heatwaves can be dangerous for elderly people. So, it affects us in many ways.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'weather patterns are changing' (correct)",
        "phrase error: 'food prices' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'significant impact', 'weather patterns', 'agriculture', 'drought', 'heatwaves', 'elderly'. >Band 5: Good range of topic vocabulary. Not Band 7: Lacks flexibility and style.",
    grammar_reason="[GRA6] Mix of simple and complex sentences. 'which destroy homes' (relative clause). 'because of drought' (reason). >Band 5: Frequent error-free sentences. Not Band 7: Complexity is limited.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 252: V6/G6 - Topic: Technology (AI)
samples.append(create_sample(
    index=252,
    vocab_band=6,
    grammar_band=6,
    question="Will AI improve our lives?",
    transcript="I think so. AI can do boring tasks for us. This saves time and increases efficiency. For example, in medicine, AI can diagnose diseases faster than doctors. However, there are risks. People might lose their jobs if machines replace them. We need to manage this technology carefully. If we use it wisely, it will be beneficial.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'boring tasks' (correct)",
        "phrase error: 'increases efficiency' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'efficiency', 'diagnose', 'diseases', 'replace', 'beneficial', 'wisely'. >Band 5: Clear meaning with some advanced words. Not Band 7: Collocations are standard.",
    grammar_reason="[GRA6] Conditionals: 'If we use it wisely...'. Comparative: 'faster than doctors'. >Band 5: Good control of grammar. Not Band 7: Lacks variety in structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 253: V6/G6 - Topic: Education (Online)
samples.append(create_sample(
    index=253,
    vocab_band=6,
    grammar_band=6,
    question="What are the disadvantages of online learning?",
    transcript="One major disadvantage is the lack of social interaction. Students sit alone at home. They miss the chance to make friends. Also, technical problems can happen. If the internet connection is bad, you cannot learn. Furthermore, it requires self-discipline. Some students get distracted easily by games or social media. It is not suitable for everyone.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'technical problems' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'disadvantage', 'social interaction', 'technical problems', 'connection', 'self-discipline', 'distracted', 'suitable'. >Band 5: Precise terms. Not Band 7: Lacks idiomatic expressions.",
    grammar_reason="[GRA6] Conditionals: 'If the internet connection is bad...'. Connectors: 'One major disadvantage...', 'Furthermore'. >Band 5: Coherent and accurate. Not Band 7: Sentences are somewhat repetitive.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 254: V6/G6 - Topic: Work (Job Security)
samples.append(create_sample(
    index=254,
    vocab_band=6,
    grammar_band=6,
    question="Is job security important?",
    transcript="Yes, it is very important. People need a stable income to pay bills and rent. If you worry about losing your job, it causes stress. You cannot plan for the future. For example, buying a house is difficult without a permanent contract. Job security gives peace of mind. It allows employees to focus on their work better.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'peace of mind' (idiomatic)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'stable income', 'permanent contract', 'peace of mind', 'focus'. >Band 5: Good vocabulary range. Not Band 7: Usage is functional.",
    grammar_reason="[GRA6] Conditionals: 'If you worry...'. Reason: 'to pay bills'. >Band 5: Error-free sentences. Not Band 7: Limited range of complex structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 255: V6/G6 - Topic: Society (Equality)
samples.append(create_sample(
    index=255,
    vocab_band=6,
    grammar_band=6,
    question="How can we achieve gender equality?",
    transcript="We need to change our mindset. Education is the first step. Schools should teach that boys and girls are equal. Also, companies must offer equal pay for equal work. Women should have the same opportunities for leadership roles. Government policies can help too. For example, providing support for childcare so mothers can work.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'change our mindset' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'mindset', 'equal pay', 'opportunities', 'leadership roles', 'policies', 'childcare'. >Band 5: Specific terms. Not Band 7: Lacks nuance.",
    grammar_reason="[GRA6] Modals: 'should teach', 'must offer'. Purpose: 'so mothers can work'. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 256: V6/G6 - Topic: Health (Mental)
samples.append(create_sample(
    index=256,
    vocab_band=6,
    grammar_band=6,
    question="What causes stress in modern life?",
    transcript="There are many factors. Work pressure is a big one. People work long hours and fear losing their jobs. Also, technology plays a part. We are always connected, so we never relax properly. Financial problems cause anxiety too. The cost of living is rising. People worry about money constantly. All these things create a stressful environment.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'cost of living' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'factors', 'pressure', 'connected', 'anxiety', 'cost of living', 'constantly', 'environment'. >Band 5: Relevant vocabulary. Not Band 7: Lacks collocations.",
    grammar_reason="[GRA6] Reason: 'so we never relax'. Relative clause implied. >Band 5: Good control. Not Band 7: Repetitive structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 257: V6/G6 - Topic: Culture (Tradition)
samples.append(create_sample(
    index=257,
    vocab_band=6,
    grammar_band=6,
    question="Is it important to preserve traditions?",
    transcript="Yes, traditions are part of our identity. They tell us who we are and where we come from. Festivals and ceremonies bring communities together. If we lose them, we lose our history. However, some traditions are outdated. We should adapt them to modern life. We can keep the good values while changing harmful practices.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'harmful practices' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'identity', 'ceremonies', 'communities', 'outdated', 'adapt', 'values', 'practices'. >Band 5: Good range. Not Band 7: Lacks idiomatic flow.",
    grammar_reason="[GRA6] Conditionals: 'If we lose them...'. Contrast: 'However'. >Band 5: Accurate complex sentences. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 258: V6/G6 - Topic: Transport (Bicycles)
samples.append(create_sample(
    index=258,
    vocab_band=6,
    grammar_band=6,
    question="Why is cycling good for cities?",
    transcript="It helps reduce traffic congestion. If more people cycle, there are fewer cars on the road. This leads to less pollution and cleaner air. Cycling is also quiet, so it reduces noise levels. For the individual, it is a healthy activity. It saves money on fuel and parking. Cities become more livable when they are bike-friendly.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'bike-friendly' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'congestion', 'pollution', 'noise levels', 'individual', 'fuel', 'livable', 'bike-friendly'. >Band 5: Specific terms. Not Band 7: Lacks sophistication.",
    grammar_reason="[GRA6] Conditionals: 'If more people cycle...'. Time clause: 'when they are bike-friendly'. >Band 5: Error-free sentences. Not Band 7: Simple phrasing.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 259: V6/G6 - Topic: Society (Happiness)
samples.append(create_sample(
    index=259,
    vocab_band=6,
    grammar_band=6,
    question="What is the key to happiness?",
    transcript="I believe it is balance. You need a good balance between work and personal life. Money is necessary, but relationships are more important. Spending time with family and friends brings joy. Also, having a purpose is key. Doing something you love gives satisfaction. Health is also vital. Without health, you cannot enjoy anything.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'brings joy' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'balance', 'personal life', 'necessary', 'joy', 'purpose', 'satisfaction', 'vital'. >Band 5: Abstract vocabulary. Not Band 7: Lacks idiomatic expressions.",
    grammar_reason="[GRA6] Contrast: 'Money is necessary, but...'. Conditionals: 'Without health, you cannot...'. >Band 5: Accurate structure. Not Band 7: Limited range.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 260: V6/G6 - Topic: Environment (Waste)
samples.append(create_sample(
    index=260,
    vocab_band=6,
    grammar_band=6,
    question="How can we deal with the problem of waste?",
    transcript="We must follow the three Rs: reduce, reuse, and recycle. Firstly, we should buy less packaging. Secondly, we can reuse items like bags and bottles. Finally, recycling is essential for materials like glass and paper. Governments should provide better facilities for recycling. Also, companies should design products that last longer. This will decrease the amount of trash.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'three Rs' (correct term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'packaging', 'essential', 'materials', 'facilities', 'design', 'decrease'. >Band 5: Relevant terms. Not Band 7: Lacks 'sustainable', 'consumption', 'waste management'.",
    grammar_reason="[GRA6] Sequencing: 'Firstly... Secondly... Finally...'. Modals: 'Should provide', 'Should design'. >Band 5: Clear organization. Not Band 7: Simple sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 261: V6/G6 - Topic: Technology (Space)
samples.append(create_sample(
    index=261,
    vocab_band=6,
    grammar_band=6,
    question="Should we spend money on space exploration?",
    transcript="It is a difficult choice. Space exploration is expensive, but it has benefits. We discover new technologies that help us on Earth. For example, satellite communication. Also, we might find resources or a new place to live. However, we have urgent problems here, like poverty. I think we should balance the budget. Spend some on space, but more on Earth.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'urgent problems' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'exploration', 'benefits', 'technologies', 'satellite communication', 'resources', 'urgent', 'budget'. >Band 5: Good range. Not Band 7: Lacks 'investment', 'scientific advancement'.",
    grammar_reason="[GRA6] Contrast: 'but it has benefits'. Relative clause: 'that help us'. >Band 5: Accurate grammar. Not Band 7: Sentences are somewhat short.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 262: V6/G6 - Topic: Culture (Global)
samples.append(create_sample(
    index=262,
    vocab_band=6,
    grammar_band=6,
    question="Is global culture a threat to local traditions?",
    transcript="Yes, it can be. Western culture is very powerful. Young people often prefer international music and fashion. They might forget their own customs. Local languages are also at risk. However, globalization allows us to share our culture too. We can learn from each other. It is not all bad, but we must protect our heritage.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'at risk' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'threat', 'powerful', 'prefer', 'customs', 'globalization', 'heritage'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'dominance', 'homogenization', 'preserve'.",
    grammar_reason="[GRA6] Contrast: 'However', 'But'. Modal: 'Must protect'. >Band 5: Clear structure. Not Band 7: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 263: V6/G6 - Topic: Work (Teamwork)
samples.append(create_sample(
    index=263,
    vocab_band=6,
    grammar_band=6,
    question="Why is teamwork important?",
    transcript="Teamwork allows people to achieve more. When we work together, we can share ideas and solve problems faster. Everyone has different skills. We can learn from each other. Also, it builds trust and friendship. Working alone can be lonely and difficult. In a team, you have support. This improves productivity and morale.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'achieve more' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'achieve', 'solve problems', 'skills', 'trust', 'support', 'productivity', 'morale'. >Band 5: Good range. Not Band 7: Lacks 'collaborate', 'synergy', 'efficiency'.",
    grammar_reason="[GRA6] Time clause: 'When we work together'. Contrast: 'Working alone can be...'. >Band 5: Correct grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 264: V6/G6 - Topic: Education (Reading)
samples.append(create_sample(
    index=264,
    vocab_band=6,
    grammar_band=6,
    question="How can we encourage children to read?",
    transcript="Parents play a big role. They should read stories to their children every night. This makes reading fun. Schools should have interesting libraries. If books are boring, children will hate reading. We can also use technology. E-books and interactive stories are popular. The main thing is to make it a habit, not a chore.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'not a chore' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'role', 'libraries', 'interactive', 'habit', 'chore'. >Band 5: Clear vocabulary. Not Band 7: Lacks 'literacy', 'engage', 'imagination'.",
    grammar_reason="[GRA6] Conditionals: 'If books are boring...'. Modals: 'Should read'. >Band 5: Accurate structures. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 265: V6/G6 - Topic: Transport (Cities)
samples.append(create_sample(
    index=265,
    vocab_band=6,
    grammar_band=6,
    question="What will transport look like in the future?",
    transcript="I think electric cars will be standard. They are cleaner and quieter. Also, self-driving cars might become common. This will reduce accidents caused by human error. Public transport will be faster. Maybe high-speed trains or flying taxis. The goal is to make travel efficient and eco-friendly. However, it will take time to build the infrastructure.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'human error' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'standard', 'self-driving', 'human error', 'efficient', 'eco-friendly', 'infrastructure'. >Band 5: Advanced vocabulary. Not Band 7: Lacks natural flow.",
    grammar_reason="[GRA6] Future forms: 'Will be', 'Might become'. Reason: 'caused by human error'. >Band 5: Good grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 266: V6/G6 - Topic: Society (Celebrity)
samples.append(create_sample(
    index=266,
    vocab_band=6,
    grammar_band=6,
    question="Why are people obsessed with celebrities?",
    transcript="People admire their lifestyle. Celebrities seem perfect. They have money, beauty, and fame. People want to escape their own ordinary lives. Also, media is responsible. They show celebrities everywhere. On TV and social media. We feel like we know them. It gives people something to talk about. But it can be unhealthy if we compare ourselves to them.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'ordinary lives' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'admire', 'lifestyle', 'fame', 'escape', 'ordinary', 'responsible', 'unhealthy', 'compare'. >Band 5: Good topic words. Not Band 7: Lacks 'fascination', 'idolize', 'influence'.",
    grammar_reason="[GRA6] Contrast: 'But it can be...'. Conditionals: 'if we compare...'. >Band 5: Accurate grammar. Not Band 7: Simple structure.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 267: V6/G6 - Topic: Environment (Animals)
samples.append(create_sample(
    index=267,
    vocab_band=6,
    grammar_band=6,
    question="Why should we protect endangered species?",
    transcript="Because every animal has a role in the ecosystem. If one species dies, it affects others. This can destroy the balance of nature. Also, animals are beautiful. Future generations should have the chance to see them. We have a moral duty to protect them. Human activity caused the problem, so we must fix it.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'moral duty' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'role', 'ecosystem', 'species', 'balance', 'generations', 'moral duty'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'biodiversity', 'extinction', 'chain reaction'.",
    grammar_reason="[GRA6] Conditionals: 'If one species dies...'. Reason: 'so we must fix it'. >Band 5: Good control. Not Band 7: Sentences are somewhat short.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 268: V6/G6 - Topic: Health (Exercise)
samples.append(create_sample(
    index=268,
    vocab_band=6,
    grammar_band=6,
    question="Why don't people exercise enough?",
    transcript="Modern life is sedentary. We sit at desks for work. We drive cars instead of walking. Also, people are busy. They say they have no time for the gym. Exercise requires effort and motivation. Many people prefer to relax and watch TV. However, lack of exercise leads to health problems like obesity.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'lack of exercise' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'sedentary', 'desks', 'requires', 'effort', 'motivation', 'lack of', 'obesity'. >Band 5: Specific terms. Not Band 7: Lacks 'priority', 'commitment', 'fitness'.",
    grammar_reason="[GRA6] Contrast: 'However'. Gerund: 'instead of walking'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 269: V6/G6 - Topic: Technology (Communication)
samples.append(create_sample(
    index=269,
    vocab_band=6,
    grammar_band=6,
    question="Has technology improved communication?",
    transcript="In many ways, yes. It is faster and easier. We can talk to people on the other side of the world instantly. Video calls help us see family. However, the quality of communication has dropped. People send short texts. They use emojis instead of words. Face-to-face conversation is becoming rare. We are connected, but maybe less close.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'quality of communication' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'instantly', 'quality', 'dropped', 'rare', 'connected'. >Band 5: Relevant words. Not Band 7: Lacks 'superficial', 'interaction', 'relationship'.",
    grammar_reason="[GRA6] Contrast: 'However', 'But'. Present Perfect: 'has dropped'. >Band 5: Good grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 270: V6/G6 - Topic: Work (Retirement)
samples.append(create_sample(
    index=270,
    vocab_band=6,
    grammar_band=6,
    question="Should there be a mandatory retirement age?",
    transcript="I don't think so. Some people are still healthy and active at 70. They have valuable experience. If we force them to stop, it is a waste of talent. Also, work gives them purpose. On the other hand, young people need jobs. If old people stay, there are fewer opportunities for the youth. A flexible system would be best.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'waste of talent' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'mandatory', 'active', 'valuable', 'force', 'purpose', 'opportunities', 'flexible'. >Band 5: Good vocabulary. Not Band 7: Lacks 'contribution', 'workforce', 'policy'.",
    grammar_reason="[GRA6] Conditionals: 'If we force them...', 'If old people stay...'. >Band 5: Accurate complex sentences. Not Band 7: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 271: V6/G6 - Topic: Education (Science vs Art)
samples.append(create_sample(
    index=271,
    vocab_band=6,
    grammar_band=6,
    question="Is science more important than art?",
    transcript="They are both important. Science helps us understand the world. It gives us technology and medicine. It solves practical problems. Art is about expression and emotion. It makes life beautiful. It encourages creativity. A society needs both engineers and artists. Focusing only on science makes us like robots. We need balance in education.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'makes us like robots' (simile)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'practical', 'expression', 'emotion', 'encourages', 'creativity', 'society', 'focusing', 'balance'. >Band 5: Relevant terms. Not Band 7: Lacks 'innovation', 'perspective', 'humanities'.",
    grammar_reason="[GRA6] Reason: 'It gives us...'. Contrast implied. >Band 5: Accurate grammar. Not Band 7: Simple sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 272: V6/G6 - Topic: Culture (Language)
samples.append(create_sample(
    index=272,
    vocab_band=6,
    grammar_band=6,
    question="Will English remain the global language?",
    transcript="For now, yes. It is the language of business, science, and the internet. Most people learn it as a second language. It is very useful for travel. However, things can change. Chinese is becoming important too. Maybe in the future, we will use translation technology more. Then we can speak our own language and understand everyone.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'things can change' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'remain', 'business', 'useful', 'translation technology'. >Band 5: Clear meaning. Not Band 7: Lacks 'dominant', 'lingua franca', 'influence'.",
    grammar_reason="[GRA6] Future tense: 'Things can change', 'Will use'. Contrast: 'However'. >Band 5: Good grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 273: V6/G6 - Topic: Society (Community)
samples.append(create_sample(
    index=273,
    vocab_band=6,
    grammar_band=6,
    question="How can we build a strong community?",
    transcript="Communication is key. Neighbors should talk to each other. We can organize local events. Like street parties or markets. This helps people connect. Also, helping each other is important. If someone is sick or old, we should offer support. Shared spaces like parks are good places to meet. A strong community feels safe and welcoming.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Communication is key' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'communication', 'organize', 'connect', 'support', 'shared spaces', 'welcoming'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'solidarity', 'initiative', 'relationships'.",
    grammar_reason="[GRA6] Conditionals: 'If someone is sick...'. Modals: 'Should talk', 'Should offer'. >Band 5: Accurate grammar. Not Band 7: Simple structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 274: V6/G6 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=274,
    vocab_band=6,
    grammar_band=6,
    question="Is it enough to just recycle?",
    transcript="No, recycling is not enough. The process uses energy too. We need to focus on reducing. Buying less stuff. Also reusing things. Repairing broken items instead of throwing them away. Companies produce too much plastic. We need to change the way we live. A circular economy is the goal. Where nothing is wasted.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'circular economy' (advanced term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'process', 'reducing', 'repairing', 'produce', 'circular economy', 'wasted'. >Band 5: Strong vocabulary. Not Band 7: Lacks idiomatic usage.",
    grammar_reason="[GRA6] Gerunds: 'Buying', 'Reusing', 'Repairing'. Reason: 'The process uses energy'. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 275: V6/G6 - Topic: Technology (Internet)
samples.append(create_sample(
    index=275,
    vocab_band=6,
    grammar_band=6,
    question="Is the internet a safe place for children?",
    transcript="Not really. There is a lot of bad content. Violence and inappropriate videos. Also, strangers can contact children. Cyberbullying is a big problem. It can hurt mental health. Parents must be careful. They should use parental controls. Also, talk to their kids about online safety. Education is better than just banning the internet.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'inappropriate videos' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'content', 'inappropriate', 'contact', 'cyberbullying', 'mental health', 'parental controls', 'banning'. >Band 5: Specific terms. Not Band 7: Lacks 'exposure', 'predator', 'monitor'.",
    grammar_reason="[GRA6] Comparison: 'Education is better than...'. Modals: 'Must be careful'. >Band 5: Good grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Generated {len(samples)} samples in {OUTPUT_FILE}")
