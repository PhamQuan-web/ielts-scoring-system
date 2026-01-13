import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 218 ---
# Total Samples: 20
# Samples Analyzed:

# 1. XNI7Jg2PzVc_q09 (Band 4.5)
# Transcript: "youngster... after my merits... did not have a lot of spare time... did not practice it a lot nowadays... football is still my hobby..."
# Analysis: "after my merits" (marriage?). "did not practice" (do not practice). "youngster".
# - Verdict: Band 4.5. "Merits" is a major meaning error.

# 2. XNI7Jg2PzVc_q10 (Band 4.5)
# Transcript: "football is not about chasing the ball... make us feel refreshed... speak with our span... freshen up after a hectic case of work... relaxing sometimes..."
# Analysis: "hectic case of work" (hectic day? pace?). "span" (friend?). "to relaxing" (to relax).
# - Verdict: Band 4.5/5.0. Some good chunks ("chasing the ball", "hectic") mixed with confusion.

# 3. XNI7Jg2PzVc_q11 (Band 4.5)
# Transcript: "do my hobby... do a work full-time... find a friend to do this hobby... own business..."
# Analysis: "do a work" (have a full-time job / work full-time).
# - Verdict: Band 4.5.

# 4. XNI7Jg2PzVc_q13 (Band 4.5)
# Transcript: "To be start with... ability to have a make a decisions... influence their experience... lack of pressure... insist them to make a decision..."
# Analysis: "To be start with" (To start with). "have a make a decisions". "insist them" (pressure them / insist they make).
# - Verdict: Band 4.5.

# 5. XNI7Jg2PzVc_q14 (Band 4.5)
# Transcript: "age going to be influenced... will not doing nothing... will not gain nothing... age going el older... experience is other thing..."
# Analysis: "will not doing nothing" (will not do anything). "age going el older" (getting older).
# - Verdict: Band 4.5. Double negatives and structure errors.

# 6. XNI7Jg2PzVc_q15 (Band 4.5)
# Transcript: "should done it with... gather all people... led us to the f of decisions..."
# Analysis: "should done it" (should do it). "f of decisions" (path? failure?).
# - Verdict: Band 4.5.

# 7. XNI7Jg2PzVc_q16 (Band 4.5)
# Transcript: "tremendously dangerous... what subject we make decision with... deal with it with that decision..."
# Analysis: "tremendously dangerous". Repetitive "with".
# - Verdict: Band 4.5.

# 8. ef8BPXPAUrA_q02 (Band 7.5)
# Transcript: "suffer from this... hang out with friends... disappointed when they suddenly change the rules... sleep too late... force myself to sleep... parttime job... video shooting... get around very well... promote overseas..."
# Analysis:
# - Grammar: "kind of disappointed" (was kind of). "change the rules" (changed). "part I should fix my is like" (fix about myself).
# - Vocabulary: "promote overseas", "video shooting", "introduction videos".
# - Verdict: Band 7.5.

# 9. ef8BPXPAUrA_q03 (Band 7.5)
# Transcript: "Political threat is very high... change the law very fast... big real estate company... take the law... dangerous... developing very fast..."
# Analysis: "Political threat" (risk?). "take the law" (handle? adapt to?).
# - Verdict: Band 7.5. Good flow, some imprecise terms.

# 10. p5Q7OqPuyaw_q01 (Band 5.5)
# Transcript: "I like the delicious food. Good morning... conduct the..."
# Analysis: Candidate answer + Examiner intro mix? The candidate said "I like the delicious food". Then text says "Good morning... I am with Bon Education".
# - Verdict: MIXED. Candidate speech is "I like the delicious food." Band 5.5.

# 11. p5Q7OqPuyaw_q03 (Band 5.5)
# Transcript: "I fled here because I want to go tracking and to experience different culture..."
# Analysis: "fled here" (flew? fled=ran away). "tracking" (trekking).
# - Verdict: Band 5.5. "fled" is a major meaning error if she meant flew.

# 12. p5Q7OqPuyaw_q04 (Band 5.5)
# Transcript: "I am from the north of China."
# Analysis: Simple.
# - Verdict: Band 5.5.

