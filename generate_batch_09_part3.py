import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch09.jsonl")

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

# --- BATCH 09 PART 3: SAMPLES 771-790 (20 Total) ---
# Combo: V9/G8 (Expert Vocab, Very Good Grammar)

# Sample 771: V9/G8 - Topic: Environment (Sustainability)
samples.append(create_sample(
    index=771,
    vocab_band=9,
    grammar_band=8,
    question="Why is sustainable development important?",
    transcript="It is fundamentally about intergenerational equity. We cannot continue to plunder the Earth's resources with reckless abandon, leaving a barren wasteland for our descendants. Sustainability necessitates a holistic paradigm shift, integrating economic viability with ecological stewardship. It is the only way to avert an existential catastrophe. While the transition may be arduous, the alternative—environmental collapse—is simply untenable.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated and natural vocabulary effortlessly: 'intergenerational equity', 'plunder', 'reckless abandon', 'barren wasteland', 'necessitates', 'holistic paradigm shift', 'ecological stewardship', 'existential catastrophe', 'arduous', 'untenable'. >Band 8: Greater precision and stylistic flair.",
    grammar_reason="[GRA8] Wide range: 'We cannot continue to plunder...', 'integrating economic viability...', 'While the transition may be...'. Error-free. >Band 7: Sophisticated structures used flexibly.",
    idiom_present=True,
    risk_level="high"
))

# Sample 772: V9/G8 - Topic: Technology (AI)
samples.append(create_sample(
    index=772,
    vocab_band=9,
    grammar_band=8,
    question="Will AI surpass human intelligence?",
    transcript="It is a scenario that oscillates between utopian dream and dystopian nightmare. While AI possesses unparalleled computational power, it currently lacks the sentient spark that characterizes human consciousness. The concept of 'superintelligence' is theoretically plausible, yet we are still in the nascent stages. If we do cross that Rubicon, we must ensure that artificial values align with human ethics to prevent unintended consequences.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses idiomatic and precise language: 'oscillates', 'utopian', 'dystopian', 'unparalleled', 'sentient spark', 'nascent stages', 'cross that Rubicon', 'unintended consequences'. >Band 8: Highly sophisticated and natural.",
    grammar_reason="[GRA8] Wide range: 'that oscillates between...', 'While AI possesses...', 'If we do cross...'. Majority error-free. >Band 7: High level of accuracy.",
    idiom_present=True,
    risk_level="high"
))

# Sample 773: V9/G8 - Topic: Education (University)
samples.append(create_sample(
    index=773,
    vocab_band=9,
    grammar_band=8,
    question="Is the cost of university education justified?",
    transcript="It is a multifaceted debate with no easy answers. From a purely utilitarian perspective, the return on investment can be substantial, unlocking doors to lucrative careers. However, the commodification of higher education has arguably turned it into a gatekeeper of privilege rather than a vehicle for social mobility. Saddling young minds with exorbitant debt is counterproductive. Education should be an intellectual right, not a financial burden.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated vocabulary naturally: 'multifaceted', 'utilitarian', 'return on investment', 'commodification', 'gatekeeper of privilege', 'social mobility', 'saddling', 'exorbitant', 'intellectual right'. >Band 8: Precise and nuanced.",
    grammar_reason="[GRA8] Wide range: 'From a purely utilitarian perspective...', 'unlocking doors to...', 'rather than a vehicle for...'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=False,
    risk_level="high"
))

# Sample 774: V9/G8 - Topic: Society (Inequality)
samples.append(create_sample(
    index=774,
    vocab_band=9,
    grammar_band=8,
    question="Can we eradicate poverty?",
    transcript="Eradication is an ambitious, perhaps asymptotic, goal. Poverty is not merely a lack of income; it is a systemic deprivation of opportunity and agency. While we have made strides in lifting millions out of destitution, structural inequalities persist. To truly banish poverty, we must dismantle the entrenched systems that perpetuate it. It requires a radical redistribution of resources and a commitment to social justice on a global scale.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses high-level items: 'asymptotic', 'systemic deprivation', 'agency', 'strides', 'destitution', 'entrenched', 'perpetuate', 'radical redistribution'. >Band 8: Very precise and sophisticated.",
    grammar_reason="[GRA8] Wide range: 'not merely..., it is...', 'While we have made...', 'To truly banish poverty, we must...'. Error-free. >Band 7: Complex sentences used effectively.",
    idiom_present=False,
    risk_level="high"
))

