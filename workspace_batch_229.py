import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 229 ---
# Total Samples: 20
# Valid Samples: 17

scored_samples = [
    {
        "id": 0, "sample_id": "zaGEC7FTpIw_q05", "video_id": "zaGEC7FTpIw",
        "part": 3,
        "question": "Future shopping?",
        "transcript": "Reality like Google glasses for example using Google glasses for shopping you can just look at objects and just select the frame.",
        "word_count": 21,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["google glasses", "select the frame"],
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
                "why_not_9": "Short.",
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
        "id": 0, "sample_id": "k3iT-wc7KHc_q02",
        "video_id": "k3iT-wc7KHc",
        "part": 1,
        "question": "TV for children?",
        "transcript": "Wall it is quite big TV and another one smaller in in the kitchen is it healthy for children to watch TV it is quite important question I think it is healthy as long as there is the time TV time is limited to 1 hour and the program are age appropriate",
        "word_count": 51,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["age appropriate", "limited to"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'the program are' (programs are)."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Agreement error.",
                "why_not_7": "Good."
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
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "SUFDkC2IYLQ_q01",
        "video_id": "SUFDkC2IYLQ",
        "part": 1,
        "question": "Bills?",
        "transcript": "What type of bills do you usually need to pay I usually need to pay bills like rent utility including water electricity or gas other than that I also need to pay subscriptions for an example internet and streaming services Etc as well do you prefer paying your bills with cash or another method I usually prefer myself paying online it could be Via Mobile Banking or online banking because I think it is more convenient okay have you ever failed to make a payment for a bill no fortunately till now I have not failed to make any kinds of payments because I think if you are organized you can pay your bills and reduce any lapses can you think of anything that might reduce your regular bills yes by reducing your water usage or if you think about electricity efficient practice your utility bill can be reduced other than that you if you think about your subscription bills then you can also reduce them as well in my case I did them so.",
        "word_count": 169,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["utility bill", "mobile banking", "reduce any lapses", "efficient practice"],
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
        "id": 0, "sample_id": "SUFDkC2IYLQ_q02",
        "video_id": "SUFDkC2IYLQ",
        "part": 2,
        "question": "Traditional dish?",
        "transcript": "History so I would like to talk about this dish today I learned this recipe from my mother my mother is a wonderful cook and she cooks Bengali traditional foods and dishes very deliciously I learned this when I was in my hometown my mother taught me when it was some kinds of Festival I remember it was family gathering so I learned it as I mentioned earlier in my hometown which is alanga and I learned there when it was a family gathering and there were many members were present and when I went to my kitchen my mother was cooking traditional dish and she was cooking the exact same dish so I asked my mother if he could she could teach me how to make this traditional dish and my mother replied with an affirmative answer and there I learned this traditional dish how to cook from my mother so cooking this dish was really heart first of all this dish actually needs much more ingredient the ingredients from the for the sauce and the mustard which we prepare to marinate the fish everything together actually make this dish more aromatic actually the aroma of this dish fill the kitchen when my mother cooked and for my mother when I cooked the dish so at the end I would like to say that this dishes not only represents the Bengali culture or Heritage it also represents the beauty how it pro traditional dish is made it also represents the Bengali culture the tradition that we are maintaining for decades okay we have the Q card and the paper and the pen sure sir thank you thank you very much thank you could you describe the location and time frame when you first.",
        "word_count": 273,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["affirmative answer", "aromatic", "marinate", "cultural heritage"],
            "grammar_structures_used": ["complex_sentences", "past_tense"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'much more ingredient' (ingredients). 'members were present' (members present)."
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
                "why_not_9": "Minor slips.",
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
        "id": 0, "sample_id": "SUFDkC2IYLQ_q03",
        "video_id": "SUFDkC2IYLQ",
        "part": 2,
        "question": "Cooking challenge?",
        "transcript": "Learned to make it of course as far as I remember I first learned to make it in my hometown in the kitchen I remember it was family gathering and the kitchen was buzzling with crowd and there I asked my mother if she could teach me and my mother taught me were there any memorable experiences or challenges during The Learning Journey yes about challenge I remember when I was learning to make this traditional dish the challenge was you need to master the art of marinating the Hilla fish where each and every piece will absorb the same Master sauce harmoniously so this was hard to accomplish because as far as I know I was struggling to marinate the HRA fish but at the end of the day with the help help of my elders I was able to marinate the fish harmoniously have you ever shared this recipe or skill with someone else of course I shared this recipe with my friends with my relatives Bengali and non-bengali as well as far I have heard from them their experience was overall positive because this dish represents the cultural heritage and they was Flav gusted to know about the beauty and they were tremendously happy to make the unique flavor in their tradition as well",
        "word_count": 213,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["master the art", "harmoniously", "buzzling", "cultural heritage"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'buzzling' (bustling/buzzing). 'Flav gusted' (flabbergasted). 'they was' (were)."
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
                "why_not_9": "Agreement error.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "Malapropisms (buzzling, flav gusted).",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level despite slips. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "SUFDkC2IYLQ_q04",
        "video_id": "SUFDkC2IYLQ",
        "part": 3,
        "question": "Early cooking?",
        "transcript": "Sagacity their credibility and it also makes them to be responsible for themselves if they cook for themselves they can understand the traditional cooking Styles and dishes as well so overall I think every person every young Generations first people should understand how to cook and they should practice their cooking skills as well are there any benefits a person can gain from learning how to cook at an early age I think cooking from very early age Fosters the sense of creativity it also improves the person's overall performance and as I mentioned earlier sagd and credibility other than that I think cooking from an early age can make a person's aware about a balanced diet can she he or she can understand the benefit of food can understand the traditional dish and how to make them it is a valuable skill as well so I think cooking from an early age is essential for everyone in your opinion how does the popularity of fast food impact the cooking habits of the younger generation I think nowadays as you can see the popularity of fast food are increasing so I think this has a negative impact on the younger generation because particularly I think that as far as they want to cook for themselves or for their family easy packaging fast foods are decreasing the motivation because they can get it so easily so I think it has an negative impact and the fast FS are easy to get and they are decreasing the overall motivation of the younger generation what measures can be taken to encourage young people to cook more and rely Less on prepackaged or fast food in my perspective I think to encourage young people to cook more and rely Less on prepackaged food educational initiatives.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["sagacity", "credibility", "fosters creativity", "educational initiatives"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Sagacity' (unusual). 'sagd' (?). 'fast food are increasing' (is)."
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "high",
            "flexibility": "sustained",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Agreement errors.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "Word choice precision.",
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
        "id": 0, "sample_id": "lvF8q44170Q_q01",
        "video_id": "lvF8q44170Q",
        "part": 1,
        "question": "Mobile phones?",
        "transcript": "Let us start off by talking about mobile phones how often do you use your mobile phone every day I cannot live without my mobile phone I think I am addicted to it at this point as soon as I wake up I have to check my phone before I go to bed I have to check my phone cannot go anywhere without the phone what are your favorite apps on your phone Instagram insta shop which is food delivering our website Amazon I think that is about it very basic apps Google maps of course yeah do you think it is a nuisance if people use their mobile phone on public transport no I do not agree with that I I think it is just a way to keep yourself engaged somehow somebody would would like to read a book or the other person might want to hear music or just text whatever so I I do not think it is it is I think it is completely normal now let.",
        "word_count": 169,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["addicted to", "nuisance", "keep yourself engaged"],
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
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "lvF8q44170Q_q02",
        "video_id": "lvF8q44170Q",
        "part": 1,
        "question": "Outdoors?",
        "transcript": "You like outdoor activities I like being outdoors so even if it is just walking I do enjoy it so anything related to Outdoors I am I what outdoor activities did you like when you were a child to be honest I did not I was not into sports as a child I think the only activity I can think of is playing with my friends running around or cycling because my dad tried to teach me how to cycle I think that is the only outdoor activity I had I did as a child.",
        "word_count": 94,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["not into sports"],
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
        "id": 0, "sample_id": "lvF8q44170Q_q04",
        "video_id": "lvF8q44170Q",
        "part": 2,
        "question": "House vs Apt?",
        "transcript": "Description thanks very much and let us get back to the video to be fair I grew up in a Countryside so the houses that is popular in on the countryside are Mansions or willas because the families they tend to live together but if you go to the bigger cities the apartments are more common so everybody has their own apartment the parents are separated the kids are separated so they like to have their own place wherein where I am from we we we like to stay together I think what are the advantages of living in a house compared to an apartment well in an apartment I think it is very congested in a sense you do not have a backyard or you do not have a place to just relax and be by yourself wherein if you are living in in a house the chances are you would have a backyard you would have a Terrace you can just walk outside have a pet it is it is very hard to have a pet in an apartment I believe so I think the house I would I would I would probably live in a house if I get a choice do you think that it is better to buy a property or rent a property I personally think it is better to buy a property from my personal experience because I bought a property I feel like if you have a property if you buy a property you are investing somewhere rather than just giving the money to the landlords every month you would pay certain amount from your pocket which goes towards the mortgage or whatever the loans by the end of 5 years or 10.",
        "word_count": 285,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["congested", "mortgage", "investing", "landlords"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'houses that is popular' (are). 'willas' (villas)."
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
                "why_not_9": "Agreement error.",
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
        "grammar_reason": "Error free mostly. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "nFJ-CKIpIGM_q04",
        "video_id": "nFJ-CKIpIGM",
        "part": 3,
        "question": "Corporate punishment?",
        "transcript": "To be punished more their head serious i need to be punished more so they are going to be more scary about consequences at least but i think like especially in korea even they need to put more taxes for them i know that a lot of big companies they do not pay a lot for lightning like this stuff electricity and you know that electricity increase is really expensive right and those companies may be so a little little and like normal people they pay a lot if they will over use like something like 300 kilowatt or something like this right and that is the main point if they will charge that big companies properly then they are not going to be any problem with the electricity in korea or any other country all right perfect and do you think should big companies donate more money to charities yeah i think they need to stop robbing other people and then they do not need to give it to charity but yeah that is this good i i really think that they take more from people so if they will just stop taking from people they can literally do nothing and without any charity because all this charity thing looks actually so fake for me personally but still if they are still going to do the same as they are doing right now yeah sure give fit for charity give it to poor people for children a lot of old people need that so maybe yes you said it seems fake could you elaborate yeah it seems like every time a big company wants to look better they are doing charity because you know if you will help a small child that is sick with something you are a hero.",
        "word_count": 298,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["consequences", "robbing", "charity"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
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
            "reason": "'more scary about' (scared of/worried about). 'lightning' (lighting)."
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
                "why_not_7": "Good."
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
    },
    {
        "id": 0, "sample_id": "nFJ-CKIpIGM_q05",
        "video_id": "nFJ-CKIpIGM",
        "part": 3,
        "question": "Working for big company?",
        "transcript": "And the reality is the expenses that child needs it is so nothing for the company so they are doing it just to cover their problems and i know that a lot of companies are doing actually that they are covering their bad parts with this small charities give that to million people and then it is going to be like wow you are giving this to one small child you are helping this child that is really good for the child and that is great I am not telling that it is bad but it is still nothing for the company and they just like oh but we helped this one child like few years ago you know that so it is just not enough what they do okay and what are some of the good things about working for a big company good things stability you mostly going there you start working and you are working there until you are over right you always know how much money you are going to get tomorrow what you are going to do in 10 years and you can just live your life very in a standard way you know how much you can spend you know where you can go you know to foreign countries you know overseas you know just you are stable you are okay okay yeah are there any any disadvantages for employees if they are working for a big company the same you are to stay like you are too standard you are stable but you are you you know that you are not going to be anything more you know that if you have money to go to i do not k.",
        "word_count": 296,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["stability", "overseas", "standard way"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["phrasing_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'covering their bad parts' (hiding their faults?). 'live your life very in a standard way' (live a standard life)."
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
        "vocab_reason": "Good. Band 7.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q03",
        "video_id": "Ut_jyNrnlYE",
        "part": 1,
        "question": "Puzzles?",
        "transcript": "Actually I am not a kind of person who is interested in playing puzzle. So and when I was a charge I I did not often play the puzzle.",
        "word_count": 29,
        "analysis_metadata": {
            "grammar_error_patterns": ["articles", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'when I was a charge' (child). 'playing puzzle' (puzzles)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Errors.",
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
        "id": 0, "sample_id": "Ut_jyNrnlYE_q04",
        "video_id": "Ut_jyNrnlYE",
        "part": 1,
        "question": "Word vs Number?",
        "transcript": "In my opinion playing puzzle is tough. either the number or the number or the letter. So I think I do not quite like it and it is sometimes difficult to tell whether it is the preferences for me.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["phrasing_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'whether it is the preferences for me' (whether I prefer it)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Phrasing errors.",
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
        "grammar_reason": "Phrasing errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q05",
        "video_id": "Ut_jyNrnlYE",
        "part": 1,
        "question": "When?",
        "transcript": "Maybe when I am on a trip. I do not have much to do. So to maybe like to for entertainment I will do the puzzle.",
        "word_count": 26,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["entertainment"],
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
                "why_not_7": "Too short/simple.",
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
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q06",
        "video_id": "Ut_jyNrnlYE",
        "part": 1,
        "question": "Good for people?",
        "transcript": "I think it is good because it helps them like to memorize better and sometimes they can entertain themselves.",
        "word_count": 18,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["memorize better", "entertain themselves"],
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
                "why_not_7": "Short.",
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
        "vocab_reason": "Good. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Ut_jyNrnlYE_q07",
        "video_id": "Ut_jyNrnlYE",
        "part": 1,
        "question": "Weather?",
        "transcript": "I live in the city now so it is quite cold and a little bit rain.",
        "word_count": 16,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["form_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'a little bit rain' (rainy / of rain)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Errors.",
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
        "id": 0, "sample_id": "Ut_jyNrnlYE_q08",
        "video_id": "Ut_jyNrnlYE",
        "part": 1,
        "question": "Preference?",
        "transcript": "In my opinion, the rainy weather is my preferences and I think when it is rain I feel.",
        "word_count": 17,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form", "agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["form_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'is my preferences' (preference). 'when it is rain' (raining)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Errors.",
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
