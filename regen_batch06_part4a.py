import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch06.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v7_g7_526",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Notre Dame Cathedral in Paris a few years ago. It is a masterpiece of Gothic architecture, known for its flying buttresses and gargoyles. The stained glass windows are mesmerizing, especially the Rose Window. I climbed the towers for a panoramic view of Paris, which was breathtaking. It was damaged by a fire recently, but restoration is underway. It remains a symbol of resilience and history for the French people. I felt a deep sense of peace inside the cathedral. It is a place that connects the past with the present.",
        "word_count": 94,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'masterpiece', 'Gothic architecture', 'flying buttresses', 'gargoyles', 'stained glass', 'mesmerizing', 'panoramic view', 'restoration', 'underway', 'resilience'. Band 7 level.",
             "grammar: 'architecture, known for', 'view... which was', 'damaged by a fire'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'masterpiece', 'Gothic architecture', 'flying buttresses', 'gargoyles', 'mesmerizing', 'panoramic', 'restoration', 'resilience'. >Band 6: 'Mesmerizing', 'resilience'. Not Band 8: 'View' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'architecture, known for', 'view... which was'. >Band 6: Participles and relative clauses used correctly. Not Band 8: Lacks full variety.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Notre Dame Cathedral in Paris a few years ago. It is a masterpiece of Gothic architecture, known for its flying buttresses and gargoyles. The stained glass windows are mesmerizing, especially the Rose Window. I climbed the towers for a panoramic view of Paris, which was breathtaking. It was damaged by a fire recently, but restoration is underway. It remains a symbol of resilience and history for the French people. I felt a deep sense of peace inside the cathedral. It is a place that connects the past with the present.\n\nWord Count: 94 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'masterpiece', 'Gothic architecture', 'flying buttresses', 'gargoyles', 'mesmerizing', 'panoramic', 'restoration', 'resilience'. \n\n>Band 6: 'Mesmerizing', 'resilience'.\n\nNot Band 8: 'View' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'architecture, known for', 'view... which was'. \n\n>Band 6: Participles and relative clauses used correctly.\n\nNot Band 8: Lacks full variety.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_527",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I tried to assemble a computer from scratch. It was a daunting task because I had no prior experience. I had to research compatible parts and order them online. Connecting the wires was confusing and required patience. I was afraid of damaging the delicate components. It took me a whole weekend to finish. When I turned it on and it worked, I was ecstatic. It was a rewarding project that taught me a lot about technology. I felt a great sense of accomplishment.",
        "word_count": 87,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'from scratch', 'daunting', 'prior experience', 'compatible', 'delicate components', 'ecstatic', 'rewarding', 'accomplishment'. Band 7 level.",
             "grammar: 'task because I had', 'Connecting the wires was', 'turned it on and it worked'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'from scratch', 'daunting', 'compatible', 'components', 'ecstatic', 'rewarding', 'accomplishment'. >Band 6: 'Daunting', 'ecstatic'. Not Band 8: 'Technology' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'task because I had', 'Connecting... was confusing'. >Band 6: Gerund subjects and causal clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I tried to assemble a computer from scratch. It was a daunting task because I had no prior experience. I had to research compatible parts and order them online. Connecting the wires was confusing and required patience. I was afraid of damaging the delicate components. It took me a whole weekend to finish. When I turned it on and it worked, I was ecstatic. It was a rewarding project that taught me a lot about technology. I felt a great sense of accomplishment.\n\nWord Count: 87 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'from scratch', 'daunting', 'compatible', 'components', 'ecstatic', 'rewarding', 'accomplishment'. \n\n>Band 6: 'Daunting', 'ecstatic'.\n\nNot Band 8: 'Technology' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'task because I had', 'Connecting... was confusing'. \n\n>Band 6: Gerund subjects and causal clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_528",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read Life of Pi by Yann Martel. It is a philosophical adventure story about a boy stranded on a lifeboat with a tiger. It explores profound themes of survival and faith. The storytelling is magical and imaginative. The ending is ambiguous, leaving the reader to decide what is real. It makes you think deeply about the nature of truth. It is a thought-provoking novel that I would recommend. It is unlike any other book I have read.",
        "word_count": 80,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'philosophical', 'adventure', 'stranded', 'lifeboat', 'profound themes', 'survival', 'faith', 'storytelling', 'imaginative', 'ambiguous', 'thought-provoking'. Band 7 level.",
             "grammar: 'story about a boy', 'reader to decide', 'makes you think'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'philosophical', 'stranded', 'profound', 'storytelling', 'imaginative', 'ambiguous', 'thought-provoking'. >Band 6: 'Ambiguous', 'philosophical'. Not Band 8: 'Tiger' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'reader to decide', 'makes you think'. >Band 6: Infinitives and causative verbs used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read Life of Pi by Yann Martel. It is a philosophical adventure story about a boy stranded on a lifeboat with a tiger. It explores profound themes of survival and faith. The storytelling is magical and imaginative. The ending is ambiguous, leaving the reader to decide what is real. It makes you think deeply about the nature of truth. It is a thought-provoking novel that I would recommend. It is unlike any other book I have read.\n\nWord Count: 80 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'philosophical', 'stranded', 'profound', 'storytelling', 'imaginative', 'ambiguous', 'thought-provoking'. \n\n>Band 6: 'Ambiguous', 'philosophical'.\n\nNot Band 8: 'Tiger' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'reader to decide', 'makes you think'. \n\n>Band 6: Infinitives and causative verbs used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_529",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I went to a tea party for a baby shower. It was a lovely afternoon. We drank herbal tea and ate delicate pastries. We played silly games that made us laugh. The mother-to-be opened her gifts with joy. The atmosphere was joyful and supportive. We shared advice on parenting and life. It was a great opportunity to catch up with friends. I enjoyed the relaxed vibe.",
        "word_count": 68,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'herbal tea', 'delicate pastries', 'mother-to-be', 'atmosphere', 'joyful', 'supportive', 'parenting', 'catch up', 'vibe'. Band 7 level.",
             "grammar: 'games that made', 'opportunity to catch up'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'herbal tea', 'delicate', 'mother-to-be', 'supportive', 'parenting', 'catch up', 'vibe'. >Band 6: 'Joyful', 'pastries'. Not Band 8: 'Gifts' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'games that made', 'opportunity to catch up'. >Band 6: Relative clauses and infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I went to a tea party for a baby shower. It was a lovely afternoon. We drank herbal tea and ate delicate pastries. We played silly games that made us laugh. The mother-to-be opened her gifts with joy. The atmosphere was joyful and supportive. We shared advice on parenting and life. It was a great opportunity to catch up with friends. I enjoyed the relaxed vibe.\n\nWord Count: 68 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'herbal tea', 'delicate', 'mother-to-be', 'supportive', 'parenting', 'catch up', 'vibe'. \n\n>Band 6: 'Joyful', 'pastries'.\n\nNot Band 8: 'Gifts' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'games that made', 'opportunity to catch up'. \n\n>Band 6: Relative clauses and infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_530",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I use a sewing machine at home. It helps me repair clothes instead of throwing them away. I can also create new garments from fabric. It has different stitch patterns for various needs. I made curtains for my living room, which saved money. It is a practical skill to have. I enjoy sewing in my free time as it is relaxing. It allows me to be creative with fashion.",
        "word_count": 70,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'sewing machine', 'repair', 'garments', 'fabric', 'stitch patterns', 'curtains', 'alterations', 'practical skill', 'creative', 'fashion'. Band 7 level.",
             "grammar: 'instead of throwing', 'room, which saved', 'allows me to be'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'sewing machine', 'repair', 'garments', 'stitch patterns', 'practical skill', 'creative'. >Band 6: 'Garments', 'fabric'. Not Band 8: 'Money' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'instead of throwing', 'room, which saved'. >Band 6: Prepositional phrases and relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I use a sewing machine at home. It helps me repair clothes instead of throwing them away. I can also create new garments from fabric. It has different stitch patterns for various needs. I made curtains for my living room, which saved money. It is a practical skill to have. I enjoy sewing in my free time as it is relaxing. It allows me to be creative with fashion.\n\nWord Count: 70 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'sewing machine', 'repair', 'garments', 'stitch patterns', 'practical skill', 'creative'. \n\n>Band 6: 'Garments', 'fabric'.\n\nNot Band 8: 'Money' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'instead of throwing', 'room, which saved'. \n\n>Band 6: Prepositional phrases and relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_531",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I saw the Berlin Wall remains in Germany. It was a symbol of division during the Cold War. Now, only sections remain as a memorial. It is covered in graffiti art by artists from around the world. I visited the East Side Gallery, which is the longest surviving section. It was a poignant reminder of history and the struggle for freedom. I felt moved by the stories of separation. It represents hope and unity now.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'symbol', 'division', 'Cold War', 'memorial', 'graffiti art', 'East Side Gallery', 'poignant reminder', 'struggle', 'separation', 'unity'. Band 7 level.",
             "grammar: 'Gallery, which is', 'moved by the stories'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'symbol', 'division', 'memorial', 'graffiti', 'poignant reminder', 'struggle', 'separation', 'unity'. >Band 6: 'Poignant', 'division'. Not Band 8: 'History' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'Gallery, which is', 'moved by the stories'. >Band 6: Relative clauses and passive voice used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I saw the Berlin Wall remains in Germany. It was a symbol of division during the Cold War. Now, only sections remain as a memorial. It is covered in graffiti art by artists from around the world. I visited the East Side Gallery, which is the longest surviving section. It was a poignant reminder of history and the struggle for freedom. I felt moved by the stories of separation. It represents hope and unity now.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'symbol', 'division', 'memorial', 'graffiti', 'poignant reminder', 'struggle', 'separation', 'unity'. \n\n>Band 6: 'Poignant', 'division'.\n\nNot Band 8: 'History' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Gallery, which is', 'moved by the stories'. \n\n>Band 6: Relative clauses and passive voice used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_532",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I like the aloe vera plant for its medicinal properties. It has thick, fleshy leaves containing a soothing gel. I use it to treat sunburns and minor cuts. It is a succulent, so it needs very little water. I keep one in my kitchen for emergencies. It is easy to grow and propagate. It adds a touch of green to my home. I appreciate its utility and resilience.",
        "word_count": 68,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'medicinal properties', 'fleshy leaves', 'soothing gel', 'treat', 'succulent', 'emergencies', 'propagate', 'utility', 'resilience'. Band 7 level.",
             "grammar: 'leaves containing a', 'succulent, so it needs'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'medicinal', 'fleshy', 'soothing', 'succulent', 'propagate', 'utility', 'resilience'. >Band 6: 'Soothing', 'medicinal'. Not Band 8: 'Water' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'leaves containing a', 'succulent, so it needs'. >Band 6: Participle phrases and causal clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I like the aloe vera plant for its medicinal properties. It has thick, fleshy leaves containing a soothing gel. I use it to treat sunburns and minor cuts. It is a succulent, so it needs very little water. I keep one in my kitchen for emergencies. It is easy to grow and propagate. It adds a touch of green to my home. I appreciate its utility and resilience.\n\nWord Count: 68 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'medicinal', 'fleshy', 'soothing', 'succulent', 'propagate', 'utility', 'resilience'. \n\n>Band 6: 'Soothing', 'medicinal'.\n\nNot Band 8: 'Water' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'leaves containing a', 'succulent, so it needs'. \n\n>Band 6: Participle phrases and causal clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_533",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "My friend James is a talented musician. He plays the piano beautifully and composes his own songs. We often go to concerts together to enjoy live music. He has a deep appreciation for classical and jazz genres. He inspires me to be creative in my own life. He is a soulful and thoughtful person. I admire his dedication to his craft. He practices for hours every day. He is a true artist.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'talented', 'musician', 'composes', 'appreciation', 'genres', 'inspires', 'creative', 'soulful', 'thoughtful', 'dedication', 'craft'. Band 7 level.",
             "grammar: 'inspires me to be', 'dedication to his'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'musician', 'composes', 'appreciation', 'genres', 'inspires', 'soulful', 'dedication', 'craft'. >Band 6: 'Composes', 'appreciation'. Not Band 8: 'Piano' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'inspires me to be', 'dedication to his'. >Band 6: Infinitives and prepositions used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a friend.\n\nTranscript: My friend James is a talented musician. He plays the piano beautifully and composes his own songs. We often go to concerts together to enjoy live music. He has a deep appreciation for classical and jazz genres. He inspires me to be creative in my own life. He is a soulful and thoughtful person. I admire his dedication to his craft. He practices for hours every day. He is a true artist.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'musician', 'composes', 'appreciation', 'genres', 'inspires', 'soulful', 'dedication', 'craft'. \n\n>Band 6: 'Composes', 'appreciation'.\n\nNot Band 8: 'Piano' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'inspires me to be', 'dedication to his'. \n\n>Band 6: Infinitives and prepositions used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_534",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I decided to adopt a healthier lifestyle, which was a tough choice. I gave up junk food and sugary drinks. I started exercising regularly at the gym. It was hard to resist cravings at first. I felt withdrawal symptoms and wanted to quit. However, I persevered and stayed focused on my goal. I lost weight and gained energy. It was the best decision for my well-being. I feel like a new person now.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'healthier lifestyle', 'gave up', 'sugary', 'resist', 'cravings', 'withdrawal symptoms', 'persevered', 'focused', 'well-being'. Band 7 level.",
             "grammar: 'lifestyle, which was', 'hard to resist', 'felt... and wanted'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'healthier lifestyle', 'gave up', 'resist', 'cravings', 'withdrawal symptoms', 'persevered', 'well-being'. >Band 6: 'Persevered', 'withdrawal'. Not Band 8: 'Gym' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'lifestyle, which was', 'hard to resist'. >Band 6: Relative clauses and infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I decided to adopt a healthier lifestyle, which was a tough choice. I gave up junk food and sugary drinks. I started exercising regularly at the gym. It was hard to resist cravings at first. I felt withdrawal symptoms and wanted to quit. However, I persevered and stayed focused on my goal. I lost weight and gained energy. It was the best decision for my well-being. I feel like a new person now.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'healthier lifestyle', 'gave up', 'resist', 'cravings', 'withdrawal symptoms', 'persevered', 'well-being'. \n\n>Band 6: 'Persevered', 'withdrawal'.\n\nNot Band 8: 'Gym' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'lifestyle, which was', 'hard to resist'. \n\n>Band 6: Relative clauses and infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_535",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I participated in a debate tournament about politics. I had to research arguments and evidence. I debated against strong opponents who were very skilled. I had to think on my feet and respond quickly. I won the debate and felt very proud. It improved my critical thinking skills significantly. It was an intellectually stimulating experience. I plan to join more debates in the future.",
        "word_count": 64,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'debate tournament', 'politics', 'arguments', 'evidence', 'opponents', 'skilled', 'think on my feet', 'critical thinking', 'intellectually stimulating'. Band 7 level.",
             "grammar: 'opponents who were', 'think on my feet'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'debate tournament', 'arguments', 'evidence', 'opponents', 'think on my feet', 'critical thinking', 'stimulating'. >Band 6: 'Stimulating', 'opponents'. Not Band 8: 'Politics' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'opponents who were', 'think on my feet'. >Band 6: Relative clauses and idioms used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I participated in a debate tournament about politics. I had to research arguments and evidence. I debated against strong opponents who were very skilled. I had to think on my feet and respond quickly. I won the debate and felt very proud. It improved my critical thinking skills significantly. It was an intellectually stimulating experience. I plan to join more debates in the future.\n\nWord Count: 64 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'debate tournament', 'arguments', 'evidence', 'opponents', 'think on my feet', 'critical thinking', 'stimulating'. \n\n>Band 6: 'Stimulating', 'opponents'.\n\nNot Band 8: 'Politics' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'opponents who were', 'think on my feet'. \n\n>Band 6: Relative clauses and idioms used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_536",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Machu Picchu ruins in Peru. It is an Incan citadel located high in the Andes mountains. The views are spectacular and breathtaking. The stone masonry is precise and durable. I hiked the Inca Trail to get there, which was challenging. It is a mystical place shrouded in clouds. It felt like stepping back in time. I was amazed by the engineering of the Incas. It is a world wonder.",
        "word_count": 72,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'ruins', 'Incan citadel', 'Andes', 'spectacular', 'breathtaking', 'stone masonry', 'precise', 'durable', 'mystical', 'shrouded', 'engineering'. Band 7 level.",
             "grammar: 'citadel located high', 'Trail... which was', 'shrouded in clouds'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'ruins', 'citadel', 'spectacular', 'masonry', 'precise', 'durable', 'mystical', 'shrouded', 'engineering'. >Band 6: 'Citadel', 'shrouded'. Not Band 8: 'Views' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'citadel located high', 'shrouded in clouds'. >Band 6: Participles and relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Machu Picchu ruins in Peru. It is an Incan citadel located high in the Andes mountains. The views are spectacular and breathtaking. The stone masonry is precise and durable. I hiked the Inca Trail to get there, which was challenging. It is a mystical place shrouded in clouds. It felt like stepping back in time. I was amazed by the engineering of the Incas. It is a world wonder.\n\nWord Count: 72 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'ruins', 'citadel', 'spectacular', 'masonry', 'precise', 'durable', 'mystical', 'shrouded', 'engineering'. \n\n>Band 6: 'Citadel', 'shrouded'.\n\nNot Band 8: 'Views' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'citadel located high', 'shrouded in clouds'. \n\n>Band 6: Participles and relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_537",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I built a dog house for my pet. I used wood and nails to construct it. I measured the pieces carefully to ensure they fit. Cutting the wood was hard work and tiring. I hammered the nails in with precision. I painted it blue to match my house. My dog loves it and sleeps there every night. It keeps him warm and dry during storms. I felt handy and capable after finishing it.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'construct', 'measured', 'ensure', 'precision', 'handy', 'capable'. Band 7 level.",
             "grammar: 'nails to construct', 'Cutting the wood was', 'painted it... to match'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'construct', 'measured', 'ensure', 'precision', 'handy', 'capable'. >Band 6: 'Handy', 'measured'. Not Band 8: 'Wood' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'nails to construct', 'Cutting the wood'. >Band 6: Infinitives and gerund subjects used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I built a dog house for my pet. I used wood and nails to construct it. I measured the pieces carefully to ensure they fit. Cutting the wood was hard work and tiring. I hammered the nails in with precision. I painted it blue to match my house. My dog loves it and sleeps there every night. It keeps him warm and dry during storms. I felt handy and capable after finishing it.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'construct', 'measured', 'ensure', 'precision', 'handy', 'capable'. \n\n>Band 6: 'Handy', 'measured'.\n\nNot Band 8: 'Wood' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'nails to construct', 'Cutting the wood'. \n\n>Band 6: Infinitives and gerund subjects used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_538",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read The Alchemist by Paulo Coelho. It is a story about a shepherd boy who travels to find treasure. He learns about his personal legend and destiny. The book is inspiring and spiritual. It teaches you to follow your dreams and listen to your heart. The writing is simple but profound. It is a spiritual journey that many people relate to. I enjoyed reading it.",
        "word_count": 66,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'shepherd boy', 'treasure', 'personal legend', 'destiny', 'inspiring', 'spiritual', 'profound', 'relate to'. Band 7 level.",
             "grammar: 'story about a shepherd', 'travels to find', 'teaches you to follow'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'shepherd boy', 'treasure', 'personal legend', 'destiny', 'inspiring', 'profound', 'spiritual'. >Band 6: 'Profound', 'legend'. Not Band 8: 'Dreams' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'travels to find', 'teaches you to follow'. >Band 6: Infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read The Alchemist by Paulo Coelho. It is a story about a shepherd boy who travels to find treasure. He learns about his personal legend and destiny. The book is inspiring and spiritual. It teaches you to follow your dreams and listen to your heart. The writing is simple but profound. It is a spiritual journey that many people relate to. I enjoyed reading it.\n\nWord Count: 66 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'shepherd boy', 'treasure', 'personal legend', 'destiny', 'inspiring', 'profound', 'spiritual'. \n\n>Band 6: 'Profound', 'legend'.\n\nNot Band 8: 'Dreams' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'travels to find', 'teaches you to follow'. \n\n>Band 6: Infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
