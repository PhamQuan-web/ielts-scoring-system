import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch05.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v7_g6_426",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a favorite movie.",
        "transcript_cleaned": "I love the movie Forrest Gump. It is a heartwarming story about a man with a low IQ but a pure heart. The film depicts significant historical events through his eyes. Tom Hanks gives a phenomenal performance as the main character. It is filled with memorable quotes that everyone knows. The soundtrack is also nostalgic and beautiful. It evokes a range of emotions, from laughter to tears. It is a cinematic gem that I have watched many times. I always feel inspired after watching it. The message is that anyone can achieve great things.",
        "word_count": 92,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'story about a man with' (prepositional phrase). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'heartwarming', 'depicts', 'significant', 'historical events', 'phenomenal', 'memorable quotes', 'nostalgic', 'evokes', 'range of emotions', 'cinematic gem'. >Band 6: 'Evokes', 'phenomenal'. Not Band 8: 'Soundtrack' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'story about a man', 'It is filled with'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a favorite movie.\n\nTranscript: I love the movie Forrest Gump. It is a heartwarming story about a man with a low IQ but a pure heart. The film depicts significant historical events through his eyes. Tom Hanks gives a phenomenal performance as the main character. It is filled with memorable quotes that everyone knows. The soundtrack is also nostalgic and beautiful. It evokes a range of emotions, from laughter to tears. It is a cinematic gem that I have watched many times. I always feel inspired after watching it. The message is that anyone can achieve great things.\n\nWord Count: 92 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'heartwarming', 'depicts', 'significant', 'historical events', 'phenomenal', 'memorable quotes', 'nostalgic', 'evokes', 'range of emotions', 'cinematic gem'. \n\n>Band 6: 'Evokes', 'phenomenal'.\n\nNot Band 8: 'Soundtrack' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'story about a man', 'It is filled with'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_427",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you received.",
        "transcript_cleaned": "My sister gifted me a handmade scarf last winter. She knitted it herself using high-quality wool. The pattern is intricate and colorful. It keeps me warm during the bitter cold of winter. I appreciate the time and effort she invested in making it. It is a unique accessory that complements my outfits perfectly. Every time I wear it, I feel loved and cherished. It is more valuable to me than any store-bought item. I will keep it forever as a memento of her kindness.",
        "word_count": 86,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'knitted it herself using' (participle). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'handmade', 'knitted', 'intricate', 'bitter cold', 'appreciate', 'invested', 'unique', 'accessory', 'complements', 'valuable', 'memento'. >Band 6: 'Intricate', 'complements'. Not Band 8: 'High-quality' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'knitted it herself using', 'Every time I wear it'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a gift you received.\n\nTranscript: My sister gifted me a handmade scarf last winter. She knitted it herself using high-quality wool. The pattern is intricate and colorful. It keeps me warm during the bitter cold of winter. I appreciate the time and effort she invested in making it. It is a unique accessory that complements my outfits perfectly. Every time I wear it, I feel loved and cherished. It is more valuable to me than any store-bought item. I will keep it forever as a memento of her kindness.\n\nWord Count: 86 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'handmade', 'knitted', 'intricate', 'bitter cold', 'appreciate', 'invested', 'unique', 'accessory', 'complements', 'valuable', 'memento'. \n\n>Band 6: 'Intricate', 'complements'.\n\nNot Band 8: 'High-quality' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'knitted it herself using', 'Every time I wear it'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_428",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a skill you learned.",
        "transcript_cleaned": "I learned to bake bread from scratch during the lockdown. It requires precision and patience. I experimented with different types of flour and yeast. Kneading the dough is therapeutic and relaxing. The aroma of fresh bread is intoxicating and makes the house smell good. I had some failures initially, but I persisted and kept trying. Now I can bake a perfect loaf every time. Sharing it with my family brings me joy. It is a satisfying culinary skill that I am proud of.",
        "word_count": 84,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'bake bread from scratch' (idiom). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'from scratch', 'precision', 'experimented', 'kneading', 'dough', 'therapeutic', 'aroma', 'intoxicating', 'failures', 'persisted', 'culinary'. >Band 6: 'Therapeutic', 'intoxicating'. Not Band 8: 'Fresh bread' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'failures initially, but', 'Sharing it with my family'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a skill you learned.\n\nTranscript: I learned to bake bread from scratch during the lockdown. It requires precision and patience. I experimented with different types of flour and yeast. Kneading the dough is therapeutic and relaxing. The aroma of fresh bread is intoxicating and makes the house smell good. I had some failures initially, but I persisted and kept trying. Now I can bake a perfect loaf every time. Sharing it with my family brings me joy. It is a satisfying culinary skill that I am proud of.\n\nWord Count: 84 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'from scratch', 'precision', 'experimented', 'kneading', 'dough', 'therapeutic', 'aroma', 'intoxicating', 'failures', 'persisted', 'culinary'. \n\n>Band 6: 'Therapeutic', 'intoxicating'.\n\nNot Band 8: 'Fresh bread' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'failures initially, but', 'Sharing it with my family'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_429",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a person you admire.",
        "transcript_cleaned": "I admire Elon Musk for his innovative vision. He is a pioneer in the electric vehicle industry. His determination to explore space is audacious and bold. He takes calculated risks that others avoid. Although he is controversial, his achievements are undeniable. He challenges the status quo in every industry he enters. He has revolutionized transportation and energy. His work ethics are intense and demanding. I find his journey very inspiring. He shows that with hard work, anything is possible.",
        "word_count": 79,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'innovative vision' (collocation). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'innovative', 'pioneer', 'determination', 'audacious', 'calculated risks', 'controversial', 'achievements', 'undeniable', 'challenges the status quo', 'revolutionized'. >Band 6: 'Audacious', 'status quo'. Not Band 8: 'Electric vehicle' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'Although he is controversial', 'risks that others avoid'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a person you admire.\n\nTranscript: I admire Elon Musk for his innovative vision. He is a pioneer in the electric vehicle industry. His determination to explore space is audacious and bold. He takes calculated risks that others avoid. Although he is controversial, his achievements are undeniable. He challenges the status quo in every industry he enters. He has revolutionized transportation and energy. His work ethics are intense and demanding. I find his journey very inspiring. He shows that with hard work, anything is possible.\n\nWord Count: 79 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'innovative', 'pioneer', 'determination', 'audacious', 'calculated risks', 'controversial', 'achievements', 'undeniable', 'challenges the status quo', 'revolutionized'. \n\n>Band 6: 'Audacious', 'status quo'.\n\nNot Band 8: 'Electric vehicle' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'Although he is controversial', 'risks that others avoid'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_430",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a journey.",
        "transcript_cleaned": "I took a road trip along the coast last summer. The route was scenic and winding. I stopped at quaint seaside towns to explore. The ocean breeze was refreshing and cool. I tasted fresh seafood at local eateries. The sunset over the horizon was spectacular. It was a liberating experience to drive without a set schedule. I felt connected to nature and relaxed. It was a memorable trip that I will never forget. I plan to do it again next year.",
        "word_count": 81,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'route was scenic' (simple). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'scenic', 'winding', 'quaint', 'seaside', 'refreshing', 'eateries', 'horizon', 'spectacular', 'liberating', 'schedule'. >Band 6: 'Quaint', 'liberating'. Not Band 8: 'Road trip' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'drive without a set schedule', 'sunset... was spectacular'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a journey.\n\nTranscript: I took a road trip along the coast last summer. The route was scenic and winding. I stopped at quaint seaside towns to explore. The ocean breeze was refreshing and cool. I tasted fresh seafood at local eateries. The sunset over the horizon was spectacular. It was a liberating experience to drive without a set schedule. I felt connected to nature and relaxed. It was a memorable trip that I will never forget. I plan to do it again next year.\n\nWord Count: 81 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'scenic', 'winding', 'quaint', 'seaside', 'refreshing', 'eateries', 'horizon', 'spectacular', 'liberating', 'schedule'. \n\n>Band 6: 'Quaint', 'liberating'.\n\nNot Band 8: 'Road trip' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'drive without a set schedule', 'sunset... was spectacular'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_431",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "Fixing my car engine was a complex undertaking. I have zero mechanical knowledge, so it was hard. I watched videos to understand the components. I bought the necessary tools from a shop. It was greasy and frustrating work. I made mistakes and had to start over. Finally, the engine started working again. The sense of relief was immense. I saved a lot of money on repairs. It was a proud moment for me. I learned a lot about cars.",
        "word_count": 80,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'complex undertaking' (collocation). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'complex undertaking', 'mechanical', 'components', 'necessary', 'greasy', 'frustrating', 'sense of relief', 'immense', 'repairs'. >Band 6: 'Undertaking', 'immense'. Not Band 8: 'Zero knowledge' is informal.",
        "grammar_reason": "[GRA6] Key evidence: 'videos to understand', 'mistakes and had to'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: Fixing my car engine was a complex undertaking. I have zero mechanical knowledge, so it was hard. I watched videos to understand the components. I bought the necessary tools from a shop. It was greasy and frustrating work. I made mistakes and had to start over. Finally, the engine started working again. The sense of relief was immense. I saved a lot of money on repairs. It was a proud moment for me. I learned a lot about cars.\n\nWord Count: 80 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'complex undertaking', 'mechanical', 'components', 'necessary', 'greasy', 'frustrating', 'sense of relief', 'immense', 'repairs'. \n\n>Band 6: 'Undertaking', 'immense'.\n\nNot Band 8: 'Zero knowledge' is informal.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'videos to understand', 'mistakes and had to'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_432",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read 1984 by George Orwell recently. It is a dystopian novel about a totalitarian regime. The concepts of surveillance and censorship are terrifyingly relevant today. The protagonist's struggle for freedom is poignant. The ending is bleak but powerful. It makes you question authority and control. The language is stark and impactful. It is a literary masterpiece that everyone should read. It opened my eyes to the dangers of power. I will never forget it.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'dystopian novel' (collocation). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'dystopian', 'totalitarian regime', 'surveillance', 'censorship', 'terrifyingly relevant', 'protagonist', 'struggle', 'poignant', 'bleak', 'stark', 'impactful', 'literary masterpiece'. >Band 6: 'Totalitarian', 'poignant'. Not Band 8: 'Authority' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'novel about', 'makes you question'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read 1984 by George Orwell recently. It is a dystopian novel about a totalitarian regime. The concepts of surveillance and censorship are terrifyingly relevant today. The protagonist's struggle for freedom is poignant. The ending is bleak but powerful. It makes you question authority and control. The language is stark and impactful. It is a literary masterpiece that everyone should read. It opened my eyes to the dangers of power. I will never forget it.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'dystopian', 'totalitarian regime', 'surveillance', 'censorship', 'terrifyingly relevant', 'protagonist', 'struggle', 'poignant', 'bleak', 'stark', 'impactful', 'literary masterpiece'. \n\n>Band 6: 'Totalitarian', 'poignant'.\n\nNot Band 8: 'Authority' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'novel about', 'makes you question'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_433",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I went to a housewarming party last week. My friends moved into a spacious apartment. They served homemade cocktails and canapés. We played board games and laughed uncontrollably. The ambiance was cozy and inviting. I met their new neighbors. It was a delightful evening of socializing. I gave them a potted plant as a gift. It was a great way to celebrate their new home. I enjoyed every moment of it.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'housewarming party' (collocation). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'housewarming', 'spacious', 'cocktails', 'canapés', 'uncontrollably', 'ambiance', 'cozy', 'inviting', 'delightful', 'socializing'. >Band 6: 'Canapés', 'ambiance'. Not Band 8: 'Board games' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'moved into', 'evening of socializing'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I went to a housewarming party last week. My friends moved into a spacious apartment. They served homemade cocktails and canapés. We played board games and laughed uncontrollably. The ambiance was cozy and inviting. I met their new neighbors. It was a delightful evening of socializing. I gave them a potted plant as a gift. It was a great way to celebrate their new home. I enjoyed every moment of it.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'housewarming', 'spacious', 'cocktails', 'canapés', 'uncontrollably', 'ambiance', 'cozy', 'inviting', 'delightful', 'socializing'. \n\n>Band 6: 'Canapés', 'ambiance'.\n\nNot Band 8: 'Board games' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'moved into', 'evening of socializing'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_434",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I use a coffee maker every morning. It is a sleek, modern appliance. I can program it to brew coffee automatically. The smell of fresh coffee wakes me up. It saves me time and money. I prefer the taste of homemade coffee. It is an integral part of my morning routine. I clean it every week to keep it working well. It is very reliable and durable. I highly recommend it.",
        "word_count": 72,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'program it to brew' (infinitive). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'sleek', 'appliance', 'program', 'brew', 'automatically', 'saves me time', 'prefer', 'integral', 'routine'. >Band 6: 'Integral', 'appliance'. Not Band 8: 'Fresh coffee' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'program it to brew', 'saves me time'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I use a coffee maker every morning. It is a sleek, modern appliance. I can program it to brew coffee automatically. The smell of fresh coffee wakes me up. It saves me time and money. I prefer the taste of homemade coffee. It is an integral part of my morning routine. I clean it every week to keep it working well. It is very reliable and durable. I highly recommend it.\n\nWord Count: 72 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'sleek', 'appliance', 'program', 'brew', 'automatically', 'saves me time', 'prefer', 'integral', 'routine'. \n\n>Band 6: 'Integral', 'appliance'.\n\nNot Band 8: 'Fresh coffee' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'program it to brew', 'saves me time'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_435",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place.",
        "transcript_cleaned": "I visited the Pyramids of Giza in Egypt. They are ancient structures that have stood the test of time. The sheer size of the blocks is baffling. I rode a camel around the site. The desert landscape adds to the mystery. It is a marvel of engineering. I wondered how they were built without modern technology. It was an awe-inspiring experience. I took many photos to remember it. It is a place everyone should visit once.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'stood the test of time' (idiom). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'ancient structures', 'stood the test of time', 'sheer size', 'baffling', 'landscape', 'mystery', 'marvel', 'engineering', 'awe-inspiring'. >Band 6: 'Baffling', 'marvel'. Not Band 8: 'Camel' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'structures that have stood', 'wondered how they were'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical place.\n\nTranscript: I visited the Pyramids of Giza in Egypt. They are ancient structures that have stood the test of time. The sheer size of the blocks is baffling. I rode a camel around the site. The desert landscape adds to the mystery. It is a marvel of engineering. I wondered how they were built without modern technology. It was an awe-inspiring experience. I took many photos to remember it. It is a place everyone should visit once.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'ancient structures', 'stood the test of time', 'sheer size', 'baffling', 'landscape', 'mystery', 'marvel', 'engineering', 'awe-inspiring'. \n\n>Band 6: 'Baffling', 'marvel'.\n\nNot Band 8: 'Camel' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'structures that have stood', 'wondered how they were'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_436",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I have a cactus collection at home. They are resilient plants that survive in harsh conditions. They come in various shapes and sizes. I like their unique appearance. They require very little water. Some of them bloom with colorful flowers. They are low-maintenance and perfect for busy people. They add a touch of greenery to my room. I enjoy taking care of them. They are very interesting plants.",
        "word_count": 68,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'plants that survive' (relative). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'collection', 'resilient', 'harsh conditions', 'unique appearance', 'require', 'bloom', 'low-maintenance', 'greenery'. >Band 6: 'Resilient', 'low-maintenance'. Not Band 8: 'Shapes and sizes' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'plants that survive', 'add a touch of'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I have a cactus collection at home. They are resilient plants that survive in harsh conditions. They come in various shapes and sizes. I like their unique appearance. They require very little water. Some of them bloom with colorful flowers. They are low-maintenance and perfect for busy people. They add a touch of greenery to my room. I enjoy taking care of them. They are very interesting plants.\n\nWord Count: 68 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'collection', 'resilient', 'harsh conditions', 'unique appearance', 'require', 'bloom', 'low-maintenance', 'greenery'. \n\n>Band 6: 'Resilient', 'low-maintenance'.\n\nNot Band 8: 'Shapes and sizes' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'plants that survive', 'add a touch of'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_437",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "I have a friend who is a chef. He is passionate about culinary arts. He creates exquisite dishes. We often dine at his restaurant. He explains the ingredients and techniques. He is generous and always treats us. His creativity inspires me. He has a refined palate. I admire his dedication to his work. He works long hours but loves what he does. He is a great friend.",
        "word_count": 68,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'friend who is' (relative). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'passionate', 'culinary arts', 'exquisite', 'dine', 'ingredients', 'techniques', 'generous', 'creativity', 'refined palate'. >Band 6: 'Exquisite', 'refined'. Not Band 8: 'Restaurant' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'friend who is', 'inspires me'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a friend.\n\nTranscript: I have a friend who is a chef. He is passionate about culinary arts. He creates exquisite dishes. We often dine at his restaurant. He explains the ingredients and techniques. He is generous and always treats us. His creativity inspires me. He has a refined palate. I admire his dedication to his work. He works long hours but loves what he does. He is a great friend.\n\nWord Count: 68 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'passionate', 'culinary arts', 'exquisite', 'dine', 'ingredients', 'techniques', 'generous', 'creativity', 'refined palate'. \n\n>Band 6: 'Exquisite', 'refined'.\n\nNot Band 8: 'Restaurant' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'friend who is', 'inspires me'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_438",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I had to choose between two universities. One was prestigious but expensive. The other was affordable but less renowned. I researched the curriculum and faculty. I worried about student debt. I prioritized my financial stability. I chose the affordable option. I do not regret my decision. It was a tough choice to make. I am happy with my education. It was the right path for me.",
        "word_count": 66,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'One was... The other was' (parallel). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'prestigious', 'affordable', 'renowned', 'curriculum', 'faculty', 'student debt', 'prioritized', 'financial stability'. >Band 6: 'Prestigious', 'renowned'. Not Band 8: 'Universities' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'choose between', 'prioritized my financial'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I had to choose between two universities. One was prestigious but expensive. The other was affordable but less renowned. I researched the curriculum and faculty. I worried about student debt. I prioritized my financial stability. I chose the affordable option. I do not regret my decision. It was a tough choice to make. I am happy with my education. It was the right path for me.\n\nWord Count: 66 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'prestigious', 'affordable', 'renowned', 'curriculum', 'faculty', 'student debt', 'prioritized', 'financial stability'. \n\n>Band 6: 'Prestigious', 'renowned'.\n\nNot Band 8: 'Universities' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'choose between', 'prioritized my financial'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
