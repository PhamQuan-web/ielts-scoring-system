import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 234 ---
# Total Samples: 20
# Valid Samples: 15

scored_samples = [
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q17", "video_id": "wYeZwxPLrfU",
        "part": 3,
        "question": "Children dislike science?",
        "transcript": "Well, they are different. they are born all everyone's born differently. You know, some people like art, some people like math, some people like science. I see some some children find science boring, but they find art is fascinating. You know, I I myself was into science, but I was not into art at all. &gt;&gt; Okay, I see. just adding a few extra questions here.",
        "word_count": 59,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["fascinating", "into science"],
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
            "flexibility": "moderate",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Hesitations.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q18", "video_id": "wYeZwxPLrfU",
        "part": 3,
        "question": "Scientific innovation?",
        "transcript": "&gt;&gt; Invention wise science-wise. Well, I talked about AI AI earlier. So, I think that is been a big hit in our daily lives. and also I know someone recently is coming out with new cancer drugs. So I think that is huge and it is going to be in the market soon. &gt;&gt; Okay. just to wrap up quickly, you said that you were more inclined towards science &gt;&gt; when I was younger. Yeah. &gt;&gt;",
        "word_count": 76,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["invention wise", "big hit", "inclined towards"],
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
            "flexibility": "moderate",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Informal (big hit).",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "-oBIT8o8ruk_q01",
        "video_id": "-oBIT8o8ruk",
        "part": 1,
        "question": "Writing?",
        "transcript": "To reset my batteries. Moreover, I also tend to play video games with my sister to strengthen bonds.",
        "word_count": 17,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["strengthen bonds"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["idiom_usage"]
        },
        "vocab_control": {
            "appropriateness": "mixed",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'reset my batteries' (recharge)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
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
                "why_not_7": "Idiom error.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Idiom error. Band 5.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 5,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "-oBIT8o8ruk_q02",
        "video_id": "-oBIT8o8ruk",
        "part": 1,
        "question": "Nap?",
        "transcript": "Yes, absolutely. I tend to take enough. this because I I find comfortable for me and I will have more energy to do other important tasks such as studying or playing with my friends.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["important tasks"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["phrasing_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'take enough' (take a nap). 'find comfortable for me' (find it comfortable)."
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
                "why_not_6": "Phrasing errors.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Word choice.",
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
        "id": 0, "sample_id": "-oBIT8o8ruk_q03",
        "video_id": "-oBIT8o8ruk",
        "part": 1,
        "question": "Feel after nap?",
        "transcript": "After I take enough I tend to feel really elated and over the moon because I cannot recharge my battery and have more energy to be prepared and do other priorities. And.",
        "word_count": 31,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "logic"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["over the moon", "recharge my battery"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["logic_error"],
            "vocabulary": ["idiom_usage"]
        },
        "vocab_control": {
            "appropriateness": "mixed",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'over the moon' (inappropriate context for napping). 'cannot recharge' (can). 'do other priorities' (attend to?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Logic error.",
                "why_not_4": "Communicates."
            },
            "vocabulary": {
                "why_not_6": "Inappropriate idioms.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Inappropriate idioms. Band 5.",
        "grammar_reason": "Logic errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "-oBIT8o8ruk_q04",
        "video_id": "-oBIT8o8ruk",
        "part": 1,
        "question": "Borrow money?",
        "transcript": "Yes, definitely I tend to borrow a lot of money from my close friends or my family members. Yeah, you know when I go out start at going to supermarket I tend to get a lot of my money at home and then I can borrow it from them. Okay. Yes, certainly this because I am really into reading books so I tend to a lot of books especially comic books from my sister and she is really willing to enable me to borrow it and I am really grateful grateful for her assistance.",
        "word_count": 92,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrasing", "word_choice"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["grateful for assistance"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'start at going' (start going). 'get a lot of my money' (leave my money?). 'tend to a lot of books' (borrow). 'enable me to borrow' (let me)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent breakdown.",
                "why_not_4": "Sustained."
            },
            "vocabulary": {
                "why_not_6": "Errors affect meaning.",
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
        "grammar_reason": "Frequent errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "-oBIT8o8ruk_q05",
        "video_id": "-oBIT8o8ruk",
        "part": 1,
        "question": "Learn from others?",
        "transcript": "certainly I am really into landing to this because as you know I do not have a lot anything at books or something like that. I tend to lance order because I I find is really essential for me to land other especially my loved one such as close friends or family members.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "phonology"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'landing to this' (lending?). 'lance order' (lend to others?). 'land other' (lend)."
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
                "why_not_6": "Unclear.",
                "why_not_4": "Attempts complex."
            },
            "vocabulary": {
                "why_not_6": "Pronunciation affects meaning.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Pronunciation causes confusion. Band 5.",
        "grammar_reason": "Confusing structure. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "-oBIT8o8ruk_q06",
        "video_id": "-oBIT8o8ruk",
        "part": 1,
        "question": "Others borrow?",
        "transcript": "Yes, when anyone borrow from me I feel really comfortable and I find is really a central for them if they must borrow me for example when they borrow a book from me I am really willing to allow borrow from me.",
        "word_count": 41,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_choice"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'a central' (essential?). 'borrow me' (borrow from me). 'allow borrow' (allow them to borrow)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent errors.",
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
        "vocab_reason": "Basic errors. Band 5.",
        "grammar_reason": "Structure errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "-oBIT8o8ruk_q07",
        "video_id": "-oBIT8o8ruk",
        "part": 1,
        "question": "Parents teach share?",
        "transcript": "Yes, absolutely. My parents tend to teach me to share a lot of things to others such at my personal my personal stories or something like that is it really enables me to strengthen ours with them.",
        "word_count": 37,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["strengthen"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'such at' (such as). 'strengthen ours' (bonds/relationships?)."
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
                "why_not_6": "Errors.",
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
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "-oBIT8o8ruk_q08",
        "video_id": "-oBIT8o8ruk",
        "part": 1,
        "question": "What share?",
        "transcript": "I to be honest I really into sharing my personal stories to other especially my parents or my grandparents because it enables me to talk and have a lot of memorable moments with them and yeah and I tend to discuss and talk talk about is with them when I have.",
        "word_count": 50,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["memorable moments"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'I really into' (I am really into). 'stories to other' (others). 'talk about is' (it?)."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Structure errors.",
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
        "grammar_reason": "Missing verbs. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "-oBIT8o8ruk_q09",
        "video_id": "-oBIT8o8ruk",
        "part": 1,
        "question": "Not suitable to share?",
        "transcript": "I think that personal items laptops or mobile phones which have which are really valuable this because as you know I think when they borrow them they can studently break down them and I can I can feel really obsessed and upset and under the weather when they do like it.",
        "word_count": 50,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "phrasing"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["valuable", "under the weather"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["idiom_usage", "word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "mixed",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'studently' (suddenly?). 'break down them' (break them). 'obsessed' (upset?). 'under the weather' (sick - incorrect context)."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Phrasal verb error.",
                "why_not_4": "Communicates."
            },
            "vocabulary": {
                "why_not_6": "Idiom error.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Inappropriate idioms. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "-oBIT8o8ruk_q10",
        "video_id": "-oBIT8o8ruk",
        "part": 1,
        "question": "Recent share?",
        "transcript": "recently I sle my pants to my classmates and you know as my as my class my friends forgot to grow them and I I am really willing to share with them and I hope sometime when I also forgot them willing to allow me me use like and.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["willing to share"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'sle my pants' (lent my pens?). 'grow them' (bring them?). 'allow me me use' (let me use)."
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
            "development_depth": "confusing"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Breakdown.",
                "why_not_4": "Communicates."
            },
            "vocabulary": {
                "why_not_5": "Unclear words.",
                "why_not_4": "Basic."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 4,
            "vocabulary_text": "Uses only basic vocabulary which may be used repetitively."
        },
        "vocab_reason": "Very unclear. Band 4.",
        "grammar_reason": "Frequent errors. Band 5.",
        "vocabulary": 4,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "-oBIT8o8ruk_q13",
        "video_id": "-oBIT8o8ruk",
        "part": 3,
        "question": "Libraries changed?",
        "transcript": "Yes, definitely. I think libraries have a lot of significant change since in this day and age. However, if I had to name once it would be about the appearance since because as you know in the past there was not a lot of cutting as facility to build it. in day and there are many modern facilities and a lot of useful ways to enable reader to read with ok and what should we do to prevent modern libraries from closing down you can repeat question.",
        "word_count": 87,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_choice"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["modern facilities"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'cutting as facility' (cutting edge?). 'since in this day' (in this day). 'enable reader to read with' (read comfortably?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent breakdown.",
                "why_not_4": "Sustained."
            },
            "vocabulary": {
                "why_not_6": "Errors.",
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
        "id": 0, "sample_id": "-oBIT8o8ruk_q14",
        "video_id": "-oBIT8o8ruk",
        "part": 3,
        "question": "Help maintenance?",
        "transcript": "To be honest, I am not really understand certainly about the question.",
        "word_count": 12,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form"],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["form_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'I am not really understand' (I do not)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Basic error.",
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
        "id": 0, "sample_id": "-oBIT8o8ruk_q15",
        "video_id": "-oBIT8o8ruk",
        "part": 3,
        "question": "Stop closing?",
        "transcript": "To stop the library closing down. I would like to say that in this day and there is very first useful method to deal with this problem. If I would be the advertisement about them through the internet this is because you know when the internet develops we can advertise them through a lot of social media platforms TikTok or Instagram to more people know them. Okay. So that is it for the practice test.",
        "word_count": 73,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["social media platforms", "advertisement"],
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
            "reason": "'If I would be the advertisement' (it would be?). 'to more people know them' (so more people)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Breakdown.",
                "why_not_4": "Sustained."
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
        "vocab_reason": "Good terms but basic. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "-oBIT8o8ruk_q18",
        "video_id": "-oBIT8o8ruk",
        "part": 1,
        "question": "Nervous?",
        "transcript": "I often get nervous, especially during that time.",
        "word_count": 8,
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
                "why_not_6": "Too short.",
                "why_not_4": "Accurate."
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
        "grammar_reason": "Accurate. Band 5.",
        "vocabulary": 5,
        "grammar": 5
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
