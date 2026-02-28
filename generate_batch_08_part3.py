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

# --- BATCH 08 PART 3: SAMPLES 691-710 (20 Total) ---
# Combo: V8/G8

# Sample 691: V8/G8 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=691,
    vocab_band=8,
    grammar_band=8,
    question="Why is it important to teach children about recycling?",
    transcript="Instilling environmental responsibility at a young age creates lifelong habits. Children who understand the finite nature of resources are more likely to become conscientious consumers. Schools play a pivotal role in demystifying the recycling process. By normalizing sustainability, we shape a generation that views eco-friendly practices as the default, not an option. It is an investment in the planet's future.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'instilling', 'finite nature', 'conscientious', 'demystifying', 'normalizing', 'eco-friendly', 'default'. >Band 7: Advanced vocabulary. Not Band 9: Lacks idiomatic flow.",
    grammar_reason="[GRA8] Wide range: 'Children who understand...', 'By normalizing...', 'that views eco-friendly practices as...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 692: V8/G8 - Topic: Technology (Games)
samples.append(create_sample(
    index=692,
    vocab_band=8,
    grammar_band=8,
    question="Do video games encourage violence?",
    transcript="This is a polarized debate. While some studies suggest a correlation between violent games and aggression, causality is harder to prove. Most gamers distinguish fantasy from reality without issue. However, desensitization to violence is a valid concern. Constant exposure to graphic content might blunt our empathy. Ultimately, other factors like family environment and mental health are likely more significant determinants of violent behavior.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'polarized', 'correlation', 'causality', 'distinguish', 'desensitization', 'blunt', 'determinants'. >Band 7: Strong vocabulary. Not Band 9: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'While some studies suggest...', 'without issue', 'might blunt our empathy'. Majority error-free. >Band 7: Varied structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 693: V8/G8 - Topic: Health (Mental)
samples.append(create_sample(
    index=693,
    vocab_band=8,
    grammar_band=8,
    question="What is the stigma surrounding mental health?",
    transcript="Historically, mental illness was viewed as a weakness or character flaw. This archaic perception persists in many cultures, leading to discrimination and silence. People fear professional repercussions or social ostracization if they disclose their struggles. Although awareness campaigns are eroding these prejudices, significant barriers remain. Normalizing conversations about mental health is the antidote to this stigma.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'archaic', 'persists', 'repercussions', 'ostracization', 'disclose', 'eroding', 'antidote'. >Band 7: Precise terms. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'leading to...', 'if they disclose...', 'Normalizing... is the antidote'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 694: V8/G8 - Topic: Education (University)
samples.append(create_sample(
    index=694,
    vocab_band=8,
    grammar_band=8,
    question="Should university entrance be based only on grades?",
    transcript="Relying solely on grades is reductive. While academic prowess is important, it does not capture the full potential of a student. Creativity, leadership, and resilience are equally valuable but harder to quantify. A holistic admissions process, considering extracurricular achievements and personal character, would be more equitable. It would identify diamonds in the rough who might not excel in standardized tests.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'diamonds in the rough' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'reductive', 'prowess', 'quantify', 'holistic', 'equitable', 'extracurricular'. Idiom: 'diamonds in the rough'. >Band 7: Advanced vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'Relying solely on...', 'considering...', 'who might not excel'. Majority error-free. >Band 7: Accurate complex sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 695: V8/G8 - Topic: Work (Remote)
samples.append(create_sample(
    index=695,
    vocab_band=8,
    grammar_band=8,
    question="Will remote work affect city centers?",
    transcript="It is already reshaping the urban landscape. As commuters vanish, the businesses that serve them—cafes, dry cleaners, shops—face an existential crisis. This could lead to a 'hollowing out' of central business districts. However, it also presents an opportunity to reimagine city centers as residential and cultural hubs rather than just commercial zones. Adaptive reuse of office buildings could solve housing shortages.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'hollowing out' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'reshaping', 'existential crisis', 'reimagine', 'hubs', 'adaptive reuse'. Idiom: 'hollowing out'. >Band 7: Strong vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'As commuters vanish...', 'rather than just...', 'could solve housing shortages'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 696: V8/G8 - Topic: Culture (Fashion)
samples.append(create_sample(
    index=696,
    vocab_band=8,
    grammar_band=8,
    question="Is fashion art?",
    transcript="At its highest level, absolutely. Haute couture is a form of wearable sculpture. Designers express complex themes and emotions through fabric and form, much like a painter uses canvas. It challenges conventions and provokes thought. While fast fashion is purely utilitarian and commercial, true fashion design is an aesthetic pursuit that reflects the zeitgeist of its era.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'zeitgeist' (advanced loanword)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'haute couture', 'sculpture', 'conventions', 'utilitarian', 'aesthetic pursuit', 'zeitgeist'. >Band 7: Precise terms. Not Band 9: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'At its highest level...', 'much like a painter...', 'that reflects the zeitgeist'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 697: V8/G8 - Topic: Society (Family)
samples.append(create_sample(
    index=697,
    vocab_band=8,
    grammar_band=8,
    question="Why are divorce rates increasing?",
    transcript="The destigmatization of divorce is a primary factor. People are no longer forced by social pressure to stay in unhappy unions. Additionally, the economic independence of women allows them to leave abusive or unfulfilling marriages. We have also shifted towards a model of marriage based on personal fulfillment rather than duty. While high divorce rates seem alarming, they may indicate higher standards for happiness.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'destigmatization', 'unions', 'unfulfilling', 'fulfillment', 'alarming', 'indicate'. >Band 7: Advanced vocabulary. Not Band 9: Lacks idiomatic expressions.",
    grammar_reason="[GRA8] Wide range: 'forced by social pressure to...', 'allows them to leave...', 'rather than duty'. Majority error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 698: V8/G8 - Topic: Environment (Climate)
samples.append(create_sample(
    index=698,
    vocab_band=8,
    grammar_band=8,
    question="What is the role of technology in climate change?",
    transcript="It acts as both villain and savior. Industrial technology caused the crisis through carbon emissions. Yet, green technology offers our best hope for mitigation. Carbon capture, renewable energy storage, and electric mobility are vital innovations. We must leverage our technological prowess to heal the planet. However, techno-optimism should not breed complacency; behavioral change is equally critical.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'techno-optimism' (specific term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'villain', 'mitigation', 'storage', 'leverage', 'prowess', 'techno-optimism', 'complacency'. >Band 7: Strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'It acts as both...', 'Yet, green technology offers...', 'should not breed complacency'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 699: V8/G8 - Topic: Transport (Cities)
samples.append(create_sample(
    index=699,
    vocab_band=8,
    grammar_band=8,
    question="How can we encourage walking in cities?",
    transcript="Urban design must prioritize pedestrians over vehicles. Widening sidewalks, creating pedestrian-only zones, and improving lighting make walking safer and more appealing. Aesthetically pleasing environments with trees and benches encourage foot traffic. We also need to integrate mixed-use zoning, ensuring that shops and workplaces are within walkable distance. If a city is designed for people, not cars, walking becomes the natural choice.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'prioritize', 'zones', 'appealing', 'aesthetically', 'integrate', 'mixed-use zoning', 'natural choice'. >Band 7: Precise terms. Not Band 9: Lacks idiomatic flow.",
    grammar_reason="[GRA8] Wide range: 'Widening sidewalks...', 'ensuring that...', 'If a city is designed...'. Majority error-free. >Band 7: Good use of gerunds and conditionals.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 700: V8/G8 - Topic: Technology (Space)
samples.append(create_sample(
    index=700,
    vocab_band=8,
    grammar_band=8,
    question="Why is Mars colonization a goal?",
    transcript="It is driven by the desire to make humanity a multi-planetary species. This is seen as an insurance policy against existential risks on Earth, such as asteroid impacts or nuclear war. Mars is the most hospitable option in our solar system. Colonizing it would push the boundaries of science and engineering. It is the ultimate frontier, appealing to our innate spirit of exploration.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'multi-planetary', 'insurance policy', 'existential risks', 'hospitable', 'boundaries', 'frontier', 'innate'. >Band 7: Advanced vocabulary. Not Band 9: Slightly robotic.",
    grammar_reason="[GRA8] Wide range: 'driven by the desire...', 'seen as an insurance policy', 'Colonizing it would push...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 701: V8/G8 - Topic: Society (Wealth)
samples.append(create_sample(
    index=701,
    vocab_band=8,
    grammar_band=8,
    question="Is wealth distribution fair?",
    transcript="Currently, it is grossly inequitable. The concentration of wealth in the hands of the top 1% is staggering. This gap creates social stratification and limits mobility for the poor. While some argue that wealth is a reward for innovation, the system often rewards inheritance and monopoly rather than merit. A fairer system would ensure a living wage and robust social safety nets for all.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'grossly inequitable', 'concentration', 'staggering', 'stratification', 'mobility', 'monopoly', 'merit', 'robust'. >Band 7: Strong vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'While some argue...', 'rather than merit', 'A fairer system would ensure...'. Majority error-free. >Band 7: Accurate complex sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 702: V8/G8 - Topic: Work (Career)
samples.append(create_sample(
    index=702,
    vocab_band=8,
    grammar_band=8,
    question="Is career success defined by money?",
    transcript="For many, money is the primary metric, but it is a shallow one. True success encompasses fulfillment, impact, and balance. A high salary cannot compensate for a toxic work environment or a lack of purpose. Many people take pay cuts to pursue vocations that align with their values. Ultimately, success is a subjective concept, defined by personal satisfaction rather than a bank balance.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'metric', 'encompasses', 'compensate', 'toxic', 'vocations', 'align', 'subjective', 'satisfaction'. >Band 7: Precise terms. Not Band 9: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'but it is a shallow one', 'defined by personal satisfaction', 'rather than a bank balance'. Error-free. >Band 7: Varied structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 703: V8/G8 - Topic: Culture (Global)
samples.append(create_sample(
    index=703,
    vocab_band=8,
    grammar_band=8,
    question="How do international events affect culture?",
    transcript="Events like the Olympics or World Cup act as catalysts for cultural exchange. They provide a platform for nations to showcase their heritage to a global audience. This exposure fosters understanding and breaks down stereotypes. However, they can also lead to commercialization, where culture is packaged for tourist consumption. The key is to maintain authenticity while welcoming the world stage.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'catalysts', 'platform', 'showcase', 'exposure', 'fosters', 'stereotypes', 'commercialization', 'packaged', 'authenticity'. >Band 7: Advanced vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'act as catalysts', 'where culture is packaged', 'The key is to maintain...'. Majority error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 704: V8/G8 - Topic: Education (Skills)
samples.append(create_sample(
    index=704,
    vocab_band=8,
    grammar_band=8,
    question="Should students learn coding?",
    transcript="In the digital era, coding is becoming a fundamental literacy, akin to reading and writing. It teaches logical reasoning and problem-solving. Even for those who do not become programmers, understanding the logic behind technology is empowering. It demystifies the digital world. Schools that ignore coding risk leaving their students ill-equipped for the future job market.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'fundamental literacy', 'akin to', 'reasoning', 'empowering', 'demystifies', 'ill-equipped'. >Band 7: Precise terms. Not Band 9: Slightly robotic.",
    grammar_reason="[GRA8] Wide range: 'akin to reading', 'Even for those who...', 'risk leaving their students...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 705: V8/G8 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=705,
    vocab_band=8,
    grammar_band=8,
    question="Why is plastic waste a global crisis?",
    transcript="Its durability is its greatest flaw; plastic persists in the environment for centuries. It fragments into microplastics, which infiltrate the food chain and water supply. The sheer volume of waste overwhelms waste management systems, particularly in developing nations. It is a transboundary issue; plastic in the ocean respects no borders. Solving it requires international treaties and a unified global effort.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'transboundary' (advanced term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'durability', 'flaw', 'persists', 'fragments', 'infiltrate', 'sheer volume', 'overwhelms', 'transboundary', 'unified'. >Band 7: Strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'Its durability is...', 'which infiltrate...', 'Solving it requires...'. Majority error-free. >Band 7: Sophisticated control.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 706: V8/G8 - Topic: Transport (Public)
samples.append(create_sample(
    index=706,
    vocab_band=8,
    grammar_band=8,
    question="What makes a good public transport system?",
    transcript="Reliability and interconnectivity are the cornerstones. Commuters need to trust that the service will be punctual. A seamless network that integrates buses, trains, and bikes encourages usage. Accessibility for the elderly and disabled is also non-negotiable. Furthermore, affordability ensures that transport remains a public service, not a luxury. An efficient system is the lifeblood of a functioning city.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'lifeblood' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'interconnectivity', 'cornerstones', 'seamless', 'integrates', 'accessibility', 'non-negotiable', 'functioning'. Metaphor: 'lifeblood'. >Band 7: Precise vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'Commuters need to trust...', 'that integrates...', 'ensures that transport remains...'. Error-free. >Band 7: Varied structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 707: V8/G8 - Topic: Health (Diet)
samples.append(create_sample(
    index=707,
    vocab_band=8,
    grammar_band=8,
    question="Why do people have unhealthy diets?",
    transcript="It is often a result of the 'obesogenic' environment we live in. Unhealthy food is ubiquitous, cheap, and heavily marketed. In contrast, fresh produce can be expensive and time-consuming to prepare. Stress and emotional eating also contribute to poor dietary choices. It is a systemic issue, not just a failure of individual willpower. We need policy changes to make the healthy choice the easy choice.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'obesogenic' (technical term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'obesogenic', 'ubiquitous', 'marketed', 'dietary', 'systemic', 'willpower'. >Band 7: Advanced vocabulary. Not Band 9: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'It is often a result of...', 'In contrast...', 'not just a failure of...'. Majority error-free. >Band 7: Sophisticated control.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 708: V8/G8 - Topic: Society (Cities)
samples.append(create_sample(
    index=708,
    vocab_band=8,
    grammar_band=8,
    question="Are cities good places to raise children?",
    transcript="They offer unparalleled access to culture, education, and diversity. Children exposed to a multicultural environment tend to be more open-minded. Museums, parks, and libraries are on their doorstep. However, pollution, lack of space, and safety concerns are significant drawbacks. Raising a child in a city requires navigating these challenges. Ultimately, it depends on the specific neighborhood and the resources available to the parents.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'unparalleled', 'multicultural', 'open-minded', 'doorstep', 'drawbacks', 'navigating'. >Band 7: Precise terms. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'exposed to...', 'tend to be...', 'Raising a child... requires...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 709: V8/G8 - Topic: Technology (Privacy)
samples.append(create_sample(
    index=709,
    vocab_band=8,
    grammar_band=8,
    question="Why is facial recognition controversial?",
    transcript="It represents a significant intrusion into personal privacy. The potential for mass surveillance and state control is dystopian. There are also concerns about bias; algorithms often have higher error rates for minorities, leading to wrongful identification. While proponents argue it enhances security, the trade-off is civil liberty. We must establish strict legal frameworks to prevent abuse of this powerful technology.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'intrusion', 'dystopian', 'bias', 'algorithms', 'wrongful identification', 'proponents', 'civil liberty', 'frameworks'. >Band 7: Strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'The potential for...', 'leading to...', 'While proponents argue...'. Majority error-free. >Band 7: Accurate and varied.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 710: V8/G8 - Topic: Culture (Art)
samples.append(create_sample(
    index=710,
    vocab_band=8,
    grammar_band=8,
    question="How does art reflect history?",
    transcript="Art is a visual record of the zeitgeist. It captures the emotions, beliefs, and struggles of a specific era. For instance, Renaissance art reflects the rebirth of learning, while modern art often critiques industrialization and consumerism. By studying art, we gain insight into the human condition across centuries. It provides a narrative that textbooks often miss, preserving the spirit of the past.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'zeitgeist' (loanword)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'zeitgeist', 'captures', 'era', 'renaissance', 'critiques', 'industrialization', 'consumerism', 'insight', 'narrative'. >Band 7: Advanced vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'Art is a visual record...', 'while modern art often...', 'By studying art...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=True,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
