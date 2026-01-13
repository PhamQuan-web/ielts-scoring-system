import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 214 ---
# Total Samples: 20
# Samples Analyzed:

# 1. pbx96FjvLp4_q04 (Band 6.5)
# Transcript: "if I have a chance, I would definitely add a library... book aholic... opportunity... add library... it is make my room more comfortable and I can reflect my personality."
# Analysis:
# - Grammar: "it is make my room" (it makes / it will make). "add library" (add a library).
# - Vocabulary: "bookaholic" (informal/creative). "reflect my personality".
# - Verdict: Band 6.5. Good vocab, structural errors.

# 2. pbx96FjvLp4_q05 (Band 6.5)
# Transcript: "turn out for study abroad... place that have a lots of memories..."
# Analysis: "turn out for" (plan to? aim to?). "place that have" (has).
# - Verdict: Band 6.0/6.5.

# 3. pbx96FjvLp4_q06 (Band 6.5)
# Transcript: "we has a nice garden..."
# Analysis: "we has" (have).
# - Verdict: Band 6.0. Basic error.

# 4. pbx96FjvLp4_q07 (Band 6.5)
# Transcript: "usually watering the plants... enjoy the sunlight... feel this is very comfortable."
# Analysis: "usually watering" (water).
# - Verdict: Band 6.0.

# 5. pbx96FjvLp4_q08 (Band 6.5)
# Transcript: "great to has both... convenience for us to has a vegetable... fresher than you buy it outside..."
# Analysis: "to has" (have). "convenience" (convenient). "has a vegetable" (have vegetables).
# - Verdict: Band 6.0. Repeated basic errors ("to has").

# 6. pbx96FjvLp4_q10 (Band 6.5)
# Transcript: "best horror movie the movie that I watch."
# Analysis: Repetitive. "movie that I watch" (watched / have watched).
# - Verdict: Band 6.0.

# 7. pbx96FjvLp4_q11 (Band 6.5)
# Transcript: "film is was very perfect... really love watch horror films... make me feel terrifying... film was terrify... I cannot stop..."
# Analysis: "film is was". "love watch" (watching). "feel terrifying" (terrified). "film was terrify" (terrifying).
# - Verdict: Band 6.0. Confusion between -ing/-ed adjectives.

# 8. pbx96FjvLp4_q12 (Band 6.5)
# Transcript: "it is will be decreased... convenience way... prefer at home to watch... has a lots of apps... very convenience for them..."
# Analysis: "it is will be". "convenience way" (convenient). "prefer at home" (prefer to watch at home).
# - Verdict: Band 6.0.

# 9. pbx96FjvLp4_q13 (Band 6.5)
# Transcript: "continue decrease... value convenience streaming that is still continue... attract audience... quantity is more is more modern."
# Analysis: "continue decrease" (decreasing). "that is still continue" (continuing). "quantity" (quality?).
# - Verdict: Band 6.0.

# 10. pbx96FjvLp4_q14 (Band 6.5)
# Transcript: "collect the informations... easier than the to use the fake situation... easier to make the content that believable... disadvantage are... make their frames like more dramatic to be are suitable."
# Analysis: "informations" (uncountable). "easier than the to use". "to be are suitable" (to be suitable).
# - Verdict: Band 6.0.

# 11. pbx96FjvLp4_q15 (Band 6.5)
# Transcript: "need to be free... need to age rating... need to freed them... protect from the inappropriate films like the violence or hierms."
# Analysis: "need to age rating" (use age ratings?). "need to freed" (free). "hierms" (harm?).
# - Verdict: Band 6.0.

# 12. UVbffyA4oko_q02 (Band 6.5)
# Transcript: "Sim City is a biggest city in Vietnam."
# Analysis: "Sim City" (HCM City?). "a biggest" (the biggest).
# - Verdict: Band 6.0.

# 13. UVbffyA4oko_q03 (Band 6.5)
# Transcript: "I guess that is a 20 or 21 years because I am born here."
# Analysis: "I am born here" (was born). "a 20" (20).
# - Verdict: Band 6.0.

# 14. UVbffyA4oko_q04 (Band 6.5)
# Transcript: "private house... lots of privacy... I will reading book... most time I will do self studies... exactly about quantum mechanics."
# Analysis: "I will reading" (read). "self studies" (self-study). "exactly about" (specifically).
# - Vocabulary: "quantum mechanics".
# - Verdict: Band 6.5 (Vocab bump).

