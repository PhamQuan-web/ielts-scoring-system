import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 12601,
        "sample_id": "-aawIOrM2GU_q10",
        "video_id": "-aawIOrM2GU",
        "part": 3,
        "question": "And what do people usually complain about?",
        "transcript": "Well, in my view, I, I believe that people usually complain about the quality of the products or services they receive because, most of customers, you know, prioritize the quality of products and if they receive a bad, bad, a bad product, they feel extremely, you know, disappointed and they want to, they want to return it back. They want to, they want to get it back. And and it is also, you know, I think all the, all the shop, all the manager should be, double check all the quality before it launch.",
        "word_count": 87,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_tense_error", "redundancy"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["prioritize the quality", "extremely disappointed", "return it back"],
            "grammar_structures_used": ["complex_sentence_reason", "modal_verb"]
        },
        "micro_flaws": {
            "grammar": ["passive_voice_missing_be"],
            "vocabulary": ["redundant_phrasing"]
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
            "length_appropriateness": "adequate",
            "redundancy": "high",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Error: 'before it launch' (before it is launched/before launching). 'Should be double check' (should double check).",
                "why_not_5": "Complex sentences used correctly ('because most of customers... if they receive...')."
            },
            "vocabulary": {
                "why_not_7": "'Return it back' is redundant (return it). 'Get it back' is vague. 'Prioritize the quality' is good.",
                "why_not_5": "Topic words used well."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex. Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate range."
        },
        "vocab_reason": "Observation: 'Prioritize'. Redundant 'return back'. Justification: Band 6.",
        "grammar_reason": "Observation: Passive/modal errors. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 12602,
        "sample_id": "-aawIOrM2GU_q11",
        "video_id": "-aawIOrM2GU",
        "part": 3,
        "question": "How would you react if you received a poor service at a restaurant?",
        "transcript": "if you ask me, I would say that if I, if I was in that situation, I would, carefully, talk with the waiter and, specifically explain the, explain the situation and I want to, I want to hear reasonable solution If the staff cannot explain it to me reasonably I will want I want to talk with the manager Who are more likely to make complaints?",
        "word_count": 59,
        "analysis_metadata": {
            "grammar_error_patterns": ["conditional_consistency"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["reasonable solution", "specifically explain", "talk with the manager"],
            "grammar_structures_used": ["second_conditional", "first_conditional"]
        },
        "micro_flaws": {
            "grammar": ["conditional_tense_shift"],
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
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Starts with 2nd conditional ('If I was... I would') but shifts to 'I want to hear' (present) and then 'If the staff cannot... I will want' (1st conditional). Inconsistent.",
                "why_not_5": "Structures are formed correctly individually."
            },
            "vocabulary": {
                "why_not_7": "Standard vocabulary.",
                "why_not_5": "Clear and accurate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Reasonable solution'. Justification: Band 6.",
        "grammar_reason": "Observation: Tense consistency issues. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 12603,
        "sample_id": "-aawIOrM2GU_q12",
        "video_id": "-aawIOrM2GU",
        "part": 3,
        "question": "Older people or younger people?",
        "transcript": "let me have a think. well, when it comes to making complaints, I believe that, younger people have a tendency to make complaints than older people because, they, are inclined to, to be aggressive and, to be impatient. So, by contrast, the older people, they are more, they are more, they are more experienced. And, I, I, I think they definitely, experience more, a lot of situations like that. So they, they will, you know, they will, they will find it, easy. And they, will, take, take another solution in this case.",
        "word_count": 92,
        "analysis_metadata": {
            "grammar_error_patterns": ["comparison_structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["tendency to", "inclined to", "impatient", "experienced"],
            "grammar_structures_used": ["comparison", "complex_sentence_contrast"]
        },
        "micro_flaws": {
            "grammar": ["missing_comparative_more"],
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
                "why_not_7": "Error: 'Have a tendency to make complaints than' (missing 'more' - 'a higher tendency' or 'make more complaints').",
                "why_not_5": "Complex range."
            },
            "vocabulary": {
                "why_not_8": "'Inclined to', 'aggressive', 'impatient'. Very strong Band 7 vocabulary.",
                "why_not_6": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Inclined to', 'impatient'. Impact: Precise. Justification: Band 7.",
        "grammar_reason": "Observation: Comparative error. Justification: Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 13001,
        "sample_id": "NmATVc2m7iM_q01",
        "video_id": "NmATVc2m7iM",
        "part": 1,
        "question": "So, could you describe your hometown for me?",
        "transcript": "Yes, I am from China and my hometown is like the middle city of China and it is close to a big river, the biggest river and a yellow river and also our hometown is like a basin and it has a clearly like four seasons. it is really good to live.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_error", "verb_pattern"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["basin", "four seasons", "middle city"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["adverb_placement", "infinitive_use"],
            "vocabulary": ["imprecise_description"]
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'It has a clearly like four seasons' (has clearly four seasons / has four clear seasons). 'Good to live' (good place to live / good for living).",
                "why_not_5": "Sentences are mainly correct."
            },
            "vocabulary": {
                "why_not_7": "'Middle city' (central city). 'Basin' is good technical geography vocab.",
                "why_not_5": "Sufficient."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Basin'. 'Middle city'. Justification: Band 6.",
        "grammar_reason": "Observation: Adverb error. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 13002,
        "sample_id": "NmATVc2m7iM_q02",
        "video_id": "NmATVc2m7iM",
        "part": 1,
        "question": "And is there anything you dislike about your hometown?",
        "transcript": "To be honest, as young people, like, we would like to have more fun in our hometown. But everything, like, in there is really for, like, good for old people. We do not have, like, a fancy park here, like there, and also, like, a restaurant or, like, a museum or some of the other facilities.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["overuse_like"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["fancy park", "facilities"],
            "grammar_structures_used": ["contrast"]
        },
        "micro_flaws": {
            "grammar": ["informal_fillers"],
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
            "length_appropriateness": "optimal",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Heavy use of 'like' disrupts structure significantly. 'In there is really for' (what is there is...).",
                "why_not_5": "Meaning clear."
            },
            "vocabulary": {
                "why_not_7": "Basic range.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Facilities'. Justification: Band 6.",
        "grammar_reason": "Observation: Broken flow. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 13003,
        "sample_id": "NmATVc2m7iM_q03",
        "video_id": "NmATVc2m7iM",
        "part": 1,
        "question": "And what do you like to do when you have some free time?",
        "transcript": "Mostly I just watch YouTube or some of the others. For example, if I watch like English TV drama or some of the others, I could learn something new like English or Korea.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["watch YouTube", "learn something new"],
            "grammar_structures_used": ["conditional_first"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["repetitive_phrase"]
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Repetitive 'some of the others'.",
                "why_not_6": "Correct conditional."
            },
            "vocabulary": {
                "why_not_7": "Limited range.",
                "why_not_5": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error free.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 6.",
        "grammar_reason": "Observation: Correct structure. Justification: Band 7.",
        "vocabulary": 6,
        "grammar": 7
    },
    {
        "id": 13004,
        "sample_id": "NmATVc2m7iM_q04",
        "video_id": "NmATVc2m7iM",
        "part": 1,
        "question": "So do you like singing?",
        "transcript": "Not really. I think my singing is kind, is kind of worse actually. So, if I do not like someone or I like to show what is the shortage of myself and I would like to sing to someone.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": ["comparison_error", "sentence_structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "variable",
            "vocab_evidence": ["shortage of myself"],
            "grammar_structures_used": ["conditional"]
        },
        "micro_flaws": {
            "grammar": ["incorrect_comparative_worse"],
            "vocabulary": ["wrong_word_meaning"]
        },
        "vocab_control": {
            "appropriateness": "inaccurate",
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
            "flexibility": "moderate",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'Is kind of worse' (bad/terrible). 'What is the shortage of myself' (my weaknesses/shortcomings) - noun clause error.",
                "why_not_5": "Conditional structure is intact."
            },
            "vocabulary": {
                "why_not_7": "'Shortage' means lack of supply, not personal weakness. 'Worse' used as absolute adjective.",
                "why_not_5": "Meaning can be guessed."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 5,
            "vocabulary_text": "Errors may cause some difficulty."
        },
        "vocab_reason": "Observation: 'Shortage'. Wrong meaning. Justification: Band 5.",
        "grammar_reason": "Observation: Comparative error. Justification: Band 6.",
        "vocabulary": 5,
        "grammar": 6
    },
    {
        "id": 13005,
        "sample_id": "NmATVc2m7iM_q05",
        "video_id": "NmATVc2m7iM",
        "part": 1,
        "question": "And have you ever learned how to sing?",
        "transcript": "I do not think so, but I learned how to play piano, but I think I am really not good at it. So, the others could learn a song in a really short time, like in the beginning, but for me it is really hard.",
        "word_count": 46,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["play piano", "short time"],
            "grammar_structures_used": ["contrast", "comparison_implied"]
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Simple sentences connected by 'but'.",
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
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