# 13. p5Q7OqPuyaw_q05 (Band 5.5)
# Transcript: "delicious food bes... cans of breakfast and some sweet food..."
# Analysis: "cans of breakfast" (kinds of?). "bes" (best?).
# - Verdict: Band 5.0. Pronunciation affecting transcription ("cans" vs "kinds").

# 14. p5Q7OqPuyaw_q06 (Band 5.5)
# Transcript: "Three people... father, mother and me."
# Analysis: Simple.
# - Verdict: Band 5.5.

# 15. p5Q7OqPuyaw_q09 (Band 5.5)
# Transcript: "Tell me about your highest education qualification."
# Analysis: EXAMINER SPEECH.
# - Verdict: INVALID (Skip).

# 16. p5Q7OqPuyaw_q12 (Band 5.5)
# Transcript: "I think it is both exciting and tiring."
# Analysis: Short.
# - Verdict: Band 5.5.

# 17. WCuVDK5T-Mc_q01 (Band 8.0)
# Transcript: "make a city to a good one... strict or not friendly to Foreigner... people in store... walk faster... pay the pay bill... houses are expensive..."
# Analysis:
# - Grammar: "make a city to a good one" (make a city a good one). "Foreigner" (foreigners). "people in store" (Seoul).
# - Verdict: Band 7.5/8.0.

# 18. WCuVDK5T-Mc_q02 (Band 8.0)
# Transcript: "clean... tiny and no dust... walk down the Heaven There... tried to sow... internships... career Branch company... centralized and more efficiency..."
# Analysis:
# - Grammar: "streets are very tiny" (tidy?). "tried to sow" (Seoul). "more efficiency" (efficient).
# - Vocabulary: "internships", "centralized".
# - Verdict: Band 8.0.

# 19. WCuVDK5T-Mc_q03 (Band 8.0)
# Transcript: "wolves inside a lot of trees... connecting to Nature... concrete jungle..."
# Analysis: "wolves" (woods?). "concrete jungle".
# - Verdict: Band 8.0.

# 20. oEUBd3ZjStA_q02 (Band 7.0)
# Transcript: "have my healthy food more than I probably should... easier way to get healthy food... limit myself to eat unhealthy food... health have declined... food have been worsened... ignoring the fast food..."
# Analysis:
# - Grammar: "easier way" (easiest way / very easy way). "food have been worsened" (has worsened / got worse). "health have declined" (has).
# - Vocabulary: "declined", "limit myself".
# - Verdict: Band 7.0.

