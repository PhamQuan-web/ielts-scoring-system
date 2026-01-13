import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 220 ---
# Total Samples: 20
# Samples Analyzed:

# 1. pBrFbXB7EAg_q16 (Band 7.5)
# Transcript: "asked my grandmother to help me... went also in the lot of shops... gave me her ring that she have from my grandfather... she is a ring she have a history family history... give some gifts only to people that I like very much... sunflower or some perum..."
# Analysis:
# - Grammar: "went also in the lot of shops" (to a lot of). "she have" (had/has). "she is a ring" (it is a ring). "perum" (perfume?).
# - Verdict: Band 7.0/7.5. Fluency good, some slips.

# 2. pBrFbXB7EAg_q17 (Band 7.5)
# Transcript: "children give to adults... some picture they make... pocket money... spend their money for some gifts... adults appreciate gifts... look like they invest their time... more complicate than to buy..."
# Analysis: "spend their money for" (on). "it is look like" (it looks like). "more complicate" (complicated).
# - Verdict: Band 7.0.

# 3. pBrFbXB7EAg_q18 (Band 7.5)
# Transcript: "glasses with bread of a company... good advertise... gift giving for the economy... buying the gifts in France particularly it is a very big business... help the poor people... make some relationships between us... third worlds..."
# Analysis: "bread of a company" (brand?). "good advertise" (advertisement). "third worlds" (third world countries / developing countries).
# - Verdict: Band 7.0.

# 4. SlAixSd2IfI_q03 (Band 9.0)
# Transcript: "One minute to look at the questions on the card."
# Analysis: EXAMINER INSTRUCTION.
# - Verdict: INVALID (Skip).

# 5. eaq7kXxtGns_q02 (Band 7.5)
# Transcript: "gain knowledge... watching videos on YouTube... interactive software... pick a good big surfing... good riding the wave... knowledge from government school... two decade prior... higher technology... lexical information..."
# Analysis:
# - Grammar: "I pick a good big surfing" (I'd pick surfing?). "good riding the wave" (good at riding). "two decade prior" (decades).
# - Vocabulary: "interactive software", "lexical information", "critical thinking".
# - Verdict: Band 7.5. Good academic vocab, some grammar slips.

# 6. wbysCUmZQZA_q02 (Band 8.5)
# Transcript: "cereal with milk... fruits on xtube... not very good at it... put too much force on it... favorite type of food is definitely a good beef... Vietnamese traditional... expensive caviar... taste amazing..."
# Analysis:
# - Grammar: "put too much force on it" (effort?). "fruits on xtube" (Youtube?). "good beef" (beef noodle soup?).
# - Verdict: Band 8.5. Very natural flow.

# 7. wbysCUmZQZA_q03 (Band 8.5)
# Transcript: "hang out with... Jim Carrey... funniest people on earth... quiet pub... let loose and be ourselves... off camera... journey to become famous... plans to do... funny jokes..."
# Analysis:
# - Vocabulary: "let loose", "off camera", "virtually impossible".
# - Verdict: Band 8.5.

# 8. QcpknFmrQzo_q02 (Band 6.5)
# Transcript: "get my haircut want them on... due to coronavirus... reasonable price... tidy hair... hang out... maintaining this style... dispatched from military service... wax and hair product... forced to cut our hair... appeared from outside... refreshed... dreamer... trimmer... represents my identity..."
# Analysis:
# - Grammar: "want them on" (once a month?). "dispatched from military" (discharged). "hair always were short" (was). "put in style my hair" (style my hair).
# - Vocabulary: "reasonable price", "military service", "identity".
# - Verdict: Band 6.5. "dispatched" is a vocab error. "dreamer" vs "trimmer".

# 9. QcpknFmrQzo_q03 (Band 6.5)
# Transcript: "Then you have one minute to think about the topic..."
# Analysis: EXAMINER INSTRUCTION.
# - Verdict: INVALID (Skip).

