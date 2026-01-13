import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 228 ---
# Total Samples: 20
# Valid Samples: 17

scored_samples = [
    {
        "id": 0, "sample_id": "mJhBTa4NX9Y_q03", "video_id": "mJhBTa4NX9Y",
        "part": 1,
        "question": "Business page?",
        "transcript": "Have a page a business page so after getting along with clients i take pictures and i post pictures on my business page so that is why i can attract more clients for improving my work wonderful",
        "word_count": 39,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["attract more clients", "getting along with"],
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
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "mJhBTa4NX9Y_q04",
        "video_id": "mJhBTa4NX9Y",
        "part": 2,
        "question": "Dinner?",
        "transcript": "Dinner so they are accepted and we went to bom land we went to a beautiful restaurant which serves arabic food we had the homos in bubble baja restaurant and the area was beautiful the design was amazing so we spent about like one or two hours there and we started talking about the future how beautiful the life is we can how easy we can enjoy the life with just eating a small food portion of food and enjoying the beautiful weather and being together this is the god mercy that we are together",
        "word_count": 93,
        "analysis_metadata": {
            "grammar_error_patterns": ["articles"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["arabic food", "god mercy"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'the god mercy' (God's mercy). 'homos' (hummus)."
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
                "why_not_9": "Minor slips.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Word choice/ASR.",
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
        "id": 0, "sample_id": "mJhBTa4NX9Y_q05",
        "video_id": "mJhBTa4NX9Y",
        "part": 3,
        "question": "Food culture?",
        "transcript": "Bored not to enjoy the food the way it should be but if you go out not every day i mean if you go outside sometimes and try different kind of food like chinese food mexican food which is my favorite of course and the italian food so you can do people watching you can see a different kind of people you can meet different people and of course taste different kind of food and taste and enjoy the food more right more than eating at home absolutely so what do people usually cook for special festivals we do not have many special festivals like thanksgiving and this kind of stuff in iran we have like a month called ramadan here they do not eat from morning to evening and evening they have a small one very very thin kind of food not to get very not to get problem for the stomach so most of the time they eat ash which is some kind of food there is noodles inside and the yogurt some kind of yogurt inside the ash which is very good for this for the stomach after fasting right so and the very famous most famous food in iran is gourmet that everyone likes it even i have some friends which are not iranian they are crazy about it i cooked maybe two or three times for them and they asked for more wonderful cool and next what more and more people so they are having people are having or getting their meals delivered so would people cook at home these days now in iran yes these days before they used to cook like traditional food which are very common in iran and everyone can eat it but nowadays as far.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["fasting", "ramadan", "traditional food"],
            "grammar_structures_used": ["complex_sentences", "relative_clauses"]
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
            "reason": "'not to get problem for the stomach' (to avoid stomach problems). 'gourmet' (Ghormeh Sabzi)."
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
        "vocab_reason": "Good range. Band 7.",
        "grammar_reason": "Fluent. Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "-BV_IrcRlEQ_q01",
        "video_id": "-BV_IrcRlEQ",
        "part": 1,
        "question": "Style?",
        "transcript": "Interesting question. I feel like my style is diverse. On some days, I just put on a black t-shirt and a jeans and on some other days, it depends on where I am going. I would like to dress up a little bit, put on some fancy clothes, and just go out with it.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["articles"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["diverse", "dress up", "fancy clothes"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'a jeans' (jeans)."
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
                "why_not_9": "Article error.",
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
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "-BV_IrcRlEQ_q02",
        "video_id": "-BV_IrcRlEQ",
        "part": 1,
        "question": "Influences?",
        "transcript": "H it depends on my mood and also it depends where I am going. So for instance, let us say I am going to the gym, of course I am going to be in like sports wear. Or if I am going to a wedding, I have to wear a suit and tie. And if I am going, let us say to a social gathering with my friends, it is just going to be like smart casual or casual clothes.",
        "word_count": 81,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["suit and tie", "smart casual", "social gathering"],
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
                "why_not_7": "Good."
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
        "id": 0, "sample_id": "-BV_IrcRlEQ_q03",
        "video_id": "-BV_IrcRlEQ",
        "part": 1,
        "question": "Style change?",
        "transcript": "A lot actually. See, when I was a teenager, it was kind of like funky or street wear, crazy colors, you know, put on some bracelets, some necklaces, crazy hairstyle. But as you get older, I changed my style a little bit to more u elegant, more simple and less crazy colors.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["street wear", "elegant"],
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
        "id": 0, "sample_id": "-BV_IrcRlEQ_q04",
        "video_id": "-BV_IrcRlEQ",
        "part": 1,
        "question": "Art?",
        "transcript": "Actually it depends because I think art is branched. So for instance art consists of music, theater, cinema and paintings. But for me personally I love art and specifically I love cinema.",
        "word_count": 32,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "creative",
            "vocab_evidence": ["art is branched"],
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
                "why_not_9": "Short.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Creative."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Creative. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "-BV_IrcRlEQ_q05",
        "video_id": "-BV_IrcRlEQ",
        "part": 1,
        "question": "Learn art?",
        "transcript": "sure. I am open for different ideas, different perspectives, especially I am not interested at the moment in let us say paintings or modern art, but I am interested in the future to learn more about it.",
        "word_count": 37,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["open for", "perspectives"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'open for' (to)."
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
                "why_not_9": "Prep error.",
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
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "-BV_IrcRlEQ_q06",
        "video_id": "-BV_IrcRlEQ",
        "part": 1,
        "question": "Relax?",
        "transcript": "Oh, I love relaxing. there is a lot of ways to relax. I could just book a massage session or the most common way and my favorite way is going to the beach on an early morning where it is empty, no one is there. I just grab my stuff, go to the beach and just sit and chill there.",
        "word_count": 59,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["chill", "massage session"],
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
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "-BV_IrcRlEQ_q07",
        "video_id": "-BV_IrcRlEQ",
        "part": 1,
        "question": "Manage stress?",
        "transcript": "Interesting question. there is a lot of ways but the first one I would always use it is just to take deep breath and just slowly exhale and since I am a Muslim guy I I read a lot of Quran so it helps me like calm instantly.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": ["articles"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["exhale", "calm instantly"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'take deep breath' (a deep breath)."
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
                "why_not_9": "Article error.",
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
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Accurate. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "-BV_IrcRlEQ_q08",
        "video_id": "-BV_IrcRlEQ",
        "part": 1,
        "question": "Busy calm?",
        "transcript": "I think just being busy the idea itself it keeps me like calm. I am not a very stressed person in general, but sometimes you get in a trouble or in a situation where it makes you just stressed or anxious. So, I try to cope with it and just like remember that it is not the end of the world. I can just finish the task and be with it.",
        "word_count": 70,
        "analysis_metadata": {
            "grammar_error_patterns": ["articles"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["not the end of the world", "anxious", "cope with it"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": ["idiom_usage"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'be with it' (be done with it?). 'get in a trouble' (get in trouble)."
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
                "why_not_9": "Article error.",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "Phrasing error.",
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
        "id": 0, "sample_id": "-BV_IrcRlEQ_q09",
        "video_id": "-BV_IrcRlEQ",
        "part": 2,
        "question": "Problem solving?",
        "transcript": "Recently a friend of mine asked me about what is the best car option to buy since he was having a lot of issues and problems in his current car. So I was like sure I would give you like few options and the first option was Ford since I own a Ford car and it was a pickup truck. So I would definitely like recommend it for him this option but he told me like I prefer something a little bit smaller and more eco fuel and efficient. I said sure and I gave them a different options about let us say Toyota is a really good option and Nissan they have a variety of options. I really decided to help him since I have the knowledge about the cars and what is good, what is bad, what is like what fits his personality because it is really important to have a car that fits your personality other than the eco fuel system or the fancy look or the color. And I really felt happy helping him about the option and he eventually ended up buying a Ford truck. the reason why he bought this pickup truck because it is a big car and when you drive a big car in the streets, it really helps you and let us say seeing the view from afar to avoid a car accident or a sudden break and at the same time people just avoid come across coming across you and it is just like you feel like a king driving a big car. So, we have been talking about a friend that you helped solve a problem. we are going to continue to talk about problem solving.",
        "word_count": 285,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["variety of options", "fits his personality"],
            "grammar_structures_used": ["complex_sentences", "past_tense"]
        },
        "micro_flaws": {
            "grammar": ["hesitation_markers"],
            "vocabulary": ["repetition_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'sudden break' (brake). 'eco fuel' (fuel efficient)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
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
                "why_not_9": "Hesitations.",
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
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good. Band 8.",
        "grammar_reason": "Fluent. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "-BV_IrcRlEQ_q11",
        "video_id": "-BV_IrcRlEQ",
        "part": 3,
        "question": "Solve alone?",
        "transcript": "For me personally, I like to feel that I am an independent person and try as much as possible to solve a certain problem with my own knowledge and with my own abilities before I go out and ask someone for help. For example, once I had a problem about choosing the right major where I wanted to study. So my parents were actually like trying to suggest for me to study interior design like my brother. But for me I was like no I prefer to choose something that I love. So I ended up choosing the media field and mass communication.",
        "word_count": 102,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["independent person", "mass communication"],
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
        "id": 0, "sample_id": "-BV_IrcRlEQ_q12",
        "video_id": "-BV_IrcRlEQ",
        "part": 3,
        "question": "Emotional intelligence?",
        "transcript": "Oh, it is a big role actually and it is really important to have the emotional intelligence. I did not have it before like when I was younger at in my teenage years also 18 19 because it is a crucial thing to have in helping you like solve problems or solving a conflict. let us say you are having a a discussion with a friend of yours. So if you have the emotional intelligence, you would not change it to become a problem or a big issue between you two. If you have the emotional intelligence, you would just take it as different perspectives between two friends and discussing and exchanging ideas. So it is really important to learn about it if you do not know a lot about the emotional intelligence. Some people think that the best way to help other people is to be as empathetic as possible, while other people think that you should be brutally honest with people.",
        "word_count": 154,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["emotional intelligence", "brutally honest", "empathetic", "exchanging ideas", "different perspectives"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
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
                "why_not_9": "Standard.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level. Band 8.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 8,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "6oD7m25BBQw_q02",
        "video_id": "6oD7m25BBQw",
        "part": 2,
        "question": "Fashionable person?",
        "transcript": "Task I should say is to describe a person who dresses fashionably or well okay that is one minute mhm so now can you describe a person who likes to dress fashionably or well okay one person comes to my mind she is my friend Miss Choy because I am not really sensitive to FAL Trend I am I am not that kind of person so I do not really think of any celebrity and she is making video kind of YouTube something and it is really related to artw work oh I think that is why she is really into that fashion things she mostly wears some which is called Street fashion it looks very funk Punky funky and it is like I think it is over than casual I think it is like too much but she loves it I think she like fashion because it represents her characters because she is working her job is related to art she is she really likes to go to Art Museum and she really loves Modern Art so I think it shows the fashion can show who she is and what she likes and that is why I think I guess she is she loves fashion okay great all right wonderful oh.",
        "word_count": 204,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["street fashion"],
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
            "reason": "'over than casual' (more than). 'represents her characters' (character)."
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
                "why_not_6": "Good flow."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good. Band 7.",
        "grammar_reason": "Errors but good flow. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "zaGEC7FTpIw_q02",
        "video_id": "zaGEC7FTpIw",
        "part": 1,
        "question": "Return trip?",
        "transcript": "Back home the same way I got here by bus then a metro button the opposite direction of course.",
        "word_count": 18,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["opposite direction"],
            "grammar_structures_used": ["simple_sentence"]
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
        "id": 0, "sample_id": "zaGEC7FTpIw_q04",
        "video_id": "zaGEC7FTpIw",
        "part": 1,
        "question": "Ereader?",
        "transcript": "Chosen to buy this ereader because I find it not to only work an ample light but also in them conditions as compared to other devices like tablets and mobile where I always feel that they hurt my eyes okay you 2.",
        "word_count": 40,
        "analysis_metadata": {
            "grammar_error_patterns": ["articles", "structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["ample light", "tablets"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'work an ample light' (in ample light). 'them conditions' (dim conditions)."
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
                "why_not_9": "Structure slip.",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "ASR ambiguity.",
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
