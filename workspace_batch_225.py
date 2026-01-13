import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 225 ---
# Total Samples: 20
# Samples Analyzed:

# 1. RP_rO0mrjnA_q08 (Band 5.5)
# Transcript: "depends on the more... prefer fast food on these foods... eat a lot more."
# Analysis: "depends on the more" (mood?). "on these foods" (to these foods?).
# - Verdict: Band 5.5.

# 2. RP_rO0mrjnA_q09 (Band 5.5)
# Transcript: "enjoy bottling... prefer my home cooking... stomach stomach is not very well conditioned... got lose motions or cooking problem..."
# Analysis: "enjoy bottling" (traveling? The question was "Do you enjoy traveling/cooking?"). "lose motions" (loose motions - diarrhea).
# - Verdict: Band 5.5.

# 3. 5FTJQE6szgo_q03 (Band 6.0)
# Transcript: "older age has a factor... get to know information... don't have narrative politics... indecisive... ages matters to the opinions... society better..."
# Analysis: "age has a factor" (is a factor). "narrative politics" (knowledge of? interest in?).
# - Verdict: Band 6.0.

# 4. 5FTJQE6szgo_q04 (Band 6.0)
# Transcript: "ages matters to the opinions... should be a blue one"
# Analysis: "ages matters" (age matters). "a blue one" (everyone? The question was 'everybody').
# - Verdict: Band 6.0.

# 5. hKGoyMp9g3w_q02 (Band 5.5)
# Transcript: "D is really very famous... used toy buy... cheer pillow which help which helps our lumber support... see the things at a saw... unnecessary things... geni generation... common in phone..."
# Analysis: "used toy buy" (to buy). "cheer pillow" (chair pillow?). "lumber support" (lumbar). "saw" (store/shop).
# - Verdict: Band 5.5.

# 6. hKGoyMp9g3w_q03 (Band 5.5)
# Transcript: "describe a time when you enjoyed visiting a member..."
# Analysis: EXAMINER INSTRUCTION.
# - Verdict: INVALID (Skip).

# 7. hKGoyMp9g3w_q04 (Band 5.5)
# Transcript: "discourse family occasions... thar and chart... Das where... putting Tika... memorable events... life phases... downwards in their life..."
# Analysis: "discourse" (discuss). "thar and chart" (Tihar and Chhath?). "Das where" (Dashain?). "downwards in their life" (difficult period/downturn).
# - Verdict: Band 5.5.

# 8. hKGoyMp9g3w_q05 (Band 5.5)
# Transcript: "school assignments... sign of good parenting... my father was also support me... made my homework... sitting in single dining table... hous World Walks... tax of your household work..."
# Analysis: "father was also support me" (supported). "single dining table" (at a dining table). "tax of your household" (tasks).
# - Verdict: Band 5.5.

# 9. hKGoyMp9g3w_q06 (Band 5.5)
# Transcript: "leave by saying sorry... tax of your household work..."
# Analysis: "tax" (tasks).
# - Verdict: Band 5.5.

# 10. hKGoyMp9g3w_q08 (Band 5.5)
# Transcript: "This time I give you five pen but but I you can get six..."
# Analysis: EXAMINER FEEDBACK/SCORE.
# - Verdict: INVALID (Skip).

# 11. 3GYrVH3BFhI_q01 (Band 5.5)
# Transcript: "go online every day by my phone... downloading software... gadget electronica... filehippo.com... update my windows... unsupervised access... dangerous for children for development..."
# Analysis: "gadget electronica" (electronic gadgets?). "by my phone" (on my phone).
# - Verdict: Band 5.5.

# 12. 3GYrVH3BFhI_q02 (Band 5.5)
# Transcript: "is of washington dc... district of columbia... neoclassical amusement monument... basic immunity... shopik show politic person... hassle-free transportation... heaven for civilized people... children education..."
# Analysis: "amusement monument" (museum/monument). "basic immunity" (amenities). "shopik show politic" (shopaholic?).
# - Verdict: Band 5.5. Strong pronunciation issues causing ASR errors ("immunity" vs "amenities").

# 13. 3GYrVH3BFhI_q03 (Band 5.5)
# Transcript: "crowd crowded place... peace peace... make up your mind... senior secondary school... recreational park... road facility... migrating to these cities... interact with stranger daily... no security... pollution..."
# Analysis: "make up your mind" (decide). "road facility" (facilities). "interact with stranger" (strangers).
# - Verdict: Band 5.5.

