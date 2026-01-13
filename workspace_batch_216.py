import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 216 ---
# Total Samples: 20
# Samples Analyzed:

# 1. u9cggZHjwS4_q02 (Band 9.0)
# Transcript: "buying presents for my friends... favorite store is a book store which is in the list of my top priority... gain another piece of knowledge... great sense of satisfaction... pour into the streets and shopping centers... considered more as a Leisure activity... window shopping... beautify themselves..."
# Analysis:
# - Grammar: "which is in the list of my top priority" (on my list of top priorities). "pour into the streets" (good idiom). "considered more as a leisure activity" (more of a leisure activity).
# - Vocabulary: "beautify themselves", "gain another piece of knowledge", "sense of satisfaction".
# - Verdict: Band 9.0.

# 2. u9cggZHjwS4_q05 (Band 9.0)
# Transcript: "repay the visit... special Cuisines... boost the unity among nations... reflects an overview of the attitude of gratitude... reluctant than ever... independent lives..."
# Analysis:
# - Grammar: "repay the visit" (return the visit). "attitude of gratitude" (rhyme/idiom).
# - Vocabulary: "unity among nations", "reluctant", "special cuisines".
# - Verdict: Band 9.0.

# 3. Mr2f4MxGmA8_q04 (Band 9.0)
# Transcript: "communicating properly... vocal about their problems... conscious about one's health... practical overview... communication gaps are reduced... data analysis... dependent on anything... emotionally involved..."
# Analysis:
# - Grammar: "dependent on anything or anyone entirely at all" (entirely dependent).
# - Vocabulary: "facilitates communication", "communication gaps", "data analysis", "workload".
# - Verdict: Band 9.0.

# 4. Mr2f4MxGmA8_q05 (Band 9.0)
# Transcript: "critical and creative thinking... thinking outside the box... adaptability and flexibility... manage the time..."
# Analysis: "thinking outside the box".
# - Verdict: Band 9.0.

# 5. ZOssSygjd7E_q02 (Band 8.0)
# Transcript: "comes in handy... mood of the product... resonates a funny feeling... resembles a serious influence... connect with the people... relate the advertisement..."
# Analysis:
# - Grammar: "mood of the product" (tone/nature). "resonates a funny feeling" (evokes/creates). "resembles a serious influence" (has/conveys).
# - Vocabulary: "comes in handy", "resonates", "resembles". Slightly misused but high level.
# - Verdict: Band 8.0.

# 6. ZOssSygjd7E_q03 (Band 8.0)
# Transcript: "collisions of thoughts and opinions... convey that feeling that I am right... justify our emotions... come into an agreement... makes our life more prosperous... non-toxic... seek for advices... take a leap of faith..."
# Analysis:
# - Grammar: "collisions of thoughts" (clashes/conflicts). "seek for advices" (seek advice - uncountable).
# - Vocabulary: "prosperous", "non-toxic", "leap of faith", "justify".
# - Verdict: Band 8.0.

# 7. ZOssSygjd7E_q04 (Band 8.0)
# Transcript: "time and generation have changed drastically... dependent on smartphones... stick to our core values... liberal enough... shortcomings in their influences..."
# Analysis:
# - Grammar: "time and generation have changed" (times have changed / generations have changed). "we does not stick" (do not).
# - Vocabulary: "drastically", "shortcomings", "core values", "liberal".
# - Verdict: Band 8.0. "we does not" is a slip.

# 8. mT29ah2C4s8_q01 (Band 5.5)
# Transcript: "math help me for the logical thinking and we can solve the problem."
# Analysis: "math help me" (helps). "for the logical thinking" (with logical thinking).
# - Verdict: Band 5.5.

# 9. mT29ah2C4s8_q02 (Band 5.5)
# Transcript: "I am a boy and I really like subject about thinking and logical... I need to my friends to help me..."
# Analysis: "like subject about thinking" (subjects). "need to my friends" (need my friends).
# - Verdict: Band 5.5.

