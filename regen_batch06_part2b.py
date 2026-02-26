import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch06.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v7_g7_488",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read The Kite Runner by Khaled Hosseini. It is a heartbreaking story about friendship and redemption set in Afghanistan. The vivid descriptions of Kabul before the war are nostalgic. The protagonist, Amir, struggles with guilt over a childhood betrayal. The plot twists are shocking and emotional. It explores themes of loyalty, forgiveness, and the father-son relationship. The writing is powerful and evocative, drawing the reader in. It brought me to tears several times. It is a book that stays with you long after you finish it.",
        "word_count": 91,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'heartbreaking', 'redemption', 'vivid descriptions', 'nostalgic', 'protagonist', 'struggles', 'guilt', 'betrayal', 'plot twists', 'shocking', 'loyalty', 'evocative'. Band 7 level.",
             "grammar: 'story about friendship', 'before the war are', 'drawing the reader in'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'heartbreaking', 'redemption', 'vivid', 'nostalgic', 'protagonist', 'guilt', 'betrayal', 'plot twists', 'evocative'. >Band 6: 'Palpable', 'redemption'. Not Band 8: 'Tears' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'story about friendship', 'drawing the reader in'. >Band 6: Participle phrases and prepositions used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read The Kite Runner by Khaled Hosseini. It is a heartbreaking story about friendship and redemption set in Afghanistan. The vivid descriptions of Kabul before the war are nostalgic. The protagonist, Amir, struggles with guilt over a childhood betrayal. The plot twists are shocking and emotional. It explores themes of loyalty, forgiveness, and the father-son relationship. The writing is powerful and evocative, drawing the reader in. It brought me to tears several times. It is a book that stays with you long after you finish it.\n\nWord Count: 91 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'heartbreaking', 'redemption', 'vivid', 'nostalgic', 'protagonist', 'guilt', 'betrayal', 'plot twists', 'evocative'. \n\n>Band 6: 'Palpable', 'redemption'.\n\nNot Band 8: 'Tears' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'story about friendship', 'drawing the reader in'. \n\n>Band 6: Participle phrases and prepositions used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_489",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I went to a surprise birthday party for my best friend. We hid in the dark until she arrived, building up the suspense. We yelled surprise when she walked in, and she was genuinely shocked. We ate a delicious chocolate cake and ice cream. We danced to her favorite songs all night long. It was a joyous celebration of her life. We made great memories that we will cherish forever. Seeing her so happy made all the planning worthwhile. It was a fantastic evening.",
        "word_count": 87,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'surprise', 'suspense', 'genuinely', 'shocked', 'delicious', 'joyous celebration', 'cherish', 'worthwhile', 'fantastic'. Band 7 level.",
             "grammar: 'hid in the dark until', 'building up the suspense', 'Seeing her so happy'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'suspense', 'genuinely', 'shocked', 'joyous celebration', 'cherish', 'worthwhile'. >Band 6: 'Genuinely', 'joyous'. Not Band 8: 'Cake' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'building up the suspense', 'Seeing her so happy'. >Band 6: Participles and gerund subjects used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I went to a surprise birthday party for my best friend. We hid in the dark until she arrived, building up the suspense. We yelled surprise when she walked in, and she was genuinely shocked. We ate a delicious chocolate cake and ice cream. We danced to her favorite songs all night long. It was a joyous celebration of her life. We made great memories that we will cherish forever. Seeing her so happy made all the planning worthwhile. It was a fantastic evening.\n\nWord Count: 87 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'suspense', 'genuinely', 'shocked', 'joyous celebration', 'cherish', 'worthwhile'. \n\n>Band 6: 'Genuinely', 'joyous'.\n\nNot Band 8: 'Cake' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'building up the suspense', 'Seeing her so happy'. \n\n>Band 6: Participles and gerund subjects used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_490",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I bought a power bank recently. It is a portable charger for my phone that fits in my pocket. It is a lifesaver when I am traveling and cannot find a plug. I do not have to worry about a dead battery anymore. It charges my devices quickly and efficiently. It is compact and lightweight, making it easy to carry. It gives me peace of mind knowing I can always stay connected. It is an essential gadget for modern life.",
        "word_count": 83,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'power bank', 'portable charger', 'lifesaver', 'dead battery', 'charges', 'efficiently', 'compact', 'lightweight', 'peace of mind', 'essential gadget'. Band 7 level.",
             "grammar: 'charger... that fits', 'lifesaver when I am', 'knowing I can always'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'power bank', 'portable charger', 'lifesaver', 'efficiently', 'compact', 'peace of mind', 'gadget'. >Band 6: 'Lifesaver', 'efficiently'. Not Band 8: 'Phone' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'charger... that fits', 'knowing I can always'. >Band 6: Relative clauses and participles used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I bought a power bank recently. It is a portable charger for my phone that fits in my pocket. It is a lifesaver when I am traveling and cannot find a plug. I do not have to worry about a dead battery anymore. It charges my devices quickly and efficiently. It is compact and lightweight, making it easy to carry. It gives me peace of mind knowing I can always stay connected. It is an essential gadget for modern life.\n\nWord Count: 83 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'power bank', 'portable charger', 'lifesaver', 'efficiently', 'compact', 'peace of mind', 'gadget'. \n\n>Band 6: 'Lifesaver', 'efficiently'.\n\nNot Band 8: 'Phone' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'charger... that fits', 'knowing I can always'. \n\n>Band 6: Relative clauses and participles used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_491",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I saw the Great Wall of China, which is an engineering marvel. It winds through the mountains like a giant dragon. I walked along the ancient stones, feeling the history beneath my feet. The view was breathtaking, stretching for miles. It was built to protect the empire from invaders centuries ago. It is a symbol of strength and perseverance of the Chinese people. It was an unforgettable experience to stand on such a monumental structure. I would recommend visiting it to anyone.",
        "word_count": 83,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'engineering marvel', 'winds', 'ancient stones', 'breathtaking', 'stretching', 'protect', 'invaders', 'symbol', 'strength', 'perseverance', 'monumental'. Band 7 level.",
             "grammar: 'China, which is', 'winds... like a', 'feeling the history'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'engineering marvel', 'winds', 'ancient', 'breathtaking', 'invaders', 'symbol', 'perseverance', 'monumental'. >Band 6: 'Marvel', 'perseverance'. Not Band 8: 'View' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'China, which is', 'feeling the history'. >Band 6: Relative clauses and participles used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I saw the Great Wall of China, which is an engineering marvel. It winds through the mountains like a giant dragon. I walked along the ancient stones, feeling the history beneath my feet. The view was breathtaking, stretching for miles. It was built to protect the empire from invaders centuries ago. It is a symbol of strength and perseverance of the Chinese people. It was an unforgettable experience to stand on such a monumental structure. I would recommend visiting it to anyone.\n\nWord Count: 83 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'engineering marvel', 'winds', 'ancient', 'breathtaking', 'invaders', 'symbol', 'perseverance', 'monumental'. \n\n>Band 6: 'Marvel', 'perseverance'.\n\nNot Band 8: 'View' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'China, which is', 'feeling the history'. \n\n>Band 6: Relative clauses and participles used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_492",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I planted a rose bush in my garden last spring. The flowers are deep red and velvety to the touch. They have a sweet fragrance that fills the air. I have to prune them regularly to encourage growth. The thorns are sharp, so I must be careful. It blooms beautifully in the summer. It adds a touch of romance and elegance to my garden. I love cutting them for vases to decorate my house. It requires effort but is worth it.",
        "word_count": 84,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'rose bush', 'velvety', 'fragrance', 'prune', 'encourage growth', 'thorns', 'blooms', 'romance', 'elegance', 'decorate'. Band 7 level.",
             "grammar: 'fragrance that fills', 'prune them... to encourage', 'thorns are sharp, so'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'velvety', 'fragrance', 'prune', 'encourage', 'blooms', 'romance', 'elegance'. >Band 6: 'Velvety', 'prune'. Not Band 8: 'Sweet' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'fragrance that fills', 'prune them... to encourage'. >Band 6: Relative clauses and infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I planted a rose bush in my garden last spring. The flowers are deep red and velvety to the touch. They have a sweet fragrance that fills the air. I have to prune them regularly to encourage growth. The thorns are sharp, so I must be careful. It blooms beautifully in the summer. It adds a touch of romance and elegance to my garden. I love cutting them for vases to decorate my house. It requires effort but is worth it.\n\nWord Count: 84 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'velvety', 'fragrance', 'prune', 'encourage', 'blooms', 'romance', 'elegance'. \n\n>Band 6: 'Velvety', 'prune'.\n\nNot Band 8: 'Sweet' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'fragrance that fills', 'prune them... to encourage'. \n\n>Band 6: Relative clauses and infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_493",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "My friend Ben is a stand-up comedian. He has a great sense of humor and makes everyone laugh. He is quick-witted and observant about daily life. We often go to comedy clubs together to watch shows. He helps me see the lighter side of life when I am stressed. His jokes are hilarious and clever. He is a joy to be around because of his positive energy. He is working hard to become famous. I admire his courage to perform on stage.",
        "word_count": 84,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'stand-up comedian', 'sense of humor', 'quick-witted', 'observant', 'lighter side', 'hilarious', 'clever', 'joy', 'positive energy', 'courage'. Band 7 level.",
             "grammar: 'makes everyone laugh', 'go... to watch', 'joy to be around'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'stand-up comedian', 'quick-witted', 'observant', 'lighter side', 'hilarious', 'clever', 'joy'. >Band 6: 'Quick-witted', 'hilarious'. Not Band 8: 'Laugh' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'makes everyone laugh', 'joy to be around'. >Band 6: Causative and infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a friend.\n\nTranscript: My friend Ben is a stand-up comedian. He has a great sense of humor and makes everyone laugh. He is quick-witted and observant about daily life. We often go to comedy clubs together to watch shows. He helps me see the lighter side of life when I am stressed. His jokes are hilarious and clever. He is a joy to be around because of his positive energy. He is working hard to become famous. I admire his courage to perform on stage.\n\nWord Count: 84 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'stand-up comedian', 'quick-witted', 'observant', 'lighter side', 'hilarious', 'clever', 'joy'. \n\n>Band 6: 'Quick-witted', 'hilarious'.\n\nNot Band 8: 'Laugh' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'makes everyone laugh', 'joy to be around'. \n\n>Band 6: Causative and infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_494",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I decided to learn to drive last year, which was a big decision. I was terrified of crashing and hurting someone. I took lessons from a professional instructor to be safe. Parallel parking was a nightmare for me. I failed my first driving test, which was discouraging. However, I tried again and finally passed. It gave me freedom and independence to travel. Overcoming my fear was a huge achievement. Now I enjoy driving on the open road.",
        "word_count": 79,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'terrified', 'crashing', 'professional instructor', 'parallel parking', 'nightmare', 'discouraging', 'freedom', 'independence', 'overcoming', 'achievement'. Band 7 level.",
             "grammar: 'year, which was', 'terrified of crashing', 'failed... which was'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'terrified', 'crashing', 'parallel parking', 'nightmare', 'discouraging', 'freedom', 'independence', 'overcoming'. >Band 6: 'Discouraged', 'nightmare'. Not Band 8: 'Lessons' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'year, which was', 'terrified of crashing'. >Band 6: Relative clauses and gerunds used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I decided to learn to drive last year, which was a big decision. I was terrified of crashing and hurting someone. I took lessons from a professional instructor to be safe. Parallel parking was a nightmare for me. I failed my first driving test, which was discouraging. However, I tried again and finally passed. It gave me freedom and independence to travel. Overcoming my fear was a huge achievement. Now I enjoy driving on the open road.\n\nWord Count: 79 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'terrified', 'crashing', 'parallel parking', 'nightmare', 'discouraging', 'freedom', 'independence', 'overcoming'. \n\n>Band 6: 'Discouraged', 'nightmare'.\n\nNot Band 8: 'Lessons' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'year, which was', 'terrified of crashing'. \n\n>Band 6: Relative clauses and gerunds used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_495",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I played in a tennis tournament representing my club. The matches were intense and physically demanding. I had to stay focused on every point. My opponent was skilled and aggressive. We had long rallies that tested my stamina. I won the final match in a tiebreaker, which was thrilling. I felt a great sense of accomplishment and pride. My teammates cheered for me loudly. It was a memorable victory that motivated me to train harder.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'tennis tournament', 'intense', 'demanding', 'focused', 'opponent', 'skilled', 'aggressive', 'rallies', 'stamina', 'tiebreaker', 'thrilling', 'accomplishment'. Band 7 level.",
             "grammar: 'matches were intense', 'tiebreaker, which was', 'victory that motivated'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'tournament', 'intense', 'demanding', 'focused', 'opponent', 'skilled', 'aggressive', 'rallies', 'stamina', 'tiebreaker', 'thrilling', 'accomplishment'. >Band 6: 'Rallies', 'thrilling'. Not Band 8: 'Matches' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'tiebreaker, which was', 'victory that motivated'. >Band 6: Relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I played in a tennis tournament representing my club. The matches were intense and physically demanding. I had to stay focused on every point. My opponent was skilled and aggressive. We had long rallies that tested my stamina. I won the final match in a tiebreaker, which was thrilling. I felt a great sense of accomplishment and pride. My teammates cheered for me loudly. It was a memorable victory that motivated me to train harder.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'tournament', 'intense', 'demanding', 'focused', 'opponent', 'skilled', 'aggressive', 'rallies', 'stamina', 'tiebreaker', 'thrilling', 'accomplishment'. \n\n>Band 6: 'Rallies', 'thrilling'.\n\nNot Band 8: 'Matches' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'tiebreaker, which was', 'victory that motivated'. \n\n>Band 6: Relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_496",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Pantheon in Rome, which is an ancient temple. It is famous for its massive dome with a hole in the center, called an oculus. The engineering is remarkable for its time and still stands strong. It is one of the best-preserved buildings from ancient Rome. I felt small standing inside under the giant dome. The light coming through the oculus was beautiful. It is a masterpiece of design and construction. I was in awe of its history.",
        "word_count": 82,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'ancient temple', 'massive dome', 'oculus', 'engineering', 'remarkable', 'well-preserved', 'masterpiece', 'construction', 'awe'. Band 7 level.",
             "grammar: 'Rome, which is', 'center, called an', 'light coming through'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'ancient', 'temple', 'dome', 'massive', 'oculus', 'engineering', 'remarkable', 'well-preserved', 'masterpiece', 'awe'. >Band 6: 'Oculus', 'remarkable'. Not Band 8: 'Hole' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'Rome, which is', 'light coming through'. >Band 6: Relative clauses and participles used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Pantheon in Rome, which is an ancient temple. It is famous for its massive dome with a hole in the center, called an oculus. The engineering is remarkable for its time and still stands strong. It is one of the best-preserved buildings from ancient Rome. I felt small standing inside under the giant dome. The light coming through the oculus was beautiful. It is a masterpiece of design and construction. I was in awe of its history.\n\nWord Count: 82 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'ancient', 'temple', 'dome', 'massive', 'oculus', 'engineering', 'remarkable', 'well-preserved', 'masterpiece', 'awe'. \n\n>Band 6: 'Oculus', 'remarkable'.\n\nNot Band 8: 'Hole' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Rome, which is', 'light coming through'. \n\n>Band 6: Relative clauses and participles used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_497",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I had to plan a wedding for my sister. It was a stressful but rewarding task. I had to coordinate with the venue and caterers to ensure everything was perfect. The guest list was long, and seating arrangements were tricky. There were budget constraints that I had to manage carefully. I made a detailed checklist to stay organized. Everything went smoothly on the day, which was a relief. It was a beautiful celebration of love. I felt proud of my contribution.",
        "word_count": 83,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'stressful', 'rewarding', 'coordinate', 'venue', 'caterers', 'arrangements', 'tricky', 'budget constraints', 'checklist', 'organized', 'smoothly', 'relief', 'contribution'. Band 7 level.",
             "grammar: 'caterers to ensure', 'constraints that I had', 'day, which was'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'stressful', 'rewarding', 'coordinate', 'venue', 'caterers', 'arrangements', 'tricky', 'budget constraints', 'checklist', 'contribution'. >Band 6: 'Constraints', 'coordinate'. Not Band 8: 'Wedding' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'caterers to ensure', 'constraints that I had', 'day, which was'. >Band 6: Infinitives and relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I had to plan a wedding for my sister. It was a stressful but rewarding task. I had to coordinate with the venue and caterers to ensure everything was perfect. The guest list was long, and seating arrangements were tricky. There were budget constraints that I had to manage carefully. I made a detailed checklist to stay organized. Everything went smoothly on the day, which was a relief. It was a beautiful celebration of love. I felt proud of my contribution.\n\nWord Count: 83 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'stressful', 'rewarding', 'coordinate', 'venue', 'caterers', 'arrangements', 'tricky', 'budget constraints', 'checklist', 'contribution'. \n\n>Band 6: 'Constraints', 'coordinate'.\n\nNot Band 8: 'Wedding' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'caterers to ensure', 'constraints that I had', 'day, which was'. \n\n>Band 6: Infinitives and relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_498",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read Harry Potter, which is a magical story about a young wizard. The characters are relatable and grow throughout the series. I loved the vivid descriptions of Hogwarts school. It explores deep themes of friendship, bravery, and love. The plot is engaging and full of twists. I couldn't put it down once I started reading. It sparked my imagination and love for reading. It is a book that appeals to all ages. I highly recommend it.",
        "word_count": 79,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'magical', 'wizard', 'relatable', 'vivid descriptions', 'themes', 'bravery', 'engaging', 'twists', 'sparked', 'imagination', 'appeals'. Band 7 level.",
             "grammar: 'Potter, which is', 'put it down once'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'magical', 'wizard', 'relatable', 'vivid', 'themes', 'bravery', 'engaging', 'twists', 'sparked', 'imagination', 'appeals'. >Band 6: 'Relatable', 'engaging'. Not Band 8: 'Story' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'Potter, which is', 'put it down once'. >Band 6: Relative clauses and time clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read Harry Potter, which is a magical story about a young wizard. The characters are relatable and grow throughout the series. I loved the vivid descriptions of Hogwarts school. It explores deep themes of friendship, bravery, and love. The plot is engaging and full of twists. I couldn't put it down once I started reading. It sparked my imagination and love for reading. It is a book that appeals to all ages. I highly recommend it.\n\nWord Count: 79 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'magical', 'wizard', 'relatable', 'vivid', 'themes', 'bravery', 'engaging', 'twists', 'sparked', 'imagination', 'appeals'. \n\n>Band 6: 'Relatable', 'engaging'.\n\nNot Band 8: 'Story' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Potter, which is', 'put it down once'. \n\n>Band 6: Relative clauses and time clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_499",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I went to a dinner party at my colleague's house. The host cooked a delicious three-course meal for us. We sat around a large table and enjoyed the food. The conversation was lively and interesting, covering many topics. We discussed politics, travel, and movies. We laughed a lot and shared stories. It was a sophisticated and elegant evening. I enjoyed meeting new people and making connections. It was a memorable night of good food and company.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'host', 'delicious', 'three-course meal', 'lively', 'topics', 'politics', 'sophisticated', 'elegant', 'connections', 'memorable'. Band 7 level.",
             "grammar: 'sat around a', 'enjoyed meeting new'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'host', 'delicious', 'three-course meal', 'lively', 'politics', 'sophisticated', 'elegant', 'connections', 'memorable'. >Band 6: 'Sophisticated', 'lively'. Not Band 8: 'Food' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'sat around a', 'enjoyed meeting new'. >Band 6: Prepositional phrases and gerunds used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I went to a dinner party at my colleague's house. The host cooked a delicious three-course meal for us. We sat around a large table and enjoyed the food. The conversation was lively and interesting, covering many topics. We discussed politics, travel, and movies. We laughed a lot and shared stories. It was a sophisticated and elegant evening. I enjoyed meeting new people and making connections. It was a memorable night of good food and company.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'host', 'delicious', 'three-course meal', 'lively', 'politics', 'sophisticated', 'elegant', 'connections', 'memorable'. \n\n>Band 6: 'Sophisticated', 'lively'.\n\nNot Band 8: 'Food' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'sat around a', 'enjoyed meeting new'. \n\n>Band 6: Prepositional phrases and gerunds used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_500",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I use a reusable water bottle made of stainless steel. It keeps my water cold for 24 hours, which is amazing. It is eco-friendly because it reduces plastic waste. I carry it everywhere in my bag. It saves me money since I don't buy bottled water anymore. It is durable and easy to clean. Using it makes me feel like I am doing my part for the environment. It is a small change with a big impact.",
        "word_count": 80,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'reusable', 'stainless steel', 'eco-friendly', 'reduces', 'plastic waste', 'durable', 'environment', 'impact'. Band 7 level.",
             "grammar: 'hours, which is', 'because it reduces', 'since I don't'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'reusable', 'stainless steel', 'eco-friendly', 'reduces', 'plastic waste', 'durable', 'environment', 'impact'. >Band 6: 'Eco-friendly', 'impact'. Not Band 8: 'Cold' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'hours, which is', 'because it reduces', 'since I don't'. >Band 6: Relative and causal clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I use a reusable water bottle made of stainless steel. It keeps my water cold for 24 hours, which is amazing. It is eco-friendly because it reduces plastic waste. I carry it everywhere in my bag. It saves me money since I don't buy bottled water anymore. It is durable and easy to clean. Using it makes me feel like I am doing my part for the environment. It is a small change with a big impact.\n\nWord Count: 80 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'reusable', 'stainless steel', 'eco-friendly', 'reduces', 'plastic waste', 'durable', 'environment', 'impact'. \n\n>Band 6: 'Eco-friendly', 'impact'.\n\nNot Band 8: 'Cold' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'hours, which is', 'because it reduces', 'since I don't'. \n\n>Band 6: Relative and causal clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
