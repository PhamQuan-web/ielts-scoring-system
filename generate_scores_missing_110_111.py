import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 11001,
        "sample_id": "COIwVbnwPsI_q03",
        "video_id": "COIwVbnwPsI",
        "part": 1,
        "question": "And are you working or are you a student?",
        "transcript": "I am a student in Australia studying in university, marketing and, majoring in marketing. Okay.",
        "word_count": 16,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["studying in university", "majoring in marketing"],
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
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "low",
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "concise",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Very simple structure.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard academic intro.",
                "why_not_7": "Correct collocations."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Majoring in'. Justification: Band 7.",
        "grammar_reason": "Observation: Correct. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 11002,
        "sample_id": "COIwVbnwPsI_q04",
        "video_id": "COIwVbnwPsI",
        "part": 1,
        "question": "And do you like your course?",
        "transcript": "Yeah. For the course itself I like it, but sometimes I meet some strange professors or lecturers, but I do enjoy my major. And tell me about what you do when you have some free time. when I have free time, I have my own YouTube channel. So I film with my friend or at so after that I edit those videos and upload it on YouTube. And, for daily, hobbies, I go to gym to workout. Okay.",
        "word_count": 83,
        "analysis_metadata": {
            "grammar_error_patterns": ["connector_error"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["lecturers", "edit videos", "upload it on YouTube", "workout"],
            "grammar_structures_used": ["compound_sentence", "time_clause"]
        },
        "micro_flaws": {
            "grammar": ["awkward_connector"],
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
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Minor awkwardness 'or at so after that'.",
                "why_not_7": "Good control."
            },
            "vocabulary": {
                "why_not_9": "Good topic vocab 'upload', 'edit'.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Upload', 'edit'. Justification: Band 7.",
        "grammar_reason": "Observation: Good structure. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 11003,
        "sample_id": "COIwVbnwPsI_q05",
        "video_id": "COIwVbnwPsI",
        "part": 1,
        "question": "And could you tell me about your hometown?",
        "transcript": "My hometown is called Daegu. it is the, located at the southern part of Korea, Korean peninsula. And, I moved to Seoul when I was six, but I still visit there once a year to visit my relatives.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["located at", "southern part", "visit my relatives"],
            "grammar_structures_used": ["passive_voice", "compound_sentence"]
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
                "why_not_9": "Good use of passive 'located at'.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard geographic vocab.",
                "why_not_7": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient."
        },
        "vocab_reason": "Observation: 'Peninsula'. Justification: Band 7.",
        "grammar_reason": "Observation: Passive structure. Justification: Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 11004,
        "sample_id": "COIwVbnwPsI_q08",
        "video_id": "COIwVbnwPsI",
        "part": 1,
        "question": "And why do you think jeans are popular?",
        "transcript": "I think I have learned this in my schools and other like I have read some articles about it. And I heard that jeans were popular when it was first invented. And rich people like thought even the poor were wearing those pants. And at first rich people thought that how could those people wear the same clothes as us. But I think that represents that, it, all the people, from every people's perspective, jeans looks okay and very fashionable. So I think I am also part of those people, I guess. Okay.",
        "word_count": 92,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "variable",
            "vocab_evidence": ["first invented", "perspective", "fashionable"],
            "grammar_structures_used": ["passive_voice", "reported_thought"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement"],
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
            "length_appropriateness": "optimal",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'Jeans looks okay' (agreement error). 'Rich people thought that how could' (embedded question error).",
                "why_not_6": "Complex sentences attempted and mostly intelligible."
            },
            "vocabulary": {
                "why_not_8": "'Every people's perspective' (should be everyone's).",
                "why_not_6": "Good words 'invented', 'perspective'."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex. Errors occur.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Perspective'. Justification: Band 7.",
        "grammar_reason": "Observation: Embedded question error. Justification: Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 11005,
        "sample_id": "COIwVbnwPsI_q10",
        "video_id": "COIwVbnwPsI",
        "part": 2,
        "question": "Can you just grab that pen back off you, please?",
        "transcript": "Okay, I think for me, ideal home would be apartment. I think, the reason why I chose this form of home is because, in Korea, because the landfill is small, most of people build, apartment for their houses. And I have lived in apartment for most of my life. So I think this is why I chose this as my ideal home. And, I think it should be located near public transportation. I think that is the most important thing. because, let us say I am studying or have a job. commuting is the most important thing for me, I guess. so maybe near bus station or subway station would be nice. And I think for my home, it should be first cozy and should be, secondly, it should be equipped with lots of furnitures and other facilities. And I would say it is better if there is like gym or swimming pool at the apartment for public use. And, for this home, I would say it does not have to be big because I would live there for my twenties. But, once I marry or get a kid, maybe I would move to a bigger apartment. And if I can, I would like to live near Seoul at least, since it is the most popular area in Korea.",
        "word_count": 218,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_missing", "uncountable_noun_plural"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["ideal home", "public transportation", "commuting", "equipped with", "facilities"],
            "grammar_structures_used": ["complex_sentence_reason", "conditional", "passive_voice"]
        },
        "micro_flaws": {
            "grammar": ["missing_article"],
            "vocabulary": ["plural_furniture"]
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
            "complexity_level": "high",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "extended",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Misses articles 'be apartment' (an apartment). 'Lots of furnitures' (uncountable error).",
                "why_not_6": "Sentence variety is excellent. Cohesion is strong."
            },
            "vocabulary": {
                "why_not_8": "'Landfill' used incorrectly (meant land mass or land area). 'Furnitures' error.",
                "why_not_6": "Topic specific words 'commuting', 'equipped with' are strong."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control. Frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common items with some awareness of style."
        },
        "vocab_reason": "Observation: 'Equipped with'. 'Landfill' error. Justification: Band 7.",
        "grammar_reason": "Observation: Article errors. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 11006,
        "sample_id": "COIwVbnwPsI_q13",
        "video_id": "COIwVbnwPsI",
        "part": 3,
        "question": "So yeah, what do you think, what are the differences between living in the city and living in the countryside?",
        "transcript": "So for, currently I am living in Australia. And, the city is Canberra. And I would say even though it is capital city, it is more countryside than Seoul, I guess. Because when I come out of my room, I can see the kangaroos running around. But, I think there is advantages and disadvantages for living in, city and countryside. For a city, I would say it is very convenient for everything, since everything is prepared already. but I would say it very packed and sometimes you want to be by yourself but there a lot there are a lot of people around you So I think it hard for you to get like personal zone But for countryside I think that very easy Like you want to be alone and you want some of your private time It very easy for you to just go out of your room and walk around But I would say for countryside yes it opposite from the city Everything is a bit uncomfortable",
        "word_count": 166,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement_error", "article_missing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["advantages and disadvantages", "convenient", "personal zone", "private time"],
            "grammar_structures_used": ["comparison", "contrast"]
        },
        "micro_flaws": {
            "grammar": ["missing_be_verb_in_it_is"],
            "vocabulary": ["imprecise_collocation"]
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
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'There is advantages' (are). 'It very packed' (is).",
                "why_not_6": "Complex sentences used well despite slips."
            },
            "vocabulary": {
                "why_not_8": "'Personal zone' (maybe personal space?).",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Personal zone'. Justification: Band 7.",
        "grammar_reason": "Observation: Agreement errors. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 11007,
        "sample_id": "COIwVbnwPsI_q14",
        "video_id": "COIwVbnwPsI",
        "part": 3,
        "question": "And do you think older people prefer living in the countryside rather than the city?",
        "transcript": "Yes, I agree with this statement because older people, especially from Korean perspective, I have heard a lot of older generations saying that after retiring, they would like to go back to countryside and run their own farm. I think that is because they care more about their health issue. They want to breathe in some more clean air and live among the nature. I think that is why.",
        "word_count": 69,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["Korean perspective", "older generations", "retiring", "run their own farm", "breathe in"],
            "grammar_structures_used": ["complex_sentence_reason", "noun_clause"]
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
            "complexity_level": "moderate_high",
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
                "why_not_9": "Solid but not fully flexible/nuanced.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Good collocations.",
                "why_not_7": "'Run their own farm', 'breathe in'. Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Run their own farm'. Impact: Natural. Justification: Band 8.",
        "grammar_reason": "Observation: Error free. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 11008,
        "sample_id": "COIwVbnwPsI_q15",
        "video_id": "COIwVbnwPsI",
        "part": 3,
        "question": "They would not like to live in the countryside?",
        "transcript": "I think they want to be exposed to more technologies and more comfortable living area. So, as I said before, commuting and transportation is very important factors for them. And they need to get access to their, working field very easily. I think that is why younger people prefer to live in the city.",
        "word_count": 53,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["exposed to", "comfortable living area", "get access to"],
            "grammar_structures_used": ["passive_voice", "complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": ["agreement_is_factors"],
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
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'Commuting and transportation is very important factors' (are).",
                "why_not_6": "Complex structure."
            },
            "vocabulary": {
                "why_not_8": "'Working field' (workplace/industry).",
                "why_not_6": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Exposed to'. Justification: Band 7.",
        "grammar_reason": "Observation: Agreement error. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 11101,
        "sample_id": "43EfsMVBHCI_q02",
        "video_id": "43EfsMVBHCI",
        "part": 1,
        "question": "Do you enjoy talking to new people?",
        "transcript": "Yes, I like it because I like to know new people and new talks. I like thinking about new things. Okay.",
        "word_count": 20,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["know new people", "new talks"],
            "grammar_structures_used": ["reason_clause"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["unnatural_phrasing"]
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
            "complexity_level": "simple",
            "accuracy_level": "high",
            "flexibility": "low",
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Too simple.",
                "why_not_5": "Correct."
            },
            "vocabulary": {
                "why_not_7": "'New talks' is unnatural (should be conversations).",
                "why_not_5": "Clear."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Simple forms.",
            "vocabulary_band": 5,
            "vocabulary_text": "Limited."
        },
        "vocab_reason": "Observation: 'New talks'. Justification: Band 5/6. Giving 5.",
        "grammar_reason": "Observation: Simple. Justification: Band 6.",
        "vocabulary": 5,
        "grammar": 6
    },
    {
        "id": 11102,
        "sample_id": "43EfsMVBHCI_q04",
        "video_id": "43EfsMVBHCI",
        "part": 1,
        "question": "When I was in university, I can make new friends from other majors.",
        "transcript": "And in my workplace, I can make friends who have same interest. Now I am not students now, I am doing modeling. So, every time I met new people, I like it. Just like it. And even in Subway, if there is a person I want to talk, I just walk to them and just make conversation, how you are from, like this, and follow on Instagram each other. I like it. that is cool.",
        "word_count": 75,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_error", "article_missing"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["make friends", "doing modeling"],
            "grammar_structures_used": ["relative_clause", "conditional"]
        },
        "micro_flaws": {
            "grammar": ["incorrect_tense_met", "missing_article_same_interest"],
            "vocabulary": ["basic_phrasing"]
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
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent errors: 'I am not students' (a student), 'every time I met' (meet), 'how you are from' (where).",
                "why_not_4": "Meaning clear."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Frequent errors.",
            "vocabulary_band": 5,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic words. Justification: Band 5.",
        "grammar_reason": "Observation: Tense/article errors. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
