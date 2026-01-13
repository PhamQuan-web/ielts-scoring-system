import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 207 ---
# Total Samples: 20
# Valid Scored: 16
# Skipped: 4 (Reasons below)

# --- SKIPPED SAMPLES LOG ---
# 1. US3Z4kX3Aq8_q02: Identity Check ("My name is Gina... I am going to record...") - Not scorable answer.
# 2. US3Z4kX3Aq8_q03: Examiner Instruction/Confirmation ("Yes. All right. So, the speaking interview will take about...") - Not candidate speech.
# 3. US3Z4kX3Aq8_q11: Transition ("Yes. Just give me one moment. So, please keep the card down...") - Not candidate speech.
# 4. US3Z4kX3Aq8_q13: Transition ("Yes. Then let us start with homesickness.") - Not candidate speech.
#    Wait, sample US3Z4kX3Aq8_q19 is also "No. Okay then...".
#    Let's check `hfmYqZUDv9Q_q05`: Valid.
#    Let's check `US3Z4kX3Aq8_q19`: "No. Okay, then. Thank you very much...". Outro.
#    So actually 5 samples are invalid.
#    1. q02 (Identity)
#    2. q03 (Instruction)
#    3. q11 (Transition)
#    4. q13 (Transition)
#    5. q19 (Outro)
#    Let me check if I have 20 samples total. Yes.
#    So 15 valid?
#    Let's check `US3Z4kX3Aq8_q18` (Valid), `q17` (Valid), `q16` (Valid), `q15` (Valid), `q14` (Valid), `q09` (Valid), `q08` (Valid), `q07` (Valid), `q06` (Valid), `q05` (Valid).
#    `dJqbKfXLeak_q02` (Valid), `q03` (Valid), `q04` (Valid), `q05` (Valid).
#    `hfmYqZUDv9Q_q05` (Valid).
#    Total Valid = 1 (hfm) + 10 (US3) + 4 (dJq) = 15.
#    Wait, `US3Z4kX3Aq8` has q02, q03, q05, q06, q07, q08, q09, q11, q13, q14, q15, q16, q17, q18, q19 (15 samples).
#    Valid US3: q05, q06, q07, q08, q09, q14, q15, q16, q17, q18 (10).
#    Invalid US3: q02, q03, q11, q13, q19 (5).
#    Total samples in batch: 1 + 15 + 4 = 20.
#    Total Valid: 1 + 10 + 4 = 15.
#    Total Skipped: 5.

