import json

output_file = "jules_scored_output_151-200.jsonl"

samples = [
    {
        "id": 1,
        "sample_id": "0x_Bl2jIOl0_q05",
        "video_id": "0x_Bl2jIOl0",
        "part": 1,
        "question": "Okay, did you do some sports when you were younger?",
        "transcript": "Yes, I actively take participants. I was a little bit more focused on the sport during my childhood. I liked to play cricket and volleyball which not only kept me physically active but also taught me various life lessons about hard work, dedication, and discipline. Now, two questions will be based on relaxation.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["collocation", "verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["life lessons", "dedication", "discipline", "physically active"],
            "grammar_structures_used": ["not_only_but_also", "relative_clause_which"]
        },
        "micro_flaws": {
            "grammar": ["wrong_verb_choice"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'actively take participants' (participated? took part?). Major vocabulary/grammar error in the first sentence."
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
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "First sentence error 'take participants' is significant.",
                "why_not_6": "Complex structures like 'not only... but also' used correctly."
            },
            "vocabulary": {
                "why_not_8": "'take participants' is incorrect.",
                "why_not_6": "'physically active', 'dedication' are good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control of grammar and punctuation but may make a few mistakes.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items with some awareness of style."
        },
        "vocab_reason": "Observation: 'take participants' (error). 'dedication', 'discipline' (good). Justification: Band 7.",
        "grammar_reason": "Observation: 'not only... but also' (good). Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 2,
        "sample_id": "0x_Bl2jIOl0_q06",
        "video_id": "0x_Bl2jIOl0",
        "part": 1,
        "question": "What do you do to relax?",
        "transcript": "I find relaxation in engaging activities such as reading, practicing mindfulness, and spending quality time with loved ones. These activities helps me to rewind, recharge, and maintain a quality and good life. Great.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["practicing mindfulness", "quality time", "recharge", "rewind"],
            "grammar_structures_used": ["listing", "infinitive_purpose"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_disagreement"],
            "vocabulary": ["wrong_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'activities helps me' (help). 'rewind' (unwind?). 'quality and good life' (redundant)."
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
                "why_not_8": "Agreement error 'helps'.",
                "why_not_6": "Good structure."
            },
            "vocabulary": {
                "why_not_8": "'rewind' vs 'unwind' is a precision error.",
                "why_not_6": "'mindfulness' is high level."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'mindfulness'. Impact: Precise. 'rewind' (error for unwind). Justification: Band 7.",
        "grammar_reason": "Observation: 'activities helps' (error). Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 3,
        "sample_id": "0x_Bl2jIOl0_q08",
        "video_id": "0x_Bl2jIOl0",
        "part": 2,
        "question": "Can you explain why you really like her?",
        "transcript": "She really helped me to encourage me and motivated me to pursue, to fulfill my dreams. So now few questions will be based on this.",
        "word_count": 27,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_pattern"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["pursue my dreams", "fulfill my dreams"],
            "grammar_structures_used": ["infinitive_purpose"]
        },
        "micro_flaws": {
            "grammar": ["redundant_pronoun"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'helped me to encourage me' (helped encourage me / encouraged me). Redundant pronoun."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Redundant pronoun usage.",
                "why_not_6": "Correct structures."
            },
            "vocabulary": {
                "why_not_8": "Good collocations.",
                "why_not_6": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'fulfill my dreams'. Impact: Natural. Justification: Band 7.",
        "grammar_reason": "Observation: 'helped me to encourage me' (error). Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 4,
        "sample_id": "0x_Bl2jIOl0_q09",
        "video_id": "0x_Bl2jIOl0",
        "part": 3,
        "question": "Who motivates children the most?",
        "transcript": "I think, as an young age, children can be motivated by their parents and teachers the most. But as they grew up, they started idealizing sports stars and movie stars, which can be, which can motivate them too.",
        "word_count": 42,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice", "preposition_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["idealizing", "movie stars"],
            "grammar_structures_used": ["passive_voice", "relative_clause_which"]
        },
        "micro_flaws": {
            "grammar": ["wrong_tense"],
            "vocabulary": ["wrong_preposition"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'as an young age' (at a young age). 'they started idealizing' (they start idealizing - general truth)."
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
                "why_not_7": "Tense shift 'grew up', 'started' for general facts.",
                "why_not_5": "Passive and relative clauses used correctly."
            },
            "vocabulary": {
                "why_not_7": "'as an young age' (at). 'idealizing' is good.",
                "why_not_5": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'idealizing'. Impact: Good. 'as an young age' (error). Justification: Band 6.",
        "grammar_reason": "Observation: Tense error (started vs start). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 5,
        "sample_id": "0x_Bl2jIOl0_q10",
        "video_id": "0x_Bl2jIOl0",
        "part": 3,
        "question": "Why do you think so?",
        "transcript": "Because, movie star and sports star are a good way to idealize and they are successful people, which can make you motivate.",
        "word_count": 25,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form", "article_error"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "wrong",
            "vocab_evidence": ["successful people"],
            "grammar_structures_used": ["relative_clause_which"]
        },
        "micro_flaws": {
            "grammar": ["wrong_verb_structure"],
            "vocabulary": ["wrong_part_of_speech"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'good way to idealize' (good people to idealize?). 'make you motivate' (motivate you / make you motivated)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "limited",
            "error_density": "frequent"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Errors 'make you motivate'. 'movie star' (stars).",
                "why_not_4": "Relative clause correct."
            },
            "vocabulary": {
                "why_not_6": "'motivate' used as adjective/noun? 'way to idealize' is odd.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts complex sentences but accuracy is inconsistent.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: 'idealize'. Impact: OK. 'make you motivate' (error). Justification: Band 5.",
        "grammar_reason": "Observation: 'make you motivate' (error). Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 6,
        "sample_id": "0x_Bl2jIOl0_q11",
        "video_id": "0x_Bl2jIOl0",
        "part": 3,
        "question": "How can teachers motivate children according to you?",
        "transcript": "Teachers can motivate children by various methods like encouraging them, appreciating their efforts, and by achieving small goals, etc.",
        "word_count": 21,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["various methods", "appreciating efforts"],
            "grammar_structures_used": ["gerund_phrase", "listing"]
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
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Simple listing.",
                "why_not_6": "Correct."
            },
            "vocabulary": {
                "why_not_8": "Good.",
                "why_not_6": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'appreciating their efforts'. Impact: Good. Justification: Band 7.",
        "grammar_reason": "Observation: Correct. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 7,
        "sample_id": "0x_Bl2jIOl0_q12",
        "video_id": "0x_Bl2jIOl0",
        "part": 3,
        "question": "Any other ways they can motivate children?",
        "transcript": "They can motivate children by think out of the box and by celebrating small success. Good.",
        "word_count": 18,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["think out of the box", "celebrating small success"],
            "grammar_structures_used": ["preposition_by_gerund"]
        },
        "micro_flaws": {
            "grammar": ["wrong_verb_form_after_preposition"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'by think' (by thinking). 'think out of the box' is idiomatic."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'by think' error.",
                "why_not_5": "Correct structure generally."
            },
            "vocabulary": {
                "why_not_8": "'think out of the box' is good.",
                "why_not_6": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses idiomatic vocabulary."
        },
        "vocab_reason": "Observation: 'think out of the box'. Impact: Idiomatic. Justification: Band 7.",
        "grammar_reason": "Observation: 'by think' (error). Justification: Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 8,
        "sample_id": "0x_Bl2jIOl0_q13",
        "video_id": "0x_Bl2jIOl0",
        "part": 3,
        "question": "How it is different from teaching kids?",
        "transcript": "The children who are not motivated are cannot gain much from a class or from a teacher And teaching alone is cannot make their performance in the academics grow And children who are motivated can gain much more in a class and non students can disrupt a class Okay. Okay.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["double_verb", "word_choice"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["academics", "disrupt"],
            "grammar_structures_used": ["relative_clause", "passive_attempt"]
        },
        "micro_flaws": {
            "grammar": ["verb_structure_error"],
            "vocabulary": ["wrong_word"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'are cannot gain' (cannot gain). 'is cannot make' (cannot make). 'non students' (non-motivated students?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "limited",
            "error_density": "frequent"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "moderate",
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Systematic double verb error 'are cannot'.",
                "why_not_4": "Relative clauses 'who are not motivated' are correct."
            },
            "vocabulary": {
                "why_not_7": "'non students' is confusing. 'disrupt' is good.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts complex sentences but accuracy is inconsistent.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses less common vocabulary."
        },
        "vocab_reason": "Observation: 'disrupt', 'academics'. Impact: Good. 'non students' (error). Justification: Band 6.",
        "grammar_reason": "Observation: 'are cannot' (error). Justification: Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 9,
        "sample_id": "iMPGHuKklD8_q03",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "Which mobile apps do you use?",
        "transcript": "To honest with you, I utilize a lot of apps for such as entertainment purpose and study. I like to use WhatsApp, YouTube, and Google. Okay.",
        "word_count": 27,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrase_structure", "preposition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["utilize", "entertainment purpose"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["missing_verb_be"],
            "vocabulary": ["wrong_preposition"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'To honest with you' (To be honest). 'apps for such as' (apps such as / apps for... such as)."
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
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Missing verb 'To honest'. Preposition error 'for such as'.",
                "why_not_5": "Sentences mainly correct."
            },
            "vocabulary": {
                "why_not_7": "'utilize' is good. 'entertainment purpose' (purposes).",
                "why_not_5": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'utilize'. Impact: Good. Justification: Band 6.",
        "grammar_reason": "Observation: 'To honest' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10,
        "sample_id": "iMPGHuKklD8_q04",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "Which one do you want to use?",
        "transcript": "I want to use YouTube, because my teacher gave me a project to complete in two months. So I decide to, complete my project with the help of this app. Okay.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["complete my project"],
            "grammar_structures_used": ["complex_sentence_because"]
        },
        "micro_flaws": {
            "grammar": ["tense_inconsistency"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'gave me a project' (past) ... 'So I decide to' (decided)."
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
                "why_not_7": "Tense inconsistency 'decide'.",
                "why_not_5": "Complex structure 'because...' used correctly."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
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
        "grammar_reason": "Observation: 'decide' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 11,
        "sample_id": "iMPGHuKklD8_q05",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "Which one are popular in your country?",
        "transcript": "In my country, there are many popular apps, such as WhatsApp for chatting and, entertainment, entertainment purposes like, Instagram. Okay.",
        "word_count": 22,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["chatting", "entertainment purposes"],
            "grammar_structures_used": ["simple_sentence"]
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
                "why_not_8": "Simple list.",
                "why_not_6": "Error-free."
            },
            "vocabulary": {
                "why_not_8": "Good.",
                "why_not_6": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'entertainment purposes'. Impact: Good. Justification: Band 7.",
        "grammar_reason": "Observation: Correct. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 12,
        "sample_id": "iMPGHuKklD8_q06",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "Do you want to make any, do you want to make any application?",
        "transcript": "I adore to make application for children, which, which it give information about college and courses. Two questions will be based on mathematics.",
        "word_count": 24,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_pattern", "relative_clause_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "wrong",
            "vocab_evidence": ["adore to make"],
            "grammar_structures_used": ["relative_clause_which"]
        },
        "micro_flaws": {
            "grammar": ["double_subject", "wrong_infinitive"],
            "vocabulary": ["wrong_verb"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'adore to make' (would love to make). 'which it give' (which gives). 'application' (an application/applications)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "'which it give' is a basic error.",
                "why_not_4": "Meaning clear."
            },
            "vocabulary": {
                "why_not_6": "'adore to make' is unnatural.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts complex sentences but accuracy is inconsistent.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: 'adore to make' (error). Justification: Band 5.",
        "grammar_reason": "Observation: 'which it give' (error). Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 13,
        "sample_id": "iMPGHuKklD8_q07",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "When did you start learning math?",
        "transcript": "To be honest with you, I started learning math when I am six year old and my father is my first person that taught me about math. Okay.",
        "word_count": 29,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_error", "phrase_structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["to be honest"],
            "grammar_structures_used": ["complex_sentence_when"]
        },
        "micro_flaws": {
            "grammar": ["wrong_tense", "wrong_singular_form"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "adequate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'when I am six year old' (was six years old). 'father is my first person' (was the first person)."
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
                "why_not_6": "Tense errors 'am', 'is'. 'six year old' (years).",
                "why_not_4": "Structure correct."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts complex sentences but accuracy is inconsistent.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 5.",
        "grammar_reason": "Observation: 'when I am' (error). Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 14,
        "sample_id": "iMPGHuKklD8_q08",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "Do you like math?",
        "transcript": "Well, I am not very good in math, but I do not dislike it. Okay.",
        "word_count": 16,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["good in math"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["wrong_preposition"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "adequate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'good in math' (good at math)."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "rare"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Preposition error 'good in'.",
                "why_not_5": "Correct."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
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
        "grammar_reason": "Observation: 'good in' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 15,
        "sample_id": "iMPGHuKklD8_q09",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "Who is your favorite teacher so far?",
        "transcript": "In my college and school year, there are many teachers who taught me about math. But Mr. Ram Mohan is my favorite teacher. Okay.",
        "word_count": 25,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrase_structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["school year"],
            "grammar_structures_used": ["relative_clause_who"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["wrong_plural"]
        },
        "vocab_control": {
            "appropriateness": "adequate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'In my college and school year' (years). 'taught me about math' (taught me math)."
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
                "why_not_7": "'school year' (years).",
                "why_not_5": "Relative clause correct."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
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
        "grammar_reason": "Observation: 'school year' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 16,
        "sample_id": "iMPGHuKklD8_q11",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "Have you, done any water sport?",
        "transcript": "Yes, last year I do swim, but I not have much opportunity to, do water sport.",
        "word_count": 18,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_error", "verb_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["water sport", "swim"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["wrong_auxiliary", "missing_auxiliary"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'last year I do swim' (I swam / did swimming). 'I not have' (I did not have / do not have)."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "low",
            "flexibility": "limited",
            "error_density": "frequent"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Basic errors 'I do swim', 'I not have'.",
                "why_not_3": "Intelligible."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Errors predominate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 5.",
        "grammar_reason": "Observation: 'I do swim' (error). Justification: Band 4.",
        "vocabulary": 5,
        "grammar": 4
    },
    {
        "id": 17,
        "sample_id": "iMPGHuKklD8_q12",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "Okay, are water sports popular in India?",
        "transcript": "Yes, in my country there are, water sports very popular, most of eastern side and south side. Of my region. Okay.",
        "word_count": 22,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure_breakdown", "preposition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["eastern side"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["missing_verb"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "adequate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'there are, water sports very popular' (water sports are very popular / there are very popular water sports). 'most of eastern side' (mostly on the eastern side)."
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
                "why_not_6": "Structural error 'there are... popular'.",
                "why_not_4": "Meaning clear."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts basic sentences.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 5.",
        "grammar_reason": "Observation: 'there are... popular' (error). Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 18,
        "sample_id": "iMPGHuKklD8_q13",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "What kind of water sports do you want to try?",
        "transcript": "I want to try surfing because last year my brother going went went to Goa he told me about surfing Okay Few questions will be based on birthdays How do children celebrate birthdays in your country In my country, children like to celebrate their birthday through, cutting cake and, and going for party. Okay.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_correction", "phrase_structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["surfing", "cutting cake"],
            "grammar_structures_used": ["complex_sentence_because"]
        },
        "micro_flaws": {
            "grammar": ["self_correction"],
            "vocabulary": ["wrong_preposition"]
        },
        "vocab_control": {
            "appropriateness": "adequate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'brother going went went' (correction). 'through cutting cake' (by cutting a cake). 'going for party' (going to a party)."
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
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Basic errors 'going for party'.",
                "why_not_4": "Corrections show awareness."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts complex sentences.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: 'surfing'. Impact: Correct. 'cutting cake' (article). Justification: Band 5.",
        "grammar_reason": "Observation: 'going went' (correction). Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    }
]

with open(output_file, "a") as f:
    for s in samples:
        f.write(json.dumps(s) + "\n")

print(f"Successfully appended {len(samples)} samples to {output_file}")
