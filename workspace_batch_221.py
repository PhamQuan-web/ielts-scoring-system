import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 221 ---
# Total Samples: 20
# Samples Analyzed:

# 1. 0ZizySMJwp4_q04 (Band 5.0)
# Transcript: "breathe into the best along na... I am actually love sleeping... relax and regress..."
# Analysis: "breathe into the best" (?). "am actually love" (I actually love). "regress" (decompress/rest?).
# - Verdict: Band 5.0.

# 2. 0ZizySMJwp4_q05 (Band 5.0)
# Transcript: "prefer comfortable shoes... when I we comfortable sho and get tired feel quickly... although good looking and nice but comfor... low co store... owe too many shoes... wear one soul... excite and hang out..."
# Analysis: "when I we comfortable sho" (wear comfortable shoes). "owe too many" (own). "low co store" (low cost). "wear one soul" (sole/pair?).
# - Verdict: Band 5.0.

# 3. FChTo7oqaTE_q02 (Band 6.0)
# Transcript: "Prices to I do not want to absolutely okay so yeah."
# Analysis: Fragment. "Prices to" (Prices are too...).
# - Verdict: Band 5.5/6.0. Very short.

# 4. 6EmlEFalEow_q01 (Band 5.5)
# Transcript: "My name is Sang. Hello, Sang. So, today I will be your examiner..."
# Analysis: Candidate said name. Examiner spoke the rest.
# - Verdict: Valid (Band 5.5).

# 5. 6EmlEFalEow_q02 (Band 5.5)
# Transcript: "Honestly, I do not like sport. So I usually spend my time for green books and also working."
# Analysis: "green books" (reading books?). "spend my time for" (on).
# - Verdict: Band 5.5.

# 6. 6EmlEFalEow_q03 (Band 5.5)
# Transcript: "I used to play football when good and such really long time ago already."
# Analysis: "when good" (when I was a kid?). "such really long time" (such a long time).
# - Verdict: Band 5.0/5.5.

# 7. 6EmlEFalEow_q04 (Band 5.5)
# Transcript: "I guess still football... people play football a lot and they usually also go swimming."
# Analysis: "I guess still football" (I guess it's still football).
# - Verdict: Band 5.5.

# 8. _ZTTjQE0p48_q02 (Band 5.0)
# Transcript: "Describe a toy that you liked when you were a kid..."
# Analysis: EXAMINER INSTRUCTION / CARD READING.
# - Verdict: INVALID (Skip).

# 9. 5Df0dc-u1HI_q04 (Band 5.5)
# Transcript: "confidence for the IELTS exam... download cambly today..."
# Analysis: ADVERTISEMENT.
# - Verdict: INVALID (Skip).

# 10. 5Df0dc-u1HI_q06 (Band 5.5)
# Transcript: "I will as I said I was happy to that he helped me so quick in my needs and I invite invited him and his whole family to to barbecue at our house."
# Analysis: "happy to that" (happy that). "helped me so quick" (quickly). "invite invited".
# - Verdict: Band 5.5.

# 11. VCyrYwvDbhI_q04 (Band 5.5)
# Transcript: "take their climbing stick and mountain back... easily found them... work-life balance is broken... just watch a movie eating snacks... not good experts... people does not people do not like the competition... got burdened depends on their roles... protect the goal..."
# Analysis: "mountain back" (backpack?). "easily found them" (find). "not good experts" (not experts / not good at it). "people does not" (do not).
# - Verdict: Band 5.5.

# 12. VCyrYwvDbhI_q05 (Band 5.5)
# Transcript: "need one bull... famous star in our career... pakison... played soccer very well... in a role of striker... world war between man and girl is broken... rough sport... stretch thing... good education for them to force them..."
# Analysis: "one bull" (ball). "in our career" (Korea). "pakison" (Park Ji-sung). "world war... is broken" (barrier/wall is broken). "man and girl" (men and women).
# - Verdict: Band 5.5. "World war" is a strange choice for "gender gap/barrier".