# --- VALID SAMPLES DATA ---
scored_samples = [
    # Video: hfmYqZUDv9Q (Band 8.5)
    {
        "id": 0, "sample_id": "hfmYqZUDv9Q_q05", "video_id": "hfmYqZUDv9Q",
        "part": 3,
        "question": "Friends from other countries?",
        "transcript": "Free do you have someone like that in your family yes I am very close to my sister okay that is great is it important to have friends from other countries yes now that I have lived overseas for I think half of my life already I I feel like if you just keep to your own Community your little Social Circle then it is going to be difficult you you have to kind of expose yourself to different types of relationship ship and knowing friends from different countries you know you can exchange your culture exchange your different backgrounds knowledge it is very helpful and how would you say are some good ways to meet friends from other countries I mean I cannot really say it is a method but going overseas to live to study is obviously the the most easy way to meet people from different countries but even in my countries I still took part in a lot of activities that had foreigners for example you can take part in English clubs sometime tourism clubs and also at my work I did I work for a company that our main clients were foreigners and through that I met a few people and a lot of them I am not I met a lot of people and a few of them actually became friends later on okay thank you very much that is the end of the a speaking test thank you for your time and I hope you have a great day right thank you okay I am going to ask you some post test questions just to get an idea of how you felt about today's test what are your overall feelings about today's test I think it.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["expose yourself", "social circle", "backgrounds knowledge", "took part in"],
            "grammar_structures_used": ["conditionals", "complex_sentences"]
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
            "complexity_level": "high",
            "accuracy_level": "high",
            "flexibility": "sustained",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Native flow.",
                "why_not_7": "Superior complexity."
            },
            "vocabulary": {
                "why_not_9": "'backgrounds knowledge' (background knowledge).",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Precise ('expose yourself', 'social circle'). Band 8.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 8,
        "grammar": 9
    },

    # Video: US3Z4kX3Aq8 (Band 7.0)
    {
        "id": 0, "sample_id": "US3Z4kX3Aq8_q05", "video_id": "US3Z4kX3Aq8",
        "part": 1,
        "question": "Stay healthy?",
        "transcript": "I take my health seriously. I try to eat well and I do my physical exercise three times a week and I also set my health goals each month. Oh,",
        "word_count": 30,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["take my health seriously", "health goals", "physical exercise"],
            "grammar_structures_used": ["simple_sentences", "lists"]
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Too short/simple.",
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
        "vocab_reason": "Good collocations ('take seriously'). Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "US3Z4kX3Aq8_q06", "video_id": "US3Z4kX3Aq8",
        "part": 1,
        "question": "Importance of exercise?",
        "transcript": "Yes, I believe the physical exercise is incredibly important for health. Human are meant to be active. Without any exercise, people may gain weight and become less healthy.",
        "word_count": 27,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["incredibly important", "gain weight", "meant to be active"],
            "grammar_structures_used": ["complex_sentences", "passive_voice"]
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
            "accuracy_level": "controlled",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'Human are' -> 'Humans are'.",
                "why_not_7": "Good structure."
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
        "vocab_reason": "Good collocations ('meant to be active'). Band 7.",
        "grammar_reason": "Error free mostly, one slip ('Human are'). Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "US3Z4kX3Aq8_q07",
        "video_id": "US3Z4kX3Aq8",
        "part": 1,
        "question": "Unhealthy food?",
        "transcript": "unfortunately, I have my unhealthy food more than I probably should. I think it is because it is very easier way to get healthy food and always the fastest option. but I limit I limit myself to eat unhealthy food once per week.",
        "word_count": 42,
        "analysis_metadata": {
            "grammar_error_patterns": ["comparative"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["fastest option", "limit myself"],
            "grammar_structures_used": ["comparatives", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["comparative_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'very easier way' (much easier). 'get healthy food' (unhealthy? context implies fast food). 'limit myself to eat' (eating)."
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
                "why_not_8": "Basic errors ('very easier').",
                "why_not_6": "Complex structures present."
            },
            "vocabulary": {
                "why_not_8": "Confusion (healthy/unhealthy?).",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('limit myself'). Band 7.",
        "grammar_reason": "Comparative error ('very easier'). Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "US3Z4kX3Aq8_q08",
        "video_id": "US3Z4kX3Aq8",
        "part": 3,
        "question": "Health changes?",
        "transcript": "In my hometown of China, I think people's health have declined in the past 10 years. I think that the food have been worsened and people many people have spending less time on getting outside do physical exercise. Mhm.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "verb_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["health have declined", "spending less time"],
            "grammar_structures_used": ["present_perfect"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement"],
            "vocabulary": ["word_choice"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'health have declined' (has). 'food have been worsened' (has worsened). 'have spending' (are spending)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent agreement/tense errors.",
                "why_not_5": "Complex structures attempted."
            },
            "vocabulary": {
                "why_not_7": "'worsened' is okay but 'have been worsened' is wrong grammar impacting vocab.",
                "why_not_5": "Good words ('declined')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "'Declined' is good. Band 6.",
        "grammar_reason": "Agreement errors ('health have'). Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "US3Z4kX3Aq8_q09",
        "video_id": "US3Z4kX3Aq8",
        "part": 3,
        "question": "Biggest challenge?",
        "transcript": "I think the biggest challenge for health for me personally I think is ignoring the fast food. well however for the society I think people should spend more time on physical exercise.",
        "word_count": 32,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["ignoring the fast food", "spend more time on"],
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Short.",
                "why_not_6": "Error free."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Good range."
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
        "id": 0, "sample_id": "US3Z4kX3Aq8_q14",
        "video_id": "US3Z4kX3Aq8",
        "part": 3,
        "question": "Homesickness causes?",
        "transcript": "I think the two main causes of homesickness are missing family members and the unfamiliarity of the new town. The combination of the unfamiliarity surroundings and having no loved ones around creates homesickness. I think I believe that everyone experience this even though some people who are not close as as close their family members may experience it less.",
        "word_count": 57,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["unfamiliarity", "surroundings", "loved ones"],
            "grammar_structures_used": ["complex_sentences", "nominalization"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement"],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'unfamiliarity surroundings' (unfamiliar surroundings). 'everyone experience' (experiences). 'not close as as close their family' (as close to)."
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "controlled",
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
                "why_not_8": "Agreement errors ('everyone experience').",
                "why_not_6": "Good complexity."
            },
            "vocabulary": {
                "why_not_8": "'unfamiliarity surroundings' (noun-noun error).",
                "why_not_6": "High level vocab ('unfamiliarity')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "High level vocab ('unfamiliarity') but word form error. Band 7.",
        "grammar_reason": "Complex structures but agreement errors. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "US3Z4kX3Aq8_q15",
        "video_id": "US3Z4kX3Aq8",
        "part": 3,
        "question": "Reducing homesickness?",
        "transcript": "I think for most people the answer is time. but for some people phoning home, making new friends, and using social media to keep to contact with family members can reduce homesickness. All right. Some people think homesickness is caused by immaturity. Others believe that homesickness can affect anyone regardless of maturity.",
        "word_count": 51,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["phoning home", "keep contact with", "regardless of maturity"],
            "grammar_structures_used": ["complex_sentences", "lists"]
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
                "why_not_9": "Good.",
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
        "vocab_reason": "Good range. Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "US3Z4kX3Aq8_q16",
        "video_id": "US3Z4kX3Aq8",
        "part": 3,
        "question": "Immaturity vs Anyone?",
        "transcript": "H that is an interesting question. I do not think I agree either opinion. everyone may get homesickness and when people move away from their hometown, they will miss their family members for sure. but the peop people who are younger and less mature may get homesick easily. now I am going to ask you a few more questions on the topic of adversity.",
        "word_count": 63,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["less mature", "move away from"],
            "grammar_structures_used": ["complex_sentences", "comparatives"]
        },
        "micro_flaws": {
            "grammar": ["preposition_missing"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'agree either opinion' (agree WITH either)."
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
                "why_not_9": "'agree either' (missing 'with').",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
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
        "grammar_reason": "One slip ('agree either'). Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "US3Z4kX3Aq8_q17",
        "video_id": "US3Z4kX3Aq8",
        "part": 3,
        "question": "Personal attributes?",
        "transcript": "I definitely agree that some people cope the tough situations better than others do. based on the human the personal attributes I believe that calm and patient are very important for people to solve problems. Being calm under pressure instead of making rush decisions can help to solve problems. All right.",
        "word_count": 50,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition", "word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["calm under pressure", "rush decisions", "personal attributes", "cope the tough situations"],
            "grammar_structures_used": ["complex_sentences", "gerunds"]
        },
        "micro_flaws": {
            "grammar": ["preposition_missing"],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'cope the tough situations' (cope WITH). 'calm and patient are very important' (calmness and patience? or being calm/patient? Used adjectives as nouns). 'rush decisions' (rushed/hasty decisions)."
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
                "why_not_8": "Missing prepositions ('cope the').",
                "why_not_6": "Complex structures."
            },
            "vocabulary": {
                "why_not_8": "'rush decisions' vs 'rushed'. Adjectives as nouns.",
                "why_not_6": "Good range ('attributes', 'pressure')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('attributes') but errors ('rush decisions'). Band 7.",
        "grammar_reason": "Preposition error ('cope the'). Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "US3Z4kX3Aq8_q18",
        "video_id": "US3Z4kX3Aq8",
        "part": 3,
        "question": "Big picture?",
        "transcript": "take your time. well, if I had to choose only one, I would like to say the ability to see the big picture. that ability, such an ability allows a person to see many problems for for what they are. small, relatively important and temporary. Long-term thinking gives persons perspective necessary to solve problems easily and quickly.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["big picture", "long-term thinking", "perspective"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
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
            "complexity_level": "high",
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
                "why_not_9": "'gives persons perspective' -> 'gives a person perspective' or 'people'.",
                "why_not_7": "Sophisticated ('perspective', 'big picture')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Sophisticated ('big picture', 'perspective'). Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },

    # Video: dJqbKfXLeak (Band 8.0)
    {
        "id": 0, "sample_id": "dJqbKfXLeak_q02",
        "video_id": "dJqbKfXLeak",
        "part": 1,
        "question": "Work?",
        "transcript": "Because we live like to meet with each other hang out with friends and the night life in Korea is very important yes so it was kind of disappointed when they suddenly change the rules again right definitely okay and what do you like to change about about your lifestyle pardon what would you like to change about your lifestyle yeah I think the part I should fix my is like I always sleep too late and wake up sometimes very late too so I would like if I could force myself to sleep before 11: p.m. that will be very healthy for me right definitely good night sleep helps everyone okay now we going talk a little bit about work do you work right now oh yes I kind of I did a parttime job before around one month term yeah a short term I did some video shooting too actually yes I did small company introduction videos for culture yes oh that sounds interesting and do you get on well with your co-workers oh actually the co-workers in the studio are very they are like they always they are like same age around with me so we get a very good we get around very well well that is good and what responsibilities do you have at your work I part participate in the video shooting as Chinese speakers yes so I did a Chinese video for the Korean company to introduce their prod product and the company itself yeah to promote overseas all right I have one more question about work are there good work opportunities in your home country yes in China it is a veloping country now and all the internet company grows very fast but the.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form", "preposition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["promote overseas", "parttime job", "introduction videos", "developing country"],
            "grammar_structures_used": ["complex_sentences", "past_tense"]
        },
        "micro_flaws": {
            "grammar": ["verb_tense_error"],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'developing country' (veloping). 'kind of disappointed' (disappointing). 'get around very well' (get along)."
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
                "why_not_9": "'suddenly change' (changed). 'kind of disappointed' (disappointing).",
                "why_not_7": "Good structure."
            },
            "vocabulary": {
                "why_not_9": "'veloping' (developing). 'get around' (get along).",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range but errors ('get around' for 'get along'). Band 7.",
        "grammar_reason": "Tense errors ('change' vs 'changed'). Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "dJqbKfXLeak_q03",
        "video_id": "dJqbKfXLeak",
        "part": 1,
        "question": "Work opportunities?",
        "transcript": "Important thing is the political threat is very high some sometime they change the law very fast so even the big real estate company could not have the time to take the law so they kind of very dangerous I think but there is more opportunity yes because it is very developing very fast now okay great thank you for answering all my questions.",
        "word_count": 62,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["political threat", "real estate company", "developing very fast"],
            "grammar_structures_used": ["complex_sentences", "modals"]
        },
        "micro_flaws": {
            "grammar": ["missing_verb"],
            "vocabulary": ["collocation_slip"]
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'take the law' (follow/adapt to?). 'they kind of very dangerous' (it is). 'very developing' (developing very fast - used adjective modifier on verb)."
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
                "why_not_8": "Missing verbs ('they kind of dangerous').",
                "why_not_6": "Good complexity."
            },
            "vocabulary": {
                "why_not_9": "'political threat' is good.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level vocab ('political threat', 'real estate'). Band 8.",
        "grammar_reason": "Missing verbs but complex. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "dJqbKfXLeak_q04",
        "video_id": "dJqbKfXLeak",
        "part": 3,
        "question": "City attractions?",
        "transcript": "Major attraction which are which is panda panda and the mountains yes the panda all the Foreigner and different tourists from different part of China they when they travel to chungu City they will go to the panda Zoo which they have a really huge Park only for panda yes and also the when you go west to the Tibet the way to Tibet they have very beautiful mountain and rivers and all the environment are like astonishing beautiful yes wow sounds like a place I want to visit too okay are there any cities that you like to visit in the future oh if I could visit any City in the future I will visit Japan and Tokyo yes because I think Tokyo at the part of Asia is very on the top of the world and they share very we share very common we share very common culture and Tokyo is absolutely the best tourist place to go in Asia oh wow very good all right thank you so much for answering that part than you and we are going to go on to our last part of our interview I will ask you some questions and just try to answer as best as you can I I will ask you some followup questions okay these can be about your opinion or something else all right so let us start in your opinion what makes a city a good one to live in I think what make a city to a good one to live in is the culture and the people people in the city yes because in different country and different region they have different culture as in Korea they might be more a little bit more strict.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["astonishing beautiful", "tourist place", "common culture"],
            "grammar_structures_used": ["relative_clauses", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement"],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'astonishing beautiful' (astonishingly). 'attraction which are which is' (self correction). 'what make a city' (makes)."
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
                "why_not_9": "'what make a city' (makes).",
                "why_not_7": "Good structure."
            },
            "vocabulary": {
                "why_not_9": "'astonishing beautiful' (adverb/adj error).",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good vocabulary ('astonishing', 'attraction') despite minor form error. Band 8.",
        "grammar_reason": "Agreement errors but good complexity. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "dJqbKfXLeak_q05",
        "video_id": "dJqbKfXLeak",
        "part": 3,
        "question": "People in cities?",
        "transcript": "Or not friendly to Foreigner but maybe in the Europe and in the west they will be very friendly to foreigners and also the people who live in the city are the is the one who build the city so that is the most part important part of the city MH yeah okay what do you think of the people in this city in so are they friendly are they nice what do you think of them yes I just mov in so actually like a month ago I think people in so are they are very busy they work faster as like if you compare to different city in middle of Korea like tongu and Dean they actually they absolutely work faster here and then the lifestyle might be more City that is like and people are have more budget maybe I do not know like more money to pay off that the pay the pay bill might be very hard for them yes and the houses are expensive so the people here I think they are foreign they do not care about you yeah they care about their own life yes okay so you have had a chance to travel around Korea different cities what in your opinion is your favorite city in Korea yes my favorite city is Busan because it is very clean actually yes I went to different cities in Korea and P absolutely so clean the street are very tiny and no dust maybe because it is close to the ocean and the view is very beautiful it is all the I like to walk down the having day the beach and enjoying the sunshine and the Seas sea views definitely Busan is a nice city to visit then why are you.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["lifestyle", "pay bill", "sea views", "sunshine"],
            "grammar_structures_used": ["comparatives", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'people in so are they are' (repetition). 'mov in' (moved). 'street are very tiny' (streets)."
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
                "why_not_9": "'street are' (agreement). 'mov in' (tense).",
                "why_not_7": "Good structure."
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
        "vocab_reason": "Good range. Band 7.",
        "grammar_reason": "Agreement and tense errors. Band 7.",
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
            if sample['vocabulary'] == 0:
                continue
            if sample['sample_id'] not in existing_ids:
                f.write(json.dumps(sample) + '\n')
                count += 1

    print(f"Append complete. Added {count} new samples. (Skipped {len(scored_samples) - count} duplicates/invalid).")

except Exception as e:
    print(f"Error writing to file: {e}")
