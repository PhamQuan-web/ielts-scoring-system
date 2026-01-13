import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 217 ---
# Total Samples: 20
# Samples Analyzed:

# 1. bbQjI9CrJak_q01 (Band 6.0)
# Transcript: "go there with my sister because she share the same... interest... also have plan... is perfect... baby sister... family orientated person... leave near my parents... short a couple of months enough... get exposed to the local local aspect... do not feel anxiety have a feeling of anxiety..."
# Analysis:
# - Grammar: "she share" (shares). "have plan" (has a plan). "is perfect" (it is perfect). "leave near" (live near).
# - Vocabulary: "family orientated", "anxiety", "exposed to".
# - Verdict: Band 6.0. Frequent basic errors.

# 2. x51j2qcODVo_q01 (Band 6.5)
# Transcript: "using Facebook and messenger... call them out to hang out... create some hangout event... share my thought... toxic... rfor in the toxicity... inappropriate content... block them like every time... algorithm... inappropriate image is a thing..."
# Analysis:
# - Grammar: "call them out" (call them up / ask them out). "share my thought" (thoughts). "rfor" (refer? rise?).
# - Vocabulary: "toxic", "algorithm", "inappropriate content".
# - Verdict: Band 6.5. Good vocab ("algorithm", "toxic"), some awkward phrasing.

# 3. X0SQAUJ0C5U_q02 (Band 6.5)
# Transcript: "creativity in writes lyrics... if i be honest... reputable for reputation... thomas friend of mine... cheerful... common... wisdom... going out with him... talk about cinema... enjoy to spend time to him... narrow-minded people... dogmatic person..."
# Analysis:
# - Grammar: "in writes lyrics" (writing). "if i be honest" (to be honest). "reputable for reputation" (redundant/wrong). "thomas friend" (close friend? best friend?). "enjoy to spend time to him" (enjoy spending time with him).
# - Vocabulary: "creativity", "lyrics", "wisdom", "philosophy", "narrow-minded", "dogmatic". Excellent vocab.
# - Verdict: Band 6.5. High-level vocab ("dogmatic") pulled down by grammar ("enjoy to spend time to him").

# 4. X0SQAUJ0C5U_q03 (Band 6.5)
# Transcript: "is it going people... non-wisdom people... go along with everything... live at moments... communication lasts his meaning... close to the social media... harder than before..."
# Analysis:
# - Grammar: "is it going" (easy-going). "communication lasts his meaning" (lost its meaning).
# - Vocabulary: "easy-going" (attempted).
# - Verdict: Band 6.0/6.5. "lasts his meaning" is incoherent. But flow is okay.

# 5. X0SQAUJ0C5U_q04 (Band 6.5)
# Transcript: "care about their mental health... checkup in every month... fewer diseases must be half must we have... solution of hill healing... educational people and medicine is so expanded..."
# Analysis:
# - Grammar: "when improve them" (improve their). "fewer diseases must be half" (?). "solution of hill healing" (healing). "medicine is so expanded" (advanced?).
# - Verdict: Band 6.0.

# 6. BshvbR37Uow_q01 (Band 7.5)
# Transcript: "tough question... advantages on the specific effect aspect... no information Rel readily... slower paste of a mode of transportation... immerse ourselves... technological advancement... schedule days book and accommodations..."
# Analysis:
# - Grammar: "traveling is feel like" (feels like). "slower paste" (pace). "transportation and everything like that it makes" (good).
# - Vocabulary: "immerse ourselves", "technological advancement", "accommodations".
# - Verdict: Band 7.5. Good fluency and range.

# 7. tCg4KBkXNG4_q01 (Band 8.0)
# Transcript: "integral part of our life... personal best friend... personal data... utilize... do transactions... acquire new knowledge... track locations... benefits me a... technological devices..."
# Analysis:
# - Grammar: "can be benefits me" (can benefit me). "just works with a phone" (work).
# - Vocabulary: "integral part", "utilize", "acquire", "transactions".
# - Verdict: Band 8.0.

# 8. eEA5PY_bbDk_q03 (Band 4.0)
# Transcript: "computer games... I will I will not have time... friends or family is important... friend helped me happier relax... teach me a lot of things when i was born..."
# Analysis:
# - Grammar: "friend helped me happier relax" (help me be happier and relax). "when i was born" (since I was born?).
# - Verdict: Band 4.0. Basic.

