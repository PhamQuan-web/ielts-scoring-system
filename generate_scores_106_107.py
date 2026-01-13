import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 10601,
        "sample_id": "gH2MFU1l0wc_q11",
        "video_id": "gH2MFU1l0wc",
        "part": 3,
        "question": "And do you usually like running outside or indoors?",
        "transcript": "Running outside I think because you see the people, oh, if I run in with my dog, it is like, oh my god, I am very happy in the time, yes.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": ["fragmented_structure", "informal_fillers"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["running outside", "run with my dog"],
            "grammar_structures_used": ["reason_clause"]
        },
        "micro_flaws": {
            "grammar": ["incoherent_structure"],
            "vocabulary": ["limited_range"]
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
            "complexity_level": "basic",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Sentence structure is broken ('I am very happy in the time').",
                "why_not_4": "Meaning is generally clear."
            },
            "vocabulary": {
                "why_not_6": "Very basic vocab.",
                "why_not_4": "Words are relevant."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts basic sentences but accuracy is variable.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: 'Happy in the time'. Justification: Band 5.",
        "grammar_reason": "Observation: Broken structure. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 10602,
        "sample_id": "gH2MFU1l0wc_q12",
        "video_id": "gH2MFU1l0wc",
        "part": 3,
        "question": "Okay, so do you think schools should provide physical education classes to students?",
        "transcript": "Yes but interesting in physical education classes When I was studying in Ukraine it was some kind of like okay take your feet okay move your hands It was not so interesting for children you know I think it may be some kind of like football something like that I think so Yes yes And do you think these days children get enough exercise I do not know. I do not have one.",
        "word_count": 71,
        "analysis_metadata": {
            "grammar_error_patterns": ["missing_verbs", "broken_sentences"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["physical education", "move your hands"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["fragmented_speech"],
            "vocabulary": ["imprecise_meaning"]
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
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent fragmentation; 'interesting in physical education classes' (missing verb/subject).",
                "why_not_4": "Can produce some correct simple forms."
            },
            "vocabulary": {
                "why_not_6": "Very limited ('some kind of like').",
                "why_not_4": "Sufficient for basic meaning."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts basic sentences.",
            "vocabulary_band": 5,
            "vocabulary_text": "Adequate for the task."
        },
        "vocab_reason": "Observation: Basic words. Justification: Band 5.",
        "grammar_reason": "Observation: Broken syntax. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 10603,
        "sample_id": "gH2MFU1l0wc_q15",
        "video_id": "gH2MFU1l0wc",
        "part": 3,
        "question": "What do you think about using popular celebrities to build awareness for health?",
        "transcript": "It is cool, but it is some kind of pressure for people because not all the people can have the same fit, you know, as in the picture. Sometimes in the picture it is like, it is some kind of like portraying. I can paint the same, but people cannot look like that, you know, you can have the very, like, it is impossible to have this form. Yeah. Yes, yes.",
        "word_count": 70,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_order", "article_usage"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["pressure for people", "impossible to have"],
            "grammar_structures_used": ["reason_clause"]
        },
        "micro_flaws": {
            "grammar": ["unnatural_structure"],
            "vocabulary": ["wrong_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "partial"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Errors cause some difficulty ('same fit', 'portraying').",
                "why_not_4": "Complex sentences attempted."
            },
            "vocabulary": {
                "why_not_6": "'Portraying' used incorrectly. 'Fit' used as noun (should be fitness or body shape).",
                "why_not_4": "Topic words used."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Frequent errors.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: 'Portraying'. Impact: Confusing. Justification: Band 5.",
        "grammar_reason": "Observation: 'Some kind of pressure'. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 10604,
        "sample_id": "gH2MFU1l0wc_q16",
        "video_id": "gH2MFU1l0wc",
        "part": 3,
        "question": "And why do you think celebrities could help people reach their exercise goals?",
        "transcript": "Mostly I do not think so. I think it is kind of pressure and pressure for mostly for women, you know, because it is like when I see some photos, even me, I am sometimes thinking like, oh my god, I am not so beautiful as her, yes. Because she is so fit, she is so beautiful, and her skin and something like that. it is impossible to have the fame in real life. But I think it is like, they motivated us to have higher standards. Yeah, it is good for us.",
        "word_count": 92,
        "analysis_metadata": {
            "grammar_error_patterns": ["comparison_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["higher standards", "motivated us", "beautiful"],
            "grammar_structures_used": ["comparison", "reason_clause"]
        },
        "micro_flaws": {
            "grammar": ["incorrect_comparison"],
            "vocabulary": ["wrong_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "mostly_accurate",
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
            "length_appropriateness": "good",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Error 'not so beautiful as her' (as beautiful as).",
                "why_not_5": "Complex sentences generally successful."
            },
            "vocabulary": {
                "why_not_7": "'Have the fame' (meaning fame/body?) is unclear. 'Motivated us' is good.",
                "why_not_5": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Higher standards'. 'Fame' error. Justification: Band 6.",
        "grammar_reason": "Observation: Comparison error. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 10701,
        "sample_id": "elhXXacJICA_q02",
        "video_id": "elhXXacJICA",
        "part": 1,
        "question": "Chloe, tell me, are you working or studying at the moment?",
        "transcript": "Actually, I am doing both. I am attending graduate school here in Seoul and at the same time I am working at a Korean barbecue restaurant. So would you like to, if we talk about schools and workplaces, would you prefer to talk about your studies or your workplace in this case? Maybe workplace. I think it is a very interesting place to work because we have members come coming from different countries such as China, Japan, Korea, of course, and Nepal.",
        "word_count": 83,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["attending graduate school", "Korean barbecue restaurant", "interesting place to work"],
            "grammar_structures_used": ["complex_sentence_reason"]
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
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good but not overly complex.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard vocabulary.",
                "why_not_7": "Natural collocations 'attending graduate school'."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Graduate school'. Impact: Accurate. Justification: Band 8.",
        "grammar_reason": "Observation: Error free. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 10702,
        "sample_id": "elhXXacJICA_q04",
        "video_id": "elhXXacJICA",
        "part": 1,
        "question": "Do you think you have got a good working environment at the moment?",
        "transcript": "sure. Absolutely. I think my manager who is very, energetic and has great leadership. he can lead the whole team into a very good, direction.",
        "word_count": 25,
        "analysis_metadata": {
            "grammar_error_patterns": ["sentence_fragment"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["great leadership", "lead the whole team", "energetic"],
            "grammar_structures_used": ["relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["fragmented_relative_clause"],
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
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Restart/fragment 'I think my manager who is... he can'.",
                "why_not_7": "Generally controlled."
            },
            "vocabulary": {
                "why_not_9": "Good collocations.",
                "why_not_7": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces good complexity.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Great leadership'. Impact: Natural. Justification: Band 8.",
        "grammar_reason": "Observation: Relative clause fragment. Justification: Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 10703,
        "sample_id": "elhXXacJICA_q05",
        "video_id": "elhXXacJICA",
        "part": 1,
        "question": "And what is challenging at your workplace?",
        "transcript": "It is super busy. Actually, I worked last night too. for the entire four or five hours, we just kept working. Yeah. Without, without like no rest at all.",
        "word_count": 29,
        "analysis_metadata": {
            "grammar_error_patterns": ["double_negative"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["super busy", "kept working"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["double_negative_informal"],
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
                "why_not_8": "'Without like no rest' is a double negative/informal error.",
                "why_not_6": "Natural flow."
            },
            "vocabulary": {
                "why_not_8": "Natural 'super busy'.",
                "why_not_6": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Natural."
        },
        "vocab_reason": "Observation: 'Super busy'. Impact: Natural. Justification: Band 7.",
        "grammar_reason": "Observation: Informal error. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 10704,
        "sample_id": "elhXXacJICA_q07",
        "video_id": "elhXXacJICA",
        "part": 1,
        "question": "What advantages do you think it has if a company has like a resting or a relaxation room?",
        "transcript": "I think it provides, the employees with a space to like, take some relaxation and, so that they can enhance their work performance. it is very important to like strike the balance between work and rest.",
        "word_count": 35,
        "analysis_metadata": {
            "grammar_error_patterns": ["informal_fillers"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["enhance their work performance", "strike the balance", "provides the employees with"],
            "grammar_structures_used": ["complex_sentence_purpose"]
        },
        "micro_flaws": {
            "grammar": [],
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
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Use of 'like' as filler.",
                "why_not_7": "Complex structure 'provides... so that...' is perfect."
            },
            "vocabulary": {
                "why_not_9": "'Strike the balance', 'enhance work performance'. Excellent.",
                "why_not_7": "Advanced."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Majority of sentences error-free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Precise and flexible."
        },
        "vocab_reason": "Observation: 'Enhance work performance'. Impact: Professional/Academic. Justification: Band 9.",
        "grammar_reason": "Observation: Complex purpose clause. Justification: Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 10705,
        "sample_id": "elhXXacJICA_q09",
        "video_id": "elhXXacJICA",
        "part": 1,
        "question": "How do you get to work like the transportation?",
        "transcript": "I go to work by subway. Yeah, I usually just take like several stops and about 20 minutes to get there. So it is very convenient. You mentioned that you were from China. another topic we can talk about is the news.",
        "word_count": 41,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["take several stops", "convenient"],
            "grammar_structures_used": ["compound_sentence"]
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
                "why_not_9": "Simple sentences.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Take several stops'. Impact: Natural. Justification: Band 8.",
        "grammar_reason": "Observation: Correct. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 10706,
        "sample_id": "elhXXacJICA_q10",
        "video_id": "elhXXacJICA",
        "part": 1,
        "question": "So how often do you talk with your friends about the news and what is happening back home?",
        "transcript": "Not very often, I guess, because I, I am not a very enthusiastic about the latest things. recently I know about a movie which is very popular in China.",
        "word_count": 29,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_error"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["enthusiastic about", "latest things"],
            "grammar_structures_used": ["reason_clause", "relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["incorrect_article"],
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
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Error 'a very enthusiastic' (should be just 'very enthusiastic').",
                "why_not_7": "Controlled."
            },
            "vocabulary": {
                "why_not_9": "'Enthusiastic about' is good.",
                "why_not_7": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Enthusiastic about'. Impact: Natural. Justification: Band 8.",
        "grammar_reason": "Observation: Article error. Justification: Band 7.",
        "vocabulary": 8,
        "grammar": 7
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
