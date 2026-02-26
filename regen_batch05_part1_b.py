import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch05.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v6_g7_356",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book you enjoyed reading.",
        "transcript_cleaned": "I want to talk about a book called 'The Alchemist' by Paulo Coelho. It is a very inspiring story about a young shepherd who travels to Egypt to find a treasure. Along the way, he meets different people who teach him about life. The book is written in a simple but profound style. I enjoyed it because it encourages readers to follow their dreams. There are many memorable quotes in the book that I really like. One of the main themes is that the universe will help you if you really want something. I read it in just two days because it was so engaging. It is a book that I would recommend to anyone who is looking for motivation.",
        "word_count": 126,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'inspiring', 'shepherd', 'treasure', 'profound', 'encourages', 'memorable quotes', 'themes', 'universe', 'engaging', 'motivation'. Band 6 level.",
             "grammar: 'shepherd who travels', 'meets different people who', 'because it encourages', 'if you really want'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'shepherd', 'profound', 'encourages', 'themes', 'engaging', 'motivation'. >Band 5: 'Profound', 'engaging'. Not Band 7: 'Inspiring story', 'memorable quotes' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'shepherd who travels', 'people who teach', 'because it encourages'. >Band 6: Frequent error-free sentences. Not Band 8: Sentence structure is relatively simple.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book you enjoyed reading.\n\nTranscript: I want to talk about a book called 'The Alchemist' by Paulo Coelho. It is a very inspiring story about a young shepherd who travels to Egypt to find a treasure. Along the way, he meets different people who teach him about life. The book is written in a simple but profound style. I enjoyed it because it encourages readers to follow their dreams. There are many memorable quotes in the book that I really like. One of the main themes is that the universe will help you if you really want something. I read it in just two days because it was so engaging. It is a book that I would recommend to anyone who is looking for motivation.\n\nWord Count: 126 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'shepherd', 'profound', 'encourages', 'themes', 'engaging', 'motivation'. \n\n>Band 5: 'Profound', 'engaging'.\n\nNot Band 7: 'Inspiring story', 'memorable quotes' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'shepherd who travels', 'people who teach', 'because it encourages'. \n\n>Band 6: Frequent error-free sentences.\n\nNot Band 8: Sentence structure is relatively simple.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_357",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a meal you had with friends.",
        "transcript_cleaned": "I would like to describe a dinner I had with my friends last month. We went to a new Italian restaurant that had just opened in the city center. The atmosphere was very cozy and welcoming. We ordered a variety of dishes, including pizza and pasta. The food was delicious, especially the dessert. We spent several hours talking and laughing. It was a great opportunity to catch up with everyone since we had not seen each other for a long time. The service was also excellent, which made the evening even better. I really enjoyed the meal because of the good company and the tasty food. It was a memorable evening that I will cherish.",
        "word_count": 120,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'city center', 'atmosphere', 'cozy', 'welcoming', 'variety', 'dessert', 'opportunity', 'catch up', 'service', 'cherish'. Band 6 level.",
             "grammar: 'restaurant that had just opened', 'including pizza and pasta', 'since we had not seen', 'which made the evening'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'atmosphere', 'cozy', 'variety', 'opportunity', 'catch up', 'cherish'. >Band 5: 'Cozy', 'cherish'. Not Band 7: 'Delicious food', 'good company' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'restaurant that had just', 'since we had not seen', 'which made the evening'. >Band 6: Good use of relative clauses and time phrases. Not Band 8: Lacks idiomatic grammar.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a meal you had with friends.\n\nTranscript: I would like to describe a dinner I had with my friends last month. We went to a new Italian restaurant that had just opened in the city center. The atmosphere was very cozy and welcoming. We ordered a variety of dishes, including pizza and pasta. The food was delicious, especially the dessert. We spent several hours talking and laughing. It was a great opportunity to catch up with everyone since we had not seen each other for a long time. The service was also excellent, which made the evening even better. I really enjoyed the meal because of the good company and the tasty food. It was a memorable evening that I will cherish.\n\nWord Count: 120 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'atmosphere', 'cozy', 'variety', 'opportunity', 'catch up', 'cherish'. \n\n>Band 5: 'Cozy', 'cherish'.\n\nNot Band 7: 'Delicious food', 'good company' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'restaurant that had just', 'since we had not seen', 'which made the evening'. \n\n>Band 6: Good use of relative clauses and time phrases.\n\nNot Band 8: Lacks idiomatic grammar.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_358",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a journey you took.",
        "transcript_cleaned": "I want to talk about a trip I took to Japan last year. It was a long flight, but I was very excited. I visited Tokyo and Kyoto. The culture there is very different from my country. I was amazed by the ancient temples and the modern skyscrapers. The public transport system was very efficient and punctual. I also tried many local foods, such as sushi and ramen. One of the highlights was seeing Mount Fuji. It was a breathtaking view. I traveled with my family, which made the experience even more special. I learned a lot about Japanese history and traditions. It was an unforgettable journey that I would love to repeat.",
        "word_count": 119,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'flight', 'ancient temples', 'skyscrapers', 'efficient', 'punctual', 'local foods', 'highlights', 'breathtaking', 'traditions', 'unforgettable'. Band 6 level.",
             "grammar: 'culture there is very', 'amazed by the', 'transport system was', 'One of the highlights was'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'ancient', 'efficient', 'punctual', 'highlights', 'breathtaking', 'unforgettable'. >Band 5: 'Efficient', 'punctual'. Not Band 7: 'Long flight', 'modern skyscrapers' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'amazed by the', 'which made the experience', 'journey that I would'. >Band 6: Frequent error-free sentences. Not Band 8: Sentence structure is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a journey you took.\n\nTranscript: I want to talk about a trip I took to Japan last year. It was a long flight, but I was very excited. I visited Tokyo and Kyoto. The culture there is very different from my country. I was amazed by the ancient temples and the modern skyscrapers. The public transport system was very efficient and punctual. I also tried many local foods, such as sushi and ramen. One of the highlights was seeing Mount Fuji. It was a breathtaking view. I traveled with my family, which made the experience even more special. I learned a lot about Japanese history and traditions. It was an unforgettable journey that I would love to repeat.\n\nWord Count: 119 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'ancient', 'efficient', 'punctual', 'highlights', 'breathtaking', 'unforgettable'. \n\n>Band 5: 'Efficient', 'punctual'.\n\nNot Band 7: 'Long flight', 'modern skyscrapers' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'amazed by the', 'which made the experience', 'journey that I would'. \n\n>Band 6: Frequent error-free sentences.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_359",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a skill you want to learn.",
        "transcript_cleaned": "I have always wanted to learn how to play the piano. I think it is a very elegant instrument. I love listening to classical music, especially pieces by Beethoven. Learning to read sheet music seems challenging, but I am willing to try. I believe that playing an instrument can help reduce stress and improve concentration. I plan to take lessons from a private tutor once I have enough free time. It requires a lot of practice and patience to become proficient. I imagine that being able to play my favorite songs would be very satisfying. It is a skill that I can enjoy for the rest of my life.",
        "word_count": 113,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'elegant', 'classical music', 'sheet music', 'challenging', 'reduce stress', 'concentration', 'private tutor', 'proficient', 'satisfying'. Band 6 level.",
             "grammar: 'wanted to learn how', 'Learning to read... seems', 'believe that playing', 'once I have enough'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'elegant', 'sheet music', 'concentration', 'tutor', 'proficient', 'satisfying'. >Band 5: 'Proficient', 'elegant'. Not Band 7: 'Reduce stress', 'free time' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'Learning to read... seems', 'believe that playing', 'once I have enough'. >Band 6: Gerunds and conditional clauses used correctly. Not Band 8: Lacks idiomatic grammar.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a skill you want to learn.\n\nTranscript: I have always wanted to learn how to play the piano. I think it is a very elegant instrument. I love listening to classical music, especially pieces by Beethoven. Learning to read sheet music seems challenging, but I am willing to try. I believe that playing an instrument can help reduce stress and improve concentration. I plan to take lessons from a private tutor once I have enough free time. It requires a lot of practice and patience to become proficient. I imagine that being able to play my favorite songs would be very satisfying. It is a skill that I can enjoy for the rest of my life.\n\nWord Count: 113 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'elegant', 'sheet music', 'concentration', 'tutor', 'proficient', 'satisfying'. \n\n>Band 5: 'Proficient', 'elegant'.\n\nNot Band 7: 'Reduce stress', 'free time' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'Learning to read... seems', 'believe that playing', 'once I have enough'. \n\n>Band 6: Gerunds and conditional clauses used correctly.\n\nNot Band 8: Lacks idiomatic grammar.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_360",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a person you admire.",
        "transcript_cleaned": "I would like to talk about my grandfather, who is someone I deeply admire. He is a very wise and kind man. He worked hard all his life to support his family. Even though he faced many difficulties, he never gave up. He taught me the value of honesty and integrity. We often spend time together gardening, which is his favorite hobby. He tells me stories about his youth, which are always fascinating. I admire his resilience and his positive outlook on life. He is always willing to help others in need. I hope to become as strong and generous as he is when I grow older.",
        "word_count": 113,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'deeply admire', 'wise', 'support', 'difficulties', 'gave up', 'integrity', 'gardening', 'hobby', 'fascinating', 'resilience', 'outlook', 'generous'. Band 6 level.",
             "grammar: 'grandfather, who is', 'Even though he faced', 'stories... which are', 'willing to help'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'wise', 'integrity', 'fascinating', 'resilience', 'outlook', 'generous'. >Band 5: 'Resilience', 'integrity'. Not Band 7: 'Worked hard', 'never gave up' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'grandfather, who is', 'Even though he faced', 'as strong... as he is'. >Band 6: Relative clauses and comparisons used correctly. Not Band 8: Sentence structure is repetitive.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a person you admire.\n\nTranscript: I would like to talk about my grandfather, who is someone I deeply admire. He is a very wise and kind man. He worked hard all his life to support his family. Even though he faced many difficulties, he never gave up. He taught me the value of honesty and integrity. We often spend time together gardening, which is his favorite hobby. He tells me stories about his youth, which are always fascinating. I admire his resilience and his positive outlook on life. He is always willing to help others in need. I hope to become as strong and generous as he is when I grow older.\n\nWord Count: 113 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'wise', 'integrity', 'fascinating', 'resilience', 'outlook', 'generous'. \n\n>Band 5: 'Resilience', 'integrity'.\n\nNot Band 7: 'Worked hard', 'never gave up' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'grandfather, who is', 'Even though he faced', 'as strong... as he is'. \n\n>Band 6: Relative clauses and comparisons used correctly.\n\nNot Band 8: Sentence structure is repetitive.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_361",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a festival in your country.",
        "transcript_cleaned": "I would like to describe the Lunar New Year, which is the most important festival in my country. It usually takes place in late January or early February. People clean their houses to sweep away bad luck and welcome good fortune. Families gather to have a reunion dinner on New Year's Eve. We eat traditional foods like sticky rice cakes, which symbolize prosperity. Children receive red envelopes with money from their elders. The streets are decorated with red lanterns and flowers. There are also dragon dances and fireworks displays. It is a time of joy and celebration. I love this festival because it brings the whole family together and strengthens our bonds.",
        "word_count": 115,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'takes place', 'sweep away', 'bad luck', 'fortune', 'reunion dinner', 'traditional foods', 'symbolize', 'prosperity', 'elders', 'decorated', 'lanterns', 'celebration', 'strengthens'. Band 6 level.",
             "grammar: 'Year, which is', 'clean their houses to', 'foods like... which symbolize'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'fortune', 'reunion', 'symbolize', 'prosperity', 'decorated', 'strengthens'. >Band 5: 'Prosperity', 'symbolize'. Not Band 7: 'Bad luck', 'traditional foods' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'Year, which is', 'to sweep away', 'foods... which symbolize'. >Band 6: Relative clauses and infinitives of purpose used correctly. Not Band 8: Standard sentence forms.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a festival in your country.\n\nTranscript: I would like to describe the Lunar New Year, which is the most important festival in my country. It usually takes place in late January or early February. People clean their houses to sweep away bad luck and welcome good fortune. Families gather to have a reunion dinner on New Year's Eve. We eat traditional foods like sticky rice cakes, which symbolize prosperity. Children receive red envelopes with money from their elders. The streets are decorated with red lanterns and flowers. There are also dragon dances and fireworks displays. It is a time of joy and celebration. I love this festival because it brings the whole family together and strengthens our bonds.\n\nWord Count: 115 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'fortune', 'reunion', 'symbolize', 'prosperity', 'decorated', 'strengthens'. \n\n>Band 5: 'Prosperity', 'symbolize'.\n\nNot Band 7: 'Bad luck', 'traditional foods' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'Year, which is', 'to sweep away', 'foods... which symbolize'. \n\n>Band 6: Relative clauses and infinitives of purpose used correctly.\n\nNot Band 8: Standard sentence forms.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_362",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of technology you use.",
        "transcript_cleaned": "I want to talk about my laptop, which is an essential device for my studies. I bought it two years ago, and it is still working perfectly. I use it every day to write assignments, research information, and watch movies. It is very lightweight, so I can carry it to the library easily. The battery life is also impressive, lasting for about ten hours. It has a high-resolution screen that makes reading text very clear. I also use it to communicate with my friends via video calls. I cannot imagine my life without it because it helps me organize my work and stay connected with the world. It is definitely a worthwhile investment.",
        "word_count": 118,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'essential', 'device', 'assignments', 'research', 'lightweight', 'battery life', 'impressive', 'high-resolution', 'communicate', 'video calls', 'organize', 'connected', 'worthwhile investment'. Band 6 level.",
             "grammar: 'laptop, which is', 'so I can carry', 'screen that makes', 'cannot imagine... because'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'essential', 'device', 'assignments', 'impressive', 'high-resolution', 'worthwhile investment'. >Band 5: 'Assignments', 'impressive'. Not Band 7: 'Watch movies', 'video calls' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'laptop, which is', 'so I can carry', 'screen that makes'. >Band 6: Relative clauses and causal structures used correctly. Not Band 8: Lacks idiomatic grammar.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a piece of technology you use.\n\nTranscript: I want to talk about my laptop, which is an essential device for my studies. I bought it two years ago, and it is still working perfectly. I use it every day to write assignments, research information, and watch movies. It is very lightweight, so I can carry it to the library easily. The battery life is also impressive, lasting for about ten hours. It has a high-resolution screen that makes reading text very clear. I also use it to communicate with my friends via video calls. I cannot imagine my life without it because it helps me organize my work and stay connected with the world. It is definitely a worthwhile investment.\n\nWord Count: 118 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'essential', 'device', 'assignments', 'impressive', 'high-resolution', 'worthwhile investment'. \n\n>Band 5: 'Assignments', 'impressive'.\n\nNot Band 7: 'Watch movies', 'video calls' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'laptop, which is', 'so I can carry', 'screen that makes'. \n\n>Band 6: Relative clauses and causal structures used correctly.\n\nNot Band 8: Lacks idiomatic grammar.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_363",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a childhood memory.",
        "transcript_cleaned": "I vividly remember a family trip to the beach when I was about six years old. It was the first time I had ever seen the ocean. I was amazed by the vastness of the water and the sound of the waves crashing on the shore. I spent the whole day building sandcastles with my brother and collecting seashells. My father taught me how to swim, which was a bit scary at first but very exciting. We also had a picnic on the sand with delicious sandwiches. I felt so happy and carefree. That day remains etched in my memory because it was filled with laughter and joy. It is a precious memory of my childhood.",
        "word_count": 121,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'vividly', 'vastness', 'crashing', 'shore', 'sandcastles', 'collecting seashells', 'picnic', 'carefree', 'etched', 'precious'. Band 6 level.",
             "grammar: 'time I had ever seen', 'amazed by the', 'taught me how to', 'which was a bit'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'vividly', 'vastness', 'carefree', 'etched', 'precious'. >Band 5: 'Vividly', 'vastness'. Not Band 7: 'Sandcastles', 'waves' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'time I had ever seen', 'taught me how to', 'which was a bit'. >Band 6: Perfect tense and relative clauses used correctly. Not Band 8: Sentence flow is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a childhood memory.\n\nTranscript: I vividly remember a family trip to the beach when I was about six years old. It was the first time I had ever seen the ocean. I was amazed by the vastness of the water and the sound of the waves crashing on the shore. I spent the whole day building sandcastles with my brother and collecting seashells. My father taught me how to swim, which was a bit scary at first but very exciting. We also had a picnic on the sand with delicious sandwiches. I felt so happy and carefree. That day remains etched in my memory because it was filled with laughter and joy. It is a precious memory of my childhood.\n\nWord Count: 121 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'vividly', 'vastness', 'carefree', 'etched', 'precious'. \n\n>Band 5: 'Vividly', 'vastness'.\n\nNot Band 7: 'Sandcastles', 'waves' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'time I had ever seen', 'taught me how to', 'which was a bit'. \n\n>Band 6: Perfect tense and relative clauses used correctly.\n\nNot Band 8: Sentence flow is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_364",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a goal you achieved.",
        "transcript_cleaned": "I would like to talk about passing my driving test, which was a significant goal for me. I had always been nervous about driving, so I procrastinated for a long time. Finally, I decided to enroll in a driving school. The lessons were challenging, especially parking and navigating busy roundabouts. I failed my first attempt, which was very discouraging. However, I did not give up. I practiced more with my instructor and focused on my weak points. On my second attempt, I passed with flying colors. I felt a huge sense of relief and accomplishment. Getting my license gave me a sense of independence. It proved to me that perseverance pays off in the end.",
        "word_count": 118,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'significant goal', 'nervous', 'procrastinated', 'enroll', 'challenging', 'navigating', 'roundabouts', 'discouraging', 'give up', 'instructor', 'relief', 'accomplishment', 'independence', 'perseverance'. Band 6 level.",
             "grammar: 'test, which was', 'nervous... so I', 'failed... which was', 'proved to me that'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'procrastinated', 'navigating', 'discouraging', 'accomplishment', 'independence', 'perseverance'. >Band 5: 'Procrastinated', 'navigating'. Not Band 7: 'Driving school', 'give up' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'test, which was', 'nervous... so I', 'proved to me that'. >Band 6: Relative clauses and noun clauses used correctly. Not Band 8: Lacks full flexibility.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a goal you achieved.\n\nTranscript: I would like to talk about passing my driving test, which was a significant goal for me. I had always been nervous about driving, so I procrastinated for a long time. Finally, I decided to enroll in a driving school. The lessons were challenging, especially parking and navigating busy roundabouts. I failed my first attempt, which was very discouraging. However, I did not give up. I practiced more with my instructor and focused on my weak points. On my second attempt, I passed with flying colors. I felt a huge sense of relief and accomplishment. Getting my license gave me a sense of independence. It proved to me that perseverance pays off in the end.\n\nWord Count: 118 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'procrastinated', 'navigating', 'discouraging', 'accomplishment', 'independence', 'perseverance'. \n\n>Band 5: 'Procrastinated', 'navigating'.\n\nNot Band 7: 'Driving school', 'give up' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'test, which was', 'nervous... so I', 'proved to me that'. \n\n>Band 6: Relative clauses and noun clauses used correctly.\n\nNot Band 8: Lacks full flexibility.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_365",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a problem you solved.",
        "transcript_cleaned": "I faced a problem with my laptop right before a major deadline. The screen suddenly went black, and I could not turn it on. I was panicked because I had not saved my final essay. I tried to restart it multiple times, but nothing worked. Instead of giving up, I looked for solutions online using my phone. I found a forum where people had similar issues. I followed a troubleshooting guide which suggested removing the battery and holding the power button. To my relief, it worked, and the laptop restarted. I immediately backed up my files. This experience taught me the importance of backing up data regularly. It was a stressful situation, but I managed to solve it calmly.",
        "word_count": 126,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'major deadline', 'panicked', 'solutions', 'forum', 'similar issues', 'troubleshooting guide', 'backed up', 'data', 'regularly', 'stressful', 'calmly'. Band 6 level.",
             "grammar: 'panicked because I had not', 'Instead of giving up', 'guide which suggested'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'panicked', 'troubleshooting', 'backed up', 'regularly', 'calmly'. >Band 5: 'Panicked', 'solutions'. Not Band 7: 'Major deadline', 'screen went black' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'panicked because I had not', 'Instead of giving up', 'guide which suggested'. >Band 6: Past perfect and relative clauses used correctly. Not Band 8: Sentence flow is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a problem you solved.\n\nTranscript: I faced a problem with my laptop right before a major deadline. The screen suddenly went black, and I could not turn it on. I was panicked because I had not saved my final essay. I tried to restart it multiple times, but nothing worked. Instead of giving up, I looked for solutions online using my phone. I found a forum where people had similar issues. I followed a troubleshooting guide which suggested removing the battery and holding the power button. To my relief, it worked, and the laptop restarted. I immediately backed up my files. This experience taught me the importance of backing up data regularly. It was a stressful situation, but I managed to solve it calmly.\n\nWord Count: 126 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'panicked', 'troubleshooting', 'backed up', 'regularly', 'calmly'. \n\n>Band 5: 'Panicked', 'solutions'.\n\nNot Band 7: 'Major deadline', 'screen went black' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'panicked because I had not', 'Instead of giving up', 'guide which suggested'. \n\n>Band 6: Past perfect and relative clauses used correctly.\n\nNot Band 8: Sentence flow is standard.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
