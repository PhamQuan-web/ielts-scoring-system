import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 231 ---
# Total Samples: 20
# Valid Samples: 13

scored_samples = [
    {
        "id": 0, "sample_id": "p0BgBmtO2Vs_q02", "video_id": "p0BgBmtO2Vs",
        "part": 1,
        "question": "Free time?",
        "transcript": "I go for go outside for watching movies and sometime eating food on local food Outlets okay and how do the people of your age spend their free time it will totally depend on their taste as my brother is also a sports lover so he spent their laser time in sports activity like playing games and other and I am a watching live music then I prefer to watching movies okay how do senior citizens spend their time in your localities so as I am leaving rural area most of people in my town opens spend their spare time with playing cards and sometimes Gosling on social issue as they are a wise member of society okay do you like meeting strangers well definitely yes as I am a socialist person and I like meeting stranger I also know about their cultural traditions and their me too",
        "word_count": 149,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form", "preposition", "word_choice"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["laser time", "socialist person", "gosling"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["form_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'laser time' (leisure). 'socialist person' (sociable/social). 'Gosling' (gossiping). 'spent their' (his). 'leaving rural area' (living in)."
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
                "why_not_4": "Can communicate."
            },
            "vocabulary": {
                "why_not_6": "Multiple wrong words.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Errors impede meaning slightly. Band 5.",
        "grammar_reason": "Frequent errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "p0BgBmtO2Vs_q05", "video_id": "p0BgBmtO2Vs",
        "part": 3,
        "question": "Family business?",
        "transcript": "Family business can be mentioned to the success of a family business first and foremost a family business can become success because of hard work of every family member and second one that their great interest and better facilities okay how is the relation among members of a family business all right no problem how is the relations among members of a family while doing business while doing business first and foremost this would be more honest to their family member and second one that is they can they should do work with their great opportunity if sometimes they are not able to do work then he definitely not impo force them so I think a family with the help of family they can make a business successful and also help them okay what are the advantages of family business well advantage of family business first and foremost as I told earlier that they can become more Rich by family business and second one is that they can provide job to their family member and also it is helpful helpful to become are there any disadvantages of family business well it there are also some disadvantages it totally depends on people person whenever they cheat their family member it is harmful for their relations and second one that whenever there is a loss then every family member in is harmful for their mental definitions okay should husbands and wife have different roles within a family well definitely yes if I talk about my hometown there are most of how wives are housewife and they have they not do any outside worker but husband most of us went doing outside work.",
        "word_count": 272,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["become success", "mental definitions"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["form_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'become success' (successful). 'mental definitions' (state/health?). 'impo force' (impose?). 'wives are housewife' (housewives)."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent breakdown.",
                "why_not_4": "Sustained."
            },
            "vocabulary": {
                "why_not_6": "Errors causing confusion.",
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
        "id": 0, "sample_id": "p0BgBmtO2Vs_q06", "video_id": "p0BgBmtO2Vs",
        "part": 3,
        "question": "Big companies?",
        "transcript": "It will be completely indispensable role to provide a good status for a employer and the second one is that they can get more job more other opportunity to become successful with the help of big companies for example if I talk about my elder brother he is also a he is also working in a big company and he is one of the best people in my country okay should big companies donate more to the charities it is an interesting question and I think most of the company should invest in Charities because nowadays education system is very bad and if they invest in this then India become more aware about studies and segment is that about health related they can also enhance the health conditions and also provide more equipment related to health treatment so I think the company should invest in Charities as they more they can okay thank you so much.",
        "word_count": 160,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "articles"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["indispensable role", "health treatment", "invest in charities"],
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
            "reason": "'status for a employer' (employee?). 'segment is that' (second is that?). 'as they more they can' (as much as they can)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors.",
                "why_not_5": "Complex structures used."
            },
            "vocabulary": {
                "why_not_7": "Some good words but errors.",
                "why_not_5": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Indispensable role is good. Band 6.",
        "grammar_reason": "Accurate enough. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "YlWTLyMd-HA_q04", "video_id": "YlWTLyMd-HA",
        "part": 1,
        "question": "Rules?",
        "transcript": "Yes, there are some basic rules. For example, you have to wear uniform whenever you go to school during user days.",
        "word_count": 20,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["basic rules", "wear uniform"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'user days' (weekdays/usual days?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
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
        "vocab_reason": "Basic. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "YlWTLyMd-HA_q05", "video_id": "YlWTLyMd-HA",
        "part": 1,
        "question": "More rules?",
        "transcript": "I think less rules because I do not know why but I enjoy freedom and that is why I I do not like a lot of do you think students would benefit more from more rooms? I think yes and no. It depends for some like primary student and secondary student I think a lot of rules will be helpful for them because at this time they can control their behaviors. So rule is really helpful but for some like a high school student I think that they can control their what they do. I think for high school students is better.",
        "word_count": 102,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["control their behaviors", "enjoy freedom"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'less rules' (fewer). 'rule is really helpful' (rules are)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Agreement errors.",
                "why_not_5": "Complex structures."
            },
            "vocabulary": {
                "why_not_7": "Good terms.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good terms. Band 6.",
        "grammar_reason": "Errors but communicative. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "YlWTLyMd-HA_q07", "video_id": "YlWTLyMd-HA",
        "part": 1,
        "question": "Public places?",
        "transcript": "No, because I am an introvert person. So I hardly ever hang out with my friends. So I think no.",
        "word_count": 19,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["hang out", "introvert person"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["collocation_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'introvert person' (introvert/introverted)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
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
                "why_not_7": "Short.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Good idiom.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Hang out. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "YlWTLyMd-HA_q08", "video_id": "YlWTLyMd-HA",
        "part": 1,
        "question": "Talk to strangers?",
        "transcript": "Yes, especially when I have to do some other activity. For example, in I usually go to the church and here I think I mean every week we have a lot of new teenagers going here. So I have to talk with them and because we have to work together. So I have to communicate with them.",
        "word_count": 56,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["communicate with"],
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
                "why_not_7": "Simple complex.",
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
        "id": 0, "sample_id": "YlWTLyMd-HA_q09", "video_id": "YlWTLyMd-HA",
        "part": 1,
        "question": "Headphones?",
        "transcript": "No, I I have never done that because I think it is so strange when it is like whenever you wear headphones meaning that like it is created a feeling for others that they can communicate with you. So I hardly do that because like whenever I go out means I want to communicate with others and share with others.",
        "word_count": 58,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["hardly do that"],
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
            "reason": "'created a feeling... that they can communicate' (likely meant 'cannot'). 'whenever I go out means' (going out means)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Structure errors.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Good.",
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
        "grammar_reason": "Errors but clear. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "YlWTLyMd-HA_q10", "video_id": "YlWTLyMd-HA",
        "part": 1,
        "question": "More public places?",
        "transcript": "Yes, because for example I would love to have more park in my area so that I could have pay for exercising or something like that. And.",
        "word_count": 26,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'have pay for exercising' (have a place/space?). 'more park' (parks)."
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
                "why_not_7": "Errors.",
                "why_not_5": "Accurate."
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
        "vocab_reason": "Basic. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "YlWTLyMd-HA_q12", "video_id": "YlWTLyMd-HA",
        "part": 3,
        "question": "Ready?",
        "transcript": "Yes, I am ready. Okay. So.",
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
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "YlWTLyMd-HA_q13", "video_id": "YlWTLyMd-HA",
        "part": 3,
        "question": "Interesting people?",
        "transcript": "I think as for me I love talking to people who have a wide range of knowledge in different fields. For example, my friends she has read a lot of different books and whenever I talk I talk to hers like I can know a lot of new knowledge that is why I really enjoy talking to her.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["pronoun"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["wide range of knowledge", "different fields"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["pronoun_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'talk to hers' (her)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "high",
            "flexibility": "low",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Pronoun error.",
                "why_not_5": "Accurate."
            },
            "vocabulary": {
                "why_not_7": "Good phrase.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good phrase. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "YlWTLyMd-HA_q14", "video_id": "YlWTLyMd-HA",
        "part": 3,
        "question": "Life experience?",
        "transcript": "Yeah, I think yes. Because like I told you before, they have a lot of experience. that is means they have a lot of knowledge and whenever I talk to them, I can gain more interesting information.",
        "word_count": 37,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["gain more interesting information"],
            "grammar_structures_used": ["complex_sentences"]
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
            "reason": "'that is means' (that means)."
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
                "why_not_7": "Structure error.",
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
        "id": 0, "sample_id": "YlWTLyMd-HA_q15", "video_id": "YlWTLyMd-HA",
        "part": 3,
        "question": "Naturally interesting?",
        "transcript": "I think the biggest reason is because of their parents and their family. Like my friend, she lives a family with you know her parents. He is really there I am sorry they are really funly and like always support on her decisions. a person like him is also very fun and I do not know why but whenever she is around people she can always make people laugh a lot and people are always like enjoy to enjoy talking to her and are celebrities always interesting dous can you clear the question ok so do you think that celebrities are always interesting people are just look like they are interesting because they famous question in my opinion I It depends on it depends on each person like but most of the celebrity I know they are have their like for example roles she is an interesting person that is real because I get to know a lot of about her and I know that yeah it is a real characters it is a real life I do not I do not great so that is it for the practice then how do you feel ha the third part is a bit confusing. Sorry, this is probably due to my carelessness, so it might have a slight psychological impact on you. He was looking for the set of science questions, but page 3 had been leaked onto another set of questions.",
        "word_count": 247,
        "analysis_metadata": {
            "grammar_error_patterns": ["pronoun", "word_choice", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["support on her decisions"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["pronoun_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'funly' (funny). 'support on her decisions' (support). 'lives a family' (with). 'real characters' (character)."
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
                "why_not_6": "Frequent breakdown.",
                "why_not_4": "Sustained."
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
    }
]

# Write to file
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
