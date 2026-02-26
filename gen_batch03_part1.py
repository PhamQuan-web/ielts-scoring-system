import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch03.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v5_g6_151",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a cafe you visited.",
        "transcript_cleaned": "I want to describe a cafe which is located in the city center. It is a nice place. I went there with my friend who lives near my house. We ordered coffee and cake. The coffee was good, but the cake was very sweet. The cafe has big windows so we could see the street. Although it was crowded, we found a table. I like this place because it is comfortable. We stayed there for two hours and talked about our school.",
        "word_count": 83,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'nice', 'good', 'sweet', 'big', 'comfortable'. Band 5 level.",
            "grammar: 'The cafe has big windows so we could see' (Correct complex sentence)",
            "grammar: 'Although it was crowded, we found' (Correct concession)"
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'cafe', 'city center', 'ordered', 'sweet', 'crowded', 'comfortable'. >Band 4: 'Comfortable', 'city center'. Not Band 6: Basic adjectives 'nice', 'good', 'big'.",
        "grammar_reason": "[GRA6] Key evidence: Mix of simple and complex forms. 'which is located', 'who lives', 'Although it was'. >Band 5: Good control of relative clauses and connectors. Not Band 7: Sentences are accurate but not sophisticated.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a cafe you visited.\n\nTranscript: I want to describe a cafe which is located in the city center. It is a nice place. I went there with my friend who lives near my house. We ordered coffee and cake. The coffee was good, but the cake was very sweet. The cafe has big windows so we could see the street. Although it was crowded, we found a table. I like this place because it is comfortable. We stayed there for two hours and talked about our school.\n\nWord Count: 83 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'cafe', 'city center', 'ordered', 'sweet', 'crowded', 'comfortable'. \n\n>Band 4: 'Comfortable', 'city center'.\n\nNot Band 6: Basic adjectives 'nice', 'good', 'big'.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: Mix of simple and complex forms. 'which is located', 'who lives', 'Although it was'. \n\n>Band 5: Good control of relative clauses and connectors.\n\nNot Band 7: Sentences are accurate but not sophisticated.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_152",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a person who helps you.",
        "transcript_cleaned": "My sister is the person who helps me the most. She is older than me. When I have homework that is difficult, she explains it to me. She is very smart. She also helps me clean my room if I am busy. I think she is kind. Sometimes we fight, but we make up quickly. I rely on her because she gives good advice. For example, she told me how to study for exams. I am lucky to have a sister like her.",
        "word_count": 85,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'helps', 'homework', 'difficult', 'explains', 'smart', 'clean', 'busy', 'kind', 'fight', 'advice'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'homework', 'explains', 'smart', 'rely on', 'advice', 'exams'. >Band 4: 'Rely on', 'advice'. Not Band 6: 'Good advice', 'very smart' are basic collocations.",
        "grammar_reason": "[GRA6] Key evidence: Relative clauses 'who helps me', 'that is difficult'. Conditionals 'if I am busy'. >Band 5: Structures used correctly. Not Band 7: Lacks flexibility.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a person who helps you.\n\nTranscript: My sister is the person who helps me the most. She is older than me. When I have homework that is difficult, she explains it to me. She is very smart. She also helps me clean my room if I am busy. I think she is kind. Sometimes we fight, but we make up quickly. I rely on her because she gives good advice. For example, she told me how to study for exams. I am lucky to have a sister like her.\n\nWord Count: 85 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'homework', 'explains', 'smart', 'rely on', 'advice', 'exams'. \n\n>Band 4: 'Rely on', 'advice'.\n\nNot Band 6: 'Good advice', 'very smart' are basic collocations.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: Relative clauses 'who helps me', 'that is difficult'. Conditionals 'if I am busy'. \n\n>Band 5: Structures used correctly.\n\nNot Band 7: Lacks flexibility.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_153",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Red Fort in India. It is a very old building which was built many years ago. It is made of red stone. The walls are very high. When I went there, I saw many tourists. They were taking photos. The guide told us about the kings who lived there. It was interesting. The building is huge and beautiful. I think it is important to protect old buildings because they show our history. I enjoyed my visit very much.",
        "word_count": 83,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'old', 'building', 'stone', 'high', 'tourists', 'photos', 'guide', 'kings', 'huge', 'protect', 'history'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'tourists', 'guide', 'protect', 'history', 'huge'. >Band 4: 'Protect', 'history'. Not Band 6: 'Very old', 'very high'. Basic descriptors.",
        "grammar_reason": "[GRA6] Key evidence: Passive voice 'was built'. Relative clause 'who lived there'. Complex sentence 'because they show'. >Band 5: Accurate use of complex forms. Not Band 7: Simple sentence chains remain.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Red Fort in India. It is a very old building which was built many years ago. It is made of red stone. The walls are very high. When I went there, I saw many tourists. They were taking photos. The guide told us about the kings who lived there. It was interesting. The building is huge and beautiful. I think it is important to protect old buildings because they show our history. I enjoyed my visit very much.\n\nWord Count: 83 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'tourists', 'guide', 'protect', 'history', 'huge'. \n\n>Band 4: 'Protect', 'history'.\n\nNot Band 6: 'Very old', 'very high'. Basic descriptors.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: Passive voice 'was built'. Relative clause 'who lived there'. Complex sentence 'because they show'. \n\n>Band 5: Accurate use of complex forms.\n\nNot Band 7: Simple sentence chains remain.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_154",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a journey you made.",
        "transcript_cleaned": "I traveled to the beach by car last summer. It was a long journey that took five hours. I went with my parents. While my father was driving, I listened to music. The scenery was nice. We saw mountains and trees. When we arrived, we were tired but happy. We stayed in a hotel which was near the sea. The next day, we swam in the water. I like traveling by car because we can stop whenever we want.",
        "word_count": 81,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'beach', 'journey', 'driving', 'scenery', 'mountains', 'arrived', 'hotel', 'sea', 'swam'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'journey', 'scenery', 'arrived', 'hotel', 'swam'. >Band 4: 'Scenery', 'arrived'. Not Band 6: 'Nice', 'happy', 'good'. Basic adjectives.",
        "grammar_reason": "[GRA6] Key evidence: 'that took five hours', 'While my father was driving', 'which was near'. >Band 5: Good range of complex structures (relative clauses, time clauses). Not Band 7: Repetitive structures.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a journey you made.\n\nTranscript: I traveled to the beach by car last summer. It was a long journey that took five hours. I went with my parents. While my father was driving, I listened to music. The scenery was nice. We saw mountains and trees. When we arrived, we were tired but happy. We stayed in a hotel which was near the sea. The next day, we swam in the water. I like traveling by car because we can stop whenever we want.\n\nWord Count: 81 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'journey', 'scenery', 'arrived', 'hotel', 'swam'. \n\n>Band 4: 'Scenery', 'arrived'.\n\nNot Band 6: 'Nice', 'happy', 'good'. Basic adjectives.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'that took five hours', 'While my father was driving', 'which was near'. \n\n>Band 5: Good range of complex structures (relative clauses, time clauses).\n\nNot Band 7: Repetitive structures.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_155",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party you went to.",
        "transcript_cleaned": "I went to a birthday party for my friend. It was last Saturday. There were many people who I did not know. But I met some new friends. We ate pizza and cake. The food was delicious. We played games that were fun. My friend received many gifts. She was very happy. I think parties are good because we can relax. I left the party late at night. I was tired but I had a good time.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'birthday party', 'met', 'pizza', 'cake', 'delicious', 'games', 'gifts', 'relax'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'birthday party', 'delicious', 'received', 'gifts', 'relax'. >Band 4: 'Received', 'delicious'. Not Band 6: 'Very happy', 'good time'. Basic phrases.",
        "grammar_reason": "[GRA6] Key evidence: 'who I did not know', 'games that were fun', 'because we can relax'. >Band 5: Correct relative clauses and reasons. Not Band 7: Short sentences dominate.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party you went to.\n\nTranscript: I went to a birthday party for my friend. It was last Saturday. There were many people who I did not know. But I met some new friends. We ate pizza and cake. The food was delicious. We played games that were fun. My friend received many gifts. She was very happy. I think parties are good because we can relax. I left the party late at night. I was tired but I had a good time.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'birthday party', 'delicious', 'received', 'gifts', 'relax'. \n\n>Band 4: 'Received', 'delicious'.\n\nNot Band 6: 'Very happy', 'good time'. Basic phrases.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'who I did not know', 'games that were fun', 'because we can relax'. \n\n>Band 5: Correct relative clauses and reasons.\n\nNot Band 7: Short sentences dominate.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_156",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I had to write a long report for my job. It was difficult because I did not have much time. I had to finish it in two days. I used my computer to type it. I searched for information on the internet. There was a lot of data which I needed to analyze. I worked until late night. Finally, I finished the report. My boss said it was good. I felt relieved. Hard work is necessary for success.",
        "word_count": 80,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'report', 'job', 'finish', 'type', 'searched', 'information', 'data', 'analyze', 'boss', 'relieved', 'necessary', 'success'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'report', 'searched', 'information', 'data', 'analyze', 'relieved', 'necessary'. >Band 4: 'Analyze', 'data', 'relieved'. Not Band 6: 'Good', 'hard work'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'because I did not have', 'which I needed to analyze'. >Band 5: Complex sentences used accurately. Not Band 7: Repetitive 'I had to', 'I used'.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I had to write a long report for my job. It was difficult because I did not have much time. I had to finish it in two days. I used my computer to type it. I searched for information on the internet. There was a lot of data which I needed to analyze. I worked until late night. Finally, I finished the report. My boss said it was good. I felt relieved. Hard work is necessary for success.\n\nWord Count: 80 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'report', 'searched', 'information', 'data', 'analyze', 'relieved', 'necessary'. \n\n>Band 4: 'Analyze', 'data', 'relieved'.\n\nNot Band 6: 'Good', 'hard work'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'because I did not have', 'which I needed to analyze'. \n\n>Band 5: Complex sentences used accurately.\n\nNot Band 7: Repetitive 'I had to', 'I used'.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_157",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a movie you like.",
        "transcript_cleaned": "I like the movie Harry Potter. It is a fantasy movie about magic. The main character is a boy who is a wizard. He goes to a special school where he learns magic. He has two friends who help him. They fight a bad wizard. The story is exciting. I like the special effects. They look real. I have watched this movie many times. It is my favorite because it is imaginative. I recommend it to everyone.",
        "word_count": 79,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'fantasy', 'magic', 'character', 'wizard', 'special', 'fight', 'effects', 'real', 'imaginative', 'recommend'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'fantasy', 'wizard', 'special effects', 'imaginative', 'recommend'. >Band 4: 'Imaginative', 'wizard'. Not Band 6: 'Bad wizard', 'look real'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'boy who is a wizard', 'school where he learns', 'friends who help him'. >Band 5: Relative clauses used correctly. Not Band 7: Structure is very predictable.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a movie you like.\n\nTranscript: I like the movie Harry Potter. It is a fantasy movie about magic. The main character is a boy who is a wizard. He goes to a special school where he learns magic. He has two friends who help him. They fight a bad wizard. The story is exciting. I like the special effects. They look real. I have watched this movie many times. It is my favorite because it is imaginative. I recommend it to everyone.\n\nWord Count: 79 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'fantasy', 'wizard', 'special effects', 'imaginative', 'recommend'. \n\n>Band 4: 'Imaginative', 'wizard'.\n\nNot Band 6: 'Bad wizard', 'look real'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'boy who is a wizard', 'school where he learns', 'friends who help him'. \n\n>Band 5: Relative clauses used correctly.\n\nNot Band 7: Structure is very predictable.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_158",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you received.",
        "transcript_cleaned": "I received a laptop for my birthday. My parents gave it to me. It is a very useful gift which I use every day. I use it to study and play games. It is small and light, so I can carry it in my bag. I was very happy when I got it. It was expensive. I thanked my parents. I take good care of it because it is valuable. It is the best gift I have ever received.",
        "word_count": 81,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'laptop', 'useful', 'study', 'games', 'light', 'carry', 'expensive', 'valuable'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'laptop', 'useful', 'carry', 'expensive', 'valuable'. >Band 4: 'Valuable', 'useful'. Not Band 6: 'Small and light', 'very happy'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'gift which I use', 'so I can carry', 'because it is valuable'. >Band 5: Mix of complex and compound sentences correctly used. Not Band 7: Simple vocabulary limits grammatical range.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a gift you received.\n\nTranscript: I received a laptop for my birthday. My parents gave it to me. It is a very useful gift which I use every day. I use it to study and play games. It is small and light, so I can carry it in my bag. I was very happy when I got it. It was expensive. I thanked my parents. I take good care of it because it is valuable. It is the best gift I have ever received.\n\nWord Count: 81 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'laptop', 'useful', 'carry', 'expensive', 'valuable'. \n\n>Band 4: 'Valuable', 'useful'.\n\nNot Band 6: 'Small and light', 'very happy'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'gift which I use', 'so I can carry', 'because it is valuable'. \n\n>Band 5: Mix of complex and compound sentences correctly used.\n\nNot Band 7: Simple vocabulary limits grammatical range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_159",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a game you played.",
        "transcript_cleaned": "I played football when I was in school. It is a team sport. We played on a big field. There were eleven players in my team. I was the goalkeeper who stops the ball. It was exciting. We practiced every week. Sometimes we won, and sometimes we lost. I liked it because I could run and exercise. It is good for health. Although I am busy now, I still watch football on TV. It brings back good memories.",
        "word_count": 80,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'football', 'team sport', 'field', 'players', 'goalkeeper', 'stops', 'exciting', 'practiced', 'won', 'lost', 'exercise', 'health', 'memories'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'team sport', 'goalkeeper', 'practiced', 'exercise', 'memories'. >Band 4: 'Goalkeeper', 'memories'. Not Band 6: 'Good for health', 'big field'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'goalkeeper who stops', 'because I could run', 'Although I am busy'. >Band 5: Complex sentences used effectively. Not Band 7: Some sentences are short and choppy.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a game you played.\n\nTranscript: I played football when I was in school. It is a team sport. We played on a big field. There were eleven players in my team. I was the goalkeeper who stops the ball. It was exciting. We practiced every week. Sometimes we won, and sometimes we lost. I liked it because I could run and exercise. It is good for health. Although I am busy now, I still watch football on TV. It brings back good memories.\n\nWord Count: 80 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'team sport', 'goalkeeper', 'practiced', 'exercise', 'memories'. \n\n>Band 4: 'Goalkeeper', 'memories'.\n\nNot Band 6: 'Good for health', 'big field'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'goalkeeper who stops', 'because I could run', 'Although I am busy'. \n\n>Band 5: Complex sentences used effectively.\n\nNot Band 7: Some sentences are short and choppy.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_160",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a photo you like.",
        "transcript_cleaned": "I like a photo of my family which hangs on the wall. It was taken five years ago. We were on holiday in the mountains. Everyone is smiling in the photo. My father is wearing a funny hat. The scenery behind us is beautiful. There are trees and snow. I like this photo because it reminds me of a happy time. We look very young in it. I will keep this photo forever because it is special to me.",
        "word_count": 80,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'photo', 'hangs', 'wall', 'holiday', 'mountains', 'smiling', 'scenery', 'snow', 'reminds', 'forever', 'special'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'hangs', 'scenery', 'reminds', 'forever', 'special'. >Band 4: 'Scenery', 'reminds'. Not Band 6: 'Funny hat', 'beautiful'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'photo... which hangs', 'because it reminds me', 'because it is special'. >Band 5: Correct use of subordinate clauses. Not Band 7: Repetitive sentence patterns.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a photo you like.\n\nTranscript: I like a photo of my family which hangs on the wall. It was taken five years ago. We were on holiday in the mountains. Everyone is smiling in the photo. My father is wearing a funny hat. The scenery behind us is beautiful. There are trees and snow. I like this photo because it reminds me of a happy time. We look very young in it. I will keep this photo forever because it is special to me.\n\nWord Count: 80 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'hangs', 'scenery', 'reminds', 'forever', 'special'. \n\n>Band 4: 'Scenery', 'reminds'.\n\nNot Band 6: 'Funny hat', 'beautiful'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'photo... which hangs', 'because it reminds me', 'because it is special'. \n\n>Band 5: Correct use of subordinate clauses.\n\nNot Band 7: Repetitive sentence patterns.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_161",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book you read.",
        "transcript_cleaned": "I read a book called \"Life of Pi\". It is an adventure story. It is about a boy who is lost at sea. He is on a boat with a tiger. It sounds scary, but it is interesting. He has to survive for many days. He catches fish to eat. I read it last month. The story taught me about courage. I think the writer is very clever. It is one of the best books that I have read.",
        "word_count": 81,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'adventure', 'story', 'lost', 'sea', 'boat', 'tiger', 'scary', 'survive', 'catches', 'courage', 'clever'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'adventure', 'survive', 'courage', 'clever'. >Band 4: 'Survive', 'courage'. Not Band 6: 'Scary', 'interesting'. Basic adjectives.",
        "grammar_reason": "[GRA6] Key evidence: 'boy who is lost', 'It sounds scary, but', 'books that I have read'. >Band 5: Mix of complex structures. Not Band 7: Short sentences predominate.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book you read.\n\nTranscript: I read a book called \"Life of Pi\". It is an adventure story. It is about a boy who is lost at sea. He is on a boat with a tiger. It sounds scary, but it is interesting. He has to survive for many days. He catches fish to eat. I read it last month. The story taught me about courage. I think the writer is very clever. It is one of the best books that I have read.\n\nWord Count: 81 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'adventure', 'survive', 'courage', 'clever'. \n\n>Band 4: 'Survive', 'courage'.\n\nNot Band 6: 'Scary', 'interesting'. Basic adjectives.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'boy who is lost', 'It sounds scary, but', 'books that I have read'. \n\n>Band 5: Mix of complex structures.\n\nNot Band 7: Short sentences predominate.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_162",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I like the sunflower. It is a tall plant which has a big yellow flower. It grows in the summer. It likes the sun and turns towards it. I have some sunflowers in my garden. They look very bright and happy. I water them every evening. When the flower dies, it has seeds. We can eat the seeds. I think sunflowers are beautiful because they are colorful. They make my garden look nice. Everyone likes them.",
        "word_count": 77,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'sunflower', 'tall', 'plant', 'yellow', 'grows', 'garden', 'bright', 'seeds', 'colorful'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'sunflower', 'grows', 'seeds', 'colorful', 'bright'. >Band 4: 'Seeds', 'colorful'. Not Band 6: 'Big yellow flower', 'look nice'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'plant which has', 'When the flower dies', 'because they are colorful'. >Band 5: Correct complex sentences. Not Band 7: Simple sentence chains.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I like the sunflower. It is a tall plant which has a big yellow flower. It grows in the summer. It likes the sun and turns towards it. I have some sunflowers in my garden. They look very bright and happy. I water them every evening. When the flower dies, it has seeds. We can eat the seeds. I think sunflowers are beautiful because they are colorful. They make my garden look nice. Everyone likes them.\n\nWord Count: 77 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'sunflower', 'grows', 'seeds', 'colorful', 'bright'. \n\n>Band 4: 'Seeds', 'colorful'.\n\nNot Band 6: 'Big yellow flower', 'look nice'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'plant which has', 'When the flower dies', 'because they are colorful'. \n\n>Band 5: Correct complex sentences.\n\nNot Band 7: Simple sentence chains.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_163",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I had to choose a high school. It was a difficult decision. There were two schools which I liked. One was near my house, but the other was better. I talked to my parents about it. They said I should choose the better school. Although it was far, I chose it. I have to travel by bus every day. It takes time, but I learn a lot there. I am happy with my choice because the teachers are good.",
        "word_count": 81,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'choose', 'high school', 'decision', 'better', 'travel', 'bus', 'choice', 'teachers'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'choose', 'decision', 'travel', 'choice'. >Band 4: 'Decision', 'choice'. Not Band 6: 'Better school', 'good'. Basic comparison.",
        "grammar_reason": "[GRA6] Key evidence: 'schools which I liked', 'Although it was far', 'because the teachers are good'. >Band 5: Good control of complex forms. Not Band 7: Limited range.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I had to choose a high school. It was a difficult decision. There were two schools which I liked. One was near my house, but the other was better. I talked to my parents about it. They said I should choose the better school. Although it was far, I chose it. I have to travel by bus every day. It takes time, but I learn a lot there. I am happy with my choice because the teachers are good.\n\nWord Count: 81 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'choose', 'decision', 'travel', 'choice'. \n\n>Band 4: 'Decision', 'choice'.\n\nNot Band 6: 'Better school', 'good'. Basic comparison.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'schools which I liked', 'Although it was far', 'because the teachers are good'. \n\n>Band 5: Good control of complex forms.\n\nNot Band 7: Limited range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_164",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a healthy habit.",
        "transcript_cleaned": "I exercise every morning. It is a habit that I started last year. I run in the park which is near my home. I run for thirty minutes. It makes me feel energetic. Before, I was lazy and tired. Now I am fit. I also eat healthy food like fruits and vegetables. I avoid fast food. I think health is important. If you exercise, you will live longer. I recommend this habit to my friends.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'exercise', 'habit', 'park', 'energetic', 'lazy', 'tired', 'fit', 'healthy', 'avoid', 'recommend'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'exercise', 'habit', 'energetic', 'fit', 'avoid', 'recommend'. >Band 4: 'Energetic', 'avoid'. Not Band 6: 'Healthy food', 'important'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'habit that I started', 'park which is near', 'If you exercise...'. >Band 5: Complex sentences used correctly. Not Band 7: Short sentences.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a healthy habit.\n\nTranscript: I exercise every morning. It is a habit that I started last year. I run in the park which is near my home. I run for thirty minutes. It makes me feel energetic. Before, I was lazy and tired. Now I am fit. I also eat healthy food like fruits and vegetables. I avoid fast food. I think health is important. If you exercise, you will live longer. I recommend this habit to my friends.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'exercise', 'habit', 'energetic', 'fit', 'avoid', 'recommend'. \n\n>Band 4: 'Energetic', 'avoid'.\n\nNot Band 6: 'Healthy food', 'important'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'habit that I started', 'park which is near', 'If you exercise...'. \n\n>Band 5: Complex sentences used correctly.\n\nNot Band 7: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_165",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical figure.",
        "transcript_cleaned": "I admire Albert Einstein. He was a famous scientist. He was born in Germany. He was very clever. He discovered many things about science. He is known for his theory of relativity. Although he was smart, he was humble. He had funny hair. I saw his picture in a book. He helped us understand the universe. He won a Nobel Prize. I think he is a genius. His ideas changed the world.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'admire', 'scientist', 'clever', 'discovered', 'theory', 'relativity', 'humble', 'universe', 'genius'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'scientist', 'discovered', 'theory', 'relativity', 'humble', 'universe', 'genius'. >Band 4: 'Theory', 'universe', 'genius'. Not Band 6: 'Funny hair', 'clever'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'Although he was smart', 'He is known for'. >Band 5: Correct use of passive and concession. Not Band 7: Simple sentence structure dominates.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical figure.\n\nTranscript: I admire Albert Einstein. He was a famous scientist. He was born in Germany. He was very clever. He discovered many things about science. He is known for his theory of relativity. Although he was smart, he was humble. He had funny hair. I saw his picture in a book. He helped us understand the universe. He won a Nobel Prize. I think he is a genius. His ideas changed the world.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'scientist', 'discovered', 'theory', 'relativity', 'humble', 'universe', 'genius'. \n\n>Band 4: 'Theory', 'universe', 'genius'.\n\nNot Band 6: 'Funny hair', 'clever'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'Although he was smart', 'He is known for'. \n\n>Band 5: Correct use of passive and concession.\n\nNot Band 7: Simple sentence structure dominates.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_166",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful skill.",
        "transcript_cleaned": "I learned how to swim. It is a skill which is very important. I learned it when I was a child. My father taught me in a pool. At first, I was scared of the water. But my father encouraged me. I practiced until I could float. Now I can swim fast. I think everyone should learn swimming because it can save your life. It is also good exercise. I enjoy swimming in the sea in summer.",
        "word_count": 79,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'skill', 'important', 'taught', 'pool', 'scared', 'encouraged', 'practiced', 'float', 'save', 'exercise'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'skill', 'scared', 'encouraged', 'practiced', 'float', 'save life'. >Band 4: 'Encouraged', 'float'. Not Band 6: 'Swim fast', 'good exercise'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'skill which is', 'when I was a child', 'practiced until I could', 'because it can save'. >Band 5: Complex sentences used correctly. Not Band 7: Repetitive 'I'.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful skill.\n\nTranscript: I learned how to swim. It is a skill which is very important. I learned it when I was a child. My father taught me in a pool. At first, I was scared of the water. But my father encouraged me. I practiced until I could float. Now I can swim fast. I think everyone should learn swimming because it can save your life. It is also good exercise. I enjoy swimming in the sea in summer.\n\nWord Count: 79 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'skill', 'scared', 'encouraged', 'practiced', 'float', 'save life'. \n\n>Band 4: 'Encouraged', 'float'.\n\nNot Band 6: 'Swim fast', 'good exercise'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'skill which is', 'when I was a child', 'practiced until I could', 'because it can save'. \n\n>Band 5: Complex sentences used correctly.\n\nNot Band 7: Repetitive 'I'.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_167",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a festival.",
        "transcript_cleaned": "I like the Moon Festival. It is a festival which happens in autumn. It is a time when families gather together. We eat mooncakes. They are sweet and round. We look at the full moon. It is beautiful. Children play with lanterns. I like this festival because the atmosphere is happy. We tell stories about the moon. It is a traditional festival in my country. I always look forward to it.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'festival', 'autumn', 'gather', 'mooncakes', 'sweet', 'round', 'lanterns', 'atmosphere', 'traditional', 'look forward'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'festival', 'autumn', 'gather', 'mooncakes', 'lanterns', 'atmosphere', 'traditional'. >Band 4: 'Atmosphere', 'traditional'. Not Band 6: 'Beautiful', 'happy'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'festival which happens', 'time when families gather', 'because the atmosphere is'. >Band 5: Accurate relative and causal clauses. Not Band 7: Simple range.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a festival.\n\nTranscript: I like the Moon Festival. It is a festival which happens in autumn. It is a time when families gather together. We eat mooncakes. They are sweet and round. We look at the full moon. It is beautiful. Children play with lanterns. I like this festival because the atmosphere is happy. We tell stories about the moon. It is a traditional festival in my country. I always look forward to it.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'festival', 'autumn', 'gather', 'mooncakes', 'lanterns', 'atmosphere', 'traditional'. \n\n>Band 4: 'Atmosphere', 'traditional'.\n\nNot Band 6: 'Beautiful', 'happy'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'festival which happens', 'time when families gather', 'because the atmosphere is'. \n\n>Band 5: Accurate relative and causal clauses.\n\nNot Band 7: Simple range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_168",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of news.",
        "transcript_cleaned": "I heard some news about a storm. I saw it on TV yesterday. The reporter said a big storm is coming. It will bring heavy rain and strong wind. People should stay at home. I was worried because my house is old. I called my parents to tell them. They live near the coast. They said they are safe. It is important to watch the news so we can prepare. I hope the storm will pass quickly.",
        "word_count": 79,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'news', 'storm', 'reporter', 'heavy rain', 'wind', 'stay', 'worried', 'coast', 'safe', 'prepare'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'storm', 'reporter', 'heavy rain', 'worried', 'coast', 'prepare'. >Band 4: 'Reporter', 'coast'. Not Band 6: 'Big storm', 'strong wind'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'reporter said... is coming', 'worried because', 'so we can prepare'. >Band 5: Complex sentences used correctly. Not Band 7: Repetitive 'I', 'It'.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a piece of news.\n\nTranscript: I heard some news about a storm. I saw it on TV yesterday. The reporter said a big storm is coming. It will bring heavy rain and strong wind. People should stay at home. I was worried because my house is old. I called my parents to tell them. They live near the coast. They said they are safe. It is important to watch the news so we can prepare. I hope the storm will pass quickly.\n\nWord Count: 79 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'storm', 'reporter', 'heavy rain', 'worried', 'coast', 'prepare'. \n\n>Band 4: 'Reporter', 'coast'.\n\nNot Band 6: 'Big storm', 'strong wind'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'reporter said... is coming', 'worried because', 'so we can prepare'. \n\n>Band 5: Complex sentences used correctly.\n\nNot Band 7: Repetitive 'I', 'It'.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_169",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a toy you liked.",
        "transcript_cleaned": "I had a teddy bear when I was young. It was brown and soft. I named it Beary. I slept with it every night. My grandmother gave it to me. It was a special gift. I talked to it when I was sad. It was my best friend. Although it is old now, I still keep it. It has one eye missing. I like it because it brings back memories of my childhood. It is very precious to me.",
        "word_count": 81,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'teddy bear', 'soft', 'named', 'gift', 'sad', 'missing', 'memories', 'childhood', 'precious'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'teddy bear', 'soft', 'gift', 'memories', 'childhood', 'precious'. >Band 4: 'Memories', 'precious'. Not Band 6: 'Best friend', 'old'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'when I was young', 'Although it is old', 'because it brings back'. >Band 5: Complex sentences used correctly. Not Band 7: Simple sentence structure.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a toy you liked.\n\nTranscript: I had a teddy bear when I was young. It was brown and soft. I named it Beary. I slept with it every night. My grandmother gave it to me. It was a special gift. I talked to it when I was sad. It was my best friend. Although it is old now, I still keep it. It has one eye missing. I like it because it brings back memories of my childhood. It is very precious to me.\n\nWord Count: 81 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'teddy bear', 'soft', 'gift', 'memories', 'childhood', 'precious'. \n\n>Band 4: 'Memories', 'precious'.\n\nNot Band 6: 'Best friend', 'old'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'when I was young', 'Although it is old', 'because it brings back'. \n\n>Band 5: Complex sentences used correctly.\n\nNot Band 7: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_170",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a place you study.",
        "transcript_cleaned": "I study in the library which is near my university. It is a quiet place. There are many desks and chairs. I go there because I can concentrate better. At home, it is noisy. The library has many books that I can use. I also use the computer there. I usually stay for three hours. I meet my friends there too. We help each other. I think the library is the best place for studying.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'library', 'university', 'quiet', 'desks', 'concentrate', 'noisy', 'books', 'computer', 'studying'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'library', 'university', 'concentrate', 'noisy', 'studying'. >Band 4: 'Concentrate', 'university'. Not Band 6: 'Quiet place', 'best place'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'library which is', 'because I can concentrate', 'books that I can use'. >Band 5: Relative clauses used correctly. Not Band 7: Sentences are short.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a place you study.\n\nTranscript: I study in the library which is near my university. It is a quiet place. There are many desks and chairs. I go there because I can concentrate better. At home, it is noisy. The library has many books that I can use. I also use the computer there. I usually stay for three hours. I meet my friends there too. We help each other. I think the library is the best place for studying.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'library', 'university', 'concentrate', 'noisy', 'studying'. \n\n>Band 4: 'Concentrate', 'university'.\n\nNot Band 6: 'Quiet place', 'best place'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'library which is', 'because I can concentrate', 'books that I can use'. \n\n>Band 5: Relative clauses used correctly.\n\nNot Band 7: Sentences are short.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_171",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a website you use.",
        "transcript_cleaned": "I use Wikipedia a lot. It is an encyclopedia on the internet. It has information about everything. When I have homework, I use it. I can find facts about history and science. It is free to use. Anyone can write articles on it. Sometimes the information is wrong, so I check other websites too. But usually it is helpful. I like it because it is easy to read. It helps me learn new things.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'encyclopedia', 'internet', 'information', 'homework', 'facts', 'history', 'science', 'articles', 'check', 'helpful'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'encyclopedia', 'information', 'facts', 'articles', 'check', 'helpful'. >Band 4: 'Encyclopedia', 'articles'. Not Band 6: 'Easy to read', 'new things'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'When I have homework', 'so I check', 'because it is easy'. >Band 5: Connectors and time clauses used correctly. Not Band 7: Simple structure.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a website you use.\n\nTranscript: I use Wikipedia a lot. It is an encyclopedia on the internet. It has information about everything. When I have homework, I use it. I can find facts about history and science. It is free to use. Anyone can write articles on it. Sometimes the information is wrong, so I check other websites too. But usually it is helpful. I like it because it is easy to read. It helps me learn new things.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'encyclopedia', 'information', 'facts', 'articles', 'check', 'helpful'. \n\n>Band 4: 'Encyclopedia', 'articles'.\n\nNot Band 6: 'Easy to read', 'new things'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'When I have homework', 'so I check', 'because it is easy'. \n\n>Band 5: Connectors and time clauses used correctly.\n\nNot Band 7: Simple structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_172",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a goal you achieved.",
        "transcript_cleaned": "I wanted to run 10 kilometers. It was my goal. I am not a sporty person, so it was hard. I started running in the park. At first, I could only run 1 kilometer. My legs hurt. But I did not give up. I practiced every day for two months. Finally, I ran 10 kilometers. I was very tired but proud. I achieved my goal. It showed me that hard work is important.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'goal', 'sporty', 'hard', 'park', 'hurt', 'give up', 'practiced', 'proud', 'achieved', 'important'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'goal', 'sporty', 'give up', 'practiced', 'proud', 'achieved'. >Band 4: 'Achieved', 'sporty', 'give up'. Not Band 6: 'Hard work', 'tired'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'so it was hard', 'that hard work is important'. >Band 5: Coherent sentences. Not Band 7: Repetitive 'I'.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a goal you achieved.\n\nTranscript: I wanted to run 10 kilometers. It was my goal. I am not a sporty person, so it was hard. I started running in the park. At first, I could only run 1 kilometer. My legs hurt. But I did not give up. I practiced every day for two months. Finally, I ran 10 kilometers. I was very tired but proud. I achieved my goal. It showed me that hard work is important.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'goal', 'sporty', 'give up', 'practiced', 'proud', 'achieved'. \n\n>Band 4: 'Achieved', 'sporty', 'give up'.\n\nNot Band 6: 'Hard work', 'tired'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'so it was hard', 'that hard work is important'. \n\n>Band 5: Coherent sentences.\n\nNot Band 7: Repetitive 'I'.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_173",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a TV program.",
        "transcript_cleaned": "I watch a show called \"The Voice\". It is a singing competition. There are four judges who are famous singers. People come to sing. If they are good, the judges turn their chairs. It is exciting. I like to guess who will win. I watch it with my family every week. We enjoy the music. Some singers have amazing voices. I think it is a good show because it gives people a chance to be famous.",
        "word_count": 77,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'competition', 'judges', 'famous', 'singers', 'chairs', 'exciting', 'guess', 'win', 'voices', 'chance'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'competition', 'judges', 'exciting', 'guess', 'voices', 'chance'. >Band 4: 'Judges', 'competition'. Not Band 6: 'Good show', 'amazing voices'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'judges who are famous', 'If they are good', 'because it gives'. >Band 5: Relative clauses and conditionals used correctly. Not Band 7: Simple sentence structure.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a TV program.\n\nTranscript: I watch a show called \"The Voice\". It is a singing competition. There are four judges who are famous singers. People come to sing. If they are good, the judges turn their chairs. It is exciting. I like to guess who will win. I watch it with my family every week. We enjoy the music. Some singers have amazing voices. I think it is a good show because it gives people a chance to be famous.\n\nWord Count: 77 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'competition', 'judges', 'exciting', 'guess', 'voices', 'chance'. \n\n>Band 4: 'Judges', 'competition'.\n\nNot Band 6: 'Good show', 'amazing voices'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'judges who are famous', 'If they are good', 'because it gives'. \n\n>Band 5: Relative clauses and conditionals used correctly.\n\nNot Band 7: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_174",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a crowded place.",
        "transcript_cleaned": "I went to a night market which was very crowded. It was in the city center. There were hundreds of people walking and eating. It was noisy. I held my bag tightly because I was afraid of thieves. The food smelled good. I bought some clothes which were cheap. Although it was crowded, I enjoyed it. The atmosphere was lively. I think it is a popular place for young people.",
        "word_count": 72,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'night market', 'crowded', 'city center', 'noisy', 'tightly', 'thieves', 'smelled', 'cheap', 'atmosphere', 'lively', 'popular'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'night market', 'crowded', 'tightly', 'thieves', 'atmosphere', 'lively'. >Band 4: 'Thieves', 'lively'. Not Band 6: 'Smelled good', 'popular place'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'market which was', 'because I was afraid', 'Although it was'. >Band 5: Complex sentences used correctly. Not Band 7: Limited range.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a crowded place.\n\nTranscript: I went to a night market which was very crowded. It was in the city center. There were hundreds of people walking and eating. It was noisy. I held my bag tightly because I was afraid of thieves. The food smelled good. I bought some clothes which were cheap. Although it was crowded, I enjoyed it. The atmosphere was lively. I think it is a popular place for young people.\n\nWord Count: 72 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'night market', 'crowded', 'tightly', 'thieves', 'atmosphere', 'lively'. \n\n>Band 4: 'Thieves', 'lively'.\n\nNot Band 6: 'Smelled good', 'popular place'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'market which was', 'because I was afraid', 'Although it was'. \n\n>Band 5: Complex sentences used correctly.\n\nNot Band 7: Limited range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v5_g6_175",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a family member.",
        "transcript_cleaned": "I want to talk about my mother. She is the person who I love the most. She is a nurse. She works in a hospital. She is very kind and patient. She cooks delicious food for us. When I am sick, she takes care of me. She works hard to earn money. She wants me to study well. I admire her because she is strong. She is my role model.",
        "word_count": 72,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'nurse', 'hospital', 'patient', 'delicious', 'sick', 'takes care', 'earn', 'admire', 'role model'. Band 5 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR5] Key evidence: 'nurse', 'patient', 'delicious', 'admire', 'role model'. >Band 4: 'Role model', 'admire'. Not Band 6: 'Works hard', 'study well'. Basic.",
        "grammar_reason": "[GRA6] Key evidence: 'person who I love', 'When I am sick', 'because she is strong'. >Band 5: Correct relative and adverbial clauses. Not Band 7: Repetitive 'She'.",
        "vocabulary": 5,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a family member.\n\nTranscript: I want to talk about my mother. She is the person who I love the most. She is a nurse. She works in a hospital. She is very kind and patient. She cooks delicious food for us. When I am sick, she takes care of me. She works hard to earn money. She wants me to study well. I admire her because she is strong. She is my role model.\n\nWord Count: 72 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Key evidence: 'nurse', 'patient', 'delicious', 'admire', 'role model'. \n\n>Band 4: 'Role model', 'admire'.\n\nNot Band 6: 'Works hard', 'study well'. Basic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'person who I love', 'When I am sick', 'because she is strong'. \n\n>Band 5: Correct relative and adverbial clauses. Not Band 7: Repetitive 'She'.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
