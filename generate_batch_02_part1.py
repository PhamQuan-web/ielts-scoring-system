import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch02.jsonl")

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

# --- BATCH 02 PART 1: SAMPLES 51-75 (25 Total) ---
# Combo: V5/G4 (Better vocab than grammar)

# Sample 51: V5/G4 - Topic: Technology (AI)
samples.append(create_sample(
    index=51,
    vocab_band=5,
    grammar_band=4,
    question="Do you think artificial intelligence will replace human jobs?",
    transcript="I think artificial intelligence is very smart. It can calculate data fast. Maybe in future, robot do job like doctor or teacher. This is a big challenge for society. But human have emotion. Robot not have feeling. So some job is safe. But simple task, maybe replace.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'robot do job' -> 'robots will do jobs'",
        "verb agreement: 'human have' -> 'humans have'",
        "verb construction: 'Robot not have' -> 'Robots do not have'",
        "verb agreement: 'job is safe' -> 'jobs are safe'",
        "sentence fragment: 'But simple task, maybe replace'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Uses some topic-specific vocabulary: 'artificial intelligence', 'calculate', 'data', 'challenge', 'society'. >Band 4: Attempts more precise terms than just 'good/bad'. Not Band 6: Limited range and flexibility.",
    grammar_reason="[GRA4] Simple sentences predominant. 'Robot not have feeling'. 'But simple task, maybe replace'. >Band 3: Logical flow. Not Band 5: Frequent basic errors in agreement and structure.",
    idiom_present=False,
    risk_level="low"
))

# Sample 52: V5/G4 - Topic: Education (Online Learning)
samples.append(create_sample(
    index=52,
    vocab_band=5,
    grammar_band=4,
    question="Is online learning effective for all students?",
    transcript="Online learning is convenient. Student can study at home. No need travel. But some student lazy. They not focus on screen. Also, internet connection sometimes bad. I think traditional class is better. Teacher can control student. Interaction is important.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'Student can study' -> 'Students can study'",
        "verb construction: 'No need travel' -> 'No need to travel'",
        "verb agreement: 'student lazy' -> 'students are lazy'",
        "verb construction: 'not focus' -> 'do not focus'",
        "verb agreement: 'connection sometimes bad' -> 'connection is sometimes bad'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic vocabulary: 'convenient', 'focus', 'screen', 'connection', 'traditional', 'interaction'. >Band 4: Uses relevant terms. Not Band 6: Some imprecision, lacks 'discipline', 'engagement'.",
    grammar_reason="[GRA4] Short simple sentences. 'No need travel'. 'They not focus'. >Band 3: Meaning clear. Not Band 5: Errors in basic verb forms are systematic.",
    idiom_present=False,
    risk_level="low"
))