scored_samples = [
    {
        "id": 0, "sample_id": "XNI7Jg2PzVc_q09", "video_id": "XNI7Jg2PzVc",
        "part": 1,
        "question": "Youngster sports?",
        "transcript": "But nowadays, after my merits, I did not have a a lot of spare time. So, I did not practice it a lot nowadays. But I can say that football is still my hobby until now.",
        "word_count": 38,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "word_choice"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["spare time"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": ["meaning_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'after my merits' (marriage?). 'did not practice' (do not practice)."
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
                "why_not_6": "Tense errors.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Wrong word 'merits'.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Meaning error ('merits'). Band 5.",
        "grammar_reason": "Tense errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "XNI7Jg2PzVc_q10",
        "video_id": "XNI7Jg2PzVc",
        "part": 1,
        "question": "Interest in hobby?",
        "transcript": "I could say that football is not about chasing the ball, running all around the field, but it is also make us feel refreshed because we just we we not just like running and kicking, we can also speak with our span our our friend I mean I am sorry and on that activity I find that really make me freshen up after a hectic case of work or just like to relaxing sometimes.",
        "word_count": 72,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_choice"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["freshen up", "chasing the ball", "hectic"],
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
            "reason": "'hectic case of work' (pace/day?). 'speak with our span' (?). 'like to relaxing' (to relax)."
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
        "vocab_reason": "Basic with errors. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "XNI7Jg2PzVc_q11",
        "video_id": "XNI7Jg2PzVc",
        "part": 1,
        "question": "Time on hobbies?",
        "transcript": "Sometimes if I have a free time, I will try to do my hobby like once a week or twice a week. It really depends on my spare time. Actually, I do a work full-time work right now. So if on a weekend sometimes I try to find a friend to do this hobby but not really often because they they have their own business as well. Now in this next part of the test I am going to give you a topic and I would like you to speak about this topic for one to two minutes. But before that.",
        "word_count": 99,
        "analysis_metadata": {
            "grammar_error_patterns": ["article", "structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["spare time", "full-time work"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'do a work full-time' (work full-time). 'have a free time' (free time)."
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
                "why_not_6": "Basic errors.",
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
        "id": 0, "sample_id": "XNI7Jg2PzVc_q13",
        "video_id": "XNI7Jg2PzVc",
        "part": 3,
        "question": "Better decisions?",
        "transcript": "To be start with I would say that there are some people have a decision making or the ability to have a make a decisions in a good level but some people the other people sometimes does not have that I do not know maybe it is because due to their knowledge to to their behavior that influence their experience to do that I am not sure about that but one thing for sure someone could make a good decision when they are not influenced by a pressure pressure I could I am sorry I mean lack of pressure or without like someone insist them to make a decision as fast as they can.",
        "word_count": 111,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["decision making", "pressure"],
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
            "reason": "'To be start with' (To start with). 'have a make a decisions'. 'insist them' (pressure them)."
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
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "XNI7Jg2PzVc_q14",
        "video_id": "XNI7Jg2PzVc",
        "part": 3,
        "question": "Decisions with age?",
        "transcript": "Oh yes absolutely. In my own perspective the age going to be influenced a lot but it really depends on the person as well. If the person is going older but they do not have any experience on that field for example then they will not doing nothing they will not gain nothing in their own personality. So the age going el older I could say is really important but the experience is nothing. No I am sorry the experience is other thing that really essential in this stage.",
        "word_count": 88,
        "analysis_metadata": {
            "grammar_error_patterns": ["double_negative", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["perspective", "essential", "experience"],
            "grammar_structures_used": ["conditionals"]
        },
        "micro_flaws": {
            "grammar": ["double_negative_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'will not doing nothing' (will not do anything). 'age going el older' (getting older)."
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
                "why_not_6": "Double negatives and errors.",
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
        "id": 0, "sample_id": "XNI7Jg2PzVc_q15",
        "video_id": "XNI7Jg2PzVc",
        "part": 3,
        "question": "Quick vs Slow decisions?",
        "transcript": "in this case I would say it really depends on the condition or situations. If they have a lot of spare time, if they have time enough to make a great decision, I could say that maybe they should done it with what can I say like carefully or they could like gather all people or the subject that may be relevant into that decision so they could make it better rather than if we just like okay we just want to make a decision at that time. So we do not need to collect other perspective but maybe it going to be like led us to the f of decisions.",
        "word_count": 108,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["spare time", "gather all people"],
            "grammar_structures_used": ["conditionals"]
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
            "reason": "'should done it' (should do it). 'f of decisions' (failure? poor decisions?)."
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
                "why_not_6": "Unclear terms.",
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
        "id": 0, "sample_id": "XNI7Jg2PzVc_q16",
        "video_id": "XNI7Jg2PzVc",
        "part": 3,
        "question": "Wrong decision?",
        "transcript": "it is going to be like a I could say it is tremendously dangerous because once they said a decision could affect our future. It really depends on what subject on what subject we make decision with. I mean like what the thing that we deal with it with that decision. maybe they can I could say have that decision is really crucial for their future but sometimes maybe it is not that too crucial.",
        "word_count": 73,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["tremendously dangerous", "crucial"],
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
            "reason": "'tremendously dangerous' (strong collocation). 'make decision with' (about/on)."
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
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Structure errors.",
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
        "id": 0, "sample_id": "ef8BPXPAUrA_q02",
        "video_id": "ef8BPXPAUrA",
        "part": 1,
        "question": "Lifestyle?",
        "transcript": "Of suffer from this because we like to meet with each other hang out with friends and the night life in Korea is very important yes so it was kind of disappointed when they suddenly change the rules again right definitely okay and what do you like to change about about your lifestyle pardon what would you like to change about your lifestyle yeah I think the part I should fix my is like I always sleep too late and wake up sometimes very late too so I would like if I could force myself to sleep before for me right definitely good night sleep helps everyone okay now we going talk a little bit about work do you work right now oh yes I kind of I did a parttime job before around one month term yeah a short term I did some video shooting too actually yes I did small company introduction videos for culture yes oh that sounds interesting and do you get on well with your co-workers oh actually the co-workers in the studio are very they are like they always they are like same age around with me so we get very good we get around very well well that is good and what responsibilities do you have at your work I part participate in the video shooting as Chinese speakers yes so I did a Chinese video for the Korean company to introduce their produ product and the company itself yeah to promote overseas all right I have one more question about work are there good work opportunities in your home country yes in China it is a Dev veloping country now and all the internet company grows very fast but the important thing is the.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "preposition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["promote overseas", "introduction videos", "night life"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'kind of disappointed' (was disappointed). 'change the rules' (changed)."
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
                "why_not_9": "Minor tense slips.",
                "why_not_7": "Complex and accurate."
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
        "grammar_reason": "Mostly error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "ef8BPXPAUrA_q03",
        "video_id": "ef8BPXPAUrA",
        "part": 1,
        "question": "Opportunities?",
        "transcript": "Political threat is very high some sometime they change the law very fast so even the big real estate company could not have the time to take the law so they kind of very dangerous I think but there is more opportunity yes because it is very developing very fast now okay great thank you for answering all my question.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["political threat", "real estate company"],
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
            "triggered": True,
            "reason": "'take the law' (adapt to?)."
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
                "why_not_9": "Minor unnatural phrasing.",
                "why_not_7": "Accurate."
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
        "id": 0, "sample_id": "p5Q7OqPuyaw_q01",
        "video_id": "p5Q7OqPuyaw",
        "part": 1,
        "question": "Like most?",
        "transcript": "I like the I like the delicious food. Good morning. I am with Bon Education Consultancy right now. today this is 9th of April 2025. I am I am I am here to conduct the.",
        "word_count": 34,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["delicious food"],
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
        "id": 0, "sample_id": "p5Q7OqPuyaw_q03",
        "video_id": "p5Q7OqPuyaw",
        "part": 1,
        "question": "Why Nepal?",
        "transcript": "I fled here because I want to go tracking and to experience different culture and different people.",
        "word_count": 16,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["tracking", "fled"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["meaning_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'fled here' (flew). 'tracking' (trekking)."
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
                "why_not_6": "Errors.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Meaning errors.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Meaning errors. Band 5.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "p5Q7OqPuyaw_q04",
        "video_id": "p5Q7OqPuyaw",
        "part": 1,
        "question": "From?",
        "transcript": "Yes. I am from the north of China. North of China.",
        "word_count": 11,
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
        "id": 0, "sample_id": "p5Q7OqPuyaw_q05",
        "video_id": "p5Q7OqPuyaw",
        "part": 1,
        "question": "Like most 2?",
        "transcript": "And I like the I like the delicious food bes. Because there are many cans of breakfast and some sweet food in my hometown. that is great. Wonderful.",
        "word_count": 27,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["delicious food"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'cans of breakfast' (kinds of)."
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
                "why_not_6": "Errors.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Pronunciation error causing wrong word.",
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
        "id": 0, "sample_id": "p5Q7OqPuyaw_q06",
        "video_id": "p5Q7OqPuyaw",
        "part": 1,
        "question": "Family?",
        "transcript": "There are three people in my family. My father, my mother and me.",
        "word_count": 13,
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
        "id": 0, "sample_id": "p5Q7OqPuyaw_q12",
        "video_id": "p5Q7OqPuyaw",
        "part": 1,
        "question": "Journey?",
        "transcript": "I think it is both exciting and tiring.",
        "word_count": 7,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["exciting", "tiring"],
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
        "id": 0, "sample_id": "WCuVDK5T-Mc_q01",
        "video_id": "WCuVDK5T-Mc",
        "part": 3,
        "question": "Good city?",
        "transcript": "We will go on to our last part of our interview I will ask you some questions and just try to answer as best as you can I will ask you some follow-up questions okay these can be about your opinion or something else all right so let us start in your opinion what makes the city a good one to live in I think what make a city to a good one to live in is the culture and the people people in the city yes because in different country and different regions they have different culture as in Korea they might be more a little bit more strict or not friendly to Foreigner but maybe in the Europe and in the west they will be very friendly to foreigners and also the people who live in the city are the is the one who built the city so that is the most part important part of the city yeah okay what do you think of the people in this city in Seoul are they friendly are they nice what do you think of them yes I just pooping so actually like a month ago I think people in store they are very busy they walk faster as like if you compare to different city in middle of Korea like Chengdu and tejan they actually the absolutely walk faster here and the lifestyle might be more City that is like and people are have more budget maybe I do not know like more money to pay off that the pay the pay bill might be very hard for them yes and the houses are expensive so the people here I think they are foreign do not care about you yeah they care about their own life yes okay so you have had a chance to travel.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["budget", "pay bill", "lifestyle"],
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
            "reason": "'make a city to a good one' (make a city a good one). 'people in store' (Seoul)."
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
                "why_not_7": "Complex and accurate."
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
        "grammar_reason": "Mostly error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "WCuVDK5T-Mc_q02",
        "video_id": "WCuVDK5T-Mc",
        "part": 1,
        "question": "Fav city?",
        "transcript": "Around Korea different cities what in your opinions your favorite city in Korea yes my favorite city is Busan because it is very clean actually oh yes where I went to different cities in Korea and Busan is absolutely so clean the streets are very tiny and no dust maybe because it is close to the ocean and the view is very beautiful it is all the I like to walk down the Heaven There the beach and enjoying the sunshine and the sea sea views definitely Busan is a nice city to visit then why are you living in Seoul if you want to Busan and so why do you think why did you choose Soul yeah I tried to sow firstly because I actually had a chance to move in my friend house so it is very easy to move in and also the internships here are very there are more chance to find a nice internship here and so because if their company will build a career Branch company they will choose so instead of Busan definitely all right and what do you think are the advantages of living in a city oh yes I think the advantage advantages for the for people to live in the city is actually why the city is built because when you build a city everything get closer and very easy to attach people live around each other and all the work facilities and everything they are closed so they are more centralized and more efficiency and more job they can they can be they can do in the same amount of time all right very good and of course living in a city like crowded City sometimes has some negative things okay so I want you to talk about negative tell.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["internship", "centralized", "work facilities"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'streets are very tiny' (tidy?). 'more efficiency' (efficient). 'attach people' (connect?)."
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
                "why_not_9": "Minor word form errors.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "'tiny' vs 'tidy'.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Sophisticated. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "WCuVDK5T-Mc_q03",
        "video_id": "WCuVDK5T-Mc",
        "part": 3,
        "question": "Negative aspects?",
        "transcript": "Me what are some negative aspects of crowded cities yes as as people just moving so I can actually feel very strongly how the different is compared to a different city in Korea I live I used to live around my university in chenju which they have very much a lot of wolves inside a lot of trees so we all always walk take a take a walk after after dinner and after move in Seoul we barely cannot see any green colors yeah not even it is winter but there is no trees around everything just concrete and buildings I think as a part of the nature humor or humans are awesome animals so I think connecting to Nature is part of our our our nature too so it is very important to get some green color in your life definitely I agree with you sometimes Soul can be like a concrete jungle yes all right thank you so much for answering my questions I thought you did really well I hope you have a nice day thank you too teacher",
        "word_count": 182,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["concrete", "connecting to nature"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'wolves inside' (woods?). 'green colors' (greenery)."
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
                "why_not_9": "Minor unnatural phrasing.",
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
        "vocab_reason": "Good range. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "oEUBd3ZjStA_q02",
        "video_id": "oEUBd3ZjStA",
        "part": 1,
        "question": "Healthy food?",
        "transcript": "Healthy okay how often do you eat unhealthy food well unfortunately I have my healthy food more than I probably should I think is because it is very easier way to get healthy food and always the fastest option but Alina I limit myself to eat unhealthy food once per week however sometimes it twice a week or even more oh okay all right how has people's health in your country changed in the past 10 years in my hometown of China I think people's health have declined in the past 10 years I think that the food have been worsened and people many people have they are spending less time on getting outside do physical exercise -what do you think is the biggest challenge and staying healthy I think the biggest challenge for health for me personally I think is ignoring the fast food well however for society I think people should spend more time physical exercise ok excellent.",
        "word_count": 169,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "comparative"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["unhealthy food", "declined", "limit myself", "physical exercise"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'very easier way' (easier/easiest). 'health have declined' (has). 'food have been worsened' (has worsened)."
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
                "why_not_8": "Agreement errors.",
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
        "grammar_reason": "Frequent error-free but some slips. Band 7.",
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
