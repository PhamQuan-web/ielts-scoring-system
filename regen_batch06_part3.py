import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch06.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v7_g7_501",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Forbidden City in Beijing, China. It served as the imperial palace for 24 emperors during the Ming and Qing dynasties. The complex is vast, covering 72 hectares. The architecture is magnificent, with traditional red walls and yellow glazed roof tiles. I was impressed by the intricate details of the dragons carved on the marble terraces. It is a UNESCO World Heritage site that preserves Chinese history and culture. Walking through the gates made me feel like I was in a different era. The sheer scale of the place is overwhelming. It is a must-visit for anyone interested in history.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'imperial palace', 'dynasties', 'vast', 'hectares', 'magnificent', 'traditional', 'glazed', 'intricate details', 'terraces', 'preserves', 'overwhelming'. Band 7 level.",
             "grammar: 'City... It served', 'dragons carved on', 'Walking through... made'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'imperial palace', 'dynasties', 'vast', 'glazed', 'intricate', 'terraces', 'preserves', 'overwhelming'. >Band 6: 'Intricate', 'overwhelming'. Not Band 8: 'History' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'dragons carved on', 'Walking through... made'. >Band 6: Participles and gerund subjects used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Forbidden City in Beijing, China. It served as the imperial palace for 24 emperors during the Ming and Qing dynasties. The complex is vast, covering 72 hectares. The architecture is magnificent, with traditional red walls and yellow glazed roof tiles. I was impressed by the intricate details of the dragons carved on the marble terraces. It is a UNESCO World Heritage site that preserves Chinese history and culture. Walking through the gates made me feel like I was in a different era. The sheer scale of the place is overwhelming. It is a must-visit for anyone interested in history.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'imperial palace', 'dynasties', 'vast', 'glazed', 'intricate', 'terraces', 'preserves', 'overwhelming'. \n\n>Band 6: 'Intricate', 'overwhelming'.\n\nNot Band 8: 'History' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'dragons carved on', 'Walking through... made'. \n\n>Band 6: Participles and gerund subjects used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_502",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I decided to build a bookshelf from scratch. I thought it would be easy, but it turned out to be quite challenging. I had to measure the wood precisely and cut it with a saw. Using the power tools was a bit scary at first. I made a mistake with the measurements and had to start over. It required a lot of patience and attention to detail. Sanding and painting the wood took hours. However, when I finished, I felt a great sense of accomplishment. The bookshelf is sturdy and looks great in my room.",
        "word_count": 98,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'from scratch', 'challenging', 'precisely', 'power tools', 'measurements', 'patience', 'attention to detail', 'sanding', 'accomplishment', 'sturdy'. Band 7 level.",
             "grammar: 'thought it would be', 'mistake... and had to', 'Sanding and painting'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'from scratch', 'precisely', 'power tools', 'measurements', 'patience', 'sanding', 'accomplishment', 'sturdy'. >Band 6: 'Sturdy', 'precisely'. Not Band 8: 'Mistake' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'Using the power tools', 'Sanding and painting'. >Band 6: Gerund subjects used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I decided to build a bookshelf from scratch. I thought it would be easy, but it turned out to be quite challenging. I had to measure the wood precisely and cut it with a saw. Using the power tools was a bit scary at first. I made a mistake with the measurements and had to start over. It required a lot of patience and attention to detail. Sanding and painting the wood took hours. However, when I finished, I felt a great sense of accomplishment. The bookshelf is sturdy and looks great in my room.\n\nWord Count: 98 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'from scratch', 'precisely', 'power tools', 'measurements', 'patience', 'sanding', 'accomplishment', 'sturdy'. \n\n>Band 6: 'Sturdy', 'precisely'.\n\nNot Band 8: 'Mistake' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Using the power tools', 'Sanding and painting'. \n\n>Band 6: Gerund subjects used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_503",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read The Da Vinci Code by Dan Brown. It is a fast-paced mystery thriller that keeps you on the edge of your seat. The plot involves a murder in the Louvre Museum and secret societies. The protagonist, Robert Langdon, uses his knowledge of symbols to solve the crime. I found the historical and religious references very intriguing. The story is full of twists and turns that I did not expect. I finished the book in just two days because I could not put it down. It is a page-turner that sparks your curiosity.",
        "word_count": 96,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'fast-paced', 'mystery thriller', 'edge of your seat', 'protagonist', 'symbols', 'intriguing', 'twists and turns', 'page-turner', 'sparks', 'curiosity'. Band 7 level.",
             "grammar: 'thriller that keeps', 'uses his knowledge... to solve', 'finished... because I'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'fast-paced', 'thriller', 'edge of your seat', 'protagonist', 'intriguing', 'twists and turns', 'page-turner', 'curiosity'. >Band 6: 'Intriguing', 'thriller'. Not Band 8: 'Murder' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'thriller that keeps', 'uses... to solve'. >Band 6: Relative clauses and infinitives used correctly. Not Band 8: Simple sentence structure.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read The Da Vinci Code by Dan Brown. It is a fast-paced mystery thriller that keeps you on the edge of your seat. The plot involves a murder in the Louvre Museum and secret societies. The protagonist, Robert Langdon, uses his knowledge of symbols to solve the crime. I found the historical and religious references very intriguing. The story is full of twists and turns that I did not expect. I finished the book in just two days because I could not put it down. It is a page-turner that sparks your curiosity.\n\nWord Count: 96 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'fast-paced', 'thriller', 'edge of your seat', 'protagonist', 'intriguing', 'twists and turns', 'page-turner', 'curiosity'. \n\n>Band 6: 'Intriguing', 'thriller'.\n\nNot Band 8: 'Murder' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'thriller that keeps', 'uses... to solve'. \n\n>Band 6: Relative clauses and infinitives used correctly.\n\nNot Band 8: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_504",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I attended a karaoke party at a friend's house. It was a casual gathering but very entertaining. We took turns singing our favorite songs, even though most of us are terrible singers. We laughed at the bad performances and cheered for the good ones. The atmosphere was relaxed and uninhibited. We ordered pizza and snacks to keep our energy up. It was a great way to bond with friends and let loose. I haven't laughed that hard in a long time. It was a memorable night filled with music and fun.",
        "word_count": 93,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'karaoke', 'casual gathering', 'entertaining', 'terrible singers', 'performances', 'uninhibited', 'bond', 'let loose', 'memorable'. Band 7 level.",
             "grammar: 'singing... even though', 'laughed at the', 'snacks to keep'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'karaoke', 'gathering', 'entertaining', 'uninhibited', 'bond', 'let loose', 'memorable'. >Band 6: 'Uninhibited', 'memorable'. Not Band 8: 'Songs' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'singing... even though', 'snacks to keep'. >Band 6: Concessive clauses and infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I attended a karaoke party at a friend's house. It was a casual gathering but very entertaining. We took turns singing our favorite songs, even though most of us are terrible singers. We laughed at the bad performances and cheered for the good ones. The atmosphere was relaxed and uninhibited. We ordered pizza and snacks to keep our energy up. It was a great way to bond with friends and let loose. I haven't laughed that hard in a long time. It was a memorable night filled with music and fun.\n\nWord Count: 93 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'karaoke', 'gathering', 'entertaining', 'uninhibited', 'bond', 'let loose', 'memorable'. \n\n>Band 6: 'Uninhibited', 'memorable'.\n\nNot Band 8: 'Songs' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'singing... even though', 'snacks to keep'. \n\n>Band 6: Concessive clauses and infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_505",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I bought a digital camera to pursue my hobby of photography. It captures high-quality images with great detail. I use it to document my travels and special family moments. It has various settings that allow me to adjust to different lighting conditions. I can easily transfer the photos to my computer for editing. It helps me preserve memories that might otherwise be forgotten. The camera is compact and easy to carry around. It is much better than my phone camera. I cherish the photos I take with it.",
        "word_count": 89,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'digital camera', 'pursue', 'hobby', 'captures', 'high-quality', 'document', 'settings', 'adjust', 'transfer', 'editing', 'preserve memories', 'compact', 'cherish'. Band 7 level.",
             "grammar: 'settings that allow', 'transfer... for editing', 'memories that might'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'pursue', 'captures', 'high-quality', 'document', 'settings', 'preserve', 'compact', 'cherish'. >Band 6: 'Document', 'preserve'. Not Band 8: 'Phone' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'settings that allow', 'memories that might'. >Band 6: Relative clauses and modals used correctly. Not Band 8: Simple sentence structure.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I bought a digital camera to pursue my hobby of photography. It captures high-quality images with great detail. I use it to document my travels and special family moments. It has various settings that allow me to adjust to different lighting conditions. I can easily transfer the photos to my computer for editing. It helps me preserve memories that might otherwise be forgotten. The camera is compact and easy to carry around. It is much better than my phone camera. I cherish the photos I take with it.\n\nWord Count: 89 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'pursue', 'captures', 'high-quality', 'document', 'settings', 'preserve', 'compact', 'cherish'. \n\n>Band 6: 'Document', 'preserve'.\n\nNot Band 8: 'Phone' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'settings that allow', 'memories that might'. \n\n>Band 6: Relative clauses and modals used correctly.\n\nNot Band 8: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_506",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Statue of Liberty in New York. It stands on Liberty Island in the harbor. It was a gift from France to the United States. I took a ferry to see it close up, which was exciting. The statue is a symbol of freedom and democracy. It is an impressive monument made of copper. I learned about its construction and history in the museum. Climbing to the pedestal gave me a great view of the city skyline. It is an iconic landmark that represents hope.",
        "word_count": 88,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'harbor', 'ferry', 'symbol', 'freedom', 'democracy', 'impressive', 'monument', 'copper', 'construction', 'pedestal', 'skyline', 'iconic landmark'. Band 7 level.",
             "grammar: 'up, which was', 'made of copper', 'Climbing... gave me'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'harbor', 'symbol', 'freedom', 'democracy', 'impressive', 'monument', 'pedestal', 'skyline', 'iconic landmark'. >Band 6: 'Iconic', 'democracy'. Not Band 8: 'Gift' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'up, which was', 'Climbing... gave me'. >Band 6: Relative clauses and gerund subjects used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Statue of Liberty in New York. It stands on Liberty Island in the harbor. It was a gift from France to the United States. I took a ferry to see it close up, which was exciting. The statue is a symbol of freedom and democracy. It is an impressive monument made of copper. I learned about its construction and history in the museum. Climbing to the pedestal gave me a great view of the city skyline. It is an iconic landmark that represents hope.\n\nWord Count: 88 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'harbor', 'symbol', 'freedom', 'democracy', 'impressive', 'monument', 'pedestal', 'skyline', 'iconic landmark'. \n\n>Band 6: 'Iconic', 'democracy'.\n\nNot Band 8: 'Gift' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'up, which was', 'Climbing... gave me'. \n\n>Band 6: Relative clauses and gerund subjects used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_507",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I planted some mint in a pot on my balcony. It grows vigorously and spreads quickly. It has a fresh and invigorating aroma. I use the leaves to make herbal tea and add flavor to salads. It is easy to care for and requires regular watering. It is a resilient plant that can survive in different conditions. I love the smell of mint in the morning. It adds a touch of greenery to my home. I enjoy having fresh herbs readily available for cooking.",
        "word_count": 86,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'vigorously', 'spreads', 'invigorating', 'aroma', 'herbal tea', 'flavor', 'resilient', 'survive', 'greenery', 'readily available'. Band 7 level.",
             "grammar: 'leaves to make', 'plant that can', 'enjoy having fresh'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'vigorously', 'invigorating', 'aroma', 'resilient', 'survive', 'greenery', 'readily available'. >Band 6: 'Vigorously', 'invigorating'. Not Band 8: 'Morning' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'plant that can', 'enjoy having fresh'. >Band 6: Relative clauses and gerunds used correctly. Not Band 8: Simple sentence structure.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I planted some mint in a pot on my balcony. It grows vigorously and spreads quickly. It has a fresh and invigorating aroma. I use the leaves to make herbal tea and add flavor to salads. It is easy to care for and requires regular watering. It is a resilient plant that can survive in different conditions. I love the smell of mint in the morning. It adds a touch of greenery to my home. I enjoy having fresh herbs readily available for cooking.\n\nWord Count: 86 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'vigorously', 'invigorating', 'aroma', 'resilient', 'survive', 'greenery', 'readily available'. \n\n>Band 6: 'Vigorously', 'invigorating'.\n\nNot Band 8: 'Morning' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'plant that can', 'enjoy having fresh'. \n\n>Band 6: Relative clauses and gerunds used correctly.\n\nNot Band 8: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_508",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "My friend Tom is a travel blogger who inspires me. He is adventurous and spontaneous, always planning his next trip. He visits exotic locations and shares his experiences online. We often talk about his travels and the cultures he encounters. He is open-minded and curious about the world. He has a zest for life that is contagious. I admire his courage to travel alone. He encourages me to step out of my comfort zone. He is a loyal friend who always keeps in touch.",
        "word_count": 86,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'travel blogger', 'inspires', 'adventurous', 'spontaneous', 'exotic locations', 'encounters', 'open-minded', 'curious', 'zest for life', 'contagious', 'courage', 'comfort zone', 'loyal'. Band 7 level.",
             "grammar: 'blogger who inspires', 'planning his next', 'courage to travel'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'travel blogger', 'adventurous', 'spontaneous', 'exotic', 'encounters', 'zest for life', 'contagious', 'comfort zone'. >Band 6: 'Spontaneous', 'zest'. Not Band 8: 'Friend' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'blogger who inspires', 'planning his next'. >Band 6: Relative clauses and participles used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a friend.\n\nTranscript: My friend Tom is a travel blogger who inspires me. He is adventurous and spontaneous, always planning his next trip. He visits exotic locations and shares his experiences online. We often talk about his travels and the cultures he encounters. He is open-minded and curious about the world. He has a zest for life that is contagious. I admire his courage to travel alone. He encourages me to step out of my comfort zone. He is a loyal friend who always keeps in touch.\n\nWord Count: 86 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'travel blogger', 'adventurous', 'spontaneous', 'exotic', 'encounters', 'zest for life', 'contagious', 'comfort zone'. \n\n>Band 6: 'Spontaneous', 'zest'.\n\nNot Band 8: 'Friend' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'blogger who inspires', 'planning his next'. \n\n>Band 6: Relative clauses and participles used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_509",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I decided to move to a new city for a fresh start. It was a difficult decision because I had to leave my friends behind. I was nervous about finding a job and an apartment. I wanted to challenge myself and grow as a person. The moving process was stressful and tiring. I had to adjust to a new environment and routine. I missed my family at first. However, I made new friends and found a job I love. It was a growth experience that made me stronger.",
        "word_count": 90,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'fresh start', 'nervous', 'challenge myself', 'grow', 'stressful', 'adjust', 'environment', 'routine', 'growth experience'. Band 7 level.",
             "grammar: 'decision because I had', 'nervous about finding', 'wanted to challenge'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'fresh start', 'challenge myself', 'stressful', 'adjust', 'environment', 'routine', 'growth experience'. >Band 6: 'Adjust', 'growth'. Not Band 8: 'Friends' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'decision because I had', 'nervous about finding'. >Band 6: Causal clauses and prepositions used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I decided to move to a new city for a fresh start. It was a difficult decision because I had to leave my friends behind. I was nervous about finding a job and an apartment. I wanted to challenge myself and grow as a person. The moving process was stressful and tiring. I had to adjust to a new environment and routine. I missed my family at first. However, I made new friends and found a job I love. It was a growth experience that made me stronger.\n\nWord Count: 90 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'fresh start', 'challenge myself', 'stressful', 'adjust', 'environment', 'routine', 'growth experience'. \n\n>Band 6: 'Adjust', 'growth'.\n\nNot Band 8: 'Friends' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'decision because I had', 'nervous about finding'. \n\n>Band 6: Causal clauses and prepositions used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_510",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I entered a dance competition with my team. We practiced for months to perfect our routine. The choreography was complex and required synchronization. I was nervous before going on stage. The music was energetic and pumped us up. We performed with passion and energy. The audience clapped loudly and cheered. We won a trophy for best performance. It was a proud moment for all of us. It motivated me to keep dancing and improving my skills.",
        "word_count": 77,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'dance competition', 'perfect', 'routine', 'choreography', 'complex', 'synchronization', 'nervous', 'energetic', 'pumped us up', 'passion', 'trophy', 'motivated'. Band 7 level.",
             "grammar: 'practiced... to perfect', 'required synchronization', 'motivated me to'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'choreography', 'complex', 'synchronization', 'energetic', 'pumped us up', 'passion', 'trophy', 'motivated'. >Band 6: 'Synchronization', 'pumped'. Not Band 8: 'Music' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'practiced... to perfect', 'motivated me to'. >Band 6: Infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I entered a dance competition with my team. We practiced for months to perfect our routine. The choreography was complex and required synchronization. I was nervous before going on stage. The music was energetic and pumped us up. We performed with passion and energy. The audience clapped loudly and cheered. We won a trophy for best performance. It was a proud moment for all of us. It motivated me to keep dancing and improving my skills.\n\nWord Count: 77 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'choreography', 'complex', 'synchronization', 'energetic', 'pumped us up', 'passion', 'trophy', 'motivated'. \n\n>Band 6: 'Synchronization', 'pumped'.\n\nNot Band 8: 'Music' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'practiced... to perfect', 'motivated me to'. \n\n>Band 6: Infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_511",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Sydney Opera House in Australia. It is a famous landmark known for its unique design. The roof looks like sails or shells. It is located on the harbor, offering beautiful views. I took a guided tour of the interior and saw the concert halls. The acoustics are excellent for performances. It is an architectural wonder that represents the country. I was impressed by its beauty and scale. It is a place I will always remember visiting.",
        "word_count": 80,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'landmark', 'unique design', 'sails', 'shells', 'harbor', 'interior', 'concert halls', 'acoustics', 'architectural wonder', 'scale'. Band 7 level.",
             "grammar: 'landmark known for', 'looks like sails', 'offering beautiful views'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'landmark', 'unique', 'sails', 'harbor', 'interior', 'acoustics', 'architectural wonder', 'scale'. >Band 6: 'Acoustics', 'wonder'. Not Band 8: 'Famous' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'landmark known for', 'offering beautiful views'. >Band 6: Participles used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Sydney Opera House in Australia. It is a famous landmark known for its unique design. The roof looks like sails or shells. It is located on the harbor, offering beautiful views. I took a guided tour of the interior and saw the concert halls. The acoustics are excellent for performances. It is an architectural wonder that represents the country. I was impressed by its beauty and scale. It is a place I will always remember visiting.\n\nWord Count: 80 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'landmark', 'unique', 'sails', 'harbor', 'interior', 'acoustics', 'architectural wonder', 'scale'. \n\n>Band 6: 'Acoustics', 'wonder'.\n\nNot Band 8: 'Famous' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'landmark known for', 'offering beautiful views'. \n\n>Band 6: Participles used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_512",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I had to give a speech at my best friend's wedding. I was extremely nervous about public speaking. I wanted it to be perfect. I wrote my speech carefully, including funny stories and heartfelt wishes. I practiced it many times in front of a mirror to gain confidence. When I spoke, my hands were shaking, but I managed to speak clearly. Everyone laughed and applauded. I felt relieved and happy when it was over. It was a special moment that I will cherish.",
        "word_count": 85,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'speech', 'nervous', 'public speaking', 'heartfelt wishes', 'practiced', 'gain confidence', 'shaking', 'applauded', 'relieved', 'cherish'. Band 7 level.",
             "grammar: 'nervous about public speaking', 'wanted it to be', 'including funny stories'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'public speaking', 'heartfelt', 'gain confidence', 'applauded', 'relieved', 'cherish'. >Band 6: 'Heartfelt', 'applauded'. Not Band 8: 'Perfect' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'nervous about', 'including funny stories'. >Band 6: Prepositions and participles used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I had to give a speech at my best friend's wedding. I was extremely nervous about public speaking. I wanted it to be perfect. I wrote my speech carefully, including funny stories and heartfelt wishes. I practiced it many times in front of a mirror to gain confidence. When I spoke, my hands were shaking, but I managed to speak clearly. Everyone laughed and applauded. I felt relieved and happy when it was over. It was a special moment that I will cherish.\n\nWord Count: 85 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'public speaking', 'heartfelt', 'gain confidence', 'applauded', 'relieved', 'cherish'. \n\n>Band 6: 'Heartfelt', 'applauded'.\n\nNot Band 8: 'Perfect' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'nervous about', 'including funny stories'. \n\n>Band 6: Prepositions and participles used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_513",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read The Hunger Games, which is a dystopian novel. The story is intense and action-packed. The protagonist, Katniss, is a brave character who fights for survival. The government is oppressive and cruel. The book explores themes of rebellion and sacrifice. I was hooked from the first page. It is a thrilling read that I couldn't put down. It made me think about society and power. I enjoyed it immensely.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'dystopian', 'intense', 'action-packed', 'protagonist', 'brave', 'survival', 'oppressive', 'cruel', 'rebellion', 'sacrifice', 'hooked', 'thrilling', 'immensely'. Band 7 level.",
             "grammar: 'Games, which is', 'character who fights'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'dystopian', 'action-packed', 'protagonist', 'oppressive', 'rebellion', 'sacrifice', 'hooked', 'thrilling', 'immensely'. >Band 6: 'Action-packed', 'oppressive'. Not Band 8: 'Story' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'Games, which is', 'character who fights'. >Band 6: Relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read The Hunger Games, which is a dystopian novel. The story is intense and action-packed. The protagonist, Katniss, is a brave character who fights for survival. The government is oppressive and cruel. The book explores themes of rebellion and sacrifice. I was hooked from the first page. It is a thrilling read that I couldn't put down. It made me think about society and power. I enjoyed it immensely.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'dystopian', 'action-packed', 'protagonist', 'oppressive', 'rebellion', 'sacrifice', 'hooked', 'thrilling', 'immensely'. \n\n>Band 6: 'Action-packed', 'oppressive'.\n\nNot Band 8: 'Story' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Games, which is', 'character who fights'. \n\n>Band 6: Relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_514",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I went to a beach party last summer. We had a bonfire on the sand, which kept us warm. We roasted marshmallows and told stories. Someone played the guitar, and we sang songs together. The sound of the waves was soothing and relaxing. It was a casual evening with close friends. I enjoyed the company and the beautiful setting. It was a memorable night under the stars.",
        "word_count": 68,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'beach party', 'bonfire', 'roasted', 'marshmallows', 'soothing', 'casual', 'company', 'setting', 'memorable'. Band 7 level.",
             "grammar: 'sand, which kept', 'sound... was soothing'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'bonfire', 'roasted', 'marshmallows', 'soothing', 'casual', 'setting', 'memorable'. >Band 6: 'Soothing', 'memorable'. Not Band 8: 'Summer' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'sand, which kept', 'sound... was soothing'. >Band 6: Relative clauses and noun phrases used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I went to a beach party last summer. We had a bonfire on the sand, which kept us warm. We roasted marshmallows and told stories. Someone played the guitar, and we sang songs together. The sound of the waves was soothing and relaxing. It was a casual evening with close friends. I enjoyed the company and the beautiful setting. It was a memorable night under the stars.\n\nWord Count: 68 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'bonfire', 'roasted', 'marshmallows', 'soothing', 'casual', 'setting', 'memorable'. \n\n>Band 6: 'Soothing', 'memorable'.\n\nNot Band 8: 'Summer' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'sand, which kept', 'sound... was soothing'. \n\n>Band 6: Relative clauses and noun phrases used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_515",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I use a tablet computer for my studies. It is lightweight and portable, making it easy to carry. I use it for reading e-books and watching educational videos. The screen is high-resolution, so everything looks clear. I can download many helpful apps. It has a long battery life, which is convenient. It keeps me organized and entertained when I travel. It is a versatile device that I use daily.",
        "word_count": 70,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'lightweight', 'portable', 'educational', 'high-resolution', 'apps', 'battery life', 'convenient', 'organized', 'entertained', 'versatile', 'device'. Band 7 level.",
             "grammar: 'portable, making it', 'screen is... so everything'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'lightweight', 'portable', 'high-resolution', 'battery life', 'convenient', 'organized', 'versatile'. >Band 6: 'Portable', 'versatile'. Not Band 8: 'Videos' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'portable, making it', 'life, which is'. >Band 6: Participles and relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I use a tablet computer for my studies. It is lightweight and portable, making it easy to carry. I use it for reading e-books and watching educational videos. The screen is high-resolution, so everything looks clear. I can download many helpful apps. It has a long battery life, which is convenient. It keeps me organized and entertained when I travel. It is a versatile device that I use daily.\n\nWord Count: 70 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'lightweight', 'portable', 'high-resolution', 'battery life', 'convenient', 'organized', 'versatile'. \n\n>Band 6: 'Portable', 'versatile'.\n\nNot Band 8: 'Videos' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'portable, making it', 'life, which is'. \n\n>Band 6: Participles and relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_516",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Pyramids of Giza. They are ancient tombs built for pharaohs. The stone blocks are huge and heavy. I wondered how they were constructed without modern machinery. I rode a camel around the site, which was a unique experience. The desert was hot and dry. It was an amazing sight to see. It is a wonder of the ancient world. I took many photos to capture the moment.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'ancient tombs', 'pharaohs', 'constructed', 'machinery', 'unique experience', 'wonder', 'capture'. Band 7 level.",
             "grammar: 'wondered how they were', 'site, which was'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'ancient tombs', 'pharaohs', 'constructed', 'machinery', 'unique', 'wonder', 'capture'. >Band 6: 'Constructed', 'wonder'. Not Band 8: 'Hot' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'wondered how they were', 'site, which was'. >Band 6: Noun clauses and relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Pyramids of Giza. They are ancient tombs built for pharaohs. The stone blocks are huge and heavy. I wondered how they were constructed without modern machinery. I rode a camel around the site, which was a unique experience. The desert was hot and dry. It was an amazing sight to see. It is a wonder of the ancient world. I took many photos to capture the moment.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'ancient tombs', 'pharaohs', 'constructed', 'machinery', 'unique', 'wonder', 'capture'. \n\n>Band 6: 'Constructed', 'wonder'.\n\nNot Band 8: 'Hot' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'wondered how they were', 'site, which was'. \n\n>Band 6: Noun clauses and relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_517",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I like the cherry blossom tree. The pink flowers are beautiful and delicate. They bloom in spring, creating a stunning scene. The petals fall like snow when the wind blows. It is a sign of new beginnings and hope. People have picnics under the trees to enjoy the view. It is a lovely tradition in many cultures. I take many photos of them. They make me feel happy and peaceful.",
        "word_count": 70,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'cherry blossom', 'delicate', 'bloom', 'stunning scene', 'petals', 'sign', 'new beginnings', 'tradition', 'peaceful'. Band 7 level.",
             "grammar: 'spring, creating a', 'fall like snow when'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'cherry blossom', 'delicate', 'stunning', 'petals', 'new beginnings', 'tradition', 'peaceful'. >Band 6: 'Stunning', 'tradition'. Not Band 8: 'Pink' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'spring, creating a', 'fall like snow when'. >Band 6: Participles and similes used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I like the cherry blossom tree. The pink flowers are beautiful and delicate. They bloom in spring, creating a stunning scene. The petals fall like snow when the wind blows. It is a sign of new beginnings and hope. People have picnics under the trees to enjoy the view. It is a lovely tradition in many cultures. I take many photos of them. They make me feel happy and peaceful.\n\nWord Count: 70 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'cherry blossom', 'delicate', 'stunning', 'petals', 'new beginnings', 'tradition', 'peaceful'. \n\n>Band 6: 'Stunning', 'tradition'.\n\nNot Band 8: 'Pink' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'spring, creating a', 'fall like snow when'. \n\n>Band 6: Participles and similes used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_518",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "My friend Sarah is kind and generous. She always helps me when I am in trouble. She listens to my problems without judging. We go shopping together and have fun. She has good taste in clothes and gives me advice. She makes me laugh with her jokes. We have been friends for years. I trust her completely with my secrets. She is a loyal companion.",
        "word_count": 66,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'generous', 'trouble', 'judging', 'good taste', 'advice', 'loyal companion'. Band 7 level.",
             "grammar: 'helps me when', 'listens... without judging'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'generous', 'judging', 'good taste', 'loyal companion'. >Band 6: 'Trust', 'taste'. Not Band 8: 'Clothes' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'helps me when', 'listens... without judging'. >Band 6: Time clauses and prepositional phrases used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a friend.\n\nTranscript: My friend Sarah is kind and generous. She always helps me when I am in trouble. She listens to my problems without judging. We go shopping together and have fun. She has good taste in clothes and gives me advice. She makes me laugh with her jokes. We have been friends for years. I trust her completely with my secrets. She is a loyal companion.\n\nWord Count: 66 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'generous', 'judging', 'good taste', 'loyal companion'. \n\n>Band 6: 'Trust', 'taste'.\n\nNot Band 8: 'Clothes' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'helps me when', 'listens... without judging'. \n\n>Band 6: Time clauses and prepositional phrases used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_519",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I decided to study abroad, which was a big step for me. I was worried about homesickness and leaving my family. I had to learn a new language, which was challenging. It was difficult at first to adjust. I made new friends from different countries. I learned about a different culture and way of life. It was a life-changing experience that broadened my mind. I am glad I took the risk.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'study abroad', 'big step', 'homesickness', 'challenging', 'adjust', 'culture', 'life-changing', 'broadened my mind', 'risk'. Band 7 level.",
             "grammar: 'abroad, which was', 'language, which was'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'study abroad', 'homesickness', 'challenging', 'life-changing', 'broadened my mind', 'risk'. >Band 6: 'Adjust', 'culture'. Not Band 8: 'Friends' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'abroad, which was', 'language, which was'. >Band 6: Relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I decided to study abroad, which was a big step for me. I was worried about homesickness and leaving my family. I had to learn a new language, which was challenging. It was difficult at first to adjust. I made new friends from different countries. I learned about a different culture and way of life. It was a life-changing experience that broadened my mind. I am glad I took the risk.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'study abroad', 'homesickness', 'challenging', 'life-changing', 'broadened my mind', 'risk'. \n\n>Band 6: 'Adjust', 'culture'.\n\nNot Band 8: 'Friends' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'abroad, which was', 'language, which was'. \n\n>Band 6: Relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_520",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I ran a 5k race for charity. I trained for weeks to build my stamina. It was exhausting but rewarding. I paced myself carefully during the race. The other runners were fast and competitive. I finished the race in good time. I got a medal for finishing. I was proud of myself for not giving up. It was a good achievement that boosted my confidence.",
        "word_count": 66,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'charity', 'stamina', 'exhausting', 'rewarding', 'paced myself', 'competitive', 'medal', 'achievement', 'boosted'. Band 7 level.",
             "grammar: 'weeks to build', 'proud... for not giving'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'stamina', 'exhausting', 'rewarding', 'paced myself', 'competitive', 'achievement', 'boosted'. >Band 6: 'Paced', 'exhausting'. Not Band 8: 'Fast' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'weeks to build', 'proud... for not giving'. >Band 6: Infinitives and gerunds used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I ran a 5k race for charity. I trained for weeks to build my stamina. It was exhausting but rewarding. I paced myself carefully during the race. The other runners were fast and competitive. I finished the race in good time. I got a medal for finishing. I was proud of myself for not giving up. It was a good achievement that boosted my confidence.\n\nWord Count: 66 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'stamina', 'exhausting', 'rewarding', 'paced myself', 'competitive', 'achievement', 'boosted'. \n\n>Band 6: 'Paced', 'exhausting'.\n\nNot Band 8: 'Fast' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'weeks to build', 'proud... for not giving'. \n\n>Band 6: Infinitives and gerunds used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_521",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Empire State Building in New York. It is a famous skyscraper that dominates the skyline. The view from the top is amazing, offering a panorama of the city. You can see the whole city stretched out below. The elevator is fast and modern. It is an iconic building that represents American ambition. It was built in the 1930s, which is impressive. It is a symbol of New York's history.",
        "word_count": 72,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'skyscraper', 'dominates', 'skyline', 'panorama', 'stretched out', 'iconic', 'ambition', 'symbol'. Band 7 level.",
             "grammar: 'skyscraper that dominates', 'offering a panorama', '1930s, which is'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'skyscraper', 'dominates', 'skyline', 'panorama', 'iconic', 'ambition'. >Band 6: 'Iconic', 'skyscraper'. Not Band 8: 'City' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'skyscraper that dominates', 'offering a panorama', '1930s, which is'. >Band 6: Relative clauses and participles used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Empire State Building in New York. It is a famous skyscraper that dominates the skyline. The view from the top is amazing, offering a panorama of the city. You can see the whole city stretched out below. The elevator is fast and modern. It is an iconic building that represents American ambition. It was built in the 1930s, which is impressive. It is a symbol of New York's history.\n\nWord Count: 72 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'skyscraper', 'dominates', 'skyline', 'panorama', 'iconic', 'ambition'. \n\n>Band 6: 'Iconic', 'skyscraper'.\n\nNot Band 8: 'City' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'skyscraper that dominates', 'offering a panorama', '1930s, which is'. \n\n>Band 6: Relative clauses and participles used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_522",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I learned to cook a turkey for Thanksgiving. It takes a long time and requires patience. I had to baste it regularly to keep it moist. I worried about undercooking it, so I used a thermometer. It turned out delicious and juicy. My family loved it and complimented me. It was a culinary success that made me proud. I learned a new cooking skill.",
        "word_count": 65,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'patience', 'baste', 'moist', 'undercooking', 'thermometer', 'delicious', 'juicy', 'complimented', 'culinary success'. Band 7 level.",
             "grammar: 'baste it... to keep', 'worried... so I used'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'baste', 'moist', 'undercooking', 'thermometer', 'culinary success'. >Band 6: 'Baste', 'culinary'. Not Band 8: 'Time' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'baste it... to keep', 'worried... so I used'. >Band 6: Infinitives and causal clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I learned to cook a turkey for Thanksgiving. It takes a long time and requires patience. I had to baste it regularly to keep it moist. I worried about undercooking it, so I used a thermometer. It turned out delicious and juicy. My family loved it and complimented me. It was a culinary success that made me proud. I learned a new cooking skill.\n\nWord Count: 65 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'baste', 'moist', 'undercooking', 'thermometer', 'culinary success'. \n\n>Band 6: 'Baste', 'culinary'.\n\nNot Band 8: 'Time' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'baste it... to keep', 'worried... so I used'. \n\n>Band 6: Infinitives and causal clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_523",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read Sherlock Holmes, which is a famous detective story. Holmes is very smart and observant. He solves crimes using logic and deduction. Watson is his loyal friend and assistant. The mysteries are intriguing and keep you guessing. I like trying to solve the puzzle before Holmes does. It is a classic book that defines the genre. I enjoy the Victorian setting and atmosphere.",
        "word_count": 64,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'detective story', 'observant', 'logic', 'deduction', 'loyal', 'assistant', 'mysteries', 'intriguing', 'puzzle', 'defines', 'genre', 'Victorian setting'. Band 7 level.",
             "grammar: 'Holmes, which is', 'solves crimes using', 'trying to solve'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'observant', 'logic', 'deduction', 'mysteries', 'intriguing', 'genre', 'Victorian setting'. >Band 6: 'Intriguing', 'logic'. Not Band 8: 'Smart' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'Holmes, which is', 'solves crimes using', 'trying to solve'. >Band 6: Relative clauses, participles, and infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read Sherlock Holmes, which is a famous detective story. Holmes is very smart and observant. He solves crimes using logic and deduction. Watson is his loyal friend and assistant. The mysteries are intriguing and keep you guessing. I like trying to solve the puzzle before Holmes does. It is a classic book that defines the genre. I enjoy the Victorian setting and atmosphere.\n\nWord Count: 64 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'observant', 'logic', 'deduction', 'mysteries', 'intriguing', 'genre', 'Victorian setting'. \n\n>Band 6: 'Intriguing', 'logic'.\n\nNot Band 8: 'Smart' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Holmes, which is', 'solves crimes using', 'trying to solve'. \n\n>Band 6: Relative clauses, participles, and infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_524",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I went to a graduation party for my friend. We celebrated his success in finishing university. There were balloons and a big cake. We took many photos to capture the moment. Everyone was happy and proud of him. We talked about the future and our plans. It was a sentimental night full of good wishes. I will miss my friends when we go our separate ways.",
        "word_count": 66,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'graduation', 'celebrated', 'success', 'capture', 'proud', 'sentimental', 'separate ways'. Band 7 level.",
             "grammar: 'photos to capture', 'miss my friends when'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'graduation', 'celebrated', 'success', 'capture', 'sentimental', 'separate ways'. >Band 6: 'Sentimental', 'celebrated'. Not Band 8: 'Happy' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'photos to capture', 'miss my friends when'. >Band 6: Infinitives and time clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I went to a graduation party for my friend. We celebrated his success in finishing university. There were balloons and a big cake. We took many photos to capture the moment. Everyone was happy and proud of him. We talked about the future and our plans. It was a sentimental night full of good wishes. I will miss my friends when we go our separate ways.\n\nWord Count: 66 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'graduation', 'celebrated', 'success', 'capture', 'sentimental', 'separate ways'. \n\n>Band 6: 'Sentimental', 'celebrated'.\n\nNot Band 8: 'Happy' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'photos to capture', 'miss my friends when'. \n\n>Band 6: Infinitives and time clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_525",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I use a backpack with many compartments. I carry my laptop and books in it safely. It is comfortable to wear because the straps are padded. It is durable and water-resistant, protecting my belongings. I take it to school every day. It is essential for students to stay organized. I can find everything I need quickly. It is a practical item that I rely on.",
        "word_count": 66,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'compartments', 'safely', 'comfortable', 'straps', 'padded', 'durable', 'water-resistant', 'protecting', 'belongings', 'essential', 'organized', 'practical', 'rely on'. Band 7 level.",
             "grammar: 'wear because the', 'water-resistant, protecting', 'essential for students to'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'compartments', 'padded', 'durable', 'water-resistant', 'protecting', 'essential', 'organized', 'practical'. >Band 6: 'Compartments', 'durable'. Not Band 8: 'Books' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'water-resistant, protecting', 'essential for students to'. >Band 6: Participles and infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I use a backpack with many compartments. I carry my laptop and books in it safely. It is comfortable to wear because the straps are padded. It is durable and water-resistant, protecting my belongings. I take it to school every day. It is essential for students to stay organized. I can find everything I need quickly. It is a practical item that I rely on.\n\nWord Count: 66 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'compartments', 'padded', 'durable', 'water-resistant', 'protecting', 'essential', 'organized', 'practical'. \n\n>Band 6: 'Compartments', 'durable'.\n\nNot Band 8: 'Books' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'water-resistant, protecting', 'essential for students to'. \n\n>Band 6: Participles and infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