# Sample 775: V9/G8 - Topic: Culture (Globalization)
samples.append(create_sample(
    index=775,
    vocab_band=9,
    grammar_band=8,
    question="How can we preserve cultural heritage?",
    transcript="Preservation requires a concerted effort to safeguard the intangible essence of a culture, not just its material artifacts. Language is the vessel of culture; when it dies, a unique worldview vanishes. We must foster an environment where indigenous traditions are not merely museum exhibits but living, breathing practices. In the face of homogenizing globalization, celebrating cultural distinctiveness is an act of resistance and resilience.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated vocabulary: 'concerted effort', 'intangible essence', 'artifacts', 'vessel', 'worldview', 'indigenous', 'homogenizing', 'distinctiveness', 'resistance', 'resilience'. >Band 8: Effortless use of advanced terms.",
    grammar_reason="[GRA8] Wide range: 'not just its...', 'when it dies...', 'where indigenous traditions are not merely...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=True,
    risk_level="high"
))

# Sample 776: V9/G8 - Topic: Work (Job)
samples.append(create_sample(
    index=776,
    vocab_band=9,
    grammar_band=8,
    question="What makes a company successful?",
    transcript="Enduring success transcends the bottom line. It hinges on cultivating a corporate ethos where innovation and integrity are paramount. A company that treats its employees as disposable assets will eventually stagnate. Conversely, one that fosters a culture of inclusivity and empowerment will thrive. Adaptability is also the watchword; in a volatile market, rigidity is a death sentence. Success is a marathon, not a sprint.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'bottom line' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'transcends', 'hinges on', 'ethos', 'paramount', 'disposable assets', 'stagnate', 'inclusivity', 'empowerment', 'watchword', 'volatile', 'rigidity'. Idiom: 'bottom line', 'marathon not a sprint'. >Band 8: Highly idiomatic and precise.",
    grammar_reason="[GRA8] Wide range: 'A company that treats...', 'Conversely, one that fosters...', 'in a volatile market...'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=True,
    risk_level="high"
))

# Sample 777: V9/G8 - Topic: Transport (Cities)
samples.append(create_sample(
    index=777,
    vocab_band=9,
    grammar_band=8,
    question="How will urban transport evolve?",
    transcript="We are standing on the precipice of a mobility revolution. The convergence of electrification, automation, and connectivity will fundamentally reshape our urban arteries. The private car, once a symbol of freedom, may become an anachronism, replaced by on-demand, shared autonomous fleets. This paradigm shift promises to unclog our cities and reclaim streets for people. However, realizing this utopia requires bold policy and infrastructure investment.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'precipice', 'convergence', 'electrification', 'arteries', 'anachronism', 'autonomous fleets', 'paradigm shift', 'unclog', 'utopia'. >Band 8: Precise and nuanced.",
    grammar_reason="[GRA8] Wide range: 'The convergence... will fundamentally reshape...', 'once a symbol of freedom...', 'However, realizing this utopia requires...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=False,
    risk_level="high"
))

# Sample 778: V9/G8 - Topic: Health (Exercise)
samples.append(create_sample(
    index=778,
    vocab_band=9,
    grammar_band=8,
    question="Why do people struggle to maintain a healthy lifestyle?",
    transcript="We are swimming upstream against a current of convenience. Our modern environment is engineered for sedentariness and caloric excess. We are biologically predisposed to conserve energy and seek sugar, instincts that are maladaptive in an era of abundance. Furthermore, the frenetic pace of contemporary life leaves little bandwidth for self-care. Overcoming these systemic inertia requires not just willpower, but a radical redesign of our daily routines.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'swimming upstream' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'engineered', 'sedentariness', 'caloric excess', 'predisposed', 'maladaptive', 'abundance', 'frenetic', 'bandwidth', 'inertia', 'radical redesign'. Idiom: 'swimming upstream'. >Band 8: Highly natural and precise.",
    grammar_reason="[GRA8] Wide range: 'instincts that are maladaptive...', 'leaves little bandwidth for...', 'requires not just..., but...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=True,
    risk_level="high"
))