# Sample 53: V5/G4 - Topic: Environment (Global Warming)
samples.append(create_sample(
    index=53,
    vocab_band=5,
    grammar_band=4,
    question="What are the main causes of global warming?",
    transcript="The main cause is pollution. Factory smoke and car exhaust. It make temperature go up. Also, deforestation is problem. People cut tree. Animal lose habitat. We need protect environment. Use renewable energy. If not, disaster happen.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'It make' -> 'It makes'",
        "singular/plural: 'People cut tree' -> 'People cut trees'",
        "verb agreement: 'Animal lose' -> 'Animals lose'",
        "verb construction: 'need protect' -> 'need to protect'",
        "verb agreement: 'disaster happen' -> 'disasters will happen'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Uses topic words: 'pollution', 'exhaust', 'temperature', 'deforestation', 'habitat', 'renewable energy'. >Band 4: Good range for the topic. Not Band 6: Collocations slightly off ('make temperature go up').",
    grammar_reason="[GRA4] Mainly simple sentences. 'It make temperature go up'. 'If not, disaster happen'. >Band 3: Coherent. Not Band 5: Frequent basic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 54: V5/G4 - Topic: Work (Remote Work)
samples.append(create_sample(
    index=54,
    vocab_band=5,
    grammar_band=4,
    question="What are the advantages of working from home?",
    transcript="Working from home is flexible. You can manage time. No traffic jam. Save money on transport. But sometimes lonely. No colleague to talk. Also, distraction at home. Maybe watch TV or sleep. Productivity can go down.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'No traffic jam'",
        "fragment: 'Save money on transport'",
        "fragment: 'But sometimes lonely'",
        "fragment: 'No colleague to talk'",
        "fragment: 'Also, distraction at home'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Vocabulary: 'flexible', 'manage', 'transport', 'colleague', 'distraction', 'productivity'. >Band 4: Uses specific work-related terms. Not Band 6: Lacks 'commute', 'socialize', 'efficiency'.",
    grammar_reason="[GRA4] Heavy reliance on fragments and simple structures. 'No traffic jam'. 'Productivity can go down'. >Band 3: Understandable. Not Band 5: Lacks full sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 55: V5/G4 - Topic: Society (Consumerism)
samples.append(create_sample(
    index=55,
    vocab_band=5,
    grammar_band=4,
    question="Do people buy things they don't really need?",
    transcript="Yes, consumerism is big now. Advertisement influence people. They buy latest phone or clothes. Just for fashion. They want impress other. It is waste of resource. People should save money. Not spend on luxury item.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Advertisement influence' -> 'Advertisements influence'",
        "missing article: 'latest phone' -> 'the latest phone'",
        "verb construction: 'want impress other' -> 'want to impress others'",
        "singular/plural: 'resource' -> 'resources'",
        "singular/plural: 'luxury item' -> 'luxury items'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'consumerism', 'advertisement', 'influence', 'fashion', 'impress', 'resource', 'luxury'. >Band 4: Specific vocabulary used correctly. Not Band 6: Lacks 'materialism', 'status symbol', 'impulse buy'.",
    grammar_reason="[GRA4] Simple sentences. 'They want impress other'. 'Not spend on luxury item'. >Band 3: Logical. Not Band 5: Systematic errors in plurals and verb patterns.",
    idiom_present=False,
    risk_level="low"
))

# Sample 56: V5/G4 - Topic: Health (Mental Health)
samples.append(create_sample(
    index=56,
    vocab_band=5,
    grammar_band=4,
    question="How can people improve their mental health?",
    transcript="Mental health is important. Stress is common problem. People work too hard. Burnout happen. To improve, need relax. Do meditation or yoga. Also, talk to friend. Don't keep feeling inside. Balance life is key.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Burnout happen' -> 'Burnout happens'",
        "verb construction: 'need relax' -> 'need to relax'",
        "singular/plural: 'friend' -> 'friends'",
        "phrase error: 'keep feeling inside' -> 'keep feelings inside'",
        "phrase error: 'Balance life' -> 'A balanced life'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'mental health', 'stress', 'common', 'burnout', 'relax', 'meditation', 'balance'. >Band 4: Good range. Not Band 6: Lacks 'well-being', 'mindfulness', 'anxiety'.",
    grammar_reason="[GRA4] Simple sentences and imperatives. 'Burnout happen'. 'Do meditation'. >Band 3: Coherent. Not Band 5: Frequent errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 57: V5/G4 - Topic: Culture (Globalization)
samples.append(create_sample(
    index=57,
    vocab_band=5,
    grammar_band=4,
    question="Is globalization good for local cultures?",
    transcript="Globalization have positive and negative. We can learn foreign culture. Try new food. But local tradition maybe disappear. Young people like western style. They forget own custom. I think we need preserve heritage. It is identity of country.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Globalization have' -> 'Globalization has'",
        "verb agreement: 'tradition maybe disappear' -> 'traditions maybe disappear' or 'might disappear'",
        "phrase error: 'forget own custom' -> 'forget their own customs'",
        "verb construction: 'need preserve' -> 'need to preserve'",
        "missing article: 'identity of country' -> 'the identity of the country'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'globalization', 'foreign', 'tradition', 'western style', 'custom', 'preserve', 'heritage', 'identity'. >Band 4: Specific terms. Not Band 6: Lacks 'cultural exchange', 'diversity', 'homogenization'.",
    grammar_reason="[GRA4] Simple sentences. 'Globalization have...'. 'They forget own custom'. >Band 3: Logical. Not Band 5: Basic grammatical errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 58: V5/G4 - Topic: Transport (Electric Cars)
samples.append(create_sample(
    index=58,
    vocab_band=5,
    grammar_band=4,
    question="Will electric cars replace petrol cars in the future?",
    transcript="Yes, electric car is future. Petrol car make pollution. CO2 emission is bad. Electric car is eco-friendly. Battery technology improve fast. But charging station is problem. Not enough place. Also expensive. But government support it.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'electric car is' -> 'electric cars are'",
        "singular/plural: 'Petrol car make' -> 'Petrol cars make'",
        "verb agreement: 'technology improve' -> 'technology is improving'",
        "singular/plural: 'charging station is' -> 'charging stations are'",
        "singular/plural: 'Not enough place' -> 'Not enough places'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Vocabulary: 'pollution', 'emission', 'eco-friendly', 'battery', 'technology', 'charging station'. >Band 4: Good topic vocabulary. Not Band 6: Lacks 'infrastructure', 'sustainable', 'alternative'.",
    grammar_reason="[GRA4] Simple sentences. 'Petrol car make pollution'. 'Battery technology improve'. >Band 3: Coherent. Not Band 5: Systematic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 59: V5/G4 - Topic: Education (University Cost)
samples.append(create_sample(
    index=59,
    vocab_band=5,
    grammar_band=4,
    question="Should university education be free for everyone?",
    transcript="Education is right for everyone. If free, poor student can study. They can get degree. Improve life. But government need money. Tax will high. Maybe only good student get free. Scholarship is good idea.",
    response_type="direct_answer",
    micro_flaws=[
        "missing article: 'Education is right' -> 'Education is a right'",
        "singular/plural: 'poor student' -> 'poor students'",
        "verb construction: 'government need' -> 'the government needs'",
        "phrase error: 'Tax will high' -> 'Taxes will be high'",
        "singular/plural: 'good student' -> 'good students'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'degree', 'government', 'tax', 'scholarship', 'right'. >Band 4: Uses specific terms. Not Band 6: Lacks 'tuition', 'funding', 'opportunity', 'merit'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'If free'. 'Tax will high'. >Band 3: Logical. Not Band 5: Missing verbs and articles.",
    idiom_present=False,
    risk_level="low"
))

# Sample 60: V5/G4 - Topic: Technology (Social Media)
samples.append(create_sample(
    index=60,
    vocab_band=5,
    grammar_band=4,
    question="How has social media changed communication?",
    transcript="Social media change how we talk. We can connect instant. Message friend far away. Share photo and video. It is convenient. But face-to-face talk is less. People look at phone. Relationship become weak. Cyberbullying is also danger.",
    response_type="direct_answer",
    micro_flaws=[
        "verb tense: 'change' -> 'has changed'",
        "adverb error: 'connect instant' -> 'connect instantly'",
        "verb construction: 'Message friend' -> 'Message friends'",
        "phrase error: 'Relationship become weak' -> 'Relationships become weak'",
        "word form: 'danger' -> 'dangerous'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Vocabulary: 'connect', 'instant', 'face-to-face', 'relationship', 'cyberbullying'. >Band 4: Relevant terms. Not Band 6: Lacks 'interaction', 'virtual', 'platform'.",
    grammar_reason="[GRA4] Simple sentences. 'Social media change...'. 'Relationship become weak'. >Band 3: Coherent. Not Band 5: Basic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 61: V5/G4 - Topic: Work (Gender)
samples.append(create_sample(
    index=61,
    vocab_band=5,
    grammar_band=4,
    question="Is there gender equality in the workplace?",
    transcript="It is better now. Women work in many field. Boss can be woman. But salary gap exist. Men earn more money. Also discrimination happen. Pregnancy is difficult for work. Company not want hire. We need equal opportunity.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'many field' -> 'many fields'",
        "verb agreement: 'salary gap exist' -> 'salary gap exists'",
        "verb agreement: 'discrimination happen' -> 'discrimination happens'",
        "verb construction: 'Company not want hire' -> 'Companies do not want to hire'",
        "phrase error: 'Pregnancy is difficult for work' -> 'Pregnancy makes work difficult'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'field', 'salary gap', 'discrimination', 'pregnancy', 'hire', 'equal opportunity'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'promotion', 'barrier', 'bias', 'pay gap'.",
    grammar_reason="[GRA4] Simple sentences. 'Company not want hire'. 'Men earn more money'. >Band 3: Logical. Not Band 5: Frequent errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 62: V5/G4 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=62,
    vocab_band=5,
    grammar_band=4,
    question="Why are some animal species becoming extinct?",
    transcript="Human activity is reason. Hunting is bad. People kill animal for fur or ivory. Also habitat loss. We build city and farm. Animal have no home. Pollution affect them too. Climate change make weather hot. Some animal cannot survive.",
    response_type="direct_answer",
    micro_flaws=[
        "missing article: 'reason' -> 'the reason'",
        "singular/plural: 'kill animal' -> 'kill animals'",
        "singular/plural: 'build city' -> 'build cities'",
        "verb agreement: 'Animal have' -> 'Animals have'",
        "verb agreement: 'Pollution affect' -> 'Pollution affects'",
        "verb agreement: 'Climate change make' -> 'Climate change makes'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'human activity', 'hunting', 'fur', 'ivory', 'habitat loss', 'survive'. >Band 4: Good range. Not Band 6: Lacks 'poaching', 'ecosystem', 'endangered'.",
    grammar_reason="[GRA4] Simple sentences. 'Animal have no home'. 'Climate change make...'. >Band 3: Coherent. Not Band 5: Errors in subject-verb agreement.",
    idiom_present=False,
    risk_level="low"
))

# Sample 63: V5/G4 - Topic: Society (Elderly)
samples.append(create_sample(
    index=63,
    vocab_band=5,
    grammar_band=4,
    question="What are the challenges of an aging population?",
    transcript="Aging population is big issue. Old people need healthcare. Hospital will full. Government pay pension. It cost much money. Young people must work hard. Support old generation. Maybe labor shortage. Not enough worker.",
    response_type="direct_answer",
    micro_flaws=[
        "missing article: 'big issue' -> 'a big issue'",
        "phrase error: 'Hospital will full' -> 'Hospitals will be full'",
        "verb agreement: 'Government pay' -> 'The government pays'",
        "verb agreement: 'It cost' -> 'It costs'",
        "fragment: 'Support old generation'",
        "singular/plural: 'Not enough worker' -> 'Not enough workers'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'healthcare', 'pension', 'generation', 'labor shortage', 'worker'. >Band 4: Uses specific terms. Not Band 6: Lacks 'burden', 'retirement', 'demographic', 'taxpayer'.",
    grammar_reason="[GRA4] Simple sentences. 'It cost much money'. 'Hospital will full'. >Band 3: Logical. Not Band 5: Errors in verb 'be' and agreement.",
    idiom_present=False,
    risk_level="low"
))

# Sample 64: V5/G4 - Topic: Travel (Culture Shock)
samples.append(create_sample(
    index=64,
    vocab_band=5,
    grammar_band=4,
    question="What problems can tourists face in a foreign country?",
    transcript="Language barrier is main problem. Cannot speak local language. Hard to order food. Also culture shock. Different custom. Maybe rude. Tourist can get lost. Scam is risk too. People cheat money. Safety is important.",
    response_type="direct_answer",
    micro_flaws=[
        "fragment: 'Cannot speak local language'",
        "fragment: 'Hard to order food'",
        "fragment: 'Different custom'",
        "fragment: 'Maybe rude'",
        "phrase error: 'Scam is risk' -> 'Scams are a risk'",
        "phrase error: 'cheat money' -> 'cheat them out of money'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'language barrier', 'local', 'culture shock', 'custom', 'rude', 'scam', 'cheat'. >Band 4: Good vocabulary range. Not Band 6: Lacks 'misunderstanding', 'navigate', 'victim'.",
    grammar_reason="[GRA4] Fragments and simple sentences. 'Maybe rude'. 'Cannot speak...'. >Band 3: Coherent. Not Band 5: Lack of complete sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 65: V5/G4 - Topic: Education (Exams)
samples.append(create_sample(
    index=65,
    vocab_band=5,
    grammar_band=4,
    question="Do you think exams are a good way to assess students?",
    transcript="Exam is standard way. It test knowledge. Fair for everyone. But it cause stress. Student pressure is high. Memorize fact not understand. Some student clever but fail exam. Maybe project or presentation is better.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Exam is' -> 'Exams are'",
        "verb agreement: 'It test' -> 'It tests'",
        "verb agreement: 'it cause' -> 'it causes'",
        "phrase error: 'Memorize fact not understand' -> 'They memorize facts but do not understand'",
        "verb agreement: 'student clever' -> 'students are clever'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'standard', 'knowledge', 'fair', 'stress', 'pressure', 'memorize', 'presentation'. >Band 4: Relevant vocabulary. Not Band 6: Lacks 'evaluate', 'assessment', 'performance', 'anxiety'.",
    grammar_reason="[GRA4] Simple sentences. 'It test knowledge'. 'Student pressure is high'. >Band 3: Logical. Not Band 5: Basic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 66: V5/G4 - Topic: Technology (Privacy)
samples.append(create_sample(
    index=66,
    vocab_band=5,
    grammar_band=4,
    question="How can we protect our privacy online?",
    transcript="Privacy is difficult now. Hacker steal data. We must be careful. Use strong password. Not share personal info. Social media is dangerous. Photo and location. Company sell data for ad. Government should make law. Protect user.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Hacker steal' -> 'Hackers steal'",
        "fragment: 'Not share personal info'",
        "fragment: 'Photo and location'",
        "verb agreement: 'Company sell' -> 'Companies sell'",
        "fragment: 'Protect user'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'hacker', 'data', 'password', 'personal info', 'location', 'ad', 'law'. >Band 4: Specific terms. Not Band 6: Lacks 'cybersecurity', 'encryption', 'regulation', 'identity theft'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'Use strong password'. 'Protect user'. >Band 3: Coherent. Not Band 5: Imperatives used as statements.",
    idiom_present=False,
    risk_level="low"
))

# Sample 67: V5/G4 - Topic: Work (Robots)
samples.append(create_sample(
    index=67,
    vocab_band=5,
    grammar_band=4,
    question="What skills will be important in the future workplace?",
    transcript="Future job need different skill. Robot do manual work. So human need soft skill. Communication and teamwork. Also creativity. Machine cannot create. Technology skill is important. Coding and computer. Learning new thing is key.",
    response_type="direct_answer",
    micro_flaws=[
        "singular/plural: 'Future job' -> 'Future jobs'",
        "verb agreement: 'Robot do' -> 'Robots do'",
        "singular/plural: 'need soft skill' -> 'need soft skills'",
        "fragment: 'Communication and teamwork'",
        "singular/plural: 'new thing' -> 'new things'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'manual work', 'soft skill', 'communication', 'creativity', 'coding'. >Band 4: Good range. Not Band 6: Lacks 'adaptability', 'critical thinking', 'emotional intelligence'.",
    grammar_reason="[GRA4] Simple sentences. 'Robot do manual work'. 'Learning new thing is key'. >Band 3: Logical. Not Band 5: Frequent errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 68: V5/G4 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=68,
    vocab_band=5,
    grammar_band=4,
    question="Is recycling enough to save the environment?",
    transcript="Recycling is good but not enough. We produce too much waste. Plastic is big problem. We need reduce consumption. Buy less thing. Reuse item. Also, government need strict rule. Ban single-use plastic. Education is important.",
    response_type="direct_answer",
    micro_flaws=[
        "phrase error: 'Buy less thing' -> 'Buy fewer things'",
        "verb agreement: 'government need' -> 'the government needs'",
        "singular/plural: 'strict rule' -> 'strict rules'",
        "fragment: 'Ban single-use plastic'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'waste', 'consumption', 'reuse', 'strict rule', 'single-use plastic'. >Band 4: Specific vocabulary. Not Band 6: Lacks 'sustainability', 'initiative', 'legislation', 'minimize'.",
    grammar_reason="[GRA4] Simple sentences. 'We need reduce'. 'Plastic is big problem'. >Band 3: Coherent. Not Band 5: Errors in structure.",
    idiom_present=False,
    risk_level="low"
))

# Sample 69: V5/G4 - Topic: Society (Urbanization)
samples.append(create_sample(
    index=69,
    vocab_band=5,
    grammar_band=4,
    question="Why are people moving from villages to cities?",
    transcript="People move for opportunity. City have better job. Higher salary. Education is good. Village is boring. No facility. Hospital is far. But city is crowded. Traffic and pollution. Housing is expensive. It is hard choice.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'City have' -> 'Cities have'",
        "fragment: 'Higher salary'",
        "fragment: 'No facility'",
        "fragment: 'Traffic and pollution'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'opportunity', 'salary', 'facility', 'crowded', 'pollution', 'housing'. >Band 4: Relevant terms. Not Band 6: Lacks 'urban', 'rural', 'migration', 'amenities'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'City have better job'. 'No facility'. >Band 3: Logical. Not Band 5: Lack of verbs in fragments.",
    idiom_present=False,
    risk_level="low"
))

# Sample 70: V5/G4 - Topic: Health (Diet)
samples.append(create_sample(
    index=70,
    vocab_band=5,
    grammar_band=4,
    question="What is a balanced diet?",
    transcript="Balanced diet mean eat everything. Vegetable and fruit. Protein like meat or fish. Carbohydrate for energy. Not eat too much sugar. Fast food is bad. Drink water. It keep body healthy. Prevent disease. Vitamin is necessary.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'diet mean' -> 'diet means'",
        "fragment: 'Vegetable and fruit'",
        "fragment: 'Carbohydrate for energy'",
        "verb agreement: 'It keep' -> 'It keeps'",
        "singular/plural: 'Vitamin' -> 'Vitamins'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'protein', 'carbohydrate', 'energy', 'sugar', 'disease', 'vitamin'. >Band 4: Specific health terms. Not Band 6: Lacks 'nutrient', 'portion', 'moderation', 'calorie'.",
    grammar_reason="[GRA4] Simple sentences. 'Balanced diet mean...'. 'It keep body healthy'. >Band 3: Coherent. Not Band 5: Basic errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 71: V5/G4 - Topic: Media (Fake News)
samples.append(create_sample(
    index=71,
    vocab_band=5,
    grammar_band=4,
    question="How does fake news affect society?",
    transcript="Fake news is dangerous. People believe wrong information. It cause panic. For example, health news. People try wrong medicine. Also politics. It change opinion. Social media spread it fast. We need check source. Not trust everything.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'It cause' -> 'It causes'",
        "fragment: 'Also politics'",
        "verb agreement: 'It change' -> 'It changes'",
        "verb agreement: 'Social media spread' -> 'Social media spreads'",
        "verb construction: 'need check' -> 'need to check'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'panic', 'medicine', 'politics', 'opinion', 'spread', 'source'. >Band 4: Good range. Not Band 6: Lacks 'misinformation', 'verify', 'consequence', 'manipulate'.",
    grammar_reason="[GRA4] Simple sentences. 'It cause panic'. 'Social media spread it'. >Band 3: Logical. Not Band 5: Subject-verb agreement errors.",
    idiom_present=False,
    risk_level="low"
))

# Sample 72: V5/G4 - Topic: Culture (Language)
samples.append(create_sample(
    index=72,
    vocab_band=5,
    grammar_band=4,
    question="Will English become the only global language?",
    transcript="English is popular now. Business and travel use it. Internet is English. But other language is important. Chinese or Spanish. Culture is in language. If we lose language, we lose culture. So I think translation technology help. Not one language only.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'other language is' -> 'other languages are'",
        "verb agreement: 'technology help' -> 'technology will help'",
        "fragment: 'Not one language only'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'popular', 'business', 'translation', 'technology', 'global'. >Band 4: Relevant terms. Not Band 6: Lacks 'dominant', 'communicate', 'preserve', 'universal'.",
    grammar_reason="[GRA4] Simple sentences. 'English is popular'. 'Culture is in language'. >Band 3: Coherent. Not Band 5: Errors in agreement.",
    idiom_present=False,
    risk_level="low"
))

# Sample 73: V5/G4 - Topic: Transport (Public)
samples.append(create_sample(
    index=73,
    vocab_band=5,
    grammar_band=4,
    question="How can public transport be improved?",
    transcript="Public transport need improvement. Bus is old and dirty. Train is late. Government should buy new vehicle. Make schedule correct. Price should cheap. If convenient, people use it. Less car on road. Less pollution.",
    response_type="direct_answer",
    micro_flaws=[
        "verb agreement: 'Public transport need' -> 'needs'",
        "phrase error: 'Price should cheap' -> 'Price should be cheap'",
        "fragment: 'Less car on road'",
        "fragment: 'Less pollution'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'improvement', 'vehicle', 'schedule', 'convenient', 'pollution'. >Band 4: Specific terms. Not Band 6: Lacks 'efficient', 'reliable', 'infrastructure', 'affordable'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'Bus is old'. 'Price should cheap'. >Band 3: Logical. Not Band 5: Missing verbs and 'be'.",
    idiom_present=False,
    risk_level="low"
))

# Sample 74: V5/G4 - Topic: Education (Teacher)
samples.append(create_sample(
    index=74,
    vocab_band=5,
    grammar_band=4,
    question="What qualities make a good teacher?",
    transcript="Good teacher is patient. Explain clear. Student understand easy. Also knowledge. Teacher must know subject well. Inspire student. Friendly but strict. If teacher is boring, student sleep. Motivation is important.",
    response_type="direct_answer",
    micro_flaws=[
        "adverb error: 'Explain clear' -> 'Explain clearly'",
        "adverb error: 'understand easy' -> 'understand easily'",
        "fragment: 'Also knowledge'",
        "fragment: 'Inspire student'",
        "verb agreement: 'student sleep' -> 'students sleep'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'patient', 'knowledge', 'subject', 'inspire', 'strict', 'motivation'. >Band 4: Good range. Not Band 6: Lacks 'encouraging', 'engaging', 'methodology', 'role model'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'Good teacher is patient'. 'Inspire student'. >Band 3: Coherent. Not Band 5: Lack of complete sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 75: V5/G4 - Topic: Society (Equality)
samples.append(create_sample(
    index=75,
    vocab_band=5,
    grammar_band=4,
    question="How can we achieve equality in society?",
    transcript="Equality is hard goal. Everyone should have same right. Education and health. Rich and poor. Government must help poor people. Law protect everyone. No discrimination. Race or gender. We need respect each other. Fair chance for all.",
    response_type="direct_answer",
    micro_flaws=[
        "missing article: 'hard goal' -> 'a hard goal'",
        "phrase error: 'same right' -> 'the same rights'",
        "fragment: 'Rich and poor'",
        "verb agreement: 'Law protect' -> 'Laws protect'",
        "fragment: 'No discrimination'",
        "fragment: 'Race or gender'"
    ],
    grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
    vocab_reason="[LR5] Topic words: 'equality', 'right', 'discrimination', 'race', 'gender', 'respect', 'fair'. >Band 4: Relevant terms. Not Band 6: Lacks 'justice', 'privilege', 'opportunity', 'society'.",
    grammar_reason="[GRA4] Simple sentences and fragments. 'Equality is hard goal'. 'Law protect everyone'. >Band 3: Logical. Not Band 5: Frequent fragments.",
    idiom_present=False,
    risk_level="low"
))

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Generated {len(samples)} samples in {OUTPUT_FILE}")