# 9. tl1ERXjlPAE_q01 (Band 4.0)
# Transcript: "what is your name... call me Anne... currently 17... turning 18..."
# Analysis: Basic intro.
# - Verdict: Valid (Band 4).

# 10. tl1ERXjlPAE_q02 (Band 4.0)
# Transcript: "husband is usually the one to go outside and make money... wife is the one who did stay home... cook it do the cooking... control of the family to keeping up the camp family... introvert person... hang out..."
# Analysis:
# - Grammar: "did stay home" (stays). "keeping up the camp family" (?).
# - Vocabulary: "introvert".
# - Verdict: Band 4.5. "camp family"? Maybe "keep the family".

# 11. POqdsxCvjGM_q02 (Band 4.5)
# Transcript: "sik religious guaras... most popular most pop place... sports Market industry... football CH side... Road Road maintenance... face less difficulties... migrating from other other cities... traffic lights..."
# Analysis:
# - Grammar: "maintenance of the roads which are going to be... definitely government should have" (broken). "population is also that increased".
# - Vocabulary: "migrating", "maintenance".
# - Verdict: Band 4.5/5.0. Repetitive and broken structures.

# 12. POqdsxCvjGM_q03 (Band 4.5)
# Transcript: "thred places... shopping areas... people do not think that what other person is facing the problem due to their own shouting..."
# Analysis: "thred places" (crowded?). "facing the problem due to".
# - Verdict: Band 4.5.

# 13. POqdsxCvjGM_q05 (Band 4.5)
# Transcript: "Physical training work or yoga... facing lot of physical problems... pain in their some body parts... prefer to sit at home... experienced... spent his half life... pursue your goals... modern techniques..."
# Analysis:
# - Grammar: "facing lot of" (a lot of). "pain in their some body parts". "is already spent his half life" (has spent half his life).
# - Verdict: Band 5.0. "pursue your goals" is a good chunk.

# 14. XNI7Jg2PzVc_q02 (Band 4.5)
# Transcript: "placed in the near of a quarter line... two season... summer and winter... never experience like snow... a lot of humid and hot..."
# Analysis: "placed in the near of a quarter line" (located near the equator?). "two season" (seasons). "a lot of humid" (very humid).
# - Verdict: Band 4.5. Meaning requires effort ("quarter line" = equator).

# 15. XNI7Jg2PzVc_q03 (Band 4.5)
# Transcript: "work in a workplace that a lot of hot exposed into my workplace... prefer a cool one..."
# Analysis: "hot exposed into" (heat exposure?).
# - Verdict: Band 4.5.

# 16. XNI7Jg2PzVc_q04 (Band 4.5)
# Transcript: "weather sometimes is not stable... postpone my activity is going where the weather is going too hot... hit by like strike of the sun..."
# Analysis: "is going where" (when). "strike of the sun" (sunstroke / heatstroke).
# - Verdict: Band 4.5.

# 17. XNI7Jg2PzVc_q05 (Band 4.5)
# Transcript: "not a big fan... manga... mana... came from Korea... love to read it."
# Analysis: "mana" (manhwa). Basic.
# - Verdict: Band 5.0.

# 18. XNI7Jg2PzVc_q06 (Band 4.5)
# Transcript: "story books... if I have a mood... historical book... related with my country history... culture of our ancestor."
# Analysis: "have a mood" (am in the mood). "ancestor" (ancestors).
# - Verdict: Band 5.0.

# 19. XNI7Jg2PzVc_q07 (Band 4.5)
# Transcript: "read books is just at my free time... not too often... two times a week... depends on my mood."
# Analysis: "read books is just" (I just read books).
# - Verdict: Band 5.0.

# 20. XNI7Jg2PzVc_q08 (Band 4.5)
# Transcript: "remember vividly... history of my country... knowing like a lot of new facts that I did not ever know before."
# Analysis: "remember vividly". "knowing like" (learning).
# - Verdict: Band 5.0.

