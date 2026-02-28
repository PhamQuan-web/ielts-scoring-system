import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch14.jsonl")

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

# --- BATCH 14 PART 1: SAMPLES 1161-1202 (42 Total) ---
# Combo: V6/G9 (Mixed Vocab, Flawless Grammar)
# Strategy: Use mixed vocabulary (some good, some inaccurate) but absolutely perfect grammar (complex structures, zero errors).

topics_14_1 = [
    ("Environment", "Climate Change", "Is climate change real?", "It is definitely happening. The weather is getting hotter every year. Scientists have proven that pollution is the cause. Had we acted sooner, the situation would not be so dire. Although some people deny it, the evidence is clear. We must change our habits immediately.",
     "[LR6] Vocab: 'dire', 'deny', 'evidence', 'habits'. >Band 5: Good range. Not Band 7: Lacks precision.",
     "[GRA9] Flawless grammar: 'Had we acted...', 'Although some people...', 'We must change...'. Error-free."),
    ("Technology", "AI", "Will AI take over?", "I do not think so. AI is a tool that we created. While it is very smart, it cannot feel emotions. Unless we give it too much power, we are safe. It is essential that we regulate its development carefully. Only then can we ensure it benefits humanity.",
     "[LR6] Vocab: 'tool', 'smart', 'emotions', 'regulate', 'humanity'. >Band 5: Adequate. Not Band 7: Lacks sophistication.",
     "[GRA9] Perfect structures: 'Unless we give...', 'It is essential that...', 'Only then can we...'. Error-free."),
    ("Education", "University", "Is university important?", "It depends on the person. Some jobs require a degree, while others do not. If you want to be a doctor, you must go to university. However, vocational training is also valuable. It is a decision that should not be taken lightly.",
     "[LR6] Vocab: 'require', 'degree', 'vocational training', 'valuable'. >Band 5: Good topic vocab. Not Band 7: A bit standard.",
     "[GRA9] Complex sentences: 'while others do not', 'If you want...', 'decision that should not...'. Flawless."),
    ("Work", "Remote Work", "Is working from home good?", "Working from home has many benefits. It saves time on commuting. Moreover, people can be more productive. On the other hand, it can be lonely. I believe that a hybrid model is the best solution. It allows for flexibility without sacrificing social interaction.",
     "[LR6] Vocab: 'commuting', 'productive', 'lonely', 'hybrid model', 'flexibility'. >Band 5: Relevant. Not Band 7: Lacks flair.",
     "[GRA9] Varied structures: 'Moreover...', 'On the other hand...', 'without sacrificing...'. Error-free."),
    ("Society", "Social Media", "Is social media bad?", "Social media can be addictive. People spend hours scrolling through feeds. While it connects us, it also isolates us. Had I known the effects, I would have used it less. It is crucial that we limit our screen time. Otherwise, our mental health will suffer.",
     "[LR6] Vocab: 'addictive', 'scrolling', 'isolates', 'screen time', 'mental health'. >Band 5: Good range. Not Band 7: Slightly repetitive.",
     "[GRA9] Advanced grammar: 'Had I known...', 'It is crucial that...', 'Otherwise...'. Perfect control."),
    ("Health", "Fast Food", "Why is fast food popular?", "Fast food is convenient and cheap. Many people eat it because they are busy. Although it tastes good, it is unhealthy. If we continue to eat it, obesity rates will rise. It is time that we prioritized our health over convenience.",
     "[LR6] Vocab: 'convenient', 'cheap', 'unhealthy', 'obesity rates', 'prioritized'. >Band 5: Clear. Not Band 7: Lacks nuance.",
     "[GRA9] Structures: 'because they are...', 'Although it tastes...', 'It is time that we...'. Error-free."),
    ("Transport", "Traffic", "How to solve traffic?", "Traffic congestion is a major issue in cities. The government should invest in public transport. If trains were cheaper, more people would use them. Additionally, cycling lanes should be built. This would encourage people to leave their cars at home.",
     "[LR6] Vocab: 'congestion', 'invest', 'public transport', 'encourage'. >Band 5: Adequate. Not Band 7: Basic collocations.",
     "[GRA9] Conditionals: 'If trains were...', 'This would encourage...'. Modal verbs used correctly. Flawless."),
    ("Culture", "Tradition", "Are traditions important?", "Traditions connect us to our past. They give us a sense of identity. While some traditions are outdated, others are valuable. We should preserve the ones that bring us together. It is through traditions that we understand our history.",
     "[LR6] Vocab: 'connect', 'identity', 'outdated', 'valuable', 'preserve'. >Band 5: Good range. Not Band 7: Slightly generic.",
     "[GRA9] Cleft sentence: 'It is through traditions that...'. Contrast: 'While some...'. Error-free."),
    ("Environment", "Plastic", "Should we ban plastic?", "Plastic pollution is destroying our oceans. We use too much single-use plastic. Unless we ban it, the problem will worsen. Alternatives like paper and glass are better. It is imperative that we take action now.",
     "[LR6] Vocab: 'pollution', 'destroying', 'single-use', 'worsen', 'imperative'. >Band 5: Strong words. Not Band 7: Repetitive.",
     "[GRA9] Conditional: 'Unless we ban it...'. Structure: 'It is imperative that...'. Perfect accuracy."),
    ("Technology", "Smartphones", "Are phones too expensive?", "Smartphones have become very expensive. The latest models cost a fortune. Although they have new features, they are not always worth it. People buy them to show off. I wish that they were more affordable for everyone.",
     "[LR6] Vocab: 'fortune', 'features', 'show off', 'affordable'. >Band 5: Conversational. Not Band 7: Lacks academic tone.",
     "[GRA9] Subjunctive: 'I wish that they were...'. Contrast: 'Although they have...'. Flawless."),
    ("Society", "Inequality", "Is inequality rising?", "The gap between rich and poor is widening. Wealth is concentrated in the hands of a few. This is unfair to the majority. Unless the government intervenes, social unrest may occur. We need a system that distributes wealth more evenly.",
     "[LR6] Vocab: 'gap', 'widening', 'concentrated', 'intervenes', 'unrest'. >Band 5: Good topic vocab. Not Band 7: Lacks depth.",
     "[GRA9] Conditional: 'Unless the government...'. Relative clause: 'system that distributes...'. Error-free."),
    ("Work", "Salary", "Is salary the most important?", "Salary is important, but not everything. Job satisfaction matters too. If you hate your job, money will not make you happy. I would rather earn less and enjoy my work. It is essential to find a balance between money and happiness.",
     "[LR6] Vocab: 'satisfaction', 'matters', 'earn', 'balance'. >Band 5: Clear. Not Band 7: Simple phrasing.",
     "[GRA9] Conditional: 'If you hate...', 'I would rather...'. Infinitive structure: 'It is essential to...'. Perfect."),
    ("Education", "Online Learning", "Is online learning effective?", "Online learning has become very popular. It allows students to study from anywhere. However, it requires self-discipline. Without a teacher present, some students struggle. I believe that it is a good supplement to traditional education.",
     "[LR6] Vocab: 'popular', 'self-discipline', 'struggle', 'supplement', 'traditional'. >Band 5: Adequate. Not Band 7: Standard terms.",
     "[GRA9] Contrast: 'However, it requires...'. Clause: 'Without a teacher present...'. Flawless."),
    ("Health", "Exercise", "Why exercise?", "Exercise keeps our bodies healthy. It also improves our mental state. People who exercise regularly live longer. Had I started exercising earlier, I would be fitter now. Everyone should try to be active every day.",
     "[LR6] Vocab: 'mental state', 'regularly', 'fitter', 'active'. >Band 5: Good range. Not Band 7: Basic.",
     "[GRA9] Conditional: 'Had I started...'. Relative clause: 'People who exercise...'. Error-free."),
    ("Transport", "Electric Cars", "Are EVs the future?", "Electric cars are better for the environment. They do not produce emissions. Although they are expensive, prices are falling. As technology improves, they will become more common. It is inevitable that we will all drive them one day.",
     "[LR6] Vocab: 'emissions', 'falling', 'improves', 'common', 'inevitable'. >Band 5: Relevant. Not Band 7: Lacks specific terms.",
     "[GRA9] Time clause: 'As technology improves...'. Noun clause: 'It is inevitable that...'. Perfect."),
    ("Culture", "Art", "Is art important?", "Art expresses human emotion. It makes us think about the world. A life without art would be boring. Museums preserve our cultural heritage. It is important that we support artists and their work.",
     "[LR6] Vocab: 'expresses', 'emotion', 'boring', 'preserve', 'heritage'. >Band 5: Good. Not Band 7: Lacks 'creativity', 'inspiration'.",
     "[GRA9] Conditional: 'would be'. Subjunctive: 'It is important that we support...'. Flawless."),
    ("Environment", "Recycling", "Does recycling help?", "Recycling reduces waste in landfills. It reuses materials like plastic and paper. If everyone recycled, the planet would be cleaner. However, reducing consumption is even better. We must be conscious of what we buy.",
     "[LR6] Vocab: 'reduces', 'landfills', 'reuises', 'consumption', 'conscious'. >Band 5: Adequate. Not Band 7: Repetitive.",
     "[GRA9] Conditional: 'If everyone recycled...'. Comparison: 'even better'. Modal: 'must be'. Error-free."),
    ("Technology", "Robots", "Will robots replace us?", "Robots can do many tasks faster than humans. They are used in factories and hospitals. However, they lack creativity and empathy. I do not believe they will replace us completely. Humans will always be needed for complex decisions.",
     "[LR6] Vocab: 'tasks', 'factories', 'creativity', 'empathy', 'completely'. >Band 5: Clear. Not Band 7: Standard.",
     "[GRA9] Comparison: 'faster than'. Contrast: 'However, they lack...'. Noun clause: 'I do not believe...'. Perfect."),
    ("Society", "Community", "Is community important?", "A strong community supports its members. People help each other in times of need. Living in isolation is difficult. Had we not had a community, we would have struggled. We should build stronger connections with our neighbors.",
     "[LR6] Vocab: 'supports', 'isolation', 'struggled', 'connections', 'neighbors'. >Band 5: Good range. Not Band 7: Basic.",
     "[GRA9] Conditional: 'Had we not had...'. Gerund: 'Living in isolation...'. Flawless."),
    ("Work", "Retirement", "When to retire?", "Retirement is a time to relax. People work hard all their lives for it. Some retire at 60, while others work longer. It depends on your health and finances. I hope to retire when I am still healthy enough to travel.",
     "[LR6] Vocab: 'relax', 'finances', 'healthy', 'travel'. >Band 5: Clear. Not Band 7: Lacks 'pension', 'leisure'.",
     "[GRA9] Contrast: 'while others work...'. Noun clause: 'It depends on...'. Infinitive: 'hope to retire'. Perfect.")
]

