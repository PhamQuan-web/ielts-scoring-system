import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch07.jsonl")

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

# --- BATCH 07 PART 3: SAMPLES 601-625 (25 Total) ---
# Combo: V8/G7 (Very Good Vocab, Good Grammar)

# Sample 601: V8/G7 - Topic: Environment (Sustainability)
samples.append(create_sample(
    index=601,
    vocab_band=8,
    grammar_band=7,
    question="How can we solve the problem of waste?",
    transcript="We need a paradigm shift towards a circular economy. Instead of the 'take-make-dispose' model, we should prioritize durability and recyclability. Planned obsolescence by manufacturers is a significant hurdle. If products were designed to last, waste would plummet. Furthermore, consumers must eschew single-use plastics. While recycling is beneficial, reduction is the ultimate goal. Governments should incentivize sustainable practices to accelerate this transition.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses wide range of precise vocabulary: 'paradigm shift', 'circular economy', 'prioritize', 'durability', 'planned obsolescence', 'hurdle', 'plummet', 'eschew', 'incentivize'. >Band 7: More sophisticated and precise. Not Band 9: Lacks full native-like naturalness.",
    grammar_reason="[GRA7] Uses complex structures: 'Instead of...', 'If products were designed...', 'While recycling is...'. >Band 6: Frequent error-free sentences. Not Band 8: Some structures are slightly standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 602: V8/G7 - Topic: Technology (AI)
samples.append(create_sample(
    index=602,
    vocab_band=8,
    grammar_band=7,
    question="Is AI a threat to job security?",
    transcript="It is undoubtedly a double-edged sword. Automation will inevitably render certain manual and repetitive jobs obsolete. However, it will also spawn new industries and roles that we cannot yet conceive. The challenge lies in reskilling the workforce to adapt to this new landscape. Rather than fearing technological encroachment, we should embrace it as a catalyst for efficiency. Humans and AI can work in synergy.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'double-edged sword' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'undoubtedly', 'inevitably', 'render', 'obsolete', 'spawn', 'conceive', 'reskilling', 'encroachment', 'catalyst', 'synergy'. Idiom: 'double-edged sword'. >Band 7: Precise and varied. Not Band 9: A bit formal.",
    grammar_reason="[GRA7] Contrast: 'However'. Gerund: 'Rather than fearing'. >Band 6: Good control. Not Band 8: Could use more inversion or emphasis.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 603: V8/G7 - Topic: Education (University)
samples.append(create_sample(
    index=603,
    vocab_band=8,
    grammar_band=7,
    question="What is the value of a university degree?",
    transcript="Beyond the acquisition of subject-specific knowledge, university fosters critical thinking and intellectual autonomy. It provides a fertile ground for networking and personal growth. While some argue that vocational skills are more pragmatic, the soft skills honed at university are invaluable. The ability to analyze complex data and articulate arguments is highly transferable. A degree is often a prerequisite for high-level careers.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses precise vocabulary: 'acquisition', 'fosters', 'intellectual autonomy', 'fertile ground', 'pragmatic', 'honed', 'invaluable', 'articulate', 'transferable', 'prerequisite'. >Band 7: Uses less common lexical items skillfully. Not Band 9: Slightly academic register.",
    grammar_reason="[GRA7] Contrast: 'While some argue...'. Relative clause: 'skills that are highly sought'. >Band 6: Frequent error-free sentences. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 604: V8/G7 - Topic: Society (Inequality)
samples.append(create_sample(
    index=604,
    vocab_band=8,
    grammar_band=7,
    question="How does inequality affect society?",
    transcript="It erodes social cohesion and breeds resentment. When a significant portion of the population feels marginalized, it can lead to civil unrest. The disparity in wealth often correlates with disparate access to healthcare and education, perpetuating a cycle of poverty. A society that fails to look after its most vulnerable members is fundamentally flawed. Egalitarian policies are essential to bridge this gap.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'erodes', 'social cohesion', 'breeds resentment', 'marginalized', 'disparity', 'correlates', 'perpetuating', 'vulnerable', 'fundamentally flawed', 'egalitarian'. >Band 7: Precise and effective. Not Band 9: Lacks full flexibility.",
    grammar_reason="[GRA7] Time clause: 'When a significant portion...'. Relative clause: 'that fails to look after'. >Band 6: Accurate complex sentences. Not Band 8: Sentences are standard length.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 605: V8/G7 - Topic: Culture (Globalization)
samples.append(create_sample(
    index=605,
    vocab_band=8,
    grammar_band=7,
    question="Does globalization mean the end of local culture?",
    transcript="Not necessarily. While there is a risk of cultural homogenization, globalization can also act as a vehicle for cultural dissemination. Local traditions can gain global appreciation. For example, yoga or sushi. However, we must be vigilant against cultural imperialism where dominant cultures suppress local ones. The goal should be a mosaic of cultures, not a melting pot where distinct identities are lost.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'melting pot' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses precise vocabulary: 'homogenization', 'dissemination', 'appreciation', 'vigilant', 'imperialism', 'suppress', 'mosaic', 'distinct identities'. Idiom: 'melting pot'. >Band 7: Sophisticated use. Not Band 9: Slightly formal.",
    grammar_reason="[GRA7] Contrast: 'However', 'not a melting pot where...'. >Band 6: Good control. Not Band 8: Limited range of complex structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 606: V8/G7 - Topic: Work (Job)
samples.append(create_sample(
    index=606,
    vocab_band=8,
    grammar_band=7,
    question="What are the most important factors when choosing a job?",
    transcript="Remuneration is obviously a primary factor, but job satisfaction is equally pivotal. Individuals seek roles that offer a sense of purpose and alignment with their values. Opportunities for professional development and upward mobility are also key. Furthermore, a toxic corporate culture can be detrimental to mental health. Therefore, a holistic view of the package, including work-life balance, is essential.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'remuneration', 'pivotal', 'alignment', 'professional development', 'upward mobility', 'toxic', 'detrimental', 'holistic'. >Band 7: Precise and varied. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA7] Contrast: 'but job satisfaction is'. Reason: 'Therefore'. >Band 6: Accurate grammar. Not Band 8: Sentences are competent.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 607: V8/G7 - Topic: Transport (Cities)
samples.append(create_sample(
    index=607,
    vocab_band=8,
    grammar_band=7,
    question="How can we reduce traffic congestion?",
    transcript="Implementing congestion charges is a proven deterrent. It discourages unnecessary car journeys in city centers. Simultaneously, we must bolster public transport infrastructure to provide a viable alternative. Investing in cycling lanes promotes active travel. Telecommuting is another effective strategy, as it removes commuters from the road entirely. A multi-pronged approach is required to tackle this perennial problem.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses less common items: 'implementing', 'deterrent', 'discourages', 'bolster', 'viable', 'promotes', 'telecommuting', 'multi-pronged', 'perennial'. >Band 7: Very good range. Not Band 9: Slightly robotic.",
    grammar_reason="[GRA7] Reason: 'as it removes...'. Gerund: 'Investing in cycling lanes'. >Band 6: Good control. Not Band 8: Standard structure.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 608: V8/G7 - Topic: Health (Exercise)
samples.append(create_sample(
    index=608,
    vocab_band=8,
    grammar_band=7,
    question="Why is physical activity declining?",
    transcript="The ubiquity of technology is a major culprit. Our lives have become increasingly sedentary due to automation and digital entertainment. We order food with a click and travel in cars. The convenience of modern life has inadvertently led to physical stagnation. Urban environments often lack green spaces, which discourages outdoor activity. Reversing this trend requires a conscious effort to integrate movement into our daily routine.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'ubiquity', 'culprit', 'sedentary', 'automation', 'inadvertently', 'stagnation', 'discourages', 'reversing', 'conscious effort', 'integrate'. >Band 7: Precise terms. Not Band 9: Lacks idiomatic expressions.",
    grammar_reason="[GRA7] Relative clause: 'which discourages'. Reason: 'due to automation'. >Band 6: Accurate complex sentences. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 609: V8/G7 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=609,
    vocab_band=8,
    grammar_band=7,
    question="Is it important to preserve biodiversity?",
    transcript="Absolutely. Biodiversity underpins the health of our planet. Each species is an integral part of a complex web of life. The extinction of a single species can trigger a cascade effect, destabilizing entire ecosystems. Furthermore, nature is a repository of potential medicines. Destroying habitats is short-sighted and reckless. We have a moral stewardship to protect the natural world for posterity.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses less common items: 'underpins', 'integral', 'cascade effect', 'destabilizing', 'repository', 'short-sighted', 'reckless', 'stewardship', 'posterity'. >Band 7: Strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA7] Conditionals: 'If we lose...', 'The extinction... can trigger'. >Band 6: Good control. Not Band 8: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 610: V8/G7 - Topic: Education (Reading)
samples.append(create_sample(
    index=610,
    vocab_band=8,
    grammar_band=7,
    question="What are the benefits of reading?",
    transcript="Reading is a gateway to knowledge and empathy. It expands our lexicon and enhances cognitive faculties. Immersion in a narrative allows us to experience diverse perspectives, fostering tolerance. In an era of ephemeral digital content, reading books demands sustained attention, which is a valuable skill. It is an intellectual pursuit that enriches the mind and soul.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'gateway', 'lexicon', 'cognitive faculties', 'immersion', 'narrative', 'fostering', 'ephemeral', 'sustained', 'intellectual pursuit'. >Band 7: Precise and varied. Not Band 9: Slightly academic.",
    grammar_reason="[GRA7] Relative clause: 'which is a valuable skill'. Gerund: 'Immersion in a narrative'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 611: V8/G7 - Topic: Technology (Data)
samples.append(create_sample(
    index=611,
    vocab_band=8,
    grammar_band=7,
    question="Should we be worried about data mining?",
    transcript="Yes, the commodification of personal data is alarming. Tech giants harvest our information to create detailed profiles, which are then monetized. This surveillance capitalism erodes privacy and autonomy. We are often unaware of how our data is being manipulated to influence our behavior or opinions. Stringent regulations are needed to safeguard digital rights. We must not surrender our privacy for convenience.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'commodification', 'alarming', 'harvest', 'monetized', 'surveillance capitalism', 'erodes', 'autonomy', 'manipulated', 'stringent', 'safeguard'. >Band 7: Very strong vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA7] Passive: 'are then monetized', 'is being manipulated'. Relative clause: 'which are then'. >Band 6: Accurate complex sentences. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 612: V8/G7 - Topic: Society (Volunteer)
samples.append(create_sample(
    index=612,
    vocab_band=8,
    grammar_band=7,
    question="Why is volunteering valuable?",
    transcript="It cultivates a sense of civic duty and altruism. By dedicating time to a cause, individuals can make a tangible difference in their community. It also combats social isolation by connecting people from diverse backgrounds. For the volunteer, it provides a sense of fulfillment that material gain cannot match. It is a mutually beneficial endeavor that strengthens the social fabric.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses less common items: 'cultivates', 'civic duty', 'altruism', 'dedicating', 'tangible', 'combats', 'fulfillment', 'mutually beneficial', 'endeavor', 'social fabric'. >Band 7: Precise terms. Not Band 9: Slightly formal.",
    grammar_reason="[GRA7] Gerund: 'By dedicating...'. Relative clause: 'that material gain cannot match'. >Band 6: Good control. Not Band 8: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 613: V8/G7 - Topic: Culture (Art)
samples.append(create_sample(
    index=613,
    vocab_band=8,
    grammar_band=7,
    question="Why is art often considered a luxury?",
    transcript="In a capitalist society, utility is often prioritized over aesthetics. Art is seen as non-essential for survival, hence a luxury. However, this view is reductionist. Art provokes thought, challenges the status quo, and nurtures the soul. While collecting high-end art is a privilege of the affluent, appreciating art should be accessible to all. It is a fundamental expression of humanity.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'utility', 'prioritized', 'aesthetics', 'non-essential', 'reductionist', 'provokes', 'status quo', 'nurtures', 'affluent', 'fundamental'. >Band 7: Advanced vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA7] Passive: 'is seen as'. Contrast: 'However'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 614: V8/G7 - Topic: Work (Gender)
samples.append(create_sample(
    index=614,
    vocab_band=8,
    grammar_band=7,
    question="How can we encourage more women into leadership?",
    transcript="We must dismantle the systemic barriers that hold them back. This involves challenging unconscious bias in recruitment and promotion. Mentorship programs can provide aspiring female leaders with guidance and advocacy. Furthermore, flexible working policies are essential to accommodate work-life balance, which disproportionately affects women. Empowering women is not just about fairness; it harnesses a wider pool of talent and perspective.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses less common items: 'dismantle', 'systemic barriers', 'unconscious bias', 'recruitment', 'aspiring', 'advocacy', 'accommodate', 'disproportionately', 'empowering', 'harnesses'. >Band 7: Precise and effective. Not Band 9: Slightly academic.",
    grammar_reason="[GRA7] Relative clause: 'that hold them back', 'which disproportionately affects'. >Band 6: Good control. Not Band 8: Structure is functional.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 615: V8/G7 - Topic: Transport (Flying)
samples.append(create_sample(
    index=615,
    vocab_band=8,
    grammar_band=7,
    question="What are the environmental impacts of air travel?",
    transcript="Aviation is a significant contributor to anthropogenic climate change. The carbon footprint of a single flight is substantial. Moreover, planes release nitrogen oxides at high altitudes, which amplifies the warming effect. While the industry is exploring biofuels, these are not yet scalable. Until zero-emission flight becomes a reality, we must be mindful of our travel habits and consider alternatives like rail.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'significant contributor', 'anthropogenic', 'carbon footprint', 'substantial', 'altitudes', 'amplifies', 'biofuels', 'scalable', 'zero-emission'. >Band 7: Technical/formal vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA7] Relative clause: 'which amplifies'. Contrast: 'While the industry...'. >Band 6: Accurate complex sentences. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 616: V8/G7 - Topic: Education (Technology)
samples.append(create_sample(
    index=616,
    vocab_band=8,
    grammar_band=7,
    question="Is technology in the classroom beneficial?",
    transcript="When integrated effectively, it is a powerful pedagogical tool. Interactive whiteboards and educational apps can enhance engagement and facilitate personalized learning. It prepares students for a digital-centric future. However, over-reliance can be detrimental. It might lead to shorter attention spans and reduced critical thinking. Technology should augment the teacher's role, not usurp it.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses less common items: 'integrated', 'pedagogical', 'interactive', 'enhance', 'facilitate', 'digital-centric', 'over-reliance', 'detrimental', 'augment', 'usurp'. >Band 7: Very strong vocabulary. Not Band 9: Slightly robotic.",
    grammar_reason="[GRA7] Contrast: 'However', 'not usurp it'. Time clause: 'When integrated...'. >Band 6: Good control. Not Band 8: Sentences are competent.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 617: V8/G7 - Topic: Society (Housing)
samples.append(create_sample(
    index=617,
    vocab_band=8,
    grammar_band=7,
    question="Why are cities becoming unaffordable?",
    transcript="Gentrification is a key driver. As wealthy individuals move into improved neighborhoods, property prices skyrocket, displacing long-term residents. Speculative investment also inflates the market. Homes are treated as assets rather than shelter. Furthermore, stagnant wages have not kept pace with the rising cost of living. This disparity creates a housing crisis that excludes the working class from urban centers.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'gentrification', 'key driver', 'skyrocket', 'displacing', 'speculative', 'inflates', 'assets', 'stagnant', 'disparity', 'excludes'. >Band 7: Precise terms. Not Band 9: Lacks idiomatic usage.",
    grammar_reason="[GRA7] Time clause: 'As wealthy individuals...'. Reason: 'rather than shelter'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 618: V8/G7 - Topic: Environment (Trees)
samples.append(create_sample(
    index=618,
    vocab_band=8,
    grammar_band=7,
    question="How do forests benefit the planet?",
    transcript="They are the lungs of the Earth, sequestration carbon and releasing oxygen. Forests regulate the climate and prevent soil erosion. They are also biodiversity hotspots, harboring countless species. Deforestation disrupts these vital functions, leading to environmental degradation. Preserving these ecosystems is not just about saving trees; it is about maintaining the planetary life-support system.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses less common items: 'sequestration', 'regulate', 'erosion', 'hotspots', 'harboring', 'disrupts', 'degradation', 'ecosystems', 'planetary'. Metaphor: 'lungs of the Earth'. >Band 7: Advanced vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA7] Participle phrase: 'sequestration carbon...'. Reason: 'leading to...'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structure.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 619: V8/G7 - Topic: Technology (Social Media)
samples.append(create_sample(
    index=619,
    vocab_band=8,
    grammar_band=7,
    question="How does social media influence opinion?",
    transcript="It creates echo chambers where users are only exposed to views that reinforce their own. Algorithms prioritize sensational content to maximize engagement, often spreading misinformation. This polarization makes constructive dialogue difficult. People become entrenched in their beliefs. While it gives a voice to the voiceless, it also amplifies divisiveness. Critical literacy is needed to navigate this digital landscape.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'voice to the voiceless' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'echo chambers', 'exposed', 'reinforce', 'algorithms', 'sensational', 'polarization', 'entrenched', 'amplifies', 'divisiveness'. Idiom: 'voice to the voiceless'. >Band 7: Strong vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA7] Relative clause: 'where users are...'. Contrast: 'While it gives...'. >Band 6: Good control. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 620: V8/G7 - Topic: Work (Job Hopping)
samples.append(create_sample(
    index=620,
    vocab_band=8,
    grammar_band=7,
    question="Is it bad to change jobs often?",
    transcript="Not necessarily. It can indicate ambition and a desire for diverse experiences. Job hopping allows individuals to broaden their skillset and increase their market value. However, excessive movement might signal a lack of commitment or resilience to employers. It is a calculated risk. Stability has its merits, but stagnation is the enemy of progress.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses less common items: 'indicate', 'ambition', 'diverse', 'skillset', 'market value', 'excessive', 'resilience', 'calculated risk', 'merits', 'stagnation'. >Band 7: Precise terms. Not Band 9: Slightly academic.",
    grammar_reason="[GRA7] Contrast: 'However', 'but stagnation is'. Reason: 'It can indicate...'. >Band 6: Accurate grammar. Not Band 8: Sentences are competent.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 621: V8/G7 - Topic: Culture (Language)
samples.append(create_sample(
    index=621,
    vocab_band=8,
    grammar_band=7,
    question="Will technology make language learning obsolete?",
    transcript="Translation devices are becoming incredibly sophisticated, offering real-time interpretation. This reduces the necessity for fluency in travel or basic business. However, language is intrinsically linked to culture and emotion. A machine cannot convey the subtleties of humor, irony, or empathy. Learning a language is an intellectual journey that fosters deep connection. Technology is an aid, not a replacement.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'sophisticated', 'interpretation', 'necessity', 'fluency', 'intrinsically', 'subtleties', 'irony', 'empathy', 'intellectual journey', 'fosters'. >Band 7: Advanced vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA7] Contrast: 'However'. Reason: 'offering real-time...'. >Band 6: Good control. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 622: V8/G7 - Topic: Society (Cities)
samples.append(create_sample(
    index=622,
    vocab_band=8,
    grammar_band=7,
    question="How can we improve city life?",
    transcript="Revitalizing urban spaces is crucial. We need to integrate green infrastructure, like vertical gardens and rooftop parks, to combat the concrete jungle effect. Promoting pedestrianization reduces pollution and encourages social interaction. Additionally, fostering a vibrant cultural scene with street art and festivals enhances the livability of a city. It is about creating a habitat for humans, not just cars.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'concrete jungle' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses less common items: 'revitalizing', 'integrate', 'infrastructure', 'vertical gardens', 'pedestrianization', 'fostering', 'vibrant', 'livability', 'habitat'. Metaphor: 'concrete jungle'. >Band 7: Very good range. Not Band 9: Slightly formal.",
    grammar_reason="[GRA7] Gerund: 'Promoting...', 'fostering...'. Purpose: 'to combat...'. >Band 6: Accurate grammar. Not Band 8: Sentences are somewhat standard.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 623: V8/G7 - Topic: Health (Diet)
samples.append(create_sample(
    index=623,
    vocab_band=8,
    grammar_band=7,
    question="What is the impact of processed food?",
    transcript="It is a catalyst for the global obesity epidemic. Processed foods are laden with preservatives, sugar, and unhealthy fats. They are engineered to be hyper-palatable, which leads to overconsumption. This dietary shift has resulted in a spike in lifestyle diseases like diabetes. We need to return to whole, unprocessed foods to reclaim our health. Convenience should not come at the cost of well-being.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'catalyst', 'epidemic', 'laden with', 'preservatives', 'engineered', 'hyper-palatable', 'overconsumption', 'dietary shift', 'spike', 'reclaim'. >Band 7: Strong vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA7] Relative clause: 'which leads to...'. Passive: 'are engineered'. >Band 6: Frequent error-free sentences. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 624: V8/G7 - Topic: Environment (Plastic)
samples.append(create_sample(
    index=624,
    vocab_band=8,
    grammar_band=7,
    question="Why is plastic pollution so difficult to solve?",
    transcript="Because plastic is ubiquitous and durable. It permeates every aspect of our lives, from packaging to clothing. Its durability, which is an asset, is also its downfall; it persists in the environment for centuries. Microplastics have infiltrated the food chain, posing a threat to all life. Transitioning away from plastic requires a monumental shift in manufacturing and consumer behavior. There is no quick fix.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'quick fix' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses less common items: 'ubiquitous', 'durable', 'permeates', 'downfall', 'persists', 'infiltrated', 'food chain', 'transitioning', 'monumental'. Idiom: 'quick fix'. >Band 7: Advanced terms. Not Band 9: Slightly academic.",
    grammar_reason="[GRA7] Relative clause: 'which is an asset'. Reason: 'Because plastic is...'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 625: V8/G7 - Topic: Transport (Flying)
samples.append(create_sample(
    index=625,
    vocab_band=8,
    grammar_band=7,
    question="Should we tax air travel more?",
    transcript="It is a justifiable measure. Air travel has a disproportionate environmental impact compared to other modes of transport. A carbon tax would internalize the environmental cost, making flying a luxury rather than a commodity. This revenue could be funneled into green alternatives like high-speed rail. While unpopular, it is a necessary step to curb emissions and combat climate change.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'justifiable', 'disproportionate', 'modes', 'internalize', 'commodity', 'revenue', 'funneled', 'alternatives', 'curb', 'combat'. >Band 7: Precise vocabulary. Not Band 9: Lacks idiomatic usage.",
    grammar_reason="[GRA7] Comparison: 'compared to other...'. Gerund: 'making flying a luxury'. >Band 6: Good control. Not Band 8: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
