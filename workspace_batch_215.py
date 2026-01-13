import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 215 ---
# Total Samples: 20
# Samples Analyzed:

# 1. HrvVGX9oMng_q02 (Band 7.0)
# Transcript: "Did you like the same kinds of TV programs when you were Funk."
# Analysis: FRAGMENT/QUESTION REPEAT.
# - Verdict: INVALID (Skip).

# 2. HrvVGX9oMng_q04 (Band 7.0)
# Transcript: "I am really into documentaries... switch off... light-hearted series..."
# Analysis:
# - Vocabulary: "switch off", "light-hearted". Good.
# - Verdict: Band 7.0.

# 3. HrvVGX9oMng_q05 (Band 7.0)
# Transcript: "fast-paced... thoughtprovoking stuff... comes with growing up."
# Analysis:
# - Vocabulary: "fast-paced", "thought-provoking".
# - Verdict: Band 7.0.

# 4. HrvVGX9oMng_q06 (Band 7.0)
# Transcript: "reality TV shows... gripping storylines... streaming services..."
# Analysis: "gripping storylines".
# - Verdict: Band 7.0.

# 5. HrvVGX9oMng_q07 (Band 7.0)
# Transcript: "addictive... wasted hours... repetitive... interruptive and annoying."
# Analysis: "interruptive" (intrusive?).
# - Verdict: Band 7.0.

# 6. HrvVGX9oMng_q08 (Band 7.0)
# Transcript: "Here we go. Now, I am going to give you a topic..."
# Analysis: EXAMINER SPEECH.
# - Verdict: INVALID (Skip).

# 7. HrvVGX9oMng_q10 (Band 7.0)
# Transcript: "Notice the use of abbreviation here. that is a good trick for writing notes quickly."
# Analysis: TUTORIAL / META COMMENTARY.
# - Verdict: INVALID (Skip).

# 8. HrvVGX9oMng_q14 (Band 7.0)
# Transcript: "To help you evaluate, you can compare your responses..."
# Analysis: TUTORIAL.
# - Verdict: INVALID (Skip).

# 9. HrvVGX9oMng_q15 (Band 7.0)
# Transcript: "changed dramatically... busy lifestyles... shift towards convenience... healthconscious eating... plant-based diets... ultrarocessed foods..."
# Analysis: "ultra-processed foods".
# - Verdict: Band 7.0.

# 10. HrvVGX9oMng_q16 (Band 7.0)
# Transcript: "individualistic... grab a burger on the go... family dynamics..."
# Analysis: "family dynamics", "on the go".
# - Verdict: Band 7.0.

# 11. HrvVGX9oMng_q17 (Band 7.0)
# Transcript: "fusion food... meal prep services... superfoods... veganism..."
# Analysis: Good topic vocab.
# - Verdict: Band 7.0.

# 12. HrvVGX9oMng_q18 (Band 7.0)
# Transcript: "If so, you are going to do well in this part. If you would like more practice..."
# Analysis: ADVERTISEMENT/OUTRO.
# - Verdict: INVALID (Skip).

# 13. POoGu6MJs0I_q01 (Band 7.0)
# Transcript: "born in Ho Chi Min City... second largest city... located in the south..."
# Analysis: Basic but accurate.
# - Verdict: Valid (Band 7).

# 14. POoGu6MJs0I_q02 (Band 7.0)
# Transcript: "all at your fun store... attract a lot of tourists... super friendly... go beyond their way..."
# Analysis: "fun store" (front door? fingertips?). "go beyond their way" (go out of their way). "this is attract" (this attracts).
# - Verdict: Band 6.5.

# 15. POoGu6MJs0I_q03 (Band 7.0)
# Transcript: "majority of people they are working as a farmers working in hospitality..."
# Analysis: "working as a farmers" (farmers).
# - Verdict: Band 6.5.

# 16. POoGu6MJs0I_q04 (Band 7.0)
# Transcript: "international concert... easy to get around now with motorcycle... cost of living is quite affordable..."
# Analysis: "international concert" (concerts).
# - Verdict: Band 7.0.

