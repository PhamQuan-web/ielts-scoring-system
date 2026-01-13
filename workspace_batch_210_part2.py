import json

output_file = 'jules_scored_output_201-250.jsonl'

# --- REMAINING SAMPLES FOR BATCH 210 ---
remaining_samples = [
    # Video: n0Ho0iOmGG8 (Band 7.0)
    {
        "id": 0, "sample_id": "n0Ho0iOmGG8_q03",
        "video_id": "n0Ho0iOmGG8",
        "part": 2,
        "question": "Tourist Attraction (Mushk Puri Top)?",
        "transcript": "Now have to speak on this topic for 1 to two minutes well this is such an interesting topic the tourist attraction I would like to talk about one of my visits to the mushk Puri top with my University's fellows there was a time when I just passed my semester and I I I I have been to a lot of trips during my school and college trips but there was only one dat trip and there was a time my friends were pushing me to go on a trip because it was a long trip of 3 days and I was not sure that my mother will allow me to go to that trip and my result came and I got a distinction in sociology so I called my mother and she told me that oh oh yeah why not you can go so I was on the top of the mountains at that time so we decided to go to the mush Puri top and that is the place that I still admire and I would say I would recommend every tourist or visitor to go there because when I went there there was a time of winters I went there in Winters so there was snow everywhere even the guest house where we were staying was the door of that guest house was filled with a lot of snow and there was and the scenery at that time well we reached there at night and then we did a lot of rest there because it was hell cold over there in the morning we had our breakfast and we moved outside to.",
        "word_count": 266,
        "analysis_metadata": {
            "grammar_error_patterns": ["coherence", "repetition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["distinction in sociology", "admire", "hell cold"],
            "grammar_structures_used": ["complex_sentences", "past_tense"]
        },
        "micro_flaws": {
            "grammar": ["fluency_breakdown"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'hell cold' (informal, but effective). 'one dat trip' (day?). 'time of winters' (in winter). 'filled with a lot of snow' (covered?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Repetition and fluency breaks.",
                "why_not_6": "Sustained narrative."
            },
            "vocabulary": {
                "why_not_8": "'time of winters' (imprecise).",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar and punctuation but they rarely reduce communication.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary to allow some flexibility and precision."
        },
        "vocab_reason": "Good range but some imprecision. Band 7.",
        "grammar_reason": "Frequent errors but understandable. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "n0Ho0iOmGG8_q04",
        "video_id": "n0Ho0iOmGG8",
        "part": 2,
        "question": "Hiking/Markets?",
        "transcript": "Do the hiking and that was the very adventurous part of that thing because there was a lot of snow everywhere and we were afraid of getting sleep there but we did it very well and then after that moving during the hiking moving down to the street there were a lot of shops and markets where you can buy local things of that place so that is the thing I would recommend every tourist and visitors to go there so that the view of the mountains The Greenery that giv Cals to your eyes all right thank you so much.",
        "word_count": 96,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["adventurous part", "local things"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'getting sleep there' (slip there?). 'gives Cals to your eyes' (calm? calls?). 'local things' (souvenirs/produce)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "moderate",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Errors present.",
                "why_not_6": "Good range."
            },
            "vocabulary": {
                "why_not_8": "Word choice errors ('sleep', 'Cals').",
                "why_not_6": "Sufficient."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors in word choice affect clarity ('sleep', 'Cals'). Band 6.",
        "grammar_reason": "Sentences are complex but contain errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    }
]

# Write to file (checking for duplicates)
try:
    existing_ids = set()
    try:
        with open(output_file, 'r') as f:
            for line in f:
                if line.strip():
                    item = json.loads(line)
                    existing_ids.add(item['sample_id'])
    except FileNotFoundError:
        pass

    with open(output_file, 'a') as f:
        count = 0
        for sample in remaining_samples:
            if sample['vocabulary'] == 0:
                continue
            if sample['sample_id'] not in existing_ids:
                f.write(json.dumps(sample) + '\n')
                count += 1

    print(f"Append complete. Added {count} new samples.")

except Exception as e:
    print(f"Error writing to file: {e}")
