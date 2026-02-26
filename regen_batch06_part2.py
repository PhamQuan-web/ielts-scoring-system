import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch06.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v7_g7_476",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Sagrada Familia in Barcelona, which is an architectural masterpiece designed by Antoni Gaudi. The basilica is known for its towering spires that reach towards the sky. The interior is filled with colorful light from the stained glass windows, creating a spiritual atmosphere. It is still under construction after more than a century, which is quite remarkable. The intricate details on the facade are mind-boggling and tell stories from the Bible. It is a unique blend of Gothic and Art Nouveau styles. Visiting this place was a surreal experience that I will never forget. It stands as a symbol of the city.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'architectural masterpiece', 'basilica', 'towering spires', 'stained glass', 'spiritual atmosphere', 'intricate details', 'facade', 'mind-boggling', 'unique blend', 'Art Nouveau', 'surreal'. Band 7 level.",
             "grammar: 'Familia... which is', 'known for its', 'still under construction', 'Visiting... was'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'architectural masterpiece', 'towering spires', 'stained glass', 'spiritual atmosphere', 'intricate details', 'mind-boggling', 'blend', 'surreal'. >Band 6: 'Mind-boggling', 'intricate'. Not Band 8: 'Symbol of the city' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'designed by Antoni Gaudi', 'filled with colorful light', 'Visiting this place was'. >Band 6: Participle phrases and gerund subjects used correctly. Not Band 8: Lacks full range.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Sagrada Familia in Barcelona, which is an architectural masterpiece designed by Antoni Gaudi. The basilica is known for its towering spires that reach towards the sky. The interior is filled with colorful light from the stained glass windows, creating a spiritual atmosphere. It is still under construction after more than a century, which is quite remarkable. The intricate details on the facade are mind-boggling and tell stories from the Bible. It is a unique blend of Gothic and Art Nouveau styles. Visiting this place was a surreal experience that I will never forget. It stands as a symbol of the city.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'architectural masterpiece', 'towering spires', 'stained glass', 'spiritual atmosphere', 'intricate details', 'mind-boggling', 'blend', 'surreal'. \n\n>Band 6: 'Mind-boggling', 'intricate'.\n\nNot Band 8: 'Symbol of the city' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'designed by Antoni Gaudi', 'filled with colorful light', 'Visiting this place was'. \n\n>Band 6: Participle phrases and gerund subjects used correctly.\n\nNot Band 8: Lacks full range.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_477",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I learned to play the guitar, which was physically demanding at first. Pressing the strings hurt my fingers, and I had to build calluses. Memorizing the chords was tedious and required a lot of repetition. I practiced daily to improve my dexterity and coordination. Learning to read sheet music was another challenge that I faced. However, playing my first full song was incredibly rewarding. It has become a creative outlet for me to express my emotions. The process taught me that persistence leads to success. I am now able to entertain my friends with my music.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'physically demanding', 'calluses', 'memorizing', 'chords', 'tedious', 'repetition', 'dexterity', 'coordination', 'sheet music', 'rewarding', 'creative outlet', 'persistence'. Band 7 level.",
             "grammar: 'guitar, which was', 'Memorizing... was', 'Learning to read', 'taught me that'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'physically demanding', 'calluses', 'memorizing', 'chords', 'tedious', 'dexterity', 'rewarding', 'creative outlet', 'persistence'. >Band 6: 'Dexterity', 'tedious'. Not Band 8: 'Entertain' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'guitar, which was', 'Memorizing the chords', 'Learning to read'. >Band 6: Gerunds and relative clauses used correctly. Not Band 8: Very short sentences included.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I learned to play the guitar, which was physically demanding at first. Pressing the strings hurt my fingers, and I had to build calluses. Memorizing the chords was tedious and required a lot of repetition. I practiced daily to improve my dexterity and coordination. Learning to read sheet music was another challenge that I faced. However, playing my first full song was incredibly rewarding. It has become a creative outlet for me to express my emotions. The process taught me that persistence leads to success. I am now able to entertain my friends with my music.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'physically demanding', 'calluses', 'memorizing', 'chords', 'tedious', 'dexterity', 'rewarding', 'creative outlet', 'persistence'. \n\n>Band 6: 'Dexterity', 'tedious'.\n\nNot Band 8: 'Entertain' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'guitar, which was', 'Memorizing the chords', 'Learning to read'. \n\n>Band 6: Gerunds and relative clauses used correctly.\n\nNot Band 8: Very short sentences included.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_478",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read Pride and Prejudice by Jane Austen, which is a classic novel. It serves as a witty social commentary on the manners of the 19th century. The protagonist, Elizabeth Bennet, is intelligent and independent, which I admire. Her relationship with Mr. Darcy is complicated and full of misunderstandings. The dialogue is sharp and humorous throughout the book. It explores themes of class, reputation, and marriage. I found it very engaging because the characters are so well-developed. It is a beloved classic that has stood the test of time. I would recommend it to anyone who enjoys romance.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'classic novel', 'witty', 'social commentary', 'manners', 'protagonist', 'intelligent', 'independent', 'complicated', 'misunderstandings', 'dialogue', 'sharp', 'humorous', 'reputation', 'engaging', 'well-developed'. Band 7 level.",
             "grammar: 'Austen, which is', 'serves as a', 'protagonist... is', 'found it very engaging'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'witty', 'social commentary', 'protagonist', 'intelligent', 'independent', 'complicated', 'dialogue', 'sharp', 'humorous', 'beloved classic', 'well-developed'. >Band 6: 'Witty', 'commentary'. Not Band 8: 'Romance' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'Austen, which is', 'serves as a witty', 'found it very engaging'. >Band 6: Relative clauses and complex noun phrases used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read Pride and Prejudice by Jane Austen, which is a classic novel. It serves as a witty social commentary on the manners of the 19th century. The protagonist, Elizabeth Bennet, is intelligent and independent, which I admire. Her relationship with Mr. Darcy is complicated and full of misunderstandings. The dialogue is sharp and humorous throughout the book. It explores themes of class, reputation, and marriage. I found it very engaging because the characters are so well-developed. It is a beloved classic that has stood the test of time. I would recommend it to anyone who enjoys romance.\n\nWord Count: 105 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'witty', 'social commentary', 'protagonist', 'intelligent', 'independent', 'complicated', 'dialogue', 'sharp', 'humorous', 'beloved classic', 'well-developed'. \n\n>Band 6: 'Witty', 'commentary'.\n\nNot Band 8: 'Romance' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Austen, which is', 'serves as a witty', 'found it very engaging'. \n\n>Band 6: Relative clauses and complex noun phrases used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_479",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I went to a pool party last weekend at my friend's house. The weather was sweltering, so the cool water was very refreshing. We had a barbecue with juicy burgers and hot dogs. Someone brought a volleyball net, and we played a competitive game. The music was upbeat, creating a fun atmosphere. I got a bit sunburnt, but I didn't care because I was having fun. It was a great way to cool off and relax. We chatted and swam until the sun went down. It was a perfect summer day.",
        "word_count": 97,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'sweltering', 'refreshing', 'barbecue', 'juicy', 'competitive', 'upbeat', 'atmosphere', 'sunburnt', 'cool off'. Band 7 level.",
             "grammar: 'sweltering, so the', 'brought... and we played', 'creating a fun atmosphere'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'sweltering', 'refreshing', 'barbecue', 'competitive', 'upbeat', 'atmosphere', 'sunburnt', 'cool off'. >Band 6: 'Sweltering', 'competitive'. Not Band 8: 'Juicy burgers' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'sweltering, so the', 'creating a fun atmosphere', 'until the sun went'. >Band 6: Causal and time clauses used correctly. Not Band 8: Very short sentences included.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I went to a pool party last weekend at my friend's house. The weather was sweltering, so the cool water was very refreshing. We had a barbecue with juicy burgers and hot dogs. Someone brought a volleyball net, and we played a competitive game. The music was upbeat, creating a fun atmosphere. I got a bit sunburnt, but I didn't care because I was having fun. It was a great way to cool off and relax. We chatted and swam until the sun went down. It was a perfect summer day.\n\nWord Count: 97 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'sweltering', 'refreshing', 'barbecue', 'competitive', 'upbeat', 'atmosphere', 'sunburnt', 'cool off'. \n\n>Band 6: 'Sweltering', 'competitive'.\n\nNot Band 8: 'Juicy burgers' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'sweltering, so the', 'creating a fun atmosphere', 'until the sun went'. \n\n>Band 6: Causal and time clauses used correctly.\n\nNot Band 8: Very short sentences included.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_480",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I rely on my smartwatch to keep track of my daily activities. It tracks my sleep patterns and monitors my heart rate. I can check notifications for messages without looking at my phone, which is very convenient. It reminds me to breathe and relax when I am stressed. It has a sleek and modern design that I really like. I can customize the watch face to match my outfit. It is a versatile accessory that helps me stay organized and healthy. I feel like I am missing something if I forget to wear it.",
        "word_count": 101,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'rely on', 'keep track', 'sleep patterns', 'monitors', 'notifications', 'convenient', 'breathe', 'sleek', 'customize', 'watch face', 'versatile', 'accessory', 'organized'. Band 7 level.",
             "grammar: 'smartwatch to keep', 'phone, which is', 'reminds me to breathe'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "good"
        },
        "vocab_reason": "[LR7] Key evidence: 'smartwatch', 'tracks', 'sleep patterns', 'notifications', 'breathe', 'relax', 'sleek design', 'customize', 'versatile', 'organized'. >Band 6: 'Versatile', 'customize'. Not Band 8: 'Messages' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'phone, which is', 'reminds me to breathe', 'helps me stay'. >Band 6: Infinitives and relative clauses used correctly. Not Band 8: Sentence flow is standard.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I rely on my smartwatch to keep track of my daily activities. It tracks my sleep patterns and monitors my heart rate. I can check notifications for messages without looking at my phone, which is very convenient. It reminds me to breathe and relax when I am stressed. It has a sleek and modern design that I really like. I can customize the watch face to match my outfit. It is a versatile accessory that helps me stay organized and healthy. I feel like I am missing something if I forget to wear it.\n\nWord Count: 101 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'smartwatch', 'tracks', 'sleep patterns', 'notifications', 'breathe', 'relax', 'sleek design', 'customize', 'versatile', 'organized'. \n\n>Band 6: 'Versatile', 'customize'.\n\nNot Band 8: 'Messages' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'phone, which is', 'reminds me to breathe', 'helps me stay'. \n\n>Band 6: Infinitives and relative clauses used correctly.\n\nNot Band 8: Sentence flow is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_481",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Colosseum, which is a massive amphitheater in Rome. The history of gladiator fights is both fascinating and horrific. I could imagine the roar of the crowd as I walked through the ruins. The structure is well-preserved despite its age. It is a powerful symbol of the Roman Empire. Walking through the stone arches was an awe-inspiring experience. It is a must-see landmark for anyone interested in history. I was amazed by the engineering skills of the ancient Romans. It is a place that really sparks the imagination.",
        "word_count": 96,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'massive', 'amphitheater', 'gladiator fights', 'fascinating', 'horrific', 'roar of the crowd', 'well-preserved', 'symbol', 'awe-inspiring', 'landmark', 'engineering skills', 'sparks'. Band 7 level.",
             "grammar: 'Colosseum, which is', 'crowd as I walked', 'Walking through... was'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'massive', 'amphitheater', 'gladiator fights', 'fascinating', 'roar of the crowd', 'well-preserved', 'symbol', 'awe-inspiring', 'landmark'. >Band 6: 'Awe-inspiring', 'well-preserved'. Not Band 8: 'History' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'Colosseum, which is', 'imagine the roar', 'Walking through... was'. >Band 6: Relative clauses and gerund subjects used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Colosseum, which is a massive amphitheater in Rome. The history of gladiator fights is both fascinating and horrific. I could imagine the roar of the crowd as I walked through the ruins. The structure is well-preserved despite its age. It is a powerful symbol of the Roman Empire. Walking through the stone arches was an awe-inspiring experience. It is a must-see landmark for anyone interested in history. I was amazed by the engineering skills of the ancient Romans. It is a place that really sparks the imagination.\n\nWord Count: 96 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'massive', 'amphitheater', 'gladiator fights', 'fascinating', 'roar of the crowd', 'well-preserved', 'symbol', 'awe-inspiring', 'landmark'. \n\n>Band 6: 'Awe-inspiring', 'well-preserved'.\n\nNot Band 8: 'History' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Colosseum, which is', 'imagine the roar', 'Walking through... was'. \n\n>Band 6: Relative clauses and gerund subjects used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_482",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I have a bonsai tree that I care for diligently. It is a miniature tree that requires careful pruning and maintenance. It is a form of art that originated in Japan. I water it sparingly to prevent root rot. It teaches me patience and precision. The shape of the tree is aesthetically pleasing and unique. It brings a sense of zen and tranquility to my home. It is a delicate living sculpture that I am proud of. Watching it grow slowly over the years has been very rewarding.",
        "word_count": 96,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'bonsai', 'diligently', 'miniature', 'pruning', 'maintenance', 'originated', 'sparingly', 'root rot', 'patience', 'precision', 'aesthetically pleasing', 'zen', 'tranquility', 'delicate', 'living sculpture', 'rewarding'. Band 7 level.",
             "grammar: 'tree that I care for', 'requires... and maintenance', 'Watching it grow'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "high",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'bonsai', 'miniature', 'pruning', 'sparingly', 'patience', 'precision', 'aesthetically pleasing', 'zen', 'delicate', 'living sculpture'. >Band 6: 'Sparingly', 'precision'. Not Band 8: 'Tree' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'tree that I care for', 'water it sparingly to', 'Watching it grow'. >Band 6: Relative clauses and gerund subjects used correctly. Not Band 8: Simple sentence structure.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I have a bonsai tree that I care for diligently. It is a miniature tree that requires careful pruning and maintenance. It is a form of art that originated in Japan. I water it sparingly to prevent root rot. It teaches me patience and precision. The shape of the tree is aesthetically pleasing and unique. It brings a sense of zen and tranquility to my home. It is a delicate living sculpture that I am proud of. Watching it grow slowly over the years has been very rewarding.\n\nWord Count: 96 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'bonsai', 'miniature', 'pruning', 'sparingly', 'patience', 'precision', 'aesthetically pleasing', 'zen', 'delicate', 'living sculpture'. \n\n>Band 6: 'Sparingly', 'precision'.\n\nNot Band 8: 'Tree' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'tree that I care for', 'water it sparingly to', 'Watching it grow'. \n\n>Band 6: Relative clauses and gerund subjects used correctly.\n\nNot Band 8: Simple sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_483",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "My friend Alice is an artist who lives in Paris. She is incredibly creative and expressive in her work. She paints vibrant landscapes that capture the beauty of nature. She has a unique perspective on life that I admire. We visit art galleries together whenever I see her. She inspires me to see beauty in everything around me. Her passion for art is infectious and motivating. She is a free spirit who follows her dreams. I always feel energized after spending time with her.",
        "word_count": 91,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'artist', 'creative', 'expressive', 'vibrant landscapes', 'capture', 'unique perspective', 'galleries', 'inspires', 'infectious', 'motivating', 'free spirit', 'energized'. Band 7 level.",
             "grammar: 'artist who lives', 'landscapes that capture', 'inspires me to see'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'artist', 'creative', 'expressive', 'vibrant landscapes', 'unique perspective', 'galleries', 'inspires', 'infectious', 'free spirit'. >Band 6: 'Infectious', 'expressive'. Not Band 8: 'Beauty' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'artist who lives', 'landscapes that capture', 'inspires me to see'. >Band 6: Relative clauses and infinitives used correctly. Not Band 8: Sentence structure is standard.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a friend.\n\nTranscript: My friend Alice is an artist who lives in Paris. She is incredibly creative and expressive in her work. She paints vibrant landscapes that capture the beauty of nature. She has a unique perspective on life that I admire. We visit art galleries together whenever I see her. She inspires me to see beauty in everything around me. Her passion for art is infectious and motivating. She is a free spirit who follows her dreams. I always feel energized after spending time with her.\n\nWord Count: 91 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'artist', 'creative', 'expressive', 'vibrant landscapes', 'unique perspective', 'galleries', 'inspires', 'infectious', 'free spirit'. \n\n>Band 6: 'Infectious', 'expressive'.\n\nNot Band 8: 'Beauty' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'artist who lives', 'landscapes that capture', 'inspires me to see'. \n\n>Band 6: Relative clauses and infinitives used correctly.\n\nNot Band 8: Sentence structure is standard.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_484",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I had to decide whether to quit my job last year. I was unhappy with the management and the toxic environment. The workload was overwhelming, and I was stressed. I worried about financial instability if I left. However, my mental health was deteriorating rapidly. I consulted my family, and they supported me. I finally handed in my resignation. It was a terrifying but necessary step for my well-being. I am now pursuing my passion for writing. It taught me to prioritize my health over my career.",
        "word_count": 92,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'quit', 'management', 'toxic environment', 'workload', 'overwhelming', 'financial instability', 'mental health', 'deteriorating', 'resignation', 'terrifying', 'necessary step', 'pursuing', 'prioritize'. Band 7 level.",
             "grammar: 'whether to quit', 'instability if I left', 'terrifying but necessary'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'quit', 'management', 'workload', 'overwhelming', 'financial instability', 'mental health', 'deteriorating', 'resignation', 'terrifying', 'necessary step', 'pursuing'. >Band 6: 'Deteriorating', 'instability'. Not Band 8: 'Job' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'whether to quit', 'instability if I left', 'terrifying but necessary'. >Band 6: Noun clauses and conditionals used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I had to decide whether to quit my job last year. I was unhappy with the management and the toxic environment. The workload was overwhelming, and I was stressed. I worried about financial instability if I left. However, my mental health was deteriorating rapidly. I consulted my family, and they supported me. I finally handed in my resignation. It was a terrifying but necessary step for my well-being. I am now pursuing my passion for writing. It taught me to prioritize my health over my career.\n\nWord Count: 92 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'quit', 'management', 'workload', 'overwhelming', 'financial instability', 'mental health', 'deteriorating', 'resignation', 'terrifying', 'necessary step', 'pursuing'. \n\n>Band 6: 'Deteriorating', 'instability'.\n\nNot Band 8: 'Job' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'whether to quit', 'instability if I left', 'terrifying but necessary'. \n\n>Band 6: Noun clauses and conditionals used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_485",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I entered a cooking competition at a local fair. I love experimenting with flavors and trying new recipes. I prepared a three-course meal for the judges. The time limit was stressful, and I almost ran out of time. I focused on presentation and taste. The judges praised my creativity and the balance of flavors. I won the first prize, which was a huge surprise. It was a validation of my culinary skills. It gave me the confidence to start my own catering business. I will never forget that day.",
        "word_count": 96,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'cooking competition', 'experimenting', 'flavors', 'three-course meal', 'time limit', 'presentation', 'praised', 'creativity', 'balance', 'validation', 'culinary skills', 'catering'. Band 7 level.",
             "grammar: 'limit was stressful', 'prize, which was', 'confidence to start'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'cooking competition', 'experimenting', 'flavors', 'three-course meal', 'time limit', 'presentation', 'praised', 'creativity', 'validation', 'culinary skills'. >Band 6: 'Validation', 'culinary'. Not Band 8: 'Meal' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'limit was stressful', 'prize, which was', 'confidence to start'. >Band 6: Relative clauses and infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I entered a cooking competition at a local fair. I love experimenting with flavors and trying new recipes. I prepared a three-course meal for the judges. The time limit was stressful, and I almost ran out of time. I focused on presentation and taste. The judges praised my creativity and the balance of flavors. I won the first prize, which was a huge surprise. It was a validation of my culinary skills. It gave me the confidence to start my own catering business. I will never forget that day.\n\nWord Count: 96 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'cooking competition', 'experimenting', 'flavors', 'three-course meal', 'time limit', 'presentation', 'praised', 'creativity', 'validation', 'culinary skills'. \n\n>Band 6: 'Validation', 'culinary'.\n\nNot Band 8: 'Meal' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'limit was stressful', 'prize, which was', 'confidence to start'. \n\n>Band 6: Relative clauses and infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_486",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Taj Mahal in Agra, India. It is a magnificent mausoleum made of white marble. The symmetry of the building is perfect and pleasing to the eye. The gardens are lush and symmetrical, adding to the beauty. It was built by an emperor for his beloved wife. It is a symbol of eternal love and devotion. The intricate carvings on the walls are breathtaking. It is a masterpiece of Mughal architecture. Seeing it at sunrise was a magical experience. It is a place of peace and beauty.",
        "word_count": 96,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'mausoleum', 'white marble', 'symmetry', 'pleasing', 'lush', 'emperor', 'beloved', 'symbol', 'eternal love', 'devotion', 'intricate carvings', 'breathtaking', 'masterpiece', 'Mughal architecture'. Band 7 level.",
             "grammar: 'made of white marble', 'built by an emperor', 'Seeing it at sunrise'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'mausoleum', 'white marble', 'symmetry', 'lush', 'emperor', 'symbol', 'eternal love', 'intricate carvings', 'breathtaking', 'masterpiece', 'Mughal architecture'. >Band 6: 'Mausoleum', 'intricate'. Not Band 8: 'Wife' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'made of white marble', 'built by an emperor', 'Seeing it at sunrise'. >Band 6: Participles and gerunds used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Taj Mahal in Agra, India. It is a magnificent mausoleum made of white marble. The symmetry of the building is perfect and pleasing to the eye. The gardens are lush and symmetrical, adding to the beauty. It was built by an emperor for his beloved wife. It is a symbol of eternal love and devotion. The intricate carvings on the walls are breathtaking. It is a masterpiece of Mughal architecture. Seeing it at sunrise was a magical experience. It is a place of peace and beauty.\n\nWord Count: 96 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'mausoleum', 'white marble', 'symmetry', 'lush', 'emperor', 'symbol', 'eternal love', 'intricate carvings', 'breathtaking', 'masterpiece', 'Mughal architecture'. \n\n>Band 6: 'Mausoleum', 'intricate'.\n\nNot Band 8: 'Wife' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'made of white marble', 'built by an emperor', 'Seeing it at sunrise'. \n\n>Band 6: Participles and gerunds used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_487",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I organized a fundraising event for a local charity. It required meticulous planning and coordination. I contacted sponsors and vendors to support the event. I managed the budget carefully to avoid overspending. There were last-minute hiccups that I had to deal with. I had to solve problems on the fly and stay calm. The event was a huge success, raising a lot of money. It was a fulfilling experience to help the community. I learned a lot about event management and leadership.",
        "word_count": 90,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'fundraising', 'meticulous', 'planning', 'coordination', 'sponsors', 'vendors', 'budget', 'overspending', 'hiccups', 'solve problems', 'on the fly', 'success', 'fulfilling', 'community'. Band 7 level.",
             "grammar: 'required meticulous planning', 'vendors to support', 'hiccups that I had'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'fundraising', 'meticulous', 'sponsors', 'vendors', 'budget', 'hiccups', 'solve problems', 'on the fly', 'success', 'charity', 'fulfilling'. >Band 6: 'Meticulous', 'hiccups'. Not Band 8: 'Money' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'required meticulous planning', 'vendors to support', 'hiccups that I had'. >Band 6: Infinitives and relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I organized a fundraising event for a local charity. It required meticulous planning and coordination. I contacted sponsors and vendors to support the event. I managed the budget carefully to avoid overspending. There were last-minute hiccups that I had to deal with. I had to solve problems on the fly and stay calm. The event was a huge success, raising a lot of money. It was a fulfilling experience to help the community. I learned a lot about event management and leadership.\n\nWord Count: 90 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'fundraising', 'meticulous', 'sponsors', 'vendors', 'budget', 'hiccups', 'solve problems', 'on the fly', 'success', 'charity', 'fulfilling'. \n\n>Band 6: 'Meticulous', 'hiccups'.\n\nNot Band 8: 'Money' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'required meticulous planning', 'vendors to support', 'hiccups that I had'. \n\n>Band 6: Infinitives and relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
