import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 10901,
        "sample_id": "rHZKaUBWqfE_q05",
        "video_id": "rHZKaUBWqfE",
        "part": 1,
        "question": "Do you think it is important for you to celebrate your birthday?",
        "transcript": "Oh yeah, I am a big birthday guy. at like midnight, like going from August 2nd to August 3rd, I would like wake up, I would have my phone out, and I am just waiting until my birthday comes out. My family's usually asleep by then, but I would like walk around with my phone and then I would say like, hey dad, hey mom, it is my birthday, and they are like, you are too old to do that. Nice. it is your only day out of, you know, whole year. there is Christmas, there are other days, but it is your day. True.",
        "word_count": 96,
        "analysis_metadata": {
            "grammar_error_patterns": ["informal_fillers", "narrative_tense"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["big birthday guy", "midnight", "waiting until"],
            "grammar_structures_used": ["narrative_past", "reported_speech"]
        },
        "micro_flaws": {
            "grammar": ["overuse_like"],
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
                "why_not_8": "Heavy reliance on 'like' as a filler/structure marker ('I would like wake up', 'say like').",
                "why_not_6": "Narrative structure is clear and effective."
            },
            "vocabulary": {
                "why_not_8": "'Big birthday guy' is very natural/colloquial, but range is not academic/formal (which is fine for Part 1, but limits higher bands).",
                "why_not_6": "Good idiomatic sense."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control of simple and complex sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common and idiomatic vocabulary."
        },
        "vocab_reason": "Observation: 'Big birthday guy'. Impact: Natural colloquialism. Justification: Band 7.",
        "grammar_reason": "Observation: Overuse of 'like'. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 10902,
        "sample_id": "rHZKaUBWqfE_q06",
        "video_id": "rHZKaUBWqfE",
        "part": 1,
        "question": "And whose birthday do you think is the most important to celebrate?",
        "transcript": "Who, like, out of, like, my, my family's going to hate this, but I do have a girlfriend right now. So, I think my girlfriend's birthday is the most important day to celebrate. Yeah. I have to think about what gift I have to give her the things to do.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": ["fragmented_speech"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["hate this", "most important day"],
            "grammar_structures_used": ["complex_sentence_opinion"]
        },
        "micro_flaws": {
            "grammar": ["hesitation"],
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Starts with 'Who, like, out of, like'. Fragmented start.",
                "why_not_6": "Structure recovers well."
            },
            "vocabulary": {
                "why_not_8": "Basic vocabulary.",
                "why_not_6": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: Natural. Justification: Band 7.",
        "grammar_reason": "Observation: Hesitation at start. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 10903,
        "sample_id": "rHZKaUBWqfE_q07",
        "video_id": "rHZKaUBWqfE",
        "part": 1,
        "question": "So, do you do some cooking in the evening?",
        "transcript": "Not when I in Korea because there are a lot of kitchen stuff that my mom doesn want me to break But when I was in college I had to do a lot of cooking There are only like five kinds of food that I could cook usually it is not really cooking. they are pretty much just put the frozen food in the tray or on the plate and then just let the microwave or the oven do all the stuff. Absolutely.",
        "word_count": 82,
        "analysis_metadata": {
            "grammar_error_patterns": ["missing_verb", "informal_structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["kitchen stuff", "frozen food", "microwave", "oven"],
            "grammar_structures_used": ["reason_clause", "past_habit"]
        },
        "micro_flaws": {
            "grammar": ["missing_be_verb"],
            "vocabulary": ["general_words"]
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
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Error: 'Not when I in Korea' (missing 'am'/'was').",
                "why_not_6": "Complex sentences used correctly ('stuff that my mom doesn't want me to break')."
            },
            "vocabulary": {
                "why_not_8": "'Kitchen stuff', 'do all the stuff' - repetitive use of 'stuff'.",
                "why_not_6": "Good topic vocabulary."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Frozen food', 'microwave'. Impact: Topic specific. Justification: Band 7.",
        "grammar_reason": "Observation: Missing verb. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 10904,
        "sample_id": "rHZKaUBWqfE_q08",
        "video_id": "rHZKaUBWqfE",
        "part": 1,
        "question": "And do you have breakfast at home every day?",
        "transcript": "I have brunch because, I would not say having a meal at 11 or 12 as breakfast, but that is my first meal of the day. And yeah, usually just lunch.",
        "word_count": 31,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["brunch", "first meal of the day"],
            "grammar_structures_used": ["reason_clause", "clarification"]
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
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good but simple.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Natural 'first meal of the day'."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Natural."
        },
        "vocab_reason": "Observation: 'Brunch'. Justification: Band 7.",
        "grammar_reason": "Observation: Correct. Justification: Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 10905,
        "sample_id": "rHZKaUBWqfE_q13",
        "video_id": "rHZKaUBWqfE",
        "part": 3,
        "question": "What kind of people?",
        "transcript": "Oh, actually, when I, every time I go to an interview at the company, there is always one, receptionist. Or that one person who just, who does all the, all the work that like, those, the people who are the, on like the board could not do. Just kind of knows everything about the company. Like where the thing is, like what do you have to do. And basically the person who you meet right when you get accepted to job because they would usually kind of help you out. So they are much more important than people like on the board because you know they pretty much run things.",
        "word_count": 108,
        "analysis_metadata": {
            "grammar_error_patterns": ["fragmented_clauses"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["receptionist", "on the board", "run things", "get accepted to job"],
            "grammar_structures_used": ["relative_clause", "comparison"]
        },
        "micro_flaws": {
            "grammar": ["heavy_hesitation"],
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
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "extended",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Sentence structure is quite fragmented due to hesitations ('who just, who does all the, all the work').",
                "why_not_6": "Subordinate clauses are used correctly."
            },
            "vocabulary": {
                "why_not_8": "'Run things' is good. 'On the board' is specific.",
                "why_not_6": "Effective."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'On the board'. Impact: Specific. Justification: Band 7.",
        "grammar_reason": "Observation: Fragmented. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 10906,
        "sample_id": "rHZKaUBWqfE_q14",
        "video_id": "rHZKaUBWqfE",
        "part": 3,
        "question": "Having a good relationship with colleagues or doing your work well?",
        "transcript": "If you do your work well, you usually have good relationship with your colleagues. that is for sure. but I mean for the company honestly it is just if you just sit down and do your work. that is the most profitable work.",
        "word_count": 42,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["profitable work", "relationship with your colleagues"],
            "grammar_structures_used": ["conditional_zero"]
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
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Simple logic.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Natural."
        },
        "vocab_reason": "Observation: 'Profitable'. Justification: Band 7.",
        "grammar_reason": "Observation: Correct. Justification: Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 10907,
        "sample_id": "rHZKaUBWqfE_q15",
        "video_id": "rHZKaUBWqfE",
        "part": 3,
        "question": "Than employees?",
        "transcript": "Oh, I do not think so. Bosses are, our enemies usually. They, they see a lot of profit. They go out of, deals from other companies usually and they do not really know all the, the pity works all the people have to do. So, yeah, bosses are not really late.",
        "word_count": 50,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "variable",
            "vocab_evidence": ["pity works", "deals from other companies"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["wrong_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "variable",
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
                "why_not_8": "'Bosses are not really late' (meaning unknown - likely transcription error or vocab error for 'liked'?).",
                "why_not_6": "Sentence structure is generally correct."
            },
            "vocabulary": {
                "why_not_7": "'Pity works' (petty works? pity work?). Unclear.",
                "why_not_5": "Meaning generally conveyed."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 6,
            "vocabulary_text": "Errors in choice."
        },
        "vocab_reason": "Observation: 'Pity works' error. Justification: Band 6.",
        "grammar_reason": "Observation: Correct structure. Justification: Band 7.",
        "vocabulary": 6,
        "grammar": 7
    },
    {
        "id": 10908,
        "sample_id": "rHZKaUBWqfE_q16",
        "video_id": "rHZKaUBWqfE",
        "part": 3,
        "question": "Is it possible for bosses to be friends with their employees?",
        "transcript": "my, my past boss I had, he tried so hard to kind of like mingle with us. he is on his 50s, but he kind of tried to catch up on the trends of the MZ generation. Yeah. So they could definitely be popular They just have to try and accept that things are changing Yes right right And what do you think are the benefits when a child is popular at school Oh, the benefits. Definitely give them confidence. that is for sure. I would not call myself, I was popular in high school, but I mean, I was an athlete obviously, and then people knew me. And, back then I did not really speak English that well, but it gave me lots of confidence, just speaking in front of people, which is very important when you grow up. And, it gives you a lot of confidence, that is for sure. So, I think it is important.",
        "word_count": 160,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition_error"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["mingle with", "catch up on the trends", "MZ generation", "athlete", "confidence"],
            "grammar_structures_used": ["narrative_past", "complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": ["wrong_preposition"],
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
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "extended",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Minor error 'on his 50s' (in his 50s).",
                "why_not_7": "Complex structures handled with ease."
            },
            "vocabulary": {
                "why_not_9": "'Mingle with', 'catch up on trends', 'MZ generation'. Very precise.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Majority of sentences error-free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Precise and flexible."
        },
        "vocab_reason": "Observation: 'Mingle with', 'MZ generation'. Impact: Precise/Cultural. Justification: Band 9.",
        "grammar_reason": "Observation: Preposition error. Justification: Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 10909,
        "sample_id": "rHZKaUBWqfE_q17",
        "video_id": "rHZKaUBWqfE",
        "part": 3,
        "question": "And what do you think is the best way to make friends with a new person?",
        "transcript": "Just try to catch up on things. I think making friends definitely takes a lot of effort. Because, I mean, it takes a lot of small talks. So if you know like the reason stuff or just try to have similarities that usually other people do. I mean, for myself, I am a big sports guy again.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["pluralization_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["catch up on things", "small talks", "takes a lot of effort"],
            "grammar_structures_used": ["complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["uncountable_noun_pluralized"]
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'Reason stuff' is vague.",
                "why_not_6": "Correct."
            },
            "vocabulary": {
                "why_not_8": "'Small talks' (should be small talk - uncountable).",
                "why_not_6": "Natural idioms."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Small talks' error. Justification: Band 7.",
        "grammar_reason": "Observation: Correct. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 11001,
        "sample_id": "PSisNgVCyqw_q02",
        "video_id": "PSisNgVCyqw",
        "part": 1,
        "question": "So, what, can you tell me what is the weather like where you live?",
        "transcript": "I am currently living in Korea at the moment. In Korea, in summer, recently the weather became really hot, scorching hot. So even though I take a shower and then I leave my house, I sweat so much as soon as I leave the house. So I guess the recent weather became a little bit very extreme compared to the past. But in Korea, we all have four seasons. So I think we could, experience all kind of activities we can do in each season. So I think it is good to travel around in Korea.",
        "word_count": 96,
        "analysis_metadata": {
            "grammar_error_patterns": ["redundancy"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["scorching hot", "extreme", "travel around", "four seasons"],
            "grammar_structures_used": ["complex_sentence_contrast", "complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": ["redundant_phrasing"],
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
                "why_not_9": "'A little bit very extreme' is contradictory/ungrammatical.",
                "why_not_7": "Structures are generally error free."
            },
            "vocabulary": {
                "why_not_9": "'Scorching hot' is Band 9 collocation.",
                "why_not_7": "Strong."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Scorching hot'. Impact: Precise. Justification: Band 8.",
        "grammar_reason": "Observation: 'Little bit very extreme'. Justification: Band 7.",
        "vocabulary": 8,
        "grammar": 7
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
