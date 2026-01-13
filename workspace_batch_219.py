import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 219 ---
# Total Samples: 20
# Samples Analyzed:

# 1. oEUBd3ZjStA_q05 (Band 7.0)
# Transcript: "single most important notion... see the big picture... perspective necessary..."
# Analysis: "notion", "big picture", "perspective".
# - Verdict: Band 7.0.

# 2. XqGa0VS5vh4_q01 (Band 6.0)
# Transcript: "where I live now is a little town that in the north... one the reason... three departments doors... yard is available... raise a dog instead... hiking with my family in gummy mountain... besides where at least... not that code..."
# Analysis:
# - Grammar: "that in the north" (that is in). "one the reason" (one reason). "departments doors" (department stores). "gummy mountain" (Yangmingshan?). "not that code" (cold).
# - Vocabulary: "convenient", "suitable".
# - Verdict: Band 6.0. Mispronunciations affecting transcription ("code", "departments doors").

# 3. XqGa0VS5vh4_q02 (Band 6.0)
# Transcript: "public renting system... do not think I have that much eager... shoes is broken... Palmer store... use of ways of time..."
# Analysis: "that much eager" (eagerness/desire). "shoes is broken" (are). "Palmer store" (department store). "use of ways of time" (waste of time).
# - Verdict: Band 6.0.

# 4. XqGa0VS5vh4_q03 (Band 6.0)
# Transcript: "pick up the sink" (thing).
# Analysis: Fragment.
# - Verdict: Band 6.0.

# 5. XqGa0VS5vh4_q04 (Band 6.0)
# Transcript: "interpersonal relations... culture change changed a lot... burrito for Panda... is something... genetically modified food... huncle..."
# Analysis: "culture change changed" (has changed). "burrito for Panda" (Food Panda). "huncle" (harmful?).
# - Verdict: Band 6.0.

# 6. XqGa0VS5vh4_q07 (Band 6.0)
# Transcript: "gave it to you... lexical rage... pretty good."
# Analysis: EXAMINER FEEDBACK.
# - Verdict: INVALID (Skip).

# 7. u8oz83O1n_g_q02 (Band 8.0)
# Transcript: "Compared to before but in terms of recreational activities there has not been much change."
# Analysis: Accurate.
# - Verdict: Band 8.0.

# 8. u8oz83O1n_g_q03 (Band 8.0)
# Transcript: "located near where i work... contemporary and minimalistic approach... essential furniture neatly arranged... prioritize neutral tones... sleek stylish and neat interior aesthetic... pleasing to the eye... economical..."
# Analysis:
# - Grammar: Error free.
# - Vocabulary: "contemporary", "minimalistic", "sleek", "aesthetic", "pleasing to the eye".
# - Verdict: Band 9.0 (GT is 8.0, but this sample is very strong).

# 9. u8oz83O1n_g_q04 (Band 8.0)
# Transcript: "requires significant financial stability... financially independent... stage of life... settle down long term... designing the interiors..."
# Analysis: "significant financial stability".
# - Verdict: Band 8.0.

# 10. pBrFbXB7EAg_q02 (Band 7.5)
# Transcript: "spent all my weekends playing... concerns... enjoy... relax out of the whole week... take a great time of sleeping..."
# Analysis: "relax out of the whole week" (relax after). "take a great time of sleeping" (get a good amount of sleep).
# - Verdict: Band 7.5.

# 11. pBrFbXB7EAg_q03 (Band 7.5)
# Transcript: "prefer listening to live music or recorded... singer is not good in life music... makes me more concentrated..."
# Analysis: "in life music" (live). "more concentrated" (focused / helps me concentrate).
# - Verdict: Band 7.5.

# 12. pBrFbXB7EAg_q05 (Band 7.5)
# Transcript: "Like to discuss with you one or two more general questions..."
# Analysis: EXAMINER SPEECH.
# - Verdict: INVALID (Skip).

# 13. pBrFbXB7EAg_q06 (Band 7.5)
# Transcript: "parents appr them up... recognize the real relationships... tied up the relationships and makes it more strong..."
# Analysis: "appr them up" (brought them up). "tied up" (ties/strengthens). "makes it more strong" (stronger).
# - Verdict: Band 7.0/7.5.

