import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 10101,
        "sample_id": "QfCcbDhYimo_q09",
        "video_id": "QfCcbDhYimo",
        "part": 3,
        "question": "Can you explain me what poaching is?",
        "transcript": "Oh sure. so, for example, when people hunt wild animals. that is poaching. Yeah, that is poaching.. Usually it is illegal. yeah, I do not agree with poaching because, for, some people who poaching, who are normally poaching, As I think the purpose is for the money, which is very bad purpose. Yeah, I do not think it is good for animals to be used for money or for being famous or something. So, yeah, I do not think that is a good way to make money.",
        "word_count": 82,
        "analysis_metadata": {
            "grammar_error_patterns": ["missing_verb", "article_missing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["hunt wild animals", "illegal", "purpose", "being famous"],
            "grammar_structures_used": ["relative_clause", "reason_clause"]
        },
        "micro_flaws": {
            "grammar": ["missing_verb_in_relative_clause", "missing_article"],
            "vocabulary": ["repetition_of_keywords"]
        },
        "vocab_control": {
            "appropriateness": "mostly_accurate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "No high-level idioms attempted."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "partial"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors in complex structures ('people who poaching'); lacks error-free sentences characteristic of Band 7.",
                "why_not_5": "Attempted complex sentences (relative clauses, 'As I think...') are generally clear despite errors; maintains flow better than Band 5."
            },
            "vocabulary": {
                "why_not_7": "Lacks less common vocabulary; relies on repetition of 'poaching' and 'money'.",
                "why_not_5": "vocabulary is sufficient to discuss the topic; 'illegal' and 'purpose' are used correctly."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Uses a mix of simple and complex sentence forms. Errors in grammar and punctuation may occur frequently.",
            "vocabulary_band": 6,
            "vocabulary_text": "Has a wide enough vocabulary to discuss topics at length and make meaning clear despite inappropriacies."
        },
        "vocab_reason": "Observation: Uses topic words 'hunt', 'wild animals', 'illegal'. Impact: Meaning is clear. Justification: Meets Band 6 criteria for adequacy, but lacks the range/precision for Band 7.",
        "grammar_reason": "Observation: Uses relative clauses ('who are normally poaching') but with errors. Impact: Communication is not impeded. Justification: Classic Band 6 mix of simple/complex forms with frequent errors.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10102,
        "sample_id": "aI0JX2qc870_q03",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "What kind of people do you like to have as friends?",
        "transcript": "Actually I do not have many friends, but I try to, become friends, to people who are confident, because I believe they can, give that confidence to me too.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition_error"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["confident", "confidence", "become friends"],
            "grammar_structures_used": ["complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": ["wrong_preposition"],
            "vocabulary": ["repetition_stem"]
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
            "accuracy_level": "controlled",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate_for_part_1"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Although mostly error-free, the range of structures is limited in this short sample. 'become friends to people' is a slight error preventing 'majority error-free' claim.",
                "why_not_5": "Complex sentence structure ('because I believe...') is well controlled."
            },
            "vocabulary": {
                "why_not_7": "Repetition of 'confident/confidence' and basic phrasing prevents higher band.",
                "why_not_5": "Correct usage of 'confident' and 'believe'."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Uses a mix of simple and complex sentence forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Has a wide enough vocabulary to discuss topics at length and make meaning clear."
        },
        "vocab_reason": "Observation: Uses 'confident' and 'confidence'. Impact: Clear meaning. Justification: Adequate for the task (Band 6).",
        "grammar_reason": "Observation: Uses 'because' clause. Impact: Clear reasoning. Justification: Competent control (Band 6).",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10103,
        "sample_id": "aI0JX2qc870_q04",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "Do you like face to face conversations with people?",
        "transcript": "Yes, I prefer, meet my friends, because, I am not a huge fan of chatting on social media.",
        "word_count": 21,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_pattern_error"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["huge fan", "chatting on social media", "face to face"],
            "grammar_structures_used": ["preference_structure"]
        },
        "micro_flaws": {
            "grammar": ["missing_to_particle"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
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
            "development_depth": "adequate_for_part_1"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Error 'prefer, meet' (should be 'prefer to meet' or 'prefer meeting').",
                "why_not_5": "Sentence structure is otherwise solid with a 'because' clause."
            },
            "vocabulary": {
                "why_not_8": "Good chunks ('huge fan', 'social media'), but sample is too short to demonstrate sustained flexibility.",
                "why_not_6": "Collocations are quite natural ('huge fan of'). Borderline 7."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors in grammar may occur frequently.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses some less common and idiomatic vocabulary and shows some awareness of style and collocation."
        },
        "vocab_reason": "Observation: Uses 'huge fan', 'social media'. Impact: Natural tone. Justification: Strong collocations push this to Band 7 for vocab.",
        "grammar_reason": "Observation: Error in verb pattern 'prefer meet'. Impact: Noticeable but minor. Justification: Band 6 for grammar.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 10104,
        "sample_id": "aI0JX2qc870_q05",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "And how often do you meet your friends?",
        "transcript": "Actually when I was younger I used to meet them at least once a week but these days because of this pandemic I could not see them.",
        "word_count": 28,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["used to meet", "at least once a week", "pandemic"],
            "grammar_structures_used": ["past_habit", "time_contrast"]
        },
        "micro_flaws": {
            "grammar": ["modal_past_for_present"],
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
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Use of 'could not' (past) for 'these days' (present context) is a slight slip. Should be 'cannot' or 'have not been able to'.",
                "why_not_5": "Correct use of 'used to' and complex sentence structure."
            },
            "vocabulary": {
                "why_not_7": "Vocabulary is accurate but lacks range/idiom.",
                "why_not_5": "Precise words 'pandemic', 'at least'."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Uses a mix of simple and complex sentence forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Has a wide enough vocabulary to discuss topics at length."
        },
        "vocab_reason": "Observation: 'Pandemic', 'used to'. Impact: Clear. Justification: Band 6.",
        "grammar_reason": "Observation: 'Used to' structure is good. Tense slip with 'could'. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10105,
        "sample_id": "aI0JX2qc870_q06",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "How often do you take a break?",
        "transcript": "To be honest, I like to go on holidays. After my exams, I prefer to have a short road trip.",
        "word_count": 21,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["short road trip", "go on holidays", "to be honest"],
            "grammar_structures_used": ["preference"]
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
                "why_not_7": "Sentences are error-free but very simple.",
                "why_not_5": "Perfect accuracy."
            },
            "vocabulary": {
                "why_not_7": "'Road trip' is a good collocation, but 'holidays' is basic. Borderline.",
                "why_not_5": "Natural phrasing."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Uses a mix of simple and complex sentence forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate vocabulary."
        },
        "vocab_reason": "Observation: 'Short road trip'. Impact: Natural. Justification: Solid Band 6.",
        "grammar_reason": "Observation: Error free. Impact: Clear. Justification: Simple structures limit it to Band 6/7. Safe Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10106,
        "sample_id": "aI0JX2qc870_q07",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "What do you usually do during a break?",
        "transcript": "We usually go to north of Iran on holidays and I always go to beach.",
        "word_count": 16,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_missing"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["go to beach", "north of Iran"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["missing_definite_article"],
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
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Two errors in a short sentence ('to north', 'to beach'). Density is high.",
                "why_not_4": "Basic sentence structure is intact."
            },
            "vocabulary": {
                "why_not_6": "Very basic vocabulary.",
                "why_not_4": "Words are correct for topic."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts basic sentences but accuracy is variable.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate for the task."
        },
        "vocab_reason": "Observation: Basic words. Justification: Band 5/6. Giving benefit of doubt 6.",
        "grammar_reason": "Observation: Missing articles twice. Justification: Band 5 level accuracy here.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 10107,
        "sample_id": "aI0JX2qc870_q08",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "Do you prefer a long break or several short breaks?",
        "transcript": "Definitely several short breaks. I think they are better than a long break.",
        "word_count": 14,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["several short breaks"],
            "grammar_structures_used": ["comparative"]
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
            "complexity_level": "basic",
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
                "why_not_5": "Error free."
            },
            "vocabulary": {
                "why_not_7": "Direct repetition of question words.",
                "why_not_5": "Accurate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Repetitive. Justification: Band 6.",
        "grammar_reason": "Observation: Correct comparative. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10108,
        "sample_id": "aI0JX2qc870_q09",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "Did you like science as a subject back in school?",
        "transcript": "Definitely no, because my major is not related to science. I study math.",
        "word_count": 14,
        "analysis_metadata": {
            "grammar_error_patterns": ["wrong_word_choice"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["major", "related to", "study math"],
            "grammar_structures_used": ["reason_clause"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["unnatural_phrasing"]
        },
        "vocab_control": {
            "appropriateness": "mostly_accurate",
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
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Good structure.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "'Definitely no' is unnatural (should be 'Definitely not').",
                "why_not_5": "Topic words correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Definitely no' error. 'Related to' good. Justification: Band 6.",
        "grammar_reason": "Observation: 'Because' clause good. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10109,
        "sample_id": "aI0JX2qc870_q10",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "And how has science helped you learn better?",
        "transcript": "As I mentioned, I am not good at science at all, but I think if I practice more chemistry lessons would help me a lot in my physics. All right, so.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": ["conditional_error", "sentence_structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["good at", "chemistry lessons", "physics"],
            "grammar_structures_used": ["conditional_mixed"]
        },
        "micro_flaws": {
            "grammar": ["broken_conditional_structure"],
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
            "complexity_level": "high",
            "accuracy_level": "low",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Complex structure ('if I practice... lessons would help') is broken.",
                "why_not_5": "Attempt is ambitious and meaning is clear."
            },
            "vocabulary": {
                "why_not_7": "Basic vocab.",
                "why_not_5": "Accurate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Uses a mix of simple and complex sentence forms. Errors may occur frequently.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Topic words used correctly. Justification: Band 6.",
        "grammar_reason": "Observation: Faulty complex structure. Justification: Band 6 (attempted complex forms).",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10110,
        "sample_id": "aI0JX2qc870_q12",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "Do people in your country try new gadgets and appliances in the market?",
        "transcript": "Why? Why not? I do not think so. I think Iranian people do not like to, somehow try new things. Maybe the most important reason is, we cannot, easily access to new gadgets in our country and we have to, wait for a while to be able to buy them. And some people find it easy to follow instructions while assembling a gadget, but others find it difficult.",
        "word_count": 71,
        "analysis_metadata": {
            "grammar_error_patterns": ["transitive_verb_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["access to", "follow instructions", "assembling a gadget"],
            "grammar_structures_used": ["reason_clause", "contrast_clause"]
        },
        "micro_flaws": {
            "grammar": ["verb_valency_error"],
            "vocabulary": ["incorrect_preposition_after_verb"]
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
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "good",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors 'access to' and fluency/hesitations prevent 'error free sentences'.",
                "why_not_5": "Good control of long sentences."
            },
            "vocabulary": {
                "why_not_7": "'Access to' is a vocab error (access is transitive). 'Assembling a gadget' is strong.",
                "why_not_5": "Range is good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate. Some errors."
        },
        "vocab_reason": "Observation: 'Assembling', 'gadgets'. 'Access to' error. Justification: Strong Band 6.",
        "grammar_reason": "Observation: Good sentence length. Minor errors. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10111,
        "sample_id": "aI0JX2qc870_q13",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "Why is it so?",
        "transcript": "I think, always when we want to try a new thing, it could be different for us, but, after a while, it will easier and be used to it. Alright Do people feel uncomfortable using new products at home or work Why and why not As I mentioned it not easy for them at first but I think when they use it they become interested in them Do people feel, well this is what I asked already, do advertisements play a key role in promoting innovative and trendy products these days? definitely yes, because I think advertisements introduce us new things and without them, we cannot be aware of what is happening.",
        "word_count": 115,
        "analysis_metadata": {
            "grammar_error_patterns": ["missing_verb", "pattern_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["introduce us", "aware of", "innovative"],
            "grammar_structures_used": ["complex_sentence_time", "reason_clause"]
        },
        "micro_flaws": {
            "grammar": ["missing_be_verb"],
            "vocabulary": ["collocation_error"]
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
            "length_appropriateness": "long",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors 'it will easier' (missing be), 'introduce us new things' (missing to).",
                "why_not_5": "Flow is sustained."
            },
            "vocabulary": {
                "why_not_7": "Errors in usage.",
                "why_not_5": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur frequently.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Innovative', 'trendy'. Usage errors. Justification: Band 6.",
        "grammar_reason": "Observation: Missing verbs. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10112,
        "sample_id": "aI0JX2qc870_q14",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "Why and why not?",
        "transcript": "I do not think so because, I am not like this. I prefer to buy important things, not just simple things.",
        "word_count": 22,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["simple things", "important things"],
            "grammar_structures_used": ["reason_clause"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["imprecise_vocabulary"]
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
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_6": "Very vague ('important things').",
                "why_not_4": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: Vague words. Justification: Band 5/6.",
        "grammar_reason": "Observation: Correct. Justification: Band 6.",
        "vocabulary": 5,
        "grammar": 6
    },
    {
        "id": 10113,
        "sample_id": "aI0JX2qc870_q15",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "And do you think good decision making can be taught?",
        "transcript": "I think, schools have, plays actually the most important role these days. And we can learn a lot of things not just about our subjects from school. But unfortunately my country is not like this and our schools just focus on education. They do not introduce us gadgets and how we can use technology.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["subject_verb_agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["important role", "focus on education"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
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
            "length_appropriateness": "good",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'Schools have, plays' is a confusion.",
                "why_not_5": "Sentence structures are generally good."
            },
            "vocabulary": {
                "why_not_7": "Limited.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur frequently.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Good collocations 'focus on'. Justification: Band 6.",
        "grammar_reason": "Observation: Agreement error. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10114,
        "sample_id": "aI0JX2qc870_q16",
        "video_id": "aI0JX2qc870",
        "part": 1,
        "question": "And did you have the same experience?",
        "transcript": "Yes, for sure. But I think they have to add some, more useful classes like how we can, use computers. Because I think most, of people know this, how to use, computers. But maybe, someone do not know it. And the schools have to learn them.",
        "word_count": 50,
        "analysis_metadata": {
            "grammar_error_patterns": ["quantifier_error", "verb_choice_error", "agreement_error"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["useful classes", "use computers"],
            "grammar_structures_used": ["reason_clause"]
        },
        "micro_flaws": {
            "grammar": ["quantifier_structure", "subject_verb_agreement"],
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
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Errors are very frequent here ('most of people', 'someone do not', 'learn them'). Density pushes to 5.",
                "why_not_4": "Subordinate clauses used."
            },
            "vocabulary": {
                "why_not_6": "'Learn them' (teach them) is a meaning error. 'Most of people' is a phrasing error.",
                "why_not_4": "Generally clear."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts basic sentences but accuracy is variable. Frequent errors.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: Wrong word 'learn'. Justification: Band 5.",
        "grammar_reason": "Observation: Agreement and quantifier errors. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    }
]

with open(output_file, 'w') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Written {len(samples)} samples to {output_file}")
