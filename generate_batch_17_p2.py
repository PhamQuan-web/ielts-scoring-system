import json
import os

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_17_p2.jsonl"

samples = [
    # --- V6/G8 (826-835) ---
    {
        "sample_id": "syn_p2_v6_g8_0826",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a place you like to visit.",
        "transcript_cleaned": "I would like to tell you about a small town I visit every summer. It is located near the sea and has a nice beach. The scenery is beautiful, with many trees and flowers. The air is clean, and the people are friendly. I usually stay there for two weeks to relax. I enjoy swimming and eating seafood. It is a quiet place where I can forget my work. Although there are not many shops, I like the atmosphere. I think it is important to take a break sometimes.",
        "word_count": 91,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 8,
        "vocab_reason": "[LR6] 'Scenery', 'atmosphere', 'seafood', 'relax', 'take a break'. Adequate range.",
        "grammar_reason": "[GRA8] 'Where I can forget' (Relative). 'Although there are not' (Concessive). 'It is located near' (Passive). Error-free complex structures.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g8_0827",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book you read recently.",
        "transcript_cleaned": "I read a book last month that was very interesting. It was a mystery story about a detective solving a crime. The plot was exciting and kept me guessing until the end. The writer described the characters very well. I could imagine what they looked like. I read it every night before sleeping. It took me one week to finish it. I would recommend this book to my friends because it is fun to read. Reading helps me improve my English skills too.",
        "word_count": 87,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 8,
        "vocab_reason": "[LR6] 'Mystery story', 'detective', 'crime', 'plot', 'characters', 'recommend'. Adequate range.",
        "grammar_reason": "[GRA8] 'That was very interesting' (Relative). 'Kept me guessing' (Participle). 'What they looked like' (Noun clause). 'Because it is fun' (Reason). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g8_0828",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you received.",
        "transcript_cleaned": "My sister gave me a watch for my birthday, which I wear every day. It is a silver watch with a leather strap. I like it because it looks classic and matches my clothes. She bought it from a famous shop in the city. It was a surprise for me. I felt very happy when I opened the box. The watch is useful because I can check the time easily. It reminds me of my sister whenever I look at it.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 8,
        "vocab_reason": "[LR6] 'Leather strap', 'classic', 'matches', 'surprise', 'useful', 'reminds'. Adequate range.",
        "grammar_reason": "[GRA8] 'Which I wear every day' (Relative). 'Because it looks classic' (Reason). 'Whenever I look at it' (Time clause). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g8_0829",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a job you would like to do.",
        "transcript_cleaned": "I am interested in becoming a teacher in the future. I think teaching is a rewarding job because you can help students learn. I want to teach history to high school students. It requires patience and good communication skills. I would enjoy preparing lessons and correcting homework. Although the salary is not very high, the satisfaction is great. I remember my history teacher who inspired me a lot. I want to be like him and make a difference in young people's lives.",
        "word_count": 87,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 8,
        "vocab_reason": "[LR6] 'Rewarding', 'patience', 'communication skills', 'satisfaction', 'inspired', 'make a difference'. Adequate range.",
        "grammar_reason": "[GRA8] 'Because you can help' (Reason). 'Preparing lessons' (Gerund). 'Although the salary is not' (Concessive). 'Who inspired me' (Relative). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g8_0830",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a sport you like to play.",
        "transcript_cleaned": "I enjoy playing badminton with my friends on weekends. It is an active sport that requires speed and agility. We play at a sports center near my house. I like it because it is good exercise and helps me stay fit. The rules are simple to understand. Sometimes we play doubles, which is more fun. After playing, we usually go for a drink. It is a good way to socialize and relieve stress. I have been playing for five years now.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 8,
        "vocab_reason": "[LR6] 'Active sport', 'agility', 'stay fit', 'doubles', 'socialize', 'relieve stress'. Adequate range.",
        "grammar_reason": "[GRA8] 'That requires speed' (Relative). 'Which is more fun' (Relative). 'After playing' (Preposition + Gerund). 'Have been playing' (Present Perfect Continuous). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g8_0831",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a meal you prepared.",
        "transcript_cleaned": "I cooked a special dinner for my parents last anniversary. I decided to make spaghetti with tomato sauce and meatballs. I bought fresh ingredients from the market in the morning. Following a recipe I found online, I prepared the sauce carefully. It took about two hours to cook everything. My parents were surprised and happy. They said the food was delicious. I felt proud of myself for making them happy. Cooking is a useful skill that I want to improve.",
        "word_count": 84,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 8,
        "vocab_reason": "[LR6] 'Anniversary', 'ingredients', 'recipe', 'prepared', 'delicious', 'proud', 'useful skill'. Adequate range.",
        "grammar_reason": "[GRA8] 'Following a recipe...' (Participle). 'That I want to improve' (Relative). 'For making them happy' (Gerund). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g8_0832",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a journey you went on.",
        "transcript_cleaned": "I went on a train journey to the mountains last winter. The trip took four hours, but the view was amazing. I could see snow on the trees and fields. The train was comfortable and clean. I sat by the window and listened to music. When we arrived, the air was very cold. We stayed in a small hotel for three days. It was a memorable trip because I saw snow for the first time. I want to go there again next year.",
        "word_count": 87,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 8,
        "vocab_reason": "[LR6] 'Journey', 'view', 'comfortable', 'memorable', 'arrived'. Adequate range.",
        "grammar_reason": "[GRA8] 'But the view was' (Connector). 'When we arrived' (Time clause). 'Because I saw snow' (Reason). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g8_0833",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision you made.",
        "transcript_cleaned": "I had to decide which university to attend after high school. It was a hard choice because I had two options. One was near my home, and the other was in another city. I talked to my parents and teachers for advice. I considered the cost and the courses. Finally, I chose the one in the other city to be independent. It was scary at first, but now I am happy. It taught me how to take responsibility for my life.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 8,
        "vocab_reason": "[LR6] 'Options', 'advice', 'considered', 'independent', 'responsibility'. Adequate range.",
        "grammar_reason": "[GRA8] 'Which university to attend' (Noun clause). 'Because I had' (Reason). 'To be independent' (Infinitive). 'How to take responsibility' (Noun clause). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g8_0834",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a successful person.",
        "transcript_cleaned": "I admire my uncle who is a successful businessman. He started his own company ten years ago. He works very hard and is always busy. Despite his success, he is humble and kind. He treats his employees with respect. He often donates money to charity. I think he is successful not only because of money but also because of his character. He taught me that hard work is the key to success. I hope to be like him in the future.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 8,
        "vocab_reason": "[LR6] 'Businessman', 'humble', 'employees', 'charity', 'character', 'key to success'. Adequate range.",
        "grammar_reason": "[GRA8] 'Who is a successful businessman' (Relative). 'Despite his success' (Prepositional). 'Not only... but also' (Correlative). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g8_0835",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a crowded place.",
        "transcript_cleaned": "I visited a shopping mall on the weekend that was extremely crowded. There were people everywhere, pushing and shouting. It was noisy and hot inside. I went there to buy clothes for a party. I had to wait in line for a long time to pay. Although I found what I wanted, the experience was tiring. I prefer shopping online because it is more convenient. Crowded places make me feel stressed. I will try to go on a weekday next time.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 8,
        "vocab_reason": "[LR6] 'Extremely crowded', 'wait in line', 'tiring', 'convenient', 'stressed'. Adequate range.",
        "grammar_reason": "[GRA8] 'That was extremely crowded' (Relative). 'Pushing and shouting' (Participle). 'Although I found' (Concessive). 'Make me feel' (Causative). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    # --- V8/G6 (836-845) ---
    {
        "sample_id": "syn_p2_v8_g6_0836",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a website you visit often.",
        "transcript_cleaned": "I frequently browse a website called Reddit, which is a massive aggregation of communities. It covers a plethora of topics from science to memes. The content is user-generated, which makes it very diverse. I enjoy reading the discussions and debates in the comment sections. It is a great way to stay updated on current events and viral trends. However, sometimes the people there is rude. The interface are a bit complicated for new users. I spending hours scrolling through the feed. It can be addictive but also informative.",
        "word_count": 92,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 6,
        "vocab_reason": "[LR8] 'Aggregation', 'plethora', 'user-generated', 'diverse', 'viral trends', 'interface', 'addictive'. Sophisticated.",
        "grammar_reason": "[GRA6] 'People there is rude' (Agreement). 'Interface are' (Agreement). 'I spending' (Tense). Complex vocab, mixed grammar.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v8_g6_0837",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you were surprised.",
        "transcript_cleaned": "I was astonished when I received a scholarship for my studies. It was a prestigious award that covers my tuition fees. I had submitted my application with skepticism, not expecting to win. The competition was fierce, with many talented candidates. When I got the email, I was ecstatic and overwhelmed. I called my parents immediately to share the news. They was very proud of me. This scholarship alleviate the financial burden on my family. It motivate me to work harder. I will never forget that moment of pure joy.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 6,
        "vocab_reason": "[LR8] 'Astonished', 'prestigious award', 'skepticism', 'fierce competition', 'ecstatic', 'overwhelmed', 'alleviate', 'financial burden'. Sophisticated.",
        "grammar_reason": "[GRA6] 'They was' (Agreement). 'Scholarship alleviate' (Agreement). 'It motivate me' (Agreement). Complex vocab, mixed grammar.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v8_g6_0838",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a photograph you like.",
        "transcript_cleaned": "I have a cherished photograph of my grandparents on their wedding day. It is a black and white image that exudes nostalgia. They look so young and vibrant, posing in front of an old car. The composition is candid and authentic. It captures a fleeting moment of happiness. I keep it in a silver frame on my desk. Every time I looking at it, I feel a sense of connection to my heritage. It remind me of the enduring power of love. The photo is a precious heirloom for our family.",
        "word_count": 95,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 6,
        "vocab_reason": "[LR8] 'Cherished', 'exudes nostalgia', 'vibrant', 'composition', 'candid', 'authentic', 'fleeting moment', 'heritage', 'enduring power', 'heirloom'. Sophisticated.",
        "grammar_reason": "[GRA6] 'Every time I looking' (Tense). 'It remind me' (Agreement). Complex vocab, mixed grammar.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v8_g6_0839",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you helped a stranger.",
        "transcript_cleaned": "I assisted a tourist who was disoriented in the city center. He was looking at a map with a confused expression. I approached him and asked if he needed directions. He was searching for the museum, which was quite obscure. I gave him detailed instructions on how to get there. He was very grateful and relieved. Helping him gave me a sense of altruism. It is important to show hospitality to visitors. Even though I was in a hurry, I stop to help. Small acts of kindness makes a difference.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 6,
        "vocab_reason": "[LR8] 'Assisted', 'disoriented', 'obscure', 'detailed instructions', 'grateful', 'altruism', 'hospitality'. Sophisticated.",
        "grammar_reason": "[GRA6] 'I stop to help' (Tense). 'Kindness makes' (Agreement - wait, kindness is singular, makes is correct. Let's force an error). 'Acts of kindness makes' (Agreement - Acts is plural). Complex vocab, mixed grammar.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v8_g6_0840",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of advice you followed.",
        "transcript_cleaned": "My father advised me to be frugal and save for a rainy day. He emphasized the importance of financial prudence and avoiding debt. I took his words to heart and started budgeting meticulously. I cut down on frivolous spending and invested in stocks. It was difficult to resist the temptation of buying new gadgets. However, seeing my savings grow was gratifying. Thanks to his wisdom, I am now financially stable. I think young people needs to learn about money management. It is a crucial life skill that is often neglected.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 6,
        "vocab_reason": "[LR8] 'Frugal', 'rainy day', 'financial prudence', 'debt', 'meticulously', 'frivolous spending', 'temptation', 'gratifying', 'neglected'. Sophisticated.",
        "grammar_reason": "[GRA6] 'Young people needs' (Agreement). 'Taking his words' (Fragment). Complex vocab, mixed grammar.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v8_g6_0841",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "The Colosseum in Rome is a monumental structure that is iconic globally. It is an amphitheater where gladiators used to fight. The architecture is imposing, showcasing the ingenuity of the Romans. Despite being in ruins, it still retains its grandeur. I visited it two years ago and was awe-struck by its scale. It stands as a testament to the ancient civilization. However, the queue to enter were very long. Also, the restoration work are ongoing. Preserving such heritage sites is imperative for future generations. It is a marvel of engineering.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 6,
        "vocab_reason": "[LR8] 'Monumental structure', 'iconic', 'amphitheater', 'imposing', 'ingenuity', 'grandeur', 'awe-struck', 'testament', 'imperative'. Sophisticated.",
        "grammar_reason": "[GRA6] 'Queue... were' (Agreement). 'Restoration work are' (Agreement). Complex vocab, mixed grammar.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v8_g6_0842",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a stressful situation.",
        "transcript_cleaned": "I experienced a chaotic situation when my laptop crashed before a deadline. I was working on a crucial assignment for university. The screen went black and I panicked. I had not backed up my files, which was negligent of me. I felt a surge of anxiety and desperation. I rushed to a technician to fix it. Fortunately, he managed to retrieve the data. It was a harrowing ordeal that taught me a lesson. Now I always saving my work on the cloud. Technology can be unpredictable and frustrating.",
        "word_count": 93,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 6,
        "vocab_reason": "[LR8] 'Chaotic', 'crucial assignment', 'negligent', 'surge of anxiety', 'desperation', 'retrieve', 'harrowing ordeal', 'unpredictable'. Sophisticated.",
        "grammar_reason": "[GRA6] 'I always saving' (Tense). 'Screen went... and I panicked' (Run-on). Complex vocab, mixed grammar.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v8_g6_0843",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a change in your local area.",
        "transcript_cleaned": "My neighborhood has undergone a significant transformation recently. A new shopping complex was constructed, replacing an old park. This development has revitalized the area, attracting more commerce. However, some residents are disgruntled about the gentrification. The traffic congestion has worsened significantly. Also, the noise pollution are unbearable during the day. While the economy has improved, the tranquility is gone. I have mixed feelings about this urbanization. Progress is inevitable, but we must consider the environmental impact. The skyline look completely different now.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 6,
        "vocab_reason": "[LR8] 'Transformation', 'revitalized', 'commerce', 'disgruntled', 'gentrification', 'congestion', 'tranquility', 'urbanization', 'inevitable'. Sophisticated.",
        "grammar_reason": "[GRA6] 'Noise pollution are' (Agreement). 'Skyline look' (Agreement). Complex vocab, mixed grammar.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v8_g6_0844",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a valuable skill.",
        "transcript_cleaned": "Being bilingual is an advantageous skill in the modern world. It enhances cognitive flexibility and cultural awareness. I learned English and Spanish, which has opened many doors for me. It allows me to communicate with a broader demographic. Employers value language proficiency highly. Learning a language require dedication and perseverance. It is not easy to master the nuances of grammar. However, the benefits outweighs the effort. It also delay the onset of dementia in old age. Everyone should try to learn a second language.",
        "word_count": 88,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 6,
        "vocab_reason": "[LR8] 'Advantageous', 'cognitive flexibility', 'cultural awareness', 'broader demographic', 'proficiency', 'dedication', 'nuances', 'dementia'. Sophisticated.",
        "grammar_reason": "[GRA6] 'Language require' (Agreement). 'Benefits outweighs' (Agreement). 'It also delay' (Agreement). Complex vocab, mixed grammar.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v8_g6_0845",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a movie you disliked.",
        "transcript_cleaned": "I watched a sci-fi movie that was utterly disappointing. The plot was convoluted and riddled with inconsistencies. The special effects were mediocre at best. I found the dialogue to be cliché and uninspired. The acting was wooden, lacking emotional depth. I struggled to stay awake during the screening. It was a waste of time and money. The critics had praised it, which baffled me. I think the hype was unjustified. I prefer movies that has a coherent narrative and compelling characters.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 6,
        "vocab_reason": "[LR8] 'Utterly disappointing', 'convoluted', 'inconsistencies', 'mediocre', 'cliché', 'uninspired', 'baffled', 'unjustified', 'coherent narrative'. Sophisticated.",
        "grammar_reason": "[GRA6] 'Movies that has' (Agreement). 'Struggled to stay' (ok). Complex vocab, mixed grammar.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    # --- V5/G4 (846-850) ---
    {
        "sample_id": "syn_p2_v5_g4_0846",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a family celebration.",
        "transcript_cleaned": "I go to my sister wedding last month. It was big party. Many people come to celebrate. We eat good food and dance. My sister wear white dress. She look beautiful. I am happy for her. We take many photo together. My mother cry because she is happy. The music was loud. I meet my cousins there. We talk and laugh. It was fun day. I like wedding because family come together. We give gift to them.",
        "word_count": 83,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Wedding', 'celebrate', 'white dress', 'beautiful', 'loud', 'gift'. Basic but accurate.",
        "grammar_reason": "[GRA4] 'I go to' (Tense). 'Many people come' (Tense). 'My sister wear' (Agreement). 'She look' (Agreement). 'Mother cry' (Agreement).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0847",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a place you want to visit.",
        "transcript_cleaned": "I want visit Japan one day. It is beautiful country. I like eat sushi. Sushi is delicious food. I want see cherry blossom trees. They are pink and nice. I also want buy electronic things. Japan have many technology. I watch anime on TV. I want see where it make. My friend go there last year. He say it is expensive. But I save money now. I hope I can go soon. It is my dream.",
        "word_count": 82,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Delicious', 'cherry blossom', 'electronic', 'technology', 'expensive', 'dream'. Basic.",
        "grammar_reason": "[GRA4] 'I want visit' (Missing to). 'Like eat' (Missing to). 'Want see' (Missing to). 'Japan have' (Agreement). 'Where it make' (Passive error).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0848",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend you like.",
        "transcript_cleaned": "My best friend is John. He is funny man. We play football together every week. He live near my house. He help me with homework. We know each other for ten years. He is tall and have black hair. He like eat pizza. Sometimes we go cinema. He is good friend. We never fight. I trust him. If I have problem, I talk to him. He listen to me. Everyone like him because he is kind.",
        "word_count": 82,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Funny', 'football', 'homework', 'cinema', 'trust', 'problem', 'kind'. Basic.",
        "grammar_reason": "[GRA4] 'He live' (Agreement). 'He help' (Agreement). 'He have' (Agreement). 'He like' (Agreement). 'Everyone like' (Agreement).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0849",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a toy you liked.",
        "transcript_cleaned": "I like my toy car when I was small. It was red color. My father buy it for me. I play with it every day. It go very fast. I race with my friends. I love that car. One day, it break. I was sad. My father fix it. I was happy again. I keep it in my room. It is old now. But I still like it. It remind me of my childhood. Toys are fun for kids.",
        "word_count": 85,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Red color', 'race', 'break', 'fix', 'childhood'. Basic.",
        "grammar_reason": "[GRA4] 'My father buy' (Tense). 'It go' (Tense). 'It break' (Tense). 'It remind' (Agreement). Basic simple sentences.",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0850",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a room in your house.",
        "transcript_cleaned": "I like my bedroom. It is my favorite room. It is small but comfortable. I have bed and desk. I sleep there at night. I study at my desk. The wall is blue. I put poster on wall. I have computer too. I play game on it. My room is quiet. I can relax there. I clean my room every week. I want to buy new chair. My room is private place. I like stay there alone.",
        "word_count": 82,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Bedroom', 'comfortable', 'desk', 'poster', 'computer', 'quiet', 'private'. Basic.",
        "grammar_reason": "[GRA4] 'I have bed' (Article). 'Wall is blue' (Article). 'Put poster' (Article). 'Like stay' (Missing to).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
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
