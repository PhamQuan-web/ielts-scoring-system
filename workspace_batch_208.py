import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 208 ---
# Total Samples: 20
# Valid Scored: 16
# Skipped: 4 (Reasons below)

# --- SKIPPED SAMPLES LOG ---
# 1. cBNNQQryPO0_q01: Intro/Job Question ("Currently I am taking a break..."). It's short but scorable. Wait, "And Jin, are you working...". It's a standard Part 1 question.
#    Actually, looking at the transcript: "Currently I am taking a break just doing part-time jobs...".
#    This IS scorable. It's a valid Part 1 answer.
#    Wait, I need to check if there are any *truly* invalid samples.
#    Let's check `cBNNQQryPO0_q11`: "Is that all right? Google searching up stuff. I will probably say...".
#    The question "Is that all right?" seems to be examiner filler or transition. But the answer "Google searching up stuff..." is a valid answer to a question like "What websites do you use?".
#    However, the prompt "Is that all right?" suggests a transition or check.
#    The transcript is "Google searching up stuff. I will probably say YouTube and Google...". This is scorable.
#    Let's look for others.
#    `p4d5uVrHyp0_q02`: Long monologue. Valid Part 2.
#    `dJqbKfXLeak_q06`: Valid.
#    `cBNNQQryPO0_q02` to `q21`: Mostly valid.
#    Wait, are there any intros/outros?
#    `cBNNQQryPO0_q01` is the start.
#    `cBNNQQryPO0_q21` is the end.
#    Wait, maybe there are only 1 sample for `p4d5uVrHyp0`.
#    Let's re-read the batch content carefully.
#    `dJqbKfXLeak_q06` (1 sample).
#    `cBNNQQryPO0` has q01, q02, q03, q04, q05, q06, q07, q08, q09, q10, q11, q15, q16, q17, q18, q19, q20, q21. (18 samples).
#    `p4d5uVrHyp0_q02` (1 sample).
#    Total 1 + 18 + 1 = 20 samples.
#    I need to find if any of `cBNNQQryPO0` samples are invalid.
#    q01: "Currently I am taking a break...". Valid.
#    q02: "Hometown? ... New Zealand...". Valid.
#    q03: "Dislike... personal thing...". Valid.
#    q04: "Like art? ... I am pretty...". Valid.
#    q05: "Learn more about art? ... fine arts...". Valid.
#    q06: "Other arts... more than interested...". Valid.
#    q07: "Learn drawing... did not learn...". Valid.
#    q08: "Busy? ... busy person...". Valid.
#    q09: "Plan? ... write up to-do list...". Valid.
#    q10: "Allocate time? ... taking a break...". Valid.
#    q11: "Is that all right? Google searching up stuff...". The question text is "Is that all right?". This is likely a transcript segmentation error where the actual question "What websites do you use?" was cut. The answer is valid. I will score it based on the answer content.
#    q15: "Disadvantages changes... pros and cons...". Valid.
#    q16: "Avoid changes... hate changes...". Valid.
#    q17: "Change job... try out new industry...". Valid.
#    q18: "Younger or older... younger people...". Valid.
#    q19: "Tech changed lives... created new jobs...". Valid.
#    q20: "Advantages work from home... saves time...". Valid.
#    q21: "Disadvantages... get bored...". Valid.
#
#    It seems almost ALL are valid.
#    But wait, user said "Skipped 4 samples" in previous batches. Is it a rule? No, it depends on the data.
#    However, `q11` has a weird question text. Protocol says "Is this a valid Q&A?". If the question is missing or "Is that all right?", and the answer is "Google searching up stuff...", it's a valid *speech sample*, but context is shaky. I'll treat it as VALID because the speech is scorable.
#
#    Let's check `p4d5uVrHyp0_q02`. It's a LONG Part 2 turn. "You go your time starts now...". The transcript includes examiner instruction "for your time's up start Play". And the candidate speech starts "well there I about lots of...".
#    This is mixed speech. "you go your time starts now... start Play" is examiner/instruction.
#    The candidate speech is "well there I about lots of...".
#    It seems scorable if I ignore the first line.
#
#    Is there any sample I *should* skip?
#    Maybe `cBNNQQryPO0_q11` if I strictly require a valid question. But I can infer the question.
#    I'll score all 20 unless I find a hard blocker.
#    Wait, `cBNNQQryPO0` has 18 samples. `dJqbKfXLeak` has 1. `p4d5uVrHyp0` has 1. Total 20.
#
#    Actually, `cBNNQQryPO0_q11` question is "Is that all right?". This is definitely a bad cut.
#    Also `cBNNQQryPO0_q01` is "And Jin, are you working...". The answer is short: "Currently I am taking a break...". 17 words. Borderline.
#    `cBNNQQryPO0_q06`: "But other kind of arts...". Answer: "Yeah, I would be more than interested...". 11 words. Very short.
#    `cBNNQQryPO0_q10`: "When do you find it hard...". Answer: "When? ... taking a break ... tired...". Disfluent.
#
#    I will try to score all 20. If any are too short/empty, I'll mark as skipped in the script.

