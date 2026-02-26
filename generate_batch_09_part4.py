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

# --- BATCH 09 PART 4: SAMPLES 791-810 (20 Total) ---
# Combo: V9/G8

# Sample 791: V9/G8 - Topic: Environment (Sustainability)
samples.append(create_sample(
    index=791,
    vocab_band=9,
    grammar_band=8,
    question="What is the role of renewable energy?",
    transcript="It is the linchpin of a carbon-neutral future. We must transition away from our reliance on fossil fuels, which are finite and ecologically destructive. Harnessing the inexhaustible power of the wind and sun is an imperative, not a choice. While the initial capital expenditure for infrastructure is high, the long-term dividends are immeasurable. It is the only viable pathway to avert climate catastrophe.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'linchpin', 'carbon-neutral', 'reliance', 'ecologically destructive', 'harnessing', 'inexhaustible', 'imperative', 'expenditure', 'dividends', 'viable pathway'. >Band 8: Highly precise and natural.",
    grammar_reason="[GRA8] Wide range: 'We must transition...', 'Harnessing... is an imperative...', 'While the initial...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=False,
    risk_level="high"
))

# Sample 792: V9/G8 - Topic: Society (Media)
samples.append(create_sample(
    index=792,
    vocab_band=9,
    grammar_band=8,
    question="Why is freedom of speech important?",
    transcript="It is the bedrock of a pluralistic society. Without the liberty to dissent, democracy withers. Freedom of speech acts as a safety valve, allowing for the ventilation of grievances. It also fosters a marketplace of ideas where truth can emerge from debate. However, this liberty is not absolute; it does not extend to incitement or hate speech. Balancing these rights is a perennial challenge for legislators.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'bedrock', 'pluralistic', 'dissent', 'withers', 'safety valve', 'ventilation', 'grievances', 'marketplace of ideas', 'incitement', 'perennial'. >Band 8: Very strong vocabulary.",
    grammar_reason="[GRA8] Wide range: 'Without the liberty...', 'allowing for...', 'However, this liberty is not...'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=True,
    risk_level="high"
))

# Sample 793: V9/G8 - Topic: Work (Job)
samples.append(create_sample(
    index=793,
    vocab_band=9,
    grammar_band=8,
    question="How is the gig economy changing work?",
    transcript="It has heralded a paradigm shift in employment. The traditional employer-employee contract is being eroded, replaced by a model of flexibility and precarity. For some, it offers liberation from the 9-to-5 grind. For others, it represents a race to the bottom in terms of wages and security. This atomization of the workforce poses significant challenges for labor rights and social protection systems.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'race to the bottom' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'heralded', 'paradigm shift', 'eroded', 'precarity', 'liberation', 'atomization'. Idiom: 'race to the bottom'. >Band 8: Highly advanced vocabulary.",
    grammar_reason="[GRA8] Wide range: 'replaced by...', 'For some, it offers..., For others...', 'poses significant challenges'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=True,
    risk_level="high"
))

# Sample 794: V9/G8 - Topic: Education (University)
samples.append(create_sample(
    index=794,
    vocab_band=9,
    grammar_band=8,
    question="Is online learning the future?",
    transcript="It is poised to become a dominant modality, but not the sole one. The ubiquity of high-speed internet has democratized access to education. We are seeing a move towards hybrid models that blend digital convenience with the irreplaceable value of face-to-face mentorship. While algorithms can personalize the curriculum, they cannot replicate the serendipitous learning that occurs in a campus environment. The future is blended.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'poised', 'dominant modality', 'ubiquity', 'democratized', 'hybrid models', 'irreplaceable', 'algorithms', 'serendipitous'. >Band 8: Very precise and natural.",
    grammar_reason="[GRA8] Wide range: 'We are seeing a move...', 'While algorithms can...', 'that occurs in...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="high"
))

# Sample 795: V9/G8 - Topic: Culture (Globalization)
samples.append(create_sample(
    index=795,
    vocab_band=9,
    grammar_band=8,
    question="Why do some people resist globalization?",
    transcript="They view it as an existential threat to their cultural sovereignty. The fear is that a tidal wave of foreign influence will wash away local traditions, leaving a bland, homogenized landscape. Economic anxiety also plays a role; globalization is often blamed for job losses and outsourcing. It is a reaction against the perceived loss of control and community cohesion in a rapidly changing world.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'existential threat', 'sovereignty', 'tidal wave', 'homogenized', 'anxiety', 'outsourcing', 'perceived', 'cohesion'. >Band 8: Strong vocabulary.",
    grammar_reason="[GRA8] Wide range: 'The fear is that...', 'leaving a bland...', 'globalization is often blamed for...'. Error-free. >Band 7: Accurate complex sentences.",
    idiom_present=True,
    risk_level="high"
))

