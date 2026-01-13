import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 226 ---
# Total Samples: 20
# Valid Samples: 17

scored_samples = [
    {
        "id": 0, "sample_id": "Yz9fa7cVUpg_q06", "video_id": "Yz9fa7cVUpg",
        "part": 1,
        "question": "Hometown?",
        "transcript": "well I I born in the city. I did not visit my hometown regularly. I visited there in a year or in a month. But I think that home my hometown is a great place to live in the future because in this city there is the traffic jams the pollions it is a problem for me and if I got a to if I got a house to in my hometown to build my own house then I will of course stay in my hometown because the environment and the nature gets my heart.",
        "word_count": 86,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form", "word_choice"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["traffic jams", "pollions", "nature"],
            "grammar_structures_used": ["conditionals", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_tense_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'I born' (I was born). 'pollions' (pollution). 'nature gets my heart' (touches/captures)."
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
                "why_not_6": "Frequent errors ('I born').",
                "why_not_4": "Can communicate complex ideas."
            },
            "vocabulary": {
                "why_not_6": "Errors ('pollions').",
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
        "grammar_reason": "Frequent basic errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Yz9fa7cVUpg_q08", "video_id": "Yz9fa7cVUpg",
        "part": 1,
        "question": "Help others?",
        "transcript": "of course not because in the past people help each other so much at that time. But in this moment from now people do not care about each other and they do not help they do not want to help each other.",
        "word_count": 40,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_tense"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["simple_sentence", "compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["verb_tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'people help each other' (helped). 'in this moment from now' (nowadays?)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "moderate",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Tense errors.",
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
        "grammar_reason": "Tense errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Yz9fa7cVUpg_q09",
        "video_id": "Yz9fa7cVUpg",
        "part": 3,
        "question": "Contribution?",
        "transcript": "Everybody has their own capacity and how can they contribute to their communities. well I did not know about that so much but in our country in Bangladesh school and college teachers can provide their educations to the poor kids who wants to study but did not have the money to admit in the schools or in a diseases countries diseases people can provide some monies to the donation they can give some donations they can help the people who are who lost their house and do do not have to eat people lost their house and they do not they okay how can schools encourage young people to help others in the schools the teachers can teach their students to help the peoples who are troubled or who are poor. they did not get eat foods in their daily lives. teachers can teach their students to help them to have some meal and know what in trouble the students can go to help them and that kind of things school can teach the students.",
        "word_count": 165,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_agreement", "word_choice", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["capacity", "donation"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'provide their educations' (education). 'admit in the schools' (get admitted). 'diseases people' (sick people). 'provide some monies' (money). 'get eat foods' (get food)."
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
                "why_not_6": "Frequent breakdown.",
                "why_not_4": "Sustained attempt."
            },
            "vocabulary": {
                "why_not_6": "Multiple errors.",
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
        "id": 0, "sample_id": "Yz9fa7cVUpg_q10",
        "video_id": "Yz9fa7cVUpg",
        "part": 3,
        "question": "Financially?",
        "transcript": "I think there is other ways to assist because if you help someone giving their some monies they will depend on you. But if you help them to develop something or helping them their businesses they can relay on that thing. they can earn money daily and grow their business as well. Then they can help other people's. So I think that the second option is the better.",
        "word_count": 66,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["develop", "business"],
            "grammar_structures_used": ["conditionals", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["word_choice_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'giving their some monies' (them money). 'relay on' (rely on). 'help other people's' (people)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Errors persist.",
                "why_not_4": "Conditionals used."
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
        "vocab_reason": "Basic errors. Band 5.",
        "grammar_reason": "Accurate conditionals but errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Yz9fa7cVUpg_q11",
        "video_id": "Yz9fa7cVUpg",
        "part": 3,
        "question": "Unwanted help?",
        "transcript": "people always do not offer to help someone. when a person get in trouble really that time he asked for help someone and some people did not get interest to help them but who are in kind and helpful to someone they stands with them and that time they help the problem man.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_order", "agreement"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["phrasing_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'help the problem man' (the person with the problem). 'people always do not offer' (don't always)."
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
                "why_not_6": "Phrasing errors.",
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
        "id": 0, "sample_id": "9KNKj0Od4Gk_q03",
        "video_id": "9KNKj0Od4Gk",
        "part": 3,
        "question": "Teachers or parents?",
        "transcript": "I think parents like teachers they also have a ex like important role of teaching them basic stuff you know history and math and like maybe English but the most important part is how to like lead them guide them to a really nice way how to grow up how to help others and have some space and time of yourself that you can develop yourself like yeah okay great and do you think smart people tend to be selfish SM people I think it depends but U most of the people I saw like really smart my exchange semester I saw some really smart friends who were studying barcel the same as me but they were working at the same time for bar Clays or something like it is a really big a company like it is global company so I was like wow that is crazy and yeah but there were like I I do not think they meant it but sometimes they they act like they do not care about others feelings yes that is why I thought like that I see okay and now your final question are smart people happier than others oh this is a hard question like happy and smart I do not think it is a really related question but maybe they are happier if they have more money they have more time and they know how to you know use them in the proper way yep MH that is it that is it all right okay very very good so.",
        "word_count": 257,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["exchange semester", "global company", "feelings"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
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
            "reason": "Frequent fillers 'like', 'you know'. 'barcel' (Barcelona). 'bar Clays' (Barclays)."
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
                "why_not_8": "Hesitations affect flow.",
                "why_not_6": "Good accuracy."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range, sufficient for 7.",
        "grammar_reason": "Frequent error-free, but flow interrupted by 'like'. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "3C-uVgVCOIA_q02",
        "video_id": "3C-uVgVCOIA",
        "part": 1,
        "question": "Town?",
        "transcript": "Is not a big city it is basically for the bad town and the people stay there and they go to work to the song so there is a noise not so much things that is distracting what do you not like about it with the onion yeah well I think it is the author the same thing and it is too quiet so there is no what would you say an excitement about the where I lived in so I always when I was young I always went to Seoul to have fun with my friends so that was kind of I did not like about it",
        "word_count": 105,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["bed town", "distracting", "excitement"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["phrasing_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'bad town' likely 'bed town' (dormitory town). 'to the song' (to Seoul)."
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
                "why_not_9": "Minor slips.",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "ASR ambiguity.",
                "why_not_7": "Bed town is excellent."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Bed town is high level. Band 8.",
        "grammar_reason": "Good flow. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "3C-uVgVCOIA_q03",
        "video_id": "3C-uVgVCOIA",
        "part": 3,
        "question": "Phone scam?",
        "transcript": "Which is basically lie the for example with a few years ago I got a text which is which says that I my father was taken yeah so that was quite a absurd so I did not believe it in the first time so yeah that I think that is the example of the the weird messages I got yeah and final question in what circumstances or situations is making a phone call better than sending a text message in what cases the phone call is better than text messages I think I think the communicating with the family is in that case the calling is much better than the texting because you know the when you as I as I said that when you the text message with other people you cannot share the emotional reaction so but when it comes to the talking with the family the most important thing is that the emotional reaction between them so whatever I text with my father and my mother I feel like I am kind of there is a wall between me and them so that that feels kind of not not that good so I prefer the calling with them so yeah sure",
        "word_count": 204,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["emotional reaction", "wall between me and them", "absurd"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["hesitation_markers"],
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
                "why_not_9": "Hesitations.",
                "why_not_7": "Superior."
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
        "grammar_reason": "Fluent. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "3C-uVgVCOIA_q04",
        "video_id": "3C-uVgVCOIA",
        "part": 2,
        "question": "Foreign job?",
        "transcript": "To have in a foreign country well I am not sure if this will be possible but personally I want to have a the short-term job a short-term job as internship whatever in the United States the company is called the the neuralink the it is the company that let me just say the the produce the the brain chip which is basically for the the helping people with the neural disability you know there are so many people who has the nerve disability and some people cannot move their their arms or the body because of their some car accident whatever it is so the basically the situation they have is the the their brain and their the body cannot be fully connected because of the accident physically so that brain chip helps to connect in those two parts and by the sending and receiving the signal and the center signal between the brain and then the body parts and that is how it works I got to know about this job about this company because while I was browsing the YouTube the video you know you know it is basically about because of the Elon Musk the company is found by the Elon Musk and he explained about the company basically for the helping the people with the nerve disability and I think that is quite fascinating and it looks it looks a little impossible but the people are doing hard work for doing that and I think the personal thing it would be done so yes as a the person who is good okay that is two minutes yeah nicely done.",
        "word_count": 270,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "articles"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["internship", "neural disability", "brain chip", "fascinating"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'the Elon Musk' (Elon Musk). 'nerve disability' (neurological?)."
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
                "why_not_9": "Minor article errors.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "Minor technical terms.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Sophisticated. Band 8.",
        "grammar_reason": "Complex structures. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "3C-uVgVCOIA_q05",
        "video_id": "3C-uVgVCOIA",
        "part": 3,
        "question": "Young people abroad?",
        "transcript": "Foreign countries I do not know it depends on a person really as for some people who want who are interested in marketing they could get a short-term job or any job which is related to the marketing another country for for other people who are who are interested in the computer programming the codings just like me that they could get an internship in in in the companies that in the field in other country so I think there is no the limitation on on what kind of company the people could get even though when they are young so yeah I think it depends on the what the people are interested in okay yeah and is it good for young people to have the experience of living and working in other countries actually I do not have a experience having a job in other countries so I am not really sure about this question but I I guess it would help because because they are having a job in other country that helps people with the broadening deals their sons for perceiving the world it is I think it is a huge difference for example when you when you do not have any any experience and just stay in one country and have a job and if they in their entire life in the one country it is also good but in order to do the bigger thing it is a chance they are making a business exporting products I think there is a limitation on that so if if someone is interested in or just say the company which which provides the product to other country I think the the working of the country it helps a lot okay good and why are some people.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["marketing", "internship", "limitation", "perceiving the world"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["phrase_error"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'broadening deals their sons' (horizons?)"
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
                "why_not_9": "ASR garble.",
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
        "grammar_reason": "Strong. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "3C-uVgVCOIA_q06",
        "video_id": "3C-uVgVCOIA",
        "part": 3,
        "question": "Domestic vs International?",
        "transcript": "Unwilling to work in other countries again I think this is this depends on a person but based on my personal experience of experience some people are not interested in working in another country because they are shy and they are not confident there are the people who wants to have a job in other country but they are not confident to do that basically because of the the language and the other thing is that they are obsessed with the being perfect person I think you know nobody nobody can cannot be perfect so if you are obsessed with this this thing they cannot do anything in any field including including anything so including the working in other countries so yeah the lack of confidence is the fundamental thing and what is the difference between working in an international company and working in a domestic company I think the the biggest difference is the culture you know when you when you say domestic country in Korea I mean obviously the culture in that the company will be more like the the Korean culture such as the there are much more the strict hierarchy they are based on the age and but the on the other hand for the international companies that I guess again I do not have an experience on that not having a job in an international country but I think it would be much loose more lose compared to the Korean country yeah so the cultural thing would be the biggest difference I think okay good the end thank you nicely done.",
        "word_count": 257,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["obsessed with", "strict hierarchy", "fundamental"],
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
            "triggered": True,
            "reason": "'obsessed with the being perfect person' (being a perfect person)."
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
        "vocab_reason": "Strong vocabulary. Band 8.",
        "grammar_reason": "High accuracy. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "szu7Xf18cwA_q02",
        "video_id": "szu7Xf18cwA",
        "part": 1,
        "question": "Primary school?",
        "transcript": "So I went to this very beautiful elementary school which is quite near my house and in that school everybody was very tough actually. So I had quite a good education from there.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["elementary school"],
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
        "id": 0, "sample_id": "szu7Xf18cwA_q03",
        "video_id": "szu7Xf18cwA",
        "part": 1,
        "question": "Secondary school?",
        "transcript": "So when I got to the secondary school actually I got into math mathematics specialized class. So actually my life got a little bit harder but it was fine. I could manage that.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["specialized class", "manage"],
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
                "why_not_8": "Short.",
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
        "id": 0, "sample_id": "szu7Xf18cwA_q04",
        "video_id": "szu7Xf18cwA",
        "part": 1,
        "question": "Fav subject?",
        "transcript": "Well I guess English. I did spend a lot of time studying it since I was 6 years old and still studying it until today. Why? I just love languages. I love foreign languages. I even managed to learn a little bit of French and planning to learn Chinese too. So I guess it is very important for a person to know different languages. Thank you. Now I am going to give you a topic and I would like you to talk about it for one to two minutes.",
        "word_count": 89,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["managed to learn", "foreign languages"],
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
                "why_not_9": "Simple complex.",
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
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Natural but standard. Band 7.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "szu7Xf18cwA_q07",
        "video_id": "szu7Xf18cwA",
        "part": 3,
        "question": "Home?",
        "transcript": "She could make a whole adventure but at the end the what she wants the most is coming back home because home is where you are from. Home is what you will become and home is what you will take as the route to contribute to the culture to your c country.",
        "word_count": 51,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["route to contribute", "what you will become"],
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
            "flexibility": "moderate",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "abstract"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Short.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "Short.",
                "why_not_7": "Abstract."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Abstract thought. Band 8.",
        "grammar_reason": "Complex. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "szu7Xf18cwA_q10",
        "video_id": "szu7Xf18cwA",
        "part": 3,
        "question": "18 years old?",
        "transcript": "To me 18 is not young anymore. So basically when you are 18 and you have the right to vote, you have the right to drive and in some country you have the right to drink. That means the society sees you as a person, a mature person who has full responsibility to the society and your life.",
        "word_count": 57,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["full responsibility", "mature person", "right to vote"],
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
                "why_not_9": "Standard complexity.",
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
        "id": 0, "sample_id": "szu7Xf18cwA_q11",
        "video_id": "szu7Xf18cwA",
        "part": 3,
        "question": "Leaving home?",
        "transcript": "Right now it is not so common but lots of people are doing that especially the young generation even younger than me I know that in my generation it is not a usual thing say I think in my class I was the only one to do so I left home at 18 to pursue my own career that I chose but at the end and in order to leave home at a young age like 18 what sort of qualities do you think you need knowledge and responsibility and that could be built during your education in school and also by your family.",
        "word_count": 103,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["pursue my own career", "young generation"],
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
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
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
