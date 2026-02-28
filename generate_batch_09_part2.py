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

# --- BATCH 09 PART 2: SAMPLES 751-770 (20 Total) ---
# Combo: V8/G9

# Sample 751: V8/G9 - Topic: Culture (Language)
samples.append(create_sample(
    index=751,
    vocab_band=8,
    grammar_band=9,
    question="Can language shape our thoughts?",
    transcript="This is known as linguistic relativity. The vocabulary we possess frames our perception of reality. For instance, if a language has multiple words for 'snow', speakers might perceive nuances that others miss. Language is not merely a tool for communication; it is a lens through which we interpret the world. Therefore, learning a new language fundamentally expands one's cognitive horizons.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'linguistic relativity', 'frames', 'perception', 'nuances', 'interpret', 'fundamentally', 'cognitive horizons'. >Band 7: Advanced vocabulary. Not Band 9: Slightly academic.",
    grammar_reason="[GRA9] Full range of structures used with complete accuracy. 'The vocabulary we possess frames...', 'if a language has..., speakers might...', 'not merely..., it is...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 752: V8/G9 - Topic: Society (Volunteering)
samples.append(create_sample(
    index=752,
    vocab_band=8,
    grammar_band=9,
    question="What is the impact of corporate volunteering?",
    transcript="It can be mutually beneficial. For the community, it provides much-needed resources and manpower. For the company, it bolsters their corporate social responsibility (CSR) profile and enhances employee engagement. However, it must be genuine, not just a PR stunt. If employees are coerced into volunteering, it breeds resentment. When done authentically, it strengthens the bond between business and society.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'PR stunt' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'mutually beneficial', 'manpower', 'bolsters', 'corporate social responsibility', 'engagement', 'coerced', 'breeds', 'authentically'. Idiom: 'PR stunt'. >Band 7: Strong vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA9] Full range of structures used effectively. 'For the community..., For the company...', 'However, it must be...', 'When done authentically...'. Error-free.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 753: V8/G9 - Topic: Environment (Water)
samples.append(create_sample(
    index=753,
    vocab_band=8,
    grammar_band=9,
    question="Why is water scarcity a growing problem?",
    transcript="It is a convergence of factors. Climate change is altering precipitation patterns, leading to prolonged droughts. Simultaneously, population growth and industrialization are driving up demand. We are depleting aquifers faster than they can replenish. Contamination of existing water sources further exacerbates the crisis. Unless we implement sustainable water management strategies immediately, we face a future of conflict over this precious resource.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'convergence', 'precipitation', 'prolonged', 'industrialization', 'depleting', 'aquifers', 'replenish', 'exacerbates'. >Band 7: Precise terms. Not Band 9: Slightly formal.",
    grammar_reason="[GRA9] Full range of structures used with precision. 'leading to...', 'driving up...', 'faster than they can...', 'Unless we implement...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 754: V8/G9 - Topic: Transport (Safety)
samples.append(create_sample(
    index=754,
    vocab_band=8,
    grammar_band=9,
    question="Will autonomous vehicles eliminate accidents?",
    transcript="They will undoubtedly reduce them drastically. Human error, such as fatigue or distraction, accounts for the vast majority of collisions. Autonomous systems are vigilant and can react faster than any human. However, eliminate is a strong word. Technical glitches or cyber-attacks remain potential threats. While the roads will become significantly safer, a zero-accident future might be an unattainable ideal.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'undoubtedly', 'drastically', 'fatigue', 'collisions', 'vigilant', 'glitches', 'potential threats', 'unattainable'. >Band 7: Advanced vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA9] Full range of structures used effortlessly. 'Human error, such as...', 'accounts for...', 'While the roads will become...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 755: V8/G9 - Topic: Education (Arts)
samples.append(create_sample(
    index=755,
    vocab_band=8,
    grammar_band=9,
    question="Why are arts programs the first to be cut?",
    transcript="They are often perceived as non-essential frills. In an education system obsessed with standardized testing and measurable outcomes, the arts are difficult to quantify. Policy makers prioritize STEM subjects, viewing them as directly linked to economic productivity. This utilitarian approach undervalues the intangible benefits of art, such as fostering creativity and emotional intelligence. It is a short-sighted strategy that stifles holistic development.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'perceived', 'non-essential', 'standardized testing', 'measurable', 'quantify', 'prioritize', 'utilitarian', 'intangible', 'stifles'. >Band 7: Strong vocabulary. Not Band 9: Slightly robotic.",
    grammar_reason="[GRA9] Full range of structures used with accuracy. 'In an education system...', 'viewing them as...', 'It is a short-sighted strategy that...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 756: V8/G9 - Topic: Technology (Space)
samples.append(create_sample(
    index=756,
    vocab_band=8,
    grammar_band=9,
    question="Is space tourism ethical?",
    transcript="It raises significant ethical questions. While it represents a triumph of engineering, the carbon footprint of a rocket launch is colossal. It seems indulgent for the ultra-wealthy to burn massive amounts of fuel for a few minutes of weightlessness, while the planet faces a climate crisis. Unless the industry can decarbonize, space tourism remains a frivolous luxury that the Earth cannot afford.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'triumph', 'carbon footprint', 'colossal', 'indulgent', 'ultra-wealthy', 'weightlessness', 'decarbonize', 'frivolous'. >Band 7: Precise terms. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA9] Full range of structures used naturally. 'While it represents...', 'It seems indulgent for... to...', 'Unless the industry can...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 757: V8/G9 - Topic: Society (Media)
samples.append(create_sample(
    index=757,
    vocab_band=8,
    grammar_band=9,
    question="How does the media shape public opinion?",
    transcript="The media acts as a gatekeeper of information. By selecting which stories to highlight and how to frame them, they influence what the public thinks about. This 'agenda-setting' power is immense. Furthermore, the rise of partisan news outlets reinforces existing biases, creating echo chambers. Critical consumption of media is essential to avoid being manipulated by narratives designed to provoke rather than inform.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'gatekeeper', 'frame', 'agenda-setting', 'partisan', 'outlets', 'reinforces', 'echo chambers', 'manipulated', 'narratives'. >Band 7: Very strong vocabulary. Not Band 9: Slightly academic.",
    grammar_reason="[GRA9] Full range of structures used with precision. 'By selecting...', 'creating echo chambers', 'essential to avoid being...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 758: V8/G9 - Topic: Culture (Tradition)
samples.append(create_sample(
    index=758,
    vocab_band=8,
    grammar_band=9,
    question="Should we modernize traditions?",
    transcript="Adaptation is often necessary for survival. Traditions that are rigid and incompatible with modern values, such as gender equality, risk being abandoned. However, modernization should not mean erasure. We can evolve practices to be inclusive while respecting their core significance. It is a delicate balance between honoring the past and embracing the future. Stagnant traditions eventually become relics.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'adaptation', 'rigid', 'incompatible', 'abandoned', 'erasure', 'inclusive', 'significance', 'delicate balance', 'stagnant', 'relics'. >Band 7: Precise vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA9] Full range of structures used effortlessly. 'Traditions that are...', 'risk being abandoned', 'while respecting...', 'It is a delicate balance between...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 759: V8/G9 - Topic: Work (Remote)
samples.append(create_sample(
    index=759,
    vocab_band=8,
    grammar_band=9,
    question="What is the biggest challenge of remote work?",
    transcript="The erosion of boundaries is a significant issue. When your home becomes your office, switching off mentally becomes arduous. The 'always-on' culture can lead to digital burnout. Furthermore, the lack of spontaneous interaction with colleagues can stifle creativity and team bonding. Maintaining a healthy work-life integration requires rigorous discipline and clear communication protocols.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'erosion', 'boundaries', 'arduous', 'always-on', 'burnout', 'spontaneous', 'stifle', 'integration', 'rigorous', 'protocols'. >Band 7: Advanced terms. Not Band 9: Slightly formal.",
    grammar_reason="[GRA9] Full range of structures used with accuracy. 'When your home becomes...', 'The lack of... can stifle...', 'requires rigorous discipline'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 760: V8/G9 - Topic: Health (Diet)
samples.append(create_sample(
    index=760,
    vocab_band=8,
    grammar_band=9,
    question="Why are eating disorders increasing?",
    transcript="The proliferation of unrealistic body images on social media is a primary driver. Young people are bombarded with digitally altered photos, leading to body dysmorphia and low self-esteem. Additionally, the cultural obsession with dieting and 'clean eating' can morph into orthorexia. It is a complex interplay of psychological, social, and biological factors. We need to promote body positivity and media literacy to combat this trend.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'proliferation', 'bombarded', 'digitally altered', 'dysmorphia', 'obsession', 'orthorexia', 'interplay', 'positivity', 'literacy'. >Band 7: Precise medical/social terms. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA9] Full range of structures used with precision. 'leading to...', 'The cultural obsession... can morph...', 'It is a complex interplay of...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 761: V8/G9 - Topic: Environment (Trees)
samples.append(create_sample(
    index=761,
    vocab_band=8,
    grammar_band=9,
    question="Why is reforestation important?",
    transcript="It is a critical strategy for carbon sequestration. Trees absorb CO2, acting as a natural brake on global warming. Beyond climate benefits, forests prevent soil degradation and regulate the water cycle. They also provide habitats for countless species, preserving biodiversity. However, planting trees is not a panacea; we must also protect existing old-growth forests, which are irreplaceable carbon stores.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'panacea' (advanced term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'critical strategy', 'sequestration', 'degradation', 'regulate', 'biodiversity', 'panacea', 'old-growth', 'irreplaceable'. >Band 7: Strong vocabulary. Not Band 9: Slightly academic.",
    grammar_reason="[GRA9] Full range of structures used naturally. 'acting as a...', 'Beyond climate benefits...', 'which are irreplaceable...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 762: V8/G9 - Topic: Technology (Games)
samples.append(create_sample(
    index=762,
    vocab_band=8,
    grammar_band=9,
    question="How do video games affect the brain?",
    transcript="They have a profound impact on neuroplasticity. Action games, for instance, enhance visuospatial skills and reaction times. Strategy games can improve executive function and planning. However, excessive gaming can overstimulate the reward system, potentially leading to addiction similar to substance abuse. The key is moderation. When used mindfully, games can be a tool for cognitive enhancement.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'profound impact', 'neuroplasticity', 'visuospatial', 'executive function', 'overstimulate', 'addiction', 'moderation', 'mindfully', 'enhancement'. >Band 7: Scientific terms. Not Band 9: Lacks idiomatic usage.",
    grammar_reason="[GRA9] Full range of structures used effectively. 'have a profound impact on...', 'leading to addiction...', 'When used mindfully...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 763: V8/G9 - Topic: Society (Cities)
samples.append(create_sample(
    index=763,
    vocab_band=8,
    grammar_band=9,
    question="What is the problem with urban sprawl?",
    transcript="It promotes car dependency and environmental degradation. As cities expand horizontally, commute times lengthen, leading to increased emissions and stress. It also encroaches on agricultural land and natural habitats. Furthermore, low-density suburbs often lack the social cohesion and amenities of vibrant city centers. Smart growth strategies, focusing on density and public transport, are needed to curb this unsustainable expansion.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'dependency', 'degradation', 'horizontally', 'encroaches', 'low-density', 'cohesion', 'amenities', 'curb', 'unsustainable'. >Band 7: Advanced vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA9] Full range of structures used with complete accuracy. 'As cities expand...', 'leading to...', 'focusing on...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 764: V8/G9 - Topic: Transport (Safety)
samples.append(create_sample(
    index=764,
    vocab_band=8,
    grammar_band=9,
    question="Are driverless cars the solution to road safety?",
    transcript="They hold immense promise. By eliminating human error, which accounts for the vast majority of accidents, they could theoretically make roads much safer. Algorithms do not get drunk, tired, or distracted. However, the transitional phase, where autonomous and human-driven cars share the road, poses significant risks. Moreover, the ethical programming of these vehicles in unavoidable accident scenarios remains a complex dilemma.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'immense promise', 'eliminating', 'accounts for', 'theoretically', 'algorithms', 'transitional phase', 'scenarios', 'dilemma'. >Band 7: Precise terms. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA9] Full range of structures used effortlessly. 'By eliminating...', 'which accounts for...', 'where autonomous... share'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 765: V8/G9 - Topic: Education (Reading)
samples.append(create_sample(
    index=765,
    vocab_band=8,
    grammar_band=9,
    question="Why is literacy important for a nation?",
    transcript="Literacy is the bedrock of economic and social development. A literate population is more productive, healthier, and politically engaged. It empowers individuals to access information and advocate for their rights. Conversely, widespread illiteracy traps a nation in poverty and hinders innovation. Investing in education is not just a moral imperative; it is an economic necessity for any country aspiring to progress.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'bedrock', 'engaged', 'empowers', 'advocate', 'widespread', 'illiteracy', 'traps', 'hinders', 'imperative', 'aspiring'. >Band 7: Strong vocabulary. Not Band 9: Slightly academic.",
    grammar_reason="[GRA9] Full range of structures used with precision. 'is the bedrock of...', 'Conversely, widespread illiteracy...', 'is not just..., it is...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 766: V8/G9 - Topic: Culture (Global)
samples.append(create_sample(
    index=766,
    vocab_band=8,
    grammar_band=9,
    question="Does cultural diversity strengthen a country?",
    transcript="Unequivocally, yes. A diverse society benefits from a plurality of perspectives, which fosters innovation and problem-solving. It creates a vibrant, dynamic cultural landscape. Tolerance and adaptability are cultivated when different groups coexist. While integration poses challenges, the friction can generate creative energy. Homogeneity might offer stability, but diversity offers growth and resilience.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'unequivocally', 'plurality', 'fosters', 'vibrant', 'cultivated', 'coexist', 'integration', 'friction', 'homogeneity', 'resilience'. >Band 7: Advanced vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA9] Full range of structures used with complete accuracy. 'benefits from...', 'which fosters...', 'While integration poses...'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 767: V8/G9 - Topic: Work (Career)
samples.append(create_sample(
    index=767,
    vocab_band=8,
    grammar_band=9,
    question="How important is networking for career success?",
    transcript="In many industries, it is indispensable. 'It's not what you know, but who you know' holds a degree of truth. Networking opens doors to unadvertised opportunities and provides mentorship. It builds a reputation and professional capital. However, superficial networking can be transparent and counterproductive. Genuine relationship building, based on mutual value and respect, is the most effective strategy.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'It's not what you know' (idiom/quote)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'indispensable', 'unadvertised', 'mentorship', 'professional capital', 'superficial', 'transparent', 'counterproductive', 'mutual value'. Quote: 'It's not what you know...'. >Band 7: Strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA9] Full range of structures used naturally. 'opens doors to...', 'However, superficial networking...', 'based on...'. Error-free.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 768: V8/G9 - Topic: Technology (Communication)
samples.append(create_sample(
    index=768,
    vocab_band=8,
    grammar_band=9,
    question="Is privacy possible in the digital age?",
    transcript="It is becoming increasingly precarious. Our digital footprint is indelible, and data brokers trade our information like a commodity. Surveillance technology is ubiquitous. Achieving total privacy would require disconnecting from modern society, which is impractical for most. However, we can reclaim some agency through encryption and legislation. Privacy is not dead, but it requires active defense.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'precarious', 'digital footprint', 'indelible', 'brokers', 'commodity', 'ubiquitous', 'impractical', 'reclaim', 'agency', 'encryption'. >Band 7: Precise terms. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA9] Full range of structures used with accuracy. 'It is becoming...', 'would require disconnecting...', 'which is impractical'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 769: V8/G9 - Topic: Society (Housing)
samples.append(create_sample(
    index=769,
    vocab_band=8,
    grammar_band=9,
    question="What is the effect of homelessness on society?",
    transcript="It is a stain on our collective conscience. Homelessness represents a failure of the social safety net. It creates visible distress and public health risks. Furthermore, the economic cost of emergency services and policing often exceeds the cost of housing. Beyond the finances, it erodes social trust and cohesion. A society is judged by how it treats its most vulnerable members.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'stain on our collective conscience' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'safety net', 'distress', 'erodes', 'cohesion', 'vulnerable'. Metaphor: 'stain on our collective conscience'. >Band 7: Strong vocabulary. Not Band 9: Slightly dramatic.",
    grammar_reason="[GRA9] Full range of structures used effortlessly. 'It represents a failure...', 'often exceeds...', 'is judged by how...'. Error-free.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 770: V8/G9 - Topic: Transport (Flying)
samples.append(create_sample(
    index=770,
    vocab_band=8,
    grammar_band=9,
    question="Should we ban short-haul flights?",
    transcript="There is a strong environmental case for it. Short flights are disproportionately polluting due to the fuel used in take-off and landing. Where high-speed rail exists as a viable alternative, banning flights makes sense. France has already implemented such measures. It forces a modal shift towards greener transport. However, in areas with poor infrastructure, a ban would isolate communities.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'disproportionately', 'viable', 'implemented', 'modal shift', 'infrastructure', 'isolate'. >Band 7: Advanced vocabulary. Not Band 9: Lacks idiomatic usage.",
    grammar_reason="[GRA9] Full range of structures used with precision. 'Where high-speed rail exists...', 'banning flights makes sense', 'a ban would isolate'. Error-free.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
