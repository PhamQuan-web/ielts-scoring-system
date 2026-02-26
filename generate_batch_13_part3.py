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

# --- BATCH 13 PART 3: SAMPLES 1121-1140 (20 Total) ---
# Combo: V4/G7 (Very Basic Vocab, Good Grammar)

# Sample 1121: V4/G7 - Topic: Environment
samples.append(create_sample(
    index=1121,
    vocab_band=4,
    grammar_band=7,
    question="Why should we protect nature?",
    transcript="It is good to protect nature because animals live there. If we cut down trees, the animals will have no home. Although people need wood, we should be careful. I think that if the air is bad, we will get sick. The world is a nice place that we must keep clean.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR4] Very basic vocabulary: 'good', 'bad', 'sick', 'clean', 'home'. >Band 3: Communicates meaning. Not Band 5: Lacks 'environment', 'pollution', 'preserve'.",
    grammar_reason="[GRA7] Uses complex structures accurately: 'If we cut down...', 'Although people need...', 'The world is a nice place that...'. Error-free. >Band 6: Frequent error-free sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 1122: V4/G7 - Topic: Technology
samples.append(create_sample(
    index=1122,
    vocab_band=4,
    grammar_band=7,
    question="Is the internet good?",
    transcript="The internet is good because it helps us find things. If I did not have the internet, I would not know many things. People who use computers can learn a lot. However, some things on the internet are bad. We should only look at good things. It is important that we use it well.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR4] Simple words: 'good', 'bad', 'things', 'know', 'learn'. >Band 3: Basic meaning clear. Not Band 5: Repetitive use of 'things'.",
    grammar_reason="[GRA7] Good use of conditionals: 'If I did not have... I would not know'. Relative clause: 'People who use...'. Contrast: 'However'. >Band 6: High accuracy.",
    idiom_present=False,
    risk_level="low"
))

# Sample 1123: V4/G7 - Topic: Education
samples.append(create_sample(
    index=1123,
    vocab_band=4,
    grammar_band=7,
    question="Why do we go to school?",
    transcript="We go to school so that we can get a job. If you do not go to school, you will not learn to read. Although it is hard work, it is good for you. Teachers are people who help us learn. I believe that school is the best place for children.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR4] Basic vocab: 'job', 'read', 'hard work', 'good', 'place'. >Band 3: Understandable. Not Band 5: Lacks 'education', 'future', 'knowledge'.",
    grammar_reason="[GRA7] Purpose: 'so that we can'. Conditionals: 'If you do not...'. Contrast: 'Although'. Relative clause: 'people who help us'. >Band 6: Error-free.",
    idiom_present=False,
    risk_level="low"
))

# Sample 1124: V4/G7 - Topic: Work
samples.append(create_sample(
    index=1124,
    vocab_band=4,
    grammar_band=7,
    question="Is money important?",
    transcript="Money is something that everyone needs. If you have no money, you cannot buy food. Although money is good, it does not make you happy. Friends are more important than money. A job that you like is better than a job with lots of money. We should work to live, not live to work.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR4] Simple words: 'needs', 'buy', 'food', 'happy', 'good'. >Band 3: Clear. Not Band 5: Lacks 'salary', 'essential', 'afford'.",
    grammar_reason="[GRA7] Relative clause: 'something that everyone needs'. Conditionals: 'If you have...'. Comparison: 'better than'. >Band 6: Good control.",
    idiom_present=False,
    risk_level="low"
))

# Sample 1125: V4/G7 - Topic: Society
samples.append(create_sample(
    index=1125,
    vocab_band=4,
    grammar_band=7,
    question="Why do people help others?",
    transcript="People help others because it is a nice thing to do. If I see someone who is sad, I want to help them. Helping people makes the world better. Although it takes time, it is good. I think that we should all be kind. A person who helps is a good person.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR4] Basic vocab: 'nice', 'sad', 'help', 'better', 'kind'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'support', 'community', 'generous'.",
    grammar_reason="[GRA7] Reason: 'because it is...'. Conditionals: 'If I see...'. Relative clause: 'someone who is sad'. >Band 6: Accurate structures.",
    idiom_present=False,
    risk_level="low"
))

# Generating 1126-1140 with explicit reasoning
topics_13_3 = [
    {
        "question": "Is sport good?",
        "transcript": "Sport is good because it makes your body strong. If you play sport, you will not get sick. Although it is tiring, it is fun. People who play games are usually happy. I think that everyone should move their body more.",
        "vocab_reason": "[LR4] Very basic vocabulary: 'good', 'strong', 'sick', 'fun', 'happy'. >Band 3: Understandable. Not Band 5: Lacks 'fitness', 'beneficial', 'enjoyable'.",
        "grammar_reason": "[GRA7] Uses complex structures accurately: 'because it makes...', 'If you play...', 'People who play...'. Error-free. >Band 6: High level of control."
    },
    {
        "question": "Are cars bad?",
        "transcript": "Cars are fast, but they make the air dirty. If we walk, it is better for the earth. Although cars are useful, we use them too much. A city with fewer cars would be a nice place. We should use the bus more.",
        "vocab_reason": "[LR4] Simple words: 'fast', 'dirty', 'walk', 'useful', 'nice'. >Band 3: Meaning clear. Not Band 5: Lacks 'pollution', 'environment', 'convenient'.",
        "grammar_reason": "[GRA7] Uses conditionals: 'If we walk...'. Contrast: 'Although cars are useful...'. Modals: 'would be', 'should use'. >Band 6: Error-free sentences."
    },
    {
        "question": "Do you like food?",
        "transcript": "I like food that tastes good. When I go to a new place, I eat new things. Although some food is strange, I try it. Food is something that brings people together. If you cook for your friends, they will be happy.",
        "vocab_reason": "[LR4] Basic vocab: 'good', 'new', 'strange', 'try', 'happy'. >Band 3: Communicates meaning. Not Band 5: Lacks 'cuisine', 'flavor', 'culture'.",
        "grammar_reason": "[GRA7] Relative clause: 'food that tastes good'. Time clause: 'When I go...'. Contrast: 'Although...'. Conditional: 'If you cook...'. >Band 6: Good control."
    },
    {
        "question": "Is your phone important?",
        "transcript": "My phone is important because I can talk to my family. If I did not have it, I would be sad. It is a small thing that does a lot. People who look at phones all day are not happy. We should use them less.",
        "vocab_reason": "[LR4] Simple words: 'talk', 'sad', 'small', 'happy', 'use'. >Band 3: Understandable. Not Band 5: Lacks 'communicate', 'device', 'technology'.",
        "grammar_reason": "[GRA7] Reason: 'because I can...'. Conditional: 'If I did not have...'. Relative clause: 'thing that does a lot', 'People who look...'. >Band 6: Accurate."
    },
    {
        "question": "Why recycle?",
        "transcript": "We should recycle so that there is less trash. If we throw things away, the earth gets dirty. Although it is easy to throw things, recycling is better. A bottle that you recycle can be used again. We must keep our home clean.",
        "vocab_reason": "[LR4] Basic vocab: 'trash', 'throw', 'dirty', 'easy', 'clean'. >Band 3: Clear. Not Band 5: Lacks 'waste', 'environment', 'reuse'.",
        "grammar_reason": "[GRA7] Purpose: 'so that there is...'. Conditional: 'If we throw...'. Contrast: 'Although it is easy...'. Relative clause: 'bottle that you recycle'. >Band 6: Error-free."
    },
    {
        "question": "Is family good?",
        "transcript": "Family are the people who love you. If you have a problem, they help. Although families fight, they are important. A life without family would be hard. I think that we should spend time with them. They are the best thing in life.",
        "vocab_reason": "[LR4] Simple words: 'love', 'help', 'fight', 'hard', 'best'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'support', 'relationship', 'connection'.",
        "grammar_reason": "[GRA7] Relative clause: 'people who love you'. Conditional: 'If you have...'. Contrast: 'Although families fight...'. Modal: 'would be'. >Band 6: Good structure."
    },
    {
        "question": "Will we work less?",
        "transcript": "I hope that we will work less in the future. If machines do the work, we can rest. Although work gives us money, time is better. A life where we play more would be nice. I think that robots will help us a lot.",
        "vocab_reason": "[LR4] Basic vocab: 'hope', 'work', 'money', 'time', 'play'. >Band 3: Understandable. Not Band 5: Lacks 'employment', 'leisure', 'technology'.",
        "grammar_reason": "[GRA7] Noun clause: 'hope that we will...'. Conditional: 'If machines do...'. Contrast: 'Although work gives...'. Relative clause: 'life where we play'. >Band 6: Accurate."
    },
    {
        "question": "Is reading good?",
        "transcript": "Reading is good because you learn new words. If you read a book, you can see a new world. Although TV is fun, books are better for your brain. People who read a lot are smart. We should read every day.",
        "vocab_reason": "[LR4] Simple words: 'good', 'learn', 'fun', 'better', 'smart'. >Band 3: Clear. Not Band 5: Lacks 'knowledge', 'imagination', 'intelligence'.",
        "grammar_reason": "[GRA7] Reason: 'because you learn...'. Conditional: 'If you read...'. Contrast: 'Although TV is fun...'. Relative clause: 'People who read...'. >Band 6: Error-free."
    },
    {
        "question": "Is traffic bad?",
        "transcript": "Traffic is bad because it wastes time. If there are too many cars, you cannot move. Although people want to go fast, they go slow. If we took the train, it would be better. We should stop driving so much.",
        "vocab_reason": "[LR4] Basic vocab: 'bad', 'time', 'fast', 'slow', 'stop'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'congestion', 'commute', 'transport'.",
        "grammar_reason": "[GRA7] Reason: 'because it wastes...'. Conditional: 'If there are...', 'If we took...'. Contrast: 'Although people want...'. >Band 6: High accuracy."
    },
    {
        "question": "Is sugar bad?",
        "transcript": "Sugar tastes good, but it is bad for your teeth. If you eat too much, you will get sick. Although I like sweet things, I do not eat them often. People who eat fruit are healthy. We should be careful with what we eat.",
        "vocab_reason": "[LR4] Simple words: 'good', 'bad', 'sick', 'sweet', 'healthy'. >Band 3: Understandable. Not Band 5: Lacks 'nutrition', 'diet', 'consume'.",
        "grammar_reason": "[GRA7] Contrast: 'but it is bad...'. Conditional: 'If you eat...'. Contrast: 'Although I like...'. Relative clause: 'People who eat...'. >Band 6: Error-free."
    },
    {
        "question": "Are computers smart?",
        "transcript": "Computers are fast, but they do not think. If you tell them what to do, they do it. Although they help us, they are just machines. A person who uses a computer is smart. We should use them to learn.",
        "vocab_reason": "[LR4] Basic vocab: 'fast', 'think', 'help', 'smart', 'learn'. >Band 3: Clear. Not Band 5: Lacks 'intelligent', 'process', 'technology'.",
        "grammar_reason": "[GRA7] Contrast: 'but they do not...'. Conditional: 'If you tell...'. Contrast: 'Although they help...'. Relative clause: 'person who uses...'. >Band 6: Good control."
    },
    {
        "question": "Why save water?",
        "transcript": "Water is something we need to drink. If we waste it, there will be none left. Although there is a lot of water, we cannot drink the sea. We should turn off the tap. It is a small thing that helps.",
        "vocab_reason": "[LR4] Simple words: 'drink', 'waste', 'sea', 'tap', 'small'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'conserve', 'resource', 'ocean'.",
        "grammar_reason": "[GRA7] Relative clause: 'something we need...'. Conditional: 'If we waste...'. Contrast: 'Although there is...'. Relative clause: 'thing that helps'. >Band 6: Accurate."
    },
    {
        "question": "Are friends important?",
        "transcript": "Friends are people who make you laugh. If you are sad, a friend can help. Although you might fight, friends are good. A life with friends is a happy life. We should be nice to the people we know.",
        "vocab_reason": "[LR4] Basic vocab: 'laugh', 'sad', 'help', 'fight', 'nice'. >Band 3: Understandable. Not Band 5: Lacks 'relationship', 'support', 'connect'.",
        "grammar_reason": "[GRA7] Relative clause: 'people who make...'. Conditional: 'If you are sad...'. Contrast: 'Although you might...'. Relative clause: 'people we know'. >Band 6: Error-free."
    },
    {
        "question": "Do you like music?",
        "transcript": "I like music because it makes me feel good. When I hear a song, I want to dance. Although some music is loud, it is fun. Music is something that everyone likes. It brings joy to the world.",
        "vocab_reason": "[LR4] Simple words: 'good', 'song', 'dance', 'loud', 'fun'. >Band 3: Clear. Not Band 5: Lacks 'melody', 'rhythm', 'enjoy'.",
        "grammar_reason": "[GRA7] Reason: 'because it makes...'. Time clause: 'When I hear...'. Contrast: 'Although some music...'. Relative clause: 'something that everyone likes'. >Band 6: Good structure."
    },
    {
        "question": "What is a good boss?",
        "transcript": "A good boss is someone who is kind. If you do a good job, they say well done. Although they are the boss, they should listen. A happy worker does a better job. I would like to have a nice boss.",
        "vocab_reason": "[LR4] Basic vocab: 'good', 'kind', 'job', 'happy', 'nice'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'leader', 'employee', 'manage'.",
        "grammar_reason": "[GRA7] Relative clause: 'someone who is kind'. Conditional: 'If you do...'. Contrast: 'Although they are...'. Modal: 'should listen'. >Band 6: Accurate."
    }
]

start_index = 1126
for i, item in enumerate(topics_13_3):
    samples.append(create_sample(
        index=start_index + i,
        vocab_band=4,
        grammar_band=7,
        question=item["question"],
        transcript=item["transcript"],
        response_type="extended",
        micro_flaws=[],
        grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
        vocab_reason=item["vocab_reason"],
        grammar_reason=item["grammar_reason"],
        idiom_present=False,
        risk_level="low"
    ))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