# 15. UVbffyA4oko_q05 (Band 6.5)
# Transcript: "My hotel is enough of Hojim... beautiful sceneries."
# Analysis: "My hotel" (hometown? The question was hometown). "enough of Hojim" (North of HCM?). "sceneries" (scenery is uncountable usually).
# - Verdict: Band 6.0.

# 16. UVbffyA4oko_q07 (Band 6.5)
# Transcript: "memories is contained... object will to remind you..."
# Analysis: "memories is contained" (contained within). "will to remind" (will remind).
# - Verdict: Band 6.0.

# 17. UVbffyA4oko_q08 (Band 6.5)
# Transcript: "family's related things... relate to your family member... best thing you you will to protect..."
# Analysis: "family's related things" (family-related). "will to protect" (want to protect?).
# - Verdict: Band 6.0.

# 18. UVbffyA4oko_q09 (Band 6.5)
# Transcript: "give you a specific answers... depend depends on your point of view... is part probably true... make the compare with another people... make the people in now day will to more you know more care about their appearance..."
# Analysis: "specific answers" (answer). "make the compare" (comparison). "people in now day" (nowadays). "will to more... care" (care more).
# - Verdict: Band 6.0.

# 19. UVbffyA4oko_q10 (Band 6.5)
# Transcript: "Can give you the answer... is is probably true... keep that object as properties... memory object..."
# Analysis: "Can give" (I can't give?). "properties" (assets?). "memory object" (memento).
# - Verdict: Band 6.0.

# 20. UVbffyA4oko_q11 (Band 6.5)
# Transcript: "Equation. Abstract, transparent, has a specific answer."
# Analysis: List of words.
# - Verdict: Valid (Band 6.5).

