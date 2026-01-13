import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 224 ---
# Total Samples: 20
# Samples Analyzed:

# 1. w6n1M3NJoG4_q05 (Band 5.5)
# Transcript: "used to draw something... punished by not drawing well."
# Analysis: "punished by not drawing well" (for not drawing well?).
# - Verdict: Band 5.5.

# 2. w6n1M3NJoG4_q06 (Band 5.5)
# Transcript: "traumatic experience for me... put you off... tell me swimming..."
# Analysis: "traumatic experience" (strong vocab).
# - Verdict: Band 5.5.

# 3. w6n1M3NJoG4_q07 (Band 5.5)
# Transcript: "most difference... really salty for the swimmers... cannot go farther to whether they want to swim deeper or not."
# Analysis: "most difference" (biggest difference). "cannot go farther to whether" (?).
# - Verdict: Band 5.0.

# 4. w6n1M3NJoG4_q08 (Band 5.5)
# Transcript: "prefer go swimming pool... distance to go ocean is quite burdensome..."
# Analysis: "prefer go" (prefer going to). "burdensome" (good word, but maybe "too far"?).
# - Verdict: Band 5.5.

# 5. w6n1M3NJoG4_q10 (Band 5.5)
# Transcript: "more likely to be popular... choose the past to be more general... can be for God among the audience..."
# Analysis: "choose the past" (path?). "for God" (forgotten?).
# - Verdict: Band 5.5. ASR/Pronunciation issues.

# 6. w6n1M3NJoG4_q11 (Band 5.5)
# Transcript: "gain some entrance interest... forex example... private space... too interested in them."
# Analysis: "entrance interest" (interest?). "forex" (for).
# - Verdict: Band 5.5.

# 7. w6n1M3NJoG4_q12 (Band 5.5)
# Transcript: "take more advantage... school president... home room teacher..."
# Analysis: "take more advantage" (get more advantages?).
# - Verdict: Band 5.5.

# 8. w6n1M3NJoG4_q14 (Band 5.5)
# Transcript: "top-down structures company especially."
# Analysis: "top-down structures". Good term.
# - Verdict: Band 5.5.

# 9. w6n1M3NJoG4_q16 (Band 5.5)
# Transcript: "pause is my habit... improve my speaking skills... native language... put a mask on... test face..."
# Analysis: Candidate speaking about speaking test.
# - Verdict: INVALID (Skip - meta discussion/feedback).

# 10. FnNVwUOszos_q01 (Band 8.0)
# Transcript: "fat big nuke we... call me queen... from Hanoi..."
# Analysis: Simple intro.
# - Verdict: Band 8.0.

# 11. FnNVwUOszos_q02 (Band 8.0)
# Transcript: "depends on what I am doing... wear something casual... hang out with my friends... swept with work... browsing online... sundress which flutter printed pattern... stylet yet functional... fashion conscious... self-centered... identify themselves distinctively..."
# Analysis:
# - Grammar: "swept with work" (swamped with work?). "stylet" (stylish). "flutter printed pattern" (floral?).
# - Vocabulary: "fashion conscious", "self-centered", "distinctively".
# - Verdict: Band 8.0. Some slips ("swept", "stylet"), but strong vocab.

# 12. FnNVwUOszos_q04 (Band 8.0)
# Transcript: "About what you are going to say."
# Analysis: EXAMINER SPEECH.
# - Verdict: INVALID (Skip).

# 13. UuNgt9Zjh4Y_q01 (Band 8.5)
# Transcript: "favorite teacher... familiar with her... engaged... technical... enjoyed the reading bit... did not get to experience the University... reunion..."
# Analysis: Natural flow. "reading bit".
# - Verdict: Band 8.5.

# 14. UuNgt9Zjh4Y_q02 (Band 8.5)
# Transcript: "Countryside... not as much modes of Transport... prefer taking public transportation..."
# Analysis: "modes of Transport".
# - Verdict: Band 8.5.

# 15. UuNgt9Zjh4Y_q03 (Band 8.5)
# Transcript: "ice bath... bucket of Ice... Dubai skyline... Birch Khalifa... cloud seating..."
# Analysis: "Birch Khalifa" (Burj Khalifa). "cloud seating" (seeding).
# - Verdict: Band 8.5.

