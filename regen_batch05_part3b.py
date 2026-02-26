import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch05.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v7_g6_413",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "My best friend is a talented musician. She plays the violin with great passion. We have known each other since childhood. She is incredibly supportive and trustworthy. We often collaborate on creative projects. She has a bubbly personality that lights up the room. Even when we disagree, we resolve our conflicts maturely. Our friendship is a bond that I cherish. I admire her dedication to her art. She practices for hours every day. She is an inspiration to me. I am lucky to have her as a friend.",
        "word_count": 87,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'lights up the room' (idiom). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'talented', 'passion', 'collaborate', 'bubbly personality', 'lights up the room', 'resolve', 'conflicts', 'maturely', 'cherish', 'dedication', 'inspiration'. >Band 6: 'Collaborate', 'maturely'. Not Band 8: 'Trustworthy' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'Even when we disagree', 'friendship is a bond that'. >Band 5: Mix of structures. Not Band 7: Short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a friend.\n\nTranscript: My best friend is a talented musician. She plays the violin with great passion. We have known each other since childhood. She is incredibly supportive and trustworthy. We often collaborate on creative projects. She has a bubbly personality that lights up the room. Even when we disagree, we resolve our conflicts maturely. Our friendship is a bond that I cherish. I admire her dedication to her art. She practices for hours every day. She is an inspiration to me. I am lucky to have her as a friend.\n\nWord Count: 87 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'talented', 'passion', 'collaborate', 'bubbly personality', 'lights up the room', 'resolve', 'conflicts', 'maturely', 'cherish', 'dedication', 'inspiration'. \n\n>Band 6: 'Collaborate', 'maturely'.\n\nNot Band 8: 'Trustworthy' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'Even when we disagree', 'friendship is a bond that'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_414",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I had to decide whether to accept a job offer in another city. It was a lucrative opportunity, but it meant leaving my family. I weighed the pros and cons carefully. The relocation would be stressful. However, the career advancement was tempting. I sought advice from my mentors. Ultimately, I decided to take the leap of faith. It was a pivotal moment in my life. It was not an easy choice to make. I missed my friends at first. But I adapted to the new environment. I think it was the right decision.",
        "word_count": 93,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'weighed the pros and cons' (idiom). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'lucrative', 'pros and cons', 'relocation', 'career advancement', 'tempting', 'mentors', 'leap of faith', 'pivotal', 'adapted'. >Band 6: 'Lucrative', 'pivotal'. Not Band 8: 'Job offer' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'whether to accept', 'opportunity, but it meant'. >Band 5: Mix of structures. Not Band 7: Short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I had to decide whether to accept a job offer in another city. It was a lucrative opportunity, but it meant leaving my family. I weighed the pros and cons carefully. The relocation would be stressful. However, the career advancement was tempting. I sought advice from my mentors. Ultimately, I decided to take the leap of faith. It was a pivotal moment in my life. It was not an easy choice to make. I missed my friends at first. But I adapted to the new environment. I think it was the right decision.\n\nWord Count: 93 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'lucrative', 'pros and cons', 'relocation', 'career advancement', 'tempting', 'mentors', 'leap of faith', 'pivotal', 'adapted'. \n\n>Band 6: 'Lucrative', 'pivotal'.\n\nNot Band 8: 'Job offer' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'whether to accept', 'opportunity, but it meant'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_415",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I participated in a chess tournament. I have been playing chess for years. The competition was fierce. I had to devise a strategic plan to defeat my opponents. Each game required intense concentration. I won several matches but lost the final one. Despite the loss, I was proud of my performance. It was a stimulating intellectual challenge. I practiced every day before the tournament. I studied the games of grandmasters. It helped me improve my skills. I want to compete again next year.",
        "word_count": 83,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'devise a strategic plan' (collocation). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'tournament', 'fierce', 'devise', 'strategic', 'opponents', 'intense concentration', 'stimulating', 'intellectual challenge', 'grandmasters'. >Band 6: 'Devise', 'stimulating'. Not Band 8: 'Chess' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'plan to defeat', 'Despite the loss'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I participated in a chess tournament. I have been playing chess for years. The competition was fierce. I had to devise a strategic plan to defeat my opponents. Each game required intense concentration. I won several matches but lost the final one. Despite the loss, I was proud of my performance. It was a stimulating intellectual challenge. I practiced every day before the tournament. I studied the games of grandmasters. It helped me improve my skills. I want to compete again next year.\n\nWord Count: 83 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'tournament', 'fierce', 'devise', 'strategic', 'opponents', 'intense concentration', 'stimulating', 'intellectual challenge', 'grandmasters'. \n\n>Band 6: 'Devise', 'stimulating'.\n\nNot Band 8: 'Chess' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'plan to defeat', 'Despite the loss'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_416",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Taj Mahal in India. It is an architectural marvel made of white marble. The intricate carvings are breathtaking. It was built as a mausoleum for the emperor's wife. The symmetry of the building is perfect. I was mesmerized by its beauty at sunrise. It is a symbol of eternal love. The history behind it is poignant and romantic. I spent hours walking around the gardens. The reflection in the pool was stunning. It is one of the most beautiful places I have ever seen. It attracts millions of tourists every year.",
        "word_count": 94,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'architectural marvel' (noun phrase). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'architectural marvel', 'marble', 'intricate carvings', 'breathtaking', 'mausoleum', 'symmetry', 'mesmerized', 'eternal love', 'poignant', 'reflection'. >Band 6: 'Mesmerized', 'poignant'. Not Band 8: 'Symbol' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'made of white marble', 'built as a mausoleum'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Taj Mahal in India. It is an architectural marvel made of white marble. The intricate carvings are breathtaking. It was built as a mausoleum for the emperor's wife. The symmetry of the building is perfect. I was mesmerized by its beauty at sunrise. It is a symbol of eternal love. The history behind it is poignant and romantic. I spent hours walking around the gardens. The reflection in the pool was stunning. It is one of the most beautiful places I have ever seen. It attracts millions of tourists every year.\n\nWord Count: 94 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'architectural marvel', 'marble', 'intricate carvings', 'breathtaking', 'mausoleum', 'symmetry', 'mesmerized', 'eternal love', 'poignant', 'reflection'. \n\n>Band 6: 'Mesmerized', 'poignant'.\n\nNot Band 8: 'Symbol' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'made of white marble', 'built as a mausoleum'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_417",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "Learning a new language was a rigorous process. I chose to learn Japanese. The writing system is complex and distinct from English. I attended classes and practiced daily. Memorizing vocabulary was tedious. I struggled with pronunciation initially. However, mastering basic conversation was rewarding. It opened doors to a new culture. It required dedication and perseverance. I watched Japanese movies to improve my listening skills. I also tried to speak with native speakers. It was hard to overcome my fear of making mistakes. But I kept trying. Now I can travel to Japan with confidence.",
        "word_count": 93,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'rigorous process' (collocation). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'rigorous', 'distinct', 'memorizing', 'tedious', 'struggled', 'initially', 'mastering', 'rewarding', 'opened doors', 'dedication', 'perseverance'. >Band 6: 'Rigorous', 'tedious'. Not Band 8: 'Japanese' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'chose to learn', 'mastering... was rewarding'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: Learning a new language was a rigorous process. I chose to learn Japanese. The writing system is complex and distinct from English. I attended classes and practiced daily. Memorizing vocabulary was tedious. I struggled with pronunciation initially. However, mastering basic conversation was rewarding. It opened doors to a new culture. It required dedication and perseverance. I watched Japanese movies to improve my listening skills. I also tried to speak with native speakers. It was hard to overcome my fear of making mistakes. But I kept trying. Now I can travel to Japan with confidence.\n\nWord Count: 93 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'rigorous', 'distinct', 'memorizing', 'tedious', 'struggled', 'initially', 'mastering', 'rewarding', 'opened doors', 'dedication', 'perseverance'. \n\n>Band 6: 'Rigorous', 'tedious'.\n\nNot Band 8: 'Japanese' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'chose to learn', 'mastering... was rewarding'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_418",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I enjoyed reading The Alchemist. It is a philosophical novel about following your dreams. The narrative is simple yet profound. The protagonist's journey is inspiring. It teaches valuable life lessons about destiny. The prose is evocative. I found the underlying message to be uplifting. It resonated with me on a personal level. I have read it multiple times. Each time, I find new meaning. It is a book that everyone should have on their shelf. It reminds us to listen to our hearts.",
        "word_count": 83,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'philosophical novel' (collocation). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'philosophical', 'narrative', 'profound', 'protagonist', 'inspiring', 'destiny', 'prose', 'evocative', 'underlying message', 'uplifting', 'resonated'. >Band 6: 'Profound', 'evocative'. Not Band 8: 'Dreams' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'novel about following', 'found... to be'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I enjoyed reading The Alchemist. It is a philosophical novel about following your dreams. The narrative is simple yet profound. The protagonist's journey is inspiring. It teaches valuable life lessons about destiny. The prose is evocative. I found the underlying message to be uplifting. It resonated with me on a personal level. I have read it multiple times. Each time, I find new meaning. It is a book that everyone should have on their shelf. It reminds us to listen to our hearts.\n\nWord Count: 83 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'philosophical', 'narrative', 'profound', 'protagonist', 'inspiring', 'destiny', 'prose', 'evocative', 'underlying message', 'uplifting', 'resonated'. \n\n>Band 6: 'Profound', 'evocative'.\n\nNot Band 8: 'Dreams' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'novel about following', 'found... to be'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_419",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I threw a surprise party for my sister. It required meticulous planning. I invited her close friends and family. We decorated the house with balloons and streamers. When she arrived, we shouted surprise. She was genuinely shocked and delighted. We had a buffet with delicious appetizers. The atmosphere was convivial. It was a joyous occasion that brought everyone together. I was happy that everything went according to plan. My sister said it was the best birthday she ever had. Seeing her smile was worth all the effort.",
        "word_count": 86,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'meticulous planning' (collocation). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'meticulous planning', 'genuinely', 'shocked', 'delighted', 'buffet', 'appetizers', 'convivial', 'joyous occasion'. >Band 6: 'Meticulous', 'convivial'. Not Band 8: 'Balloons' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'When she arrived', 'occasion that brought'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I threw a surprise party for my sister. It required meticulous planning. I invited her close friends and family. We decorated the house with balloons and streamers. When she arrived, we shouted surprise. She was genuinely shocked and delighted. We had a buffet with delicious appetizers. The atmosphere was convivial. It was a joyous occasion that brought everyone together. I was happy that everything went according to plan. My sister said it was the best birthday she ever had. Seeing her smile was worth all the effort.\n\nWord Count: 86 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'meticulous planning', 'genuinely', 'shocked', 'delighted', 'buffet', 'appetizers', 'convivial', 'joyous occasion'. \n\n>Band 6: 'Meticulous', 'convivial'.\n\nNot Band 8: 'Balloons' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'When she arrived', 'occasion that brought'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_420",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I rely on my laptop for work. It is a high-performance machine. I use it to draft reports and analyze data. The processing speed is lightning fast. It allows me to multitask efficiently. I also use it for video conferencing with clients. It is compact and portable. It is an essential asset for my profession. I can work from anywhere with it. It has transformed the way I work. I treat it with care because it is expensive.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'high-performance machine' (compound noun). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'rely on', 'high-performance', 'draft', 'analyze', 'processing speed', 'lightning fast', 'multitask', 'efficiently', 'conferencing', 'compact', 'essential asset'. >Band 6: 'Multitask', 'asset'. Not Band 8: 'Reports' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'use it to draft', 'allows me to multitask'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I rely on my laptop for work. It is a high-performance machine. I use it to draft reports and analyze data. The processing speed is lightning fast. It allows me to multitask efficiently. I also use it for video conferencing with clients. It is compact and portable. It is an essential asset for my profession. I can work from anywhere with it. It has transformed the way I work. I treat it with care because it is expensive.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'rely on', 'high-performance', 'draft', 'analyze', 'processing speed', 'lightning fast', 'multitask', 'efficiently', 'conferencing', 'compact', 'essential asset'. \n\n>Band 6: 'Multitask', 'asset'.\n\nNot Band 8: 'Reports' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'use it to draft', 'allows me to multitask'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_421",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place.",
        "transcript_cleaned": "I explored the ruins of Pompeii. It was buried under volcanic ash. The preservation is remarkable. You can see the remnants of ancient houses and streets. It offers a glimpse into the past. I was struck by the tragedy of the event. It is a hauntingly beautiful site. It serves as a grim reminder of nature's power. Walking through the empty streets was eerie. It felt like time had stopped. I learned a lot about Roman daily life. It was a fascinating visit.",
        "word_count": 83,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'buried under' (passive). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'ruins', 'volcanic ash', 'preservation', 'remarkable', 'remnants', 'glimpse', 'tragedy', 'hauntingly beautiful', 'grim reminder'. >Band 6: 'Hauntingly', 'grim'. Not Band 8: 'Houses' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'buried under volcanic ash', 'see the remnants of'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical place.\n\nTranscript: I explored the ruins of Pompeii. It was buried under volcanic ash. The preservation is remarkable. You can see the remnants of ancient houses and streets. It offers a glimpse into the past. I was struck by the tragedy of the event. It is a hauntingly beautiful site. It serves as a grim reminder of nature's power. Walking through the empty streets was eerie. It felt like time had stopped. I learned a lot about Roman daily life. It was a fascinating visit.\n\nWord Count: 83 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'ruins', 'volcanic ash', 'preservation', 'remarkable', 'remnants', 'glimpse', 'tragedy', 'hauntingly beautiful', 'grim reminder'. \n\n>Band 6: 'Hauntingly', 'grim'.\n\nNot Band 8: 'Houses' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'buried under volcanic ash', 'see the remnants of'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_422",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I admire the lotus flower. It grows in muddy water but remains pristine. The petals are delicate and vibrant. It blooms in the morning sun. It is a symbol of purity and enlightenment. I often see them in ponds at temples. The sight is tranquil. It teaches us to rise above adversity. I have a small pond in my garden with a lotus. It brings me peace to watch it grow. It is a very resilient plant.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'pristine' (adjective). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'pristine', 'delicate', 'vibrant', 'blooms', 'symbol', 'purity', 'enlightenment', 'tranquil', 'adversity', 'resilient'. >Band 6: 'Pristine', 'adversity'. Not Band 8: 'Muddy water' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'grows... but remains', 'teaches us to rise'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I admire the lotus flower. It grows in muddy water but remains pristine. The petals are delicate and vibrant. It blooms in the morning sun. It is a symbol of purity and enlightenment. I often see them in ponds at temples. The sight is tranquil. It teaches us to rise above adversity. I have a small pond in my garden with a lotus. It brings me peace to watch it grow. It is a very resilient plant.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'pristine', 'delicate', 'vibrant', 'blooms', 'symbol', 'purity', 'enlightenment', 'tranquil', 'adversity', 'resilient'. \n\n>Band 6: 'Pristine', 'adversity'.\n\nNot Band 8: 'Muddy water' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'grows... but remains', 'teaches us to rise'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_423",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "My friend Sarah is a compassionate nurse. She works long hours at the hospital. She cares for patients with unwavering dedication. She is always empathetic and kind. We often discuss her experiences. She deals with emotional stress gracefully. Her resilience is admirable. She inspires me to be a better person. We met in university and have been friends ever since. She is a good listener. I know I can rely on her for support. She is a true gem.",
        "word_count": 79,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'compassionate nurse' (noun phrase). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'compassionate', 'unwavering', 'dedication', 'empathetic', 'gracefully', 'resilience', 'admirable', 'inspires', 'gem'. >Band 6: 'Unwavering', 'gracefully'. Not Band 8: 'Patients' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'cares for patients', 'inspires me to be'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a friend.\n\nTranscript: My friend Sarah is a compassionate nurse. She works long hours at the hospital. She cares for patients with unwavering dedication. She is always empathetic and kind. We often discuss her experiences. She deals with emotional stress gracefully. Her resilience is admirable. She inspires me to be a better person. We met in university and have been friends ever since. She is a good listener. I know I can rely on her for support. She is a true gem.\n\nWord Count: 79 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'compassionate', 'unwavering', 'dedication', 'empathetic', 'gracefully', 'resilience', 'admirable', 'inspires', 'gem'. \n\n>Band 6: 'Unwavering', 'gracefully'.\n\nNot Band 8: 'Patients' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'cares for patients', 'inspires me to be'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_424",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I debated whether to pursue a master's degree. It was a significant financial commitment. I consulted with academic advisors. They highlighted the long-term benefits. I was concerned about the workload. However, the prospect of specialized knowledge was appealing. I decided to enroll. It was a strategic move for my career. It was hard to balance work and study. I had to manage my time well. In the end, it was worth it. I learned a lot and got a promotion.",
        "word_count": 80,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'debated whether to' (noun clause). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'debated', 'pursue', 'financial commitment', 'consulted', 'advisors', 'highlighted', 'workload', 'prospect', 'specialized', 'appealing', 'strategic'. >Band 6: 'Strategic', 'prospect'. Not Band 8: 'Master's degree' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'whether to pursue', 'prospect... was appealing'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I debated whether to pursue a master's degree. It was a significant financial commitment. I consulted with academic advisors. They highlighted the long-term benefits. I was concerned about the workload. However, the prospect of specialized knowledge was appealing. I decided to enroll. It was a strategic move for my career. It was hard to balance work and study. I had to manage my time well. In the end, it was worth it. I learned a lot and got a promotion.\n\nWord Count: 80 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'debated', 'pursue', 'financial commitment', 'consulted', 'advisors', 'highlighted', 'workload', 'prospect', 'specialized', 'appealing', 'strategic'. \n\n>Band 6: 'Strategic', 'prospect'.\n\nNot Band 8: 'Master's degree' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'whether to pursue', 'prospect... was appealing'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_425",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I entered a photography contest. The theme was urban life. I captured candid moments on the street. The lighting was challenging. I adjusted the settings manually. I submitted my best shot. I did not win, but I received an honorable mention. It validated my skills. It encouraged me to keep practicing. I was proud of my work. I saw many amazing photos from other photographers. It was a great learning experience. I plan to enter again next year.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'photography contest' (compound noun). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'contest', 'theme', 'urban life', 'captured', 'candid', 'challenging', 'manually', 'submitted', 'honorable mention', 'validated'. >Band 6: 'Candid', 'validated'. Not Band 8: 'Settings' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'did not win, but', 'encouraged me to keep'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I entered a photography contest. The theme was urban life. I captured candid moments on the street. The lighting was challenging. I adjusted the settings manually. I submitted my best shot. I did not win, but I received an honorable mention. It validated my skills. It encouraged me to keep practicing. I was proud of my work. I saw many amazing photos from other photographers. It was a great learning experience. I plan to enter again next year.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'contest', 'theme', 'urban life', 'captured', 'candid', 'challenging', 'manually', 'submitted', 'honorable mention', 'validated'. \n\n>Band 6: 'Candid', 'validated'.\n\nNot Band 8: 'Settings' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'did not win, but', 'encouraged me to keep'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