# 13. VCyrYwvDbhI_q08 (Band 5.5)
# Transcript: "terrible at okay always at... depends on people right it should be it depends on the person... wording of questions... I will go over the whole thing with you later..."
# Analysis: EXAMINER FEEDBACK.
# - Verdict: INVALID (Skip).

# 14. -idzfr3SUog_q02 (Band 6.5)
# Transcript: "prefer to go international cuisine... eat an international food like a sushi... choose a food... playing piano... relaxing thing for for getting energy..."
# Analysis: "go international cuisine" (go for). "an international food" (international food - uncountable). "a sushi" (sushi). "playing piano" (playing the piano).
# - Verdict: Band 6.0. Articles issues.

# 15. -idzfr3SUog_q04 (Band 6.5)
# Transcript: "for for understand about it better... if they have not enough time... prefer to the parents help them... maybe they one for example students do not have any person... not important have a degree... experience experiences..."
# Analysis: "for understand" (to understand). "have not enough" (do not have). "prefer to the parents help" (prefer parents to help). "experience experiences".
# - Verdict: Band 6.0.

# 16. hXEZgYzVCLo_q02 (Band 6.0)
# Transcript: "your topic today is talk about an unexpected event turn out to be happy event that you have in your life"
# Analysis: EXAMINER INSTRUCTION.
# - Verdict: INVALID (Skip).

# 17. hXEZgYzVCLo_q03 (Band 6.0)
# Transcript: "depends on how old the children are... under grade seven the parents need to choose... ordered around like after grade eight... make their brilliant their mind probably more creative... enjoyed inserting both... study online I usually do not listen... didn't get to play games a lot in Nuka... focus on my study more offline..."
# Analysis: "ordered around" (older?). "inserting both" (doing both?). "Nuka" (?). "make their brilliant their mind" (make their minds brilliant?).
# - Verdict: Band 6.0.

# 18. w6n1M3NJoG4_q02 (Band 5.5)
# Transcript: "listen to K-pop and pop music... spare time... go to concert... biased idols."
# Analysis: "go to concert" (concerts). "biased idols" (favorite idols - 'bias' is K-pop slang).
# - Verdict: Band 5.5.

# 19. w6n1M3NJoG4_q03 (Band 5.5)
# Transcript: "17 is my favorite guru which is the one of the most famous idol in Korea."
# Analysis: "guru" (group). "famous idol" (idols).
# - Verdict: Band 5.5.

# 20. w6n1M3NJoG4_q04 (Band 5.5)
# Transcript: "younger sister loves the same idol with me. So she hang out with me usually... really beneficial for me."
# Analysis: "same idol with me" (as me). "she hang out" (hangs).
# - Verdict: Band 5.5.

