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

# --- BATCH 07 PART 2: SAMPLES 576-600 (25 Total) ---
# Combo: V7/G8

# Sample 576: V7/G8 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=576,
    vocab_band=7,
    grammar_band=8,
    question="Why do some people refuse to recycle?",
    transcript="Often, it is due to a lack of convenience or understanding. If recycling facilities are not readily accessible, people are less likely to make the effort. Additionally, skepticism plays a role; some believe that their individual actions make no difference or that recyclables end up in landfills anyway. To change this mindset, governments must ensure transparency in the recycling process and provide incentives for participation.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'readily accessible', 'skepticism', 'mindset', 'transparency', 'incentives', 'participation'. >Band 6: Strong vocabulary. Not Band 8: Lacks idiomatic expressions.",
    grammar_reason="[GRA8] Wide range: 'If recycling facilities are...', 'believe that their individual actions...', 'To change this mindset...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 577: V7/G8 - Topic: Technology (Games)
samples.append(create_sample(
    index=577,
    vocab_band=7,
    grammar_band=8,
    question="Are video games a waste of time?",
    transcript="Not necessarily. While excessive gaming can be detrimental, moderate play has benefits. Games can improve cognitive functions such as problem-solving and hand-eye coordination. Furthermore, many modern games are social platforms where players build communities and friendships. Dismissing them as a waste of time ignores their cultural and educational potential. Like any hobby, the value depends on how it is used.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'excessive', 'detrimental', 'cognitive functions', 'coordination', 'dismissing', 'cultural', 'potential'. >Band 6: Precise terms. Not Band 8: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'While excessive gaming...', 'where players build...', 'Dismissing them as...'. Majority error-free. >Band 7: Complex sentence variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 578: V7/G8 - Topic: Education (Teacher)
samples.append(create_sample(
    index=578,
    vocab_band=7,
    grammar_band=8,
    question="Can technology replace teachers?",
    transcript="I strongly believe that technology should complement, not replace, teachers. While AI can provide personalized content and instant feedback, it cannot replicate the emotional support and mentorship that a human teacher offers. Education is not just about data transfer; it is about inspiration and social development. A machine cannot empathize with a struggling student or celebrate their success in a meaningful way.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'complement', 'personalized', 'replicate', 'mentorship', 'data transfer', 'inspiration', 'empathize', 'meaningful'. >Band 6: Good range. Not Band 8: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'should complement, not replace', 'While AI can...', 'that a human teacher offers'. Error-free. >Band 7: Accurate complex structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 579: V7/G8 - Topic: Culture (Tradition)
samples.append(create_sample(
    index=579,
    vocab_band=7,
    grammar_band=8,
    question="Why are festivals important?",
    transcript="Festivals serve as a vital link to our heritage. They allow us to celebrate our shared history and values, strengthening community bonds. In a rapidly changing world, these events provide a sense of continuity and identity. Moreover, they are often a significant source of tourism revenue for local economies. Preserving these celebrations is essential for maintaining cultural diversity.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'vital link', 'heritage', 'strengthening', 'bonds', 'continuity', 'revenue', 'economies', 'preserving', 'diversity'. >Band 6: Sophisticated vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'serve as a...', 'In a rapidly changing world...', 'Preserving these celebrations is...'. Error-free. >Band 7: High level of accuracy.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 580: V7/G8 - Topic: Society (Crime)
samples.append(create_sample(
    index=580,
    vocab_band=7,
    grammar_band=8,
    question="Why do young people commit crimes?",
    transcript="Juvenile delinquency is often a symptom of broader social issues. Lack of parental guidance, peer pressure, and economic deprivation are significant factors. When young people feel marginalized or hopeless, they may turn to crime for status or survival. The education system also plays a role; if students feel excluded, they disengage. addressing these root causes is more effective than punishment alone.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'delinquency', 'symptom', 'deprivation', 'marginalized', 'disengage', 'root causes'. >Band 6: Advanced vocabulary. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'is often a symptom of...', 'When young people feel...', 'than punishment alone'. Majority error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 581: V7/G8 - Topic: Work (Job)
samples.append(create_sample(
    index=581,
    vocab_band=7,
    grammar_band=8,
    question="What makes a good colleague?",
    transcript="Reliability and communication are paramount. A good colleague is someone who pulls their weight and keeps others informed. They should be supportive and willing to share knowledge rather than hoard it. A positive attitude also makes a huge difference in the workplace atmosphere. Ultimately, it is about mutual respect and the ability to collaborate effectively towards a common goal.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'pulls their weight' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'paramount', 'hoard', 'atmosphere', 'mutual respect', 'collaborate', 'common goal'. Idiom: 'pulls their weight'. >Band 6: Strong vocabulary. Not Band 8: Slightly list-like.",
    grammar_reason="[GRA8] Wide range: 'someone who pulls...', 'rather than hoard it', 'it is about...'. Error-free. >Band 7: Accurate and varied.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 582: V7/G8 - Topic: Transport (Safety)
samples.append(create_sample(
    index=582,
    vocab_band=7,
    grammar_band=8,
    question="How can we reduce traffic accidents?",
    transcript="A multifaceted approach is required. Stricter enforcement of traffic laws, such as speed limits and seatbelt use, is a deterrent. However, infrastructure improvements are equally important. Better road design can minimize human error. Furthermore, public education campaigns can raise awareness about the dangers of distracted driving. Technology, like autonomous braking systems, will also play a pivotal role in the future.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'multifaceted', 'enforcement', 'deterrent', 'minimize', 'campaigns', 'awareness', 'distracted', 'pivotal'. >Band 6: Advanced vocabulary. Not Band 8: Lacks idiomatic expressions.",
    grammar_reason="[GRA8] Wide range: 'A multifaceted approach is...', 'such as...', 'can raise awareness about...'. Majority error-free. >Band 7: Sophisticated structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 583: V7/G8 - Topic: Health (Sleep)
samples.append(create_sample(
    index=583,
    vocab_band=7,
    grammar_band=8,
    question="Why is sleep important?",
    transcript="Sleep is essential for physical and mental restoration. During sleep, the body repairs tissues and the brain processes information from the day. Chronic sleep deprivation is linked to a host of health problems, including obesity, heart disease, and depression. Moreover, a lack of sleep impairs cognitive function and decision-making. In a fast-paced world, we often undervalue sleep, but it is the foundation of good health.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'restoration', 'deprivation', 'host of', 'impairs', 'cognitive function', 'undervalue', 'foundation'. >Band 6: Medical/formal terms. Not Band 8: Slightly robotic.",
    grammar_reason="[GRA8] Wide range: 'linked to a host of...', 'including...', 'In a fast-paced world...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 584: V7/G8 - Topic: Environment (Global Warming)
samples.append(create_sample(
    index=584,
    vocab_band=7,
    grammar_band=8,
    question="What can individuals do to fight climate change?",
    transcript="While systemic change is needed, individual actions matter. We can reduce our carbon footprint by making conscious choices, such as eating less meat or using public transport. Reducing energy consumption at home is another simple step. We can also use our voice to demand action from politicians and corporations. Collective individual action sends a powerful message that change is necessary.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'systemic', 'carbon footprint', 'conscious', 'consumption', 'corporations', 'collective'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'advocacy', 'lifestyle'.",
    grammar_reason="[GRA8] Wide range: 'While systemic change...', 'by making conscious choices', 'sends a powerful message that...'. Majority error-free. >Band 7: Varied structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 585: V7/G8 - Topic: Technology (Internet)
samples.append(create_sample(
    index=585,
    vocab_band=7,
    grammar_band=8,
    question="Has the internet made the world a better place?",
    transcript="On balance, yes. It has democratized access to information and education, empowering people globally. It has also facilitated communication and trade. However, we cannot ignore the negative aspects, such as cyberbullying, misinformation, and privacy erosion. The internet is a tool, and its impact depends on how we use it. We must address the harms while maximizing the benefits.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'democratized', 'empowering', 'facilitated', 'misinformation', 'erosion', 'maximizing'. >Band 6: Advanced vocabulary. Not Band 8: Lacks idiomatic flow.",
    grammar_reason="[GRA8] Wide range: 'It has also facilitated...', 'such as...', 'The internet is a tool, and...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 586: V7/G8 - Topic: Culture (Art)
samples.append(create_sample(
    index=586,
    vocab_band=7,
    grammar_band=8,
    question="Why do we need museums?",
    transcript="Museums are custodians of our history and culture. They preserve artifacts and artworks for future generations, ensuring that our heritage is not lost. They also serve as educational hubs, inspiring curiosity and learning. By visiting museums, we gain perspective on our place in the world. Furthermore, they contribute to the local economy through tourism. They are essential institutions for a civilized society.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'custodians', 'artifacts', 'heritage', 'hubs', 'curiosity', 'perspective', 'institutions', 'civilized'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'ensuring that...', 'By visiting museums...', 'Furthermore, they contribute...'. Majority error-free. >Band 7: Complex sentences used naturally.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 587: V7/G8 - Topic: Transport (Cities)
samples.append(create_sample(
    index=587,
    vocab_band=7,
    grammar_band=8,
    question="Should cars be banned from city centers?",
    transcript="There is a compelling case for banning them. Car-free zones significantly reduce air and noise pollution, creating a healthier environment. They also encourage walking and cycling, which boosts public health. Moreover, reclaiming streets for pedestrians can revitalize local businesses. While it might cause inconvenience for some drivers, the long-term benefits for the community are undeniable.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'compelling', 'zones', 'reclaiming', 'revitalize', 'inconvenience', 'undeniable'. >Band 6: Precise terms. Not Band 8: Lacks 'pedestrianize', 'congestion'.",
    grammar_reason="[GRA8] Wide range: 'There is a compelling case...', 'creating a healthier environment', 'While it might cause...'. Error-free. >Band 7: Sophisticated structure.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 588: V7/G8 - Topic: Education (Skills)
samples.append(create_sample(
    index=588,
    vocab_band=7,
    grammar_band=8,
    question="Are practical skills more important than academic ones?",
    transcript="Both are necessary, but their importance depends on the context. Academic skills develop critical thinking and theoretical knowledge, which are vital for research and innovation. However, practical skills are essential for daily life and many trades. We need plumbers as much as we need philosophers. An education system should value both equally, rather than prioritizing one over the other.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'context', 'theoretical', 'vital', 'trades', 'philosophers', 'prioritizing'. >Band 6: Good range. Not Band 8: Lacks 'vocational', 'hands-on', 'competence'.",
    grammar_reason="[GRA8] Wide range: 'which are vital...', 'as much as...', 'rather than prioritizing...'. Majority error-free. >Band 7: Accurate complex sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 589: V7/G8 - Topic: Society (Aging)
samples.append(create_sample(
    index=589,
    vocab_band=7,
    grammar_band=8,
    question="What are the challenges of an aging population?",
    transcript="The primary challenge is the strain on the healthcare and pension systems. As the ratio of retirees to workers increases, the tax burden on the younger generation grows. This can lead to intergenerational conflict. Additionally, there may be a labor shortage in certain sectors. Governments need to implement innovative policies, such as raising the retirement age or encouraging immigration, to address these demographic shifts.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'strain', 'ratio', 'retirees', 'burden', 'intergenerational', 'sectors', 'implement', 'demographic shifts'. >Band 6: Advanced vocabulary. Not Band 8: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'As the ratio... increases...', 'such as raising...', 'to address these...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 590: V7/G8 - Topic: Work (Gender)
samples.append(create_sample(
    index=590,
    vocab_band=7,
    grammar_band=8,
    question="Why is there a gender pay gap?",
    transcript="It is a complex issue rooted in historical and structural factors. Women are often overrepresented in lower-paying industries. Furthermore, the 'motherhood penalty' means women's careers often stall when they have children, while men's do not. Discrimination and unconscious bias also play a role in hiring and promotion. Closing the gap requires not just policy changes, but a cultural shift in how we value work and caregiving.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'motherhood penalty' (specific term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'rooted', 'structural', 'overrepresented', 'stall', 'unconscious bias', 'caregiving'. Term: 'motherhood penalty'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'systemic', 'parity'.",
    grammar_reason="[GRA8] Wide range: 'while men's do not', 'requires not just..., but...'. Majority error-free. >Band 7: Complex sentence structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 591: V7/G8 - Topic: Environment (Water)
samples.append(create_sample(
    index=591,
    vocab_band=7,
    grammar_band=8,
    question="How can we conserve water?",
    transcript="We can start by adopting water-saving habits at home, such as fixing leaks and taking shorter showers. On a larger scale, agriculture consumes the vast majority of our fresh water. Implementing efficient irrigation techniques, like drip irrigation, would make a huge difference. Industries also need to recycle wastewater. Water is a finite resource, and we must treat it with the value it deserves.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'adopting', 'leaks', 'consumes', 'vast majority', 'efficient', 'irrigation', 'wastewater', 'finite'. >Band 6: Specific terms. Not Band 8: Lacks 'scarcity', 'management', 'sustainable'.",
    grammar_reason="[GRA8] Wide range: 'such as fixing...', 'Implementing... would make...', 'and we must treat...'. Error-free. >Band 7: Good use of gerunds.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 592: V7/G8 - Topic: Technology (Games)
samples.append(create_sample(
    index=592,
    vocab_band=7,
    grammar_band=8,
    question="Can video games be educational?",
    transcript="Certainly. Many games require strategic thinking, resource management, and problem-solving skills. Simulation games can teach history or city planning. Moreover, multiplayer games foster teamwork and communication in a digital environment. While they should not replace traditional learning, they can be a powerful supplementary tool. Gamification is increasingly being used in schools to engage students.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'gamification' (advanced term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'strategic', 'resource management', 'simulation', 'foster', 'supplementary', 'gamification', 'engage'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'cognitive', 'immersive', 'pedagogical'.",
    grammar_reason="[GRA8] Wide range: 'While they should not...', 'is increasingly being used...'. Majority error-free. >Band 7: Varied sentence structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 593: V7/G8 - Topic: Culture (Fashion)
samples.append(create_sample(
    index=593,
    vocab_band=7,
    grammar_band=8,
    question="Does fashion reflect society?",
    transcript="Yes, fashion is a mirror of the times. It reflects our values, economic status, and social attitudes. For example, the shift towards casual wear reflects a more relaxed and informal society. Fashion also allows for individual expression and rebellion against norms. It is not just about clothes; it is a cultural language that communicates who we are and what we stand for.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'mirror of the times' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'mirror', 'status', 'attitudes', 'casual wear', 'expression', 'rebellion', 'norms'. >Band 6: Good range. Not Band 8: Lacks 'zeitgeist', 'aesthetic', 'trend'.",
    grammar_reason="[GRA8] Wide range: 'towards casual wear reflects...', 'allows for...', 'communicates who we are'. Error-free. >Band 7: Sophisticated structure.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 594: V7/G8 - Topic: Society (Housing)
samples.append(create_sample(
    index=594,
    vocab_band=7,
    grammar_band=8,
    question="Why is there a housing crisis in many cities?",
    transcript="It is a result of supply not keeping up with demand. Urbanization has led to a population explosion in cities, but housing construction has lagged behind. Additionally, real estate is often treated as an investment rather than a human right, driving up prices. Zoning laws can also restrict new developments. To fix this, governments must prioritize affordable housing projects.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'supply', 'urbanization', 'explosion', 'lagged behind', 'investment', 'zoning laws', 'restrict', 'prioritize'. >Band 6: Advanced vocabulary. Not Band 8: Lacks 'speculation', 'gentrification', 'density'.",
    grammar_reason="[GRA8] Wide range: 'not keeping up with...', 'has led to..., but...', 'rather than...'. Majority error-free. >Band 7: Complex sentence variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 595: V7/G8 - Topic: Health (Exercise)
samples.append(create_sample(
    index=595,
    vocab_band=7,
    grammar_band=8,
    question="Why don't people exercise enough?",
    transcript="Modern life is inherently sedentary. We work at desks, drive cars, and relax in front of screens. This lack of movement is normalized. Also, many people perceive exercise as a chore or lack the time and energy after a long workday. However, prioritizing physical activity is essential. We need to integrate movement into our daily routines, like walking or cycling to work.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'inherently', 'sedentary', 'normalized', 'perceive', 'chore', 'prioritizing', 'integrate'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'commitment', 'wellness', 'lifestyle'.",
    grammar_reason="[GRA8] Wide range: 'We work..., drive..., and relax...', 'lack the time... after...', 'We need to integrate...'. Error-free. >Band 7: Good control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 596: V7/G8 - Topic: Transport (Flying)
samples.append(create_sample(
    index=596,
    vocab_band=7,
    grammar_band=8,
    question="Should we fly less?",
    transcript="From an environmental perspective, yes. Aviation is a major contributor to carbon emissions. Reducing air travel would significantly lower our personal carbon footprint. However, in a globalized world, flying is often necessary for business and family connections. Instead of stopping completely, we should fly responsibly, choose direct flights, and offset our carbon emissions. Ultimately, the industry needs to develop greener technologies.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'perspective', 'aviation', 'contributor', 'carbon footprint', 'globalized', 'responsibly', 'offset'. >Band 6: Precise terms. Not Band 8: Lacks 'sustainable', 'alternative', 'frequency'.",
    grammar_reason="[GRA8] Wide range: 'From an environmental perspective...', 'Instead of stopping...', 'needs to develop'. Majority error-free. >Band 7: Sophisticated sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 597: V7/G8 - Topic: Education (Reading)
samples.append(create_sample(
    index=597,
    vocab_band=7,
    grammar_band=8,
    question="Why is reading important for children?",
    transcript="Reading is fundamental for cognitive development. It expands vocabulary and improves language skills. Moreover, stories stimulate the imagination and foster empathy by allowing children to experience different lives. In an age of short attention spans, reading teaches patience and focus. Parents who read to their children give them a head start in life. It is a gift that lasts a lifetime.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'head start' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'fundamental', 'cognitive', 'stimulate', 'foster', 'empathy', 'attention spans'. Idiom: 'head start'. >Band 6: Very good vocabulary. Not Band 8: Lacks 'literacy', 'academic', 'comprehension'.",
    grammar_reason="[GRA8] Wide range: 'by allowing children...', 'In an age of...', 'Parents who read...'. Error-free. >Band 7: Complex structures used naturally.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 598: V7/G8 - Topic: Work (Job Hopping)
samples.append(create_sample(
    index=598,
    vocab_band=7,
    grammar_band=8,
    question="Why do people change careers?",
    transcript="People seek fulfillment and growth. Staying in the same job for decades can lead to stagnation. Changing careers allows individuals to learn new skills and face new challenges. It can also be a way to increase earnings or escape a toxic work environment. In the modern economy, adaptability is valued. Career paths are no longer linear; they are fluid and evolving.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'fulfillment', 'stagnation', 'toxic', 'adaptability', 'valued', 'linear', 'fluid', 'evolving'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'trajectory', 'reinvent', 'prospects'.",
    grammar_reason="[GRA8] Wide range: 'Staying in the same job...', 'allows individuals to...', 'Career paths are no longer...'. Majority error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 599: V7/G8 - Topic: Society (Volunteering)
samples.append(create_sample(
    index=599,
    vocab_band=7,
    grammar_band=8,
    question="Do you think volunteering is important?",
    transcript="I believe it is vital for a healthy society. Volunteering bridges the gap between different social groups and fosters a sense of community. It provides essential support to those in need, where government services might fall short. For the volunteer, it offers a sense of purpose and a chance to give back. It is a mutually beneficial arrangement that strengthens the social fabric.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'fall short' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'vital', 'bridges', 'fosters', 'essential', 'beneficial', 'arrangement', 'fabric'. Idiom: 'fall short'. >Band 6: Good range. Not Band 8: Lacks 'solidarity', 'altruism', 'civic'.",
    grammar_reason="[GRA8] Wide range: 'where government services might...', 'For the volunteer...', 'that strengthens...'. Error-free. >Band 7: Accurate complex structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 600: V7/G8 - Topic: Technology (Data)
samples.append(create_sample(
    index=600,
    vocab_band=7,
    grammar_band=8,
    question="Should we be concerned about data privacy?",
    transcript="We should be extremely concerned. In the digital age, data is a valuable commodity. Tech giants collect vast amounts of information about our habits and preferences. This data can be used to manipulate our behavior or even influence elections. If we lose control of our privacy, we lose our freedom. We need robust laws to protect our digital rights and ensure transparency.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'commodity', 'vast', 'preferences', 'manipulate', 'influence', 'robust', 'transparency'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'surveillance', 'consent', 'exploitation'.",
    grammar_reason="[GRA8] Wide range: 'can be used to...', 'If we lose..., we lose...', 'We need robust laws to...'. Majority error-free. >Band 7: Good use of passive and conditionals.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
