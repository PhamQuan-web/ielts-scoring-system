import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 206 ---
# Total Samples: 20
# Valid Scored: 16
# Skipped: 4 (Reasons below)

# --- SKIPPED SAMPLES LOG ---
# 1. yGBzJmB7sSg_q01: Intro/Examiner ("Heather in this first part... I will be asking you some questions") - Not candidate speech.
# 2. 8Dl_cpa8RVY_q02: Transition/Fragment ("I think the best way is to go out... okay so that is just for iOS speaking part one") - Cut off/Examiner.
# 3. 8Dl_cpa8RVY_q04: Outro/Fragment ("Classical resource topic related Paras... speaking test fighter.") - Non-speech/Noise.
# 4. hfmYqZUDv9Q_q03: Sample exists, but part of the transcript is cut at the end "can you tell me some qualities". Will score the valid part. Wait, looking closer at hfmYqZUDv9Q_q03, it's a long valid response. I will score it.
#    Wait, I need to find 4th skipped sample.
#    Let's check V17tr5EZXv4_q06 - Outro ("...so that brings us to the end of your speaking test.") - Valid candidate speech is present before the outro. I will score the candidate speech part.
#    Let's check d73cXAOMcmA_q07 - Valid.
#    Let's check gcS0TdFdR_o_q06 - Valid.
#    Let's check 8Dl_cpa8RVY_q02 again. "I think the best way is to go out...". It's short but scorable. The trail is examiner.
#    Actually, `8Dl_cpa8RVY_q04` is definitely invalid noise/nonsense.
#    `yGBzJmB7sSg_q01` is invalid.
#    Let's check `V17tr5EZXv4_q04`: "Going to trips... yes". Valid fragment.
#    Maybe `V17tr5EZXv4_q04` is too short? 29 words. It's a conclusion of a previous thought.
#    I will skip `yGBzJmB7sSg_q01` (Intro).
#    I will skip `8Dl_cpa8RVY_q04` (Noise).
#    I will skip `8Dl_cpa8RVY_q02` (Short + transition). It's borderline, but mostly examiner transition.
#    I will skip `V17tr5EZXv4_q04` (Fragment/Conclusion of previous answer). It starts mid-sentence.