scored_samples = [
    {
        "id": 0, "sample_id": "0ZizySMJwp4_q04", "video_id": "0ZizySMJwp4",
        "part": 1,
        "question": "After work?",
        "transcript": "To be honest, my favorite thing is just breathe into the best along na because I am actually love sleeping. Usually I go out with friend while I listen to some music. YES. it is a good way for me to relax and regress.",
        "word_count": 41,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form", "coherence"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["relax"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": ["meaning_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'breathe into the best along na' (unclear/incoherent). 'am actually love' (actually love). 'regress' (relax?)."
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
                "why_not_4": "Meaning mostly clear."
            },
            "vocabulary": {
                "why_not_6": "Incoherent phrases.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic/Unclear. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "0ZizySMJwp4_q05",
        "video_id": "0ZizySMJwp4",
        "part": 1,
        "question": "Shoes?",
        "transcript": "I prefer comfortable shoes bu when I we comfortable sho and get tired feel quickly. YES. So although good looking and nice but comfor you need to spend a lot of money on shoes no I do not think so because I can buy that can have both the same quality and affordable and I usually start at the low co store and try to find sales rather than mine because people owe too many shoes? Yes, I think people too because I usually see people playing two or three and they only wear one soul. So for me only three or four this one event like work, excite and hang out.",
        "word_count": 109,
        "analysis_metadata": {
            "grammar_error_patterns": ["coherence", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["affordable", "sales"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["coherence_breakdown"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'we comfortable sho' (wear comfortable shoes). 'low co store' (low cost). 'owe too many' (own). 'wear one soul' (sole/pair)."
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
                "why_not_6": "Frequent breakdowns.",
                "why_not_4": "Understandable."
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
        "vocab_reason": "Errors. Band 5.",
        "grammar_reason": "Breakdowns. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "FChTo7oqaTE_q02",
        "video_id": "FChTo7oqaTE",
        "part": 1,
        "question": "Prices?",
        "transcript": "Prices to I do not want to absolutely okay so yeah.",
        "word_count": 11,
        "analysis_metadata": {
            "grammar_error_patterns": ["incoherence"],
            "grammar_error_frequency": "dominant",
            "vocab_collocation_usage": "none",
            "vocab_evidence": [],
            "grammar_structures_used": ["fragment"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "none",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "none",
            "accuracy_level": "none",
            "flexibility": "none",
            "error_density": "dominant"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "high",
            "development_depth": "none"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Fragment.",
                "why_not_4": "No structure."
            },
            "vocabulary": {
                "why_not_6": "None.",
                "why_not_4": "Basic."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Produces simple sentences accurately.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses limited vocabulary."
        },
        "vocab_reason": "Basic. Band 5.",
        "grammar_reason": "Fragment. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "6EmlEFalEow_q01",
        "video_id": "6EmlEFalEow",
        "part": 1,
        "question": "Name?",
        "transcript": "My name is Sang. Hello, Sang. So, today I will be your examiner and we will start with test one and then task two and task three of the speaking test. Okay, so let us start it. firstly I will ask you some questions related to sports and games.",
        "word_count": 47,
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
                "why_not_7": "Too short/Examiner speech mixed.",
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
        "id": 0, "sample_id": "6EmlEFalEow_q02",
        "video_id": "6EmlEFalEow",
        "part": 1,
        "question": "Favorite sport?",
        "transcript": "Honestly, I do not like sport. So I usually spend my time for green books and also working.",
        "word_count": 17,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["spend my time"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'spend my time for' (on). 'green books' (reading?)."
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
                "why_not_6": "Preposition error.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Unclear term 'green books'.",
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
        "id": 0, "sample_id": "6EmlEFalEow_q03",
        "video_id": "6EmlEFalEow",
        "part": 1,
        "question": "Younger sport?",
        "transcript": "I used to play football when good and such really long time ago already.",
        "word_count": 13,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["used to play"],
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
            "reason": "'when good' (when I was a kid?). 'such really long time' (a long time)."
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
                "why_not_6": "Structure breakdown.",
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
        "grammar_reason": "Structure errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "6EmlEFalEow_q04",
        "video_id": "6EmlEFalEow",
        "part": 1,
        "question": "Popular sport?",
        "transcript": "I guess still football in my hometown people play football a lot and they usually also go swimming.",
        "word_count": 17,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["go swimming"],
            "grammar_structures_used": ["compound_sentence"]
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
            "reason": "'guess still football' (it is still)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Missing subjects.",
                "why_not_4": "Clear."
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
        "grammar_reason": "Fragment. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "5Df0dc-u1HI_q06",
        "video_id": "5Df0dc-u1HI",
        "part": 3,
        "question": "Thank friend?",
        "transcript": "Do for your friend to thank him for helping you in this situation I will as I said I was happy to that he helped me so quick in my needs and I invite invited him and his whole family to to barbecue at our house.",
        "word_count": 46,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["barbecue"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'happy to that' (happy that). 'so quick' (quickly). 'invite invited' (invited)."
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
                "why_not_6": "Frequent errors.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Form errors.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Form errors. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "VCyrYwvDbhI_q04",
        "video_id": "VCyrYwvDbhI",
        "part": 3,
        "question": "Hiking/Sports?",
        "transcript": "It is hiking and we can see many other elder group a group of other people who who take their climbing stick and mountain back to go to mountain we can easily found them at near the at the subway station near the mountain because they can do conversation with them with each other and also it is the easiest easy hobby that can enjoy in korea because there is so many mountains in korea okay do you think younger people like to go hiking no i do not think so nowadays there is so many gyms so young people can in enjoy workout at the gym so sometimes they enjoy it but not that much okay and do you think people exercise more these days compared to the past it is depend on people but in my opinion i think they are not because nowadays the work-life balance is broken because of the overwork so after after the work at the company people just come back to their house and just sleep just enjoy the extra time at the day with just watch a movie eating snacks so i think nowadays people not try to do out okay and why do some people hate playing sports simply there is some the reason of some people hate the sport is simply they are not good experts and another reason is people does not people do not like the competition like sports and workout is different sport is something like competition like soccer basketball so people got burdened depends on their depends on their depend on their roles in that sport like as a core people have to protect the goal from the others other strikers kit yeah and what sports do you think are popular in your country in my.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "verb_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["work-life balance", "competition", "workout"],
            "grammar_structures_used": ["complex_sentences"]
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
            "reason": "'mountain back' (backpack). 'easily found them' (find). 'people does not' (do not). 'got burdened' (feel burdened)."
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
                "why_not_5": "Complex structures attempted."
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
        "vocab_reason": "Adequate range ('work-life balance'). Band 6.",
        "grammar_reason": "Frequent errors. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "VCyrYwvDbhI_q05",
        "video_id": "VCyrYwvDbhI",
        "part": 1,
        "question": "Sports?",
        "transcript": "Country soccer and baseball I am a fan of on soccer i think it is easy to play to enjoy it we just need one bull and also there is a famous star in our career in my country his name is pakison he he is very he is played soccer very well and he plays he is in a role of striker in manchester united before so that is why korean people like soccer in baseball i like it i like baseball okay and do you think is there any difference between gender when it comes to the sports they like it is so okay how can i explain it gender in our country or in general in the world in general nowadays the world war between between man and girl is broken instead broken constantly but i think yes there is a difference between men and girl usually men like to play soccer and rugby like a rough sport but girl like go like pilates yoga it is such a stretch thing but it is not a stereotype but i think like this okay okay and if children are not interested in sport should their parents like force them or make them try new sports can i hear one more time sure if a child is not interested in sports should their parents force them to try new sports no they do not they do not need i think because children can find any other hobbies like like draw a picture draw a picture take a picture or or sing a song it can be a it can be a it can instead of the outside activity expert and also i think it is not a good education for them to force them okay all right mate that will do us that is our.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "tense"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "mixed",
            "vocab_evidence": ["striker", "rough sport", "stereotype"],
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
            "reason": "'world war between man and girl' (gender barrier?). 'one bull' (ball). 'played soccer very well' (plays). 'stretch thing' (stretching?)."
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
                "why_not_5": "Complex structures used."
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
        "vocab_reason": "Adequate ('stereotype', 'rough sport'). Band 6.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "-idzfr3SUog_q02",
        "video_id": "-idzfr3SUog",
        "part": 1,
        "question": "Eat out?",
        "transcript": "Do you like to eat out at to be honest i prefer to go international cuisine and i like to eat an international food like a sushi or an italian food and what would your perfect meal be altogether could you please repeat your question sure what would your perfect meal be i if i want to choose a food i like to choose for example an italian food like a pasta or a pizza great I would like now to talk about your hobbies tell me about any hobbies you have okay to be honest these days i do not have enough free time but if i have free time i usually i like playing volleyball with my friends or reading reading books are there any hobbies you would like to have in the future yes if i if i can choose a a hobby i would choose for example playing piano because i like it wonderful and do you think hobbies should be relaxing or should they be exciting well if i want to choose a hobby i prefer to choose a relaxing hobby because these days I am very busy and i prefer to choose a relaxing thing for for getting energy wonderful okay now I am going to give you a topic and I would like you to talk about it for one to two minutes.",
        "word_count": 213,
        "analysis_metadata": {
            "grammar_error_patterns": ["article", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["international cuisine", "relaxing hobby"],
            "grammar_structures_used": ["conditionals"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": ["collocation_minor"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'go international cuisine' (go for). 'an international food' (international food). 'a sushi' (sushi). 'playing piano' (the piano)."
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
                "why_not_7": "Article errors.",
                "why_not_5": "Complex structures."
            },
            "vocabulary": {
                "why_not_7": "Collocation issues.",
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
        "grammar_reason": "Errors present. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "-idzfr3SUog_q04",
        "video_id": "-idzfr3SUog",
        "part": 3,
        "question": "Homework/Education?",
        "transcript": "Should do some homework about it for for understand about it better and if they want to use them in the situation in this situation i think they can use better than other situations right and how much homework should they be given do you think i think they should do homework every day but if they have not enough time they can do their homework for example three or four times a week but i prefer but i prefer to do the do for example my homework every day and do you think parents should help their children with their homework or should it be done alone to be honest i prefer to the parents help them but in some situation i think it is better they do their homework alone because maybe they one for example students do not have any person for helping them okay and we will now discuss the relationship between education and work how important is it to have a university education to get a job in your country to be honest i have never thought about it but i think in my car especially in my country people when whenever they want to find a job it is not important have a degree or not it is important to have some experience experiences and after that i think they can they can find a good job and does having a degree from another country enhance employment opportunities in your country you please repeat your question absolutely now does having a degree from another country help get a job in your country i think it is not important when a person have a degree of another country because in my country whenever for example.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "verb_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["experience", "degree"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'for understand' (to understand). 'have not enough' (do not have). 'prefer to the parents help' (parents to help). 'not important have' (to have)."
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
        "vocab_reason": "Adequate. Band 6.",
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "hXEZgYzVCLo_q03",
        "video_id": "hXEZgYzVCLo",
        "part": 3,
        "question": "Outdoor Activity?",
        "transcript": "The Outdoor Activity I think it depends on how old the children are because like people when they kids when they are like around eight two I will say like under grade seven the parents need to choose what they need to do out or and because they are not like they are not old enough to know what they are doing and when we are ordered around like after grade eight I think we should the parents should let the children choose what to do because so they can be more independent and to be and to make their brilliant their mind probably more creative yes sir do you enjoy studying online or studying offline to be honest I enjoyed inserting both but when I study online I usually do not listen to the teacher and I just play games but that was like a long time ago since I did not get to play games a lot in Nuka but when now but now I prefer studying offline because because I feel but like because I get to meet my friends and I actually and I actually get to like to like move around and play some sports and stuff with my friends and I get and I actually can focus on my study more offline all right so that is the end of our speaking test today thank you so much foreign bye foreign.",
        "word_count": 232,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_choice"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["independent", "creative", "focus on"],
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
            "reason": "'ordered around' (older?). 'inserting both' (doing both?). 'make their brilliant their mind' (?)."
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
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Adequate. Band 6.",
        "grammar_reason": "Errors present. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "w6n1M3NJoG4_q02",
        "video_id": "w6n1M3NJoG4",
        "part": 1,
        "question": "Hobbies?",
        "transcript": "usually I listen to K-pop and pop music. And so when I have spare time, I usually go to concert to listen live music of my biased idols.",
        "word_count": 28,
        "analysis_metadata": {
            "grammar_error_patterns": ["article"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["spare time", "biased idols"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'go to concert' (concerts). 'biased idols' (bias idols / favorite idols)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
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
                "why_not_7": "Article error.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Slang usage.",
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
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "w6n1M3NJoG4_q03",
        "video_id": "w6n1M3NJoG4",
        "part": 1,
        "question": "Groups?",
        "transcript": "17 is my favorite guru which is the one of the most famous idol in Korea.",
        "word_count": 16,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["relative_clause"]
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
            "reason": "'guru' (group). 'idol' (idols)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Agreement error.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Word choice error.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors. Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "w6n1M3NJoG4_q04",
        "video_id": "w6n1M3NJoG4",
        "part": 1,
        "question": "Share hobbies?",
        "transcript": "Yes, my younger sister loves the same idol with me. So she hang out with me usually. Yeah. And that is really beneficial for me. Yeah.",
        "word_count": 25,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "preposition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["hang out", "beneficial"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'same idol with me' (as me). 'she hang out' (hangs)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Agreement errors.",
                "why_not_5": "Clear."
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
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
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

    print(f"Append complete. Added {count} new samples. (Skipped duplicates/invalid).")

except Exception as e:
    print(f"Error writing to file: {e}")
