import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch05.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v6_g7_366",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a park you like to visit.",
        "transcript_cleaned": "I enjoy visiting Central Park in my hometown. It is a large recreational area with many trees and flowers. The park has a jogging track that I use frequently to stay fit. There is also a playground for children, which is always busy on weekends. I like to sit on the benches and watch people go by. It is a very peaceful place where I can escape the noise of the traffic. Sometimes, I bring a book and read under the shade of a big tree. The park is well-maintained and clean. It is a vital part of our community because it provides a safe space for relaxation and exercise.",
        "word_count": 113,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'recreational area', 'jogging track', 'frequently', 'stay fit', 'playground', 'peaceful', 'escape', 'shade', 'well-maintained', 'vital', 'community'. Band 6 level.",
             "grammar: 'track that I use', 'playground... which is', 'place where I can'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'recreational', 'frequently', 'well-maintained', 'vital', 'community'. >Band 5: 'Frequently', 'vital'. Not Band 7: 'Large area', 'stay fit' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'track that I use', 'playground... which is', 'place where I can'. >Band 6: Relative clauses used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a park you like to visit.\n\nTranscript: I enjoy visiting Central Park in my hometown. It is a large recreational area with many trees and flowers. The park has a jogging track that I use frequently to stay fit. There is also a playground for children, which is always busy on weekends. I like to sit on the benches and watch people go by. It is a very peaceful place where I can escape the noise of the traffic. Sometimes, I bring a book and read under the shade of a big tree. The park is well-maintained and clean. It is a vital part of our community because it provides a safe space for relaxation and exercise.\n\nWord Count: 113 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'recreational', 'frequently', 'well-maintained', 'vital', 'community'. \n\n>Band 5: 'Frequently', 'vital'.\n\nNot Band 7: 'Large area', 'stay fit' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'track that I use', 'playground... which is', 'place where I can'. \n\n>Band 6: Relative clauses used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_367",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you received.",
        "transcript_cleaned": "I received a bicycle for my birthday last year. It was a gift from my parents. I had been wanting a bike for a long time, so I was very happy. It is a mountain bike with many gears, which makes it easy to ride uphill. I use it to commute to school every day. It saves me money on bus fares and is good exercise. I also ride it on weekends to explore the countryside. The bike is very durable and reliable. I take good care of it by cleaning it regularly. It is the best present I have ever received because it gives me freedom and independence.",
        "word_count": 113,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'mountain bike', 'gears', 'commute', 'fares', 'explore', 'countryside', 'durable', 'reliable', 'independence'. Band 6 level.",
             "grammar: 'wanting... so I was', 'gears, which makes', 'because it gives me'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'commute', 'fares', 'explore', 'durable', 'reliable', 'independence'. >Band 5: 'Explore', 'reliable'. Not Band 7: 'Mountain bike', 'good exercise' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'wanting... so I was', 'gears, which makes', 'because it gives me'. >Band 6: Causal and relative clauses used correctly. Not Band 8: Lacks idiomatic grammar.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a gift you received.\n\nTranscript: I received a bicycle for my birthday last year. It was a gift from my parents. I had been wanting a bike for a long time, so I was very happy. It is a mountain bike with many gears, which makes it easy to ride uphill. I use it to commute to school every day. It saves me money on bus fares and is good exercise. I also ride it on weekends to explore the countryside. The bike is very durable and reliable. I take good care of it by cleaning it regularly. It is the best present I have ever received because it gives me freedom and independence.\n\nWord Count: 113 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'commute', 'fares', 'explore', 'durable', 'reliable', 'independence'. \n\n>Band 5: 'Explore', 'reliable'.\n\nNot Band 7: 'Mountain bike', 'good exercise' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'wanting... so I was', 'gears, which makes', 'because it gives me'. \n\n>Band 6: Causal and relative clauses used correctly.\n\nNot Band 8: Lacks idiomatic grammar.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_368",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a movie you watched recently.",
        "transcript_cleaned": "I watched an action movie called 'Fast and Furious'. It is about street racing and heists. The car chase scenes were very exciting and fast-paced. I was impressed by the stunts, which looked very dangerous. The plot was simple, but the action kept me entertained. I liked the camaraderie between the characters. They worked together as a team to solve problems. Although it is not a serious movie, it was a fun way to relax. The special effects were also top-notch. I would recommend it to people who like adrenaline and cars. It was an enjoyable experience overall.",
        "word_count": 103,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'street racing', 'heists', 'fast-paced', 'stunts', 'camaraderie', 'entertained', 'top-notch', 'adrenaline', 'enjoyable'. Band 6 level.",
             "grammar: 'stunts, which looked', 'simple, but the action', 'recommend it to people who'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'heists', 'fast-paced', 'camaraderie', 'top-notch', 'adrenaline'. >Band 5: 'Fast-paced', 'stunts'. Not Band 7: 'Car chase', 'simple plot' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'stunts, which looked', 'people who like'. >Band 6: Relative clauses used correctly. Not Band 8: Simple sentences are frequent.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a movie you watched recently.\n\nTranscript: I watched an action movie called 'Fast and Furious'. It is about street racing and heists. The car chase scenes were very exciting and fast-paced. I was impressed by the stunts, which looked very dangerous. The plot was simple, but the action kept me entertained. I liked the camaraderie between the characters. They worked together as a team to solve problems. Although it is not a serious movie, it was a fun way to relax. The special effects were also top-notch. I would recommend it to people who like adrenaline and cars. It was an enjoyable experience overall.\n\nWord Count: 103 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'heists', 'fast-paced', 'camaraderie', 'top-notch', 'adrenaline'. \n\n>Band 5: 'Fast-paced', 'stunts'.\n\nNot Band 7: 'Car chase', 'simple plot' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'stunts, which looked', 'people who like'. \n\n>Band 6: Relative clauses used correctly.\n\nNot Band 8: Simple sentences are frequent.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_369",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a teacher who helped you.",
        "transcript_cleaned": "I remember my English teacher, Mrs. Jones. She was very kind and patient with all her students. I used to struggle with grammar, which was frustrating for me. She noticed my difficulty and offered to give me extra lessons after school. She explained the rules clearly and gave me practice exercises. Her encouragement helped me improve my confidence. I started to enjoy learning English because of her. She also recommended some good books for me to read. I am very grateful for her help. She was a true mentor who cared about her students' success.",
        "word_count": 100,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'patient', 'struggle', 'frustrating', 'difficulty', 'encouragement', 'confidence', 'recommended', 'grateful', 'mentor'. Band 6 level.",
             "grammar: 'grammar, which was', 'offered to give', 'because of her', 'mentor who cared'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'struggle', 'frustrating', 'encouragement', 'grateful', 'mentor'. >Band 5: 'Patient', 'confidence'. Not Band 7: 'Extra lessons', 'good books' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'grammar, which was', 'mentor who cared'. >Band 6: Relative clauses used correctly. Not Band 8: Sentence flow is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a teacher who helped you.\n\nTranscript: I remember my English teacher, Mrs. Jones. She was very kind and patient with all her students. I used to struggle with grammar, which was frustrating for me. She noticed my difficulty and offered to give me extra lessons after school. She explained the rules clearly and gave me practice exercises. Her encouragement helped me improve my confidence. I started to enjoy learning English because of her. She also recommended some good books for me to read. I am very grateful for her help. She was a true mentor who cared about her students' success.\n\nWord Count: 100 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'struggle', 'frustrating', 'encouragement', 'grateful', 'mentor'. \n\n>Band 5: 'Patient', 'confidence'.\n\nNot Band 7: 'Extra lessons', 'good books' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'grammar, which was', 'mentor who cared'. \n\n>Band 6: Relative clauses used correctly.\n\nNot Band 8: Sentence flow is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_370",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place you visited.",
        "transcript_cleaned": "I visited the Tower of London when I was in England. It is a historic castle located in the center of London. It has a long and bloody history, which I found fascinating. I saw the Crown Jewels, which were very shiny and expensive. The guards, called Beefeaters, gave us a tour. They told us stories about the prisoners who were kept there. I walked along the old stone walls and looked at the river. It was a very educational visit. I learned a lot about the kings and queens of England. It is a place that brings history to life.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'historic castle', 'bloody history', 'fascinating', 'Crown Jewels', 'shiny', 'prisoners', 'educational', 'kings and queens'. Band 6 level.",
             "grammar: 'history, which I found', 'Jewels, which were', 'prisoners who were'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'historic', 'bloody', 'fascinating', 'educational'. >Band 5: 'Fascinating', 'educational'. Not Band 7: 'Shiny', 'old stone walls' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'history, which I found', 'prisoners who were'. >Band 6: Relative clauses used correctly. Not Band 8: Sentence structure is repetitive.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical place you visited.\n\nTranscript: I visited the Tower of London when I was in England. It is a historic castle located in the center of London. It has a long and bloody history, which I found fascinating. I saw the Crown Jewels, which were very shiny and expensive. The guards, called Beefeaters, gave us a tour. They told us stories about the prisoners who were kept there. I walked along the old stone walls and looked at the river. It was a very educational visit. I learned a lot about the kings and queens of England. It is a place that brings history to life.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'historic', 'bloody', 'fascinating', 'educational'. \n\n>Band 5: 'Fascinating', 'educational'.\n\nNot Band 7: 'Shiny', 'old stone walls' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'history, which I found', 'prisoners who were'. \n\n>Band 6: Relative clauses used correctly.\n\nNot Band 8: Sentence structure is repetitive.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_371",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book you enjoyed reading.",
        "transcript_cleaned": "I enjoyed reading 'Harry Potter and the Sorcerer's Stone'. It is a fantasy novel about a young wizard. The story is set in a magical school called Hogwarts. I liked the characters, especially Harry and his friends. They face many challenges and fight against evil. The plot is very exciting and full of surprises. I was captivated by the magical world the author created. It made me wish I could do magic too. I read the book in bed every night before sleeping. It is a book that appeals to both children and adults because of its universal themes of friendship and bravery.",
        "word_count": 107,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'fantasy novel', 'wizard', 'magical', 'challenges', 'evil', 'surprises', 'captivated', 'appeals', 'universal themes', 'bravery'. Band 6 level.",
             "grammar: 'world the author created', 'wish I could do', 'because of its universal'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'fantasy', 'captivated', 'appeals', 'universal themes', 'bravery'. >Band 5: 'Magical', 'evil'. Not Band 7: 'Young wizard', 'full of surprises' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'world the author created', 'wish I could do'. >Band 6: Relative clauses and wish structures used correctly. Not Band 8: Simple sentences are frequent.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book you enjoyed reading.\n\nTranscript: I enjoyed reading 'Harry Potter and the Sorcerer's Stone'. It is a fantasy novel about a young wizard. The story is set in a magical school called Hogwarts. I liked the characters, especially Harry and his friends. They face many challenges and fight against evil. The plot is very exciting and full of surprises. I was captivated by the magical world the author created. It made me wish I could do magic too. I read the book in bed every night before sleeping. It is a book that appeals to both children and adults because of its universal themes of friendship and bravery.\n\nWord Count: 107 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'fantasy', 'captivated', 'appeals', 'universal themes', 'bravery'. \n\n>Band 5: 'Magical', 'evil'.\n\nNot Band 7: 'Young wizard', 'full of surprises' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'world the author created', 'wish I could do'. \n\n>Band 6: Relative clauses and wish structures used correctly.\n\nNot Band 8: Simple sentences are frequent.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_372",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a meal you had with friends.",
        "transcript_cleaned": "I remember a barbecue party we had last summer. It was at my friend's house, which has a big garden. We grilled burgers, sausages, and vegetables. Everyone brought a side dish or a drink to share. The weather was perfect, sunny and warm. We sat on the grass and ate while listening to music. The food tasted amazing because it was cooked over charcoal. We talked about our plans for the future and told jokes. It was a very relaxed and informal gathering. I enjoyed it because it was a great way to bond with my friends and enjoy the outdoors.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'barbecue', 'grilled', 'sausages', 'side dish', 'charcoal', 'informal', 'gathering', 'bond', 'outdoors'. Band 6 level.",
             "grammar: 'house, which has', 'ate while listening', 'because it was cooked'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'grilled', 'charcoal', 'informal', 'gathering', 'bond'. >Band 5: 'Barbecue', 'sausages'. Not Band 7: 'Perfect weather', 'told jokes' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'house, which has', 'ate while listening'. >Band 6: Relative clauses and time clauses used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a meal you had with friends.\n\nTranscript: I remember a barbecue party we had last summer. It was at my friend's house, which has a big garden. We grilled burgers, sausages, and vegetables. Everyone brought a side dish or a drink to share. The weather was perfect, sunny and warm. We sat on the grass and ate while listening to music. The food tasted amazing because it was cooked over charcoal. We talked about our plans for the future and told jokes. It was a very relaxed and informal gathering. I enjoyed it because it was a great way to bond with my friends and enjoy the outdoors.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'grilled', 'charcoal', 'informal', 'gathering', 'bond'. \n\n>Band 5: 'Barbecue', 'sausages'.\n\nNot Band 7: 'Perfect weather', 'told jokes' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'house, which has', 'ate while listening'. \n\n>Band 6: Relative clauses and time clauses used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_373",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a journey you took.",
        "transcript_cleaned": "I took a train journey across Europe a few years ago. It was an amazing experience. I visited several countries, including France, Italy, and Switzerland. The scenery was breathtaking, especially the Alps. I liked watching the landscape change from the train window. The trains were very comfortable and fast. I met many interesting travelers from all over the world. We shared stories and tips about places to visit. One challenge was the language barrier in some places, but I managed to communicate. This journey broadened my horizons and made me appreciate different cultures. I would highly recommend traveling by train in Europe.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'scenery', 'breathtaking', 'landscape', 'comfortable', 'travelers', 'language barrier', 'communicate', 'broadened my horizons', 'appreciate', 'cultures'. Band 6 level.",
             "grammar: 'countries, including France', 'watching the landscape change', 'made me appreciate'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'scenery', 'breathtaking', 'language barrier', 'broadened my horizons', 'appreciate'. >Band 5: 'Comfortable', 'travelers'. Not Band 7: 'Train journey', 'interesting travelers' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'watching the landscape change', 'made me appreciate'. >Band 6: Gerunds and causative verbs used correctly. Not Band 8: Sentence flow is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a journey you took.\n\nTranscript: I took a train journey across Europe a few years ago. It was an amazing experience. I visited several countries, including France, Italy, and Switzerland. The scenery was breathtaking, especially the Alps. I liked watching the landscape change from the train window. The trains were very comfortable and fast. I met many interesting travelers from all over the world. We shared stories and tips about places to visit. One challenge was the language barrier in some places, but I managed to communicate. This journey broadened my horizons and made me appreciate different cultures. I would highly recommend traveling by train in Europe.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'scenery', 'breathtaking', 'language barrier', 'broadened my horizons', 'appreciate'. \n\n>Band 5: 'Comfortable', 'travelers'.\n\nNot Band 7: 'Train journey', 'interesting travelers' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'watching the landscape change', 'made me appreciate'. \n\n>Band 6: Gerunds and causative verbs used correctly.\n\nNot Band 8: Sentence flow is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_374",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a skill you want to learn.",
        "transcript_cleaned": "I would love to learn photography. I have always admired beautiful photos in magazines. I think it is a great way to capture memories. I want to learn how to use a professional camera and understand lighting and composition. Currently, I only use my smartphone, which is convenient but limited. I plan to take an online course or join a local photography club. I know it takes practice to take good shots. I want to travel and take pictures of landscapes and people. Photography allows you to see the world from a different perspective. It would be a very creative and rewarding hobby.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'photography', 'admired', 'capture memories', 'professional camera', 'lighting', 'composition', 'convenient', 'landscapes', 'perspective', 'creative', 'rewarding'. Band 6 level.",
             "grammar: 'way to capture', 'how to use', 'smartphone, which is', 'allows you to see'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'admired', 'capture', 'composition', 'perspective', 'rewarding'. >Band 5: 'Photography', 'creative'. Not Band 7: 'Beautiful photos', 'online course' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'how to use', 'smartphone, which is', 'allows you to see'. >Band 6: Relative clauses and infinitives used correctly. Not Band 8: Lacks idiomatic grammar.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a skill you want to learn.\n\nTranscript: I would love to learn photography. I have always admired beautiful photos in magazines. I think it is a great way to capture memories. I want to learn how to use a professional camera and understand lighting and composition. Currently, I only use my smartphone, which is convenient but limited. I plan to take an online course or join a local photography club. I know it takes practice to take good shots. I want to travel and take pictures of landscapes and people. Photography allows you to see the world from a different perspective. It would be a very creative and rewarding hobby.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'admired', 'capture', 'composition', 'perspective', 'rewarding'. \n\n>Band 5: 'Photography', 'creative'.\n\nNot Band 7: 'Beautiful photos', 'online course' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'how to use', 'smartphone, which is', 'allows you to see'. \n\n>Band 6: Relative clauses and infinitives used correctly.\n\nNot Band 8: Lacks idiomatic grammar.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_375",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a person you admire.",
        "transcript_cleaned": "I admire my mother very much. She is a nurse and works very hard. She is always caring and compassionate towards her patients. She balances her work and family life perfectly. Even when she is tired, she cooks dinner for us and helps me with my homework. She has taught me to be kind and responsible. I remember when I was sick, she stayed up all night to take care of me. Her strength and dedication inspire me every day. She is my role model, and I hope to be like her in the future.",
        "word_count": 98,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'admire', 'compassionate', 'patients', 'balances', 'responsible', 'strength', 'dedication', 'inspire', 'role model'. Band 6 level.",
             "grammar: 'Even when she is', 'taught me to be', 'remember when I was'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'compassionate', 'balances', 'dedication', 'inspire', 'role model'. >Band 5: 'Caring', 'responsible'. Not Band 7: 'Works very hard', 'cooks dinner' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'Even when she is', 'taught me to be'. >Band 6: Adverbial clauses and infinitives used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a person you admire.\n\nTranscript: I admire my mother very much. She is a nurse and works very hard. She is always caring and compassionate towards her patients. She balances her work and family life perfectly. Even when she is tired, she cooks dinner for us and helps me with my homework. She has taught me to be kind and responsible. I remember when I was sick, she stayed up all night to take care of me. Her strength and dedication inspire me every day. She is my role model, and I hope to be like her in the future.\n\nWord Count: 98 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'compassionate', 'balances', 'dedication', 'inspire', 'role model'. \n\n>Band 5: 'Caring', 'responsible'.\n\nNot Band 7: 'Works very hard', 'cooks dinner' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'Even when she is', 'taught me to be'. \n\n>Band 6: Adverbial clauses and infinitives used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
