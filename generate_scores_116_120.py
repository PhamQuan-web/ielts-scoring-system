import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 11601,
        "sample_id": "OicvdCp5wrM_q09",
        "video_id": "OicvdCp5wrM",
        "part": 1,
        "question": "How many languages do you speak?",
        "transcript": "Oh, so basically I am born in Myanmar, but my grandparents are from China. So my native language will be Burmese and Chinese. it is like lots of people they born in, their parents move here and work here for a long time. And then they were born here, but their nationality, their culture, their background, their passport will still remain with their original countries.",
        "word_count": 63,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_error", "verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["native language", "nationality", "background", "remain with"],
            "grammar_structures_used": ["complex_sentence_explanation"]
        },
        "micro_flaws": {
            "grammar": ["incorrect_be_born", "missing_verb_were"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors: 'I am born' (I was born). 'People they born in' (who were born in).",
                "why_not_5": "Complex structure 'their nationality... will still remain' is controlled."
            },
            "vocabulary": {
                "why_not_8": "Standard vocabulary.",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms. Errors occur.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Nationality', 'remain with'. Justification: Band 7.",
        "grammar_reason": "Observation: 'I am born'. Justification: Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 11602,
        "sample_id": "OicvdCp5wrM_q10",
        "video_id": "OicvdCp5wrM",
        "part": 1,
        "question": "How useful will the English language be to you in the future?",
        "transcript": "In the future, from in a school till high school, I have to study English as one subject. And then after that I have to take some courses to understand. that is it. I only use most of my English in Dubai. And then my conversation English I improve a lot in Dubai. But back in the home country people from my country they are not that good in English.",
        "word_count": 70,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice", "preposition_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["study English", "take some courses", "conversation English"],
            "grammar_structures_used": ["time_clause", "contrast"]
        },
        "micro_flaws": {
            "grammar": ["tense_future_context_past_form"],
            "vocabulary": ["imprecise_collocation"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'Conversation English I improve a lot' (My conversational English improved). Tense confusion.",
                "why_not_5": "Meaning is clear."
            },
            "vocabulary": {
                "why_not_7": "Limited range. 'Conversation English' is slightly unnatural.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Conversation English'. Justification: Band 6.",
        "grammar_reason": "Observation: Tense confusion. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 11603,
        "sample_id": "OicvdCp5wrM_q13",
        "video_id": "OicvdCp5wrM",
        "part": 1,
        "question": "Did you learn to swim when you were a child?",
        "transcript": "No, I am afraid, really afraid. In my country we have a river, but it is kind of dangerous. So it is kind of not that hygiene enough. So I learned swimming in Dubai. We have pools, even in the building, they have a pool, lots of pools. So I learned by myself though.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["hygiene", "learned by myself", "dangerous"],
            "grammar_structures_used": ["reason_clause", "contrast"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["wrong_word_form"]
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'Not that hygiene enough' (hygienic). 'Learned swimming' (learned to swim).",
                "why_not_6": "Good flow."
            },
            "vocabulary": {
                "why_not_8": "'Hygiene' used as adjective.",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Hygiene'. Error in form but high level word. Justification: Band 7.",
        "grammar_reason": "Observation: Word form error. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 11604,
        "sample_id": "OicvdCp5wrM_q15",
        "video_id": "OicvdCp5wrM",
        "part": 3,
        "question": "Why are there so many stories in the news about famous people?",
        "transcript": "People want to be famous, I would say. Majority people are ordinary and then they want to be outstanding. They want to be working better than other people. They want to feel better. They want to feel nice. that is why I think they want to be famous.",
        "word_count": 46,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_missing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["outstanding", "ordinary"],
            "grammar_structures_used": ["complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": ["missing_preposition_of"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'Majority people' (Majority of people).",
                "why_not_6": "Correct."
            },
            "vocabulary": {
                "why_not_8": "'Outstanding' vs 'ordinary' contrast is good.",
                "why_not_6": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Outstanding'. Impact: Precise. Justification: Band 7.",
        "grammar_reason": "Observation: 'Majority people'. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 11605,
        "sample_id": "OicvdCp5wrM_q16",
        "video_id": "OicvdCp5wrM",
        "part": 3,
        "question": "Do you agree or disagree that many young people want to be famous today?",
        "transcript": "Very disagree, very agree because as you can see, influencer, internet, people you can have a phone, you can record and then can be your own influencer without any teamwork helping you.",
        "word_count": 32,
        "analysis_metadata": {
            "grammar_error_patterns": ["collocation_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["influencer", "teamwork"],
            "grammar_structures_used": ["reason_clause"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["wrong_intensifier"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'Very disagree' (strongly disagree).",
                "why_not_6": "Sentence structure is fragmented."
            },
            "vocabulary": {
                "why_not_8": "'Teamwork' is okay but 'support team' might be better.",
                "why_not_6": "Topic words."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Very disagree' error. Justification: Band 6.",
        "grammar_reason": "Observation: Fragmented. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 11606,
        "sample_id": "OicvdCp5wrM_q17",
        "video_id": "OicvdCp5wrM",
        "part": 3,
        "question": "Do you think that it is easy for famous people to become rich?",
        "transcript": "Not really. Fame and rich, sometimes it comes along, but not everyone can make money, especially on the internet right now. You can make famous by individual yourself and then you cannot earn the money from that.",
        "word_count": 36,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["earn the money", "individual"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["adjective_as_noun"],
            "vocabulary": ["wrong_collocation_make_famous"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'Fame and rich' (riches/wealth). 'Make famous' (become famous).",
                "why_not_5": "Meaning clear."
            },
            "vocabulary": {
                "why_not_7": "Errors in word choice.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Make famous'. Justification: Band 6.",
        "grammar_reason": "Observation: 'Rich' as noun. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