# Sample 796: V9/G8 - Topic: Technology (AI)
samples.append(create_sample(
    index=796,
    vocab_band=9,
    grammar_band=8,
    question="Can AI be creative?",
    transcript="It can simulate creativity, but whether it possesses it is a philosophical quagmire. AI can generate art by synthesizing vast datasets, producing novel combinations. Yet, it lacks the subjective experience and emotional impetus that drive human creation. It creates without intent or suffering. Until an algorithm can feel pain or joy, its output remains a hollow mimicry of true art, however technically impressive.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'simulate', 'philosophical quagmire', 'synthesizing', 'novel', 'subjective experience', 'impetus', 'algorithm', 'hollow mimicry'. >Band 8: Very advanced vocabulary.",
    grammar_reason="[GRA8] Wide range: 'but whether it possesses it is...', 'by synthesizing...', 'Until an algorithm can...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=False,
    risk_level="high"
))

# Sample 797: V9/G8 - Topic: Transport (Cities)
samples.append(create_sample(
    index=797,
    vocab_band=9,
    grammar_band=8,
    question="What is the impact of ride-sharing apps?",
    transcript="They have been a disruptive force in urban mobility. By leveraging technology to match supply and demand, they have enhanced convenience. However, they have also circumvented labor laws, creating a precarious workforce. Furthermore, contrary to initial hopes, they have exacerbated congestion in many cities. The challenge now is to regulate these platforms to ensure they complement rather than cannibalize public transport systems.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'disruptive force', 'leveraging', 'enhanced', 'circumvented', 'precarious', 'exacerbated', 'regulate', 'cannibalize'. >Band 8: Highly precise and effective.",
    grammar_reason="[GRA8] Wide range: 'By leveraging...', 'creating a precarious...', 'contrary to initial hopes...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="high"
))

# Sample 798: V9/G8 - Topic: Health (Mental)
samples.append(create_sample(
    index=798,
    vocab_band=9,
    grammar_band=8,
    question="Is mental health treated the same as physical health?",
    transcript="Sadly, a false dichotomy remains. While a broken bone elicits sympathy, a broken mind often elicits judgment or fear. Mental health services are woefully under-resourced compared to somatic medicine. We are slowly dismantling the stigma, but parity is still a distant goal. True health is holistic; we must recognize that the mind and body are not separate entities but an integrated system.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'dichotomy', 'elicits', 'woefully under-resourced', 'somatic', 'dismantling', 'parity', 'holistic', 'integrated'. >Band 8: Very strong vocabulary.",
    grammar_reason="[GRA8] Wide range: 'While a broken bone...', 'compared to...', 'we must recognize that...'. Error-free. >Band 7: Accurate and varied.",
    idiom_present=False,
    risk_level="high"
))

# Sample 799: V9/G8 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=799,
    vocab_band=9,
    grammar_band=8,
    question="Why are invasive species a problem?",
    transcript="They are biological pollutants that wreak havoc on established ecosystems. Introduced often by human error, these species lack natural checks and balances, allowing them to proliferate unchecked. They outcompete indigenous flora and fauna, driving them toward extinction. The economic cost of controlling them is astronomical. It is a cautionary tale about the unintended consequences of human interference in the natural world.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'wreak havoc' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'biological pollutants', 'ecosystems', 'checks and balances', 'proliferate', 'indigenous', 'fauna', 'astronomical', 'cautionary tale', 'interference'. Idiom: 'wreak havoc'. >Band 8: Precise and natural.",
    grammar_reason="[GRA8] Wide range: 'Introduced often by...', 'allowing them to...', 'driving them toward...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=True,
    risk_level="high"
))

# Sample 800: V9/G8 - Topic: Education (Reading)
samples.append(create_sample(
    index=800,
    vocab_band=9,
    grammar_band=8,
    question="Does reading shape our personality?",
    transcript="It shapes our interior landscape profoundly. Literature serves as a simulation of life, allowing us to inhabit the consciousness of others. This cultivates empathy and emotional granularity. By grappling with the moral dilemmas of fictional characters, we refine our own ethical framework. We are not merely consumers of stories; we are transformed by them. As the saying goes, a reader lives a thousand lives.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'interior landscape' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'interior landscape', 'profoundly', 'simulation', 'inhabit', 'cultivates', 'granularity', 'grappling', 'ethical framework'. >Band 8: Highly advanced vocabulary.",
    grammar_reason="[GRA8] Wide range: 'allowing us to inhabit...', 'By grappling with...', 'As the saying goes...'. Error-free. >Band 7: Complex structures.",
    idiom_present=True,
    risk_level="high"
))