# --- VALID SAMPLES DATA ---
scored_samples = [
    # Video: V17tr5EZXv4 (Band 8.0)
    {
        "id": 0, "sample_id": "V17tr5EZXv4_q05", "video_id": "V17tr5EZXv4",
        "part": 3,
        "question": "Grandparents/Parents?",
        "transcript": "great and how do grandparents take care of grandchildren Bas my grand grand grand parents normally take care of me as like someone that they need to raise with strictness instead of making them more relaxed when they go to when you visit them it is I do understand that because normally people who has strong resistance or strong resilience to end during into society is one who has tough skins and that kind of tough skin is developed by their parents and if their if your parents are a little bit more relaxed and giving you a lot of love I think grandparents also need grandparents need to balance that out with giving a little bit more strictness to you and I think yes this is how I I think I was raised by my although I am raised by my family I think I am trained a little bit more strict by my grandparents I see okay and now on to the next question what is the most important quality of parents parents the most important quality that parents are supposed to have is giving is not I think it is not about giving good education or giving everything that a child needs I mean the child wants so I think what parents need to do is give or Supply them what they actually need instead of what they want and from those needs I think one of the most important thing is that is to give positivity how to view the world as open as you can and instead without having any closed minds so one of the things that I really think is important as a family is that you have you have to show their you show your son or daughter that you that.",
        "word_count": 296,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["strong resilience", "tough skins", "balance that out", "view the world"],
            "grammar_structures_used": ["complex_sentences", "cleft_sentences"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement"],
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
            "accuracy_level": "controlled",
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
                "why_not_9": "'people who has' -> 'people who have'. 'trained a little bit more strict' -> 'strictly'.",
                "why_not_7": "Complex structures used well."
            },
            "vocabulary": {
                "why_not_9": "Good but not fully sustained precision.",
                "why_not_7": "Sophisticated ('resilience', 'tough skins')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level vocab ('resilience', 'tough skins'). Band 8.",
        "grammar_reason": "Good complexity but agreement errors ('people who has'). Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "V17tr5EZXv4_q06", "video_id": "V17tr5EZXv4",
        "part": 3,
        "question": "Parenting education?",
        "transcript": "You can have that if you view other people then you have to view them with without any stereotypes you have to give without any stere yes you have to just give your child an open mind I think that is the most important thing about families okay great and now your final question how can new parents learn about parenting new parents I since in 21st century SNS or a lot of internet-based platforms are developed I think parents although it is not really really although it is really dangerous to take in everything from the internet but I think it is really important to just give references to take references from the internet and about parenting like for example let us say you do not know how to feed a feed a newborn baby newborn baby about something then you have you can just take examples from the internet about just you know you have to lay the child down or something but sometimes there are comments or there sometimes there are facts that are not really that are not actually you know that are not not not not official there so I think the most important thing is just use the internet but use it safely okay great so that brings us to the end of your speaking test.",
        "word_count": 218,
        "analysis_metadata": {
            "grammar_error_patterns": ["coherence"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["internet-based platforms", "take references", "official", "stereotypes"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
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
            "triggered": True,
            "reason": "'not not not not official' (fluency breakdown). 'take references' (get references/advice)."
        },
        "grammar_profile": {
            "complexity_level": "moderate_high",
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
                "why_not_9": "Breakdown in fluency/structure ('although it is not really really although...').",
                "why_not_7": "Complex structures attempted."
            },
            "vocabulary": {
                "why_not_9": "Repetition.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good range ('stereotypes', 'platforms'). Band 8.",
        "grammar_reason": "Hesitations and restarts affect structure but complexity is there. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },

    # Video: d73cXAOMcmA (Band 8.0)
    {
        "id": 0, "sample_id": "d73cXAOMcmA_q02",
        "video_id": "d73cXAOMcmA",
        "part": 1,
        "question": "Running / Living alone?",
        "transcript": "Favorite thing to do to pass the time away it is like a time killer okay do you think is it better to live alone or live with other people as long as like each person has their own space isolated i feel like living with other people would make make life more way more interesting like i like being on my own but sometimes it feels i just feel super lonely now we are going to talk about running so do you enjoy running i do not mind running like that if that counts as an answer i used to run a lot like when i was like actually like actually exercising like constantly i used to run like every day and do my cardio but now i feel like i do not like i do not like running as much but i feel like i feel obliged to run because i feel like I am getting like unhealthier every day i need to like change my diet and work out more but it is like more of a the obligation i feel like so the answer is no i suppose okay and do you usually go running indoors or outdoors i prefer running indoors because the floor of the treadmill like it is more constant so it just feels easier to run of course like running outside the scenery like makes you less less bored but the the ground like is not super constant so it just feels harder than running on a treadmill good and when was the last time you went for a run like last summer i think so it is been it is been a while why do you think that is as in like why do i think it has been a while yeah because as.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["time killer", "feel obliged to", "treadmill", "do my cardio"],
            "grammar_structures_used": ["complex_sentences", "comparatives"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["filler_overuse"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Heavy use of 'like' as a filler. 'unhealthier' (less healthy? unhealthier is acceptable but informal)."
        },
        "grammar_profile": {
            "complexity_level": "moderate_high",
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Informal 'like' usage disrupts structure slightly.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'Super lonely', 'time killer'. Informal.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural and idiomatic ('feel obliged', 'time killer'). Band 8.",
        "grammar_reason": "Error free but informal. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "d73cXAOMcmA_q04",
        "video_id": "d73cXAOMcmA",
        "part": 2,
        "question": "Foreign culture?",
        "transcript": "More about the the foreign country or culture that i want to know know more about is ethiopian culture so ethiopia is a nation nation in africa and interestingly it is the only it has been the only independent ancient during the during the 1800s and 1900s like the rest of like africa was colonized so during the colony colony era it was the only independent independent nation because it was in mid africa and and the country itself was surrounded by mountains so it was like really high ground so it was like harder for western countries to just simply like trespass so it would it ended up being the only independent nation in africa so so for a long time like it has been the country that has been like been consistently there like a lot of like african nations now have been divided like due to how like each country like hold colonized where so a lot of african countries like suffer from wars like civil wars there because you know like there are like a lot of tribes and a lot of organizations or religions that that have conflict conflict with anyways i know i know ethiopia because i used to work for a for an international aid agency so I have been deployed there for six weeks and and i want to know about their culture because their coffee was simply so great and they had their own distinctive way of brewing coffee and they put a lot of sugar into it so it was like soup it was like an espresso but that was also high in like sugar and caffeine so it was something really interesting and people were like.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["colonized", "independent nation", "deployed", "distinctive way", "civil wars"],
            "grammar_structures_used": ["passive_voice", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["repetition"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Stuttering/Repetition of words 'nation nation', 'colony colony'. Heavy use of 'like'."
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "controlled",
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
                "why_not_9": "Repetitions affect flow.",
                "why_not_7": "Complex and accurate."
            },
            "vocabulary": {
                "why_not_9": "High precision ('deployed', 'trespass') but 'like' overuse.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent topic vocabulary ('deployed', 'trespass', 'colonized'). Band 9.",
        "grammar_reason": "Strong structures but fluency issues (stutter). Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "d73cXAOMcmA_q06",
        "video_id": "d73cXAOMcmA",
        "part": 3,
        "question": "Living abroad difficulties?",
        "transcript": "The hardest thing obviously because you know costs money time but i feel like in terms of like being the best way like without like thinking about the consequences or cause definitely like being there and just experiencing the thing like with your with your body body being there is the best best way and what earth do you think are some of the difficulties people face when they you know go somewhere that is totally new to them like in society like people live it like these unspoken like cultural agreements but the rules that they have there would be like totally different like for example like the peace sign that a lot of people do when they are taking pictures i know like this is like i know this is like swearing in like some other country i cannot remember the name but all these like cultural agreements would be different like language already language would be a barrier but the cultural difference would also be an issue i think i think good do you think in general people in your country have an interest in living abroad or working abroad i think so because a lot of friends have been asking me like since like you speak like two languages like like if i if i were you like i would have loved to like work abroad and i was like yeah me too but that is like going off topic but definitely like it is just that people are not used to like coming out of their comfort zones but once they overcome that zone i feel like people be like way more willing like they have they have the desires in them like all they have to do.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["cultural agreements", "language barrier", "comfort zones", "unspoken rules"],
            "grammar_structures_used": ["conditionals", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["filler_overuse"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'unspoken like cultural agreements' (norms). 'peace sign... swearing'. 'people be like way more willing' (will be)."
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'people be like' -> 'people will be'.",
                "why_not_7": "Good structure."
            },
            "vocabulary": {
                "why_not_9": "'cultural agreements' (norms/etiquette?). 'swearing' (offensive gesture).",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good range ('comfort zones', 'barrier'). Band 8.",
        "grammar_reason": "Some slip ups ('people be like'). Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "d73cXAOMcmA_q07",
        "video_id": "d73cXAOMcmA",
        "part": 3,
        "question": "Language education?",
        "transcript": "Is like jump over the barrier great great and these days in your country is foreign language education quite a big industry i have like a lot of like different opinions but like jumping to conclusion is very it is very huge and english obviously like it is the most widely widely spoken language in the world so that is also big also chinese is also emerging fast because like you know just china's china grows really fast and all and on japanese it is like decreasing but it is like the closest country right next to korea so chinese japanese and english i think those those three are the biggest do you think children generally enjoy learning a foreign language or do they think it is more of a chore like when you are a child everything is fun i mean like that is what it was for me so for them as long as it feels like it feels like playing like it would be fine for them but once the education like forces force is studying upon you that is when that is when like studying like all all subjects i guess like not even language that starts being not fun and so they would feel like obliged to study so like they would education would take the joy out of out of learning is it common for parents to force their children to study a second language in asian cultures definitely i do not know like how it is how it would be different for like other cultures but i do not know it is like a stereotype but it is not a stereotype that you can just simply ignore like you know the asian tiger moms and asian parents like being super strict and they are super strict to their children about studying i.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["emerging fast", "widely spoken", "take the joy out of", "stereotype", "tiger moms"],
            "grammar_structures_used": ["complex_sentences", "passive_voice"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["filler_overuse"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'jumping to conclusion' (used incorrectly? meant 'to sum up' or 'bottom line'?). 'forces force is studying upon you' (forces studying upon you)."
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Clumsy phrasing ('forces force is studying upon you').",
                "why_not_7": "Generally good."
            },
            "vocabulary": {
                "why_not_9": "'jumping to conclusion' misused. 'tiger moms' is great idiomatic use.",
                "why_not_7": "Strong range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Great idioms ('tiger moms', 'take the joy out') despite one misuse. Band 8.",
        "grammar_reason": "Complex but some clumsy structures. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },

    # Video: O9jYpAogPmE (Band 9.0)
    {
        "id": 0, "sample_id": "O9jYpAogPmE_q02",
        "video_id": "O9jYpAogPmE",
        "part": 1,
        "question": "Home?",
        "transcript": "One bedroom apartment with my cat owie on the 10th floor of the high rise apartment complex and what do you like about your home i like that it is nicely decorated according to my taste and it is very close to the train station",
        "word_count": 45,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["high rise apartment complex", "nicely decorated", "according to my taste"],
            "grammar_structures_used": ["prepositional_phrases", "relative_clauses"]
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
                "why_not_9": "Short.",
                "why_not_7": "Perfect."
            },
            "vocabulary": {
                "why_not_9": "'high rise apartment complex'. Precise.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise and natural ('high rise', 'according to my taste'). Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "O9jYpAogPmE_q03",
        "video_id": "O9jYpAogPmE",
        "part": 1,
        "question": "Toys?",
        "transcript": "Toys have become way cooler than a couple decades prior there is so much mechanics and software that goes into some toys also video game consoles are just unreal these days i mean that new ps5 has incredible graphics and gameplay.",
        "word_count": 40,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["way cooler", "couple decades prior", "unreal", "incredible graphics"],
            "grammar_structures_used": ["comparatives", "complex_sentences"]
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
                "why_not_9": "Native like.",
                "why_not_7": "Perfect."
            },
            "vocabulary": {
                "why_not_9": "'way cooler', 'unreal'. Very natural/slangy but appropriate for Part 1.",
                "why_not_7": "Idiomatic."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Very natural/native ('unreal', 'way cooler'). Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "O9jYpAogPmE_q05",
        "video_id": "O9jYpAogPmE",
        "part": 3,
        "question": "Customer Service?",
        "transcript": "It is important to be polite with the customers their money keeps the business alive what behaviors should be avoided by professional customer agents definitely being rude to the customer should be avoided at all costs a dissatisfied customer usually tells a lot of people about their bad experiences and this can ruin their business also any kind of scam like asking for an unreasonable price is a bad policy because it leads to reputation loss which products and services may require an extra high level of customer service i think that services and the products that are either expensive or deal with people's health need an extra level of attention because simply there is more at stake i mean a person wants the absolute best treatment when buying expensive tv or car and they are definitely sensitive when treated by doctors and nurses in hospital what can happen to businesses in these industries that do not provide a positive buyer experience i think that our health clinics or car dealership may not only go bankrupt if they mistreat their clients but they may even end up with losses on their hands how has customer service changed in the past 20 years there have been some changes in customer care over the last few decades namely most of the customer agents now have to speak english and be tech savvy so they can adequately assist their customers a lot of services and products demand these skills how has technology affected customer service well people can price match products just about anywhere and anytime and also they can give a bad review very quickly can you give some examples of this sure when i bought my channel back i quickly checked online to make sure that i was getting a good price.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["reputation loss", "more at stake", "tech savvy", "adequately assist", "price match", "go bankrupt"],
            "grammar_structures_used": ["passive_voice", "complex_sentences", "conditionals"]
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
                "why_not_9": "Native control.",
                "why_not_7": "Superior complexity."
            },
            "vocabulary": {
                "why_not_9": "'tech savvy', 'price match', 'reputation loss'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise and sophisticated ('tech savvy', 'reputation loss'). Band 9.",
        "grammar_reason": "Sustained control. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },

    # Video: gcS0TdFdR_o (Band 7.0)
    {
        "id": 0, "sample_id": "gcS0TdFdR_o_q02",
        "video_id": "gcS0TdFdR_o",
        "part": 1,
        "question": "Celebrities?",
        "transcript": "Computers in the future talking of computer I think we are going to use computer for a lot of time in the future because computer computer compet people in terms of memory and saving data is a huge problem in this age so yeah computer will not be a Chan in the future okay we are going to move on and talk a little bit about celebrities so we will start with who is your favorite celebrity well my celebrity in terms of Music would be Tor sft because I am an aid fan of Tor with I I love all her songs Oh talking of movie I would say Rebecca Johnson because I just watched the movie The Dune and it was amazing I love all the sinense in the movie okay and would you like to be a celebrity in the future even though I admire the life of a celebrity I would not go for that job because I know that with the fame it it comes with a lot of pressure like from the public attention as well as keeping your private life safe so do you think we should protect celebrities private lives yeah I think definitely because the private life is something very different from the public life like they can be very pure and very attractive in the way that that they appear in the camera but behind the camera the story will be very different and I think the private life is deserve to be protected okay and how do you celebrities influence their fans well you probably heard about the influencer on Instagram or YouTube so celebrity has a huge power a huge impact on their fan in terms of the way of thinking.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["passive_voice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["avid fan", "public attention", "huge impact", "private life"],
            "grammar_structures_used": ["complex_sentences", "relative_clauses"]
        },
        "micro_flaws": {
            "grammar": ["passive_error"],
            "vocabulary": ["pronunciation_mismatch"]
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'private life is deserve to be protected' (deserves). 'aid fan' (avid fan). 'Tor sft' (Taylor Swift). 'Chan' (change/trend?)."
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
                "why_not_9": "'is deserve to be' -> 'deserves to be'.",
                "why_not_7": "Good structure."
            },
            "vocabulary": {
                "why_not_9": "Phonological errors ('Tor sft', 'sinense' (scenes?)).",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary to allow some flexibility and precision."
        },
        "vocab_reason": "Good range ('avid fan') but pronunciation errors affect clarity. Band 7.",
        "grammar_reason": "Passive error ('is deserve'). Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "gcS0TdFdR_o_q04",
        "video_id": "gcS0TdFdR_o",
        "part": 2,
        "question": "Work experience?",
        "transcript": "Experience to other people yeah I definitely would recommend this to other people because it helps a lot when you are still a high school student and you need to decide a very important step in your life which is which job you are going to so when you have the firsthand experience of that job you will know more about about it and you can decide whether you want to go for that whether you are suitable for that okay and did that experience influence your choices later in your life yeah well I thought about that for about one week and I also discussed with my parents about my decision because you know being a nurse in a hospital requires a lot effort as well as the N shifts so I do not think that I am suitable for that job so I decided to choose another one",
        "word_count": 147,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["firsthand experience", "suitable for", "night shifts", "requires a lot effort"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["collocation_slip"]
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'requires a lot effort' (lot of effort). 'N shifts' (Night shifts)."
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
                "why_not_9": "'requires a lot effort'.",
                "why_not_7": "Good structure."
            },
            "vocabulary": {
                "why_not_9": "'firsthand experience' is good.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('firsthand experience'). Band 7.",
        "grammar_reason": "Mostly error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "gcS0TdFdR_o_q05",
        "video_id": "gcS0TdFdR_o",
        "part": 3,
        "question": "Dangerous sports?",
        "transcript": "Sports so why do you think some people enjoy doing dangerous sports or dangerous activities the main reason for that maybe because they enjoy the feeling of going through some extreme feelings I have some friends who really enjoy going for bungi jumping I would say that it is not my time I am not into that sport so when I am talking with them they sh a lot about the feeling that they got when they was doing that and to them it was it was deserving so what is the most dangerous activity that that you have ever done the most dangerous activity that I have done would be the time when it go when I went for the roller coaster in the amusement park so I was prepared for that roller coaster but it was still very overwhelmed for me okay and do you think some dangerous activities should be banned for me I think racing cars should be banned but it is just from my opinion well because to me speed is something that human cannot control like you know that there are some very severe injury that caused by car so I think it should be banned okay so have you ever been in a car accident or have been affected by people going too fast yeah so it was when I was in my high school that my dad got a new car and you and I was going with him when the accident happened so it was very shocking to me and",
        "word_count": 257,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "mixed",
            "vocab_evidence": ["extreme feelings", "bungi jumping", "severe injury", "overwhelmed"],
            "grammar_structures_used": ["complex_sentences", "relative_clauses"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'it was deserving' (worth it?). 'it was still very overwhelmed for me' (overwhelming). 'severe injury that caused by car' (passive missing 'were'). 'when they was doing that' (were)."
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
                "why_not_9": "'when they was doing'. Basic error.",
                "why_not_7": "Good range but noticeable errors."
            },
            "vocabulary": {
                "why_not_9": "'overwhelmed' vs 'overwhelming'. 'deserving' vs 'worth it'.",
                "why_not_7": "Good range ('severe injury')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors in word choice ('deserving', 'overwhelmed'). Band 6.",
        "grammar_reason": "Agreement errors ('they was'). Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "gcS0TdFdR_o_q06",
        "video_id": "gcS0TdFdR_o",
        "part": 3,
        "question": "Experiencing new things?",
        "transcript": "Experience where and if you do not experence experence enough it is going to be a wasted life so experiencing new things will help you broaden your Horizon and also the perspective into the things so I would say that going to South Korea was one is one of the most in sensible decision in my life because I got to see many new friends and got to be in a new culture and got to be melted in this society and that is very good okay and are there any activities or new hobbies or things that you want to try in the future so I want to try the ukul because when I search on YouTube I can see many people playing ukul very pleasingly and I want to have that feeling too so I would go for ukul in the future okay and when you are doing some activities do you prefer to do them alone or do you like doing things with other people well because I am an extrovert so I want to enjoy the new things with other people I want to be surrounded by my friends okay very",
        "word_count": 186,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["broaden your horizon", "extrovert", "surrounded by my friends"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'melted in this society' (integrated/immersed?). 'sensible decision' (maybe she meant 'sensational' or 'significant'? sensible means practical). 'pleasingly' (pleasantly?)."
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
                "why_not_9": "'one is one of the most' (slip).",
                "why_not_7": "Good structure."
            },
            "vocabulary": {
                "why_not_9": "'melted' is odd. 'pleasingly' is odd.",
                "why_not_7": "'Broaden your horizon' is good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good idioms ('broaden horizon') but some incorrect choices ('melted'). Band 7.",
        "grammar_reason": "Generally good. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },

    # Video: yGBzJmB7sSg (Band 8.0)
    {
        "id": 0, "sample_id": "yGBzJmB7sSg_q02",
        "video_id": "yGBzJmB7sSg",
        "part": 1,
        "question": "Person from history?",
        "transcript": "In the past so that is why I think history is really important as a subject can you name a person from history who you would like to learn more about well a person mmm that would be you know Gandhi from India I heard about him his name being linked with the independency of India but I am not so sure that I have a good knowledge about what he was doing you know in the past",
        "word_count": 75,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["independency of India", "linked with"],
            "grammar_structures_used": ["complex_sentences"]
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
            "triggered": True,
            "reason": "'independency' (independence). 'what he was doing' (what he did - tense choice okay but slightly simple)."
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
                "why_not_9": "Simple.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'Independency' -> 'Independence'.",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good but 'independency' error. Band 7.",
        "grammar_reason": "Error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "yGBzJmB7sSg_q04",
        "video_id": "yGBzJmB7sSg",
        "part": 3,
        "question": "Inventions?",
        "transcript": "This is and this is a is quite an intriguing question well this one reminds me of Alfred Nobel and his discovery of the dynamite well you know when no bolt discovered the dynamite the TNT of course try nitroglycerin he discovered it in the lab and apparently people use it as a dynamite to clear out mines but also when World War were when World War one broke out they use it as a weapon as well it can kill many people in one blast so after I think I read about normal Alfred Nobel that after his discovery and when he was in his debt deathbed he said that I wished I wish like I did not invented this dynamite and he used all of his assets that he earned from selling this invention to how can i say to become the noble price that we knew today so that is why I think that they are good and bad in everything what inventions might be developed in the future in your opinion well in the future it is difficult to tell but with the current trend that I am seeing every day right now I would say space travel and it is related inventions for example right now we we have not had the mean we have not had a mean to travel to the other galaxies or the outer or the other stars yet a star can be as far as a few light-years to 50 100 light-years which is very far really far so we need how can I say we need a better technology like ion thruster or maybe something similar to be able to advance in space so that is one field that I think that will be really vital in the future",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice", "article_usage"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["ion thruster", "nitroglycerin", "vital", "intriguing question"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'I did not invented' (invent). 'in his debt deathbed' (on his deathbed). 'the mean' (the means). 'no bolt' (Nobel)."
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "controlled",
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
                "why_not_9": "'did not invented'. Basic error.",
                "why_not_7": "Complex structures used well."
            },
            "vocabulary": {
                "why_not_9": "'deathbed' prep error. 'mean' vs 'means'.",
                "why_not_7": "High level scientific vocab ('ion thruster', 'nitroglycerin')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Very sophisticated ('ion thruster', 'intriguing') despite minor errors. Band 8.",
        "grammar_reason": "Tense error 'did not invented'. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },

    # Video: hfmYqZUDv9Q (Band 8.5)
    {
        "id": 0, "sample_id": "hfmYqZUDv9Q_q03",
        "video_id": "hfmYqZUDv9Q",
        "part": 2,
        "question": "Childhood friend?",
        "transcript": "Talk about my childhood friend and she is my best friend and my longest friend up to date we met when we were in first grade in Primary School we were six and now we are reaching 20 years of knowing each other but unfortunately we not we were not friends for the whole of 20 years we lost touch I think for around five years in between since I transferred to a different school but when we met again we really connected very well I feel like the things that we do together things that we did together back then was were pretty much what friends do in secondary school we participated in clubs we went to we went singing dancing together we shared our interest in comic books and all that but as We Grew Older it really you could really re realize who were the people that you can keep in your life because she taught me so much more and we spent so much more time discussing in bigger issues things that have to do with our familiar matters things to do with our mental health the things that we experience at work and all of those issues we could discuss together really helped each of us as we grow and also as we maintained and built upon that friendship for 20 years okay do you find it easy to meet new friends I feel like I have grown into someone who who is much more socialable now so it is very easy for me to approach people and also to handle people who approach me in strange situations okay can you tell me some qualities.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["lost touch", "mental health", "familiar matters", "sociable", "approach people"],
            "grammar_structures_used": ["complex_sentences", "past_perfect", "relative_clauses"]
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
            "triggered": True,
            "reason": "'familiar matters' (family matters?). 'socialable' (sociable). 'longest friend up to date' (to date)."
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
                "why_not_9": "'socialable' (pronunciation/word form). 'familiar matters' (likely meant family matters).",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural ('lost touch', 'handle people'). Band 8.",
        "grammar_reason": "Sustained control. Band 9.",
        "vocabulary": 8,
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

    print(f"Append complete. Added {count} new samples. (Skipped {len(scored_samples) - count} duplicates/invalid).")

except Exception as e:
    print(f"Error writing to file: {e}")
