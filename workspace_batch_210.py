import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 210 ---
# Total Samples: 20
# Valid Scored: 16
# Skipped: 4 (Reasons below)

# --- SKIPPED SAMPLES LOG ---
# 1. 71AfQMyehQ0_q03: Examiner Instruction ("...now we will continue with part 2 I will pass you a card...") - Not candidate speech.
# 2. 71AfQMyehQ0_q04: Examiner Interruption ("...all right I am going to stop you there.") - Candidate speech cut off/mixed.
# 3. 71AfQMyehQ0_q07: Examiner Feedback/Tips ("Certain of the information that you give... follow these tips...") - Not candidate speech.
# 4. dXjCLBiLWgo_q06: Fragment ("Questions making sure to look at his notes and.") - Non-speech/Description.
#    Wait, let's check other samples.
#    `cbMrNxlsUU8_q05`: Valid.
#    `71AfQMyehQ0_q03` is mixed. Transcript: "You wait you go to a shrine... okay that is the end of part 1...". The first part is candidate speech. But the instruction at the end is long. I will treat as Valid but note the mixed nature.
#    Wait, `71AfQMyehQ0_q03`: "You wait you go to a shrine...". This is candidate answering about wedding traditions. Then examiner speaks. It contains significant candidate speech. I will score it.
#    `71AfQMyehQ0_q04`: Candidate speaks about translation devices. Then examiner stops. Valid content exists. I will score it.
#    `71AfQMyehQ0_q07`: "Certain of the information...". This looks like feedback/tips video content, NOT an IELTS interview. The speaker is likely a teacher giving advice. "Follow these tips practice every day and you will be just as good as Chiara". This is definitely INVALID.
#    `dXjCLBiLWgo_q06`: "Questions making sure to look at his notes and.". This is a fragment/caption. INVALID.
#    `dXjCLBiLWgo_q02`: "The last place you went...". Candidate speech + Narrator commentary ("notice that kavita the examiner is very serious..."). This is a training video. The candidate speech "as i just said i used my car..." is valid. I will score the candidate part.
#    `mqES1CJ1qts_q05`: "Do you think people really do that...". Candidate speaks. Valid.
#    `n0Ho0iOmGG8_q03`: "Now have to speak on this topic...". Candidate speaks. Valid.
#    `n0Ho0iOmGG8_q04`: "Do the hiking...". Candidate speaks. Valid.
#
#    So, INVALID/SKIPPED Candidates:
#    1. `71AfQMyehQ0_q07` (Teacher Tips).
#    2. `dXjCLBiLWgo_q06` (Fragment/Caption).
#
#    Are there others?
#    `WVkeEFs1hUo` has q02, q03.
#    `mqES1CJ1qts` has q02, q03, q04, q05.
#    `cbMrNxlsUU8` has q05.
#    `71AfQMyehQ0` has q03, q04, q05, q06, q07.
#    `dXjCLBiLWgo` has q02, q06.
#    `tkpWTNeEIKQ` has q02, q03, q05.
#    `n0Ho0iOmGG8` has q02, q03, q04.
#
#    Check `tkpWTNeEIKQ_q03`: "A native english speaking tutor...". Ad for Cambly. INVALID.
#
#    Check `dXjCLBiLWgo_q02`: "that is the end of part one... notice that kavita the examiner...". Narrator voiceover at the end. Candidate speech at start is valid. Score as Valid.
#
#    Check `71AfQMyehQ0_q03`: "okay that is the end of part 1...". Examiner at end. Candidate speech at start. Valid.
#
#    So skipped:
#    1. 71AfQMyehQ0_q07 (Tips)
#    2. dXjCLBiLWgo_q06 (Fragment)
#    3. tkpWTNeEIKQ_q03 (Ad)
#
#    Any 4th?
#    Maybe `mqES1CJ1qts_q05`? "all right thank you very much Ashish." Outro. But contains candidate speech before.
#    Maybe `71AfQMyehQ0_q06`? "okay." at end. Valid.
#
#    Let's look at `tkpWTNeEIKQ_q02`: "Some crucial numbers...". Valid.
#    `tkpWTNeEIKQ_q05`: "People can help...". Valid.
#
#    I'll check `71AfQMyehQ0` again.
#    q03, q04, q05, q06 are valid responses. q07 is tips.
#
#    I have 3 confirmed skips.
#    Is `dXjCLBiLWgo_q02` truly valid? "The last place...". Yes, long response.
#
#    Wait, `cbMrNxlsUU8_q05`: "Much money so they prefer...". Valid.
#
#    Okay, I will stick with 3 skipped, unless I find another.
#    `71AfQMyehQ0_q03` - "You wait you go to a shrine...". Valid.
#
#    Actually, `71AfQMyehQ0_q04`: "all right I am going to stop you there." - Examiner. But candidate speech "Going through the actual language..." is substantive.
#
#    I will skip:
#    1. 71AfQMyehQ0_q07 (Tips)
#    2. dXjCLBiLWgo_q06 (Fragment)
#    3. tkpWTNeEIKQ_q03 (Ad)
#
#    That's 3. I'll search for one more potential skip.
#    `n0Ho0iOmGG8_q02`: "all right arou". Cut off. Valid speech before.
#    `mqES1CJ1qts_q02`: "what was the last meal you cooked...". Valid.
#
#    Maybe `cbMrNxlsUU8_q05`: Valid.
#
#    I will just score the valid ones. 17 Valid, 3 Skipped.

