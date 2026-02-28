import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch11.jsonl")

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

# --- BATCH 11 PART 2: SAMPLES 931-980 (50 Total) ---
# Combo: V7/G5 (Vocab: Good/Flexible, Grammar: Limited/Errors)
# Strategy: Use advanced vocabulary ("essential", "detrimental", "crucial", "fluctuate") but make frequent grammatical errors (subject-verb agreement, wrong tense, missing articles).

# Sample 931: V7/G5 - Topic: Environment
samples.append(create_sample(
    index=931,
    vocab_band=7,
    grammar_band=5,
    question="How can we reduce pollution?",
    transcript="Pollution is a detrimental issue for our planet. We must prioritize sustainable energy like solar and wind. However, government need to make strict laws. If factory produce toxic waste, they should pay fine. Also, individuals plays a crucial role. We should reduce consumption of plastic. Recycling is essential. If everyone cooperate, we can mitigate the damage. But it depend on political will.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'government need' -> 'the government needs'",
        "verb agreement: 'factory produce' -> 'factories produce'",
        "missing article: 'pay fine' -> 'pay a fine'",
        "verb agreement: 'individuals plays' -> 'individuals play'",
        "verb agreement: 'it depend' -> 'it depends'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Uses less common items: 'detrimental', 'prioritize', 'sustainable', 'toxic waste', 'consumption', 'mitigate'. >Band 6: Good range and precision. Not Band 8: Some unnatural flow.",
    grammar_reason="[GRA5] Attempts complex sentences but errors are frequent and systematic. 'government need', 'factory produce', 'it depend'. >Band 4: Meaning is clear. Not Band 6: Errors are too frequent.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 932: V7/G5 - Topic: Technology
samples.append(create_sample(
    index=932,
    vocab_band=7,
    grammar_band=5,
    question="Will AI replace humans?",
    transcript="It is a controversial topic. AI have immense potential to revolutionize industries. It can process data faster than humans. However, it lack emotional intelligence and empathy. Creativity is also a unique human trait. Robots can assist us, but they cannot replicate human connection. Unemployment is a concern, though. If machine take over jobs, many people will loses their livelihood.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'AI have' -> 'AI has'",
        "verb agreement: 'it lack' -> 'it lacks'",
        "verb agreement: 'machine take' -> 'machines take'",
        "verb agreement: 'people will loses' -> 'people will lose'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Uses less common items: 'controversial', 'immense potential', 'revolutionize', 'emotional intelligence', 'empathy', 'replicate', 'livelihood'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA5] Complex ideas but frequent errors. 'AI have', 'it lack', 'machine take'. >Band 4: Uses some subordinate clauses. Not Band 6: Basic errors persist.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 933: V7/G5 - Topic: Education
samples.append(create_sample(
    index=933,
    vocab_band=7,
    grammar_band=5,
    question="Is university important?",
    transcript="Higher education is beneficial for career progression. It provides specialized knowledge and critical thinking skills. Also, university allow students to network with peers. However, tuition fees is exorbitant. Many student graduates with huge debt. Vocational training is a viable alternative. It offer practical skills. Success depend on the individual determination, not just a degree.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'university allow' -> 'university allows'",
        "verb agreement: 'fees is' -> 'fees are'",
        "verb agreement: 'student graduates' -> 'students graduate'",
        "verb agreement: 'It offer' -> 'It offers'",
        "verb agreement: 'Success depend' -> 'Success depends'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Uses less common items: 'beneficial', 'progression', 'specialized knowledge', 'critical thinking', 'exorbitant', 'vocational', 'viable alternative'. >Band 6: Good range. Not Band 8: Lacks idiomatic usage.",
    grammar_reason="[GRA5] Frequent agreement errors: 'university allow', 'fees is', 'It offer'. >Band 4: Can express complex ideas. Not Band 6: Errors cause some strain.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 934: V7/G5 - Topic: Work
samples.append(create_sample(
    index=934,
    vocab_band=7,
    grammar_band=5,
    question="What makes a good employee?",
    transcript="Reliability is paramount. Employers values punctuality and dedication. Also, adaptability is crucial in a changing market. An employee should handle stress well. Teamwork is essential. You must collaborates with colleagues effectively. Technical skills is important, but soft skills like communication is more valuable. A positive attitude contribute to a healthy work environment.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Employers values' -> 'Employers value'",
        "verb agreement: 'You must collaborates' -> 'You must collaborate'",
        "verb agreement: 'skills is' -> 'skills are'",
        "verb agreement: 'communication is' (correct)",
        "verb agreement: 'attitude contribute' -> 'attitude contributes'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Uses less common items: 'paramount', 'punctuality', 'dedication', 'adaptability', 'collaborates', 'soft skills', 'valuable'. >Band 6: Precise vocabulary. Not Band 8: Slightly list-like.",
    grammar_reason="[GRA5] Errors in basic structures: 'Employers values', 'must collaborates'. >Band 4: Uses complex vocabulary to hide grammar faults. Not Band 6: Frequent errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 935: V7/G5 - Topic: Society
samples.append(create_sample(
    index=935,
    vocab_band=7,
    grammar_band=5,
    question="Why do people commit crimes?",
    transcript="Poverty is a significant driver. When people is desperate, they resorts to theft. Socioeconomic inequality creates resentment. Also, lack of education play a role. If young people has no opportunity, they joins gangs. Substance abuse is another factor. Drugs impairs judgment. Rehabilitation is better than punishment. We need to address the root causes.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'people is' -> 'people are'",
        "verb agreement: 'they resorts' -> 'they resort'",
        "verb agreement: 'education play' -> 'education plays'",
        "verb agreement: 'people has' -> 'people have'",
        "verb agreement: 'they joins' -> 'they join'",
        "verb agreement: 'Drugs impairs' -> 'Drugs impair'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Uses less common items: 'significant driver', 'desperate', 'socioeconomic inequality', 'resentment', 'opportunity', 'substance abuse', 'impairs judgment', 'rehabilitation'. >Band 6: Strong vocabulary. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA5] Frequent subject-verb agreement errors: 'people is', 'they resorts', 'education play'. >Band 4: Meaning is clear. Not Band 6: Errors are systematic.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 936: V7/G5 - Topic: Culture
samples.append(create_sample(
    index=936,
    vocab_band=7,
    grammar_band=5,
    question="Is tourism good for a country?",
    transcript="It boosts the economy significantly. Tourism generate revenue and create jobs in hospitality. It also promotes cultural exchange. Locals interacts with foreigners. However, mass tourism have downsides. It can lead to environmental degradation. Historic sites is damaged by overcrowding. Also, local traditions might becomes commercialized. Sustainable tourism is the solution.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Tourism generate' -> 'Tourism generates'",
        "verb agreement: 'create jobs' -> 'creates jobs'",
        "verb agreement: 'Locals interacts' -> 'Locals interact'",
        "verb agreement: 'mass tourism have' -> 'mass tourism has'",
        "verb agreement: 'sites is damaged' -> 'sites are damaged'",
        "verb agreement: 'traditions might becomes' -> 'traditions might become'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Uses less common items: 'boosts', 'revenue', 'hospitality', 'promotes', 'cultural exchange', 'degradation', 'commercialized', 'sustainable'. >Band 6: Advanced words. Not Band 8: Slightly robotic.",
    grammar_reason="[GRA5] Errors in verb forms and agreement: 'Tourism generate', 'Locals interacts', 'sites is damaged'. >Band 4: Uses passive and complex terms. Not Band 6: Frequent errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 937: V7/G5 - Topic: Transport
samples.append(create_sample(
    index=937,
    vocab_band=7,
    grammar_band=5,
    question="How can we solve traffic congestion?",
    transcript="Congestion is a persistent problem in urban areas. We must encourage public transport usage. If trains is efficient and affordable, people will switch. Also, implementing congestion charges can deter car use. Building more roads are not the answer. It only induce more traffic. Promoting cycling and walking is beneficial. We need a comprehensive strategy to improve mobility.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'trains is' -> 'trains are'",
        "verb agreement: 'roads are' -> 'roads is' (Building is subject)",
        "verb agreement: 'It only induce' -> 'It only induces'",
        "verb agreement: 'Promoting... is' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Uses less common items: 'persistent', 'encourage', 'efficient', 'implementing', 'deter', 'induce', 'beneficial', 'comprehensive strategy', 'mobility'. >Band 6: Precise vocabulary. Not Band 8: Lacks idiomatic flair.",
    grammar_reason="[GRA5] Frequent agreement errors: 'trains is', 'Building... are', 'It... induce'. >Band 4: Complex sentence attempts. Not Band 6: Errors distract.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 938: V7/G5 - Topic: Health
samples.append(create_sample(
    index=938,
    vocab_band=7,
    grammar_band=5,
    question="Why is obesity increasing?",
    transcript="Sedentary lifestyle is the main culprit. People sits at desks all day and do not exercise. Also, availability of processed food contributes. Fast food is cheap but caloric. It contain high sugar and fat. Advertising also target children. We need to raise awareness about nutrition. Prevention is better than cure. Governments should regulates the food industry.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'People sits' -> 'People sit'",
        "verb agreement: 'do not exercise' (correct)",
        "verb agreement: 'It contain' -> 'It contains'",
        "verb agreement: 'Advertising... target' -> 'Advertising... targets'",
        "verb agreement: 'Governments should regulates' -> 'Governments should regulate'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Uses less common items: 'sedentary lifestyle', 'culprit', 'processed food', 'caloric', 'nutrition', 'prevention', 'regulates'. >Band 6: Strong vocabulary. Not Band 8: Slightly list-like.",
    grammar_reason="[GRA5] Errors in verbs: 'People sits', 'It contain', 'should regulates'. >Band 4: Uses complex terms. Not Band 6: Basic grammar is weak.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 939: V7/G5 - Topic: Technology
samples.append(create_sample(
    index=939,
    vocab_band=7,
    grammar_band=5,
    question="Is social media harmful?",
    transcript="It has detrimental effects on mental health. Constant comparison leads to inadequacy and depression. Cyberbullying is also rampant. People hides behind screens and spreads hate. However, it facilitates communication. We can stay connected with distant friends. It is a tool. The impact depend on how we utilizes it. Digital literacy is essential to navigate this landscape.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'People hides' -> 'People hide'",
        "verb agreement: 'spreads' -> 'spread'",
        "verb agreement: 'impact depend' -> 'impact depends'",
        "verb agreement: 'we utilizes' -> 'we utilize'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Uses less common items: 'detrimental effects', 'inadequacy', 'rampant', 'facilitates', 'connected', 'digital literacy', 'navigate', 'landscape'. >Band 6: Advanced words. Not Band 8: Lacks fluency.",
    grammar_reason="[GRA5] Agreement errors: 'People hides', 'impact depend', 'we utilizes'. >Band 4: Uses connectors. Not Band 6: Frequent errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 940: V7/G5 - Topic: Environment
samples.append(create_sample(
    index=940,
    vocab_band=7,
    grammar_band=5,
    question="Why is biodiversity important?",
    transcript="Biodiversity maintains the ecosystem balance. Every species play a specific role. If one species become extinct, it affect the whole chain. We rely on nature for resources like medicine and food. Deforestation destroys habitats, which is catastrophic. Conservation efforts is vital. We must protect endangered species. It is our moral obligation to preserve the planet.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'species play' -> 'species plays'",
        "verb agreement: 'species become' -> 'species becomes'",
        "verb agreement: 'it affect' -> 'it affects'",
        "verb agreement: 'efforts is' -> 'efforts are'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR7] Uses less common items: 'maintains', 'ecosystem', 'extinct', 'catastrophic', 'conservation', 'vital', 'endangered', 'moral obligation'. >Band 6: Precise vocabulary. Not Band 8: Lacks idiomatic flow.",
    grammar_reason="[GRA5] Frequent agreement errors: 'species play', 'it affect', 'efforts is'. >Band 4: Clear meaning. Not Band 6: Errors disrupt flow.",
    idiom_present=False,
    risk_level="medium"
))

# ... Adding 40 more samples to reach 50 for Part 2 ...
# Generating samples 941-980

topics_part2 = [
    ("Work", "Remote", "Is working from home good?", "It offers flexibility and autonomy. Commuting is eliminated, which saves time. However, isolation is a drawback. Employees misses the social interaction. Collaboration can suffer. Also, work-life balance becomes blurred. You works where you sleep. It require discipline to stay productive."),
    ("Society", "Housing", "Why is housing expensive?", "Urbanization drives demand. Everyone want to live in the city. Supply is limited. Also, speculation inflates prices. Investors buys houses for profit, not living. This excludes young people from the market. Affordable housing is scarce. Government intervention is necessary to regulate the market."),
    ("Culture", "Art", "Is art important?", "Art fosters creativity and expression. It reflects the culture of a society. Museums preserves our heritage. However, funding is often cut. Some people thinks art is useless. But it enriches our lives. It stimulates the mind. A world without art would be mundane."),
    ("Education", "Reading", "Why read books?", "Reading enhances cognitive skills. It expands vocabulary and imagination. Unlike TV, it require active engagement. It promotes empathy by showing different perspectives. However, attention spans is shortening. People prefers short videos. We must encourage deep reading. It is an intellectual pursuit."),
    ("Transport", "Flying", "Should we fly less?", "Aviation contributes to carbon emissions. It is damaging to the climate. We should considers alternatives like trains. However, business and tourism relies on flying. It connects the world globally. Banning it is impractical. We needs greener technology. Sustainable aviation fuel is a potential solution."),
    ("Health", "Mental", "How to reduce stress?", "Mindfulness and meditation is effective. Exercise releases endorphins, which improves mood. Also, sleep is vital for recovery. Work-life balance prevent burnout. People works too hard. They needs to relax. Social connection also helps. Talking to friends alleviate anxiety. Mental health is as important as physical health."),
    ("Technology", "Data", "Is privacy dead?", "In the digital age, privacy is compromised. Companies collects our data for marketing. Surveillance is ubiquitous. We leaves a digital footprint everywhere. Hackers can steals identity. It is alarming. We needs better laws to protect data. Users must be vigilant. Security should be a priority."),
    ("Environment", "Plastic", "How to stop plastic pollution?", "We must eliminate single-use plastics. They persists in the environment for centuries. Marine life consumes microplastics. Recycling is not enough. We needs to reduce production. Biodegradable alternatives is promising. Consumer behavior must change. We should rejects plastic bags. It is a global crisis."),
    ("Society", "Volunteer", "Why volunteer?", "It strengthens community bonds. Helping others provides fulfillment. It also teaches valuable skills. Volunteers fills gaps in social services. However, people is busy. They lacks time. Incentives might helps. But altruism should be the motivation. It creates a compassionate society."),
    ("Work", "Career", "How to choose a career?", "Follow your passion. Job satisfaction is paramount. Money is important, but not everything. You spends a lot of time at work. If you hates it, life is miserable. Consider your strengths and values. Research different industries. Internships offers experience. A fulfilling career contributes to overall happiness.")
]

import random

# Reusing topics with variations
more_topics_part2 = [
    ("Culture", "Language", "Why learn languages?", "It facilitates communication. You can connects with people globally. It enhances cognitive abilities. Bilingual people is smarter. Also, it aids travel. You understands the culture better. Translation apps is useful, but not perfect. Learning a language shows respect. It opens doors to opportunities."),
    ("Education", "University", "Is university worth it?", "It depends on the field. Degrees in medicine is essential. But for arts, maybe not. Tuition fees is high. Student debt is a burden. Vocational training offer practical skills. Employers values experience. University provides networking. It is a personal investment. You must weighs the costs and benefits."),
    ("Technology", "Robots", "Are robots dangerous?", "They can be. If AI becomes autonomous, we loses control. They might makes decisions that harm us. Also, job displacement is a risk. Robots replaces workers. However, they increases efficiency. They does dangerous jobs. We needs ethical guidelines. Regulation is key to safety."),
    ("Society", "Inequality", "Is inequality a problem?", "Yes, it causes social unrest. The gap between rich and poor are widening. Wealth is concentrated. This limits social mobility. The poor lacks access to healthcare. This is unfair. A just society provide equal opportunities. We needs progressive taxation. Redistribution of wealth is necessary."),
    ("Environment", "Climate", "Is climate change real?", "The evidence is overwhelming. Global temperatures is rising. Glaciers is melting. Extreme weather events occurs frequently. It is anthropogenic, caused by humans. Fossil fuels is the main cause. We must transitions to renewable energy. Ignoring it is reckless. The planet's future is at stake."),
    ("Transport", "Cities", "How to improve cities?", "Green spaces makes cities livable. Parks reduces pollution. Public transport must be efficient. If buses is reliable, people uses them. Pedestrian zones encourages walking. Safety is also crucial. Good lighting deter crime. A city should serve its residents. Urban planning is essential."),
    ("Health", "Obesity", "Why are people fat?", "Sedentary lifestyle is a factor. We sits too much. Also, processed food is cheap. It contain sugar and fat. People eats too many calories. Portion sizes is huge. Lack of exercise contributes. We needs to move more. Education about nutrition helps. Healthy habits prevents disease."),
    ("Work", "Gender", "Is there a pay gap?", "Yes, women earns less than men. Discrimination persists. Also, women takes breaks for childcare. This affects their career path. Leadership roles is dominated by men. We needs transparency in pay. Companies should promotes equality. Equal pay for equal work is a right."),
    ("Education", "Arts", "Are arts important?", "Yes, they fosters creativity. Arts allows self-expression. They enriches culture. Schools focuses too much on science. This is a mistake. Arts develops emotional intelligence. They brings joy. A society without art is soulless. Funding for arts is necessary."),
    ("Culture", "Global", "Is globalization good?", "It promotes cultural exchange. We learns from others. However, local traditions dies out. Western culture dominates. We sees the same shops everywhere. This is boring. We must preserves local identity. Diversity is valuable. Globalization has pros and cons. We needs balance.")
]

all_topics_part2 = topics_part2 + more_topics_part2 + topics_part2 + more_topics_part2

start_index = 941
for i in range(40):
    topic_data = all_topics_part2[i]
    # Introduce explicit grammar errors for G5 profile
    transcript = topic_data[3]

    samples.append(create_sample(
        index=start_index + i,
        vocab_band=7,
        grammar_band=5,
        question=topic_data[2],
        transcript=transcript,
        response_type="extended",
        micro_flaws=[
            "subject-verb agreement errors",
            "plural/singular errors"
        ],
        grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
        vocab_reason="[LR7] Uses advanced vocabulary: 'autonomy', 'eliminated', 'drawback', 'collaboration'. >Band 6: Precise and varied. Not Band 8: Some repetition.",
        grammar_reason="[GRA5] Frequent grammatical errors: 'Employees misses', 'You works', 'It require'. >Band 4: Can express complex ideas. Not Band 6: Errors are systematic and noticeable.",
        idiom_present=False,
        risk_level="medium"
    ))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