# Sample 779: V9/G8 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=779,
    vocab_band=9,
    grammar_band=8,
    question="Why is poaching still a problem?",
    transcript="It persists because of the exorbitant profits generated by the illicit wildlife trade. As long as there is a market for ivory or rhino horn, fueled by status-seeking or pseudoscience, the slaughter will continue. Criminal syndicates exploit the poverty of local communities, recruiting poachers with the promise of quick riches. Breaking this cycle requires a holistic approach: crushing the demand while providing sustainable livelihoods for those on the ground.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'exorbitant', 'illicit', 'fueled by', 'pseudoscience', 'slaughter', 'syndicates', 'exploit', 'recruiting', 'holistic', 'livelihoods'. >Band 8: Precise and effective.",
    grammar_reason="[GRA8] Wide range: 'As long as there is...', 'recruiting poachers with...', 'Breaking this cycle requires...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="high"
))

# Sample 780: V9/G8 - Topic: Education (Reading)
samples.append(create_sample(
    index=780,
    vocab_band=9,
    grammar_band=8,
    question="How does reading benefit critical thinking?",
    transcript="Reading is a workout for the intellect. It compels us to suspend judgment and inhabit the mind of another, fostering cognitive empathy. Complex narratives require us to track multiple threads and synthesize information, sharpening our analytical faculties. In a world of soundbites and superficial hot takes, reading trains us to appreciate nuance and ambiguity. It is the antidote to the atrophy of attention.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'compels', 'suspend judgment', 'inhabit', 'cognitive empathy', 'synthesize', 'analytical faculties', 'soundbites', 'superficial', 'nuance', 'ambiguity', 'atrophy'. >Band 8: Very strong vocabulary.",
    grammar_reason="[GRA8] Wide range: 'It compels us to...', 'require us to track...', 'In a world of...'. Error-free. >Band 7: Accurate and varied.",
    idiom_present=False,
    risk_level="high"
))

# Sample 781: V9/G8 - Topic: Technology (Data)
samples.append(create_sample(
    index=781,
    vocab_band=9,
    grammar_band=8,
    question="Is data privacy a lost cause?",
    transcript="It feels like a losing battle in the age of surveillance capitalism. Our digital exhaust is constantly harvested and monetized by tech behemoths. The notion of privacy has been eroded by the convenience of connectivity. However, giving up is not an option. We are seeing a burgeoning awareness and a push for regulatory frameworks like GDPR. Privacy is a fundamental right, and we must fight to reclaim sovereignty over our digital selves.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'losing battle' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'surveillance capitalism', 'digital exhaust', 'harvested', 'monetized', 'behemoths', 'eroded', 'burgeoning', 'regulatory frameworks', 'sovereignty'. Idiom: 'losing battle'. >Band 8: Highly advanced vocabulary.",
    grammar_reason="[GRA8] Wide range: 'which corporations harvest...', 'The notion... has been eroded...', 'We are seeing...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=True,
    risk_level="high"
))

# Sample 782: V9/G8 - Topic: Society (Volunteer)
samples.append(create_sample(
    index=782,
    vocab_band=9,
    grammar_band=8,
    question="Should volunteering be incentivized?",
    transcript="Offering material incentives risks corrupting the very essence of volunteering, which is altruism. If the motivation shifts from intrinsic desire to extrinsic reward, the act loses its moral nobility. However, we should certainly remove barriers to entry. Incentives like academic credit or time off work can validate the contribution without commodifying it. The goal is to facilitate engagement, not to purchase it.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'corrupting', 'essence', 'altruism', 'intrinsic', 'extrinsic', 'nobility', 'validate', 'commodifying', 'facilitate'. >Band 8: Precise and natural.",
    grammar_reason="[GRA8] Wide range: 'risks corrupting...', 'If the motivation shifts...', 'The goal is to...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="high"
))

