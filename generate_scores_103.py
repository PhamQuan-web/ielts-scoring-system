import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 10301,
        "sample_id": "RFOdBq2EGVo_q24",
        "video_id": "RFOdBq2EGVo",
        "part": 1,
        "question": "And how often do you see your friends?",
        "transcript": "It depends. I, I try to see them as much as possible. It can be very hard to arrange meetings with friends, especially when you have like a, such a wide range. I see friends that I do sport with every day almost because I play sport every day, but then other people I do not see as often, but I am still just as close with when I meet up with them finally.",
        "word_count": 78,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["arrange meetings", "wide range", "meet up with"],
            "grammar_structures_used": ["relative_clause", "complex_sentence_contrast"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["repetitive_structure"]
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
            "complexity_level": "moderate_high",
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
                "why_not_9": "Sentence structure is natural but not highly sophisticated. Uses 'like a, such a' filler/hesitation.",
                "why_not_7": "Sentences are error free and relatively complex."
            },
            "vocabulary": {
                "why_not_9": "Good collocations but range is limited to daily life.",
                "why_not_7": "'Arrange meetings', 'wide range' are solid Band 7/8 features."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Majority of sentences are error-free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Fluently and flexibly uses a wide vocabulary."
        },
        "vocab_reason": "Observation: 'Wide range', 'arrange meetings'. Impact: Natural. Justification: Band 8.",
        "grammar_reason": "Observation: Complex sentences. Error free. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 10302,
        "sample_id": "RFOdBq2EGVo_q25",
        "video_id": "RFOdBq2EGVo",
        "part": 1,
        "question": "And do you have a best friend?",
        "transcript": "I w I wouldn really say that I have a best friend I have a couple of friends I would consider myself to be closer with but I think I think the word best friend can be very set in stone and you know things change Life is pretty variable So I tend to just know who my close friends are and yeah I keep it at that",
        "word_count": 68,
        "analysis_metadata": {
            "grammar_error_patterns": ["hesitation_fragment"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["set in stone", "consider myself to be", "variable"],
            "grammar_structures_used": ["complex_sentence_opinion"]
        },
        "micro_flaws": {
            "grammar": ["fluency_restart"],
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
            "flexibility": "moderate_high",
            "error_density": "rare"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Minor fluency glitches ('I w I wouldn').",
                "why_not_7": "Structures are complex and accurate."
            },
            "vocabulary": {
                "why_not_9": "Excellent idiom 'set in stone' used perfectly. 'Variable' is academic. Very strong.",
                "why_not_7": "Clearly above Band 7."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Majority of sentences error-free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses idiomatic language naturally and accurately."
        },
        "vocab_reason": "Observation: 'Set in stone', 'variable'. Impact: High precision. Justification: Band 9.",
        "grammar_reason": "Observation: Complex thought expressed clearly. Justification: Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 10303,
        "sample_id": "RFOdBq2EGVo_q28",
        "video_id": "RFOdBq2EGVo",
        "part": 1,
        "question": "Are you good at saving money?",
        "transcript": "No, I am not good at saving money at all. I tend to, I tend to do a lot of shopping. so I really like finding new brands and new boutiques. And I also love to go out and socialize with my friends. So I find it very hard to save money. and that is something I am definitely trying to work on.",
        "word_count": 61,
        "analysis_metadata": {
            "grammar_error_patterns": ["hesitation"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["boutiques", "socialize with", "work on"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["repetition_start"],
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
                "why_not_9": "Repetition 'I tend to, I tend to'.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Good words 'boutiques', 'socialize', but not fully flexible.",
                "why_not_7": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Boutiques'. Impact: Specific. Justification: Band 8.",
        "grammar_reason": "Observation: Error free. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 10304,
        "sample_id": "RFOdBq2EGVo_q29",
        "video_id": "RFOdBq2EGVo",
        "part": 1,
        "question": "And have you ever made an expensive purchase?",
        "transcript": "Yes I have. I would say I do a lot of rowing and that is a very expensive sport. So I would say that all my expenses for, for that sport have been very large I would say. And the memberships are always pretty expensive. So I consider it something that is very important to me and it is obviously a lot of money. Obviously like one of my main sports that I do so I tend to put it at a high priority.",
        "word_count": 86,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["memberships", "high priority", "expensive sport"],
            "grammar_structures_used": ["complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": ["repetitive_phrasing"],
            "vocabulary": ["repetition_of_adjectives"]
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
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Repetitive 'I would say', 'obviously'.",
                "why_not_7": "Sentences are technically accurate."
            },
            "vocabulary": {
                "why_not_9": "Repetitive 'expensive'.",
                "why_not_7": "'High priority' is good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control of grammar and punctuation but may make a few mistakes.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses some less common and idiomatic vocabulary."
        },
        "vocab_reason": "Observation: 'High priority'. Repetitive 'expensive'. Justification: Band 7/8. Repetition pulls it down.",
        "grammar_reason": "Observation: Repetitive structures 'I would say'. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 10305,
        "sample_id": "RFOdBq2EGVo_q33",
        "video_id": "RFOdBq2EGVo",
        "part": 3,
        "question": "Is there a good way to give constructive feedback to someone about something?",
        "transcript": "Yes, I definitely think there is, and this is something that I have learned about in one of the courses I am studying at uni too, which was about, sports coaching. So, how we can give constructive feedback and help our students to learn, to learn from their mistakes. I think it is really important when giving constructive feedback to say something positive first. to make sure you are not too negative and that you do not have a negative tone to your voice, that you are happy. and that you are just generally trying to help them. You want to give off the vibe that you are just trying to help them and not that you are trying to put them down. I think it is one of the worst things when someone's telling you something and you know they are just trying to let you down and trying to make you feel bad about yourself.",
        "word_count": 161,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["constructive feedback", "negative tone", "give off the vibe", "put them down", "let you down"],
            "grammar_structures_used": ["complex_sentence_noun_clause", "relative_clause", "infinitive_purpose"]
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
                "why_not_9": "Very strong. Minor hesitation but structures are complex.",
                "why_not_8": "Sustained control."
            },
            "vocabulary": {
                "why_not_9": "Phrasal verbs 'give off the vibe', 'put them down', 'let you down' used with total naturalness. 'Constructive feedback' is precise.",
                "why_not_8": "Better than skilful."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Full range of structures naturally.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility."
        },
        "vocab_reason": "Observation: 'Give off the vibe', 'put them down'. Impact: Highly natural/idiomatic. Justification: Band 9.",
        "grammar_reason": "Observation: Complex sentences flow naturally. Justification: Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 10306,
        "sample_id": "RFOdBq2EGVo_q34",
        "video_id": "RFOdBq2EGVo",
        "part": 3,
        "question": "This or how about next time you do this?",
        "transcript": "I think always phrasing it as a question is also a more sensitive way to approach the topic.",
        "word_count": 18,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["phrasing it as a question", "sensitive way", "approach the topic"],
            "grammar_structures_used": ["gerund_subject"]
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
            "length_appropriateness": "concise",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Short but perfect. Gerund subject 'Phrasing it... is'.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'Phrasing it', 'approach the topic' are academic and precise.",
                "why_not_7": "Advanced."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Full range.",
            "vocabulary_band": 9,
            "vocabulary_text": "Precise."
        },
        "vocab_reason": "Observation: 'Phrasing it', 'approach'. Impact: Precise. Justification: Band 9.",
        "grammar_reason": "Observation: Gerund subject. Justification: Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 10307,
        "sample_id": "rhUfegetw4o_q04",
        "video_id": "rhUfegetw4o",
        "part": 1,
        "question": "What is your first name please?",
        "transcript": "My first name is Chiara.",
        "word_count": 5,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["simple"]
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
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Too simple.",
                "why_not_7": "Correct."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Basic."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Simple forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Name only. Justification: Band 6 default for short answers.",
        "grammar_reason": "Observation: Correct. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