# 10. mT29ah2C4s8_q03 (Band 5.5)
# Transcript: "use the math for go to the market to can calculate... basic math for support the university..."
# Analysis: "for go to" (for going to / when going to). "to can calculate" (to calculate).
# - Verdict: Band 5.5.

# 11. CzpbsecP4Qs_q01 (Band 6.5)
# Transcript: "If my memory served me right... Nike shoes which I am currently brings on this mocking test day... currently wearing..."
# Analysis: "memory served me right" (serves). "currently brings" (bringing / wearing). "mocking test" (mock test).
# - Verdict: Band 6.5. Good idiom attempt.

# 12. EfDqSBUoS6Y_q01 (Band 5.0)
# Transcript: "favorite meal is this a delicious thank you... spicy foods that is spicy noodles... favorite Cuisine is J... very common in Vietnam... have many coming in all over the world..."
# Analysis: "meal is this a delicious". "have many coming in" (many people coming?).
# - Verdict: Band 5.0.

# 13. 3th2fIaDQQ4_q02 (Band 3.5)
# Transcript: "B the working time and relaxing time is it is good for them for them H it it had be people relaxing after a hard work a hard working day."
# Analysis: "it it had be people relaxing". Broken speech.
# - Verdict: Band 3.5/4.0.

# 14. _acfkNS31Fo_q01 (Band 7.5)
# Transcript: "housemate usually does their cooking... mother lives in Cox's Bazaar... owned by my grandfather..."
# Analysis: Simple, accurate.
# - Verdict: Band 7.5.

# 15. _acfkNS31Fo_q02 (Band 7.5)
# Transcript: "My sister because of the environment that we cannot get at home"
# Analysis: Fragment? "My sister [lives there] because...". Valid continuation.
# - Verdict: Band 7.5.

# 16. _acfkNS31Fo_q03 (Band 7.5)
# Transcript: "cabinet consists of her valuable items... necklace on when she passed away... renovate the kitchen... different Outlook... connects me to her... depressing time..."
# Analysis:
# - Grammar: "different Outlook" (look/appearance?). "consists of" (contains).
# - Vocabulary: "passed away", "valuable items", "renovate".
# - Verdict: Band 7.5.

# 17. _acfkNS31Fo_q04 (Band 7.5)
# Transcript: "renovate at any time soon... make a backyard... waste of money... move out anytime soon... requires a certain age..."
# Analysis: "renovate at any time soon" (renovate anytime). "requires a certain age".
# - Verdict: Band 7.5.

# 18. w5NMQefa1O0_q01 (Band 6.5)
# Transcript: "utilizing the social media... text each other... keep the connection strong and the bond is secure."
# Analysis: "utilizing" (using). "bond is secure".
# - Verdict: Band 6.5.

# 19. ASSx9VicKcM_q02 (Band 7.0)
# Transcript: "grab something... working as a high school C counselor... supervising and assisting... promoted herself... monthly one-on-one meetings... implementing fun activities... builds self-confidence and esteem..."
# Analysis:
# - Vocabulary: "implementing", "supervising", "promoted", "one-on-one meetings".
# - Verdict: Band 7.0.

# 20. ASSx9VicKcM_q03 (Band 7.0)
# Transcript: "feel motivated... can do attitude... positive influencer... understand their weaknesses... creates commitment... raising awareness..."
# Analysis: "can do attitude" (can-do attitude). "raising awareness".
# - Verdict: Band 7.0.

