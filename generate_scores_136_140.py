import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 13601,
        "sample_id": "aF1dgp2J4v4_q05",
        "video_id": "aF1dgp2J4v4",
        "part": 1,
        "question": "How you worked or studied in a group?",
        "transcript": "Definitely yes, because even like being a student, it always requires me to study in a group because there are always some teamwork like projects where being a good partner is really a necessity.",
        "word_count": 35,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["study in a group", "teamwork like projects", "necessity"],
            "grammar_structures_used": ["complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": [],
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
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Structure is good but 'it always requires me' is slightly unnatural (I am always required / it requires students).",
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
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Necessity'. Justification: Band 8.",
        "grammar_reason": "Observation: Correct complex sentence. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 13602,
        "sample_id": "aF1dgp2J4v4_q06",
        "video_id": "aF1dgp2J4v4",
        "part": 1,
        "question": "What does it take to be a good partner?",
        "transcript": "I think that there are two most important qualities. First of all, it is being able to listen to your partner to understand what their, what, what their aims are, what they want from the project to be. And also it is being able to express yourself normally, concisely. So, so your partner would understand you.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure_error"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["concisely", "express yourself", "aims"],
            "grammar_structures_used": ["gerund_subject", "noun_clause"]
        },
        "micro_flaws": {
            "grammar": ["what_they_want_from_the_project_to_be_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "highly_accurate",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "high",
            "flexibility": "high",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Minor error: 'what they want from the project to be' (what they want the project to be / what they want from the project).",
                "why_not_7": "Complex gerund structures used well."
            },
            "vocabulary": {
                "why_not_9": "'Concisely' is excellent Band 9 vocab.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Majority of sentences error-free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Precise and flexible."
        },
        "vocab_reason": "Observation: 'Concisely'. Impact: Precise. Justification: Band 9.",
        "grammar_reason": "Observation: Gerund phrases. Minor slip. Justification: Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 13603,
        "sample_id": "aF1dgp2J4v4_q08",
        "video_id": "aF1dgp2J4v4",
        "part": 1,
        "question": "What do you think are the disadvantages of being in a group?",
        "transcript": "I think that the primary disadvantage of it would be the fact that sometimes you are not given the chance to kind of create the project the way how you want it to be. Sometimes like people are more dominant and their ideas are more appealing to others and you might not be listened to by others.",
        "word_count": 57,
        "analysis_metadata": {
            "grammar_error_patterns": ["redundancy"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["primary disadvantage", "dominant", "appealing"],
            "grammar_structures_used": ["passive_voice", "noun_clause"]
        },
        "micro_flaws": {
            "grammar": ["the_way_how_redundancy"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "highly_accurate",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "high",
            "flexibility": "high",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Minor redundancy 'the way how you want it to be' (the way you want it / how you want it).",
                "why_not_7": "Passive 'might not be listened to' is strong."
            },
            "vocabulary": {
                "why_not_9": "'Dominant', 'primary disadvantage'. Academic.",
                "why_not_7": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free sentences.",
            "vocabulary_band": 9,
            "vocabulary_text": "Precise."
        },
        "vocab_reason": "Observation: 'Dominant', 'primary disadvantage'. Impact: Academic. Justification: Band 9.",
        "grammar_reason": "Observation: Passive modal. Justification: Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 13604,
        "sample_id": "aF1dgp2J4v4_q09",
        "video_id": "aF1dgp2J4v4",
        "part": 1,
        "question": "So how can you make them listen?",
        "transcript": "Probably the best way would be first of all, listen to yourself. Like you have to be a role model and show them an example of yourself that you are willing to listen to others. And probably in return, they will do the same thing to you.",
        "word_count": 47,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["role model", "willing to listen", "in return"],
            "grammar_structures_used": ["modal_verb", "complex_sentence_purpose"]
        },
        "micro_flaws": {
            "grammar": [],
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
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good control.",
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
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Role model', 'in return'. Justification: Band 8.",
        "grammar_reason": "Observation: Error free. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 13605,
        "sample_id": "aF1dgp2J4v4_q10",
        "video_id": "aF1dgp2J4v4",
        "part": 3,
        "question": "What skills do they develop?",
        "transcript": "I think that, that it is really important to listen to others and that other people's Opinion matters a lot and it is really important to be supportive whenever you work with someone because otherwise it is, it would be really chaotic. It would not be a team. It would be just a chaos. Thank you. What advice would you give someone who wants to study effectively in a group Apart from listening to their partner right Yeah and just stick to it So I think that maybe I don know like probably it just the best advice that I could have given to anyone But apart from that, it would be like not behaving in a way that you, I mean not coming across as self-important and thinking that you are the only one here. And everything depends on you because it is really important that to acknowledge the fact that you are not alone and you should like, bear in mind that other people also exist. So, okay. Very nice.",
        "word_count": 169,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_error"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["chaotic", "stick to it", "come across as", "self-important", "acknowledge the fact", "bear in mind"],
            "grammar_structures_used": ["complex_sentence_condition", "noun_clause", "modal_perfect"]
        },
        "micro_flaws": {
            "grammar": ["article_error_chaos"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "highly_accurate",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "high",
            "flexibility": "high",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "extended",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'It would be just a chaos' (just chaos - uncountable). 'Best advice I could have given' (modal perfect used well).",
                "why_not_7": "High complexity and control."
            },
            "vocabulary": {
                "why_not_9": "'Bear in mind', 'come across as self-important'. Extremely natural and precise idiomatic usage.",
                "why_not_8": "Better than skilful."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Majority of sentences error-free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Precise and flexible."
        },
        "vocab_reason": "Observation: 'Bear in mind', 'self-important'. Impact: Highly natural. Justification: Band 9.",
        "grammar_reason": "Observation: Modal perfect. Article error. Justification: Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 13606,
        "sample_id": "aF1dgp2J4v4_q13",
        "video_id": "aF1dgp2J4v4",
        "part": 3,
        "question": "What kinds of movies are popular in Uzbekistan?",
        "transcript": "To be perfectly honest with you, I have no idea because I do not like watch any movies in Uzbek or I do not even have friends that are interested in Uzbek movies. But I can only assume that it is something like related to the modern world, maybe some relationship, family drama, something like this. it is really varies, but I believe that it is familiar with the rest of the world.",
        "word_count": 73,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_pattern_error", "verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["perfectly honest", "assume that", "familiar with"],
            "grammar_structures_used": ["complex_sentence_contrast"]
        },
        "micro_flaws": {
            "grammar": ["verb_pattern_like_watch", "agreement_it_varies"],
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
                "why_not_8": "'I do not like watch' (watching/to watch). 'It is really varies' (It really varies).",
                "why_not_6": "Complex sentences used correctly."
            },
            "vocabulary": {
                "why_not_8": "'To be perfectly honest' is a great opener.",
                "why_not_6": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Perfectly honest'. Justification: Band 7.",
        "grammar_reason": "Observation: 'Like watch'. Justification: Band 6.",
        "vocabulary": 7,
        "grammar": 6
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
