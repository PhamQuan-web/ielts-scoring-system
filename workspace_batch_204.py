import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 204 ---
# Total Samples: 20
# Valid Scored: 16
# Skipped: 4 (Reasons below)

# --- SKIPPED SAMPLES LOG ---
# 1. WkqJSGnsOe8_q07: Examiner Promo/Instruction ("So before proceeding further... at your ISS partner platform") - Not candidate speech.
# 2. bGlQDqwIadE_q02: Fragment ("As ginger ginger tea... plenty Choice thank you") - Too short/incomplete to score reliably.
# 3. o9_Qsvc2QP4_q05: Examiner Instruction/Question heavy ("...so you haven't made your mind... did computer really help...") - Candidate answer is interrupted/mixed.
# 4. o9_Qsvc2QP4_q06: Examiner Instruction/Question heavy ("...do you let him for hair to use...") - Mixed speech, candidate answer is cut or rambling.

# Note: Samples for video o9_Qsvc2QP4 (Band 4.5) are very long and rambling with mixed examiner speech. I will score them but noting the difficulty.

# --- VALID SAMPLES DATA ---
scored_samples = [
    # Video: WkqJSGnsOe8 (Band 7.5)
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q06", "video_id": "WkqJSGnsOe8", "part": 1,
        "question": "Do you buy jewelry?",
        "transcript": "Not so often but I buy jewelry on any occasion on or any in any family function whenever it is required.",
        "word_count": 21,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["family function", "whenever it is required"],
            "grammar_structures_used": ["complex_sentences"]
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
            "flexibility": "limited",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Short.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Natural ('whenever it is required'). Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q08", "video_id": "WkqJSGnsOe8",
        "part": 1,
        "question": "Do you like weekends?",
        "transcript": "Yes, of course. I love weekends because it is the only time which when I can relax and spend time with my loved ones after a long week.",
        "word_count": 28,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["spend time with my loved ones", "long week"],
            "grammar_structures_used": ["relative_clauses", "causal_clauses"]
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
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Simple.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard phrases.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Natural ('loved ones'). Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q09", "video_id": "WkqJSGnsOe8",
        "part": 1,
        "question": "What do you do on weekends?",
        "transcript": "Basically, I spend weekends by watching movie or spending time with my loved ones or sometimes I prefer going out to any restaurant or cafe. And I basically do not study a lot on weekends but I study only when it is required or necessary.",
        "word_count": 45,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["required or necessary", "prefer going out"],
            "grammar_structures_used": ["compound_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["repetition"]
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
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Simple.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Repetition of 'basically'.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range. Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q10",
        "video_id": "WkqJSGnsOe8",
        "part": 1,
        "question": "Gender differences in weekends?",
        "transcript": "according to me yes people do men and women do same kind of things like watching movies or going to restaurants or pursuing their hobbies because I think it does not matter whether it is a man or woman. It is it depends on the personal interest.",
        "word_count": 47,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["pursuing their hobbies", "personal interest"],
            "grammar_structures_used": ["complex_sentences", "causal_clauses"]
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
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'It is it depends' (slip).",
                "why_not_7": "Generally error free."
            },
            "vocabulary": {
                "why_not_9": "Good but not sophisticated.",
                "why_not_7": "'Pursuing their hobbies'. Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Natural collocations ('pursuing hobbies'). Band 7.",
        "grammar_reason": "Mostly error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q11",
        "video_id": "WkqJSGnsOe8",
        "part": 1,
        "question": "Family time?",
        "transcript": "I basically spend time with my family on weekends because my both of my parents are working and I also do have a lot of work or studies to do. So we do get time to spend time on weekends. moreover we go to family dinners on weekends.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_order"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["family dinners"],
            "grammar_structures_used": ["causal_clauses", "compound_sentences"]
        },
        "micro_flaws": {
            "grammar": ["awkward_structure"],
            "vocabulary": ["repetition"]
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
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'my both of my parents' -> 'both of my parents'.",
                "why_not_7": "Good structure."
            },
            "vocabulary": {
                "why_not_9": "Repetition of 'weekends', 'time'.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Natural. Band 7.",
        "grammar_reason": "One slip ('my both of my'). Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q12",
        "video_id": "WkqJSGnsOe8",
        "part": 1,
        "question": "People like music?",
        "transcript": "Yes. I think many people love music because it enh it it boosts their energy and music is something that everybody needs in their daytoday life.",
        "word_count": 25,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["boosts their energy", "daytoday life"],
            "grammar_structures_used": ["complex_sentences"]
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
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Short.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Good collocations."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good collocations ('boosts energy'). Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q13",
        "video_id": "WkqJSGnsOe8",
        "part": 1,
        "question": "What music?",
        "transcript": "I generally listen to every kind of music but it depends upon my mood. but most often I listen to Punjabi pop music because it gives me energy and boosts me to do any work.",
        "word_count": 35,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["depends upon my mood", "boosts me"],
            "grammar_structures_used": ["complex_sentences"]
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
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Simple.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Natural. Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q14",
        "video_id": "WkqJSGnsOe8",
        "part": 1,
        "question": "Easy to learn music?",
        "transcript": "Basically it depends on personal interest because I personally love to learn music and it is a work of patient patient. It is a work that must be done patiently and with lot of practice. So it depends person to person.",
        "word_count": 40,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "mixed",
            "vocab_evidence": ["depends on personal interest", "patiently"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": ["word_choice"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'work of patient patient' (patience). 'depends person to person' (from person to person)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "controlled",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Basic errors.",
                "why_not_7": "Depends person to person -> depends on the person."
            },
            "vocabulary": {
                "why_not_9": "'patient' vs 'patience'.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range but error in word formation ('patient'). Band 7.",
        "grammar_reason": "Preposition errors ('depends person to person'). Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q15",
        "video_id": "WkqJSGnsOe8",
        "part": 1,
        "question": "Music lessons at school?",
        "transcript": "Yes. I remember I had a few music lessons at my school but I used to take personal music classes extra classes because I had a keen interest in music and I want from my childhood I wanted to enhance my music and singing skills.",
        "word_count": 45,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["keen interest", "enhance my music skills", "personal music classes"],
            "grammar_structures_used": ["complex_sentences", "past_habitual"]
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
            "complexity_level": "moderate_high",
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
                "why_not_9": "'I want from my childhood I wanted' (self correction).",
                "why_not_7": "Generally error free."
            },
            "vocabulary": {
                "why_not_9": "'keen interest'. Good.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('keen interest', 'enhance'). Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q16",
        "video_id": "WkqJSGnsOe8",
        "part": 3,
        "question": "Meeting people from different cultures?",
        "transcript": "Yes indeed it is quite easy to meet different cultural backgrounds people because India is a diverse country and people from different traditions, cultures, languages meet together and live together in big cities. Often people live and learn to live with different cultural background people in schools and colleges.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_order"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["diverse country", "traditions"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["adjective_position"],
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
            "accuracy_level": "controlled",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'different cultural background people' -> 'people from different cultural backgrounds'.",
                "why_not_7": "Good structure."
            },
            "vocabulary": {
                "why_not_9": "'diverse country' is good.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('diverse'). Band 7.",
        "grammar_reason": "Slight awkwardness in noun phrase structure. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q17",
        "video_id": "WkqJSGnsOe8",
        "part": 3,
        "question": "What do they talk about?",
        "transcript": "According to me, people talk about their languages, their food, their tradition, their way of living, their living standards and people learn from each other the way they communicate.",
        "word_count": 28,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["living standards", "way of living"],
            "grammar_structures_used": ["lists", "complex_sentences"]
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
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Simple.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('living standards'). Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q18",
        "video_id": "WkqJSGnsOe8",
        "part": 3,
        "question": "Multicultural society good?",
        "transcript": "Yes, it is really good and I really appreciate it because if we will we live with different cultural background people, we get new exposure and we get to know about the that we do not have very low boundaries. We should love to we should like to live with new people. It really enhances our living standards.",
        "word_count": 56,
        "analysis_metadata": {
            "grammar_error_patterns": ["coherence"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["new exposure", "low boundaries", "enhances our living standards"],
            "grammar_structures_used": ["conditionals", "modals"]
        },
        "micro_flaws": {
            "grammar": ["coherence_break"],
            "vocabulary": ["imprecise_phrasing"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'low boundaries' (unclear meaning). 'if we will we live' (hesitation/grammar)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Hesitations and clarity issues.",
                "why_not_7": "Generally controlled."
            },
            "vocabulary": {
                "why_not_9": "'exposure' is good. 'low boundaries' is confusing.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('exposure', 'enhances') but some confusion. Band 7.",
        "grammar_reason": "Generally good despite some hesitations. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q19",
        "video_id": "WkqJSGnsOe8",
        "part": 3,
        "question": "Example?",
        "transcript": "As I told you earlier, I went to Pune and it was a really it was a totally new city to me as I am living in Hana and it is in Maharashtra. So earlier I was really afraid and my parents were also so much afraid but with the passage of time I loved living in Pune and I give the example to my younger siblings that how can we live with different cultural people. So you mean to say that you are basically from Hana and when you visited Maharashtra it was very different to you. &gt;&gt; It was amazing experience for me.",
        "word_count": 105,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["passage of time", "totally new city"],
            "grammar_structures_used": ["complex_sentences", "past_tense"]
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
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Simple.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Natural ('passage of time'). Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q20",
        "video_id": "WkqJSGnsOe8",
        "part": 3,
        "question": "Advantages of friends from diff cultures?",
        "transcript": "&gt;&gt; it has so many advantages and disadvantages too. I think we like we learn to live according to those people and we learn new things. We learn their culture. We learn to respect people and give harmony towards our society. &gt;&gt; Mhm.",
        "word_count": 42,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["give harmony", "advantages and disadvantages"],
            "grammar_structures_used": ["compound_sentences"]
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
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Simple.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "'harmony' is a good word."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('harmony'). Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q21",
        "video_id": "WkqJSGnsOe8",
        "part": 3,
        "question": "Why live abroad?",
        "transcript": "I think people choose to travel abroad because some of the people I know they have keen interest for exploring new countries and cities &gt;&gt; and some people go to abroad for their further studies because of good and advanced studies.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["keen interest", "exploring new countries", "advanced studies"],
            "grammar_structures_used": ["complex_sentences", "causal_clauses"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["repetition"]
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
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Simple.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'go to abroad' -> 'go abroad'.",
                "why_not_7": "'keen interest' is good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('keen interest') but 'go to abroad' error. Band 7.",
        "grammar_reason": "Error free structure. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },

    # Video: o9_Qsvc2QP4 (Band 4.5)
    {
        "id": 0, "sample_id": "o9_Qsvc2QP4_q02", "video_id": "o9_Qsvc2QP4",
        "part": 1,
        "question": "Place of living / Scenery?",
        "transcript": "Mean the place of your living and your job are they close to each other yes I work in a smaller Refinery and my my my apartment my house is about 50 minutes away from my working place and and we have a service they they pick us and you know and take a take us to walk and this is a kind of easy road to you know get to work and to come back home so you have kind of service we have a service for 50 minutes it takes yes it takes almost 15 minutes I have been talking about your place of living is it important for you the view of the window that you might see out of the window or not I mean scenery yes yes I think it is you know sometimes you feel nervous sometimes you feel like you know angry and it is good to you know to have a to have a point to have a view sorry to have a view that you know it is it is kind of make you make you relax it is going to make you feel you know it is take away your anxious take away take away your stress and yes where I live it is it has got a really good view and it is like a park almost and sometimes I go and walk her there with my wife and I feel really good being there okay talking about family you are married yeah yes I am married very good so any children no okay so in the future you will have I have I hope so I hope so okay thank you very much so this is going to be a.",
        "word_count": 272,
        "analysis_metadata": {
            "grammar_error_patterns": ["basic_sentence_structure", "word_order"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["take away your anxious", "smaller refinery", "service"],
            "grammar_structures_used": ["simple_sentences", "fragments"]
        },
        "micro_flaws": {
            "grammar": ["repetition_stutter"],
            "vocabulary": ["wrong_word_form"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'take away your anxious' (anxiety). Frequent pauses/fillers. 'walk her there' (?)."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "long_but_disorganized",
            "redundancy": "high",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Frequent basic errors, stuttering, and self-correction. 'it is kind of make you make you relax'.",
                "why_not_3": "Can convey meaning."
            },
            "vocabulary": {
                "why_not_5": "Limited. 'Anxious' used as noun.",
                "why_not_3": "Sufficient for basic topics."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Uses a very limited range of structures with rare use of subordinate clauses.",
            "vocabulary_band": 4,
            "vocabulary_text": "Uses a limited range of vocabulary, but this is minimally adequate for the task."
        },
        "vocab_reason": "Basic and often incorrect forms ('anxious' for 'anxiety'). Band 4.",
        "grammar_reason": "Frequent errors and breakdown in fluency/structure. Band 4.",
        "vocabulary": 4,
        "grammar": 4
    }
]

# Write to file (checking for duplicates)
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
            if sample['sample_id'] not in existing_ids:
                f.write(json.dumps(sample) + '\n')
                count += 1

    print(f"Append complete. Added {count} new samples. (Skipped {len(scored_samples) - count} duplicates).")

except Exception as e:
    print(f"Error writing to file: {e}")
