import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch01.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v4_g5_039",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a creative person you know.",
        "transcript_cleaned": "I know a creative person. His name is Tom. He is my friend from school. He likes to draw pictures. He draws animals and trees. They look very real. I cannot draw like him. He also makes things with paper. It is called origami. He made a paper bird for me. It was beautiful. He wants to be an artist in the future. I think he is very good. He has a lot of ideas in his head. He is the most creative person I know.",
        "word_count": 87,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'He likes to draw' (Correct)",
            "grammar: 'They look very real' (Correct linking verb + adj)",
            "grammar: 'I cannot draw like him' (Correct modal)",
            "grammar: 'He wants to be' (Correct)",
            "vocab: 'creative', 'draw', 'pictures', 'animals', 'paper', 'artist', 'ideas'. Band 4 level.",
            "repetitive: 'He is', 'He draws'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'creative', 'draw', 'pictures', 'paper', 'artist', 'ideas'. >Band 3: Topic words. Not Band 5: 'Look very real', 'very good'. Basic.",
        "grammar_reason": "[GRA5] Key evidence: Accurate simple sentences. 'He wants to be', 'I think he is'. >Band 4: Frequent error-free sentences. Not Band 6: Simple range.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a creative person you know.\n\nTranscript: I know a creative person. His name is Tom. He is my friend from school. He likes to draw pictures. He draws animals and trees. They look very real. I cannot draw like him. He also makes things with paper. It is called origami. He made a paper bird for me. It was beautiful. He wants to be an artist in the future. I think he is very good. He has a lot of ideas in his head. He is the most creative person I know.\n\nWord Count: 87 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'creative', 'draw', 'pictures', 'paper', 'artist', 'ideas'. \n\n>Band 3: Topic words.\n\nNot Band 5: 'Look very real', 'very good'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate simple sentences. 'He wants to be', 'I think he is'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Simple range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_040",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a crowded place you visited.",
        "transcript_cleaned": "I went to a concert last year. It was in a big stadium. There were many people. Maybe thousands. It was very crowded. I could not move easily. Everyone was standing and singing. The music was loud. I lost my friend for ten minutes. I was scared. But I found him later. Although it was crowded, I liked it. The atmosphere was exciting. People were happy. But after the concert, my legs were tired because I stood for a long time.",
        "word_count": 83,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'There were many people' (Correct)",
            "grammar: 'I could not move' (Correct)",
            "grammar: 'Although it was crowded, I liked it' (Correct use of 'Although' - complex structure)",
            "grammar: 'because I stood' (Correct 'because')",
            "vocab: 'concert', 'stadium', 'crowded', 'move', 'singing', 'loud', 'scared', 'tired'. Band 4 level.",
            "repetitive: 'was', 'crowded'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'concert', 'stadium', 'crowded', 'singing', 'loud', 'scared', 'tired'. >Band 3: Topic words. Not Band 5: 'Big stadium', 'happy'. Basic.",
        "grammar_reason": "[GRA5] Key evidence: Use of 'Although' and 'because' correctly. 'I could not move'. >Band 4: Complex sentences attempted successfully. Not Band 6: Limited flexibility.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a crowded place you visited.\n\nTranscript: I went to a concert last year. It was in a big stadium. There were many people. Maybe thousands. It was very crowded. I could not move easily. Everyone was standing and singing. The music was loud. I lost my friend for ten minutes. I was scared. But I found him later. Although it was crowded, I liked it. The atmosphere was exciting. People were happy. But after the concert, my legs were tired because I stood for a long time.\n\nWord Count: 83 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'concert', 'stadium', 'crowded', 'singing', 'loud', 'scared', 'tired'. \n\n>Band 3: Topic words.\n\nNot Band 5: 'Big stadium', 'happy'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Use of 'Although' and 'because' correctly. 'I could not move'. \n\n>Band 4: Complex sentences attempted successfully.\n\nNot Band 6: Limited flexibility.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_041",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a science subject you liked or disliked at school.",
        "transcript_cleaned": "I liked biology at school. It is about living things. I learned about animals and plants. It was interesting to know how they live. My teacher was good. He showed us pictures. Sometimes we went to the garden to see insects. I liked it because I like nature. But I did not like chemistry. It was difficult. I did not understand it. Biology was easier for me. I got good marks in biology exams.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'It is about living things' (Correct)",
            "grammar: 'It was interesting to know' (Correct adjective + infinitive)",
            "grammar: 'I liked it because I like nature' (Correct)",
            "grammar: 'I did not like chemistry' (Correct negative)",
            "vocab: 'biology', 'living things', 'animals', 'plants', 'insects', 'nature', 'chemistry', 'marks'. Band 4 level.",
            "repetitive: 'liked', 'interesting'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'biology', 'animals', 'plants', 'insects', 'chemistry', 'marks'. >Band 3: School subjects. Not Band 5: 'Good marks', 'difficult'. Basic adjectives.",
        "grammar_reason": "[GRA5] Key evidence: Accurate simple sentences. 'It was interesting to know'. >Band 4: Frequent error-free sentences. Not Band 6: Simple structures.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a science subject you liked or disliked at school.\n\nTranscript: I liked biology at school. It is about living things. I learned about animals and plants. It was interesting to know how they live. My teacher was good. He showed us pictures. Sometimes we went to the garden to see insects. I liked it because I like nature. But I did not like chemistry. It was difficult. I did not understand it. Biology was easier for me. I got good marks in biology exams.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'biology', 'animals', 'plants', 'insects', 'chemistry', 'marks'. \n\n>Band 3: School subjects.\n\nNot Band 5: 'Good marks', 'difficult'. Basic adjectives.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate simple sentences. 'It was interesting to know'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Simple structures.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_042",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a cafe you like to visit.",
        "transcript_cleaned": "I like a small cafe near my office. It is called The Coffee House. I go there every morning. I drink black coffee. It gives me energy. The cafe is quiet. I can read news on my phone there. The chairs are soft. I feel relaxed. The people working there are friendly. They know my name. Sometimes I meet my friend there. We talk for a short time. It is a nice place to start the day. I like the smell of coffee there.",
        "word_count": 85,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'It gives me energy' (Correct)",
            "grammar: 'I can read' (Correct)",
            "grammar: 'The people working there' (Correct participle phrase)",
            "vocab: 'cafe', 'office', 'coffee', 'energy', 'quiet', 'news', 'soft', 'relaxed', 'friendly', 'smell'. Band 4 level.",
            "repetitive: 'there', 'coffee'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'cafe', 'office', 'coffee', 'energy', 'soft', 'relaxed', 'smell'. >Band 3: Place words. Not Band 5: 'Nice place', 'friendly'. Basic.",
        "grammar_reason": "[GRA5] Key evidence: Accurate sentences. 'People working there', 'It gives me'. >Band 4: Frequent error-free sentences. Not Band 6: Simple range.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a cafe you like to visit.\n\nTranscript: I like a small cafe near my office. It is called The Coffee House. I go there every morning. I drink black coffee. It gives me energy. The cafe is quiet. I can read news on my phone there. The chairs are soft. I feel relaxed. The people working there are friendly. They know my name. Sometimes I meet my friend there. We talk for a short time. It is a nice place to start the day. I like the smell of coffee there.\n\nWord Count: 85 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'cafe', 'office', 'coffee', 'energy', 'soft', 'relaxed', 'smell'. \n\n>Band 3: Place words.\n\nNot Band 5: 'Nice place', 'friendly'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate sentences. 'People working there', 'It gives me'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Simple range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_043",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a happy event in your life.",
        "transcript_cleaned": "A happy event was my sister's wedding. It was two years ago. She married a good man. I was very happy for her. We had a big party. Many family members came. We wore beautiful clothes. I took many photos. We ate a lot of food. There was music and dancing. It was a special day. I remember my sister looked like a princess. We laughed a lot. It is my best memory.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'It was two years ago' (Correct)",
            "grammar: 'She married a good man' (Correct)",
            "grammar: 'There was music' (Correct existential)",
            "grammar: 'My sister looked like a princess' (Correct comparison)",
            "vocab: 'wedding', 'married', 'party', 'clothes', 'photos', 'food', 'music', 'dancing', 'princess', 'memory'. Band 4 level.",
            "repetitive: 'happy', 'lot'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'wedding', 'married', 'party', 'clothes', 'dancing', 'princess'. >Band 3: Event words. Not Band 5: 'Good man', 'beautiful clothes'. Basic.",
        "grammar_reason": "[GRA5] Key evidence: Accurate past tense sentences. 'We had', 'We wore', 'There was'. >Band 4: Consistent tenses. Not Band 6: Simple range.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a happy event in your life.\n\nTranscript: A happy event was my sister's wedding. It was two years ago. She married a good man. I was very happy for her. We had a big party. Many family members came. We wore beautiful clothes. I took many photos. We ate a lot of food. There was music and dancing. It was a special day. I remember my sister looked like a princess. We laughed a lot. It is my best memory.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'wedding', 'married', 'party', 'clothes', 'dancing', 'princess'. \n\n>Band 3: Event words.\n\nNot Band 5: 'Good man', 'beautiful clothes'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate past tense sentences. 'We had', 'We wore', 'There was'. \n\n>Band 4: Consistent tenses.\n\nNot Band 6: Simple range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_044",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of art you like.",
        "transcript_cleaned": "I like a painting in my house. It is a picture of flowers. The flowers are yellow and red. My mother painted it. She likes art. The painting is in the living room. It is colorful. When I look at it, I feel happy. It makes the room look nice. I do not know much about art, but I like this one. It is simple but beautiful. I want to learn how to paint like my mother.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'The flowers are' (Correct agreement)",
            "grammar: 'My mother painted it' (Correct)",
            "grammar: 'It makes the room look nice' (Correct causative 'make')",
            "grammar: 'I do not know much... but I like' (Correct compound)",
            "vocab: 'painting', 'picture', 'flowers', 'art', 'colorful', 'room', 'paint'. Band 4 level.",
            "repetitive: 'like', 'it is'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'painting', 'picture', 'flowers', 'art', 'colorful', 'paint'. >Band 3: Art words. Not Band 5: 'Look nice', 'simple'. Basic.",
        "grammar_reason": "[GRA5] Key evidence: Accurate sentences. 'It makes the room look nice', 'I do not know... but'. >Band 4: Frequent error-free sentences. Not Band 6: Simple range.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a piece of art you like.\n\nTranscript: I like a painting in my house. It is a picture of flowers. The flowers are yellow and red. My mother painted it. She likes art. The painting is in the living room. It is colorful. When I look at it, I feel happy. It makes the room look nice. I do not know much about art, but I like this one. It is simple but beautiful. I want to learn how to paint like my mother.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'painting', 'picture', 'flowers', 'art', 'colorful', 'paint'. \n\n>Band 3: Art words.\n\nNot Band 5: 'Look nice', 'simple'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate sentences. 'It makes the room look nice', 'I do not know... but'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Simple range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_045",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant you like.",
        "transcript_cleaned": "I like the rose plant. It has beautiful flowers. They are red or pink. It smells very good. I have roses in my garden. I water them every day. They need sun and water to grow. Be careful, they have thorns. They can hurt your hand. I cut the flowers and put them in a vase. They make my house smell nice. I think roses are the best flowers. They mean love.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'They are red or pink' (Correct)",
            "grammar: 'They need sun and water to grow' (Correct infinitive purpose)",
            "grammar: 'They can hurt your hand' (Correct modal)",
            "vocab: 'rose', 'plant', 'flowers', 'smells', 'garden', 'water', 'sun', 'grow', 'thorns', 'vase', 'love'. Band 4 level.",
            "repetitive: 'they', 'flowers'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'rose', 'plant', 'flowers', 'smells', 'garden', 'water', 'thorns'. >Band 3: Nature words. Not Band 5: 'Smell nice', 'beautiful'. Basic.",
        "grammar_reason": "[GRA5] Key evidence: Accurate simple sentences. 'They need... to grow'. >Band 4: Frequent error-free sentences. Not Band 6: Simple range.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant you like.\n\nTranscript: I like the rose plant. It has beautiful flowers. They are red or pink. It smells very good. I have roses in my garden. I water them every day. They need sun and water to grow. Be careful, they have thorns. They can hurt your hand. I cut the flowers and put them in a vase. They make my house smell nice. I think roses are the best flowers. They mean love.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'rose', 'plant', 'flowers', 'smells', 'garden', 'water', 'thorns'. \n\n>Band 3: Nature words.\n\nNot Band 5: 'Smell nice', 'beautiful'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate simple sentences. 'They need... to grow'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Simple range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_046",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a disagreement you had.",
        "transcript_cleaned": "I had a disagreement with my brother. It was about TV. I wanted to watch a movie, but he wanted to watch football. We argued. I was angry. I shouted at him. He shouted too. My mother came and stopped us. She said we must share. So we watched football for one hour, then we watched my movie. It was fair. I said sorry to my brother. Fighting is not good. We should be nice to family.",
        "word_count": 80,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'I wanted to watch... but he wanted' (Correct compound)",
            "grammar: 'My mother came and stopped us' (Correct)",
            "grammar: 'She said we must share' (Correct reported speech/modal)",
            "vocab: 'disagreement', 'movie', 'football', 'argued', 'angry', 'shouted', 'share', 'fair', 'sorry', 'fighting'. Band 4 level.",
            "repetitive: 'watch', 'shouted'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'disagreement', 'argued', 'angry', 'shouted', 'share', 'fair', 'fighting'. >Band 3: Conflict words. Not Band 5: 'Not good', 'nice'. Basic.",
        "grammar_reason": "[GRA5] Key evidence: Accurate past tense and modals. 'She said we must share'. >Band 4: Frequent error-free sentences. Not Band 6: Simple range.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a disagreement you had.\n\nTranscript: I had a disagreement with my brother. It was about TV. I wanted to watch a movie, but he wanted to watch football. We argued. I was angry. I shouted at him. He shouted too. My mother came and stopped us. She said we must share. So we watched football for one hour, then we watched my movie. It was fair. I said sorry to my brother. Fighting is not good. We should be nice to family.\n\nWord Count: 80 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'disagreement', 'argued', 'angry', 'shouted', 'share', 'fair', 'fighting'. \n\n>Band 3: Conflict words.\n\nNot Band 5: 'Not good', 'nice'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate past tense and modals. 'She said we must share'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Simple range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_047",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a rule at your school.",
        "transcript_cleaned": "In my school, we must wear a uniform. It is a blue shirt and black trousers. Everyone wears the same clothes. I think it is a good rule. We do not need to choose clothes every morning. It saves time. Also, no one judges your clothes. But some students do not like it. They want to wear their own clothes. The teachers are strict about this rule. If you do not wear uniform, you cannot enter class.",
        "word_count": 81,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'We must wear' (Correct modal)",
            "grammar: 'Everyone wears' (Correct agreement)",
            "grammar: 'If you do not wear... you cannot enter' (Correct first conditional)",
            "vocab: 'school', 'rule', 'uniform', 'shirt', 'trousers', 'clothes', 'judges', 'strict', 'enter'. Band 4 level.",
            "repetitive: 'clothes', 'wear'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'uniform', 'shirt', 'trousers', 'choose', 'judges', 'strict', 'enter'. >Band 3: School words. Not Band 5: 'Good rule', 'saves time'. Basic.",
        "grammar_reason": "[GRA5] Key evidence: Accurate sentences with modals and conditional. 'If you do not wear...'. >Band 4: Frequent error-free sentences. Not Band 6: Simple range.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a rule at your school.\n\nTranscript: In my school, we must wear a uniform. It is a blue shirt and black trousers. Everyone wears the same clothes. I think it is a good rule. We do not need to choose clothes every morning. It saves time. Also, no one judges your clothes. But some students do not like it. They want to wear their own clothes. The teachers are strict about this rule. If you do not wear uniform, you cannot enter class.\n\nWord Count: 81 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'uniform', 'shirt', 'trousers', 'choose', 'judges', 'strict', 'enter'. \n\n>Band 3: School words.\n\nNot Band 5: 'Good rule', 'saves time'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate sentences with modals and conditional. 'If you do not wear...'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Simple range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_048",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a toy you liked as a child.",
        "transcript_cleaned": "I had a toy car when I was small. It was red. It was a fast car. I played with it every day. I pushed it on the floor. It made a noise. I liked it because it looked like a real car. My father bought it for me. I kept it in a box. I did not want to break it. I still have it in my room. It is old now, but it brings back memories.",
        "word_count": 81,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'I had a toy car' (Correct)",
            "grammar: 'I liked it because it looked like' (Correct reason/comparison)",
            "grammar: 'It brings back memories' (Correct phrase)",
            "vocab: 'toy', 'car', 'small', 'floor', 'noise', 'box', 'break', 'memories'. Band 4 level.",
            "repetitive: 'it', 'car'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'toy', 'car', 'floor', 'noise', 'box', 'break', 'memories'. >Band 3: Toy words. Not Band 5: 'Fast car', 'real car'. Basic.",
        "grammar_reason": "[GRA5] Key evidence: Accurate past tense sentences. 'I liked it because it looked like'. >Band 4: Consistent tenses. Not Band 6: Simple range.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a toy you liked as a child.\n\nTranscript: I had a toy car when I was small. It was red. It was a fast car. I played with it every day. I pushed it on the floor. It made a noise. I liked it because it looked like a real car. My father bought it for me. I kept it in a box. I did not want to break it. I still have it in my room. It is old now, but it brings back memories.\n\nWord Count: 81 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'toy', 'car', 'floor', 'noise', 'box', 'break', 'memories'. \n\n>Band 3: Toy words.\n\nNot Band 5: 'Fast car', 'real car'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate past tense sentences. 'I liked it because it looked like'. \n\n>Band 4: Consistent tenses.\n\nNot Band 6: Simple range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_049",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a prize you want to win.",
        "transcript_cleaned": "I want to win a lottery. It is a big prize. It is a lot of money. If I win, I can buy many things. I can buy a big house and a new car. I can travel to other countries. I can help my family. Winning the lottery is difficult. It depends on luck. But I buy a ticket sometimes. It is exciting to check the numbers. I hope one day I will be lucky.",
        "word_count": 79,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'If I win, I can buy' (Correct first conditional)",
            "grammar: 'Winning the lottery is difficult' (Correct gerund subject)",
            "grammar: 'It depends on luck' (Correct)",
            "vocab: 'lottery', 'prize', 'money', 'buy', 'house', 'car', 'travel', 'luck', 'ticket', 'numbers'. Band 4 level.",
            "repetitive: 'I can', 'buy'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'lottery', 'prize', 'money', 'buy', 'travel', 'luck', 'ticket'. >Band 3: Topic words. Not Band 5: 'Big house', 'new car'. Basic.",
        "grammar_reason": "[GRA5] Key evidence: Accurate sentences with conditional. 'If I win, I can buy'. >Band 4: Frequent error-free sentences. Not Band 6: Simple range.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a prize you want to win.\n\nTranscript: I want to win a lottery. It is a big prize. It is a lot of money. If I win, I can buy many things. I can buy a big house and a new car. I can travel to other countries. I can help my family. Winning the lottery is difficult. It depends on luck. But I buy a ticket sometimes. It is exciting to check the numbers. I hope one day I will be lucky.\n\nWord Count: 79 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'lottery', 'prize', 'money', 'buy', 'travel', 'luck', 'ticket'. \n\n>Band 3: Topic words.\n\nNot Band 5: 'Big house', 'new car'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate sentences with conditional. 'If I win, I can buy'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Simple range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_050",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a long walk you enjoyed.",
        "transcript_cleaned": "I walked in the park last Sunday. It was a sunny day. I walked with my dog. We walked for two hours. The park is very big. I saw many trees and birds. The air was fresh. I felt relaxed. I like walking because it is good exercise. It makes me healthy. I was tired after the walk, but it was a good feeling. I think everyone should walk more. It is easy and free.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'It was a sunny day' (Correct)",
            "grammar: 'I like walking because it is good exercise' (Correct)",
            "grammar: 'It makes me healthy' (Correct)",
            "vocab: 'walk', 'park', 'sunny', 'dog', 'trees', 'birds', 'fresh', 'exercise', 'healthy', 'free'. Band 4 level.",
            "repetitive: 'walked', 'was'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'walk', 'park', 'sunny', 'dog', 'fresh', 'exercise', 'healthy'. >Band 3: Topic words. Not Band 5: 'Good feeling', 'easy'. Basic.",
        "grammar_reason": "[GRA5] Key evidence: Accurate simple sentences. 'I like walking because...'. >Band 4: Frequent error-free sentences. Not Band 6: Simple range.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a long walk you enjoyed.\n\nTranscript: I walked in the park last Sunday. It was a sunny day. I walked with my dog. We walked for two hours. The park is very big. I saw many trees and birds. The air was fresh. I felt relaxed. I like walking because it is good exercise. It makes me healthy. I was tired after the walk, but it was a good feeling. I think everyone should walk more. It is easy and free.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'walk', 'park', 'sunny', 'dog', 'fresh', 'exercise', 'healthy'. \n\n>Band 3: Topic words.\n\nNot Band 5: 'Good feeling', 'easy'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate simple sentences. 'I like walking because...'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Simple range.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