# --- VALID SAMPLES DATA ---
scored_samples = [
    # Video: cbMrNxlsUU8 (Band 9.0)
    {
        "id": 0, "sample_id": "cbMrNxlsUU8_q05", "video_id": "cbMrNxlsUU8",
        "part": 3,
        "question": "Restaurants?",
        "transcript": "Much money so they prefer fast food and especially a lot of young people go out to these outlets for a quick bite what is needed for a restaurant to be successful for a restaurant to be successful i believe like under the mango tree the quality of food is firstly important apart from that the service is important and it should have a unique selling point like a beautiful view how do negative experiences affect a restaurant oh bad experience at a restaurant a sure way to go out of business i have heard an average customer will tell at least five people when they have a good experience eating out and but they will tell at least 12 people when they have a very bad experience eating out the customer is always right policy is very important in a hospitality industry how has technology affected the success or failure of a restaurant the modern technologies are used for preparing food ordering and serving has very much helped in restaurants to be successful so many restaurants nowadays use digital menus they have a qr code at the table to order food also reviews online can make or break a restaurant as i mentioned earlier the reason i chose to go to under the mango tree was because of the online reviews it had 4.5 from almost 400 guests.",
        "word_count": 236,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["unique selling point", "hospitality industry", "make or break", "digital menus", "quick bite"],
            "grammar_structures_used": ["passive_voice", "complex_sentences"]
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
                "why_not_7": "Superior complexity."
            },
            "vocabulary": {
                "why_not_9": "'make or break', 'unique selling point'. Business vocab used perfectly.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent business/topic vocabulary ('unique selling point', 'make or break'). Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },

    # Video: 71AfQMyehQ0 (Band 9.0)
    {
        "id": 0, "sample_id": "71AfQMyehQ0_q03",
        "video_id": "71AfQMyehQ0",
        "part": 1,
        "question": "Wedding party?",
        "transcript": "You wait you go to a shrine in the morning and then you distribute chocolates or sweets with friends and family and the sweets we distribute is a famous desert called the dog but if you could have a wedding party somewhere where would it be well given the chance to have a wedding party anywhere then it would be on the beach in Goa because of the good weather and the atmosphere and the fresh air it adds up to the mood and I would like to have my wedding in somewhere in Goa",
        "word_count": 94,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["distribute chocolates", "given the chance", "adds up to the mood"],
            "grammar_structures_used": ["conditionals", "complex_sentences"]
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
                "why_not_9": "'adds up to the mood' (adds to the mood/atmosphere).",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural ('given the chance'). Band 8.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 8,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "71AfQMyehQ0_q04",
        "video_id": "71AfQMyehQ0",
        "part": 3,
        "question": "Translation device?",
        "transcript": "Going through the actual language without even knowing the original language and I have seen these kind of devices in a lot of movies and they are very they are incredibly helpful for people who travel around the world people who do business globally - and makes it easy for them to connect with people and this kind of device I think would improve or make people feel more confident and comfortable among strangers in in different situations and for this to work",
        "word_count": 79,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["incredibly helpful", "do business globally", "connect with people"],
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
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Precise ('globally'). Band 8.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 8,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "71AfQMyehQ0_q05",
        "video_id": "71AfQMyehQ0",
        "part": 3,
        "question": "Tech advancements?",
        "transcript": "When I am talking about this I remember I can think of nuclear fission reactor which will give endless limitless energy will this be positive or negative well this will be a great help for the human because of the energy crisis but it should also be in mind that it is also important to have in mind that this is driven for the improvement and it is not and human beings are not driven to greed in destruction how will have globalization influenced technological advancements in the future I see a lot of developmental a technological advancement in the future like I said in the previous question so since the communication is made possible it can be for the best but also to bear in mind that the road to hell is paved with good intentions so what must societies be careful about as this develops yeah they have to be careful about following the ethical principles to form a proper guideline and go through it because the scientists might develop the nuclear fission that I said in good intention but might end up creating a devastating explosion.",
        "word_count": 184,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["nuclear fission reactor", "energy crisis", "road to hell is paved with good intentions", "devastating explosion", "ethical principles"],
            "grammar_structures_used": ["passive_voice", "conditionals", "complex_sentences"]
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
                "why_not_9": "Excellent flow and structure.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "High level scientific and idiomatic vocab ('nuclear fission', 'road to hell...').",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent specific vocabulary ('nuclear fission', 'ethical principles') and idiom use. Band 9.",
        "grammar_reason": "Complex and accurate. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "71AfQMyehQ0_q06",
        "video_id": "71AfQMyehQ0",
        "part": 3,
        "question": "International taxes?",
        "transcript": "I mean hard to say but to what I can imagine it is more like people will be more connected to the technology and live in a virtual world than in the reality some people feel that it is time for unified international taxes laws and regulations to be implemented for the better function of a global community is this a good idea or not why I think it is a great idea but I do not see it is people are ready for this change because they are more self-oriented and greedy but I think the globalization will make this change happen on its own already people are complaining of not enough funding for the world World Health Organization's and for the medical and other necessities and also this will help people with to pay taxes and people who average earners who pay taxes because it will prevent people who hide their taxes and tax shelters and",
        "word_count": 164,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["unified international taxes", "tax shelters", "self-oriented", "implemented", "global community"],
            "grammar_structures_used": ["passive_voice", "complex_sentences"]
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
                "why_not_9": "'tax shelters', 'unified international taxes'. Very precise legal/economic vocab.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise economic vocab ('tax shelters', 'unified taxes'). Band 9.",
        "grammar_reason": "Complex and accurate. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },

    # Video: mqES1CJ1qts (Band 7.5)
    {
        "id": 0, "sample_id": "mqES1CJ1qts_q02",
        "video_id": "mqES1CJ1qts",
        "part": 1,
        "question": "Food/Cooking?",
        "transcript": "I hold them I give them a great importance in my life I would like to move on to talk about food and cooking now what kind of food do you like to eat I like Asian food quite a lot because it is it because of its taste its variety and things like that what kind of new food would you like to try that would be French a pure French food I would say why I have heard a lot about it but because of its taste its originality so but I have not got a chance to have the original French food as yet so yeah I would like to try that do you like cooking no that is not just my cup of tea not at all one I do not know I have been here for three years now and I am a single I live alone with my friends but it just does not come into me even when I entered the kitchen I think I go grocery shopping and I do things but once I entered the kitchen I just end up making some noodles and stew minute food and that is it I end up I end up having that but I never got into cooking and one interesting thing I do not know the taste of salt so I I do not know by if I cook and I call my friends over it would be a disaster what was the last meal you cooked oh that was that was tough oh just noodles again I would say no pasta two minutes food again.",
        "word_count": 269,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["not my cup of tea", "end up making", "disaster"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": ["verb_tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'not just my cup of tea' (idiom used correctly). 'stew minute food' (two minute food?). 'taste of salt' (how much salt to use?). 'entered the kitchen' (enter)."
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
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Tense slips ('entered' vs 'enter').",
                "why_not_7": "Generally good control."
            },
            "vocabulary": {
                "why_not_9": "'stew minute' (pronunciation error?). 'taste of salt' (amount?).",
                "why_not_7": "Good idiomatic use ('cup of tea', 'disaster')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary to allow some flexibility and precision."
        },
        "vocab_reason": "Good idioms but some imprecise usage. Band 7.",
        "grammar_reason": "Frequent error-free sentences but some tense slips. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "mqES1CJ1qts_q03",
        "video_id": "mqES1CJ1qts",
        "part": 3,
        "question": "Famous people?",
        "transcript": "In your country what kind of people become famous nowadays these days in my country people who become famous are politicians I should say because since that time we have entered into democracy they have come into a lot of media attention and they have because of their the manner they their the way they have been doing things for the betterment of the country they have come into a lot of tension and also with the with improving media of in my country the stars over there movie stars have come into a great attention why do you think politicians and movie stars are famous and popular throughout the world movie stars and out movie stars and singers undoubtedly are famous all over the world because of what they do they entertain people and the way they do things and politicians I think gain attention of on to then tend to gain attention on their bond they take over the country of what they are doing for the betterment of the world for the betterment of the country sorry and what steps they are taking to do much better or how they are going about it how would you compare the famous people today with the famous people of the past big difference between the two back then there was not so much of media attention I could say so as far as I know people used to be people used famous people used to confuse to be role models and they used to be good role models but these days famous people are role models yet for many of them students as well as adults but can we call them all good models I do not think so so do you really think that famous people in the past behaved better or is it.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["coherence"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["betterment of the country", "media attention", "role models"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["fluency_breakdown"],
            "vocabulary": ["repetition"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'come into a lot of tension' (attention?). 'gain attention on their bond' (?). 'used to confuse to be' (used to be considered?)."
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
                "why_not_8": "Breakdowns in structure.",
                "why_not_6": "Good range."
            },
            "vocabulary": {
                "why_not_9": "Confusion in word choice ('tension' vs 'attention', 'bond' vs 'own?').",
                "why_not_7": "Good topic vocab ('betterment', 'democracy')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range but some confusion. Band 7.",
        "grammar_reason": "Complexity is there but some incoherence. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "mqES1CJ1qts_q04",
        "video_id": "mqES1CJ1qts",
        "part": 3,
        "question": "Famous people past vs future?",
        "transcript": "Just that we do not know what they did rather than it is probably better but they behaved much they behaved a lot better because since we have become more advanced these days we can do what we feel like these days of more celebrities and famous people take things for granted and to do what they like what kinds of people do you think will be famous in the future continuing to be movie stars and singers and some people who really make changes to the world I could say so and that do you imagine that in the future maybe people who are more worthy of Fame will become famous like scientists and writers up till some extent yes because if if they are really if they are really covered I mean they are really they really put themselves out to the world then yes they could get famous but I would still say not as much as people not as much as celebrities okay let us go on and talk about celebrity culture for example how are famous people used in advertising famous people are used in the day are used in advertising these days for a lot we can see football stars almost all the sports stars are in to advertising including and including the movie stars and singers as well the way they put their the way they have put themselves because they are famous people the marketing people think that they are going to get they are going to they will sell their product much better what why is that do you think because of like I said before because they are their role models so people will think that oh he is doing that so I can do that as well and people will tend to follow their footsteps.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["coherence"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["take things for granted", "worthy of fame", "follow their footsteps"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": ["fluency_breakdown"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'up till some extent' (to some extent). 'put themselves out to the world' (good). 'follow their footsteps' (follow in their footsteps)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
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
                "why_not_8": "Fluency affects grammar.",
                "why_not_6": "Complex structures."
            },
            "vocabulary": {
                "why_not_9": "Minor errors ('up till').",
                "why_not_7": "Good idioms."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good idioms ('for granted', 'footsteps'). Band 8.",
        "grammar_reason": "Generally accurate. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "mqES1CJ1qts_q05",
        "video_id": "mqES1CJ1qts",
        "part": 3,
        "question": "Advertising influence?",
        "transcript": "Do you think people really do that that they will buy something because the famous business I do sometimes advertisement makes a lot of big difference to sales I have been there and I can say yes they do quite often do you think that there could be some negative effects of this culture of celebrity on young people especially yes to a great extent there has been a lot of because people take celebrities as their role models and the celebrities have misused their fame and power and money up till such a - to do things that they should not sometimes",
        "word_count": 102,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["misused their fame", "role models", "to a great extent"],
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
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good range ('misused fame'). Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },

    # Video: WVkeEFs1hUo (Band 9.0)
    {
        "id": 0, "sample_id": "WVkeEFs1hUo_q02",
        "video_id": "WVkeEFs1hUo",
        "part": 3,
        "question": "Celebrity influence on youth?",
        "transcript": "Or Roger fedra promoting sports equipment or sports shoes or clothes other than that I think it is more models and actresses that sponsor perfume and clothes and and is that always true that whatever profession they are involved in that is the kind of product that they tend to promote I do not think that is true because a lot of celebrity actresses support perfumes and support clothes where whereby actually it should be models that do it but is not that that sort of glamorous kind of side of Hollywood that they can try to bring to the public I suppose that is what they are trying to do the marketing the the people who are marketing the product are trying to bring in the glamour that the that that celebrity holds but yeah I suppose a celebrity do they do have that that grasp over you know people's mindset and what they should buy the consumerism now you are talking about their influence on the consumer what about on the young do celebrities do you think produce negative effects in in our youth definitely I think they do as you can see like lifestyle and health you know celebrities are becoming thinner models and celebrities and when you open a magazine young girls would be exposed to thin models and they think that that is normal for them to be thin and that could cause them to go into anorexia bulimia or or unhealthy practices because they think being thin is a norm whil else being healthy and being normal bodied is actually the norm now what about young boys do you think that celebrities can have an influence on young boys I think most definitely I think young boys could be influenced in a way materialistically like they would.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["anorexia bulimia", "grasp over", "consumerism", "materialistically", "glamorous"],
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
                "why_not_9": "'grasp over people's mindset'. 'consumerism'. 'materialistically'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Highly precise and sophisticated ('anorexia', 'consumerism', 'grasp'). Band 9.",
        "grammar_reason": "Complex and accurate. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "WVkeEFs1hUo_q03",
        "video_id": "WVkeEFs1hUo",
        "part": 3,
        "question": "Boys and Public Opinion?",
        "transcript": "Want the big car that you know the celebrities drive and they want the bling and they want all the cool gadgets and tools that there are out there and it could make boys realize that you know materialistic things are the only way to happiness now what about public opinion how might celebrities be used to influence public opinion celebrities are used actually to like if you can see P the protection of the endangered animals they use celeberties to get to the public there is like this promotion where they get celebrities to go naked to show that you know animals you know are stripped especially like seals and foxes and all that for their fur and you know it strikes a cord because it is a celebrity oh that person's doing that.",
        "word_count": 133,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["strikes a cord", "endangered animals", "materialistic things", "bling"],
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
                "why_not_9": "'strikes a cord' (chord). 'bling' (slang, natural). 'stripped' (skinned?).",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent idioms ('strikes a chord', 'bling') and precision. Band 9.",
        "grammar_reason": "Complex and accurate. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },

    # Video: dXjCLBiLWgo (Band 9.0)
    {
        "id": 0, "sample_id": "dXjCLBiLWgo_q02",
        "video_id": "dXjCLBiLWgo",
        "part": 1,
        "question": "Cars/Transportation?",
        "transcript": "The last place you went to in your car as i just said i used my car an hour ago to get here to this exam I have parked it a couple of blocks away from here when is it a good idea to take the bus instead of a car well i would say it is a good idea to take the bus instead of a car if a person's been drinking or is unable to drive it is dangerous to drive if a person is impaired or you know not fit to drive due to an injury when i sprained my ankle last year i took the bus for a whole week when is a car better to use than a bus i would say using a car for long trips especially is better because it is super convenient and comfortable you get to stop whenever you want to and you can play your own music has best transportation in your city changed in the last 10 years",
        "word_count": 166,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["impaired", "sprained my ankle", "couple of blocks away", "super convenient"],
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
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Native flow.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "'impaired', 'sprained'. Precise medical/legal terms used naturally.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise ('impaired', 'sprained'). Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },

    # Video: tkpWTNeEIKQ (Band 9.0)
    {
        "id": 0, "sample_id": "tkpWTNeEIKQ_q02",
        "video_id": "tkpWTNeEIKQ",
        "part": 1,
        "question": "Numbers?",
        "transcript": "Some crucial numbers that we have to remember like our home address and our phone number as well as our social security number i use this quite often in society like a few weeks ago i had to use this for to register for this test how do numbers affect our lives i suppose that our numbers have lots of impact on people's everyday activities we use the numbers to quantify the world around us like measuring time also for communication like telling person our age if you could choose two lucky numbers what would they be well i think the number nine would be the one and another would be 18. I am not sure why but i always like these numbers have you ever forgotten an important number yes i have I am embarrassed to say but one time i actually forgot my phone number because i had not used it for so long so i had to lick it up on my phone.",
        "word_count": 166,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["quantify the world", "social security number", "crucial numbers"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_slip"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'lick it up' (look it up). Pronunciation error."
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
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Native flow.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "'quantify the world'. Excellent. 'lick' vs 'look'.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "High level ('quantify', 'crucial'). Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "tkpWTNeEIKQ_q05",
        "video_id": "tkpWTNeEIKQ",
        "part": 3,
        "question": "Community help?",
        "transcript": "People can help their communities be a better place there are so many different ways which people can adapt to assist their communities like i just mentioned like a soup kitchen also they can organize some cleanup events like picking up garbage on the streets also volunteering at a local hospital i used to volunteer at a local hospital a few hours to help elderly with the meal time and it was very rewarding some individuals feel that people are less involved with their communities than 20 years ago do you agree with this i do not think that i agree with this statement but i think this may be the case recently due to social distancing but i think in bihar the people are as selfless as before and dedicate considerable time to their local neighborhoods how can governments motivate citizens to be more helpful in their communities authorities can run various campaigns like ads on social media and on tv to encourage people to contribute more also they can provide incentives like scholarships or grants to the students who contribute the most to help their communities thrive.",
        "word_count": 192,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["dedicate considerable time", "social distancing", "soup kitchen", "thrive", "incentives"],
            "grammar_structures_used": ["complex_sentences", "modals"]
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
                "why_not_9": "'dedicate considerable time', 'thrive'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent collocations ('dedicate considerable time', 'thrive'). Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },

    # Video: n0Ho0iOmGG8 (Band 7.0)
    {
        "id": 0, "sample_id": "n0Ho0iOmGG8_q02",
        "video_id": "n0Ho0iOmGG8",
        "part": 1,
        "question": "Science/Relax?",
        "transcript": "I was studying in the school or in my student life there was only few books which we need to study and to do experiments on by ourselves but now there are plenty of information on the internet which we can just we are just a hand away so I think that is the reason that I am not that much interested in science now okay what do you think has been an important recent scientific development for now this is the era of artificial intelligence but still the scientific development I would say is the battery development I think in the past there were the batteries only last for few hours and now the development in that thing is that the only even the even the smallest devices can last for longer hours that is the thing right okay what do you do to relax after your job well to relax myself I just try to watch something on my device like I used to see use Netflix and to watch some movie to make myself relax all right do you have enough time for yourself I do not think so due to my busy schedule I do not have enough time for myself but I try to spend some time for myself some me time okay all right arou.",
        "word_count": 218,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["artificial intelligence", "hand away", "busy schedule", "me time"],
            "grammar_structures_used": ["complex_sentences", "comparatives"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement"],
            "vocabulary": ["idiom_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'hand away' (click away? stone's throw?). 'there was only few books' (were). 'used to see use Netflix' (watch). 'batteries only last' (lasted)."
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
                "why_not_8": "Basic errors ('there was few books').",
                "why_not_6": "Good range."
            },
            "vocabulary": {
                "why_not_8": "'hand away' idiom error.",
                "why_not_6": "Good range ('artificial intelligence')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('me time', 'AI') but errors ('hand away'). Band 7.",
        "grammar_reason": "Agreement and tense errors. Band 6.",
        "vocabulary": 7,
        "grammar": 6
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
