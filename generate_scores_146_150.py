import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 14601,
        "sample_id": "qLf6L-Y27M0_q12",
        "video_id": "qLf6L-Y27M0",
        "part": 3,
        "question": "And do you prefer to take these with your phone or a camera?",
        "transcript": "I like with my, actually with my phone because it is easy for me.",
        "word_count": 13,
        "analysis_metadata": {
            "grammar_error_patterns": ["omission_of_verb"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["easy for me"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["omitted_verb_take_photos"],
            "vocabulary": []
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
            "complexity_level": "simple",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Missing main verb 'I like [taking them] with my phone'.",
                "why_not_4": "Meaning clear."
            },
            "vocabulary": {
                "why_not_6": "Very basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts basic sentences.",
            "vocabulary_band": 5,
            "vocabulary_text": "Limited."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 5.",
        "grammar_reason": "Observation: Missing verb. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 14602,
        "sample_id": "qLf6L-Y27M0_q13",
        "video_id": "qLf6L-Y27M0",
        "part": 3,
        "question": "For example, they told me, could you hang up with us?",
        "transcript": "And I said, no I cannot, I could not. And because I do not like to hang up with them and just I wanted to watch a movie in my home. And then tomorrow, that time, I want to, I wanted to travel to my home, hometown. And, I felt I, it is, I am, I was wrong because, always, I, I think I, I have to, tell the truth to my friends. And because there are, truth with me, and, yes, that is all.",
        "word_count": 87,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_error", "phrasal_verb_error"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["tell the truth", "hometown"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["tense_inconsistency"],
            "vocabulary": ["wrong_phrasal_verb_hang_up"]
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
                "why_not_6": "Frequent self-correction and tense errors 'I want to, I wanted to'. 'There are truth with me' (unclear/ungrammatical).",
                "why_not_4": "Can form basic compound sentences."
            },
            "vocabulary": {
                "why_not_6": "'Hang up with them' (hang out with them) - repeated error. 'Truth with me' (honest?).",
                "why_not_4": "Generally understandable."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Frequent errors.",
            "vocabulary_band": 5,
            "vocabulary_text": "Errors occur."
        },
        "vocab_reason": "Observation: 'Hang up' error. Justification: Band 5.",
        "grammar_reason": "Observation: Tense/correction issues. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 14603,
        "sample_id": "qLf6L-Y27M0_q14",
        "video_id": "qLf6L-Y27M0",
        "part": 3,
        "question": "Anything else?",
        "transcript": "Yes,. When I was sitting in my couch, our couch, and my friend hanging, my friend were hanging to me, and yes, with my phone, and I told them, no, I could not hang out with you.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_tense", "preposition_error"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["hang out"],
            "grammar_structures_used": ["past_continuous"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement_friend_were"],
            "vocabulary": ["wrong_verb_hanging_to_me"]
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
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "'My friend were hanging to me' (was calling me? messaging me?). Very confusing structure.",
                "why_not_4": "Past continuous attempted."
            },
            "vocabulary": {
                "why_not_6": "Meaning obscured by poor choice 'hanging to me'.",
                "why_not_4": "Basic words correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Frequent errors.",
            "vocabulary_band": 5,
            "vocabulary_text": "Limited."
        },
        "vocab_reason": "Observation: 'Hanging to me'. Justification: Band 5.",
        "grammar_reason": "Observation: Agreement/tense errors. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 14604,
        "sample_id": "qLf6L-Y27M0_q16",
        "video_id": "qLf6L-Y27M0",
        "part": 3,
        "question": "When is it acceptable to lie?",
        "transcript": "I think, the lie is accepted, when, for example, you are in a, in worst situation and, for example, dangerous situation. I think everyone can, tell a lie. And, but, in total I do not like, lying. And I want just, I hope, I am a person who always tell truth to others.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_error", "word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["dangerous situation", "tell a lie", "tell truth"],
            "grammar_structures_used": ["complex_sentence_condition", "relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["missing_article_truth"],
            "vocabulary": ["wrong_word_form_accepted"]
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
                "why_not_7": "'Person who always tell truth' (tells the truth). 'The lie is accepted' (acceptable).",
                "why_not_5": "Complex sentences used successfully."
            },
            "vocabulary": {
                "why_not_7": "'Accepted' (acceptable). 'In total' (overall/generally).",
                "why_not_5": "Clear."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Accepted' error. Justification: Band 6.",
        "grammar_reason": "Observation: Agreement/article errors. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 14605,
        "sample_id": "qLf6L-Y27M0_q17",
        "video_id": "qLf6L-Y27M0",
        "part": 3,
        "question": "What do you think about the fact that everybody has lied at least once?",
        "transcript": "The real lie or lie for, for example, help to others. Real lie. The real lie. Well, you have to answer the question. In fact, I think, always tell the truth can help us to solve our problems. And, as I told you, when we are, for example, in a dangerous situation and we are forced to tell lies, we can tell lies to others.",
        "word_count": 66,
        "analysis_metadata": {
            "grammar_error_patterns": ["gerund_missing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["dangerous situation", "forced to", "solve our problems"],
            "grammar_structures_used": ["passive_voice", "gerund_subject_attempt"]
        },
        "micro_flaws": {
            "grammar": ["infinitive_as_subject_error"],
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
                "why_not_7": "'Always tell the truth can help us' (Telling the truth). Subject must be gerund/noun.",
                "why_not_5": "Passive 'we are forced to' used correctly."
            },
            "vocabulary": {
                "why_not_7": "Good range 'forced to', 'solve problems'.",
                "why_not_5": "Clear."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Forced to'. Justification: Band 6.",
        "grammar_reason": "Observation: Gerund subject error. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 14606,
        "sample_id": "qLf6L-Y27M0_q18",
        "video_id": "qLf6L-Y27M0",
        "part": 3,
        "question": "Do you think we can lie to our friends and family?",
        "transcript": "Not actually. I always tell the truth to my family or friend. But it depends on that situation. It depends on every situation.",
        "word_count": 22,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["tell the truth", "depends on"],
            "grammar_structures_used": ["simple_sentence"]
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
            "redundancy": "medium",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Too simple/short.",
                "why_not_5": "Correct."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
                "why_not_5": "Clear."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Simple forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 6.",
        "grammar_reason": "Observation: Correct. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 14607,
        "sample_id": "qLf6L-Y27M0_q19",
        "video_id": "qLf6L-Y27M0",
        "part": 3,
        "question": "And, do you find it acceptable to lie about your feelings to someone because you do not want to hurt them?",
        "transcript": "I think it not a it it is a bad it is the worst things in the world to lie the friends or some someone can for example broke their heart And for example they think about us as a bad person And, has anybody ever lied to you about their real identity? real.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_pattern", "agreement"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["worst things", "bad person"],
            "grammar_structures_used": ["complex_sentence_attempt"]
        },
        "micro_flaws": {
            "grammar": ["omitted_verb_to_lie_to"],
            "vocabulary": ["broke_heart_tense"]
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
                "why_not_6": "'It not a' (is not). 'To lie the friends' (lie to friends). 'Someone can broke their heart' (break).",
                "why_not_4": "Meaning clear."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
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
        "grammar_reason": "Observation: Frequent errors. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 14608,
        "sample_id": "qLf6L-Y27M0_q20",
        "video_id": "qLf6L-Y27M0",
        "part": 3,
        "question": "Has anybody ever lied to you about their real identity?",
        "transcript": "That is the question. I think I do not like, I do not like, somebody are, reliable, to everyone. I want, I, I prefer to make a friendship with, everyone can be a truth, for example, truth person. And there are a lot of people who, in the world, that, they are, for example, fake. And always tell us, for example, the lie, lying things.",
        "word_count": 66,
        "analysis_metadata": {
            "grammar_error_patterns": ["sentence_structure", "agreement"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["make a friendship", "fake"],
            "grammar_structures_used": ["relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["confused_structure"],
            "vocabulary": ["wrong_word_choice_truth_person"]
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
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "'Somebody are reliable' (is). 'Everyone can be a truth person' (honest/truthful). 'The lie, lying things' (lies).",
                "why_not_4": "Core meaning attempts complex forms."
            },
            "vocabulary": {
                "why_not_6": "'Truth person' is unnatural. 'Reliable' used correctly.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Frequent errors.",
            "vocabulary_band": 5,
            "vocabulary_text": "Limited."
        },
        "vocab_reason": "Observation: 'Truth person'. Justification: Band 5.",
        "grammar_reason": "Observation: Structure errors. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 15001,
        "sample_id": "4A6nm0ZK7VI_q02",
        "video_id": "4A6nm0ZK7VI",
        "part": 1,
        "question": "Okay, can you tell me something about your family members?",
        "transcript": "I would love to join family. There are eight members in my family. My parents and, siblings, my parents and my parents and family.",
        "word_count": 23,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["eight members", "siblings"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["wrong_word_join_family"]
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
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "high",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "'I would love to join family' (I live in a joint family?). Repetitive listing.",
                "why_not_4": "Simple sentences correct."
            },
            "vocabulary": {
                "why_not_6": "Wrong word 'join'.",
                "why_not_4": "Basic."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts basic sentences.",
            "vocabulary_band": 5,
            "vocabulary_text": "Limited."
        },
        "vocab_reason": "Observation: 'Join family' error. Justification: Band 5.",
        "grammar_reason": "Observation: Repetitive. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 15002,
        "sample_id": "4A6nm0ZK7VI_q03",
        "video_id": "4A6nm0ZK7VI",
        "part": 1,
        "question": "Okay, who is very close to you in your family?",
        "transcript": "In my family. My father and mother are very close to me and I share all things with my father.",
        "word_count": 19,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["close to me", "share all things"],
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
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Too simple.",
                "why_not_5": "Correct."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
                "why_not_5": "Clear."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Simple forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 6.",
        "grammar_reason": "Observation: Correct. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 15003,
        "sample_id": "4A6nm0ZK7VI_q04",
        "video_id": "4A6nm0ZK7VI",
        "part": 1,
        "question": "How much time do you give to your family every day?",
        "transcript": "I am a student and all day I am busy in my study.",
        "word_count": 13,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition_error"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["busy"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["wrong_preposition_busy_in"],
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
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Too simple. 'Busy in my study' (busy with my studies).",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Simple forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 6.",
        "grammar_reason": "Observation: Preposition error. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 15004,
        "sample_id": "4A6nm0ZK7VI_q06",
        "video_id": "4A6nm0ZK7VI",
        "part": 1,
        "question": "How do you spend your free time?",
        "transcript": "I have lots of hobbies. I spend time with my hobbies. Like as a, when I am free time, I like to listen music and I like to play games with my friends.",
        "word_count": 34,
        "analysis_metadata": {
            "grammar_error_patterns": ["connector_error", "verb_pattern"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["spend time", "listen music"],
            "grammar_structures_used": ["complex_sentence_time"]
        },
        "micro_flaws": {
            "grammar": ["when_i_am_free_time_error"],
            "vocabulary": ["wrong_connector_like_as_a"]
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
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "'Like as a' (For example/Such as). 'When I am free time' (When I have free time). 'Listen music' (listen to music). Frequent errors.",
                "why_not_4": "Meaning clear."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Frequent errors.",
            "vocabulary_band": 5,
            "vocabulary_text": "Limited."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 5.",
        "grammar_reason": "Observation: Frequent structural errors. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 15005,
        "sample_id": "4A6nm0ZK7VI_q07",
        "video_id": "4A6nm0ZK7VI",
        "part": 3,
        "question": "What type of hobbies you recommend to young people to have?",
        "transcript": "I recommend to young people mostly they prefer to spend time with their friends but I think one of the hobbies is the best to play games It very good for their health Ok what the difference between the hobbies of the young and children Young people have hobbies like as go for shopping with their friends and spend time with their friends and watching movies But the children have always like to play games So now turn to the next part of the speaking. This is your topic.",
        "word_count": 90,
        "analysis_metadata": {
            "grammar_error_patterns": ["connector_error", "verb_pattern"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["spend time", "watching movies"],
            "grammar_structures_used": ["complex_sentence_contrast"]
        },
        "micro_flaws": {
            "grammar": ["like_as_error", "missing_verb_is"],
            "vocabulary": ["imprecise_meaning"]
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
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "'Like as go for shopping' (like going shopping). 'It very good' (It is). 'Children have always like to' (always like to).",
                "why_not_4": "Sentences are recognizable."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Frequent errors.",
            "vocabulary_band": 5,
            "vocabulary_text": "Limited."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 5.",
        "grammar_reason": "Observation: Missing verbs/connectors. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