# 14. pBrFbXB7EAg_q07 (Band 7.5)
# Transcript: "work in the redic... psychological aids... refugees... Invasion... pass and get over this... living in the same glob... small village..."
# Analysis: "redic" (Red Cross?). "psychological aids" (aid). "same glob" (globe).
# - Verdict: Band 7.5.

# 15. pBrFbXB7EAg_q08 (Band 7.5)
# Transcript: "I am a nurse... have to reason for that... pass the very difficult exam... get Mark for the just nursing... my mom always contrast..."
# Analysis: "have to reason" (two reasons). "get Mark" (got the marks). "mom always contrast" (disagreed?).
# - Verdict: Band 7.0.

# 16. pBrFbXB7EAg_q09 (Band 7.5)
# Transcript: "Studies English as well is when you start job or study you you would like to fresh..."
# Analysis: "am Studies" (studying). "like to fresh" (freshen up/relax).
# - Verdict: Band 7.0.

# 17. pBrFbXB7EAg_q10 (Band 7.5)
# Transcript: "special glass... Turkish tea... golden Turkish glasses... mother-in-law... she Haven never she had never had any present... celebrate Mother Days very especially... exciting and sensible..."
# Analysis: "Haven never" (had never). "sensible" (emotional/sensitive?).
# - Verdict: Band 7.0.

# 18. pBrFbXB7EAg_q12 (Band 7.5)
# Transcript: "Dro in the price... GI us very important... keep money turned... turned again and again... expect that..."
# Analysis: "Dro" (drop). "GI us" (gift giving is?). "money turned" (circulating).
# - Verdict: Band 7.0.

# 19. pBrFbXB7EAg_q13 (Band 7.5)
# Transcript: "People will help you and it will be Circle again... TR train at the young age... like a habit..."
# Analysis: "be Circle" (a circle).
# - Verdict: Band 7.0.

# 20. pBrFbXB7EAg_q14 (Band 7.5)
# Transcript: "stressful week... play football... do some kity... show some films... English students... she speak also French... I help him I I help her... decompress..."
# Analysis: "kity" (karate? activity?). "she speak" (speaks). "decompress".
# - Verdict: Band 7.5.