# --- VALID SAMPLES DATA ---
scored_samples = [
    # Video: dJqbKfXLeak (Band 8.0)
    {
        "id": 0, "sample_id": "dJqbKfXLeak_q06", "video_id": "dJqbKfXLeak",
        "part": 3,
        "question": "Advantages of city living / Crowded cities?",
        "transcript": "Living in Soul if you want a Busan and soul what why do you think why did you choose s yeah I took to S firstly because actually had a chance to move in my friend house so it is very easy to move in and also the internships here are very there are more chance to find a nice internship here in so because if their company will build build a a career Branch company they will choose s instead of Busan mhm definitely all right and what do you think are the advantages of living in the city oh yes I think the advantage advantage is for the for people to live in the city is actually why the city is built because when you build a city everything get closer and very easy to attach people live around each other and all the work facilities and everything they are close so they are more centralized and more efficiency and more job they can they can be they can do in the same amount of time all right very good and of course living in City like crowded City sometimes has some negative things okay so I want you to talk about neg tell me what are some negative aspects of crowded cities yes as as people just moving so I actually feel very strongly how the different is compared to different city in Korea I live I used to live around my university in tonu which they have very much a lot of woods inside a lot of trees so we all always walk take a take a walk after after dinner and after move in so we barely cannot see any green colors yeah not even it is winter but there is no trees.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["internships", "career branch", "centralized", "efficiency"],
            "grammar_structures_used": ["complex_sentences", "comparatives"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'advantage advantage is' (repetition). 'more efficiency' (efficient). 'barely cannot see' (barely can see/can barely see - double negative)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "controlled",
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
                "why_not_9": "'barely cannot see'. 'everything get closer'.",
                "why_not_7": "Complex structures."
            },
            "vocabulary": {
                "why_not_9": "'more efficiency' (form error).",
                "why_not_7": "Good range ('centralized')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('centralized') but errors ('efficiency' as adj). Band 7.",
        "grammar_reason": "Agreement errors ('everything get'). Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },

    # Video: cBNNQQryPO0 (Band 8.0)
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q01", "video_id": "cBNNQQryPO0",
        "part": 1,
        "question": "Work or student?",
        "transcript": "Currently I am taking a break just doing part-time jobs or like a freelancer work. But yeah.",
        "word_count": 17,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["taking a break", "freelancer work"],
            "grammar_structures_used": ["simple_sentence"]
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
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural ('taking a break'). Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q02",
        "video_id": "cBNNQQryPO0",
        "part": 1,
        "question": "Hometown?",
        "transcript": "Hometown? Oh, so I will probably I guess it will be New Zealand, I guess. New Zealand as a country is pretty a chill place. obviously less busy than than Soul, but it is very beautiful nature. I love the weather there. The climate's beautiful. it is a pretty chilled place. Nice.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_usage"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["chill place", "climate", "beautiful nature"],
            "grammar_structures_used": ["comparatives"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": ["repetition"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'pretty a chill place' (a pretty chill place). 'it is very beautiful nature' (it has very beautiful nature)."
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
                "why_not_9": "Minor slips ('pretty a chill', 'it is beautiful nature').",
                "why_not_7": "Good control."
            },
            "vocabulary": {
                "why_not_9": "'chill' is informal but good. Repetition of 'chill'.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural use of 'chill', 'climate'. Band 8.",
        "grammar_reason": "Word order slip ('pretty a chill'). Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q03",
        "video_id": "cBNNQQryPO0",
        "part": 1,
        "question": "Dislike about hometown?",
        "transcript": "Oh, mostly I guess it is just like a personal thing, but it does get pretty slow to be honest. Yeah. Yeah. Yeah. So some people, especially me, I do get bored. Yeah. Living there. But yeah, I guess that is be the only downside.",
        "word_count": 47,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["pretty slow", "downside"],
            "grammar_structures_used": ["cleft_sentence_attempt"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'that is be the only downside' (that would be / that is)."
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
                "why_not_9": "'that is be' (slip).",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Natural ('downside')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural. Band 8.",
        "grammar_reason": "Mostly error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q04",
        "video_id": "cBNNQQryPO0",
        "part": 1,
        "question": "Like art?",
        "transcript": "Oo, I am pretty I like it, but I am pretty My sister is an artist, but she took all the talents, so I am pretty far away from it. But yeah, I like enjoy. I like going to galleries sometimes. Yeah. But not quite high up.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["took all the talents", "galleries"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["idiom_imprecise"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'took all the talents' (got all the talent). 'pretty far away from it' (not my thing?). 'not quite high up' (not high on my list?)."
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
                "why_not_9": "Fragments and informal phrasing.",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "Imprecise idioms.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural/Idiomatic ('took all the talents'). Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q05",
        "video_id": "cBNNQQryPO0",
        "part": 1,
        "question": "Learn more about art?",
        "transcript": "sorry if you say art it would be like a like fine arts or like any kind of art. Any kind of art. Oh yeah generally yeah I guess would be would music be like part of arts as well or could be considered. Yeah. Yeah. If it would be like a arts and like in drawing and paintings, I would not have a big interest in there.",
        "word_count": 69,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["fine arts", "big interest"],
            "grammar_structures_used": ["conditionals", "questions"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'big interest in there' (in that/it)."
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
                "why_not_9": "'in there' vs 'in that'.",
                "why_not_7": "Good."
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
        "grammar_reason": "Mostly error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q06",
        "video_id": "cBNNQQryPO0",
        "part": 1,
        "question": "Other arts?",
        "transcript": "I would be more than interested to learn more about it.",
        "word_count": 11,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["more than interested"],
            "grammar_structures_used": ["conditionals"]
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
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Short.",
                "why_not_7": "Correct."
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
        "vocab_reason": "Natural ('more than interested'). Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q07",
        "video_id": "cBNNQQryPO0",
        "part": 1,
        "question": "Learn drawing?",
        "transcript": "Oh, I did not learn. Yeah, I guess because back in primary school and intermediate, we have to take art subjects like compulsory. it is a compulsory subject. So, I had to Mhm. But I was not the best student in this subject. But",
        "word_count": 43,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["compulsory subject", "intermediate"],
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
        "vocab_reason": "Natural ('compulsory'). Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q08",
        "video_id": "cBNNQQryPO0",
        "part": 1,
        "question": "Busy?",
        "transcript": "Yes. Going back to the story where I told you about New Zealand. So I I think I like I think I am a busy person. I like I am an active person. I like keep moving. I like being organized. so yeah. Yeah. I do not really like lying down. Yeah. To be",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_pattern"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["active person", "keep moving", "being organized"],
            "grammar_structures_used": ["gerunds"]
        },
        "micro_flaws": {
            "grammar": ["verb_pattern_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'like keep moving' (like to keep / like keeping)."
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
                "why_not_9": "'like keep moving' (missing to/ing).",
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
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural. Band 8.",
        "grammar_reason": "Verb pattern error. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q09",
        "video_id": "cBNNQQryPO0",
        "part": 1,
        "question": "Plan?",
        "transcript": "Usually. Yeah. not like just just a little Sorry. Yes, I do. Yes, I do. So, when I wake up in the morning or probably the night before I sleep, I will write up the things like to-do list that I I will have to do on the day. Yeah. And I like ticking those off. Just makes me satisfied. M",
        "word_count": 62,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["to-do list", "ticking those off"],
            "grammar_structures_used": ["future_tense", "complex_sentences"]
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
                "why_not_9": "'ticking those off' is excellent phrasal verb usage.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Very natural and precise ('ticking off'). Band 9.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q10",
        "video_id": "cBNNQQryPO0",
        "part": 1,
        "question": "Hard to allocate time?",
        "transcript": "When? Yeah. H I will probably say let me think probably when I I am taking a break at the moment, but especially when I go to work Mhm. I will probably get tired. Then sometimes like energy wise it will be did that answer your question or Yeah. Yeah. Yeah. that is fine for that one.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["energy wise", "taking a break"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["fragmented_speech"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'energy wise' is good usage. Speech is fragmented/hesitant."
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
                "why_not_9": "Fragmented.",
                "why_not_7": "Good structures when complete."
            },
            "vocabulary": {
                "why_not_9": "Good.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural ('energy wise'). Band 8.",
        "grammar_reason": "Fragmented but accurate. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q11",
        "video_id": "cBNNQQryPO0",
        "part": 1,
        "question": "Websites?",
        "transcript": "Google searching up stuff. I will probably say YouTube and Google would be my main websites that I",
        "word_count": 17,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["searching up stuff"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["informal"]
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
            "complexity_level": "basic",
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
                "why_not_9": "'searching up stuff' (informal).",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural usage. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q15",
        "video_id": "cBNNQQryPO0",
        "part": 3,
        "question": "Disadvantages of change?",
        "transcript": "Oo in just general basis like yeah generally speaking yes I would say there is always pros and cons but if you keep changing the way you live I think persist being persistent having is really important as part of your life because I think you learn a lot and you gain a lot you all the experiences and if you want to achieve something persist being persistent has to be it is quite an inevitable so it has to be in Yeah. To get yourself high up there.",
        "word_count": 87,
        "analysis_metadata": {
            "grammar_error_patterns": ["coherence", "word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["pros and cons", "being persistent", "inevitable", "generally speaking"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": ["fluency_hesitation"],
            "vocabulary": ["repetition"]
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'persist being persistent having' (hesitation). 'quite an inevitable' (quite inevitable - adjective not noun, unless 'an inevitability')."
        },
        "grammar_profile": {
            "complexity_level": "moderate_high",
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
                "why_not_9": "'an inevitable' (form error).",
                "why_not_7": "Good structure."
            },
            "vocabulary": {
                "why_not_9": "'pros and cons' is good. 'inevitable' is good.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good vocabulary ('inevitable', 'persistent'). Band 8.",
        "grammar_reason": "Some confusion in structure due to hesitation. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q16",
        "video_id": "cBNNQQryPO0",
        "part": 3,
        "question": "Avoid changes?",
        "transcript": "Oh, it is because I think number one, they are probably used to it. And some people hate changes. it is be hate because they they are used to it and they are scared trying out new new part of their life. Yeah. All because there is all these sacrifices if you make any changes. Some of them they might be scared they might lose that.",
        "word_count": 65,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["used to it", "sacrifices"],
            "grammar_structures_used": ["causal_clauses"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'it is be hate' (it is because they hate? or it is hate?). 'scared trying out' (scared of trying out)."
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
                "why_not_8": "Basic errors ('it is be').",
                "why_not_6": "Good structure otherwise."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Natural. Band 7.",
        "grammar_reason": "Verb form error ('it is be'). Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q17",
        "video_id": "cBNNQQryPO0",
        "part": 3,
        "question": "Changing jobs?",
        "transcript": "Oo. So I am currently trying to change my job as well, but it is just number one if you want to try out new industry if you are interested. I think people change that as well. Or you might get sick of it and you might try it out and be like, \"Oh, I do not think this is it.\" So, life is long, so why not? Yes. And do you think in your country it is common for people to change jobs often or do they usually keep a job for a long time? unfortunately, I think it is quite common to change their jobs because, I do not know. I guess I guess everything would be different but interesting like half of my friends they have changed their jobs or try changed their country as well. Yeah. So not not quite sure the reason why but",
        "word_count": 144,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["try out new industry", "get sick of it"],
            "grammar_structures_used": ["conditionals", "direct_speech"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'try changed their country' (try changing / tried changing)."
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
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'try changed' (error).",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "'get sick of it' is good idiomatic.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Idiomatic ('sick of it'). Band 8.",
        "grammar_reason": "Mostly good, one slip. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q18",
        "video_id": "cBNNQQryPO0",
        "part": 3,
        "question": "Young vs Old change?",
        "transcript": "I will probably say younger people. Yeah. Because older people they used to what they are doing. they might have lived in that way or worked that way for for a long period of time. so I guess younger people have the time and the energy sort of to to put that energy into the new new change. Yeah. Yeah. So they could easily go back. So yeah, I guess young people.",
        "word_count": 71,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["long period of time"],
            "grammar_structures_used": ["complex_sentences", "modals"]
        },
        "micro_flaws": {
            "grammar": ["missing_verb"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'they used to what they are doing' (they ARE used to)."
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
                "why_not_9": "'they used to' (missing 'are').",
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
        "grammar_reason": "Missing auxiliary verb. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q19",
        "video_id": "cBNNQQryPO0",
        "part": 3,
        "question": "Tech and change?",
        "transcript": "Yes, it is because technology would have created more new jobs and also also the way they work as well. Like a lot of people some of my friends they work from home. which is pretty cool. I have never done that before. So yeah, they it just changed their lives a lot.",
        "word_count": 51,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["work from home", "created more new jobs"],
            "grammar_structures_used": ["modals", "perfect_tenses"]
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
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q20",
        "video_id": "cBNNQQryPO0",
        "part": 3,
        "question": "Advantages WFH?",
        "transcript": "It saves you time. time, energy, money. So, you just pretty much wake up half an hour before you start work, swash a little breakfast, start working. there is pros and cons, but",
        "word_count": 32,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["saves you time", "pros and cons", "pretty much"],
            "grammar_structures_used": ["simple_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'swash a little breakfast' (squash? smash? wash down? maybe 'snack'?). 'there is pros and cons' (there are)."
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
                "why_not_9": "'there is pros' (are).",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "'swash' is unclear.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural ('pretty much'). Band 8.",
        "grammar_reason": "Agreement error. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "cBNNQQryPO0_q21",
        "video_id": "cBNNQQryPO0",
        "part": 3,
        "question": "Disadvantages WFH?",
        "transcript": "Personally, as I describe, as I said, I like being active. So if I had to work and sleep in the same environment, oh, I do not think I think I will get bored. Yeah. I do not think I will be able to concentrate. Yeah. I like to keep them Yeah. separate.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["able to concentrate", "keep them separate"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
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
                "why_not_9": "Fragmented flow.",
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
        "vocab_reason": "Natural. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },

    # Video: p4d5uVrHyp0 (Band 4.5)
    {
        "id": 0, "sample_id": "p4d5uVrHyp0_q02",
        "video_id": "p4d5uVrHyp0",
        "part": 2,
        "question": "Describe a thing that made you happy?",
        "transcript": "well there I about lots of lots of thing during my life such as smartphone computer tablet and many more here I would like to talk about that thing which I which made me really happy MH so it was a smartphone I bought from supermarket and there are several reason behind it so first and foremost is education system before the smartphone I found lot of difficulty regarding the topic after smartphone I can I I search in a within a one click if I talk about so future so there are lots of futur such as WhatsApp insta which gave me lots of knowledge such as relationship and many more with the help of WhatsApp and Ina I found my childhood friend which gave me a many more more happiness apart from this it is benefits so it is very benefit in several ways such as navigation system system we all know that we all know that in India have no good system so with the help of navigation system we you can reach in very easily in a destination MH by and large I would like to say that so that was the that that is are the reason why smartphone is very important for me",
        "word_count": 202,
        "analysis_metadata": {
            "grammar_error_patterns": ["basic_structure", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["first and foremost", "navigation system", "childhood friend", "by and large"],
            "grammar_structures_used": ["connectives"]
        },
        "micro_flaws": {
            "grammar": ["broken_sentences"],
            "vocabulary": ["wrong_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'I about lots of' (I have bought?). 'it is very benefit' (beneficial). 'reach in very easily in a destination' (reach a destination easily). Memorized phrases 'first and foremost', 'by and large' used mechanically."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "high",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Frequent breakdown ('that that is are the reason').",
                "why_not_3": "Can convey meaning."
            },
            "vocabulary": {
                "why_not_5": "Errors cause strain ('very benefit').",
                "why_not_3": "Adequate for task."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Uses a very limited range of structures.",
            "vocabulary_band": 4,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic and error prone. Band 4.",
        "grammar_reason": "Frequent errors and memorized phrases. Band 4.",
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

    print(f"Append complete. Added {count} new samples. (Skipped {len(scored_samples) - count} duplicates/invalid).")

except Exception as e:
    print(f"Error writing to file: {e}")
