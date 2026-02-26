import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch12.jsonl")

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

# --- BATCH 12 PART 3: SAMPLES 1031-1055 (25 Total) ---
# Combo: V7/G9 (Good Vocab, Expert Grammar)
# Strategy: Use standard but precise vocabulary (V7) within flawlessly constructed, complex sentences (G9).

# Sample 1031: V7/G9 - Topic: Environment
samples.append(create_sample(
    index=1031,
    vocab_band=7,
    grammar_band=9,
    question="Why is climate change a problem?",
    transcript="Climate change poses a significant threat because it disrupts weather patterns globally. Were we to ignore the rising temperatures, the consequences would be severe. Not only does it affect agriculture, leading to food shortages, but it also endangers wildlife. It is crucial that we take immediate action. Unless governments implement strict policies, the damage will become irreversible.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'disrupts', 'consequences', 'severe', 'shortages', 'endangers', 'crucial', 'implement', 'irreversible'. >Band 6: Precise. Not Band 8: Lacks sophistication.",
    grammar_reason="[GRA9] Full range of structures used naturally and accurately. 'Were we to ignore...' (inversion), 'Not only does it affect..., but it also...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1032: V7/G9 - Topic: Technology
samples.append(create_sample(
    index=1032,
    vocab_band=7,
    grammar_band=9,
    question="Is the internet beneficial?",
    transcript="Undoubtedly, the internet has transformed our lives. It provides access to a vast amount of information, which allows us to learn about any topic. Furthermore, it facilitates communication across the globe. However, there are downsides. Cyberbullying and addiction are growing concerns. Should we fail to manage our usage, the negative effects could outweigh the positives.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'transformed', 'vast', 'facilitates', 'downsides', 'cyberbullying', 'addiction', 'outweigh'. >Band 6: Good range. Not Band 8: Lacks idiomatic flair.",
    grammar_reason="[GRA9] Uses advanced structures effortlessly. 'which allows us to...', 'Should we fail to manage...' (inversion). Completely error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1033: V7/G9 - Topic: Education
samples.append(create_sample(
    index=1033,
    vocab_band=7,
    grammar_band=9,
    question="Should education be free?",
    transcript="Ideally, education should be accessible to everyone, regardless of their financial background. By providing free education, society ensures that talent is not wasted. Students who might otherwise be unable to afford tuition can pursue their dreams. Moreover, an educated population contributes to economic growth. Therefore, investing in education is investing in the future of the nation.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'accessible', 'financial background', 'tuition', 'pursue', 'contributes', 'investing'. >Band 6: Relevant vocabulary. Not Band 8: Slightly standard.",
    grammar_reason="[GRA9] Full range of structures. 'regardless of...', 'Students who might otherwise be unable...', 'investing in education is investing...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1034: V7/G9 - Topic: Work
samples.append(create_sample(
    index=1034,
    vocab_band=7,
    grammar_band=9,
    question="What makes a job satisfying?",
    transcript="Job satisfaction stems from a variety of factors. While salary is important, a sense of purpose is equally vital. Employees need to feel that their work has meaning. Additionally, a supportive work environment fosters productivity. When colleagues collaborate effectively, the workplace becomes enjoyable. Ultimately, a balance between work and personal life is essential for long-term happiness.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'stems from', 'factors', 'vital', 'supportive', 'fosters', 'collaborate', 'ultimately', 'essential'. >Band 6: Precise. Not Band 8: Lacks nuance.",
    grammar_reason="[GRA9] Wide range of structures used naturally. 'While salary is important...', 'Employees need to feel that...', 'When colleagues collaborate...'. Error-free.",
    idiom_present=False,
    risk_level="low"
))

# Sample 1035: V7/G9 - Topic: Society
samples.append(create_sample(
    index=1035,
    vocab_band=7,
    grammar_band=9,
    question="Why do people commit crimes?",
    transcript="There are numerous reasons why individuals turn to crime. Poverty is often a primary driver; when people are desperate, they may feel they have no other choice. Lack of education also plays a significant role. Without skills, finding employment is difficult. Furthermore, peer pressure can influence young people. Addressing these root causes is more effective than punishment alone.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'numerous', 'primary driver', 'desperate', 'significant role', 'employment', 'peer pressure', 'addressing', 'root causes'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA9] Full range of structures. 'There are numerous reasons why...', 'when people are desperate, they may...', 'Addressing these... is...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1036: V7/G9 - Topic: Culture
samples.append(create_sample(
    index=1036,
    vocab_band=7,
    grammar_band=9,
    question="Is it important to keep traditions?",
    transcript="Traditions are the foundation of our cultural identity. They connect us to our ancestors and provide a sense of belonging. By participating in rituals, we strengthen community bonds. However, not all traditions should be preserved. Practices that are harmful or discriminatory must be abandoned. We should cherish the customs that bring us together while adapting to modern values.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'foundation', 'identity', 'ancestors', 'rituals', 'bonds', 'preserved', 'discriminatory', 'abandoned', 'cherish'. >Band 6: Good range. Not Band 8: Lacks idiomatic expressions.",
    grammar_reason="[GRA9] Wide range of structures. 'By participating...', 'Practices that are harmful... must be abandoned'. Error-free.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 1037: V7/G9 - Topic: Transport
samples.append(create_sample(
    index=1037,
    vocab_band=7,
    grammar_band=9,
    question="How can we solve traffic problems?",
    transcript="Investing in public transport is the most effective solution. If trains and buses were more reliable and affordable, fewer people would drive private cars. This would significantly reduce congestion. Additionally, encouraging cycling by building safe lanes is beneficial. Governments could also implement congestion charges to deter drivers. A comprehensive strategy is required to tackle this issue.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'investing', 'effective', 'reliable', 'congestion', 'encouraging', 'beneficial', 'implement', 'deter', 'comprehensive'. >Band 6: Precise. Not Band 8: Slightly robotic.",
    grammar_reason="[GRA9] Full range of structures. 'If trains... were... fewer people would...' (conditional), 'encouraging cycling... is beneficial'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1038: V7/G9 - Topic: Health
samples.append(create_sample(
    index=1038,
    vocab_band=7,
    grammar_band=9,
    question="Why is obesity a problem?",
    transcript="Obesity is a major public health concern because it leads to chronic diseases. Conditions such as diabetes and heart disease are often linked to excess weight. The modern lifestyle, which is largely sedentary, contributes to this epidemic. People consume processed foods that are high in sugar and fat. Unless we change our habits, the burden on the healthcare system will increase.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'chronic diseases', 'linked to', 'excess weight', 'sedentary', 'epidemic', 'consume', 'processed foods', 'burden'. >Band 6: Relevant terms. Not Band 8: Lacks fluency.",
    grammar_reason="[GRA9] Wide range: 'The modern lifestyle, which is..., contributes...', 'Unless we change..., the burden... will...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1039: V7/G9 - Topic: Technology
samples.append(create_sample(
    index=1039,
    vocab_band=7,
    grammar_band=9,
    question="Do phones affect relationships?",
    transcript="They have a profound impact on how we interact. While phones allow us to stay connected with distant friends, they can also create a barrier. People often stare at their screens instead of talking to the person next to them. This can lead to feelings of isolation. We must be mindful of our usage to ensure that technology enhances, rather than diminishes, our relationships.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'profound impact', 'interact', 'barrier', 'stare', 'isolation', 'mindful', 'enhances', 'diminishes'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA9] Full range of structures. 'While phones allow...', 'This can lead to...', 'to ensure that technology enhances...'. Error-free.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 1040: V7/G9 - Topic: Environment
samples.append(create_sample(
    index=1040,
    vocab_band=7,
    grammar_band=9,
    question="Why should we recycle?",
    transcript="Recycling is essential for minimizing waste. By reusing materials, we reduce the need to extract new resources, which protects the environment. It also conserves energy and reduces pollution. If everyone recycled, the amount of trash sent to landfills would decrease dramatically. It is a simple action that has a significant positive impact on our planet.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'essential', 'minimizing', 'extract', 'conserves', 'landfills', 'decrease dramatically', 'significant'. >Band 6: Good range. Not Band 8: Lacks idiomatic usage.",
    grammar_reason="[GRA9] Wide range: 'By reusing materials...', 'If everyone recycled... would decrease...', 'It is a simple action that...'. Error-free.",
    idiom_present=False,
    risk_level="low"
))

# ... Adding 15 more samples to reach 25 ...
# Generating 1041-1055

topics_12_3 = [
    ("Work", "Remote", "Is remote work good?", "It offers flexibility that many employees crave. Working from home eliminates the commute, saving time and money. However, it requires self-discipline. Without a structured environment, productivity can suffer. Also, the lack of face-to-face interaction might hinder team cohesion. Ultimately, a hybrid model seems the best solution."),
    ("Society", "Cities", "Why do people move to cities?", "They are drawn by the abundance of opportunities. Cities offer better jobs, education, and healthcare. The vibrant culture and entertainment options are also attractive. However, the cost of living is often high. Housing can be unaffordable for many. Despite the challenges, the allure of city life remains strong."),
    ("Culture", "Global", "Is globalization good?", "It facilitates the exchange of ideas and goods. We have access to products from all over the world. Cultural diversity is enriched. However, it can also lead to the loss of local traditions. Small businesses might struggle to compete with multinational corporations. We must find a balance."),
    ("Education", "Reading", "Is reading important?", "Reading is fundamental to personal growth. It expands our knowledge and improves our vocabulary. Fiction helps us develop empathy by allowing us to experience different lives. In a digital age, reading books helps improve concentration. It is a habit that pays dividends throughout life."),
    ("Transport", "Flying", "Is flying bad?", "Aviation is a major contributor to carbon emissions. Frequent flying damages the environment. However, it connects the world in a way no other transport can. It supports tourism and international business. We need to develop greener fuels to make aviation sustainable. Banning it completely is not realistic."),
    ("Health", "Mental", "How to reduce stress?", "Engaging in regular physical activity is very effective. Exercise releases chemicals that improve mood. Mindfulness and meditation can also help calm the mind. It is important to maintain a work-life balance. Taking time to relax and pursue hobbies prevents burnout. Mental health should be a priority."),
    ("Technology", "Robots", "Will robots replace us?", "They will likely automate repetitive tasks. This could increase efficiency and productivity. However, jobs requiring creativity and emotional intelligence are safe. Robots cannot replicate human empathy. Instead of replacing us, they will likely work alongside us. We must adapt to this new reality."),
    ("Environment", "Wildlife", "Why protect animals?", "Biodiversity is crucial for a healthy ecosystem. Every species plays a unique role. If one goes extinct, it can disrupt the balance. We have a moral duty to protect vulnerable species. Conservation efforts ensure that future generations can enjoy nature. It is about respecting all life."),
    ("Society", "Volunteer", "Why volunteer?", "It fosters a sense of community. Helping others gives people a purpose. It also allows volunteers to learn new skills and meet people. By contributing to society, we make it a better place. The benefits are mutual. It is a rewarding experience."),
    ("Work", "Career", "How to choose a job?", "You should identify your strengths and passions. Doing work you enjoy leads to greater satisfaction. Financial stability is also important, but it should not be the only factor. Researching different industries helps you make an informed decision. A fulfilling career is a journey, not a destination."),
    ("Culture", "Art", "Is art necessary?", "Art is an expression of the human experience. It challenges us to think and feel. It documents our history and values. A society without art would be culturally poor. Government funding is essential to support artists. It is an investment in our collective soul."),
    ("Education", "Skills", "Are soft skills important?", "They are increasingly vital in the workplace. Communication, teamwork, and adaptability are highly valued by employers. While technical skills get you the job, soft skills help you succeed. They enable you to navigate complex social situations. Schools should emphasize their development."),
    ("Transport", "Traffic", "How to fix traffic?", "Improving public transport is the key. If buses and trains are efficient, people will use them. Congestion charges can also deter car usage. We need to design cities for people, not cars. Promoting cycling and walking creates a healthier environment. It requires bold policy changes."),
    ("Health", "Diet", "Why eat healthy?", "Nutrition is the foundation of physical well-being. A balanced diet prevents chronic diseases. Processed foods, high in sugar, should be avoided. Eating fresh vegetables and fruit provides essential vitamins. It is an investment in your long-term health. You are what you eat."),
    ("Technology", "Privacy", "Is privacy important?", "It is a fundamental human right. In the digital age, our data is constantly harvested. This intrusion can lead to manipulation. We must protect our personal information. Stronger regulations are needed to hold tech companies accountable. Privacy ensures our freedom and autonomy.")
]

start_index = 1041
for i, topic in enumerate(topics_12_3):
    samples.append(create_sample(
        index=start_index + i,
        vocab_band=7,
        grammar_band=9,
        question=topic[2],
        transcript=topic[3],
        response_type="extended",
        micro_flaws=[],
        grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
        vocab_reason="[LR7] Uses precise and relevant vocabulary. >Band 6: Strong collocation. Not Band 8: Lacks idiomatic nuance.",
        grammar_reason="[GRA9] Uses a full range of structures naturally and appropriately. Produces consistently error-free sentences. >Band 8: Complete control.",
        idiom_present=False,
        risk_level="medium"
    ))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
