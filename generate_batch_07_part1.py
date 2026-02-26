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

# --- BATCH 07 PART 1: SAMPLES 551-575 (25 Total) ---
# Combo: V7/G8 (Good Vocab, Very Good Grammar)

# Sample 551: V7/G8 - Topic: Environment (Sustainability)
samples.append(create_sample(
    index=551,
    vocab_band=7,
    grammar_band=8,
    question="Why is it important to live sustainably?",
    transcript="If we continue to exploit our natural resources at the current rate, we will inevitably face catastrophic consequences. Sustainable living ensures that we do not compromise the ability of future generations to meet their own needs. It is not merely about recycling; it is about fundamentally shifting our mindset. Unless we take drastic action now, the damage to our ecosystem will be irreversible. Therefore, adopting a sustainable lifestyle is an moral imperative.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'exploit', 'inevitably', 'catastrophic', 'compromise', 'mindset', 'drastic', 'irreversible', 'imperative'. >Band 6: Precise and flexible. Not Band 8: Lacks idiomatic nuance.",
    grammar_reason="[GRA8] Wide range of structures used flexibly. 'If we continue...', 'It is not merely..., it is about...', 'Unless we take...'. Majority of sentences are error-free. >Band 7: No systematic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 552: V7/G8 - Topic: Technology (AI)
samples.append(create_sample(
    index=552,
    vocab_band=7,
    grammar_band=8,
    question="Should we fear artificial intelligence?",
    transcript="While apprehension is understandable, I believe fear is misplaced. AI has the potential to revolutionize industries, from healthcare to transportation. The key lies in how we regulate its development. If we establish strict ethical guidelines, AI can serve as a powerful tool for human advancement. However, should we fail to control it, the risks could outweigh the benefits. Ultimately, it is a tool, and its impact depends on the user.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'apprehension', 'misplaced', 'revolutionize', 'regulate', 'ethical guidelines', 'advancement', 'outweigh'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal/academic.",
    grammar_reason="[GRA8] Wide range: 'While apprehension is...', 'The key lies in...', 'should we fail to control it' (inversion). >Band 7: Sophisticated structures used accurately.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 553: V7/G8 - Topic: Education (University)
samples.append(create_sample(
    index=553,
    vocab_band=7,
    grammar_band=8,
    question="Is higher education necessary for a successful career?",
    transcript="Not necessarily. Although a degree opens doors in certain specialized fields, such as medicine or law, it is not the only path to success. Vocational training and apprenticeships offer valuable practical skills that are highly sought after by employers. In fact, many successful entrepreneurs never attended university. What matters most is a willingness to learn and adapt, which can be acquired outside of a formal academic setting.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'specialized fields', 'vocational training', 'apprenticeships', 'sought after', 'entrepreneurs', 'adapt', 'academic setting'. >Band 6: Good collocation. Not Band 8: Lacks flair.",
    grammar_reason="[GRA8] Wide range: 'Although a degree...', 'such as...', 'What matters most is...'. Error-free sentences predominate. >Band 7: Flexibility in complex structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 554: V7/G8 - Topic: Society (Cities)
samples.append(create_sample(
    index=554,
    vocab_band=7,
    grammar_band=8,
    question="What makes a city livable?",
    transcript="A livable city is one that prioritizes the well-being of its residents. This includes having accessible green spaces, efficient public transport, and a low crime rate. Moreover, a sense of community is vital. When people feel connected to their neighbors, they are happier and safer. Urban planning should focus on creating environments that foster social interaction, rather than just building more skyscrapers. Quality of life must be the main goal.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'prioritizes', 'well-being', 'accessible', 'efficient', 'urban planning', 'foster', 'skyscrapers'. >Band 6: Precise terms. Not Band 8: Lacks idiomatic flow.",
    grammar_reason="[GRA8] Wide range: 'one that prioritizes...', 'When people feel...', 'rather than just building...'. Majority error-free. >Band 7: Complex structures used naturally.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 555: V7/G8 - Topic: Work (Remote)
samples.append(create_sample(
    index=555,
    vocab_band=7,
    grammar_band=8,
    question="Is remote work the future?",
    transcript="It certainly seems that way. The pandemic accelerated a shift that was already happening. Remote work offers unparalleled flexibility, allowing employees to balance their professional and personal lives more effectively. Furthermore, companies can hire talent from anywhere in the world, breaking down geographical barriers. While some face-to-face interaction is still valuable, the hybrid model appears to be the most sustainable solution for the modern workforce.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'accelerated', 'shift', 'unparalleled', 'flexibility', 'geographical barriers', 'hybrid model', 'sustainable'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'paradigm', 'ubiquitous'.",
    grammar_reason="[GRA8] Wide range: 'accelerated a shift that was...', 'allowing employees to...', 'While some...'. Error-free. >Band 7: High level of accuracy and variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 556: V7/G8 - Topic: Culture (Globalization)
samples.append(create_sample(
    index=556,
    vocab_band=7,
    grammar_band=8,
    question="Does globalization lead to cultural loss?",
    transcript="There is a risk of cultural homogenization, where local traditions are overshadowed by global trends. For instance, fast food chains are replacing traditional eateries in many countries. However, globalization also facilitates the spread of culture. We can now enjoy music, art, and food from all over the globe. The challenge lies in finding a balance between embracing the new and preserving the old. Cultural exchange should be a two-way street.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'homogenization', 'overshadowed', 'trends', 'eateries', 'facilitates', 'preserving'. Idiom: 'two-way street'. >Band 6: Sophisticated terms. Not Band 8: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'where local traditions are...', 'The challenge lies in...', 'should be a two-way street'. Majority error-free. >Band 7: Control of complex forms.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 557: V7/G8 - Topic: Health (Diet)
samples.append(create_sample(
    index=557,
    vocab_band=7,
    grammar_band=8,
    question="Why are plant-based diets becoming popular?",
    transcript="Increasingly, people are becoming aware of the environmental impact of meat production. Rearing livestock consumes vast resources and contributes significantly to greenhouse gas emissions. Consequently, many are choosing plant-based diets to reduce their carbon footprint. Additionally, there are health benefits, as such diets are often lower in saturated fats. It is a conscious choice that reflects a growing concern for both personal health and the planet's well-being.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'rearing livestock', 'consumes', 'greenhouse gas', 'emissions', 'carbon footprint', 'saturated fats', 'conscious choice'. >Band 6: Strong topic vocabulary. Not Band 8: Lacks 'mitigate', 'ethical'.",
    grammar_reason="[GRA8] Wide range: 'Increasingly, people are...', 'as such diets are...', 'that reflects a growing concern'. Error-free sentences. >Band 7: Sophisticated structure.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 558: V7/G8 - Topic: Transport (Public)
samples.append(create_sample(
    index=558,
    vocab_band=7,
    grammar_band=8,
    question="How can we improve public transport?",
    transcript="Investment is key. Governments must allocate funds to upgrade infrastructure and expand networks. If trains and buses were more reliable and frequent, more people would leave their cars at home. Moreover, making public transport affordable is essential to encourage usage. Integrated ticketing systems, which allow seamless travel between different modes of transport, would also enhance the user experience. Efficiency and convenience are the primary drivers of change.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'allocate funds', 'infrastructure', 'reliable', 'integrated ticketing', 'seamless', 'enhance', 'primary drivers'. >Band 6: Precise vocabulary. Not Band 8: Lacks 'incentivize', 'congestion'.",
    grammar_reason="[GRA8] Wide range: 'If trains... were... would...', 'making public transport affordable...', 'which allow...'. Majority error-free. >Band 7: Complex conditionals and relative clauses.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 559: V7/G8 - Topic: Society (Crime)
samples.append(create_sample(
    index=559,
    vocab_band=7,
    grammar_band=8,
    question="Is punishment the best way to stop crime?",
    transcript="While punishment serves as a deterrent, it does not address the root causes of crime. Many offenders come from disadvantaged backgrounds where opportunities are scarce. Therefore, rehabilitation should be the focus. By providing education and vocational training in prisons, we can help inmates reintegrate into society. Punishment without support merely creates a cycle of reoffending. We must look at the bigger picture to solve the problem.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'deterrent', 'root causes', 'offenders', 'disadvantaged', 'scarce', 'reintegrate', 'reoffending'. >Band 6: Good range. Not Band 8: Lacks 'recidivism', 'punitive'.",
    grammar_reason="[GRA8] Wide range: 'While punishment serves...', 'By providing...', 'where opportunities are scarce'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 560: V7/G8 - Topic: Technology (Communication)
samples.append(create_sample(
    index=560,
    vocab_band=7,
    grammar_band=8,
    question="Has social media improved communication?",
    transcript="It has certainly increased the quantity of communication, but I question the quality. We are more connected than ever, yet many people feel isolated. Social media encourages superficial interactions rather than deep, meaningful conversations. Furthermore, the anonymity of the internet often leads to hostility and misunderstanding. While it is a useful tool for staying in touch, it cannot replace the nuance and empathy of face-to-face dialogue.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'quantity', 'isolated', 'superficial', 'anonymity', 'hostility', 'misunderstanding', 'nuance', 'empathy'. >Band 6: Precise terms. Not Band 8: Lacks 'paradox', 'facade'.",
    grammar_reason="[GRA8] Wide range: 'It has certainly increased...', 'encourages... rather than...', 'While it is...'. Majority error-free. >Band 7: Varied and accurate.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 561: V7/G8 - Topic: Work (Job Satisfaction)
samples.append(create_sample(
    index=561,
    vocab_band=7,
    grammar_band=8,
    question="What contributes to job satisfaction?",
    transcript="Beyond a fair salary, employees seek a sense of purpose. Knowing that their work makes a difference is highly motivating. Autonomy is also crucial; people want to be trusted to manage their own tasks. Additionally, a supportive work environment, where colleagues collaborate rather than compete, fosters happiness. When employees feel valued and challenged, they are likely to be satisfied and productive.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'seek', 'motivating', 'autonomy', 'manage', 'collaborate', 'fosters', 'valued', 'productive'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'recognition', 'fulfillment', 'micromanagement'.",
    grammar_reason="[GRA8] Wide range: 'Knowing that...', 'where colleagues collaborate...', 'When employees feel...'. Error-free. >Band 7: Complex sentences used naturally.",
    idiom_present=False,
    risk_level="low"
))

# Sample 562: V7/G8 - Topic: Education (Skills)
samples.append(create_sample(
    index=562,
    vocab_band=7,
    grammar_band=8,
    question="Should schools teach critical thinking?",
    transcript="Absolutely. In the information age, the ability to analyze and evaluate sources is indispensable. Students are bombarded with data, and they need to distinguish between fact and opinion. Critical thinking empowers them to make informed decisions and solve complex problems. Rather than rote memorization, schools should encourage questioning and debate. This skill is essential for navigating the modern world.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'information age', 'analyze', 'evaluate', 'indispensable', 'bombarded', 'distinguish', 'empowers', 'rote memorization'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'cognitive', 'scrutinize'.",
    grammar_reason="[GRA8] Wide range: 'the ability to...', 'Rather than...', 'This skill is essential for navigating...'. Majority error-free. >Band 7: Good control of gerunds and infinitives.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 563: V7/G8 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=563,
    vocab_band=7,
    grammar_band=8,
    question="Why should we care about biodiversity?",
    transcript="Biodiversity is the foundation of a healthy ecosystem. Every species, no matter how small, plays a role in maintaining the balance of nature. If we lose biodiversity, we risk ecosystem collapse, which would directly affect human survival. For instance, bees are essential for pollination. Without them, our food supply would be threatened. Protecting nature is not just altruistic; it is a matter of self-preservation.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'foundation', 'ecosystem', 'maintaining', 'collapse', 'pollination', 'altruistic', 'self-preservation'. >Band 6: Advanced terms. Not Band 8: Lacks 'interconnected', 'fragility'.",
    grammar_reason="[GRA8] Wide range: 'no matter how small', 'If we lose..., we risk...', 'Without them...'. Error-free. >Band 7: Sophisticated conditionals.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 564: V7/G8 - Topic: Culture (Art)
samples.append(create_sample(
    index=564,
    vocab_band=7,
    grammar_band=8,
    question="Why is art important in society?",
    transcript="Art serves as a mirror to society, reflecting our values, struggles, and aspirations. It challenges us to think differently and see the world from new perspectives. Moreover, art preserves our history and cultural heritage. It is a universal language that transcends borders. A society without art would be culturally impoverished. Therefore, supporting the arts is investing in the soul of a nation.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'soul of a nation' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'mirror', 'aspirations', 'challenges', 'perspectives', 'preserves', 'transcends', 'impoverished'. Metaphor: 'soul of a nation'. >Band 6: Very good range. Not Band 8: Lacks 'provocative', 'aesthetic'.",
    grammar_reason="[GRA8] Wide range: 'serves as a...', 'challenges us to think...', 'A society without art would be...'. Majority error-free. >Band 7: Accurate use of modal verbs and participles.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 565: V7/G8 - Topic: Society (Friendship)
samples.append(create_sample(
    index=565,
    vocab_band=7,
    grammar_band=8,
    question="How has technology changed friendship?",
    transcript="It has redefined how we connect. We can maintain friendships across vast distances, which was impossible in the past. Social media allows us to stay updated on our friends' lives instantly. However, it has also led to a superficiality in relationships. A 'like' is not the same as a conversation. While we have more connections, they might lack the depth and intimacy of traditional friendships.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'redefined', 'vast distances', 'updated', 'superficiality', 'connections', 'depth', 'intimacy'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'virtual', 'interaction'.",
    grammar_reason="[GRA8] Wide range: 'which was impossible', 'allows us to stay', 'While we have...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 566: V7/G8 - Topic: Technology (Robots)
samples.append(create_sample(
    index=566,
    vocab_band=7,
    grammar_band=8,
    question="Will robots take over all jobs?",
    transcript="It is highly unlikely that robots will replace all human labor. While they excel at repetitive and dangerous tasks, they lack the emotional intelligence and creativity required for many professions. Jobs in healthcare, education, and the arts rely on human connection, which machines cannot replicate. Instead of replacing us, robots will likely work alongside us, enhancing our productivity and handling mundane tasks.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'unlikely', 'excel', 'repetitive', 'emotional intelligence', 'rely on', 'replicate', 'enhancing', 'mundane'. >Band 6: Precise terms. Not Band 8: Lacks 'collaborate', 'automation', 'nuance'.",
    grammar_reason="[GRA8] Wide range: 'It is highly unlikely that...', 'While they excel...', 'Instead of replacing us...'. Majority error-free. >Band 7: Sophisticated comparison and contrast.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 567: V7/G8 - Topic: Work (Job)
samples.append(create_sample(
    index=567,
    vocab_band=7,
    grammar_band=8,
    question="Is it better to be a leader or a follower?",
    transcript="Both roles are essential for a functioning organization. Leaders provide vision and direction, but they cannot achieve their goals without dedicated followers to execute the plans. Being a follower does not mean being passive; it involves active contribution and teamwork. In fact, good followers often make the best leaders because they understand the dynamics of the team. Ideally, one should be adaptable enough to take on either role.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'functioning', 'vision', 'execute', 'passive', 'contribution', 'dynamics', 'adaptable'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'hierarchy', 'initiative', 'delegate'.",
    grammar_reason="[GRA8] Wide range: 'but they cannot...', 'Being a follower does not mean...', 'because they understand...'. Error-free. >Band 7: Varied sentence beginnings.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 568: V7/G8 - Topic: Environment (Climate)
samples.append(create_sample(
    index=568,
    vocab_band=7,
    grammar_band=8,
    question="Can we rely on technology to save the planet?",
    transcript="Technology is a crucial tool, but it is not a magic wand. Innovations like carbon capture and renewable energy are vital. However, technology alone cannot solve the crisis if our consumption habits remain unchanged. We need political will and a shift in societal values. Relying solely on a technological fix is dangerous because it delays necessary behavioral changes. It must be part of a broader strategy.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'magic wand' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'crucial', 'innovations', 'carbon capture', 'consumption habits', 'societal values', 'solely', 'behavioral'. Idiom: 'magic wand'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'mitigation', 'complacency'.",
    grammar_reason="[GRA8] Wide range: 'Innovations like...', 'if our consumption...', 'Relying solely on...'. Majority error-free. >Band 7: Complex noun phrases.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 569: V7/G8 - Topic: Transport (Safety)
samples.append(create_sample(
    index=569,
    vocab_band=7,
    grammar_band=8,
    question="Why do accidents happen on the road?",
    transcript="Human error is the predominant cause. Distractions, such as using a mobile phone, significantly reduce reaction times. Speeding is another major factor; drivers often overestimate their ability to control the vehicle. Fatigue also plays a role, as tired drivers are less alert. While road conditions and mechanical failures contribute, the vast majority of accidents could be prevented if drivers were more responsible and attentive.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'predominant', 'distractions', 'reaction times', 'overestimate', 'fatigue', 'mechanical failures', 'prevented', 'attentive'. >Band 6: Advanced terms. Not Band 8: Lacks 'negligence', 'impairment'.",
    grammar_reason="[GRA8] Wide range: 'Distractions, such as...', 'as tired drivers are...', 'could be prevented if...'. Error-free. >Band 7: Sophisticated clause structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 570: V7/G8 - Topic: Education (Reading)
samples.append(create_sample(
    index=570,
    vocab_band=7,
    grammar_band=8,
    question="Does reading fiction improve empathy?",
    transcript="Research suggests that it does. When we read fiction, we are transported into the minds of characters. We experience their struggles and emotions, which helps us understand perspectives different from our own. This process strengthens our ability to empathize with others in real life. Unlike non-fiction, which deals with facts, fiction deals with the human condition, making it a powerful tool for emotional growth.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'transported', 'struggles', 'perspectives', 'strengthens', 'empathize', 'human condition', 'emotional growth'. >Band 6: Good range. Not Band 8: Lacks 'narrative', 'vicarious', 'identification'.",
    grammar_reason="[GRA8] Wide range: 'When we read...', 'which helps us understand...', 'making it a powerful tool'. Majority error-free. >Band 7: Good use of participles.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 571: V7/G8 - Topic: Culture (Language)
samples.append(create_sample(
    index=571,
    vocab_band=7,
    grammar_band=8,
    question="Why do languages die out?",
    transcript="Languages usually die out due to cultural assimilation. When a dominant culture imposes its language, minority languages are often marginalized. Younger generations might stop learning their ancestral tongue to access better economic opportunities. Once the last native speakers pass away, the language is lost forever. This is a tragedy because language carries unique knowledge and history. Preservation efforts are critical to save linguistic diversity.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'assimilation', 'dominant', 'marginalized', 'ancestral tongue', 'native speakers', 'tragedy', 'preservation', 'linguistic diversity'. >Band 6: Sophisticated vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'When a dominant culture...', 'Once the last native speakers...', 'This is a tragedy because...'. Error-free. >Band 7: Complex time clauses.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 572: V7/G8 - Topic: Society (Cities)
samples.append(create_sample(
    index=572,
    vocab_band=7,
    grammar_band=8,
    question="What problems do megacities face?",
    transcript="Megacities face immense challenges, primarily regarding infrastructure. The rapid population growth often outpaces the development of housing and transport, leading to overcrowding and congestion. Pollution is another severe issue, affecting the health of millions. Additionally, the gap between rich and poor is often stark in these metropolises. Managing resources like water and waste becomes a logistical nightmare. Sustainable urban planning is the only way forward.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'logistical nightmare' (collocation)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'immense', 'infrastructure', 'outpaces', 'congestion', 'severe', 'stark', 'metropolises', 'sustainable'. Idiom: 'logistical nightmare'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'strain', 'inequality', 'sanitation'.",
    grammar_reason="[GRA8] Wide range: 'regarding infrastructure', 'leading to overcrowding', 'Managing resources... becomes...'. Majority error-free. >Band 7: Use of participial phrases.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 573: V7/G8 - Topic: Technology (Internet)
samples.append(create_sample(
    index=573,
    vocab_band=7,
    grammar_band=8,
    question="Is the internet making us less intelligent?",
    transcript="I wouldn't say less intelligent, but perhaps less focused. The internet provides instant access to information, which means we no longer need to memorize facts. This externalization of memory changes how our brains work. We are becoming better at finding information but worse at retaining it. However, the internet also offers unlimited educational resources. It is a tool that can either enhance or degrade our intellect, depending on usage.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'focused', 'instant access', 'externalization', 'retaining', 'unlimited', 'enhance', 'degrade', 'intellect'. >Band 6: Advanced vocabulary. Not Band 8: Lacks 'cognitive', 'shallow', 'processing'.",
    grammar_reason="[GRA8] Wide range: 'which means we...', 'becoming better at finding... but worse at...', 'depending on usage'. Error-free. >Band 7: Complex contrasts.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 574: V7/G8 - Topic: Work (Gender)
samples.append(create_sample(
    index=574,
    vocab_band=7,
    grammar_band=8,
    question="Why is there a gender pay gap?",
    transcript="The pay gap is complex and stems from multiple factors. Historically, women have been concentrated in lower-paying industries. There is also the 'motherhood penalty', where women's careers stall due to childcare responsibilities. Discrimination, though illegal, still exists in subtle forms. Women are sometimes less likely to negotiate for higher salaries. Closing the gap requires policy changes and a shift in cultural attitudes towards work and family.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'motherhood penalty' (specific term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'stems from', 'concentrated', 'stall', 'discrimination', 'subtle', 'negotiate', 'cultural attitudes'. Term: 'motherhood penalty'. >Band 6: Precise vocabulary. Not Band 8: Lacks 'systemic', 'glass ceiling', 'parity'.",
    grammar_reason="[GRA8] Wide range: 'where women's careers...', 'though illegal', 'Closing the gap requires...'. Majority error-free. >Band 7: Sophisticated clause structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 575: V7/G8 - Topic: Society (Consumerism)
samples.append(create_sample(
    index=575,
    vocab_band=7,
    grammar_band=8,
    question="How can we be ethical consumers?",
    transcript="Being an ethical consumer means being informed. We should research the companies we buy from to ensure they treat workers fairly and respect the environment. Avoiding fast fashion and disposable products is a good start. We can support local businesses and buy fair trade goods. It is about voting with our wallets. Although it might cost more, the moral value of supporting ethical practices is worth the price.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'voting with our wallets' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR7] Uses less common items: 'informed', 'ensure', 'disposable', 'fair trade', 'moral value', 'practices'. Idiom: 'voting with our wallets'. >Band 6: Good range. Not Band 8: Lacks 'transparency', 'supply chain', 'exploitation'.",
    grammar_reason="[GRA8] Wide range: 'means being informed', 'to ensure they treat...', 'Although it might cost more...'. Error-free. >Band 7: Accurate gerunds and conditionals.",
    idiom_present=True,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Generated {len(samples)} samples in {OUTPUT_FILE}")