# Sample 801: V9/G8 - Topic: Society (Cities)
samples.append(create_sample(
    index=801,
    vocab_band=9,
    grammar_band=8,
    question="Why is urban green space important?",
    transcript="It acts as a vital counterpoint to the concrete jungle. Green spaces are not just aesthetic amenities; they are public health infrastructure. They mitigate the urban heat island effect, filter pollutants, and provide a sanctuary for mental restoration. Furthermore, they function as social equalizers, offering a shared space for all citizens regardless of status. Integrating nature into the urban fabric is essential for a livable city.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'concrete jungle' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'counterpoint', 'aesthetic amenities', 'mitigate', 'urban heat island', 'sanctuary', 'restoration', 'equalizers', 'urban fabric'. Metaphor: 'concrete jungle'. >Band 8: Very strong vocabulary.",
    grammar_reason="[GRA8] Wide range: 'are not just..., they are...', 'offering a shared space...', 'Integrating nature... is essential'. Error-free. >Band 7: Accurate complex sentences.",
    idiom_present=True,
    risk_level="high"
))

# Sample 802: V9/G8 - Topic: Culture (Art)
samples.append(create_sample(
    index=802,
    vocab_band=9,
    grammar_band=8,
    question="Is graffiti vandalism?",
    transcript="The line between vandalism and art is often blurred by intent and permission. Wanton tagging of private property is indefensible, a blight on the community. However, street art can be a potent form of cultural expression and political dissent. It reclaims public space from corporate advertising. When executed with skill, it transforms urban decay into an open-air gallery. It challenges our definitions of ownership and beauty.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'blurred', 'wanton', 'indefensible', 'blight', 'potent', 'dissent', 'reclaims', 'executed', 'decay'. >Band 8: Precise and nuanced.",
    grammar_reason="[GRA8] Wide range: 'is often blurred by...', 'When executed with skill...', 'It challenges our definitions...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="high"
))

# Sample 803: V9/G8 - Topic: Work (Job)
samples.append(create_sample(
    index=803,
    vocab_band=9,
    grammar_band=8,
    question="Is job satisfaction more important than salary?",
    transcript="For long-term psychological well-being, absolutely. While a high salary provides a cushion against hardship, it yields diminishing returns for happiness. To toil in a job that lacks purpose or autonomy is soul-destroying, regardless of the pay. Intrinsic motivation—the joy of the work itself—is a more sustainable fuel than external rewards. A sense of vocation is the ultimate luxury.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'diminishing returns' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'psychological', 'cushion', 'diminishing returns', 'toil', 'autonomy', 'soul-destroying', 'intrinsic', 'sustainable', 'vocation'. >Band 8: Highly idiomatic and precise.",
    grammar_reason="[GRA8] Wide range: 'While a high salary...', 'regardless of the pay', 'is a more sustainable fuel than...'. Error-free. >Band 7: Varied structures.",
    idiom_present=True,
    risk_level="high"
))

# Sample 804: V9/G8 - Topic: Technology (Internet)
samples.append(create_sample(
    index=804,
    vocab_band=9,
    grammar_band=8,
    question="Has the internet empowered people?",
    transcript="It has been the greatest leveler in human history. It has democratized information, allowing the autodidact to rival the academic. It has given a megaphone to the marginalized, catalyzing social movements. However, this power is double-edged; it also empowers demagogues and spreads disinformation. While it has dismantled traditional gatekeepers, it has replaced them with algorithmic ones. True empowerment requires digital literacy.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'leveler', 'democratized', 'autodidact', 'marginalized', 'catalyzing', 'demagogues', 'disinformation', 'dismantled', 'gatekeepers', 'algorithmic'. >Band 8: Very advanced vocabulary.",
    grammar_reason="[GRA8] Wide range: 'allowing the autodidact to...', 'While it has dismantled...', 'It is a tool of...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=False,
    risk_level="high"
))

# Sample 805: V9/G8 - Topic: Environment (Climate)
samples.append(create_sample(
    index=805,
    vocab_band=9,
    grammar_band=8,
    question="Why is biodiversity loss a crisis?",
    transcript="It is an unraveling of the web of life. Ecosystems are resilient but not invincible; they rely on a complex interplay of species. Removing key species triggers a trophic cascade that can lead to system collapse. We are currently presiding over the sixth mass extinction event. This is not just a tragedy for nature; it is a direct threat to human civilization, which depends on these biosphere services.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'unraveling', 'resilient', 'invincible', 'interplay', 'trophic cascade', 'presiding', 'mass extinction', 'biosphere'. >Band 8: Scientific/academic precision.",
    grammar_reason="[GRA8] Wide range: 'Removing key species triggers...', 'which depends on...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="high"
))