# 14. 3GYrVH3BFhI_q04 (Band 5.5)
# Transcript: "basic amenities to countryside... create job for youngster... cannot move to other other cities..."
# Analysis: "create job" (jobs). "cannot move" (will not move?).
# - Verdict: Band 5.5.

# 15. 1xTxxHMfUE8_q02 (Band 5.5)
# Transcript: "Focus businesses... near and dear ones... enhance my knowledge... culture of that place... wasted some new places... recessed... participated many activities..."
# Analysis: "wasted some new places" (visited). "recessed" (recess).
# - Verdict: Band 5.5.

# 16. 1xTxxHMfUE8_q04 (Band 5.5)
# Transcript: "entirely changed... new opportunity... Commerce streams in deeply... so enjoyed over there... darker side of this aspect... adults people... socialize... worldwide knowledge... creative..."
# Analysis: "streams in deeply" (in depth). "adults people" (adults). "darker side of this aspect" (negative side).
# - Verdict: Band 5.5.

# 17. Yz9fa7cVUpg_q02 (Band 5.5)
# Transcript: "like about my hometown is the nature... green nature... helpful to me..."
# Analysis: "like about my hometown" (what I like).
# - Verdict: Band 5.5.

# 18. Yz9fa7cVUpg_q03 (Band 5.5)
# Transcript: "hometown change quite little bit change... old houses developed... local budgets... local teas with breads... bajars... house owner has a TV..."
# Analysis: "change quite little bit change" (changed a bit). "budgets" (markets? bazaars?). "bajars" (bazaars).
# - Verdict: Band 5.5.

# 19. Yz9fa7cVUpg_q04 (Band 5.5)
# Transcript: "not there is any challenges... natural diseases... helpful to each other..."
# Analysis: "not there is" (there are no). "natural diseases" (disasters?).
# - Verdict: Band 5.5.

# 20. Yz9fa7cVUpg_q05 (Band 5.5)
# Transcript: "should be need development... roads are so bricked... solved out..."
# Analysis: "should be need development" (need development). "bricked" (broken? brick?). "solved out" (solved).
# - Verdict: Band 5.5.

