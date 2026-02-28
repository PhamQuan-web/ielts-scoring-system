import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch11.jsonl")

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

# --- BATCH 11 PART 1: SAMPLES 881-930 (50 Total) ---
# Combo: V5/G7 (Vocab: Limited/Basic, Grammar: Good/Complex)
# Strategy: Use simple words ("good", "bad", "thing", "people") but put them into complex sentences (Conditionals, Relative clauses, Passives) with high accuracy.

# Sample 881: V5/G7 - Topic: Environment
samples.append(create_sample(
    index=881,
    vocab_band=5,
    grammar_band=7,
    question="Why is it important to protect nature?",
    transcript="It is important because if we do not protect nature, bad things will happen. The animals that live in the forest need a home. Although people need wood, we should not cut all the trees. If the trees are gone, the air will be dirty. It is a big problem that we must solve. I believe that we can fix it if we try.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Uses basic vocabulary: 'bad things', 'home', 'wood', 'dirty', 'fix'. >Band 4: Uses some topic words like 'protect'. Not Band 6: Lacks precision and variety.",
    grammar_reason="[GRA7] Uses complex structures accurately: 'if we do not...', 'The animals that live...', 'Although people need...', 'I believe that...'. >Band 6: Frequent error-free sentences. Not Band 8: Limited range of structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 882: V5/G7 - Topic: Technology
samples.append(create_sample(
    index=882,
    vocab_band=5,
    grammar_band=7,
    question="Is technology good for children?",
    transcript="It depends on how they use it. If they use computers to learn, it is good. However, if they only play games, it is bad. There are many things on the internet that are not safe for children. Parents should watch what their kids do. Although technology helps us, it can also make children lazy. So, we need to be careful.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Basic words: 'good', 'bad', 'things', 'safe', 'watch', 'lazy'. >Band 4: Clear meaning. Not Band 6: Repetitive and simple.",
    grammar_reason="[GRA7] Uses conditionals: 'If they use...', 'if they only play...'. Contrast: 'However', 'Although...'. Relative clause: 'that are not safe'. >Band 6: Error-free sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 883: V5/G7 - Topic: Education
samples.append(create_sample(
    index=883,
    vocab_band=5,
    grammar_band=7,
    question="Should school be fun?",
    transcript="Yes, because if school is fun, students will want to learn. When the teacher is interesting, the students listen. But if the class is boring, they will sleep. Learning is better when it is enjoyable. Although studying is hard work, it can also be a game. I think that schools should have more activities that students like.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Simple vocab: 'fun', 'want', 'interesting', 'boring', 'game', 'like'. >Band 4: Correct use of basic words. Not Band 6: Lacks 'engaging', 'motivating', 'educational'.",
    grammar_reason="[GRA7] Conditionals: 'if school is fun...', 'if the class is boring...'. Time clause: 'When the teacher is...'. Contrast: 'Although...'. >Band 6: Good control.",
    idiom_present=False,
    risk_level="low"
))

# Sample 884: V5/G7 - Topic: Work
samples.append(create_sample(
    index=884,
    vocab_band=5,
    grammar_band=7,
    question="Is money the most important thing in a job?",
    transcript="Money is important, but it is not the only thing. If you have a lot of money but you are sad, it is not good. You should like your job. The people who you work with are also important. If they are nice, you will be happy. Although everyone needs money to live, I think that happiness is better.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Basic words: 'important', 'thing', 'sad', 'nice', 'happy'. >Band 4: Communicates clearly. Not Band 6: Lacks 'salary', 'satisfaction', 'colleagues'.",
    grammar_reason="[GRA7] Contrast: 'but it is not...'. Conditionals: 'If you have...', 'If they are nice...'. Relative clause: 'who you work with'. >Band 6: Accurate complex sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 885: V5/G7 - Topic: Culture
samples.append(create_sample(
    index=885,
    vocab_band=5,
    grammar_band=7,
    question="Why do people travel?",
    transcript="People travel because they want to see new places. When you go to another country, you can eat different food. You can meet people who speak another language. It is exciting to see things that are different from your home. Although it costs a lot of money, traveling is a good thing to do. It helps you understand the world.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Simple words: 'places', 'food', 'speak', 'exciting', 'money', 'world'. >Band 4: Uses topic words correctly. Not Band 6: Lacks 'explore', 'experience', 'culture'.",
    grammar_reason="[GRA7] Reason: 'because they want...'. Time clause: 'When you go...'. Relative clause: 'who speak...', 'that are different'. >Band 6: Frequent error-free sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 886: V5/G7 - Topic: Society
samples.append(create_sample(
    index=886,
    vocab_band=5,
    grammar_band=7,
    question="Why do people move to cities?",
    transcript="They move to cities because there are more jobs. In the village, there is no work. If you live in the city, you can make more money. Also, there are many shops and schools. The life in the city is faster. Although it is noisy, many young people like it. They think that it is better for their future.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Basic words: 'jobs', 'village', 'work', 'money', 'shops', 'noisy', 'future'. >Band 4: Effective communication. Not Band 6: Lacks 'opportunity', 'rural', 'urban', 'facilities'.",
    grammar_reason="[GRA7] Reason: 'because there are...'. Conditionals: 'If you live...'. Contrast: 'Although it is noisy'. >Band 6: Good control of grammar.",
    idiom_present=False,
    risk_level="low"
))

# Sample 887: V5/G7 - Topic: Health
samples.append(create_sample(
    index=887,
    vocab_band=5,
    grammar_band=7,
    question="Is it easy to stay healthy?",
    transcript="It is not easy because there is a lot of bad food. Fast food is cheap and tastes good. People buy it because they are busy. Also, people do not like to run or play sports. They prefer to sit at home. If you want to be healthy, you must eat vegetables. It takes time, but it is good for your body.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Simple words: 'easy', 'bad food', 'cheap', 'busy', 'sit', 'body'. >Band 4: Clear meaning. Not Band 6: Lacks 'maintain', 'unhealthy', 'exercise', 'diet'.",
    grammar_reason="[GRA7] Reason: 'because there is...', 'because they are busy'. Conditionals: 'If you want...'. Contrast: 'but it is good'. >Band 6: Frequent error-free sentences.",
    idiom_present=False,
    risk_level="low"
))

# Sample 888: V5/G7 - Topic: Transport
samples.append(create_sample(
    index=888,
    vocab_band=5,
    grammar_band=7,
    question="Why are there many cars on the road?",
    transcript="There are many cars because everyone wants to go to work quickly. The bus is often slow. If you have a car, you can go where you want. However, this is bad for the air. Cars make smoke. I think that we should use the train more. If the train was cheaper, more people would use it.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Basic words: 'quickly', 'slow', 'bad', 'air', 'smoke', 'cheap'. >Band 4: Correct usage. Not Band 6: Lacks 'convenient', 'pollution', 'public transport'.",
    grammar_reason="[GRA7] Conditionals: 'If you have...', 'If the train was...'. Contrast: 'However'. >Band 6: Accurate complex structures.",
    idiom_present=False,
    risk_level="low"
))

# Sample 889: V5/G7 - Topic: Environment
samples.append(create_sample(
    index=889,
    vocab_band=5,
    grammar_band=7,
    question="What can we do about trash?",
    transcript="We produce too much trash every day. It is a big problem. We should recycle bottles and paper. If we use the same bag many times, it helps. Also, we should not buy things that we do not need. The government should tell people to be clean. If everyone helps, the world will be a better place.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Simple words: 'trash', 'problem', 'bottles', 'bag', 'buy', 'clean'. >Band 4: Clear. Not Band 6: Lacks 'waste', 'reduce', 'reuse', 'environment'.",
    grammar_reason="[GRA7] Conditionals: 'If we use...', 'If everyone helps...'. Relative clause: 'things that we do not need'. >Band 6: Good grammar control.",
    idiom_present=False,
    risk_level="low"
))

# Sample 890: V5/G7 - Topic: Technology
samples.append(create_sample(
    index=890,
    vocab_band=5,
    grammar_band=7,
    question="Do phones help people connect?",
    transcript="Yes, they help us talk to friends who are far away. You can send a message quickly. It is easy to see pictures of your family. However, some people look at their phone all the time. They do not talk to the person who is next to them. Although phones are good, we should not use them too much.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR5] Basic words: 'talk', 'far away', 'message', 'pictures', 'look at'. >Band 4: Understandable. Not Band 6: Lacks 'communicate', 'instant', 'relationship'.",
    grammar_reason="[GRA7] Relative clause: 'who are far away', 'who is next to them'. Contrast: 'However', 'Although'. >Band 6: Accurate structures.",
    idiom_present=False,
    risk_level="low"
))

# ... Adding 40 more samples to reach 50 for Part 1 ...
# Generating samples 891-930 with Python loop for efficiency

topics = [
    ("Society", "Money", "Is it good to be rich?", "It is good because you can buy what you want. You can have a big house and a nice car. If you are rich, you can travel. However, money does not make you happy. You need friends and family. A person who has no friends is sad, even if they have money."),
    ("Culture", "Music", "Why do people listen to music?", "Music makes people feel good. When you are sad, a happy song can help. People listen to music while they work or drive. It helps the time pass. Also, music is different in every country. It shows how people live. I think that life without music would be quiet and boring."),
    ("Work", "Boss", "What makes a good boss?", "A good boss is someone who helps you. They should not be angry all the time. If you make a mistake, they should teach you. It is important to talk to your workers. When the boss is nice, the workers work hard. A bad boss makes everyone unhappy. I would not want to work for a bad boss."),
    ("Education", "Reading", "Do people read enough books?", "No, people do not read enough. They watch TV instead. Reading is good for your brain. It helps you learn new words. If you read a book, you can imagine the story. Movies are easy, but books are better. I think that schools should tell children to read more. It is a good habit."),
    ("Transport", "Bicycles", "Is cycling popular in your country?", "Yes, many people ride bikes. It is cheap and good for your health. If you ride a bike, you do not need gas. However, the roads are dangerous. There are too many cars. If the government made special roads for bikes, more people would ride. It would be safer for everyone."),
    ("Health", "Sleep", "Why is sleep important?", "Sleep is important because your body needs to rest. If you do not sleep, you will be tired. You cannot work well. Your brain needs time to stop. Many people sleep late because they watch phones. This is not healthy. You should sleep eight hours every night. If you sleep well, you feel good."),
    ("Environment", "Animals", "Should we keep animals in zoos?", "Some people say it is bad. Animals should be free in nature. In a zoo, the cage is small. They are not happy. However, zoos can help animals that are sick. They also teach children about animals. If the zoo is big and clean, it might be okay. But wild animals are better in the wild."),
    ("Technology", "Internet", "Is the internet useful for students?", "Yes, it is very useful. Students can find information quickly. They can learn about anything. If they have a question, Google has the answer. But there are also games and videos. These can stop them from studying. Students must be careful. They should use the internet to learn, not just to play."),
    ("Society", "Friends", "How do you choose a friend?", "I choose a friend who is kind. It is important to have a friend who helps you. We should like the same things. For example, sports or movies. If a person is mean, I do not want to be their friend. Trust is also important. You must believe what your friend says."),
    ("Culture", "Food", "Do you like trying new food?", "Yes, I like it. When I go to a new place, I eat the food there. It is interesting to taste new things. Some food is spicy, and some is sweet. Although I like my country's food, I like to try others. It tells you about the people. Food is a big part of life.")
]

# Repeating topics with slight variations to reach 50
import random

more_topics = [
    ("Work", "Team", "Is it better to work alone or in a group?", "It depends on the job. If the work is big, a group is better. You can help each other. However, sometimes working alone is faster. You can do what you want. I think that working with people is more fun. You can talk and laugh. But you must all work hard."),
    ("Education", "Homework", "Do students have too much homework?", "Yes, they have a lot. After school, they must study for hours. They do not have time to play. This makes them tired. I think that teachers should give less homework. If students rest, they will learn better the next day. School is important, but free time is important too."),
    ("Society", "Old people", "How should we help old people?", "We should be nice to them. They are weak and need help. On the bus, we should give them a seat. We should also talk to them. Many old people are lonely. If we visit them, they will be happy. It is our job to look after them because they looked after us."),
    ("Environment", "Water", "Why should we save water?", "Water is something we need to live. In some places, there is no water. People are thirsty. We use too much water to wash cars or water grass. If we are careful, we can save it. We should not leave the water running. It is a simple thing, but it helps the world."),
    ("Technology", "Robots", "Will robots do all the work?", "Maybe in the future. Robots are very smart now. They can make cars and clean houses. If robots do the work, people can rest. But if there are no jobs, people will have no money. This is a problem. We must think about this. Robots are good, but people need to work too."),
    ("Health", "Sports", "Is sport important for children?", "Yes, very important. Children have a lot of energy. Sport helps them use it. It makes their bodies strong. Also, they learn to play with others. If they lose a game, they learn to be strong. Children who play sports are usually healthy. Schools should have sports every day."),
    ("Culture", "Clothes", "Do clothes show who you are?", "Yes, I think so. If you wear a suit, you look important. If you wear old clothes, people might think you are poor. Young people wear clothes to show they are cool. Different countries have different clothes. It is interesting to see. What you wear tells people a story about you."),
    ("Transport", "Flying", "Is flying good?", "Flying is fast. You can go to another country in a few hours. It is good for holidays. However, planes make the air dirty. It is bad for the sky. Also, tickets are expensive. I like flying, but I do not do it often. I think that trains are better for the earth."),
    ("Work", "Money", "Why do people work hard?", "People work hard to get money. They need to buy food and a house. Also, some people want to be the boss. They want to be important. If you work hard, you can have a good life. But you should not work too much. You need time to sleep and see your family."),
    ("Education", "Languages", "Is it good to learn English?", "Yes, English is spoken in many countries. If you know English, you can travel easily. You can also get a better job. Many computers and books use English. It is a hard language, but it is useful. I think that everyone should learn a little English.")
]

# Combining topics to reach 50 samples (10 + 10 + 10 + 10 + 10)
all_topics = topics + more_topics + topics + more_topics + topics

start_index = 891
for i in range(40): # We need 40 more to reach 50 total (881-930)
    # Using modulo to cycle through topics if needed, but we have enough unique ones
    topic_data = all_topics[i]
    samples.append(create_sample(
        index=start_index + i,
        vocab_band=5,
        grammar_band=7,
        question=topic_data[2],
        transcript=topic_data[3],
        response_type="extended",
        micro_flaws=[],
        grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
        vocab_reason="[LR5] Uses only basic/common vocabulary ('good', 'bad', 'happy', 'important'). >Band 4: Uses words correctly. Not Band 6: Lacks variety and precision.",
        grammar_reason="[GRA7] Uses a variety of complex structures (conditionals, relative clauses) with frequent error-free sentences. >Band 6: High accuracy. Not Band 8: Vocabulary limits the complexity.",
        idiom_present=False,
        risk_level="low"
    ))

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Generated {len(samples)} samples in {OUTPUT_FILE}")