# Sample 806: V9/G8 - Topic: Transport (Flying)
samples.append(create_sample(
    index=806,
    vocab_band=9,
    grammar_band=8,
    question="Will we stop flying for leisure?",
    transcript="The wanderlust of the human spirit is difficult to curb. Exploration is in our DNA. However, the ethical calculus of travel is changing. 'Flight shame' is prompting a renaissance of slow travel, like rail. We are likely to see a bifurcation: short-haul flights may vanish, replaced by high-speed trains, while long-haul flights become a rare luxury. We will not stop exploring, but we must explore more lightly.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'ethical calculus' (advanced collocation)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'wanderlust', 'curb', 'ethical calculus', 'renaissance', 'bifurcation', 'vanish', 'rare luxury'. >Band 8: Highly nuanced and precise.",
    grammar_reason="[GRA8] Wide range: 'replaced by...', 'while long-haul flights...', 'We will not stop..., but we must...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=True,
    risk_level="high"
))

# Sample 807: V9/G8 - Topic: Society (Consumerism)
samples.append(create_sample(
    index=807,
    vocab_band=9,
    grammar_band=8,
    question="Why do we buy things we don't need?",
    transcript="We are attempting to satisfy non-material needs with material solutions. Consumer culture is predicated on manufacturing dissatisfaction. Advertisers exploit our insecurities, linking products to concepts of worthiness and belonging. This acquisition offers a fleeting hedonic treadmill; the joy fades, and we crave the next fix. Breaking this cycle requires introspection and a shift towards finding meaning in experiences and relationships rather than objects.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'hedonic treadmill' (psychological term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'predicated', 'dissatisfaction', 'exploit', 'insecurities', 'worthiness', 'acquisition', 'hedonic treadmill', 'introspection'. >Band 8: Very strong vocabulary.",
    grammar_reason="[GRA8] Wide range: 'linking products to...', 'Breaking this cycle requires...', 'rather than objects'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=True,
    risk_level="high"
))

# Sample 808: V9/G8 - Topic: Education (University)
samples.append(create_sample(
    index=808,
    vocab_band=9,
    grammar_band=8,
    question="Should university be free?",
    transcript="If we view education as a public good rather than a private commodity, then yes. Removing tuition fees eliminates the financial barrier to entry, ensuring a meritocracy where talent rises regardless of background. An educated populace yields immense dividends for the economy and democracy. However, this requires a societal commitment to taxation. It is a question of priorities: do we value collective enlightenment enough to pay for it?",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'commodity', 'eliminates', 'barrier to entry', 'meritocracy', 'populace', 'dividends', 'societal commitment', 'enlightenment'. >Band 8: Precise and academic.",
    grammar_reason="[GRA8] Wide range: 'If we view..., then yes', 'ensuring a meritocracy where...', 'It is a question of...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="high"
))

# Sample 809: V9/G8 - Topic: Work (Gender)
samples.append(create_sample(
    index=809,
    vocab_band=9,
    grammar_band=8,
    question="How can we achieve gender equality at work?",
    transcript="It demands the deconstruction of archaic patriarchal structures. We must move beyond tokenism to substantive change. This includes enforcing pay transparency to close the wage gap and destigmatizing paternity leave to share the domestic burden. We need to challenge the unconscious biases that govern recruitment and promotion. True equality will be achieved when gender is no longer a predictor of professional trajectory.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'deconstruction', 'archaic', 'patriarchal', 'tokenism', 'substantive', 'transparency', 'destigmatizing', 'domestic burden', 'predictor', 'trajectory'. >Band 8: Very advanced vocabulary.",
    grammar_reason="[GRA8] Wide range: 'This includes enforcing...', 'that govern recruitment...', 'when gender is no longer...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="high"
))

# Sample 810: V9/G8 - Topic: Culture (Global)
samples.append(create_sample(
    index=810,
    vocab_band=9,
    grammar_band=8,
    question="Is cultural diversity essential?",
    transcript="It is the lifeblood of a resilient society. Homogeneity leads to stagnation, whereas diversity catalyzes innovation through the cross-pollination of ideas. Exposure to different worldviews nurtures empathy and adaptability, traits essential in a globalized era. While navigating cultural differences can be challenging, the friction generates light as well as heat. A diverse society is a rich tapestry, infinitely more interesting than a blank canvas.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'cross-pollination' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR9] Uses sophisticated items: 'lifeblood', 'resilient', 'homogeneity', 'stagnation', 'catalyzes', 'cross-pollination', 'nurtures', 'adaptability', 'friction', 'tapestry'. >Band 8: Highly idiomatic and precise.",
    grammar_reason="[GRA8] Wide range: 'whereas diversity catalyzes...', 'While navigating...', 'infinitely more interesting than...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=True,
    risk_level="high"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
