import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 10801,
        "sample_id": "iIN3QQnVgXY_q02",
        "video_id": "iIN3QQnVgXY",
        "part": 1,
        "question": "So are you working or studying right now?",
        "transcript": "I am working as a freelancer. I was a teacher. I taught English to kindergarten students and elementary students, but now I am a freelancer.",
        "word_count": 25,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["working as a freelancer", "kindergarten students", "elementary students"],
            "grammar_structures_used": ["past_simple", "present_simple", "contrast"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "low",
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Simple sentences, although error-free.",
                "why_not_7": "Accuracy is perfect."
            },
            "vocabulary": {
                "why_not_9": "Standard job vocabulary.",
                "why_not_7": "Correct collocations."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Freelancer', 'kindergarten'. Impact: Accurate. Justification: Band 7.",
        "grammar_reason": "Observation: Error free. Justification: Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 10802,
        "sample_id": "iIN3QQnVgXY_q03",
        "video_id": "iIN3QQnVgXY",
        "part": 1,
        "question": "Did you like your job as a teacher?",
        "transcript": "Yes, I loved it. I love, kindergarten students. they are just so cute. I love their random behaviors. Just everywhere.",
        "word_count": 21,
        "analysis_metadata": {
            "grammar_error_patterns": ["fragmented_sentence"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["random behaviors", "so cute"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["fragment"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "simple",
            "accuracy_level": "high",
            "flexibility": "low",
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Too simple/short.",
                "why_not_5": "Correct."
            },
            "vocabulary": {
                "why_not_8": "'Random behaviors' is a nice collocation.",
                "why_not_6": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common items ('random')."
        },
        "vocab_reason": "Observation: 'Random behaviors'. Impact: Natural. Justification: Band 7.",
        "grammar_reason": "Observation: Simple sentences. Justification: Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 10803,
        "sample_id": "iIN3QQnVgXY_q04",
        "video_id": "iIN3QQnVgXY",
        "part": 1,
        "question": "And what do you enjoy doing in your free time?",
        "transcript": "I usually go for a walk. I really love walking. I walk for like three hours. I have a puppy. So I take him outside and just walk everywhere.",
        "word_count": 30,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["go for a walk", "take him outside"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "simple",
            "accuracy_level": "high",
            "flexibility": "low",
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Repetitive sentence openings 'I usually', 'I really', 'I walk'.",
                "why_not_6": "Error free."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Go for a walk'. Impact: Natural. Justification: Band 7.",
        "grammar_reason": "Observation: Simple but correct. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 10804,
        "sample_id": "iIN3QQnVgXY_q07",
        "video_id": "iIN3QQnVgXY",
        "part": 1,
        "question": "Yeah, where, where did you grow up?",
        "transcript": "Oh, I lived in Incheon, but I went to Canada for like six years. So I lived there and then I came back and then I went to America and then I lived there for like four years and then I came back. So, my hometown is Incheon, but I was everywhere. Yeah, but still home.",
        "word_count": 57,
        "analysis_metadata": {
            "grammar_error_patterns": ["overuse_and_then"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["hometown", "came back"],
            "grammar_structures_used": ["compound_sentence_sequence"]
        },
        "micro_flaws": {
            "grammar": ["repetitive_connectors"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "high",
            "flexibility": "low",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "high",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Heavy reliance on 'and then... and then...'.",
                "why_not_6": "Grammatically correct past tense usage."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms. Repetitive connectors.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic words. Justification: Band 6.",
        "grammar_reason": "Observation: Repetitive 'and then'. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10805,
        "sample_id": "iIN3QQnVgXY_q08",
        "video_id": "iIN3QQnVgXY",
        "part": 1,
        "question": "And thinking of Incheon and your hometown, what do you like about it?",
        "transcript": "I love people. So I think my hometown is near like department stores and every, and there is a lot of people there. So I think being convenient to things that I can go and go and shop.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement_error", "awkward_phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["department stores", "convenient"],
            "grammar_structures_used": ["reason_clause"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error_there_is"],
            "vocabulary": ["imprecise_phrasing"]
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
            "development_depth": "partial"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'There is a lot of people' (agreement). 'Being convenient to things that I can go and go and shop' is grammatically tangled.",
                "why_not_5": "Meaning is clear."
            },
            "vocabulary": {
                "why_not_7": "Limited range.",
                "why_not_5": "Correct words for topic."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur frequently.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Convenient'. Justification: Band 6.",
        "grammar_reason": "Observation: 'There is a lot of people'. Tangled end. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10806,
        "sample_id": "iIN3QQnVgXY_q10",
        "video_id": "iIN3QQnVgXY",
        "part": 1,
        "question": "And when you are shopping, Do you compare prices before you buy things?",
        "transcript": "If that product is really pretty, I just buy it. But if like it is over my amount, then I look at the price. And is it difficult for you to make choices when you shop Yes I can choose Everything looks so pretty for me I usually ask my friends or my mom Take a picture and then send them and then ask them if it pretty and then why Because if I can choose I just stay there for a lot of time So yeah I ask them usually",
        "word_count": 91,
        "analysis_metadata": {
            "grammar_error_patterns": ["missing_verbs", "informal_structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["compare prices", "make choices"],
            "grammar_structures_used": ["conditional_zero", "sequence"]
        },
        "micro_flaws": {
            "grammar": ["run_on_sentences"],
            "vocabulary": ["imprecise_word_choice"]
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
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Run-on sentences and missing subjects/verbs in the second half. 'If like it is over my amount' is unnatural.",
                "why_not_5": "Conditionals are used correctly."
            },
            "vocabulary": {
                "why_not_7": "'Over my amount' (budget). 'Stay there for a lot of time' (long time).",
                "why_not_5": "Clear."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex. Errors frequent.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Over my amount' error. Justification: Band 6.",
        "grammar_reason": "Observation: Conditionals used but with errors. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10807,
        "sample_id": "iIN3QQnVgXY_q11",
        "video_id": "iIN3QQnVgXY",
        "part": 1,
        "question": "Do you think expensive products are always better than cheaper ones?",
        "transcript": "I, it is in the middle I think because expensive product, their design is similar I think but then what they use for the material it is different I think if it is expensive. But the design is similar so if I am just wearing for a season and then I am throwing it away I just buy the cheaper one.",
        "word_count": 61,
        "analysis_metadata": {
            "grammar_error_patterns": ["topic_comment_structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["material", "throwing it away"],
            "grammar_structures_used": ["complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": ["unnatural_word_order"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "low",
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
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'Expensive product, their design is similar' (Topic-comment structure common in Asian learners, not standard English).",
                "why_not_5": "Complex ideas expressed clearly."
            },
            "vocabulary": {
                "why_not_7": "Basic but correct.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex. Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Throwing it away', 'material'. Justification: Band 6.",
        "grammar_reason": "Observation: Structural issues but meaning clear. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
