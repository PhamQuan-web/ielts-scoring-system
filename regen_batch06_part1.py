import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch06.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v7_g7_451",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Palace of Versailles in France, which is a magnificent example of French Baroque architecture. It was the principal royal residence of France from 1682 until the French Revolution. The sheer scale of the palace is breathtaking, with its opulent rooms and vast gardens. I was particularly impressed by the Hall of Mirrors, where the Treaty of Versailles was signed. The gardens are meticulously maintained and stretch for miles, featuring fountains and sculptures. It was a fascinating glimpse into the lavish lifestyle of the French monarchy. Although it was crowded with tourists, the grandeur of the place made it worth the visit. I learned a lot about French history and culture during my tour.",
        "word_count": 113,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'magnificent example', 'Baroque architecture', 'principal', 'residence', 'sheer scale', 'breathtaking', 'opulent', 'meticulously maintained', 'lavish lifestyle', 'monarchy', 'grandeur'. Band 7 level.",
             "grammar: 'Palace... which is', 'where the Treaty... was signed', 'Although it was crowded'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'magnificent example', 'Baroque architecture', 'sheer scale', 'breathtaking', 'opulent', 'meticulously maintained', 'lavish lifestyle', 'grandeur'. >Band 6: 'Meticulously', 'grandeur'. Not Band 8: 'Worth the visit' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'Palace... which is', 'where the Treaty... was signed', 'Although it was crowded'. >Band 6: Frequent error-free sentences. Not Band 8: Lacks full flexibility.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Palace of Versailles in France, which is a magnificent example of French Baroque architecture. It was the principal royal residence of France from 1682 until the French Revolution. The sheer scale of the palace is breathtaking, with its opulent rooms and vast gardens. I was particularly impressed by the Hall of Mirrors, where the Treaty of Versailles was signed. The gardens are meticulously maintained and stretch for miles, featuring fountains and sculptures. It was a fascinating glimpse into the lavish lifestyle of the French monarchy. Although it was crowded with tourists, the grandeur of the place made it worth the visit. I learned a lot about French history and culture during my tour.\n\nWord Count: 113 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'magnificent example', 'Baroque architecture', 'sheer scale', 'breathtaking', 'opulent', 'meticulously maintained', 'lavish lifestyle', 'grandeur'. \n\n>Band 6: 'Meticulously', 'grandeur'.\n\nNot Band 8: 'Worth the visit' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Palace... which is', 'where the Treaty... was signed', 'Although it was crowded'. \n\n>Band 6: Frequent error-free sentences.\n\nNot Band 8: Lacks full flexibility.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_452",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I had to decide whether to move abroad for work or stay close to my family. It was a pivotal moment in my career that required careful consideration. On one hand, the international exposure would be invaluable for my professional growth. On the other hand, I would miss important family gatherings and the support of my friends. After much deliberation and consulting with mentors, I chose to take the job. It was a leap of faith, but I believe it was the right choice. The experience has broadened my horizons significantly and made me more independent. Looking back, I think it was the best decision I could have made at that time.",
        "word_count": 113,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'pivotal moment', 'international exposure', 'invaluable', 'professional growth', 'deliberation', 'consulting', 'leap of faith', 'broadened my horizons', 'significantly'. Band 7 level.",
             "grammar: 'whether to move', 'career that required', 'After much deliberation', 'believe it was'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'pivotal moment', 'international exposure', 'invaluable', 'deliberation', 'leap of faith', 'broadened my horizons', 'significantly'. >Band 6: 'Pivotal', 'deliberation'. Not Band 8: 'Right choice' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'whether to move', 'career that required', 'After much deliberation', 'believe it was'. >Band 6: Complex structures used accurately. Not Band 8: Some simple sentences remain.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I had to decide whether to move abroad for work or stay close to my family. It was a pivotal moment in my career that required careful consideration. On one hand, the international exposure would be invaluable for my professional growth. On the other hand, I would miss important family gatherings and the support of my friends. After much deliberation and consulting with mentors, I chose to take the job. It was a leap of faith, but I believe it was the right choice. The experience has broadened my horizons significantly and made me more independent. Looking back, I think it was the best decision I could have made at that time.\n\nWord Count: 113 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'pivotal moment', 'international exposure', 'invaluable', 'deliberation', 'leap of faith', 'broadened my horizons', 'significantly'. \n\n>Band 6: 'Pivotal', 'deliberation'.\n\nNot Band 8: 'Right choice' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'whether to move', 'career that required', 'After much deliberation', 'believe it was'. \n\n>Band 6: Complex structures used accurately.\n\nNot Band 8: Some simple sentences remain.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_453",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I recently read Sapiens by Yuval Noah Harari, which offers a thought-provoking perspective on human history. The author argues that our ability to create myths is what separates us from other species. I found the chapter on the agricultural revolution particularly enlightening as it challenged my preconceived notions about progress. The book is dense but accessible, making complex ideas easy to understand. It encouraged me to think critically about our impact on the planet and our future. It is a must-read for anyone interested in anthropology and sociology. I have recommended it to all my friends because it is such an eye-opening book.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'thought-provoking', 'perspective', 'myths', 'separates', 'agricultural revolution', 'enlightening', 'preconceived notions', 'dense', 'accessible', 'critically', 'anthropology'. Band 7 level.",
             "grammar: 'Harari, which offers', 'argues that our ability', 'what separates us', 'making complex ideas'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'thought-provoking', 'perspective', 'myths', 'separates', 'agricultural revolution', 'enlightening', 'preconceived notions', 'dense', 'accessible', 'critically', 'anthropology'. >Band 6: 'Enlightening', 'preconceived'. Not Band 8: 'Impact on the planet' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'Harari, which offers', 'argues that our ability', 'what separates us', 'making complex ideas'. >Band 6: Variety of complex structures. Not Band 8: Sentence length is uniform.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I recently read Sapiens by Yuval Noah Harari, which offers a thought-provoking perspective on human history. The author argues that our ability to create myths is what separates us from other species. I found the chapter on the agricultural revolution particularly enlightening as it challenged my preconceived notions about progress. The book is dense but accessible, making complex ideas easy to understand. It encouraged me to think critically about our impact on the planet and our future. It is a must-read for anyone interested in anthropology and sociology. I have recommended it to all my friends because it is such an eye-opening book.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'thought-provoking', 'perspective', 'myths', 'separates', 'agricultural revolution', 'enlightening', 'preconceived notions', 'dense', 'accessible', 'critically', 'anthropology'. \n\n>Band 6: 'Enlightening', 'preconceived'.\n\nNot Band 8: 'Impact on the planet' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Harari, which offers', 'argues that our ability', 'what separates us', 'making complex ideas'. \n\n>Band 6: Variety of complex structures.\n\nNot Band 8: Sentence length is uniform.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_454",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I attended a masquerade ball for charity last month. It was an elegant affair held in a grand ballroom in the city center. Everyone wore elaborate masks and formal attire, which added to the mystery. The atmosphere was enchanting, with dim lighting and soft music. We danced to a live orchestra, which played classical waltzes. I struck up a conversation with a stranger who turned out to be a famous author. The evening culminated with a raffle draw for expensive prizes. It was a memorable night filled with glamour and excitement. I thoroughly enjoyed the experience and would love to attend again.",
        "word_count": 103,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'masquerade ball', 'elegant affair', 'elaborate masks', 'attire', 'mystery', 'enchanting', 'orchestra', 'waltzes', 'struck up', 'culminated', 'raffle draw', 'glamour'. Band 7 level.",
             "grammar: 'affair held in', 'attire, which added', 'orchestra, which played', 'stranger who turned'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'masquerade ball', 'elegant affair', 'elaborate masks', 'attire', 'enchanting', 'struck up', 'culminated', 'glamour'. >Band 6: 'Culminated', 'enchanting'. Not Band 8: 'Memorable night' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'affair held in', 'attire, which added', 'stranger who turned'. >Band 6: Relative clauses and participle phrases used well. Not Band 8: Somewhat repetitive structure.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I attended a masquerade ball for charity last month. It was an elegant affair held in a grand ballroom in the city center. Everyone wore elaborate masks and formal attire, which added to the mystery. The atmosphere was enchanting, with dim lighting and soft music. We danced to a live orchestra, which played classical waltzes. I struck up a conversation with a stranger who turned out to be a famous author. The evening culminated with a raffle draw for expensive prizes. It was a memorable night filled with glamour and excitement. I thoroughly enjoyed the experience and would love to attend again.\n\nWord Count: 103 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'masquerade ball', 'elegant affair', 'elaborate masks', 'attire', 'enchanting', 'struck up', 'culminated', 'glamour'. \n\n>Band 6: 'Culminated', 'enchanting'.\n\nNot Band 8: 'Memorable night' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'affair held in', 'attire, which added', 'stranger who turned'. \n\n>Band 6: Relative clauses and participle phrases used well.\n\nNot Band 8: Somewhat repetitive structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_455",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "My e-reader is an indispensable gadget that I use every day. It allows me to carry hundreds of books in a lightweight device, which is perfect for commuting. The screen uses e-ink technology, which is easy on the eyes and reads like paper. I can adjust the font size and lighting to suit my preference. It has rekindled my love for reading because it is so convenient. I can download new titles instantly, no matter where I am in the world. It is a convenient tool for any bookworm who loves to read on the go. I consider it one of my best investments.",
        "word_count": 107,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'indispensable', 'gadget', 'lightweight', 'e-ink', 'technology', 'preference', 'rekindled', 'instantly', 'convenient', 'bookworm', 'investments'. Band 7 level.",
             "grammar: 'gadget that I use', 'device, which is', 'technology, which is', 'lighting to suit'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'indispensable', 'gadget', 'e-ink', 'technology', 'rekindled', 'instantly', 'bookworm', 'investments'. >Band 6: 'Rekindled', 'indispensable'. Not Band 8: 'Easy on the eyes' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'gadget that I use', 'device, which is', 'lighting to suit'. >Band 6: Complex structures used accurately. Not Band 8: Simple sentences included.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: My e-reader is an indispensable gadget that I use every day. It allows me to carry hundreds of books in a lightweight device, which is perfect for commuting. The screen uses e-ink technology, which is easy on the eyes and reads like paper. I can adjust the font size and lighting to suit my preference. It has rekindled my love for reading because it is so convenient. I can download new titles instantly, no matter where I am in the world. It is a convenient tool for any bookworm who loves to read on the go. I consider it one of my best investments.\n\nWord Count: 107 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'indispensable', 'gadget', 'e-ink', 'technology', 'rekindled', 'instantly', 'bookworm', 'investments'. \n\n>Band 6: 'Rekindled', 'indispensable'.\n\nNot Band 8: 'Easy on the eyes' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'gadget that I use', 'device, which is', 'lighting to suit'. \n\n>Band 6: Complex structures used accurately.\n\nNot Band 8: Simple sentences included.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_456",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place.",
        "transcript_cleaned": "I explored the ancient city of Petra in Jordan, which is often called the Rose City. It is carved directly into the red rock face, making it unique. The Treasury is the most iconic structure, featuring intricate architectural details. Walking through the narrow gorge to reach it built up the anticipation. It felt like stepping back in time to a different civilization. The scale of the engineering is impressive for its era. It is a UNESCO World Heritage site that truly deserves its reputation. I was overwhelmed by the beauty and history of the place. It was a highlight of my travels.",
        "word_count": 103,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'ancient city', 'carved', 'rock face', 'iconic', 'intricate', 'details', 'narrow gorge', 'anticipation', 'civilization', 'engineering', 'era', 'reputation'. Band 7 level.",
             "grammar: 'Jordan, which is', 'carved... making it', 'structure, featuring', 'gorge to reach'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'ancient city', 'carved', 'iconic', 'intricate details', 'narrow gorge', 'anticipation', 'civilization', 'engineering', 'reputation'. >Band 6: 'Iconic', 'anticipation'. Not Band 8: 'World Heritage site' is a proper noun.",
        "grammar_reason": "[GRA7] Key evidence: 'Jordan, which is', 'structure, featuring', 'gorge to reach'. >Band 6: Participle phrases and infinitives used well. Not Band 8: Lacks full range.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical place.\n\nTranscript: I explored the ancient city of Petra in Jordan, which is often called the Rose City. It is carved directly into the red rock face, making it unique. The Treasury is the most iconic structure, featuring intricate architectural details. Walking through the narrow gorge to reach it built up the anticipation. It felt like stepping back in time to a different civilization. The scale of the engineering is impressive for its era. It is a UNESCO World Heritage site that truly deserves its reputation. I was overwhelmed by the beauty and history of the place. It was a highlight of my travels.\n\nWord Count: 103 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'ancient city', 'carved', 'iconic', 'intricate details', 'narrow gorge', 'anticipation', 'civilization', 'engineering', 'reputation'. \n\n>Band 6: 'Iconic', 'anticipation'.\n\nNot Band 8: 'World Heritage site' is a proper noun.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Jordan, which is', 'structure, featuring', 'gorge to reach'. \n\n>Band 6: Participle phrases and infinitives used well.\n\nNot Band 8: Lacks full range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_457",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I am fond of the sunflower, which is a very cheerful plant. It is known for its tall stem and large yellow petals that resemble the sun. What fascinates me is how it turns its head to follow the sun across the sky. This phenomenon is called heliotropism. It symbolizes loyalty and adoration in many cultures. I grow them in my backyard because they brighten up the space instantly. Seeing them in full bloom brings a smile to my face every morning. They are a resilient and beautiful addition to any garden. I also harvest the seeds to eat as a snack.",
        "word_count": 103,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'fond of', 'stem', 'petals', 'resemble', 'fascinates', 'heliotropism', 'symbolizes', 'loyalty', 'adoration', 'brighten up', 'full bloom', 'resilient'. Band 7 level.",
             "grammar: 'sunflower, which is', 'petals that resemble', 'fascinates me is', 'turns its head to follow'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'fond of', 'resemble', 'fascinates', 'heliotropism', 'symbolizes', 'loyalty', 'adoration', 'brighten up', 'resilient'. >Band 6: 'Heliotropism', 'adoration'. Not Band 8: 'Smile to my face' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'sunflower, which is', 'fascinates me is', 'turns its head to follow'. >Band 6: Cleft sentences and relative clauses used accurately. Not Band 8: Some simple sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I am fond of the sunflower, which is a very cheerful plant. It is known for its tall stem and large yellow petals that resemble the sun. What fascinates me is how it turns its head to follow the sun across the sky. This phenomenon is called heliotropism. It symbolizes loyalty and adoration in many cultures. I grow them in my backyard because they brighten up the space instantly. Seeing them in full bloom brings a smile to my face every morning. They are a resilient and beautiful addition to any garden. I also harvest the seeds to eat as a snack.\n\nWord Count: 103 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'fond of', 'resemble', 'fascinates', 'heliotropism', 'symbolizes', 'loyalty', 'adoration', 'brighten up', 'resilient'. \n\n>Band 6: 'Heliotropism', 'adoration'.\n\nNot Band 8: 'Smile to my face' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'sunflower, which is', 'fascinates me is', 'turns its head to follow'. \n\n>Band 6: Cleft sentences and relative clauses used accurately.\n\nNot Band 8: Some simple sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_458",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "My friend David is a charismatic individual who works as a motivational speaker. He has an uncanny ability to connect with people from all walks of life. We met at a conference five years ago and have been friends since. He is always optimistic, even in the face of adversity. I value his honest feedback on my projects, which helps me improve. He pushes me to step out of my comfort zone and try new things. His friendship is a constant source of encouragement for me. I admire his energy and passion for helping others. He is truly a unique person.",
        "word_count": 101,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'charismatic', 'individual', 'motivational speaker', 'uncanny ability', 'walks of life', 'optimistic', 'adversity', 'feedback', 'comfort zone', 'encouragement', 'passion'. Band 7 level.",
             "grammar: 'individual who works', 'ability to connect', 'feedback... which helps', 'pushes me to step'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'charismatic', 'motivational speaker', 'uncanny ability', 'walks of life', 'optimistic', 'adversity', 'comfort zone', 'encouragement'. >Band 6: 'Uncanny', 'charismatic'. Not Band 8: 'Step out' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'individual who works', 'ability to connect', 'feedback... which helps'. >Band 6: Relative clauses and infinitives used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a friend.\n\nTranscript: My friend David is a charismatic individual who works as a motivational speaker. He has an uncanny ability to connect with people from all walks of life. We met at a conference five years ago and have been friends since. He is always optimistic, even in the face of adversity. I value his honest feedback on my projects, which helps me improve. He pushes me to step out of my comfort zone and try new things. His friendship is a constant source of encouragement for me. I admire his energy and passion for helping others. He is truly a unique person.\n\nWord Count: 101 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'charismatic', 'motivational speaker', 'uncanny ability', 'walks of life', 'optimistic', 'adversity', 'comfort zone', 'encouragement'. \n\n>Band 6: 'Uncanny', 'charismatic'.\n\nNot Band 8: 'Step out' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'individual who works', 'ability to connect', 'feedback... which helps'. \n\n>Band 6: Relative clauses and infinitives used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_459",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I had to choose a university major, which was a daunting decision. I was torn between studying law or graphic design. My parents pressured me to choose law for financial security, but my passion lay in the arts. I consulted a career counselor to weigh my options and get advice. Ultimately, I decided to pursue design because it felt right. It was a risky move, but I prioritized my happiness over money. I have never regretted following my heart. Now I work as a designer and love my job. It taught me to trust my instincts and make my own choices.",
        "word_count": 101,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'daunting', 'torn between', 'financial security', 'passion', 'consulted', 'weigh my options', 'ultimately', 'pursue', 'risky move', 'prioritized', 'regretted', 'instincts'. Band 7 level.",
             "grammar: 'major, which was', 'pressured me to choose', 'decided to pursue', 'risky move, but'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'daunting', 'torn between', 'financial security', 'passion', 'consulted', 'weigh my options', 'ultimately', 'risky move', 'prioritized', 'instincts'. >Band 6: 'Daunting', 'prioritized'. Not Band 8: 'Following my heart' is a cliché.",
        "grammar_reason": "[GRA7] Key evidence: 'major, which was', 'pressured me to choose', 'decided to pursue'. >Band 6: Relative clauses and infinitives used correctly. Not Band 8: Lacks full variety.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I had to choose a university major, which was a daunting decision. I was torn between studying law or graphic design. My parents pressured me to choose law for financial security, but my passion lay in the arts. I consulted a career counselor to weigh my options and get advice. Ultimately, I decided to pursue design because it felt right. It was a risky move, but I prioritized my happiness over money. I have never regretted following my heart. Now I work as a designer and love my job. It taught me to trust my instincts and make my own choices.\n\nWord Count: 101 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'daunting', 'torn between', 'financial security', 'passion', 'consulted', 'weigh my options', 'ultimately', 'risky move', 'prioritized', 'instincts'. \n\n>Band 6: 'Daunting', 'prioritized'.\n\nNot Band 8: 'Following my heart' is a cliché.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'major, which was', 'pressured me to choose', 'decided to pursue'. \n\n>Band 6: Relative clauses and infinitives used correctly.\n\nNot Band 8: Lacks full variety.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_460",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I entered a public speaking contest last year representing my school. The topic was environmental conservation, which I am passionate about. I spent weeks refining my speech and practicing my delivery. Standing on stage in front of a large audience was nerve-wracking. I focused on articulating my points clearly and maintaining eye contact. Although I stumbled on a few words, I managed to recover gracefully. I was awarded second place, which was a surprise. The experience significantly boosted my self-confidence and public speaking skills. I learned that preparation is key to success. I plan to participate again in the future.",
        "word_count": 100,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'contest', 'conservation', 'passionate', 'refining', 'delivery', 'nerve-wracking', 'articulating', 'maintaining', 'stumbled', 'recover', 'gracefully', 'boosted', 'self-confidence'. Band 7 level.",
             "grammar: 'conservation, which I am', 'Standing on stage... was', 'Although I stumbled', 'managed to recover'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'contest', 'conservation', 'refining', 'delivery', 'nerve-wracking', 'articulating', 'stumbled', 'recover', 'gracefully', 'boosted'. >Band 6: 'Articulating', 'nerve-wracking'. Not Band 8: 'Large audience' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'conservation, which I am', 'Standing on stage... was', 'Although I stumbled'. >Band 6: Gerund subjects and concessive clauses used correctly. Not Band 8: Simple sentence endings.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I entered a public speaking contest last year representing my school. The topic was environmental conservation, which I am passionate about. I spent weeks refining my speech and practicing my delivery. Standing on stage in front of a large audience was nerve-wracking. I focused on articulating my points clearly and maintaining eye contact. Although I stumbled on a few words, I managed to recover gracefully. I was awarded second place, which was a surprise. The experience significantly boosted my self-confidence and public speaking skills. I learned that preparation is key to success. I plan to participate again in the future.\n\nWord Count: 100 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'contest', 'conservation', 'refining', 'delivery', 'nerve-wracking', 'articulating', 'stumbled', 'recover', 'gracefully', 'boosted'. \n\n>Band 6: 'Articulating', 'nerve-wracking'.\n\nNot Band 8: 'Large audience' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'conservation, which I am', 'Standing on stage... was', 'Although I stumbled'. \n\n>Band 6: Gerund subjects and concessive clauses used correctly.\n\nNot Band 8: Simple sentence endings.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_461",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Leaning Tower of Pisa in Italy. It is famous for its unintended tilt, which makes it unique. The architecture is Romanesque, featuring beautiful marble arches. Climbing to the top was a dizzying experience due to the slant. I learned that the foundation was built on soft soil, causing it to lean. Engineers have stabilized it to prevent it from falling over. It is a quirky yet impressive monument. Seeing it in person was surreal and exciting. I took a photo pretending to hold it up. It is a memory I will cherish.",
        "word_count": 97,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'unintended tilt', 'Romanesque', 'featuring', 'dizzying', 'slant', 'foundation', 'stabilized', 'prevent', 'quirky', 'monument', 'surreal', 'cherish'. Band 7 level.",
             "grammar: 'tilt, which makes', 'Climbing... was', 'built on soft soil, causing', 'stabilized it to prevent'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'unintended tilt', 'Romanesque', 'dizzying', 'slant', 'foundation', 'stabilized', 'prevent', 'quirky', 'monument', 'surreal'. >Band 6: 'Quirky', 'dizzying'. Not Band 8: 'Falling over' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'tilt, which makes', 'Climbing... was', 'causing it to lean'. >Band 6: Gerunds and participle phrases used accurately. Not Band 8: Lacks full variety.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Leaning Tower of Pisa in Italy. It is famous for its unintended tilt, which makes it unique. The architecture is Romanesque, featuring beautiful marble arches. Climbing to the top was a dizzying experience due to the slant. I learned that the foundation was built on soft soil, causing it to lean. Engineers have stabilized it to prevent it from falling over. It is a quirky yet impressive monument. Seeing it in person was surreal and exciting. I took a photo pretending to hold it up. It is a memory I will cherish.\n\nWord Count: 97 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'unintended tilt', 'Romanesque', 'dizzying', 'slant', 'foundation', 'stabilized', 'prevent', 'quirky', 'monument', 'surreal'. \n\n>Band 6: 'Quirky', 'dizzying'.\n\nNot Band 8: 'Falling over' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'tilt, which makes', 'Climbing... was', 'causing it to lean'. \n\n>Band 6: Gerunds and participle phrases used accurately.\n\nNot Band 8: Lacks full variety.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_462",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "Renovating my kitchen was a laborious project that I undertook recently. I decided to do it myself to save money. I had to learn how to install tiles and fix the plumbing. It involved heavy lifting and precise measurements. There were moments of frustration when things went wrong. However, seeing the finished result was incredibly satisfying. It taught me the value of patience and hard work. I am proud of what I accomplished with my own hands. My kitchen looks modern and fresh now. It was worth all the sweat and effort.",
        "word_count": 94,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'renovating', 'laborious', 'undertook', 'install tiles', 'plumbing', 'heavy lifting', 'precise measurements', 'frustration', 'satisfying', 'accomplished', 'modern'. Band 7 level.",
             "grammar: 'project that I undertook', 'decided to do', 'learn how to install', 'seeing... was satisfying'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'renovating', 'laborious', 'undertook', 'install tiles', 'plumbing', 'heavy lifting', 'precise measurements', 'frustration', 'satisfying'. >Band 6: 'Laborious', 'precise'. Not Band 8: 'Save money' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'project that I undertook', 'learn how to install', 'seeing... was satisfying'. >Band 6: Complex structures used accurately. Not Band 8: Sentences are somewhat short.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: Renovating my kitchen was a laborious project that I undertook recently. I decided to do it myself to save money. I had to learn how to install tiles and fix the plumbing. It involved heavy lifting and precise measurements. There were moments of frustration when things went wrong. However, seeing the finished result was incredibly satisfying. It taught me the value of patience and hard work. I am proud of what I accomplished with my own hands. My kitchen looks modern and fresh now. It was worth all the sweat and effort.\n\nWord Count: 94 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'renovating', 'laborious', 'undertook', 'install tiles', 'plumbing', 'heavy lifting', 'precise measurements', 'frustration', 'satisfying'. \n\n>Band 6: 'Laborious', 'precise'.\n\nNot Band 8: 'Save money' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'project that I undertook', 'learn how to install', 'seeing... was satisfying'. \n\n>Band 6: Complex structures used accurately.\n\nNot Band 8: Sentences are somewhat short.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_463",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I enjoyed reading The Great Gatsby by F. Scott Fitzgerald. It is a critique of the American Dream set in the roaring twenties. The descriptions of the lavish parties are vivid and colorful. The protagonist, Jay Gatsby, is an enigmatic figure who throws parties hoping to see his lost love. His obsession with the past is tragic. The novel explores themes of wealth, love, and disillusionment. The writing style is elegant and poetic. It left a lasting impression on me. It is considered a masterpiece of American literature. I highly recommend it.",
        "word_count": 94,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'critique', 'American Dream', 'roaring twenties', 'lavish', 'vivid', 'protagonist', 'enigmatic', 'obsession', 'tragic', 'disillusionment', 'poetic', 'masterpiece'. Band 7 level.",
             "grammar: 'set in the roaring twenties', 'figure who throws', 'obsession... is tragic'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'critique', 'American Dream', 'roaring twenties', 'lavish', 'vivid', 'protagonist', 'enigmatic', 'obsession', 'tragic', 'disillusionment', 'poetic'. >Band 6: 'Enigmatic', 'disillusionment'. Not Band 8: 'Parties' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'set in the roaring twenties', 'figure who throws', 'obsession... is tragic'. >Band 6: Participle phrases and complex noun phrases used correctly. Not Band 8: Simple sentence structure.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I enjoyed reading The Great Gatsby by F. Scott Fitzgerald. It is a critique of the American Dream set in the roaring twenties. The descriptions of the lavish parties are vivid and colorful. The protagonist, Jay Gatsby, is an enigmatic figure who throws parties hoping to see his lost love. His obsession with the past is tragic. The novel explores themes of wealth, love, and disillusionment. The writing style is elegant and poetic. It left a lasting impression on me. It is considered a masterpiece of American literature. I highly recommend it.\n\nWord Count: 94 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'critique', 'American Dream', 'roaring twenties', 'lavish', 'vivid', 'protagonist', 'enigmatic', 'obsession', 'tragic', 'disillusionment', 'poetic'. \n\n>Band 6: 'Enigmatic', 'disillusionment'.\n\nNot Band 8: 'Parties' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'set in the roaring twenties', 'figure who throws', 'obsession... is tragic'. \n\n>Band 6: Participle phrases and complex noun phrases used correctly.\n\nNot Band 8: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_464",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I organized a farewell party for my colleague who was retiring. It was a bittersweet occasion held at a cozy cafe. I prepared a speech to acknowledge his contributions to the company. We gifted him a personalized watch as a token of appreciation. Everyone shared funny anecdotes about working with him over the years. There were tears and laughter. We promised to stay in touch and meet up. It was a heartfelt send-off for a great friend. I felt happy to be part of it.",
        "word_count": 87,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'farewell', 'retiring', 'bittersweet', 'acknowledge', 'contributions', 'personalized', 'token of appreciation', 'anecdotes', 'heartfelt', 'send-off'. Band 7 level.",
             "grammar: 'colleague who was retiring', 'speech to acknowledge', 'anecdotes about working'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'farewell', 'bittersweet', 'acknowledge', 'contributions', 'personalized', 'token of appreciation', 'anecdotes', 'heartfelt', 'send-off'. >Band 6: 'Bittersweet', 'anecdotes'. Not Band 8: 'Stay in touch' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'colleague who was retiring', 'speech to acknowledge', 'anecdotes about working'. >Band 6: Infinitives and gerunds used correctly. Not Band 8: Sentences are similar in length.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I organized a farewell party for my colleague who was retiring. It was a bittersweet occasion held at a cozy cafe. I prepared a speech to acknowledge his contributions to the company. We gifted him a personalized watch as a token of appreciation. Everyone shared funny anecdotes about working with him over the years. There were tears and laughter. We promised to stay in touch and meet up. It was a heartfelt send-off for a great friend. I felt happy to be part of it.\n\nWord Count: 87 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'farewell', 'bittersweet', 'acknowledge', 'contributions', 'personalized', 'token of appreciation', 'anecdotes', 'heartfelt', 'send-off'. \n\n>Band 6: 'Bittersweet', 'anecdotes'.\n\nNot Band 8: 'Stay in touch' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'colleague who was retiring', 'speech to acknowledge', 'anecdotes about working'. \n\n>Band 6: Infinitives and gerunds used correctly.\n\nNot Band 8: Sentences are similar in length.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_465",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I use a fitness tracker daily to monitor my health. It monitors my heart rate, steps, and sleep quality. It motivates me to lead a sedentary lifestyle less and move more. I can sync it with my phone to track my progress over time. It alerts me when I have been sitting for too long. It is waterproof, so I can wear it while swimming. It has become an integral part of my wellness routine. I feel more in control of my health now.",
        "word_count": 87,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'fitness tracker', 'monitor', 'heart rate', 'motivates', 'sedentary', 'sync', 'track', 'progress', 'alerts', 'integral', 'wellness routine'. Band 7 level.",
             "grammar: 'motivates me to lead', 'sync it with', 'alerts me when', 'wear it while swimming'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'fitness tracker', 'monitors', 'heart rate', 'sedentary', 'sync', 'track progress', 'alerts', 'integral', 'wellness routine'. >Band 6: 'Sedentary', 'integral'. Not Band 8: 'Swimming' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'motivates me to lead', 'alerts me when', 'so I can wear'. >Band 6: Infinitives and causal clauses used correctly. Not Band 8: Simple sentence structure.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I use a fitness tracker daily to monitor my health. It monitors my heart rate, steps, and sleep quality. It motivates me to lead a sedentary lifestyle less and move more. I can sync it with my phone to track my progress over time. It alerts me when I have been sitting for too long. It is waterproof, so I can wear it while swimming. It has become an integral part of my wellness routine. I feel more in control of my health now.\n\nWord Count: 87 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'fitness tracker', 'monitors', 'heart rate', 'sedentary', 'sync', 'track progress', 'alerts', 'integral', 'wellness routine'. \n\n>Band 6: 'Sedentary', 'integral'.\n\nNot Band 8: 'Swimming' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'motivates me to lead', 'alerts me when', 'so I can wear'. \n\n>Band 6: Infinitives and causal clauses used correctly.\n\nNot Band 8: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_466",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Alhambra in Spain last year. It is a stunning fortress complex located in Granada. The Islamic architecture features intricate tile work and beautiful courtyards. The Generalife gardens are a highlight, with flowing water features and flowers. I was captivated by the history of the Moorish rulers who built it. The view of the city from the ramparts is spectacular. It is a testament to a rich cultural past. Walking through it felt like being in a different world.",
        "word_count": 83,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'fortress complex', 'Islamic architecture', 'intricate', 'highlight', 'captivated', 'Moorish', 'ramparts', 'spectacular', 'testament', 'cultural past'. Band 7 level.",
             "grammar: 'features intricate tile work', 'rulers who built it', 'view... is spectacular'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'fortress complex', 'Islamic architecture', 'intricate', 'highlight', 'captivated', 'Moorish', 'ramparts', 'testament', 'cultural past'. >Band 6: 'Captivated', 'testament'. Not Band 8: 'Gardens' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'features intricate tile work', 'view... is spectacular'. >Band 6: Complex noun phrases used correctly. Not Band 8: Lacks full variety.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Alhambra in Spain last year. It is a stunning fortress complex located in Granada. The Islamic architecture features intricate tile work and beautiful courtyards. The Generalife gardens are a highlight, with flowing water features and flowers. I was captivated by the history of the Moorish rulers who built it. The view of the city from the ramparts is spectacular. It is a testament to a rich cultural past. Walking through it felt like being in a different world.\n\nWord Count: 83 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'fortress complex', 'Islamic architecture', 'intricate', 'highlight', 'captivated', 'Moorish', 'ramparts', 'testament', 'cultural past'. \n\n>Band 6: 'Captivated', 'testament'.\n\nNot Band 8: 'Gardens' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'features intricate tile work', 'view... is spectacular'. \n\n>Band 6: Complex noun phrases used correctly.\n\nNot Band 8: Lacks full variety.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_467",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "Writing my master's thesis was an arduous journey. It required extensive research and critical analysis. I spent countless hours in the library reading books. I struggled with writer's block occasionally, which was frustrating. My supervisor provided valuable guidance and feedback. Editing the draft was tedious but necessary. Submitting the final copy felt like a weight off my shoulders. It was a significant academic achievement for me. I learned a lot about discipline and time management.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'arduous journey', 'extensive research', 'critical analysis', 'countless', 'writer's block', 'guidance', 'tedious', 'weight off my shoulders', 'academic achievement'. Band 7 level.",
             "grammar: 'required extensive research', 'Editing... was tedious'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'thesis', 'arduous', 'extensive research', 'critical analysis', 'writer's block', 'guidance', 'tedious', 'weight off my shoulders', 'academic achievement'. >Band 6: 'Arduous', 'critical'. Not Band 8: 'Library' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'required extensive research', 'Editing... was tedious'. >Band 6: Gerund subjects and complex noun phrases used correctly. Not Band 8: Short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: Writing my master's thesis was an arduous journey. It required extensive research and critical analysis. I spent countless hours in the library reading books. I struggled with writer's block occasionally, which was frustrating. My supervisor provided valuable guidance and feedback. Editing the draft was tedious but necessary. Submitting the final copy felt like a weight off my shoulders. It was a significant academic achievement for me. I learned a lot about discipline and time management.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'thesis', 'arduous', 'extensive research', 'critical analysis', 'writer's block', 'guidance', 'tedious', 'weight off my shoulders', 'academic achievement'. \n\n>Band 6: 'Arduous', 'critical'.\n\nNot Band 8: 'Library' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'required extensive research', 'Editing... was tedious'. \n\n>Band 6: Gerund subjects and complex noun phrases used correctly.\n\nNot Band 8: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_468",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read The Catcher in the Rye. It portrays teenage angst and rebellion perfectly. The protagonist, Holden Caulfield, is cynical about the adult world. He wanders around New York City feeling alienated. The voice of the narrator is distinctive and authentic. It explores themes of innocence and loss. It is a classic coming-of-age story that resonates with many. I found it very moving and relatable.",
        "word_count": 66,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'portrays', 'angst', 'rebellion', 'protagonist', 'cynical', 'wanders', 'alienated', 'distinctive', 'authentic', 'innocence', 'coming-of-age', 'resonates'. Band 7 level.",
             "grammar: 'cynical about', 'feeling alienated', 'story that resonates'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'portrays', 'angst', 'rebellion', 'protagonist', 'cynical', 'wanders', 'alienated', 'distinctive', 'authentic', 'innocence', 'coming-of-age', 'resonates'. >Band 6: 'Cynical', 'alienated'. Not Band 8: 'Adult world' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'feeling alienated', 'story that resonates'. >Band 6: Participle phrases and relative clauses used correctly. Not Band 8: Simple sentence structure.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read The Catcher in the Rye. It portrays teenage angst and rebellion perfectly. The protagonist, Holden Caulfield, is cynical about the adult world. He wanders around New York City feeling alienated. The voice of the narrator is distinctive and authentic. It explores themes of innocence and loss. It is a classic coming-of-age story that resonates with many. I found it very moving and relatable.\n\nWord Count: 66 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'portrays', 'angst', 'rebellion', 'protagonist', 'cynical', 'wanders', 'alienated', 'distinctive', 'authentic', 'innocence', 'coming-of-age', 'resonates'. \n\n>Band 6: 'Cynical', 'alienated'.\n\nNot Band 8: 'Adult world' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'feeling alienated', 'story that resonates'. \n\n>Band 6: Participle phrases and relative clauses used correctly.\n\nNot Band 8: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_469",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I threw a barbecue party in my backyard last weekend. The weather was perfect for grilling outdoors. I marinated the meat overnight for extra flavor. My friends brought side dishes and drinks to share. We played music and chatted until late at night. The atmosphere was casual and relaxed. It was a great way to unwind after a busy week. Everyone complimented the food. We had a great time together.",
        "word_count": 70,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'barbecue', 'grilling', 'marinated', 'side dishes', 'casual', 'relaxed', 'unwind', 'complimented'. Band 7 level.",
             "grammar: 'perfect for grilling', 'way to unwind'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'barbecue', 'grilling', 'marinated', 'overnight', 'side dishes', 'casual', 'relaxed', 'unwind', 'complimented'. >Band 6: 'Marinated', 'unwind'. Not Band 8: 'Drinks' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'perfect for grilling', 'way to unwind'. >Band 6: Prepositional phrases and infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I threw a barbecue party in my backyard last weekend. The weather was perfect for grilling outdoors. I marinated the meat overnight for extra flavor. My friends brought side dishes and drinks to share. We played music and chatted until late at night. The atmosphere was casual and relaxed. It was a great way to unwind after a busy week. Everyone complimented the food. We had a great time together.\n\nWord Count: 70 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'barbecue', 'grilling', 'marinated', 'overnight', 'side dishes', 'casual', 'relaxed', 'unwind', 'complimented'. \n\n>Band 6: 'Marinated', 'unwind'.\n\nNot Band 8: 'Drinks' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'perfect for grilling', 'way to unwind'. \n\n>Band 6: Prepositional phrases and infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_470",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I use a noise-cancelling headset at work to focus. It blocks out background distractions effectively. I can focus on my tasks without interruption. The sound quality is crisp for calls and music. It is comfortable to wear for long periods. It is an essential tool for maintaining productivity in an open-plan office. I highly recommend it to anyone who works in a noisy environment.",
        "word_count": 65,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'noise-cancelling', 'blocks out', 'distractions', 'effectively', 'interruption', 'crisp', 'essential', 'maintaining', 'productivity', 'open-plan'. Band 7 level.",
             "grammar: 'blocks out', 'focus... without interruption'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'noise-cancelling', 'blocks out', 'distractions', 'effectively', 'interruption', 'crisp', 'essential', 'maintaining', 'productivity', 'open-plan'. >Band 6: 'Productivity', 'distractions'. Not Band 8: 'Tool' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'focus... without interruption', 'wear for long periods'. >Band 6: Prepositional phrases used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I use a noise-cancelling headset at work to focus. It blocks out background distractions effectively. I can focus on my tasks without interruption. The sound quality is crisp for calls and music. It is comfortable to wear for long periods. It is an essential tool for maintaining productivity in an open-plan office. I highly recommend it to anyone who works in a noisy environment.\n\nWord Count: 65 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'noise-cancelling', 'blocks out', 'distractions', 'effectively', 'interruption', 'crisp', 'essential', 'maintaining', 'productivity', 'open-plan'. \n\n>Band 6: 'Productivity', 'distractions'.\n\nNot Band 8: 'Tool' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'focus... without interruption', 'wear for long periods'. \n\n>Band 6: Prepositional phrases used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_471",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Tower of London. It has a gruesome history as a prison. I saw the Crown Jewels, which were dazzling. The Yeoman Warders gave an entertaining tour. They shared stories of executions and intrigue. The medieval architecture is imposing. It is a key part of British heritage. I learned a lot about the royal family.",
        "word_count": 57,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'gruesome', 'prison', 'dazzling', 'entertaining', 'executions', 'intrigue', 'medieval', 'imposing', 'heritage'. Band 7 level.",
             "grammar: 'Jewels, which were', 'history as a prison'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'gruesome', 'prison', 'dazzling', 'Yeoman Warders', 'entertaining', 'executions', 'intrigue', 'medieval', 'imposing', 'heritage'. >Band 6: 'Gruesome', 'intrigue'. Not Band 8: 'Stories' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'Jewels, which were', 'history as a prison'. >Band 6: Relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Tower of London. It has a gruesome history as a prison. I saw the Crown Jewels, which were dazzling. The Yeoman Warders gave an entertaining tour. They shared stories of executions and intrigue. The medieval architecture is imposing. It is a key part of British heritage. I learned a lot about the royal family.\n\nWord Count: 57 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'gruesome', 'prison', 'dazzling', 'Yeoman Warders', 'entertaining', 'executions', 'intrigue', 'medieval', 'imposing', 'heritage'. \n\n>Band 6: 'Gruesome', 'intrigue'.\n\nNot Band 8: 'Stories' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Jewels, which were', 'history as a prison'. \n\n>Band 6: Relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_472",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I had to give a presentation to senior management. I was anxious about public speaking. I prepared thoroughly by researching the data. I practiced my delivery in front of a mirror. I anticipated potential questions. The presentation went smoothly. I received positive feedback. It was a confidence-building experience. I felt very proud of myself.",
        "word_count": 54,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'senior management', 'anxious', 'thoroughly', 'researching', 'delivery', 'anticipated', 'potential', 'smoothly', 'positive feedback', 'confidence-building'. Band 7 level.",
             "grammar: 'anxious about', 'thoroughly by researching'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'senior management', 'anxious', 'thoroughly', 'researching', 'delivery', 'anticipated', 'potential', 'smoothly', 'positive feedback', 'confidence-building'. >Band 6: 'Anticipated', 'thoroughly'. Not Band 8: 'Mirror' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'thoroughly by researching', 'practiced... in front of'. >Band 6: Prepositional phrases and gerunds used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I had to give a presentation to senior management. I was anxious about public speaking. I prepared thoroughly by researching the data. I practiced my delivery in front of a mirror. I anticipated potential questions. The presentation went smoothly. I received positive feedback. It was a confidence-building experience. I felt very proud of myself.\n\nWord Count: 54 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'senior management', 'anxious', 'thoroughly', 'researching', 'delivery', 'anticipated', 'potential', 'smoothly', 'positive feedback', 'confidence-building'. \n\n>Band 6: 'Anticipated', 'thoroughly'.\n\nNot Band 8: 'Mirror' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'thoroughly by researching', 'practiced... in front of'. \n\n>Band 6: Prepositional phrases and gerunds used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_473",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read The Hobbit by Tolkien. It is a fantasy adventure involving dwarves and a dragon. The world-building is immersive. Bilbo Baggins is a reluctant hero. He faces many perils on his journey. The story highlights the importance of courage. It is a delightful prelude to The Lord of the Rings. It is a classic of fantasy literature.",
        "word_count": 57,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'fantasy adventure', 'dwarves', 'world-building', 'immersive', 'reluctant hero', 'perils', 'highlights', 'courage', 'delightful prelude'. Band 7 level.",
             "grammar: 'adventure involving', 'highlights the importance'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'fantasy adventure', 'dwarves', 'world-building', 'immersive', 'reluctant hero', 'perils', 'highlights', 'courage', 'delightful prelude'. >Band 6: 'Immersive', 'perils'. Not Band 8: 'Dragon' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'adventure involving', 'highlights the importance'. >Band 6: Participle phrases used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read The Hobbit by Tolkien. It is a fantasy adventure involving dwarves and a dragon. The world-building is immersive. Bilbo Baggins is a reluctant hero. He faces many perils on his journey. The story highlights the importance of courage. It is a delightful prelude to The Lord of the Rings. It is a classic of fantasy literature.\n\nWord Count: 57 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'fantasy adventure', 'dwarves', 'world-building', 'immersive', 'reluctant hero', 'perils', 'highlights', 'courage', 'delightful prelude'. \n\n>Band 6: 'Immersive', 'perils'.\n\nNot Band 8: 'Dragon' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'adventure involving', 'highlights the importance'. \n\n>Band 6: Participle phrases used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_474",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I attended a costume party for Halloween. I dressed up as a pirate. The decorations were spooky, with cobwebs and pumpkins. We played games like bobbing for apples. The music was eerie and atmospheric. I won a prize for best costume. It was a fun-filled night of frights. Everyone was in a good mood.",
        "word_count": 54,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'costume party', 'dressed up', 'spooky', 'cobwebs', 'pumpkins', 'bobbing', 'eerie', 'atmospheric', 'fun-filled', 'frights'. Band 7 level.",
             "grammar: 'dressed up as', 'games like bobbing'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'costume party', 'dressed up', 'spooky', 'cobwebs', 'pumpkins', 'bobbing', 'eerie', 'atmospheric', 'fun-filled', 'frights'. >Band 6: 'Atmospheric', 'eerie'. Not Band 8: 'Prize' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'dressed up as', 'games like bobbing'. >Band 6: Phrasal verbs and comparisons used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I attended a costume party for Halloween. I dressed up as a pirate. The decorations were spooky, with cobwebs and pumpkins. We played games like bobbing for apples. The music was eerie and atmospheric. I won a prize for best costume. It was a fun-filled night of frights. Everyone was in a good mood.\n\nWord Count: 54 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'costume party', 'dressed up', 'spooky', 'cobwebs', 'pumpkins', 'bobbing', 'eerie', 'atmospheric', 'fun-filled', 'frights'. \n\n>Band 6: 'Atmospheric', 'eerie'.\n\nNot Band 8: 'Prize' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'dressed up as', 'games like bobbing'. \n\n>Band 6: Phrasal verbs and comparisons used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_475",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I bought a blender to make smoothies. It has a powerful motor. I can blend frozen fruit and ice easily. It helps me consume more vitamins. It is easy to clean. I use it every morning for a quick breakfast. It is a convenient appliance for a healthy lifestyle. I feel better since I started using it.",
        "word_count": 57,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'blender', 'smoothies', 'powerful motor', 'blend', 'frozen fruit', 'consume', 'vitamins', 'appliance', 'healthy lifestyle'. Band 7 level.",
             "grammar: 'blender to make', 'helps me consume'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'blender', 'smoothies', 'powerful motor', 'blend', 'frozen fruit', 'consume', 'vitamins', 'appliance', 'healthy lifestyle'. >Band 6: 'Consume', 'appliance'. Not Band 8: 'Ice' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'blender to make', 'helps me consume'. >Band 6: Infinitives and causal structures used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I bought a blender to make smoothies. It has a powerful motor. I can blend frozen fruit and ice easily. It helps me consume more vitamins. It is easy to clean. I use it every morning for a quick breakfast. It is a convenient appliance for a healthy lifestyle. I feel better since I started using it.\n\nWord Count: 57 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'blender', 'smoothies', 'powerful motor', 'blend', 'frozen fruit', 'consume', 'vitamins', 'appliance', 'healthy lifestyle'. \n\n>Band 6: 'Consume', 'appliance'.\n\nNot Band 8: 'Ice' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'blender to make', 'helps me consume'. \n\n>Band 6: Infinitives and causal structures used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