# 17. POoGu6MJs0I_q05 (Band 7.0)
# Transcript: "full of stuff is containing many different ingredients... easy to access to..."
# Analysis: "stuff is containing" (stuff containing / which contains). "access to" (access).
# - Verdict: Band 6.5.

# 18. POoGu6MJs0I_q06 (Band 7.0)
# Transcript: "not a very easy eater... where the stuff that I purchase from... get to know another country culture better to understanding..."
# Analysis: "easy eater" (fussy eater? easy-going eater?). "purchase from" (purchase come from?). "better to understanding" (better understand).
# - Verdict: Band 6.5.

# 19. POoGu6MJs0I_q07 (Band 7.0)
# Transcript: "chicken soup... weather was quite cold... boiling the chicken... exciting for about in the future..."
# Analysis: "exciting for about" (excited about). "visame" (Vietnamese).
# - Verdict: Band 6.5.

# 20. POoGu6MJs0I_q09 (Band 7.0)
# Transcript: "Make sure you enunciate your words... opening your mouth when you talk..."
# Analysis: TUTORIAL (Mixed with answer repeat). The end is tutorial. "Make sure you enunciate...".
# - Verdict: INVALID (Skip) - mostly tutorial text at end.

scored_samples = [
    {
        "id": 0, "sample_id": "HrvVGX9oMng_q04", "video_id": "HrvVGX9oMng",
        "part": 1,
        "question": "TV programs liked?",
        "transcript": "I am really into documentaries, especially ones about history or true crime. I love getting drawn into real life stories, and I suppose they are a great way to learn something without feeling like you are studying. That said, sometimes I just want to switch off, so I will watch a good comedy or a light-hearted series. Second question.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["switch off", "light-hearted", "drawn into"],
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
        "id": 0, "sample_id": "HrvVGX9oMng_q05", "video_id": "HrvVGX9oMng",
        "part": 1,
        "question": "Young TV preferences?",
        "transcript": "Not really. As a kid, I was all about cartoons and adventure shows, programs that were fun and fast-paced. I was not into anything too serious, but as I got older, my tastes changed. I started enjoying more thoughtprovoking stuff like dramas and documentaries. I guess it just comes with growing up.",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["fast-paced", "thought-provoking", "comes with growing up"],
            "grammar_structures_used": ["complex_sentences", "past_tense"]
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
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good adjectives ('fast-paced'). Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "HrvVGX9oMng_q06",
        "video_id": "HrvVGX9oMng",
        "part": 1,
        "question": "Popular programs?",
        "transcript": "reality TV shows seem to be extremely popular. People love those based on competitions, things like cooking contests or talent shows. And of course, dramas are huge, especially ones with gripping storylines. But I would also have to say that streaming services have changed things a lot. So now people want a mix of both international and local productions. Fourth question.",
        "word_count": 60,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["gripping storylines", "streaming services", "local productions"],
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
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Precise ('gripping'). Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "HrvVGX9oMng_q07",
        "video_id": "HrvVGX9oMng",
        "part": 1,
        "question": "Dislike about TV?",
        "transcript": "definitely. I think the biggest downside is how addictive it can be. it is so easy to say just one more episode and suddenly you have wasted hours. Also, some shows feel a bit repetitive, like they have the same plot lines just recycled. And of course, the ads can be really interruptive and annoying.",
        "word_count": 54,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["downside", "addictive", "recycled"],
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
            "reason": "'interruptive' (uncommon, usually 'intrusive' or 'interrupting')."
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
                "why_not_9": "'interruptive' vs 'intrusive'.",
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
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 7,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "HrvVGX9oMng_q15",
        "video_id": "HrvVGX9oMng",
        "part": 3,
        "question": "Eating habits changed?",
        "transcript": "eating habits have changed dramatically over the last few decades. People used to cook at home more often, but now with busy lifestyles, there is a shift towards convenience, which means people are eating more ready meals, takeaways, and eating out more. there is also been a big rise in healthconscious eating. You see more organic food, plant-based diets, and people cutting down on sugar. In saying that, ultrarocessed foods are also more common than ever. For example, in many cities, you will find fast food joints on every street corner, which was not really the case 30 years ago. If this trend continues, we might see even more health related problems in the future.",
        "word_count": 113,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["shift towards convenience", "ultra-processed foods", "plant-based diets", "fast food joints"],
            "grammar_structures_used": ["complex_sentences", "comparatives"]
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
                "why_not_9": "'ultra-processed', 'health-conscious'. Excellent.",
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
        "id": 0, "sample_id": "HrvVGX9oMng_q16",
        "video_id": "HrvVGX9oMng",
        "part": 3,
        "question": "Fast food culture?",
        "transcript": "I think so. Fast food has made eating more individualistic. People often grab a burger on the go instead of sitting down for a proper meal. Traditionally, meals were a social event, especially in cultures where family dinners were important. But now with things like food delivery apps, people eat at different times in front of screens or even alone, even when they are in the same home. This kind of change is a bit of a shame and could have quite negative consequences on family dynamics, especially.",
        "word_count": 87,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["individualistic", "family dynamics", "on the go", "social event"],
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'family dynamics', 'individualistic'. Excellent.",
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
        "id": 0, "sample_id": "HrvVGX9oMng_q17",
        "video_id": "HrvVGX9oMng",
        "part": 3,
        "question": "Young vs Old eating?",
        "transcript": "There is definitely a contrast. Older generations tend to prefer home-cooked meals and traditional recipes, while younger people experiment more with different cuisines like Persian and Sri Lankan food or fusion food. Plus, young people often eat on the move, relying on fast food or a meal prep services, whereas older people usually sit down for meals. Another big difference is social media. Young people are influenced by food trends online like superfoods or veganism. But one thing's for sure, both groups seem to be becoming more aware of the importance of nutrition for general health, which is a good thing for society overall.",
        "word_count": 102,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["fusion food", "meal prep services", "superfoods", "veganism"],
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
                "why_not_9": "'fusion food', 'superfoods'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Topic vocabulary is precise. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "POoGu6MJs0I_q01",
        "video_id": "POoGu6MJs0I",
        "part": 1,
        "question": "Place is it?",
        "transcript": "I was born in Ho Chi Min City, which is the second largest city in Vietnam. it is located in the south of Vietnam.",
        "word_count": 23,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["located in the south"],
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
                "why_not_8": "Too short.",
                "why_not_6": "Accurate."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Accurate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Accurate. Band 7.",
        "grammar_reason": "Accurate. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "POoGu6MJs0I_q02",
        "video_id": "POoGu6MJs0I",
        "part": 1,
        "question": "Interesting part?",
        "transcript": "The most interesting place about this place, you can pretty much find everything in the city from cultural events to food scenes. they are all at your fun store. it is not far from Australia about 8 hours by plan. So this is attract a lot of tourists coming to visit every year. The most important thing is that the people are super friendly even though they do not speak a lot of English, but they will try to go beyond their way to help you to navigate the city.",
        "word_count": 89,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "idiom"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["food scenes", "cultural events", "navigate the city"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["idiom_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'at your fun store' (fingertips? doorstep?). 'this is attract' (this attracts). 'go beyond their way' (go out of their way)."
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
                "why_not_8": "Basic errors ('this is attract').",
                "why_not_6": "Complex structures."
            },
            "vocabulary": {
                "why_not_8": "Idiom errors ('fun store', 'beyond their way').",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range but idiom errors. Band 7.",
        "grammar_reason": "Errors like 'this is attract'. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "POoGu6MJs0I_q03",
        "video_id": "POoGu6MJs0I",
        "part": 1,
        "question": "Jobs?",
        "transcript": "The majority of people they are working as a farmers working in hospitality factory workers and some professional jobs such as marketing and project management.",
        "word_count": 23,
        "analysis_metadata": {
            "grammar_error_patterns": ["article"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["hospitality", "project management"],
            "grammar_structures_used": ["list"]
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
            "reason": "'working as a farmers' (as farmers)."
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
                "why_not_8": "Article error.",
                "why_not_6": "Accurate list."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Good terms."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good terms. Band 7.",
        "grammar_reason": "Minor error. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "POoGu6MJs0I_q04",
        "video_id": "POoGu6MJs0I",
        "part": 1,
        "question": "Good place to live?",
        "transcript": "To me is a wonderful place to live because there is always something going on in there such as international concert, cultural event and food festival. It is easy to get around now with motorcycle and Ho Chi Min City is now recently built a new train system which is so easy for the local and tourists to get around and from too. More importantly, the cost of living is quite affordable so you can live comfortably there when you have a stable job.",
        "word_count": 83,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["cost of living", "affordable", "stable job"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'To me is a wonderful place' (To me, it is...). 'is now recently built' (has recently built / recently built)."
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
                "why_not_8": "Structural errors.",
                "why_not_6": "Complex sentences."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
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
        "grammar_reason": "Some errors but frequently accurate. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "POoGu6MJs0I_q05",
        "video_id": "POoGu6MJs0I",
        "part": 1,
        "question": "New food?",
        "transcript": "If I would like to try some food, I would like to try sushi and ramen when I am going to Japan next time because this kind of food is full of stuff is containing many different ingredients and very easy to access to no matter where you are in Japan. you do not need to go to a very fancy restaurant to have this. you can pretty much have everything on the street.",
        "word_count": 72,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["fancy restaurant", "access to"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'stuff is containing' (stuff containing). 'access to' (access)."
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
                "why_not_8": "Structural errors.",
                "why_not_6": "Good."
            },
            "vocabulary": {
                "why_not_8": "Minor errors.",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good. Band 7.",
        "grammar_reason": "Errors present but clear. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "POoGu6MJs0I_q06",
        "video_id": "POoGu6MJs0I",
        "part": 1,
        "question": "Like cooking?",
        "transcript": "Yes, I do love cooking. this help me to know where the ingredients coming from and I am not a very easy eater so it will be better for me to know where the stuff that I purchase from. more importantly being able to cook a meal has me to get to know another country culture better to understanding why some certain ingredient in that kind of food to make them to unique to that particular country.",
        "word_count": 75,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "verb_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["ingredients", "culture"],
            "grammar_structures_used": ["complex_sentences"]
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
            "reason": "'easy eater' (fussy?). 'purchase from' (purchase come from?). 'has me to get to know' (helps me). 'better to understanding' (understand). 'make them to unique' (make them unique)."
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
                "why_not_5": "Complex structures."
            },
            "vocabulary": {
                "why_not_7": "Imprecise ('easy eater').",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Imprecise. Band 6.",
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "POoGu6MJs0I_q07",
        "video_id": "POoGu6MJs0I",
        "part": 1,
        "question": "Last meal cooked?",
        "transcript": "The the last thing I made was probably yesterday. It was the chicken soup with carrots and potatoes because the weather was quite cold at that time. It was very delicious. took me about 45 minutes to get ready because all of the the prep just washing the vegetable, cutting the and boiling the chicken. but I really enjoying eating the food that I have put in an effort to make for Do people in your country generally eat meals at home? I think for the V Vietnamese people they tend to eat at home more so that they they be able to spend more time with the family after a busy day. So during that time they be able to share the story of what the day happening what what what are they exciting for about in the future. A typical visame dinner at home will include some rice some meat some stir-fried vegetable and a bowl of soup where everyone can share with each other.",
        "word_count": 160,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["stir-fried", "put in an effort"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'really enjoying' (enjoyed). 'exciting for about' (excited about)."
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
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Verb errors.",
                "why_not_6": "Good range."
            },
            "vocabulary": {
                "why_not_8": "Minor slips.",
                "why_not_6": "Good terms ('stir-fried')."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good. Band 7.",
        "grammar_reason": "Minor errors. Band 7.",
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
