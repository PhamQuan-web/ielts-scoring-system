import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 223 ---
# Total Samples: 20
# Samples Analyzed:

# 1. eAz-JoMrXJE_q04 (Band 6.0)
# Transcript: "prefer texting because calling that that takes a lot of time... transmit my message exactly..."
# Analysis: "calling that that takes" (calling takes). "transmit my message" (convey?).
# - Verdict: Band 6.0.

# 2. eAz-JoMrXJE_q05 (Band 6.0)
# Transcript: "going to be sometimes be broken... ability got get lower... change the phone..."
# Analysis: "going to be sometimes be broken" (might break). "ability got get lower" (performance gets worse/battery degrades).
# - Verdict: Band 5.5/6.0.

# 3. eAz-JoMrXJE_q06 (Band 6.0)
# Transcript: "did not use smartphone... old folder phone... surf the internet... watch YouTube on the road... call to my mom..."
# Analysis: "folder phone" (flip phone). "call to my mom" (call my mom).
# - Verdict: Band 6.0.

# 4. eAz-JoMrXJE_q07 (Band 6.0)
# Transcript: "really love it... baseball... watch live baseball games on weekdays in spring season..."
# Analysis: "spring season". Good.
# - Verdict: Band 6.0.

# 5. eAz-JoMrXJE_q08 (Band 6.0)
# Transcript: "watch along because my friends do not like baseball..."
# Analysis: "watch along" (watch alone).
# - Verdict: Band 6.0.

# 6. eAz-JoMrXJE_q09 (Band 6.0)
# Transcript: "loved baseball from 10 years ago... best game was Korean series... I the fan of my team my team won..."
# Analysis: "from 10 years ago" (for 10 years / since 10 years ago). "I the fan of my team" (as a fan?).
# - Verdict: Band 6.0.

# 7. eAz-JoMrXJE_q10 (Band 6.0)
# Transcript: "football games on England... Tottenham Hotspur which is Ton Min... look forward to it..."
# Analysis: "on England" (in England). "Ton Min" (Son Heung-min).
# - Verdict: Band 6.0.

# 8. eAz-JoMrXJE_q11 (Band 6.0)
# Transcript: "dreamed about being a teacher... eager to get along... sigh open to the new world... good knowledges... doing some stuffs... happy with saying about her students..."
# Analysis: "sigh open" (eye opening?). "knowledges" (knowledge). "stuffs" (stuff). "happy with saying about" (happy talking about).
# - Verdict: Band 6.0.

# 9. eAz-JoMrXJE_q13 (Band 6.0)
# Transcript: "after graduate the school... job jobs information... envy them..."
# Analysis: "after graduate" (graduating). "job jobs" (job).
# - Verdict: Band 6.0.

# 10. eAz-JoMrXJE_q14 (Band 6.0)
# Transcript: "lowwage jobs... students do believe teachers... low quality jobs..."
# Analysis: Good flow.
# - Verdict: Band 6.0.

# 11. eAz-JoMrXJE_q15 (Band 6.0)
# Transcript: "it is half and half... parents can give provide information... what should child want to do... working on bodies... making some building... tough job... dangerous... human safety..."
# Analysis: "working on bodies" (manual labor? bodies as in construction?). "making some building" (constructing buildings).
# - Verdict: Band 6.0.

# 12. eAz-JoMrXJE_q16 (Band 6.0)
# Transcript: "desperate are most likely to get a job... not that very hard to get... men with low wages... in low condition..."
# Analysis: "low condition" (poor conditions).
# - Verdict: Band 6.0.

# 13. eAz-JoMrXJE_q17 (Band 6.0)
# Transcript: "older people had high salary jobs... struggle to get house or job... young people deserve to get high salary..."
# Analysis: "struggle to get house" (a house).
# - Verdict: Band 6.0.

# 14. eAz-JoMrXJE_q19 (Band 6.0)
# Transcript: "work as a video editor... transmit my message... get my point across... call to my mom..."
# Analysis: EXAMINER FEEDBACK / CORRECTION.
# - Verdict: INVALID (Skip).

# 15. eAz-JoMrXJE_q21 (Band 6.0)
# Transcript: "But yeah, it was definitely a good test. I will give you this. You can have a look at it after..."
# Analysis: EXAMINER OUTRO.
# - Verdict: INVALID (Skip).

# 16. 6UP3bpCtzQs_q02 (Band 6.5)
# Transcript: "will doing that... close friends... got my back... walking meet people... choose whether i want to be friends..."
# Analysis: "will doing that" (will keep doing that). "got my back" (idiom). "walking meet people" (walking and meeting).
# - Verdict: Band 6.5.

