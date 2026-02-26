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

# --- BATCH 06 PART 1: SAMPLES 451-475 (25 Total) ---
# Combo: V7/G7 (Good Vocab, Good Grammar)

# Sample 451: V7/G7 - Topic: Environment (Sustainability)
samples.append(create_sample(
    index=451,
    vocab_band=7,
    grammar_band=7,
    question="How can individuals contribute to sustainability?",
    transcript="Individuals play a pivotal role. Adopting a minimalist lifestyle is one way. By reducing consumption, we generate less waste. Another method is supporting eco-friendly businesses. When we buy organic or locally sourced products, we vote for a greener economy. Furthermore, energy conservation at home, such as using LED bulbs, makes a difference. It is about making conscious, responsible choices every day.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'pivotal role', 'minimalist lifestyle', 'consumption', 'eco-friendly', 'locally sourced', 'conservation', 'conscious'. >Band 6: Shows precision and style. Not Band 8: Lacks full fluency and flexibility.",
    grammar_reason="[GRA7] Uses gerunds as subjects: 'Adopting...', 'supporting...'. Relative clause implied. >Band 6: Frequent error-free sentences. Not Band 8: Structure is slightly repetitive.",
    idiom_present=False,
    risk_level="low"
))

# Sample 452: V7/G7 - Topic: Technology (AI)
samples.append(create_sample(
    index=452,
    vocab_band=7,
    grammar_band=7,
    question="Will AI replace human creativity?",
    transcript="It is unlikely to replace it entirely. AI can mimic artistic styles and generate content based on patterns. However, it lacks the human experience and emotional depth that drive true creativity. Art is often a reflection of suffering, joy, or love, which machines cannot feel. While AI can be a powerful tool for artists, the spark of originality remains uniquely human.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'unlikely', 'mimic', 'generate', 'patterns', 'emotional depth', 'reflection', 'spark of originality'. >Band 6: sophisticated vocabulary. Not Band 8: Some collocations are standard.",
    grammar_reason="[GRA7] Contrast: 'However', 'While AI can be...'. Relative clause: 'that drive true creativity'. >Band 6: Good control of complex structures. Not Band 8: Could use more inversion or emphasis.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 453: V7/G7 - Topic: Education (University)
samples.append(create_sample(
    index=453,
    vocab_band=7,
    grammar_band=7,
    question="Is online education as effective as traditional learning?",
    transcript="It can be, but it depends on the student. Online platforms offer flexibility and a vast array of resources. For self-motivated learners, this is ideal. However, traditional classrooms provide face-to-face interaction, which fosters soft skills like teamwork and communication. Also, the immediate feedback from a teacher is invaluable. So, while online learning is convenient, it might lack the holistic development of a campus experience.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'flexibility', 'vast array', 'self-motivated', 'ideal', 'fosters', 'soft skills', 'invaluable', 'holistic development'. >Band 6: Strong lexical resource. Not Band 8: Slightly formal tone.",
    grammar_reason="[GRA7] Contrast: 'However', 'So, while...'. Relative clause: 'which fosters...'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 454: V7/G7 - Topic: Society (Aging)
samples.append(create_sample(
    index=454,
    vocab_band=7,
    grammar_band=7,
    question="What are the benefits of an aging population?",
    transcript="Often we focus on the negatives, but there are positives too. Older people possess a wealth of experience and wisdom. They can mentor younger generations in the workplace. Moreover, retirees often contribute significantly to the voluntary sector. They have time to help charities and community projects. They also play a crucial role in childcare, looking after grandchildren, which allows parents to work.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'possess', 'wealth of experience', 'wisdom', 'mentor', 'retirees', 'significantly', 'voluntary sector', 'crucial role'. >Band 6: Good collocation. Not Band 8: Lacks idiomatic expressions.",
    grammar_reason="[GRA7] Contrast: 'but there are positives'. Relative clause: 'which allows parents'. >Band 6: Frequent error-free sentences. Not Band 8: Structure is functional.",
    idiom_present=False,
    risk_level="low"
))

# Sample 455: V7/G7 - Topic: Work (Remote)
samples.append(create_sample(
    index=455,
    vocab_band=7,
    grammar_band=7,
    question="Does remote work improve work-life balance?",
    transcript="For many, it certainly does. Eliminating the daily commute saves time and reduces stress. Employees can structure their day to fit in personal commitments, like exercise or family time. However, it can also blur the lines between professional and private life. Without a physical office, some people find it hard to switch off. Discipline is required to maintain a healthy boundary.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'eliminating', 'commute', 'structure', 'commitments', 'blur the lines', 'switch off', 'discipline', 'boundary'. >Band 6: Precise vocabulary. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA7] Reason: 'Because...'. Contrast: 'However'. >Band 6: Accurate complex sentences. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 456: V7/G7 - Topic: Culture (Globalization)
samples.append(create_sample(
    index=456,
    vocab_band=7,
    grammar_band=7,
    question="Is globalization a threat to local cultures?",
    transcript="There is a valid concern that it leads to cultural homogenization. We see the same brands and trends everywhere. This can dilute local traditions. However, globalization also allows cultures to showcase their uniqueness to a global audience. For example, local food or music can gain international popularity. So, it can actually preserve culture by giving it value and economic viability.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'valid concern', 'homogenization', 'dilute', 'showcase', 'uniqueness', 'international popularity', 'preserve', 'viability'. >Band 6: Sophisticated terms. Not Band 8: Slightly academic.",
    grammar_reason="[GRA7] Contrast: 'However'. Reason: 'by giving it value'. >Band 6: Good control. Not Band 8: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 457: V7/G7 - Topic: Transport (Cities)
samples.append(create_sample(
    index=457,
    vocab_band=7,
    grammar_band=7,
    question="How can we encourage people to use public transport?",
    transcript="Efficiency and affordability are key. If trains and buses are reliable and frequent, people will choose them over cars. Governments should subsidize fares to make them cheaper than driving. Additionally, improving the comfort and safety of the vehicles is important. If the experience is pleasant, commuters will switch. Integrating different modes of transport into one seamless system would also help.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'efficiency', 'affordability', 'subsidize', 'fares', 'commuters', 'integrating', 'modes', 'seamless system'. >Band 6: Strong vocabulary. Not Band 8: Lacks idiomatic usage.",
    grammar_reason="[GRA7] Conditionals: 'If trains are reliable...', 'If the experience is pleasant...'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 458: V7/G7 - Topic: Health (Exercise)
samples.append(create_sample(
    index=458,
    vocab_band=7,
    grammar_band=7,
    question="Why is a sedentary lifestyle dangerous?",
    transcript="It significantly increases the risk of chronic diseases. Sitting for long periods slows down metabolism and affects blood circulation. This can lead to obesity, heart disease, and diabetes. Furthermore, a lack of physical activity impacts mental health. Exercise releases endorphins, so without it, people are more prone to depression. An active lifestyle is fundamental for longevity.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'significantly', 'chronic diseases', 'metabolism', 'circulation', 'obesity', 'diabetes', 'prone to', 'longevity'. >Band 6: Medical/formal terms. Not Band 8: Slightly robotic.",
    grammar_reason="[GRA7] Reason: 'so without it...'. Relative clause implied. >Band 6: Frequent error-free sentences. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="low"
))

# Sample 459: V7/G7 - Topic: Society (Consumerism)
samples.append(create_sample(
    index=459,
    vocab_band=7,
    grammar_band=7,
    question="What drives consumerism?",
    transcript="Marketing is a powerful driver. Advertisements create artificial needs, making us feel that we must buy the latest product to be happy or successful. Social pressure also plays a part. We compare ourselves to others and want to display status through material possessions. This culture of constant consumption is fueled by planned obsolescence, where products are designed to break quickly.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'driver', 'artificial needs', 'status', 'material possessions', 'constant consumption', 'fueled by', 'planned obsolescence'. >Band 6: Advanced vocabulary. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA7] Relative clause: 'where products are designed'. Reason: 'making us feel'. >Band 6: Good control. Not Band 8: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 460: V7/G7 - Topic: Technology (Communication)
samples.append(create_sample(
    index=460,
    vocab_band=7,
    grammar_band=7,
    question="Is face-to-face communication still important?",
    transcript="Absolutely. Non-verbal cues like body language and tone of voice convey meaning that text cannot. These subtleties prevent misunderstandings. Face-to-face interaction builds trust and empathy more effectively than digital communication. While technology is convenient for quick exchanges, deep relationships require physical presence. It is the foundation of human connection.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'non-verbal cues', 'convey', 'subtleties', 'misunderstandings', 'empathy', 'effectively', 'convenient', 'foundation'. >Band 6: Precise terms. Not Band 8: Lacks idiomatic expressions.",
    grammar_reason="[GRA7] Contrast: 'While technology is convenient'. Comparative: 'more effectively than'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 461: V7/G7 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=461,
    vocab_band=7,
    grammar_band=7,
    question="How does deforestation affect the planet?",
    transcript="It has dire consequences. Trees act as carbon sinks, absorbing CO2. When they are cut down, this carbon is released, accelerating global warming. Deforestation also destroys habitats, leading to a loss of biodiversity. Many species are pushed to the brink of extinction. Furthermore, it disrupts the water cycle, which can cause droughts and soil erosion.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'dire consequences', 'carbon sinks', 'absorbing', 'accelerating', 'biodiversity', 'brink of extinction', 'disrupts', 'erosion'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA7] Time clause: 'When they are cut down'. Relative clause: 'which can cause'. >Band 6: Frequent error-free sentences. Not Band 8: Simple sentence links.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 462: V7/G7 - Topic: Education (Arts)
samples.append(create_sample(
    index=462,
    vocab_band=7,
    grammar_band=7,
    question="Should arts be part of the school curriculum?",
    transcript="Yes, they are integral to a well-rounded education. Arts foster creativity and critical thinking, skills that are transferable to other subjects. They also provide an emotional outlet for students, helping to reduce stress. By neglecting the arts, schools risk producing students who lack imagination and cultural awareness. Education should nurture the whole child, not just the academic side.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'integral', 'well-rounded', 'foster', 'transferable', 'emotional outlet', 'neglecting', 'imagination', 'nurture'. >Band 6: Good range. Not Band 8: Lacks idiomatic flow.",
    grammar_reason="[GRA7] Relative clause: 'skills that are transferable'. Gerund: 'By neglecting...'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 463: V7/G7 - Topic: Work (Job Hopping)
samples.append(create_sample(
    index=463,
    vocab_band=7,
    grammar_band=7,
    question="Why do people change jobs frequently nowadays?",
    transcript="The concept of a job for life is outdated. People seek career progression and new challenges. Staying in one role can feel stagnant. Changing jobs often leads to a higher salary and a broader skillset. Also, the job market is volatile. Companies downsize, forcing people to move. Loyalty is less valued than adaptability in the modern economy.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'concept', 'outdated', 'progression', 'stagnant', 'skillset', 'volatile', 'downsize', 'loyalty', 'adaptability'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'tenure', 'dynamic', 'ladder'.",
    grammar_reason="[GRA7] Reason: 'Staying in one role can feel...'. Comparison: 'less valued than'. >Band 6: Good control. Not Band 8: Sentences are somewhat short.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 464: V7/G7 - Topic: Society (Crime)
samples.append(create_sample(
    index=464,
    vocab_band=7,
    grammar_band=7,
    question="Can technology help reduce crime?",
    transcript="It is a powerful tool for law enforcement. Surveillance cameras act as a deterrent and provide evidence. Facial recognition can identify suspects quickly. Moreover, data analysis helps police predict crime hotspots. However, we must balance security with privacy. Excessive surveillance can lead to a police state. Technology should protect citizens, not control them.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'law enforcement', 'surveillance', 'deterrent', 'facial recognition', 'suspects', 'hotspots', 'excessive', 'police state'. >Band 6: Advanced vocabulary. Not Band 8: Slightly robotic.",
    grammar_reason="[GRA7] Contrast: 'However'. Modal: 'Should protect'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 465: V7/G7 - Topic: Culture (Food)
samples.append(create_sample(
    index=465,
    vocab_band=7,
    grammar_band=7,
    question="Why is traditional food losing popularity?",
    transcript="Convenience is the main factor. Traditional dishes often require long preparation times and fresh ingredients. In our fast-paced lives, people prefer quick options like fast food or ready meals. Also, international cuisine is trendy. Young people might find traditional food boring or old-fashioned. However, there is a resurgence of interest in slow food, as people value health and heritage.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'convenience', 'preparation times', 'fast-paced', 'cuisine', 'trendy', 'old-fashioned', 'resurgence', 'heritage'. >Band 6: Good topic words. Not Band 8: Lacks 'culinary', 'authentic', 'preservation'.",
    grammar_reason="[GRA7] Contrast: 'However'. Reason: 'as people value...'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 466: V7/G7 - Topic: Transport (Cars)
samples.append(create_sample(
    index=466,
    vocab_band=7,
    grammar_band=7,
    question="What are the disadvantages of owning a car?",
    transcript="The costs are significant. Beyond the purchase price, you have insurance, fuel, and maintenance. Cars also depreciate in value quickly. Finding parking in cities can be a nightmare and very expensive. Furthermore, owning a car contributes to environmental damage. For city dwellers, the stress of driving in traffic often outweighs the convenience.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'significant', 'purchase price', 'maintenance', 'depreciate', 'nightmare', 'contributes', 'dwellers', 'outweighs'. >Band 6: Precise terms. Not Band 8: Lacks idiomatic flow.",
    grammar_reason="[GRA7] Reason: 'For city dwellers...'. Sequencing: 'Furthermore'. >Band 6: Accurate complex sentences. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 467: V7/G7 - Topic: Health (Mental)
samples.append(create_sample(
    index=467,
    vocab_band=7,
    grammar_band=7,
    question="How can we improve mental health in society?",
    transcript="Destigmatizing mental illness is the first step. People should feel safe seeking help without fear of judgment. Employers need to prioritize worker well-being, perhaps by offering counseling or mental health days. Education is also key; teaching coping mechanisms in schools can build resilience. A supportive community where people look out for each other is essential for collective mental health.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'destigmatizing', 'seeking help', 'judgment', 'prioritize', 'well-being', 'coping mechanisms', 'resilience', 'collective'. >Band 6: Advanced vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA7] Gerund: 'Destigmatizing...'. Relative clause: 'where people look out'. >Band 6: Good control. Not Band 8: Sentences are competent but standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 468: V7/G7 - Topic: Technology (Games)
samples.append(create_sample(
    index=468,
    vocab_band=7,
    grammar_band=7,
    question="Are video games art?",
    transcript="I firmly believe they are. Modern games feature stunning visual design and complex narratives that rival cinema. Composers create original scores that evoke deep emotion. Players are not just spectators; they interact with the world, making the experience unique. While not all games aim for artistic value, many achieve a level of creativity that deserves recognition.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'firmly', 'visual design', 'narratives', 'rival', 'scores', 'evoke', 'spectators', 'interact', 'recognition'. >Band 6: Sophisticated terms. Not Band 8: Lacks 'masterpiece', 'aesthetic', 'medium'.",
    grammar_reason="[GRA7] Relative clause: 'that rival cinema'. Contrast: 'While not all games...'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 469: V7/G7 - Topic: Society (Housing)
samples.append(create_sample(
    index=469,
    vocab_band=7,
    grammar_band=7,
    question="Is it better to rent or buy a home?",
    transcript="It depends on your circumstances. Buying offers stability and is a long-term investment. You have the freedom to renovate. However, it requires a large deposit and ties you to one location. Renting offers flexibility. You can move easily for work. Maintenance is the landlord's responsibility. In an uncertain economy, renting might be the safer option.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'circumstances', 'stability', 'investment', 'renovate', 'deposit', 'ties you to', 'flexibility', 'landlord', 'uncertain'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'equity', 'mortgage', 'asset'.",
    grammar_reason="[GRA7] Contrast: 'However'. Reason: 'It depends on...'. >Band 6: Frequent error-free sentences. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="low"
))

# Sample 470: V7/G7 - Topic: Environment (Global Warming)
samples.append(create_sample(
    index=470,
    vocab_band=7,
    grammar_band=7,
    question="What is the role of international agreements in climate change?",
    transcript="They are critical for coordinating a global response. Climate change is a borderless issue. Agreements like the Paris Accord set targets for emission reductions that countries must aim for. They hold nations accountable. Without such frameworks, countries might prioritize short-term economic gain over long-term sustainability. International cooperation is the only way to tackle a planetary crisis.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'critical', 'coordinating', 'borderless', 'accord', 'emission reductions', 'accountable', 'frameworks', 'prioritize', 'sustainability', 'planetary'. >Band 6: Advanced vocabulary. Not Band 8: Slightly robotic.",
    grammar_reason="[GRA7] Relative clause: 'that countries must aim for'. Conditionals: 'Without such frameworks...'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 471: V7/G7 - Topic: Education (University)
samples.append(create_sample(
    index=471,
    vocab_band=7,
    grammar_band=7,
    question="Why do some students drop out of university?",
    transcript="Financial pressure is a common reason. Tuition fees and living costs can be overwhelming. Some students find the academic workload too demanding and burn out. Others might realize they chose the wrong course and lack passion for the subject. Personal issues, like family problems or mental health struggles, also play a role. It is rarely a simple decision.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'financial pressure', 'overwhelming', 'academic workload', 'demanding', 'burn out', 'lack passion', 'struggles'. >Band 6: Good range. Not Band 8: Lacks 'disillusioned', 'compatibility', 'support system'.",
    grammar_reason="[GRA7] Reason: 'Others might realize...'. List structure. >Band 6: Frequent error-free sentences. Not Band 8: Structure is standard.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 472: V7/G7 - Topic: Work (Leadership)
samples.append(create_sample(
    index=472,
    vocab_band=7,
    grammar_band=7,
    question="What challenges do leaders face today?",
    transcript="They must navigate a rapidly changing world. Technology evolves quickly, requiring constant adaptation. Managing a diverse and often remote workforce is also challenging. Leaders need to foster inclusion and maintain morale from a distance. Additionally, there is pressure to be ethical and sustainable. Balancing profit with social responsibility is a complex task for modern executives.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'navigate', 'evolves', 'adaptation', 'diverse', 'foster', 'inclusion', 'morale', 'sustainable', 'responsibility', 'executives'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'visionary', 'scrutiny', 'stakeholders'.",
    grammar_reason="[GRA7] Gerund: 'Managing a diverse...'. Reason: 'requiring constant adaptation'. >Band 6: Accurate complex sentences. Not Band 8: Limited flexibility.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 473: V7/G7 - Topic: Culture (Tradition)
samples.append(create_sample(
    index=473,
    vocab_band=7,
    grammar_band=7,
    question="Why do some traditions disappear?",
    transcript="Ideally, traditions evolve, but some fade away due to modernization. As societies become more urban and secular, old rural customs lose relevance. Young people might view them as obsolete or restrictive. Globalization also introduces new cultural norms that replace local ones. If a tradition does not adapt to contemporary values, it is likely to be forgotten.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'evolve', 'fade away', 'modernization', 'secular', 'relevance', 'obsolete', 'restrictive', 'norms', 'contemporary'. >Band 6: Sophisticated vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA7] Time clause: 'As societies become...'. Conditionals: 'If a tradition does not...'. >Band 6: Good control. Not Band 8: Sentences are competent but standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 474: V7/G7 - Topic: Technology (Space)
samples.append(create_sample(
    index=474,
    vocab_band=7,
    grammar_band=7,
    question="What is the future of space travel?",
    transcript="I predict that commercial space travel will become a reality. Private companies are already investing heavily in this sector. We might see hotels in orbit or colonies on Mars within our lifetime. This could solve overpopulation and resource depletion on Earth. However, it raises legal and ethical questions. Space should not become a battleground for nations or corporations.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'predict', 'commercial', 'investing heavily', 'sector', 'orbit', 'colonies', 'overpopulation', 'depletion', 'battleground'. >Band 6: Advanced vocabulary. Not Band 8: Lacks 'frontier', 'exploration', 'sovereignty'.",
    grammar_reason="[GRA7] Future forms: 'will become', 'might see'. Contrast: 'However'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 475: V7/G7 - Topic: Transport (Safety)
samples.append(create_sample(
    index=475,
    vocab_band=7,
    grammar_band=7,
    question="How can we reduce traffic accidents?",
    transcript="Stricter enforcement of traffic laws is essential. Speed cameras and heavy fines deter reckless driving. Improving road infrastructure, like better lighting and signage, also helps. Education campaigns can change driver behavior, especially regarding alcohol and phone use. Furthermore, vehicle technology, such as automatic braking, can prevent collisions. A combination of law, engineering, and education is required.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'enforcement', 'deter', 'reckless', 'infrastructure', 'signage', 'campaigns', 'automatic braking', 'collisions'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'negligence', 'fatalities', 'initiative'.",
    grammar_reason="[GRA7] Gerund: 'Improving road infrastructure'. Reason: 'can prevent collisions'. >Band 6: Frequent error-free sentences. Not Band 8: Structure is standard.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Generated {len(samples)} samples in {OUTPUT_FILE}")