# 16. UuNgt9Zjh4Y_q04 (Band 8.5)
# Transcript: "roads were flooded... took us two hours..."
# Analysis: Good.
# - Verdict: Band 8.5.

# 17. UuNgt9Zjh4Y_q05 (Band 8.5)
# Transcript: "cabin crew... flights might be delayed... have an impact of in in a in a way."
# Analysis: "impact of" (on).
# - Verdict: Band 8.5.

# 18. UuNgt9Zjh4Y_q12 (Band 8.5)
# Transcript: "intonation their speech patterns are a little bit rigid and formal and robotic..."
# Analysis: EXAMINER FEEDBACK.
# - Verdict: INVALID (Skip).

# 19. eAz-JoMrXJE_q01 (Band 6.0)
# Transcript: "worked as a video editor... very tough actually... very busy and so urgent things to report..."
# Analysis: "so urgent things" (many urgent things).
# - Verdict: Band 6.0.

# 20. eAz-JoMrXJE_q03 (Band 6.0)
# Transcript: "innovative at the time... do internet on the road... remember of the first moment..."
# Analysis: "do internet" (use the internet). "remember of" (remember).
# - Verdict: Band 6.0.

scored_samples = [
    {
        "id": 0, "sample_id": "w6n1M3NJoG4_q05", "video_id": "w6n1M3NJoG4",
        "part": 1,
        "question": "Drawing?",
        "transcript": "I used to draw something but when I was young I was punished by not drawing well.",
        "word_count": 18,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["punished"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'punished by not drawing' (for)."
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
                "why_not_6": "Preposition error.",
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
        "id": 0, "sample_id": "w6n1M3NJoG4_q06",
        "video_id": "w6n1M3NJoG4",
        "part": 1,
        "question": "Traumatic?",
        "transcript": "I think so. You should not. You should still be trying it if you enjoy doing it. Tell me. swimming, that is also a hobby to some people.",
        "word_count": 28,
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
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "w6n1M3NJoG4_q07",
        "video_id": "w6n1M3NJoG4",
        "part": 1,
        "question": "Pool vs Ocean?",
        "transcript": "Yes. The most difference between swimming pool and the beach is the water I think. So the the ocean water is really salty for the swimmers. So they cannot go farther to whether they want to swim deeper or not.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["salty"],
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
            "reason": "'most difference' (biggest). 'go farther to whether' (?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Structure breakdown.",
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
        "id": 0, "sample_id": "w6n1M3NJoG4_q08",
        "video_id": "w6n1M3NJoG4",
        "part": 1,
        "question": "Prefer?",
        "transcript": "In my opinion I think they prefer go swimming pool because since most people live in soul I think for them the distance to go ocean is quite burdensome for them. Yeah. And that is the reason I guess.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["burdensome"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'prefer go' (prefer going). 'distance to go ocean' (to the ocean). 'burdensome' (too far?)."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors.",
                "why_not_5": "Complex attempts."
            },
            "vocabulary": {
                "why_not_7": "Word choice.",
                "why_not_5": "Good word 'burdensome'."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good word 'burdensome' lifts it. Band 6.",
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "w6n1M3NJoG4_q10",
        "video_id": "w6n1M3NJoG4",
        "part": 3,
        "question": "Popular children?",
        "transcript": "It is more likely to be popular, but it depends on their future career path. For example, when they choose to be a movie star, I think they can be more popular. But when when they choose the past to be more general, I think they can be for God among the audience. Mhm.",
        "word_count": 53,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["career path", "movie star"],
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
            "reason": "'choose the past' (path?). 'for God' (forgotten? a god?)."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Good.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Unclear words due to pron.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors. Band 6.",
        "grammar_reason": "Accurate mostly. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "w6n1M3NJoG4_q11",
        "video_id": "w6n1M3NJoG4",
        "part": 3,
        "question": "Disadvantages popularity?",
        "transcript": "Yes, definitely. I think they can gain some entrance interest among the friends even they do not want to be they do not want to gain much interest about forex example their families or some more private space that people are maybe too interested in them. Yes, too interested.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["private space"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'entrance interest' (intense interest?). 'forex' (for)."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Good.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Word choice errors.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors. Band 6.",
        "grammar_reason": "Good. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "w6n1M3NJoG4_q12",
        "video_id": "w6n1M3NJoG4",
        "part": 3,
        "question": "Benefits popularity?",
        "transcript": "I think they can take more advantage when they wanted to be a school president. And I guess their home room teacher can take more time to take care of them. Okay. let us say you go out of school.",
        "word_count": 40,
        "analysis_metadata": {
            "grammar_error_patterns": ["collocation"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["school president", "home room teacher"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["collocation_minor"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'take more advantage' (have an advantage)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Good.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Collocation issues.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Adequate. Band 6.",
        "grammar_reason": "Good. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "w6n1M3NJoG4_q14",
        "video_id": "w6n1M3NJoG4",
        "part": 3,
        "question": "Important?",
        "transcript": "H I think it depends on the job but most of all I think the real good relationship with the coworker is the most effective way in Korea I guess for their top-down structures company especially.",
        "word_count": 36,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["top-down structures", "effective way", "coworker"],
            "grammar_structures_used": ["complex_sentences"]
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
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Good.",
                "why_not_6": "Error free."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Good term 'top-down'."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good terms. Band 7.",
        "grammar_reason": "Accurate. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "FnNVwUOszos_q01",
        "video_id": "FnNVwUOszos",
        "part": 1,
        "question": "Intro?",
        "transcript": "Please come in okay good morning good morning my name is Aaron what is your name my name is fat big nuke we and what can I call you you can call me queen thank you where are you from I am from Hanoi can I see some identification please here",
        "word_count": 50,
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
                "why_not_8": "Too short.",
                "why_not_6": "Accurate."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Basic. Band 7.",
        "grammar_reason": "Accurate. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "FnNVwUOszos_q02",
        "video_id": "FnNVwUOszos",
        "part": 1,
        "question": "Clothes?",
        "transcript": "I am going to wear what kind of clothes do you usually wear well it depends on what I am doing really if I go to work I would wear something casual like shirts or jeans if you hang out with my friends putting on a dress would not be a bad choice right and if I stay at home I just wear something comfortable like t-shirts or shorts where do you usually buy your clothes I used to go to trendy shops when I was a student but now since I have to work and I have little time for shopping I just go to a shopping center or department store and just get everything from there have you ever bought clothes online is of course as I mentioned before I am all swept with work right now so browsing online to shop is very convenient and I can have all my clothes shipped directly to my house what is your favourite item of clothing well that is tough question I think it also depends on the weather if the weather is kind of hot it would be perfect if you put on a sundress which flutter printed pattern on it and if the weather gets a bit chilly I would definitely go for a long one coat which is stylet yet functional do people from your country think fashion is important well I think they are getting more and more fashion conscious than ever I think this is because now they are more self-centered and they want to identify themselves distinctively from other people so they kind of choose to express themselves through the way they dress the more trendy and fashionable the clothes are the more confident they will become I suppose.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["fashion conscious", "self-centered", "distinctively", "browsing online"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'swept with work' (swamped). 'flutter printed' (floral?). 'stylet' (stylish)."
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "high",
            "flexibility": "sustained",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Minor slips.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "Errors ('stylet', 'swept').",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level but errors. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "UuNgt9Zjh4Y_q01",
        "video_id": "UuNgt9Zjh4Y",
        "part": 1,
        "question": "High school?",
        "transcript": "Let us start off by talking about high school who was your favorite teacher in high school I think my favorite teacher in high school was Miss Malika she was my second grade teacher and I think she eventually like at the later stages she became my eighth grade teacher as well so I was very familiar with her and she remembered me so we had good memories together what was your favorite subject in high school my favorite subject would be I think was English because I liked reading stories and novels and it just kept me engaged wherein like with the other subjects you had to it was more technical by enjoyed the reading bit and I still do enjoy reading so i' say English do you ever miss being in high school I do actually because I started working very early I did not get to experience the University or college so the memories that I have or the friends I have is from high school and I do think about times where we could just go back and have a reunion and like have that moment again.",
        "word_count": 182,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["familiar with", "engaged", "reunion"],
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
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good.",
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
        "vocab_reason": "Natural. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "UuNgt9Zjh4Y_q02",
        "video_id": "UuNgt9Zjh4Y",
        "part": 1,
        "question": "Private car?",
        "transcript": "is driving a private car popular in your country I would say in Countryside it is quite popular as there is not as much modes of Transport as in the big cities so in the countryside it is quite popular wherein in the big cities people prefer taking public transportation it is faster it is convenient.",
        "word_count": 54,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["modes of transport", "public transportation"],
            "grammar_structures_used": ["complex_sentences"]
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
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "UuNgt9Zjh4Y_q03",
        "video_id": "UuNgt9Zjh4Y",
        "part": 2,
        "question": "Perfect weather?",
        "transcript": "To do on the weekend like I mentioned earlier I like to see my friends try different restaurant Cafe or an activity just last weekend I went to try this ice bath you just jump into or bucket of Ice so just yeah try different things describe a day when you thought the weather is perfect where we I was inai a couple of months ago just when the summer was about to end there was this day when I was just standing in my balcony it was bit cloudy that day and then like few minutes later I saw the lightning and the thunderstorm and it just got darker and then we I was S standing in my balcony and I saw the lightning and I have the whole view of jabai skyline so I could see the Birch Khalifa the Dubai frame and I saw the lightning on top of like right on top of Birch Khalifa which was beautiful I recorded it and I posted on Instagram and then I saw a lot of people were posting the same stories but from different places a friend of mine came over we had a glass of wine on the balcony and then it started to rain like heavily rain heavily so thunderstorm rain and it just not very common to see that in Dubai that is why I thought the weather was perfect because it is always hot and sunny and humid and as soon as like the season starts to change I think they do something called cloud seating where then they make it rain apparently so it was very beautiful to see the rain we had a nice day nice evening in.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["ice bath", "skyline", "cloud seeding", "humid"],
            "grammar_structures_used": ["complex_sentences", "past_tense"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'cloud seating' (cloud seeding). 'Birch Khalifa' (Burj Khalifa)."
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
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "Minor error 'seating'.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level. Band 8.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 8,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "UuNgt9Zjh4Y_q04",
        "video_id": "UuNgt9Zjh4Y",
        "part": 2,
        "question": "Perfect weather cont?",
        "transcript": "The balcony having glass of wine looking at the beautiful weather the traffic was very crazy by the way the roads were flooded and I think like a lot of we ordered some food by the way and it took us two hours to get the food the deliveries.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["flooded", "traffic"],
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
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 8,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "UuNgt9Zjh4Y_q05",
        "video_id": "UuNgt9Zjh4Y",
        "part": 3,
        "question": "Weather affect jobs?",
        "transcript": "Not easy to use public transportation or walk around because when it is just so hot so I suppose they would hate the hot climate more than the cold yeah what jobs can be affected by different weather conditions a lot of jobs related to transport I feel will be affected driving I would say taxis or or buses even the flights Pilots or cabin crew when the weather is not right the flights might be delayed and then if it is raining the the taxis would not be able to Dy because of the water or the floods so I think a lot of Transport related jobs and even food for that matter like deliveries all the delivery u companies they would have an impact of in in a in a way.",
        "word_count": 133,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["cabin crew", "delayed", "impact"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["preposition_error"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'impact of' (on)."
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
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Minor prep error.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good range. Band 8.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 8,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "eAz-JoMrXJE_q01",
        "video_id": "eAz-JoMrXJE",
        "part": 1,
        "question": "Work?",
        "transcript": "I am not working right now, but I had worked as a video editor and videographer. and I usually edited news videos and it was very tough actually because I it was very busy and so urgent things to report. So yeah, I really but I really enjoyed the job.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["videographer", "urgent things"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["phrasing_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'so urgent things' (many urgent things)."
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
                "why_not_7": "Phrasing error.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Good.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good. Band 6.",
        "grammar_reason": "Phrasing error. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "eAz-JoMrXJE_q03",
        "video_id": "eAz-JoMrXJE",
        "part": 1,
        "question": "First mobile?",
        "transcript": "I do not really remember but I remember the first moment that I used iPhone. I think I thought it was very innovative at the time and and it was it was very useful to me to that I could do internet on the road. So I really remember of the first moment. Mhm.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["collocation", "preposition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["innovative"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": ["collocation_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'do internet' (use the internet). 'remember of' (remember)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Collocation errors.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Collocation errors. Band 6.",
        "grammar_reason": "Errors. Band 6.",
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
