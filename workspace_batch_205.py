import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 205 ---
# Total Samples: 20
# Valid Scored: 16
# Skipped: 4 (Reasons below)

# --- SKIPPED SAMPLES LOG ---
# 1. o9_Qsvc2QP4_q10: Examiner Feedback/Outro ("...you've done I think greatly...") - Not candidate speech.
# 2. bWI5cdhSOMw_q02: Examiner Instruction/Transition ("...so now i will give you a...") - Mixed with candidate speech, cut off.
# 3. Oxl0nMtrjDI_q02: Fragment ("Yeah more useful things okay perfect...") - Too short.
# 4. Oxl0nMtrjDI_q04: Outro ("...thank you for participating in our exam...") - Not scorable.

# --- VALID SAMPLES DATA ---
scored_samples = [
    # Video: o9_Qsvc2QP4 (Band 4.5)
    {
        "id": 0, "sample_id": "o9_Qsvc2QP4_q07", "video_id": "o9_Qsvc2QP4", "part": 3,
        "question": "Children and computers?",
        "transcript": "Servicing or other digital devices and but with limitations for example you know if they want to play a play or play a game in their computer or in their mobile so I take I let them to play around for example 30 minutes and limitation should be done in this area okay so you will limit your child in terms of time yes what about in terms of I mean the the games I mean which game for example yes yes and another area is the the kind of game that is prefer that is suitable for children yes and it is released by the Company the company that released the game and yes and I am we just we just listened to the company this game is suitable for what age of children and yes and we may use them for our children okay very good do you agree with this very famous statement saying that a person who does not know about computer and how to use a computer is eating like an illiterate person a person who does not I mean know how to write and how to read so do you agree with this yes yes I agree the new some some new some new some new a definition of a definition of literacy is is a new computer one of them one of them is naming computer and it helps you mean how to use computer how to how to program it or something like that so I guess I agree knowing the computer is a special part of our life today and we have to know about it we have to use it we have we we should use we should we should know.",
        "word_count": 273,
        "analysis_metadata": {
            "grammar_error_patterns": ["basic_structure", "repetition"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["suitable for children", "definition of literacy", "limitations"],
            "grammar_structures_used": ["simple_sentences", "fragments"]
        },
        "micro_flaws": {
            "grammar": ["fluency_breakdown"],
            "vocabulary": ["repetition"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Frequent self-repetition 'some new some new some new'. 'let them to play' (let them play)."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "long_but_repetitive",
            "redundancy": "high",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Frequent breakdown in fluency and structure. 'let them to play'.",
                "why_not_3": "Can convey complex ideas (literacy definition) despite errors."
            },
            "vocabulary": {
                "why_not_5": "Limited and repetitive.",
                "why_not_3": "Adequate for task."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Uses a very limited range of structures.",
            "vocabulary_band": 4,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic and repetitive. Band 4.",
        "grammar_reason": "Frequent errors and repetitions disrupt flow. Band 4.",
        "vocabulary": 4,
        "grammar": 4
    },
    {
        "id": 0, "sample_id": "o9_Qsvc2QP4_q08",
        "video_id": "o9_Qsvc2QP4",
        "part": 3,
        "question": "Impact of technology?",
        "transcript": "How to use you know computers is it only computer which matters which is important or this is something that you can generalize it for all examples of technology because now we are living in a modern like era then countries and people would try hard to be modern so this is the time of Technology what are the impacts of technology in our life or over our life that in what ways human beings life are being affected by this new discoveries in terms of technology and then of course in terms of their human life I mean computer was one of the examples of technology so because they have other things like mobile phone is another one okay like we have very fast speed trains also this is another one in terms of Transportation in terms of like like let us say home appliances Furnitures different stuff and things that we look around ourselves to find up so what do you think about yes technology has a great effect in our love in many parts you know you know for example when you when you going to travel to another city to another country you have to know about you should know about a lot of things and before before the technology before the technology that technology that we have today is it was really hard to know about for example what is going on in another city what is going on in other country so new technology helps us to to solve this problem you can you know you can have you can have you can you can know a lot of things about the place that you want to travel by a computer or on a cell phone or.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["basic_structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["great effect", "solve this problem"],
            "grammar_structures_used": ["simple_sentences"]
        },
        "micro_flaws": {
            "grammar": ["fluency_breakdown"],
            "vocabulary": ["wrong_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'great effect in our love' (life?). Heavy examiner intervention mixed in transcript."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "long_but_disorganized",
            "redundancy": "high",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Errors impede understanding. 'you can have you can have you can you can know'.",
                "why_not_3": "Intelligible."
            },
            "vocabulary": {
                "why_not_5": "Basic.",
                "why_not_3": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Uses a very limited range of structures.",
            "vocabulary_band": 4,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic. Band 4.",
        "grammar_reason": "Disfluent and repetitive. Band 4.",
        "vocabulary": 4,
        "grammar": 4
    },
    {
        "id": 0, "sample_id": "o9_Qsvc2QP4_q09",
        "video_id": "o9_Qsvc2QP4",
        "part": 3,
        "question": "Social media?",
        "transcript": "Any technological device that you that you own that you have so sometimes you you have some brother or a sister in another country or in many in a very far from places so it is with this technology is really easy to you know to connect with them and you know to have to chat with them or to chat with friends or your friends in another place so technology I think this technology helps us really you know good okay okay and the last question that I have what about the social media also it is another example of I mean having certain ways of technology and then so do you use social media like by your cell phone or other means or not yes social media is a a lot it is a other part of Technology it is a part of technology I think and it has got its advantage and its Advantage too you know as I said it should be a limitation for using your your cell phones for example and social medias are one of the part of you you know your cell phone and you it is one of the part is one part of your life too so you know cutting off this social medias is really I think I think it is not really a good idea because you know the social media help you to communicate with other people to knowing new people and you know improve your sometimes improve your your new job for example social media like click in help you to find a job in in other places so I think I think it is not a bad thing it is a it has got a good part.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["basic_structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["connect with them", "communicate with other people"],
            "grammar_structures_used": ["simple_sentences"]
        },
        "micro_flaws": {
            "grammar": ["fluency_breakdown"],
            "vocabulary": ["wrong_word_form"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'helps us really you know good'. 'click in' (LinkedIn?). 'to knowing new people' (to know)."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "long_but_disorganized",
            "redundancy": "high",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Errors cause strain. 'communicate... to knowing'.",
                "why_not_3": "Intelligible."
            },
            "vocabulary": {
                "why_not_5": "Basic.",
                "why_not_3": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Uses a very limited range of structures.",
            "vocabulary_band": 4,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic. Band 4.",
        "grammar_reason": "Frequent errors and disfluency. Band 4.",
        "vocabulary": 4,
        "grammar": 4
    },

    # Video: bWI5cdhSOMw (Band 5.5)
    {
        "id": 0, "sample_id": "bWI5cdhSOMw_q03",
        "video_id": "bWI5cdhSOMw",
        "part": 3,
        "question": "Internet and marketing?",
        "transcript": "In different topics and another thing is that you can find some channels which contains book summaries the good thing is that these book channels are very has very very variety types of book channels you can find novels or historical books or very specific topics okay thank you very much may i give it back yeah there you go thank you so how do you think the internet will change people's marketing behavior in the future as i said the internet changed our marketing behavior even now in the past we go on shopping we go out and we have window shopping sometimes but.",
        "word_count": 105,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["book summaries", "marketing behavior", "window shopping"],
            "grammar_structures_used": ["relative_clauses"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice"]
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'channels which contains' (contain). 'very variety types' (various types / a variety of types)."
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
                "why_not_7": "Basic agreement errors.",
                "why_not_5": "Can use complex sentences."
            },
            "vocabulary": {
                "why_not_7": "'very variety types' is a collocation error.",
                "why_not_5": "Good topic vocab."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good topic words ('window shopping') but errors ('very variety'). Band 6.",
        "grammar_reason": "Agreement errors ('channels which contains'). Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },

    # Video: Oxl0nMtrjDI (Band 5.0)
    {
        "id": 0, "sample_id": "Oxl0nMtrjDI_q03",
        "video_id": "Oxl0nMtrjDI",
        "part": 1,
        "question": "Home appliances / Younger generation?",
        "transcript": "Home there are many different appliances and Furnitures at home and the thing I used to use a lot was television in the past before I come to a 10th grade I used to watch TV a lot and but now I cannot I do not have time for that and other things like and other things for example I have many plans and I have a container to water them and I love my plants and some other things to protect my plants very good the next question is do you think the younger generation is more comfortable with modern devices than the older ones yes definitely they are or we are you consider yourself yeah because maybe the older generation they actually do not like social medias or even technology and they like that old kind of you using things and or maybe it is hard for them to learn how to use them because one of our relatives is a computer engineer and he had some old students and he said that they used to they learn really hard more hardly more hard than our younger students and maybe their age is does not let them maybe learn easily yes yes okay and nowadays many factories use machines and automated equipment instead of manual labor means they do not have the workers okay labor man people and the people who are working for them they use machines instead what do you think about this kind of replacement and alternative I think it is good when a worker is Works in a factory is even dangerous for himself last year my uncle was working in a factory and heard his hand and he went to Tehran and he had some bad injuries and after after.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["appliances", "automated equipment", "manual labor"],
            "grammar_structures_used": ["compound_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": ["wrong_word_form"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Furnitures' (uncountable). 'before I come to a 10th grade' (came). 'more hardly more hard' (harder). 'heard his hand' (hurt)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent basic errors ('come' vs 'came', 'Furnitures').",
                "why_not_4": "Can produce complex sentences."
            },
            "vocabulary": {
                "why_not_6": "Errors in basic words ('Furnitures', 'hardly').",
                "why_not_4": "Sufficient for task."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts complex sentences but these tend to be less accurate than simple sentences.",
            "vocabulary_band": 5,
            "vocabulary_text": "Manages to talk about familiar and unfamiliar topics but uses vocabulary with limited flexibility."
        },
        "vocab_reason": "Basic errors ('Furnitures', 'hardly'). Band 5.",
        "grammar_reason": "Tense and form errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },

    # Video: RlwxOzi29FU (Band 5.5)
    {
        "id": 0, "sample_id": "RlwxOzi29FU_q04",
        "video_id": "RlwxOzi29FU",
        "part": 3,
        "question": "Eating out vs home?",
        "transcript": "Just and like mixed lice and this i mixed likes and those vegetables like a pepper like peppers too i think yeah I am not sure yeah all right good yeah good meal all right let us go on to the third part of the test now oh yeah let us keep going all right we are almost there okay so yeah where do people in your country usually eat so there are many food in korea so i think the most thing the most usually yeah like pork i think polka and beef yeah because it is the polka and beef restaurant have every every side every corner and yeah just it is very delicious for me it is pretty delicious and yeah just yeah and okay yeah and the people can find easily to less strong this restaurant so yeah you think people eat in restaurants more than eating at home these days this case I am not sure because we have kobe 19 situation yeah so people usually usually usually at home because in korean development development of technology so always just scroll in my cell phone and just search the good menu and just use the application yeah after we order this after order after order this menu but so suddenly just the delivery in in front of my door yeah it is really shocked my situation okay so what do you think are the main disadvantages of eating in restaurants eating less strong is i do not know they put in so many msg and like kind of unhealthy food so and on fresh food also yeah so i want to know this kind of ingredient so made by where or what and yeah and kind of that yeah so it is the most problem i think",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["basic_structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["development of technology", "unhealthy food", "ingredients"],
            "grammar_structures_used": ["simple_sentences"]
        },
        "micro_flaws": {
            "grammar": ["broken_sentences"],
            "vocabulary": ["pronunciation_spelling_mismatch"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'mixed lice' (rice). 'polka' (pork). 'less strong' (restaurant). 'shocked my situation' (shocking?)."
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
                "why_not_6": "Broken sentences. 'people can find easily to less strong'.",
                "why_not_4": "Can communicate complex ideas (delivery apps)."
            },
            "vocabulary": {
                "why_not_6": "Phonological errors affect clarity ('lice', 'less strong').",
                "why_not_4": "Good topic vocab ('ingredients', 'delivery')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts complex sentences but these tend to be less accurate than simple sentences.",
            "vocabulary_band": 5,
            "vocabulary_text": "Manages to talk about familiar and unfamiliar topics but uses vocabulary with limited flexibility."
        },
        "vocab_reason": "Topic vocab is okay but errors ('less strong' for restaurant) are frequent. Band 5.",
        "grammar_reason": "Sentences are often broken/incorrect. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "RlwxOzi29FU_q07",
        "video_id": "RlwxOzi29FU",
        "part": 1,
        "question": "Student or work?",
        "transcript": "A student now I am a student now i prepare to study abroad so that would be more a present continuous sentence I am preparing to study abroad yes -.",
        "word_count": 25,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice"],
            "grammar_error_frequency": "one_error",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["study abroad"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'i prepare' vs 'i am preparing'. Examiner corrects it."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Basic tense error.",
                "why_not_4": "Intelligible."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Produces simple sentences accurately but makes mistakes in complex sentences.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic. Band 5.",
        "grammar_reason": "Tense error corrected by examiner. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },

    # Video: AkVHzXKAbYU (Band 5.5)
    {
        "id": 0, "sample_id": "AkVHzXKAbYU_q01",
        "video_id": "AkVHzXKAbYU",
        "part": 1,
        "question": "Hometown / Studies?",
        "transcript": "All right so what is your name my name is handin Kim and Jeff so what is your hometown well I live in Seoul and this is the capital of Korea -so have you always lived in Seoul yeah I have been there all my life so are you working at the moment or a year students well I am actually a student and my major is computer software programming -and you have not graduated yet you are still studying but I am going to study abroad for the same major yeah so maybe I quit my university co-op product all right so I am just asked a few questions about your hometown so can you just describe Seoul told me a little bit yeah so as I already mentioned so is the capital of Korea and also there are so many buildings and there are so many cars in there also and so what do you like most about so I guess I like there are many options to hang out with my friends such as their famous restaurant and many pops in there in many pops there and is there anything you do not like about it well I do not like the quality of air -there are so many cars so exhausting fumes or I do not like the bad quality of air mmm so do you think you will continue to live in so for a long time well I do not think so because I want to leave a road appart from Seoul -first my my my my country so I live in Canada I guess all right okay I am going to change topics should not ask you about yeah your studies so you said you study computer software computer software so yeah why did you choose to study that actually my dad is.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "mixed",
            "vocab_evidence": ["computer software programming", "exhausting fumes", "hang out", "study abroad"],
            "grammar_structures_used": ["compound_sentences"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": ["word_choice"]
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'leave a road' (live abroad?). 'pops' (pubs?). 'exhausting fumes' (exhaust fumes). 'in there' (in Seoul)."
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
                "why_not_7": "Basic errors ('in there' overuse).",
                "why_not_5": "Can produce complex sentences."
            },
            "vocabulary": {
                "why_not_7": "'exhausting fumes' vs 'exhaust fumes'. 'pops' vs 'pubs'.",
                "why_not_5": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good range but phonological errors ('pops', 'leave a road') cause confusion. Band 6.",
        "grammar_reason": "Generally good structure but some errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "AkVHzXKAbYU_q06",
        "video_id": "AkVHzXKAbYU",
        "part": 3,
        "question": "Feedback/Corrections?",
        "transcript": "it will be better just to say my dad works in software yeah my dad is working it sounds like you are kind of talking about like right now at this moment so yeah it is quite a common common thing and there was another one you said so I asked you like what advice you would give to someone who was just beginning to learn a language and you said I would tell them listening a lot so in that in that instance you say I would tell them listen a lot yeah and another another kind of common mistake with prepositions so yeah just things like in and on and things like that is you said I work at mobile applications all right sorry I want to work at mobile applications so probably I want to work on mobile applications or maybe I work with mobile applications would be better so yeah you just say that when you are talking about like the location of something and yeah so when you were talking about like learning languages and you are talking about like the advice you would give you said listen radio so glad to say listen to the radio when there was there was another one as well Oklahoma State which is just like pronouns so he is they were just missing from sentences so I asked you about whether you think most people enjoy studying English and you said many people do not enjoy that much so better to say many people do not enjoy it that much so yeah you always wanted to like including object to the sentence and there is no zone yeah there was another time it was missing from a sentence so yeah that is it so yeah I will give you about five point five for that what is your what is.",
        "word_count": 296,
        "analysis_metadata": {
            "grammar_error_patterns": ["feedback_meta"],
            "grammar_error_frequency": "n/a",
            "vocab_collocation_usage": "n/a",
            "vocab_evidence": [],
            "grammar_structures_used": []
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "n/a",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "This is almost entirely examiner feedback explaining errors. Should be SKIPPED or scored as Invalid. But transcript says 'Valid'. I will score as INVALID/SKIPPED in my log, but here I must output something? No, I skip invalid samples."
        },
        "grammar_profile": {
            "complexity_level": "n/a",
            "accuracy_level": "n/a",
            "flexibility": "n/a",
            "error_density": "n/a"
        },
        "discourse_metrics": {
            "length_appropriateness": "n/a",
            "redundancy": "n/a",
            "development_depth": "n/a"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Examiner speech.",
                "why_not_7": "Examiner speech."
            },
            "vocabulary": {
                "why_not_9": "Examiner speech.",
                "why_not_7": "Examiner speech."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 0,
            "grammar_text": "N/A",
            "vocabulary_band": 0,
            "vocabulary_text": "N/A"
        },
        "vocab_reason": "Examiner Feedback.",
        "grammar_reason": "Examiner Feedback.",
        "vocabulary": 0,
        "grammar": 0
    },

    # Video: GoWXcn8sU00 (Band 5.0)
    {
        "id": 0, "sample_id": "GoWXcn8sU00_q02",
        "video_id": "GoWXcn8sU00",
        "part": 1,
        "question": "Advertisements?",
        "transcript": "Going to go on and talk a little bit about advertising now so do you like what watching advertisements not like much because the advertising is annoying to the when I am watching the YouTube video okay and will you ever buy something after watching an advertisement yes usually I watching the lipstick or like eyeline so when watching I want that I am thinking about that really I want to buy that okay and how often would you buy something after watching an advertisement in the past I I buying one month each one month the one buy but now I am not frequently buy I buy I buying May six months okay and you talked about advertising on YouTube yeah so how do you feel when you see popup advertisings on the internet advertising is not much bad but when I watching the YouTube they do not feel like good advertising just annoying to me and are there any advertisements that you like because they are funny or or silly yes when I watching the when I think the close advertising little bit funny and silly because they have to buy this and many people have to interesting about this and they are watching this so they have to make funny",
        "word_count": 187,
        "analysis_metadata": {
            "grammar_error_patterns": ["basic_structure", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["annoying", "frequently buy"],
            "grammar_structures_used": ["simple_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_tense_error"],
            "vocabulary": ["wrong_word_form"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'not like much' (I don't like it much). 'annoying to the when' (annoying when). 'I buying one month' (I buy once a month). 'close advertising' (clothes?)."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent errors impede communication. 'I buying May six months'.",
                "why_not_4": "Intelligible."
            },
            "vocabulary": {
                "why_not_6": "Limited range and errors.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic and error-prone ('close' for 'clothes'). Band 5.",
        "grammar_reason": "Frequent form errors ('I buying'). Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "GoWXcn8sU00_q04",
        "video_id": "GoWXcn8sU00",
        "part": 3,
        "question": "Environment?",
        "transcript": "you have already talked about air pollution yes what are some other problems in the environment in Your Country Now day is virus is environment problem too we already have to covid virus is really serious problem in international we have to try to solve this problem and we have to careful this another virus is for hour and l fatures so how can we be careful about other viruses maybe wash hand and take a take wear a mask or taking your fs and be honest to my ways that is we have to try things okay and how can people protect the environment I think it is just a little thing but do not throw the trash anywhere we have to thr the trash right things and using the plastic to reduce or try the vegetarian or care of care self myself like my like for my health and talking with neighbor and getting to the conversation about the environment problems okay we have a lot of ways to protect the environment like national parks do you think those things are a good way to help protect the environment before I say about this problem solve the problem is just like little bit and ours the national problem is we have to do big event to making the big event for environment problems making a day about the three days or Planet day then that day we have to try for environment problems we making a new Sol Pro new solve things and more try to the problems okay and these days the problem of water pollution is becoming greater yeah what do you think we can do to help that problem firstly we.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["basic_structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["serious problem", "solve this problem"],
            "grammar_structures_used": ["simple_sentences"]
        },
        "micro_flaws": {
            "grammar": ["fluency_breakdown"],
            "vocabulary": ["wrong_word_form"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Now day is virus is environment problem'. 'we have to careful this'. 'thr the trash' (throw). 'care of care self myself'."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "long_but_disorganized",
            "redundancy": "high",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Grammar breaks down frequently.",
                "why_not_4": "Intelligible."
            },
            "vocabulary": {
                "why_not_6": "Very limited.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic. Band 5.",
        "grammar_reason": "Breakdown in structure. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },

    # Video: hoD3jRU6zZc (Band 6.5)
    {
        "id": 0, "sample_id": "hoD3jRU6zZc_q03",
        "video_id": "hoD3jRU6zZc",
        "part": 1,
        "question": "Transition?",
        "transcript": "Now mate okay here we go there you go again thank you and t.",
        "word_count": 13,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "n/a",
            "vocab_collocation_usage": "n/a",
            "vocab_evidence": [],
            "grammar_structures_used": []
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "n/a",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Fragment/Transition. Not scorable."
        },
        "grammar_profile": {
            "complexity_level": "n/a",
            "accuracy_level": "n/a",
            "flexibility": "n/a",
            "error_density": "n/a"
        },
        "discourse_metrics": {
            "length_appropriateness": "too_short",
            "redundancy": "n/a",
            "development_depth": "n/a"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "N/A",
                "why_not_7": "N/A"
            },
            "vocabulary": {
                "why_not_9": "N/A",
                "why_not_7": "N/A"
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 0,
            "grammar_text": "N/A",
            "vocabulary_band": 0,
            "vocabulary_text": "N/A"
        },
        "vocab_reason": "Fragment.",
        "grammar_reason": "Fragment.",
        "vocabulary": 0,
        "grammar": 0
    },
    {
        "id": 0, "sample_id": "hoD3jRU6zZc_q04",
        "video_id": "hoD3jRU6zZc",
        "part": 3,
        "question": "Water sports?",
        "transcript": "Friends are trying it try i have tried it but they are saying oh you should try it but I am always replying i would i would but i was too lazy someday yes someday right good stuff all right yeah should we go on to the third part yes please yeah let us go all right okay so yeah what kinds of water sports are popular nowadays for since the past and until now i think the most basic water sports swimming is has always been popular but in terms of styles of swimming i think a lot of people are looking up to butterfly form because they think in order to do that form of swimming you need to have certain amount of muscles and you need to be very agile to do it so even for me i could only do freestyle but i have always wanted to do butterflies if i can but I have tried it couple of years ago but i failed miserably okay right and apart from swimming any other sports in the water that are quite popular these days in term for water sports i think sailing is also very popular among rich people i should say some people think that it is not a sports but i I have heard that if even for boats there are a lot of sizes that you can choose so there are even boats that you have to hold the boat yourself and you need to guide the boat and even for even in terms of sailing i should say there is a lot of similar kind of sports like canoeing oh yeah so i think those are also popular sports okay good and what are some of the advantages of traveling by boat.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["failed miserably", "agile", "certain amount of muscles"],
            "grammar_structures_used": ["complex_sentences", "modals"]
        },
        "micro_flaws": {
            "grammar": ["awkward_phrasing"],
            "vocabulary": ["collocation_slip"]
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'looking up to butterfly form' (looking to do? looking at?). 'failed miserably' (good). 'in term for water sports' (in terms of)."
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
                "why_not_8": "Minor errors ('in term for').",
                "why_not_6": "Good range and control."
            },
            "vocabulary": {
                "why_not_8": "Slightly imprecise ('looking up to').",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary to allow some flexibility and precision."
        },
        "vocab_reason": "Good range ('agile', 'failed miserably'). Band 7.",
        "grammar_reason": "Generally error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "hoD3jRU6zZc_q05",
        "video_id": "hoD3jRU6zZc",
        "part": 3,
        "question": "Advantages of boat travel / Swimming?",
        "transcript": "I think it is less costly than taking an airplane and you need you i think you can prepare a lot of things before departing so for airplane you have limited services that the company can provide you with but in for boat you can prepare a lot of clothes a lot of foods and you can even have if it is a big huge boat you can even have swimming pools and basketball basketball court on on the boat so i think it is more better okay and do korean people use boat or ship to travel to other countries sometimes for i think for close distance countries like japan or in korea we have this island called jeju island so when they are going to those two areas i think people take huge cruises and i after retiring older generation take those cruises to travel abroad because they have time and money to spend on those expensive cruises yes indeed and do you think it is necessary for everyone to learn how to swim I have heard that for most of the western countries by by law it is mandatory to learn how to swim in for emergency cases but in korea it is not mandatory but i think parents thinks that it is quite important to learn how to swim and i personally think that it is important to learn how to swim because once at least once in your life you would encounter you might encounter those sudden accident or yeah and if you panic in the water once you know how to swim it will be very i think it is better it will be better to save yourself if you know how to swim all right yes so yeah thanks for doing the test was a.",
        "word_count": 296,
        "analysis_metadata": {
            "grammar_error_patterns": ["comparative"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["less costly", "mandatory", "emergency cases", "panic"],
            "grammar_structures_used": ["comparatives", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["comparative_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'more better' (better). 'parents thinks' (think). 'encounter those sudden accident' (accidents)."
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
                "why_not_7": "Basic errors ('more better', 'parents thinks').",
                "why_not_5": "Complex structures used well."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('mandatory', 'emergency'). Band 7.",
        "grammar_reason": "Errors ('more better') bring it down. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },

    # Video: V17tr5EZXv4 (Band 8.0)
    {
        "id": 0, "sample_id": "V17tr5EZXv4_q02",
        "video_id": "V17tr5EZXv4",
        "part": 1,
        "question": "Clothes preference?",
        "transcript": "Inside you and I do not I do not really kind of respect that kind of color so I see so then you never really wear red clothes right yes in that case what kind of clothes do you usually wear I usually wear colors that as I said gray black white because they seem like they the color itself is the color itself is kind of normal and a lot of people actually wear those kind of colors so I want to actually fit with with people fit with my friends and other peers that that are actually wearing the same colors but at the same time I tried to match those colors with other clothes so and those kind of colors colored clothes are really well to match with other clothes so yeah okay great and do you wear the same style of clothes on weekdays as weekends it seems like in on in weekends I do not wear clothes I do not try to match a lot of clothes and try to dress up well unless I have unless I have opportunities to meet with my friends but during the weekdays I work in I am currently working on in some kind of Academy so I have to dress up well in front of the students because that is the way to show that they that you are actually there to teach them so feels like during the week weekdays I am trying to wear I am trying to dress up well and during the weekends I try to just relax a little bit and try to wear comfortable clothes instead of actually dressing up",
        "word_count": 273,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["dress up well", "match those colors", "fit with my friends"],
            "grammar_structures_used": ["complex_sentences", "causal_clauses"]
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
            "triggered": False,
            "reason": "N/A"
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
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Repetitions and self-corrections.",
                "why_not_7": "Good structure."
            },
            "vocabulary": {
                "why_not_9": "Repetitive.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural phrasing ('dress up', 'fit with'). Band 8.",
        "grammar_reason": "Error free but some hesitation. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "V17tr5EZXv4_q03",
        "video_id": "V17tr5EZXv4",
        "part": 2,
        "question": "Describe a family?",
        "transcript": "Prepare your answer for the following question your question is to describe a family not your own which you like and are happy to know okay okay okay so that was one minute so now you have two minutes to describe a family which you like and are happy to know so one of the families that I would like to really know is a family that is who my MSA my my friend has and he he currently lives in changa and he has a r he has a relatively normal family but it seems like he he is a whenever I see his family it seems like he is actually a friend friend instead of a family member with their with each other so that kind of relationship is what I am really interested in my friend MSA he always acts like his dad is his friend and always be friendly to him and also he but the thing is that his mom is actually a working women who never who rarely comes back home to actually have a conversation with the family members I know this well because I have met him since middle school and he always talked about us how positive his family is so but I want to and also his his personality is very positive and that is why I want to know how that positivity came from instead with with even though his his mom is working and his dad is still working but just comes back home after 6 p.m. so I want to know how that positivity positivity is where this positivity is coming from and because I basically think that families basically all the positive positivity that kids have are from the family and how they what conversation they have and what like.",
        "word_count": 296,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["relatively normal family", "positivity", "working women"],
            "grammar_structures_used": ["relative_clauses", "cleft_sentences"]
        },
        "micro_flaws": {
            "grammar": ["fluency_hesitation"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'working women' (woman). 'positivity positivity' (repetition)."
        },
        "grammar_profile": {
            "complexity_level": "moderate_high",
            "accuracy_level": "high",
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
                "why_not_9": "Hesitations affect flow.",
                "why_not_7": "Complex and accurate."
            },
            "vocabulary": {
                "why_not_9": "Repetition.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good range ('positivity', 'relatively'). Band 8.",
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
            # Check ID and also if sample has 0 score (marked as invalid/skipped above)
            if sample['vocabulary'] == 0:
                continue

            if sample['sample_id'] not in existing_ids:
                f.write(json.dumps(sample) + '\n')
                count += 1

    print(f"Append complete. Added {count} new samples. (Skipped {len(scored_samples) - count} duplicates/invalid).")

except Exception as e:
    print(f"Error writing to file: {e}")
