import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_18_p1.jsonl"

samples = [
    # --- V4/G4 (851-860) ---
    {
        "sample_id": "syn_p2_v4_g4_0851",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a color you like.",
        "transcript_cleaned": "I like blue color. It is nice color. I see blue in sky and sea. I wear blue shirt today. My room is blue. Blue make me feel happy. It is good color for boys. My car is blue too. I like blue because it is clean. My friend like red but I like blue. Blue is best color. I want paint my house blue. It is very beautiful color. Everyone should like blue.",
        "word_count": 83,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 4,
        "vocab_reason": "[LR4] Basic vocab: 'blue', 'sky', 'sea', 'shirt', 'room', 'happy', 'clean', 'beautiful'. Repetitive.",
        "grammar_reason": "[GRA4] 'Blue make me' (Agreement). 'Friend like red' (Agreement). 'Want paint' (Missing to). Simple sentences only.",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g4_0852",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a bag you have.",
        "transcript_cleaned": "I have a black bag. I use it for school. It is big bag. I put my books in it. I buy it last year. It cost not much money. It is strong bag. I like it because it carry many things. My mother give me money to buy. I take it every day. Sometimes I put my lunch inside. It has two pockets. It is useful for me. I keep it clean. It is my favorite bag.",
        "word_count": 84,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 4,
        "vocab_reason": "[LR4] Basic vocab: 'bag', 'school', 'books', 'money', 'strong', 'carry', 'pockets', 'useful'. Repetitive.",
        "grammar_reason": "[GRA4] 'I buy it' (Tense). 'It cost' (Tense). 'It carry' (Agreement). 'Mother give me' (Tense). Simple sentences only.",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g4_0853",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a drink you like.",
        "transcript_cleaned": "I like drink orange juice. It is sweet and good. I drink it in morning. It have vitamin C. It is healthy drink. I buy it from shop. Sometimes I make at home. I use fresh orange. My family like it too. We drink together at breakfast. It is yellow color. It taste very nice. I drink cold juice. It is better than water. I like fruit juice very much. It give me energy.",
        "word_count": 81,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 4,
        "vocab_reason": "[LR4] Basic vocab: 'orange juice', 'sweet', 'morning', 'healthy', 'shop', 'fresh', 'breakfast', 'energy'. Repetitive.",
        "grammar_reason": "[GRA4] 'I like drink' (Verb pattern). 'It have' (Agreement). 'Family like it' (Agreement). 'It taste' (Agreement). 'It give me' (Agreement).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g4_0854",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a flower you like.",
        "transcript_cleaned": "I like rose flower. It is red and beautiful. I see rose in garden. It smell very good. People give rose for love. I give rose to my mother. She like it. Rose has thorns so be careful. It grow in summer. I want plant rose in my house. It make garden look nice. There are many color of rose. White and pink also. But red is best. I think rose is queen of flowers.",
        "word_count": 81,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 4,
        "vocab_reason": "[LR4] Basic vocab: 'rose', 'flower', 'red', 'garden', 'smell', 'love', 'thorns', 'plant'. Repetitive.",
        "grammar_reason": "[GRA4] 'It smell' (Agreement). 'She like it' (Agreement). 'It grow' (Agreement). 'I want plant' (Missing to). 'It make garden' (Agreement).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g4_0855",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a bird you saw.",
        "transcript_cleaned": "I see a parrot in zoo. It was green and red. It can talk. It say hello to me. I was surprised. The parrot sit on a tree. It eat fruit. It look very funny. I take photo of it. It has big beak. Birds are nice animal. They can fly. I want to have parrot at home. But my mother say no. She say it is noisy. I like watch birds.",
        "word_count": 78,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 4,
        "vocab_reason": "[LR4] Basic vocab: 'parrot', 'zoo', 'green', 'talk', 'funny', 'photo', 'beak', 'fly', 'noisy'. Repetitive.",
        "grammar_reason": "[GRA4] 'I see' (Tense). 'It say' (Tense). 'Parrot sit' (Tense). 'It eat' (Tense). 'It look' (Tense). 'I like watch' (Verb pattern).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g4_0856",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a fruit you like.",
        "transcript_cleaned": "I like apple. It is red and round. It is sweet fruit. I eat apple every day. It is good for health. Doctor say eat apple is good. I buy apple at market. It is cheap. Sometimes I make apple juice. I like green apple too. But red is better. My brother like banana. I don't like banana. Apple is crunchy. I wash it before eat. It is tasty snack.",
        "word_count": 76,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 4,
        "vocab_reason": "[LR4] Basic vocab: 'apple', 'round', 'sweet', 'health', 'market', 'cheap', 'juice', 'crunchy', 'snack'. Repetitive.",
        "grammar_reason": "[GRA4] 'Doctor say' (Agreement). 'Eat apple is good' (Structure). 'Brother like' (Agreement). 'Before eat' (Form). Simple sentences.",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g4_0857",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a shoe you like.",
        "transcript_cleaned": "I like my running shoes. They are white and blue. I use them for running. They are very comfortable. I buy them from sports shop. They are expensive but good. I wear them to gym. I can run fast with them. I clean them every week. I like Nike brand. They look cool. My friends like my shoes. I want buy new pair soon. Shoes are important for feet.",
        "word_count": 75,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 4,
        "vocab_reason": "[LR4] Basic vocab: 'running shoes', 'comfortable', 'sports shop', 'expensive', 'gym', 'fast', 'brand', 'cool'. Repetitive.",
        "grammar_reason": "[GRA4] 'I buy them' (Tense context). 'I want buy' (Missing to). Simple sentences only.",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g4_0858",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a street in your city.",
        "transcript_cleaned": "There is a busy street in my city. It has many shops. People go there to buy things. There are many cars and buses. It is noisy street. I go there with friends. We eat food there. There are restaurants too. At night, it has lights. It looks nice. But sometimes it is dirty. I like walk there. It is center of city. Everyone know this street.",
        "word_count": 74,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 4,
        "vocab_reason": "[LR4] Basic vocab: 'busy street', 'shops', 'cars', 'buses', 'noisy', 'restaurants', 'lights', 'dirty', 'center'. Repetitive.",
        "grammar_reason": "[GRA4] 'I like walk' (Verb pattern). 'Everyone know' (Agreement). Simple sentences only.",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g4_0859",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a pen you use.",
        "transcript_cleaned": "I use a blue pen for writing. It is my favorite pen. It write very smooth. I use it for homework. I buy it at stationer. It is cheap. I have many pens but this one is best. I like the color. It is plastic pen. I keep it in my bag. I don't lose it. If I lose, I buy new one. Writing is important for student. Pen is useful tool.",
        "word_count": 78,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 4,
        "vocab_reason": "[LR4] Basic vocab: 'pen', 'writing', 'homework', 'stationer', 'cheap', 'plastic', 'bag', 'student', 'tool'. Repetitive.",
        "grammar_reason": "[GRA4] 'It write' (Agreement). 'This one is best' (Article). 'If I lose' (Conditional structure). Simple sentences.",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g4_0860",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a hat you like.",
        "transcript_cleaned": "I like my baseball cap. It is black color. I wear it when sunny. It protect my eyes. It has logo on front. It look cool. I wear it to park. My brother give it to me. It is old but good. I wash it sometimes. I like wear hat. It make me look handsome. I have many hats. But this is number one. I wear it backwards sometimes.",
        "word_count": 75,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 4,
        "vocab_reason": "[LR4] Basic vocab: 'baseball cap', 'black', 'sunny', 'protect', 'logo', 'cool', 'handsome', 'backwards'. Repetitive.",
        "grammar_reason": "[GRA4] 'It protect' (Agreement). 'It look' (Agreement). 'Brother give' (Tense). 'I like wear' (Verb pattern). 'It make me' (Agreement).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    # --- V5/G5 (861-870) ---
    {
        "sample_id": "syn_p2_v5_g5_0861",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a famous singer.",
        "transcript_cleaned": "I like Taylor Swift. She is very famous singer. She has blonde hair and blue eyes. She sings pop music. I like her songs because they are catchy. She write her own songs. I listen to her music every day. She is also rich and kind. She helps people. I went to her concert last year. It was exciting. Many people were there. She danced on stage. I want to meet her one day. She is my idol.",
        "word_count": 83,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Famous', 'blonde hair', 'catchy', 'concert', 'stage', 'idol'. Adequate.",
        "grammar_reason": "[GRA5] 'She write' (Agreement error). 'I went to' (Correct tense). 'She danced' (Correct tense). Simple sentences mostly correct.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0862",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful app.",
        "transcript_cleaned": "I use WhatsApp every day. It is a messaging app. I use it to talk to my friends and family. It is free and easy to use. I can send photos and videos. I can also make calls. It is very useful for me. I have a group chat with my classmates. We talk about homework. I like it because it is fast. I check it in the morning. Everyone uses WhatsApp now. It helps me stay connected.",
        "word_count": 84,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Messaging app', 'free', 'videos', 'group chat', 'classmates', 'connected'. Adequate.",
        "grammar_reason": "[GRA5] 'Easy to use' (Correct structure). 'I can send' (Modal). 'Everyone uses' (Correct agreement). Simple sentences mostly correct.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0863",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a healthy habit.",
        "transcript_cleaned": "I drink a lot of water every day. It is my healthy habit. Water is good for body. I drink 2 liters. It helps me feel fresh. I don't drink soda because it has sugar. Sugar is bad for teeth. I carry a water bottle with me. When I am thirsty, I drink water. My skin looks better now. I think everyone should drink water. It is cheap and healthy. I feel more energetic when I drink water.",
        "word_count": 85,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Habit', 'liters', 'fresh', 'soda', 'sugar', 'thirsty', 'energetic'. Adequate.",
        "grammar_reason": "[GRA5] 'Water is good' (Correct). 'It helps me' (Correct agreement). 'Because it has' (Connector). Simple sentences mostly correct.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0864",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a comedy movie.",
        "transcript_cleaned": "I watched a movie called 'Mr. Bean'. It is very funny. Mr. Bean is a silly man. He does stupid things. He does not talk much. He makes funny faces. I laughed a lot when I watched it. I watched it with my brother. He liked it too. It is a British movie. The story is simple. He goes to dentist or park. It makes people happy. I like comedy movies because they are relaxing.",
        "word_count": 80,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Funny', 'silly', 'stupid', 'faces', 'laughed', 'British', 'relaxing'. Adequate.",
        "grammar_reason": "[GRA5] 'Called Mr. Bean' (Participle). 'He does' (Agreement). 'I laughed' (Tense). 'Because they are' (Connector). Simple sentences mostly correct.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0865",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a computer game.",
        "transcript_cleaned": "I play a game called Minecraft. It is very popular. In this game, you can build things. You use blocks to make houses. There are monsters at night. You must be careful. I play it on my computer. I can play with friends online. It is creative game. I learned how to build designs. It is fun to explore the world. Sometimes I play for many hours. My parents say I play too much. But I like it.",
        "word_count": 85,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Popular', 'blocks', 'monsters', 'online', 'creative', 'designs', 'explore'. Adequate.",
        "grammar_reason": "[GRA5] 'You can build' (Modal). 'There are monsters' (Correct). 'I learned how to' (Structure). Simple sentences mostly correct.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0866",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a rainy day.",
        "transcript_cleaned": "Yesterday it rained all day. I stayed at home. I looked out the window. The sky was grey. The trees were wet. I could hear the rain. I felt sleepy. I read a book and drank tea. It was cozy inside. I did not go out. My dog was sleeping too. I like rain sometimes. It makes the air clean. But I don't like getting wet. Rainy days are good for resting.",
        "word_count": 78,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Rained', 'window', 'grey', 'wet', 'sleepy', 'cozy', 'resting'. Adequate.",
        "grammar_reason": "[GRA5] 'It rained' (Tense). 'I stayed' (Tense). 'Sky was grey' (Tense). Simple past used correctly mostly.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0867",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a fast food you like.",
        "transcript_cleaned": "I like eating burgers. It is my favorite fast food. I go to McDonald's often. The burger is tasty. It has meat, cheese, and salad. I also eat french fries. They are salty and good. I know it is not healthy. So I don't eat it every day. Only on weekends. It is cheap and fast. I like the sauce too. Fast food is convenient when I am busy. But I try to eat vegetables too.",
        "word_count": 82,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Burgers', 'tasty', 'meat', 'cheese', 'salad', 'french fries', 'salty', 'convenient'. Adequate.",
        "grammar_reason": "[GRA5] 'It is' (Agreement). 'I don't eat' (Negative). 'When I am busy' (Time clause). Simple sentences mostly correct.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0868",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a clever person.",
        "transcript_cleaned": "My friend Alex is very clever. He is good at math. He always gets high scores in exams. He helps me study. He can solve difficult problems. He reads many books. He knows about science and history. He wants to be a doctor. I think he is smart because he works hard. He is also funny. Being clever is a good thing. I respect him. He explains things clearly to me.",
        "word_count": 78,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Clever', 'math', 'scores', 'solve', 'difficult', 'smart', 'respect', 'explains'. Adequate.",
        "grammar_reason": "[GRA5] 'He is good at' (Idiom). 'He helps me study' (Verb pattern). 'Because he works hard' (Reason). Simple sentences mostly correct.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0869",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a quiet room.",
        "transcript_cleaned": "I like the library at my school. It is a quiet room. Students go there to read. You must be silent. There are many tables and chairs. I like the smell of old books. I can concentrate there. No one talks loudly. It is peaceful. I do my homework there. The lights are bright. I stay there for two hours. It is better than my house. My house is noisy. The library helps me study.",
        "word_count": 81,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Library', 'silent', 'concentrate', 'loudly', 'peaceful', 'bright', 'noisy'. Adequate.",
        "grammar_reason": "[GRA5] 'Students go' (Agreement). 'You must be' (Modal). 'There are many' (Structure). 'Better than' (Comparative). Simple sentences mostly correct.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0870",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a cheap item you bought.",
        "transcript_cleaned": "I bought a keychain last week. It was very cheap. It cost only one dollar. It is shaped like a cat. I put it on my bag. It looks cute. I bought it at a small shop. I didn't have much money. But I wanted a souvenir. It is made of plastic. It is not strong, but I like it. Cheap things can be nice too. I showed it to my sister. She wants one too.",
        "word_count": 83,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Keychain', 'cheap', 'shaped', 'cute', 'souvenir', 'plastic'. Adequate.",
        "grammar_reason": "[GRA5] 'I bought' (Tense). 'It cost' (Tense). 'Made of plastic' (Passive/Participle). Simple sentences mostly correct.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    # --- V6/G6 (871-880) ---
    {
        "sample_id": "syn_p2_v6_g6_0871",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a magazine you read.",
        "transcript_cleaned": "I enjoy reading a fashion magazine called 'Vogue'. I buy it every month from the bookstore. It has many pictures of clothes and models. I like looking at the new trends. The articles are interesting too. They talk about designers and lifestyle. It helps me improve my fashion sense. Sometimes there are interviews with famous people. The magazine is a bit expensive, but I think it is worth it. I usually read it on Sunday mornings with coffee.",
        "word_count": 84,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 6,
        "vocab_reason": "[LR6] 'Fashion magazine', 'models', 'trends', 'articles', 'designers', 'lifestyle', 'interviews'. Good range.",
        "grammar_reason": "[GRA6] 'Called Vogue' (Participle). 'Looking at' (Gerund). 'It helps me improve' (Verb pattern). 'But I think' (Connector). Correct simple/compound sentences.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v6_g6_0872",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a nice smell.",
        "transcript_cleaned": "I really love the smell of fresh coffee in the morning. It wakes me up and makes me feel energetic. When I walk into a cafe, the aroma is very strong. It smells rich and roasted. I usually drink coffee black, so I can taste the flavor better. The smell reminds me of relaxing weekends. It is a comforting scent. Even if I don't drink it, I like the smell. It is one of my favorite things.",
        "word_count": 84,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 6,
        "vocab_reason": "[LR6] 'Fresh coffee', 'energetic', 'aroma', 'rich', 'roasted', 'flavor', 'comforting scent'. Good range.",
        "grammar_reason": "[GRA6] 'Makes me feel' (Causative). 'When I walk' (Time clause). 'So I can taste' (Result). Correct simple/compound sentences.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v6_g6_0873",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a daily routine.",
        "transcript_cleaned": "My daily routine is quite simple. I wake up at 7 am and brush my teeth. Then I have breakfast, usually toast and eggs. I take the bus to work, which takes about thirty minutes. I work in an office until 5 pm. After work, I go to the gym to exercise. It helps me relieve stress. In the evening, I cook dinner and watch TV. I try to sleep early to get enough rest. I like having a routine because it keeps me organized.",
        "word_count": 89,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 6,
        "vocab_reason": "[LR6] 'Routine', 'breakfast', 'exercise', 'relieve stress', 'organized'. Good range.",
        "grammar_reason": "[GRA6] 'Which takes about' (Relative). 'To exercise' (Infinitive). 'To get enough rest' (Infinitive). 'Because it keeps' (Reason). Correct structures.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v6_g6_0874",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a park you know.",
        "transcript_cleaned": "There is a large park in the center of my city called Central Park. It is a green space with many trees and a lake. People go there to jog, have picnics, or just relax. I like visiting it on sunny days. The atmosphere is peaceful, away from the traffic noise. I often see children playing and people walking their dogs. Last week, I went there with my friends. We rented a boat on the lake. It is a great place to escape the city.",
        "word_count": 91,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 6,
        "vocab_reason": "[LR6] 'Green space', 'jog', 'picnics', 'atmosphere', 'traffic noise', 'rented', 'escape'. Good range.",
        "grammar_reason": "[GRA6] 'Called Central Park' (Participle). 'To jog' (Infinitive). 'Playing' (Participle). Correct simple/compound sentences.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v6_g6_0875",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a neighbor you know.",
        "transcript_cleaned": "I have a neighbor named Mrs. Smith. She is an elderly woman who lives alone. She is very kind and friendly. I often help her with carrying groceries. She likes gardening and has beautiful flowers in her yard. Sometimes she bakes cookies and gives them to me. We talk about the weather and news. I think it is important to be nice to neighbors. She treats me like a grandson. I respect her very much.",
        "word_count": 79,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 6,
        "vocab_reason": "[LR6] 'Elderly', 'groceries', 'gardening', 'bakes', 'treats', 'respect'. Good range.",
        "grammar_reason": "[GRA6] 'Who lives alone' (Relative). 'Carrying groceries' (Gerund). 'Gives them to me' (Object). Correct structures.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    }
]

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for sample in samples:
        # Standard fields
        sample["dataset_source"] = "synthetic"
        sample["is_valid"] = True
        sample["idiom_present"] = False
        sample["risk_level"] = "low"
        sample["instruction"] = "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning."

        # Micro flaws
        sample["micro_flaws"] = []
        if sample["grammar"] <= 5:
             sample["micro_flaws"] = ["Basic sentence structures", "Frequent grammatical errors"]

        # Input/Output construction
        sample["input"] = f"Part: {sample['part']}\nQuestion: {sample['question']}\n\nTranscript: {sample['transcript_cleaned']}\n\nWord Count: {sample['word_count']} words\nResponse Type: {sample['response_type']}"

        output_text = f"## Vocabulary (Lexical Resource): Band {sample['vocabulary']}\n\n**Reasoning:** {sample['vocab_reason']}\n\n>Band {sample['vocabulary']-1}: ...\n\nNot Band {sample['vocabulary']+1}: ...\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band {sample['grammar']}\n\n**Reasoning:** {sample['grammar_reason']}\n\n>Band {sample['grammar']-1}: ...\n\nNot Band {sample['grammar']+1}: ...\n\n**Micro flaws identified:**\n- None."

        sample["output"] = output_text

        f.write(json.dumps(sample) + '\n')
