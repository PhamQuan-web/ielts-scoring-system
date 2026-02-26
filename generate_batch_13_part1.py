import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch13.jsonl")

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

# --- BATCH 13 PART 1: SAMPLES 1081-1100 (20 Total) ---
# Combo: V5/G8 (Limited Vocab, Expert Grammar)

# Sample 1081: V5/G8 - Topic: Environment
samples.append(create_sample(
    index=1081,
    vocab_band=5,
    grammar_band=8,
    question="Why should we protect nature?",
    transcript="It is a very big thing that we must do. If we do not look after the trees and the animals, the world will become a bad place. Although many people say they care, they do not do enough. Had we started to help nature before, it would be better now. It is essential that everyone tries to do good things for the earth.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR5] Uses basic vocabulary: 'big thing', 'bad place', 'help', 'good things'. >Band 4: Uses words correctly. Not Band 6: Lacks precision and variety.",
    grammar_reason="[GRA8] Wide range of structures used accurately: 'If we do not...', 'Although many people...', 'Had we started...'. Error-free. >Band 7: High level of accuracy and complexity.",
    idiom_present=False,
    risk_level="low"
))

# Sample 1082: V5/G8 - Topic: Technology
samples.append(create_sample(
    index=1082,
    vocab_band=5,
    grammar_band=8,
    question="Is the internet good for us?",
    transcript="I think that the internet is very good, but it has some bad parts. While it helps us find things out, it can also make us lazy. If I had not used the internet, I would not know so much. However, we should be careful. There are people who use it for bad things. It is important that we use it in a good way.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR5] Simple words: 'good', 'bad parts', 'lazy', 'careful', 'good way'. >Band 4: Clear meaning. Not Band 6: Lacks 'beneficial', 'detrimental', 'information'.",
    grammar_reason="[GRA8] Wide range: 'While it helps...', 'If I had not used... I would not...', 'It is important that...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 1083: V5/G8 - Topic: Education
samples.append(create_sample(
    index=1083,
    vocab_band=5,
    grammar_band=8,
    question="Why is school important?",
    transcript="School is the place where we learn everything. Unless we go to school, we cannot get a job. Although some subjects are hard, they help us think. Teachers who are kind make us want to learn. If I could change one thing, I would make school more fun. It is necessary for us to go there so that we can have a good life.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR5] Basic vocabulary: 'place', 'job', 'hard', 'kind', 'fun', 'good life'. >Band 4: Relevant words. Not Band 6: Lacks 'institution', 'career', 'challenging'.",
    grammar_reason="[GRA8] Wide range: 'Unless we go...', 'Although some subjects...', 'Teachers who are kind...', 'so that we can...'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=False,
    risk_level="low"
))

# Sample 1084: V5/G8 - Topic: Work
samples.append(create_sample(
    index=1084,
    vocab_band=5,
    grammar_band=8,
    question="Should people work hard?",
    transcript="Working hard is something that everyone should do. If you do not work hard, you will not get money. However, you should also rest. A person who works all the time will get sick. While money is nice, health is better. I believe that we should find a job that we like. If we are happy at work, we will do a good job.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR5] Simple words: 'money', 'rest', 'sick', 'nice', 'job', 'happy'. >Band 4: Clear. Not Band 6: Lacks 'salary', 'balance', 'career', 'satisfaction'.",
    grammar_reason="[GRA8] Wide range: 'something that everyone...', 'If you do not...', 'A person who works...', 'While money is...'. Error-free. >Band 7: Good complexity.",
    idiom_present=False,
    risk_level="low"
))

# Sample 1085: V5/G8 - Topic: Society
samples.append(create_sample(
    index=1085,
    vocab_band=5,
    grammar_band=8,
    question="Why do people live in cities?",
    transcript="There are many reasons why people choose the city. First, there are more places to work. Second, there are shops and things to do. Although the city is noisy, it is exciting. People who live in the country might feel lonely. If I had to choose, I would live in the city. It is a place where you can meet many people.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR5] Basic words: 'reasons', 'places', 'shops', 'noisy', 'exciting', 'lonely'. >Band 4: Communicates well. Not Band 6: Lacks 'opportunities', 'rural', 'urban', 'facilities'.",
    grammar_reason="[GRA8] Wide range: 'reasons why people...', 'Although the city is...', 'People who live...', 'If I had to choose...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=False,
    risk_level="low"
))

# Generating 1086-1100
topics_13_1 = [
    {
        "question": "Is fast food bad?",
        "transcript": "It is bad because it has a lot of fat. If you eat it every day, you will get fat. Although it tastes good, it is not healthy. People who eat fast food should stop. It is better to eat fruit. If we cooked at home, we would be healthier. We must look after our bodies.",
        "vocab_reason": "[LR5] Basic vocab: 'fat', 'eat', 'good', 'healthy', 'stop', 'fruit'. >Band 4: Accurate. Not Band 6: Repetitive 'eat'.",
        "grammar_reason": "[GRA8] Wide range: 'It is bad because...', 'If you eat...', 'Although it tastes...', 'People who eat...'. Error-free. >Band 7: High accuracy."
    },
    {
        "question": "Is music important?",
        "transcript": "Yes, music is something that makes us happy. When we listen to songs, we feel good. Although some music is loud, I like it. If there was no music, the world would be quiet. It helps people who are sad. Everyone should listen to music.",
        "vocab_reason": "[LR5] Simple words: 'happy', 'songs', 'good', 'loud', 'quiet', 'sad'. >Band 4: Clear. Not Band 6: Lacks 'melody', 'rhythm', 'emotion'.",
        "grammar_reason": "[GRA8] Structures: 'something that makes...', 'When we listen...', 'Although some music...', 'If there was no music...'. Error-free. >Band 7: Excellent control."
    },
    {
        "question": "Should we stop using cars?",
        "transcript": "It would be good if we stopped using cars. Cars make the air dirty. Although they are fast, they are bad for the earth. If people took the bus, there would be less smoke. We should try to walk more. It is a simple thing that helps everyone.",
        "vocab_reason": "[LR5] Basic words: 'good', 'dirty', 'fast', 'bad', 'smoke', 'walk'. >Band 4: Meaning clear. Not Band 6: Lacks 'pollution', 'environment', 'transport'.",
        "grammar_reason": "[GRA8] Conditionals: 'It would be good if...', 'If people took...'. Contrast: 'Although they are fast...'. Error-free. >Band 7: Sophisticated."
    },
    {
        "question": "Do you like phones?",
        "transcript": "I like my phone because it helps me. I can talk to my friends who are far away. Although it is small, it can do many things. If I lost my phone, I would be sad. However, we should not look at it all the time. It is important to talk to people.",
        "vocab_reason": "[LR5] Simple words: 'helps', 'talk', 'far away', 'small', 'sad'. >Band 4: Understandable. Not Band 6: Lacks 'communicate', 'device', 'connect'.",
        "grammar_reason": "[GRA8] Structures: 'because it helps...', 'friends who are...', 'Although it is...', 'If I lost...'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Why save water?",
        "transcript": "Water is something we need to live. If we do not have water, we will die. Although the sea is big, we cannot drink it. We should not waste water when we wash. If everyone saves a little, it will help a lot. We must be careful with it.",
        "vocab_reason": "[LR5] Basic vocab: 'live', 'die', 'big', 'drink', 'waste', 'wash'. >Band 4: Clear. Not Band 6: Lacks 'survive', 'consume', 'conserve'.",
        "grammar_reason": "[GRA8] Structures: 'something we need...', 'If we do not...', 'Although the sea...', 'when we wash'. Error-free. >Band 7: Complex and accurate."
    },
    {
        "question": "Do we need friends?",
        "transcript": "Yes, friends are people who help us. If you have a problem, a friend can help. Although family is important, friends are important too. A life without friends would be sad. It is good to have someone who you can talk to. We should be nice to our friends.",
        "vocab_reason": "[LR5] Simple words: 'help', 'problem', 'important', 'sad', 'nice'. >Band 4: Accurate. Not Band 6: Lacks 'support', 'relationship', 'lonely'.",
        "grammar_reason": "[GRA8] Relative clause: 'people who help...'. Conditional: 'If you have...'. Contrast: 'Although family is...'. Error-free. >Band 7: High control."
    },
    {
        "question": "Why learn history?",
        "transcript": "History tells us about the past. If we know what happened before, we can learn. Although it was a long time ago, it is interesting. People who study history are smart. It helps us understand the world. We should know about our country.",
        "vocab_reason": "[LR5] Basic words: 'past', 'happened', 'learn', 'long time ago', 'interesting'. >Band 4: Clear. Not Band 6: Lacks 'events', 'ancient', 'knowledge'.",
        "grammar_reason": "[GRA8] Noun clause: 'what happened before'. Conditional: 'If we know...'. Contrast: 'Although it was...'. Relative clause: 'People who study...'. Error-free."
    },
    {
        "question": "Is money everything?",
        "transcript": "Money is good, but it is not everything. If you are rich but sick, it is bad. You cannot buy friends. Although we need money to eat, love is better. I think that being happy is the most important thing. Money is just paper.",
        "vocab_reason": "[LR5] Simple words: 'good', 'rich', 'sick', 'buy', 'eat', 'paper'. >Band 4: Understandable. Not Band 6: Lacks 'wealth', 'health', 'essential'.",
        "grammar_reason": "[GRA8] Contrast: 'but it is not...'. Conditional: 'If you are...'. Contrast: 'Although we need...'. Noun clause: 'that being happy...'. Error-free."
    },
    {
        "question": "Is walking good?",
        "transcript": "Walking is the best way to move. It is free and good for you. If you walk, you do not need a car. Although it is slow, you can see many things. People who walk are usually healthy. We should walk whenever we can.",
        "vocab_reason": "[LR5] Basic vocab: 'best', 'move', 'free', 'car', 'slow', 'healthy'. >Band 4: Clear. Not Band 6: Lacks 'exercise', 'transport', 'beneficial'.",
        "grammar_reason": "[GRA8] Conditional: 'If you walk...'. Contrast: 'Although it is...'. Relative clause: 'People who walk...'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Do you like pictures?",
        "transcript": "I like looking at pictures. They are beautiful. An artist is someone who can draw well. Although I cannot draw, I like to see art. It makes me think. If the world had no art, it would be boring. Museums are good places to go.",
        "vocab_reason": "[LR5] Simple words: 'pictures', 'beautiful', 'draw', 'art', 'think', 'boring'. >Band 4: Accurate. Not Band 6: Lacks 'painting', 'creative', 'appreciate'.",
        "grammar_reason": "[GRA8] Relative clause: 'someone who can...'. Contrast: 'Although I cannot...'. Conditional: 'If the world had...'. Error-free. >Band 7: Good complexity."
    },
    {
        "question": "Why sleep?",
        "transcript": "If we do not sleep, we get tired. Our body needs to rest. Although we have many things to do, we must sleep. People who sleep well are happy. It is important to go to bed early. If I sleep a lot, I feel good the next day.",
        "vocab_reason": "[LR5] Basic vocab: 'tired', 'rest', 'happy', 'bed', 'early'. >Band 4: Clear. Not Band 6: Lacks 'energy', 'recover', 'health'.",
        "grammar_reason": "[GRA8] Conditional: 'If we do not...'. Contrast: 'Although we have...'. Relative clause: 'People who sleep...'. Error-free. >Band 7: Excellent control."
    },
    {
        "question": "Are computers clever?",
        "transcript": "Computers can do many things that people cannot. They are very fast. Although they are machines, they seem clever. If we use them well, they help us. However, they can break. We should not trust them too much. People are still smarter than computers.",
        "vocab_reason": "[LR5] Simple words: 'things', 'fast', 'machines', 'clever', 'break', 'trust'. >Band 4: Understandable. Not Band 6: Lacks 'calculate', 'intelligent', 'rely'.",
        "grammar_reason": "[GRA8] Relative clause: 'things that people cannot'. Contrast: 'Although they are...'. Conditional: 'If we use them...'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Is trash a problem?",
        "transcript": "Yes, there is too much trash. People throw things away. If we recycled, it would be better. Although it is hard, we must try. The earth is getting dirty. We should put trash in the bin. It is a bad thing that we must fix.",
        "vocab_reason": "[LR5] Basic vocab: 'trash', 'throw', 'hard', 'dirty', 'bin', 'fix'. >Band 4: Clear. Not Band 6: Lacks 'waste', 'environment', 'solve'.",
        "grammar_reason": "[GRA8] Conditional: 'If we recycled...'. Contrast: 'Although it is...'. Relative clause: 'thing that we must fix'. Error-free. >Band 7: Sophisticated."
    },
    {
        "question": "Is family important?",
        "transcript": "Family is the most important thing. They are the people who love you. If you are in trouble, they will help. Although families fight, they stay together. A person without family is lonely. We should love our parents.",
        "vocab_reason": "[LR5] Simple words: 'thing', 'love', 'trouble', 'fight', 'stay', 'lonely'. >Band 4: Accurate. Not Band 6: Lacks 'support', 'relationship', 'connect'.",
        "grammar_reason": "[GRA8] Relative clause: 'people who love you'. Conditional: 'If you are...'. Contrast: 'Although families fight...'. Error-free. >Band 7: Good control."
    },
    {
        "question": "Will we work less?",
        "transcript": "I hope that we will work less. Machines can do the work for us. If machines do the work, we can play. Although work is good, free time is better. We should enjoy our lives. The future might be a place where we relax more.",
        "vocab_reason": "[LR5] Basic vocab: 'hope', 'work', 'machines', 'play', 'free time'. >Band 4: Clear. Not Band 6: Lacks 'labor', 'technology', 'leisure'.",
        "grammar_reason": "[GRA8] Noun clause: 'hope that we will...'. Conditional: 'If machines do...'. Contrast: 'Although work is...'. Relative clause: 'place where we relax'. Error-free."
    }
]

start_index = 1086
for i, item in enumerate(topics_13_1):
    samples.append(create_sample(
        index=start_index + i,
        vocab_band=5,
        grammar_band=8,
        question=item["question"],
        transcript=item["transcript"],
        response_type="extended",
        micro_flaws=[],
        grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
        vocab_reason=item["vocab_reason"],
        grammar_reason=item["grammar_reason"],
        idiom_present=False,
        risk_level="low"
    ))

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Generated {len(samples)} samples in {OUTPUT_FILE}")