scored_samples = [
    {
        "id": 0, "sample_id": "bbQjI9CrJak_q01", "video_id": "bbQjI9CrJak",
        "part": 2,
        "question": "Trip with whom?",
        "transcript": "I think that I will go there with my sister because she share the same like the same interest with me and she all she also have plan to come there to study abroad so I think is perfect to go with my baby sister and why I say that a short amount of time is suitable for me is that because I am a family orientated person so I would like to leave near my parents in order to take care of them",
        "word_count": 81,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "verb_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["study abroad", "family orientated"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'she share' (shares). 'have plan' (has a plan). 'leave near' (live near)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent basic errors.",
                "why_not_5": "Complex sentences attempted."
            },
            "vocabulary": {
                "why_not_7": "Errors.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Adequate. Band 6.",
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "x51j2qcODVo_q01",
        "video_id": "x51j2qcODVo",
        "part": 1,
        "question": "Social media?",
        "transcript": "Firstly I would like to talk about social media do you use any social media platforms currently I am using Facebook and messenger it is such a great way that social media I provide a platform where I could contact my friend and call them out to hang out and share my thoughts and what do you use these media platforms for as I said before I usually use this to contact my friend to to create some hangout event or to share my thought on social media do you think social media is toxic in my opinion I do not think that it is that toxic like in Vietnam context it is quite toxic because it rfor in the toxicity in on social media but overall I think that is okay have you ever seen inappropriate content on social media somehow I I do see inappropriate image on social media although that I block them like every time so I do not know the algorithm but I I must agree that inappropriate image is a thing and is common on social media.",
        "word_count": 182,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["toxic", "algorithm", "inappropriate content", "hang out"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'call them out' (ask them out). 'share my thought' (thoughts). 'rfor' (?)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Minor phrasing issues.",
                "why_not_5": "Good flow."
            },
            "vocabulary": {
                "why_not_8": "Some inaccuracy.",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('toxic', 'algorithm'). Band 7.",
        "grammar_reason": "Phrasing errors. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "X0SQAUJ0C5U_q02",
        "video_id": "X0SQAUJ0C5U",
        "part": 2,
        "question": "Friend description?",
        "transcript": "obsessed with her because her creativity in writes lyrics and songs would you like to be a celebrity in the future actually if i be honest no cause I am so scared of being famous or reputable for reputation and i think reputation maybe changed me and i do not like it at all okay so now I will give you a piece of paper and you have time to think about this question around one minute after that you should talk around two minutes okay is that clear yeah yeah so thank you sir you are thank you and this is so okay all right thank you very much okay i have a thomas friend of mine he is so cheerful and he is so kind and we have a lot of things in common actually we have met each other when we went to university and he was my classmate and i think he is so unique and he is he is so thoughtful and he has a lot of wisdom and it is a lot of fun that is going out with him and we all we sometimes go to cafe and talk about cinema movies and philosophy and something like that and we have I am so enjoy to spend time to him yes he is my best friend now and he is the reason that I am like to the cinema I am like to be a filmmaker in the future very good what types of people interact easily with each other i think in this world in modern world actually the narrow-minded people it is so hard to get along with other people you know because they have own ideas and how like they are so dogma a dogmatic person and it is not works.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form", "preposition"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["narrow-minded", "dogmatic", "wisdom", "thoughtful"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'enjoy to spend time to him' (spending time with). 'reputable for reputation'. 'not works' (doesn't work)."
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex ideas."
            },
            "vocabulary": {
                "why_not_8": "Inaccuracies.",
                "why_not_6": "Sophisticated words ('dogmatic')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "High level words ('dogmatic') pull up score despite errors. Band 7.",
        "grammar_reason": "Frequent errors ('enjoy to spend'). Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "X0SQAUJ0C5U_q03",
        "video_id": "X0SQAUJ0C5U",
        "part": 3,
        "question": "Interaction types?",
        "transcript": "In our modern world okay and what type of people interact easily with others i think is it going people is it going people and not non-wisdom people or is it going i mean that go along with everything not so there is no big deal with everything and yes they are so live at moments actually and little moments and they are so happier than other people do people now have enough time for communication after colonel virus pandemic i think the communication lasts his meaning actually it is close to the social media and just we just saw and meet each other in social media for in instagram and so i think in this pandemic communication is so harder than before does technology make it easier to communicate with family and friends can you read reread your question from yeah does technology make it easier to communicate with family and friends yes for example for the students all around the world that is far from their family it is so easier to connect with their family and friends and it is so good and yes technology it is help people right now",
        "word_count": 182,
        "analysis_metadata": {
            "grammar_error_patterns": ["coherence", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["pandemic", "social media"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["coherence_breakdown"],
            "vocabulary": ["meaning_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'is it going' (easy-going?). 'lasts his meaning' (lost its meaning?). 'so easier' (much easier)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "moderate",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "high",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Incoherent parts.",
                "why_not_5": "Structure attempts."
            },
            "vocabulary": {
                "why_not_7": "Unclear meaning.",
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
        "grammar_reason": "Breakdowns in coherence. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "X0SQAUJ0C5U_q04",
        "video_id": "X0SQAUJ0C5U",
        "part": 3,
        "question": "Health/Diseases?",
        "transcript": "And first of all they should care about their mental health and when improve them and mental issues they should go along with another people and then care about themselves for example in checkup in every month and the government should help these people too okay do you think that in the future there will be fewer diseases in the future i do not know i i do not think so the fewer diseases must be half must we have in the future but i think the solution of hill healing is much better than these days and and i think educational people and medicine is so expanded in the future",
        "word_count": 107,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["mental health", "checkup"],
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
            "reason": "'solution of hill healing' (healing?). 'fewer diseases must be half' (?)."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex attempts."
            },
            "vocabulary": {
                "why_not_7": "Errors.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Adequate. Band 6.",
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "BshvbR37Uow_q01",
        "video_id": "BshvbR37Uow",
        "part": 3,
        "question": "Travel past vs present?",
        "transcript": "Do you think traveling was better in the past than it is now I think it is a tough question because I believe that in the past or at the present it all have the advantages on the specific effect aspect that we have to consider so for example in the past it traveling is feel like is more of an adventure so there was no information Rel readily at that time so we got to travel more and it has the lower slower paste of a mode of transportation like like we have trains or buses and it allows us to you know take the traveling more relaxing and we can immerse ourselves with the surroundings however these days with the technological advancement in in trans transportation and everything like that it makes the U traveling more easier and everyone can you know afford it like you know we have apps we have we can schedule days book and accommodations everything like that everything is more easier",
        "word_count": 164,
        "analysis_metadata": {
            "grammar_error_patterns": ["comparative", "agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["technological advancement", "immerse ourselves", "accommodations"],
            "grammar_structures_used": ["complex_sentences", "comparatives"]
        },
        "micro_flaws": {
            "grammar": ["comparative_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'more easier' (easier). 'slower paste' (pace). 'traveling is feel like' (feels like)."
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "moderate",
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
                "why_not_9": "Comparative error.",
                "why_not_7": "Good complexity."
            },
            "vocabulary": {
                "why_not_9": "'paste' error.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level vocab ('immerse'). Band 8.",
        "grammar_reason": "Comparative error 'more easier'. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "tCg4KBkXNG4_q01",
        "video_id": "tCg4KBkXNG4",
        "part": 3,
        "question": "Tech importance?",
        "transcript": "I feel like it has become not only a tool but but like an has changed into like an integral part of our life and becomes for me it is become like my personal best friend because it not only knows my personal data it also holds a lot of my online money and a lot of my knowledge about a lot of stuff. it it not only became a tool for me to utilize but I can learn a lot from the technology as well because from my personal experience I feel like my phone is not only a tool for me to do transactions to acquire new knowledge and is a way for me to track locations around me but I can but it can be benefits me a Because nowadays you do not need like a big laptop or other tech technological devices to you know work effectively. You can just works with a phone and I think it is really good. Fantastic.",
        "word_count": 165,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["integral part", "transactions", "acquire new knowledge"],
            "grammar_structures_used": ["not_only_but_also"]
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
            "reason": "'can be benefits me' (can benefit me). 'just works' (work)."
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
                "why_not_9": "Minor errors.",
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
        "vocab_reason": "Precise terms. Band 8.",
        "grammar_reason": "Mostly error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "eEA5PY_bbDk_q03",
        "video_id": "eEA5PY_bbDk",
        "part": 1,
        "question": "Games/Family?",
        "transcript": "Computer games and i think if i play computer game i will i will not have time for my homework okay and last one are friends more important than family i think friends or family is important my friend helped me happier relax and help me and i can talk about my friend secret things and now my family is the home and my parents helped me understand and teach me a lot of things when i was born okay finish it yes good job yes yeah you can take it yes goodbye.",
        "word_count": 92,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["homework"],
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
            "reason": "'helped me happier' (help me be happier). 'when i was born' (since?)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Frequent errors.",
                "why_not_3": "Can form sentences."
            },
            "vocabulary": {
                "why_not_5": "Basic.",
                "why_not_3": "Adequate for task."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Cannot use sentence forms except in memorised phrases.",
            "vocabulary_band": 4,
            "vocabulary_text": "Uses basic vocabulary."
        },
        "vocab_reason": "Basic. Band 4.",
        "grammar_reason": "Errors. Band 4.",
        "vocabulary": 4,
        "grammar": 4
    },
    {
        "id": 0, "sample_id": "tl1ERXjlPAE_q01",
        "video_id": "tl1ERXjlPAE",
        "part": 1,
        "question": "Intro?",
        "transcript": "what is your name so my name is Hong but you can call me Anne and how old are you I am currently 17 I will be turning 18 next month",
        "word_count": 31,
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
                "why_not_6": "Simple.",
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
            "vocabulary_text": "Uses limited vocabulary."
        },
        "vocab_reason": "Basic. Band 5.",
        "grammar_reason": "Accurate simple sentences. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "tl1ERXjlPAE_q02",
        "video_id": "tl1ERXjlPAE",
        "part": 1,
        "question": "Roles?",
        "transcript": "And wives have different roles within the family can you repeat the question should husbands and wives have different roles within the family I think they do because I think for Vietnamese cultural the husband is usually the one to go outside and make money and the wife is the one who did stay home and cook it do the cooking but I think both of them have the same role because they all the they want to do control of the family to keeping up the camp family okay which are more important to you your family or your friends so I am more an introvert person so I spend most of my time with my family because they the one who know me the best but sometimes I do go out hang out with my friends okay you can take this one.",
        "word_count": 133,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["introvert", "hang out"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'did stay home' (stays). 'keeping up the camp family' (?)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent errors.",
                "why_not_4": "Meaning clear mostly."
            },
            "vocabulary": {
                "why_not_6": "Basic range.",
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
        "id": 0, "sample_id": "POqdsxCvjGM_q02",
        "video_id": "POqdsxCvjGM",
        "part": 1,
        "question": "Hometown?",
        "transcript": "In zand are very very famous and like some of the sik religious guaras in the sultanpur side are very famous okay if I may ask which is the most popular place in your hometown the most popular place in my hometown in my hometown if according to me the most popular most pop place in my hometown is the sports Market industry which is near to the football CH side and it is well known for its Sports food production only okay so what changes you think there would be in your hometown in future if I talk about the changes which which will be promoted in the future according to according to me it will be the first the first change which I which I will talk about is the Road Road maintenance of the roads which are going to be which which are going to be definitely government should have should have to work on it so that the people of my city Can U face less difficulties to travel from one place to another and the other thing is that here there with the with the advancement and a lot of number a lot of people now migrating from other other cities to the other cities to here due to which population is also that increased and a lot of traffic problems also so according to me more traffic lights will be introduced in the future okay is there anything that you do not like about your hometown to be honest I I do not think so there are too many there are so many things I will talk about only one thing which I do not.",
        "word_count": 272,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["maintenance", "migrating", "advancement"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Severe repetition and broken structure. 'which which are going to be definitely government'."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Broken sentences.",
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
        "vocab_reason": "Adequate. Band 5.",
        "grammar_reason": "Broken structures. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "POqdsxCvjGM_q03",
        "video_id": "POqdsxCvjGM",
        "part": 1,
        "question": "Dislike?",
        "transcript": "Like it is the it is some it is the thred places which which is mostly in the shopping areas in that I will I I do not like that places because people do not think that what other person is facing the problem due to their own shouting and other things and and if I and the other and that place okay G so.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["facing the problem"],
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
            "reason": "'thred places' (crowded?). 'facing the problem due to'."
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
        "id": 0, "sample_id": "POqdsxCvjGM_q05",
        "video_id": "POqdsxCvjGM",
        "part": 3,
        "question": "Young and Old?",
        "transcript": "Physical training work or yoga sessions or meditation something like that and so people are busy in the in their cell phones due to which they are facing lot of physical problems like pain in their some body parts in their knees and in the old age and other problem is that people in the old age right now are only prefer to sit at home they do not want to go anywhere they only want to spend their time with their small younger children with in their family okay so do you think is it possible to have friendship between people who are young and people who are old yes and definitely it is a very good thing if if you have a if you have a old friend because you will have to learn so many things which he is already experienced because because that person is already spent his half life so he is more experienced than you and in the outer world he will teach you so many things that what is right for you what is what is going to happen if you will do this thing and what you will have to do to pursue your goals in the future okay what can old people learn from the younger generation if from if I will talk about people what they will learn from Young Generation is mostly the tech techniques like modern techniques of the using cell phones using computers and the other things to other things like playing the new traditional trend of traditional trend of that old playing the old culture games on their cell phones only okay so thank you gorov we will.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "article"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["meditation", "pursue your goals", "modern techniques"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'facing lot of' (a lot of). 'already spent his half life' (has spent). 'traditional trend' (?)."
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent errors.",
                "why_not_4": "Meaning clear."
            },
            "vocabulary": {
                "why_not_6": "Errors.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Adequate. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "XNI7Jg2PzVc_q02",
        "video_id": "XNI7Jg2PzVc",
        "part": 1,
        "question": "Weather?",
        "transcript": "Indonesia is placed in the near of a quarter line. So, I could say that we had just two season here. it is summer and winter. So, we never experience like snow or a fall or something. So, it is I could say that the weather is a lot of humid and hot. I could say.",
        "word_count": 53,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "agreement"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["humid"],
            "grammar_structures_used": ["simple_sentence"]
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
            "reason": "'quarter line' (equator). 'two season' (seasons). 'a lot of humid' (very humid)."
        },
        "grammar_profile": {
            "complexity_level": "low",
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
                "why_not_6": "Frequent errors.",
                "why_not_4": "Understandable."
            },
            "vocabulary": {
                "why_not_6": "Wrong words ('quarter line').",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Errors. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "XNI7Jg2PzVc_q03",
        "video_id": "XNI7Jg2PzVc",
        "part": 1,
        "question": "Prefer weather?",
        "transcript": "generally I work in a workplace that a lot of hot exposed into my workplace. So I will prefer a cool one for the best weather.",
        "word_count": 25,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["workplace"],
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
            "reason": "'hot exposed into' (heat exposure?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
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
        "id": 0, "sample_id": "XNI7Jg2PzVc_q04",
        "video_id": "XNI7Jg2PzVc",
        "part": 1,
        "question": "Weather affect?",
        "transcript": "The weather sometimes is not stable here in my area. So I will postpone my activity is going where the weather is going too hot. So I will wait until evening for example. If not I am just like going to hit by like strike of the sun.",
        "word_count": 47,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["postpone"],
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
            "reason": "'strike of the sun' (sunstroke?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Errors.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Errors.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Errors. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "XNI7Jg2PzVc_q05",
        "video_id": "XNI7Jg2PzVc",
        "part": 1,
        "question": "Reading?",
        "transcript": "I could say that I am not a big fan of reading books but sometimes when I found like I can say like a manga for example or like mana it is the same like manga but it came from Korea I would really love to read it.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["not a big fan"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'when I found' (find)."
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
                "why_not_6": "Tense error.",
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
        "id": 0, "sample_id": "XNI7Jg2PzVc_q06",
        "video_id": "XNI7Jg2PzVc",
        "part": 1,
        "question": "Book types?",
        "transcript": "About type of book. I would really love to read like a story books but sometimes if I have a mood I will try to find about historical book that maybe related with my country history or like another country history so I can learn about the culture of our ancestor.",
        "word_count": 50,
        "analysis_metadata": {
            "grammar_error_patterns": ["article", "agreement"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["culture"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'story books' (storybooks). 'have a mood' (am in the mood). 'ancestor' (ancestors)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
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
        "id": 0, "sample_id": "XNI7Jg2PzVc_q07",
        "video_id": "XNI7Jg2PzVc",
        "part": 1,
        "question": "How often read?",
        "transcript": "I read books is just at my free time. I could say that maybe not too often. I could say maybe just like two times a week or three times. It really depends on my mood as well.",
        "word_count": 37,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["depends on my mood", "free time"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'I read books is just' (I just read books)."
        },
        "grammar_profile": {
            "complexity_level": "low",
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
                "why_not_6": "Structure error.",
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
        "id": 0, "sample_id": "XNI7Jg2PzVc_q08",
        "video_id": "XNI7Jg2PzVc",
        "part": 1,
        "question": "Last book?",
        "transcript": "I still remember vividly that I have read a book about history of my country and I found it really fascinating that knowing like a lot of new facts that I did not ever know before.",
        "word_count": 35,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["remember vividly", "fascinating"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'fascinating that knowing' (fascinating learning / to learn)."
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
                "why_not_6": "Structure error.",
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
