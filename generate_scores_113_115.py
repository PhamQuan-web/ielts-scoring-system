import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 11301,
        "sample_id": "wwTUb238_zY_q08",
        "video_id": "wwTUb238_zY",
        "part": 3,
        "question": "And in what kinds of professions do people help others more?",
        "transcript": "I believe more service jobs like, firefighters, policemen. Those types of people are willing to always help others and, well, that is the easy answer, but I do feel like, a more intricate answer, I would say, more deeper answer than just firefighters and policemen is I do feel like, really lawyers need more credit than what they normally get. being able to help a family through legal trouble, being able to help an individual through, like, bankruptcy, through hard times is something really a lawyer can do. And I feel like that is an underrated statement of the job.",
        "word_count": 97,
        "analysis_metadata": {
            "grammar_error_patterns": ["comparison_error"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["intricate answer", "underrated statement", "legal trouble", "bankruptcy"],
            "grammar_structures_used": ["complex_sentence_contrast", "parallelism"]
        },
        "micro_flaws": {
            "grammar": ["double_comparative"],
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
            "length_appropriateness": "extended",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Error: 'more deeper answer' (double comparative - should be 'deeper' or 'more deep' though deeper is better).",
                "why_not_7": "Structure is very sophisticated otherwise."
            },
            "vocabulary": {
                "why_not_9": "'Intricate answer' is excellent. 'Underrated statement' is slightly unusual collocation but acceptable.",
                "why_not_7": "High level."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Majority of sentences error-free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Precise and flexible."
        },
        "vocab_reason": "Observation: 'Intricate', 'bankruptcy'. Impact: Precise. Justification: Band 9.",
        "grammar_reason": "Observation: 'More deeper'. Justification: Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 11302,
        "sample_id": "wwTUb238_zY_q09",
        "video_id": "wwTUb238_zY",
        "part": 3,
        "question": "Parents or teachers?",
        "transcript": "I do feel like parents should be the up up front with their teaching especially regards to young children I do believe that the parents should set a good role model they should set a good example for the children to learn and the teachers should be more of like guiders like general direction yeah They point them towards the general direction but the parents should be the one to really get in really teach them the intricacies of what right what wrong how to help people when should you help people and I feel like that isn something you learn out of school",
        "word_count": 103,
        "analysis_metadata": {
            "grammar_error_patterns": ["collocation_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["up front", "role model", "intricacies"],
            "grammar_structures_used": ["complex_sentence_contrast", "noun_clause"]
        },
        "micro_flaws": {
            "grammar": ["missing_preposition"],
            "vocabulary": ["wrong_collocation"]
        },
        "vocab_control": {
            "appropriateness": "accurate",
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
                "why_not_9": "Minor slip 'regards to' (with regards to/in regards to).",
                "why_not_7": "Complex structures."
            },
            "vocabulary": {
                "why_not_9": "'Set a good role model' is a collocation error (be a role model / set a good example). 'Guiders' is not a standard word (guides).",
                "why_not_7": "'Intricacies' is Band 9 level word."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use with occasional inaccuracy."
        },
        "vocab_reason": "Observation: 'Guiders', 'set a role model'. Impact: Occasional inaccuracy. Justification: Band 8.",
        "grammar_reason": "Observation: Strong structures. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 11501,
        "sample_id": "Up5hLgMQy5A_q02",
        "video_id": "Up5hLgMQy5A",
        "part": 1,
        "question": "So do you live in a house or an apartment?",
        "transcript": "I live in apartment. And, I live in an apartment with my family members. So my sister and my parents, so, and me, so four of us. And I think it is a good place to live.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_missing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["apartment", "family members"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["missing_article"],
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
            "complexity_level": "low",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "medium",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Missed article 'in apartment'.",
                "why_not_5": "Correct self-correction to 'an apartment' later."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Accurate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 6.",
        "grammar_reason": "Observation: Article error then corrected. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 11502,
        "sample_id": "Up5hLgMQy5A_q04",
        "video_id": "Up5hLgMQy5A",
        "part": 1,
        "question": "Would you like to change anything about your apartment?",
        "transcript": "My apartment, has a gym for the residents who live in the same, the apartment. And the gym is a little bit too far, so maybe if the gym was close enough from my apartment, then it would have been, it would have been convenient. And also, recycling. About recycling. I cannot do it, when I want to. it is only, the day that I can recycle is fixed Monday, Tuesday. So, if they make it a little bit longer, then I think that will be also, convenient.",
        "word_count": 89,
        "analysis_metadata": {
            "grammar_error_patterns": ["conditional_error"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["residents", "recycling", "fixed"],
            "grammar_structures_used": ["third_conditional_attempt", "relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["conditional_tense_mismatch"],
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
            "complexity_level": "high",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "extended",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'If the gym was close... it would have been' (Mixed conditional - acceptable but 'would be' might fit better for current state, or 'had been' for past).",
                "why_not_6": "Complex attempts."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Good topic words."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Residents', 'recycling'. Justification: Band 7.",
        "grammar_reason": "Observation: Complex conditional attempt. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 11503,
        "sample_id": "Up5hLgMQy5A_q05",
        "video_id": "Up5hLgMQy5A",
        "part": 1,
        "question": "So, are there many street markets in your country?",
        "transcript": "Of course, I think there are many street markets. nowadays compared to, like 10 years ago, 20 years ago, it has, the number of street markets has been reduced. But still, I think there are many compared to other countries like US or England. Especially in Jong-lo, you can find at least, I think, three or four big small street markets. And I think still they are popular enough.",
        "word_count": 70,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["number of street markets", "reduced", "popular enough"],
            "grammar_structures_used": ["passive_voice", "comparison"]
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
                "why_not_9": "Good control.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Reduced'. Justification: Band 7.",
        "grammar_reason": "Observation: Passive 'has been reduced'. Justification: Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 11504,
        "sample_id": "Up5hLgMQy5A_q06",
        "video_id": "Up5hLgMQy5A",
        "part": 1,
        "question": "And what do people usually buy at street markets?",
        "transcript": "I think usually it is groceries or food, like street foods as well. So, people, some people have this norm which is they sell more fresh groceries or food than normal supermarkets. So people tend to go there and also you, you can find many street food, delicious street food that you cannot find in other stores. So I think, yeah, that is the reason why people visit there and buy things.",
        "word_count": 72,
        "analysis_metadata": {
            "grammar_error_patterns": ["relative_clause_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["groceries", "fresh groceries", "norm"],
            "grammar_structures_used": ["relative_clause", "reason_clause"]
        },
        "micro_flaws": {
            "grammar": ["awkward_relative_clause"],
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
                "why_not_8": "'Have this norm which is they sell' (awkward structure).",
                "why_not_6": "Complex sentences."
            },
            "vocabulary": {
                "why_not_8": "'Norm' used incorrectly (belief/perception?).",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Groceries'. 'Norm' error. Justification: Band 7.",
        "grammar_reason": "Observation: Awkward relative clause. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 11505,
        "sample_id": "Up5hLgMQy5A_q11",
        "video_id": "Up5hLgMQy5A",
        "part": 3,
        "question": "And, apart from advertisements, what else influences, consumers when they are looking to buy a product?",
        "transcript": "Apart from advertisements, I think, advertisements. I think maybe promotion, which is I think this is sort of advertisement but like if we speak about advertisement, it is usually showed by tv or like online banners. I think promotion is a little bit different. So where like celebrities, famous like public figures, they, advertise promote this item actually like using and showing the reviews, of the item. yeah, I would say promotion.",
        "word_count": 71,
        "analysis_metadata": {
            "grammar_error_patterns": ["passive_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["public figures", "online banners", "promotion"],
            "grammar_structures_used": ["complex_sentence_contrast"]
        },
        "micro_flaws": {
            "grammar": ["passive_verb_form"],
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
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'It is usually showed' (shown).",
                "why_not_6": "Complex structures."
            },
            "vocabulary": {
                "why_not_8": "'Public figures', 'banners' are good.",
                "why_not_6": "Accurate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Public figures'. Justification: Band 7.",
        "grammar_reason": "Observation: 'Showed' error. Justification: Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 11506,
        "sample_id": "Up5hLgMQy5A_q12",
        "video_id": "Up5hLgMQy5A",
        "part": 3,
        "question": "Yes, and why do some people like to ask for advice when making decisions?",
        "transcript": "Awesome, because I think if you think of the concept of brainstorming you can find the answer easily from the question, for the question. So I think more and more opinions and options the people here and And people here then they have, they have more chances to decide on something. So, so, you are, you are more creative when you, gather, people's opinions than, thinking alone. Yeah, again, so that is why people brainstorm to get the best solution. So I think that is why.",
        "word_count": 86,
        "analysis_metadata": {
            "grammar_error_patterns": ["awkward_phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["brainstorming", "gather opinions", "best solution"],
            "grammar_structures_used": ["complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": ["broken_syntax"],
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
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'The people here and And people here then they have' (confusing syntax).",
                "why_not_6": "Complex sentences."
            },
            "vocabulary": {
                "why_not_9": "'Brainstorming', 'gather opinions'. Excellent.",
                "why_not_7": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Brainstorming'. Impact: Precise. Justification: Band 8.",
        "grammar_reason": "Observation: Syntactic slip. Justification: Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 11507,
        "sample_id": "Up5hLgMQy5A_q13",
        "video_id": "Up5hLgMQy5A",
        "part": 3,
        "question": "Yes, and why do some people dislike asking other people for their opinion when making a decision?",
        "transcript": "Maybe it is because, maybe it is because they actually decided, like, actually in their mind, They have decided for an option but if they don want to hear anything than that then they will avoid to talking to people to get some help because he or she already decided what to buy or what to do So that can be one reason or maybe he or she is a bit snobbish. So I do not need anyone to help me. I only think the best way.",
        "word_count": 89,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_pattern_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["snobbish", "avoid talking"],
            "grammar_structures_used": ["complex_sentence_reason"]
        },
        "micro_flaws": {
            "grammar": ["verb_pattern_avoid_to"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "high",
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
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'Avoid to talking' (avoid talking). 'Decided for' (on).",
                "why_not_6": "Complex structures."
            },
            "vocabulary": {
                "why_not_9": "'Snobbish' is very precise.",
                "why_not_7": "Advanced."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Snobbish'. Impact: Precise. Justification: Band 8.",
        "grammar_reason": "Observation: 'Avoid to talking'. Justification: Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 11508,
        "sample_id": "MSoBQSoiIT8_q04",
        "video_id": "MSoBQSoiIT8",
        "part": 1,
        "question": "And could you tell me about your hometown?",
        "transcript": "I was born and raised in Changwon, where it is situated in the southern part of Korea. And it is located near the beautiful beach.",
        "word_count": 24,
        "analysis_metadata": {
            "grammar_error_patterns": ["relative_clause_error"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["born and raised", "situated in", "located near"],
            "grammar_structures_used": ["relative_clause", "passive_voice"]
        },
        "micro_flaws": {
            "grammar": ["redundant_relative_pronoun"],
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
            "length_appropriateness": "concise",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'Where it is situated' (which is situated / where it is situated - 'where' usually doesn't take 'it' subject in this relative clause structure, redundancy).",
                "why_not_6": "Complex structures."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Good collocations."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Born and raised'. Justification: Band 7.",
        "grammar_reason": "Observation: Relative clause slip. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 11509,
        "sample_id": "MSoBQSoiIT8_q05",
        "video_id": "MSoBQSoiIT8",
        "part": 1,
        "question": "And do you think you will live in your hometown in the future?",
        "transcript": "I do not think I am going to live in my hometown anymore. it is because I already moved to Seoul for my university. And then I am planning to go abroad again. So I do not think hometown is my future home.",
        "word_count": 43,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["go abroad", "future home"],
            "grammar_structures_used": ["future_intention", "reason_clause"]
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
                "why_not_7": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Go abroad'. Justification: Band 7.",
        "grammar_reason": "Observation: Error free. Justification: Band 8.",
        "vocabulary": 7,
        "grammar": 8
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