# 10. QcpknFmrQzo_q04 (Band 6.5)
# Transcript: "sleepy during the exam... rehashed to myself... stayed up all the night... worth it... let us stay like very good..."
# Analysis: "rehashed to myself" (asked myself? repeated?). "stayed up all the night" (all night).
# - Verdict: Band 6.5.

# 11. QcpknFmrQzo_q05 (Band 6.5)
# Transcript: "people are have they have stressed... tiredness into their body... difficult for them to and to wake up... night shift workers... life balances kind of break down... confuse if they want to work... problem has been at rest... prestigious University... leave them away..."
# Analysis:
# - Grammar: "people are have they have stressed" (people are stressed). "at rest" (addressed?). "leave them away" (leave them alone?).
# - Vocabulary: "night shift", "prestigious university".
# - Verdict: Band 6.5.

# 12. QcpknFmrQzo_q07 (Band 6.5)
# Transcript: "speaking presenters tense... grammatical flaw... linking words... fillers... boosters... self-corrections... flow of speech..."
# Analysis: EXAMINER FEEDBACK/TUTORIAL.
# - Verdict: INVALID (Skip).

# 13. FrTPoIMqNFQ_q03 (Band 5.5)
# Transcript: "territory has a really convenient things... provided two parts and restrooms... gives to my girlfriends to great impacts... tiger for on studying... positive impacts... same Asia with me... rent their rooms..."
# Analysis:
# - Grammar: "territory" (dormitory). "convenient things" (conveniences). "tiger for on studying" (desk for studying?). "same Asia" (same age).
# - Verdict: Band 5.5. ASR errors or heavy accent impacting clarity.

# 14. FrTPoIMqNFQ_q04 (Band 5.5)
# Transcript: "living with roommates give some great advantages... share our ideas each other... talk less speechless... Wi-Fi connection... contact with the company... parents responsibility to teach..."
# Analysis: "talk less speechless" (talk less / are speechless?). "make some Wi-Fi" (set up).
# - Verdict: Band 5.5.

# 15. FzmocI_ikjU_q01 (Band 5.0)
# Transcript: "computer difficulty attested kasam... birthday boy name... sumit yaar anju call me punit... educational qualification most my password my graduation adham english skills... chronic illness... 19.51 family... dena distik fatehabad..."
# Analysis: Highly incoherent transcript. Likely heavy accent or background noise. "password my graduation" (passed my graduation). "chronic illness" (?).
# - Verdict: Band 4.5/5.0. Hard to score higher due to incoherence.

# 16. FzmocI_ikjU_q03 (Band 5.0)
# Transcript: "system very good girl... master of me... shopping and changing... love my family... female condom you got troubled system... Vaikunth Family... Jain A Co... Bigg Boss..."
# Analysis: Incoherent. "female condom"? "Vaikunth"?
# - Verdict: Band 4.5. Incoherent.

# 17. l6M6oX6jI8w_q03 (Band 5.0)
# Transcript: "sellers set price... shoes items selling... online shopping will replace shopping... I prefer in-store shopping... check my size if big size... many material..."
# Analysis:
# - Grammar: "if big size" (if it's a big size). "many material" (materials).
# - Verdict: Band 5.0.

# 18. 0ZizySMJwp4_q01 (Band 5.0)
# Transcript: "Okay, let us go. Ok so."
# Analysis: Short.
# - Verdict: Valid (Band 5).

# 19. 0ZizySMJwp4_q02 (Band 5.0)
# Transcript: "doing a bit of right now... university degrees in logistics and supply chain management... support my family financially... do a part job."
# Analysis: "doing a bit of right now" (a bit of work?). "part job" (part-time job).
# - Vocabulary: "logistics and supply chain management".
# - Verdict: Band 5.5 (Vocab bump).

