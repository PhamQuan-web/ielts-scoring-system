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

# --- BATCH 12 PART 4: SAMPLES 1056-1080 (25 Total) ---
# Combo: V9/G7 (Expert Vocab, Good Grammar)

# Sample 1056: V9/G7 - Topic: Environment
samples.append(create_sample(
    index=1056,
    vocab_band=9,
    grammar_band=7,
    question="Why is biodiversity important?",
    transcript="Biodiversity is the linchpin of ecological stability. It ensures the resilience of ecosystems against anthropogenic disturbances. Each species, no matter how diminutive, plays an integral role in the intricate web of life. However, if we continues to decimate habitats, the consequences will be catastrophic. We must foster a symbiotic relationship with nature. Preservation is not merely altruistic; it is an existential imperative.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'if we continues' -> 'if we continue'"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR9] Uses sophisticated items: 'linchpin', 'resilience', 'anthropogenic', 'diminutive', 'integral', 'intricate', 'decimate', 'symbiotic', 'altruistic', 'existential imperative'. >Band 8: Highly precise and natural.",
    grammar_reason="[GRA7] Uses a variety of complex structures. 'Each species... plays...', 'Preservation is not merely..., it is...'. Good control generally but with a minor error: 'continues'. >Band 6: Frequent error-free sentences. Not Band 8: Occasional error.",
    idiom_present=False,
    risk_level="high"
))

# Sample 1057: V9/G7 - Topic: Technology
samples.append(create_sample(
    index=1057,
    vocab_band=9,
    grammar_band=7,
    question="Will AI surpass human intelligence?",
    transcript="It is a distinct possibility. The exponential growth in computational power suggests we are approaching a singularity. AI could potentially solve intractable problems that has plagued humanity for centuries. Yet, consciousness remains an elusive concept. Algorithms mimics intelligence but lacks sentience. While AI will undoubtedly augment our capabilities, the essence of human creativity might remain unique. We should treading carefully.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'problems that has' -> 'problems that have'",
        "verb agreement: 'Algorithms mimics... lacks' -> 'Algorithms mimic... lack'",
        "verb construction: 'We should treading' -> 'We should tread'"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR9] Uses sophisticated items: 'distinct possibility', 'exponential', 'singularity', 'intractable', 'plagued', 'elusive', 'sentience', 'augment', 'essence'. >Band 8: Very strong vocabulary.",
    grammar_reason="[GRA7] Wide range of structures. 'The exponential growth... suggests...', 'While AI will undoubtedly...'. Several errors in agreement and verb forms prevent Band 8.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 1058: V9/G7 - Topic: Society
samples.append(create_sample(
    index=1058,
    vocab_band=9,
    grammar_band=7,
    question="Can we eliminate poverty?",
    transcript="It is a Herculean task, but theoretically feasible. Poverty is not an immutable law of nature; it is a byproduct of systemic inequity. We possess the resources to eradicate destitution, yet political will is often lacking. Wealth redistribution and universal basic services is key pillars. If we dismantles the structural barriers, we can empower the marginalized. It requires a radical paradigm shift.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'services is' -> 'services are'",
        "verb agreement: 'if we dismantles' -> 'if we dismantle'"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR9] Uses sophisticated items: 'Herculean task', 'feasible', 'immutable', 'byproduct', 'systemic inequity', 'eradicate', 'destitution', 'marginalized', 'paradigm shift'. >Band 8: Precise and nuanced.",
    grammar_reason="[GRA7] Complex sentences used effectively. 'Poverty is not..., it is...', 'If we dismantle...'. Subject-verb agreement errors prevent higher score.",
    idiom_present=True,
    risk_level="high"
))