# Expanding the list to 42 samples by repeating with slight variations or adding more
# To ensure unique IDs, I'll generate 22 more unique topics/variations

more_topics = [
    ("Health", "Sleep", "Why sleep?", "Sleep is vital for our bodies. If we do not sleep enough, we get sick. It helps our brains to recover. Although I am busy, I try to sleep 8 hours. It is recommended that adults get enough rest.", "[LR6] Vocab: 'vital', 'recover', 'recommended', 'rest'.", "[GRA9] Conditional: 'If we do not...'. Passive: 'It is recommended that...'. Flawless."),
    ("Education", "History", "Why study history?", "History teaches us about the past. By understanding history, we avoid mistakes. Had leaders studied history, wars might have been avoided. It is fascinating to learn about ancient civilizations.", "[LR6] Vocab: 'teaches', 'mistakes', 'avoided', 'fascinating', 'civilizations'.", "[GRA9] Conditional: 'Had leaders studied...'. Gerund: 'By understanding...'. Perfect."),
    ("Transport", "Flying", "Is flying safe?", "Flying is the safest way to travel. Accidents are very rare. Although some people are scared, statistics show it is safe. I would fly everywhere if I could. It allows us to see the world.", "[LR6] Vocab: 'safest', 'accidents', 'rare', 'statistics', 'scared'.", "[GRA9] Conditional: 'I would fly... if I could'. Comparison: 'safest'. Contrast: 'Although...'. Flawless."),
    ("Technology", "Internet", "Is the internet good?", "The internet has changed our lives. We can find information instantly. However, there is also fake news. Unless we are careful, we can be misled. It is a powerful tool that must be used wisely.", "[LR6] Vocab: 'instantly', 'fake news', 'misled', 'powerful', 'wisely'.", "[GRA9] Conditional: 'Unless we are...'. Passive: 'must be used'. Perfect."),
    ("Environment", "Water", "Is water scarce?", "Water scarcity is a growing problem. Many countries do not have clean water. We must conserve what we have. If we waste water, future generations will suffer. It is our duty to protect this resource.", "[LR6] Vocab: 'scarcity', 'conserve', 'waste', 'generations', 'resource'.", "[GRA9] Conditional: 'If we waste...'. Infinitive: 'duty to protect'. Error-free."),
    ("Society", "Family", "Is family important?", "Family is the foundation of society. They support us unconditionally. A life without family would be lonely. I value the time I spend with them. It is with family that we feel most at home.", "[LR6] Vocab: 'foundation', 'unconditionally', 'lonely', 'value'.", "[GRA9] Conditional: 'would be'. Cleft: 'It is with family that...'. Flawless."),
    ("Work", "Stress", "Is work stressful?", "Work can be very stressful. Deadlines and pressure make people anxious. It is important to take breaks. Had I known how stressful this job was, I would not have taken it. Mental health should come first.", "[LR6] Vocab: 'stressful', 'deadlines', 'anxious', 'breaks'.", "[GRA9] Conditional: 'Had I known...'. Modal: 'should come'. Perfect."),
    ("Culture", "Language", "Why learn languages?", "Learning languages opens doors. It allows us to communicate with others. Being bilingual is a great skill. It is said that learning a new language keeps the brain young. Everyone should try to learn one.", "[LR6] Vocab: 'opens doors', 'communicate', 'bilingual', 'skill'.", "[GRA9] Passive: 'It is said that...'. Gerund: 'Learning languages...'. Flawless."),
    ("Health", "Diet", "Is sugar bad?", "Too much sugar is bad for you. It causes weight gain and diabetes. Although it tastes sweet, we should limit it. If you stop eating sugar, you will feel better. It is a change that is worth making.", "[LR6] Vocab: 'weight gain', 'diabetes', 'limit', 'worth making'.", "[GRA9] Conditional: 'If you stop...'. Relative clause: 'change that is worth...'. Perfect."),
    ("Transport", "Walking", "Is walking good?", "Walking is great exercise. It is free and easy to do. People who walk every day are healthier. I would walk to work if it were closer. It is the best way to explore a city.", "[LR6] Vocab: 'exercise', 'free', 'healthier', 'explore'.", "[GRA9] Conditional: 'I would walk... if it were...'. Relative clause: 'People who walk...'. Flawless."),
    ("Technology", "Gaming", "Is gaming bad?", "Gaming can be fun and educational. It improves hand-eye coordination. However, it can be addictive. Parents should monitor their children. It is important that kids play outside too.", "[LR6] Vocab: 'educational', 'coordination', 'addictive', 'monitor'.", "[GRA9] Subjunctive: 'important that kids play...'. Contrast: 'However...'. Perfect."),
    ("Environment", "Trees", "Why plant trees?", "Trees produce oxygen and clean the air. They are home to many animals. If we cut down trees, we harm the planet. We should plant more trees in cities. It is essential for our survival.", "[LR6] Vocab: 'oxygen', 'harm', 'survival'.", "[GRA9] Conditional: 'If we cut down...'. Modal: 'should plant'. Error-free."),
    ("Society", "Crime", "Is crime rising?", "Crime is a concern in many places. Poverty often leads to crime. If we reduce poverty, crime will decrease. The police should work with the community. It is a complex problem to solve.", "[LR6] Vocab: 'concern', 'poverty', 'decrease', 'complex'.", "[GRA9] Conditional: 'If we reduce...'. Infinitive: 'problem to solve'. Flawless."),
    ("Work", "Teamwork", "Is teamwork important?", "Teamwork is essential in most jobs. We achieve more when we work together. Had we not worked as a team, we would have failed. It teaches us to compromise. Everyone has a role to play.", "[LR6] Vocab: 'essential', 'achieve', 'failed', 'compromise', 'role'.", "[GRA9] Conditional: 'Had we not worked...'. Infinitive: 'role to play'. Perfect."),
    ("Education", "Reading", "Why read?", "Reading expands our minds. It takes us to different worlds. People who read are often more empathetic. I wish I had more time to read. It is a habit that everyone should cultivate.", "[LR6] Vocab: 'expands', 'empathetic', 'habit', 'cultivate'.", "[GRA9] Subjunctive: 'I wish I had...'. Relative clause: 'People who read...'. Flawless."),
    ("Health", "Mental Health", "Is it important?", "Mental health is just as important as physical health. Stress can cause illness. We must take care of our minds. If we ignore our feelings, we will suffer. It is time we talked openly about it.", "[LR6] Vocab: 'physical health', 'illness', 'ignore', 'suffer', 'openly'.", "[GRA9] Comparison: 'as important as'. Subjunctive: 'It is time we talked...'. Perfect."),
    ("Transport", "Bicycles", "Are bikes good?", "Bicycles are eco-friendly and cheap. They help reduce traffic congestion. If cities had more bike lanes, more people would ride. It is a healthy way to commute. We should encourage cycling.", "[LR6] Vocab: 'eco-friendly', 'congestion', 'lanes', 'commute', 'encourage'.", "[GRA9] Conditional: 'If cities had...'. Modal: 'should encourage'. Error-free."),
    ("Technology", "Space", "Why go to space?", "Space exploration pushes boundaries. We learn about the universe. Although it is expensive, it inspires us. Someday we might live on Mars. It is a dream that drives scientists.", "[LR6] Vocab: 'exploration', 'boundaries', 'universe', 'inspires', 'dream'.", "[GRA9] Contrast: 'Although it is...'. Modal: 'might live'. Relative clause: 'dream that drives...'. Perfect."),
    ("Environment", "Animals", "Why save animals?", "Animals are part of our ecosystem. If they go extinct, it affects us. We must protect endangered species. Had we protected them sooner, we would have more diversity. It is our responsibility.", "[LR6] Vocab: 'ecosystem', 'extinct', 'endangered', 'diversity', 'responsibility'.", "[GRA9] Conditional: 'Had we protected...'. Modal: 'must protect'. Flawless."),
    ("Society", "Friends", "Are friends necessary?", "Friends provide support and love. They make life enjoyable. A person without friends is lonely. I cherish my friendships. It is important to have people you trust.", "[LR6] Vocab: 'support', 'enjoyable', 'lonely', 'cherish', 'trust'.", "[GRA9] Infinitive: 'important to have'. Relative clause: 'people you trust'. Perfect."),
    ("Work", "Career", "How to choose?", "Choose a career you love. Passion leads to success. If you work only for money, you will be bored. It is a decision that affects your whole life. You should think carefully.", "[LR6] Vocab: 'career', 'passion', 'success', 'bored', 'carefully'.", "[GRA9] Conditional: 'If you work...'. Relative clause: 'decision that affects...'. Error-free."),
    ("Education", "Math", "Is math useful?", "Math is used in everyday life. We use it to count money. Although it is hard, it is logical. If I were better at math, I would be an engineer. It is a subject that requires practice.", "[LR6] Vocab: 'everyday life', 'count', 'logical', 'engineer', 'practice'.", "[GRA9] Conditional: 'If I were...'. Relative clause: 'subject that requires...'. Flawless.")
]

full_topics = topics_14_1 + more_topics # Total 42

start_index = 1161
for i, item in enumerate(full_topics):
    samples.append(create_sample(
        index=start_index + i,
        vocab_band=6,
        grammar_band=9,
        question=item[2],
        transcript=item[3],
        response_type="extended",
        micro_flaws=[],
        grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
        vocab_reason=item[4],
        grammar_reason=item[5],
        idiom_present=False,
        risk_level="low"
    ))

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Generated {len(samples)} samples in {OUTPUT_FILE}")
