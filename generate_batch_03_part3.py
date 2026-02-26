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

# --- BATCH 03 PART 3: SAMPLES 201-225 (25 Total) ---
# Combo: V6/G5 (Competent Vocab, Modest Grammar)

# Sample 201: V6/G5 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=201,
    vocab_band=6,
    grammar_band=5,
    question="Why is recycling becoming more important?",
    transcript="Well, the amount of waste is increasing significantly every year. People consume too much products. Plastic is a major issue because it does not decompose. It harm the marine life. If we recycle, we can reduce the pollution. But many people is lazy. They throw everything in one bin. Government need to enforce strict regulations.",
    response_type="extended",
    micro_flaws=[
        "singular/plural: 'too much products' -> 'too many products'",
        "verb agreement: 'It harm' -> 'It harms'",
        "verb agreement: 'many people is' -> 'many people are'",
        "verb construction: 'Government need' -> 'The government needs'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'significantly', 'consume', 'decompose', 'marine life', 'enforce', 'regulations'. >Band 5: Vocabulary is more precise and varied. Not Band 7: Some collocations are slightly unnatural.",
    grammar_reason="[GRA5] Attempts complex sentences: 'because it does not decompose', 'If we recycle...'. >Band 4: Uses subordinate clauses. Not Band 6: Frequent errors in subject-verb agreement and plurals.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 202: V6/G5 - Topic: Technology (Robots)
samples.append(create_sample(
    index=202,
    vocab_band=6,
    grammar_band=5,
    question="Will robots take our jobs?",
    transcript="It is highly possible. Robots are more efficient than human. They can perform repetitive tasks without getting tired. For example, manufacturing and assembly lines. However, jobs that require creativity and emotional intelligence is safe. Robots cannot replace human empathy. But we must adapt to this technological advancement. If not, unemployment rate will rise.",
    response_type="extended",
    micro_flaws=[
        "singular/plural: 'than human' -> 'than humans'",
        "verb agreement: 'jobs... is safe' -> 'jobs... are safe'",
        "missing article: 'unemployment rate' -> 'the unemployment rate'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'efficient', 'repetitive tasks', 'manufacturing', 'assembly lines', 'creativity', 'emotional intelligence', 'technological advancement'. >Band 5: Clear topic-specific vocabulary. Not Band 7: Lacks full flexibility.",
    grammar_reason="[GRA5] Uses complex structures: 'jobs that require...', 'If not...'. >Band 4: Attempts relative clauses. Not Band 6: Agreement errors in complex sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 203: V6/G5 - Topic: Education (University)
samples.append(create_sample(
    index=203,
    vocab_band=6,
    grammar_band=5,
    question="Is a university degree essential for success?",
    transcript="Not necessarily. In the past, a degree was a requirement for a stable career. But nowadays, skills and experience is more valuable. Many successful entrepreneurs does not have a degree. Vocational training is also a good option. It provides practical skills. However, for specialized fields like medicine, university is mandatory. It depend on the profession.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'skills... is' -> 'skills... are'",
        "verb agreement: 'entrepreneurs does not' -> 'entrepreneurs do not'",
        "verb agreement: 'It depend' -> 'It depends'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'requirement', 'stable career', 'entrepreneurs', 'vocational training', 'practical skills', 'specialized fields', 'mandatory'. >Band 5: Good range of vocabulary. Not Band 7: Occasional imprecision.",
    grammar_reason="[GRA5] Comparison: 'more valuable'. Contrast: 'But nowadays', 'However'. >Band 4: Uses cohesive devices. Not Band 6: Basic subject-verb agreement errors persist.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 204: V6/G5 - Topic: Society (Consumerism)
samples.append(create_sample(
    index=204,
    vocab_band=6,
    grammar_band=5,
    question="Why do people buy things they don't need?",
    transcript="Advertising play a big role. Companies use psychological tactics to persuade consumers. They create a desire for luxury goods. People want to display their social status. Buying latest gadgets make them feel superior. Also, retail therapy is common. People shop to relieve stress. But this habit lead to financial debt.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Advertising play' -> 'Advertising plays'",
        "missing article: 'latest gadgets' -> 'the latest gadgets'",
        "verb agreement: 'gadgets make' -> 'gadgets makes' (subject is Buying)",
        "verb agreement: 'habit lead' -> 'habit leads'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'psychological tactics', 'persuade', 'consumers', 'luxury goods', 'social status', 'retail therapy', 'financial debt'. >Band 5: Precise vocabulary. Not Band 7: Lacks idiomatic awareness.",
    grammar_reason="[GRA5] Reason: 'to persuade consumers'. Purpose: 'to relieve stress'. >Band 4: Complex ideas expressed. Not Band 6: Frequent verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 205: V6/G5 - Topic: Health (Diet)
samples.append(create_sample(
    index=205,
    vocab_band=6,
    grammar_band=5,
    question="How can we encourage healthy eating?",
    transcript="Education is crucial. Schools should teach nutrition and the benefits of a balanced diet. Children need to understand the consequences of junk food. Like obesity and diabetes. Also, healthy food is often expensive. Government should subsidize fresh produce. If vegetables is cheaper, people will buy them. We must discourage consumption of processed food.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'vegetables is' -> 'vegetables are'",
        "missing article: 'consumption' -> 'the consumption'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'crucial', 'nutrition', 'balanced diet', 'consequences', 'obesity', 'diabetes', 'subsidize', 'processed food'. >Band 5: Strong topic vocabulary. Not Band 7: Lacks stylistic flair.",
    grammar_reason="[GRA5] Modals: 'should teach', 'must discourage'. Conditionals: 'If vegetables is cheaper...'. >Band 4: Uses a range of structures. Not Band 6: Basic grammar errors remain.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 206: V6/G5 - Topic: Transport (Traffic)
samples.append(create_sample(
    index=206,
    vocab_band=6,
    grammar_band=5,
    question="What is the best solution for traffic congestion?",
    transcript="Improving public transportation is the most effective method. If buses and trains is reliable and affordable, people will use them. Currently, the infrastructure is inadequate. Commuters prefer private vehicles because of comfort. Government should invest in subway systems. Also, congestion charges can deter people from driving in city centers.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'buses and trains is' -> 'buses and trains are'",
        "verb agreement: 'infrastructure is' (correct)",
        "verb agreement: 'Commuters prefer' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'effective method', 'reliable', 'affordable', 'infrastructure', 'inadequate', 'commuters', 'private vehicles', 'invest', 'congestion charges', 'deter'. >Band 5: Sophisticated vocabulary. Not Band 7: Usage is functional.",
    grammar_reason="[GRA5] Conditionals: 'If buses...'. Reason: 'because of comfort'. >Band 4: Complex sentences used. Not Band 6: Subject-verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 207: V6/G5 - Topic: Culture (Globalization)
samples.append(create_sample(
    index=207,
    vocab_band=6,
    grammar_band=5,
    question="Does globalization destroy local culture?",
    transcript="To some extent, yes. Western influence is dominant. Local traditions is disappearing. Young generation prefer Hollywood movies and pop music. They forget their cultural heritage. However, globalization also allow cultural exchange. We can learn about other nations. It promote understanding. We should preserve our identity while accepting new ideas.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'traditions is' -> 'traditions are'",
        "verb agreement: 'generation prefer' -> 'generation prefers'",
        "verb agreement: 'globalization also allow' -> 'globalization also allows'",
        "verb agreement: 'It promote' -> 'It promotes'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'dominant', 'disappearing', 'cultural heritage', 'cultural exchange', 'promote', 'preserve', 'identity'. >Band 5: Good range. Not Band 7: Lacks precision in collocations.",
    grammar_reason="[GRA5] Contrast: 'However'. Reason: 'To some extent'. >Band 4: Uses connectors. Not Band 6: Consistent subject-verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 208: V6/G5 - Topic: Work (Leadership)
samples.append(create_sample(
    index=208,
    vocab_band=6,
    grammar_band=5,
    question="Are leaders born or made?",
    transcript="I believe it is a combination. Some individuals has innate qualities like charisma and confidence. But leadership skills can be acquired. Through training and experience, anyone can become a leader. Effective communication and decision-making is essential. A good leader inspire others. Education play a vital role in developing these traits.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'individuals has' -> 'individuals have'",
        "verb agreement: 'skills can be' (correct)",
        "verb agreement: 'decision-making is' (correct)",
        "verb agreement: 'leader inspire' -> 'leader inspires'",
        "verb agreement: 'Education play' -> 'Education plays'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'combination', 'innate qualities', 'charisma', 'acquired', 'effective communication', 'decision-making', 'inspire', 'vital role', 'traits'. >Band 5: Strong vocabulary. Not Band 7: Lacks idiomatic flow.",
    grammar_reason="[GRA5] Passive voice: 'can be acquired'. Reason: 'Through training...'. >Band 4: Complex structures attempted. Not Band 6: Frequent verb errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 209: V6/G5 - Topic: Environment (Climate Change)
samples.append(create_sample(
    index=209,
    vocab_band=6,
    grammar_band=5,
    question="Is climate change the biggest threat to humanity?",
    transcript="Undoubtedly. The consequences is severe. Rising sea levels and extreme weather events. It threaten our survival. Agriculture is affected, leading to food shortages. We must take immediate action. Reduce carbon emissions and switch to renewable energy. If we ignore the warning signs, the damage will be irreversible. It is a global crisis.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'consequences is' -> 'consequences are'",
        "verb agreement: 'It threaten' -> 'It threatens'",
        "fragment: 'Rising sea levels... events'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'undoubtedly', 'consequences', 'severe', 'extreme weather', 'survival', 'agriculture', 'shortages', 'immediate action', 'carbon emissions', 'irreversible', 'crisis'. >Band 5: Very good vocabulary. Not Band 7: Lacks flexibility.",
    grammar_reason="[GRA5] Conditionals: 'If we ignore...'. Modals: 'must take'. >Band 4: Uses range of forms. Not Band 6: Agreement errors and fragments.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 210: V6/G5 - Topic: Education (Exams)
samples.append(create_sample(
    index=210,
    vocab_band=6,
    grammar_band=5,
    question="Do exams measure intelligence accurately?",
    transcript="No, they does not. Exams only test memory and ability to work under pressure. They do not assess creativity or critical thinking. A student might be intelligent but fail due to anxiety. Continuous assessment is a better alternative. It evaluate progress over time. Exams is just a snapshot of performance.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'they does not' -> 'they do not'",
        "verb agreement: 'It evaluate' -> 'It evaluates'",
        "verb agreement: 'Exams is' -> 'Exams are'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'accurately', 'ability', 'assess', 'creativity', 'critical thinking', 'anxiety', 'continuous assessment', 'alternative', 'evaluate', 'snapshot', 'performance'. >Band 5: Precise terms. Not Band 7: Lacks stylistic variation.",
    grammar_reason="[GRA5] Contrast: 'might be intelligent but fail'. Reason: 'due to anxiety'. >Band 4: Complex reasoning. Not Band 6: Basic verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 211: V6/G5 - Topic: Society (Aging)
samples.append(create_sample(
    index=211,
    vocab_band=6,
    grammar_band=5,
    question="What are the challenges of an aging population?",
    transcript="The main challenge is the burden on the healthcare system. Elderly people require more medical attention. This cost a lot of money. Also, the workforce shrink. There are fewer young people to support the economy. Pension schemes is under pressure. We need to encourage people to work longer. Or increase immigration to fill the labor gap.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'This cost' -> 'This costs'",
        "verb agreement: 'workforce shrink' -> 'workforce shrinks'",
        "verb agreement: 'schemes is' -> 'schemes are'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'burden', 'healthcare system', 'medical attention', 'workforce', 'pension schemes', 'encourage', 'immigration', 'labor gap'. >Band 5: Topic-specific vocabulary. Not Band 7: Lacks nuanced expression.",
    grammar_reason="[GRA5] Reason: 'There are fewer...'. Modals: 'Need to encourage'. >Band 4: Logical structure. Not Band 6: Frequent agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 212: V6/G5 - Topic: Technology (AI)
samples.append(create_sample(
    index=212,
    vocab_band=6,
    grammar_band=5,
    question="Should we rely on AI for decision making?",
    transcript="It depends on the context. AI can process vast amounts of data quickly. It is objective and unbiased. However, it lack ethical judgment. Human intuition is important for moral decisions. If we rely too much on AI, we might lose control. A collaboration between human and machine is ideal. We should use AI as a tool, not a master.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'it lack' -> 'it lacks'",
        "singular/plural: 'between human' -> 'between humans'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'context', 'process', 'vast', 'objective', 'unbiased', 'ethical judgment', 'intuition', 'moral decisions', 'collaboration'. >Band 5: Sophisticated vocabulary. Not Band 7: Lacks natural flow.",
    grammar_reason="[GRA5] Conditionals: 'If we rely...'. Contrast: 'However'. >Band 4: Complex sentences used. Not Band 6: Agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 213: V6/G5 - Topic: Travel (Tourism)
samples.append(create_sample(
    index=213,
    vocab_band=6,
    grammar_band=5,
    question="Does tourism benefit the host country?",
    transcript="Yes, it bring significant economic benefits. It create employment opportunities in hospitality. Hotels and restaurants flourish. However, there are drawbacks. Overcrowding can damage historical sites. Local culture might be commodified. The environment suffer from pollution. Sustainable tourism is the solution. We must protect the destination.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'it bring' -> 'it brings'",
        "verb agreement: 'It create' -> 'It creates'",
        "verb agreement: 'environment suffer' -> 'environment suffers'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'significant', 'economic benefits', 'employment opportunities', 'hospitality', 'flourish', 'drawbacks', 'overcrowding', 'historical sites', 'commodified', 'sustainable tourism'. >Band 5: Advanced vocabulary. Not Band 7: Collocations slightly stiff.",
    grammar_reason="[GRA5] Contrast: 'However'. Passive: 'might be commodified'. >Band 4: Uses complex forms. Not Band 6: Subject-verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 214: V6/G5 - Topic: Education (Online)
samples.append(create_sample(
    index=214,
    vocab_band=6,
    grammar_band=5,
    question="Will online learning replace traditional schools?",
    transcript="I don't think so. Online learning offers flexibility and convenience. Access to resources is easy. But face-to-face interaction is vital. Social skills is developed in the classroom. Students need guidance from teachers. Also, isolation can lead to lack of motivation. A hybrid model is the future. Combining both methods.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'skills is' -> 'skills are'",
        "fragment: 'Combining both methods'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'flexibility', 'convenience', 'resources', 'interaction', 'vital', 'social skills', 'guidance', 'isolation', 'motivation', 'hybrid model'. >Band 5: Precise terms. Not Band 7: Lacks full fluency.",
    grammar_reason="[GRA5] Contrast: 'But face-to-face...'. Passive: 'is developed'. >Band 4: Complex reasoning. Not Band 6: Agreement errors and fragments.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 215: V6/G5 - Topic: Work (Remote)
samples.append(create_sample(
    index=215,
    vocab_band=6,
    grammar_band=5,
    question="Is remote work effective?",
    transcript="It has proven to be effective. Productivity often increase because there are fewer distractions. Employees save time on commuting. They have better work-life balance. However, communication can be a challenge. Team cohesion might suffer. It depend on the individual discipline. Some people needs supervision.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Productivity often increase' -> 'Productivity often increases'",
        "verb agreement: 'It depend' -> 'It depends'",
        "verb agreement: 'Some people needs' -> 'Some people need'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'proven', 'productivity', 'distractions', 'commuting', 'work-life balance', 'cohesion', 'discipline', 'supervision'. >Band 5: Strong vocabulary. Not Band 7: Lacks idiomatic expressions.",
    grammar_reason="[GRA5] Reason: 'because there are...'. Contrast: 'However'. >Band 4: Connectors used well. Not Band 6: Frequent verb errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 216: V6/G5 - Topic: Society (Happiness)
samples.append(create_sample(
    index=216,
    vocab_band=6,
    grammar_band=5,
    question="Does money buy happiness?",
    transcript="It facilitate happiness but does not guarantee it. Money provide security and comfort. You can enjoy experiences like travel. However, material possessions does not bring lasting joy. Relationships and health is more important. If you are lonely, money has no value. Fulfillment come from helping others. So, money is a tool, not the goal.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'It facilitate' -> 'It facilitates'",
        "verb agreement: 'Money provide' -> 'Money provides'",
        "verb agreement: 'possessions does not' -> 'possessions do not'",
        "verb agreement: 'health is' (compound subject) -> 'health are'",
        "verb agreement: 'Fulfillment come' -> 'Fulfillment comes'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'facilitate', 'guarantee', 'security', 'material possessions', 'lasting joy', 'fulfillment', 'value'. >Band 5: Abstract vocabulary. Not Band 7: Lacks flexibility.",
    grammar_reason="[GRA5] Contrast: 'However'. Conditionals: 'If you are lonely...'. >Band 4: Complex structures attempted. Not Band 6: Systematic agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 217: V6/G5 - Topic: Culture (Language)
samples.append(create_sample(
    index=217,
    vocab_band=6,
    grammar_band=5,
    question="Why are some languages disappearing?",
    transcript="Globalization is the main culprit. Dominant languages like English is replacing local dialects. Young people prefer to learn major languages for economic opportunities. They view their native tongue as useless. Also, education systems often ignore minority languages. Without preservation efforts, cultural diversity will vanish. Language is linked to identity. Losing it is a tragedy.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'English is replacing' (correct)",
        "verb agreement: 'languages... is replacing' -> 'languages... are replacing'",
        "verb agreement: 'people prefer' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'culprit', 'dominant', 'dialects', 'economic opportunities', 'native tongue', 'minority', 'preservation', 'diversity', 'vanish', 'tragedy'. >Band 5: Sophisticated terms. Not Band 7: Lacks natural collocation.",
    grammar_reason="[GRA5] Reason: 'for economic opportunities'. Conditionals implied. >Band 4: Logical flow. Not Band 6: Subject-verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 218: V6/G5 - Topic: Environment (Waste)
samples.append(create_sample(
    index=218,
    vocab_band=6,
    grammar_band=5,
    question="How can we reduce household waste?",
    transcript="We need to adopt a zero-waste lifestyle. Recycling is essential, but reducing consumption is better. Avoid single-use plastics. Composting organic waste is beneficial. It enrich the soil. People should repair items instead of throwing them away. Consumerism encourage waste. We must be mindful of our impact. Sustainable habits is necessary.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'It enrich' -> 'It enriches'",
        "verb agreement: 'Consumerism encourage' -> 'Consumerism encourages'",
        "verb agreement: 'habits is' -> 'habits are'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'adopt', 'zero-waste', 'lifestyle', 'essential', 'consumption', 'single-use plastics', 'composting', 'organic', 'beneficial', 'consumerism', 'mindful', 'sustainable'. >Band 5: High-level vocabulary. Not Band 7: Lacks idiomatic usage.",
    grammar_reason="[GRA5] Contrast: 'but reducing...'. Modals: 'must be mindful'. >Band 4: Varied structures. Not Band 6: Basic verb errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 219: V6/G5 - Topic: Technology (Space)
samples.append(create_sample(
    index=219,
    vocab_band=6,
    grammar_band=5,
    question="What are the benefits of space exploration?",
    transcript="It drive technological innovation. Many inventions, like GPS and satellite imagery, comes from space research. It also expand our understanding of the universe. We might find resources on other planets. However, the cost is astronomical. Critics argue that we should solve problems on Earth first. But curiosity is human nature. Exploration lead to progress.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'It drive' -> 'It drives'",
        "verb agreement: 'inventions... comes' -> 'inventions... come'",
        "verb agreement: 'It also expand' -> 'It also expands'",
        "verb agreement: 'Exploration lead' -> 'Exploration leads'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'innovation', 'inventions', 'satellite imagery', 'universe', 'resources', 'astronomical', 'critics', 'curiosity', 'human nature'. >Band 5: Advanced vocabulary. Not Band 7: Usage is slightly academic.",
    grammar_reason="[GRA5] Contrast: 'However'. Reason: 'like GPS...'. >Band 4: Complex sentences. Not Band 6: Persistent agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 220: V6/G5 - Topic: Health (Sport)
samples.append(create_sample(
    index=220,
    vocab_band=6,
    grammar_band=5,
    question="Why are extreme sports becoming popular?",
    transcript="People seek adrenaline and excitement. Modern life is routine and safe. They want to challenge their limits. Extreme sports like skydiving offer a thrill. It allow them to escape boredom. Also, social media influence is strong. People want to share impressive photos. Risk-taking behavior is attractive. It make them feel alive.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'It allow' -> 'It allows'",
        "verb agreement: 'It make' -> 'It makes'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'seek', 'adrenaline', 'routine', 'challenge', 'limits', 'skydiving', 'thrill', 'boredom', 'influence', 'impressive', 'risk-taking'. >Band 5: Good topic vocabulary. Not Band 7: Lacks natural phrasing.",
    grammar_reason="[GRA5] Reason: 'People seek adrenaline'. Description: 'like skydiving'. >Band 4: Logical structure. Not Band 6: Subject-verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 221: V6/G5 - Topic: Society (Celebrity)
samples.append(create_sample(
    index=221,
    vocab_band=6,
    grammar_band=5,
    question="Should celebrities be role models?",
    transcript="Ideally, yes. They have a huge platform and influence. Young people look up to them. If they promote positive values, it inspire fans. For example, charity work or environmental awareness. However, many celebrities is famous for bad behavior. Scandal and controversy attracts attention. They are not obligated to be moral leaders. Parents should guide their children instead.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'it inspire' -> 'it inspires'",
        "verb agreement: 'celebrities is' -> 'celebrities are'",
        "verb agreement: 'controversy attracts' (correct, singular)",
        "verb agreement: 'Scandal... attracts' (compound subject implied plural?)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'platform', 'influence', 'look up to', 'promote', 'positive values', 'awareness', 'scandal', 'controversy', 'obligated', 'moral leaders'. >Band 5: Sophisticated terms. Not Band 7: Lacks flexibility.",
    grammar_reason="[GRA5] Conditionals: 'If they promote...'. Contrast: 'However'. >Band 4: Complex structures. Not Band 6: Verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 222: V6/G5 - Topic: Education (Music)
samples.append(create_sample(
    index=222,
    vocab_band=6,
    grammar_band=5,
    question="What is the value of music education?",
    transcript="It foster creativity and self-expression. Learning an instrument require discipline and patience. It also improve cognitive abilities. Studies show that music help with math skills. Furthermore, it relieve stress. Students can relax through playing. It is a vital part of a holistic education. Cutting arts funding is a mistake.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'It foster' -> 'It fosters'",
        "verb agreement: 'instrument require' -> 'instrument requires'",
        "verb agreement: 'It also improve' -> 'It also improves'",
        "verb agreement: 'music help' -> 'music helps'",
        "verb agreement: 'it relieve' -> 'it relieves'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'foster', 'self-expression', 'instrument', 'discipline', 'patience', 'cognitive abilities', 'relieve', 'holistic', 'funding'. >Band 5: Advanced vocabulary. Not Band 7: Slightly academic tone.",
    grammar_reason="[GRA5] Reason: 'It foster...'. Addition: 'Furthermore'. >Band 4: Logical flow. Not Band 6: Systematic verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 223: V6/G5 - Topic: Transport (Bicycles)
samples.append(create_sample(
    index=223,
    vocab_band=6,
    grammar_band=5,
    question="Is cycling a viable alternative to driving?",
    transcript="In some cities, yes. It is eco-friendly and inexpensive. Cycling reduce traffic congestion and carbon footprint. It is also beneficial for health. However, infrastructure is often lacking. Safety is a concern. If there is no dedicated lanes, cyclists is in danger. Also, weather limit its usage. It is not practical for long distances.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Cycling reduce' -> 'Cycling reduces'",
        "verb agreement: 'there is no dedicated lanes' -> 'there are no dedicated lanes'",
        "verb agreement: 'cyclists is' -> 'cyclists are'",
        "verb agreement: 'weather limit' -> 'weather limits'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'viable', 'alternative', 'eco-friendly', 'inexpensive', 'congestion', 'carbon footprint', 'beneficial', 'infrastructure', 'dedicated lanes', 'practical'. >Band 5: Strong vocabulary. Not Band 7: Lacks idiomatic phrases.",
    grammar_reason="[GRA5] Contrast: 'However'. Conditionals: 'If there is no...'. >Band 4: Complex sentences. Not Band 6: Frequent agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 224: V6/G5 - Topic: Work (Job Satisfaction)
samples.append(create_sample(
    index=224,
    vocab_band=6,
    grammar_band=5,
    question="How important is the working environment?",
    transcript="It is paramount. A toxic environment decrease productivity. Employees need to feel valued and supported. Good relationships with colleagues is essential. If the atmosphere is stressful, turnover rate increase. People quit. Physical environment matter too. Lighting and ergonomics affects performance. Companies should prioritize employee well-being.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'environment decrease' -> 'environment decreases'",
        "verb agreement: 'relationships... is' -> 'relationships... are'",
        "verb agreement: 'rate increase' -> 'rate increases'",
        "verb agreement: 'environment matter' -> 'environment matters'",
        "verb agreement: 'ergonomics affects' (correct singular)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'paramount', 'toxic', 'productivity', 'valued', 'atmosphere', 'turnover rate', 'ergonomics', 'performance', 'prioritize', 'well-being'. >Band 5: Precise vocabulary. Not Band 7: Lacks natural flow.",
    grammar_reason="[GRA5] Conditionals: 'If the atmosphere is...'. Modals: 'Should prioritize'. >Band 4: Varied structures. Not Band 6: Agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 225: V6/G5 - Topic: Society (History)
samples.append(create_sample(
    index=225,
    vocab_band=6,
    grammar_band=5,
    question="Can we learn from the past?",
    transcript="Absolutely. History provide valuable lessons. We can analyze past mistakes to avoid repeating them. For instance, wars and economic crises. Understanding our origins help us shape the future. However, humanity often forget these lessons. We make the same errors. Historical knowledge is crucial for progress. Without it, we are lost.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'History provide' -> 'History provides'",
        "verb agreement: 'origins help' -> 'origins helps' (Understanding is subject)",
        "verb agreement: 'humanity often forget' -> 'humanity often forgets'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'valuable', 'analyze', 'mistakes', 'economic crises', 'origins', 'shape', 'humanity', 'crucial', 'progress'. >Band 5: Good range. Not Band 7: Lacks stylistic nuance.",
    grammar_reason="[GRA5] Purpose: 'to avoid repeating'. Contrast: 'However'. >Band 4: Uses connectors. Not Band 6: Subject-verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