# 17. 6UP3bpCtzQs_q03 (Band 6.5)
# Transcript: "decide later... see myself in that picture... hanging around... street animal is crossing... plenty of cars are parked..."
# Analysis: "street animal" (stray?).
# - Verdict: Band 6.5.

# 18. 6UP3bpCtzQs_q04 (Band 6.5)
# Transcript: "entertaining... rock metal... mainstream music... pop culture... traditional art... not allowed... sketches caricatures... innovative... life's complications... philosophical..."
# Analysis: "rock metal". "caricatures". "philosophical".
# - Verdict: Band 6.5. High vocab but some fluency gaps.

# 19. 6UP3bpCtzQs_q06 (Band 6.5)
# Transcript: "not enough for me right now but it may improve the future of course you can improve that."
# Analysis: Very short.
# - Verdict: Valid (Band 6).

# 20. NmKZi8kqsFo_q02 (Band 8.5)
# Transcript: "Snapchat Instagram... means of communicating... new Norm... screen time function... software engineering and computer science... cacao talk... Data Center crisis... suffering... vary from age to age..."
# Analysis: "new Norm" (norm). "Data Center crisis". "vary from age to age".
# - Verdict: Band 8.5.

scored_samples = [
    {
        "id": 0, "sample_id": "eAz-JoMrXJE_q04", "video_id": "eAz-JoMrXJE",
        "part": 1,
        "question": "Texting vs Calling?",
        "transcript": "For I prefer texting because calling that that takes a lot of time. I usually call friends a for an hour. So texting also it takes time but yeah I can transmit my message exactly. So I prefer testing.",
        "word_count": 42,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["transmit"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'transmit my message' (convey/send). 'calling that that takes' (calling takes)."
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
                "why_not_7": "Minor errors.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Unnatural 'transmit'.",
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
        "id": 0, "sample_id": "eAz-JoMrXJE_q05",
        "video_id": "eAz-JoMrXJE",
        "part": 1,
        "question": "New phone?",
        "transcript": "Yes. because I I am now using iPhone 15 Pro but it is going to be sometimes be broken or the ability got get lower. So maybe I will change the phone. Mhm.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
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
            "reason": "'going to be sometimes be broken' (might break). 'ability got get lower' (performance/battery degrades)."
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
                "why_not_7": "Structure errors.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Imprecise.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Imprecise. Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "eAz-JoMrXJE_q06",
        "video_id": "eAz-JoMrXJE",
        "part": 1,
        "question": "Life change?",
        "transcript": "When I was young, I did not use smartphone. I just used old folder phone. Yeah. But I just I could just text you. I could just send text messages. But nowadays I can surf the internet, watch YouTube on the road or everywhere and I can call to my mom when I was in foreign country.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["surf the internet"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'folder phone' (flip phone). 'call to my mom' (call my mom)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Preposition errors.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Folder phone vs Flip phone.",
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
        "id": 0, "sample_id": "eAz-JoMrXJE_q07",
        "video_id": "eAz-JoMrXJE",
        "part": 1,
        "question": "Sports on TV?",
        "transcript": "Yes, I really love it. especially I really love baseball and I and I usually watch live baseball games on weekdays in spring season.",
        "word_count": 23,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["spring season", "live baseball games"],
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
                "why_not_7": "Simple.",
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
        "id": 0, "sample_id": "eAz-JoMrXJE_q08",
        "video_id": "eAz-JoMrXJE",
        "part": 1,
        "question": "Who with?",
        "transcript": "I usually watch along because my friends do not like baseball so I usually watch.",
        "word_count": 15,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["compound_sentence"]
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
            "reason": "'watch along' (alone)."
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
                "why_not_7": "Too short.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Error 'along'.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Error 'along'. Band 6.",
        "grammar_reason": "Basic. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "eAz-JoMrXJE_q09",
        "video_id": "eAz-JoMrXJE",
        "part": 1,
        "question": "Stadium?",
        "transcript": "Oh yes, of course. Because I I loved baseball from 10 years ago. So the best game was Korean series with SK and Dan. Yeah. The and that game I the fan of my team my team won the game. Yeah. Great.",
        "word_count": 42,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition", "structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["fan of my team"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'from 10 years ago' (since/for). 'I the fan of my team' (as a fan?)."
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
                "why_not_7": "Structure errors.",
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
        "id": 0, "sample_id": "eAz-JoMrXJE_q10",
        "video_id": "eAz-JoMrXJE",
        "part": 1,
        "question": "Future sports?",
        "transcript": "I am going to the UK this year. So I really want to watch football games on England. So especially Tottenham Hotspur which is Ton Min. he is in the team. So I really look forward to it.",
        "word_count": 38,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["look forward to it"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'on England' (in)."
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
                "why_not_7": "Preposition error.",
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
        "grammar_reason": "Error. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "eAz-JoMrXJE_q11",
        "video_id": "eAz-JoMrXJE",
        "part": 3,
        "question": "Useful job?",
        "transcript": "I think it is teacher. because my mom is a retired teacher and I some I also dreamed about being a teacher when I was young. I think the teacher is the people who are eager to get along with young people and they are very smart and they really want to teach something to young people and it makes young people sigh open to the new world and new trends and they can get some good knowledges from the school and but nowadays teachers are really get tired of doing some stuffs in school but they do like people because my one of my friend became teacher and she says she is very hard doing works at school but she I saw her I saw her her face really happy with saying about her students and she she really wants to be a good teacher.",
        "word_count": 147,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form", "agreement", "article"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["retired teacher", "eager to"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["word_form_error"],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'knowledges' (knowledge). 'stuffs' (stuff). 'sigh open' (eyes open?). 'happy with saying about' (talking about)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex structures."
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
        "vocab_reason": "Errors present. Band 6.",
        "grammar_reason": "Errors present. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "eAz-JoMrXJE_q13",
        "video_id": "eAz-JoMrXJE",
        "part": 3,
        "question": "Career advice?",
        "transcript": "I think I school should do that because when I was in high school I just had to study and study and study and but I wanted to know what job could I get after graduate the school graduating the school. So yeah, but I nowadays schools provide job jobs information. So I really envy them. Yes.",
        "word_count": 57,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form", "structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["envy them"],
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
            "reason": "'after graduate' (graduating). 'job jobs' (job)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Repetition/Slips.",
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
        "id": 0, "sample_id": "eAz-JoMrXJE_q14",
        "video_id": "eAz-JoMrXJE",
        "part": 3,
        "question": "Listen to teachers?",
        "transcript": "I think it really depends because teachers provide jobs in school. the the jobs are very temporary and lowwage jobs and but students do believe teachers because they want to get jobs. So even if have even if they get low quality low quality jobs I think they will believe the teachers.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["low quality", "temporary"],
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
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Simple structure.",
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
        "grammar_reason": "Good. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "eAz-JoMrXJE_q15",
        "video_id": "eAz-JoMrXJE",
        "part": 3,
        "question": "Parents input?",
        "transcript": "As I think it is half and half I think because as ch children have no information about jobs or career. So parents can give provide information of that but I think the most important is is child what should the children have what should child want to do what should a child want to do yeah and I think that is the very that is very important okay yes and what kind of jobs deserve a high salary Nowadays I think it is about IT jobs gets high high wages but I think working on bodies like such as construction or making some whatever u making some building. Yeah, they they deserve high qual high salary because it is really tough job and really dangerous and it is related to human safety. So I think it deserves the high salary.",
        "word_count": 139,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["high wages", "human safety"],
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
            "reason": "'working on bodies' (physical labor?). 'making some building' (construction)."
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Imprecise terms.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Imprecise. Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "eAz-JoMrXJE_q16",
        "video_id": "eAz-JoMrXJE",
        "part": 3,
        "question": "Jobs popular?",
        "transcript": "Yes maybe because people who are desperate are most likely to get a job in construction. Yeah, because it is not that very hard to get job, but it is really tough. Most of men men with low wages and in low condition do have a job like that.",
        "word_count": 49,
        "analysis_metadata": {
            "grammar_error_patterns": ["collocation"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["desperate", "likely to"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["collocation_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'in low condition' (poor conditions)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Minor errors.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Collocation error.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Collocation issues. Band 6.",
        "grammar_reason": "Good. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "eAz-JoMrXJE_q17",
        "video_id": "eAz-JoMrXJE",
        "part": 3,
        "question": "Who higher salary?",
        "transcript": "M I think it is younger people because in Korea nowadays older people had high salary jobs so they have they they are now living in good condition but nowadays young people have low wages jobs and uncomfortable jobs. So and they have to struggle to get house or job or good condition. So I think young people deserve to get high salary.",
        "word_count": 62,
        "analysis_metadata": {
            "grammar_error_patterns": ["article", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["struggle to get", "deserve"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'struggle to get house' (a house)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
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
                "why_not_7": "Article errors.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Repetitive.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Repetitive. Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "6UP3bpCtzQs_q02",
        "video_id": "6UP3bpCtzQs",
        "part": 1,
        "question": "Friends?",
        "transcript": "Will doing that i will be doing that forever i think do you have a lot of friends i do not have a lot of friends but my close friends are you know the ones who always support me and they got my back all the time so i do not need a lot of friends as long as they you know stay stay with me for you know all the time you know okay with whom would you like to be friends and why with no particular person i just you know walking meet people and we get to know each other so then i choose whether i want to be friends with that person or not okay so now i will give you a.",
        "word_count": 122,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["got my back", "get to know"],
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
                "why_not_8": "Minor slips.",
                "why_not_6": "Good."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Idiomatic."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Idioms. Band 7.",
        "grammar_reason": "Good. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "6UP3bpCtzQs_q03",
        "video_id": "6UP3bpCtzQs",
        "part": 1,
        "question": "Picture?",
        "transcript": "I will decide later but maybe i can see myself in that picture with my friends you know hanging around and sitting in the side of road maybe a cat or a dog or some some animal some street animal is crossing crossing the street the the you know the image plenty of cars are parked there but i do not see them.",
        "word_count": 62,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["hanging around", "street animal"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'sitting in the side' (on the side)."
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
                "why_not_8": "Preposition error.",
                "why_not_6": "Good."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
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
        "grammar_reason": "Minor error. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "6UP3bpCtzQs_q04",
        "video_id": "6UP3bpCtzQs",
        "part": 3,
        "question": "Art?",
        "transcript": "I have mentioned music can be so much more entertaining for my for you know people in my country than a painting or a book a story because they do not they do not have time or things to you know enjoy that and what kind of music do people like in your country most of the people enjoy pop music but i personally listen to rock metal or anything any kind of music but most of the people in my country follow the mainstream music the pop culture or what traditional art forms exist in your country as much as i know there is no traditional art in my country it is not allowed but i can i cannot think of anything i just know it was it used to be some paintings or you know thing things like that you mean there is no traditional art right now i cannot think of anything but I am aware that it was something there was something in the past i do not know why what exactly but i reckon maybe paintings or sketches caricatures and stuff like that how can children benefit from learning art well it makes them you know their minds to be more active or more creative that makes them more innovative in such ways like you know mathematics or dealing with life's complications and stuff maybe i do not i do not want to be i do not want to get more philosophical but by experience i think it makes them more active mentally mentally active do you think that the state should support the arts and cultural activities yeah of course they can they can support it in many ways you know financially or they can support it all the time by simply giving money and time but i.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["mainstream music", "pop culture", "philosophical", "mentally active", "caricatures"],
            "grammar_structures_used": ["complex_sentences", "hedging"]
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
                "why_not_8": "Hesitations.",
                "why_not_6": "Error free."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "High level ('caricatures')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "High level. Band 7.",
        "grammar_reason": "Good. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "6UP3bpCtzQs_q06",
        "video_id": "6UP3bpCtzQs",
        "part": 3,
        "question": "Improve future?",
        "transcript": "You know not enough for me right now but it may improve the future of course you can improve that.",
        "word_count": 19,
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
        "id": 0, "sample_id": "NmKZi8kqsFo_q02",
        "video_id": "NmKZi8kqsFo",
        "part": 1,
        "question": "Social media?",
        "transcript": "Our house yeah okay good now we are going to talk about social media so do you or your friends like to use social media yeah definitely I have Snapchat Instagram all sorts of social media applications yeah and why do you like using these applications I say social media is pretty much a new means of communicating between people so I find myself using the social media chat functions more than calling people or messaging them and also sharing photos and looking at other people's reactions I mean some people may call it unhealthy but I think it became a new Norm in especially among teenagers and do you think any of your friends use social media too much I I guess so because I find some people if you look at the screen time function on your iPhone you can see how many hours you have spent on your phone and they some people spent like more than 10 hours a day and I feel like that is really unhealthy and do you want to work in social media in the future I am interested in technology like software engineering and computer science so yeah why not give it a try okay and what is the most popular social media in your country oh in Korea definitely cacao talk yeah because KakaoTalk I mean recently there was a a Data Center crisis a data center accident and everyone was suffering so that shows how much important how important kekko talk is in our daily lives and is there any difference between the way young people use social media and older people use social media the type of social media applications that people use differently vary from age to age because I find older people using.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["software engineering", "computer science", "means of communicating", "screen time"],
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
                "why_not_9": "'means of communicating', 'vary from age to age'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
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
