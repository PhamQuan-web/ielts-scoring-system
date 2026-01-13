import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 230 ---
# Total Samples: 20
# Valid Samples: 15

scored_samples = [
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q09", "video_id": "Ut_jyNrnlYE",
        "part": 1,
        "question": "Dry or wet weather?",
        "transcript": "The wet weather makes me feel uncomfortable. So I prefer the dry weather.",
        "word_count": 13,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["uncomfortable"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
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
            "complexity_level": "low",
            "accuracy_level": "high",
            "flexibility": "low",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Too short.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Basic. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q10", "video_id": "Ut_jyNrnlYE",
        "part": 1,
        "question": "Checking forecast?",
        "transcript": "I am not person who often checks the weather up. So I I go out without checking it.",
        "word_count": 17,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["phrasing_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'checks the weather up' (checks the weather)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Phrasing error.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q11", "video_id": "Ut_jyNrnlYE",
        "part": 1,
        "question": "Start internet?",
        "transcript": "As I remembered, I started using the internet since I was in secondary school when I first had my first phone.",
        "word_count": 20,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'since I was' with 'when I first had' creates structural redundancy."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Structural redundancy.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q12", "video_id": "Ut_jyNrnlYE",
        "part": 1,
        "question": "Often online?",
        "transcript": "Every day when I have free time, I serve the internet and charge with my friend.",
        "word_count": 16,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_error", "pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'serve the internet' (surf). 'charge with' (chat with)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Errors.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Word choice errors.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Errors. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q13", "video_id": "Ut_jyNrnlYE",
        "part": 1,
        "question": "Too much time?",
        "transcript": "Personally, I myself in the internet. So, yeah, I am a social butterfly and I spend most of my time on the internet.",
        "word_count": 22,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["social butterfly"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'I myself in the internet' (immerse myself?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Missing verb.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Errors.",
                "why_not_5": "Good idiom."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Idiom lifts it. Band 6.",
        "grammar_reason": "Structural error. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q14",
        "video_id": "Ut_jyNrnlYE",
        "part": 1,
        "question": "Influence?",
        "transcript": "Maybe in a technological era the internet can provide a variety of knowledge for people and for students especially. it is a useful tool for first to study and learn. And.",
        "word_count": 30,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["technological era", "variety of knowledge"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'tool for first to study' (for us?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Short.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "ASR errors/Pron.",
                "why_not_5": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good collocations. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q16",
        "video_id": "Ut_jyNrnlYE",
        "part": 3,
        "question": "Recycle items?",
        "transcript": "I am not interested in this field if but I think they will recycle by throwing them away and then the garbage collector collected and to recycle it in in somewhere.",
        "word_count": 30,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition", "structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["garbage collector"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["repetition_error", "structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'collector collected'. 'in in somewhere'."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "high",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Repetitive/Broken.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q17",
        "video_id": "Ut_jyNrnlYE",
        "part": 3,
        "question": "Government encourage?",
        "transcript": "Yes, I think it is a good decision because it helps to boost the awareness of people and the government does not have to pay much attention to the Soviet Union. Moreover when people are aware of the importance of cycling, it is not the financial problem to the government.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "mixed",
            "vocab_evidence": ["boost the awareness", "financial problem"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "mixed",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Soviet Union' (?? nonsensical context). 'cycling' (recycling). 'financial problem to' (for)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Preposition errors.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Wrong words (cycling, Soviet Union).",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Errors in key words. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q18",
        "video_id": "Ut_jyNrnlYE",
        "part": 3,
        "question": "Problems if no recycle?",
        "transcript": "Maybe the maybe in the future the world will be affected and days by day by day it is worse than the past because the pollution will be affected. It can be more air and what will happen if there is more air the people's longevity will be affected it is shortened and maybe people will feel uncomfortable because they cannot breathe So do you feel uncomfortable when you have the opportunity to Yes, of course.",
        "word_count": 73,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition", "logic"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["longevity", "pollution"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["repetition_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'pollution will be affected' (pollution will increase?). 'more air' (more pollution?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "high",
            "development_depth": "confusing"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Confusing structure.",
                "why_not_4": "Communicates."
            },
            "vocabulary": {
                "why_not_6": "Wrong word choice.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic with errors. Band 5.",
        "grammar_reason": "Confusing. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q19", "video_id": "Ut_jyNrnlYE",
        "part": 3,
        "question": "Raise awareness?",
        "transcript": "Moreover, we can plant more trees and we can reduce the emissions from the factory or the vehicles.",
        "word_count": 17,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["plant more trees", "reduce the emissions"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
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
            "flexibility": "low",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Short.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Good terms.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good terms. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q20", "video_id": "Ut_jyNrnlYE",
        "part": 3,
        "question": "Easy to plant?",
        "transcript": "I think it is easier than the other options because anyone can do that and if we do and I think if we do often or the government encourages it can Wi spread. Okay. Already.",
        "word_count": 34,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["government encourages", "widespread"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Wi spread' (widespread)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Short.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Good term.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Widespread. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q21", "video_id": "Ut_jyNrnlYE",
        "part": 3,
        "question": "Practice?",
        "transcript": "Yeah, I kind of practice writing essays on my own, but it is not a regular occurrence.",
        "word_count": 16,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["regular occurrence"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
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
            "complexity_level": "low",
            "accuracy_level": "high",
            "flexibility": "low",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Short.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Good term.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good term. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q22", "video_id": "Ut_jyNrnlYE",
        "part": 3,
        "question": "Scanning?",
        "transcript": "Yes. it is been a long time since I have touched it.",
        "word_count": 11,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["been a long time since"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
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
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Short.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Natural.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Natural. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q23", "video_id": "Ut_jyNrnlYE",
        "part": 3,
        "question": "Training volume?",
        "transcript": "Currently, as I mentioned, I do not do it regularly; it is more spontaneous.",
        "word_count": 13,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["spontaneous"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
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
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Short.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Good word.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good word. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q25", "video_id": "Ut_jyNrnlYE",
        "part": 3,
        "question": "Center?",
        "transcript": "Yes, before the exam, I took the exam last year and I studied at a center.",
        "word_count": 16,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
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
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "low",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Short.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Basic. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q26", "video_id": "Ut_jyNrnlYE",
        "part": 3,
        "question": "Two years ago?",
        "transcript": "Two years ago, two years ago, the exam was held already.",
        "word_count": 11,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
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
            "complexity_level": "low",
            "accuracy_level": "high",
            "flexibility": "low",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Short.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Basic. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    }
]

# Write to file
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
        for sample in scored_samples:
            if sample['vocabulary'] == 0:
                continue
            if sample['sample_id'] not in existing_ids:
                f.write(json.dumps(sample) + '\n')
                count += 1

    print(f"Append complete. Added {count} new samples. (Skipped duplicates/invalid).")

except Exception as e:
    print(f"Error writing to file: {e}")
