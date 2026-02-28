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

# --- BATCH 05 PART 3: SAMPLES 401-425 (25 Total) ---
# Combo: V7/G6 (Good Vocab, Competent Grammar)

# Sample 401: V7/G6 - Topic: Environment (Sustainability)
samples.append(create_sample(
    index=401,
    vocab_band=7,
    grammar_band=6,
    question="What is sustainable living?",
    transcript="It means living in a way that preserves the environment for future generations. We should minimize our carbon footprint. Using renewable energy sources like solar power is crucial. Also, reducing waste by recycling and composting. It is about making conscious choices. However, some people finds it difficult. It require effort and sometimes costs more money. But it is vital for our planet's survival.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'people finds' -> 'people find'",
        "verb agreement: 'It require' -> 'It requires'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common lexical items: 'preserves', 'future generations', 'minimize', 'carbon footprint', 'renewable energy', 'composting', 'conscious choices', 'vital'. >Band 6: Shows style awareness and collocation. Not Band 8: Lacks full precision and sophistication.",
    grammar_reason="[GRA6] Mix of simple and complex sentences. 'living in a way that...' (relative clause). 'However, some people finds...' (error). >Band 5: Good range of structures. Not Band 7: Frequent minor errors like subject-verb agreement.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 402: V7/G6 - Topic: Technology (AI)
samples.append(create_sample(
    index=402,
    vocab_band=7,
    grammar_band=6,
    question="Is artificial intelligence a threat to humanity?",
    transcript="It is a double-edged sword. On one hand, it offers immense benefits, like in healthcare diagnostics. It can process data faster than humans. On the other hand, there are ethical concerns. Automation might lead to mass unemployment. Also, if AI becomes autonomous, we might lose control. We need strict regulations to mitigate these risks. If we are not careful, the consequences could be disastrous.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'double-edged sword' (idiom used correctly)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'immense benefits', 'diagnostics', 'process data', 'ethical concerns', 'automation', 'unemployment', 'autonomous', 'mitigate', 'disastrous'. Idiom: 'double-edged sword'. >Band 6: Flexible use of vocabulary. Not Band 8: Some phrasing is slightly standard.",
    grammar_reason="[GRA6] Conditionals: 'If AI becomes...', 'If we are not careful...'. >Band 5: Meaning is clear with complex forms. Not Band 7: Some sentences are short and simple.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 403: V7/G6 - Topic: Education (University)
samples.append(create_sample(
    index=403,
    vocab_band=7,
    grammar_band=6,
    question="Is a university degree worth the debt?",
    transcript="It depends on the field of study. For specialized professions like medicine or law, it is indispensable. The potential earnings justify the investment. However, for other subjects, it might not be financially viable. Vocational training can offer a better return on investment. Students should weigh the pros and cons carefully. Graduating with a heavy burden of debt can hinder their future financial stability.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'weigh the pros and cons' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'specialized professions', 'indispensable', 'potential earnings', 'financially viable', 'vocational training', 'return on investment', 'burden', 'hinder'. Idiom: 'weigh the pros and cons'. >Band 6: Precise vocabulary. Not Band 8: Slightly academic tone.",
    grammar_reason="[GRA6] Contrast: 'However'. Reason: 'For specialized professions...'. >Band 5: Accurate grammar. Not Band 7: Limited variety in sentence structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 404: V7/G6 - Topic: Society (Inequality)
samples.append(create_sample(
    index=404,
    vocab_band=7,
    grammar_band=6,
    question="Why is income inequality a problem?",
    transcript="It creates social unrest. When the gap between the wealthy and the impoverished widens, it leads to resentment. The rich have access to superior healthcare and education, while the poor struggle to make ends meet. This disparity can stifle economic growth. A fair society should provide equal opportunities for everyone. Reducing inequality is essential for social cohesion and stability.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'make ends meet' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'social unrest', 'impoverished', 'resentment', 'superior', 'disparity', 'stifle', 'economic growth', 'social cohesion'. Idiom: 'make ends meet'. >Band 6: flexible use. Not Band 8: Some collocations are predictable.",
    grammar_reason="[GRA6] Contrast: 'while the poor...'. Relative clause implied. >Band 5: Good control. Not Band 7: Lacks complex sentence chains.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 405: V7/G6 - Topic: Health (Lifestyle)
samples.append(create_sample(
    index=405,
    vocab_band=7,
    grammar_band=6,
    question="How does modern lifestyle affect health?",
    transcript="It has a detrimental effect. Our sedentary lifestyle is a major contributor to health issues. We spend hours sitting in front of screens, which leads to obesity and back problems. Processed food is convenient but lacks nutritional value. Stress is also prevalent in our fast-paced society. We need to prioritize physical activity and mindful eating to combat these negative trends.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'fast-paced society' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'detrimental', 'sedentary lifestyle', 'contributor', 'obesity', 'nutritional value', 'prevalent', 'prioritize', 'mindful', 'combat'. >Band 6: Strong vocabulary. Not Band 8: Lacks full fluency.",
    grammar_reason="[GRA6] Relative clause: 'which leads to...'. Reason: 'because it is convenient' (implied). >Band 5: Accurate grammar. Not Band 7: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 406: V7/G6 - Topic: Transport (Public)
samples.append(create_sample(
    index=406,
    vocab_band=7,
    grammar_band=6,
    question="What are the benefits of an efficient public transport system?",
    transcript="It alleviates traffic congestion significantly. If people rely on trains and buses, there are fewer private vehicles on the road. This reduces carbon emissions and improves air quality. Moreover, it is cost-effective for commuters. It enhances mobility for those who cannot drive. An integrated transport network is the backbone of a modern, sustainable city.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'backbone of a city' (metaphor)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'alleviates', 'congestion', 'carbon emissions', 'cost-effective', 'commuters', 'enhances', 'mobility', 'integrated', 'sustainable'. Metaphor: 'backbone'. >Band 6: Precise and varied. Not Band 8: Slightly formal.",
    grammar_reason="[GRA6] Conditionals: 'If people rely...'. Reason: 'because there are fewer' (implied). >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 407: V7/G6 - Topic: Culture (Globalization)
samples.append(create_sample(
    index=407,
    vocab_band=7,
    grammar_band=6,
    question="How does globalization affect cultural identity?",
    transcript="It can lead to cultural homogenization. Local traditions might be overshadowed by dominant Western culture. For instance, fast food chains are ubiquitous, replacing local cuisine. However, it also facilitates cultural exchange. We become more cosmopolitan and open-minded. It is a balancing act. We must embrace global connectivity while preserving our unique heritage and customs.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'balancing act' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'homogenization', 'overshadowed', 'dominant', 'ubiquitous', 'cuisine', 'facilitates', 'cosmopolitan', 'connectivity', 'unique heritage'. Idiom: 'balancing act'. >Band 6: Sophisticated vocabulary. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA6] Contrast: 'However'. Passive: 'might be overshadowed'. >Band 5: Good control. Not Band 7: Sentences are of medium length.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 408: V7/G6 - Topic: Work (Remote)
samples.append(create_sample(
    index=408,
    vocab_band=7,
    grammar_band=6,
    question="What are the pros and cons of remote work?",
    transcript="The flexibility is a major advantage. Employees can manage their work-life balance better. It eliminates the daily commute, which saves time and reduces stress. However, isolation can be a drawback. Without face-to-face interaction, team cohesion might suffer. Also, the boundary between work and personal life can become blurred. It requires self-discipline to stay productive.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'blurred' (correct context)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'flexibility', 'work-life balance', 'eliminates', 'commute', 'drawback', 'interaction', 'cohesion', 'boundary', 'blurred', 'self-discipline'. >Band 6: Precise terms. Not Band 8: Lacks idiomatic expressions.",
    grammar_reason="[GRA6] Relative clause: 'which saves time'. Contrast: 'However'. >Band 5: Accurate grammar. Not Band 7: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 409: V7/G6 - Topic: Society (Crime)
samples.append(create_sample(
    index=409,
    vocab_band=7,
    grammar_band=6,
    question="Does poverty cause crime?",
    transcript="There is a strong correlation. When people are desperate, they might resort to theft to survive. Lack of education and employment opportunities traps people in a cycle of poverty. However, greed is also a factor. White-collar crime is committed by wealthy individuals. So, poverty is a significant driver, but not the only cause. Social inequality plays a major role.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'white-collar crime' (specific term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'correlation', 'desperate', 'resort to', 'traps', 'cycle of poverty', 'greed', 'white-collar crime', 'significant driver', 'inequality'. >Band 6: Strong vocabulary. Not Band 8: Slightly academic.",
    grammar_reason="[GRA6] Time clause: 'When people are desperate'. Contrast: 'However'. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 410: V7/G6 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=410,
    vocab_band=7,
    grammar_band=6,
    question="Why is it important to protect endangered species?",
    transcript="Every species plays a role in maintaining the ecological balance. If one goes extinct, it can have a domino effect on the food chain. Biodiversity is essential for a healthy planet. Furthermore, animals have an intrinsic value. We have a moral obligation to protect them from human-induced threats like habitat destruction and poaching. Conservation efforts are vital.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'domino effect' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'ecological balance', 'extinct', 'domino effect', 'food chain', 'biodiversity', 'intrinsic value', 'moral obligation', 'human-induced', 'poaching', 'conservation'. >Band 6: Very good vocabulary. Not Band 8: Lacks fluency.",
    grammar_reason="[GRA6] Conditionals: 'If one goes extinct...'. Reason: 'essential for a healthy planet'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 411: V7/G6 - Topic: Technology (Space)
samples.append(create_sample(
    index=411,
    vocab_band=7,
    grammar_band=6,
    question="Is space exploration worth the cost?",
    transcript="It is a contentious issue. The financial investment is astronomical. Critics argue that we should prioritize solving problems on Earth, like hunger and disease. However, space research drives technological innovation. Many everyday gadgets originated from space programs. Moreover, exploring the cosmos satisfies human curiosity. It inspires us to push boundaries. So, I believe it has long-term value.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'push boundaries' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'contentious', 'astronomical', 'prioritize', 'innovation', 'gadgets', 'originated', 'cosmos', 'curiosity', 'push boundaries'. >Band 6: Advanced vocabulary. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA6] Contrast: 'However'. Reason: 'It inspires us'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 412: V7/G6 - Topic: Education (Arts)
samples.append(create_sample(
    index=412,
    vocab_band=7,
    grammar_band=6,
    question="Why are arts subjects often undervalued?",
    transcript="Society tends to prioritize STEM subjects because they are seen as more practical and lucrative. Arts are often viewed as a hobby rather than a career. This perception is misguided. The arts foster creativity and critical thinking, which are transferable skills. They enrich our culture and emotional intelligence. Undervaluing the arts limits our potential as human beings.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'transferable skills' (specific term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'undervalued', 'prioritize', 'STEM', 'lucrative', 'perception', 'misguided', 'foster', 'critical thinking', 'transferable skills', 'enrich'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA6] Reason: 'because they are seen...'. Relative clause: 'which are transferable skills'. >Band 5: Accurate grammar. Not Band 7: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 413: V7/G6 - Topic: Work (Job Hopping)
samples.append(create_sample(
    index=413,
    vocab_band=7,
    grammar_band=6,
    question="Is job hopping good for a career?",
    transcript="It can be beneficial. Changing jobs allows you to acquire diverse skills and experiences. It expands your professional network. Also, it is often the fastest way to increase your salary. However, frequent changes might look bad on a resume. Employers might question your loyalty and commitment. It is a balancing act between growth and stability.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'balancing act' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'beneficial', 'acquire', 'diverse', 'professional network', 'resume', 'loyalty', 'commitment', 'stability'. Idiom: 'balancing act'. >Band 6: Precise terms. Not Band 8: Lacks idiomatic flair.",
    grammar_reason="[GRA6] Contrast: 'However'. Reason: 'It expands...'. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 414: V7/G6 - Topic: Society (Celebrity)
samples.append(create_sample(
    index=414,
    vocab_band=7,
    grammar_band=6,
    question="Why does the media focus on celebrities?",
    transcript="Because it sells. People have an insatiable appetite for gossip and glamour. Celebrities represent a fantasy lifestyle that ordinary people aspire to. The media exploits this fascination to generate revenue. However, this obsession can be unhealthy. It sets unrealistic standards of beauty and success. We should focus more on real heroes, like doctors and teachers.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'insatiable appetite' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'insatiable appetite', 'gossip', 'glamour', 'fantasy', 'aspire to', 'exploits', 'fascination', 'revenue', 'obsession', 'unrealistic standards'. >Band 6: Sophisticated vocabulary. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA6] Reason: 'Because it sells'. Relative clause: 'that ordinary people aspire to'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 415: V7/G6 - Topic: Environment (Plastic)
samples.append(create_sample(
    index=415,
    vocab_band=7,
    grammar_band=6,
    question="Is banning plastic bags effective?",
    transcript="It is a step in the right direction. It raises awareness about the issue of plastic waste. It forces consumers to change their habits and use reusable bags. However, it is not a silver bullet. Plastic is ubiquitous in packaging. We need comprehensive regulations to tackle the root cause. Reducing production is more important than just recycling.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'silver bullet' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'awareness', 'consumers', 'habits', 'reusable', 'ubiquitous', 'packaging', 'comprehensive', 'regulations', 'tackle', 'root cause'. Idiom: 'silver bullet'. >Band 6: Strong vocabulary. Not Band 8: Slightly robotic.",
    grammar_reason="[GRA6] Contrast: 'However'. Comparison: 'more important than'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 416: V7/G6 - Topic: Technology (Internet)
samples.append(create_sample(
    index=416,
    vocab_band=7,
    grammar_band=6,
    question="How has the internet changed shopping?",
    transcript="It has revolutionized the retail industry. E-commerce offers unparalleled convenience. We can browse endless products from the comfort of our homes. Price comparison is effortless. However, it has negatively impacted brick-and-mortar stores. Many high street shops are closing down. Also, impulsive buying has increased. It is too easy to spend money with a click.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'brick-and-mortar' (specific term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'revolutionized', 'retail industry', 'e-commerce', 'unparalleled', 'browse', 'effortless', 'negatively impacted', 'brick-and-mortar', 'impulsive buying'. >Band 6: Advanced vocabulary. Not Band 8: Lacks idiomatic flow.",
    grammar_reason="[GRA6] Contrast: 'However'. Present perfect: 'has revolutionized'. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 417: V7/G6 - Topic: Culture (Travel)
samples.append(create_sample(
    index=417,
    vocab_band=7,
    grammar_band=6,
    question="Does tourism help cultural understanding?",
    transcript="Ideally, yes. It fosters cross-cultural exchange. When we interact with locals, we gain insight into their way of life. It breaks down stereotypes and prejudice. However, mass tourism can be superficial. Tourists often stay in a bubble. They visit landmarks but don't engage with the culture. Authentic experiences are rare. We need to be responsible travelers.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'stay in a bubble' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'fosters', 'cross-cultural', 'interact', 'insight', 'stereotypes', 'prejudice', 'superficial', 'landmarks', 'engage', 'authentic'. Idiom: 'stay in a bubble'. >Band 6: Very good vocabulary. Not Band 8: Lacks fluency.",
    grammar_reason="[GRA6] Time clause: 'When we interact'. Contrast: 'However'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 418: V7/G6 - Topic: Health (Exercise)
samples.append(create_sample(
    index=418,
    vocab_band=7,
    grammar_band=6,
    question="What are the benefits of outdoor activities?",
    transcript="They improve both physical and mental well-being. Fresh air and sunlight boost our mood and energy levels. Being in nature reduces cortisol, the stress hormone. It helps us disconnect from technology. Hiking or cycling are excellent cardiovascular exercises. Unlike the gym, the outdoors offers variety and scenery. It is rejuvenating for the soul.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'boost our mood' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'well-being', 'boost', 'cortisol', 'stress hormone', 'disconnect', 'cardiovascular', 'variety', 'scenery', 'rejuvenating'. >Band 6: Strong vocabulary. Not Band 8: Slightly academic.",
    grammar_reason="[GRA6] Reason: 'It helps us...'. Contrast: 'Unlike the gym'. >Band 5: Accurate grammar. Not Band 7: Simple structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 419: V7/G6 - Topic: Society (Volunteer)
samples.append(create_sample(
    index=419,
    vocab_band=7,
    grammar_band=6,
    question="Why do people volunteer?",
    transcript="It gives them a sense of purpose. Helping others is intrinsically rewarding. It strengthens community bonds. Volunteers can also develop valuable skills, like leadership and teamwork. It is a good way to network. Some do it for altruistic reasons, while others want to boost their resume. Regardless of the motive, the contribution is positive.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'intrinsically rewarding' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'purpose', 'intrinsically', 'strengthens', 'bonds', 'valuable', 'network', 'altruistic', 'resume', 'motive', 'contribution'. >Band 6: Advanced vocabulary. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA6] Contrast: 'while others want...'. Reason: 'It gives them...'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 420: V7/G6 - Topic: Transport (Cars)
samples.append(create_sample(
    index=420,
    vocab_band=7,
    grammar_band=6,
    question="Will we ever stop using cars?",
    transcript="It is unlikely in the near future. Cars offer autonomy and convenience that public transport cannot match. However, the type of car will evolve. Electric and autonomous vehicles will dominate. Urban planning might prioritize pedestrians, making cars less necessary in city centers. But for rural areas, cars remain essential. We need a shift in mindset.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'shift in mindset' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'unlikely', 'autonomy', 'convenience', 'evolve', 'autonomous', 'dominate', 'urban planning', 'prioritize', 'pedestrians', 'rural', 'essential'. >Band 6: Sophisticated terms. Not Band 8: Lacks flexibility.",
    grammar_reason="[GRA6] Contrast: 'However', 'But'. Future tense: 'Will dominate'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 421: V7/G6 - Topic: Education (Science)
samples.append(create_sample(
    index=421,
    vocab_band=7,
    grammar_band=6,
    question="Why are fewer students choosing science subjects?",
    transcript="They are perceived as difficult and demanding. The curriculum is often rigid and theoretical. Students fail to see the relevance to their daily lives. Also, there is a lack of engaging teaching methods. We need to make science more hands-on and exciting. Showing the practical applications can spark interest. Inspiring mentors are also crucial.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'spark interest' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'perceived', 'demanding', 'curriculum', 'rigid', 'theoretical', 'relevance', 'engaging', 'hands-on', 'applications', 'spark', 'mentors'. >Band 6: Good range. Not Band 8: Slightly formal.",
    grammar_reason="[GRA6] Reason: 'They are perceived as...'. Passive: 'are perceived'. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 422: V7/G6 - Topic: Culture (Festivals)
samples.append(create_sample(
    index=422,
    vocab_band=7,
    grammar_band=6,
    question="How do festivals preserve culture?",
    transcript="They are a celebration of heritage. Rituals and customs are performed and passed down. It keeps history alive. Festivals strengthen communal identity. Young people learn about their roots. However, commercialization is a threat. If festivals become just about money, the meaning is lost. We must safeguard the authenticity of these events.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'safeguard the authenticity' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'celebration', 'heritage', 'rituals', 'customs', 'communal identity', 'roots', 'commercialization', 'threat', 'safeguard', 'authenticity'. >Band 6: Strong vocabulary. Not Band 8: Lacks idiomatic flow.",
    grammar_reason="[GRA6] Conditionals: 'If festivals become...'. Passive: 'are performed'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 423: V7/G6 - Topic: Work (Gender)
samples.append(create_sample(
    index=423,
    vocab_band=7,
    grammar_band=6,
    question="How can companies promote gender equality?",
    transcript="They should implement transparent hiring policies. Eliminate bias in recruitment. Also, equal pay for equal work is non-negotiable. Offering flexible working hours helps parents, especially mothers. Mentorship programs for women can boost their confidence and career progression. A diverse workforce leads to better innovation. It is a moral and business imperative.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'business imperative' (advanced term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'implement', 'transparent', 'bias', 'recruitment', 'non-negotiable', 'flexible', 'mentorship', 'progression', 'diverse', 'innovation', 'imperative'. >Band 6: Advanced vocabulary. Not Band 8: Slightly robotic.",
    grammar_reason="[GRA6] Modals: 'Should implement'. Reason: 'leads to better innovation'. >Band 5: Accurate grammar. Not Band 7: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 424: V7/G6 - Topic: Technology (Games)
samples.append(create_sample(
    index=424,
    vocab_band=7,
    grammar_band=6,
    question="Can video games be educational?",
    transcript="Certainly. Simulation games teach strategy and resource management. Puzzle games enhance problem-solving skills. Some games have historical settings, which spark interest in history. Multiplayer games foster teamwork and communication. However, content matters. Violent games have little educational value. We should choose games that stimulate the mind.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'stimulate the mind' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'simulation', 'strategy', 'resource management', 'enhance', 'settings', 'spark', 'foster', 'content', 'educational value', 'stimulate'. >Band 6: Good range. Not Band 8: Lacks natural phrasing.",
    grammar_reason="[GRA6] Relative clause: 'which spark interest'. Contrast: 'However'. >Band 5: Accurate grammar. Not Band 7: Simple sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 425: V7/G6 - Topic: Environment (Global Warming)
samples.append(create_sample(
    index=425,
    vocab_band=7,
    grammar_band=6,
    question="What is the impact of rising sea levels?",
    transcript="It is catastrophic for coastal communities. Flooding becomes frequent, destroying homes and infrastructure. Saltwater contamination affects agriculture and drinking water. Small island nations might disappear completely. This leads to climate refugees. People are forced to migrate. It is an existential threat. We must mitigate the effects by reducing emissions immediately.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'existential threat' (advanced term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'catastrophic', 'coastal', 'infrastructure', 'contamination', 'agriculture', 'refugees', 'migrate', 'existential threat', 'mitigate', 'emissions'. >Band 6: Sophisticated vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA6] Passive: 'are forced to migrate'. Reason: 'It is catastrophic'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
