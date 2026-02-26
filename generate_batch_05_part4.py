import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch05.jsonl")

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

# --- BATCH 05 PART 4: SAMPLES 426-450 (25 Total) ---
# Combo: V7/G6

# Sample 426: V7/G6 - Topic: Transport (Cities)
samples.append(create_sample(
    index=426,
    vocab_band=7,
    grammar_band=6,
    question="What are the benefits of walking?",
    transcript="It is the most natural form of exercise. It boosts circulation and improves cardiovascular health. Walking in nature is therapeutic. It reduces anxiety and clears the mind. It is also an eco-friendly mode of transport. No emissions. Cities should be designed for pedestrians. Wide pavements and safe crossings. It promotes a healthier, slower pace of life.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'pace of life' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'natural form', 'boosts circulation', 'cardiovascular', 'therapeutic', 'anxiety', 'eco-friendly', 'emissions', 'pedestrians', 'pavements', 'pace of life'. >Band 6: Strong vocabulary. Not Band 8: Lacks idiomatic expressions.",
    grammar_reason="[GRA6] Reason: 'It boosts circulation'. Passive: 'should be designed'. >Band 5: Accurate grammar. Not Band 7: Simple sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 427: V7/G6 - Topic: Health (Children)
samples.append(create_sample(
    index=427,
    vocab_band=7,
    grammar_band=6,
    question="How can we prevent childhood obesity?",
    transcript="We need a multi-faceted approach. Parents must encourage healthy eating habits. Providing nutritious meals instead of junk food. Schools should prioritize physical education. Make sports mandatory. Also, we need to regulate advertising. Fast food companies target children aggressively. This is unethical. By promoting an active lifestyle and balanced diet, we can reverse this trend.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'multi-faceted approach' (advanced term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'multi-faceted approach', 'nutritious', 'prioritize', 'mandatory', 'regulate', 'target', 'aggressively', 'unethical', 'promoting', 'reverse'. >Band 6: Sophisticated vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA6] Modals: 'Must encourage', 'Should prioritize'. Gerund: 'Providing nutritious meals'. >Band 5: Good control. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 428: V7/G6 - Topic: Technology (Communication)
samples.append(create_sample(
    index=428,
    vocab_band=7,
    grammar_band=6,
    question="Why do some people prefer texting to calling?",
    transcript="It is less intrusive. Calling demands immediate attention, which can be stressful. Texting allows you to respond at your convenience. It gives you time to formulate your thoughts. Also, it is efficient for conveying simple information. However, nuances and tone are lost in text. Misunderstandings occur easily. While texting is practical, voice calls build stronger connections.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'formulate your thoughts' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'intrusive', 'immediate attention', 'stressful', 'convenience', 'formulate', 'conveying', 'nuances', 'tone', 'misunderstandings', 'connections'. >Band 6: Precise vocabulary. Not Band 8: Lacks idiomatic usage.",
    grammar_reason="[GRA6] Relative clause: 'which can be stressful'. Contrast: 'However'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 429: V7/G6 - Topic: Society (Happiness)
samples.append(create_sample(
    index=429,
    vocab_band=7,
    grammar_band=6,
    question="Is happiness a choice?",
    transcript="To some degree, yes. Our mindset determines our outlook. We can choose to focus on the positive aspects of life. Practicing gratitude fosters happiness. However, external circumstances play a role. Poverty, illness, or trauma can make happiness difficult. We cannot simply choose to ignore suffering. But resilience helps us cope. Happiness is a combination of attitude and circumstance.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'practicing gratitude' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'mindset', 'determines', 'outlook', 'positive aspects', 'gratitude', 'fosters', 'external circumstances', 'trauma', 'resilience'. >Band 6: Advanced vocabulary. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA6] Contrast: 'However'. Reason: 'make happiness difficult'. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 430: V7/G6 - Topic: Work (Career)
samples.append(create_sample(
    index=430,
    vocab_band=7,
    grammar_band=6,
    question="How can people find a job they love?",
    transcript="They should identify their passions and strengths. Self-reflection is the first step. Then, they need to research industries that align with their interests. Networking is also crucial. Talking to professionals gives insight into the reality of the job. Internships offer hands-on experience. It might take time and experimentation. Finding a fulfilling career is a journey, not a destination.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'align with' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'identify', 'passions', 'self-reflection', 'align with', 'crucial', 'professionals', 'insight', 'internships', 'hands-on', 'fulfilling'. >Band 6: Strong vocabulary. Not Band 8: Slightly robotic.",
    grammar_reason="[GRA6] Sequencing: 'Then, they need...'. Gerund: 'Talking to professionals'. >Band 5: Good control. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 431: V7/G6 - Topic: Culture (Art)
samples.append(create_sample(
    index=431,
    vocab_band=7,
    grammar_band=6,
    question="Why is abstract art controversial?",
    transcript="Because it is open to interpretation. Unlike realistic art, it does not depict recognizable objects. Some people find this liberating. They enjoy the emotional impact of color and form. Others find it confusing or pretentious. They think it requires no skill. This debate is ongoing. However, art is subjective. What one person sees as a masterpiece, another sees as a mess.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'open to interpretation' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'interpretation', 'realistic', 'depict', 'recognizable', 'liberating', 'emotional impact', 'pretentious', 'debate', 'subjective', 'masterpiece'. >Band 6: Sophisticated terms. Not Band 8: Lacks idiomatic flair.",
    grammar_reason="[GRA6] Contrast: 'Unlike realistic art'. Relative clause: 'What one person sees'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 432: V7/G6 - Topic: Education (Teacher)
samples.append(create_sample(
    index=432,
    vocab_band=7,
    grammar_band=6,
    question="How can teachers motivate students?",
    transcript="By making learning relevant. If students see the practical application, they are more engaged. Teachers should also be encouraging. Positive reinforcement boosts confidence. Creating a stimulating environment is key. Group projects and interactive lessons keep students interested. A passionate teacher inspires curiosity. Fear of punishment is a poor motivator. Inspiration works better.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'practical application' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'relevant', 'practical application', 'engaged', 'encouraging', 'positive reinforcement', 'stimulating', 'interactive', 'passionate', 'curiosity', 'motivator'. >Band 6: Very good vocabulary. Not Band 8: Lacks fluency.",
    grammar_reason="[GRA6] Gerund: 'By making learning relevant'. Conditionals: 'If students see...'. >Band 5: Accurate grammar. Not Band 7: Simple sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 433: V7/G6 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=433,
    vocab_band=7,
    grammar_band=6,
    question="What happens to recycled waste?",
    transcript="It goes through a sorting process. Machines and workers separate materials like paper, glass, and plastic. Then, it is processed into raw materials. For example, plastic bottles are melted down to make new products. Like clothing or carpets. This conserves natural resources and saves energy. Recycling closes the loop. It turns waste into a valuable resource.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'closes the loop' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'sorting process', 'separate', 'processed', 'raw materials', 'melted down', 'conserves', 'natural resources', 'valuable'. Idiom: 'closes the loop'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA6] Passive: 'is processed', 'are melted down'. Sequencing: 'Then, it is...'. >Band 5: Good control. Not Band 7: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 434: V7/G6 - Topic: Transport (Safety)
samples.append(create_sample(
    index=434,
    vocab_band=7,
    grammar_band=6,
    question="Should there be an age limit for driving?",
    transcript="Safety is the priority. As people age, their reaction time slows down. Vision and hearing deteriorate. This can make driving dangerous. Therefore, regular health checks for elderly drivers are essential. If they are not fit to drive, their license should be revoked. It is a sensitive issue because driving represents independence. But public safety must come first.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'sensitive issue' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'priority', 'reaction time', 'deteriorate', 'dangerous', 'essential', 'revoked', 'sensitive issue', 'independence'. >Band 6: Advanced vocabulary. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA6] Reason: 'As people age'. Conditionals: 'If they are not fit...'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 435: V7/G6 - Topic: Technology (Robots)
samples.append(create_sample(
    index=435,
    vocab_band=7,
    grammar_band=6,
    question="Are robots good for the economy?",
    transcript="They increase productivity and efficiency. Robots can work 24/7 without rest. This lowers production costs. Companies become more profitable. However, there is a downside. Automation displaces workers. Low-skilled jobs are disappearing. We need to retrain the workforce. Education systems must adapt to the new reality. Robots create wealth, but we must ensure it is shared.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'displaces workers' (advanced term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'productivity', 'efficiency', 'production costs', 'profitable', 'downside', 'automation', 'displaces', 'retrain', 'workforce', 'adapt'. >Band 6: Relevant terms. Not Band 8: Lacks 'inequality', 'redistribution'.",
    grammar_reason="[GRA6] Contrast: 'However', 'but we must ensure'. Modals: 'Must adapt'. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 436: V7/G6 - Topic: Society (Cities)
samples.append(create_sample(
    index=436,
    vocab_band=7,
    grammar_band=6,
    question="Why do some people dislike cities?",
    transcript="They find them overwhelming. The noise, the crowds, and the pollution can be stressful. The pace of life is frantic. There is no time to relax. Also, the cost of living is exorbitant. Rent is high. Some people prefer the tranquility of the countryside. They value community and nature. Cities can feel anonymous and cold.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'frantic' (advanced adjective)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'overwhelming', 'pollution', 'stressful', 'pace of life', 'frantic', 'exorbitant', 'tranquility', 'value', 'anonymous'. >Band 6: Strong vocabulary. Not Band 8: Slightly list-like.",
    grammar_reason="[GRA6] Reason: 'The noise... can be stressful'. Contrast: 'Some people prefer...'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 437: V7/G6 - Topic: Culture (Global)
samples.append(create_sample(
    index=437,
    vocab_band=7,
    grammar_band=6,
    question="Is it important to speak a second language?",
    transcript="In a globalized world, it is a huge asset. It opens doors to employment and travel. You can communicate with people from diverse backgrounds. It broadens your horizons. Also, it is good for the brain. Learning a language improves cognitive function. While translation technology is improving, it cannot replace human connection. Speaking the local language shows respect.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'broadens your horizons' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'globalized', 'asset', 'employment', 'diverse', 'cognitive function', 'translation', 'replace', 'connection'. Idiom: 'broadens your horizons'. >Band 6: Sophisticated terms. Not Band 8: Lacks fluency.",
    grammar_reason="[GRA6] Contrast: 'While translation technology...'. Reason: 'It opens doors'. >Band 5: Accurate complex sentences. Not Band 7: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 438: V7/G6 - Topic: Work (Job)
samples.append(create_sample(
    index=438,
    vocab_band=7,
    grammar_band=6,
    question="What makes a company a good place to work?",
    transcript="A positive company culture is paramount. Employees should feel valued and heard. Opportunities for professional development are also key. Training and promotion motivate staff. Furthermore, fair compensation and benefits are expected. Work-life balance is increasingly important. If a company respects its workers' time, loyalty increases. A toxic environment drives talent away.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'paramount' (advanced adjective)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'culture', 'paramount', 'valued', 'professional development', 'promotion', 'compensation', 'benefits', 'loyalty', 'toxic'. >Band 6: Precise vocabulary. Not Band 8: Lacks idiomatic flow.",
    grammar_reason="[GRA6] Modals: 'Should feel'. Conditionals: 'If a company respects...'. >Band 5: Accurate grammar. Not Band 7: Simple sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 439: V7/G6 - Topic: Society (Volunteer)
samples.append(create_sample(
    index=439,
    vocab_band=7,
    grammar_band=6,
    question="How does volunteering benefit the community?",
    transcript="It fills gaps in social services. Volunteers support the vulnerable, like the elderly or homeless. They provide essential care that the government cannot always afford. It strengthens social cohesion. People working together for a common cause builds trust. Also, it fosters civic responsibility. When citizens are active, the community thrives. It creates a kinder society.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'social cohesion' (advanced term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'gaps', 'social services', 'vulnerable', 'essential', 'afford', 'social cohesion', 'civic responsibility', 'thrives'. >Band 6: Advanced vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA6] Relative clause: 'that the government cannot'. Reason: 'It fills gaps'. >Band 5: Accurate grammar. Not Band 7: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 440: V7/G6 - Topic: Environment (Trees)
samples.append(create_sample(
    index=440,
    vocab_band=7,
    grammar_band=6,
    question="What threatens forests today?",
    transcript="Deforestation is the primary threat. Trees are cut down for logging and agriculture. This destroys habitats and reduces biodiversity. Climate change also plays a role. Droughts and wildfires are becoming more frequent and severe. Pests and diseases are spreading. Urban expansion is encroaching on forest land. We are losing our green lungs at an alarming rate.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'alarming rate' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'deforestation', 'primary threat', 'logging', 'habitats', 'biodiversity', 'droughts', 'wildfires', 'severe', 'encroaching', 'alarming rate'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'ecosystem', 'mitigation'.",
    grammar_reason="[GRA6] Reason: 'This destroys habitats'. Passive: 'are cut down'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 441: V7/G6 - Topic: Health (Exercise)
samples.append(create_sample(
    index=441,
    vocab_band=7,
    grammar_band=6,
    question="Is exercise important for mental health?",
    transcript="Crucially so. Physical activity releases endorphins, which are natural mood lifters. It reduces symptoms of anxiety and depression. Exercise also improves sleep quality. When you are rested, you feel better mentally. It provides a distraction from negative thoughts. Achieving fitness goals boosts self-esteem. The mind and body are interconnected. Treating one helps the other.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'mood lifters' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'crucially', 'endorphins', 'mood lifters', 'symptoms', 'anxiety', 'depression', 'distraction', 'self-esteem', 'interconnected'. >Band 6: Very good vocabulary. Not Band 8: Lacks 'therapeutic', 'psychological'.",
    grammar_reason="[GRA6] Relative clause: 'which are natural mood lifters'. Time clause: 'When you are rested'. >Band 5: Accurate grammar. Not Band 7: Simple structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 442: V7/G6 - Topic: Technology (Internet)
samples.append(create_sample(
    index=442,
    vocab_band=7,
    grammar_band=6,
    question="How can we stay safe online?",
    transcript="We must be vigilant. Use strong, unique passwords for every account. Two-factor authentication adds an extra layer of security. Be skeptical of emails from unknown sources. Phishing scams are sophisticated. Don't share personal details on public forums. Keep software updated to patch vulnerabilities. Digital literacy is the best defense against cyber threats.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'digital literacy' (advanced term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'vigilant', 'authentication', 'layer', 'skeptical', 'phishing scams', 'sophisticated', 'patch', 'vulnerabilities', 'digital literacy', 'cyber threats'. >Band 6: Technical vocabulary. Not Band 8: Slightly instructional.",
    grammar_reason="[GRA6] Imperatives: 'Use', 'Be', 'Don't share'. Reason: 'adds an extra layer'. >Band 5: Accurate grammar. Not Band 7: Mostly simple commands.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 443: V7/G6 - Topic: Transport (Traffic)
samples.append(create_sample(
    index=443,
    vocab_band=7,
    grammar_band=6,
    question="How can technology reduce traffic?",
    transcript="Smart traffic lights can optimize flow. They change based on real-time data. GPS apps help drivers avoid congestion. They suggest alternative routes. Autonomous vehicles could drive closer together safely, increasing road capacity. Also, remote work technology reduces the number of commuters. If we don't need to travel, the roads are emptier. Technology offers innovative solutions.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'optimize flow' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'optimize', 'real-time data', 'congestion', 'alternative routes', 'autonomous', 'capacity', 'commuters', 'innovative'. >Band 6: Good topic words. Not Band 8: Lacks 'efficiency', 'integrated'.",
    grammar_reason="[GRA6] Conditionals: 'If we don't need...'. Modals: 'Could drive'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 444: V7/G6 - Topic: Education (Reading)
samples.append(create_sample(
    index=444,
    vocab_band=7,
    grammar_band=6,
    question="What are the benefits of reading fiction?",
    transcript="It stimulates the imagination. You visualize worlds and characters. It develops empathy. You experience life through someone else's eyes. Fiction also improves vocabulary and language skills. It reduces stress by offering an escape from reality. Reading is a workout for the brain. It keeps the mind sharp and creative.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'workout for the brain' (metaphor)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'stimulates', 'visualize', 'empathy', 'vocabulary', 'escape', 'reality', 'workout', 'sharp'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'cognitive', 'perspective', 'narrative'.",
    grammar_reason="[GRA6] Reason: 'by offering an escape'. List structure. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 445: V7/G6 - Topic: Culture (Fashion)
samples.append(create_sample(
    index=445,
    vocab_band=7,
    grammar_band=6,
    question="Is the fashion industry sustainable?",
    transcript="Currently, no. Fast fashion is very wasteful. Clothes are made cheaply and thrown away quickly. This creates huge amounts of landfill. The industry consumes vast water and energy. It also uses toxic dyes. However, there is a movement towards sustainable fashion. Using organic materials and recycling fabrics. We need to shift from quantity to quality.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'fast fashion' (specific term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'sustainable', 'fast fashion', 'wasteful', 'landfill', 'consumes', 'vast', 'toxic dyes', 'organic', 'fabrics'. >Band 6: Precise terms. Not Band 8: Lacks 'ethical', 'supply chain', 'circular'.",
    grammar_reason="[GRA6] Passive: 'are made'. Gerund: 'Using organic materials'. >Band 5: Accurate grammar. Not Band 7: Simple sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 446: V7/G6 - Topic: Society (Cities)
samples.append(create_sample(
    index=446,
    vocab_band=7,
    grammar_band=6,
    question="Why is noise pollution a problem?",
    transcript="It affects our health invisibly. Constant noise from traffic or construction causes stress. It raises blood pressure. It disturbs sleep, leading to fatigue. It interferes with communication and concentration. Children in noisy schools learn less. Wildlife is also affected. Birds cannot hear each other sing. We need quieter cities for our sanity.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'invisibly' (adverb usage)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'invisibly', 'constant', 'blood pressure', 'disturbs', 'fatigue', 'interferes', 'concentration', 'sanity'. >Band 6: Good range. Not Band 8: Lacks 'chronic', 'psychological', 'mitigate'.",
    grammar_reason="[GRA6] Reason: 'leading to fatigue'. Passive: 'is also affected'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 447: V7/G6 - Topic: Work (Job)
samples.append(create_sample(
    index=447,
    vocab_band=7,
    grammar_band=6,
    question="Should companies allow flexible working hours?",
    transcript="Yes, it boosts morale. Employees feel trusted and respected. It allows them to manage childcare or hobbies. Productivity often increases because people work when they are most alert. It reduces rush hour traffic too. However, it requires good communication. Managers need to know when staff are available. Trust is the foundation of flexible work.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'boosts morale' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'boosts morale', 'manage', 'productivity', 'alert', 'rush hour', 'requires', 'foundation'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'autonomy', 'efficiency', 'work-life balance'.",
    grammar_reason="[GRA6] Reason: 'because people work...'. Contrast: 'However'. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 448: V7/G6 - Topic: Technology (Space)
samples.append(create_sample(
    index=448,
    vocab_band=7,
    grammar_band=6,
    question="Will space tourism become popular?",
    transcript="Eventually, yes. It is the ultimate adventure. Seeing Earth from space is a unique experience. Currently, it is the playground of the super-rich. The cost is prohibitive. But as technology advances, prices will drop. It might become like air travel today. However, safety concerns and environmental impact are major hurdles. It will take time.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'playground of the super-rich' (metaphor)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'eventually', 'ultimate', 'unique', 'playground', 'super-rich', 'prohibitive', 'advances', 'hurdles'. >Band 6: Sophisticated terms. Not Band 8: Lacks 'commercial', 'accessible', 'industry'.",
    grammar_reason="[GRA6] Future tense: 'will drop', 'might become'. Contrast: 'But as technology...'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 449: V7/G6 - Topic: Environment (Global Warming)
samples.append(create_sample(
    index=449,
    vocab_band=7,
    grammar_band=6,
    question="What is the role of individuals in saving the environment?",
    transcript="Collective individual action is powerful. We vote with our wallets. Buying sustainable products forces companies to change. Reducing meat consumption helps the climate. Using public transport lowers emissions. We can also influence policy by voting for green parties. Small changes accumulate. We cannot wait for governments to solve everything. We must take ownership.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'vote with our wallets' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'collective', 'sustainable', 'consumption', 'emissions', 'influence', 'policy', 'accumulate', 'ownership'. Idiom: 'vote with our wallets'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA6] Gerunds: 'Buying', 'Reducing', 'Using'. Modals: 'Must take'. >Band 5: Accurate grammar. Not Band 7: Simple sentence structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 450: V7/G6 - Topic: Society (Crime)
samples.append(create_sample(
    index=450,
    vocab_band=7,
    grammar_band=6,
    question="How can we prevent juvenile crime?",
    transcript="Prevention starts at home. Parents need to provide guidance and love. Neglect often leads to bad behavior. Schools also play a role. They should keep students engaged and offer support. After-school programs can keep kids off the streets. Mentorship is powerful. If young people have positive role models, they are less likely to offend. We need to invest in youth.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'juvenile crime' (specific term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'prevention', 'guidance', 'neglect', 'engaged', 'mentorship', 'role models', 'offend', 'invest'. >Band 6: Relevant terms. Not Band 8: Lacks 'delinquency', 'intervention', 'peer pressure'.",
    grammar_reason="[GRA6] Conditionals: 'If young people have...'. Modals: 'Should keep'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