scored_samples = [
    {
        "id": 0, "sample_id": "u9cggZHjwS4_q02", "video_id": "u9cggZHjwS4",
        "part": 1,
        "question": "Shopping types?",
        "transcript": "In the household so we we always tend to go shopping together okay and what type of shopping do you like and why what I like most about shopping when it comes to shopping is buying presents for my friends or maybe people's birthdays or even Christmas my favorite store is a book store which is in the list of my top priority and I believe if I buy a book for someone it is not only considered a gift but also I can help that person gain another piece of knowledge so it makes me it brings me a great sense of satisfaction great and is shopping a popular activity in your country why why not it is indeed on Thursdays and Fridays people pour into the streets and shopping centers it is considered more as a Leisure activity than just they are not aiming to buy something practical so I see that most teen teenagers and people go shopping go sometimes window shopping or they wander around the mall so I do not think they buy something practical for okay so what type of shops do teenagers like best in your country well I have not thought about this before but obviously like any other teenagers they are much more into shopping clothes makeup to beautify themselves or maybe some music stuffs and these kind of things",
        "word_count": 216,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["beautify themselves", "pour into the streets", "window shopping", "leisure activity"],
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
                "why_not_9": "'pour into the streets'. Excellent idiom.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "u9cggZHjwS4_q05",
        "video_id": "u9cggZHjwS4",
        "part": 1,
        "question": "Celebrations?",
        "transcript": "It is like a huge celebration they sometimes pay and repay the visit to one another and sometimes they buy some new clothes and they cook some special Cuisines on that day and it is considered a happy moment on that day wow and why is it important to have national celebrations when I come to think of it national celebrations can boost the unity among nations and another thing about these National festivals is the great advantage that it it is an over it gives an overview of it reflects an overview of the attitude of gratitude and enjoying every thing that we own everything we have instead of the things that we do not or that we want in the future so it is a great moment to be grateful for what we have and how is the way your national celebrations are celebrated now different from the way they were celebrated in the past actually I am not very into the celebrations that have happen that people used to have in the past but about today I think people tend to care a lot more about some private parties that people in the past did not used to have it is something that people in the past I think used to celebrate more indoors whereas today people are celebrating outdoors with their friends like teenagers they are you know more reluctant than ever to celebrate these National festivals with their family members or relatives they like to have their own independent lives and enjoy themselves independently okay and are there any celebrations from other countries that you celebrate in your country absolutely recently we can easily see that people are celebrating some celebrations that.",
        "word_count": 273,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["boost the unity", "attitude of gratitude", "reluctant", "special cuisines"],
            "grammar_structures_used": ["complex_sentences", "contrast"]
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
            "reason": "'repay the visit' (return the visit)."
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
                "why_not_9": "'attitude of gratitude'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "Mr2f4MxGmA8_q04",
        "video_id": "Mr2f4MxGmA8",
        "part": 3,
        "question": "Problem solving?",
        "transcript": "Relationship issues could be solved by communicating properly with each other and being more vocal about their problems the health issues can be prevented by being more conscious about one's health and about the time management issues people can always create a schedule that they can tightly follow is it important to involve others in problem solving I believe it is required to involve others in problem solving in certain situations for instance if you are too involved emotionally with a certain project and you need a practical overview that is when you can involve someone else and you can also involve others in problem solving when you have too much workload and too much stress and you need to reduce some of it can technology help people solve problems more effectively and how definitely technology can help people solve problems more effectively technology facilitates communication the communication gaps are reduced in our generation due to the help of Technologies and they always provide us information whenever and wherever we need it and they also do proper data analysis which help individuals to carry out their projects forward what are some potential downsides of relying too heavily on technology to solve problems well no one should be dependent on anything or anyone entirely at all so the same goes for technology as well Technologies are not able to do some things on their own such as they cannot solve situations that are in related to emotions so a person can face a problem that they are emotionally involved with and Technology will not be able to give a proper answer for that okay so in your opinion what skills are necessary for Effective problem solving I believe it depends on the type of problem that we are solving however in general there are.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["communication gaps", "emotionally involved", "data analysis", "facilitates communication"],
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
                "why_not_9": "'facilitates', 'vocal about'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise terms ('facilitates'). Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "Mr2f4MxGmA8_q05",
        "video_id": "Mr2f4MxGmA8",
        "part": 3,
        "question": "Skills for solving?",
        "transcript": "Certain skills that an individual should have for every problem solving for instance critical and creative thinking the ability to analyze a situation before solving it and thinking outside the box after that good communication skills are very important nowadays so it is very important to happen adaptability and flexibility to be able to adapt to any situation and be flexible about solving them and lastly time management skills it is very important to manage the time when it comes to solving a problem.",
        "word_count": 82,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["critical and creative thinking", "thinking outside the box", "adaptability and flexibility"],
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
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard business English.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "ZOssSygjd7E_q02",
        "video_id": "ZOssSygjd7E",
        "part": 1,
        "question": "Advertisement?",
        "transcript": "Things that I am looking for so that comes in handy but not always do you like funny or serious advertisement I think that depends on the mood of the product the product that resonates a funny feeling should go with a funny advertisement or the product that resembles a serious influence should have a serious advertisement great what do you think makes a good advertisement I think the ability of that advertisement to connect with the people plays the most key role and when an audience can relate the advertisement with their daily life I think that influences them more work hom now I am going to give you a topic and I would like like you to talk about it for 2 minutes you have 1 minute to think about what you are going to say and.",
        "word_count": 139,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["comes in handy", "mood of the product", "resonates"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["collocation_minor"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'resonates a funny feeling' (creates/evokes). 'resembles a serious influence' (has?)."
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
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Minor unnatural phrasing.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'resonates a feeling' - slightly off.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level but slight misuse. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "ZOssSygjd7E_q03",
        "video_id": "ZOssSygjd7E",
        "part": 3,
        "question": "Advice?",
        "transcript": "Have conversation with them but we do not always get along with them so sometimes we have collisions of thoughts and opinions so when we see that I am right and the person the other person might be wrong in my perspective we always try to convey that feeling that I am right whether we do not always care about we are whether we are hurting the people or the emotions but we try to justify our emotions first but if we think a little bit carefully that it is not always necessary that I have to be right it is better that if we come into an agreement that we put the happiness first and being right to the second position it is all it makes our life more prosperous and I think it makes ourselves more non-toxic to other people we are dealing with all right one approximately 1 minute 24 25 seconds 45 second it is a very good time seconds second describe a piece of advice you recently received you should say when this happened who gave you the advice ADV what the advice was actually and explain how you felt about the ADV rather he talks about now you have been telling me about an advice you recently received I am going to ask you some questions related to this so first of all do you think people ought to get advice before making big decisions I think in certain parts of life we always seek for advices from elderly or from our parents but there are some cases when you have to take a leap of faith and you just have to do whatever your mind tells to do I think that is not a conventional approach but when you are in doubt and no no one or nothing is helping I think.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["leap of faith", "collisions of thoughts", "non-toxic", "prosperous"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'seek for advices' (advice). 'collisions of thoughts' (clashes). 'justify our emotions'."
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
                "why_not_9": "Minor error ('advices').",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "'advices' (uncountable).",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level but 'advices' error. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "ZOssSygjd7E_q04",
        "video_id": "ZOssSygjd7E",
        "part": 3,
        "question": "Decisions?",
        "transcript": "That is the way to go all right do you think young people today have different types of decisions to make about their lives compared to young people in the past well without a doubt I think that time and generation have changed drastically so the decisions people used to take back in the in their days have changed compared to the decisions we take now in our daily lives see the generation have come to a point where we are dependent on smartphones and other social activities but in the past there was nothing like that and people used to take decisions based on their real life experiences so I think nowadays we take take decisions that in that are influenced by the social activities and other factors great should children be allowed to make decisions on their own well it depends on the decision they are taking obviously sometimes that decisions they take might lead to something harmful which they might not understand so I think it is always better to supervise them before giving them any advice or watch them as they are following the instructions okay what do you think about people who change their minds after making a decision well to be honest I think they are the best kinds of people because this is the hardest thing a human can do is changing their opinion when we get new opinions we try to rethink that over and over again but it is it does not happen always that we does not stick to our core values so whatever the decisions or the influences are coming we try to always stick to our core values but when some people are liberal enough that they accept that there are some shortcomings in their influences or activities they change their decisions I.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["drastically", "core values", "liberal enough", "shortcomings"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'we does not stick' (do not)."
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
                "why_not_9": "Agreement error 'we does'.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "'shortcomings', 'core values'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent. Band 9.",
        "grammar_reason": "Minor error. Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mT29ah2C4s8_q01",
        "video_id": "mT29ah2C4s8",
        "part": 1,
        "question": "Subjects?",
        "transcript": "I think that is math because math help me for the logical thinking and we can solve the problem. Thank you. Well done.",
        "word_count": 20,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "preposition"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["logical thinking"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'math help me' (helps). 'for the logical thinking' (with)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "moderate",
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
                "why_not_6": "Basic errors.",
                "why_not_4": "Understandable."
            },
            "vocabulary": {
                "why_not_6": "Limited.",
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
        "grammar_reason": "Basic errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "mT29ah2C4s8_q02",
        "video_id": "mT29ah2C4s8",
        "part": 1,
        "question": "Why study?",
        "transcript": "I think that is maybe I am a boy and I really like subject about thinking and logical but when I study it I feel it really hard and I need to my friends to help me solve all the problem. Fantastic.",
        "word_count": 40,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["logical", "solve"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'like subject' (subjects). 'need to my friends' (need my friends)."
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
                "why_not_6": "Frequent basic errors.",
                "why_not_4": "Understandable."
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
        "id": 0, "sample_id": "mT29ah2C4s8_q03",
        "video_id": "mT29ah2C4s8",
        "part": 1,
        "question": "Subject popular?",
        "transcript": "M I think in Vietnam we usually use the math for go to the market to can calculate how much price we spend for the like the lunch or the afternoon with our family and we use the basic math for support the university like some about building or engineering. Fantastic.",
        "word_count": 51,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["calculate", "engineering"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'use the math for go to' (for going to). 'to can calculate' (to calculate)."
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
                "why_not_6": "Frequent structural errors.",
                "why_not_4": "Meaning mostly clear."
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
        "grammar_reason": "Structure breakdown. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "CzpbsecP4Qs_q01",
        "video_id": "CzpbsecP4Qs",
        "part": 1,
        "question": "Last bought?",
        "transcript": "If my memory served me right. Fantastic phrase. If my memory serves me right. Wow. It was my Nike shoes which I am currently brings on this mocking test day. So it should be which I am currently wearing on this.",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["memory serves me right", "mock test"],
            "grammar_structures_used": ["self_correction"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'currently brings' (wearing/bringing). 'mocking test' (mock test). Self-correction: 'should be wearing'."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "moderate",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Verb error.",
                "why_not_5": "Self-correction shows awareness."
            },
            "vocabulary": {
                "why_not_7": "'mocking' vs 'mock'.",
                "why_not_5": "Idiom attempt."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good idiom but errors. Band 6.",
        "grammar_reason": "Self-correction. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "EfDqSBUoS6Y_q01",
        "video_id": "EfDqSBUoS6Y",
        "part": 1,
        "question": "Food?",
        "transcript": "First of all I would like us to talk about food tell me what is your favorite meal yeah my favorite meal is this a delicious thank you is there any food you do not like I do not like spicy foods that is spicy noodles and because it is hot really which type of Cuisine is your favorite my favorite Cuisine is J yeah it is delicious why do you like Chinese food because it is very common in Vietnam can you tell me a little bit about is a very delicious and have many coming in all over the world brilliant",
        "word_count": 98,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["spicy foods"],
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
            "reason": "'meal is this a delicious'. 'have many coming in' (?)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "low",
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
                "why_not_6": "Sentence structure failure.",
                "why_not_4": "Meaning clear."
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
        "grammar_reason": "Breakdown. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "3th2fIaDQQ4_q02",
        "video_id": "3th2fIaDQQ4",
        "part": 1,
        "question": "Work relax?",
        "transcript": "B the working time and relaxing time is it is good for them for them H it it had be people relaxing after a hard work a hard working day.",
        "word_count": 29,
        "analysis_metadata": {
            "grammar_error_patterns": ["incoherence"],
            "grammar_error_frequency": "dominant",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["fragment"]
        },
        "micro_flaws": {
            "grammar": ["coherence_breakdown"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Incoherent speech."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "low",
            "flexibility": "none",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "high",
            "development_depth": "none"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Incoherent.",
                "why_not_3": "Words recognizable."
            },
            "vocabulary": {
                "why_not_5": "Basic.",
                "why_not_3": "English words."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Cannot use sentence forms except in memorised phrases.",
            "vocabulary_band": 4,
            "vocabulary_text": "Uses basic vocabulary."
        },
        "vocab_reason": "Basic. Band 4.",
        "grammar_reason": "Incoherent. Band 4.",
        "vocabulary": 4,
        "grammar": 4
    },
    {
        "id": 0, "sample_id": "_acfkNS31Fo_q01",
        "video_id": "_acfkNS31Fo",
        "part": 1,
        "question": "House?",
        "transcript": "Our housemate usually does their cooking in my house because my mother lives in Cox's Bazaar the house I would like to describe is owned by my grandfather in my country I believe apartments are more popular among the people hello and welcome to this practice exam conducted by the British American Resource Center my name is Maru and I am your practice examiner these questions have been designed to simulate the our speaking test so.",
        "word_count": 71,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["owned by"],
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
                "why_not_8": "Simple sentences.",
                "why_not_6": "Error free."
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
        "grammar_reason": "Accurate. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "_acfkNS31Fo_q02",
        "video_id": "_acfkNS31Fo",
        "part": 1,
        "question": "Sister?",
        "transcript": "My sister because of the environment that we cannot get at home",
        "word_count": 11,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["environment"],
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
                "why_not_8": "Short.",
                "why_not_6": "Accurate."
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
        "grammar_reason": "Accurate. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "_acfkNS31Fo_q03",
        "video_id": "_acfkNS31Fo",
        "part": 2,
        "question": "Cabinet?",
        "transcript": "Cancer I think this happened around four years back and it the cabinet consists of her valuable items for example she had this necklace on when she passed away which is still stored preciously in the cabinet I do not think there is anything I dislike about the house however if I could I would definitely renovate the kitchen because it became quite old now and it needs a different Outlook and the favorite part about the house is the garden which my grandmother made be before she died it has different kind of flowers and trees and I feel like it connects me to her and whenever I am going through a hard time or a very depressing time I feel like I can go and rest over there it is very it is very relaxing and sometimes I like to talk about different things with my grandfather in the garden",
        "word_count": 147,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["valuable items", "passed away", "stored preciously", "renovate", "Outlook"],
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
            "reason": "'different Outlook' (look). 'stored preciously' (carefully?)."
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
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Minor errors.",
                "why_not_6": "Complex."
            },
            "vocabulary": {
                "why_not_8": "Minor word choice issues.",
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
        "id": 0, "sample_id": "_acfkNS31Fo_q04",
        "video_id": "_acfkNS31Fo",
        "part": 3,
        "question": "House vs Apartment?",
        "transcript": "Yourself whereas in a house you can renovate at any time soon you can make a backyard or a garden do you think that everyone would like to live in a larger home if we do have the choice yes I I think anyone would like to live in a larger home because we can simply make a music or Art Studio or anything that we personally love how easy is it to find a place to live in your country it is moderately easy to find a place in my country however I feel like it is better and easier to find a house or an apartment in the city because it people mostly live over there because of their job and their work do you think it is better to buy or to rent a place to live in it varies from person to person in my opinion because if you are looking for something more permanent I believe buying a house would be better for you however if you feel like you going to move abroad or move out anytime soon I think it is simply a waste of money do you agree that there is a right age for young adults to stop living with your parents I do not think there is a certain age that we need to follow for us to move out of the house or stop living with our parents we have been growing up with them for a very long time and I believe if you want you can still live with them however if you want to go for better opportunities or something else that relates to your studies or work you can definitely move out anytime soon but it does not require a certain age for you to do so right thank.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["waste of money", "renovate", "moderately easy", "permanent"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
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
                "why_not_7": "Good range."
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
        "id": 0, "sample_id": "w5NMQefa1O0_q01",
        "video_id": "w5NMQefa1O0",
        "part": 1,
        "question": "Friendship?",
        "transcript": "How can people maintain longdistance friendships in my opinion longdistance friendship is a very hard thing to do because I have not had any longdistance friendship before but but the way that people might do to maintain a longdistance friendship Is by utilizing the social media they could use like Facebook Instagram to text each other and maybe time so that they could keep the connection and maybe do some like online game together yeah that could keep the connection strong and the bond is secure.",
        "word_count": 84,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["longdistance friendship", "keep the connection strong", "utilizing"],
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
                "why_not_8": "Repetition.",
                "why_not_6": "Error free."
            },
            "vocabulary": {
                "why_not_8": "Repetitive.",
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
        "id": 0, "sample_id": "ASSx9VicKcM_q02",
        "video_id": "ASSx9VicKcM",
        "part": 1,
        "question": "Advice work?",
        "transcript": "Is when I travel or have an appointment to meet someone for breakfast in these instances I do not eat at home and instead grab something or go somewhere to eat but usually I prefer to eat breakfast at home as I know that breakfast is an important meal for people like myself who spend all day out a few years ago when I was working as a high school C counselor I received some positive advice from my boss on how to help support students I would be supervising and assisting my boss at the time had been working in the position for a few years prior and had been promoted herself so she was familiar with the tasks that counselors had during our TR monthly one-on-one meetings my boss would go over my work per performance with me my boss would focus on areas for me to improve for example creating new events for students to participate in I felt thankful for receiving open and helpful suggestions the provided suggestions helped me focus on finding planning and implementing fun activities for the students I supported when should parents encourage their children parents should encourage their children when they show that they are able to complete things it could be they are able to tie their shoes brush their teeth ride a bike study on their own or even receive praise from their teachers parents should encourage and praise their children whenever they achieve something this builds self-confidence and esteem should parents always encourage their children it depends sometimes encouragement is needed to help children grow however if children are self-motivated themselves then it is best to let the children try on their own learning is an important part of growing up all children eventually must learn to do.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["supervising", "implementing", "one-on-one meetings", "self-motivated", "promoted"],
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
        "vocab_reason": "Good terms. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "ASSx9VicKcM_q03",
        "video_id": "ASSx9VicKcM",
        "part": 3,
        "question": "Feedback?",
        "transcript": "Things on their own and they should feel motivated to try things this will help in creating a can do attitude towards studying playing and even engaging in society do you think negative feedback is more important than positive feedback yes I do negative feedback can be a positive influencer in terms of pushing you to try harder next time while the term negative itself is not viewed as good negative feedback is feedback feedback given to a person from their boss teacher or friend can help the person better understand their weaknesses they can also focus on improving this weakness trying to improve creates commitment and increase es an individual's personal drive to do better why is negative feedback as important as positive feedback at work or in study feedback is needed to help improve one's performance positive feedback while considered good does not make a person feel the need to improve or study harder the reason being is because positive feedback confirms that the person is working working hard or studying well however negative feedback can help in raising awareness of something that is not good or beneficial for the person when receiving negative feedback we should not feel bad instead we should learn from the negative feedback and work harder to improve.",
        "word_count": 204,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["can do attitude", "positive influencer", "raising awareness", "commitment"],
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
        "vocab_reason": "Good terms. Band 8.",
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
