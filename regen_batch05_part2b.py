import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch05.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v6_g7_388",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a journey you took.",
        "transcript_cleaned": "I took a road trip along the coast of California. I rented a convertible car and drove on Highway 1. The scenery was breathtaking, with the ocean on one side and mountains on the other. I stopped at several small towns to explore. I visited a lighthouse and saw some seals on the beach. Driving with the top down was very liberating. I listened to my favorite music and sang along. The sunset over the Pacific Ocean was spectacular. I felt a sense of freedom that I rarely experience. It was the best vacation I have ever had because it was so spontaneous and relaxing.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'road trip', 'convertible', 'scenery', 'breathtaking', 'lighthouse', 'seals', 'liberating', 'spectacular', 'freedom', 'spontaneous'. Band 6 level.",
             "grammar: 'scenery was breathtaking', 'Driving... was', 'vacation I have ever had'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'convertible', 'breathtaking', 'liberating', 'spectacular', 'spontaneous'. >Band 5: 'Scenery', 'freedom'. Not Band 7: 'Road trip', 'small towns' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'Driving with the top down', 'vacation I have ever had'. >Band 6: Gerund subjects and superlatives used correctly. Not Band 8: Sentence flow is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a journey you took.\n\nTranscript: I took a road trip along the coast of California. I rented a convertible car and drove on Highway 1. The scenery was breathtaking, with the ocean on one side and mountains on the other. I stopped at several small towns to explore. I visited a lighthouse and saw some seals on the beach. Driving with the top down was very liberating. I listened to my favorite music and sang along. The sunset over the Pacific Ocean was spectacular. I felt a sense of freedom that I rarely experience. It was the best vacation I have ever had because it was so spontaneous and relaxing.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'convertible', 'breathtaking', 'liberating', 'spectacular', 'spontaneous'. \n\n>Band 5: 'Scenery', 'freedom'.\n\nNot Band 7: 'Road trip', 'small towns' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'Driving with the top down', 'vacation I have ever had'. \n\n>Band 6: Gerund subjects and superlatives used correctly.\n\nNot Band 8: Sentence flow is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_389",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a skill you want to learn.",
        "transcript_cleaned": "I am interested in learning how to code. I think it is a very valuable skill in the digital age. I want to be able to create my own websites and apps. It seems complicated, but I like solving problems. I have watched some tutorials online, but I need a structured course. I plan to enroll in a coding bootcamp next summer. Learning a programming language is like learning a foreign language. It requires logic and precision. I believe that coding will open up many career opportunities for me. It would be amazing to build something from scratch using code.",
        "word_count": 101,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'valuable skill', 'digital age', 'apps', 'complicated', 'tutorials', 'structured', 'bootcamp', 'programming language', 'logic', 'precision', 'opportunities', 'from scratch'. Band 6 level.",
             "grammar: 'learning how to code', 'plan to enroll', 'believe that coding'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'digital age', 'complicated', 'structured', 'bootcamp', 'precision', 'opportunities', 'from scratch'. >Band 5: 'Skill', 'logic'. Not Band 7: 'Create websites', 'online' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'learning how to code', 'believe that coding will'. >Band 6: Noun clauses and infinitives used correctly. Not Band 8: Lacks idiomatic grammar.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a skill you want to learn.\n\nTranscript: I am interested in learning how to code. I think it is a very valuable skill in the digital age. I want to be able to create my own websites and apps. It seems complicated, but I like solving problems. I have watched some tutorials online, but I need a structured course. I plan to enroll in a coding bootcamp next summer. Learning a programming language is like learning a foreign language. It requires logic and precision. I believe that coding will open up many career opportunities for me. It would be amazing to build something from scratch using code.\n\nWord Count: 101 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'digital age', 'complicated', 'structured', 'bootcamp', 'precision', 'opportunities', 'from scratch'. \n\n>Band 5: 'Skill', 'logic'.\n\nNot Band 7: 'Create websites', 'online' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'learning how to code', 'believe that coding will'. \n\n>Band 6: Noun clauses and infinitives used correctly.\n\nNot Band 8: Lacks idiomatic grammar.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_390",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a person you admire.",
        "transcript_cleaned": "I admire Elon Musk for his innovation and ambition. He is the founder of several successful companies like Tesla and SpaceX. I am impressed by his vision to colonize Mars. He is not afraid to take risks and challenge the status quo. I think he is a genius, although some people find him controversial. He works extremely hard to achieve his goals. I like his electric cars because they are good for the environment. His determination to change the world is inspiring. He proves that anything is possible if you work hard enough. He is a true visionary of our time.",
        "word_count": 101,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'innovation', 'ambition', 'founder', 'colonize', 'risks', 'status quo', 'genius', 'controversial', 'environment', 'determination', 'visionary'. Band 6 level.",
             "grammar: 'impressed by his vision', 'afraid to take', 'proves that anything'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'innovation', 'colonize', 'status quo', 'controversial', 'determination', 'visionary'. >Band 5: 'Ambition', 'risks'. Not Band 7: 'Successful companies', 'electric cars' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'impressed by his vision', 'proves that anything is'. >Band 6: Passive voice and noun clauses used correctly. Not Band 8: Sentences are somewhat repetitive.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a person you admire.\n\nTranscript: I admire Elon Musk for his innovation and ambition. He is the founder of several successful companies like Tesla and SpaceX. I am impressed by his vision to colonize Mars. He is not afraid to take risks and challenge the status quo. I think he is a genius, although some people find him controversial. He works extremely hard to achieve his goals. I like his electric cars because they are good for the environment. His determination to change the world is inspiring. He proves that anything is possible if you work hard enough. He is a true visionary of our time.\n\nWord Count: 101 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'innovation', 'colonize', 'status quo', 'controversial', 'determination', 'visionary'. \n\n>Band 5: 'Ambition', 'risks'.\n\nNot Band 7: 'Successful companies', 'electric cars' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'impressed by his vision', 'proves that anything is'. \n\n>Band 6: Passive voice and noun clauses used correctly.\n\nNot Band 8: Sentences are somewhat repetitive.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_391",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a festival in your country.",
        "transcript_cleaned": "I want to talk about the Songkran festival in Thailand. It is the Thai New Year celebration held in April. It is famous for the water fights that happen in the streets. People splash water on each other to wash away bad luck. It is a very fun and chaotic festival. Everyone gets wet, but nobody gets angry. It is also a time to visit temples and pay respect to elders. I love the energy and happiness during this time. It is a unique cultural experience that attracts tourists from all over the world. It is the hottest time of the year, so the water is refreshing.",
        "word_count": 107,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'celebration', 'splash', 'wash away', 'bad luck', 'chaotic', 'temples', 'respect', 'elders', 'energy', 'cultural experience', 'refreshing'. Band 6 level.",
             "grammar: 'held in April', 'splash water... to wash', 'time to visit'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'splash', 'chaotic', 'respect', 'cultural experience', 'refreshing'. >Band 5: 'Celebration', 'energy'. Not Band 7: 'Water fights', 'hottest time' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'held in April', 'so the water is'. >Band 6: Participles and result clauses used correctly. Not Band 8: Simple sentence structure.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a festival in your country.\n\nTranscript: I want to talk about the Songkran festival in Thailand. It is the Thai New Year celebration held in April. It is famous for the water fights that happen in the streets. People splash water on each other to wash away bad luck. It is a very fun and chaotic festival. Everyone gets wet, but nobody gets angry. It is also a time to visit temples and pay respect to elders. I love the energy and happiness during this time. It is a unique cultural experience that attracts tourists from all over the world. It is the hottest time of the year, so the water is refreshing.\n\nWord Count: 107 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'splash', 'chaotic', 'respect', 'cultural experience', 'refreshing'. \n\n>Band 5: 'Celebration', 'energy'.\n\nNot Band 7: 'Water fights', 'hottest time' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'held in April', 'so the water is'. \n\n>Band 6: Participles and result clauses used correctly.\n\nNot Band 8: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_392",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of technology you use.",
        "transcript_cleaned": "I use wireless earbuds every day. They are very small and convenient. I connect them to my phone via Bluetooth. I use them to listen to music and podcasts while I commute. The sound quality is surprisingly good for such a small device. They also have a microphone, so I can take calls hands-free. The charging case is compact and easy to carry. I like that there are no wires to get tangled. They are a bit expensive, but I think they are worth it. They have made listening to audio much more enjoyable for me.",
        "word_count": 98,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'wireless earbuds', 'convenient', 'connect', 'via', 'podcasts', 'commute', 'sound quality', 'device', 'microphone', 'hands-free', 'compact', 'tangled', 'audio'. Band 6 level.",
             "grammar: 'while I commute', 'so I can take', 'like that there are'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'wireless', 'podcasts', 'commute', 'hands-free', 'tangled', 'audio'. >Band 5: 'Convenient', 'quality'. Not Band 7: 'Small device', 'expensive' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'while I commute', 'so I can take'. >Band 6: Time and result clauses used correctly. Not Band 8: Lacks full flexibility.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a piece of technology you use.\n\nTranscript: I use wireless earbuds every day. They are very small and convenient. I connect them to my phone via Bluetooth. I use them to listen to music and podcasts while I commute. The sound quality is surprisingly good for such a small device. They also have a microphone, so I can take calls hands-free. The charging case is compact and easy to carry. I like that there are no wires to get tangled. They are a bit expensive, but I think they are worth it. They have made listening to audio much more enjoyable for me.\n\nWord Count: 98 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'wireless', 'podcasts', 'commute', 'hands-free', 'tangled', 'audio'. \n\n>Band 5: 'Convenient', 'quality'.\n\nNot Band 7: 'Small device', 'expensive' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'while I commute', 'so I can take'. \n\n>Band 6: Time and result clauses used correctly.\n\nNot Band 8: Lacks full flexibility.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_393",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a childhood memory.",
        "transcript_cleaned": "I remember going camping with my father when I was eight. We went to a forest near a lake. We set up a tent together, which was fun but difficult. We made a campfire and roasted marshmallows. My father told me ghost stories that scared me a little. We slept in sleeping bags, and it was very cold at night. In the morning, we went fishing and caught a small fish. I felt very proud of myself. It was a simple trip, but it is a cherished memory. I learned to appreciate nature and enjoy simple things.",
        "word_count": 98,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'camping', 'forest', 'tent', 'campfire', 'roasted', 'marshmallows', 'ghost stories', 'sleeping bags', 'proud', 'cherished', 'appreciate', 'nature'. Band 6 level.",
             "grammar: 'tent... which was', 'scared me a little', 'learned to appreciate'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'roasted', 'marshmallows', 'cherished', 'appreciate', 'nature'. >Band 5: 'Camping', 'forest'. Not Band 7: 'Ghost stories', 'fishing' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'tent... which was', 'learned to appreciate'. >Band 6: Relative clauses and infinitives used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a childhood memory.\n\nTranscript: I remember going camping with my father when I was eight. We went to a forest near a lake. We set up a tent together, which was fun but difficult. We made a campfire and roasted marshmallows. My father told me ghost stories that scared me a little. We slept in sleeping bags, and it was very cold at night. In the morning, we went fishing and caught a small fish. I felt very proud of myself. It was a simple trip, but it is a cherished memory. I learned to appreciate nature and enjoy simple things.\n\nWord Count: 98 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'roasted', 'marshmallows', 'cherished', 'appreciate', 'nature'. \n\n>Band 5: 'Camping', 'forest'.\n\nNot Band 7: 'Ghost stories', 'fishing' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'tent... which was', 'learned to appreciate'. \n\n>Band 6: Relative clauses and infinitives used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_394",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a goal you achieved.",
        "transcript_cleaned": "I wanted to save money to buy a new guitar. It was expensive, so I had to be disciplined. I got a part-time job at a cafe. I worked on weekends and saved most of my earnings. I also cut down on spending money on clothes and snacks. It took me six months to reach my target. When I finally bought the guitar, I was ecstatic. I felt that my hard work had paid off. It taught me the value of money and patience. Now, I cherish the guitar even more because I earned it myself.",
        "word_count": 98,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'expensive', 'disciplined', 'earnings', 'cut down', 'target', 'ecstatic', 'paid off', 'patience', 'cherish', 'earned'. Band 6 level.",
             "grammar: 'expensive, so I had', 'When I finally bought', 'felt that my hard work'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'disciplined', 'earnings', 'cut down', 'target', 'ecstatic', 'cherish'. >Band 5: 'Expensive', 'money'. Not Band 7: 'Part-time job', 'hard work' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'expensive, so I had', 'felt that my hard work'. >Band 6: Causal and noun clauses used correctly. Not Band 8: Lacks idiomatic grammar.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a goal you achieved.\n\nTranscript: I wanted to save money to buy a new guitar. It was expensive, so I had to be disciplined. I got a part-time job at a cafe. I worked on weekends and saved most of my earnings. I also cut down on spending money on clothes and snacks. It took me six months to reach my target. When I finally bought the guitar, I was ecstatic. I felt that my hard work had paid off. It taught me the value of money and patience. Now, I cherish the guitar even more because I earned it myself.\n\nWord Count: 98 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'disciplined', 'earnings', 'cut down', 'target', 'ecstatic', 'cherish'. \n\n>Band 5: 'Expensive', 'money'.\n\nNot Band 7: 'Part-time job', 'hard work' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'expensive, so I had', 'felt that my hard work'. \n\n>Band 6: Causal and noun clauses used correctly.\n\nNot Band 8: Lacks idiomatic grammar.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_395",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a problem you solved.",
        "transcript_cleaned": "I once lost my passport while traveling in France. I was terrified because I had a flight the next day. I searched my hotel room, but it was gone. I went to the local police station to report it. The police officer was helpful but did not speak much English. I used a translation app on my phone to communicate. He told me to go to the embassy. I rushed to the embassy and explained my situation. They issued me an emergency travel document. I barely made my flight. It was a very stressful experience, but I learned to be more careful with my belongings.",
        "word_count": 107,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'terrified', 'report', 'officer', 'translation app', 'communicate', 'embassy', 'situation', 'issued', 'emergency', 'document', 'barely', 'stressful', 'belongings'. Band 6 level.",
             "grammar: 'terrified because I had', 'told me to go', 'learned to be more'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'terrified', 'translation', 'embassy', 'issued', 'emergency', 'barely', 'belongings'. >Band 5: 'Report', 'helpful'. Not Band 7: 'Police station', 'stressful' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'terrified because I had', 'told me to go'. >Band 6: Causal clauses and infinitives used correctly. Not Band 8: Sentence flow is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a problem you solved.\n\nTranscript: I once lost my passport while traveling in France. I was terrified because I had a flight the next day. I searched my hotel room, but it was gone. I went to the local police station to report it. The police officer was helpful but did not speak much English. I used a translation app on my phone to communicate. He told me to go to the embassy. I rushed to the embassy and explained my situation. They issued me an emergency travel document. I barely made my flight. It was a very stressful experience, but I learned to be more careful with my belongings.\n\nWord Count: 107 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'terrified', 'translation', 'embassy', 'issued', 'emergency', 'barely', 'belongings'. \n\n>Band 5: 'Report', 'helpful'.\n\nNot Band 7: 'Police station', 'stressful' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'terrified because I had', 'told me to go'. \n\n>Band 6: Causal clauses and infinitives used correctly.\n\nNot Band 8: Sentence flow is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_396",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a park you like to visit.",
        "transcript_cleaned": "There is a botanical garden in my city that I love. It has a huge variety of plants and flowers from all over the world. There is a greenhouse with tropical plants, which is very humid and green. I like the Japanese garden section the best. It has a small pond with koi fish and a wooden bridge. It is very serene and quiet. I often go there to read or meditate. The air is fresh and smells of flowers. It is a great place to escape the concrete jungle of the city. I feel very peaceful whenever I visit.",
        "word_count": 103,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'botanical garden', 'variety', 'greenhouse', 'tropical', 'humid', 'koi fish', 'wooden bridge', 'serene', 'meditate', 'concrete jungle', 'peaceful'. Band 6 level.",
             "grammar: 'plants, which is', 'go there to read', 'whenever I visit'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'botanical', 'tropical', 'humid', 'serene', 'meditate', 'concrete jungle'. >Band 5: 'Variety', 'fresh'. Not Band 7: 'Huge variety', 'small pond' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'plants, which is', 'whenever I visit'. >Band 6: Relative clauses and time clauses used correctly. Not Band 8: Sentence structure is repetitive.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a park you like to visit.\n\nTranscript: There is a botanical garden in my city that I love. It has a huge variety of plants and flowers from all over the world. There is a greenhouse with tropical plants, which is very humid and green. I like the Japanese garden section the best. It has a small pond with koi fish and a wooden bridge. It is very serene and quiet. I often go there to read or meditate. The air is fresh and smells of flowers. It is a great place to escape the concrete jungle of the city. I feel very peaceful whenever I visit.\n\nWord Count: 103 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'botanical', 'tropical', 'humid', 'serene', 'meditate', 'concrete jungle'. \n\n>Band 5: 'Variety', 'fresh'.\n\nNot Band 7: 'Huge variety', 'small pond' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'plants, which is', 'whenever I visit'. \n\n>Band 6: Relative clauses and time clauses used correctly.\n\nNot Band 8: Sentence structure is repetitive.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_397",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you received.",
        "transcript_cleaned": "My best friend gave me a sketchbook for my birthday. I love drawing, so it was a perfect gift. The cover is made of recycled paper, which I appreciate. The paper inside is thick and high quality. It came with a set of charcoal pencils. I use it to sketch portraits of my friends and family. It encourages me to practice my art every day. I take it with me everywhere I go. It is a place where I can express my creativity freely. I will always treasure it because it shows how well my friend knows me.",
        "word_count": 100,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'sketchbook', 'recycled', 'appreciate', 'charcoal pencils', 'sketch portraits', 'encourages', 'creativity', 'freely', 'treasure'. Band 6 level.",
             "grammar: 'drawing, so it was', 'paper, which I appreciate', 'because it shows'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'sketchbook', 'recycled', 'charcoal', 'portraits', 'encourages', 'creativity', 'treasure'. >Band 5: 'Drawing', 'perfect'. Not Band 7: 'High quality', 'every day' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'paper, which I appreciate', 'because it shows'. >Band 6: Relative clauses and causal structures used correctly. Not Band 8: Standard sentence forms.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a gift you received.\n\nTranscript: My best friend gave me a sketchbook for my birthday. I love drawing, so it was a perfect gift. The cover is made of recycled paper, which I appreciate. The paper inside is thick and high quality. It came with a set of charcoal pencils. I use it to sketch portraits of my friends and family. It encourages me to practice my art every day. I take it with me everywhere I go. It is a place where I can express my creativity freely. I will always treasure it because it shows how well my friend knows me.\n\nWord Count: 100 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'sketchbook', 'recycled', 'charcoal', 'portraits', 'encourages', 'creativity', 'treasure'. \n\n>Band 5: 'Drawing', 'perfect'.\n\nNot Band 7: 'High quality', 'every day' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'paper, which I appreciate', 'because it shows'. \n\n>Band 6: Relative clauses and causal structures used correctly.\n\nNot Band 8: Standard sentence forms.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_398",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a movie you watched recently.",
        "transcript_cleaned": "I watched an animated movie called 'Coco'. It is about a young boy who wants to be a musician. His family bans music, which is a big conflict. He travels to the Land of the Dead to find his ancestor. The animation is colorful and vibrant. The music is catchy and emotional. I cried at the end because it was so touching. It teaches the importance of family and remembering loved ones. Even though it is a cartoon, it deals with mature themes like death and memory. I think it is a masterpiece that everyone should watch.",
        "word_count": 99,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'animated', 'musician', 'bans', 'conflict', 'ancestor', 'vibrant', 'catchy', 'emotional', 'touching', 'mature themes', 'masterpiece'. Band 6 level.",
             "grammar: 'music, which is', 'travels... to find', 'Even though it is'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'ancestor', 'vibrant', 'catchy', 'emotional', 'touching', 'mature themes', 'masterpiece'. >Band 5: 'Musician', 'colorful'. Not Band 7: 'Young boy', 'family' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'music, which is', 'Even though it is'. >Band 6: Relative clauses and concession clauses used correctly. Not Band 8: Simple sentences are frequent.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a movie you watched recently.\n\nTranscript: I watched an animated movie called 'Coco'. It is about a young boy who wants to be a musician. His family bans music, which is a big conflict. He travels to the Land of the Dead to find his ancestor. The animation is colorful and vibrant. The music is catchy and emotional. I cried at the end because it was so touching. It teaches the importance of family and remembering loved ones. Even though it is a cartoon, it deals with mature themes like death and memory. I think it is a masterpiece that everyone should watch.\n\nWord Count: 99 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'ancestor', 'vibrant', 'catchy', 'emotional', 'touching', 'mature themes', 'masterpiece'. \n\n>Band 5: 'Musician', 'colorful'.\n\nNot Band 7: 'Young boy', 'family' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'music, which is', 'Even though it is'. \n\n>Band 6: Relative clauses and concession clauses used correctly.\n\nNot Band 8: Simple sentences are frequent.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_399",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a teacher who helped you.",
        "transcript_cleaned": "My art teacher, Ms. Lee, was amazing. She encouraged me to express myself through painting. She taught me different techniques, like watercolors and oil painting. She was very patient when I made mistakes. I used to be shy about showing my work, but she gave me confidence. She organized an art exhibition for our class. Seeing my painting on the wall was a proud moment. She believed in my talent when I doubted myself. Her passion for art was contagious. I still paint in my free time because of her influence. She was a wonderful role model.",
        "word_count": 100,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'encouraged', 'express myself', 'techniques', 'watercolors', 'oil painting', 'patient', 'exhibition', 'talent', 'doubted', 'contagious', 'influence', 'role model'. Band 6 level.",
             "grammar: 'patient when I made', 'shy... but she', 'believed... when I'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'express myself', 'techniques', 'exhibition', 'talent', 'doubted', 'contagious', 'influence', 'role model'. >Band 5: 'Painting', 'shy'. Not Band 7: 'Art teacher', 'proud moment' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'patient when I made', 'believed... when I'. >Band 6: Time clauses and coordinating conjunctions used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a teacher who helped you.\n\nTranscript: My art teacher, Ms. Lee, was amazing. She encouraged me to express myself through painting. She taught me different techniques, like watercolors and oil painting. She was very patient when I made mistakes. I used to be shy about showing my work, but she gave me confidence. She organized an art exhibition for our class. Seeing my painting on the wall was a proud moment. She believed in my talent when I doubted myself. Her passion for art was contagious. I still paint in my free time because of her influence. She was a wonderful role model.\n\nWord Count: 100 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'express myself', 'techniques', 'exhibition', 'talent', 'doubted', 'contagious', 'influence', 'role model'. \n\n>Band 5: 'Painting', 'shy'.\n\nNot Band 7: 'Art teacher', 'proud moment' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'patient when I made', 'believed... when I'. \n\n>Band 6: Time clauses and coordinating conjunctions used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_400",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place you visited.",
        "transcript_cleaned": "I visited the Great Wall of China. It is a massive stone wall that stretches for thousands of miles. I went to a section near Beijing. The climb was steep and tiring, but the view from the top was incredible. I could see mountains and forests as far as the eye could see. It was built to protect the country from invaders. I marveled at the engineering skills of the ancient people. It is amazing that it is still standing after so many centuries. Walking on the wall made me feel connected to history. It is a true wonder of the world.",
        "word_count": 103,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'massive', 'stretches', 'steep', 'tiring', 'invaders', 'marveled', 'engineering skills', 'centuries', 'connected', 'wonder'. Band 6 level.",
             "grammar: 'wall that stretches', 'view... was incredible', 'amazing that it is'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'stretches', 'steep', 'invaders', 'marveled', 'engineering', 'centuries', 'wonder'. >Band 5: 'Massive', 'ancient'. Not Band 7: 'Stone wall', 'mountains' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'wall that stretches', 'amazing that it is'. >Band 6: Relative clauses and noun clauses used correctly. Not Band 8: Lacks idiomatic grammar.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical place you visited.\n\nTranscript: I visited the Great Wall of China. It is a massive stone wall that stretches for thousands of miles. I went to a section near Beijing. The climb was steep and tiring, but the view from the top was incredible. I could see mountains and forests as far as the eye could see. It was built to protect the country from invaders. I marveled at the engineering skills of the ancient people. It is amazing that it is still standing after so many centuries. Walking on the wall made me feel connected to history. It is a true wonder of the world.\n\nWord Count: 103 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'stretches', 'steep', 'invaders', 'marveled', 'engineering', 'centuries', 'wonder'. \n\n>Band 5: 'Massive', 'ancient'.\n\nNot Band 7: 'Stone wall', 'mountains' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'wall that stretches', 'amazing that it is'. \n\n>Band 6: Relative clauses and noun clauses used correctly.\n\nNot Band 8: Lacks idiomatic grammar.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