scored_samples = [
    {
        "id": 0, "sample_id": "oEUBd3ZjStA_q05", "video_id": "oEUBd3ZjStA",
        "part": 3,
        "question": "Important notion?",
        "transcript": "Think is the single most important notion to keep in mind when facing a difficult situation and why is this notion key to solving a difficult situation that is a difficult question could you give me a moment to think about it yeah taqutor well if I had to choose only one I would like to say the ability to see the big picture that billet special ability allows a person to see many problems for what they are small relatively important and temporary long-term thinking gives person perspective necessary to solve problems easily and quickly",
        "word_count": 91,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["big picture", "perspective", "long-term thinking"],
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
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Natural. Band 7.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "XqGa0VS5vh4_q01",
        "video_id": "XqGa0VS5vh4",
        "part": 1,
        "question": "Living where?",
        "transcript": "Can you tell me a little about where you are living at the moment where I live now is a little town that in the north of Taipei City it is called Kim Moo and I think it is a very suitable place for us to live in because one the reason is that the yummy national that yummy Mountain National Park is just besides our cows so it is very convenient for us if we want to go hiking with our family members and also it is also very convenient if we want to buy something because there are three departments doors in Tim move so if we want to go searching for some food or buy something it is really convenient to us do you prefer living in a house or an apartment I think that I prefer living in a house than a department it is because the yard is available in a house but there there would not be any yard for us to raise a dog instead so I think a house it is quite convenient for us too to have a pet with and also a house is usually much bigger than an apartment I think it provides a better standard of living for for me to stay in a house rather than department some of the things that you like to do at the weekend in the summer in summertime I like to go hiking with my family in gummy mountain which is just besides where at least and that is because in summertime it is not that code for us to to be in the top of the mountain because in winter time is it is really cold in the mountain and also I like to go to do some water activities in summertime in weekend I usually go to the northern.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["standard of living", "convenient"],
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
            "reason": "'departments doors' (department stores). 'besides our cows' (house?). 'not that code' (cold). 'department' (apartment)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
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
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex attempts."
            },
            "vocabulary": {
                "why_not_7": "Word choice errors.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors present. Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "XqGa0VS5vh4_q02",
        "video_id": "XqGa0VS5vh4",
        "part": 1,
        "question": "Families weekends?",
        "transcript": "Coast of Taiwan and like we can do some boat boating and some diving there I think it is quite enjoyable what are some of the things that families do together at the weekend in your country I think that families in my country which is Taiwan usually go to a supermarket together in the weekend they to buy some new clothes or new shoes or even go to the supermarket under the department store because there are more choices compared here to the supermarket outside and then they also usually go to a movie theater to watch the latest movie and Nancy I could come up ways is that they can also go cycling the curse I think it is very convenient for us to use a public renting system do you like shopping I think I do not really like shopping because I do not think I have that much eager to buy fancy things I own I only buy what I really need to use so for example if my shoes is broken I will get buy it but I will not keep shopping for for the new shoes because it may be unnecessary for me so in conclusion I do not like shopping not necess do you feel it is true that women like shopping more than men in my life experience I believe that this is true because I think that woman is more patient to a search for something that they want to buy so they can spend the whole day and you know this Palmer store which sounds ridiculous to a man I think males will think that it is very very a use of ways of time to spend holding and the common store if a man wanted by something they will just go to the shop.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form", "agreement"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["department store", "unnecessary"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'much eager' (eagerness). 'shoes is broken' (are). 'Palmer store' (department store). 'use of ways of time' (waste of time)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
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
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex attempts."
            },
            "vocabulary": {
                "why_not_7": "Errors affect meaning.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors present. Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "XqGa0VS5vh4_q03",
        "video_id": "XqGa0VS5vh4",
        "part": 1,
        "question": "Pick up?",
        "transcript": "And pick up the sink",
        "word_count": 5,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["fragment"]
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
                "why_not_7": "Too short.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Basic. Band 6.",
        "grammar_reason": "Basic. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "XqGa0VS5vh4_q04",
        "video_id": "XqGa0VS5vh4",
        "part": 3,
        "question": "Food culture?",
        "transcript": "Generation and also I sing that would bring people closer because that we usually eat together with our friends in our country so so I think through eating put together we can strengthen our interpersonal relations so I think that the two men culture role to play in our country how has food culture changed in your country over the last 20 years I sing the food culture change changed a lot during the last two decades 20 years ago many families will cooked at home frequently or maybe go out maybe occasionally go outside for a fashion restaurant to eat together the nowadays people in Taiwan are more likely to use the sharing economy like a burrito for Panda to order their food from our restaurant home so I think that is a significant change that people become more lazy with food they just want to is something instead of really cooked together with family or eat together outside travels family they just want to have it have it done what are your feelings about the use of genetically modified food I think I am quite concerned about that genetically modified food it is because that no research can can strongly suggest that this kind of food would not be harmful to our health and so I usually choose to eat the natural or even organic food if I have choice is available for me so I sing that genetically modified food should be prevented from the restaurant because it may be huncle to our health and nobody want to put themselves under risky situation",
        "word_count": 269,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "verb_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "mixed",
            "vocab_evidence": ["interpersonal relations", "genetically modified food", "harmful to health"],
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
            "reason": "'culture change changed' (has changed). 'fashion restaurant' (fancy?). 'burrito for Panda' (Food Panda). 'huncle' (harmful)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
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
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex structures attempted."
            },
            "vocabulary": {
                "why_not_7": "Errors ('huncle', 'fashion').",
                "why_not_5": "Good topic range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good topic vocab but errors. Band 6.",
        "grammar_reason": "Errors present. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "u8oz83O1n_g_q02",
        "video_id": "u8oz83O1n_g",
        "part": 1,
        "question": "Recreation?",
        "transcript": "Compared to before but in terms of recreational activities there has not been much change.",
        "word_count": 14,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["recreational activities", "in terms of"],
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
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Short.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Short.",
                "why_not_7": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Precise. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "u8oz83O1n_g_q03",
        "video_id": "u8oz83O1n_g",
        "part": 2,
        "question": "Apartment?",
        "transcript": "It is located near where i work and where i have easy access to grocery stores restaurants coffee shops and other places of entertainment in terms of interior design the apartment would have a contemporary and minimalistic approach it does not have to be a huge apartment but i would like it to have a lot of open space with only the most essential furniture neatly arranged in all of the rooms furthermore i would prioritize neutral tones brown beige white etc for my walls doors and furniture as well as as decorative objects in addition the apartment would be filled with natural light so there would be a lot of windows i would like to have such a place to my own in a couple of years before I am 30 and there are a few reasons why i would like it to be modern and minimalistic so first I am really into this sleek stylish and neat interior aesthetic it is all very pleasing to the eye and I am not a fan of cluttered space so that would be the perfect apartment for me second it would be quite easy to tidy up and maintain cleanliness and orderliness in such an apartment and finally it would be quite economical to live in a minimalistic apartment because i would not have to spend too much money on furniture and decoration so",
        "word_count": 222,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["minimalistic approach", "neutral tones", "sleek stylish", "cluttered space", "pleasing to the eye"],
            "grammar_structures_used": ["complex_sentences", "passive_voice"]
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
                "why_not_9": "'sleek', 'cluttered space'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise terms. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "u8oz83O1n_g_q04",
        "video_id": "u8oz83O1n_g",
        "part": 3,
        "question": "Housing?",
        "transcript": "Do not agree that there is such a thing as the right age for young adults to move out of their parents house because living on your own requires significant financial stability and not everyone can achieve that at the same age some people manage to be in financially independent quite early in their 20s for example but others may not so it is completely fine that you live with your parents until you are completely financially ready to move out and live on your own all right so is it better to own your own home or to rent so it really depends on the stage of life that you are in for example if you are a college student or a young adult who has just started to work it might be better to rent a place rather than own your own house because you cannot afford to own own a house anyway and but if you already have a family it might be a better idea to own a house so that you can settle down long term all right my next one would be what types of places do most people in your country live in so people in big cities mostly live in either apartment complexes or just normal houses but i would say that apartment complexes are becoming increasingly popular in the recent years but people in the country in the countryside mostly live in just normal houses for all i know so what are some of the pleasures involved in making a home for ourselves so i think that the process of designing the interiors for our home is especially exciting so personally i think that i would very much enjoy choosing the furniture furniture arrangements the apartment style and decorative objects for my.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["financial stability", "settle down", "apartment complexes", "interiors"],
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
                "why_not_9": "'financial stability', 'settle down'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise terms. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "pBrFbXB7EAg_q02",
        "video_id": "pBrFbXB7EAg",
        "part": 1,
        "question": "Weekends?",
        "transcript": "Weekends now more than you did when you were a child well not really when I was a child I just spent all my weekends playing and but now I have lots of concerns sometimes I I have to stay at home to study so know when I was a child I was I enjoyed most how important is it for you to relax at the end of the week well it is very important because you just relax out of the whole week because you were studying or working so you need peace and relax and and sometimes to take a great time of sleeping just to PR prepare yourself for the next week.",
        "word_count": 113,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["concerns", "peace and relax"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["phrasing_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'relax out of' (relax after). 'take a great time of sleeping' (get good sleep)."
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
                "why_not_9": "Phrasing errors.",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good. Band 7.",
        "grammar_reason": "Phrasing errors. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "pBrFbXB7EAg_q03",
        "video_id": "pBrFbXB7EAg",
        "part": 1,
        "question": "Live vs Recorded?",
        "transcript": "When I was a child do you prefer listening to live music or recorded music well recorded I do not like live music because I feel because I feel always the singer is not good in life music so I feel that recorded is better do you think listening to music helps you study yes I always listen to music when I am studying sometimes my friends make fun of me because I am I am not concentrating but actually it makes me more concentrated thank you now I am going to give you a topic and I would like you to talk about it for one to two minutes.",
        "word_count": 107,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["concentrating", "recorded music"],
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
            "reason": "'in life music' (live). 'makes me more concentrated' (helps me concentrate)."
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
                "why_not_9": "Minor errors.",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "'concentrated' vs 'concentrate'.",
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
        "grammar_reason": "Mostly error free. Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "pBrFbXB7EAg_q06",
        "video_id": "pBrFbXB7EAg",
        "part": 3,
        "question": "Gift giving?",
        "transcript": "Parents do you think well it depends how the parents appr them up sometimes I think it is it is when they start to recognize the the the the real relationships because when they were before seven or before six years old they tend not to recognize what does it mean to give a gift or to give and even they do not recognize the relationships but after seven I think they start to to recognize and to feel that I need to give a present to my father or mother as they are giving me and every time I have an occasion so how important do you think giving gifts is within families yeah it is important because you always give them the feeling that you are really caring for them and you really think of them and whenever you give them things that they like you feel that you are really all the time thinking of them and I mean yeah I mean you it it is also tied up the the the relationships and makes it more strong",
        "word_count": 182,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["caring for them", "relationships"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["phrasing_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'appr them up' (brought up?). 'tied up the relationships' (strengthens/ties). 'makes it more strong' (stronger)."
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
                "why_not_9": "Comparison error 'more strong'.",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "Phrasing issues.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range. Band 7.",
        "grammar_reason": "Minor errors. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "pBrFbXB7EAg_q07",
        "video_id": "pBrFbXB7EAg",
        "part": 3,
        "question": "Aid?",
        "transcript": "Psychological AIDS when as we do because I am I work in the redic and so I know what this does not mean to give a psychological aids for sometimes for refugees or for even to go for the near countries that in really in Need For example in my country we go to Iraq or to Lebanon in in the when when the Invasion and so we help them psychologically to just pass and get over this so what do you think motivates government to give Aid to other countries well it is important because I feel feel that it is it is it is let us recognize ourself that at the end we are all human beings and we are living in the same glob and it is like a small village and you are we are the all members of the same or the same land so I feel it is it is just really makes the relationships more strong and it gives you it really feel let you feel like you are Humanity at the end and do you think the aid is always helpful yes I think so because whenever you think of giving Aid to other countries I mean it is when they are in need I mean it is it is really helpful",
        "word_count": 213,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["psychological aid", "refugees", "human beings"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'redic' (Red Cross?). 'psychological aids' (aid). 'same glob' (globe). 'makes relationships more strong' (stronger)."
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
                "why_not_9": "Comparison error.",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "Pronunciation/word form errors.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good topic vocab. Band 7.",
        "grammar_reason": "Good. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "pBrFbXB7EAg_q08",
        "video_id": "pBrFbXB7EAg",
        "part": 1,
        "question": "Work?",
        "transcript": "You work or are you a student I am a nurse and why did you choose this kind of work I have to reason for that first I am from Turkey in Turkey you have to pass the very difficult exam if you like to go to the university and I get Mark for the just nursing I think and the second one from my childhood I always be like doctor or nurse and to help other people I really like that which is my mom always contrast she because she wants to me be a teacher like my sisters what kind of work would you like to do in the future I do not know system in England very well but maybe nursing advisor or some management job I do not know exactly.",
        "word_count": 139,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["management job", "nursing advisor"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'have to reason' (two reasons). 'get Mark' (got the marks). 'mom always contrast' (disagreed)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Structure errors.",
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
        "grammar_reason": "Errors present. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "pBrFbXB7EAg_q09",
        "video_id": "pBrFbXB7EAg",
        "part": 1,
        "question": "Important week?",
        "transcript": "Of the week it is very important but at the moment it is not possible because now I am Studies English as well is when you start job or study you you would like to fresh but it is really difficult to be.",
        "word_count": 42,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'am Studies' (studying). 'like to fresh' (freshen up)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Verb errors.",
                "why_not_6": "Good."
            },
            "vocabulary": {
                "why_not_8": "Phrasing errors.",
                "why_not_6": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Adequate. Band 7.",
        "grammar_reason": "Errors. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "pBrFbXB7EAg_q10",
        "video_id": "pBrFbXB7EAg",
        "part": 2,
        "question": "Gift teacher?",
        "transcript": "My I give it to my English teacher last year she is a fan of turkey and the Turkish culture I gave to her some special glass which is we just use for the Turkish tea and she loves Turkish tea and last when I last my last holiday I bring some special like a golden Turkish glasses and she she really liked them it was special because she likes Turkish culture Turkish food and she knows a lot about turkey when we are together we can speak a lot about my culture my religion and stuff from tury or cities of turkey and she is great I think because it is really nice to know somebody from England and know about you all and another gift another special gifts I give some somebody who was my mother-in-law and normally we do not celebrate mother days and she Haven never she had never had any present from her child and in my family we celebrate Mother Days very especially and i b a ring for her and she was really exciting and sensible because the first time somebody celebrate her mother's day and she she even do not know she even did not know about Mother's Day but I explained to her and then I give the gifts and after that I always do thank you do you enjoy giving gifts yes I really like to give people gifts when I saw them they like it they excited about it I feel have to",
        "word_count": 233,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["culture", "religion"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Haven never' (had never). 'sensible' (emotional?)."
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
                "why_not_8": "Tense errors.",
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
        "grammar_reason": "Accurate mostly. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "pBrFbXB7EAg_q12",
        "video_id": "pBrFbXB7EAg",
        "part": 3,
        "question": "Gift giving economy?",
        "transcript": "Sale or Dro in the price something like that and how important is gift giving for a country's economy I think in England is perfect for economy because GI us very important normally for us if we know people have not got the money they do not have to buy anything but I think this country have to buy something and is a good Circle for to keep money turned and turned again and again do you think there is pressure on people to buy too many gifts yes I think so yeah why because I I do not know very well but if you have some special days and you did not get anything maybe you will be sad and we expect that do you think it would be better for society if all the money that was spent on gifts was given to help poor people yeah that would be perfect but I do not think it is possible but that will be really good yeah why why not possible because people still like like have a present or being remembered something like that but it is would be nice yeah do you think people in society should be made to give money to help other people yes why I do not know maybe I do not know where is the poor people or I do not know there is or not if the society or the government or the another community help me to find poor people probably I will yeah and other people will too is it get better for people to give money or their time to help other people I am sorry could you repeat it is it better for people to give money or their time to help other people yes it is better because when you need the help other.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["economy"],
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
            "reason": "'Dro' (drop). 'GI us' (gifts are?). 'money turned' (circulating)."
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
                "why_not_8": "Imprecise terms.",
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
        "id": 0, "sample_id": "pBrFbXB7EAg_q13",
        "video_id": "pBrFbXB7EAg",
        "part": 3,
        "question": "Help others?",
        "transcript": "People will help you and it will be Circle again and everybody will help each other do you think that we should be made or school children should be made to help other people yeah if you TR train at the young age it will be like a habit for you when a adult or older you will always help the people",
        "word_count": 59,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["habit", "train"],
            "grammar_structures_used": ["conditionals"]
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
            "reason": "'be Circle' (be a circle)."
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
                "why_not_8": "Minor error.",
                "why_not_6": "Good."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good. Band 7.",
        "grammar_reason": "Good. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "pBrFbXB7EAg_q14",
        "video_id": "pBrFbXB7EAg",
        "part": 1,
        "question": "Weekend activities?",
        "transcript": "At the weekend depends sometimes I like to relax and when I have a very stressful week but usually I like to meet some friends because I play football on the sometimes we have some competition also I play I do some kity but just like am not in competition and also with my friends we like to go to the pub at night or some restaurants or usually I like also to show to show some films new films it is very interesting what do you think you will do next weekend next weekend I will meet English students so because I need to practice English and she speak also French so I help him I I help her in French and she helped me in English so yes do you enjoy your weekends now more than you did when you were a child yes I think so because when I was child I think we are less stressful than now now in the work usually we are very very stressful we are very stress and at the weekend we can relax so it is U more enjoying how important is it for you to relax at the end of the week sorry how important is it for you to relax at the end of the week this is very important because all all week we are very stressful we are we have a I have a a work very stressful and at the end of the week I like to decompress to to relax.",
        "word_count": 242,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["stressful", "decompress", "competition"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'she speak' (speaks). 'we are very stress' (stressed). 'more enjoying' (enjoyable)."
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
        "grammar_reason": "Accurate mostly. Band 7.",
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
            if sample['vocabulary'] == 0:
                continue
            if sample['sample_id'] not in existing_ids:
                f.write(json.dumps(sample) + '\n')
                count += 1

    print(f"Append complete. Added {count} new samples. (Skipped duplicates/invalid).")

except Exception as e:
    print(f"Error writing to file: {e}")
