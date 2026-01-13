import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 12201,
        "sample_id": "ahibrktrDcA_q03",
        "video_id": "ahibrktrDcA",
        "part": 1,
        "question": "What did you study in history lessons when you were in school?",
        "transcript": "The history lessons that I took as a child taught me about different events that, made a huge impact in our country and, different events that happened in our early time that changed our country's politics and that also have had a huge impact on our social Did you enjoy studying history at school? I would say that I did not really enjoy studying history as a child because it was a really boring topic for me because I had to learn about some people I did not know and what they did in the past and what kind. I had to remember all of that and it really came up as a boring topic to me so I did not really enjoy it.",
        "word_count": 121,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition_of_clauses"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["huge impact", "boring topic"],
            "grammar_structures_used": ["relative_clause", "reason_clause"]
        },
        "micro_flaws": {
            "grammar": ["run_on_sentence"],
            "vocabulary": ["repetitive_adjectives"]
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
            "length_appropriateness": "extended",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Repetitive structures 'that... that... that'.",
                "why_not_6": "Complex sentences generally correct."
            },
            "vocabulary": {
                "why_not_8": "Basic vocabulary 'huge impact', 'boring topic'.",
                "why_not_6": "Accurate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Huge impact'. Justification: Band 7.",
        "grammar_reason": "Observation: Relative clauses used well. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 12202,
        "sample_id": "ahibrktrDcA_q04",
        "video_id": "ahibrktrDcA",
        "part": 1,
        "question": "And how often do you watch television programs that are made on the basis of history or that are about history?",
        "transcript": "I don really find myself watching that kind of TV shows or any documentaries because as of now too I don I not really interested in history What period in history would you like to learn more about if you get an opportunity to I would like to learn about the history, time period where people really did not exist. And I would like to learn about what kind of animals existed in that period and what life was, life really was like to, the animals, That existed back then. that is it.",
        "word_count": 92,
        "analysis_metadata": {
            "grammar_error_patterns": ["omission_of_verb"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["time period", "existed"],
            "grammar_structures_used": ["conditional_hypothetical", "relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["missing_be_verb_am"],
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
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'I not really interested' (I am not).",
                "why_not_6": "Complex structures attempts."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Clear."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Time period'. Justification: Band 7.",
        "grammar_reason": "Observation: Missing auxiliary. Justification: Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 12203,
        "sample_id": "ahibrktrDcA_q06",
        "video_id": "ahibrktrDcA",
        "part": 3,
        "question": "The first question will be, how well do you think people generally know about their neighbors in your country?",
        "transcript": "I think that it really depends on the type of people we are talking about. Some people are really outgoing and forward and they like to learn about their neighbors and interact with them and create bonds with them. While some other people are not really interested in talking to their neighbors and getting to know them personally. So I would say that it really depends on people to know about their neighbors. How important do you think it is to have a good neighbor I think it is very important to have a good neighbor because it can really impact on your children and they can learn how you can interact with other people that you meet for the first time And it can also make them learn about helping each other helping each other in need And I think it is very important to have a good neighbor because of that reason",
        "word_count": 149,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["create bonds", "interact with", "getting to know them", "impact on"],
            "grammar_structures_used": ["complex_sentence_contrast", "noun_clause"]
        },
        "micro_flaws": {
            "grammar": [],
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
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "extended",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Very strong.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'Create bonds', 'outgoing and forward'. Precise.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Create bonds'. Impact: Precise. Justification: Band 8.",
        "grammar_reason": "Observation: Error free. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 12204,
        "sample_id": "ahibrktrDcA_q07",
        "video_id": "ahibrktrDcA",
        "part": 3,
        "question": "Which facilities do you think are the most important for people living in cities?",
        "transcript": "I think, all kinds of facilities should be given priority to develop and improve in cities because it is one of the main aspects that differentiates cities from other rural areas. And, it also, various, facilities like, education, transportation, health, drinking water, and, other facilities are very important, for our city to have. Because it will be very helpful to, the people that are living in that city.",
        "word_count": 66,
        "analysis_metadata": {
            "grammar_error_patterns": ["passive_voice"],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["given priority", "differentiates cities", "rural areas"],
            "grammar_structures_used": ["passive_voice", "relative_clause"]
        },
        "micro_flaws": {
            "grammar": [],
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
                "why_not_9": "Passive 'should be given priority' is excellent. Minor hesitation.",
                "why_not_7": "Complex structures."
            },
            "vocabulary": {
                "why_not_9": "'Differentiates', 'priority'. Academic.",
                "why_not_7": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Differentiates'. Impact: Academic. Justification: Band 8.",
        "grammar_reason": "Observation: Passive voice. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 12205,
        "sample_id": "ahibrktrDcA_q08",
        "video_id": "ahibrktrDcA",
        "part": 3,
        "question": "Do you think children should always go to a school that is nearest to their home?",
        "transcript": "I think it really depends on the parents to decide what kind of school their child will be attended to. Because at the end of the day, those parents will know what kind of services their child will receive, what kind of teachings their child will receive, and what kind of environment their child will be learning on. So it really depends on the parents to know what kind of school their children will be attended to.",
        "word_count": 75,
        "analysis_metadata": {
            "grammar_error_patterns": ["passive_error", "preposition_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["at the end of the day", "receive services"],
            "grammar_structures_used": ["noun_clause", "passive_voice"]
        },
        "micro_flaws": {
            "grammar": ["incorrect_passive_attended_to"],
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
                "why_not_8": "'Child will be attended to' (attend). Passive error.",
                "why_not_6": "Complex structures."
            },
            "vocabulary": {
                "why_not_8": "'Services' is odd for school (education?).",
                "why_not_6": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'At the end of the day'. Justification: Band 7.",
        "grammar_reason": "Observation: Passive error. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 12501,
        "sample_id": "f4zp__bJafI_q01",
        "video_id": "f4zp__bJafI",
        "part": 1,
        "question": "Where do you come from?",
        "transcript": "I come from a small town Tohana which is located in district Wartabad and state Haryana and it is located in the northern part of India.",
        "word_count": 25,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["located in", "northern part"],
            "grammar_structures_used": ["relative_clause"]
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
            "length_appropriateness": "concise",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Standard intro.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient."
        },
        "vocab_reason": "Observation: Standard. Justification: Band 7.",
        "grammar_reason": "Observation: Correct. Justification: Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 12502,
        "sample_id": "f4zp__bJafI_q02",
        "video_id": "f4zp__bJafI",
        "part": 1,
        "question": "Do you like sports?",
        "transcript": "Yes, of course. I am a sports enthusiastic person and I love to play sports.",
        "word_count": 15,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "variable",
            "vocab_evidence": ["sports enthusiastic"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["adjective_noun_order_error"],
            "vocabulary": ["wrong_collocation"]
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
            "complexity_level": "simple",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "concise",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'Sports enthusiastic person' (sports enthusiast or enthusiastic about sports).",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Collocation error.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Sports enthusiastic'. Justification: Band 6.",
        "grammar_reason": "Observation: Word form error. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 12503,
        "sample_id": "f4zp__bJafI_q06",
        "video_id": "f4zp__bJafI",
        "part": 1,
        "question": "Do you think children need more exercise?",
        "transcript": "Yes, of course. Children nowadays need more exercise. Not only children. All of us need to do more exercise as it keeps us happy. Keeps us healthy.",
        "word_count": 26,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["do more exercise", "keeps us healthy"],
            "grammar_structures_used": ["reason_clause"]
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
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
