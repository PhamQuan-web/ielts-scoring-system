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

# --- BATCH 03 PART 4: SAMPLES 226-250 (25 Total) ---
# Combo: V6/G5

# Sample 226: V6/G5 - Topic: Technology (Privacy)
samples.append(create_sample(
    index=226,
    vocab_band=6,
    grammar_band=5,
    question="Is online privacy important?",
    transcript="It is essential. Data protection is a major concern. Hackers can steal personal information like credit card details. This lead to identity theft. Also, companies track our online activity. They use it for targeted advertising. This is an invasion of privacy. We must use secure passwords and encryption. If not, we is vulnerable.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'This lead' -> 'This leads'",
        "verb agreement: 'we is' -> 'we are'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'essential', 'data protection', 'concern', 'identity theft', 'targeted advertising', 'invasion of privacy', 'secure', 'encryption', 'vulnerable'. >Band 5: Precise topic words. Not Band 7: Lacks flexibility.",
    grammar_reason="[GRA5] Conditionals: 'If not, we is vulnerable'. Reason: 'like credit card...'. >Band 4: Uses connectors. Not Band 6: Basic verb 'be' error.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 227: V6/G5 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=227,
    vocab_band=6,
    grammar_band=5,
    question="Can individuals make a difference to the environment?",
    transcript="Yes, collective action is powerful. Small changes in lifestyle can have a significant impact. For example, reducing plastic usage. Or conserving water. If everyone participate, the result is huge. We can influence corporations too. By choosing eco-friendly products. Public awareness is growing. We have a responsibility to the planet.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'everyone participate' -> 'everyone participates'",
        "verb agreement: 'result is' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'collective action', 'lifestyle', 'significant impact', 'usage', 'conserving', 'corporations', 'eco-friendly', 'awareness', 'responsibility'. >Band 5: Advanced vocabulary. Not Band 7: Slightly repetitive.",
    grammar_reason="[GRA5] Conditionals: 'If everyone participate...'. Modals: 'Can have', 'Must be'. >Band 4: Complex structures attempted. Not Band 6: Subject-verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 228: V6/G5 - Topic: Society (Crime)
samples.append(create_sample(
    index=228,
    vocab_band=6,
    grammar_band=5,
    question="Is prison the best punishment for criminals?",
    transcript="Not always. For serious offenses like murder, incarceration is necessary. It protects society. But for minor crimes, rehabilitation is better. Community service is a good alternative. It allow offenders to pay back. Prison often fail to reform people. They might learn more criminal behavior inside. The justice system should focus on prevention.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'It allow' -> 'It allows'",
        "verb agreement: 'Prison often fail' -> 'Prisons often fail' or 'Prison often fails'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'offenses', 'incarceration', 'rehabilitation', 'alternative', 'offenders', 'pay back', 'reform', 'criminal behavior', 'justice system', 'prevention'. >Band 5: Strong vocabulary. Not Band 7: Lacks nuance.",
    grammar_reason="[GRA5] Contrast: 'But for minor crimes'. Modals: 'Should focus'. >Band 4: Logical flow. Not Band 6: Frequent verb errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 229: V6/G5 - Topic: Work (Robots)
samples.append(create_sample(
    index=229,
    vocab_band=6,
    grammar_band=5,
    question="What skills are safe from automation?",
    transcript="Soft skills is difficult to automate. Empathy, leadership, and negotiation. These require human connection. Also, creative professions is safe. Artists, writers, and designers. Computers cannot replicate human imagination. Complex problem-solving is another area. Robots follows rules, but humans can think outside the box. Adaptability is key for the future.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Soft skills is' -> 'Soft skills are'",
        "verb agreement: 'professions is' -> 'professions are'",
        "verb agreement: 'Robots follows' -> 'Robots follow'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'automate', 'empathy', 'negotiation', 'professions', 'replicate', 'imagination', 'problem-solving', 'adaptability'. Idiom: 'think outside the box'. >Band 5: Idiom used correctly. Not Band 7: Lacks flexibility.",
    grammar_reason="[GRA5] Contrast: 'but humans can think'. Reason: 'These require...'. >Band 4: Clear reasoning. Not Band 6: Persistent agreement errors.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 230: V6/G5 - Topic: Education (University)
samples.append(create_sample(
    index=230,
    vocab_band=6,
    grammar_band=5,
    question="Should university education be free?",
    transcript="Ideally, yes. Education is a fundamental right. It promotes social mobility. If tuition is free, talent is not wasted. However, funding is a challenge. Universities requires huge budgets. Staff salaries and facilities. Taxpayers might object to higher taxes. A compromise might be scholarships for merit. Or income-based repayment loans.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Universities requires' -> 'Universities require'",
        "fragment: 'Staff salaries and facilities'",
        "fragment: 'Or income-based repayment loans'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'ideally', 'fundamental right', 'social mobility', 'tuition', 'funding', 'budgets', 'taxpayers', 'compromise', 'merit', 'repayment loans'. >Band 5: Advanced vocabulary. Not Band 7: Lacks flow.",
    grammar_reason="[GRA5] Conditionals: 'If tuition is free...'. Contrast: 'However'. >Band 4: Complex structures attempted. Not Band 6: Agreement errors and fragments.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 231: V6/G5 - Topic: Culture (Language)
samples.append(create_sample(
    index=231,
    vocab_band=6,
    grammar_band=5,
    question="What is the best way to learn a language?",
    transcript="Immersion is the most effective method. Living in the country where the language is spoken. You are forced to communicate. Also, consistency is crucial. Practice every day. Using apps or watching movies help. But grammar rules is complicated. You need patience. Making mistakes is part of the learning process.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'watching movies help' -> 'watching movies helps'",
        "verb agreement: 'grammar rules is' -> 'grammar rules are'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'immersion', 'effective method', 'communicate', 'consistency', 'crucial', 'complicated', 'patience', 'learning process'. >Band 5: Good topic words. Not Band 7: Lacks idiomatic expressions.",
    grammar_reason="[GRA5] Relative clause: 'where the language is spoken'. Passive: 'forced to communicate'. >Band 4: Complex forms. Not Band 6: Subject-verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 232: V6/G5 - Topic: Health (Mental)
samples.append(create_sample(
    index=232,
    vocab_band=6,
    grammar_band=5,
    question="How can employers reduce workplace stress?",
    transcript="They should promote work-life balance. Flexible hours is beneficial. Employees can manage personal commitments. Also, create a supportive atmosphere. Open communication is vital. Managers should listen to grievances. Mental health days is a good idea. Allowing staff to recharge. A healthy workforce is more productive. Burnout is costly for companies.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Flexible hours is' -> 'Flexible hours are'",
        "verb agreement: 'days is' -> 'days are'",
        "fragment: 'Allowing staff to recharge'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'promote', 'work-life balance', 'beneficial', 'commitments', 'supportive atmosphere', 'grievances', 'recharge', 'productive', 'burnout', 'costly'. >Band 5: Specific vocabulary. Not Band 7: Lacks natural collocation.",
    grammar_reason="[GRA5] Modals: 'Should promote', 'Can manage'. Reason: 'A healthy workforce...'. >Band 4: Logical flow. Not Band 6: Agreement errors and fragments.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 233: V6/G5 - Topic: Society (Gender)
samples.append(create_sample(
    index=233,
    vocab_band=6,
    grammar_band=5,
    question="Are gender roles changing?",
    transcript="Significantly. Traditional stereotypes is fading. Women are pursuing careers in male-dominated fields. Engineering and politics. Men is taking more domestic responsibilities. Childcare and cooking. This shift is positive. It promotes equality. However, bias still exist. The glass ceiling is real. We have not reached total parity yet.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'stereotypes is' -> 'stereotypes are'",
        "verb agreement: 'Men is' -> 'Men are'",
        "verb agreement: 'bias still exist' -> 'bias still exists'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'significantly', 'stereotypes', 'fading', 'pursuing', 'male-dominated', 'domestic responsibilities', 'equality', 'bias', 'glass ceiling', 'parity'. >Band 5: Very good vocabulary. Not Band 7: Lacks flexibility.",
    grammar_reason="[GRA5] Contrast: 'However'. Reason: 'This shift is positive'. >Band 4: Coherent structure. Not Band 6: Systematic agreement errors.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 234: V6/G5 - Topic: Transport (Cities)
samples.append(create_sample(
    index=234,
    vocab_band=6,
    grammar_band=5,
    question="How will transport change in the future?",
    transcript="Autonomous vehicles is the next big thing. Driverless cars will reduce accidents. Human error is the main cause of crashes. Also, electric vehicles will become standard. To combat pollution. Public transport might become faster. Hyperloop technology is promising. Commuting times will decrease. However, regulation is needed. Safety protocols must be strict.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'vehicles is' -> 'vehicles are'",
        "fragment: 'To combat pollution'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'autonomous vehicles', 'driverless', 'human error', 'crashes', 'standard', 'combat', 'hyperloop', 'promising', 'commuting', 'regulation', 'protocols'. >Band 5: Advanced terms. Not Band 7: Slightly robotic.",
    grammar_reason="[GRA5] Future tense: 'will become', 'will reduce'. Modals: 'must be strict'. >Band 4: Uses future forms. Not Band 6: Agreement errors and fragments.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 235: V6/G5 - Topic: Environment (Animals)
samples.append(create_sample(
    index=235,
    vocab_band=6,
    grammar_band=5,
    question="Is it ethical to keep animals in zoos?",
    transcript="It is a controversial topic. Conservationists argue that zoos protects endangered species. Breeding programs help increase population numbers. It is educational for the public. However, animal rights activists disagrees. Confinement is unnatural. Animals suffer from stress and boredom. Their welfare should be priority. Sanctuaries is a better alternative.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'zoos protects' -> 'zoos protect'",
        "verb agreement: 'activists disagrees' -> 'activists disagree'",
        "verb agreement: 'Sanctuaries is' -> 'Sanctuaries are'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'controversial', 'conservationists', 'endangered species', 'breeding programs', 'educational', 'activists', 'confinement', 'unnatural', 'welfare', 'sanctuaries'. >Band 5: Sophisticated vocabulary. Not Band 7: Lacks idiomatic flow.",
    grammar_reason="[GRA5] Contrast: 'However'. Reason: 'It is a controversial topic'. >Band 4: Logical connectors. Not Band 6: Frequent verb errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 236: V6/G5 - Topic: Technology (Communication)
samples.append(create_sample(
    index=236,
    vocab_band=6,
    grammar_band=5,
    question="Has social media improved relationships?",
    transcript="It has mixed effects. On one hand, it facilitates connection. We can stay in touch with distant friends. Sharing updates is easy. On the other hand, interactions is often superficial. People present a curated version of their lives. It creates envy and insecurity. Face-to-face intimacy is lost. Cyberbullying is also a negative aspect.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'interactions is' -> 'interactions are'",
        "verb agreement: 'People present' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'mixed effects', 'facilitates', 'connection', 'stay in touch', 'superficial', 'curated', 'envy', 'insecurity', 'intimacy', 'cyberbullying'. >Band 5: Precise vocabulary. Not Band 7: Lacks flexibility.",
    grammar_reason="[GRA5] Connectors: 'On one hand... On the other hand'. Passive: 'is lost'. >Band 4: Complex structures. Not Band 6: Verb agreement error.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 237: V6/G5 - Topic: Work (Retirement)
samples.append(create_sample(
    index=237,
    vocab_band=6,
    grammar_band=5,
    question="What challenges do retired people face?",
    transcript="Financial instability is a major concern. Pensions might not cover living expenses. Inflation reduce purchasing power. Also, loss of purpose is common. Work gives structure to life. Without it, people feels useless. Social isolation is another issue. Colleagues was their social circle. Health deterioration also limit their activities.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Inflation reduce' -> 'Inflation reduces'",
        "verb agreement: 'people feels' -> 'people feel'",
        "verb agreement: 'Colleagues was' -> 'Colleagues were'",
        "verb agreement: 'deterioration... limit' -> 'deterioration... limits'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'financial instability', 'pensions', 'living expenses', 'inflation', 'purchasing power', 'structure', 'social isolation', 'social circle', 'deterioration'. >Band 5: Advanced vocabulary. Not Band 7: Somewhat academic.",
    grammar_reason="[GRA5] Reason: 'Without it...'. Contrast: 'Also'. >Band 4: Logical flow. Not Band 6: Systemic agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 238: V6/G5 - Topic: Society (Migration)
samples.append(create_sample(
    index=238,
    vocab_band=6,
    grammar_band=5,
    question="Why do people migrate to other countries?",
    transcript="Economic factors is the primary driver. People seek better employment opportunities and higher wages. Developing nations lacks resources. Political instability is another reason. War and persecution forces people to flee. They seek safety and asylum. Also, quality of life. Healthcare and education is better in developed countries. It is a pursuit of happiness.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'factors is' -> 'factors are'",
        "verb agreement: 'nations lacks' -> 'nations lack'",
        "verb agreement: 'persecution forces' -> 'persecution forces' (correct sing.) or 'War and persecution force' (plural subject)",
        "verb agreement: 'Healthcare... is' -> 'Healthcare... are'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'primary driver', 'employment opportunities', 'wages', 'instability', 'persecution', 'flee', 'asylum', 'developed countries', 'pursuit'. >Band 5: Sophisticated terms. Not Band 7: Lacks natural phrasing.",
    grammar_reason="[GRA5] Reason: 'Political instability is another reason'. List structure. >Band 4: Clear organization. Not Band 6: Subject-verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 239: V6/G5 - Topic: Education (Reading)
samples.append(create_sample(
    index=239,
    vocab_band=6,
    grammar_band=5,
    question="Is reading still important in the digital age?",
    transcript="Absolutely. Reading enhance cognitive function. It improves concentration and vocabulary. Digital content is often fragmented. Short articles and videos. Deep reading requires focus. Books offers in-depth knowledge and analysis. Critical thinking is developed through reading. Even if the medium change, the skill remain essential.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Reading enhance' -> 'Reading enhances'",
        "verb agreement: 'Books offers' -> 'Books offer'",
        "verb agreement: 'medium change' -> 'medium changes'",
        "verb agreement: 'skill remain' -> 'skill remains'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'cognitive function', 'concentration', 'fragmented', 'deep reading', 'in-depth', 'analysis', 'critical thinking', 'medium', 'essential'. >Band 5: Advanced vocabulary. Not Band 7: Lacks flexibility.",
    grammar_reason="[GRA5] Contrast: 'Digital content is... Deep reading requires...'. Conditionals: 'Even if...'. >Band 4: Complex structures. Not Band 6: Frequent verb errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 240: V6/G5 - Topic: Culture (Art)
samples.append(create_sample(
    index=240,
    vocab_band=6,
    grammar_band=5,
    question="Does art have a purpose?",
    transcript="Art serve multiple functions. It is a form of expression. Artists communicate complex emotions and ideas. It provokes thought and reflection. Art also document history. Paintings reflects the society of their time. Furthermore, it is aesthetic. Beauty enriches our lives. Without art, the world would be mundane. It inspire creativity.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Art serve' -> 'Art serves'",
        "verb agreement: 'Art also document' -> 'Art also documents'",
        "verb agreement: 'Paintings reflects' -> 'Paintings reflect'",
        "verb agreement: 'It inspire' -> 'It inspires'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'multiple functions', 'expression', 'communicate', 'provokes', 'reflection', 'document', 'aesthetic', 'enriches', 'mundane', 'creativity'. >Band 5: Precise vocabulary. Not Band 7: Usage is academic.",
    grammar_reason="[GRA5] Conditionals: 'Without art...'. Reason: 'It is a form...'. >Band 4: Logical flow. Not Band 6: Systematic agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 241: V6/G5 - Topic: Technology (Games)
samples.append(create_sample(
    index=241,
    vocab_band=6,
    grammar_band=5,
    question="Are video games art?",
    transcript="I believe they is. Modern games has incredible graphics and soundtracks. The storytelling is immersive. It rival movies and literature. Players is active participants. They make choices that affects the outcome. Game designers are artists. They create worlds and characters. However, some people dismiss it as mere entertainment. This view is outdated.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'they is' -> 'they are'",
        "verb agreement: 'games has' -> 'games have'",
        "verb agreement: 'It rival' -> 'It rivals'",
        "verb agreement: 'Players is' -> 'Players are'",
        "verb agreement: 'choices that affects' -> 'choices that affect'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'incredible graphics', 'soundtracks', 'storytelling', 'immersive', 'rival', 'literature', 'participants', 'outcome', 'dismiss', 'mere', 'outdated'. >Band 5: Strong vocabulary. Not Band 7: Lacks idiomatic flow.",
    grammar_reason="[GRA5] Contrast: 'However'. Reason: 'This view is outdated'. >Band 4: Complex reasoning. Not Band 6: Frequent basic verb errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 242: V6/G5 - Topic: Environment (Global Warming)
samples.append(create_sample(
    index=242,
    vocab_band=6,
    grammar_band=5,
    question="What is the impact of deforestation?",
    transcript="It destroy habitats. Biodiversity is lost. Many species faces extinction. Trees absorbs carbon dioxide. When they are cut, this gas is released. It contribute to the greenhouse effect. Global warming accelerate. Also, soil erosion occur. Floods becomes more frequent. We must preserve forests for climate stability.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'It destroy' -> 'It destroys'",
        "verb agreement: 'species faces' -> 'species face'",
        "verb agreement: 'Trees absorbs' -> 'Trees absorb'",
        "verb agreement: 'It contribute' -> 'It contributes'",
        "verb agreement: 'Global warming accelerate' -> 'Global warming accelerates'",
        "verb agreement: 'erosion occur' -> 'erosion occurs'",
        "verb agreement: 'Floods becomes' -> 'Floods become'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'habitats', 'biodiversity', 'extinction', 'absorbs', 'carbon dioxide', 'released', 'greenhouse effect', 'accelerate', 'erosion', 'stability'. >Band 5: Scientific vocabulary. Not Band 7: Lacks variety.",
    grammar_reason="[GRA5] Cause and Effect: 'It contribute to...'. Time clause: 'When they are cut'. >Band 4: Logical sequence. Not Band 6: Consistent verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 243: V6/G5 - Topic: Society (History)
samples.append(create_sample(
    index=243,
    vocab_band=6,
    grammar_band=5,
    question="Is history relevant to modern life?",
    transcript="Yes, it provides context. Current events is rooted in the past. To understand politics, we must know history. Patterns repeats. For example, economic bubbles and crashes. Leaders can learn from historical figures. Strategies and mistakes. Ignoring history lead to ignorance. It helps us navigate the present.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'events is' -> 'events are'",
        "verb agreement: 'Patterns repeats' -> 'Patterns repeat'",
        "verb agreement: 'Ignoring history lead' -> 'Ignoring history leads'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'context', 'rooted', 'politics', 'patterns', 'bubbles', 'crashes', 'historical figures', 'strategies', 'ignorance', 'navigate'. >Band 5: Sophisticated terms. Not Band 7: Lacks nuance.",
    grammar_reason="[GRA5] Purpose: 'To understand politics'. Reason: 'It helps us...'. >Band 4: Clear structure. Not Band 6: Agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 244: V6/G5 - Topic: Health (Sleep)
samples.append(create_sample(
    index=244,
    vocab_band=6,
    grammar_band=5,
    question="What happens if we don't sleep enough?",
    transcript="Sleep deprivation has serious consequences. Cognitive performance decline. Memory and concentration suffers. It affect mood. People become irritable and anxious. Long-term lack of sleep is linked to chronic diseases. Heart disease and obesity. The body need time to repair itself. Rest is not a luxury, it is a biological necessity.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'performance decline' -> 'performance declines'",
        "verb agreement: 'concentration suffers' (correct singular)",
        "verb agreement: 'It affect' -> 'It affects'",
        "verb agreement: 'body need' -> 'body needs'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'deprivation', 'consequences', 'cognitive performance', 'concentration', 'irritable', 'anxious', 'chronic diseases', 'repair', 'biological necessity'. >Band 5: Medical/formal vocabulary. Not Band 7: Slightly robotic.",
    grammar_reason="[GRA5] Contrast: 'Rest is not a luxury...'. Reason: 'The body need time'. >Band 4: Logical flow. Not Band 6: Verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 245: V6/G5 - Topic: Culture (Global)
samples.append(create_sample(
    index=245,
    vocab_band=6,
    grammar_band=5,
    question="How can we preserve local traditions?",
    transcript="Education is vital. Schools should include cultural studies in the curriculum. Teaching folklore, music, and crafts. Communities should organize festivals. Celebrate local heritage. Elders plays a key role. They must pass down knowledge to the youth. Government support is also needed. Funding for cultural projects. If we value our roots, they will survive.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Elders plays' -> 'Elders play'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'vital', 'curriculum', 'folklore', 'crafts', 'heritage', 'pass down', 'funding', 'roots', 'survive'. >Band 5: Good range. Not Band 7: Lacks idiomatic expressions.",
    grammar_reason="[GRA5] Conditionals: 'If we value...'. Modals: 'Should include', 'Must pass down'. >Band 4: Varied structures. Not Band 6: Minor agreement error.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 246: V6/G5 - Topic: Work (Satisfaction)
samples.append(create_sample(
    index=246,
    vocab_band=6,
    grammar_band=5,
    question="What contributes to job satisfaction?",
    transcript="Beyond salary, recognition is important. Employees wants to feel appreciated. A sense of achievement motivate people. Career progression opportunities is essential. If there is no growth, staff gets bored. Autonomy is also a factor. Being trusted to make decisions. Work relationships matters too. A toxic culture drive people away.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Employees wants' -> 'Employees want'",
        "verb agreement: 'achievement motivate' -> 'achievement motivates'",
        "verb agreement: 'opportunities is' -> 'opportunities are'",
        "verb agreement: 'staff gets' (staff can be plural/singular)",
        "verb agreement: 'relationships matters' -> 'relationships matter'",
        "verb agreement: 'culture drive' -> 'culture drives'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'recognition', 'appreciated', 'achievement', 'progression', 'growth', 'autonomy', 'toxic culture'. >Band 5: Precise vocabulary. Not Band 7: Lacks flow.",
    grammar_reason="[GRA5] Conditionals: 'If there is no growth...'. Reason: 'Employees want to feel...'. >Band 4: Complex structures attempted. Not Band 6: Frequent verb errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 247: V6/G5 - Topic: Technology (Communication)
samples.append(create_sample(
    index=247,
    vocab_band=6,
    grammar_band=5,
    question="Is video calling better than face-to-face?",
    transcript="It is a convenient alternative, but not better. Video calls lacks physical presence. Non-verbal cues is missed. Body language and eye contact. However, for long-distance communication, it is indispensable. It bridge the gap. Business meetings is efficient via video. Saves travel time and cost. But for emotional connection, in-person interaction is superior.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'calls lacks' -> 'calls lack'",
        "verb agreement: 'cues is' -> 'cues are'",
        "verb agreement: 'It bridge' -> 'It bridges'",
        "verb agreement: 'meetings is' -> 'meetings are'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'alternative', 'physical presence', 'non-verbal cues', 'indispensable', 'efficient', 'emotional connection', 'interaction', 'superior'. >Band 5: Advanced vocabulary. Not Band 7: Lacks idiomatic usage.",
    grammar_reason="[GRA5] Contrast: 'However', 'But'. Comparison: 'superior'. >Band 4: Logical structure. Not Band 6: Frequent agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 248: V6/G5 - Topic: Society (Volunteer)
samples.append(create_sample(
    index=248,
    vocab_band=6,
    grammar_band=5,
    question="Should volunteering be mandatory for students?",
    transcript="I oppose mandatory volunteering. It contradict the spirit of volunteering. Which should be voluntary. Forced labor create resentment. Students might view it as a burden. However, schools should encourage participation. Highlight the benefits. Skill development and community service. If students chooses to help, the impact is greater.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'It contradict' -> 'It contradicts'",
        "verb agreement: 'labor create' -> 'labor creates'",
        "verb agreement: 'students chooses' -> 'students choose'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'oppose', 'mandatory', 'contradict', 'voluntary', 'resentment', 'burden', 'encourage', 'participation', 'development'. >Band 5: Sophisticated terms. Not Band 7: Lacks natural flow.",
    grammar_reason="[GRA5] Conditionals: 'If students chooses...'. Modals: 'Should encourage'. >Band 4: Complex forms. Not Band 6: Verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 249: V6/G5 - Topic: Environment (Water)
samples.append(create_sample(
    index=249,
    vocab_band=6,
    grammar_band=5,
    question="How can we solve the water crisis?",
    transcript="Desalination technology is a potential solution. Turning seawater into freshwater. However, it is energy-intensive and expensive. Wastewater recycling is another option. Treating water for reuse. Agriculture consume the most water. Efficient irrigation methods is needed. Drip irrigation. Also, individual conservation matter. We must stop wasting water. It is a finite resource.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Agriculture consume' -> 'Agriculture consumes'",
        "verb agreement: 'methods is' -> 'methods are'",
        "verb agreement: 'conservation matter' -> 'conservation matters'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'desalination', 'potential', 'freshwater', 'energy-intensive', 'wastewater', 'reuse', 'irrigation', 'conservation', 'finite'. >Band 5: Technical vocabulary. Not Band 7: Slightly dry.",
    grammar_reason="[GRA5] Contrast: 'However'. Reason: 'It is a finite resource'. >Band 4: Logical flow. Not Band 6: Agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 250: V6/G5 - Topic: Transport (Safety)
samples.append(create_sample(
    index=250,
    vocab_band=6,
    grammar_band=5,
    question="Why are speed limits important?",
    transcript="They ensures road safety. High speed increase the risk of accidents. Reaction time is reduced. The impact of a crash is more severe. Speed limits protects pedestrians and cyclists. Vulnerable road users. Drivers often ignores the limit. Strict enforcement is necessary. Speed cameras and fines. Saving a few minutes is not worth a life.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'They ensures' -> 'They ensure'",
        "verb agreement: 'speed increase' -> 'speed increases'",
        "verb agreement: 'limits protects' -> 'limits protect'",
        "verb agreement: 'Drivers often ignores' -> 'Drivers often ignore'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "moderate", "flexibility": "low"},
    vocab_reason="[LR6] Uses less common items: 'ensures', 'risk', 'reaction time', 'severe', 'pedestrians', 'vulnerable', 'enforcement', 'fines'. >Band 5: Relevant vocabulary. Not Band 7: Lacks idiomatic expressions.",
    grammar_reason="[GRA5] Reason: 'The impact... is more severe'. Contrast implied. >Band 4: Coherent. Not Band 6: Consistent verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