scored_samples = [
    {
        "id": 0, "sample_id": "RP_rO0mrjnA_q08", "video_id": "RP_rO0mrjnA",
        "part": 1,
        "question": "Enjoy food?",
        "transcript": "Well, it depends on the more. If I if I need to get a fast food, I enjoy fast food too. But I prefer fast food on these foods because they are spicy and I can eat a lot more.",
        "word_count": 41,
        "analysis_metadata": {
            "grammar_error_patterns": ["coherence"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["coherence_breakdown"],
            "vocabulary": ["meaning_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'depends on the more' (mood?). 'prefer fast food on these foods' (?)."
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
                "why_not_6": "Frequent errors.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Confusion.",
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
        "id": 0, "sample_id": "RP_rO0mrjnA_q09",
        "video_id": "RP_rO0mrjnA",
        "part": 1,
        "question": "Traveling?",
        "transcript": "Not much. I prefer my home cooking because my stomach stomach is not very well conditioned. So whenever I eat food from hotels I got lose motions or cooking problem. Thank you Harasher.",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["home cooking"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'enjoy bottling' (traveling?). 'lose motions' (loose motions). 'cooking problem' (stomach problem?)."
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
                "why_not_7": "Simple.",
                "why_not_5": "Clear."
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
        "vocab_reason": "Adequate range despite errors. Band 6.",
        "grammar_reason": "Good. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "5FTJQE6szgo_q03",
        "video_id": "5FTJQE6szgo",
        "part": 3,
        "question": "Changing opinions?",
        "transcript": "You are older do you think age has a factor in that yeah i think so i believe it is one of the factors of course it depends on the personality but usually i think younger people change their minds easily yeah when do people change opinions let me think i think when they face some difficulties they probably change their opinions and think other ways to solve the problem do you think media plays a big role in changing people's opinions yes i think so because if they get to know information about things I am sure it might change their opinions who do people turn to for advice sorry can you repeat the question sure who do people turn to for advice i think people usually want advice from teachers or parents and older people because they have more experience than them friends do not have that much difference of an experience though right so when would be an opportunity that you can ask your friends for advice do you think well it also depends on the person of course but for me I am really indecisive so i usually ask my friends to give me some opinions about my idea because I am not always sure if my opinion is right or wrong so yeah okay do people like to give opinions about politics some of them yeah i do not really like to talk about politics because i do not have narrative politics but some of them probably want to talk about it especially if they are interested in politics do you think more people should give their opinions about politics yeah i think so in order to make the society better i think they should discuss politics more often do you think it should be everybody in.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["collocation"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["indecisive", "face difficulties", "solve the problem"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["collocation_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'age has a factor' (is a factor). 'narrative politics' (interest in?)."
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
                "why_not_7": "Good.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Collocation slips.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good words ('indecisive'). Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "5FTJQE6szgo_q04",
        "video_id": "5FTJQE6szgo",
        "part": 3,
        "question": "Politics?",
        "transcript": "General or do you think it should be more older people or younger people i think it should be everyone talking about politics because people have different opinion and i believe their ages matters to the opinions so yeah i think it should be a blue one okay thank you that is the end of the speaking test you.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["different opinion"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'ages matters' (age matters). 'a blue one' (everyone?)."
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
                "why_not_7": "Agreement errors.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Pronunciation ambiguity.",
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
        "id": 0, "sample_id": "hKGoyMp9g3w_q02",
        "video_id": "hKGoyMp9g3w",
        "part": 1,
        "question": "Online shopping?",
        "transcript": "Called D is really very famous it is famous Yeah Yeah from that platform I used toy buy several things like I also I also buy some item watches i m buy it several time how often can you say in a precise how often do you tend to buy yeah yeah I once a month no no I used to buy it twice or Thrice you know annual okay so what are the last item that you bought from the online platform it is very recently I think it is become two week ago we ago you bought about one cheer pillow which help which helps our lumber support oh pillow yes Lumber pillow you can say that that means every kind of items are available in this platform all right do you ever see things in shops and then you you buy online or you see online and you buy online what do you do sorry pardon please do you see do you first see the things at a saw in your city and then you decide to buy through online or you see all those things necessary on the online platforms and then you decide to buy online I prefer I do not use to buy unnecessary things I do not want to waste my money if I think it is need or it is necessary for them I just scroll my phone and M and I just you use only this platform right so do you think the popularity of online shopping is more popular and popular these days yes it now there is this is trending oh yeah being now geni generation today's guys and guys are really very what is called that common in phone always using phone and.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form", "preposition"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["lumber support", "unnecessary things"],
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
            "reason": "'used toy buy' (to buy). 'cheer pillow' (chair). 'lumber support' (lumbar). 'things at a saw' (store). 'it is need' (needed)."
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
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Adequate range ('lumbar support'). Band 6.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "hKGoyMp9g3w_q04",
        "video_id": "hKGoyMp9g3w",
        "part": 3,
        "question": "Family occasions?",
        "transcript": "Going to be there again maybe in the next marriage we discuss about that type of things okay thank you very much thank you well in the second well in the third part of the speaking test we will discuss on some topics on a couple of topics let us first discourse family occasions when do families celebrate together in your country country is occasionally in a festival like thar and chart these these are our main Festival which are celebrated in our Nepal how often do all the generations in a family come together in a country it is like all generations come together there are some occasions yes yes I think that is the Das where wow okay all generation are get together and putting Tika on their forehead and enjoying their meals having fun and playing cards together together with our family members and that is the one of the most memorable events for why do you think some people actually do not enjoy attending occasions some occasions it is some people do not enjoy it is about their it is about their individuals thinking and and their mentality too and their life phases how their life is going on of the life is going smoothly then they generally come to and meet us if they they are in downwards in their life then they used to pretend this type of things and if they they are suffering from something sick illness body illness then they used to they do not able to come or present in yeah our occasion okay mainly people are in our country are so what we can say all right so.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "verb_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["life phases", "mentality", "downwards in their life"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'discourse' (discuss). 'downwards in their life' (downturn/hard time). 'body illness' (illness). 'do not able to' (are not able to)."
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
                "why_not_7": "Word choice.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good attempts ('mentality', 'life phases'). Band 6.",
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "hKGoyMp9g3w_q05",
        "video_id": "hKGoyMp9g3w",
        "part": 3,
        "question": "Parental help?",
        "transcript": "Think it is a good thing for parents to help their children with their school assignments or with the school work some people some parents actually like to help the children with the school work Works do you think it is a good idea or not yes it is really very good idea it is a sign of good parenting yes it is it is sign of good parenting and in the past my father's my father was also support me to make my homework made my homework which I do not know and I even ask also with my elder sister please help me I do not know this and this is one of the good things and it is good guidance too okay how you think it is for families to eat together at least once a week is it necessary that all family members gather together in a dining hall around the dining table and eat together at least once a week yeah it is really very important because in a because in our daily life nowadays we are so busy oh yeah yeah yeah you are right we are so busy in our da we cannot able to sit always have meal or dinner in a single dining table by sitting in single dining table or eating together we can share our feelings thoughts or what we are going or what happened to our in our past life how we can we can discuss about that things and any problem is there arise we can discuss or find out any Solution by eating or having this do you believe that everyone in a family should share some hous World Walks Like The walks hous world tours housew World talks would be divided among.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["verb_form", "preposition"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["good parenting", "guidance", "school assignments"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'father was also support me' (supported). 'make my homework' (do). 'cannot able to' (are not able to). 'single dining table' (at the same table). 'tax' (tasks/talks)."
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
                "why_not_7": "Collocations ('make homework').",
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
        "grammar_reason": "Errors. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "hKGoyMp9g3w_q06",
        "video_id": "hKGoyMp9g3w",
        "part": 3,
        "question": "Housework?",
        "transcript": "All family members and get get get them done or one person should you know perform more than the other family members what do you say about it I think doing all together is a good thing for our family and for all of the family because if we have no idea about that work then we have to leave by saying sorry I do not know about I have noide idea about these things if you have some idea or you can give some help to do any tax of your household work then you have to support your family or any family members",
        "word_count": 94,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["support your family"],
            "grammar_structures_used": ["conditionals"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'tax of your household' (tasks). 'leave by saying sorry' (avoid it?)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Wrong word 'tax'.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Adequate despite 'tax'. Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "3GYrVH3BFhI_q01",
        "video_id": "3GYrVH3BFhI",
        "part": 1,
        "question": "Internet?",
        "transcript": "Yes thank you welcome okay so how often do you go online i usually go online every day by my phone what do you use the internet for i being a computer engineer i use these for downloading software uploading software and also for some time use networking and these are the things i do on internet okay how do you get online i i have got a 2-3 gadget electronica so i can go easily online preferably i use my cell phone for all go online and other from laptop do you have your own computer yes I have got two computers i got one laptop and one desktop i use mostly my laptop because because it is easy to carry and carry anywhere okay what is your favorite website well being a computer engineer my favorite website is a filehippo.com and i can easily find out their mac and windows software easily and update my windows and these are very helpful for me do you think children should be allowed unsupervised access to the internet well according to me and this is a very dangerous for children for development and for their character they should use internet in the supervision of their parents okay let me ask you your.",
      "word_count": 204,
        "analysis_metadata": {
            "grammar_error_patterns": ["preposition", "article"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["computer engineer", "unsupervised access", "downloading software"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["preposition_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'by my phone' (on). 'gadget electronica' (electronic gadgets). 'for all go online' (to go online)."
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
                "why_not_7": "Preposition/Structure errors.",
                "why_not_5": "Complex structures."
            },
            "vocabulary": {
                "why_not_7": "Phrasing errors.",
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
        "id": 0, "sample_id": "3GYrVH3BFhI_q02",
        "video_id": "3GYrVH3BFhI",
        "part": 2,
        "question": "Washington DC?",
        "transcript": "Is of washington dc and this is district of columbia and it is a capital of usa and it is situated in the central part of america and it is famous for neoclassical amusement monument buildings and it is also famous for iconic museum it is a most beautiful and elegant and planned city and here i can easily find out basic immunity and i am a shopik show politic person so i love to shop everywhere so i can find easily here world-class shopping wall i can shop there and one other thing is the famous that is a smooth and hassle-free transportation system and and there is no environment pollution and it is safe and secure to live here and it is a heaven for civilized people and one other thing is a good good job opportunity and for a better future for my children education that is why i want to move there okay so can i take it back please yes here it is thank you let me ask you some more questions.",
      "word_count": 182,
        "analysis_metadata": {
            "grammar_error_patterns": ["article", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["neoclassical", "hassle-free transportation", "civilized"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'amusement monument' (museums/monuments?). 'basic immunity' (amenities). 'shopik show politic' (shopaholic). 'shopping wall' (mall)."
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Pronunciation affects meaning ('immunity').",
                "why_not_5": "Good range attempts."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good range but clarity issues. Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "3GYrVH3BFhI_q03",
        "video_id": "3GYrVH3BFhI",
        "part": 3,
        "question": "Cities/Migration?",
        "transcript": "Old when choosing where to live well young generations love to live in crowd crowded place and for better job opportunity they love to live in cities modern cities and on the other hand if we talk about older people so they they want to live in safe and peace peace they chose countryside area okay when did you make up your mind to move to city well when i passed my senior secondary school i was looking for an engineering college for my higher education then i cannot find here and i find that college in gurgaon and i moved to that city how long did you stay there i stayed there for four hours during my graduation okay and what kind of changes can you see in modern cities nowadays well there is a too much changes in modern city that there is recreational park shopping malls and metros and a good transportation system road facility and bridges these are coming good in modern cities okay and where are the people migrating to these cities for all well mostly people come from countryside for their to for their good opportunity for jobs business and for their better health education system they are moving from countryside to cities okay and what kind of problems people are facing in modern cities well there are a lot of problems they are facing day by day like they have to interact with stranger daily and there is no security in living in the cities so these are most prominent and one one other also problem is the pollution that is facing daily these are the most problems last question for today and that is can you suggest some solution to these problems yes i can suggest solution to government that they should provide.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "article"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["recreational park", "transportation system", "migrating", "prominent"],
            "grammar_structures_used": ["complex_sentences", "contrast"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'make up your mind' (decide). 'road facility' (facilities). 'interact with stranger' (strangers). 'too much changes' (many changes)."
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
                "why_not_7": "Errors ('too much changes').",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Minor errors.",
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
        "id": 0, "sample_id": "3GYrVH3BFhI_q04",
        "video_id": "3GYrVH3BFhI",
        "part": 3,
        "question": "Solutions?",
        "transcript": "These basic amenities to countryside area and also good education and create job for youngster then they cannot move to other other cities so.",
        "word_count": 22,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["basic amenities", "create job"],
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
            "reason": "'create job' (jobs). 'cannot move' (will not/might not)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
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
                "why_not_7": "Short.",
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
        "vocab_reason": "Adequate. Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "1xTxxHMfUE8_q02",
        "video_id": "1xTxxHMfUE8",
        "part": 1,
        "question": "Holidays?",
        "transcript": "Focus businesses yes few questions will be based on holidays do you like holidays yes of course I really like holidays because in the holidays I have a lot of spare time in order to spend with my families as well as my near and dear ones where do you go for your holidays in my holidays I I prefer to visit new places so that I can ex I can enhance my knowledge about about the places and know it it it helps me to enhance my knowledge about the culture of that place what what do you want holidays well as a earlier mentioned sometimes I wasted some new places but when there is no plan to go anywhere so I prefer to visit in the library in order to complete my study work few questions will be based on Primary School okay how was your primary school like a primary school was very good where the tea where the the all of the experience of teachers was very good and I enjoyed a lot with my friends over there yes of course I really like my primary schools in the past even today I also like my primary school because all of the ma'am all of the good memories are connected with my primary school what did you do in your leisure time in your primary school I would really remember when the time was a recessed so I usually played with my with my classmates as well as participated many activities which were given by our teachers one now I am going to ask a.",
        "word_count": 236,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["near and dear ones", "enhance my knowledge", "spare time"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'wasted some new places' (visited). 'recessed' (recess). 'participated many activities' (participated in)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Errors.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Word choice errors.",
                "why_not_5": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good range but errors. Band 6.",
        "grammar_reason": "Errors present. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "1xTxxHMfUE8_q04",
        "video_id": "1xTxxHMfUE8",
        "part": 3,
        "question": "School change?",
        "transcript": "Life my life was entirely changed I got new opportunity to meet new teachers as well as friends so I and one most interesting fact was that you know I got opportunity to to enhance my knowledge about the Commerce streams in deeply and I was so enjoyed over there in my new schools overall that was the time when I have changed my school okay this is time to ask some follow-up questions are children better at solving problem than adults according to my perspective children should better children should better in order to solve any kind of problems but but but the darker side of this aspect must not be ignored because because the adults people have a lot of experience so they can they can try they can try better in order to solve problem how do children well there are many there are many ways in order to socialize with with each other and children can follow all of them such as they can and they can talk to each other and as well as they can share their majority of the things with with each other which makes them socialize what there may be a lot of benefits to changing to change a school such as children can learn a lot of things from there not only related their study but also worldwide knowledge they can gain over there you know in addition to this they can they can meet their new friends which which which make which which would make them creative who will make them okay how do parents prepare their kids to go to school on very first day can you repeat the question yes how do parents prepare their children or kids to go to school on Thursday well.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["entirely changed", "enhance my knowledge", "socialize", "worldwide knowledge"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'streams in deeply' (in depth). 'was so enjoyed' (enjoyed it). 'darker side of this aspect' (negative aspect). 'adults people' (adults). 'majority of the things' (most things)."
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
                "why_not_7": "Structure errors.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Word choice errors.",
                "why_not_5": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Good range. Band 6.",
        "grammar_reason": "Errors present. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Yz9fa7cVUpg_q02",
        "video_id": "Yz9fa7cVUpg",
        "part": 1,
        "question": "Hometown?",
        "transcript": "Well, I like about my hometown is the nature, the green nature around me and the locals. They are so helpful to me and the environment I enjoy the most.",
        "word_count": 29,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["green nature", "locals"],
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
            "reason": "'like about my hometown' (what I like about...)."
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
                "why_not_7": "Fragment.",
                "why_not_5": "Clear."
            },
            "vocabulary": {
                "why_not_7": "Basic.",
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
        "grammar_reason": "Structure issues. Band 5.",
        "vocabulary": 6,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Yz9fa7cVUpg_q03",
        "video_id": "Yz9fa7cVUpg",
        "part": 1,
        "question": "Hometown changes?",
        "transcript": "Yes, of course. my hometown change quite little bit change there because when I was a child I go to my hometown I see the environment is so normal at that time but now there are changes so many things like the old houses developed so much and the people living are changed from them that to now what is the most famous landmark or attraction in your hometown Well, I do not know about that thing so much. but I think the attraction place that is the local budgets of my hometown because when I visited my hometown, I often spend my whole day I say that the afternoon I spend there. I go to the tea shops. I try the local teas with breads. they are so tasty. And I see the most people they came from the town they also visited the bajars because the bajger is so what do people in your hometown usually do in their free time? well in the free time they often spend time with their families and go outside with their friends because there there is everyone like a family. They visited each other houses. In the afternoon they go to the house. the house owner has a TV. They go there and sit to watch a television show with everyone. that is they do in their free time.",
        "word_count": 218,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["attraction place", "local teas"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'change quite little bit change' (changed a bit). 'budgets' (markets/bazaars). 'bajars' (bazaars)."
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
                "why_not_6": "Word choice errors.",
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
        "id": 0, "sample_id": "Yz9fa7cVUpg_q04",
        "video_id": "Yz9fa7cVUpg",
        "part": 1,
        "question": "Problems?",
        "transcript": "Well I think not there is any challenges or problem in my hometown because the my hometown is normal place. There is no natural natural how should I say that there is no natural diseases and people are helpful to each other. when when someone gets in trouble the others came to help help them and that is it.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["natural diseases"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["structure_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'not there is any' (there are no). 'natural diseases' (disasters?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
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
                "why_not_6": "Structure errors.",
                "why_not_4": "Clear."
            },
            "vocabulary": {
                "why_not_6": "Word choice error.",
                "why_not_4": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts to use complex sentences but these tend to be less accurate.",
            "vocabulary_band": 5,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Error. Band 5.",
        "grammar_reason": "Error. Band 5.",
        "vocabulary": 5,
        "grammar": 5
    },
    {
        "id": 0, "sample_id": "Yz9fa7cVUpg_q05",
        "video_id": "Yz9fa7cVUpg",
        "part": 1,
        "question": "Improvements?",
        "transcript": "Well I I think that the roads, the schools, the hospital I think that they should be need development because in my hometown the roads are so bricked and I think that if the government looks at the roads they should help the locals by the roads and the schools are far away for the students to go to study in the schools. It takes so many times to travel. that is why I think that it should be solved out.",
        "word_count": 80,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["development", "government"],
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
            "reason": "'should be need development' (need development). 'bricked' (broken?). 'solved out' (solved)."
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
        "vocab_reason": "Errors. Band 5.",
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
