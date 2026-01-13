import json

output_file = "jules_scored_output_151-200.jsonl"

samples = [
    {
        "id": 19,
        "sample_id": "iMPGHuKklD8_q14",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "How did you celebrate your last birthday?",
        "transcript": "At my last birthday, I, I cut a cake and, and donated foods in poor children. Okay.",
        "word_count": 18,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition_error", "phrase_structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "wrong",
            "vocab_evidence": ["donated foods"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["wrong_preposition"],
            "vocabulary": ["wrong_collocation"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'donated foods in poor children' (donated food to poor children). 'At my last birthday' (On)."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "frequent"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Basic errors 'in poor children'.",
                "why_not_4": "Meaning clear."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts basic sentences.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 5.",
        "grammar_reason": "Observation: 'in poor children' (error). Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 20,
        "sample_id": "iMPGHuKklD8_q15",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "What kind of birthday gifts do you like to receive?",
        "transcript": "I like to receive expensive gifts and that gift who can help me in future. Okay.",
        "word_count": 17,
        "analysis_metadata": {
            "grammar_error_patterns": ["relative_pronoun", "article_error"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["expensive gifts"],
            "grammar_structures_used": ["relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["wrong_relative_pronoun"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "adequate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'that gift who' (which/that). 'in future' (in the future)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Relative pronoun error 'who' for object.",
                "why_not_4": "Structure attempted."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts complex sentences.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 5.",
        "grammar_reason": "Observation: 'gift who' (error). Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 21,
        "sample_id": "iMPGHuKklD8_q17",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "Is it more difficult for old people to accept new technologies?",
        "transcript": "I believe that people have very difficulty to, to adapt new changes. they find very difficult. so I, I think we have to, help older people to, Adapt this new technology. Okay.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrase_structure", "word_class"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "wrong",
            "vocab_evidence": ["adapt new changes"],
            "grammar_structures_used": ["complex_sentence"]
        },
        "micro_flaws": {
            "grammar": ["wrong_word_form"],
            "vocabulary": ["wrong_collocation"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'have very difficulty' (have great difficulty). 'find very difficult' (find it very difficult)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "frequent"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Systematic errors 'have very difficulty'.",
                "why_not_4": "Communication effective."
            },
            "vocabulary": {
                "why_not_6": "'adapt new changes' (adapt to).",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts complex sentences but accuracy is inconsistent.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: 'adapt'. Impact: OK. Errors present. Justification: Band 5.",
        "grammar_reason": "Observation: 'have very difficulty' (error). Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 22,
        "sample_id": "iMPGHuKklD8_q19",
        "video_id": "iMPGHuKklD8",
        "part": 1,
        "question": "Related to what?",
        "transcript": "To. To make their product popular. that is why they. And, to make learn new technologies to the older people. is not it? Yes.",
        "word_count": 23,
        "analysis_metadata": {
            "grammar_error_patterns": ["fragment", "verb_structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["make learn"],
            "grammar_structures_used": ["fragment"]
        },
        "micro_flaws": {
            "grammar": ["fragmented_speech"],
            "vocabulary": ["wrong_causative"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'make learn' (teach / make them learn). Fragmented speech."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "low",
            "flexibility": "limited",
            "error_density": "frequent"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Fragments.",
                "why_not_4": "Meaning inferred."
            },
            "vocabulary": {
                "why_not_6": "Basic.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts sentences.",
            "vocabulary_band": 5,
            "vocabulary_text": "Minimally adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 5.",
        "grammar_reason": "Observation: Fragments. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 23,
        "sample_id": "jJDD0bhXAOQ_q02",
        "video_id": "jJDD0bhXAOQ",
        "part": 1,
        "question": "General questions about money and work",
        "transcript": "Buy anything with card okay and do you ever save money to buy special things and well i think it is it is not the people cannot cannot save money now because anything is very are very expensive and people cannot save good money i think my idea in my opinion my idea i think and would you ever take a job which had low pay job video pay yes i think i think the the job in a in airlines have paid low pay i do not i do not idea about this question okay so would winning a lot of money make a big difference in your life for example when you work a lot or or you should vote any time you can you can give good money or you can save money but now you need all of the time and the people work and work and work but cannot make big money i think okay and.",
        "word_count": 145,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure_breakdown", "agreement", "negation"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "wrong",
            "vocab_evidence": ["save good money", "make big money"],
            "grammar_structures_used": ["simple_sentence", "coordination"]
        },
        "micro_flaws": {
            "grammar": ["incoherent_structure"],
            "vocabulary": ["limited_range"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'anything is very are very expensive' (everything is). 'I do not idea' (I have no idea). 'paid low pay' (pays poorly)."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "low",
            "flexibility": "limited",
            "error_density": "frequent"
        },
        "discourse_metrics": {
            "length_appropriateness": "long",
            "redundancy": "high",
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Errors cause strain. 'I do not idea'.",
                "why_not_3": "Can convey basic meaning."
            },
            "vocabulary": {
                "why_not_5": "Very limited, repetitive.",
                "why_not_3": "Can talk about familiar topics."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Errors predominate.",
            "vocabulary_band": 4,
            "vocabulary_text": "Basic."
        },
        "vocab_reason": "Observation: 'good money', 'big money'. Impact: Repetitive. Justification: Band 4.",
        "grammar_reason": "Observation: 'I do not idea' (error). Justification: Band 4.",
        "vocabulary": 4,
        "grammar": 4
    },
    {
        "id": 24,
        "sample_id": "jJDD0bhXAOQ_q03",
        "video_id": "jJDD0bhXAOQ",
        "part": 1,
        "question": "Sports impact on children",
        "transcript": "Sports because then the child go and go younger and go and go then go older and the health is better",
        "word_count": 20,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition", "coherence"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["health is better"],
            "grammar_structures_used": ["coordination"]
        },
        "micro_flaws": {
            "grammar": ["incoherent_repetition"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "adequate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Extreme repetition 'go and go younger and go and go'."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "low",
            "flexibility": "limited",
            "error_density": "frequent"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "high",
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Incoherent repetition.",
                "why_not_3": "Meaning barely emerges."
            },
            "vocabulary": {
                "why_not_5": "Basic.",
                "why_not_3": "Basic."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Errors predominate.",
            "vocabulary_band": 4,
            "vocabulary_text": "Basic."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 4.",
        "grammar_reason": "Observation: Repetition. Justification: Band 4.",
        "vocabulary": 4,
        "grammar": 4
    },
    {
        "id": 25,
        "sample_id": "jJDD0bhXAOQ_q04",
        "video_id": "jJDD0bhXAOQ",
        "part": 1,
        "question": "Learning and updating knowledge",
        "transcript": "You started your study and you learned learn about any article you can describe anything but when you can you do not you do not update and you do not you do not know about a new article you cannot explain and you cannot describe anything",
        "word_count": 43,
        "analysis_metadata": {
            "grammar_error_patterns": ["coherence", "repetition"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["update", "explain", "describe"],
            "grammar_structures_used": ["complex_sentence_but"]
        },
        "micro_flaws": {
            "grammar": ["stuttering", "coherence_break"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "adequate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Coherence breakdown. Repetitive negatives."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "low",
            "flexibility": "limited",
            "error_density": "frequent"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "high",
            "development_depth": "shallow"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Coherence issues.",
                "why_not_3": "Meaning clear enough."
            },
            "vocabulary": {
                "why_not_5": "Basic.",
                "why_not_3": "Basic."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Errors predominate.",
            "vocabulary_band": 4,
            "vocabulary_text": "Basic."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 4.",
        "grammar_reason": "Observation: Breakdown. Justification: Band 4.",
        "vocabulary": 4,
        "grammar": 4
    },
    {
        "id": 26,
        "sample_id": "ROm_8Oeuj1Q_q02",
        "video_id": "ROm_8Oeuj1Q",
        "part": 1,
        "question": "Internet and website usage",
        "transcript": "My job is related to internet and my major is computer engineering when i come back home we watch tv most of the time online and i think all of our life is engaged with internet right and what is your favorite website google because whatever i want i can find it in google and it makes it easy to find whatever you want and whatever you want to know sometimes i think about the old days that we wanted to learn something we want to search something it was really hard but now it is really easy to search something on google right and do you think children should be allowed unsupervised access to the internet of course not i think parents should have extreme supervision on their children and their access to the internet and there are lots of softwares and that helps parents to do that for them and.",
        "word_count": 147,
        "analysis_metadata": {
            "grammar_error_patterns": ["article", "agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["computer engineering", "engaged with internet", "extreme supervision", "unsupervised access"],
            "grammar_structures_used": ["complex_sentence_because", "relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["article_error", "uncountable_plural"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'lots of softwares' (software). 'related to internet' (the internet). 'find it in google' (redundant it)."
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "high",
            "flexibility": "high",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "long",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Minor errors 'softwares'.",
                "why_not_6": "High complexity and flow."
            },
            "vocabulary": {
                "why_not_8": "'extreme supervision' is good, but 'engaged with internet' is slightly off.",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'extreme supervision'. Impact: Good. Justification: Band 7.",
        "grammar_reason": "Observation: 'softwares' (error). Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 27,
        "sample_id": "ROm_8Oeuj1Q_q05",
        "video_id": "ROm_8Oeuj1Q",
        "part": 1,
        "question": "Children and internet interest",
        "transcript": "Students it would become a combined with a computer game i think it is really becomes interesting for for students okay and how could we make children interested in things that they do not have on the internet i did not understand your question okay so how could we make children interested in things that they do not have that they will be probably interested in on the internet you are you mean it is not on the internet or they they do not have access so so how could you sort of take their attention off the internet to be interested in things i think it is really hard to get the children's attention off the internet because when I am in my 30s I am fully interested in internet young children is interested in it interested in it as well and i think it i we could not completely neglect internet and make their attention to something else we could have less internet besides other things",
        "word_count": 156,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["take their attention off", "neglect internet"],
            "grammar_structures_used": ["complex_sentence_because", "conditional"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_disagreement"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'it is really becomes' (it really becomes). 'young children is interested' (are). 'neglect internet' (the internet)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "long",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Agreement errors 'children is'.",
                "why_not_5": "Complex structures handled well."
            },
            "vocabulary": {
                "why_not_7": "'neglect' is good. Range is adequate.",
                "why_not_5": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'neglect'. Impact: Good. Justification: Band 6.",
        "grammar_reason": "Observation: 'children is' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 28,
        "sample_id": "DNNJy1g18p8_q02",
        "video_id": "DNNJy1g18p8",
        "part": 1,
        "question": "TV habits and preferences",
        "transcript": "And I prefer to actually spend my time on other things like reading books and watching movies on my laptop or cell phone okay and what is your favorite TV program or movie and why I am really keen on sport programs and I love to watch competitions especially soccer games and also boxing okay and are there any TV programs or shows you do not like watching and why reality shows are not that much fascinating to me H I believe that they are not real and they just want to f some things or persuade people that these are real shows so I am not into reality shows right and do you think you will watch more TV or fewer TV programs or shows in the future and why I anticipate that I will not actually watch more TV programs in future because I want to have a baby and I do not will not have time to actually to devote on TV channels and programs and I want to devot it to my baby okay and would you consider watching movies or TV programs on your phone or laptop sometimes when I do not have access to TV especially when I am on a trip and something that and a TV program is very essential to be seen I watch it on my laptop or cell phone and do you get the same feel of it do you still enjoy it as much watching it on your device rather than tel no actually not because the screen is not that much wide and when you watch TV programs on TV it is wider and it has better resolution so it is more fascinating to watch it on.",
        "word_count": 273,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition_choice", "comparative"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["keen on", "fascinating", "persuade", "anticipate", "devote to", "resolution"],
            "grammar_structures_used": ["complex_sentence_because", "relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["wrong_preposition"],
            "vocabulary": ["wrong_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'devote on' (devote to). 'not that much wide' (not as wide / not very wide)."
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "high",
            "flexibility": "high",
            "error_density": "rare"
        },
        "discourse_metrics": {
            "length_appropriateness": "long",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Minor errors 'not that much wide'.",
                "why_not_6": "Frequent error-free complex sentences."
            },
            "vocabulary": {
                "why_not_8": "'anticipate', 'persuade' are good. Errors are minor.",
                "why_not_6": "High range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'anticipate', 'resolution'. Impact: Precise. Justification: Band 7.",
        "grammar_reason": "Observation: 'devote on' (error). Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 29,
        "sample_id": "DNNJy1g18p8_q03",
        "video_id": "DNNJy1g18p8",
        "part": 1,
        "question": "Cinema vs Home",
        "transcript": "TV rather than laptop and cell phones right and what about Cinemas do you like going to the cinema yeah I am really to cinema and before the pandemic I had gone to cinema on a regular basis",
        "word_count": 36,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["regular basis"],
            "grammar_structures_used": ["past_perfect"]
        },
        "micro_flaws": {
            "grammar": ["missing_word"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'I am really to cinema' (into?). 'had gone to cinema' (used to go / went)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Minor error 'really to'.",
                "why_not_6": "Good structure."
            },
            "vocabulary": {
                "why_not_8": "Good.",
                "why_not_6": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'regular basis'. Impact: Good. Justification: Band 7.",
        "grammar_reason": "Observation: 'really to' (error). Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 30,
        "sample_id": "DNNJy1g18p8_q04",
        "video_id": "DNNJy1g18p8",
        "part": 1,
        "question": "Device usage and health",
        "transcript": "That I could be aware of that for using my device but also because of the health function that it has I can be aware of the heartbeat my my heartbeat especially when I use it for the physical activities for my physical activities and my running courses and all these items make this device so fascinating for me and I use it daily and the U most inconvenient part about this device was the show was the small screen up that at first the tiny letters was so actually disturbing for me and I cannot use them but then I was accustomed to reading them and it was quite fascinating",
        "word_count": 107,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["health function", "physical activities", "inconvenient part", "accustomed to", "fascinating"],
            "grammar_structures_used": ["complex_sentence_because", "relative_clause"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_disagreement"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'tiny letters was' (were). 'running courses' (routes?)."
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "high",
            "flexibility": "high",
            "error_density": "rare"
        },
        "discourse_metrics": {
            "length_appropriateness": "long",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Agreement error 'letters was'.",
                "why_not_6": "Complex structures."
            },
            "vocabulary": {
                "why_not_8": "'accustomed to' is good. 'running courses' is slightly imprecise.",
                "why_not_6": "High range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses less common lexical items."
        },
        "vocab_reason": "Observation: 'accustomed to'. Impact: Precise. Justification: Band 7.",
        "grammar_reason": "Observation: 'letters was' (error). Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 31,
        "sample_id": "DNNJy1g18p8_q05",
        "video_id": "DNNJy1g18p8",
        "part": 1,
        "question": "Technology in schools",
        "transcript": "Children should start to use these kind of devices okay and do you think that schools should use more technology to help children learn in my point of view schools are important organization to help children learn these kind of things because parents May not be familiar with the state-of-the-art Technologies and devices and I suppose that teachers are better people who can take this responsibility okay and do you agree or disagree that computers will replace teachers one day I do not think so I suppose that I talking to someone in person does not cannot be replaced by talking with computers and then children actually have teachers they can learn things better and their lessons become internalized in them better and I suppose that teachers will not be replaced by computers but their responsibilities might somehow change in future in future and for example some tasks might be devoted to CH to teachers and some them to computers.",
        "word_count": 156,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrase_structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["state-of-the-art", "internalized", "devoted to", "take this responsibility"],
            "grammar_structures_used": ["complex_sentence", "passive_voice"]
        },
        "micro_flaws": {
            "grammar": ["missing_preposition"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'some them' (some of them)."
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "high",
            "flexibility": "high",
            "error_density": "rare"
        },
        "discourse_metrics": {
            "length_appropriateness": "long",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Minor error 'some them'.",
                "why_not_6": "Complex structures correct."
            },
            "vocabulary": {
                "why_not_8": "'state-of-the-art' is very good. 'internalized' is advanced.",
                "why_not_6": "High range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Uses less common lexical items skilfully."
        },
        "vocab_reason": "Observation: 'internalized', 'state-of-the-art'. Impact: Sophisticated. Justification: Band 8.",
        "grammar_reason": "Observation: 'some them' (error). Justification: Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 32,
        "sample_id": "rhLgKf41nhA_q02",
        "video_id": "rhLgKf41nhA",
        "part": 1,
        "question": "Jewelry traditions",
        "transcript": "Another two common Rings this is with special stone called opalo okay and do people in your country ever wear jewelry such as Rings or necklaces yes I know a lot of people uses some necklace of w I do not have necklace but a lot of people use it okay perfect and why do some people wear a jewelry for a long time in your idea for example I need to have with me my w ring I need to have it for a lot a lot of time but there is another gy that the family could keep through generations I think",
        "word_count": 98,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "article"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "wrong",
            "vocab_evidence": ["necklace of w", "wear a jewelry"],
            "grammar_structures_used": ["complex_sentence_but"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_disagreement"],
            "vocabulary": ["wrong_word_choice", "uncountable_plural"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'people uses' (use). 'wear a jewelry' (wear jewelry). 'necklace of w' (gold?). 'opalo' (opal)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Agreement errors.",
                "why_not_5": "Structures mainly correct."
            },
            "vocabulary": {
                "why_not_7": "Basic errors 'a jewelry'.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'jewelry', 'generations'. Impact: OK. 'a jewelry' (error). Justification: Band 6.",
        "grammar_reason": "Observation: 'people uses' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 33,
        "sample_id": "rhLgKf41nhA_q04",
        "video_id": "rhLgKf41nhA",
        "part": 1,
        "question": "Favorite painter",
        "transcript": "Think she is the very the best painter in the in the world I think I I love her and I think we have we had an exposition of of her paintings in the in a museum and near here and it was very beautiful because I can see all he all her paintings right in front of me",
        "word_count": 57,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["exposition", "right in front of me"],
            "grammar_structures_used": ["complex_sentence_because"]
        },
        "micro_flaws": {
            "grammar": ["stuttering"],
            "vocabulary": ["wrong_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'exposition' (exhibition - partial false friend?). 'very the best' (the very best)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "rare"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Fluency/stuttering affects flow.",
                "why_not_5": "Correct structures."
            },
            "vocabulary": {
                "why_not_7": "'exposition' vs 'exhibition'.",
                "why_not_5": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'exposition'. Impact: Minor error. Justification: Band 6.",
        "grammar_reason": "Observation: Correct but stuttered. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 34,
        "sample_id": "rhLgKf41nhA_q05",
        "video_id": "rhLgKf41nhA",
        "part": 1,
        "question": "Social media influence",
        "transcript": "Influence of these famous people and of course social media is a platform for such people so how does social media influence human behavior in your opinion I think the human behavior is a it is very very influenced by the social media because we are living in a moment that is very important to have this social life and this social media and making a strong Community because the this moment is very fast and all the social media can have the all the moments all the things of the life right in front of you in a few seconds okay and so can you talk about the disadvantages of social media because now we talked about some of the advantages of it like how it can shap the community but how about it disadvantages I think the social media have a lot of disadvantages because a young people can be really hurt in the self-esteem because they can have a lot of.",
        "word_count": 158,
        "analysis_metadata": {
            "grammar_error_patterns": ["article", "word_order"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["social media", "platform", "self-esteem", "human behavior"],
            "grammar_structures_used": ["complex_sentence_because", "passive_voice"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'things of the life' (of life). 'hurt in the self-esteem' (hurt their self-esteem)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "occasional"
        },
        "discourse_metrics": {
            "length_appropriateness": "long",
            "redundancy": "moderate",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Article errors.",
                "why_not_5": "Complex structures used well."
            },
            "vocabulary": {
                "why_not_7": "'self-esteem' is good.",
                "why_not_5": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex forms.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'self-esteem'. Impact: Good. Justification: Band 6.",
        "grammar_reason": "Observation: 'hurt in the' (error). Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    }
]

with open(output_file, "a") as f:
    for s in samples:
        f.write(json.dumps(s) + "\n")

print(f"Successfully appended {len(samples)} samples to {output_file}")
