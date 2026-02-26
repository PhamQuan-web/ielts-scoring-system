import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch01.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v4_g5_026",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a website you use often.",
        "transcript_cleaned": "I want to talk about Facebook. It is a very big website. I use it every day to talk with my friends. I have used this website for five years. It is easy to use because everything is clear. I can see photos of my family and I can write messages. If I have free time, I always check Facebook. Sometimes I read news on it. But some news is not true. I like this website because it helps me know about the world. Also, I can find old friends there.",
        "word_count": 94,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'some news is' -> 'some news items are' or 'some news is' (news is uncountable, so 'is' is correct, but 'some news is' sounds slightly unnatural for high band, but acceptable for G5). Let's say 'some news are' (common error) -> actually transcript says 'is'. This is correct grammar.",
            "collocation: 'too much big' (not present)",
            "sentence structure: 'The website helps me know' (causative 'know' is a bit basic).",
            "tense/aspect: 'I have used... for five years' (Correct present perfect).",
            "complex sentence: 'If I have free time, I always check' (Correct zero conditional).",
            "connector: 'But', 'Also', 'because'.",
            "vocab: 'big', 'use', 'talk', 'friends', 'easy', 'clear', 'photos', 'write', 'messages', 'free time', 'check', 'read', 'news', 'true', 'know', 'world', 'find', 'old'. All very basic."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'website', 'talk', 'friends', 'photos', 'messages', 'news', 'world'. >Band 3: Topic clear. Not Band 5: 'Big website', 'good thing'. No less common vocabulary.",
        "grammar_reason": "[GRA5] Key evidence: Uses complex sentences with some accuracy. 'I have used... for', 'If I have... I check'. >Band 4: Frequent error-free sentences. Not Band 6: Sentences are accurate but very simple in structure.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a website you use often.\n\nTranscript: I want to talk about Facebook. It is a very big website. I use it every day to talk with my friends. I have used this website for five years. It is easy to use because everything is clear. I can see photos of my family and I can write messages. If I have free time, I always check Facebook. Sometimes I read news on it. But some news is not true. I like this website because it helps me know about the world. Also, I can find old friends there.\n\nWord Count: 94 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'website', 'talk', 'friends', 'photos', 'messages', 'news', 'world'. \n\n>Band 3: Topic clear.\n\nNot Band 5: 'Big website', 'good thing'. No less common vocabulary.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Uses complex sentences with some accuracy. 'I have used... for', 'If I have... I check'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Sentences are accurate but very simple in structure.\n\n**Micro flaws identified:**\n- none significant (grammar is accurate but simple/repetitive)"
    },
    {
        "sample_id": "syn_p2_v4_g5_027",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a famous person you would like to meet.",
        "transcript_cleaned": "I would like to meet Lionel Messi. He is a football player. Everyone knows him because he is very famous. He plays for a big team. I have watched him on TV since I was a child. He is very good at football. If I meet him, I will take a photo with him. I think he is a nice man. He helps poor people too. I want to ask him how to play football well. It would be a dream come true for me.",
        "word_count": 91,
        "response_type": "long_turn",
        "micro_flaws": [
            "cliché: 'dream come true' (memorized phrase, acceptable)",
            "grammar: 'I have watched... since I was' (Perfect tense used correctly)",
            "grammar: 'If I meet... I will take' (First conditional used correctly)",
            "vocab: 'player', 'famous', 'big team', 'child', 'good', 'photo', 'nice man', 'poor people', 'ask', 'play well'. Band 4 level.",
            "repetitive: 'He is', 'He plays', 'He helps'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'football player', 'famous', 'team', 'TV', 'child', 'good', 'photo'. >Band 3: Clear meaning. Not Band 5: 'Big team', 'nice man'. Very basic descriptors.",
        "grammar_reason": "[GRA5] Key evidence: Attempt at complex structures. 'Since I was a child', 'If I meet him'. >Band 4: Connectors and tenses used correctly. Not Band 6: Range is limited to basic complex structures.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a famous person you would like to meet.\n\nTranscript: I would like to meet Lionel Messi. He is a football player. Everyone knows him because he is very famous. He plays for a big team. I have watched him on TV since I was a child. He is very good at football. If I meet him, I will take a photo with him. I think he is a nice man. He helps poor people too. I want to ask him how to play football well. It would be a dream come true for me.\n\nWord Count: 91 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'football player', 'famous', 'team', 'TV', 'child', 'good', 'photo'. \n\n>Band 3: Clear meaning.\n\nNot Band 5: 'Big team', 'nice man'. Very basic descriptors.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Attempt at complex structures. 'Since I was a child', 'If I meet him'. \n\n>Band 4: Connectors and tenses used correctly.\n\nNot Band 6: Range is limited to basic complex structures.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_028",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historic place you visited.",
        "transcript_cleaned": "I visited the Great Wall in China. It is a very old place. I went there last year with my friends. The wall is very long and high. We walked for a long time. I felt tired but happy. There were many people there. I think it is important because it is old history. I saw mountains around the wall. The view was beautiful. I took many pictures. I want to go there again if I have money. It is the best place I have seen.",
        "word_count": 89,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'There were many people' (Correct existential 'there were')",
            "grammar: 'I want to go... if I have money' (Correct conditional)",
            "grammar: 'It is the best place I have seen' (Correct superlative + present perfect)",
            "vocab: 'old place', 'long', 'high', 'tired', 'happy', 'important', 'history', 'mountains', 'view', 'pictures'. Band 4 level.",
            "repetitive: 'long', 'old'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'wall', 'old', 'long', 'high', 'tired', 'people', 'history', 'mountains'. >Band 3: Describes place. Not Band 5: 'Old place', 'old history'. Repetitive and basic.",
        "grammar_reason": "[GRA5] Key evidence: Accurate simple and compound sentences. 'There were', 'It is the best place I have seen'. >Band 4: Tenses are consistent (past simple). Not Band 6: Lacks flexibility.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historic place you visited.\n\nTranscript: I visited the Great Wall in China. It is a very old place. I went there last year with my friends. The wall is very long and high. We walked for a long time. I felt tired but happy. There were many people there. I think it is important because it is old history. I saw mountains around the wall. The view was beautiful. I took many pictures. I want to go there again if I have money. It is the best place I have seen.\n\nWord Count: 89 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'wall', 'old', 'long', 'high', 'tired', 'people', 'history', 'mountains'. \n\n>Band 3: Describes place.\n\nNot Band 5: 'Old place', 'old history'. Repetitive and basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate simple and compound sentences. 'There were', 'It is the best place I have seen'. \n\n>Band 4: Tenses are consistent (past simple).\n\nNot Band 6: Lacks flexibility.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_029",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you were very busy.",
        "transcript_cleaned": "I was very busy last week. I had many things to do. I had to study for my exam. Also, I had to help my mother in the house. I did not have time to sleep much. I felt tired. My exam was difficult. I studied math and English. I worked until late night. But I finished everything. After the exam, I slept for a long time. Being busy is not good. I like to have free time to play games.",
        "word_count": 86,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'I had to study', 'I had to help' (Correct use of modal 'had to')",
            "grammar: 'I did not have time' (Correct negative past)",
            "grammar: 'Being busy is not good' (Gerund subject used correctly)",
            "vocab: 'busy', 'things', 'study', 'exam', 'mother', 'house', 'sleep', 'tired', 'math', 'English', 'play games'. Band 4 level.",
            "repetitive: 'time', 'busy'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'busy', 'study', 'exam', 'house', 'sleep', 'tired', 'math', 'games'. >Band 3: Narrates events. Not Band 5: 'Late night', 'long time'. Basic collocations.",
        "grammar_reason": "[GRA5] Key evidence: Accurate past tense and modals. 'I had to', 'I did not have'. >Band 4: Consistent past tense. Not Band 6: Sentence structures are repetitive (Subject-Verb-Object).",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a time you were very busy.\n\nTranscript: I was very busy last week. I had many things to do. I had to study for my exam. Also, I had to help my mother in the house. I did not have time to sleep much. I felt tired. My exam was difficult. I studied math and English. I worked until late night. But I finished everything. After the exam, I slept for a long time. Being busy is not good. I like to have free time to play games.\n\nWord Count: 86 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'busy', 'study', 'exam', 'house', 'sleep', 'tired', 'math', 'games'. \n\n>Band 3: Narrates events.\n\nNot Band 5: 'Late night', 'long time'. Basic collocations.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate past tense and modals. 'I had to', 'I did not have'. \n\n>Band 4: Consistent past tense.\n\nNot Band 6: Sentence structures are repetitive (Subject-Verb-Object).\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_030",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party you went to.",
        "transcript_cleaned": "I went to a birthday party last month. It was my friend's party. He turned twenty years old. Many people came to his house. We ate cake and pizza. The food was good. We danced to music. I gave him a gift. It was a shirt. He liked it. We sang happy birthday song. Everyone was happy. I stayed there for four hours. It was a fun time. I like parties because I can meet friends and eat good food.",
        "word_count": 86,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'It was my friend\\'s party' (Correct possessive)",
            "grammar: 'He turned twenty' (Correct verb)",
            "grammar: 'I gave him a gift' (Correct double object)",
            "vocab: 'birthday', 'party', 'cake', 'pizza', 'food', 'music', 'shirt', 'song', 'happy', 'fun'. Band 4 level.",
            "repetitive: 'happy', 'good'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'birthday', 'party', 'cake', 'pizza', 'danced', 'gift', 'shirt', 'sang'. >Band 3: Topic words. Not Band 5: 'Good food', 'fun time'. Basic descriptions.",
        "grammar_reason": "[GRA5] Key evidence: Accurate simple past tense. 'We ate', 'We danced', 'I gave'. >Band 4: Frequent error-free simple sentences. Not Band 6: Almost no complex structures used.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party you went to.\n\nTranscript: I went to a birthday party last month. It was my friend's party. He turned twenty years old. Many people came to his house. We ate cake and pizza. The food was good. We danced to music. I gave him a gift. It was a shirt. He liked it. We sang happy birthday song. Everyone was happy. I stayed there for four hours. It was a fun time. I like parties because I can meet friends and eat good food.\n\nWord Count: 86 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'birthday', 'party', 'cake', 'pizza', 'danced', 'gift', 'shirt', 'sang'. \n\n>Band 3: Topic words.\n\nNot Band 5: 'Good food', 'fun time'. Basic descriptions.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate simple past tense. 'We ate', 'We danced', 'I gave'. \n\n>Band 4: Frequent error-free simple sentences.\n\nNot Band 6: Almost no complex structures used.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_031",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of furniture in your home.",
        "transcript_cleaned": "I want to describe my sofa. It is in the living room. It is big and brown. It is made of leather. My father bought it five years ago. It is very comfortable. I sit on it every evening to watch TV. Sometimes I sleep on it. It is long enough for me. My family likes this sofa too. We sit together and talk. It is old but still good. I think it is the most useful thing in my house.",
        "word_count": 87,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'It is made of leather' (Correct passive)",
            "grammar: 'It is long enough for me' (Correct use of 'enough')",
            "grammar: 'It is the most useful thing' (Correct superlative)",
            "vocab: 'sofa', 'living room', 'brown', 'leather', 'bought', 'comfortable', 'sit', 'watch TV', 'sleep'. Band 4 level.",
            "repetitive: 'It is', 'sit'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'sofa', 'living room', 'leather', 'comfortable', 'sit', 'watch TV'. >Band 3: Household words. Not Band 5: 'Big and brown'. Basic descriptors.",
        "grammar_reason": "[GRA5] Key evidence: Accurate sentences. 'It is made of', 'It is long enough'. >Band 4: Uses passive and adjectives correctly. Not Band 6: Repetitive 'It is' structure.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a piece of furniture in your home.\n\nTranscript: I want to describe my sofa. It is in the living room. It is big and brown. It is made of leather. My father bought it five years ago. It is very comfortable. I sit on it every evening to watch TV. Sometimes I sleep on it. It is long enough for me. My family likes this sofa too. We sit together and talk. It is old but still good. I think it is the most useful thing in my house.\n\nWord Count: 87 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'sofa', 'living room', 'leather', 'comfortable', 'sit', 'watch TV'. \n\n>Band 3: Household words.\n\nNot Band 5: 'Big and brown'. Basic descriptors.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate sentences. 'It is made of', 'It is long enough'. \n\n>Band 4: Uses passive and adjectives correctly.\n\nNot Band 6: Repetitive 'It is' structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_032",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you used a map.",
        "transcript_cleaned": "I used a map when I went to London. I was lost. I did not know where to go. I used the map on my phone. It is called Google Maps. I wanted to find the train station. The map showed me the way. I walked for ten minutes. It was easy to follow. If I did not have the map, I would be late. Maps are very helpful. Now I use map every time I go to a new place.",
        "word_count": 86,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'I did not know where to go' (Correct indirect question)",
            "grammar: 'If I did not have... I would be' (Correct 2nd conditional mixed - 'did not have' (present state in past context?) No, 'did not have' is past. 'I would be late' (past result). Actually 'would have been late' is correct. 'Would be late' is acceptable for Band 5/6 error).",
            "vocab: 'map', 'London', 'lost', 'phone', 'train station', 'way', 'walked', 'easy'. Band 4 level.",
            "repetitive: 'map', 'go'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'map', 'lost', 'phone', 'train station', 'walked', 'easy'. >Band 3: Topic clear. Not Band 5: 'Showed me the way'. Basic directions.",
        "grammar_reason": "[GRA5] Key evidence: Attempt at complex structures. 'I did not know where to go'. >Band 4: Meaning clear with some complex attempts. Not Band 6: Error in conditional ('If I did not have... I would be' instead of 'would have been').",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a time you used a map.\n\nTranscript: I used a map when I went to London. I was lost. I did not know where to go. I used the map on my phone. It is called Google Maps. I wanted to find the train station. The map showed me the way. I walked for ten minutes. It was easy to follow. If I did not have the map, I would be late. Maps are very helpful. Now I use map every time I go to a new place.\n\nWord Count: 86 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'map', 'lost', 'phone', 'train station', 'walked', 'easy'. \n\n>Band 3: Topic clear.\n\nNot Band 5: 'Showed me the way'. Basic directions.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Attempt at complex structures. 'I did not know where to go'. \n\n>Band 4: Meaning clear with some complex attempts.\n\nNot Band 6: Error in conditional ('If I did not have... I would be' instead of 'would have been').\n\n**Micro flaws identified:**\n- conditional error: 'would be late' (would have been)"
    },
    {
        "sample_id": "syn_p2_v4_g5_033",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a polite person you know.",
        "transcript_cleaned": "I know a very polite person. Her name is Sarah. She is my neighbor. She always says hello to me. She smiles when she sees me. She is old but very kind. If she needs help, she asks nicely. She says please and thank you. I help her carry bags sometimes. She gives me cookies. Everyone likes her because she is good. I think it is important to be polite. It makes people happy. I want to be like her.",
        "word_count": 86,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'She always says' (Correct frequency adverb placement)",
            "grammar: 'She smiles when she sees me' (Correct time clause)",
            "grammar: 'If she needs help, she asks' (Correct zero conditional)",
            "vocab: 'polite', 'neighbor', 'hello', 'smiles', 'kind', 'help', 'bags', 'cookies', 'happy'. Band 4 level.",
            "repetitive: 'She is', 'She says'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'polite', 'neighbor', 'smiles', 'kind', 'help', 'cookies'. >Band 3: Character words. Not Band 5: 'Good' used for 'kind'. Basic social words.",
        "grammar_reason": "[GRA5] Key evidence: Accurate complex sentences. 'Smiles when she sees me'. >Band 4: Frequent error-free sentences. Not Band 6: Structures are very standard and repetitive.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a polite person you know.\n\nTranscript: I know a very polite person. Her name is Sarah. She is my neighbor. She always says hello to me. She smiles when she sees me. She is old but very kind. If she needs help, she asks nicely. She says please and thank you. I help her carry bags sometimes. She gives me cookies. Everyone likes her because she is good. I think it is important to be polite. It makes people happy. I want to be like her.\n\nWord Count: 86 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'polite', 'neighbor', 'smiles', 'kind', 'help', 'cookies'. \n\n>Band 3: Character words.\n\nNot Band 5: 'Good' used for 'kind'. Basic social words.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate complex sentences. 'Smiles when she sees me'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Structures are very standard and repetitive.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_034",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you forgot something.",
        "transcript_cleaned": "I forgot my keys yesterday. It was a bad day. I went to school in the morning. When I came home, I looked in my bag. No keys. I was outside my house. I could not open the door. I called my mother but she was at work. I had to wait for two hours. It was cold outside. I felt stupid. Finally my mother came and opened the door. Next time I will check my bag carefully.",
        "word_count": 83,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'When I came home, I looked' (Correct time clause)",
            "grammar: 'I could not open' (Correct modal)",
            "grammar: 'I had to wait' (Correct obligation)",
            "vocab: 'forgot', 'keys', 'bag', 'outside', 'open', 'door', 'cold', 'stupid', 'wait'. Band 4 level.",
            "repetitive: 'door', 'home'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'forgot', 'keys', 'bag', 'door', 'work', 'wait', 'cold', 'stupid'. >Band 3: Tells story. Not Band 5: 'Bad day'. No specific vocab for 'locked out'.",
        "grammar_reason": "[GRA5] Key evidence: Accurate use of past tenses and modals. 'Could not', 'Had to'. >Band 4: Frequent error-free sentences. Not Band 6: Simple range of structures.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a time you forgot something.\n\nTranscript: I forgot my keys yesterday. It was a bad day. I went to school in the morning. When I came home, I looked in my bag. No keys. I was outside my house. I could not open the door. I called my mother but she was at work. I had to wait for two hours. It was cold outside. I felt stupid. Finally my mother came and opened the door. Next time I will check my bag carefully.\n\nWord Count: 83 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'forgot', 'keys', 'bag', 'door', 'work', 'wait', 'cold', 'stupid'. \n\n>Band 3: Tells story.\n\nNot Band 5: 'Bad day'. No specific vocab for 'locked out'.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate use of past tenses and modals. 'Could not', 'Had to'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Simple range of structures.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_035",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a noisy place you have been to.",
        "transcript_cleaned": "I went to a market in my city. It is very noisy. Many people shout to sell things. Cars drive near the market and make noise. I went there to buy fruit. I could not hear my friend talking. It was too loud. My head hurt. I stayed for only thirty minutes. I do not like noisy places. I prefer quiet places like library. But the market has good food, so many people go there.",
        "word_count": 80,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'make noise' (Correct collocation/grammar)",
            "grammar: 'I could not hear' (Correct modal)",
            "grammar: 'I prefer quiet places like library' (Missing article 'a library' or 'libraries', but 'prefer... like' is correct structure)",
            "vocab: 'market', 'noisy', 'shout', 'sell', 'fruit', 'loud', 'head hurt', 'quiet'. Band 4 level.",
            "repetitive: 'places', 'noisy'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'market', 'noisy', 'shout', 'sell', 'loud', 'head', 'quiet'. >Band 3: Topic clear. Not Band 5: 'Head hurt' (My head ached). Basic descriptors.",
        "grammar_reason": "[GRA5] Key evidence: Accurate sentences mostly. 'Could not hear'. >Band 4: Frequent error-free sentences. Not Band 6: Missing articles ('like library') and simple connectors.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a noisy place you have been to.\n\nTranscript: I went to a market in my city. It is very noisy. Many people shout to sell things. Cars drive near the market and make noise. I went there to buy fruit. I could not hear my friend talking. It was too loud. My head hurt. I stayed for only thirty minutes. I do not like noisy places. I prefer quiet places like library. But the market has good food, so many people go there.\n\nWord Count: 80 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'market', 'noisy', 'shout', 'sell', 'loud', 'head', 'quiet'. \n\n>Band 3: Topic clear.\n\nNot Band 5: 'Head hurt' (My head ached). Basic descriptors.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate sentences mostly. 'Could not hear'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Missing articles ('like library') and simple connectors.\n\n**Micro flaws identified:**\n- article error: 'like library'"
    },
    {
        "sample_id": "syn_p2_v4_g5_036",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a family business you know.",
        "transcript_cleaned": "My uncle has a restaurant. It is a family business. He cooks the food. His wife helps him. His children work there too. They wash dishes and serve food. I like to eat there. The food is traditional. It is not a big restaurant, but it is popular. Many people know my uncle. He works very hard every day. He wants to make money for his family. I think it is good to work with family.",
        "word_count": 81,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'He cooks', 'His wife helps' (Correct subject-verb agreement)",
            "grammar: 'It is not... but it is' (Correct compound sentence)",
            "vocab: 'restaurant', 'cooks', 'wife', 'children', 'wash dishes', 'serve', 'money', 'work'. Band 4 level.",
            "repetitive: 'family', 'food'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'restaurant', 'business', 'cooks', 'wash dishes', 'serve', 'money'. >Band 3: Work context clear. Not Band 5: 'Make money', 'good'. Basic vocabulary.",
        "grammar_reason": "[GRA5] Key evidence: Accurate simple and compound sentences. 'It is not a big restaurant, but it is popular'. >Band 4: Frequent error-free sentences. Not Band 6: Limited range of complex structures.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a family business you know.\n\nTranscript: My uncle has a restaurant. It is a family business. He cooks the food. His wife helps him. His children work there too. They wash dishes and serve food. I like to eat there. The food is traditional. It is not a big restaurant, but it is popular. Many people know my uncle. He works very hard every day. He wants to make money for his family. I think it is good to work with family.\n\nWord Count: 81 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'restaurant', 'business', 'cooks', 'wash dishes', 'serve', 'money'. \n\n>Band 3: Work context clear.\n\nNot Band 5: 'Make money', 'good'. Basic vocabulary.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate simple and compound sentences. 'It is not a big restaurant, but it is popular'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Limited range of complex structures.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_037",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful app on your phone.",
        "transcript_cleaned": "I use WhatsApp. It is a messaging app. I use it to talk to my friends. I can send photos and videos. It is free. I do not need to pay money. It is very fast. I can make a group with my family. We talk every day. I like it because it is simple. I have it on my phone always. If I do not have internet, I cannot use it. But usually I have internet.",
        "word_count": 82,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'I do not need to pay' (Correct)",
            "grammar: 'I can make a group' (Correct)",
            "grammar: 'If I do not have... I cannot use' (Correct first conditional)",
            "vocab: 'app', 'messaging', 'send', 'photos', 'videos', 'free', 'money', 'internet'. Band 4 level.",
            "repetitive: 'use', 'have'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'app', 'messaging', 'send', 'photos', 'videos', 'free', 'internet'. >Band 3: Tech words. Not Band 5: 'Simple', 'fast'. Basic adjectives.",
        "grammar_reason": "[GRA5] Key evidence: Accurate simple sentences and one conditional. 'If I do not have...'. >Band 4: Frequent error-free sentences. Not Band 6: Very short sentences predominately.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful app on your phone.\n\nTranscript: I use WhatsApp. It is a messaging app. I use it to talk to my friends. I can send photos and videos. It is free. I do not need to pay money. It is very fast. I can make a group with my family. We talk every day. I like it because it is simple. I have it on my phone always. If I do not have internet, I cannot use it. But usually I have internet.\n\nWord Count: 82 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'app', 'messaging', 'send', 'photos', 'videos', 'free', 'internet'. \n\n>Band 3: Tech words.\n\nNot Band 5: 'Simple', 'fast'. Basic adjectives.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate simple sentences and one conditional. 'If I do not have...'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Very short sentences predominately.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v4_g5_038",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a foreign country you want to visit.",
        "transcript_cleaned": "I want to visit Japan. It is in Asia. I see pictures of Japan on TV. It looks beautiful. I want to see Tokyo. It is a big city. Also I want to eat sushi. I like Japanese food. I heard people are polite there. I want to wear traditional clothes. Name is Kimono. I think it will be expensive to go there. I need to save money. If I go, I will be very happy.",
        "word_count": 81,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'It looks beautiful' (Correct)",
            "grammar: 'I heard people are polite' (Correct reported speech structure)",
            "grammar: 'Name is Kimono' (Missing article/possessive 'The name is' or 'Its name is')",
            "grammar: 'I think it will be expensive' (Correct future prediction)",
            "vocab: 'Japan', 'Asia', 'pictures', 'city', 'sushi', 'food', 'clothes', 'money'. Band 4 level.",
            "repetitive: 'want to'."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR4] Key evidence: 'Japan', 'Asia', 'city', 'sushi', 'food', 'clothes', 'money'. >Band 3: Travel words. Not Band 5: 'Big city', 'beautiful'. No specific culture words beyond 'sushi/Kimono'.",
        "grammar_reason": "[GRA5] Key evidence: Accurate sentences mostly. 'I think it will be'. >Band 4: Frequent error-free sentences. Not Band 6: Missing article 'Name is Kimono'. Simple structures.",
        "vocabulary": 4,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a foreign country you want to visit.\n\nTranscript: I want to visit Japan. It is in Asia. I see pictures of Japan on TV. It looks beautiful. I want to see Tokyo. It is a big city. Also I want to eat sushi. I like Japanese food. I heard people are polite there. I want to wear traditional clothes. Name is Kimono. I think it will be expensive to go there. I need to save money. If I go, I will be very happy.\n\nWord Count: 81 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Key evidence: 'Japan', 'Asia', 'city', 'sushi', 'food', 'clothes', 'money'. \n\n>Band 3: Travel words.\n\nNot Band 5: 'Big city', 'beautiful'. No specific culture words beyond 'sushi/Kimono'.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Accurate sentences mostly. 'I think it will be'. \n\n>Band 4: Frequent error-free sentences.\n\nNot Band 6: Missing article 'Name is Kimono'. Simple structures.\n\n**Micro flaws identified:**\n- article error: 'Name is Kimono'"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
