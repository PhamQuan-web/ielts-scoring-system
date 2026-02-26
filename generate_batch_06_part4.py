import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch06.jsonl")

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

# --- BATCH 06 PART 4: SAMPLES 526-550 (25 Total) ---
# Combo: V7/G7

# Sample 526: V7/G7 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=526,
    vocab_band=7,
    grammar_band=7,
    question="Why don't more people recycle?",
    transcript="It is often due to a lack of convenience. If recycling bins are hard to find, people will throw trash in the general waste. Also, confusion plays a part. People don't know what can be recycled. Education is needed to clarify this. Furthermore, some are cynical. They think it doesn't make a difference. We need to show them the positive impact of their actions.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'convenience', 'confusion', 'clarify', 'cynical', 'positive impact'. >Band 6: Clear meaning. Not Band 8: Lacks 'infrastructure', 'incentive', 'skepticism'.",
    grammar_reason="[GRA7] Conditionals: 'If recycling bins are...'. Reason: 'due to a lack of'. >Band 6: Frequent error-free sentences. Not Band 8: Sentences are competent but standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 527: V7/G7 - Topic: Technology (Social Media)
samples.append(create_sample(
    index=527,
    vocab_band=7,
    grammar_band=7,
    question="Should children use social media?",
    transcript="I think there should be an age limit. Children are vulnerable to bullying and predators online. They are not mature enough to handle the pressure of social media. It can affect their self-image. However, it is also a way to connect with friends. Parents must monitor their usage closely. Total banning might be impossible, but regulation is necessary.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'vulnerable', 'predators', 'mature', 'self-image', 'monitor', 'regulation'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'exposure', 'psychological', 'guidance'.",
    grammar_reason="[GRA7] Modals: 'Should be', 'Must monitor'. Contrast: 'However'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 528: V7/G7 - Topic: Society (Cities)
samples.append(create_sample(
    index=528,
    vocab_band=7,
    grammar_band=7,
    question="What makes a city a good place to live?",
    transcript="A combination of factors. Employment opportunities are crucial. People move to cities for work. Also, infrastructure is key. Good transport, hospitals, and schools. But quality of life matters too. Green spaces, culture, and safety. A city needs a soul. It should be a place where people feel they belong, not just a concrete jungle.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'concrete jungle' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'combination', 'opportunities', 'infrastructure', 'quality of life', 'soul', 'belong', 'concrete jungle'. >Band 6: Strong vocabulary. Not Band 8: Slightly list-like.",
    grammar_reason="[GRA7] Relative clause: 'where people feel'. List structure. >Band 6: Accurate grammar. Not Band 8: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 529: V7/G7 - Topic: Work (Career)
samples.append(create_sample(
    index=529,
    vocab_band=7,
    grammar_band=7,
    question="Is ambition important for success?",
    transcript="Yes, it is the fuel for success. Ambition drives you to work hard and overcome obstacles. Without it, you might settle for mediocrity. However, blind ambition can be dangerous. It can lead to burnout or unethical behavior. You might step on others to get ahead. So, ambition is good, but it needs to be balanced with integrity.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'step on others' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'fuel', 'drives', 'overcome obstacles', 'mediocrity', 'blind ambition', 'burnout', 'unethical', 'integrity'. Idiom: 'step on others'. >Band 6: Advanced terms. Not Band 8: Lacks 'aspiration', 'determination', 'consequences'.",
    grammar_reason="[GRA7] Contrast: 'However', 'but it needs...'. Conditionals implied. >Band 6: Good control. Not Band 8: Limited complexity.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 530: V7/G7 - Topic: Education (University)
samples.append(create_sample(
    index=530,
    vocab_band=7,
    grammar_band=7,
    question="Should university entrance exams be abolished?",
    transcript="It is a difficult question. Exams are a fair way to measure knowledge. They provide a standard for everyone. However, they are very stressful. One day can decide your future. This is not always accurate. Some students are bad at exams but good at learning. Maybe a portfolio system would be better. It shows a student's work over time.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'measure', 'standard', 'stressful', 'accurate', 'portfolio'. >Band 6: Clear meaning. Not Band 8: Lacks 'assessment', 'meritocracy', 'holistic'.",
    grammar_reason="[GRA7] Contrast: 'However'. Reason: 'This is not always accurate'. >Band 6: Frequent error-free sentences. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="low"
))

# Sample 531: V7/G7 - Topic: Culture (Food)
samples.append(create_sample(
    index=531,
    vocab_band=7,
    grammar_band=7,
    question="Why do people enjoy trying new food?",
    transcript="It is an adventure for the senses. New flavors and textures are exciting. It breaks the routine of daily life. Also, food is a gateway to culture. When you eat a country's food, you understand its people better. It is a shared experience. Trying strange food shows you are open-minded. It expands your culinary horizons.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'gateway to culture' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'adventure', 'senses', 'textures', 'gateway', 'open-minded', 'culinary horizons'. >Band 6: Sophisticated vocabulary. Not Band 8: Lacks 'palate', 'cuisine', 'gastronomy'.",
    grammar_reason="[GRA7] Time clause: 'When you eat...'. Reason: 'It is a shared experience'. >Band 6: Accurate grammar. Not Band 8: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 532: V7/G7 - Topic: Transport (Cars)
samples.append(create_sample(
    index=532,
    vocab_band=7,
    grammar_band=7,
    question="What is the future of the car industry?",
    transcript="It is definitely electric. The era of the combustion engine is ending. Governments are banning petrol cars. Also, technology will play a huge role. Cars will be like computers on wheels. Autonomous driving will change how we travel. We might not even own cars in the future. We will just order a ride when we need it. It will be a service, not a product.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'computers on wheels' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'combustion engine', 'banning', 'autonomous', 'service'. >Band 6: Relevant terms. Not Band 8: Lacks 'emissions', 'mobility', 'transition'.",
    grammar_reason="[GRA7] Future tense: 'will play', 'will be'. Contrast: 'not a product'. >Band 6: Good control. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 533: V7/G7 - Topic: Health (Mental)
samples.append(create_sample(
    index=533,
    vocab_band=7,
    grammar_band=7,
    question="Is it possible to be happy all the time?",
    transcript="No, I don't think so. Life is full of ups and downs. Sadness and anger are natural emotions. If we suppress them, it is unhealthy. Happiness is not a constant state. It comes in moments. We should aim for contentment and peace, not constant joy. Dealing with challenges makes us stronger. Without sadness, we cannot appreciate happiness.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'ups and downs' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'suppress', 'constant state', 'contentment', 'appreciate'. Idiom: 'ups and downs'. >Band 6: Clear meaning. Not Band 8: Lacks 'resilience', 'perspective', 'spectrum'.",
    grammar_reason="[GRA7] Conditionals: 'If we suppress them...'. Contrast: 'not constant joy'. >Band 6: Accurate grammar. Not Band 8: Sentences are somewhat short.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 534: V7/G7 - Topic: Society (Media)
samples.append(create_sample(
    index=534,
    vocab_band=7,
    grammar_band=7,
    question="Does the media report the truth?",
    transcript="Not always. Media outlets often have an agenda. They might support a political party. This creates bias. They select stories that fit their narrative. Also, sensationalism sells. Bad news travels faster than good news. So, they focus on disasters and conflict. We need to be critical consumers of news. Checking multiple sources is the best way to find the truth.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'outlets', 'agenda', 'bias', 'narrative', 'sensationalism', 'critical consumers'. >Band 6: Advanced vocabulary. Not Band 8: Lacks 'objectivity', 'impartial', 'integrity'.",
    grammar_reason="[GRA7] Reason: 'So, they focus...'. Comparison: 'faster than good news'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structure.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 535: V7/G7 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=535,
    vocab_band=7,
    grammar_band=7,
    question="Why are coral reefs dying?",
    transcript="The main cause is rising ocean temperatures. Corals are very sensitive to heat. When the water gets too warm, they bleach and die. Pollution is another factor. Chemicals and plastic damage the reef. Also, overfishing disrupts the balance. If we lose the reefs, we lose a huge part of marine life. It is a warning sign for the planet.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'warning sign' (collocation)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'sensitive', 'bleach', 'factor', 'disrupts', 'marine life', 'warning sign'. >Band 6: Specific terms. Not Band 8: Lacks 'ecosystem', 'biodiversity', 'acidity'.",
    grammar_reason="[GRA7] Time clause: 'When the water gets...'. Conditionals: 'If we lose...'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 536: V7/G7 - Topic: Technology (Internet)
samples.append(create_sample(
    index=536,
    vocab_band=7,
    grammar_band=7,
    question="What is the digital divide?",
    transcript="It is the gap between those who have access to technology and those who don't. In rich countries, everyone has the internet. In poor countries, many do not. This creates inequality. Without the internet, you cannot learn or find a job easily. You are left behind. Bridging this divide is essential for global development. Everyone deserves access to information.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'left behind' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'gap', 'access', 'inequality', 'bridging', 'essential', 'development'. Idiom: 'left behind'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'opportunity', 'infrastructure', 'socioeconomic'.",
    grammar_reason="[GRA7] Contrast: 'In rich countries..., In poor countries...'. Reason: 'Without the internet...'. >Band 6: Good control. Not Band 8: Simple sentence links.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 537: V7/G7 - Topic: Work (Job)
samples.append(create_sample(
    index=537,
    vocab_band=7,
    grammar_band=7,
    question="Is it better to be a specialist or a generalist?",
    transcript="It depends on the industry. Specialists are experts in one field. They are highly valued for their deep knowledge. However, they might struggle if their field changes. Generalists have a broad range of skills. They are adaptable. In a changing world, adaptability is a strength. But they might not reach the top level. A mix of both, a 'T-shaped' person, is often best.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'T-shaped person' (business term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'specialists', 'generalists', 'valued', 'adaptable', 'strength', 'T-shaped'. >Band 6: Specific terms. Not Band 8: Lacks 'niche', 'versatile', 'expertise'.",
    grammar_reason="[GRA7] Contrast: 'However', 'But'. Reason: 'It depends on...'. >Band 6: Accurate grammar. Not Band 8: Sentences are somewhat standard.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 538: V7/G7 - Topic: Culture (Language)
samples.append(create_sample(
    index=538,
    vocab_band=7,
    grammar_band=7,
    question="Can translation technology replace learning a language?",
    transcript="Not completely. Technology is great for tourists. It helps you order food or find a hotel. But it cannot translate culture or emotion perfectly. Language is more than just words. It is about connection. When you speak to someone in their language, you show respect. A machine cannot do that. So, learning languages will always be important.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'completely', 'translate', 'culture', 'emotion', 'connection', 'respect'. >Band 6: Clear meaning. Not Band 8: Lacks 'nuance', 'interpret', 'subtlety'.",
    grammar_reason="[GRA7] Contrast: 'But it cannot...'. Time clause: 'When you speak...'. >Band 6: Frequent error-free sentences. Not Band 8: Simple structure.",
    idiom_present=False,
    risk_level="low"
))

# Sample 539: V7/G7 - Topic: Society (Volunteering)
samples.append(create_sample(
    index=539,
    vocab_band=7,
    grammar_band=7,
    question="What motivates people to help others?",
    transcript="It is human nature. We have empathy. When we see someone suffering, we want to help. It makes us feel good too. There is a sense of satisfaction in giving. Also, some people are motivated by religion or duty. They feel it is the right thing to do. Helping others strengthens our social bonds. We are social animals, after all.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'social animals' (common phrase)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'nature', 'empathy', 'suffering', 'satisfaction', 'motivated', 'duty', 'bonds'. >Band 6: Good range. Not Band 8: Lacks 'altruism', 'compassion', 'innate'.",
    grammar_reason="[GRA7] Time clause: 'When we see...'. Reason: 'because we have empathy' (implied). >Band 6: Accurate grammar. Not Band 8: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 540: V7/G7 - Topic: Environment (Climate)
samples.append(create_sample(
    index=540,
    vocab_band=7,
    grammar_band=7,
    question="What is the most effective way to reduce carbon footprint?",
    transcript="Changing our diet is very effective. Meat production produces a lot of greenhouse gases. If we eat less meat, we help the planet. Also, travel. Flying less and using trains is better. At home, we can use renewable energy. However, individual action is not enough. We need systemic change from governments and corporations. Everyone has a part to play.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'part to play' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'effective', 'greenhouse gases', 'renewable', 'systemic change', 'corporations'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'impact', 'mitigate', 'policy'.",
    grammar_reason="[GRA7] Conditionals: 'If we eat less meat...'. Contrast: 'However'. >Band 6: Frequent error-free sentences. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 541: V7/G7 - Topic: Transport (Public)
samples.append(create_sample(
    index=541,
    vocab_band=7,
    grammar_band=7,
    question="Why is public transport important for the economy?",
    transcript="It moves people to work. If transport is efficient, people are on time and productive. It connects businesses with customers. Also, it reduces congestion. Traffic jams cost money in lost time and fuel. Public transport is the veins of the city. If it flows well, the economy is healthy. Investing in transport is investing in growth.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'veins of the city' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'efficient', 'productive', 'connects', 'congestion', 'investing', 'growth'. Metaphor: 'veins of the city'. >Band 6: Sophisticated terms. Not Band 8: Lacks 'infrastructure', 'logistics', 'vital'.",
    grammar_reason="[GRA7] Conditionals: 'If transport is efficient...'. Reason: 'because it reduces' (implied). >Band 6: Accurate grammar. Not Band 8: Sentences are somewhat standard.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 542: V7/G7 - Topic: Health (Children)
samples.append(create_sample(
    index=542,
    vocab_band=7,
    grammar_band=7,
    question="Should children have more time for play?",
    transcript="Yes, definitely. Play is not just fun; it is learning. Children learn social skills, creativity, and problem-solving through play. Nowadays, children are too busy with homework and lessons. They have no free time. This causes stress. We need to let children be children. Unstructured play is vital for their development. It helps them grow into happy adults.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'let children be children' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'social skills', 'problem-solving', 'unstructured', 'vital', 'development'. Idiom: 'let children be children'. >Band 6: Good range. Not Band 8: Lacks 'cognitive', 'autonomy', 'well-being'.",
    grammar_reason="[GRA7] Reason: 'This causes stress'. Contrast: 'Play is not just fun'. >Band 6: Frequent error-free sentences. Not Band 8: Limited complexity.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 543: V7/G7 - Topic: Education (Technology)
samples.append(create_sample(
    index=543,
    vocab_band=7,
    grammar_band=7,
    question="What are the risks of using technology in class?",
    transcript="Distraction is the main risk. Students might play games instead of listening. Also, they might rely on Google for answers. They stop thinking for themselves. There is also the risk of cyberbullying. However, the benefits outweigh the risks. Technology prepares them for the future. Teachers just need to manage it well. Balance is key.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'outweigh the risks' (collocation)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'distraction', 'rely on', 'cyberbullying', 'outweigh', 'manage', 'balance'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'dependency', 'critical thinking', 'monitor'.",
    grammar_reason="[GRA7] Contrast: 'However'. Reason: 'Because distraction is...' (implied). >Band 6: Accurate grammar. Not Band 8: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 544: V7/G7 - Topic: Culture (Art)
samples.append(create_sample(
    index=544,
    vocab_band=7,
    grammar_band=7,
    question="Why do governments support the arts?",
    transcript="Because art defines a nation. It is our cultural heritage. Without support, many artists could not survive. Museums and theaters would close. Art brings tourism and money. It also makes life beautiful. A country without art has no soul. It fosters creativity and national pride. It is an investment in our identity.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'no soul' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'defines', 'heritage', 'survive', 'tourism', 'fosters', 'national pride', 'investment', 'identity'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'expression', 'subsidize', 'enrich'.",
    grammar_reason="[GRA7] Conditionals: 'Without support...'. Reason: 'Because art defines...'. >Band 6: Good control. Not Band 8: Sentences are somewhat standard.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 545: V7/G7 - Topic: Work (Job)
samples.append(create_sample(
    index=545,
    vocab_band=7,
    grammar_band=7,
    question="Is it important to get along with colleagues?",
    transcript="Yes, it is crucial. You spend most of your day at work. If you have conflict, it is stressful. Good relationships make work enjoyable. You can help each other and share ideas. Teamwork is essential for success. You don't have to be best friends, but you must be professional and respectful. A happy team is a productive team.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'crucial', 'conflict', 'stressful', 'enjoyable', 'essential', 'professional', 'respectful', 'productive'. >Band 6: Clear meaning. Not Band 8: Lacks 'environment', 'collaboration', 'morale'.",
    grammar_reason="[GRA7] Conditionals: 'If you have conflict...'. Contrast: 'You don't have to be..., but...'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="low"
))

# Sample 546: V7/G7 - Topic: Society (Crime)
samples.append(create_sample(
    index=546,
    vocab_band=7,
    grammar_band=7,
    question="Do strict laws prevent crime?",
    transcript="To some extent, yes. People are afraid of punishment. If the penalty is high, they might think twice. However, it is not the only solution. Some people commit crime because they are desperate. Poverty and addiction are strong drivers. Strict laws don't fix these problems. We need social programs to address the root causes. Prevention is better than cure.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'Prevention is better than cure' (proverb)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'extent', 'penalty', 'desperate', 'drivers', 'address', 'root causes'. Proverb: 'Prevention is better than cure'. >Band 6: Sophisticated terms. Not Band 8: Lacks 'deterrent', 'rehabilitation', 'socioeconomic'.",
    grammar_reason="[GRA7] Conditionals: 'If the penalty is high...'. Contrast: 'However'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structure.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 547: V7/G7 - Topic: Technology (Space)
samples.append(create_sample(
    index=547,
    vocab_band=7,
    grammar_band=7,
    question="What can we learn from space exploration?",
    transcript="We learn about our place in the universe. It makes us realize how small and fragile Earth is. This perspective is important. Also, we learn science. Physics, biology, engineering. Many technologies we use today came from space research. It pushes the boundaries of human knowledge. It teaches us to dream big.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'pushes the boundaries' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'universe', 'fragile', 'perspective', 'research', 'boundaries', 'knowledge'. >Band 6: Good range. Not Band 8: Lacks 'innovation', 'scientific', 'advancement'.",
    grammar_reason="[GRA7] Reason: 'It makes us realize...'. Relative clause implied. >Band 6: Accurate grammar. Not Band 8: Short sentences.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 548: V7/G7 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=548,
    vocab_band=7,
    grammar_band=7,
    question="Why do people keep pets?",
    transcript="For companionship. Pets give unconditional love. They are always happy to see you. This helps with loneliness and depression. Dogs also encourage exercise because you have to walk them. For children, pets teach responsibility. Caring for another living being is a valuable lesson. They become part of the family.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'unconditional love' (collocation)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'companionship', 'unconditional', 'loneliness', 'depression', 'encourage', 'responsibility', 'valuable'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'bond', 'emotional support', 'nurture'.",
    grammar_reason="[GRA7] Reason: 'because you have to...'. Gerund: 'Caring for another...'. >Band 6: Good control. Not Band 8: Limited complexity.",
    idiom_present=True,
    risk_level="low"
))

# Sample 549: V7/G7 - Topic: Culture (Fashion)
samples.append(create_sample(
    index=549,
    vocab_band=7,
    grammar_band=7,
    question="Does fashion affect our confidence?",
    transcript="Yes, it does. When you look good, you feel good. Wearing a nice suit or dress can boost your self-esteem. It changes your posture and how you speak. People treat you with more respect too. It is not just vanity. Clothing is a tool for communication. It tells the world who you are. So, fashion has a psychological power.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'boost your self-esteem' (collocation)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'boost', 'self-esteem', 'posture', 'vanity', 'communication', 'psychological'. >Band 6: Precise terms. Not Band 8: Lacks 'perception', 'image', 'impact'.",
    grammar_reason="[GRA7] Time clause: 'When you look good'. Reason: 'So, fashion has...'. >Band 6: Accurate grammar. Not Band 8: Simple sentence links.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 550: V7/G7 - Topic: Society (Cities)
samples.append(create_sample(
    index=550,
    vocab_band=7,
    grammar_band=7,
    question="Why are some cities more popular than others?",
    transcript="It is usually the economy and culture. Popular cities like London or New York offer great jobs. They attract talent. Also, they have a vibrant culture. Museums, theaters, restaurants. There is always something to do. Safety and infrastructure matter too. If a city is clean and easy to travel in, people want to live there. It is a mix of opportunity and lifestyle.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'economy', 'attract', 'talent', 'vibrant', 'infrastructure', 'opportunity', 'lifestyle'. >Band 6: Good range. Not Band 8: Lacks 'cosmopolitan', 'amenities', 'hub'.",
    grammar_reason="[GRA7] Conditionals: 'If a city is clean...'. List structure. >Band 6: Frequent error-free sentences. Not Band 8: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
