import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch13.jsonl")

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

# --- BATCH 13 PART 2: SAMPLES 1101-1120 (20 Total) ---
# Combo: V8/G5 (Expert Vocab, Basic Grammar)

# Sample 1101: V8/G5 - Topic: Environment
samples.append(create_sample(
    index=1101,
    vocab_band=8,
    grammar_band=5,
    question="Why is biodiversity important?",
    transcript="Biodiversity is paramount for the ecological balance. It ensure the resilience of the environment. If we loses species, the ecosystem collapse. Every animal play a integral role. For example, bees is crucial for pollination. Without them, agriculture fails. Habitat destruction is a catastrophic problem. We must preserves nature for posterity. It is our moral obligation to protect the planet.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'It ensure' -> 'It ensures'",
        "verb agreement: 'we loses' -> 'we lose'",
        "verb agreement: 'ecosystem collapse' -> 'ecosystem collapses'",
        "verb agreement: 'animal play' -> 'animal plays'",
        "verb agreement: 'bees is' -> 'bees are'",
        "verb agreement: 'We must preserves' -> 'We must preserve'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR8] Uses sophisticated items: 'paramount', 'ecological balance', 'resilience', 'integral role', 'pollination', 'catastrophic', 'posterity', 'moral obligation'. >Band 7: Precise terms. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA5] Frequent agreement errors: 'It ensure', 'we loses', 'ecosystem collapse'. >Band 4: Uses some complex structures. Not Band 6: Errors are systematic.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1102: V8/G5 - Topic: Technology
samples.append(create_sample(
    index=1102,
    vocab_band=8,
    grammar_band=5,
    question="Will AI take our jobs?",
    transcript="Automation is inevitable. It will render many jobs obsolete. However, it also spawn new industries. The workforce need to adapt. Reskilling is essential. While AI excels at repetitive tasks, it lack creativity. Human ingenuity is irreplaceable. We should embraces technology as a tool. It can augment our capabilities. The transition might be turbulent, but innovation drive progress.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'it also spawn' -> 'it also spawns'",
        "verb agreement: 'workforce need' -> 'workforce needs'",
        "verb agreement: 'it lack' -> 'it lacks'",
        "verb agreement: 'We should embraces' -> 'We should embrace'",
        "verb agreement: 'innovation drive' -> 'innovation drives'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR8] Uses sophisticated items: 'inevitable', 'render', 'obsolete', 'spawn', 'reskilling', 'excels', 'ingenuity', 'irreplaceable', 'augment', 'turbulent'. >Band 7: Advanced vocabulary. Not Band 9: Slightly robotic.",
    grammar_reason="[GRA5] Frequent verb errors: 'spawn', 'need', 'lack', 'embraces'. >Band 4: Clear meaning. Not Band 6: Frequent errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1103: V8/G5 - Topic: Education
samples.append(create_sample(
    index=1103,
    vocab_band=8,
    grammar_band=5,
    question="Is university worth the cost?",
    transcript="The exorbitant tuition fees is a deterrent. However, a degree provide a competitive edge. It opens doors to lucrative careers. But many students graduates with debilitating debt. This burden stifle their financial freedom. Vocational training is a pragmatic alternative. It offer tangible skills. Education should be a right, not a privilege. The system need reform to ensure accessibility.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'fees is' -> 'fees are'",
        "verb agreement: 'degree provide' -> 'degree provides'",
        "verb agreement: 'students graduates' -> 'students graduate'",
        "verb agreement: 'burden stifle' -> 'burden stifles'",
        "verb agreement: 'It offer' -> 'It offers'",
        "verb agreement: 'system need' -> 'system needs'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR8] Uses sophisticated items: 'exorbitant', 'deterrent', 'competitive edge', 'lucrative', 'debilitating', 'stifle', 'pragmatic', 'tangible', 'accessibility'. >Band 7: Strong vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA5] Systematic agreement errors: 'fees is', 'degree provide', 'It offer'. >Band 4: Uses complex vocabulary to carry meaning. Not Band 6: Frequent errors.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 1104: V8/G5 - Topic: Society
samples.append(create_sample(
    index=1104,
    vocab_band=8,
    grammar_band=5,
    question="Why is inequality increasing?",
    transcript="The disparity between the affluent and the destitute is widening. Wealth accumulation at the top is staggering. This create social stratification. The marginalized lacks opportunities for mobility. Systemic bias perpetuate the cycle of poverty. We needs equitable policies. Redistribution of wealth is controversial but necessary. A cohesive society depend on fairness. If we ignores this, unrest will follow.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'accumulation... is' (correct)",
        "verb agreement: 'This create' -> 'This creates'",
        "verb agreement: 'marginalized lacks' -> 'marginalized lack'",
        "verb agreement: 'bias perpetuate' -> 'bias perpetuates'",
        "verb agreement: 'We needs' -> 'We need'",
        "verb agreement: 'society depend' -> 'society depends'",
        "verb agreement: 'we ignores' -> 'we ignore'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR8] Uses sophisticated items: 'disparity', 'affluent', 'destitute', 'accumulation', 'staggering', 'stratification', 'mobility', 'systemic', 'perpetuate', 'equitable', 'cohesive'. >Band 7: Precise terms. Not Band 9: Slightly formal.",
    grammar_reason="[GRA5] Frequent agreement errors: 'This create', 'marginalized lacks', 'We needs'. >Band 4: Complex ideas. Not Band 6: Errors disrupt flow.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1105: V8/G5 - Topic: Work
samples.append(create_sample(
    index=1105,
    vocab_band=8,
    grammar_band=5,
    question="What makes a good leader?",
    transcript="A leader must possesses integrity and vision. They inspires the team to achieve excellence. Empathy is also a vital trait. A leader who listen foster loyalty. They must makes tough decisions. Resilience in the face of adversity is crucial. It is not about authority, but influence. A true leader empower others. They leads by example.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'leader must possesses' -> 'leader must possess'",
        "verb agreement: 'They inspires' -> 'They inspire'",
        "verb agreement: 'leader who listen' -> 'leader who listens'",
        "verb agreement: 'listen foster' -> 'listens fosters'",
        "verb agreement: 'must makes' -> 'must make'",
        "verb agreement: 'leader empower' -> 'leader empowers'",
        "verb agreement: 'They leads' -> 'They lead'"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR8] Uses sophisticated items: 'integrity', 'vision', 'excellence', 'vital trait', 'adversity', 'authority', 'influence', 'empower'. >Band 7: Strong vocabulary. Not Band 9: Lacks idiomatic usage.",
    grammar_reason="[GRA5] Systematic errors in verbs: 'must possesses', 'They inspires', 'must makes'. >Band 4: Clear meaning. Not Band 6: Frequent errors.",
    idiom_present=False,
    risk_level="medium"
))

# Generating 1106-1120 with explicit reasoning and flaws
topics_13_2 = [
    {
        "question": "Is globalization good?",
        "transcript": "It facilitates cultural exchange. We becomes more cosmopolitan. However, it can leads to homogenization. Local traditions is overshadowed by dominant cultures. We risks losing our distinctiveness. It is a complex phenomenon. We should embraces diversity while preserving our heritage. Cultural imperialism is a threat. We must safeguards our identity.",
        "micro_flaws": ["verb error: 'We becomes' (S-V)", "verb error: 'can leads' (modal)", "verb error: 'traditions is' (S-V)", "verb error: 'We risks' (S-V)", "verb error: 'should embraces' (modal)", "verb error: 'must safeguards' (modal)"],
        "vocab_reason": "[LR8] Vocab: 'facilitates', 'cosmopolitan', 'homogenization', 'overshadowed', 'distinctiveness', 'phenomenon', 'imperialism'. >Band 7: Precise. Not Band 9: Slightly unnatural.",
        "grammar_reason": "[GRA5] Errors: 'becomes', 'leads' (after can), 'is' (plural subject), 'risks', 'embraces', 'safeguards'. >Band 4: Meaning clear. Not Band 6: Systematic errors."
    },
    {
        "question": "How to fix traffic?",
        "transcript": "Congestion is a perennial problem. We must incentivizes public transport. If trains is efficient, people switches from cars. Implementing congestion charges deter drivers. Urban sprawl exacerbates the issue. We needs smart city planning. Promoting cycling is also beneficial. It alleviate pressure on the roads.",
        "micro_flaws": ["verb error: 'must incentivizes' (modal)", "verb error: 'trains is' (S-V)", "verb error: 'people switches' (S-V)", "verb error: 'charges deter' (correct)", "verb error: 'We needs' (S-V)", "verb error: 'It alleviate' (S-V)"],
        "vocab_reason": "[LR8] Vocab: 'congestion', 'perennial', 'incentivizes', 'urban sprawl', 'exacerbates', 'smart city planning', 'alleviate'. >Band 7: Advanced. Not Band 9: Formulaic.",
        "grammar_reason": "[GRA5] Errors: 'incentivizes', 'is' (plural), 'switches', 'needs', 'alleviate'. >Band 4: Complex words but grammar fails. Not Band 6: Frequent errors."
    },
    {
        "question": "Why eat healthy?",
        "transcript": "Nutrition is the foundation of well-being. Processed foods is laden with preservatives. They contributes to the obesity epidemic. A balanced diet boost the immune system. We should consumes whole foods. Hydration is also paramount. What we eats affects our physical and mental state. Prevention is better than cure.",
        "micro_flaws": ["verb error: 'foods is' (S-V)", "verb error: 'contributes' (S-V)", "verb error: 'diet boost' (S-V)", "verb error: 'should consumes' (modal)", "verb error: 'we eats' (S-V)"],
        "vocab_reason": "[LR8] Vocab: 'nutrition', 'foundation', 'processed foods', 'preservatives', 'obesity epidemic', 'immune system', 'hydration', 'paramount'. >Band 7: High level. Not Band 9: Rigid.",
        "grammar_reason": "[GRA5] Errors: 'is' (plural), 'contributes', 'boost', 'consumes', 'eats'. >Band 4: Clear. Not Band 6: Systematic errors."
    },
    {
        "question": "Is privacy dead?",
        "transcript": "In the digital age, privacy is compromised. Companies collects our data for marketing. Surveillance is ubiquitous. We leaves a digital footprint everywhere. Hackers can steals identity. It is alarming. We needs better laws to protect data. Users must be vigilant. Security should be a priority.",
        "micro_flaws": ["verb error: 'Companies collects' (S-V)", "verb error: 'We leaves' (S-V)", "verb error: 'can steals' (modal)", "verb error: 'We needs' (S-V)"],
        "vocab_reason": "[LR8] Vocab: 'compromised', 'surveillance', 'ubiquitous', 'digital footprint', 'vigilant', 'priority'. >Band 7: Sophisticated. Not Band 9: Slightly repetitive.",
        "grammar_reason": "[GRA5] Errors: 'collects', 'leaves', 'steals', 'needs'. >Band 4: Uses complex terms. Not Band 6: Basic grammar errors."
    },
    {
        "question": "How to stop plastic?",
        "transcript": "We must eliminate single-use plastics. They persists in the environment for centuries. Marine life consumes microplastics. Recycling is not enough. We needs to reduce production. Biodegradable alternatives is promising. Consumer behavior must change. We should rejects plastic bags. It is a global crisis.",
        "micro_flaws": ["verb error: 'They persists' (S-V)", "verb error: 'We needs' (S-V)", "verb error: 'alternatives is' (S-V)", "verb error: 'should rejects' (modal)"],
        "vocab_reason": "[LR8] Vocab: 'eliminate', 'single-use plastics', 'marine life', 'microplastics', 'biodegradable', 'alternatives', 'crisis'. >Band 7: Precise. Not Band 9: Functional.",
        "grammar_reason": "[GRA5] Errors: 'persists', 'needs', 'is' (plural), 'rejects'. >Band 4: Understandable. Not Band 6: High error rate."
    },
    {
        "question": "Why volunteer?",
        "transcript": "It cultivates civic duty and altruism. By dedicating time, individuals makes a tangible difference. It strengthens the social fabric. Volunteers fills gaps in services. It is a mutually beneficial endeavor. The volunteer gain perspective and skills. Society becomes more compassionate. It is a noble pursuit.",
        "micro_flaws": ["verb error: 'individuals makes' (S-V)", "verb error: 'Volunteers fills' (S-V)", "verb error: 'volunteer gain' (S-V)"],
        "vocab_reason": "[LR8] Vocab: 'cultivates', 'civic duty', 'altruism', 'tangible difference', 'social fabric', 'mutually beneficial', 'compassionate', 'noble pursuit'. >Band 7: Excellent. Not Band 9: Stiff.",
        "grammar_reason": "[GRA5] Errors: 'makes', 'fills', 'gain'. >Band 4: Meaning conveyed via vocab. Not Band 6: Basic errors."
    },
    {
        "question": "How to choose a job?",
        "transcript": "Follow your vocation. Intrinsic motivation is more sustainable than extrinsic rewards. Job satisfaction stems from a sense of purpose. A toxic environment is detrimental to health. You should seeks a role that aligns with your values. Professional development is also important. A fulfilling career contributes to happiness.",
        "micro_flaws": ["verb error: 'should seeks' (modal)"],
        "vocab_reason": "[LR8] Vocab: 'vocation', 'intrinsic motivation', 'sustainable', 'extrinsic rewards', 'toxic environment', 'detrimental', 'aligns', 'fulfilling'. >Band 7: Advanced. Not Band 9: Academic tone.",
        "grammar_reason": "[GRA5] Errors: 'seeks'. (Note: fewer errors in this sample, but 'seeks' is a major one). >Band 4: Complex sentence attempt. Not Band 6: Error in modal."
    },
    {
        "question": "Is reading good?",
        "transcript": "It enhances cognitive faculties. Reading complex texts stimulate the brain. It expands our lexicon. Fiction fosters empathy by allowing us to inhabit other minds. In an era of short attention spans, deep reading is a dying art. We must encourages children to read. It is food for the soul.",
        "micro_flaws": ["verb error: 'texts stimulate' (correct)", "verb error: 'must encourages' (modal)"],
        "vocab_reason": "[LR8] Vocab: 'enhances', 'cognitive faculties', 'lexicon', 'fosters empathy', 'inhabit', 'dying art'. >Band 7: Sophisticated. Not Band 9: Slightly flowery.",
        "grammar_reason": "[GRA5] Errors: 'encourages' (after must). >Band 4: Uses complex terms. Not Band 6: Basic error."
    },
    {
        "question": "Is flying bad?",
        "transcript": "Aviation is a significant contributor to carbon emissions. It exacerbates climate change. 'Flight shame' is a growing phenomenon. We should considers alternatives like high-speed rail. However, flying connects the world. It facilitates trade and tourism. We needs greener aviation technology.",
        "micro_flaws": ["verb error: 'should considers' (modal)", "verb error: 'We needs' (S-V)"],
        "vocab_reason": "[LR8] Vocab: 'aviation', 'contributor', 'carbon emissions', 'exacerbates', 'phenomenon', 'facilitates'. >Band 7: Precise. Not Band 9: Functional.",
        "grammar_reason": "[GRA5] Errors: 'considers', 'needs'. >Band 4: Clear. Not Band 6: Recurring errors."
    },
    {
        "question": "How to reduce stress?",
        "transcript": "Mindfulness is effective. Exercise releases endorphins, which improves mood. Also, sleep is vital for recovery. Work-life balance prevent burnout. People works too hard. They needs to relax. Social connection also helps. Talking to friends alleviate anxiety. Mental health is paramount.",
        "micro_flaws": ["verb error: 'balance prevent' (S-V)", "verb error: 'People works' (S-V)", "verb error: 'They needs' (S-V)", "verb error: 'friends alleviate' (S-V)"],
        "vocab_reason": "[LR8] Vocab: 'mindfulness', 'endorphins', 'vital', 'recovery', 'burnout', 'alleviate', 'paramount'. >Band 7: High level. Not Band 9: List-like.",
        "grammar_reason": "[GRA5] Errors: 'prevent', 'works', 'needs', 'alleviate'. >Band 4: Good vocab. Not Band 6: Grammar fails."
    },
    {
        "question": "Will robots rule?",
        "transcript": "The singularity is a theoretical risk. If AI develops sentience, it might views us as obsolete. However, this is speculative. The immediate danger is human misuse. Autonomous weapons is terrifying. We needs ethical guardrails. We must ensures AI serves humanity. Control is essential.",
        "micro_flaws": ["verb error: 'might views' (modal)", "verb error: 'weapons is' (S-V)", "verb error: 'We needs' (S-V)", "verb error: 'must ensures' (modal)"],
        "vocab_reason": "[LR8] Vocab: 'singularity', 'theoretical risk', 'sentience', 'obsolete', 'speculative', 'autonomous weapons', 'guardrails'. >Band 7: Very advanced. Not Band 9: Robotic.",
        "grammar_reason": "[GRA5] Errors: 'views', 'is' (plural), 'needs', 'ensures'. >Band 4: Complex thought. Not Band 6: Basic errors."
    },
    {
        "question": "Is art necessary?",
        "transcript": "Art is a reflection of the human condition. It provokes thought and challenge the status quo. It is not a luxury, but a necessity. It nurtures the soul. A society without art is culturally impoverished. Funding for the arts is essential. It is an investment in our humanity.",
        "micro_flaws": ["verb error: 'challenge' (S-V)"],
        "vocab_reason": "[LR8] Vocab: 'reflection', 'human condition', 'provokes', 'status quo', 'necessity', 'nurtures', 'culturally impoverished'. >Band 7: Sophisticated. Not Band 9: Flowery.",
        "grammar_reason": "[GRA5] Errors: 'challenge' (It... challenge). >Band 4: Meaning clear. Not Band 6: Agreement error."
    },
    {
        "question": "Why is rent high?",
        "transcript": "Gentrification is a major factor. Wealthy people moves into neighborhoods, driving up prices. Speculation also plays a role. Housing is treated as an asset, not a right. This displaces long-term residents. Affordability is a crisis. We needs rent control and social housing.",
        "micro_flaws": ["verb error: 'people moves' (S-V)", "verb error: 'We needs' (S-V)"],
        "vocab_reason": "[LR8] Vocab: 'gentrification', 'speculation', 'asset', 'displaces', 'residents', 'affordability', 'social housing'. >Band 7: Precise. Not Band 9: Standard.",
        "grammar_reason": "[GRA5] Errors: 'moves', 'needs'. >Band 4: Clear. Not Band 6: Errors persist."
    },
    {
        "question": "Are soft skills key?",
        "transcript": "They are indispensable. Communication and collaboration is key. Technical skills can be automated, but empathy cannot. Emotional intelligence allow us to navigate complex social situations. Employers values these traits. Schools should integrates them into the curriculum. They are future-proof.",
        "micro_flaws": ["verb error: 'collaboration is' (plural subject)", "verb error: 'intelligence allow' (S-V)", "verb error: 'Employers values' (S-V)", "verb error: 'should integrates' (modal)"],
        "vocab_reason": "[LR8] Vocab: 'indispensable', 'collaboration', 'automated', 'emotional intelligence', 'navigate', 'curriculum', 'future-proof'. >Band 7: Advanced. Not Band 9: Buzzwords.",
        "grammar_reason": "[GRA5] Errors: 'is', 'allow', 'values', 'integrates'. >Band 4: Meaning clear. Not Band 6: Frequent errors."
    },
    {
        "question": "Is it too late?",
        "transcript": "The window of opportunity is closing. We faces an existential threat. Immediate action is imperative. We must transitions to renewable energy. Fossil fuels is the enemy. If we delays, the consequences will be catastrophic. We needs a global effort. Hope is not lost, but time is short.",
        "micro_flaws": ["verb error: 'We faces' (S-V)", "verb error: 'must transitions' (modal)", "verb error: 'fuels is' (S-V)", "verb error: 'we delays' (S-V)", "verb error: 'We needs' (S-V)"],
        "vocab_reason": "[LR8] Vocab: 'window of opportunity', 'existential threat', 'imperative', 'renewable energy', 'catastrophic'. >Band 7: High level. Not Band 9: Dramatic.",
        "grammar_reason": "[GRA5] Errors: 'faces', 'transitions', 'is' (plural), 'delays', 'needs'. >Band 4: Clear. Not Band 6: High error rate."
    }
]

start_index = 1106
for i, item in enumerate(topics_13_2):
    samples.append(create_sample(
        index=start_index + i,
        vocab_band=8,
        grammar_band=5,
        question=item["question"],
        transcript=item["transcript"],
        response_type="extended",
        micro_flaws=item["micro_flaws"],
        grammar_profile={"complexity": "moderate", "accuracy": "low", "flexibility": "low"},
        vocab_reason=item["vocab_reason"],
        grammar_reason=item["grammar_reason"],
        idiom_present=False,
        risk_level="medium"
    ))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
