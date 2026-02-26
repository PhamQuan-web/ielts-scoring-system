import json

OUTPUT_FILE = 'batch05_fix_part1.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v7_g6_412",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I am fascinated by the bamboo plant, which is incredibly versatile. It grows rapidly and can survive in many different climates. In my country, it is used for construction, food, and decoration. Bamboo forests are serene and peaceful places to visit. The stalks are hollow but resilient, bending in the wind without breaking. It symbolizes flexibility and strength in Asian culture. I have some bamboo in my garden, and it requires minimal maintenance. It is an eco-friendly resource because it grows back so quickly. I think it is amazing how such a simple plant can be so useful. It adds a touch of elegance to any landscape.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'plant, which is', 'bending in the wind' (participle). Good control."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'fascinated', 'versatile', 'rapidly', 'serene', 'stalks', 'hollow', 'resilient', 'symbolizes', 'minimal maintenance', 'eco-friendly'. >Band 6: 'Resilient', 'versatile'. Not Band 8: 'Asian culture' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'plant, which is', 'bending in the wind'. >Band 5: Mix of structures. Not Band 7: Some sentences are simple.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: ...",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'fascinated', 'versatile', 'rapidly', 'serene', 'stalks', 'hollow', 'resilient', 'symbolizes', 'minimal maintenance', 'eco-friendly'. \n\n>Band 6: 'Resilient', 'versatile'.\n\nNot Band 8: 'Asian culture' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'plant, which is', 'bending in the wind'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Some sentences are simple.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_413",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "I want to talk about my best friend, Sarah, who has been a pillar of support in my life. We met in high school and instantly clicked. She is an incredibly generous and kind-hearted person. I admire her ability to stay positive even in difficult situations. We have shared many adventures together, traveling to different countries. One memorable trip was when we went to Japan. We got lost in Tokyo but managed to find our way back, laughing all the while. She always gives me honest advice when I need it. I value her friendship more than words can say. She is like a sister to me, and I know I can always count on her.",
        "word_count": 116,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'friend, Sarah, who', 'when we went'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'pillar of support', 'instantly clicked', 'generous', 'kind-hearted', 'adventures', 'memorable', 'honest advice', 'value'. >Band 6: 'Clicked', 'pillar'. Not Band 8: 'Best friend' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'Sarah, who has', 'trip was when'. >Band 5: Mix of structures. Not Band 7: Some errors or simpler forms.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score...",
        "input": "Part: 2...",
        "output": "## Vocabulary... Band 7... ## Grammar... Band 6"
    },
    {
        "sample_id": "syn_p2_v7_g6_414",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a decision.",
        "transcript_cleaned": "I had to make a tough decision about my career path last year. I was offered a job in another city, which meant leaving my family behind. I weighed the pros and cons carefully before deciding. The new job offered better pay and opportunities for growth. However, I was worried about feeling lonely in a new place. After consulting with my parents, I decided to take the leap of faith. It was scary at first, but I adapted quickly. I met new people and learned new skills. I believe it was the right choice for my future. It taught me to be independent and resilient.",
        "word_count": 105,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'city, which meant', 'weighed the pros'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'career path', 'weighed the pros and cons', 'opportunities', 'growth', 'consulting', 'leap of faith', 'adapted', 'independent', 'resilient'. >Band 6: 'Resilient', 'leap of faith'. Not Band 8: 'Job' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'city, which meant', 'After consulting with'. >Band 5: Mix of structures. Not Band 7: Repetitive sentence starts.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score...",
        "input": "Part: 2...",
        "output": "## Vocabulary... Band 7... ## Grammar... Band 6"
    },
    # ... I will write the rest up to 430 in the file ...
]

# Helper to generate the rest with templates but ensuring I write specific content
# Actually, I cannot use the loop I used before because I need specific content.
# I will write them out one by one in the script.
# Due to length constraints in this turn, I will just output these 3 for now and append the rest in subsequent calls.
# I will output 3 samples per file write to be safe? No, that's too slow.
# I'll create the file with 3 samples for now to test.

with open(OUTPUT_FILE, 'w') as f:
    for sample in samples:
        # Populate input field fully
        sample["input"] = f"Part: 2\nQuestion: {sample['question']}\n\nTranscript: {sample['transcript_cleaned']}\n\nWord Count: {sample['word_count']} words\nResponse Type: long_turn"
        # Populate output field fully if not already
        if "##" not in sample["output"]:
             sample["output"] = f"## Vocabulary (Lexical Resource): Band {sample['vocabulary']}\n\n**Reasoning:** {sample['vocab_reason']}\n\n**Idiom present:** {'Yes' if sample['idiom_present'] else 'No'}\n**Risk level:** {sample['risk_level']}\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band {sample['grammar']}\n\n**Reasoning:** {sample['grammar_reason']}\n\n**Micro flaws identified:**\n- {sample['micro_flaws'][0]}"

        json.dump(sample, f)
        f.write('\n')
