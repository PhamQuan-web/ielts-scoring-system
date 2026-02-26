import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch08.jsonl")

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

# --- BATCH 08 PART 4: SAMPLES 711-730 (20 Total) ---
# Combo: V8/G8

# Sample 711: V8/G8 - Topic: Environment (Sustainability)
samples.append(create_sample(
    index=711,
    vocab_band=8,
    grammar_band=8,
    question="What is the role of renewable energy?",
    transcript="It is the cornerstone of a sustainable future. Transitioning from fossil fuels to renewables is imperative to mitigate the catastrophic effects of climate change. Solar, wind, and geothermal energy offer inexhaustible alternatives that produce zero emissions. While the initial infrastructure investment is substantial, the long-term ecological and economic dividends are incalculable. It is the only viable path forward.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'cornerstone', 'transitioning', 'imperative', 'mitigate', 'catastrophic', 'inexhaustible', 'dividends', 'incalculable', 'viable'. >Band 7: Very strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'Transitioning... is imperative...', 'While the initial...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 712: V8/G8 - Topic: Society (Media)
samples.append(create_sample(
    index=712,
    vocab_band=8,
    grammar_band=8,
    question="Why is freedom of speech important?",
    transcript="It is a fundamental tenet of democracy. Without it, a society stagnates and oppression flourishes. The ability to express dissenting opinions fosters debate and innovation. It holds power to account. However, freedom of speech is not absolute; it does not protect hate speech or incitement to violence. Navigating the boundary between liberty and responsibility is a perennial challenge for any free society.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'tenet', 'stagnates', 'oppression', 'flourishes', 'dissenting', 'fosters', 'incitement', 'boundary', 'perennial'. >Band 7: Precise terms. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'Without it...', 'The ability to express...', 'Navigating the boundary... is...'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 713: V8/G8 - Topic: Work (Job)
samples.append(create_sample(
    index=713,
    vocab_band=8,
    grammar_band=8,
    question="How is the gig economy changing work?",
    transcript="It has disrupted traditional employment models. The gig economy offers flexibility and autonomy, allowing individuals to monetize their skills on their own terms. However, it also introduces precarity. Gig workers often lack the safety net of benefits like health insurance and paid leave. This 'uberization' of work shifts the risk from the employer to the employee, creating a new class of vulnerable workers.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'uberization' (neologism)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'disrupted', 'autonomy', 'monetize', 'precarity', 'safety net', 'uberization', 'vulnerable'. >Band 7: Advanced vocabulary. Not Band 9: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'allowing individuals to...', 'However, it also introduces...', 'shifts the risk... creating...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 714: V8/G8 - Topic: Education (University)
samples.append(create_sample(
    index=714,
    vocab_band=8,
    grammar_band=8,
    question="Is online learning the future?",
    transcript="It will undoubtedly play a central role, but it will not entirely supplant traditional methods. The hybrid model, blending digital flexibility with in-person interaction, seems the most robust. Online platforms democratize access to knowledge, reaching remote learners. Yet, the social acclimatization and mentorship found on campus are irreplaceable. The future lies in synergy, leveraging the strengths of both modalities.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'undoubtedly', 'supplant', 'hybrid', 'blending', 'robust', 'democratize', 'acclimatization', 'irreplaceable', 'synergy', 'leveraging', 'modalities'. >Band 7: Very strong vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'blending digital flexibility...', 'reaching remote learners', 'The future lies in...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 715: V8/G8 - Topic: Culture (Globalization)
samples.append(create_sample(
    index=715,
    vocab_band=8,
    grammar_band=8,
    question="Why do some people resist globalization?",
    transcript="They perceive it as a threat to their sovereignty and identity. The influx of foreign goods and ideas can feel like an invasion, eroding local customs. Economic dislocation is another factor; outsourcing jobs to cheaper markets breeds resentment. People fear the loss of community and the homogenization of culture. This resistance is often a defense mechanism against rapid, uncontrollable change.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'perceive', 'sovereignty', 'influx', 'eroding', 'dislocation', 'outsourcing', 'breeds', 'homogenization', 'defense mechanism'. >Band 7: Strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'The influx... can feel like...', 'outsourcing jobs... breeds...', 'This resistance is...'. Error-free. >Band 7: Accurate complex sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 716: V8/G8 - Topic: Technology (AI)
samples.append(create_sample(
    index=716,
    vocab_band=8,
    grammar_band=8,
    question="Can AI be creative?",
    transcript="In a derivative sense, yes. AI can synthesize vast amounts of existing art to produce novel combinations. However, true creativity stems from human consciousness, emotion, and lived experience—qualities that algorithms lack. AI can mimic the style of Van Gogh, but it cannot feel the anguish that inspired his strokes. It is a powerful tool for augmentation, but the spark of genesis remains human.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'derivative', 'synthesize', 'novel', 'consciousness', 'algorithms', 'mimic', 'anguish', 'augmentation', 'genesis'. >Band 7: Precise terms. Not Band 9: Lacks idiomatic usage.",
    grammar_reason="[GRA8] Wide range: 'In a derivative sense...', 'However, true creativity stems...', 'qualities that algorithms lack'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 717: V8/G8 - Topic: Transport (Cities)
samples.append(create_sample(
    index=717,
    vocab_band=8,
    grammar_band=8,
    question="What is the impact of ride-sharing apps?",
    transcript="They have revolutionized urban mobility by offering on-demand convenience. They reduce the need for car ownership, potentially lowering the number of vehicles on the road. However, they have also disrupted the taxi industry and raised concerns about worker rights. Furthermore, studies suggest they might actually increase congestion by adding 'dead miles' where drivers circulate without passengers. The net impact is complex and multifaceted.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'dead miles' (specific term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'revolutionized', 'mobility', 'on-demand', 'disrupted', 'congestion', 'circulate', 'net impact', 'multifaceted'. Term: 'dead miles'. >Band 7: Advanced vocabulary. Not Band 9: Slightly robotic.",
    grammar_reason="[GRA8] Wide range: 'by offering...', 'potentially lowering...', 'where drivers circulate...'. Error-free. >Band 7: Varied structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 718: V8/G8 - Topic: Health (Mental)
samples.append(create_sample(
    index=718,
    vocab_band=8,
    grammar_band=8,
    question="Is mental health treated the same as physical health?",
    transcript="Unfortunately, a disparity persists. While we immediately treat a broken leg, a broken mind is often ignored or stigmatized. Mental health services are frequently underfunded and inaccessible compared to physical healthcare. However, the paradigm is shifting. There is a growing recognition that the two are inextricably linked. Holistic health requires treating the mind with the same urgency and compassion as the body.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'disparity', 'persists', 'stigmatized', 'underfunded', 'inaccessible', 'paradigm', 'inextricably linked', 'holistic', 'urgency'. >Band 7: Strong vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'While we immediately treat...', 'compared to...', 'There is a growing recognition that...'. Error-free. >Band 7: Accurate complex sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 719: V8/G8 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=719,
    vocab_band=8,
    grammar_band=8,
    question="Why are invasive species a problem?",
    transcript="They disrupt the delicate equilibrium of ecosystems. Introduced species often lack natural predators in their new environment, allowing their populations to explode. They outcompete native species for resources, driving them towards extinction. This loss of biodiversity weakens the resilience of the habitat. Controlling invasive species is often a costly and difficult battle, but it is necessary to preserve ecological integrity.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'delicate equilibrium', 'predators', 'outcompete', 'native', 'extinction', 'resilience', 'integrity'. >Band 7: Precise terms. Not Band 9: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'allowing their populations to explode', 'driving them towards...', 'Controlling... is...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 720: V8/G8 - Topic: Education (Reading)
samples.append(create_sample(
    index=720,
    vocab_band=8,
    grammar_band=8,
    question="Does reading shape our personality?",
    transcript="It has a profound formative influence. Literature exposes us to the inner lives of others, fostering deep empathy and emotional intelligence. By encountering diverse characters and dilemmas, we refine our own moral compass. Reading also cultivates patience and focus, traits that are increasingly rare. In a sense, we become the sum of the stories we have absorbed. It sculpts our character.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'profound', 'formative', 'inner lives', 'fostering', 'dilemmas', 'moral compass', 'cultivates', 'traits', 'absorbed', 'sculpts'. >Band 7: Advanced vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'By encountering...', 'traits that are...', 'In a sense...'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 721: V8/G8 - Topic: Society (Cities)
samples.append(create_sample(
    index=721,
    vocab_band=8,
    grammar_band=8,
    question="Why is urban green space important?",
    transcript="It is an essential antidote to the stresses of city life. Parks provide a sanctuary for relaxation and recreation, boosting mental well-being. They also mitigate the 'urban heat island' effect and improve air quality. Green spaces foster social cohesion by providing a communal meeting ground. A city without nature is a sterile environment; green spaces inject vitality and humanity into the concrete landscape.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'urban heat island' (technical term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'antidote', 'sanctuary', 'recreation', 'mitigate', 'foster', 'social cohesion', 'communal', 'sterile', 'vitality'. Term: 'urban heat island'. >Band 7: Strong vocabulary. Not Band 9: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'boosting mental well-being', 'by providing...', 'A city without nature is...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 722: V8/G8 - Topic: Culture (Art)
samples.append(create_sample(
    index=722,
    vocab_band=8,
    grammar_band=8,
    question="Is graffiti vandalism?",
    transcript="The distinction lies in permission and intent. Unsolicited tagging of private property is undoubtedly vandalism, a criminal act that degrades the environment. However, commissioned street art can be a powerful form of cultural expression. It can revitalize neglected urban areas and provoke public discourse. When executed with skill and consent, it transforms a wall into a canvas, adding aesthetic value to the community.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'distinction', 'unsolicited', 'tagging', 'undoubtedly', 'degrades', 'commissioned', 'revitalize', 'neglected', 'discourse', 'executed', 'aesthetic'. >Band 7: Precise terms. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'The distinction lies in...', 'a criminal act that degrades...', 'When executed with skill...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 723: V8/G8 - Topic: Work (Job)
samples.append(create_sample(
    index=723,
    vocab_band=8,
    grammar_band=8,
    question="Is job satisfaction more important than salary?",
    transcript="Ultimately, yes. While a high salary provides financial security, it does not guarantee happiness. Spending forty hours a week in a role that feels meaningless or toxic takes a heavy psychological toll. Job satisfaction, derived from autonomy, mastery, and purpose, sustains us. A fat paycheck might buy comfort, but it cannot buy the fulfillment that comes from doing work you love.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'fat paycheck' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'guarantee', 'meaningless', 'toxic', 'psychological toll', 'derived', 'autonomy', 'mastery', 'sustains', 'fulfillment'. Idiom: 'fat paycheck'. >Band 7: Very strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'While a high salary...', 'Spending forty hours... takes...', 'derived from...'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 724: V8/G8 - Topic: Technology (Internet)
samples.append(create_sample(
    index=724,
    vocab_band=8,
    grammar_band=8,
    question="Has the internet empowered people?",
    transcript="Unquestionably. It has dismantled information gatekeepers, allowing anyone to broadcast their voice. It facilitates grassroots movements and holds power to account. Marginalized groups have found community and solidarity online. However, this empowerment has a dark side; it also empowers hate groups and misinformation agents. The internet amplifies all voices, both benevolent and malevolent. It is a tool of immense, neutral power.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'unquestionably', 'dismantled', 'gatekeepers', 'facilitates', 'grassroots', 'marginalized', 'solidarity', 'amplifies', 'benevolent', 'malevolent'. >Band 7: Advanced vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'allowing anyone to...', 'However, this empowerment...', 'It is a tool of...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 725: V8/G8 - Topic: Environment (Climate)
samples.append(create_sample(
    index=725,
    vocab_band=8,
    grammar_band=8,
    question="Why is biodiversity loss a crisis?",
    transcript="Because it threatens the stability of the biosphere. Ecosystems rely on a complex web of interactions between species. Removing one strand can cause the entire web to unravel. We rely on biodiversity for food, medicine, and clean air. The accelerated rate of extinction we are witnessing is anthropogenic, driven by habitat destruction and climate change. It is an ecological emergency.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'stability', 'biosphere', 'unravel', 'accelerated', 'extinction', 'anthropogenic', 'habitat destruction', 'ecological emergency'. >Band 7: Scientific terms. Not Band 9: Slightly robotic.",
    grammar_reason="[GRA8] Wide range: 'Removing one strand can...', 'The accelerated rate... is...', 'driven by...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 726: V8/G8 - Topic: Transport (Flying)
samples.append(create_sample(
    index=726,
    vocab_band=8,
    grammar_band=8,
    question="Will we stop flying for leisure?",
    transcript="It is unlikely, despite the environmental cost. The desire to explore new horizons is deeply human. However, 'flight shaming' and carbon awareness are changing behaviors. We might see a shift towards fewer, longer trips rather than frequent weekend breaks. Unless zero-emission aviation becomes a reality, ethical tourism will require a difficult trade-off between wanderlust and planetary health.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'flight shaming' (neologism)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'environmental cost', 'horizons', 'carbon awareness', 'zero-emission', 'aviation', 'ethical tourism', 'trade-off', 'wanderlust'. Term: 'flight shaming'. >Band 7: Precise vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'despite the environmental cost', 'rather than frequent...', 'Unless zero-emission...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 727: V8/G8 - Topic: Society (Consumerism)
samples.append(create_sample(
    index=727,
    vocab_band=8,
    grammar_band=8,
    question="Why do we buy things we don't need?",
    transcript="We are trying to fill a psychological void. Consumerism promises that happiness can be purchased. Advertisers exploit our insecurities, convincing us that a product will make us better, cooler, or more loved. This 'retail therapy' provides a dopamine hit, but it is fleeting. We end up in a cycle of desire and dissatisfaction. True contentment cannot be bought.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'dopamine hit' (collocation)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'psychological void', 'exploit', 'insecurities', 'convincing', 'fleeting', 'cycle', 'dissatisfaction', 'contentment'. >Band 7: Strong vocabulary. Not Band 9: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'convincing us that...', 'provides a dopamine hit, but...', 'cannot be bought'. Error-free. >Band 7: Accurate complex sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 728: V8/G8 - Topic: Education (University)
samples.append(create_sample(
    index=728,
    vocab_band=8,
    grammar_band=8,
    question="Should university be free?",
    transcript="In an ideal world, yes. Education is a public good, not a commodity. Free tuition removes financial barriers, allowing social mobility based on merit, not wealth. It produces an educated workforce, which benefits the economy. However, the cost must be borne by taxpayers. It requires a societal consensus that education is a priority worthy of collective investment. It is a question of values.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'public good', 'commodity', 'financial barriers', 'social mobility', 'merit', 'borne by', 'societal consensus', 'collective investment'. >Band 7: Advanced terms. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'removes..., allowing...', 'which benefits the economy', 'It requires... that...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 729: V8/G8 - Topic: Work (Gender)
samples.append(create_sample(
    index=729,
    vocab_band=8,
    grammar_band=8,
    question="How can we achieve gender equality at work?",
    transcript="It requires a dismantling of patriarchal structures. We need transparency in pay to close the wage gap. Paid parental leave for both genders is crucial to break the stigma that caregiving is women's work. Mentorship and quotas can help break the glass ceiling. Cultural change is slow, but policy intervention can accelerate it. Equality is not a zero-sum game; it benefits everyone.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'zero-sum game' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'dismantling', 'patriarchal', 'transparency', 'stigma', 'caregiving', 'quotas', 'glass ceiling', 'intervention', 'accelerate'. Idiom: 'zero-sum game'. >Band 7: Strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'to break the stigma that...', 'Mentorship... can help...', 'Equality is not..., it benefits...'. Error-free. >Band 7: Varied structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 730: V8/G8 - Topic: Culture (Global)
samples.append(create_sample(
    index=730,
    vocab_band=8,
    grammar_band=8,
    question="Is cultural diversity essential?",
    transcript="It is indispensable for a thriving society. Monocultures are stagnant; diverse cultures are dynamic. The collision of different perspectives drives innovation and art. It teaches us tolerance and adaptability. In a globalized world, the ability to navigate cultural differences is a key skill. Embracing diversity enriches our collective human experience and makes us more resilient to change.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'indispensable', 'thriving', 'monocultures', 'stagnant', 'dynamic', 'collision', 'adaptability', 'navigate', 'embracing', 'resilient'. >Band 7: Precise terms. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'The collision... drives...', 'It teaches us...', 'Embracing diversity enriches...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