scored_samples = [
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q04", "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Change house?",
        "transcript": "if I have a chance, I would definitely add a library into my house because I am a book aholic. Yeah, I think if I have an opportunity, I will add library and it is make my room more comfortable and I can reflect my personality.",
        "word_count": 43,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["bookaholic", "reflect my personality"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'it is make my room' (it makes). 'add library' (a library)."
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
                "why_not_7": "Structural errors.",
                "why_not_5": "Complex structures."
            },
            "vocabulary": {
                "why_not_8": "Limited range.",
                "why_not_6": "Creative ('bookaholic')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Creative vocab. Band 7.",
        "grammar_reason": "Errors present. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q05", "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Live long?",
        "transcript": "I think so. At least I turn out for study abroad and this is a place that have a lots of memories and yeah I really love it.",
        "word_count": 27,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["study abroad"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["phrasing_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'turn out for' (plan to?). 'place that have' (has)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "moderate",
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
                "why_not_7": "Basic errors.",
                "why_not_5": "Understandable."
            },
            "vocabulary": {
                "why_not_7": "Unclear phrasing.",
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
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q06",
        "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Garden?",
        "transcript": "Of course. we has a nice garden at the back of my house and my parents grow some flowers and vegetables there.",
        "word_count": 21,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["nice garden"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'we has' (have)."
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
                "why_not_7": "Basic agreement error.",
                "why_not_5": "Clear meaning."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate than simple sentences.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Basic. Band 6.",
        "grammar_reason": "'we has' is a Band 5 error (basic sentence structure error). Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q07",
        "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Enjoy gardening?",
        "transcript": "Of course. after school I usually watering the plants and sometime in the morning I also enjoy the sunlight. Yeah, I feel this is very comfortable.",
        "word_count": 25,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["enjoy the sunlight"],
            "grammar_structures_used": ["compound_sentence"]
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
            "reason": "'usually watering' (water)."
        },
        "grammar_profile": {
            "complexity_level": "low",
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
                "why_not_7": "Verb form error.",
                "why_not_5": "Clear."
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
        "vocab_reason": "Adequate. Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q08",
        "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Veg or flowers?",
        "transcript": "This is really hard for me to choose, but I think this is great to has both because this is very convenience for us to has a vegetable in our garden for easier to eat and it is also fresher than you buy it outside and flowers for us to relax and we can enjoy the moment in the garden here.",
        "word_count": 60,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["enjoy the moment"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'to has both' (have). 'very convenience' (convenient). 'to has a vegetable' (have)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent basic errors.",
                "why_not_5": "Complex attempts."
            },
            "vocabulary": {
                "why_not_7": "Word form errors.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Word form errors. Band 6.",
        "grammar_reason": "Basic errors repeated ('to has'). Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q10",
        "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Movie share?",
        "transcript": "I think this is the best horror movie the movie that I watch.",
        "word_count": 13,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["horror movie"],
            "grammar_structures_used": ["relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'movie that I watch' (watched)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "high",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Tense error.",
                "why_not_5": "Clear."
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
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q11",
        "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Dislike movie?",
        "transcript": "I think the film is was very perfect. Yeah. Because I really love watch horror films but any films before that did not carry that make me feel terrifying but that film was terrify watching M8 and to be honest I cannot stop I can stop watching it. So.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'film is was'. 'love watch' (watching). 'feel terrifying' (terrified). 'film was terrify' (terrifying)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Sentences attempted."
            },
            "vocabulary": {
                "why_not_7": "Confusion -ing/-ed.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Confusion. Band 6.",
        "grammar_reason": "Frequent disruptive errors. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q12",
        "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Cinema popularity?",
        "transcript": "I think it is will be decreased because right now nowadays people prefer that it is convenience convenience way to watch TV. So I think they will prefer at home to watch films and right now it has a lots of apps are growing and this is very convenience for them to watch it at home like Netflix or HBO Max. Yeah I think so this is a reason why the cinemas will decrease in recent years.",
        "word_count": 76,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["apps", "convenience"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'it is will be decreased'. 'convenience way' (convenient). 'prefer at home to watch' (prefer to watch at home)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Meaning clear."
            },
            "vocabulary": {
                "why_not_7": "Word form errors.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Word form errors. Band 6.",
        "grammar_reason": "Frequent errors. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q13",
        "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Trend future?",
        "transcript": "I think they it will continue decrease because the con because people value convenience streaming that is still continue but I think some some type of film like horror films like the conjuring this that will attract audience because of the big screen and the sound system of the cinema that is better than at home. So I feel this is make people prefer to go to the cinema to watch the harm films. Yeah. Because of the quantity is more is more modern.",
        "word_count": 83,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["sound system", "attract audience", "big screen"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'continue decrease' (decreasing). 'streaming that is still continue' (continuing). 'quantity is more modern' (quality?)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex attempts."
            },
            "vocabulary": {
                "why_not_7": "Meaning error ('quantity').",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors but good collocations ('sound system'). Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q14",
        "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Real life films?",
        "transcript": "The first is the advantages like the director will collect the informations. I think it is easier than the to use the fake situation like they can easier to make the content that believable and can easier to educate the viewers but the disadvantage are that they they need to change the content and the informations to make their frames like more dramatic to be are suitable.",
        "word_count": 66,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["educate the viewers", "dramatic"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["word_form_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'informations' (uncountable). 'easier than the to use'. 'frames' (films?). 'to be are suitable' (to be suitable)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Attempts complex."
            },
            "vocabulary": {
                "why_not_7": "Errors ('frames').",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Adequate. Band 6.",
        "grammar_reason": "Frequent disruptive errors. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "pbx96FjvLp4_q15",
        "video_id": "pbx96FjvLp4",
        "part": 1,
        "question": "Censorship?",
        "transcript": "I think we need to be free. Yeah. Instead of strict censorship, the government or the director need to age rating instead of treat. Yeah. Because we need to freed them to choose. that some young people need to protect from the inappropriate films like the violence or hierms.",
        "word_count": 47,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["strict censorship", "inappropriate films", "age rating"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'need to age rating' (use age ratings). 'need to freed' (free). 'hierms' (harm/horrors?)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors.",
                "why_not_5": "Complex structures."
            },
            "vocabulary": {
                "why_not_7": "Unclear words.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good terms 'strict censorship'. Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "UVbffyA4oko_q02",
        "video_id": "UVbffyA4oko",
        "part": 1,
        "question": "Where live?",
        "transcript": "You know, Sim City is a biggest city in Vietnam.",
        "word_count": 10,
        "analysis_metadata": {
            "grammar_error_patterns": ["article"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'a biggest' (the biggest)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "moderate",
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
                "why_not_7": "Basic error.",
                "why_not_5": "Clear."
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
        "grammar_reason": "Error. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "UVbffyA4oko_q03",
        "video_id": "UVbffyA4oko",
        "part": 1,
        "question": "How long?",
        "transcript": "I guess that is a 20 or 21 years because I am born here.",
        "word_count": 13,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'I am born here' (was born)."
        },
        "grammar_profile": {
            "complexity_level": "low",
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
                "why_not_7": "Tense error.",
                "why_not_5": "Clear."
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
        "grammar_reason": "Error. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "UVbffyA4oko_q04",
        "video_id": "UVbffyA4oko",
        "part": 1,
        "question": "Accommodation?",
        "transcript": "I guess that is private house. Private house because in there I have a lots of privacy and I have a lot of private so what kind of accommodation would you like to live in? I think I will reading book and sleeping and cooking but u most time I will do self studies especially about my my favorite subject exactly about quantum mechanics. So.",
        "word_count": 64,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form", "article"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["quantum mechanics", "self studies"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'I will reading' (read). 'private house' (a private house)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Meaning clear."
            },
            "vocabulary": {
                "why_not_8": "Limited range outside topic.",
                "why_not_6": "Advanced term 'quantum mechanics'."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Topic vocab good. Band 7.",
        "grammar_reason": "Basic errors. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "UVbffyA4oko_q05",
        "video_id": "UVbffyA4oko",
        "part": 1,
        "question": "Hometown?",
        "transcript": "My hotel is enough of Hojim and there is a beautiful place with Kai people, friendly people and beautiful sceneries.",
        "word_count": 19,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["friendly people"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'hotel' (hometown). 'sceneries' (scenery)."
        },
        "grammar_profile": {
            "complexity_level": "low",
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
                "why_not_7": "Basic errors.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Errors.",
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
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "UVbffyA4oko_q07",
        "video_id": "UVbffyA4oko",
        "part": 1,
        "question": "Keep objects?",
        "transcript": "Well, I think I think it is not about the value of that object. it is about memories is contained. u maybe you do not you do not want to forget someone and this object will to remind you about this person the the story behind it I guess.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["value", "story behind it"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'memories is contained' (contained within). 'will to remind' (will remind)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex attempts."
            },
            "vocabulary": {
                "why_not_7": "Limited range.",
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
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "UVbffyA4oko_q08",
        "video_id": "UVbffyA4oko",
        "part": 1,
        "question": "Value most?",
        "transcript": "I think this is a family's related things because you know it is maybe a gift or a pictures or anything else relate to your family member. because in my country family is always the best the best thing you you will to protect maybe sometime.",
        "word_count": 46,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["family member"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["word_form_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'family's related' (family-related). 'will to protect' (want to protect?)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Clear."
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
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "UVbffyA4oko_q09",
        "video_id": "UVbffyA4oko",
        "part": 1,
        "question": "Materialistic?",
        "transcript": "it is hard to give you a specific answers. It depend depends on your point of view. But with me is is part probably true because with the social media a lot of people can make the compare with another people what they have and and that is make the people in now day will to more you know more care about their appearance or they they what they have. Okay, I have a final question.",
        "word_count": 75,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["social media", "point of view", "appearance"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'specific answers' (answer). 'make the compare' (comparison). 'will to more... care' (care more)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex attempts."
            },
            "vocabulary": {
                "why_not_7": "Word form errors.",
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
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "UVbffyA4oko_q10",
        "video_id": "UVbffyA4oko",
        "part": 1,
        "question": "Why?",
        "transcript": "Can give you the answer because it is is a hard question, but I think is is probably true. Maybe it depends on your purpose. when you want to keep that object as properties, you know, maybe it is a gold or diamonds to keep balance as another type of kind of money. you want to keep that object is a memory object to remind you about something. Okay, good job. that is just the end of the test. Thank you for your attendance.",
        "word_count": 84,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["memory object", "balance"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["meaning_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Can give' (I can't give). 'properties' (assets). 'memory object' (memento)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Attempts complex."
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
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "UVbffyA4oko_q11",
        "video_id": "UVbffyA4oko",
        "part": 1,
        "question": "Abstract?",
        "transcript": "Equation. Abstract, transparent, has a specific answer.",
        "word_count": 7,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["equation", "abstract", "transparent"],
            "grammar_structures_used": ["list"]
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
                "why_not_7": "List.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_8": "Limited.",
                "why_not_6": "Good terms."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good terms. Band 7.",
        "grammar_reason": "Fragment. Band 6.",
        "vocabulary": 7,
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