# Sample 783: V9/G8 - Topic: Culture (Art)
samples.append(create_sample(
    index=783,
    vocab_band=9,
    grammar_band=8,
    question="How does art influence society?",
    transcript="Art is a potent vehicle for social commentary and transformation. It has the capacity to subvert norms and give voice to the marginalized. Through visceral imagery or compelling narrative, art can bypass our intellectual defenses and strike a chord emotionally. It holds a mirror up to society, forcing us to confront uncomfortable truths. It is not just an aesthetic pursuit; it is a moral compass.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'strike a chord' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'potent vehicle', 'subvert norms', 'marginalized', 'visceral', 'bypasses', 'intellectual defenses', 'aesthetic pursuit'. Idioms: 'strike a chord', 'holds a mirror up'. >Band 8: Highly idiomatic.",
    grammar_reason="[GRA8] Wide range: 'It has the capacity to...', 'Through visceral imagery...', 'forcing us to confront...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=True,
    risk_level="high"
))

# Sample 784: V9/G8 - Topic: Work (Gender)
samples.append(create_sample(
    index=784,
    vocab_band=9,
    grammar_band=8,
    question="What obstacles do women face in the workplace?",
    transcript="The 'glass ceiling' is a persistent, invisible barrier. Despite legislative progress, subtle forms of discrimination permeate the workplace. Women often face the double bind of being viewed as either competent but cold, or warm but incompetent. The unequal burden of unpaid domestic labor also creates a 'leaky pipeline' to leadership. Dismantling these structural impediments requires a concerted effort to change corporate culture and societal expectations.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'glass ceiling' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'persistent', 'permeate', 'double bind', 'incompetent', 'unpaid domestic labor', 'leaky pipeline', 'impediments', 'concerted effort'. Idiom: 'glass ceiling'. >Band 8: Very strong vocabulary.",
    grammar_reason="[GRA8] Wide range: 'Despite legislative progress...', 'The unequal burden... also creates...', 'Dismantling... requires...'. Error-free. >Band 7: Complex sentences.",
    idiom_present=True,
    risk_level="high"
))

# Sample 785: V9/G8 - Topic: Transport (Flying)
samples.append(create_sample(
    index=785,
    vocab_band=9,
    grammar_band=8,
    question="Are budget airlines good for the industry?",
    transcript="They have democratized travel, making the world accessible to the masses. This has undeniably stimulated global tourism and cultural exchange. However, this race to the bottom has come at a cost. It has fostered a culture of disposability and entitlement. The environmental toll of cheap flights is staggering. While they have revolutionized mobility, the business model is arguably unsustainable in the face of the climate crisis.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'race to the bottom' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'democratized', 'masses', 'undeniably', 'stimulated', 'disposability', 'entitlement', 'toll', 'staggering', 'revolutionized', 'unsustainable'. Idiom: 'race to the bottom'. >Band 8: Highly natural and precise.",
    grammar_reason="[GRA8] Wide range: 'making the world accessible...', 'However, this race...', 'While they have revolutionized...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=True,
    risk_level="high"
))

# Sample 786: V9/G8 - Topic: Education (Technology)
samples.append(create_sample(
    index=786,
    vocab_band=9,
    grammar_band=8,
    question="Does technology hinder learning?",
    transcript="It is a double-edged sword. While it provides instant access to the sum of human knowledge, it also fosters shallow processing. The constant barrage of notifications fragments our attention, making deep work increasingly difficult. We risk raising a generation of skimmers rather than thinkers. However, if harnessed correctly as a tool for inquiry rather than a distraction, technology can augment our cognitive capabilities. The fault lies not in the tool, but in the usage.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'sum of human knowledge', 'fosters', 'shallow processing', 'barrage', 'fragments', 'skimmers', 'harnessed', 'inquiry', 'augment', 'cognitive capabilities'. >Band 8: Very advanced vocabulary.",
    grammar_reason="[GRA8] Wide range: 'While it provides...', 'making deep work...', 'The fault lies not..., but in...'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=True,
    risk_level="high"
))

