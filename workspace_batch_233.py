import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 233 ---
# Total Samples: 20
# Valid Samples: 17

scored_samples = [
    {
        "id": 0, "sample_id": "WBMu2HYFt-k_q06", "video_id": "WBMu2HYFt-k",
        "part": 3,
        "question": "Test feelings?",
        "transcript": "About your opinions and feelings about doing the test what were your overall feelings about today's test the most feeling is nervous and I my heart is keep beating and I keep shaking now okay and of course you ready answer my question did you feel nervous what do you think was the most difficult part about the test oh I think the topic of books is more difficult for me because I am really not interesting in reading books so maybe I I have to read more books or before test or prepare more topics before Tex all right that is okay and what do you find the easiest actually I forget everything for all it head because I am too nervous so not really easy for me because I cannot come up lelab very fast and yes okay and what topics would you have preferred to have come up during the test maybe the topics of movies or for the traveling will be more comfortable for me yes okay thank you so much for answering all my questions I hope you have a nice day.",
        "word_count": 189,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form", "word_choice"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["nervous", "shaking"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["form_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'heart is keep beating' (keeps). 'not interesting in' (interested). 'lelab' (elaborate?)."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent breakdown.",
                "why_not_4": "Communicates."
            },
            "vocabulary": {
                "why_not_6": "Word choice errors.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic with errors. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "oi6On-F-Pvk_q02", "video_id": "oi6On-F-Pvk",
        "part": 1,
        "question": "Helping others?",
        "transcript": "This medication will help her thank you okay so do you like helping other people sure yeah like charities yeah I like I like I prefer helping other people especially all the old people because they always need help",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["charities"],
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
                "why_not_8": "Too short/simple.",
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
        "vocab_reason": "Good. Band 7.",
        "grammar_reason": "Accurate. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "KG7Yd_z_iUw_q02", "video_id": "KG7Yd_z_iUw",
        "part": 1,
        "question": "Hometown?",
        "transcript": "With a lot of government rules so I would say I recommend Singapore more I am sorry to Seoul but yeah okay so you think the rules make the living there more harmonious yes that is correct okay and how long have you lived in Seoul I lived in Seoul for five years now since 2018. oh okay and are there big changes in the city big changes but mainly I have been taking care of my grandfather for when I came to Korea in 2018 so my grandfather had pneumonia and dementia so I helped my mother out for about three years so I I could not really go out and have fun and I I do not really have friends in Korea at all so and then after three years he just passed away so that was kind of a sad story that I would tell I guess let us see yeah is solo your permanent city of residence yes because since twin 20 since I was in secondary school which it is a British way of saying right secondary school I had permanent residency from Singapore but then I just gave up my my permanent residency because my all my family is here so I decided to kind of like want to settle down and Seoul because my mom and my dad and my grandma is here and I want to get married and Seoul so yeah that is I think my where my future is okay and are there people of different age groups living in this city different age groups like what do you mean like are there is there like a mix of like very young children and like kind of middle-aged people older people or is it more of a city that just.",
        "word_count": 298,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["pneumonia", "dementia", "permanent residency", "settle down"],
            "grammar_structures_used": ["complex_sentences", "past_perfect"]
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
                "why_not_9": "Precise terms.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses a wide range of vocabulary with very natural and sophisticated control."
        },
        "vocab_reason": "Excellent. Band 9.",
        "grammar_reason": "Native-like. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "KG7Yd_z_iUw_q03", "video_id": "KG7Yd_z_iUw",
        "part": 1,
        "question": "Age groups?",
        "transcript": "Young families live in or just older people well I guess in my apartment I guess older people they live here a lot because it is it is a very old apartment and my grandma he she goes to an old folks home every single day so I see a lot of old people and you know it is an older growing population so older people are coming and and the newborn babies they are like not they they are not really giving birth to because you know the educational fees and everything is so expensive so for an example I am 32 2 years old but I do not really want to get married and have kids because it is so expensive yeah so I guess older people are more more widespread in this country okay very good so now you are going to start the extended speaking section yeah and the topic is about an interesting job so.",
        "word_count": 166,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["old folks home", "widespread", "educational fees"],
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
                "why_not_9": "Precise terms.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses a wide range of vocabulary with very natural and sophisticated control."
        },
        "vocab_reason": "Excellent. Band 9.",
        "grammar_reason": "Native-like. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "KG7Yd_z_iUw_q05", "video_id": "KG7Yd_z_iUw",
        "part": 3,
        "question": "Career advice?",
        "transcript": "Because that is what my mom every time tells me because if you go for income it is never going to last it is if you go for your income it is not going to interest you for your whole life but if you chase your own dreams and if you go for your interest it is you are going to be successful for whatever reason and yeah so if you go after your interests and dreams you are going to be successful for sure okay very good and this kind of leads into the next question so do young people take their parents advice when they are choosing a major that is a very hard question I think their own individuality and their own self-interest is different from their own parents expectations so I think you should choose your own major so for example my grandfather actually chose a major for my my mom which is to become a kindergarten teacher because it is just a stable job but she did not enjoy it at all so that was a very very not not a very good choice for her so I think you should choice you should choose your own job okay so besides parents who else would people take advice from who else you can choose to have your advice from your professional professors or your school teachers or even there are a lot of government supporters who can tell you what to do so there are right now there are a lot of programs that you can take on so you can choose to get help from a lot of government informations yeah okay and our final question it is a bit unrelated but why do some people prefer to study alone why do we.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["individuality", "self-interest", "stable job", "chase your own dreams"],
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
            "triggered": True,
            "reason": "'government informations' (information - uncountable)."
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
                "why_not_9": "Minor uncountable noun error.",
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
        "id": 0, "sample_id": "wYeZwxPLrfU_q02", "video_id": "wYeZwxPLrfU",
        "part": 1,
        "question": "Without internet?",
        "transcript": "Wow. I definitely would not go back to reading books or looking for stuff on encyclopedia. But I honestly do not know what I would do without internet now because it is so immersed immersed in my life. you know everything from looking for any information or even going to finding information about restaurants I would go on internet so I I honestly cannot live without internet now yeah &gt;&gt; makes a lot of sense to say that do you think you spend too much time online &gt;&gt; yes yes I do so I try to limit myself by reading books &gt;&gt; because I I I feel like &gt;&gt; it is not good for my mental health in some ways and I constantly need some kind of what do you call it distraction just just to just to keep my mind busy. So I am I try to stay away from internet as much as possible if I if I can. Yeah. &gt;&gt;",
        "word_count": 165,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["immersed in my life", "mental health", "distraction"],
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
            "development_depth": "extended"
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
        "vocab_reason": "Good range. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q03",
        "video_id": "wYeZwxPLrfU",
        "part": 1,
        "question": "Influence?",
        "transcript": "Well well I had one instance recently we are talking about politics and I had one friend who has no knowledge of any politics in and no mind of his own. He just looks at internet and then just reads it reads off of it and then thinking making that his idea and he never even you know fact check checked it to see if that was real or not. &gt;&gt; Yeah. &gt;&gt;",
        "word_count": 72,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["mind of his own", "fact check"],
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
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good collocations. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q04",
        "video_id": "wYeZwxPLrfU",
        "part": 1,
        "question": "How often?",
        "transcript": "&gt;&gt; Me the moment I wake up. &gt;&gt; Yeah. To to you know when I go to sleep. &gt;&gt;",
        "word_count": 19,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": [],
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
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q05",
        "video_id": "wYeZwxPLrfU",
        "part": 1,
        "question": "When started?",
        "transcript": "&gt;&gt; Internet I started using maybe when I was 12 13. Yeah. &gt;&gt; Okay. Going to something completely opposite from the internet.",
        "word_count": 21,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": [],
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
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q06",
        "video_id": "wYeZwxPLrfU",
        "part": 1,
        "question": "Fishing?",
        "transcript": "&gt;&gt; Yes. &gt;&gt; Okay. &gt;&gt; Yes. I I actually want to get into fishing right now because I I used to go fishing when I used to travel backpacking Southeast Asia and then I found it to be fun and enjoyable even though when you are not catching anything there there is a calmness behind it. &gt;&gt; Okay. And so I guess you you would like fishing in that case. &gt;&gt; -huh. &gt;&gt;",
        "word_count": 71,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["backpacking", "calmness", "enjoyable"],
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
                "why_not_7": "Good."
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
        "id": 0, "sample_id": "wYeZwxPLrfU_q07",
        "video_id": "wYeZwxPLrfU",
        "part": 1,
        "question": "Fishing popular?",
        "transcript": "Fishing amongst I think like older guys is is popular. I do not know anyone that goes deep dive fishing in Korea, but they do they have like a indoor fishing area where they just put fish in like a artificial pond. &gt;&gt; Okay. And then they, you know, spend time there just like, you know, chitchatting with people next to them. And then, &gt;&gt; yeah, but apart from that, I do not know any young people that does fishing. I know a lot of 40, 50, 60 year old that that likes to go fishing. &gt;&gt; Okay. let us say you catch it.",
        "word_count": 102,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["artificial pond", "chitchatting"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'deep dive fishing' (deep sea fishing?)."
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Word choice.",
                "why_not_7": "Good."
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
        "id": 0, "sample_id": "wYeZwxPLrfU_q08",
        "video_id": "wYeZwxPLrfU",
        "part": 1,
        "question": "Eating fish?",
        "transcript": "&gt;&gt; I love fish. &gt;&gt; Okay. &gt;&gt; Yeah, I love fish. I know so many fish anatomy. So I know to pick the bones really &gt;&gt; like professionally. &gt;&gt; that is pretty cool. &gt;&gt; You also mentioned that you used to go as a child when you went fishing.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["fish anatomy", "pick the bones"],
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
        "id": 0, "sample_id": "wYeZwxPLrfU_q09",
        "video_id": "wYeZwxPLrfU",
        "part": 1,
        "question": "Activities?",
        "transcript": "&gt;&gt; I was really outdoorsy. I I used to spend a lot of time at near the beach and then we used to do a lot of bic bike r bike cycling. &gt;&gt; Mhm. &gt;&gt; Yeah. We used to ride bicycles a lot. and skateboarding. &gt;&gt; Oh, okay. &gt;&gt; And those all this California stuff. &gt;&gt; I see.",
        "word_count": 57,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["outdoorsy", "skateboarding"],
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
                "why_not_9": "Hesitations.",
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
        "vocab_reason": "Good words. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q10",
        "video_id": "wYeZwxPLrfU",
        "part": 1,
        "question": "Where?",
        "transcript": "where we grew up is we just made everywhere our our playground. You know we would you know go to the train tracks, we would go to the beach, you know we would go to school. &gt;&gt; we we used to ride our bicycles everywhere. So we just you know made everywhere our playgrounds. &gt;&gt; Okay, that is awesome.",
        "word_count": 58,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["train tracks", "playground"],
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
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q11",
        "video_id": "wYeZwxPLrfU",
        "part": 1,
        "question": "Memories?",
        "transcript": "&gt;&gt; I would say in middle school or elementary, middle school when I was spend when I was spending time in the states. when I when I just got there, I just met so many people from different walks of life and then it was it was not so study oriented like like in Korea. So I had a lot of freedom and time to grow up as a person during those times. &gt;&gt; Yeah. &gt;&gt; Okay. Excellent.",
        "word_count": 75,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["walks of life", "study oriented", "grow up as a person"],
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
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q12",
        "video_id": "wYeZwxPLrfU",
        "part": 3,
        "question": "Scientific news?",
        "transcript": "&gt;&gt; just Google, YouTube. and then if I am interested in some subject, I will I will research it myself. Apart from that, I I just I just read what pops pops up on on the internet mostly or CNN or, you know, Bloomberg, whatever. Yeah. &gt;&gt;",
        "word_count": 45,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["pops up", "research it myself"],
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
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q13",
        "video_id": "wYeZwxPLrfU",
        "part": 3,
        "question": "Study science?",
        "transcript": "&gt;&gt; Yes. because well unless you want to be stuck in one place for all your life, you you kind of have to get to know the trend not just like fashion or food but you know science and technology as well because you do not want to be left behind when everybody knows you know more information and the information is is you know money. &gt;&gt; Absolutely.",
        "word_count": 66,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["stuck in one place", "left behind"],
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q14",
        "video_id": "wYeZwxPLrfU",
        "part": 3,
        "question": "Subject?",
        "transcript": "Like of the STEM subjects. &gt;&gt; Huh. Right now, STEM subject. give me a sec. &gt;&gt; Yeah, it is not an easy one. &gt;&gt; Yeah. well,",
        "word_count": 24,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["STEM subjects"],
            "grammar_structures_used": ["simple_sentence"]
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
                "why_not_9": "Too short.",
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
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q15",
        "video_id": "wYeZwxPLrfU",
        "part": 3,
        "question": "Life works?",
        "transcript": "But then when they get to middle school, they could learn, you know, more about chemical stuff. Yeah. &gt;&gt;",
        "word_count": 18,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["chemical stuff"],
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
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Informal.",
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
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "wYeZwxPLrfU_q16",
        "video_id": "wYeZwxPLrfU",
        "part": 3,
        "question": "Where else?",
        "transcript": "I think it is very important for them to learn it when they are forced to in their forced. &gt;&gt; I see.",
        "word_count": 21,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["forced to"],
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
                "why_not_9": "Repetitive.",
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
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    }
]

# Write to file
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
