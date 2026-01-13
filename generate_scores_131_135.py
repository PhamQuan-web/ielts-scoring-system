import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 13501,
        "sample_id": "r35hw5FbqMw_q02",
        "video_id": "r35hw5FbqMw",
        "part": 1,
        "question": "Do you often talk with your friends about the news?",
        "transcript": "Not really. Because I think I do not like watching news because I think there is a lot of bad news in Korea. So that is why I do not want to watch.",
        "word_count": 35,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition_because"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["bad news"],
            "grammar_structures_used": ["complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": ["repetitive_structure"],
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
            "redundancy": "medium",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Repetitive 'because... because'.",
                "why_not_6": "Error free."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Frequent error-free sentences.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 6.",
        "grammar_reason": "Observation: Correct. Justification: Band 7.",
        "vocabulary": 6,
        "grammar": 7
    },
    {
        "id": 13502,
        "sample_id": "r35hw5FbqMw_q03",
        "video_id": "r35hw5FbqMw",
        "part": 1,
        "question": "And how do your friends get the news?",
        "transcript": "Oh, I think from phone, from the phone. Yeah. And because we do not, my friends do not usually have TV because they live alone. So we just watch news on the phone.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["live alone", "watch news"],
            "grammar_structures_used": ["complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": ["missing_article_phone"],
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
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'From phone' (from their phones).",
                "why_not_6": "Complex sentences."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 6.",
        "grammar_reason": "Observation: Article error. Justification: Band 7.",
        "vocabulary": 6,
        "grammar": 7
    },
    {
        "id": 13503,
        "sample_id": "r35hw5FbqMw_q07",
        "video_id": "r35hw5FbqMw",
        "part": 1,
        "question": "Like, how do you learn a foreign language?",
        "transcript": "Oh, I think we need more opportunities to talk with foreign teachers. Yes, because Korean students cannot speak English at all, I think. Like, they can understand everything, but they do not like to speak. So, I think we should learn from foreign teachers more.",
        "word_count": 45,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["foreign teachers", "opportunities to talk"],
            "grammar_structures_used": ["modal_verb", "complex_sentence_contrast"]
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
            "flexibility": "moderate",
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good flow.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Foreign teachers'. Justification: Band 7.",
        "grammar_reason": "Observation: Correct. Justification: Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 13504,
        "sample_id": "r35hw5FbqMw_q08",
        "video_id": "r35hw5FbqMw",
        "part": 1,
        "question": "What languages would you like to learn in the future?",
        "transcript": "Oh, I love to learn English. So, yes, my plan is to go to live in another country because I love English. So, and I want to learn Spanish too.",
        "word_count": 30,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["plan is to", "learn Spanish"],
            "grammar_structures_used": ["infinitive_purpose"]
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
                "why_not_8": "Simple sentences.",
                "why_not_6": "Error free."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error free.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 6.",
        "grammar_reason": "Observation: Correct. Justification: Band 7.",
        "vocabulary": 6,
        "grammar": 7
    },
    {
        "id": 13505,
        "sample_id": "r35hw5FbqMw_q14",
        "video_id": "r35hw5FbqMw",
        "part": 2,
        "question": "Describe something you do to keep fit and healthy.",
        "transcript": "something I, to do to keep it healthy is soccer. Because I play soccer every Sunday with my friends. And, I think to keep fit and healthy is important. The reason is, the research shows that we will be able to live in almost 100 years old. So, that is why we have to keep healthy and I think people have to make their hobbies to keep healthy. So, I think I can, I made it with my friends. I play soccer with my friends. I made my own team, because my friends love to play, but they did not have any place to play soccer. So that is why I made it and, we all love to play soccer because whenever we play, we do not have to think anything about that make, us, you know, how can I say? they, we do not have to think about that, like about bad thing that we, that made us really sad or something. So, we all chose soccer.",
        "word_count": 169,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_pattern", "preposition_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["keep fit", "research shows", "made my own team"],
            "grammar_structures_used": ["complex_sentence_reason", "relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["infinitive_structure_error"],
            "vocabulary": ["imprecise_expression"]
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
            "length_appropriateness": "extended",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'Something I to do to keep it healthy' (Something I do to keep healthy). 'Live in almost 100 years old' (live to almost 100).",
                "why_not_5": "Complex sentences used correctly."
            },
            "vocabulary": {
                "why_not_7": "'Keep it healthy' (keep healthy). 'Make their hobbies' (take up hobbies).",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Keep fit'. Justification: Band 6.",
        "grammar_reason": "Observation: Structural errors. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 13506,
        "sample_id": "r35hw5FbqMw_q17",
        "video_id": "r35hw5FbqMw",
        "part": 3,
        "question": "Do you think it is good for governments to use celebrities or famous people to build health awareness?",
        "transcript": "Yes. Because a lot of people love celebrities. So, like, if someone likes a celebrity a lot, like, if the person, like, plays something, and they could play, you know, like, they play it like her or him.",
        "word_count": 37,
        "analysis_metadata": {
            "grammar_error_patterns": ["overuse_like"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["likes a celebrity"],
            "grammar_structures_used": ["conditional_first"]
        },
        "micro_flaws": {
            "grammar": ["informal_fillers"],
            "vocabulary": ["imprecise_phrasing"]
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
            "redundancy": "high",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Heavily fragmented by 'like'. Logic is hard to follow.",
                "why_not_4": "Basic conditional is attempted."
            },
            "vocabulary": {
                "why_not_6": "Very basic.",
                "why_not_4": "Relevant."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Frequent errors.",
            "vocabulary_band": 5,
            "vocabulary_text": "Limited."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 5.",
        "grammar_reason": "Observation: Fragmented. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 13507,
        "sample_id": "r35hw5FbqMw_q21",
        "video_id": "r35hw5FbqMw",
        "part": 3,
        "question": "Like what is the difference you would say?",
        "transcript": "Oh kids have to do exercise like running or jumping rope something like that because of their growth But old people should make their muscles because of their good health because my grandparents, whenever they got older, they could not walk and they, they were likely to, you know, fall down because they do not have muscles on the legs. So that is why we, they have to make more muscles.",
        "word_count": 70,
        "analysis_metadata": {
            "grammar_error_patterns": ["collocation_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["jumping rope", "fall down"],
            "grammar_structures_used": ["reason_clause", "modal_verb"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["wrong_collocation_make_muscles"]
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
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'Make their muscles' (build muscle). 'Muscles on the legs' (leg muscles).",
                "why_not_5": "Complex sentences."
            },
            "vocabulary": {
                "why_not_7": "Collocation errors.",
                "why_not_5": "Good topic words."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Jumping rope'. 'Make muscles' error. Justification: Band 6.",
        "grammar_reason": "Observation: Good structure. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