# Sample 787: V9/G8 - Topic: Society (Housing)
samples.append(create_sample(
    index=787,
    vocab_band=9,
    grammar_band=8,
    question="Is home ownership a realistic goal for young people?",
    transcript="For the millennial and Gen Z cohorts, it is becoming a mirage. The decoupling of wages from property prices has created an unbridgeable chasm. Housing has morphed from a basic human right into a speculative asset class. This financial exclusion has profound social implications, delaying family formation and eroding community stability. Without radical policy intervention to decompose the housing market, we risk creating a permanent class of renters.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'cohorts', 'mirage', 'decoupling', 'unbridgeable chasm', 'morphed', 'speculative asset', 'exclusion', 'implications', 'eroding', 'decompose'. >Band 8: Highly precise and academic.",
    grammar_reason="[GRA8] Wide range: 'The decoupling... has created...', 'delaying family formation...', 'Without radical policy...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="high"
))

# Sample 788: V9/G8 - Topic: Environment (Trees)
samples.append(create_sample(
    index=788,
    vocab_band=9,
    grammar_band=8,
    question="How can we prevent deforestation?",
    transcript="We need a paradigm shift in how we value nature. Forests must be seen as vital infrastructure, not just timber yards. Implementing strict legal frameworks and enforcing them rigorously is the first step. But we must also address the demand side. Certifying supply chains to ensure they are deforestation-free is crucial. Furthermore, we must empower indigenous communities, who are the most effective guardians of the forest. It requires global solidarity.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'paradigm shift', 'infrastructure', 'timber yards', 'rigorously', 'certifying', 'supply chains', 'empower', 'indigenous', 'guardians', 'solidarity'. >Band 8: Strong vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'Forests must be seen as...', 'Implementing... is the first step', 'who are the most effective...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="high"
))

# Sample 789: V9/G8 - Topic: Technology (Social Media)
samples.append(create_sample(
    index=789,
    vocab_band=9,
    grammar_band=8,
    question="Is social media addictive?",
    transcript="It is designed to be insidiously addictive. Tech companies exploit our neurochemistry, using variable reward schedules to keep us scrolling. The 'like' button triggers a dopamine hit similar to gambling. This constant feedback loop creates a dependency that is hard to break. We are the product, and our attention is being harvested. Recognizing these manipulative mechanics is essential for reclaiming our cognitive autonomy.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'dopamine hit' (collocation)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'insidiously', 'exploit', 'neurochemistry', 'variable reward schedules', 'feedback loop', 'dependency', 'harvested', 'manipulative', 'cognitive autonomy'. >Band 8: Highly technical/precise.",
    grammar_reason="[GRA8] Wide range: 'using variable reward schedules...', 'The 'like' button triggers...', 'Recognizing... is essential'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=True,
    risk_level="high"
))

# Sample 790: V9/G8 - Topic: Work (Job Hopping)
samples.append(create_sample(
    index=790,
    vocab_band=9,
    grammar_band=8,
    question="Does job hopping look bad on a resume?",
    transcript="The stigma surrounding job hopping has largely evaporated. In the modern gig economy, fluidity is the new norm. Employers value adaptability and a diverse portfolio of skills over blind loyalty. Staying in one role for too long can even be perceived as stagnation. However, one must be able to articulate a coherent narrative for the changes. If the moves are strategic rather than impulsive, they demonstrate ambition and agility.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'stigma', 'evaporated', 'fluidity', 'adaptability', 'portfolio', 'blind loyalty', 'stagnation', 'articulate', 'coherent narrative', 'impulsive', 'agility'. >Band 8: Very strong vocabulary.",
    grammar_reason="[GRA8] Wide range: 'Staying in one role... can be perceived...', 'However, one must be able...', 'If the moves are...'. Error-free. >Band 7: Accurate and varied.",
    idiom_present=False,
    risk_level="high"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
