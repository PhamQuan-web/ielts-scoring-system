import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch05.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v7_g6_401",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place.",
        "transcript_cleaned": "I visited the Colosseum in Rome, which is a magnificent ancient amphitheater. It was built thousands of years ago and it is still standing. The architecture is stunning, with huge arches and columns. I was amazed by the sheer scale of the structure. It was used for gladiator battles, which sounds terrifying. I took many photos to capture the beauty of the ruins. Although it is crowded with tourists, it is definitely worth a visit if you are in Italy. I learned a lot about Roman history during my visit. The guide explained how the gladiators fought and died there. It was a very educational and memorable experience for me.",
        "word_count": 108,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'built thousands of years ago and it is still standing' (run-on), 'sounds terrifying' (informal)."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'magnificent', 'amphitheater', 'architecture', 'stunning', 'sheer scale', 'gladiator battles', 'terrifying', 'ruins'. >Band 6: 'Sheer scale', 'magnificent'. Not Band 8: 'Worth a visit' is a cliché.",
        "grammar_reason": "[GRA6] Key evidence: 'Colosseum in Rome, which is', 'Although it is crowded'. >Band 5: Mix of simple/complex. Not Band 7: Some errors in complex structures or less variety.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical place.\n\nTranscript: I visited the Colosseum in Rome, which is a magnificent ancient amphitheater. It was built thousands of years ago and it is still standing. The architecture is stunning, with huge arches and columns. I was amazed by the sheer scale of the structure. It was used for gladiator battles, which sounds terrifying. I took many photos to capture the beauty of the ruins. Although it is crowded with tourists, it is definitely worth a visit if you are in Italy. I learned a lot about Roman history during my visit. The guide explained how the gladiators fought and died there. It was a very educational and memorable experience for me.\n\nWord Count: 108 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'magnificent', 'amphitheater', 'architecture', 'stunning', 'sheer scale', 'gladiator battles', 'terrifying', 'ruins'. \n\n>Band 6: 'Sheer scale', 'magnificent'.\n\nNot Band 8: 'Worth a visit' is a cliché.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'Colosseum in Rome, which is', 'Although it is crowded'. \n\n>Band 5: Mix of simple/complex.\n\nNot Band 7: Some errors in complex structures or less variety.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_402",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a favorite movie.",
        "transcript_cleaned": "One of my all-time favorite movies is Inception. It has a compelling plot about dream infiltration. The visual effects are mind-blowing and very realistic. The actors delivered exceptional performances, especially Leonardo DiCaprio. I was particularly impressed by the intricate storyline. It kept me on the edge of my seat the whole time. However, I think the ending was a bit ambiguous and confusing. I have watched it multiple times to understand all the details. It is a masterpiece of science fiction cinema. The music score by Hans Zimmer is also fantastic and adds to the tension. I highly recommend it to anyone who likes thrillers.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'compelling plot about' (preposition), 'ending was a bit ambiguous' (simple structure)."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'compelling plot', 'infiltration', 'mind-blowing', 'exceptional performances', 'intricate storyline', 'ambiguous', 'masterpiece'. >Band 6: 'Intricate', 'ambiguous'. Not Band 8: 'All-time favorite' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'It kept me on the edge', 'However, I think'. >Band 5: Uses complex structures. Not Band 7: Some sentences are simple and repetitive.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a favorite movie.\n\nTranscript: One of my all-time favorite movies is Inception. It has a compelling plot about dream infiltration. The visual effects are mind-blowing and very realistic. The actors delivered exceptional performances, especially Leonardo DiCaprio. I was particularly impressed by the intricate storyline. It kept me on the edge of my seat the whole time. However, I think the ending was a bit ambiguous and confusing. I have watched it multiple times to understand all the details. It is a masterpiece of science fiction cinema. The music score by Hans Zimmer is also fantastic and adds to the tension. I highly recommend it to anyone who likes thrillers.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'compelling plot', 'infiltration', 'mind-blowing', 'exceptional performances', 'intricate storyline', 'ambiguous', 'masterpiece'. \n\n>Band 6: 'Intricate', 'ambiguous'.\n\nNot Band 8: 'All-time favorite' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'It kept me on the edge', 'However, I think'. \n\n>Band 5: Uses complex structures.\n\nNot Band 7: Some sentences are simple and repetitive.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_403",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you received.",
        "transcript_cleaned": "My parents gave me a vintage watch for my graduation. It is a sentimental gift that I cherish deeply. The craftsmanship is exquisite and very detailed. It has a leather strap and a gold face. I wear it on special occasions because I don't want to damage it. It reminds me of their support and love throughout my studies. I was overwhelmed with gratitude when I opened the box. It is not just a watch; it is a family heirloom that I will pass down to my children. I think it is the best gift I have ever received in my life.",
        "word_count": 103,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'gift that I cherish' (relative), 'reminds me of' (preposition). Simple structures dominate."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'vintage', 'sentimental', 'cherish deeply', 'craftsmanship', 'exquisite', 'gratitude', 'heirloom'. >Band 6: 'Heirloom', 'exquisite'. Not Band 8: 'Special occasions' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'gift that I cherish', 'when I opened the box'. >Band 5: Mix of simple and complex. Not Band 7: Errors in punctuation or flow.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a gift you received.\n\nTranscript: My parents gave me a vintage watch for my graduation. It is a sentimental gift that I cherish deeply. The craftsmanship is exquisite and very detailed. It has a leather strap and a gold face. I wear it on special occasions because I don't want to damage it. It reminds me of their support and love throughout my studies. I was overwhelmed with gratitude when I opened the box. It is not just a watch; it is a family heirloom that I will pass down to my children. I think it is the best gift I have ever received in my life.\n\nWord Count: 103 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'vintage', 'sentimental', 'cherish deeply', 'craftsmanship', 'exquisite', 'gratitude', 'heirloom'. \n\n>Band 6: 'Heirloom', 'exquisite'.\n\nNot Band 8: 'Special occasions' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'gift that I cherish', 'when I opened the box'. \n\n>Band 5: Mix of simple and complex.\n\nNot Band 7: Errors in punctuation or flow.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_404",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a skill you learned.",
        "transcript_cleaned": "I learned how to code in Python last year. It was a challenging but rewarding experience for me. I utilized online tutorials to grasp the basics of programming. At first, the syntax was confusing, but I persisted and practiced every day. Now I can build simple websites and applications. Coding enhances my problem-solving abilities and logical thinking. It requires attention to detail and patience. I hope to pursue a career in software development in the future. It opens up many career opportunities in the tech industry. I am glad I decided to learn this skill because it is very useful.",
        "word_count": 100,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'challenging but rewarding' (adjective phrase), 'At first, the syntax was confusing' (simple). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'challenging but rewarding', 'utilized', 'grasp', 'syntax', 'persisted', 'enhances', 'logical thinking', 'attention to detail'. >Band 6: 'Syntax', 'enhances'. Not Band 8: 'Career opportunities' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'learned how to code', 'challenging but rewarding'. >Band 5: Mix of structures. Not Band 7: Frequent simple sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a skill you learned.\n\nTranscript: I learned how to code in Python last year. It was a challenging but rewarding experience for me. I utilized online tutorials to grasp the basics of programming. At first, the syntax was confusing, but I persisted and practiced every day. Now I can build simple websites and applications. Coding enhances my problem-solving abilities and logical thinking. It requires attention to detail and patience. I hope to pursue a career in software development in the future. It opens up many career opportunities in the tech industry. I am glad I decided to learn this skill because it is very useful.\n\nWord Count: 100 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'challenging but rewarding', 'utilized', 'grasp', 'syntax', 'persisted', 'enhances', 'logical thinking', 'attention to detail'. \n\n>Band 6: 'Syntax', 'enhances'.\n\nNot Band 8: 'Career opportunities' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'learned how to code', 'challenging but rewarding'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Frequent simple sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_405",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a person you admire.",
        "transcript_cleaned": "I deeply admire my grandfather because he is a very strong person. He is a man of integrity and wisdom. He overcame many hardships in his life, including poverty. He always offers sage advice when I am in a dilemma. His resilience is inspiring to me. He taught me the importance of hard work and honesty. Even though he is old, he stays active and reads books daily. He is a pillar of strength for our family. I aspire to be like him one day. He is the most influential person in my life and I respect him greatly.",
        "word_count": 101,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'man of integrity' (noun phrase), 'Even though he is old' (concession). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'integrity', 'wisdom', 'hardships', 'sage advice', 'dilemma', 'resilience', 'inspiring', 'pillar of strength', 'aspire'. >Band 6: 'Sage advice', 'pillar of strength'. Not Band 8: 'Hard work' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'Even though he is old', 'when I am in a dilemma'. >Band 5: Mix of structures. Not Band 7: Lack of complex variety.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a person you admire.\n\nTranscript: I deeply admire my grandfather because he is a very strong person. He is a man of integrity and wisdom. He overcame many hardships in his life, including poverty. He always offers sage advice when I am in a dilemma. His resilience is inspiring to me. He taught me the importance of hard work and honesty. Even though he is old, he stays active and reads books daily. He is a pillar of strength for our family. I aspire to be like him one day. He is the most influential person in my life and I respect him greatly.\n\nWord Count: 101 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'integrity', 'wisdom', 'hardships', 'sage advice', 'dilemma', 'resilience', 'inspiring', 'pillar of strength', 'aspire'. \n\n>Band 6: 'Sage advice', 'pillar of strength'.\n\nNot Band 8: 'Hard work' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'Even though he is old', 'when I am in a dilemma'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Lack of complex variety.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_406",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a journey.",
        "transcript_cleaned": "I went on a backpacking trip to Thailand with my friends last summer. The landscape was picturesque, with turquoise waters and white sandy beaches. I immersed myself in the local culture and tried many things. The street food was delectable and very affordable. I navigated through bustling markets and visited ancient temples. It was a transformative experience that broadened my horizons. I met fellow travelers from all over the globe. The memories I made there are invaluable to me. I would love to go back there again someday because it was such a wonderful adventure.",
        "word_count": 95,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'The landscape was picturesque' (simple), 'It was a transformative experience that broadened' (relative clause). Repetitive structure."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'picturesque', 'turquoise', 'immersed', 'delectable', 'navigated', 'bustling', 'transformative', 'broadened my horizons', 'invaluable'. >Band 6: 'Delectable', 'transformative'. Not Band 8: 'Street food' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'experience that broadened', 'navigated... and visited'. >Band 5: Mix of structures. Not Band 7: Simple sentence chains.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a journey.\n\nTranscript: I went on a backpacking trip to Thailand with my friends last summer. The landscape was picturesque, with turquoise waters and white sandy beaches. I immersed myself in the local culture and tried many things. The street food was delectable and very affordable. I navigated through bustling markets and visited ancient temples. It was a transformative experience that broadened my horizons. I met fellow travelers from all over the globe. The memories I made there are invaluable to me. I would love to go back there again someday because it was such a wonderful adventure.\n\nWord Count: 95 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'picturesque', 'turquoise', 'immersed', 'delectable', 'navigated', 'bustling', 'transformative', 'broadened my horizons', 'invaluable'. \n\n>Band 6: 'Delectable', 'transformative'.\n\nNot Band 8: 'Street food' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'experience that broadened', 'navigated... and visited'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Simple sentence chains.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_407",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "Organizing a charity event was a daunting task that I undertook last year. I had to coordinate with various vendors and sponsors. The logistics were complex, and I faced several unexpected hurdles. I had to delegate tasks to my team members to ensure everything ran smoothly. Effective communication was crucial for the success of the event. Despite the stress, the event was a resounding success. We raised a substantial amount of money for the orphanage. It gave me a sense of accomplishment and pride. I learned a lot about leadership and teamwork from this experience.",
        "word_count": 96,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'Organizing a charity event was' (gerund subject), 'Despite the stress' (prepositional phrase). Simple structure."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'daunting', 'coordinate', 'vendors', 'logistics', 'hurdles', 'delegate', 'resounding success', 'substantial', 'accomplishment'. >Band 6: 'Hurdles', 'resounding success'. Not Band 8: 'Effective communication' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'Organizing... was', 'Despite the stress'. >Band 5: Mix of structures. Not Band 7: Short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: Organizing a charity event was a daunting task that I undertook last year. I had to coordinate with various vendors and sponsors. The logistics were complex, and I faced several unexpected hurdles. I had to delegate tasks to my team members to ensure everything ran smoothly. Effective communication was crucial for the success of the event. Despite the stress, the event was a resounding success. We raised a substantial amount of money for the orphanage. It gave me a sense of accomplishment and pride. I learned a lot about leadership and teamwork from this experience.\n\nWord Count: 96 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'daunting', 'coordinate', 'vendors', 'logistics', 'hurdles', 'delegate', 'resounding success', 'substantial', 'accomplishment'. \n\n>Band 6: 'Hurdles', 'resounding success'.\n\nNot Band 8: 'Effective communication' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'Organizing... was', 'Despite the stress'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_408",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read a biography of Steve Jobs recently, which was very inspiring. It provided a fascinating insight into his life and career. He was a visionary who revolutionized the technology industry. The book details his eccentric personality and his relentless pursuit of perfection. It was an engaging read that I could not put down. I learned a lot about innovation and leadership from his story. It motivated me to think outside the box and chase my dreams. It is a book that everyone should read because it is so educational and interesting.",
        "word_count": 92,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'visionary who revolutionized' (relative clause). 'think outside the box' (idiom). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'biography', 'fascinating insight', 'visionary', 'revolutionized', 'eccentric', 'relentless pursuit', 'engaging', 'innovation'. >Band 6: 'Eccentric', 'relentless pursuit'. Not Band 8: 'Think outside the box' is a cliché.",
        "grammar_reason": "[GRA6] Key evidence: 'visionary who revolutionized', 'read that I could not put down'. >Band 5: Mix of structures. Not Band 7: Simple sentence flow.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read a biography of Steve Jobs recently, which was very inspiring. It provided a fascinating insight into his life and career. He was a visionary who revolutionized the technology industry. The book details his eccentric personality and his relentless pursuit of perfection. It was an engaging read that I could not put down. I learned a lot about innovation and leadership from his story. It motivated me to think outside the box and chase my dreams. It is a book that everyone should read because it is so educational and interesting.\n\nWord Count: 92 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'biography', 'fascinating insight', 'visionary', 'revolutionized', 'eccentric', 'relentless pursuit', 'engaging', 'innovation'. \n\n>Band 6: 'Eccentric', 'relentless pursuit'.\n\nNot Band 8: 'Think outside the box' is a cliché.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'visionary who revolutionized', 'read that I could not put down'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Simple sentence flow.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_409",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I attended a lavish wedding reception last month for my cousin. The venue was decorated with elaborate floral arrangements. The atmosphere was festive and jubilant. We were served a gourmet meal with exquisite desserts. I mingled with the guests and danced to lively music. The highlight was the fireworks display at the end of the night. It was a memorable celebration of love and happiness. I thoroughly enjoyed the festivities and meeting new people. It was one of the best parties I have ever been to because everything was so perfect.",
        "word_count": 91,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'venue was decorated with' (passive). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'lavish', 'reception', 'elaborate', 'floral arrangements', 'festive', 'jubilant', 'gourmet', 'exquisite', 'mingled', 'memorable'. >Band 6: 'Jubilant', 'lavish'. Not Band 8: 'Lively music' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'venue was decorated', 'danced to lively music'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I attended a lavish wedding reception last month for my cousin. The venue was decorated with elaborate floral arrangements. The atmosphere was festive and jubilant. We were served a gourmet meal with exquisite desserts. I mingled with the guests and danced to lively music. The highlight was the fireworks display at the end of the night. It was a memorable celebration of love and happiness. I thoroughly enjoyed the festivities and meeting new people. It was one of the best parties I have ever been to because everything was so perfect.\n\nWord Count: 91 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'lavish', 'reception', 'elaborate', 'floral arrangements', 'festive', 'jubilant', 'gourmet', 'exquisite', 'mingled', 'memorable'. \n\n>Band 6: 'Jubilant', 'lavish'.\n\nNot Band 8: 'Lively music' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'venue was decorated', 'danced to lively music'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_410",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "My smartphone is an indispensable tool in my daily life. It is sleek and user-friendly. I use it for multiple functions, such as checking emails and navigation. It keeps me connected with the world. The camera quality is superb, allowing me to capture high-resolution photos. However, I am sometimes addicted to scrolling through social media. It can be a distraction when I need to study. Nevertheless, I cannot imagine life without it because it helps me in so many ways. It is a vital part of my modern lifestyle.",
        "word_count": 90,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'indispensable tool in' (correct), 'allowing me to capture' (participle phrase). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'indispensable', 'sleek', 'user-friendly', 'navigation', 'superb', 'high-resolution', 'addicted', 'distraction'. >Band 6: 'Indispensable', 'superb'. Not Band 8: 'Social media' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'allowing me to capture', 'However, I am'. >Band 5: Mix of structures. Not Band 7: Simple sentence structure dominates.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: My smartphone is an indispensable tool in my daily life. It is sleek and user-friendly. I use it for multiple functions, such as checking emails and navigation. It keeps me connected with the world. The camera quality is superb, allowing me to capture high-resolution photos. However, I am sometimes addicted to scrolling through social media. It can be a distraction when I need to study. Nevertheless, I cannot imagine life without it because it helps me in so many ways. It is a vital part of my modern lifestyle.\n\nWord Count: 90 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'indispensable', 'sleek', 'user-friendly', 'navigation', 'superb', 'high-resolution', 'addicted', 'distraction'. \n\n>Band 6: 'Indispensable', 'superb'.\n\nNot Band 8: 'Social media' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'allowing me to capture', 'However, I am'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Simple sentence structure dominates.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_411",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place.",
        "transcript_cleaned": "I visited the Great Wall of China a few years ago. It is a monumental structure that stretches for miles. It was constructed to protect the empire from invaders. Walking on the wall was physically demanding but exhilarating. The panoramic views of the mountains were breathtaking. It is a testament to human ingenuity and perseverance. I felt a sense of awe standing there and looking at the view. It is undoubtedly a world wonder that everyone should see. The history behind it is very rich and interesting.",
        "word_count": 87,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'monumental structure that stretches' (relative), 'Walking on the wall was' (gerund). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'monumental', 'stretches', 'invaders', 'physically demanding', 'exhilarating', 'panoramic', 'breathtaking', 'testament', 'ingenuity', 'perseverance'. >Band 6: 'Ingenuity', 'testament'. Not Band 8: 'World wonder' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'structure that stretches', 'Walking on the wall was'. >Band 5: Mix of structures. Not Band 7: Short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical place.\n\nTranscript: I visited the Great Wall of China a few years ago. It is a monumental structure that stretches for miles. It was constructed to protect the empire from invaders. Walking on the wall was physically demanding but exhilarating. The panoramic views of the mountains were breathtaking. It is a testament to human ingenuity and perseverance. I felt a sense of awe standing there and looking at the view. It is undoubtedly a world wonder that everyone should see. The history behind it is very rich and interesting.\n\nWord Count: 87 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'monumental', 'stretches', 'invaders', 'physically demanding', 'exhilarating', 'panoramic', 'breathtaking', 'testament', 'ingenuity', 'perseverance'. \n\n>Band 6: 'Ingenuity', 'testament'.\n\nNot Band 8: 'World wonder' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'structure that stretches', 'Walking on the wall was'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_412",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I am fascinated by the bamboo plant. It is incredibly versatile and grows rapidly. It is used for construction, food, and decoration. Bamboo forests are serene and peaceful. The stalks are hollow but resilient. It symbolizes flexibility and strength in Asian culture. I have some bamboo in my garden. It requires minimal maintenance. It is an eco-friendly resource. I like watching it sway in the wind. It is a beautiful plant.",
        "word_count": 70,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'incredibly versatile' (adverb-adjective). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'fascinated', 'versatile', 'rapidly', 'serene', 'stalks', 'hollow', 'resilient', 'symbolizes', 'minimal maintenance', 'eco-friendly'. >Band 6: 'Resilient', 'versatile'. Not Band 8: 'Asian culture' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'used for construction', 'requires minimal maintenance'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I am fascinated by the bamboo plant. It is incredibly versatile and grows rapidly. It is used for construction, food, and decoration. Bamboo forests are serene and peaceful. The stalks are hollow but resilient. It symbolizes flexibility and strength in Asian culture. I have some bamboo in my garden. It requires minimal maintenance. It is an eco-friendly resource. I like watching it sway in the wind. It is a beautiful plant.\n\nWord Count: 70 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'fascinated', 'versatile', 'rapidly', 'serene', 'stalks', 'hollow', 'resilient', 'symbolizes', 'minimal maintenance', 'eco-friendly'. \n\n>Band 6: 'Resilient', 'versatile'.\n\nNot Band 8: 'Asian culture' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'used for construction', 'requires minimal maintenance'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
