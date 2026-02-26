import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch02.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v5_g4_076",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a childhood friend.",
        "transcript_cleaned": "I want to talk about my friend Tom. We played together when we were small. He lived next door. We went to same school. He was funny boy. He liked to tell jokes. We played football in the street. Sometimes we fought, but we became friends again. He moved to another city ten years ago. I was sad. We still talk on phone sometimes. He is married now. I hope to see him soon. He is my best memory of childhood.",
        "word_count": 82,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'funny boy' -> 'a funny boy'",
            "article error: 'to same school' -> 'to the same school'",
            "article error: 'on phone' -> 'on the phone'",
            "vocab: 'small', 'jokes', 'street', 'fought', 'city', 'sad', 'married', 'memory'. Band 5 level.",
            "repetitive: 'He'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'jokes', 'fought', 'married', 'memory', 'childhood'. >Band 4: 'Memory', 'childhood'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'He was funny boy'. >Band 3: Simple sentences. Not Band 5: Frequent article errors.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a childhood friend.\n\nTranscript: I want to talk about my friend Tom. We played together when we were small. He lived next door. We went to same school. He was funny boy. He liked to tell jokes. We played football in the street. Sometimes we fought, but we became friends again. He moved to another city ten years ago. I was sad. We still talk on phone sometimes. He is married now. I hope to see him soon. He is my best memory of childhood.\n\nWord Count: 82 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'jokes', 'fought', 'married', 'memory', 'childhood'. \n\n>Band 4: 'Memory', 'childhood'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'He was funny boy'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Frequent article errors.\n\n**Micro flaws identified:**\n- article error: 'funny boy', 'to same school', 'on phone'"
    },
    {
        "sample_id": "syn_p2_v5_g4_077",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a favorite song.",
        "transcript_cleaned": "I like the song \"Yesterday\" by Beatles. It is old song but beautiful. My father played it on guitar. I learned to sing it. The melody is sad and slow. The lyrics are easy to understand. It is about lost love. I listen to it when I am tired. It makes me feel calm. It is famous song in the world. Many singers sing it. I think it is masterpiece. I never get bored of it.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'is old song' -> 'is an old song'",
            "article error: 'on guitar' -> 'on the guitar'",
            "article error: 'is famous song' -> 'is a famous song'",
            "article error: 'is masterpiece' -> 'is a masterpiece'",
            "vocab: 'melody', 'lyrics', 'lost love', 'calm', 'famous', 'singers', 'masterpiece', 'bored'. Band 5 level.",
            "repetitive: 'It is'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'melody', 'lyrics', 'lost love', 'calm', 'masterpiece', 'bored'. >Band 4: 'Melody', 'lyrics', 'masterpiece'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'It is old song'. >Band 3: Simple sentences. Not Band 5: Systematic article errors.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a favorite song.\n\nTranscript: I like the song \"Yesterday\" by Beatles. It is old song but beautiful. My father played it on guitar. I learned to sing it. The melody is sad and slow. The lyrics are easy to understand. It is about lost love. I listen to it when I am tired. It makes me feel calm. It is famous song in the world. Many singers sing it. I think it is masterpiece. I never get bored of it.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'melody', 'lyrics', 'lost love', 'calm', 'masterpiece', 'bored'. \n\n>Band 4: 'Melody', 'lyrics', 'masterpiece'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'It is old song'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Systematic article errors.\n\n**Micro flaws identified:**\n- article error: 'is old song', 'on guitar', 'is famous song', 'is masterpiece'"
    },
    {
        "sample_id": "syn_p2_v5_g4_078",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a local festival.",
        "transcript_cleaned": "There is a flower festival in my town. It happens in spring. People decorate streets with flowers. It looks very colorful. Many tourists come to see. There is a parade. People wear traditional clothes and dance. I like to take photos there. The smell of flowers is everywhere. We eat special food on street. It is a happy time for everyone. I feel proud of my town. It is best time of year.",
        "word_count": 74,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'decorate streets' -> 'decorate the streets'",
            "article error: 'on street' -> 'on the street'",
            "article error: 'best time' -> 'the best time'",
            "vocab: 'festival', 'spring', 'decorate', 'colorful', 'tourists', 'parade', 'traditional', 'proud'. Band 5 level.",
            "repetitive: 'It is'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'festival', 'decorate', 'colorful', 'tourists', 'parade', 'traditional', 'proud'. >Band 4: 'Decorate', 'parade', 'traditional'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'It happens', 'People wear'. >Band 3: Simple sentences. Not Band 5: Article errors.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a local festival.\n\nTranscript: There is a flower festival in my town. It happens in spring. People decorate streets with flowers. It looks very colorful. Many tourists come to see. There is a parade. People wear traditional clothes and dance. I like to take photos there. The smell of flowers is everywhere. We eat special food on street. It is a happy time for everyone. I feel proud of my town. It is best time of year.\n\nWord Count: 74 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'festival', 'decorate', 'colorful', 'tourists', 'parade', 'traditional', 'proud'. \n\n>Band 4: 'Decorate', 'parade', 'traditional'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'It happens', 'People wear'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article errors.\n\n**Micro flaws identified:**\n- article error: 'decorate streets', 'on street', 'best time'"
    },
    {
        "sample_id": "syn_p2_v5_g4_079",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a family member you admire.",
        "transcript_cleaned": "I admire my older brother. He is smart and hard-working. He is an engineer. He works for big company. He helps me with my homework. He is good at math. He also plays guitar well. He is very kind to me. He buys me gifts on my birthday. I want to be like him. He is successful man. He inspires me to study hard. We have good relationship.",
        "word_count": 69,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'big company' -> 'a big company'",
            "article error: 'plays guitar' -> 'plays the guitar'",
            "article error: 'successful man' -> 'a successful man'",
            "article error: 'good relationship' -> 'a good relationship'",
            "vocab: 'admire', 'smart', 'hard-working', 'engineer', 'math', 'successful', 'inspires', 'relationship'. Band 5 level.",
            "repetitive: 'He is'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'admire', 'hard-working', 'engineer', 'math', 'successful', 'inspires', 'relationship'. >Band 4: 'Inspires', 'relationship', 'hard-working'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'He is smart', 'He works'. >Band 3: Simple sentences. Not Band 5: Systematic article errors.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a family member you admire.\n\nTranscript: I admire my older brother. He is smart and hard-working. He is an engineer. He works for big company. He helps me with my homework. He is good at math. He also plays guitar well. He is very kind to me. He buys me gifts on my birthday. I want to be like him. He is successful man. He inspires me to study hard. We have good relationship.\n\nWord Count: 69 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'admire', 'hard-working', 'engineer', 'math', 'successful', 'inspires', 'relationship'. \n\n>Band 4: 'Inspires', 'relationship', 'hard-working'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'He is smart', 'He works'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Systematic article errors.\n\n**Micro flaws identified:**\n- article error: 'big company', 'plays guitar', 'successful man', 'good relationship'"
    },
    {
        "sample_id": "syn_p2_v5_g4_080",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a foreign food you tried.",
        "transcript_cleaned": "I tried pizza for the first time. It is Italian food. I ate it in a restaurant. It was round and flat. It had cheese and tomato sauce. I chose pepperoni topping. It tasted salty and cheesy. I liked it very much. It was hot. The crust was crispy. I ate three slices. It is different from my country's food. I want to learn how to make pizza. It is delicious meal.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'is delicious meal' -> 'is a delicious meal'",
            "vocab: 'Italian', 'round', 'flat', 'cheese', 'tomato sauce', 'topping', 'salty', 'cheesy', 'crust', 'crispy', 'slices'. Band 5 level.",
            "repetitive: 'It was', 'It is'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'topping', 'salty', 'cheesy', 'crust', 'crispy', 'slices', 'delicious'. >Band 4: 'Topping', 'crust', 'crispy'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'It was round', 'It had cheese'. >Band 3: Simple sentences. Not Band 5: Article errors.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a foreign food you tried.\n\nTranscript: I tried pizza for the first time. It is Italian food. I ate it in a restaurant. It was round and flat. It had cheese and tomato sauce. I chose pepperoni topping. It tasted salty and cheesy. I liked it very much. It was hot. The crust was crispy. I ate three slices. It is different from my country's food. I want to learn how to make pizza. It is delicious meal.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'topping', 'salty', 'cheesy', 'crust', 'crispy', 'slices', 'delicious'. \n\n>Band 4: 'Topping', 'crust', 'crispy'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'It was round', 'It had cheese'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article errors.\n\n**Micro flaws identified:**\n- article error: 'is delicious meal'"
    },
    {
        "sample_id": "syn_p2_v5_g4_081",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition you entered.",
        "transcript_cleaned": "I entered a running competition at school. It was 100 meters race. I practiced for two weeks. I ran fast in training. On race day, I was nervous. My heart beat fast. There were eight runners. When the whistle blew, I ran. I tried my best. But I was not the fastest. I came third. I got a bronze medal. I was happy with result. It was exciting day for me.",
        "word_count": 72,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: '100 meters race' -> 'a 100 meters race'",
            "article error: 'with result' -> 'with the result'",
            "article error: 'exciting day' -> 'an exciting day'",
            "vocab: 'competition', 'race', 'practiced', 'training', 'nervous', 'heart beat', 'runners', 'whistle', 'fastest', 'bronze medal'. Band 5 level.",
            "repetitive: 'I'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'competition', 'race', 'training', 'nervous', 'whistle', 'medal', 'result'. >Band 4: 'Whistle', 'medal', 'training'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I practiced', 'I ran'. >Band 3: Simple sentences. Not Band 5: Article errors.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition you entered.\n\nTranscript: I entered a running competition at school. It was 100 meters race. I practiced for two weeks. I ran fast in training. On race day, I was nervous. My heart beat fast. There were eight runners. When the whistle blew, I ran. I tried my best. But I was not the fastest. I came third. I got a bronze medal. I was happy with result. It was exciting day for me.\n\nWord Count: 72 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'competition', 'race', 'training', 'nervous', 'whistle', 'medal', 'result'. \n\n>Band 4: 'Whistle', 'medal', 'training'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I practiced', 'I ran'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article errors.\n\n**Micro flaws identified:**\n- article error: '100 meters race', 'with result', 'exciting day'"
    },
    {
        "sample_id": "syn_p2_v5_g4_082",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful app.",
        "transcript_cleaned": "I use a map app called Google Maps. It is very useful. It helps me find places. I use it when I travel. It shows the best way. It tells me which bus to take. It saves time. I do not get lost anymore. The app is free. I downloaded it on my phone. It works with GPS. I think it is clever invention. Everyone uses it. It is essential for modern life.",
        "word_count": 74,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'clever invention' -> 'a clever invention'",
            "vocab: 'map', 'app', 'useful', 'travel', 'bus', 'saves time', 'lost', 'downloaded', 'GPS', 'invention', 'essential', 'modern'. Band 5 level.",
            "repetitive: 'It'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'app', 'useful', 'travel', 'downloaded', 'GPS', 'invention', 'essential', 'modern'. >Band 4: 'Invention', 'essential', 'downloaded'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'It helps me', 'It shows'. >Band 3: Simple sentences. Not Band 5: Article error.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful app.\n\nTranscript: I use a map app called Google Maps. It is very useful. It helps me find places. I use it when I travel. It shows the best way. It tells me which bus to take. It saves time. I do not get lost anymore. The app is free. I downloaded it on my phone. It works with GPS. I think it is clever invention. Everyone uses it. It is essential for modern life.\n\nWord Count: 74 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'app', 'useful', 'travel', 'downloaded', 'GPS', 'invention', 'essential', 'modern'. \n\n>Band 4: 'Invention', 'essential', 'downloaded'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'It helps me', 'It shows'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article error.\n\n**Micro flaws identified:**\n- article error: 'clever invention'"
    },
    {
        "sample_id": "syn_p2_v5_g4_083",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a photograph.",
        "transcript_cleaned": "I have a photo of my graduation. I am wearing a black gown. I am holding a diploma. My parents are standing next to me. We are all smiling. It was a sunny day. The photo is bright. I keep it in a frame on my desk. When I look at it, I feel proud. I worked hard for my degree. This photo captures a special moment. It reminds me of my achievement.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'graduation', 'gown', 'diploma', 'smiling', 'bright', 'frame', 'desk', 'degree', 'captures', 'moment', 'achievement'. Band 5 level.",
            "repetitive: 'I', 'It'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'graduation', 'gown', 'diploma', 'frame', 'degree', 'captures', 'moment', 'achievement'. >Band 4: 'Captures', 'achievement', 'diploma'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I am wearing', 'I keep it'. >Band 3: Simple sentences. Not Band 5: Very limited range.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a photograph.\n\nTranscript: I have a photo of my graduation. I am wearing a black gown. I am holding a diploma. My parents are standing next to me. We are all smiling. It was a sunny day. The photo is bright. I keep it in a frame on my desk. When I look at it, I feel proud. I worked hard for my degree. This photo captures a special moment. It reminds me of my achievement.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'graduation', 'gown', 'diploma', 'frame', 'degree', 'captures', 'moment', 'achievement'. \n\n>Band 4: 'Captures', 'achievement', 'diploma'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I am wearing', 'I keep it'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Very limited range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g4_084",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a garden you visited.",
        "transcript_cleaned": "I visited a rose garden in the park. It was very beautiful. There were many colors. Red, white, pink roses. The smell was sweet. I walked on the path. I saw butterflies on the flowers. It was peaceful place. I sat on a bench and read a book. I stayed there for an hour. I like gardens because they are quiet. I want to grow roses in my house. It is hard work but rewarding.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'peaceful place' -> 'a peaceful place'",
            "vocab: 'rose garden', 'colors', 'smell', 'sweet', 'path', 'butterflies', 'peaceful', 'bench', 'quiet', 'grow', 'rewarding'. Band 5 level.",
            "repetitive: 'I'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'rose garden', 'smell', 'path', 'butterflies', 'peaceful', 'bench', 'grow', 'rewarding'. >Band 4: 'Rewarding', 'peaceful', 'butterflies'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I walked', 'I saw'. >Band 3: Simple sentences. Not Band 5: Article error.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a garden you visited.\n\nTranscript: I visited a rose garden in the park. It was very beautiful. There were many colors. Red, white, pink roses. The smell was sweet. I walked on the path. I saw butterflies on the flowers. It was peaceful place. I sat on a bench and read a book. I stayed there for an hour. I like gardens because they are quiet. I want to grow roses in my house. It is hard work but rewarding.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'rose garden', 'smell', 'path', 'butterflies', 'peaceful', 'bench', 'grow', 'rewarding'. \n\n>Band 4: 'Rewarding', 'peaceful', 'butterflies'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I walked', 'I saw'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article error.\n\n**Micro flaws identified:**\n- article error: 'peaceful place'"
    },
    {
        "sample_id": "syn_p2_v5_g4_085",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I had to fix my computer. It was broken. The screen was black. I did not know what to do. I called my friend. He told me to check the cables. I opened the computer case. It was dusty inside. I cleaned it. Then I checked the wires. One wire was loose. I fixed it. When I turned it on, it worked. I was relieved. It was difficult task because I am not good with machines.",
        "word_count": 77,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'difficult task' -> 'a difficult task'",
            "vocab: 'fix', 'broken', 'screen', 'cables', 'case', 'dusty', 'wires', 'loose', 'relieved', 'machines'. Band 5 level.",
            "repetitive: 'I', 'It'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'fix', 'broken', 'cables', 'dusty', 'wires', 'loose', 'relieved', 'machines'. >Band 4: 'Relieved', 'loose', 'cables'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I called', 'I opened'. >Band 3: Simple sentences. Not Band 5: Article error.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I had to fix my computer. It was broken. The screen was black. I did not know what to do. I called my friend. He told me to check the cables. I opened the computer case. It was dusty inside. I cleaned it. Then I checked the wires. One wire was loose. I fixed it. When I turned it on, it worked. I was relieved. It was difficult task because I am not good with machines.\n\nWord Count: 77 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'fix', 'broken', 'cables', 'dusty', 'wires', 'loose', 'relieved', 'machines'. \n\n>Band 4: 'Relieved', 'loose', 'cables'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I called', 'I opened'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article error.\n\n**Micro flaws identified:**\n- article error: 'difficult task'"
    },
    {
        "sample_id": "syn_p2_v5_g4_086",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a meal you prepared.",
        "transcript_cleaned": "I cooked dinner for my parents. I made spaghetti. It is Italian dish. I bought pasta and tomato sauce. I also bought meat. I cooked the meat in a pan. I added the sauce. It smelled good. I boiled the pasta. Then I mixed them together. We ate it with salad. My parents liked it. They said it was delicious. I was happy. Cooking is fun but tiring. I want to learn more recipes.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'Italian dish' -> 'an Italian dish'",
            "vocab: 'cooked', 'spaghetti', 'dish', 'pasta', 'sauce', 'meat', 'pan', 'boiled', 'mixed', 'salad', 'delicious', 'recipes'. Band 5 level.",
            "repetitive: 'I', 'It'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'spaghetti', 'dish', 'sauce', 'pan', 'boiled', 'mixed', 'delicious', 'recipes'. >Band 4: 'Boiled', 'mixed', 'recipes'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I cooked', 'I added'. >Band 3: Simple sentences. Not Band 5: Article error.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a meal you prepared.\n\nTranscript: I cooked dinner for my parents. I made spaghetti. It is Italian dish. I bought pasta and tomato sauce. I also bought meat. I cooked the meat in a pan. I added the sauce. It smelled good. I boiled the pasta. Then I mixed them together. We ate it with salad. My parents liked it. They said it was delicious. I was happy. Cooking is fun but tiring. I want to learn more recipes.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'spaghetti', 'dish', 'sauce', 'pan', 'boiled', 'mixed', 'delicious', 'recipes'. \n\n>Band 4: 'Boiled', 'mixed', 'recipes'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I cooked', 'I added'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article error.\n\n**Micro flaws identified:**\n- article error: 'Italian dish'"
    },
    {
        "sample_id": "syn_p2_v5_g4_087",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a goal you achieved.",
        "transcript_cleaned": "I learned to play guitar. It was my goal. I bought a guitar last year. I practiced every day. My fingers hurt at first. I watched videos on YouTube. I learned chords. It was difficult. But I did not stop. After three months, I could play a song. I played for my friends. They clapped. I felt proud. Achieving a goal feels good. Now I want to learn more songs. Music makes me happy.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'guitar', 'goal', 'practiced', 'fingers', 'chords', 'stop', 'song', 'clapped', 'proud', 'achieving'. Band 5 level.",
            "repetitive: 'I'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'guitar', 'goal', 'practiced', 'chords', 'clapped', 'proud', 'achieving'. >Band 4: 'Chords', 'achieving', 'proud'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I bought', 'I practiced'. >Band 3: Simple sentences. Not Band 5: Very limited range.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a goal you achieved.\n\nTranscript: I learned to play guitar. It was my goal. I bought a guitar last year. I practiced every day. My fingers hurt at first. I watched videos on YouTube. I learned chords. It was difficult. But I did not stop. After three months, I could play a song. I played for my friends. They clapped. I felt proud. Achieving a goal feels good. Now I want to learn more songs. Music makes me happy.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'guitar', 'goal', 'practiced', 'chords', 'clapped', 'proud', 'achieving'. \n\n>Band 4: 'Chords', 'achieving', 'proud'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I bought', 'I practiced'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Very limited range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g4_088",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you received.",
        "transcript_cleaned": "I received a phone from my parents. It was my birthday gift. It is a smartphone. It is black and thin. I like it very much. I use it to call friends. I also play games. It has a good camera. I take many photos. It was expensive gift. I said thank you to my parents. I take care of it. I put a cover on it. A phone is useful for everything.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'expensive gift' -> 'an expensive gift'",
            "vocab: 'received', 'phone', 'smartphone', 'thin', 'camera', 'photos', 'cover', 'useful'. Band 5 level.",
            "repetitive: 'It', 'I'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'received', 'smartphone', 'camera', 'cover', 'useful'. >Band 4: 'Smartphone', 'received'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I received', 'I use'. >Band 3: Simple sentences. Not Band 5: Article error.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a gift you received.\n\nTranscript: I received a phone from my parents. It was my birthday gift. It is a smartphone. It is black and thin. I like it very much. I use it to call friends. I also play games. It has a good camera. I take many photos. It was expensive gift. I said thank you to my parents. I take care of it. I put a cover on it. A phone is useful for everything.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'received', 'smartphone', 'camera', 'cover', 'useful'. \n\n>Band 4: 'Smartphone', 'received'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I received', 'I use'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article error.\n\n**Micro flaws identified:**\n- article error: 'expensive gift'"
    },
    {
        "sample_id": "syn_p2_v5_g4_089",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a job you would like to have.",
        "transcript_cleaned": "I want to be a teacher. I like children. I want to teach English. It is interesting job. I can help students learn. I think teachers are important. They share knowledge. I have to study at university first. It takes four years. I need to be patient and kind. Teachers work hard. But they have long holidays. I think I will be good teacher. I want to make a difference.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'interesting job' -> 'an interesting job'",
            "article error: 'good teacher' -> 'a good teacher'",
            "vocab: 'teacher', 'children', 'teach', 'students', 'knowledge', 'university', 'patient', 'kind', 'holidays', 'difference'. Band 5 level.",
            "repetitive: 'I want', 'teachers'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'teach', 'knowledge', 'university', 'patient', 'holidays', 'difference'. >Band 4: 'Knowledge', 'patient', 'difference'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I want', 'I can help'. >Band 3: Simple sentences. Not Band 5: Article errors.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a job you would like to have.\n\nTranscript: I want to be a teacher. I like children. I want to teach English. It is interesting job. I can help students learn. I think teachers are important. They share knowledge. I have to study at university first. It takes four years. I need to be patient and kind. Teachers work hard. But they have long holidays. I think I will be good teacher. I want to make a difference.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'teach', 'knowledge', 'university', 'patient', 'holidays', 'difference'. \n\n>Band 4: 'Knowledge', 'patient', 'difference'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I want', 'I can help'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article errors.\n\n**Micro flaws identified:**\n- article error: 'interesting job', 'good teacher'"
    },
    {
        "sample_id": "syn_p2_v5_g4_090",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical period.",
        "transcript_cleaned": "I like the dinosaur period. It was millions of years ago. Dinosaurs lived on Earth. They were very big. Some ate plants, some ate meat. T-Rex was famous dinosaur. It was scary. I learned about them in school. I saw skeletons in museum. It is amazing to think about them. They died a long time ago. I watched movies about dinosaurs. Jurassic Park is my favorite. I wish I could see a real dinosaur.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'famous dinosaur' -> 'a famous dinosaur'",
            "article error: 'in museum' -> 'in a museum' or 'museums'",
            "vocab: 'dinosaur', 'period', 'millions', 'plants', 'meat', 'skeletons', 'museum', 'amazing', 'real'. Band 5 level.",
            "repetitive: 'It', 'They'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'dinosaur', 'period', 'millions', 'skeletons', 'museum', 'amazing', 'real'. >Band 4: 'Skeletons', 'period', 'amazing'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'They were', 'I learned'. >Band 3: Simple sentences. Not Band 5: Article errors.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical period.\n\nTranscript: I like the dinosaur period. It was millions of years ago. Dinosaurs lived on Earth. They were very big. Some ate plants, some ate meat. T-Rex was famous dinosaur. It was scary. I learned about them in school. I saw skeletons in museum. It is amazing to think about them. They died a long time ago. I watched movies about dinosaurs. Jurassic Park is my favorite. I wish I could see a real dinosaur.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'dinosaur', 'period', 'millions', 'skeletons', 'museum', 'amazing', 'real'. \n\n>Band 4: 'Skeletons', 'period', 'amazing'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'They were', 'I learned'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article errors.\n\n**Micro flaws identified:**\n- article error: 'famous dinosaur', 'in museum'"
    },
    {
        "sample_id": "syn_p2_v5_g4_091",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a successful person.",
        "transcript_cleaned": "I admire Bill Gates. He is a successful person. He started Microsoft. It is a big computer company. He is very rich. But he is also kind. He gives money to charity. He helps sick people in poor countries. He is smart and hard-working. I read about him in a magazine. He changed the world with technology. I respect him. Success is not just money, it is helping others.",
        "word_count": 70,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'admire', 'successful', 'company', 'rich', 'charity', 'sick', 'poor', 'smart', 'hard-working', 'technology', 'respect'. Band 5 level.",
            "repetitive: 'He is', 'He'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'admire', 'successful', 'company', 'charity', 'technology', 'respect'. >Band 4: 'Charity', 'technology', 'admire'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'He is', 'He started'. >Band 3: Simple sentences. Not Band 5: Very limited range.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a successful person.\n\nTranscript: I admire Bill Gates. He is a successful person. He started Microsoft. It is a big computer company. He is very rich. But he is also kind. He gives money to charity. He helps sick people in poor countries. He is smart and hard-working. I read about him in a magazine. He changed the world with technology. I respect him. Success is not just money, it is helping others.\n\nWord Count: 70 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'admire', 'successful', 'company', 'charity', 'technology', 'respect'. \n\n>Band 4: 'Charity', 'technology', 'admire'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'He is', 'He started'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Very limited range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g4_092",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a place you study.",
        "transcript_cleaned": "I study in my bedroom. I have a desk and chair. It is my private place. It is quiet. I can concentrate there. I have a lamp on my desk. I keep my books on a shelf. I study every evening. Sometimes I listen to music. It helps me relax. My room is comfortable. I do not like studying in library. It is too far. My room is the best place for me.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'in library' -> 'in the library'",
            "vocab: 'study', 'desk', 'private', 'quiet', 'concentrate', 'lamp', 'shelf', 'relax', 'comfortable', 'library'. Band 5 level.",
            "repetitive: 'I', 'It is'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'private', 'concentrate', 'shelf', 'relax', 'comfortable', 'library'. >Band 4: 'Concentrate', 'private', 'comfortable'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I have', 'It is'. >Band 3: Simple sentences. Not Band 5: Article error and limited range.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a place you study.\n\nTranscript: I study in my bedroom. I have a desk and chair. It is my private place. It is quiet. I can concentrate there. I have a lamp on my desk. I keep my books on a shelf. I study every evening. Sometimes I listen to music. It helps me relax. My room is comfortable. I do not like studying in library. It is too far. My room is the best place for me.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'private', 'concentrate', 'shelf', 'relax', 'comfortable', 'library'. \n\n>Band 4: 'Concentrate', 'private', 'comfortable'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I have', 'It is'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article error and limited range.\n\n**Micro flaws identified:**\n- article error: 'in library'"
    },
    {
        "sample_id": "syn_p2_v5_g4_093",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of clothes you wear often.",
        "transcript_cleaned": "I often wear jeans. They are blue. I wear them every day. They are comfortable. I bought them in a shop near my house. They were cheap. Jeans are good because they are strong. I can wear them with t-shirt or shirt. They fit me well. I have three pairs of jeans. I wash them once a week. They are casual clothes. I do not wear them to weddings. I like my jeans.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'with t-shirt' -> 'with a t-shirt'",
            "vocab: 'jeans', 'comfortable', 'shop', 'cheap', 'strong', 't-shirt', 'fit', 'pairs', 'casual', 'weddings'. Band 5 level.",
            "repetitive: 'They', 'wear'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'jeans', 'comfortable', 'strong', 'fit', 'pairs', 'casual', 'weddings'. >Band 4: 'Casual', 'comfortable', 'fit'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'They are', 'I wear'. >Band 3: Simple sentences. Not Band 5: Article error.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a piece of clothes you wear often.\n\nTranscript: I often wear jeans. They are blue. I wear them every day. They are comfortable. I bought them in a shop near my house. They were cheap. Jeans are good because they are strong. I can wear them with t-shirt or shirt. They fit me well. I have three pairs of jeans. I wash them once a week. They are casual clothes. I do not wear them to weddings. I like my jeans.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'jeans', 'comfortable', 'strong', 'fit', 'pairs', 'casual', 'weddings'. \n\n>Band 4: 'Casual', 'comfortable', 'fit'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'They are', 'I wear'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article error.\n\n**Micro flaws identified:**\n- article error: 'with t-shirt'"
    },
    {
        "sample_id": "syn_p2_v5_g4_094",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a TV show.",
        "transcript_cleaned": "I watch a show called Friends. It is American comedy. It is about six friends. They live in New York. It is very funny. They sit in a cafe and talk. They have problems but they help each other. The actors are good. I laugh a lot. It helps me learn English slang. I watch it on computer. It is old show but still popular. I like the character Joey. He is stupid but cute.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'American comedy' -> 'an American comedy'",
            "article error: 'on computer' -> 'on the computer' or 'a computer'",
            "article error: 'old show' -> 'an old show'",
            "vocab: 'comedy', 'actors', 'slang', 'popular', 'character', 'stupid', 'cute'. Band 5 level.",
            "repetitive: 'It is'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'comedy', 'actors', 'slang', 'popular', 'character', 'cute'. >Band 4: 'Slang', 'character', 'comedy'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'It is', 'They live'. >Band 3: Simple sentences. Not Band 5: Article errors.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a TV show.\n\nTranscript: I watch a show called Friends. It is American comedy. It is about six friends. They live in New York. It is very funny. They sit in a cafe and talk. They have problems but they help each other. The actors are good. I laugh a lot. It helps me learn English slang. I watch it on computer. It is old show but still popular. I like the character Joey. He is stupid but cute.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'comedy', 'actors', 'slang', 'popular', 'character', 'cute'. \n\n>Band 4: 'Slang', 'character', 'comedy'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'It is', 'They live'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article errors.\n\n**Micro flaws identified:**\n- article error: 'American comedy', 'on computer', 'old show'"
    },
    {
        "sample_id": "syn_p2_v5_g4_095",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a song.",
        "transcript_cleaned": "I like the song \"Happy\". It is by Pharrell Williams. It is a pop song. The rhythm is fast. It makes me want to dance. The lyrics are simple. It says \"Clap along if you feel happy\". I listen to it in the morning. It gives me energy. The singer has a good voice. I saw the music video. People were dancing in the street. It is a cheerful song. I love it.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'pop song', 'rhythm', 'dance', 'lyrics', 'clap', 'energy', 'voice', 'music video', 'cheerful'. Band 5 level.",
            "repetitive: 'It'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'pop song', 'rhythm', 'lyrics', 'energy', 'voice', 'music video', 'cheerful'. >Band 4: 'Rhythm', 'lyrics', 'cheerful'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'It is', 'I listen'. >Band 3: Simple sentences. Not Band 5: Very limited range.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a song.\n\nTranscript: I like the song \"Happy\". It is by Pharrell Williams. It is a pop song. The rhythm is fast. It makes me want to dance. The lyrics are simple. It says \"Clap along if you feel happy\". I listen to it in the morning. It gives me energy. The singer has a good voice. I saw the music video. People were dancing in the street. It is a cheerful song. I love it.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'pop song', 'rhythm', 'lyrics', 'energy', 'voice', 'music video', 'cheerful'. \n\n>Band 4: 'Rhythm', 'lyrics', 'cheerful'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'It is', 'I listen'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Very limited range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g4_096",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a holiday.",
        "transcript_cleaned": "I went to the beach last year. It was summer. The weather was very hot. I went with my family. We stayed in a hotel. It was near the sea. We swam every day. I built sandcastles. We ate seafood. It was fresh. In the evening, we walked on the beach. I saw the sunset. It was beautiful. I relaxed a lot. I did not think about school. It was a perfect holiday.",
        "word_count": 72,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'beach', 'summer', 'hotel', 'sea', 'swam', 'sandcastles', 'seafood', 'fresh', 'sunset', 'relaxed', 'perfect'. Band 5 level.",
            "repetitive: 'I', 'It was'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'beach', 'hotel', 'swam', 'sandcastles', 'seafood', 'sunset', 'relaxed', 'perfect'. >Band 4: 'Sandcastles', 'seafood', 'relaxed'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I went', 'It was'. >Band 3: Simple sentences. Not Band 5: Very limited range.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a holiday.\n\nTranscript: I went to the beach last year. It was summer. The weather was very hot. I went with my family. We stayed in a hotel. It was near the sea. We swam every day. I built sandcastles. We ate seafood. It was fresh. In the evening, we walked on the beach. I saw the sunset. It was beautiful. I relaxed a lot. I did not think about school. It was a perfect holiday.\n\nWord Count: 72 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'beach', 'hotel', 'swam', 'sandcastles', 'seafood', 'sunset', 'relaxed', 'perfect'. \n\n>Band 4: 'Sandcastles', 'seafood', 'relaxed'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I went', 'It was'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Very limited range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g4_097",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a thing you bought.",
        "transcript_cleaned": "I bought a new bag. It is a backpack. I bought it for school. It is red and black. It has many pockets. I can put my books and laptop in it. It is very strong. I bought it online. It was cheap. I like it because it is comfortable. I carry it every day. My friends like it too. It is useful item. I hope it lasts for a long time.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'useful item' -> 'a useful item'",
            "vocab: 'bag', 'backpack', 'pockets', 'laptop', 'online', 'cheap', 'comfortable', 'carry', 'useful', 'lasts'. Band 5 level.",
            "repetitive: 'It is', 'I'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'backpack', 'pockets', 'laptop', 'online', 'comfortable', 'carry', 'useful', 'lasts'. >Band 4: 'Backpack', 'laptop', 'lasts'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I bought', 'It is'. >Band 3: Simple sentences. Not Band 5: Article error and limited range.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a thing you bought.\n\nTranscript: I bought a new bag. It is a backpack. I bought it for school. It is red and black. It has many pockets. I can put my books and laptop in it. It is very strong. I bought it online. It was cheap. I like it because it is comfortable. I carry it every day. My friends like it too. It is useful item. I hope it lasts for a long time.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'backpack', 'pockets', 'laptop', 'online', 'comfortable', 'carry', 'useful', 'lasts'. \n\n>Band 4: 'Backpack', 'laptop', 'lasts'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I bought', 'It is'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article error and limited range.\n\n**Micro flaws identified:**\n- article error: 'useful item'"
    },
    {
        "sample_id": "syn_p2_v5_g4_098",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a sport match.",
        "transcript_cleaned": "I watched a tennis match. It was on TV. It was Wimbledon final. Two players played. They were very good. They hit the ball hard. They ran fast. The match was long. It took four hours. The crowd cheered. I was excited. One player won. He cried. He was happy. I like tennis. It is exciting sport. But I cannot play it well. I want to learn.",
        "word_count": 68,
        "response_type": "long_turn",
        "micro_flaws": [
            "article error: 'Wimbledon final' -> 'the Wimbledon final'",
            "article error: 'exciting sport' -> 'an exciting sport'",
            "vocab: 'tennis match', 'final', 'players', 'hit', 'ball', 'crowd', 'cheered', 'excited', 'won'. Band 5 level.",
            "repetitive: 'They', 'It'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'tennis match', 'final', 'players', 'crowd', 'cheered', 'excited'. >Band 4: 'Crowd', 'cheered', 'final'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I watched', 'They were'. >Band 3: Simple sentences. Not Band 5: Article errors.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a sport match.\n\nTranscript: I watched a tennis match. It was on TV. It was Wimbledon final. Two players played. They were very good. They hit the ball hard. They ran fast. The match was long. It took four hours. The crowd cheered. I was excited. One player won. He cried. He was happy. I like tennis. It is exciting sport. But I cannot play it well. I want to learn.\n\nWord Count: 68 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'tennis match', 'final', 'players', 'crowd', 'cheered', 'excited'. \n\n>Band 4: 'Crowd', 'cheered', 'final'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I watched', 'They were'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Article errors.\n\n**Micro flaws identified:**\n- article error: 'Wimbledon final', 'exciting sport'"
    },
    {
        "sample_id": "syn_p2_v5_g4_099",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I had to clean my house. It was very dirty. My parents were away. I had to do it alone. I swept the floor. I washed the dishes. I cleaned the bathroom. It was disgusting. I worked for three hours. I was very tired. My back hurt. But the house looked clean. My parents were happy when they came home. It was hard work. I do not like cleaning.",
        "word_count": 70,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'clean', 'dirty', 'alone', 'swept', 'floor', 'washed', 'dishes', 'bathroom', 'disgusting', 'hurt'. Band 5 level.",
            "repetitive: 'I'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'clean', 'dirty', 'swept', 'washed', 'disgusting', 'tired', 'hurt'. >Band 4: 'Swept', 'disgusting'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I had to', 'I swept'. >Band 3: Simple sentences. Not Band 5: Very limited range.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I had to clean my house. It was very dirty. My parents were away. I had to do it alone. I swept the floor. I washed the dishes. I cleaned the bathroom. It was disgusting. I worked for three hours. I was very tired. My back hurt. But the house looked clean. My parents were happy when they came home. It was hard work. I do not like cleaning.\n\nWord Count: 70 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'clean', 'dirty', 'swept', 'washed', 'disgusting', 'tired', 'hurt'. \n\n>Band 4: 'Swept', 'disgusting'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I had to', 'I swept'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Very limited range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g4_100",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a crowded place.",
        "transcript_cleaned": "I went to a shopping mall on Saturday. It was very crowded. There were many people. They were shopping for clothes. It was noisy. Babies were crying. I wanted to buy shoes. But the shop was full. I had to wait in line. It took a long time. I felt hot and tired. I do not like crowds. I prefer to shop online. It is easier. The mall is too busy.",
        "word_count": 72,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'shopping mall', 'crowded', 'noisy', 'crying', 'shop', 'wait in line', 'online', 'busy'. Band 5 level.",
            "repetitive: 'I', 'It was'."
        ],
        "grammar_profile": {
            "complexity": "low",
            "accuracy": "low",
            "flexibility": "low"
        },
        "vocab_reason": "[LR5] Key evidence: 'shopping mall', 'crowded', 'noisy', 'wait in line', 'online', 'busy'. >Band 4: 'Wait in line', 'crowded'. Not Band 6: Basic sentences.",
        "grammar_reason": "[GRA4] Key evidence: Simple sentences. 'I went', 'It was'. >Band 3: Simple sentences. Not Band 5: Very limited range.",
        "vocabulary": 5,
        "grammar": 4,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a crowded place.\n\nTranscript: I went to a shopping mall on Saturday. It was very crowded. There were many people. They were shopping for clothes. It was noisy. Babies were crying. I wanted to buy shoes. But the shop was full. I had to wait in line. It took a long time. I felt hot and tired. I do not like crowds. I prefer to shop online. It is easier. The mall is too busy.\n\nWord Count: 72 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'shopping mall', 'crowded', 'noisy', 'wait in line', 'online', 'busy'. \n\n>Band 4: 'Wait in line', 'crowded'.\n\nNot Band 6: Basic sentences.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Key evidence: Simple sentences. 'I went', 'It was'. \n\n>Band 3: Simple sentences.\n\nNot Band 5: Very limited range.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
