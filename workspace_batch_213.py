import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 213 ---
# Total Samples: 20
# Samples Analyzed:

# 1. ArXzJwpStqs_q03 (Band 6.0)
# Transcript: "Right so can I have the Penance paper back all right thank you..."
# Analysis: EXAMINER INSTRUCTION.
# - Verdict: INVALID (Skip).

# 2. mqGHL6ppfwM_q03 (Band 8.0)
# Transcript: "I would say I like my living room the most... specific division... workbench... studies and work."
# Analysis:
# - Grammar: "specific division" (good). "It is my living room has most" (My living room has...).
# - Vocabulary: "workbench", "specific division".
# - Verdict: Band 8.0.

# 3. mqGHL6ppfwM_q04 (Band 8.0)
# Transcript: "lived there since fifth grade which is about 13 years now."
# Analysis: Short but accurate.
# - Verdict: Valid (Band 8).

# 4. mqGHL6ppfwM_q05 (Band 8.0)
# Transcript: "neighborhood is quite a social place... tutor some of the kids... familiar with me."
# Analysis:
# - Grammar: "I would most of the times I would just smile" (repetition).
# - Verdict: Band 8.0.

# 5. mqGHL6ppfwM_q06 (Band 8.0)
# Transcript: "separate choosers against the things that youngsters would bring... recommend young people to choose..."
# Analysis:
# - Grammar: "separate choosers against" (prejudices against?). "youngsters".
# - Verdict: Band 8.0. "choosers" might be ASR error for "issues" or "prejudices".

# 6. mqGHL6ppfwM_q07 (Band 8.0)
# Transcript: "make list almost every day... daily checklist..."
# Analysis: Accurate.
# - Verdict: Band 8.0.

# 7. mqGHL6ppfwM_q08 (Band 8.0)
# Transcript: "Most specifically, the noting app..."
# Analysis: "noting app" (notes app).
# - Verdict: Band 8.0.

# 8. mqGHL6ppfwM_q09 (Band 8.0)
# Transcript: "depends on my schedule... three or four times a week..."
# Analysis: "just I do not really stay up late" (I just don't).
# - Verdict: Band 8.0.

# 9. mqGHL6ppfwM_q10 (Band 8.0)
# Transcript: "chase deadlines... work for my other jobs."
# Analysis: "chase deadlines" (meet deadlines / chase deadlines is okay).
# - Verdict: Band 8.0.

# 10. mqGHL6ppfwM_q11 (Band 8.0)
# Transcript: "pull an allnighter... night owl... problem against it..."
# Analysis:
# - Vocabulary: "pull an allnighter", "night owl". Excellent idioms.
# - Verdict: Band 8.0+.

# 11. mqGHL6ppfwM_q12 (Band 8.0)
# Transcript: "habit of going shopping..."
# Analysis: Good.
# - Verdict: Band 8.0.

# 12. mqGHL6ppfwM_q13 (Band 8.0)
# Transcript: "chose the right store... chose like the whole period of time..."
# Analysis: "chose" (choose).
# - Verdict: Band 8.0.

# 13. mqGHL6ppfwM_q14 (Band 8.0)
# Transcript: "manage my financial situation very thoroughly... useless stuffs."
# Analysis: "useless stuffs" (stuff is uncountable). "thoroughly".
# - Verdict: Band 8.0.

# 14. mqGHL6ppfwM_q16 (Band 8.0)
# Transcript: "divided into many different types... long-term or short term... lifelong learning... change everywhere you could."
# Analysis: "lifelong learning".
# - Verdict: Band 8.0.

# 15. mqGHL6ppfwM_q17 (Band 8.0)
# Transcript: "dream big... bucket list... reasonable for them."
# Analysis: "dream big", "bucket list". Good.
# - Verdict: Band 8.0.

# 16. mqGHL6ppfwM_q18 (Band 8.0)
# Transcript: "five types of validation... people failed... because they did not really follow..."
# Analysis: "validation steps".
# - Verdict: Band 8.0.

# 17. mqGHL6ppfwM_q19 (Band 8.0)
# Transcript: "it is really vague for me."
# Analysis: "vague". Good.
# - Verdict: Band 8.0.

# 18. pbx96FjvLp4_q01 (Band 6.5)
# Transcript: "my name is Hunan and you can call me. Yeah."
# Analysis: Intro. Valid.
# - Verdict: Band 6.5.

# 19. pbx96FjvLp4_q02 (Band 6.5)
# Transcript: "Yes."
# Analysis: Too short.
# - Verdict: Valid (Band 6).

