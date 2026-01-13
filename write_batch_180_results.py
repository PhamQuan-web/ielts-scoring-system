import json

output_file = "jules_scored_output_151-200.jsonl"

samples = [
    {
        "id": 1,
        "sample_id": "caKKsV4CkWA_q18",
        "video_id": "caKKsV4CkWA",
        "part": 3,
        "question": "And how do you think this is possible?",
        "transcript": "Because, as I mentioned before, there are many materials out there, and, children, have to choose one or two of them. And they follow their peers, they follow the culture of the, school, and, so the role of teacher would be to, recommend useful. And, maybe they have to make some, new materials for their, children and students.",
        "word_count": 59,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_error", "phrase_structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["materials out there", "follow their peers", "role of teacher"],
            "grammar_structures_used": ["modal_would", "modal_have_to"]
        },
        "micro_flaws": {
            "grammar": ["missing_article"],
            "vocabulary": ["incomplete_phrase"]
        },
        "vocab_control": {
            "appropriateness": "precise",
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
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'recommend useful' (useful ones/materials) is incomplete.",
                "why_not_6": "Structure 'role of teacher would be to...' is good."
            },
            "vocabulary": {
                "why_not_8": "Basic topic words.",
                "why_not_6": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'peers', 'materials'. Impact: Good. Justification: Band 7.",
        "grammar_reason": "Observation: 'role of teacher would be'. Impact: Good. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 2,
        "sample_id": "eCMxuQanvIE_q02",
        "video_id": "eCMxuQanvIE",
        "part": 1,
        "question": "Are you working or student?",
        "transcript": "Well, I am a student. Recently I have done my graduation in Bukongfield.",
        "word_count": 13,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["graduation"],
            "grammar_structures_used": ["present_perfect"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'have done my graduation' (graduated). 'I am a student' vs 'done my graduation' (contradictory unless post-grad)."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Short.",
                "why_not_5": "Correct."
            },
            "vocabulary": {
                "why_not_7": "'done my graduation' is awkward.",
                "why_not_5": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 6.",
        "grammar_reason": "Observation: 'have done my graduation' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 3,
        "sample_id": "eCMxuQanvIE_q03",
        "video_id": "eCMxuQanvIE",
        "part": 1,
        "question": "What kind of clothes you like to wear?",
        "transcript": "Well, I like to wear different kinds of clothes like t-shirts, jeans, and suits also. But sometimes it depends on the circumstances.",
        "word_count": 22,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["depends on the circumstances"],
            "grammar_structures_used": ["complex_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
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
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Simple.",
                "why_not_6": "Error-free."
            },
            "vocabulary": {
                "why_not_8": "'circumstances' is good.",
                "why_not_6": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'circumstances'. Impact: Good. Justification: Band 7.",
        "grammar_reason": "Observation: Correct. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 4,
        "sample_id": "eCMxuQanvIE_q04",
        "video_id": "eCMxuQanvIE",
        "part": 1,
        "question": "Do you like wearing t-shirts?",
        "transcript": "Without a shadow of doubt, I can easily say that I like to wear t-shirts because I feel comfortable whenever I wear them. And I have different kind of colors t-shirts like white, green, yellow, and blue ones.",
        "word_count": 38,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["without a shadow of doubt", "comfortable"],
            "grammar_structures_used": ["complex_sentence_because", "list"]
        },
        "micro_flaws": {
            "grammar": ["singular_plural_mismatch"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Without a shadow of doubt' is a memorized phrase used slightly formally for a simple question. 'different kind of colors t-shirts' (different kinds/colors of t-shirts)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "rare"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Grammar error 'different kind of'.",
                "why_not_5": "Complex structures correct."
            },
            "vocabulary": {
                "why_not_8": "Memorized idiom.",
                "why_not_6": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'shadow of doubt'. Impact: Cliche. Justification: Band 6.",
        "grammar_reason": "Observation: 'different kind of' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 5,
        "sample_id": "eCMxuQanvIE_q05",
        "video_id": "eCMxuQanvIE",
        "part": 1,
        "question": "Do you spend a lot of time choosing clothes?",
        "transcript": "Now I do not spend a lot of time of choosing clothes because at home I decide which things I need to buy and which things and clothes I can buy at a reasonable price. that is good.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["reasonable price"],
            "grammar_structures_used": ["complex_sentence_because"]
        },
        "micro_flaws": {
            "grammar": ["wrong_preposition"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
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
            "error_density": "rare"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'time of choosing' (time choosing).",
                "why_not_6": "Error-free sentences."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "'reasonable price' is good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'reasonable price'. Impact: Good. Justification: Band 7.",
        "grammar_reason": "Observation: 'time of choosing' (error). Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 6,
        "sample_id": "eCMxuQanvIE_q06",
        "video_id": "eCMxuQanvIE",
        "part": 1,
        "question": "So Nikita, do you prefer to wear comfortable and smart or smart clothes?",
        "transcript": "Well, on the daily basis, I always prefer to wear comfortable clothes. Whenever I have to go to other places like in birthday parties, ceremony, and marriages also, at that moment, I prefer to wear smart clothes. It always increases the beauty of my personality. Now, few questions will be based on noise.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["on the daily basis", "smart clothes", "personality"],
            "grammar_structures_used": ["complex_sentence_whenever"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": ["wrong_collocation"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'on the daily basis' (on a daily basis). 'increases the beauty of my personality' (enhances my appearance?). Personality is internal."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors 'on the daily basis'.",
                "why_not_5": "Complex sentences."
            },
            "vocabulary": {
                "why_not_7": "'beauty of personality' is unnatural.",
                "why_not_5": "Correct words."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'beauty of personality'. Impact: Unnatural. Justification: Band 6.",
        "grammar_reason": "Observation: 'on the daily basis' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 7,
        "sample_id": "eCMxuQanvIE_q07",
        "video_id": "eCMxuQanvIE",
        "part": 1,
        "question": "Do you like to stay in a place with lot of noise?",
        "transcript": "Yes, definitely no. I do not like to stay in a noisy place because I like to stay in a tranquil place.",
        "word_count": 22,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["tranquil place"],
            "grammar_structures_used": ["complex_sentence_because"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Yes, definitely no.' (Contradictory)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Short.",
                "why_not_6": "Error-free."
            },
            "vocabulary": {
                "why_not_8": "'tranquil' is excellent.",
                "why_not_6": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'tranquil'. Impact: Precise. Justification: Band 7.",
        "grammar_reason": "Observation: Correct. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 8,
        "sample_id": "eCMxuQanvIE_q09",
        "video_id": "eCMxuQanvIE",
        "part": 3,
        "question": "Do you think there is too much noise in today's world?",
        "transcript": "Definitely there are lots of noise and pollution in the world because every people have their own vehicle and they always use them to go at the workplace or a personal spaces also And vehicles always increase the toxic gases Now few questions will be based on robots Are robots important Absolutely robots are important They help us to do different kinds of works like cooking mopping and dusting also And they can also easy work Do robots affect people's lives? Indeed, robots affect the people's lives because people do not put their, physical effort on the work. They always depend on the robots for doing any kind of work at their workplace or at a personal place. Great.",
        "word_count": 121,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement_error", "article_error"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["toxic gases", "physical effort"],
            "grammar_structures_used": ["complex_sentence_because"]
        },
        "micro_flaws": {
            "grammar": ["singular_plural_mismatch"],
            "vocabulary": ["repetition"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'every people have' (every person has). 'go at the workplace' (go to). 'can also easy work' (can also ease work/make work easy)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "limited",
            "error_density": "frequent"
        },
        "discourse_metrics": {
            "length_appropriateness": "extended",
            "redundancy": "moderate",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Systematic errors. 'every people have'. 'go at'.",
                "why_not_4": "Complex structures attempted."
            },
            "vocabulary": {
                "why_not_7": "Good words 'toxic gases', 'mopping', 'dusting'.",
                "why_not_5": "Errors."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts complex sentences but accuracy is inconsistent.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses less common vocabulary but may make mistakes."
        },
        "vocab_reason": "Observation: 'toxic gases', 'dusting'. Impact: Good. Justification: Band 6.",
        "grammar_reason": "Observation: 'every people have' (error). Justification: Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 9,
        "sample_id": "eCMxuQanvIE_q10",
        "video_id": "eCMxuQanvIE",
        "part": 3,
        "question": "What can robots do for you at home?",
        "transcript": "Well, if I talk about the robots like things, computer, washing machine, and refrigerators also. With the help of computer, I can make a spreadsheet, Excel sheet also. And we do not put our more physical effort on them. They, they do the work in an efficient way. Okay, that is wonderful. So Nikita, this is end of the part one. Now I am going to give you a.",
        "word_count": 71,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrase_structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["spreadsheet", "efficient way"],
            "grammar_structures_used": ["complex_sentence"]
        },
        "micro_flaws": {
            "grammar": ["awkward_phrasing"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'robots like things' (robotic things?). 'put our more physical effort on them' (put more physical effort into them)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Phrasing errors 'put our more physical effort'.",
                "why_not_5": "Meaning clear."
            },
            "vocabulary": {
                "why_not_7": "'spreadsheet' is good.",
                "why_not_5": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'spreadsheet'. Impact: Precise. Justification: Band 6.",
        "grammar_reason": "Observation: 'put our more' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10,
        "sample_id": "eCMxuQanvIE_q11",
        "video_id": "eCMxuQanvIE",
        "part": 3,
        "question": "Do you think it is easy to make friends on social media?",
        "transcript": "According to my own perception, it is very difficult to make friends on social media because a lot of people always put their fake identity to misguide other person and it is very difficult for them to trust on other people. And if I talk about me, I always follow them to those people who, put their actual identity like name, and age also. And they always put, their different kinds of things and post also which are related to the knowledge. Like study.",
        "word_count": 83,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["fake identity", "misguide", "perception"],
            "grammar_structures_used": ["complex_sentence_because", "relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["wrong_preposition"],
            "vocabulary": ["wrong_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'trust on other people' (trust other people). 'follow them to those people' (follow those people)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "extended",
            "redundancy": "moderate",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Preposition errors 'trust on'.",
                "why_not_5": "Complex sentences used well."
            },
            "vocabulary": {
                "why_not_7": "'perception', 'misguide', 'fake identity' are good.",
                "why_not_5": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses less common vocabulary."
        },
        "vocab_reason": "Observation: 'fake identity', 'misguide'. Impact: Good. Justification: Band 6.",
        "grammar_reason": "Observation: 'trust on' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 11,
        "sample_id": "eCMxuQanvIE_q12",
        "video_id": "eCMxuQanvIE",
        "part": 3,
        "question": "What can people do on social media?",
        "transcript": "People can do a lot of things on social media because different people have different talents. They can post the pictures and videos also by making the reels and they can also get more followers and views also and that is the platform which is very famous in the all over the world. They can also get the, Okay, so do not you think that people can do acting, comedy, or they can perform the talent of sports? Well, it depends on the person choice. They can post different things like comedy, dance, and singing also. That platform is very demandable. it is a demanding platform. Demanding platform, and they can also get more name and fame from this platform. Okay.",
        "word_count": 120,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_error", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["name and fame", "reels"],
            "grammar_structures_used": ["complex_sentence"]
        },
        "micro_flaws": {
            "grammar": ["unnecessary_article"],
            "vocabulary": ["wrong_word_form"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'in the all over the world' (all over the world). 'demandable' (in demand / popular - self corrected to demanding). 'person choice' (person's choice)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "extended",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Article errors. 'the all over the world'.",
                "why_not_5": "Structures are accurate enough."
            },
            "vocabulary": {
                "why_not_7": "'name and fame' is a fixed phrase. 'demandable' is not a word.",
                "why_not_5": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses less common vocabulary."
        },
        "vocab_reason": "Observation: 'name and fame'. Impact: Idiomatic. 'demandable' (error). Justification: Band 6.",
        "grammar_reason": "Observation: 'the all over' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 12,
        "sample_id": "eCMxuQanvIE_q13",
        "video_id": "eCMxuQanvIE",
        "part": 3,
        "question": "Do you think people will read, newspaper or books in the future?",
        "transcript": "According to my point of view, technology is increasing day by day and, people will not read more newspaper and printed books in future because, they can read anything on social media but, but they can also misguide from the internet also. But older people have different opinions about the reading newspaper. They are addicted to read, from the printed books.",
        "word_count": 60,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_pattern", "article_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["increasing day by day", "printed books", "misguide"],
            "grammar_structures_used": ["complex_sentence_because"]
        },
        "micro_flaws": {
            "grammar": ["wrong_verb_pattern"],
            "vocabulary": ["wrong_voice"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'misguide from the internet' (be misguided by). 'addicted to read' (addicted to reading)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Verb pattern errors 'addicted to read'.",
                "why_not_5": "Structures are mostly correct."
            },
            "vocabulary": {
                "why_not_7": "'misguide' used actively instead of passively.",
                "why_not_5": "Good words."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses less common vocabulary."
        },
        "vocab_reason": "Observation: 'printed books'. Impact: Correct. 'misguide' (usage error). Justification: Band 6.",
        "grammar_reason": "Observation: 'addicted to read' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 13,
        "sample_id": "eCMxuQanvIE_q14",
        "video_id": "eCMxuQanvIE",
        "part": 3,
        "question": "Do older people spend much time on social media?",
        "transcript": "Well, I think older people do not spend excessive amount of time on social media because they always get connected with their friends on Facebook only. And younger spend a lot of time on social media to post their pictures and reels also because they have different opinion from the older ones. Okay.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["excessive amount of time", "connected with"],
            "grammar_structures_used": ["complex_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
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
            "error_density": "rare"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Minor errors 'younger spend' (younger people spend).",
                "why_not_6": "Correct."
            },
            "vocabulary": {
                "why_not_8": "'excessive amount' is good.",
                "why_not_6": "Accurate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'excessive amount'. Impact: Good. Justification: Band 7.",
        "grammar_reason": "Observation: 'younger spend' (minor). Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 14,
        "sample_id": "0x_Bl2jIOl0_q02",
        "video_id": "0x_Bl2jIOl0",
        "part": 1,
        "question": "Where do you come from?",
        "transcript": "I came from a small town Nirvana which is under the district Jindh in the state Haryana. Now few questions will be based on sports.",
        "word_count": 24,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["district", "state"],
            "grammar_structures_used": ["relative_clause"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
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
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Short.",
                "why_not_6": "Correct."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error-free sentences.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 6.",
        "grammar_reason": "Observation: Correct. Justification: Band 7.",
        "vocabulary": 6,
        "grammar": 7
    },
    {
        "id": 15,
        "sample_id": "0x_Bl2jIOl0_q03",
        "video_id": "0x_Bl2jIOl0",
        "part": 1,
        "question": "Okay, what sports do you like?",
        "transcript": "I like to watch many sports like cricket, football, tennis, and volleyball, but personally, I love to play cricket and volleyball the most.",
        "word_count": 23,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": [],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
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
            "flexibility": "moderate",
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Simple.",
                "why_not_6": "Correct."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error-free sentences.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 6.",
        "grammar_reason": "Observation: Correct. Justification: Band 7.",
        "vocabulary": 6,
        "grammar": 7
    },
    {
        "id": 16,
        "sample_id": "0x_Bl2jIOl0_q04",
        "video_id": "0x_Bl2jIOl0",
        "part": 1,
        "question": "Where did you learn to play?",
        "transcript": "I learned to play cricket by watching it on TV and through dedicated practice and guidance from experienced coaches.",
        "word_count": 18,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["dedicated practice", "guidance", "experienced coaches"],
            "grammar_structures_used": ["prepositional_phrase"]
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
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Short.",
                "why_not_7": "Error-free."
            },
            "vocabulary": {
                "why_not_9": "'dedicated practice', 'guidance'.",
                "why_not_7": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'dedicated practice'. Impact: Precise. Justification: Band 8.",
        "grammar_reason": "Observation: Correct. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    }
]

with open(output_file, "a") as f:
    for s in samples:
        f.write(json.dumps(s) + "\n")

print(f"Successfully appended {len(samples)} samples to {output_file}")
