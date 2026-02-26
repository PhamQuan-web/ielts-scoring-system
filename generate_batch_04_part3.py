import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch04.jsonl")

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

# --- BATCH 04 PART 3: SAMPLES 301-325 (25 Total) ---
# Combo: V6/G6

# Sample 301: V6/G6 - Topic: Culture (Globalization)
samples.append(create_sample(
    index=301,
    vocab_band=6,
    grammar_band=6,
    question="Does globalization help or hurt small businesses?",
    transcript="It is a double-edged sword. On one side, it opens new markets. Small businesses can sell products online to the world. But on the other side, competition is fierce. Big multinational companies have more money. They can sell cheaper. It is hard for small shops to survive. They need to offer something unique. Something big brands cannot copy.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'double-edged sword' (idiom correctly used)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'markets', 'multinational', 'competition', 'fierce', 'survive', 'unique', 'copy'. Idiom: 'double-edged sword'. >Band 5: Idiom used well. Not Band 7: Slightly repetitive.",
    grammar_reason="[GRA6] Contrast: 'On one side... But on the other...'. Comparison: 'sell cheaper'. >Band 5: Accurate grammar. Not Band 7: Structure is standard.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 302: V6/G6 - Topic: Education (Skills)
samples.append(create_sample(
    index=302,
    vocab_band=6,
    grammar_band=6,
    question="What skills are most important for the future?",
    transcript="I think adaptability is number one. The world changes fast. You need to learn new things quickly. Also, critical thinking. Computers have information, but we need to analyze it. Creativity is also key. Robots cannot be creative yet. Finally, emotional intelligence. Working with people requires understanding feelings. These soft skills are more important than facts.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'adaptability' (advanced word)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'adaptability', 'critical thinking', 'analyze', 'creativity', 'emotional intelligence', 'soft skills'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'cognitive', 'innovation', 'interpersonal'.",
    grammar_reason="[GRA6] Comparison: 'more important than facts'. Contrast: 'but we need to analyze'. >Band 5: Error-free sentences. Not Band 7: Simple phrasing.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 303: V6/G6 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=303,
    vocab_band=6,
    grammar_band=6,
    question="Why is biodiversity important?",
    transcript="Because everything is connected. Plants and animals depend on each other. If we lose one species, the whole system can fail. For example, bees. They pollinate flowers. Without them, we have no food. Biodiversity makes the ecosystem strong. It helps us survive changes. Protecting nature is protecting ourselves.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'pollinate' (technical term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'connected', 'species', 'system', 'fail', 'pollinate', 'ecosystem', 'survive'. >Band 5: Scientific terms used correctly. Not Band 7: Lacks 'interdependent', 'resilience', 'collapse'.",
    grammar_reason="[GRA6] Conditionals: 'If we lose one species...'. Reason: 'Because everything is connected'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 304: V6/G6 - Topic: Society (Aging)
samples.append(create_sample(
    index=304,
    vocab_band=6,
    grammar_band=6,
    question="How can we support the elderly?",
    transcript="We need better healthcare for them. Old bodies are weak. Also, social support is vital. Many old people are lonely. We should visit them. Community centers can offer activities. To keep them active. Pensions should be higher too. So they can live with dignity. It is our duty to care for the generation that raised us.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'live with dignity' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'healthcare', 'vital', 'lonely', 'community centers', 'pensions', 'dignity', 'duty'. >Band 5: Good range. Not Band 7: Lacks 'welfare', 'isolation', 'retirement', 'obligation'.",
    grammar_reason="[GRA6] Modals: 'Should visit', 'Should be'. Purpose: 'To keep them active'. >Band 5: Accurate grammar. Not Band 7: Simple structure.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 305: V6/G6 - Topic: Technology (Data)
samples.append(create_sample(
    index=305,
    vocab_band=6,
    grammar_band=6,
    question="Who owns our personal data?",
    transcript="This is a big debate. Companies like Facebook collect our data. They say it is theirs because we use their service. But it is my information. My photos, my chats. I think individuals should own their data. We should have the right to delete it. Laws need to change to protect users. Privacy is a human right.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'human right' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'debate', 'collect', 'service', 'individuals', 'delete', 'laws', 'protect', 'privacy'. >Band 5: Clear vocabulary. Not Band 7: Lacks 'ownership', 'consent', 'regulation', 'exploit'.",
    grammar_reason="[GRA6] Contrast: 'But it is my information'. Modals: 'Should have', 'Need to'. >Band 5: Good control. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 306: V6/G6 - Topic: Work (Career)
samples.append(create_sample(
    index=306,
    vocab_band=6,
    grammar_band=6,
    question="Is it better to have one career or many?",
    transcript="In the past, people had one job for life. But now, it is different. Changing careers is common. It keeps life interesting. You learn new skills. However, one career offers stability. You become an expert in your field. I think changing is better. It stops you from getting bored. Adaptability is important today.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'job for life' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'careers', 'common', 'stability', 'expert', 'field', 'bored', 'adaptability'. >Band 5: Relevant terms. Not Band 7: Lacks 'path', 'specialization', 'diverse', 'security'.",
    grammar_reason="[GRA6] Comparison: 'Changing is better'. Contrast: 'However'. >Band 5: Accurate grammar. Not Band 7: Simple sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 307: V6/G6 - Topic: Transport (Safety)
samples.append(create_sample(
    index=307,
    vocab_band=6,
    grammar_band=6,
    question="What causes the most accidents on the road?",
    transcript="I think it is distraction. Drivers using mobile phones. They text or call while driving. This is very dangerous. Also, speeding is a major cause. People are in a hurry. They ignore the limit. Alcohol is another factor. Drunk driving kills many people. We need stricter penalties to stop this behavior. Education campaigns can help too.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'major cause' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'distraction', 'dangerous', 'speeding', 'ignore', 'factor', 'drunk driving', 'penalties', 'campaigns'. >Band 5: Strong vocabulary. Not Band 7: Lacks 'negligence', 'fatal', 'consequence', 'enforce'.",
    grammar_reason="[GRA6] Reason: 'I think it is distraction'. Gerunds: 'using mobile phones', 'speeding'. >Band 5: Accurate grammar. Not Band 7: Simple phrasing.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 308: V6/G6 - Topic: Education (Teacher)
samples.append(create_sample(
    index=308,
    vocab_band=6,
    grammar_band=6,
    question="How has teaching changed in recent years?",
    transcript="Technology has changed it a lot. Teachers use projectors and computers now. Not just chalk and board. Lessons are more interactive. Also, the relationship is different. Teachers are more like guides. They help students find answers. In the past, they were strict authorities. Now it is more friendly. Learning is student-centered.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'student-centered' (advanced term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'projectors', 'interactive', 'relationship', 'guides', 'strict', 'authorities', 'student-centered'. >Band 5: Good range. Not Band 7: Lacks 'methodology', 'facilitator', 'traditional', 'approach'.",
    grammar_reason="[GRA6] Comparison: 'More interactive', 'More friendly'. Contrast: 'In the past... Now...'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 309: V6/G6 - Topic: Culture (Art)
samples.append(create_sample(
    index=309,
    vocab_band=6,
    grammar_band=6,
    question="Should government fund art?",
    transcript="Yes, art is part of our culture. Museums and galleries need money to stay open. Artists need support to create. If the government doesn't help, art will become a business. Only popular art will survive. We might lose traditional or experimental art. Art feeds the soul of a nation. It is worth the investment.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'feeds the soul' (metaphor)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'galleries', 'support', 'create', 'survive', 'experimental', 'soul', 'investment'. >Band 5: Relevant vocabulary. Not Band 7: Lacks 'subsidize', 'heritage', 'commercial', 'enrich'.",
    grammar_reason="[GRA6] Conditionals: 'If the government doesn't help...'. Modals: 'Need to stay'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 310: V6/G6 - Topic: Health (Children)
samples.append(create_sample(
    index=310,
    vocab_band=6,
    grammar_band=6,
    question="Why is childhood obesity increasing?",
    transcript="It is because of lifestyle. Children don't play outside anymore. They stay inside with video games. They are sedentary. Also, diet is a problem. They eat processed food with lots of sugar. Parents are busy, so they buy fast food. It is quick but unhealthy. Schools need to promote sport and healthy eating to fix this.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'sedentary' (advanced word)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'lifestyle', 'sedentary', 'processed food', 'unhealthy', 'promote', 'fix'. >Band 5: Clear meaning. Not Band 7: Lacks 'consumption', 'calories', 'nutritional', 'epidemic'.",
    grammar_reason="[GRA6] Reason: 'Because of lifestyle'. Contrast: 'It is quick but unhealthy'. >Band 5: Accurate grammar. Not Band 7: Simple sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 311: V6/G6 - Topic: Society (Media)
samples.append(create_sample(
    index=311,
    vocab_band=6,
    grammar_band=6,
    question="How does the news affect people?",
    transcript="It affects our mood. If we watch bad news all day, we feel sad or scared. It creates anxiety. Also, it shapes our opinion. If the news is biased, we believe wrong things. We need to be careful. Check the source. Don't believe everything. Good news can inspire us, but it is rare on TV.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'shapes our opinion' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'mood', 'anxiety', 'shapes', 'opinion', 'biased', 'source', 'inspire', 'rare'. >Band 5: Good range. Not Band 7: Lacks 'influence', 'perspective', 'sensationalism', 'objective'.",
    grammar_reason="[GRA6] Conditionals: 'If we watch...', 'If the news is biased...'. >Band 5: Accurate complex sentences. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 312: V6/G6 - Topic: Environment (Plastic)
samples.append(create_sample(
    index=312,
    vocab_band=6,
    grammar_band=6,
    question="Can we live without plastic?",
    transcript="It would be very hard. Plastic is in everything. Computers, cars, medical tools. It is cheap and light. But we can reduce single-use plastic. Bags and bottles. We can use glass or metal instead. It takes effort, but it is possible. We need innovation to find new materials that are biodegradable. Nature cannot handle more plastic.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'biodegradable' (advanced word)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'medical tools', 'reduce', 'single-use', 'instead', 'innovation', 'materials', 'biodegradable', 'handle'. >Band 5: Advanced terms. Not Band 7: Lacks 'alternative', 'replace', 'ubiquitous', 'sustainable'.",
    grammar_reason="[GRA6] Contrast: 'But we can reduce'. Relative clause: 'materials that are...'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 313: V6/G6 - Topic: Technology (Communication)
samples.append(create_sample(
    index=313,
    vocab_band=6,
    grammar_band=6,
    question="Has technology made us lonely?",
    transcript="In a way, yes. We have hundreds of friends online, but maybe no real friends. We text, but don't talk. It is a shallow connection. People stare at screens at dinner. They ignore the person next to them. This causes isolation. However, technology also helps lonely people find groups. It connects similar minds. It depends on how you use it.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'shallow connection' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'shallow', 'connection', 'stare', 'ignore', 'isolation', 'similar minds'. >Band 5: Good vocabulary. Not Band 7: Lacks 'virtual', 'interaction', 'social skills', 'detach'.",
    grammar_reason="[GRA6] Contrast: 'but maybe no real friends'. Conditionals implied. >Band 5: Accurate grammar. Not Band 7: Simple structure.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 314: V6/G6 - Topic: Work (Gender)
samples.append(create_sample(
    index=314,
    vocab_band=6,
    grammar_band=6,
    question="Why are there few women in science?",
    transcript="It is historical. In the past, girls were told science is for boys. This stereotype is strong. Also, there are few role models. If girls don't see female scientists, they don't dream of it. Workplaces can be unfriendly too. But it is changing. Schools are encouraging girls now. We need diverse minds in science to solve problems.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'diverse minds' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'historical', 'stereotype', 'role models', 'female', 'unfriendly', 'encouraging', 'diverse'. >Band 5: Relevant terms. Not Band 7: Lacks 'bias', 'gender gap', 'representation', 'field'.",
    grammar_reason="[GRA6] Conditionals: 'If girls don't see...'. Reason: 'This stereotype is strong'. >Band 5: Good grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 315: V6/G6 - Topic: Culture (Language)
samples.append(create_sample(
    index=315,
    vocab_band=6,
    grammar_band=6,
    question="Should everyone learn English?",
    transcript="It is very useful. English is the language of the world. Business, travel, internet. If you know English, you have more opportunities. But I don't think it should be forced. People should love their own language too. Diversity is beautiful. If everyone speaks only English, we lose culture. Learning English is a tool, not a replacement.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'language of the world' (common phrase)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'opportunities', 'forced', 'diversity', 'tool', 'replacement'. >Band 5: Clear meaning. Not Band 7: Lacks 'global', 'lingua franca', 'essential', 'communication'.",
    grammar_reason="[GRA6] Conditionals: 'If you know English...', 'If everyone speaks...'. >Band 5: Accurate complex sentences. Not Band 7: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 316: V6/G6 - Topic: Transport (Cities)
samples.append(create_sample(
    index=316,
    vocab_band=6,
    grammar_band=6,
    question="What is the future of public transport?",
    transcript="It will be greener and faster. Electric buses and trains. This reduces pollution. Also, it will be smart. Apps will tell you exactly when the bus comes. No waiting. Maybe we will have driverless pods. Small vehicles for short trips. The goal is to make it better than cars. So people choose to leave their car at home.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'driverless pods' (specific term)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'greener', 'pollution', 'smart', 'driverless pods', 'vehicles', 'trips', 'goal'. >Band 5: Good topic words. Not Band 7: Lacks 'efficient', 'integrated', 'network', 'sustainable'.",
    grammar_reason="[GRA6] Future tense: 'It will be...', 'Apps will tell...'. Comparison: 'Better than cars'. >Band 5: Accurate grammar. Not Band 7: Simple sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 317: V6/G6 - Topic: Society (Housing)
samples.append(create_sample(
    index=317,
    vocab_band=6,
    grammar_band=6,
    question="Why is housing so expensive in cities?",
    transcript="Because everyone wants to live there. Demand is high, but supply is low. There is not enough land. So prices go up. Also, rich people buy houses as investment. They don't live in them. This pushes prices up more. Normal people cannot afford rent. The government needs to build affordable homes. Housing is a need, not just a business.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'pushes prices up' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'demand', 'supply', 'investment', 'afford', 'rent', 'affordable'. >Band 5: Relevant terms. Not Band 7: Lacks 'urban', 'market', 'property', 'speculation'.",
    grammar_reason="[GRA6] Contrast: 'Demand is high, but...'. Reason: 'Because everyone wants...'. >Band 5: Good control. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 318: V6/G6 - Topic: Environment (Global Warming)
samples.append(create_sample(
    index=318,
    vocab_band=6,
    grammar_band=6,
    question="How does global warming affect animals?",
    transcript="It destroys their homes. For example, polar bears need ice. But the ice is melting. They cannot hunt. Many animals are moving to cooler places. But sometimes there is nowhere to go. They might become extinct. The ocean is getting warmer too. Coral reefs are dying. This affects all fish. It is a tragedy for nature.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'tragedy for nature' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'destroys', 'melting', 'hunt', 'extinct', 'coral reefs', 'tragedy'. >Band 5: Specific terms. Not Band 7: Lacks 'habitat', 'migration', 'ecosystem', 'bleaching'.",
    grammar_reason="[GRA6] Contrast: 'But the ice is melting'. Reason: 'For example...'. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 319: V6/G6 - Topic: Health (Food)
samples.append(create_sample(
    index=319,
    vocab_band=6,
    grammar_band=6,
    question="Should schools sell fast food?",
    transcript="No, they shouldn't. Schools are for learning, including learning how to eat well. If they sell burgers and fries, children will eat them. It is tasty but bad. It causes obesity and tiredness. Students cannot focus in class. Schools should provide healthy meals. Vegetables and fruit. It helps their brain and body. Health comes first.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Health comes first' (idiom)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'learning', 'tasty', 'obesity', 'tiredness', 'focus', 'provide', 'meals'. >Band 5: Clear meaning. Not Band 7: Lacks 'nutrition', 'policy', 'available', 'ban'.",
    grammar_reason="[GRA6] Conditionals: 'If they sell burgers...'. Modals: 'Should provide'. >Band 5: Accurate grammar. Not Band 7: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 320: V6/G6 - Topic: Culture (Travel)
samples.append(create_sample(
    index=320,
    vocab_band=6,
    grammar_band=6,
    question="Does travel open the mind?",
    transcript="Yes, absolutely. When you travel, you see different ways of living. You meet people with different ideas. It breaks stereotypes. You realize that your way is not the only way. You become more tolerant and understanding. Also, you try new things. Food and customs. It makes you a better person. Staying in one place limits your view.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'breaks stereotypes' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'absolutely', 'stereotypes', 'realize', 'tolerant', 'understanding', 'customs', 'limits'. >Band 5: Good range. Not Band 7: Lacks 'perspective', 'culture shock', 'broaden', 'horizon'.",
    grammar_reason="[GRA6] Time clause: 'When you travel'. Contrast implied. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 321: V6/G6 - Topic: Work (Remote)
samples.append(create_sample(
    index=321,
    vocab_band=6,
    grammar_band=6,
    question="What are the challenges of working from home?",
    transcript="The biggest challenge is distraction. At home, you have TV, family, or pets. It is hard to focus. You need self-discipline. Also, you miss the social side. No coffee break with colleagues. You feel isolated. It is also hard to separate work and life. You might work too late. You never leave the office because your home is the office.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'social side' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'distraction', 'focus', 'self-discipline', 'social side', 'isolated', 'separate'. >Band 5: Relevant terms. Not Band 7: Lacks 'boundary', 'productivity', 'environment', 'remote'.",
    grammar_reason="[GRA6] Reason: 'Because your home is the office'. Contrast: 'But...'. >Band 5: Good grammar. Not Band 7: Simple structure.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 322: V6/G6 - Topic: Technology (Robots)
samples.append(create_sample(
    index=322,
    vocab_band=6,
    grammar_band=6,
    question="Should we be afraid of robots?",
    transcript="Not afraid, but careful. Robots can help us. They do dangerous work. But if they become too smart, maybe they don't need us. Science fiction movies show robots fighting humans. It is possible. Also, they take our jobs. We need rules for AI. Humans must always be in control. If we are smart, robots will be our friends, not enemies.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'in control' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'careful', 'dangerous', 'smart', 'fiction', 'fighting', 'rules', 'control', 'enemies'. >Band 5: Clear meaning. Not Band 7: Lacks 'threat', 'artificial intelligence', 'regulate', 'superior'.",
    grammar_reason="[GRA6] Conditionals: 'If they become...', 'If we are smart...'. Contrast: 'But if...'. >Band 5: Accurate grammar. Not Band 7: Simple sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 323: V6/G6 - Topic: Society (Advertising)
samples.append(create_sample(
    index=323,
    vocab_band=6,
    grammar_band=6,
    question="Is advertising necessary?",
    transcript="For companies, yes. They need to tell people about their products. Without ads, we don't know what to buy. It drives the economy. But for people, it is annoying. Ads are everywhere. TV, phone, street. They try to manipulate us. Make us buy things we don't need. I think there should be less advertising. It is too much.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'drives the economy' (collocation)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'products', 'drives', 'economy', 'annoying', 'manipulate', 'less'. >Band 5: Good range. Not Band 7: Lacks 'consumer', 'marketing', 'influence', 'limit'.",
    grammar_reason="[GRA6] Contrast: 'But for people'. Reason: 'Without ads...'. >Band 5: Accurate grammar. Not Band 7: Short sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 324: V6/G6 - Topic: Education (University)
samples.append(create_sample(
    index=324,
    vocab_band=6,
    grammar_band=6,
    question="Why do students feel stress at university?",
    transcript="The pressure is high. They have exams and assignments all the time. They want to get good grades. Also, money is a worry. Tuition and rent are expensive. Some students work and study. They are exhausted. Also, living away from home. They miss their family. It is a big change in life. Universities should offer mental support.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'mental support' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'pressure', 'assignments', 'grades', 'tuition', 'expensive', 'exhausted', 'mental support'. >Band 5: Relevant terms. Not Band 7: Lacks 'academic', 'financial', 'burden', 'counseling'.",
    grammar_reason="[GRA6] Reason: 'The pressure is high'. Modals: 'Should offer'. >Band 5: Accurate grammar. Not Band 7: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 325: V6/G6 - Topic: Environment (Water)
samples.append(create_sample(
    index=325,
    vocab_band=6,
    grammar_band=6,
    question="How can we save water?",
    transcript="We can do small things. Turn off the tap when brushing teeth. Take shorter showers. Fix leaking pipes. These small actions help. Also, we can collect rain water for the garden. Farmers should use better irrigation. Not waste water. Water is precious. We must protect it for the future. Education is important to change habits.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'leaking pipes' (correct)"
    ],
    grammar_profile={"complexity": "moderate", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR6] Uses less common items: 'tap', 'leaking', 'actions', 'irrigation', 'precious', 'protect', 'habits'. >Band 5: Specific terms. Not Band 7: Lacks 'conserve', 'consumption', 'scarcity', 'efficient'.",
    grammar_reason="[GRA6] Modals: 'Should use', 'Must protect'. Time clause: 'When brushing teeth'. >Band 5: Accurate grammar. Not Band 7: Imperatives mostly.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
