import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 227 ---
# Total Samples: 20
# Valid Samples: 16

scored_samples = [
    {
        "id": 0, "sample_id": "szu7Xf18cwA_q12", "video_id": "szu7Xf18cwA",
        "part": 1,
        "question": "Irresponsible age?",
        "transcript": "So, it is I think it does not matter how old you are, but it does matter how you see life and how responsible you are to yourself. Thank you very much, Mai. That is the end of the speaking test.",
        "word_count": 42,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["does not matter", "responsible to yourself"],
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
                "why_not_8": "Too short.",
                "why_not_6": "Accurate."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Natural."
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
        "id": 0, "sample_id": "szu7Xf18cwA_q15",
        "video_id": "szu7Xf18cwA",
        "part": 1,
        "question": "Easier?",
        "transcript": "I think the one that I took the previous time was better because I do not really remember about the topic but I guess that topic was more interesting to me so I had more things to say while this one it was it was fine. It was all right.",
        "word_count": 51,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["interesting to me"],
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
                "why_not_8": "Simple structure.",
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
        "id": 0, "sample_id": "vtW8TJCnk2k_q02",
        "video_id": "vtW8TJCnk2k",
        "part": 1,
        "question": "Clothes style?",
        "transcript": "To be comfortable mhm yeah I think that is it okay great and do you wear the same style of clothes on weekends and weekdays as of now yes because I am on like it is summer and I am I currently do not have a job right now so I just wear comfortable clothes all the time like sweats and stuff but during like school year and stuff I try to look more formal and like as a student and well yeah I try to look better like during the weekdays",
        "word_count": 91,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "informal",
            "vocab_evidence": ["sweats", "stuff"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["hesitation_markers"],
            "vocabulary": ["repetition_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Frequent fillers 'like', 'stuff'."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Hesitations.",
                "why_not_6": "Accurate."
            },
            "vocabulary": {
                "why_not_8": "Too informal ('stuff').",
                "why_not_6": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Natural but informal. Band 7.",
        "grammar_reason": "Accurate. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "vtW8TJCnk2k_q03",
        "video_id": "vtW8TJCnk2k",
        "part": 1,
        "question": "Good leader?",
        "transcript": "Example of a good leader I would say like an energetic person always can always bring the energy up and stuff yeah okay great yeah okay very good and.",
        "word_count": 29,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["energetic person", "bring the energy up"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["repetition_minor"]
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
                "why_not_8": "Short.",
                "why_not_6": "Accurate."
            },
            "vocabulary": {
                "why_not_8": "Repetitive.",
                "why_not_6": "Good collocation."
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
        "id": 0, "sample_id": "vtW8TJCnk2k_q04",
        "video_id": "vtW8TJCnk2k",
        "part": 1,
        "question": "Future jobs?",
        "transcript": "Receive higher salaries in the future I would say definitely no because just looking at how technology is evolving so fast like robots are definitely going to replace our jobs like especially physical jobs and yeah and yeah I think like there would be no more like physical jobs in the future yeah and I mean it is a sad reality but yeah I would say there would be like less physical jobs like Less jobs that require physical activities okay and your final question do you think machines could replace human workers in the future yes definitely I kind of answered that qu that question already but yeah like the tech like Technologies this these days is like growing up so fast and yeah and as I grew up like I already saw those changes for example like now like I like I will give you one specific example like I saw a Jamba Juice machine that like makes you a juice like and like it does not require a worker and it is just coming out of the machine and I like when I was like a kid like that did not exist right and yeah like just like that yeah robots can definitely replace like physical jobs okay all right so that is everything for your speaking test and.",
        "word_count": 218,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["sad reality", "evolving", "physical activities"],
            "grammar_structures_used": ["complex_sentences", "future_tense"]
        },
        "micro_flaws": {
            "grammar": ["hesitation_markers"],
            "vocabulary": ["repetition_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Frequent 'like'. 'growing up so fast' (evolving?)."
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Hesitations.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range. Band 7.",
        "grammar_reason": "Strong flow. Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "K46uEm8ksVE_q01",
        "video_id": "K46uEm8ksVE",
        "part": 1,
        "question": "Intro?",
        "transcript": "What is your name my name is yang zu li and you can call me as young soon very good so are you working or are you a student I am a student I am not working what are you studying oh I am preparing for going to university so I am studying english and art now okay and tell me about your hobbies oh I am interested in doing pictures like painting and or doing some sketches and my favorite kind of picture is animation and I am also preparing for university which is about innovation as well okay and could you describe your home please my home my home is an apartment and my home is in the first floor and around my home there are a lot of artificial forests so i can see various kinds of flowers and trees and i really like them they unwind me and it is relaxing to see the view through my window and i i live with my mom and in my home there are three rooms my brother's room my parents room and my room but these days my my dad and my brother is not home because they are working in the in the other place okay all right and would you like to change anything about your home i think there are not or too many furniture in my room so my room is quite narrow to push other monitor these days so i would like to move or get rid of some monitors like bookshelves because I am not interested in reading books so i want to move out them to my brother's room okay right now we are going to talk about discussion topics so what do you like to talk about with your friends do you mean what i want.",
        "word_count": 298,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition", "word_choice", "agreement"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["unwind me", "artificial forests", "narrow"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'call me as' (call me). 'preparing for going to' (preparing to go). 'artificial forests' (parks?). 'unwind me' (help me unwind). 'too many furniture' (much). 'narrow to push' (too small to put?)."
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent small errors.",
                "why_not_4": "Sustained."
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
        "vocab_reason": "Errors but communicative. Band 5.",
        "grammar_reason": "Frequent errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "eFwU7XI5Qh0_q02",
        "video_id": "eFwU7XI5Qh0",
        "part": 1,
        "question": "Eating out?",
        "transcript": "Outside which I think you know in a long term is not really good for my health do you prefer eating at home or at a restaurant if I have someone to cook for me at home then I would go for that currently I do not have that kind of luxury so I will only stick with grand food or now.",
        "word_count": 61,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["long term", "luxury", "stick with"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'grand food' (GrabFood - app). 'in a long term' (in the long term)."
        },
        "grammar_profile": {
            "complexity_level": "high",
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
                "why_not_9": "Minor slip.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "ASR ambiguity.",
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
        "id": 0, "sample_id": "eFwU7XI5Qh0_q03",
        "video_id": "eFwU7XI5Qh0",
        "part": 3,
        "question": "Patience?",
        "transcript": "70 or 80% of Vietnamese have patience especially those living in foreign countries they have jobs like nursing nails and your like manual work so if they do not have patience they would quit right away and just go at back home when do you need patience the most well I think when I am up to a new challenge for my case it is going to be studying in Berlin without any knowledge of German language so I have to take you know I have to be a hundred twenty percent patient with the new language with a new OCD new friends new white living.",
        "word_count": 105,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["manual work", "quit right away", "new challenge"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'new OCD' (new city?). 'white living' (way of living?)."
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
                "why_not_9": "Native flow.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "ASR errors.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses a wide range of vocabulary with very natural and sophisticated control."
        },
        "vocab_reason": "High level despite ASR. Band 9.",
        "grammar_reason": "Native-like. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "eFwU7XI5Qh0_q05",
        "video_id": "eFwU7XI5Qh0",
        "part": 3,
        "question": "Buying habits?",
        "transcript": "People like to buy well I think nowadays young people especially teenagers like to buy expensive or luxury items just to show up their wealth and family you know like financial conditions.",
        "word_count": 31,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["luxury items", "financial conditions"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["phrasing_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'show up their wealth' (show off)."
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
                "why_not_9": "Phrasing slip.",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "Phrasal verb error.",
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
        "grammar_reason": "Error free mostly. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "n0A2bI2QsIc_q04",
        "video_id": "n0A2bI2QsIc",
        "part": 2,
        "question": "Delayed trip?",
        "transcript": "you can begin all make that is one minute now all right okay so could you describe a trip that you were looking forward to but was delayed it happened when I was 14 I remember and I I was I was traveling London with my parents and we were heading to Paris in that day and so we went to the station and we had to take the Euro star the underground Railway that goes to Paris and actually we just thought the the Eurostar as a normal train we did not really think about the concept that it goes abroad so we were kind of late at that time because we did not think that they would check our luggage or they would check our passports so we did not really expect it it was our mistake obviously but yes we so we could not take the Train to Paris because we were so late at the time we did arrive at the train departure time but it was about we should have been there about 30 minutes before for our luggage and our visa and all to check all those stuffs to go to Paris and because it is another country obviously and at that time England was out of the Europe United yes Europe unions after the brexit so yes we were delayed to go to Paris so we had to book another train and at that time my mom was in charge of our family's trip and I would talk rather talk how she felt about the experience because she was in charge of the trip I was like a kid and I was it is okay we can take the on other the train but it was her who paid the fees and it was her who paid the overpaid.",
        "word_count": 302,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["Eurostar", "abroad", "brexit", "in charge of"],
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
            "reason": "'Europe United' (European Union). 'overpaid' (extra fees?)."
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
                "why_not_9": "Minor collocations.",
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
        "grammar_reason": "Fluent narration. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "n0A2bI2QsIc_q06",
        "video_id": "n0A2bI2QsIc",
        "part": 3,
        "question": "Travel views?",
        "transcript": "Not because obviously it is too different from the lives we are living right now at the moment so I think they are afraid of yes like traveling abroad and do you think traveling abroad is something that everyone should do I think if they are happily living happily enough at the moment in their daily routines and their lives I think they do not really have to travel because travel quite costs on Co a lot and we do not really have to pay for something we do not really like to do Soh they can do something else they like to do with that money so I would not recommend everyone to like travel around but most of the people who if they feel that Curiosity to what what it would feel like if I travel abroad like if people have some kind of curiosity like that or those questions in their mind I think they should definitely move on to the next level and travel abroad absolutely and what do you think is the difference between how younger people travel and how older people travel I think the younger ones are more concentrated on on like traveling around walking around because they obviously have more energy to use they drink a lot of alcohol at night like they their travels are more concentrated on on the energy they have to spend but I think older ones they the elders their travels are more peaceful like their their travels are more concentrated on rest on the term of rest because they have less energy than the younger on they want to just they do want to see like some famous sites but not too much so they have to be like full of energy all the time so because obviously they old.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_order"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["daily routines", "curiosity", "concentrated on"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": ["phrasing_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'travel quite costs' (costs quite a lot). 'concentrated on' (focused on?)."
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Phrasing slips.",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "Collocation precision.",
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
        "id": 0, "sample_id": "tGgXWLutx9M_q02",
        "video_id": "tGgXWLutx9M",
        "part": 1,
        "question": "Teenager clothes?",
        "transcript": "Ju wear like the style for teenagers I think teenagers they belong to the the age where when they go to school so most of the time I would see the teenagers in my hometown wearing uniforms other than that I think they would choose to wear casual clothes",
        "word_count": 47,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["casual clothes", "uniforms"],
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
                "why_not_9": "Simple.",
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
        "id": 0, "sample_id": "tGgXWLutx9M_q03",
        "video_id": "tGgXWLutx9M",
        "part": 2,
        "question": "Saving resources?",
        "transcript": "About saving resources as well including water and electricity and I have always been taught to save those Resources by you know simply switching off the electronic devices when we do not use them or safe Waters when we take a shower and things like that my beloved father also tells me that instead of using my private vehicles to commute to my school or work I should make use of public transportation to lower the carbon emissions or the personal carbon Footprints things like that so I was really impressed by his concern for the environment",
        "word_count": 93,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["carbon emissions", "carbon footprints", "commute", "public transportation"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'safe Waters' (save water)."
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
                "why_not_9": "Minor error.",
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
        "id": 0, "sample_id": "tGgXWLutx9M_q04",
        "video_id": "tGgXWLutx9M",
        "part": 3,
        "question": "Sustainability?",
        "transcript": "In but then I would want to add more actions into that list and that is trash categorization so it is really important for factories to dissolve all the trust or rubbish thrown into the the environment by categorizing them I mean people should join hands in categorizing trust into Solid Waste or toxic waste yeah like that so do you think people should be personally responsible for their environmental impact the questions just sound so similar yes it is our personal responsibility to save the environment and the nature and the natural resources and I have also just listed some actions that we can engage in so I think I I have nothing to say more about it what do you think are the most effective ways to improve environmental sustainability environmental Su sustainability is of great importance of great importance to the Social Development and I think that it is not only our personal responsibility but it is the obligation of the International Community or government to you know truly take actions instead of just raising awareness about it so the government from different countries should like Implement policies or practical actions to protect our nature either by preventing public I am sorry either by preventing private vehicles or just reducing the amount the number of private vehicles and just transfer to public ones mhm and what do you think we can teach children about protect the environment so for children I think the master of environment is kind of complicated for them to understand so like are you questioning questioning me about the methods we can use to teach them or the pieces of knowledge we should teach them mhm either so you can talk about the method that we can teach them and what we can.",
        "word_count": 290,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["trash categorization", "obligation", "international community", "implement policies", "raising awareness"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'trust' (trash/rubbish). 'dissolve all the trust' (dispose of/dissolve trash?)."
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
                "why_not_9": "ASR/Pronunciation ambiguity.",
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
        "id": 0, "sample_id": "tGgXWLutx9M_q05",
        "video_id": "tGgXWLutx9M",
        "part": 3,
        "question": "Teaching children?",
        "transcript": "Teach them about so concerning the methods of teaching I think we should make use of know the schools and teachers should make use of videos really simple videos about just some simple aspects of environment such as animals those who are going extinct in order to raise awareness among them about the importance of other life forms to us as humans and concerning the pieces of knowledge we should introduce to them I think it should be made simple as well like introducing to them what truly is natural resources and some small actions that children themselves can take in order to protect the environment for example telling them the negative impacts of throwing trust into the atmosphere instead of throwing trust in in the trust means M",
        "word_count": 128,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["going extinct", "life forms", "natural resources", "negative impacts"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'trust' (trash)."
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
                "why_not_9": "Pronunciation of trash.",
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
        "id": 0, "sample_id": "mJhBTa4NX9Y_q02",
        "video_id": "mJhBTa4NX9Y",
        "part": 1,
        "question": "Hobbies?",
        "transcript": "Of course anyone i think anyone has a hobby because if we do not have a hobby we get bored so we cannot enjoy the life we cannot enjoy the time and definitely we will waste the time and we get bored so i have a hobby like others and most important hobby that i have is going out and catching up with friends having dinner outside going to see my friends and spending time with them okay and do you think hobbies should be shared with other people in my opinion i think no because I am a close person so i do not have many friends so i prefer to have just one close friend or two and share my hobby only with them so this is my character i do not say anyone has to be like me this is me and how i am great and did you have a hobby as a child yes when i was a child i was about like seven years old i really wanted to sing i was crazy about singing and started the learning from my father because my father also used to sing so i got the tricks about singing from my father and i continued when i was like 18 years old i started working with the with the group that they were singing in iran they call the aryan so i used to be their local team in their locality.",
        "word_count": 221,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["crazy about", "catching up"],
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
            "reason": "'close person' (private person? closed?). 'local team' (vocal team?)."
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Minor slips.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Word choice errors.",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range. Band 7.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 7,
        "grammar": 8
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
