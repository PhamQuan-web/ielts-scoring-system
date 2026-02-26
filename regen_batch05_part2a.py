import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch05.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v6_g7_376",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a festival in your country.",
        "transcript_cleaned": "I would like to talk about the Mid-Autumn Festival, which is a traditional celebration in my country. It is usually held in September or October when the moon is fullest. Families gather to eat mooncakes and drink tea while admiring the moon. Children play with colorful lanterns, which is a beautiful sight. There are also lion dances in the streets. It is a time for reunion and harmony. I love the festive atmosphere and the delicious food. One of the legends associated with it is about a lady who lives on the moon. It is a very meaningful festival that connects us with our heritage.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'celebration', 'fullest', 'mooncakes', 'admiring', 'lanterns', 'reunion', 'harmony', 'festive', 'legends', 'heritage'. Band 6 level.",
             "grammar: 'Festival, which is', 'held... when the moon', 'associated with it is'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'mooncakes', 'admiring', 'lanterns', 'reunion', 'harmony', 'legends', 'heritage'. >Band 5: 'Lanterns', 'reunion'. Not Band 7: 'Traditional celebration', 'delicious food' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'Festival, which is', 'associated with it is'. >Band 6: Relative clauses and passive voice used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a festival in your country.\n\nTranscript: I would like to talk about the Mid-Autumn Festival, which is a traditional celebration in my country. It is usually held in September or October when the moon is fullest. Families gather to eat mooncakes and drink tea while admiring the moon. Children play with colorful lanterns, which is a beautiful sight. There are also lion dances in the streets. It is a time for reunion and harmony. I love the festive atmosphere and the delicious food. One of the legends associated with it is about a lady who lives on the moon. It is a very meaningful festival that connects us with our heritage.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'mooncakes', 'admiring', 'lanterns', 'reunion', 'harmony', 'legends', 'heritage'. \n\n>Band 5: 'Lanterns', 'reunion'.\n\nNot Band 7: 'Traditional celebration', 'delicious food' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'Festival, which is', 'associated with it is'. \n\n>Band 6: Relative clauses and passive voice used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_377",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of technology you use.",
        "transcript_cleaned": "I want to describe my smartwatch, which I wear every day. It is a very convenient device that connects to my phone via Bluetooth. I use it to track my fitness activities, such as running and swimming. It monitors my heart rate and counts my steps. I also receive notifications for messages and calls on my wrist. It saves me time because I do not have to check my phone constantly. The battery life is decent, lasting for two days. It has a sleek design that looks good with any outfit. I find it very useful for maintaining a healthy lifestyle and staying organized.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'convenient', 'connects', 'via', 'fitness activities', 'monitors', 'notifications', 'wrist', 'constantly', 'decent', 'sleek design', 'maintaining'. Band 6 level.",
             "grammar: 'smartwatch, which I wear', 'use it to track', 'because I do not'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'convenient', 'via', 'monitors', 'notifications', 'sleek design', 'maintaining'. >Band 5: 'Convenient', 'monitors'. Not Band 7: 'Heart rate', 'battery life' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'smartwatch, which I wear', 'saves me time because'. >Band 6: Relative clauses and causal structures used correctly. Not Band 8: Lacks full flexibility.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a piece of technology you use.\n\nTranscript: I want to describe my smartwatch, which I wear every day. It is a very convenient device that connects to my phone via Bluetooth. I use it to track my fitness activities, such as running and swimming. It monitors my heart rate and counts my steps. I also receive notifications for messages and calls on my wrist. It saves me time because I do not have to check my phone constantly. The battery life is decent, lasting for two days. It has a sleek design that looks good with any outfit. I find it very useful for maintaining a healthy lifestyle and staying organized.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'convenient', 'via', 'monitors', 'notifications', 'sleek design', 'maintaining'. \n\n>Band 5: 'Convenient', 'monitors'.\n\nNot Band 7: 'Heart rate', 'battery life' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'smartwatch, which I wear', 'saves me time because'. \n\n>Band 6: Relative clauses and causal structures used correctly.\n\nNot Band 8: Lacks full flexibility.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_378",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a childhood memory.",
        "transcript_cleaned": "I remember my first day of primary school very clearly. I was five years old and feeling very nervous. My mother walked me to the classroom and introduced me to the teacher. I was shy at first, but soon I made friends with a girl named Sarah. We played with blocks and drew pictures together. The teacher was kind and read us a story. I remember wearing my new uniform, which was a bit too big for me. At lunchtime, I shared my sandwich with my new friend. It was a day mixed with anxiety and excitement, but it turned out to be a great start to my education.",
        "word_count": 109,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'nervous', 'introduced', 'shy', 'blocks', 'uniform', 'anxiety', 'excitement', 'education'. Band 6 level.",
             "grammar: 'old and feeling', 'uniform, which was', 'turned out to be'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'nervous', 'introduced', 'anxiety', 'excitement', 'education'. >Band 5: 'Nervous', 'shy'. Not Band 7: 'First day', 'made friends' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'uniform, which was', 'mixed with anxiety', 'turned out to be'. >Band 6: Relative clauses and participles used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a childhood memory.\n\nTranscript: I remember my first day of primary school very clearly. I was five years old and feeling very nervous. My mother walked me to the classroom and introduced me to the teacher. I was shy at first, but soon I made friends with a girl named Sarah. We played with blocks and drew pictures together. The teacher was kind and read us a story. I remember wearing my new uniform, which was a bit too big for me. At lunchtime, I shared my sandwich with my new friend. It was a day mixed with anxiety and excitement, but it turned out to be a great start to my education.\n\nWord Count: 109 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'nervous', 'introduced', 'anxiety', 'excitement', 'education'. \n\n>Band 5: 'Nervous', 'shy'.\n\nNot Band 7: 'First day', 'made friends' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'uniform, which was', 'mixed with anxiety', 'turned out to be'. \n\n>Band 6: Relative clauses and participles used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_379",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a goal you achieved.",
        "transcript_cleaned": "I set a goal to lose weight last year. I was not happy with my health, so I decided to make a change. I joined a gym and started working out three times a week. I also changed my diet, eating more vegetables and less sugar. It was difficult at first because I missed my favorite snacks. However, I stayed motivated by tracking my progress. After six months, I lost ten kilograms. I felt much more energetic and confident. Achieving this goal taught me discipline and perseverance. It was not easy, but the result was worth the effort.",
        "word_count": 98,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'health', 'change', 'gym', 'working out', 'diet', 'missed', 'motivated', 'tracking', 'progress', 'energetic', 'confident', 'discipline', 'perseverance'. Band 6 level.",
             "grammar: 'health, so I decided', 'difficult... because I', 'Achieving this goal'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'motivated', 'tracking', 'energetic', 'confident', 'discipline', 'perseverance'. >Band 5: 'Gym', 'diet'. Not Band 7: 'Lose weight', 'vegetables' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'health, so I decided', 'Achieving this goal taught'. >Band 6: Causal clauses and gerund subjects used correctly. Not Band 8: Sentences are somewhat short.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a goal you achieved.\n\nTranscript: I set a goal to lose weight last year. I was not happy with my health, so I decided to make a change. I joined a gym and started working out three times a week. I also changed my diet, eating more vegetables and less sugar. It was difficult at first because I missed my favorite snacks. However, I stayed motivated by tracking my progress. After six months, I lost ten kilograms. I felt much more energetic and confident. Achieving this goal taught me discipline and perseverance. It was not easy, but the result was worth the effort.\n\nWord Count: 98 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'motivated', 'tracking', 'energetic', 'confident', 'discipline', 'perseverance'. \n\n>Band 5: 'Gym', 'diet'.\n\nNot Band 7: 'Lose weight', 'vegetables' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'health, so I decided', 'Achieving this goal taught'. \n\n>Band 6: Causal clauses and gerund subjects used correctly.\n\nNot Band 8: Sentences are somewhat short.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_380",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a problem you solved.",
        "transcript_cleaned": "I had a problem with my car recently. It broke down in the middle of the road. I was very worried because I was late for a meeting. I did not know much about cars, so I called a mechanic. While waiting, I checked the engine and realized the battery was loose. I tightened the connection myself. To my surprise, the car started. I felt very proud that I could fix it without help. It saved me money and time. This experience taught me to be more self-reliant and calm in stressful situations.",
        "word_count": 96,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'broke down', 'worried', 'mechanic', 'engine', 'loose', 'tightened', 'connection', 'proud', 'self-reliant', 'stressful'. Band 6 level.",
             "grammar: 'worried because I was', 'While waiting, I', 'proud that I could'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'broke down', 'mechanic', 'tightened', 'connection', 'self-reliant', 'stressful'. >Band 5: 'Engine', 'proud'. Not Band 7: 'Late for a meeting' is common.",
        "grammar_reason": "[GRA7] Various complex structures: 'While waiting, I checked', 'proud that I could'. >Band 6: Participle phrases and noun clauses used correctly. Not Band 8: Sentence flow is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a problem you solved.\n\nTranscript: I had a problem with my car recently. It broke down in the middle of the road. I was very worried because I was late for a meeting. I did not know much about cars, so I called a mechanic. While waiting, I checked the engine and realized the battery was loose. I tightened the connection myself. To my surprise, the car started. I felt very proud that I could fix it without help. It saved me money and time. This experience taught me to be more self-reliant and calm in stressful situations.\n\nWord Count: 96 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'broke down', 'mechanic', 'tightened', 'connection', 'self-reliant', 'stressful'. \n\n>Band 5: 'Engine', 'proud'.\n\nNot Band 7: 'Late for a meeting' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'While waiting, I checked', 'proud that I could'. \n\n>Band 6: Participle phrases and noun clauses used correctly.\n\nNot Band 8: Sentence flow is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_381",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a park you like to visit.",
        "transcript_cleaned": "I like going to Hyde Park when I visit London. It is a huge park in the center of the city. There is a lake called the Serpentine where you can swim or boat. I enjoy walking through the rose gardens, which are beautiful in summer. There are also many squirrels that are very friendly. People go there to have picnics, cycle, or play sports. It is a great place to relax and forget about the busy city life. I always feel refreshed after spending time there. It is one of my favorite places because of its lively atmosphere and scenic views.",
        "word_count": 103,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'huge', 'center', 'swim', 'boat', 'rose gardens', 'squirrels', 'picnics', 'cycle', 'relax', 'refreshed', 'atmosphere', 'scenic views'. Band 6 level.",
             "grammar: 'lake called... where you', 'gardens, which are', 'squirrels that are'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'refreshed', 'atmosphere', 'scenic views'. >Band 5: 'Relax', 'beautiful'. Not Band 7: 'Huge park', 'play sports' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'lake called... where you', 'gardens, which are'. >Band 6: Relative clauses used correctly. Not Band 8: Sentence structure is repetitive.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a park you like to visit.\n\nTranscript: I like going to Hyde Park when I visit London. It is a huge park in the center of the city. There is a lake called the Serpentine where you can swim or boat. I enjoy walking through the rose gardens, which are beautiful in summer. There are also many squirrels that are very friendly. People go there to have picnics, cycle, or play sports. It is a great place to relax and forget about the busy city life. I always feel refreshed after spending time there. It is one of my favorite places because of its lively atmosphere and scenic views.\n\nWord Count: 103 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'refreshed', 'atmosphere', 'scenic views'. \n\n>Band 5: 'Relax', 'beautiful'.\n\nNot Band 7: 'Huge park', 'play sports' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'lake called... where you', 'gardens, which are'. \n\n>Band 6: Relative clauses used correctly.\n\nNot Band 8: Sentence structure is repetitive.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_382",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you received.",
        "transcript_cleaned": "My sister bought me a leather wallet for Christmas. It was unexpected but very useful. My old wallet was falling apart, so I really needed a new one. The new wallet is brown and has many compartments for cards and cash. It smells like real leather. I like it because it is stylish and durable. It fits perfectly in my pocket. Every time I use it, I think of my sister's generosity. It was a thoughtful gift that I use every day. I hope to keep it for a long time as it is very good quality.",
        "word_count": 98,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'leather', 'unexpected', 'useful', 'falling apart', 'compartments', 'stylish', 'durable', 'generosity', 'thoughtful', 'quality'. Band 6 level.",
             "grammar: 'unexpected but very', 'falling apart, so I', 'think of my sister's'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'unexpected', 'compartments', 'stylish', 'durable', 'generosity', 'thoughtful'. >Band 5: 'Leather', 'useful'. Not Band 7: 'New wallet', 'good quality' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'falling apart, so I', 'because it is stylish'. >Band 6: Causal and coordinating conjunctions used correctly. Not Band 8: Simple sentences are frequent.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a gift you received.\n\nTranscript: My sister bought me a leather wallet for Christmas. It was unexpected but very useful. My old wallet was falling apart, so I really needed a new one. The new wallet is brown and has many compartments for cards and cash. It smells like real leather. I like it because it is stylish and durable. It fits perfectly in my pocket. Every time I use it, I think of my sister's generosity. It was a thoughtful gift that I use every day. I hope to keep it for a long time as it is very good quality.\n\nWord Count: 98 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'unexpected', 'compartments', 'stylish', 'durable', 'generosity', 'thoughtful'. \n\n>Band 5: 'Leather', 'useful'.\n\nNot Band 7: 'New wallet', 'good quality' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'falling apart, so I', 'because it is stylish'. \n\n>Band 6: Causal and coordinating conjunctions used correctly.\n\nNot Band 8: Simple sentences are frequent.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_383",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a movie you watched recently.",
        "transcript_cleaned": "I saw a comedy movie called 'The Hangover'. It is about four friends who go to Las Vegas for a bachelor party. They get drunk and lose the groom. The rest of the movie is about them trying to find him. It was hilarious and full of crazy situations. I laughed so much that my stomach hurt. The actors were very funny and had great chemistry. Although the plot was a bit ridiculous, it was very entertaining. It was a great way to escape from reality for a few hours. I would recommend it if you want a good laugh.",
        "word_count": 102,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'comedy', 'bachelor party', 'drunk', 'groom', 'hilarious', 'crazy situations', 'chemistry', 'ridiculous', 'entertaining', 'escape', 'reality'. Band 6 level.",
             "grammar: 'friends who go', 'movie is about them', 'laughed so much that'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'bachelor party', 'hilarious', 'chemistry', 'ridiculous', 'entertaining', 'escape'. >Band 5: 'Funny', 'drunk'. Not Band 7: 'Great way', 'good laugh' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'friends who go', 'so much that', 'Although the plot'. >Band 6: Relative clauses and result clauses used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a movie you watched recently.\n\nTranscript: I saw a comedy movie called 'The Hangover'. It is about four friends who go to Las Vegas for a bachelor party. They get drunk and lose the groom. The rest of the movie is about them trying to find him. It was hilarious and full of crazy situations. I laughed so much that my stomach hurt. The actors were very funny and had great chemistry. Although the plot was a bit ridiculous, it was very entertaining. It was a great way to escape from reality for a few hours. I would recommend it if you want a good laugh.\n\nWord Count: 102 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'bachelor party', 'hilarious', 'chemistry', 'ridiculous', 'entertaining', 'escape'. \n\n>Band 5: 'Funny', 'drunk'.\n\nNot Band 7: 'Great way', 'good laugh' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'friends who go', 'so much that', 'Although the plot'. \n\n>Band 6: Relative clauses and result clauses used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_384",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a teacher who helped you.",
        "transcript_cleaned": "My science teacher, Mr. Brown, was very inspiring. He made complex topics easy to understand. He used experiments to demonstrate scientific principles. I remember making a volcano in his class. It was fun and educational. He encouraged us to ask questions and be curious. He helped me prepare for my exams by giving me extra practice papers. Thanks to him, I got an A in science. He was strict but fair. He taught me the importance of hard work and dedication. I will always remember him as a great mentor.",
        "word_count": 91,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'inspiring', 'complex topics', 'demonstrate', 'principles', 'educational', 'encouraged', 'curious', 'dedication', 'mentor'. Band 6 level.",
             "grammar: 'experiments to demonstrate', 'helped me prepare', 'Thanks to him'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'inspiring', 'demonstrate', 'principles', 'encouraged', 'dedication', 'mentor'. >Band 5: 'Complex', 'curious'. Not Band 7: 'Fun', 'hard work' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'experiments to demonstrate', 'helped me prepare', 'Thanks to him'. >Band 6: Infinitives and thanks structures used correctly. Not Band 8: Sentences are somewhat short.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a teacher who helped you.\n\nTranscript: My science teacher, Mr. Brown, was very inspiring. He made complex topics easy to understand. He used experiments to demonstrate scientific principles. I remember making a volcano in his class. It was fun and educational. He encouraged us to ask questions and be curious. He helped me prepare for my exams by giving me extra practice papers. Thanks to him, I got an A in science. He was strict but fair. He taught me the importance of hard work and dedication. I will always remember him as a great mentor.\n\nWord Count: 91 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'inspiring', 'demonstrate', 'principles', 'encouraged', 'dedication', 'mentor'. \n\n>Band 5: 'Complex', 'curious'.\n\nNot Band 7: 'Fun', 'hard work' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'experiments to demonstrate', 'helped me prepare', 'Thanks to him'. \n\n>Band 6: Infinitives and thanks structures used correctly.\n\nNot Band 8: Sentences are somewhat short.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_385",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place you visited.",
        "transcript_cleaned": "I went to Stonehenge in England. It is a prehistoric monument made of massive stones. It is very mysterious because nobody knows exactly how it was built or why. I took an audio tour to learn more about it. The stones are arranged in a circle. It is believed to be an ancient burial ground or a calendar. I felt a sense of awe standing there. The landscape around it is green and open. It was crowded with tourists, but still very impressive. It is a UNESCO World Heritage site and a must-see if you are in the UK.",
        "word_count": 101,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'prehistoric monument', 'massive', 'mysterious', 'audio tour', 'arranged', 'burial ground', 'calendar', 'awe', 'landscape', 'impressive', 'heritage'. Band 6 level.",
             "grammar: 'monument made of', 'because nobody knows', 'believed to be'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'prehistoric', 'massive', 'mysterious', 'burial ground', 'landscape', 'impressive'. >Band 5: 'Stones', 'circle'. Not Band 7: 'Must-see', 'tourists' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'monument made of', 'how it was built', 'believed to be'. >Band 6: Passive voice and noun clauses used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical place you visited.\n\nTranscript: I went to Stonehenge in England. It is a prehistoric monument made of massive stones. It is very mysterious because nobody knows exactly how it was built or why. I took an audio tour to learn more about it. The stones are arranged in a circle. It is believed to be an ancient burial ground or a calendar. I felt a sense of awe standing there. The landscape around it is green and open. It was crowded with tourists, but still very impressive. It is a UNESCO World Heritage site and a must-see if you are in the UK.\n\nWord Count: 101 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'prehistoric', 'massive', 'mysterious', 'burial ground', 'landscape', 'impressive'. \n\n>Band 5: 'Stones', 'circle'.\n\nNot Band 7: 'Must-see', 'tourists' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'monument made of', 'how it was built', 'believed to be'. \n\n>Band 6: Passive voice and noun clauses used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_386",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book you enjoyed reading.",
        "transcript_cleaned": "I loved reading 'To Kill a Mockingbird'. It is a classic novel about racial injustice in the American South. The story is told from the perspective of a young girl named Scout. Her father, Atticus, is a lawyer who defends an innocent black man. I admired Atticus for his courage and moral compass. The book deals with serious themes but also has humorous moments. It made me think about prejudice and empathy. I read it for a school assignment but ended up loving it. It is a powerful story that teaches important life lessons. I think everyone should read it at least once.",
        "word_count": 104,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'classic novel', 'racial injustice', 'perspective', 'innocent', 'admired', 'courage', 'moral compass', 'themes', 'humorous', 'prejudice', 'empathy'. Band 6 level.",
             "grammar: 'story is told', 'lawyer who defends', 'made me think', 'ended up loving'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'injustice', 'perspective', 'courage', 'moral compass', 'prejudice', 'empathy'. >Band 5: 'Serious', 'loving'. Not Band 7: 'Classic novel', 'life lessons' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'lawyer who defends', 'made me think', 'ended up loving'. >Band 6: Relative clauses and gerunds used correctly. Not Band 8: Standard sentence forms.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book you enjoyed reading.\n\nTranscript: I loved reading 'To Kill a Mockingbird'. It is a classic novel about racial injustice in the American South. The story is told from the perspective of a young girl named Scout. Her father, Atticus, is a lawyer who defends an innocent black man. I admired Atticus for his courage and moral compass. The book deals with serious themes but also has humorous moments. It made me think about prejudice and empathy. I read it for a school assignment but ended up loving it. It is a powerful story that teaches important life lessons. I think everyone should read it at least once.\n\nWord Count: 104 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'injustice', 'perspective', 'courage', 'moral compass', 'prejudice', 'empathy'. \n\n>Band 5: 'Serious', 'loving'.\n\nNot Band 7: 'Classic novel', 'life lessons' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'lawyer who defends', 'made me think', 'ended up loving'. \n\n>Band 6: Relative clauses and gerunds used correctly.\n\nNot Band 8: Standard sentence forms.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_387",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a meal you had with friends.",
        "transcript_cleaned": "I had a potluck dinner with my friends last week. Everyone brought a different dish to share. There was a mix of cuisines, including Indian curry, Mexican tacos, and Chinese noodles. I made a chocolate cake for dessert. We ate in my living room and listened to music. It was fun trying different foods and guessing the ingredients. We played board games after eating. The atmosphere was very lively and cheerful. It was a cheap and enjoyable way to spend time together. I love potlucks because they are collaborative and less stressful than cooking a whole meal for everyone.",
        "word_count": 100,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'potluck', 'cuisines', 'curry', 'tacos', 'noodles', 'ingredients', 'board games', 'lively', 'cheerful', 'collaborative', 'stressful'. Band 6 level.",
             "grammar: 'brought a different dish', 'mix of... including', 'guessing the ingredients', 'less stressful than'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'potluck', 'cuisines', 'ingredients', 'lively', 'collaborative', 'stressful'. >Band 5: 'Mix', 'fun'. Not Band 7: 'Different dish', 'chocolate cake' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'mix of... including', 'guessing the ingredients', 'less stressful than'. >Band 6: Participles and comparisons used correctly. Not Band 8: Lacks idiomatic grammar.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a meal you had with friends.\n\nTranscript: I had a potluck dinner with my friends last week. Everyone brought a different dish to share. There was a mix of cuisines, including Indian curry, Mexican tacos, and Chinese noodles. I made a chocolate cake for dessert. We ate in my living room and listened to music. It was fun trying different foods and guessing the ingredients. We played board games after eating. The atmosphere was very lively and cheerful. It was a cheap and enjoyable way to spend time together. I love potlucks because they are collaborative and less stressful than cooking a whole meal for everyone.\n\nWord Count: 100 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'potluck', 'cuisines', 'ingredients', 'lively', 'collaborative', 'stressful'. \n\n>Band 5: 'Mix', 'fun'.\n\nNot Band 7: 'Different dish', 'chocolate cake' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'mix of... including', 'guessing the ingredients', 'less stressful than'. \n\n>Band 6: Participles and comparisons used correctly.\n\nNot Band 8: Lacks idiomatic grammar.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