# 20. pbx96FjvLp4_q03 (Band 6.5)
# Transcript: "stay in my hour... do everything I want at that room... always in the time in my room."
# Analysis:
# - Grammar: "stay in my hour" (own hour? room?). "at that room" (in). "always in the time" (spend time?).
# - Verdict: Band 6.0/6.5.

scored_samples = [
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q03", "video_id": "mqGHL6ppfwM",
        "part": 1,
        "question": "Favorite room?",
        "transcript": "I would say I like my living room the most. Even though my apartment does not really have any specific division for each part of the house. It is my living room has most of the things that I need. most specifically my workbench where I do most of my studies and work.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["workbench", "specific division"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["extra_word_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'It is my living room has most' (My living room has...)."
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
                "why_not_9": "Structural glitch ('It is... has').",
                "why_not_7": "Complex structures used correctly otherwise."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Precise. Band 8.",
        "grammar_reason": "Mostly error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q04", "video_id": "mqGHL6ppfwM",
        "part": 1,
        "question": "How long lived?",
        "transcript": "I think I have lived there since fifth grade which is about 13 years now.",
        "word_count": 14,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["fifth grade"],
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
            "flexibility": "moderate",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Short.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Natural."
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
        "id": 0, "sample_id": "mqGHL6ppfwM_q05",
        "video_id": "mqGHL6ppfwM",
        "part": 1,
        "question": "Neighborhood like?",
        "transcript": "I would say my neighborhood is quite a social place because all the people there are very friendly and they would welcome me in every way. I would most of the times I would just smile at them whenever I see them going around. I also tutor some of the kids there so they are very familiar with me.",
        "word_count": 58,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["social place", "familiar with"],
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
                "why_not_9": "Repetition 'I would... I would'.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q06",
        "video_id": "mqGHL6ppfwM",
        "part": 1,
        "question": "Good for young people?",
        "transcript": "I would say not quite because my neighborhood has been around for about like 20 years or so now is not new. So people may have separate choosers against the things that youngsters would bring to the environment. So I would recommend young people to choose another place to live rather than this one.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["recommend", "youngsters"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'separate choosers against' (prejudices/issues?). 'not quite' (good)."
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
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'choosers' error.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Error in 'choosers'. Band 7.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q07",
        "video_id": "mqGHL6ppfwM",
        "part": 1,
        "question": "Make lists?",
        "transcript": "I make list almost every day. whenever I wake up, I would make a daily checklist for the things I need to do.",
        "word_count": 22,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["daily checklist"],
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
            "flexibility": "moderate",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Short.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Natural."
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
        "id": 0, "sample_id": "mqGHL6ppfwM_q08",
        "video_id": "mqGHL6ppfwM",
        "part": 1,
        "question": "Paper or phone?",
        "transcript": "I always make lists on my phone. Most specifically, the noting app that every phone has.",
        "word_count": 16,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["noting app"],
            "grammar_structures_used": ["simple_sentence"]
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
                "why_not_9": "Short.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Accurate. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q09",
        "video_id": "mqGHL6ppfwM",
        "part": 1,
        "question": "Stay up late?",
        "transcript": "It really depends on my schedule. Sometimes I stay up late for about three or four times a week. Other times, just I do not really stay up late at all.",
        "word_count": 31,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_order"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["depends on my schedule"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["word_order_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'just I do not' (I just do not)."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Minor error.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural. Band 8.",
        "grammar_reason": "Minor slip. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q10",
        "video_id": "mqGHL6ppfwM",
        "part": 1,
        "question": "What do?",
        "transcript": "Mostly to chase deadlines and do the studies that I need to do and all and the work for my other jobs.",
        "word_count": 21,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["chase deadlines"],
            "grammar_structures_used": ["fragment"]
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
                "why_not_9": "Fragment answer.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "'chase deadlines' (Good).",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good collocation. Band 8.",
        "grammar_reason": "Accurate fragment. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q11",
        "video_id": "mqGHL6ppfwM",
        "part": 1,
        "question": "Feel next morning?",
        "transcript": "I think it depends on how long I stay up late. If I pull an allnighter, yes, it will affect me a day or two later, but people always call me a night owl. So, I do not really have any problem against it. I just feel sleepy when I go whenever I go to university. that is all.",
        "word_count": 59,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["pull an allnighter", "night owl"],
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
                "why_not_9": "'pull an allnighter', 'night owl'. Excellent native idioms.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent idioms. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q12",
        "video_id": "mqGHL6ppfwM",
        "part": 1,
        "question": "Shopping?",
        "transcript": "I do not really go shopping that much because all I need is here and whenever I need something, I just go. I do not really have a habit of going shopping anywhere.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["habit of"],
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
            "flexibility": "moderate",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q13",
        "video_id": "mqGHL6ppfwM",
        "part": 1,
        "question": "Online or stores?",
        "transcript": "I would say I like shopping online more because one you can get a lot of coupons if you chose the right store to buy in and you chose the right you chose like the whole period of time to buy your stuffs.",
        "word_count": 42,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["coupons"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'chose' (choose). 'stuffs' (stuff). 'buy in' (buy from/at)."
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
                "why_not_9": "Tense error 'chose'.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "'stuffs' error.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Error in 'stuffs'. Band 7.",
        "grammar_reason": "Tense slip but mostly accurate. Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q14",
        "video_id": "mqGHL6ppfwM",
        "part": 1,
        "question": "Changed habits?",
        "transcript": "I would say yes. Now that I have a job, I will consider spending my money more carefully because it now because I I have to manage my financial situation very thoroughly so that I would not spend any money on like useless stuffs.",
        "word_count": 42,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["manage my financial situation", "thoroughly"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'useless stuffs' (stuff)."
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
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'stuffs' error.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Error in 'stuffs'. Band 7.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q16",
        "video_id": "mqGHL6ppfwM",
        "part": 3,
        "question": "Goals stages?",
        "transcript": "I think as you grow up the goals should change. goals I think would be divided into many different types of goals either long-term or short term and as life goes on people will have to change their goals. They will maybe will they will achieve it and they will set another goal for themselves. because it is lifelong learning. So you have to do everything you must do and change everywhere you could.",
        "word_count": 73,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["lifelong learning", "long-term", "short term"],
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
                "why_not_9": "Standard.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good range. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q17",
        "video_id": "mqGHL6ppfwM",
        "part": 3,
        "question": "Types of goals?",
        "transcript": "As I said, it really depends on the stages of life that they are in. So, young people would usually set just normal short goals. Sometimes they would dream big and set their long-term goals for jobs or, the things that they want to do as a bucket list. But for older people, they usually do not have that much time. So, they would set any goal that are any goals that are the most reasonable for them.",
        "word_count": 76,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["dream big", "bucket list", "stages of life"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'any goal that are' (is). 'short goals' (short-term?)."
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
                "why_not_9": "Agreement error 'goal that are'.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "'dream big', 'bucket list'. Excellent.",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Excellent idioms. Band 8.",
        "grammar_reason": "Minor error. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q18",
        "video_id": "mqGHL6ppfwM",
        "part": 3,
        "question": "Why fail?",
        "transcript": "I had a some I had someone who taught me in co in college that in order to set a goal they need to to follow five types of validation for them to for the goals to be reasonable. And people failed to set goals because people fa people failed to achieve goals was because they did not really follow that five validation steps.",
        "word_count": 64,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["validation steps", "achieve goals"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'people failed... was because' (the reason people failed was because / people failed because). 'five validation steps'."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
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
                "why_not_9": "Structural errors.",
                "why_not_7": "Complex structures."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good. Band 7.",
        "grammar_reason": "Structural mixups. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "mqGHL6ppfwM_q19",
        "video_id": "mqGHL6ppfwM",
        "part": 3,
        "question": "Five validations?",
        "transcript": "I would say is I do not really remember it but I think there was time let us see I do not I do not have any idea but yeah I remember they they taught me about like how to set goals but I it is really it is really vague for me.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["vague"],
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
            "flexibility": "moderate",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "high",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Hesitation/filler dominant.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Natural."
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
        "id": 0, "sample_id": "pbx96FjvLp4_q01",
        "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Name?",
        "transcript": "my name is Hunan and you can call me. Yeah.",
        "word_count": 10,
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
        "grammar_reason": "Basic. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q02",
        "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Ready?",
        "transcript": "Yes.",
        "word_count": 1,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["fragment"]
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
        "grammar_reason": "Basic. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q03",
        "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Like about room?",
        "transcript": "I think I really love my bedroom because this is my room to be honest. And I really love it because when I stay in my room like I can stay in my hour, I can do everything I want at that room. I do my homework and sometimes I always in the time in my room.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["homework"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["word_choice_error"],
            "vocabulary": ["meaning_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'stay in my hour' (spend my time? stay for hours?). 'at that room' (in). 'always in the time' (spend time?)."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex sentences attempted."
            },
            "vocabulary": {
                "why_not_7": "Meaning errors.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Meaning errors. Band 6.",
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
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

    print(f"Append complete. Added {count} new samples. (Skipped duplicates/invalid).")

except Exception as e:
    print(f"Error writing to file: {e}")