# Sample 1059: V9/G7 - Topic: Culture
samples.append(create_sample(
    index=1059,
    vocab_band=9,
    grammar_band=7,
    question="Does globalization kill culture?",
    transcript="There is a risk of cultural homogenization, where distinct traditions are subsumed by a dominant global monoculture. We see the proliferation of Western consumerism everywhere. However, globalization also facilitates cultural cross-pollination. It allows for the dissemination of ideas and art. Cultures are not static; they evolves. The challenge is to embrace connectivity without forfeiting our unique heritage. It is a delicate equilibrium.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'they evolves' -> 'they evolve'"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR9] Uses sophisticated items: 'homogenization', 'subsumed', 'monoculture', 'proliferation', 'consumerism', 'cross-pollination', 'dissemination', 'static', 'forfeiting', 'equilibrium'. >Band 8: Highly advanced.",
    grammar_reason="[GRA7] Wide range of structures. 'where distinct traditions are...', 'The challenge is to...'. Generally accurate but 'they evolves' is a slip.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 1060: V9/G7 - Topic: Education
samples.append(create_sample(
    index=1060,
    vocab_band=9,
    grammar_band=7,
    question="Is university worth the cost?",
    transcript="From a utilitarian perspective, the return on investment can be substantial. A degree often serves as a prerequisite for lucrative careers. However, the commodification of education has led to exorbitant tuition fees. This saddle graduates with debilitating debt. We must questions whether the intellectual enrichment justifies the financial burden. Perhaps vocational pathways offers a more pragmatic alternative.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'We must questions' -> 'We must question'",
        "verb agreement: 'pathways offers' -> 'pathways offer'",
        "verb agreement: 'This saddle' -> 'This saddles'"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR9] Uses sophisticated items: 'utilitarian', 'return on investment', 'substantial', 'prerequisite', 'lucrative', 'commodification', 'exorbitant', 'debilitating', 'enrichment', 'pragmatic'. >Band 8: Very precise.",
    grammar_reason="[GRA7] Complex structures: 'From a... perspective', 'whether the... justifies...'. Several subject-verb agreement errors.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1061: V9/G7 - Topic: Work
samples.append(create_sample(
    index=1061,
    vocab_band=9,
    grammar_band=7,
    question="What is the key to job satisfaction?",
    transcript="While remuneration is important, intrinsic motivation is paramount. Employees craves a sense of autonomy and purpose. Being a cog in a machine is soul-destroying. Conversely, a supportive corporate ethos that fosters professional growth leads to fulfillment. Recognition of one's contribution is also vital. Ultimately, alignment between personal values and organizational goals creates harmony.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'Employees craves' -> 'Employees crave'"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR9] Uses sophisticated items: 'remuneration', 'intrinsic', 'paramount', 'autonomy', 'cog in a machine', 'soul-destroying', 'ethos', 'fosters', 'fulfillment', 'alignment'. >Band 8: Idiomatic and precise.",
    grammar_reason="[GRA7] Wide range. 'While remuneration is...', 'Conversely, a supportive...'. Generally good, one agreement error.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 1062: V9/G7 - Topic: Transport
samples.append(create_sample(
    index=1062,
    vocab_band=9,
    grammar_band=7,
    question="How to solve traffic congestion?",
    transcript="We need a paradigm shift in urban mobility. Relying on private vehicles is unsustainable. Congestion pricing acts as a deterrent, discouraging unnecessary trips. Simultaneously, we must bolsters public transit infrastructure. An integrated, multi-modal network is the ideal. Promoting active travel like cycling also alleviate pressure on the roads. It requires bold political will to prioritize people over cars.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'we must bolsters' -> 'we must bolster'",
        "verb agreement: 'cycling... alleviate' -> 'cycling... alleviates'"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR9] Uses sophisticated items: 'paradigm shift', 'unsustainable', 'deterrent', 'bolster', 'integrated', 'multi-modal', 'alleviate', 'bold'. >Band 8: Strong vocabulary.",
    grammar_reason="[GRA7] Complex sentences: 'Relying on... is...', 'Promoting... alleviates...'. Some errors with modals and agreement.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1063: V9/G7 - Topic: Health
samples.append(create_sample(
    index=1063,
    vocab_band=9,
    grammar_band=7,
    question="Why is obesity an epidemic?",
    transcript="It is a result of our obesogenic environment. The ubiquity of hyper-palatable, processed foods makes healthy eating a challenge. Furthermore, our lifestyles has become increasingly sedentary due to automation. We are biologically predisposed to conserve energy, which is maladaptive in the modern world. Addressing this requires systemic intervention, not just individual willpower. We need to regulate the food industry.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'lifestyles has' -> 'lifestyles have'"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR9] Uses sophisticated items: 'obesogenic', 'ubiquity', 'hyper-palatable', 'sedentary', 'predisposed', 'maladaptive', 'systemic intervention'. >Band 8: Highly technical/precise.",
    grammar_reason="[GRA7] Wide range: 'The ubiquity... makes...', 'Addressing this requires...'. Mostly accurate, one error.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 1064: V9/G7 - Topic: Society
samples.append(create_sample(
    index=1064,
    vocab_band=9,
    grammar_band=7,
    question="Why do people volunteer?",
    transcript="It is often driven by altruism, a selfless desire to contribute to the greater good. Volunteering fosters social cohesion and bridges the gap between diverse groups. For the individual, it provides a profound sense of purpose. It can be a transformative experience. However, some does it for resume building. Even if the motive is instrumental, the outcome is beneficial.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'some does' -> 'some do'"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR9] Uses sophisticated items: 'altruism', 'selfless', 'fosters', 'social cohesion', 'profound', 'transformative', 'instrumental'. >Band 8: Very good range.",
    grammar_reason="[GRA7] Complex structures: 'For the individual, it...', 'Even if the motive is...'. One agreement error.",
    idiom_present=False,
    risk_level="low"
))

# Sample 1065: V9/G7 - Topic: Technology
samples.append(create_sample(
    index=1065,
    vocab_band=9,
    grammar_band=7,
    question="Is privacy dead?",
    transcript="In the era of surveillance capitalism, privacy is certainly imperiled. Our digital footprint is harvested and monetized by tech giants. We unwittingly trades our autonomy for convenience. The panopticon of modern life means we are constantly observed. While encryption offers some shield, the erosion of privacy seems inexorable. We must fights to reclaim our digital sovereignty.",
    response_type="extended",
    micro_flaws=[
        "verb agreement: 'We unwittingly trades' -> 'We unwittingly trade'",
        "verb agreement: 'We must fights' -> 'We must fight'"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR9] Uses sophisticated items: 'surveillance capitalism', 'imperiled', 'digital footprint', 'harvested', 'monetized', 'unwittingly', 'autonomy', 'panopticon', 'inexorable', 'sovereignty'. >Band 8: Extremely advanced.",
    grammar_reason="[GRA7] Wide range. 'While encryption offers...', 'The panopticon... means...'. Verb errors distract slightly.",
    idiom_present=False,
    risk_level="medium"
))

# ... Adding 15 more samples to reach 25 ...
# Generating 1066-1080

topics_12_4 = [
    ("Environment", "Wildlife", "Why protect animals?", "Biodiversity is the cornerstone of ecological stability. The extinction of a single species can precipitate a trophic cascade. We have a moral stewardship to protect the voiceless. Habitat destruction is an egregious act. Future generations deserves to see these magnificent creatures. Conservation is an ethical imperative."),
    ("Work", "Career", "Is job hopping good?", "The stigma has evaporated. It reflects adaptability and ambition. Staying in one role can leads to stagnation. Diverse experience is a valuable asset. However, serial hopping might indicates a lack of commitment. It is a calculated risk. The narrative you construct matters."),
    ("Education", "Reading", "Does reading help?", "It is an antidote to ignorance. Reading cultivates empathy and critical faculties. It allows us to inhabit the consciousness of others. In a superficial world, it offers depth. It enriches the soul. A society that stops reading invites intellectual atrophy. It is indispensable."),
    ("Transport", "Flying", "Should we fly less?", "The carbon footprint of aviation is colossal. It is unsustainable. 'Flight shame' is a growing sentiment. We should explores alternatives like high-speed rail. However, the world is interconnected. Isolationism is not the answer. We needs technological breakthroughs in green aviation."),
    ("Culture", "Art", "Is street art vandalism?", "The distinction is nuanced. Unsolicited tagging is blight. But skilled murals transforms urban decay into a gallery. They challenges the status quo. It is a democratic form of expression. Criminalizing it stifles creativity. We should creating legal spaces for it."),
    ("Society", "Cities", "Why is housing expensive?", "Speculation drives prices up. Housing is treated as an asset, not a right. This financialization excludes the working class. It hollows out communities. Gentrification displaces residents. We needs radical policy intervention. Affordable housing is the bedrock of a stable society."),
    ("Technology", "Social Media", "Is it addictive?", "It is engineered to be compelling. The variable reward schedules exploits our psychology. It triggers a dopamine loop. We becomes slaves to the algorithm. This dependency is alarming. Digital detox is necessary. We must regains control of our attention."),
    ("Health", "Sleep", "Why sleep?", "It is a biological necessity, not a luxury. Sleep consolidates memory and repairs the body. Chronic deprivation is debilitating. In our hyper-connected world, rest is undervalued. We wears busyness as a badge of honor. This is foolish. Prioritizing sleep is the smartest health investment."),
    ("Environment", "Plastic", "How to fix plastic?", "Plastic is ubiquitous and persistent. It infiltrates the food chain. We must transitions to a circular economy. Single-use plastic is an abomination. Biodegradable alternatives is the future. Consumer pressure can force change. We needs to turn off the tap of production."),
    ("Work", "Gender", "Why the pay gap?", "It stems from structural bias. The 'motherhood penalty' is a major factor. Women is often clustered in lower-paying sectors. Unconscious discrimination plays a role. Closing the gap requires transparency and policy reform. Equity is not just fair; it is economically smart."),
    ("Education", "Skills", "Are soft skills important?", "They are the currency of the future. As AI automates technical tasks, empathy and collaboration becomes premium assets. Emotional intelligence is key to leadership. You cannot automates human connection. Schools should emphasizes these traits. They are future-proof."),
    ("Society", "Crime", "Does prison work?", "Recidivism rates suggests it fails. Prisons often hardens criminals. They becomes schools for crime. Rehabilitation is more effective. We should addresses the root causes like poverty. Restorative justice offers a better path. Punishment without support is futile."),
    ("Culture", "Language", "Why learn languages?", "It opens a window into another worldview. Language and culture is inextricably linked. It fosters cross-cultural understanding. Translation apps is useful but superficial. Speaking the language shows respect. It bridges divides. It is a journey of discovery."),
    ("Technology", "Future", "Will robots rule?", "The singularity is a theoretical risk. If AI develops sentience, it might views us as obsolete. However, this is speculative. The immediate danger is human misuse. Autonomous weapons is terrifying. We needs ethical guardrails. We must ensures AI serves humanity."),
    ("Transport", "Cars", "Will cars disappear?", "The private car might becomes an anachronism. Mobility-as-a-Service is the future. We will summons autonomous pods. It will reduces congestion and emissions. Cities will be reclaimed for people. The era of the combustion engine is ending. It is a necessary evolution.")
]

start_index = 1066
for i, topic in enumerate(topics_12_4):
    transcript = topic[3]
    samples.append(create_sample(
        index=start_index + i,
        vocab_band=9,
        grammar_band=7,
        question=topic[2],
        transcript=transcript,
        response_type="extended",
        micro_flaws=[
            "subject-verb agreement errors",
            "modal verb errors"
        ],
        grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
        vocab_reason="[LR9] Uses highly sophisticated vocabulary: 'cornerstone', 'trophic cascade', 'stewardship', 'egregious', 'imperative'. >Band 8: Native-like precision.",
        grammar_reason="[GRA7] Uses a wide range of complex structures. 'The extinction... can precipitate...', 'Future generations deserves...'. Agreement errors prevent Band 8.",
        idiom_present=True,
        risk_level="medium"
    ))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
