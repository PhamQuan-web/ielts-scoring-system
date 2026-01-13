import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 202 ---
# Total Samples: 20
# Valid Scored: 16
# Skipped: 4 (Reasons below)

# --- SKIPPED SAMPLES LOG ---
# 1. LVlJZIkTMDE_q06: Examiner Feedback/Instruction ("And it tells you to explain how you felt... let us see how orhan does") - Not candidate speech.
# 2. Cp_POC_0WhA_q01: Intro/Promo ("Foreign let us watch Rajiv... I will give you tips") - Not candidate speech.
# 3. Cp_POC_0WhA_q05: Transition/Instruction ("Better English now on to the rest... I am going to show you some questions") - Not candidate speech.
# 4. IevmdO16GuE_q02: Fragment ("Of your home if you just have like those planted trees around you.") - Too short/incomplete to score reliably.

# --- VALID SAMPLES DATA ---
scored_samples = [
    # Video: ybNEwnnIxWw (Band 9.0)
    {
        "id": 0, "sample_id": "ybNEwnnIxWw_q06", "video_id": "ybNEwnnIxWw", "part": 3,
        "question": "Should scholarships only be given to gifted children?",
        "transcript": "We effectively cut her loan by half and that is amazing should scholarships only be given to gifted children in a world with finite resources I I suppose I guess this is a tricky question right because if there are own n number of seats and there is a cost that is why and whatever then you have to ensure that students who are I guess U academically talented or talented at a sporting level or an athletic level or whatever are able to get that push that they need because there are only limited seats so you know if they are not going to get it then somebody else is going to get the seat and they are going to miss out so in that scenario yes scholarships and when I in this scenar in this sense I mean 100% scholarships should be given to gifted children because they have displayed some sort of aptitude or level where they can succeed and they should be given that push I think now who determines how scholarships are given out and I know there is a lot of Foul Play at the University level or you know this guy is my cousin's kid so give him 100% scholarship it should not be like that there should be an unbiased counsil that has to vote and decide or however these things are done but it should be fair but in a world with limited seats and limited opportunities I guess you know you have to make sure that students who are who display a level of talent get access to those scholarships I suppose but again just coming back to the previous question if if every student was allowed to study that is a much more Ideal World I think some people think that Charities should provide.",
        "word_count": 273,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["finite resources", "academically talented", "displayed some sort of aptitude", "unbiased counsil", "foul play"],
            "grammar_structures_used": ["conditionals", "complex_sentences", "modals"]
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
                "why_not_9": "Maintains control.",
                "why_not_7": "Superior complexity."
            },
            "vocabulary": {
                "why_not_9": "Precise terms 'finite resources', 'aptitude', 'unbiased'.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise and sophisticated vocabulary ('aptitude', 'unbiased'). Band 9.",
        "grammar_reason": "Sustained control of complex arguments. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "ybNEwnnIxWw_q08", "video_id": "ybNEwnnIxWw", "part": 3,
        "question": "Future of education / Universities?",
        "transcript": "I have the resources my ambition in life is to someday open schools not university schools at the primary level or up to the Middle School level and make it free just for any student to come and get a great education for free literally so that is something that I am passionate about that is also why I work a 100 hours a week on secure my scholarship so I mean if there is a charity or a nonprofit that is committed to this cause then 100% and the third I guess stakeholder is the universities themselves I mean let us let us get one thing straight right universities are incredibly wealthy institutions you look at not even your top 20 or top 30 you look at your top 200 universities in the US in the UK they have billion doll endowment funds that are invested into you know some some invested into government bonds or t- builds or or whatever it may be there are billion I think Harvard's endowment fund is 40 billion or 50 billion I mean do not quote me on that but it is it is in that ballark range that is a lot of money from a un iversity standpoint as well I I I feel like it should just be a part of their social responsibility to give back to the community that has given them so much that is what I think how will third level education change in the future I think tary education u university education is going to get more creative it is already happening as well but I mean these like higher education is something that it will never go through like a a sudden like shift a lot of people said after Co everything will be online physical campuses are done whatever.",
        "word_count": 302,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["endowment funds", "stakeholder", "government bonds", "social responsibility", "tertiary education"],
            "grammar_structures_used": ["complex_sentences", "cleft_sentences"]
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
                "why_not_9": "Maintains control.",
                "why_not_7": "Superior complexity."
            },
            "vocabulary": {
                "why_not_9": "Highly specific financial/educational terms ('endowment funds', 'stakeholder', 'tertiary education').",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Specific domain vocabulary used naturally ('endowment funds', 'stakeholder'). Band 9.",
        "grammar_reason": "Complex and accurate. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },

    # Video: MUj-UaHrHS8 (Band 8.0)
    {
        "id": 0, "sample_id": "MUj-UaHrHS8_q02", "video_id": "MUj-UaHrHS8", "part": 1,
        "question": "Do you like watching sports?",
        "transcript": "The energy for you know the day to get started but to be honest right now I do not really eat breakfast I would just drink coffee it is so much easier and I feel like I want to spend more time on doing something else than eating breakfast which is kind of I do not know but yeah I feel that way indeed all right now we are going to talk about sports programs okay so do you like watching sports programs on TV yes and no it depends on what sports program it is for example I am really into volleyball especially like the Korean woman volleyball so I would definitely watch that but except for that no not really so it depends on the programs yeah and do you like to watch live sports games if it is like Olympic like a big sports event I would definitely watch since I am also studying event so it is also like studying but also watching something fun but if it is not like a big event I I would not watch okay and who do you like to watch sports games with oh my friends or my family I do not think it really depends like who I am watching it actually it depends I like to watch it with people who likes the sports so we can cheer for the same team maybe we can argue I think that way it is even more fun yep and what kind of games do you expect to watch in the future in the future I am not sure about that question but yeah I would again go for it volleyball since I am really into it and yeah volleyball I will say yeah okay and when you were a child did.",
        "word_count": 278,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["really into", "cheer for", "big sports event"],
            "grammar_structures_used": ["conditionals", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement"],
            "vocabulary": ["repetitive_like"]
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
            "complexity_level": "moderate_high",
            "accuracy_level": "high",
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
                "why_not_9": "'people who likes' -> 'people who like'. Slip prevents 9.",
                "why_not_7": "Good range of complex structures."
            },
            "vocabulary": {
                "why_not_9": "Heavy use of 'like' as filler. 'Big sports event' is a bit generic.",
                "why_not_7": "Idiomatic ('really into')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free. Occasional inappropriacies occur.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural and idiomatic ('really into'). Band 8.",
        "grammar_reason": "Mostly error free, one slip ('people who likes'). Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "MUj-UaHrHS8_q05",
        "video_id": "MUj-UaHrHS8",
        "part": 3,
        "question": "Travel journals and social media?",
        "transcript": "Good memories but also they would post on social media since it is a big platform right now I think social media is not only just about showing off but it is also about telling people new informations and sharing good things nice and can can you trust other people's travel journals on the internet and it depends on the person or the personality I think some these days a lot of people get sponsored by certain like platform or they get a lot of sponsorship so if it is sponsored by someone or something that might make the post not so easy to believe but if it is like really personal opinions about it then yes I would trust but yeah you would have to seek for those who have really good informations yeah yes and how do you think people get information about new travel destinations these days oh actually I was surprised about how people search for the information I would usually go for Google or like Google Map for the informations but for example my friend and a lot of my friends around they use Instagram to search up the information for traveling so they would use hashtag to search up for example when they are going to it is a small country in I do not know Germany they would search up like a small town in Germany so it is so different these days and there is a lot of information so do you think is there any difference in the way younger people travel and the way older people travel totally totally I actually right now I am studying about that so older people would use a travel agent to go to certain places since they have a lot of money first of all it depends on people of course.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["uncountable_nouns"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["sponsored by", "showing off", "personal opinions", "travel agent"],
            "grammar_structures_used": ["passive_voice", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["uncountable_plural"],
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
                "why_not_9": "'new informations' -> 'new information'. Repeated error.",
                "why_not_7": "Good complexity."
            },
            "vocabulary": {
                "why_not_9": "Repetition of 'search up', 'informations'.",
                "why_not_7": "Good topic vocabulary ('sponsored', 'hashtag')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary to allow some flexibility and precision."
        },
        "vocab_reason": "Good range but 'informations' is a basic error. Band 7.",
        "grammar_reason": "Frequent error-free sentences but repeated error with 'informations'. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },

    # Video: LVlJZIkTMDE (Band 8.5)
    {
        "id": 0, "sample_id": "LVlJZIkTMDE_q04", "video_id": "LVlJZIkTMDE", "part": 2,
        "question": "Time travel?",
        "transcript": "Spot with that one you know I would say that I would like to go back to the time when Moses delivered the Israelites from the land of Egypt that would be a really great time to be in because I would like to be an eyewitness to all the 10 plagues and all the other Miracles Moses and Aron performed such as The Parting of the Red Sea that would be really cool.",
        "word_count": 68,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["delivered", "eyewitness", "plagues", "parting of the red sea"],
            "grammar_structures_used": ["complex_sentences", "infinitives"]
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Flawless.",
                "why_not_7": "Complex."
            },
            "vocabulary": {
                "why_not_9": "'Eyewitness', 'delivered'. Very precise.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise ('eyewitness', 'delivered'). Band 9.",
        "grammar_reason": "Flawless structure. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "LVlJZIkTMDE_q09", "video_id": "LVlJZIkTMDE", "part": 3,
        "question": "Lateness?",
        "transcript": "Consider first of all arriving late do you think it is okay to arrive late when meeting a friend well I I really do not like that to be honest because I do not I do not like standing up people and ruffling their feathers like personally I am a very punctual person if I do say so myself and I think that is the way to do you know this answer starts strong he gives his opinion straight away I really do not like that to be honest but standing people up means not arriving at all rather than arriving late and ruffling their feathers is an idiomatic phrase that feels a little unnatural here a more precise response might have mean something like I do not like keeping people waiting because I know it aggravates them and makes them feel like I do not value their time let us keep watching so how do you react if you have arranged to meet a friend and they are very late for your appointment I am enraged to be honest and you know I just tell them directly and the next time time if they do it again I might cancel my meeting and just just let them have the taste of their own medicine you know what do you think should happen to people who arrive late for work as harsh as it may sound I think they should be severely punished because punctuality comes first if you want to get things done if you are not not really on time it is very unlikely for you to get things done and be productive at your work so they must be punished so that they do not repeat that again this response had a fantastic opening statement as harsh as it may sound.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["ruffling their feathers", "punctual person", "standing up people", "taste of their own medicine", "severely punished"],
            "grammar_structures_used": ["idioms", "conditionals", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["idiom_appropriateness"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Ruffling feathers' and 'standing up people' are used slightly inaccurately or awkwardly here (as noted in the transcript itself). This prevents a pure 9."
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
                "why_not_9": "Control is high.",
                "why_not_7": "Superior complexity."
            },
            "vocabulary": {
                "why_not_9": "Idioms used ('ruffling feathers', 'taste of own medicine') but maybe slightly forced or slightly off-context.",
                "why_not_7": "Strong range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items despite occasional inaccuracies."
        },
        "vocab_reason": "Strong idioms but slightly forced/inaccurate ('standing up people' vs 'keeping waiting'). Band 8.",
        "grammar_reason": "Excellent control. Band 9.",
        "vocabulary": 8,
        "grammar": 9
    },

    # Video: Hjl3Cu6PceY (Band 7.0)
    {
        "id": 0, "sample_id": "Hjl3Cu6PceY_q02", "video_id": "Hjl3Cu6PceY",
        "part": 1,
        "question": "What do you study?",
        "transcript": "Just play games on my phone have a podcast playing in the background and that is about it okay we are going to talk a little bit now about studying for a student right now what do you study I study English literature I am a master's student right now and I heard that it is a little weird to talk about what you are focusing on as a master's student but to be a little bit more precise than literature I study Irish drama and do you enjoy it I have a love and hate relationship with it I mean I definitely enjoy it enough to choose the path of pursuing my studies but I hate it at times because it makes me feel very stupid fair enough fair enough do you do you look forward to finishing and beginning work in the near future yeah I am planning on it because this is my fourth semester as a master's student and usually a master's program would end about in a in a two-year three-year type of situation I am plan I have not gotten started on my thesis yet so that is a bit of a problem but other than that I am planning to graduate next summer okay so after that maybe I could start working good good and one final question do you prefer to study in the morning or the afternoon or the evening I am a night owl so I definitely prefer to study at night or in around 3 A.M 4 a.m that is when I function the best I am definitely not a morning person I usually sleep till around noon or 1pm",
        "word_count": 257,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["master's student", "love and hate relationship", "pursuing my studies", "night owl", "function the best"],
            "grammar_structures_used": ["compound_sentences", "complex_sentences"]
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
            "complexity_level": "moderate_high",
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
                "why_not_9": "Good but not fully sophisticated. 'I am plan' -> 'I am planning' (slip).",
                "why_not_7": "Generally error free."
            },
            "vocabulary": {
                "why_not_9": "'love and hate relationship', 'night owl'. Good but standard idioms.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural use of idioms ('night owl', 'love and hate relationship'). Band 8.",
        "grammar_reason": "Mostly error free, one slip ('I am plan'). Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "Hjl3Cu6PceY_q05", "video_id": "Hjl3Cu6PceY",
        "part": 3,
        "question": "Being popular?",
        "transcript": "or doing well or being good at your job huh I personally want to be the person who is good at their job but to be popular I think maintaining a good relationship with your colleagues is a little bit better and therefore it seems like that is the better person that is the a better employee to have at workplace sometimes yeah and one more question what benefits are there when a child is popular at school benefits I I think they would get a lot of Valentines or gifts they would have a lot of friends wanting to come to their birthday parties yeah yeah and how would that impact the child's life in school I think being very popular from a very young age would impact a child to not have as many problems in their social life probably because normally because they would always have people who want to be with them who would want to be with them and but at the same time I feel like that would always also help not help them impact them in ways where they will not be able to fulfill certain things as well when they have like you know challenges faced in front of them because they would not have had to try so hard in the past yeah all right well really nicely done and with that.",
        "word_count": 222,
        "analysis_metadata": {
            "grammar_error_patterns": ["complex_structure_breakdown"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["maintaining a good relationship", "social life", "fulfill certain things"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": ["coherence_break"],
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
                "why_not_9": "Structure breaks down at the end: 'help not help them impact them...'",
                "why_not_7": "Generally controlled but some errors."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Functional."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar and punctuation but they rarely reduce communication.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Functional range ('maintaining relationship'). Band 7.",
        "grammar_reason": "Breakdown in complex structure at end puts it at Band 6/7 border. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },

    # Video: IevmdO16GuE (Band 9.0)
    {
        "id": 0, "sample_id": "IevmdO16GuE_q01", "video_id": "IevmdO16GuE", "part": 1,
        "question": "Holiday in mountains?",
        "transcript": "Let us start off by talking about the mountains do you like to go on holiday in the mountains definitely it is one of my favorite things to do I actually love nature and the mountains specifically like I always handpick locations which have mountains and like a beautiful landscape Greenery and I love hiking as well so that is why are there any hotels in the mountains in your country Yes actually in Himel they have lodges they rent it out to people who are there on vacations and it is the most beautiful experience because you get to actually see how people who are based there how they live and how they cook and how they clean and you get the whole experience of everything.",
        "word_count": 122,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["handpick locations", "beautiful landscape", "rent it out", "based there"],
            "grammar_structures_used": ["relative_clauses", "complex_sentences"]
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
            "complexity_level": "moderate_high",
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
                "why_not_9": "Good flow, error free.",
                "why_not_7": "Superior flow."
            },
            "vocabulary": {
                "why_not_9": "'Handpick' is a nice touch. 'Rent it out'. Natural.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural and precise ('handpick'). Band 8.",
        "grammar_reason": "Error free and natural. Band 9.",
        "vocabulary": 8,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "IevmdO16GuE_q04", "video_id": "IevmdO16GuE", "part": 1,
        "question": "TV and News?",
        "transcript": "Have to do is just click the link in the description thanks very much and let us get back to the video I do not think so no I think there is enough for everyone so I think there is a lot of different genres that people can watch and game shows are mostly educational so I think that is also very necessary in today's generation and to remind everyone to have fun and not take life so seriously is TV the main way people get news in your country yes for sure I would agree I mean it is one of the most important Outlets from where people can know what is going on like the breaking news or what happened yesterday everyone's always aware.",
        "word_count": 119,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["genres", "breaking news", "outlets", "take life so seriously"],
            "grammar_structures_used": ["complex_sentences", "relative_clauses"]
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
            "complexity_level": "moderate_high",
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
                "why_not_9": "Good control.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'Outlets', 'genres'. Precise.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Precise ('genres', 'outlets'). Band 8.",
        "grammar_reason": "Error free and natural. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "IevmdO16GuE_q05", "video_id": "IevmdO16GuE", "part": 3,
        "question": "TV Regulations?",
        "transcript": "You have any questions about the VIP course always feel free to get in touch with us we answer 100% of the questions that we get hope that you become a VIP if not enjoy the rest of this free video not as much as they used to because back then it was a form of entertainment but now they just want to skip and Reach the the show that they are watching it is not as much as it used to be I think people grew impatient now they are not as patient as they used to be because of the fast-paced life everyone's going through so they want everything quick how important are regulations on TV advertising I think they are very important and there should be regulations but at the same time I think that it is not followed as much as it it should be.",
        "word_count": 149,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["form of entertainment", "fast-paced life", "regulations"],
            "grammar_structures_used": ["comparatives", "passive_voice"]
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
                "why_not_9": "'fast-paced life' is good.",
                "why_not_7": "Functional."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural collocations ('fast-paced life'). Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },

    # Video: qkkiBblCE9k (Band 7.5)
    {
        "id": 0, "sample_id": "qkkiBblCE9k_q03", "video_id": "qkkiBblCE9k",
        "part": 1,
        "question": "Travel destination?",
        "transcript": "Would you like to travel to in the future actually there are two countries that I would love to visit at some point one is Italy and the other one is Japan Japan especially for their Pine because I love Asian food here in my in my city I like trying that kind of food so I would like to try the original one great thank you very much great now we are done with the first part of the exam so.",
        "word_count": 82,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["Asian food", "visit at some point"],
            "grammar_structures_used": ["simple_sentences"]
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
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Too simple.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Functional."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Functional range. Band 7.",
        "grammar_reason": "Error free but simple. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "qkkiBblCE9k_q04", "video_id": "qkkiBblCE9k",
        "part": 2,
        "question": "Ambition?",
        "transcript": "In a dancing contest in February which is kind of curious I did not dance before like I started dancing like four years ago before that I thought that I was not able to dance I was actually in party sitting down and just watching people and when people invited me I was saying that no I am not able to I I do not like it but this actually took me out of my comfort zone it was pretty funny the way it worked out and I think that just participating in this contest will move me to another level in my life I am going to create like evidence that I can do things that I am that I have always thought that I was not useful or good at so I have been particip well I have been practicing for this contest for the last three months so it is kind of difficult because not of practice actually but it is more than being in front of a lot of people getting all these comments and I do not know like not knowing what they are thinking about me dancing it is kind of like curious because I am used to being from people because that is what I have been doing for 10 years in my life that is my job but this is different because this is not what I am or what I am comfortable with so this ambition is important for what I said it is going to to I",
        "word_count": 257,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice", "preposition_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["comfort zone", "participating", "move me to another level"],
            "grammar_structures_used": ["complex_sentences", "past_perfect"]
        },
        "micro_flaws": {
            "grammar": ["awkward_phrasing"],
            "vocabulary": ["repetitive_like"]
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
                "why_not_9": "'not of practice actually' (awkward). 'being from people' (unclear).",
                "why_not_7": "Good complexity."
            },
            "vocabulary": {
                "why_not_9": "Repetition.",
                "why_not_7": "'Comfort zone' is good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('comfort zone'). Band 7.",
        "grammar_reason": "Mostly error free but some awkward phrasing. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },

    # Video: 9AdJTIAtnBY (Band 8.0)
    {
        "id": 0, "sample_id": "9AdJTIAtnBY_q02", "video_id": "9AdJTIAtnBY",
        "part": 1,
        "question": "Laughter / Planning?",
        "transcript": "Fan of a show called the couple Sharma show which premiered on a national Channel I do love to watch it with my family okay do you usually make your friends laugh I try to make my friend laugh by telling them jokes however sometime I failed miserably but I do try to make them laugh good are you kind of person who makes people laugh as I mentioned earlier I am that kind of person who likes to tell a joke once or twice in a chatting but sometimes I failed and sometime I achieve my task of making someone laugh do you think it is important to laugh with friends definitely it is very important because there are some expert opinion as well that laughing makes a person more healthy and vigorous so I think it is very necessary for human body body to laugh great now few questions will be based on planning do you make plans every day I do try to make plans every day as I am a working girl so I definitely try to stick to my plans so I can be organized and productive okay are you good at managing your time I am not expert or master or veteran at managing time but I do try to remain sticky to my plans always okay what is the latest plan you made just recently I made a plan to visit my grandmother who who is very ill so I decided to meet her at my maternal home M what is the hardest part about making plans I think it is the div dividation of some task and time managing the time as per the task I think it is very hard because sometime the task is very big or unimportant and I.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_usage", "word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "mixed",
            "vocab_evidence": ["failed miserably", "premiered", "vigorous", "stick to my plans", "sticky to my plans"],
            "grammar_structures_used": ["complex_sentences", "passive_voice"]
        },
        "micro_flaws": {
            "grammar": ["article_missing"],
            "vocabulary": ["collocation_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Sticky to my plans' is unnatural (should be 'stick to'). 'expert opinion' (plural missing). 'dividation' (incorrect word form -> division)."
        },
        "grammar_profile": {
            "complexity_level": "moderate_high",
            "accuracy_level": "controlled",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Several errors: 'expert opinion' (plural), 'dividation'.",
                "why_not_7": "Structures are generally good."
            },
            "vocabulary": {
                "why_not_9": "'Sticky to my plans', 'dividation'. Errors in word formation.",
                "why_not_7": "'Failed miserably', 'premiered', 'vigorous'. Strong highs."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary to allow some flexibility and precision."
        },
        "vocab_reason": "Strong vocabulary ('vigorous', 'premiered') mixed with errors ('sticky', 'dividation'). Band 7.",
        "grammar_reason": "Frequent error-free sentences but evident errors. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "9AdJTIAtnBY_q04", "video_id": "9AdJTIAtnBY",
        "part": 2,
        "question": "Websites?",
        "transcript": "Got plora of information regarding it we clicked on a website called www.wikipedia.com it there was enormous information available for the specific task I was very glad I read thoroughly the whole information and prepared a gist of it it took us around 2 weeks to complete that task however we were able to complete it within our deadline on the day of our presentation when we present present the project in front of class my peers really were happy and appreciated us even our teacher applaud us for our for our information that we give in the task on the day of result declaration we were quite elated that we got passed with a marks on that project so that was the task I did with the help of a website good thank you so much this is end of the Q card and very wonderful now I am going to ask some followup questions which will be based on the Q card right what are the most popular and least popular apps in your country I think the most eminent one in my country are some social media application like Instagram WhatsApp Facebook whereas the least popular are the one which are designed for one specific viewers for example Hulu is a website or a application which is designed specifically for producers or directors okay so why some apps are most popular and some apps are least popular I think it really depend upon the Curiosity of the journal audience if there is a trend of one particular app then the whole audience will install that app for example Tik Tok was a viral sensation in 2019 okay what is the difference between internet and the TV according to.",
        "word_count": 285,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_usage", "agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["plethora of information", "viral sensation", "eminent", "elated", "gist of it"],
            "grammar_structures_used": ["passive_voice", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_missing"],
            "vocabulary": ["pronunciation_spelling_mismatch"]
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
            "accuracy_level": "controlled",
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
                "why_not_9": "'depend upon' (agreement error - depends). 'Got plora' (plethora).",
                "why_not_7": "Complex structures used well."
            },
            "vocabulary": {
                "why_not_9": "'plora' (plethora), 'enormous information' (collocation - usually vast amount of information).",
                "why_not_7": "'Elated', 'eminent', 'viral sensation'. Very strong 8 range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level vocabulary ('elated', 'eminent', 'plethora'). Band 8.",
        "grammar_reason": "Good structure but some slips ('depend upon'). Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "9AdJTIAtnBY_q05", "video_id": "9AdJTIAtnBY",
        "part": 3,
        "question": "Internet vs TV?",
        "transcript": "Me the main difference between these two aspects or things are that people can choose the subject they want to watch on the internet whereas one can have to watch what is being telecasted on the television mhm why some people like to read news on the internet instead of getting it from TV there are multiple reasons for this for example first of all is one can watch news or letters at any time at any remote location secondly they can search for the news they are particularly interested in for example I am very interested in movies and glamorous words so I search for that news only okay are libraries still beneficial if yes why if not why not indeed they are very beneficial because it is a hub of books one can read en numerous books under one place and it is also a place where one can achieve Qui atmosphere for reading or doing their work okay what kind of people still like to go to the library to study I think those people who find it very hard to look at computer screen and find it very straining to look at these screens go to library moreover one who need to focus on their work go go to libraries can internet help children in their study definitely internet is an ocean of knowledge it provide enous information to the child for their academics so yes children can do work from internet thank you so much as thank you so much this end of the test so guys this is time to give the feedback I have no feedback for this interview I have no words for this interview this was really a wonderful and amazing interview",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["ocean of knowledge", "hub of books", "remote location", "straining"],
            "grammar_structures_used": ["complex_sentences", "connectives"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement"],
            "vocabulary": ["word_choice_imprecise"]
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
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'it provide' -> 'it provides'. 'one who need' -> 'one who needs'.",
                "why_not_7": "Good range."
            },
            "vocabulary": {
                "why_not_9": "'glamorous words' (likely meant 'world'?). 'en numerous' (innumerable?).",
                "why_not_7": "'Ocean of knowledge', 'hub of books'. Good metaphors."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary to allow some flexibility and precision."
        },
        "vocab_reason": "Good metaphors ('ocean', 'hub') but some imprecision ('glamorous words'). Band 7.",
        "grammar_reason": "Frequent error-free sentences, some agreement errors. Band 7.",
        "vocabulary": 7,
        "grammar": 7
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
            if sample['sample_id'] not in existing_ids:
                f.write(json.dumps(sample) + '\n')
                count += 1

    print(f"Append complete. Added {count} new samples. (Skipped {len(scored_samples) - count} duplicates).")

except Exception as e:
    print(f"Error writing to file: {e}")
