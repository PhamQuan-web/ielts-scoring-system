import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch03.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v5_g6_176",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult journey.",
        "transcript_cleaned": "I went to a village in the mountains. The journey was long and difficult. I traveled by bus. The road was narrow and winding. I felt sick because the bus moved too much. It took six hours to get there. Although I was tired, I liked the view. I saw green forests and rivers. When I arrived, the air was fresh. It was worth the long trip. I think traveling is tiring but interesting.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'village', 'mountains', 'journey', 'narrow', 'winding', 'sick', 'view', 'forests', 'fresh', 'worth'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'village', 'narrow', 'winding', 'view', 'forests', 'worth'. >Band 4: 'Winding', 'worth'. Not Band 6: 'Long and difficult', 'fresh air'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'because the bus moved', 'Although I was tired', 'When I arrived'. >Band 5: Complex sentences used correctly. Not Band 7: Simple sentence structure dominates.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult journey.\n\nTranscript: I went to a village in the mountains. The journey was long and difficult. I traveled by bus. The road was narrow and winding. I felt sick because the bus moved too much. It took six hours to get there. Although I was tired, I liked the view. I saw green forests and rivers. When I arrived, the air was fresh. It was worth the long trip. I think traveling is tiring but interesting.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'village', 'narrow', 'winding', 'view', 'forests', 'worth'. \n\n>Band 4: 'Winding', 'worth'.\n\nNot Band 6: 'Long and difficult', 'fresh air'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'because the bus moved', 'Although I was tired', 'When I arrived'. \n\n>Band 5: Complex sentences used correctly.\n\nNot Band 7: Simple sentence structure dominates.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_177",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a favorite song.",
        "transcript_cleaned": "I like the song \"Imagine\" by John Lennon. It is a slow song. The lyrics are meaningful. He sings about peace and love. I listen to it when I am sad. It makes me feel better. The melody is beautiful. I think everyone knows this song. It is a classic. I like it because it gives hope. If everyone listened to this song, the world would be better. It is my favorite song.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'slow', 'lyrics', 'meaningful', 'peace', 'melody', 'classic', 'hope', 'world'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'lyrics', 'meaningful', 'peace', 'melody', 'classic', 'hope'. >Band 4: 'Lyrics', 'melody'. Not Band 6: 'Beautiful', 'better'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'listen to it when', 'because it gives hope', 'If everyone listened... would be'. >Band 5: 2nd conditional used correctly. Not Band 7: Short sentences.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a favorite song.\n\nTranscript: I like the song \"Imagine\" by John Lennon. It is a slow song. The lyrics are meaningful. He sings about peace and love. I listen to it when I am sad. It makes me feel better. The melody is beautiful. I think everyone knows this song. It is a classic. I like it because it gives hope. If everyone listened to this song, the world would be better. It is my favorite song.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'lyrics', 'meaningful', 'peace', 'melody', 'classic', 'hope'. \n\n>Band 4: 'Lyrics', 'melody'.\n\nNot Band 6: 'Beautiful', 'better'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'listen to it when', 'because it gives hope', 'If everyone listened... would be'. \n\n>Band 5: 2nd conditional used correctly.\n\nNot Band 7: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_178",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a local festival.",
        "transcript_cleaned": "There is a food festival in my city every year. It happens in the summer. Many people come to eat. There are stalls which sell different kinds of food. I like the spicy food. I went there with my friends last week. We tried many dishes. It was crowded but fun. There was music too. I think festivals are important because they bring people together. I always enjoy this time of year.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'festival', 'stalls', 'spicy', 'dishes', 'crowded', 'important', 'bring together'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'festival', 'stalls', 'spicy', 'dishes', 'crowded', 'bring together'. >Band 4: 'Stalls', 'dishes'. Not Band 6: 'Different kinds', 'fun'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'stalls which sell', 'because they bring people together'. >Band 5: Relative and causal clauses correct. Not Band 7: Simple sentence structure.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a local festival.\n\nTranscript: There is a food festival in my city every year. It happens in the summer. Many people come to eat. There are stalls which sell different kinds of food. I like the spicy food. I went there with my friends last week. We tried many dishes. It was crowded but fun. There was music too. I think festivals are important because they bring people together. I always enjoy this time of year.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'festival', 'stalls', 'spicy', 'dishes', 'crowded', 'bring together'. \n\n>Band 4: 'Stalls', 'dishes'.\n\nNot Band 6: 'Different kinds', 'fun'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'stalls which sell', 'because they bring people together'. \n\n>Band 5: Relative and causal clauses correct.\n\nNot Band 7: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_179",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a family member.",
        "transcript_cleaned": "I admire my grandfather. He is 80 years old. He lives in the countryside. He was a farmer. He is very strong. He works in his garden every day. He grows vegetables which are healthy. He tells me stories about the past. I like listening to him. He is wise. He teaches me to be honest. Although he is old, he is active. I visit him every weekend. I love him very much.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'admire', 'countryside', 'farmer', 'garden', 'vegetables', 'healthy', 'wise', 'honest', 'active'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'admire', 'countryside', 'farmer', 'vegetables', 'wise', 'honest', 'active'. >Band 4: 'Wise', 'honest', 'active'. Not Band 6: 'Very strong', 'every day'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'vegetables which are healthy', 'Although he is old', 'teaches me to be'. >Band 5: Complex sentences used correctly. Not Band 7: Repetitive 'He'.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a family member.\n\nTranscript: I admire my grandfather. He is 80 years old. He lives in the countryside. He was a farmer. He is very strong. He works in his garden every day. He grows vegetables which are healthy. He tells me stories about the past. I like listening to him. He is wise. He teaches me to be honest. Although he is old, he is active. I visit him every weekend. I love him very much.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'admire', 'countryside', 'farmer', 'vegetables', 'wise', 'honest', 'active'. \n\n>Band 4: 'Wise', 'honest', 'active'.\n\nNot Band 6: 'Very strong', 'every day'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'vegetables which are healthy', 'Although he is old', 'teaches me to be'. \n\n>Band 5: Complex sentences used correctly.\n\nNot Band 7: Repetitive 'He'.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_180",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a foreign food.",
        "transcript_cleaned": "I ate tacos in a Mexican restaurant. Tacos are a traditional food from Mexico. They are made of corn tortillas. Inside, there is meat and vegetables. I put some spicy sauce on it. It tasted very good. It was different from my country's food. I ate three tacos. My friend, who likes spicy food, ate five. I want to learn how to make them. It is a delicious meal which is easy to eat.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'traditional', 'corn', 'tortillas', 'meat', 'vegetables', 'spicy', 'sauce', 'tasted', 'delicious'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'traditional', 'tortillas', 'spicy', 'sauce', 'delicious'. >Band 4: 'Tortillas', 'spicy'. Not Band 6: 'Very good', 'easy to eat'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'friend, who likes spicy food', 'meal which is easy'. >Band 5: Relative clauses used correctly. Not Band 7: Simple sentence structure.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a foreign food.\n\nTranscript: I ate tacos in a Mexican restaurant. Tacos are a traditional food from Mexico. They are made of corn tortillas. Inside, there is meat and vegetables. I put some spicy sauce on it. It tasted very good. It was different from my country's food. I ate three tacos. My friend, who likes spicy food, ate five. I want to learn how to make them. It is a delicious meal which is easy to eat.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'traditional', 'tortillas', 'spicy', 'sauce', 'delicious'. \n\n>Band 4: 'Tortillas', 'spicy'.\n\nNot Band 6: 'Very good', 'easy to eat'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'friend, who likes spicy food', 'meal which is easy'. \n\n>Band 5: Relative clauses used correctly.\n\nNot Band 7: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_181",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I watched a basketball competition at school. Two teams played against each other. My class team wore red shirts. The game was very exciting. The players ran fast and jumped high. I cheered for my friends. The score was close. In the last minute, my friend scored a point. We won the game. Everyone was happy. I think competitions are good because they teach teamwork. It was a memorable day.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'competition', 'teams', 'exciting', 'cheered', 'score', 'scored', 'won', 'teamwork', 'memorable'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'competition', 'cheered', 'score', 'teamwork', 'memorable'. >Band 4: 'Cheered', 'memorable'. Not Band 6: 'Ran fast', 'jumped high'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'competitions are good because', 'teach teamwork'. >Band 5: Cause and effect used correctly. Not Band 7: Short simple sentences predominate.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I watched a basketball competition at school. Two teams played against each other. My class team wore red shirts. The game was very exciting. The players ran fast and jumped high. I cheered for my friends. The score was close. In the last minute, my friend scored a point. We won the game. Everyone was happy. I think competitions are good because they teach teamwork. It was a memorable day.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'competition', 'cheered', 'score', 'teamwork', 'memorable'. \n\n>Band 4: 'Cheered', 'memorable'.\n\nNot Band 6: 'Ran fast', 'jumped high'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'competitions are good because', 'teach teamwork'. \n\n>Band 5: Cause and effect used correctly.\n\nNot Band 7: Short simple sentences predominate.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_182",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful app.",
        "transcript_cleaned": "I use an app called Duolingo. It is for learning languages. I am learning French on it. It is very useful. The lessons are short and easy. I can use it on the bus. It has games which make learning fun. I practice every day. I have learned many words. If I study hard, I will speak French well. I recommend this app to anyone who wants to learn a language.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'app', 'languages', 'lessons', 'short', 'easy', 'games', 'practice', 'study', 'recommend'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'app', 'languages', 'lessons', 'practice', 'recommend'. >Band 4: 'Recommend', 'app'. Not Band 6: 'Short and easy', 'very useful'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'games which make', 'If I study... I will', 'anyone who wants'. >Band 5: Relative clauses and conditionals correct. Not Band 7: Simple structure.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful app.\n\nTranscript: I use an app called Duolingo. It is for learning languages. I am learning French on it. It is very useful. The lessons are short and easy. I can use it on the bus. It has games which make learning fun. I practice every day. I have learned many words. If I study hard, I will speak French well. I recommend this app to anyone who wants to learn a language.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'app', 'languages', 'lessons', 'practice', 'recommend'. \n\n>Band 4: 'Recommend', 'app'.\n\nNot Band 6: 'Short and easy', 'very useful'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'games which make', 'If I study... I will', 'anyone who wants'. \n\n>Band 5: Relative clauses and conditionals correct.\n\nNot Band 7: Simple structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_183",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a photo.",
        "transcript_cleaned": "I have a photo of my dog. He is a white dog named Snowy. I took this photo in the park. He was running and playing. He looks very happy in the photo. The grass is green. I like this photo because it is cute. I show it to my friends. They say he is lovely. I keep this photo on my phone. It reminds me of my dog when I am at school.",
        "word_count": 77,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'photo', 'named', 'running', 'playing', 'grass', 'cute', 'lovely', 'reminds'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'photo', 'named', 'cute', 'lovely', 'reminds'. >Band 4: 'Reminds', 'lovely'. Not Band 6: 'Very happy', 'green'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'He was running', 'because it is cute', 'reminds me... when I am'. >Band 5: Past continuous and adverbial clauses correct. Not Band 7: Simple sentences.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a photo.\n\nTranscript: I have a photo of my dog. He is a white dog named Snowy. I took this photo in the park. He was running and playing. He looks very happy in the photo. The grass is green. I like this photo because it is cute. I show it to my friends. They say he is lovely. I keep this photo on my phone. It reminds me of my dog when I am at school.\n\nWord Count: 77 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'photo', 'named', 'cute', 'lovely', 'reminds'. \n\n>Band 4: 'Reminds', 'lovely'.\n\nNot Band 6: 'Very happy', 'green'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'He was running', 'because it is cute', 'reminds me... when I am'. \n\n>Band 5: Past continuous and adverbial clauses correct.\n\nNot Band 7: Simple sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_184",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a garden.",
        "transcript_cleaned": "My grandmother has a beautiful garden. It is behind her house. There are many flowers which are colorful. She grows roses and lilies. She also grows vegetables like tomatoes and carrots. I help her water the plants. It is hard work, but I enjoy it. The garden is a quiet place where I can read books. I like the smell of flowers. I think gardening is a good hobby for old people.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'garden', 'flowers', 'colorful', 'roses', 'lilies', 'vegetables', 'tomatoes', 'carrots', 'water', 'quiet', 'smell', 'gardening', 'hobby'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'garden', 'colorful', 'roses', 'lilies', 'vegetables', 'gardening', 'hobby'. >Band 4: 'Lilies', 'gardening'. Not Band 6: 'Hard work', 'good hobby'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'flowers which are colorful', 'place where I can read'. >Band 5: Relative clauses used correctly. Not Band 7: Simple sentence structure.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a garden.\n\nTranscript: My grandmother has a beautiful garden. It is behind her house. There are many flowers which are colorful. She grows roses and lilies. She also grows vegetables like tomatoes and carrots. I help her water the plants. It is hard work, but I enjoy it. The garden is a quiet place where I can read books. I like the smell of flowers. I think gardening is a good hobby for old people.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'garden', 'colorful', 'roses', 'lilies', 'vegetables', 'gardening', 'hobby'. \n\n>Band 4: 'Lilies', 'gardening'.\n\nNot Band 6: 'Hard work', 'good hobby'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'flowers which are colorful', 'place where I can read'. \n\n>Band 5: Relative clauses used correctly.\n\nNot Band 7: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_185",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I had to learn how to drive a car. It was difficult for me. I was nervous. My father taught me. He was patient. I made many mistakes. I forgot to signal. I drove too fast. But I practiced every weekend. After two months, I took the test. I passed it. I was very happy. Now I can drive alone. It is a useful skill which makes my life easier.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'drive', 'nervous', 'patient', 'mistakes', 'signal', 'practiced', 'test', 'passed', 'skill', 'easier'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'drive', 'nervous', 'patient', 'mistakes', 'signal', 'skill'. >Band 4: 'Signal', 'patient'. Not Band 6: 'Too fast', 'very happy'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'skill which makes', 'forgot to signal', 'practiced every weekend'. >Band 5: Relative clauses and past tense correct. Not Band 7: Short sentences.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I had to learn how to drive a car. It was difficult for me. I was nervous. My father taught me. He was patient. I made many mistakes. I forgot to signal. I drove too fast. But I practiced every weekend. After two months, I took the test. I passed it. I was very happy. Now I can drive alone. It is a useful skill which makes my life easier.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'drive', 'nervous', 'patient', 'mistakes', 'signal', 'skill'. \n\n>Band 4: 'Signal', 'patient'.\n\nNot Band 6: 'Too fast', 'very happy'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'skill which makes', 'forgot to signal', 'practiced every weekend'. \n\n>Band 5: Relative clauses and past tense correct.\n\nNot Band 7: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_186",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a meal.",
        "transcript_cleaned": "I ate a delicious meal at a Chinese restaurant. I went with my family. We ordered many dishes. We had dumplings, noodles, and duck. The duck was crispy. The noodles were spicy. I used chopsticks to eat. It was fun. We drank tea. The meal was expensive, but we enjoyed it. My father paid the bill. I like Chinese food because it has many flavors. I want to go there again.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'delicious', 'restaurant', 'ordered', 'dishes', 'dumplings', 'noodles', 'duck', 'crispy', 'chopsticks', 'flavors'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'restaurant', 'dumplings', 'crispy', 'spicy', 'chopsticks', 'flavors'. >Band 4: 'Crispy', 'chopsticks'. Not Band 6: 'Delicious meal', 'many dishes'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'food because it has', 'meal was expensive, but'. >Band 5: Correct compound and complex sentences. Not Band 7: Simple structure.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a meal.\n\nTranscript: I ate a delicious meal at a Chinese restaurant. I went with my family. We ordered many dishes. We had dumplings, noodles, and duck. The duck was crispy. The noodles were spicy. I used chopsticks to eat. It was fun. We drank tea. The meal was expensive, but we enjoyed it. My father paid the bill. I like Chinese food because it has many flavors. I want to go there again.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'restaurant', 'dumplings', 'crispy', 'spicy', 'chopsticks', 'flavors'. \n\n>Band 4: 'Crispy', 'chopsticks'.\n\nNot Band 6: 'Delicious meal', 'many dishes'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'food because it has', 'meal was expensive, but'. \n\n>Band 5: Correct compound and complex sentences.\n\nNot Band 7: Simple structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_187",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a goal.",
        "transcript_cleaned": "My goal is to buy a house. I am saving money now. Houses are expensive in my city. I need a lot of money. I work hard every day. I put money in the bank. I want a house which has a garden. I want to plant flowers there. It will take five years to save enough. But I am patient. Having my own house is my dream. It will make me feel secure.",
        "word_count": 77,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'goal', 'saving', 'expensive', 'bank', 'garden', 'plant', 'patient', 'dream', 'secure'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'goal', 'saving', 'expensive', 'patient', 'dream', 'secure'. >Band 4: 'Secure', 'patient'. Not Band 6: 'Work hard', 'big house'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'house which has', 'take five years to save'. >Band 5: Relative clauses and infinitive phrases correct. Not Band 7: Short sentences.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a goal.\n\nTranscript: My goal is to buy a house. I am saving money now. Houses are expensive in my city. I need a lot of money. I work hard every day. I put money in the bank. I want a house which has a garden. I want to plant flowers there. It will take five years to save enough. But I am patient. Having my own house is my dream. It will make me feel secure.\n\nWord Count: 77 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'goal', 'saving', 'expensive', 'patient', 'dream', 'secure'. \n\n>Band 4: 'Secure', 'patient'.\n\nNot Band 6: 'Work hard', 'big house'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'house which has', 'take five years to save'. \n\n>Band 5: Relative clauses and infinitive phrases correct.\n\nNot Band 7: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_188",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you gave.",
        "transcript_cleaned": "I gave a scarf to my sister. It was her graduation. I knitted it myself. It took two weeks. The scarf was red and soft. I wrapped it in a box. When she opened it, she was surprised. She liked it very much. She wore it immediately. She said it was warm. I felt happy because she liked my gift. Handmade gifts are special because they show love. I want to knit another one.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'scarf', 'graduation', 'knitted', 'soft', 'wrapped', 'surprised', 'immediately', 'warm', 'handmade', 'special'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'scarf', 'knitted', 'wrapped', 'surprised', 'immediately', 'handmade'. >Band 4: 'Knitted', 'immediately'. Not Band 6: 'Soft', 'warm'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'When she opened it', 'because she liked', 'gifts are special because'. >Band 5: Time and causal clauses correct. Not Band 7: Simple structure.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a gift you gave.\n\nTranscript: I gave a scarf to my sister. It was her graduation. I knitted it myself. It took two weeks. The scarf was red and soft. I wrapped it in a box. When she opened it, she was surprised. She liked it very much. She wore it immediately. She said it was warm. I felt happy because she liked my gift. Handmade gifts are special because they show love. I want to knit another one.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'scarf', 'knitted', 'wrapped', 'surprised', 'immediately', 'handmade'. \n\n>Band 4: 'Knitted', 'immediately'.\n\nNot Band 6: 'Soft', 'warm'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'When she opened it', 'because she liked', 'gifts are special because'. \n\n>Band 5: Time and causal clauses correct.\n\nNot Band 7: Simple structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_189",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a job.",
        "transcript_cleaned": "I think being a chef is an interesting job. Chefs cook food in restaurants. They create new dishes. It is a creative job. But it is also stressful. They work long hours. They stand all day. The kitchen is hot and noisy. Chefs must be fast and careful. If the food is bad, customers will complain. I like cooking, but I do not want to be a chef. It is too hard.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'chef', 'restaurants', 'create', 'dishes', 'creative', 'stressful', 'kitchen', 'careful', 'customers', 'complain'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'chef', 'create', 'dishes', 'creative', 'stressful', 'customers', 'complain'. >Band 4: 'Creative', 'stressful'. Not Band 6: 'New dishes', 'hard'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'If the food is bad', 'like cooking, but'. >Band 5: Conditionals and compound sentences correct. Not Band 7: Repetitive 'They'.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a job.\n\nTranscript: I think being a chef is an interesting job. Chefs cook food in restaurants. They create new dishes. It is a creative job. But it is also stressful. They work long hours. They stand all day. The kitchen is hot and noisy. Chefs must be fast and careful. If the food is bad, customers will complain. I like cooking, but I do not want to be a chef. It is too hard.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'chef', 'create', 'dishes', 'creative', 'stressful', 'customers', 'complain'. \n\n>Band 4: 'Creative', 'stressful'.\n\nNot Band 6: 'New dishes', 'hard'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'If the food is bad', 'like cooking, but'. \n\n>Band 5: Conditionals and compound sentences correct.\n\nNot Band 7: Repetitive 'They'.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_190",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical period.",
        "transcript_cleaned": "I am interested in the Victorian era. It was in England a long time ago. Queen Victoria was the ruler. It was a time of change. Many machines were invented. Trains became popular. People wore formal clothes. Men wore hats and women wore long dresses. Life was hard for poor people. I read a book about it. It was fascinating. I would like to visit a museum to see things from that time.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'era', 'ruler', 'change', 'machines', 'invented', 'formal', 'fascinating'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'era', 'ruler', 'machines', 'invented', 'formal', 'fascinating'. >Band 4: 'Invented', 'fascinating'. Not Band 6: 'Long dresses', 'hard'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'machines were invented', 'visit a museum to see'. >Band 5: Passive voice and infinitive purpose correct. Not Band 7: Simple sentences.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical period.\n\nTranscript: I am interested in the Victorian era. It was in England a long time ago. Queen Victoria was the ruler. It was a time of change. Many machines were invented. Trains became popular. People wore formal clothes. Men wore hats and women wore long dresses. Life was hard for poor people. I read a book about it. It was fascinating. I would like to visit a museum to see things from that time.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'era', 'ruler', 'machines', 'invented', 'formal', 'fascinating'. \n\n>Band 4: 'Invented', 'fascinating'.\n\nNot Band 6: 'Long dresses', 'hard'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'machines were invented', 'visit a museum to see'. \n\n>Band 5: Passive voice and infinitive purpose correct.\n\nNot Band 7: Simple sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_191",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a successful person.",
        "transcript_cleaned": "I admire Elon Musk. He is a successful businessman. He started companies like Tesla and SpaceX. He is very rich. He makes electric cars which are good for the environment. He also wants to send people to Mars. He is smart and innovative. He works very hard. I watch his interviews on YouTube. He has big ideas. I think he is changing the world. He inspires me to dream big.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'admire', 'businessman', 'companies', 'electric cars', 'environment', 'Mars', 'innovative', 'interviews', 'inspires'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'admire', 'businessman', 'electric cars', 'environment', 'innovative', 'inspires'. >Band 4: 'Innovative', 'environment'. Not Band 6: 'Very rich', 'big ideas'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'cars which are good', 'wants to send'. >Band 5: Relative clauses used correctly. Not Band 7: Repetitive 'He'.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a successful person.\n\nTranscript: I admire Elon Musk. He is a successful businessman. He started companies like Tesla and SpaceX. He is very rich. He makes electric cars which are good for the environment. He also wants to send people to Mars. He is smart and innovative. He works very hard. I watch his interviews on YouTube. He has big ideas. I think he is changing the world. He inspires me to dream big.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'admire', 'businessman', 'electric cars', 'environment', 'innovative', 'inspires'. \n\n>Band 4: 'Innovative', 'environment'.\n\nNot Band 6: 'Very rich', 'big ideas'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'cars which are good', 'wants to send'. \n\n>Band 5: Relative clauses used correctly.\n\nNot Band 7: Repetitive 'He'.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_192",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a place you study.",
        "transcript_cleaned": "I study in a coffee shop near my house. It is called Star Coffee. I go there on weekends. It is quiet in the morning. I drink coffee while I study. It keeps me awake. The atmosphere is nice. There is soft music. I bring my laptop and books. I can use the free wifi. I study for three hours. I like this place because I can concentrate. It is better than my noisy house.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'coffee shop', 'quiet', 'awake', 'atmosphere', 'soft', 'laptop', 'wifi', 'concentrate', 'noisy'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'coffee shop', 'awake', 'atmosphere', 'laptop', 'concentrate'. >Band 4: 'Concentrate', 'atmosphere'. Not Band 6: 'Nice', 'soft music'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'while I study', 'because I can concentrate', 'better than'. >Band 5: Time/causal clauses and comparatives correct. Not Band 7: Simple sentences.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a place you study.\n\nTranscript: I study in a coffee shop near my house. It is called Star Coffee. I go there on weekends. It is quiet in the morning. I drink coffee while I study. It keeps me awake. The atmosphere is nice. There is soft music. I bring my laptop and books. I can use the free wifi. I study for three hours. I like this place because I can concentrate. It is better than my noisy house.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'coffee shop', 'awake', 'atmosphere', 'laptop', 'concentrate'. \n\n>Band 4: 'Concentrate', 'atmosphere'.\n\nNot Band 6: 'Nice', 'soft music'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'while I study', 'because I can concentrate', 'better than'. \n\n>Band 5: Time/causal clauses and comparatives correct. Not Band 7: Simple sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_193",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of clothes.",
        "transcript_cleaned": "I like wearing T-shirts. I have a favorite one which is blue. It has a picture of a cat on it. I bought it in a market. It was cheap. The cotton is soft. It is comfortable to wear. I wear it in summer when it is hot. I wear it with shorts. My friends say it is cute. I have washed it many times, but the color is still good. It is simple clothes, but I like it.",
        "word_count": 82,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'T-shirts', 'market', 'cheap', 'cotton', 'soft', 'comfortable', 'shorts', 'cute', 'washed'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'T-shirts', 'market', 'cotton', 'comfortable', 'shorts'. >Band 4: 'Comfortable', 'cotton'. Not Band 6: 'Cute', 'soft'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'one which is blue', 'when it is hot', 'but the color is'. >Band 5: Relative/time clauses and compound sentences correct. Not Band 7: Repetitive 'I', 'It'.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a piece of clothes.\n\nTranscript: I like wearing T-shirts. I have a favorite one which is blue. It has a picture of a cat on it. I bought it in a market. It was cheap. The cotton is soft. It is comfortable to wear. I wear it in summer when it is hot. I wear it with shorts. My friends say it is cute. I have washed it many times, but the color is still good. It is simple clothes, but I like it.\n\nWord Count: 82 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'T-shirts', 'market', 'cotton', 'comfortable', 'shorts'. \n\n>Band 4: 'Comfortable', 'cotton'.\n\nNot Band 6: 'Cute', 'soft'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'one which is blue', 'when it is hot', 'but the color is'. \n\n>Band 5: Relative/time clauses and compound sentences correct.\n\nNot Band 7: Repetitive 'I', 'It'.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_194",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a TV show.",
        "transcript_cleaned": "I like a show called \"The Big Bang Theory\". It is a comedy about scientists. They are very smart but socially awkward. They live in an apartment. I laugh a lot when I watch it. The jokes are funny. I like the character Sheldon. He is strange. I watch it every evening after dinner. It helps me relax. I have seen all the episodes. It is a popular show in my country. I think everyone should watch it.",
        "word_count": 80,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'comedy', 'scientists', 'smart', 'socially awkward', 'apartment', 'jokes', 'character', 'strange', 'relax', 'episodes', 'popular'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'comedy', 'scientists', 'socially awkward', 'apartment', 'character', 'episodes'. >Band 4: 'Socially awkward', 'episodes'. Not Band 6: 'Smart', 'strange'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'when I watch it', 'everyone should watch'. >Band 5: Time clauses and modals used correctly. Not Band 7: Simple sentences.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a TV show.\n\nTranscript: I like a show called \"The Big Bang Theory\". It is a comedy about scientists. They are very smart but socially awkward. They live in an apartment. I laugh a lot when I watch it. The jokes are funny. I like the character Sheldon. He is strange. I watch it every evening after dinner. It helps me relax. I have seen all the episodes. It is a popular show in my country. I think everyone should watch it.\n\nWord Count: 80 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'comedy', 'scientists', 'socially awkward', 'apartment', 'character', 'episodes'. \n\n>Band 4: 'Socially awkward', 'episodes'.\n\nNot Band 6: 'Smart', 'strange'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'when I watch it', 'everyone should watch'. \n\n>Band 5: Time clauses and modals used correctly. Not Band 7: Simple sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_195",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a song.",
        "transcript_cleaned": "I love the song \"Let It Go\". It is from the movie Frozen. It is a powerful song. The singer has a high voice. I like the lyrics because they are inspiring. It says we should be free. I sing it in the shower. It makes me feel strong. My little sister likes it too. We sing together. It is a very famous song. Even adults like it. I think it is a masterpiece of music.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'powerful', 'singer', 'voice', 'lyrics', 'inspiring', 'free', 'shower', 'strong', 'famous', 'adults', 'masterpiece'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'powerful', 'lyrics', 'inspiring', 'famous', 'masterpiece'. >Band 4: 'Lyrics', 'inspiring'. Not Band 6: 'High voice', 'strong'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'because they are inspiring', 'we should be'. >Band 5: Causal clauses and modals correct. Not Band 7: Simple sentences.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a song.\n\nTranscript: I love the song \"Let It Go\". It is from the movie Frozen. It is a powerful song. The singer has a high voice. I like the lyrics because they are inspiring. It says we should be free. I sing it in the shower. It makes me feel strong. My little sister likes it too. We sing together. It is a very famous song. Even adults like it. I think it is a masterpiece of music.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'powerful', 'lyrics', 'inspiring', 'famous', 'masterpiece'. \n\n>Band 4: 'Lyrics', 'inspiring'.\n\nNot Band 6: 'High voice', 'strong'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'because they are inspiring', 'we should be'. \n\n>Band 5: Causal clauses and modals correct. Not Band 7: Simple sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_196",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a holiday.",
        "transcript_cleaned": "I went to Japan for a holiday. It was a wonderful trip. I visited Tokyo and Kyoto. I saw many temples which were old. I ate sushi and ramen. The food was fresh. I traveled by train. It was fast and clean. I met Japanese people who were polite. I bought souvenirs for my family. I stayed there for one week. I was sad when I left. I want to visit Japan again because it is beautiful.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'wonderful', 'trip', 'temples', 'sushi', 'ramen', 'fresh', 'train', 'polite', 'souvenirs'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'wonderful', 'temples', 'fresh', 'polite', 'souvenirs'. >Band 4: 'Souvenirs', 'temples'. Not Band 6: 'Fast and clean', 'beautiful'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'temples which were old', 'people who were polite', 'when I left'. >Band 5: Relative and time clauses correct. Not Band 7: Repetitive 'I'.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a holiday.\n\nTranscript: I went to Japan for a holiday. It was a wonderful trip. I visited Tokyo and Kyoto. I saw many temples which were old. I ate sushi and ramen. The food was fresh. I traveled by train. It was fast and clean. I met Japanese people who were polite. I bought souvenirs for my family. I stayed there for one week. I was sad when I left. I want to visit Japan again because it is beautiful.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'wonderful', 'temples', 'fresh', 'polite', 'souvenirs'. \n\n>Band 4: 'Souvenirs', 'temples'.\n\nNot Band 6: 'Fast and clean', 'beautiful'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'temples which were old', 'people who were polite', 'when I left'. \n\n>Band 5: Relative and time clauses correct. Not Band 7: Repetitive 'I'.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_197",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a thing you bought.",
        "transcript_cleaned": "I bought a pair of running shoes. They are Nike shoes. They are black and white. I bought them because I wanted to exercise. I went to a sport shop. They were on sale, so they were cheap. They are very comfortable. I wear them when I run in the park. They protect my feet. I clean them every week. I think good shoes are important for running. I am happy with my purchase.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'running shoes', 'exercise', 'sport shop', 'sale', 'cheap', 'comfortable', 'protect', 'feet', 'purchase'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'running shoes', 'exercise', 'sale', 'comfortable', 'protect', 'purchase'. >Band 4: 'Purchase', 'comfortable'. Not Band 6: 'Good shoes', 'black and white'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'because I wanted to', 'when I run'. >Band 5: Causal and time clauses used correctly. Not Band 7: Short sentences.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a thing you bought.\n\nTranscript: I bought a pair of running shoes. They are Nike shoes. They are black and white. I bought them because I wanted to exercise. I went to a sport shop. They were on sale, so they were cheap. They are very comfortable. I wear them when I run in the park. They protect my feet. I clean them every week. I think good shoes are important for running. I am happy with my purchase.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'running shoes', 'exercise', 'sale', 'comfortable', 'protect', 'purchase'. \n\n>Band 4: 'Purchase', 'comfortable'.\n\nNot Band 6: 'Good shoes', 'black and white'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'because I wanted to', 'when I run'. \n\n>Band 5: Causal and time clauses used correctly.\n\nNot Band 7: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_198",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a sport match.",
        "transcript_cleaned": "I watched a volleyball match last Sunday. It was between my school team and another school. We played in the gym. It was a close match. The players hit the ball over the net. They jumped very high. I shouted to support my team. In the end, my school won. I was so excited. We celebrated with ice cream. I like volleyball because it is fast. Watching sports is a fun way to spend time.",
        "word_count": 77,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'volleyball', 'match', 'team', 'gym', 'close match', 'hit', 'net', 'shouted', 'support', 'won', 'celebrated'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'volleyball', 'match', 'gym', 'net', 'support', 'celebrated'. >Band 4: 'Celebrated', 'gym'. Not Band 6: 'Jumped high', 'fast'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'between my school... and another', 'because it is fast', 'way to spend time'. >Band 5: Prepositional phrases and reasons correct. Not Band 7: Simple structure.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a sport match.\n\nTranscript: I watched a volleyball match last Sunday. It was between my school team and another school. We played in the gym. It was a close match. The players hit the ball over the net. They jumped very high. I shouted to support my team. In the end, my school won. I was so excited. We celebrated with ice cream. I like volleyball because it is fast. Watching sports is a fun way to spend time.\n\nWord Count: 77 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'volleyball', 'match', 'gym', 'net', 'support', 'celebrated'. \n\n>Band 4: 'Celebrated', 'gym'.\n\nNot Band 6: 'Jumped high', 'fast'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'between my school... and another', 'because it is fast', 'way to spend time'. \n\n>Band 5: Prepositional phrases and reasons correct.\n\nNot Band 7: Simple structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_199",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I had to give a presentation in my English class. It was a difficult task for me. I am shy, so I was nervous. I had to speak for five minutes. I prepared my speech at home. I practiced in front of a mirror. When I started speaking, my hands were shaking. But I remembered my words. My teacher smiled at me. I finished the speech successfully. My classmates clapped. I felt very proud of myself.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'presentation', 'task', 'shy', 'nervous', 'speech', 'mirror', 'shaking', 'remembered', 'successfully', 'clapped', 'proud'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'presentation', 'shy', 'nervous', 'speech', 'shaking', 'successfully', 'proud'. >Band 4: 'Presentation', 'successfully'. Not Band 6: 'Very proud', 'difficult task'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'so I was nervous', 'When I started speaking'. >Band 5: Connectors and time clauses used correctly. Not Band 7: Simple sentence structure.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I had to give a presentation in my English class. It was a difficult task for me. I am shy, so I was nervous. I had to speak for five minutes. I prepared my speech at home. I practiced in front of a mirror. When I started speaking, my hands were shaking. But I remembered my words. My teacher smiled at me. I finished the speech successfully. My classmates clapped. I felt very proud of myself.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'presentation', 'shy', 'nervous', 'speech', 'shaking', 'successfully', 'proud'. \n\n>Band 4: 'Presentation', 'successfully'.\n\nNot Band 6: 'Very proud', 'difficult task'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'so I was nervous', 'When I started speaking'. \n\n>Band 5: Connectors and time clauses used correctly.\n\nNot Band 7: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_200",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a crowded place.",
        "transcript_cleaned": "I went to a music concert in a stadium. It was the most crowded place I have ever seen. There were thousands of people. Everyone was standing and shouting. I lost my friend for a few minutes. I was scared. The music was very loud. People were dancing and singing. It was a crazy atmosphere. Although it was crowded, I had fun. It was an unforgettable experience. I want to go to another concert soon.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'concert', 'stadium', 'crowded', 'shouting', 'scared', 'loud', 'atmosphere', 'unforgettable', 'experience'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'concert', 'stadium', 'crowded', 'atmosphere', 'unforgettable', 'experience'. >Band 4: 'Atmosphere', 'unforgettable'. Not Band 6: 'Crazy', 'loud'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'most crowded place I have ever seen', 'Although it was crowded'. >Band 5: Superlative + present perfect and concession used correctly. Not Band 7: Short sentences.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a crowded place.\n\nTranscript: I went to a music concert in a stadium. It was the most crowded place I have ever seen. There were thousands of people. Everyone was standing and shouting. I lost my friend for a few minutes. I was scared. The music was very loud. People were dancing and singing. It was a crazy atmosphere. Although it was crowded, I had fun. It was an unforgettable experience. I want to go to another concert soon.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'concert', 'stadium', 'crowded', 'atmosphere', 'unforgettable', 'experience'. \n\n>Band 4: 'Atmosphere', 'unforgettable'.\n\nNot Band 6: 'Crazy', 'loud'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'most crowded place I have ever seen', 'Although it was crowded'. \n\n>Band 5: Superlative + present perfect and concession used correctly. Not Band 7: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
