import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch05.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v6_g7_351",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a park you like to visit.",
        "transcript_cleaned": "I would like to describe a local park called Green Meadows, which is situated near my house. It is a vast green space that offers a welcome escape from the noisy city. I usually go there on weekends to jog or simply relax on the grass. The park features a large pond where people can rent boats, which is quite popular in the summer. There are also several walking paths lined with old oak trees. What I enjoy most is the peaceful atmosphere. It is a place where I can clear my mind and recharge my batteries. Although it can get crowded during holidays, it remains my favorite spot for outdoor activities because of its natural beauty and convenient location.",
        "word_count": 126,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'vast', 'welcome escape', 'noisy city', 'features', 'walking paths', 'lined', 'peaceful atmosphere', 'clear my mind', 'recharge my batteries', 'natural beauty'. Band 6 level.",
             "grammar: 'which is situated', 'offers a welcome escape', 'where people can rent', 'What I enjoy most is'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'vast', 'escape', 'features', 'atmosphere', 'recharge my batteries'. >Band 5: Uses some less common items. Not Band 7: 'Noisy city', 'natural beauty' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'park called... which is', 'pond where people can', 'What I enjoy most is'. >Band 6: Frequent error-free sentences. Not Band 8: Some sentences are standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a park you like to visit.\n\nTranscript: I would like to describe a local park called Green Meadows, which is situated near my house. It is a vast green space that offers a welcome escape from the noisy city. I usually go there on weekends to jog or simply relax on the grass. The park features a large pond where people can rent boats, which is quite popular in the summer. There are also several walking paths lined with old oak trees. What I enjoy most is the peaceful atmosphere. It is a place where I can clear my mind and recharge my batteries. Although it can get crowded during holidays, it remains my favorite spot for outdoor activities because of its natural beauty and convenient location.\n\nWord Count: 126 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'vast', 'escape', 'features', 'atmosphere', 'recharge my batteries'. \n\n>Band 5: Uses some less common items.\n\nNot Band 7: 'Noisy city', 'natural beauty' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'park called... which is', 'pond where people can', 'What I enjoy most is'. \n\n>Band 6: Frequent error-free sentences.\n\nNot Band 8: Some sentences are standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_352",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you received.",
        "transcript_cleaned": "I want to talk about a watch that my parents gave me for my graduation. It was a complete surprise because I had not asked for it. The watch is made of silver and has a classic design. I remember feeling very emotional when I opened the box. It represents their pride in my achievements. I wear it on special occasions, such as job interviews or family gatherings. It is not just a device to tell time; it is a sentimental item that I cherish deeply. Whenever I look at it, I am reminded of their support and love. It is definitely the most meaningful gift I have ever received.",
        "word_count": 126,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'complete surprise', 'classic design', 'emotional', 'achievements', 'special occasions', 'gatherings', 'device', 'sentimental', 'cherish deeply', 'meaningful'. Band 6 level.",
             "grammar: 'that my parents gave me', 'because I had not asked', 'not just... it is', 'Whenever I look at it'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'classic design', 'emotional', 'achievements', 'sentimental', 'cherish deeply'. >Band 5: 'Sentimental', 'cherish'. Not Band 7: 'Complete surprise', 'meaningful gift' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'watch that my parents', 'because I had not', 'Whenever I look at it'. >Band 6: Good control of subordination. Not Band 8: Lacks full flexibility.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a gift you received.\n\nTranscript: I want to talk about a watch that my parents gave me for my graduation. It was a complete surprise because I had not asked for it. The watch is made of silver and has a classic design. I remember feeling very emotional when I opened the box. It represents their pride in my achievements. I wear it on special occasions, such as job interviews or family gatherings. It is not just a device to tell time; it is a sentimental item that I cherish deeply. Whenever I look at it, I am reminded of their support and love. It is definitely the most meaningful gift I have ever received.\n\nWord Count: 126 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'classic design', 'emotional', 'achievements', 'sentimental', 'cherish deeply'. \n\n>Band 5: 'Sentimental', 'cherish'.\n\nNot Band 7: 'Complete surprise', 'meaningful gift' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'watch that my parents', 'because I had not', 'Whenever I look at it'. \n\n>Band 6: Good control of subordination.\n\nNot Band 8: Lacks full flexibility.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_353",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a movie you watched recently.",
        "transcript_cleaned": "I recently watched a science fiction movie called Interstellar. It is about a group of astronauts who travel through a wormhole to find a new home for humanity. The visual effects were spectacular and very realistic. I was particularly impressed by the acting of the main character. The plot was complicated, but it kept me on the edge of my seat. It explores themes of love and sacrifice. Although the movie was quite long, I did not feel bored at all. It made me think about the future of our planet. I would recommend it to anyone who likes space adventures because it is a truly memorable cinematic experience.",
        "word_count": 125,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'science fiction', 'astronauts', 'wormhole', 'humanity', 'visual effects', 'spectacular', 'realistic', 'impressed', 'complicated', 'edge of my seat', 'sacrifice', 'memorable'. Band 6 level.",
             "grammar: 'who travel through', 'impressed by the', 'although the movie was', 'anyone who likes'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'wormhole', 'spectacular', 'realistic', 'sacrifice', 'cinematic experience'. >Band 5: 'Spectacular', 'realistic'. Not Band 7: 'Main character', 'science fiction' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'astronauts who travel', 'Although the movie was', 'recommend it to anyone who'. >Band 6: Frequent error-free sentences. Not Band 8: Structure is somewhat repetitive.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a movie you watched recently.\n\nTranscript: I recently watched a science fiction movie called Interstellar. It is about a group of astronauts who travel through a wormhole to find a new home for humanity. The visual effects were spectacular and very realistic. I was particularly impressed by the acting of the main character. The plot was complicated, but it kept me on the edge of my seat. It explores themes of love and sacrifice. Although the movie was quite long, I did not feel bored at all. It made me think about the future of our planet. I would recommend it to anyone who likes space adventures because it is a truly memorable cinematic experience.\n\nWord Count: 125 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'wormhole', 'spectacular', 'realistic', 'sacrifice', 'cinematic experience'. \n\n>Band 5: 'Spectacular', 'realistic'.\n\nNot Band 7: 'Main character', 'science fiction' are common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'astronauts who travel', 'Although the movie was', 'recommend it to anyone who'. \n\n>Band 6: Frequent error-free sentences.\n\nNot Band 8: Structure is somewhat repetitive.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_354",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a teacher who helped you.",
        "transcript_cleaned": "I would like to talk about Mr. Smith, who was my history teacher in high school. He was a very knowledgeable and passionate person. He made history lessons interesting by telling us fascinating stories instead of just reading from the textbook. I remember one time when he helped me with a difficult project. He spent extra time explaining the topic to me, which I really appreciated. His dedication inspired me to study harder. He taught me the importance of critical thinking. Even though he was strict at times, he was always fair. I believe he had a significant impact on my education and helped me become a better student.",
        "word_count": 125,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'knowledgeable', 'passionate', 'fascinating', 'textbook', 'project', 'appreciated', 'dedication', 'inspired', 'critical thinking', 'strict', 'significant impact'. Band 6 level.",
             "grammar: 'who was my', 'instead of just reading', 'time when he helped', 'Even though he was'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'knowledgeable', 'passionate', 'fascinating', 'dedication', 'significant impact'. >Band 5: 'Knowledgeable', 'passionate'. Not Band 7: 'Interesting', 'study harder' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'Mr. Smith, who was', 'instead of just reading', 'Even though he was'. >Band 6: Good use of relative clauses and linking words. Not Band 8: Lacks idiomatic grammar.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a teacher who helped you.\n\nTranscript: I would like to talk about Mr. Smith, who was my history teacher in high school. He was a very knowledgeable and passionate person. He made history lessons interesting by telling us fascinating stories instead of just reading from the textbook. I remember one time when he helped me with a difficult project. He spent extra time explaining the topic to me, which I really appreciated. His dedication inspired me to study harder. He taught me the importance of critical thinking. Even though he was strict at times, he was always fair. I believe he had a significant impact on my education and helped me become a better student.\n\nWord Count: 125 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'knowledgeable', 'passionate', 'fascinating', 'dedication', 'significant impact'. \n\n>Band 5: 'Knowledgeable', 'passionate'.\n\nNot Band 7: 'Interesting', 'study harder' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'Mr. Smith, who was', 'instead of just reading', 'Even though he was'. \n\n>Band 6: Good use of relative clauses and linking words.\n\nNot Band 8: Lacks idiomatic grammar.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g7_355",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place you visited.",
        "transcript_cleaned": "I visited the Colosseum in Rome a few years ago. It is a massive amphitheater that was built in ancient times. I was amazed by the sheer size of the structure. It is famous for the gladiator fights that used to take place there. Walking around the ruins gave me a sense of history. I could imagine the crowds cheering. Although it is partially ruined, it is still an impressive sight. The guide explained how it was constructed without modern technology. It is a major tourist attraction that draws people from all over the world. Visiting this place was an unforgettable experience that taught me a lot about Roman civilization.",
        "word_count": 126,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'massive', 'amphitheater', 'ancient times', 'sheer size', 'gladiator fights', 'ruins', 'sense of history', 'cheering', 'partially ruined', 'impressive sight', 'constructed', 'tourist attraction', 'civilization'. Band 6 level.",
             "grammar: 'amphitheater that was built', 'used to take place', 'explained how it was constructed'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR6] Adequate range: 'massive', 'amphitheater', 'gladiator', 'ruins', 'impressive', 'constructed', 'civilization'. >Band 5: 'Impressive', 'constructed'. Not Band 7: 'Ancient times', 'tourist attraction' are common.",
        "grammar_reason": "[GRA7] Various complex structures: 'amphitheater that was built', 'explained how it was', 'Visiting this place was'. >Band 6: Passive voice and noun clauses used correctly. Not Band 8: Sentence flow is standard.",
        "vocabulary": 6,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical place you visited.\n\nTranscript: I visited the Colosseum in Rome a few years ago. It is a massive amphitheater that was built in ancient times. I was amazed by the sheer size of the structure. It is famous for the gladiator fights that used to take place there. Walking around the ruins gave me a sense of history. I could imagine the crowds cheering. Although it is partially ruined, it is still an impressive sight. The guide explained how it was constructed without modern technology. It is a major tourist attraction that draws people from all over the world. Visiting this place was an unforgettable experience that taught me a lot about Roman civilization.\n\nWord Count: 126 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Adequate range: 'massive', 'amphitheater', 'gladiator', 'ruins', 'impressive', 'constructed', 'civilization'. \n\n>Band 5: 'Impressive', 'constructed'.\n\nNot Band 7: 'Ancient times', 'tourist attraction' are common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Various complex structures: 'amphitheater that was built', 'explained how it was', 'Visiting this place was'. \n\n>Band 6: Passive voice and noun clauses used correctly.\n\nNot Band 8: Sentence flow is standard.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'w') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
