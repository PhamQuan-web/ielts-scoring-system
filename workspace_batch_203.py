import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 203 ---
# Total Samples: 20
# Valid Scored: 16
# Skipped: 4 (Reasons below)

# --- SKIPPED SAMPLES LOG ---
# 1. iGvQIFr8npI_q14: Examiner Feedback ("She tried to use passive sentences... So this is advisable") - Not candidate speech.
# 2. WkqJSGnsOe8_q01: Intro/Identity Check ("Yeah, sure. Here it is. Oh, thank you. Mandi.") - Not a scorable answer.
# 3. WkqJSGnsOe8_q03: Transition/Instruction ("Now, a few questions will be based on jewelry.") - Examiner instruction included in transcript.
# 4. GVS7fufibLY_q02: Fragment/Incoherent ("Which I would hopefully achieve are you a kind of person...") - Merged/Bad cut.

# --- VALID SAMPLES DATA ---
scored_samples = [
    # Video: iGvQIFr8npI (Band 7.0)
    {
        "id": 0, "sample_id": "iGvQIFr8npI_q02", "video_id": "iGvQIFr8npI", "part": 1,
        "question": "Where do you live?",
        "transcript": "I hear from Tahana. It is a small but elegant town which is located in the northern part of India. That place is full of amenities.",
        "word_count": 25,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["elegant town", "located in", "full of amenities"],
            "grammar_structures_used": ["relative_clauses"]
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
                "why_not_9": "Too short/simple.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Good but not sophisticated.",
                "why_not_7": "'Elegant', 'amenities'. Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary to allow some flexibility and precision."
        },
        "vocab_reason": "Precise vocabulary ('amenities', 'elegant'). Band 7.",
        "grammar_reason": "Error free relative clause. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "iGvQIFr8npI_q03", "video_id": "iGvQIFr8npI",
        "part": 1,
        "question": "Do you study or work?",
        "transcript": "I do not work and I am still a student. I have completed my Bachelor of Commerce and I am looking forward for my further education. Now some questions will be based on dreams.",
        "word_count": 35,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["Bachelor of Commerce", "further education"],
            "grammar_structures_used": ["present_perfect", "continuous"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
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
            "accuracy_level": "controlled",
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
                "why_not_9": "'looking forward for' -> 'looking forward to'.",
                "why_not_7": "Generally error free."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Functional."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 6,
            "vocabulary_text": "Has a wide enough vocabulary to discuss topics."
        },
        "vocab_reason": "Functional vocabulary. Band 6.",
        "grammar_reason": "Good structure but preposition error ('for' vs 'to'). Band 7.",
        "vocabulary": 6,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "iGvQIFr8npI_q04", "video_id": "iGvQIFr8npI",
        "part": 1,
        "question": "Do you remember your dreams?",
        "transcript": "Not really but some time people dreams reveals the thoughts and feelings of them beside this you consider that it is the random brain activity of our mind during sleep but I personally feel that is the thing what is going on in our mind so you do not often remember your dreams ok do you think dreams have any meaning I do not think so every dream has a meaning but when we see the dream from the open eyes it could be fulfilled and realistic. Apart from it when we see the dream from the subconscious mind it it could not be optimistic or realistic in our real life and that could not be complete for the further life. Ok.",
        "word_count": 128,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "article_usage"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "mixed",
            "vocab_evidence": ["random brain activity", "subconscious mind", "optimistic", "realistic"],
            "grammar_structures_used": ["complex_sentences", "passive_voice"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement"],
            "vocabulary": ["imprecise_phrasing"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'people dreams reveals' (agreement). 'open eyes' (awake?). 'complete for the further life' (unclear)."
        },
        "grammar_profile": {
            "complexity_level": "moderate_high",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Frequent basic errors.",
                "why_not_7": "Some complex structures but frequent errors."
            },
            "vocabulary": {
                "why_not_9": "Imprecise.",
                "why_not_7": "Good range ('subconscious', 'optimistic') but some confusion."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar and punctuation but they rarely reduce communication.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary to allow some flexibility and precision."
        },
        "vocab_reason": "Good range ('subconscious', 'brain activity') despite some awkwardness. Band 7.",
        "grammar_reason": "Frequent agreement errors ('people dreams reveals'). Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "iGvQIFr8npI_q05", "video_id": "iGvQIFr8npI",
        "part": 1,
        "question": "Talking about dreams?",
        "transcript": "I have seen many dreams which could be fulfilled and not but recently I saw a dream I became a teacher in my dream we ok do you like talking about your dreams with others from my perspective I do not like to talk about my dreams with others because I think that it should be kept secret and private but some time I think we should discuss it with others because we can get different opinions and thoughts from our homies and friends and family also. Ok good. So Nikita, next few questions will be based on cooking.",
        "word_count": 105,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["from my perspective", "kept secret and private", "homies"],
            "grammar_structures_used": ["complex_sentences", "modals"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["slang_usage"]
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
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Simple.",
                "why_not_7": "Generally error free."
            },
            "vocabulary": {
                "why_not_9": "'homies' is slang, maybe inappropriate for exam.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range, 'homies' is interesting/natural if informal. Band 7.",
        "grammar_reason": "Mostly error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "iGvQIFr8npI_q06", "video_id": "iGvQIFr8npI",
        "part": 1,
        "question": "Do you like cooking?",
        "transcript": "Definitely I am a foodie person. I love to cook and eat distinct kinds of dishes at home and I like to make beverages also. I have different kinds of knowledge about different foods like continental Thai and Japanese also. We are ok.",
        "word_count": 45,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["foodie person", "distinct kinds", "beverages", "continental"],
            "grammar_structures_used": ["simple_sentences", "lists"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["redundancy"]
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
                "why_not_9": "'foodie person' (redundant - just foodie).",
                "why_not_7": "Good range ('distinct', 'beverages')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('distinct', 'beverages'). Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "iGvQIFr8npI_q07", "video_id": "iGvQIFr8npI",
        "part": 1,
        "question": "How often do you cook?",
        "transcript": "it is not a random activity for me because I personally mention it because I am a food holic and I love to cook at home with my mommy and I always made distinct kind of dishes like vegetables, noodles, pizza and pasta also.",
        "word_count": 47,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "mixed",
            "vocab_evidence": ["food holic", "random activity", "distinct kind"],
            "grammar_structures_used": ["causal_clauses"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": ["word_formation_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'food holic' (workaholic -> foodaholic? or foodie). 'personally mention it' (weird context). 'always made' (tense)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
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
                "why_not_9": "'I always made' -> 'make'.",
                "why_not_7": "Basic error."
            },
            "vocabulary": {
                "why_not_9": "'food holic'.",
                "why_not_7": "'random activity' is good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "'Food holic' is creative but incorrect. Band 6.",
        "grammar_reason": "Tense error 'always made'. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "iGvQIFr8npI_q08",
        "video_id": "iGvQIFr8npI",
        "part": 1,
        "question": "Eating out vs home?",
        "transcript": "it totally depends on my mode whenever I am at my home then I cook with my mother for making different dishes for my relatives and family members also I always make breakfast and lunch everyday oh great now your questions will be based on technology how often do you use technology in your daily life in my daily life I use different kinds of electrical appliances like mobile phone, computer, microwave and so on. But I personally use only mobile phone for using different kinds of applications like Lindin, Twitter, WhatsApp and Instagram also. But I Think That Instagram is the Famous App Today's Generation Because Every People Can Upload Their Talent Video on Social Apps and Get a Name and Swimming. So you mean to say that every person can upload his and her talent and whatever he and she wants. Yes ok.",
        "word_count": 149,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["depends on my mode", "electrical appliances", "upload their talent"],
            "grammar_structures_used": ["complex_sentences", "connectives"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'depends on my mode' (mood?). 'Get a Name and Swimming' (Transcription error? or nonsense? Likely 'Name and Fame'). 'Every People' (Every person)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'Every People' -> 'Every person'.",
                "why_not_7": "Basic errors."
            },
            "vocabulary": {
                "why_not_9": "'Mode' vs 'Mood'.",
                "why_not_7": "Good range ('appliances', 'upload')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "'Mode' instead of 'mood'. 'Every people'. Band 6.",
        "grammar_reason": "Agreement errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "iGvQIFr8npI_q09",
        "video_id": "iGvQIFr8npI",
        "part": 1,
        "question": "What technology do you use?",
        "transcript": "I usually use the most mobile phones and computers. If I Talk About the Computer We Can Make Our Assignment and Project by Electrically. And we can also use our mobile phone for learning different kinds of things like cooking, singing. And we can also learn different languages ​​like Spanish, Japanese, Chinese and others also. Ok?",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["make our assignment", "electrically"],
            "grammar_structures_used": ["conditionals"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Project by Electrically' (completely wrong - electronically? digitally?). 'use the most mobile phones' (word order)."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Basic errors.",
                "why_not_7": "Errors impede meaning ('by electrically')."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Wrong word choice."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "'Electrically' is wrong. Band 6.",
        "grammar_reason": "Word order and form errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "iGvQIFr8npI_q10",
        "video_id": "iGvQIFr8npI",
        "part": 3,
        "question": "Does technology make life easier?",
        "transcript": "Definitely technology has made our life easier and convenient also. Because we can do our work without any physical efforts and we are totally dependent on it. And in a minimum time we can do different tasks at home. Like we can wash our clothes. Childo members making audio",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["convenient", "physical efforts", "totally dependent", "minimum time"],
            "grammar_structures_used": ["complex_sentences", "passive_implied"]
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
                "why_not_9": "Good but standard.",
                "why_not_7": "Good range ('dependent', 'convenient')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('physical efforts'). Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "iGvQIFr8npI_q11",
        "video_id": "iGvQIFr8npI",
        "part": 3,
        "question": "Disadvantages of technology?",
        "transcript": "Absolutely there are plenty of disadvantages. Firstly, people do not put their physical efforts on every work. They are depriving themselves from physical efforts and from outdoor activities and they can also become sluggish and they can get different kinds of chronic diseases. Ok.",
        "word_count": 41,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["plenty of disadvantages", "depriving themselves", "sluggish", "chronic diseases"],
            "grammar_structures_used": ["complex_sentences", "reflexive_pronouns"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
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
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'Depriving themselves', 'sluggish', 'chronic diseases'. Very strong.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent vocabulary ('sluggish', 'chronic diseases', 'depriving'). Band 9.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "iGvQIFr8npI_q12",
        "video_id": "iGvQIFr8npI",
        "part": 3,
        "question": "Modern vs Traditional buildings?",
        "transcript": "Traditional buildings and the modern buildings are quite different from each other. because modern buildings come with the different amenities. And if I talk about the traditional once we can preserve our culture and heritage and modern and the modern development always brings a lot of benefits firstly the economy can be boosted and the different sources of employment could be generated. Ok.",
        "word_count": 59,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["culture and heritage", "economy can be boosted", "sources of employment", "amenities"],
            "grammar_structures_used": ["passive_voice", "conditionals"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
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
                "why_not_9": "Good control of passive.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'boosted', 'generated', 'amenities'. Precise.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Precise ('boosted', 'amenities', 'heritage'). Band 8.",
        "grammar_reason": "Error free and complex. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "iGvQIFr8npI_q13",
        "video_id": "iGvQIFr8npI",
        "part": 3,
        "question": "Government investment in architecture?",
        "transcript": "According to my own perception spending money on the modern architecture of a building could not be a good thing but we should and the government also spend money on the traditional buildings also because it is a good thing for all people because in the upcoming generation children can get more information about the different buildings and the ancestors also how they operate the people in an efficient manner to give them the money and the employment sources in different things. Ok.",
        "word_count": 82,
        "analysis_metadata": {
            "grammar_error_patterns": ["coherence"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["perception", "modern architecture", "upcoming generation", "efficient manner"],
            "grammar_structures_used": ["complex_sentences", "modals"]
        },
        "micro_flaws": {
            "grammar": ["run_on_sentence"],
            "vocabulary": ["imprecise_phrasing"]
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
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Sentence becomes rambling/unclear at the end ('operate the people in an efficient manner').",
                "why_not_7": "Good range but some loss of control."
            },
            "vocabulary": {
                "why_not_9": "Good words ('perception', 'efficient') but confused meaning.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('perception', 'efficient'). Band 7.",
        "grammar_reason": "Complex but loses coherence at the end. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },

    # Video: GVS7fufibLY (Band 7.0)
    {
        "id": 0, "sample_id": "GVS7fufibLY_q03", "video_id": "GVS7fufibLY",
        "part": 1,
        "question": "Favorite City?",
        "transcript": "Chandigar is a masterpie is a masterpiece out of waste material and sukna Lake which is the largest man-made lake in the chandigar and it is famous for the Smoke free city in the country and it is also famous for cleanliness and the happiest city in the country there are many Masterpiece Gardens Lakes Hills and art galleries museums in chandigar and architecture building as I early mentioned about Capital complex great so explain why this is your favorite City I visit to this city that is why I this is my favorite city and there are many things things like Gardens and it is very clean City okay so because of gardens because of greenery and cleanness you like I love nature",
        "word_count": 119,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_usage", "preposition_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["man-made lake", "smoke free city", "art galleries", "architecture"],
            "grammar_structures_used": ["relative_clauses", "passive_voice"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
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
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'visit to this city' -> 'visit this city'. 'in the chandigar' -> 'in Chandigarh'.",
                "why_not_7": "Generally controlled."
            },
            "vocabulary": {
                "why_not_9": "'Masterpiece' used repetitively/incorrectly (Masterpiece Gardens?).",
                "why_not_7": "Good topic vocab."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good topic words ('man-made', 'smoke free') but 'masterpiece' misused. Band 7.",
        "grammar_reason": "Preposition and article errors. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },

    # Video: WkqJSGnsOe8 (Band 7.5)
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q02", "video_id": "WkqJSGnsOe8",
        "part": 1,
        "question": "Where do you live?",
        "transcript": "&gt;&gt; I live in a small town named Toana. It is located in northern part of my country, India.",
        "word_count": 18,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["located in", "small town"],
            "grammar_structures_used": ["passive_voice"]
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
                "why_not_7": "Too simple/short.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
                "why_not_5": "Accurate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 6,
            "vocabulary_text": "Has a wide enough vocabulary."
        },
        "vocab_reason": "Basic. Band 6.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 6,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q04", "video_id": "WkqJSGnsOe8",
        "part": 1,
        "question": "Do you wear jewelry?",
        "transcript": "&gt;&gt; Yes, indeed. I love to wear jewelry because it enhances my look and I really look good because people and my loved one really appreciate me whenever I wear jewelry. and it also suits with every clothes I wear. &gt;&gt; Mhm.",
        "word_count": 42,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["enhances my look", "appreciate", "suits"],
            "grammar_structures_used": ["complex_sentences", "causal_clauses"]
        },
        "micro_flaws": {
            "grammar": ["plural_error"],
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
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'suits with every clothes' -> 'suits every outfit'. 'every clothes' is wrong.",
                "why_not_7": "Good structure."
            },
            "vocabulary": {
                "why_not_9": "'enhances my look' is good.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('enhances'). Band 7.",
        "grammar_reason": "Mostly error free, slight error with 'every clothes'. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "WkqJSGnsOe8_q05", "video_id": "WkqJSGnsOe8",
        "part": 1,
        "question": "What type of jewelry?",
        "transcript": "&gt;&gt; Basically, I love to wear golden jewelry because I think golden jewelry is my type because it really suits me and u gives me confidence too.",
        "word_count": 27,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["gives me confidence", "suits me", "my type"],
            "grammar_structures_used": ["causal_clauses"]
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
        "vocab_reason": "Natural ('gives me confidence'). Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
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