# 20. 0ZizySMJwp4_q03 (Band 5.0)
# Transcript: "have at the convenience store... My dirty is surviving customer... filling up the new products... store clean and tidy."
# Analysis: "My dirty" (duty). "surviving customer" (serving customers).
# - Verdict: Band 5.0. Pronunciation/Vocab issues.

scored_samples = [
    {
        "id": 0, "sample_id": "pBrFbXB7EAg_q16", "video_id": "pBrFbXB7EAg",
        "part": 2,
        "question": "Gift ring?",
        "transcript": "It but I never find the ring that I like because some rings are more complicated more too the too much and some rings it is too too simple so I asked my grandmother to to help me to find this ring for my girlfriend so so we went also in the lot of shops and we do not find the very good after that she gave me his her ring that she that she that she have from his from my grandfather so that is a my gift for it is a special gift because she is a she is a ring she have a a history family history and that is that is okay do you enjoy giving gifts yes yes because usually I give some gifts only to people that I like very very much not just my friends so for my friends I can give some gifts like sunflower or some perum that is some gift that they do not take for a long time thank you can I have the booklet and the pencil and paperback please than.",
        "word_count": 189,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "preposition"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["complicated", "simple", "family history"],
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
            "reason": "'went also in the lot of shops' (to a lot of). 'she have' (had). 'she is a ring' (it is). 'perum' (perfume)."
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
                "why_not_8": "Frequent errors.",
                "why_not_6": "Complex sentences."
            },
            "vocabulary": {
                "why_not_8": "Word choice errors.",
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
        "grammar_reason": "Errors present but clear. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "pBrFbXB7EAg_q17",
        "video_id": "pBrFbXB7EAg",
        "part": 3,
        "question": "Children gifts?",
        "transcript": "Yes a lot of money and sometimes for just when there are no events just usually we can give some gifts so what sort of gifts do children give to adults in their families I usually some picture they make in the school or or some flowers also yes because they have usually some pocket money and they spend their their money for some gifts usually for their mother or not for their friend for their brother or sister and do you think adults appreciate gifts that children have made themselves eles more than gifts that they have bought in a shop yes I think made it is it is look like they invest their time on their thinking about that so it is U more complicate than to buy something in the chop so how important do you think it is for families to give gifts to each other it is a make some relationships between us and they prove their feelings between us so it is very important.",
        "word_count": 172,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["pocket money", "appreciate", "invest their time"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'it is look like' (it looks like). 'more complicate' (complicated). 'chop' (shop)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Structure errors.",
                "why_not_6": "Good."
            },
            "vocabulary": {
                "why_not_8": "Word form errors.",
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
        "grammar_reason": "Errors present. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "pBrFbXB7EAg_q18",
        "video_id": "pBrFbXB7EAg",
        "part": 3,
        "question": "Corporate gifts?",
        "transcript": "Some pants or some glasses with bread of a company so sometimes it is also a good advertise right so it is important for the company but what about gift giving for the economy of the country in general I in France is buying gifts an important part of the economy do you think yes I think so I think buying the gifts in France particularly it is a a very big business and many shops and many employers depend that this this sector and the also the tourist sector live with this with this things and that is all right now some people say that it would be better for society if all the money that was spent on gifts was given to help poor people instead what do you think about that I think we have to to help the poor people but we have also to make some relationships between us because I think it is also very important",
        "word_count": 169,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["tourist sector", "relationships"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'bread of a company' (brand). 'good advertise' (advertisement)."
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
                "why_not_8": "Minor errors.",
                "why_not_6": "Good."
            },
            "vocabulary": {
                "why_not_8": "Word choice errors.",
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
        "grammar_reason": "Accurate. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "eaq7kXxtGns_q02",
        "video_id": "eaq7kXxtGns",
        "part": 3,
        "question": "Learning sources?",
        "transcript": "Use several sources to gain knowledge and experience that watching videos on YouTube or learning I add with interactive software perfect tutorial or ebooks if you could learn any new skill what would it be maybe I pick a good big surfing he sounds very fun and I am good riding the wave has the information people learn in public schools changed from 20 years ago knowledge from government school this day compared to two decade prior has completely developed with higher technology and more information this day still did not focus more on critical thinking like computer back then there was more focus on lexical information and what memory",
        "word_count": 107,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "article"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["interactive software", "critical thinking", "lexical information", "gain knowledge"],
            "grammar_structures_used": ["complex_sentences"]
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
            "reason": "'pick a good big surfing' (pick up surfing?). 'good riding the wave' (good at riding). 'two decade prior' (decades)."
        },
        "grammar_profile": {
            "complexity_level": "high",
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
                "why_not_8": "Minor errors.",
                "why_not_6": "Complex."
            },
            "vocabulary": {
                "why_not_8": "Precision issues.",
                "why_not_6": "Academic terms."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level terms ('lexical', 'interactive'). Band 8.",
        "grammar_reason": "Errors present. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "wbysCUmZQZA_q02",
        "video_id": "wbysCUmZQZA",
        "part": 1,
        "question": "Breakfast?",
        "transcript": "A day I have breakfast lunch and dinner and one or two snacks what do you usually eat for breakfast well if I had to say I like Li cereal with milk most often although I eat fruits on xtube I think I the bowl of cereal more than anything else do you like to cook why or why not mmm I do not really like to good because I am not very good at it like last weekend I try to make some spaghetti and it just did not really taste very good so I think I put too much force on it what is your favorite food and what do you like about it my favorite type of food is definitely a good beef it is Vietnamese traditional another sort that if done correctly it just tastes great if you could eat any kind of food what would it be and why that is an uncommon question just give me a moment to think sure if I could try any food I think I would like to try the most expensive caviar not just because it costs a lot but also because I think it would probably like taste amazing alright that is the end of part one now we will continue with part two for part two I am going to give you a card please do not turn it over also here is some note paper and a pencil.",
      "word_count": 223,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["cereal", "spaghetti", "caviar", "uncommon question"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
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
            "triggered": True,
            "reason": "'xtube' (YouTube?). 'put too much force on it' (effort/pressure?)."
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
                "why_not_9": "Minor oddity 'force'.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Excellent. Band 8.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 8,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "wbysCUmZQZA_q03",
        "video_id": "wbysCUmZQZA",
        "part": 2,
        "question": "Hang out with?",
        "transcript": "If I had a chance to hang out with the person for 24 hours it would probably be Jim Carrey I love comedy and I think he is one of the funniest people on earth I have seen many of his movies over the years and they all made me laugh so hard I would love to find out more about his personal life and maybe even hear some original jokes I think a good place to meet mr. Kerry would be in a quiet pub after a few drinks we could really get into some conversation we could order some food I could find out what a true comedian really likes to eat and most importantly I think quite odd would give the right atmosphere to just let loose and be ourselves I would like to talk about a variety of topics with mr. Carey but most importantly just to find out who he really is off camera I am interested to know more about his journey to become famous which one of his movies in like doing the most was for some of the biggest difficulties he had during his career and what he plans to do in the future of course I would ask him if he knows some funny jokes and the reason I would like to meet with mr. Kerry is because I think good love is one of the most amazing parts of life and there are many people who know more about this than him since he is very very famous it is virtually impossible to have a one conversation video",
        "word_count": 266,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["let loose", "off camera", "virtually impossible", "hang out"],
            "grammar_structures_used": ["conditionals", "complex_sentences"]
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
                "why_not_9": "Idiomatic ('let loose', 'off camera').",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent idioms. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "QcpknFmrQzo_q02",
        "video_id": "QcpknFmrQzo",
        "part": 1,
        "question": "Haircut?",
        "transcript": "It I get my haircut want them on I usually went to Barbershop but nowadays due to coronavirus I go to a shop that is near my house they offer a reasonable price to University students and because I want to have a tidy hair and so I look good so I can go and hang out with my friends thank you how long have you had your character's hairstyle I have maintaining this style about a year since I dispatched from military service and I like it because I do not have to put a lot of wax and hair product on it and I like this air serving Style thank you have you have your card experience bring my military service we were forced to cut our hair very very short and that is I did not like how it appeared from outside so I did not like that okay very good do you like getting your hair cut as I mentioned before I like to have it and tied up hair and so be refreshed so I look refreshed and yeah I because after that I go into the barbershop once a month thank you can you compare your hairstyle now to when you are very child and that is a great question when I was a child my brother used to cut my hair and he had a dreamer because he used trimmer to cut my hair my hair always were short very short and I did not like that but nowadays I cannot put put in style my hair which represents my identity so I prefer this kind of style from the one I had in childhood",
        "word_count": 273,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["military service", "reasonable price", "hang out"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'want them on' (once a month). 'dispatched' (discharged). 'hair always were' (was). 'dreamer' (trimmer). 'put in style' (style)."
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
                "why_not_8": "Errors.",
                "why_not_6": "Complex."
            },
            "vocabulary": {
                "why_not_8": "Word choice errors.",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range but errors. Band 7.",
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "QcpknFmrQzo_q04",
        "video_id": "QcpknFmrQzo",
        "part": 2,
        "question": "Sleepy?",
        "transcript": "I was very sleepy during the exam and during the exam I rehashed to myself why am I doing this why I stayed up all the night and after the exam I got the result and that was very great and I said okay it was worth it let us stay like very good and so.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["worth it", "stayed up"],
            "grammar_structures_used": ["compound_sentence"]
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
            "reason": "'rehashed to myself' (asked myself? repeated?). 'stayed up all the night' (all night)."
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
                "why_not_8": "Good.",
                "why_not_6": "Error free."
            },
            "vocabulary": {
                "why_not_8": "Minor errors.",
                "why_not_6": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Adequate. Band 6.",
        "grammar_reason": "Error free sentences. Band 7.",
        "vocabulary": 6,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "QcpknFmrQzo_q05",
        "video_id": "QcpknFmrQzo",
        "part": 3,
        "question": "Wakes up early?",
        "transcript": "I would say oh yes yes right and who do you think wakes up earlier younger people or older people people are have they have stressed and they are they have tiredness into their body so it is difficult for them to and to wake up early but younger people are able to wake up early morning so what kind of sleep I have not thought about that so let me think I would say night shift workers like asleep because they should they wake up at the night they start working at during the night and they asleep they go back to their sleep at the morning their life balances kind of break down and and they come they always confuse if they want to work right now or sleep right now and because of this confusion they lose a lot of time during the day yeah that is right and I think there is a lot of debate these days about high school students do they sleep enough can you tell me the situation in your country I personally think and this problem has been at rest in my country now but but my in my country people think College college is a place that and people get a degree and graduate and go to a good prestigious University after their graduation they find a decent job and then they have a better life that is the thought of my people because of that a student working very hard studying very hard and I saw some of my friends during college they were working they were studying they were doing their homework doing their lecture times and the audience and the teacher would not give them a notice because they they say leave them away they are a student they they.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["prestigious university", "night shift", "tiredness"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'people are have they have stressed' (stressed). 'problem has been at rest' (addressed?). 'leave them away' (alone)."
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
                "why_not_8": "Errors.",
                "why_not_6": "Complex."
            },
            "vocabulary": {
                "why_not_8": "Word choice errors.",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range. Band 7.",
        "grammar_reason": "Errors present. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "FrTPoIMqNFQ_q03",
        "video_id": "FrTPoIMqNFQ",
        "part": 3,
        "question": "Dormitory?",
        "transcript": "Is located in the school and territory has a really convenient things like they provided two parts and restrooms and it gives it gives to my girlfriends to great impacts or effects it is because like dormitory has as a result it is too bad and restroom also they provided a tiger for on studying and laptop as well so she can easily study when she wants and it gives her lots of advantages such as like near go to it is easy to go library because it is nearly the dormitory and and yeah so it is it is really positive impacts to my girlfriends and actually I have experiences about living in a dormitory and this experience was really great so I hope my girlfriend has a great experiences and yeah okay mate that is yeah that is two minutes now all right cool nice one okay perfect let us go on to the third part of the test let us keep going okay so why do some young people keep moving house if if we say young people to like same Asia with me like 22 to 28. I feel they do not have enough money because like for young people they usually rent their rooms so if they have enough money they can buy a house but yeah because of that they usually moved to a new place I think and do you think people like moving to new places I think it is because right new place always gives people positive effects and yeah what kind of positive effects I think right relationship with new neighborhoods and yeah and like for example I was moved to a new place nearly my school and right the thief Thief trying to try to store my package and my.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["convenient", "dormitory", "advantages"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["meaning_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'territory' (dormitory). 'tiger for on studying' (desk?). 'same Asia' (same age). 'store my package' (steal?)."
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
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex attempts."
            },
            "vocabulary": {
                "why_not_7": "Meaning errors.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Adequate range but confusion. Band 6.",
        "grammar_reason": "Frequent errors. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "FrTPoIMqNFQ_q04",
        "video_id": "FrTPoIMqNFQ",
        "part": 3,
        "question": "Roommates vs Alone?",
        "transcript": "Neighborhoods saw them and protect my boxes so yeah okay all right what is the difference between living alone and living with roommates a day has a huge differences maybe living with to I mean living with roommates give some great advantages such as like for example like my roommates can cook for me or like we can share our we can share our ideas each other about studying yeah and like if there is a I mean like if I need to say differences living alone is really lonely so I have experience about living alone and it was really lonely like talk less speechless so but if I have a roommates I feel really a great relationship with my friends yeah all right nice and besides cooking what are some other skills that people need to learn if they live by themselves oh I think cleaning of course like cleaning is really easy but it is hard to start so yeah cleaning or like like it is a little bit specific but it is make some Wi-Fi or Wi-Fi connection when I was in United States it was Wi-Fi connection is really problem it was really serious problem so I really need to contact with the company and such like they sending your emails so they really need to learn about this I think yeah yeah yeah and do you think it is parents responsibility to teach their children how to live independently oh yes of course because like living alone is really difficult it is hard really hard to do that so if if if people who live alone or like independently they if there is a have from parents either European grades and yeah it is really conducive to people.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["independently", "cleaning", "roommates"],
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
            "reason": "'talk less speechless' (speechless/talk less). 'make some Wi-Fi' (set up). 'conducive to people' (?)."
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
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex attempts."
            },
            "vocabulary": {
                "why_not_7": "Word choice errors.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Adequate. Band 6.",
        "grammar_reason": "Frequent errors. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "FzmocI_ikjU_q01",
        "video_id": "FzmocI_ikjU",
        "part": 1,
        "question": "Introduction?",
        "transcript": "On your clothes yes a computer difficulty attested kasam a week after all they exam birthday boy name of a good tamiflu please my name is sumit yaar anju call me punit ok pandit festival passport ki aapke ghar me share it oon toh neeche karo ab tak kya office me online tell me something about your educational qualification most my password my graduation adham english skills and chronic illness nupur institute located in the old city stone clear shot that describe your family setting family player for 19.51 family father mother and sister and brother hai aap akele talk about their home town where hello viewers welcome to play a very important role in life is like believing beautiful city name is dena distik fatehabad and i love my home because most of the facility available in here fall it is gold.",
        "word_count": 139,
        "analysis_metadata": {
            "grammar_error_patterns": ["incoherence"],
            "grammar_error_frequency": "dominant",
            "vocab_collocation_usage": "none",
            "vocab_evidence": [],
            "grammar_structures_used": ["none"]
        },
        "micro_flaws": {
            "grammar": ["coherence_breakdown"],
            "vocabulary": ["foreign_language"]
        },
        "vocab_control": {
            "appropriateness": "none",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Transcript contains Hindi/Urdu ('ki aapke ghar me', 'hai aap akele') and incoherent English ('password my graduation')."
        },
        "grammar_profile": {
            "complexity_level": "none",
            "accuracy_level": "none",
            "flexibility": "none",
            "error_density": "dominant"
        },
        "discourse_metrics": {
            "length_appropriateness": "none",
            "redundancy": "high",
            "development_depth": "none"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Incoherent.",
                "why_not_3": "Words recognizable."
            },
            "vocabulary": {
                "why_not_5": "Mixed language.",
                "why_not_3": "Basic words."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Cannot use sentence forms except in memorised phrases.",
            "vocabulary_band": 4,
            "vocabulary_text": "Uses basic vocabulary."
        },
        "vocab_reason": "Basic/Mixed. Band 4.",
        "grammar_reason": "Incoherent. Band 4.",
        "vocabulary": 4,
        "grammar": 4
    },
    {
        "id": 0, "sample_id": "l6M6oX6jI8w_q03",
        "video_id": "l6M6oX6jI8w",
        "part": 3,
        "question": "Sellers price?",
        "transcript": "Should sellers set price for their products should a product I am sorry the product it is harder for me so how should sellers set prices for their items that they are selling items shoes items selling is very important i think so yes do you think online shopping will replace shopping in stores online store do you think online shopping will replace shopping in stores in store i i prefer in-store shopping because i i will check my size if big size so i ordered online that was not good yes that is why i prefer in-store shopping do you think most people also prefer in-store shopping like you i think so because so many sizes and many material so i i want to check it and yeah people need it yes thank you that is the end of the speaking test",
        "word_count": 139,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["in-store shopping", "replace", "ordered online"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'if big size' (if it is a big size). 'many material' (materials)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "moderate",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent errors.",
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
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "0ZizySMJwp4_q01",
        "video_id": "0ZizySMJwp4",
        "part": 1,
        "question": "Ready?",
        "transcript": "Okay, let us go. Ok so.",
        "word_count": 6,
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
                "why_not_6": "Too short.",
                "why_not_4": "Accurate."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Produces simple sentences accurately.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic. Band 5.",
        "grammar_reason": "Accurate. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "0ZizySMJwp4_q02",
        "video_id": "0ZizySMJwp4",
        "part": 1,
        "question": "Work study?",
        "transcript": "Well, I am actually doing a bit of right now. My primary focus is my university degrees in logistics and supply chain management. I am a full-time student but to support my family financially and to do a part job.",
        "word_count": 38,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["logistics", "supply chain management", "financially"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'doing a bit of right now' (both?). 'part job' (part-time job)."
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
                "why_not_7": "Fragmented ideas.",
                "why_not_5": "Complex words used."
            },
            "vocabulary": {
                "why_not_7": "Minor errors.",
                "why_not_5": "Topic vocab."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Topic words. Band 6.",
        "grammar_reason": "Fragments. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "0ZizySMJwp4_q03",
        "video_id": "0ZizySMJwp4",
        "part": 1,
        "question": "Job?",
        "transcript": "I have at the convenience store. My dirty is surviving customer at the culture filling up the new products and making sure the store clean and tidy.",
        "word_count": 26,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["convenience store", "clean and tidy"],
            "grammar_structures_used": ["simple_sentence"]
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
            "reason": "'My dirty' (duty). 'surviving customer' (serving). 'at the culture' (counter?)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent errors.",
                "why_not_4": "Meaning clear."
            },
            "vocabulary": {
                "why_not_6": "Wrong words.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Wrong words. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
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
