import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 212 ---
# Total Samples: 20
# Samples Analyzed:

# 1. Nj9xEQZbtYs_q04 (Band 9.0)
# Transcript: "...make pottery or how to act on the stage... ITV is our channel three in the uk... watch that together as a family... making a painting... presenter hosts the show... theatrical and very friendly... picks on people in the audience... cilla black's blind date... match make people... hidden candidate..."
# Analysis:
# - Grammar: "picks on people" (good phrasal verb, though usually negative, here means 'selects playfully'). "match make people" (matchmake). "making a painting" (painting / creating a painting).
# - Vocabulary: "theatrical", "presenter", "match make", "hidden candidate", "pottery".
# - Note: British English context ("ITV", "Cilla Black"). Native speaker or very high proficiency.
# - Verdict: Band 9.0.

# 2. Nj9xEQZbtYs_q07 (Band 9.0)
# Transcript: "sense a pattern... drama related to action... view romantic things... nitpicky and definitely generalize... sweet angle towards it... energetic... hormones... gripping stuff..."
# Analysis:
# - Grammar: "issues are to do with hormones" (good). "most likely to view" (are most likely).
# - Vocabulary: "nitpicky", "generalize", "hormones", "gripping stuff", "sweet angle".
# - Verdict: Band 9.0. "nitpicky" is excellent informal vocab.

# 3. Nj9xEQZbtYs_q11 (Band 9.0)
# Transcript: "The idea and stop answering the question... pace of your speech... connectives and conjunctions... conversational... eye contact... reduce your stress levels..."
# Analysis: FEEDBACK/TUTORIAL. The examiner is giving feedback to the candidate.
# - Verdict: INVALID (Skip).

# 4. dOVJbK6SWR4_q02 (Band 6.0)
# Transcript: "appreciate this this person... prefer computer to type in computer... write by pen... feel more comfortable... explain my some things... technology nowadays really go first... opinions my view..."
# Analysis:
# - Grammar: "explain my some things" (explain some things). "technology nowadays really go first" (goes fast? advances?). "type in computer" (on a computer).
# - Vocabulary: Basic. "appreciate", "opinions", "view".
# - Verdict: Band 6.0. Frequent errors but intelligible.

# 5. dOVJbK6SWR4_q04 (Band 6.0)
# Transcript: "About a time when you helped someone and I would like to discuss with you one or two more general questions related to this so."
# Analysis: EXAMINER SPEECH (Instruction).
# - Verdict: INVALID (Skip).

# 6. dOVJbK6SWR4_q05 (Band 6.0)
# Transcript: "Caring jobs... nurses doctors help people to to become healthy again... kind tolerant and Cooperative... people need some help... nurses also teachers are get less salaries... they should be paid more... become health... get their confidence again..."
# Analysis:
# - Grammar: "teachers are get less salaries" (get lower salaries / are paid less). "become health" (healthy). "very great thing".
# - Vocabulary: "tolerant", "cooperative", "salaries".
# - Verdict: Band 6.0.

# 7. Xz0scl3ozAg_q02 (Band 7.0)
# Transcript: "many vexillators such as cinema hospital... concentrate on my study... around 30 days per year... korean thanksgiving day... i lived in germany for 10 years... extend the public holidays... i am foodie... how to cook various foods..."
# Analysis:
# - Grammar: "vexillators" (facilities? vacations?). "i am foodie" (a foodie). "eating many food" (much food / lots of food). "mother always want to teach me" (wants).
# - Vocabulary: "foodie", "concentrate", "extend".
# - Verdict: Band 6.5/7.0. "vexillators" is a strange error (mispronunciation of 'facilities'?). "many food" is a common error. I'll stick to 6.5 given the errors. GT is 7.0. Maybe "vexillators" was "vacation spots"?

# 8. Xz0scl3ozAg_q03 (Band 7.0)
# Transcript: "dreamed of being a politician... barack obama... attended his speech... informative... charismatic... reduce unemployment rates... financial crisis... health welfare... looked up to him a lot..."
# Analysis:
# - Grammar: "finish the world in the iraq" (finish the war in Iraq). "improves the health welfare" (improved). "most successful politician who i have ever met" (met? or seen? Obama is famous).
# - Vocabulary: "charismatic", "unemployment rates", "financial crisis", "health welfare". Good topic vocab.
# - Verdict: Band 7.0. Stronger vocab here.

# 9. Xz0scl3ozAg_q04 (Band 7.0)
# Transcript: "youtube star... own concert... easy to be a famous... disadvantages of being a famous person... like of their privacy... take picture of them together... make profits... keep be famous... make small mistakes... alter other ties doing election... public sciences..."
# Analysis:
# - Grammar: "easy to be a famous" (famous). "famous people like of their privacy" (lack?). "keep be famous" (remain famous). "alter other ties" (advertise?). "public sciences" (public service announcements?).
# - Vocabulary: "privacy", "profits", "disadvantages".
# - Verdict: Band 6.5. "like of their privacy" (lack) is a key meaning error. "public sciences" (?). GT is 7.0. I will score 6.5/7.0.

# 10. Xz0scl3ozAg_q05 (Band 7.0)
# Transcript: "positive influence... youngsters always want to follow them... commit screening... mimic children to follow their behavior... donate to society... commit criminals... taking drugs..."
# Analysis:
# - Grammar: "commit screening" (commit crimes? screening?). "mimic children" (children mimic them?). "commit criminals" (commit crimes).
# - Vocabulary: "donate", "positive influence".
# - Verdict: Band 6.5. "commit screening" and "commit criminals" are significant errors.

# 11. kP31U0YoKr4_q02 (Band 6.0)
# Transcript: "And go to cinema my favorite movies Avengers okay very good very good and yeah in keeping with the topic of public holidays."
# Analysis: Short. "go to cinema".
# - Verdict: Valid (Band 6).

# 12. kP31U0YoKr4_q04 (Band 6.0)
# Transcript: "more people likes to travel... older people enjoy traveling... after I retire they already got some money... after every coin in Virginia... private transport is more convenient... do not need to wait this destination... stalled... Gangnam station... satisfied... i satisfy him..."
# Analysis:
# - Grammar: "more people likes to travel" (like). "after every coin in Virginia" (ASR error? "after having coin"?). "public trans person" (transport). "i satisfy him" (I am satisfied).
# - Vocabulary: "convenient", "destination", "advantage".
# - Verdict: Band 6.0.

# 13. kP31U0YoKr4_q05 (Band 6.0)
# Transcript: "I went China... use transfer our public transport... feel a little bit confused... streaky and raging... travel one year before to go university... spread their vision... dangerous by accident... take their monies... all ones ponies..."
# Analysis:
# - Grammar: "I went China" (went to China). "use transfer" (used). "spread their vision" (broaden their horizon?). "take their monies" (money). "all ones ponies" (phones?).
# - Vocabulary: Limited. "streaky and raging" (ASR error? "tricky and raging"?).
# - Verdict: Band 5.5/6.0. Significant coherence issues due to vocab/pronunciation.

# 14. reaDH_jQkxw_q03 (Band 8.5)
# Transcript: "ski trip... Afra R of learning schem... foreign teacher... gifted ability... delivered like what he learned... beginner courses... has my back... reliable person... playing tricks on me..."
# Analysis:
# - Grammar: "Afra R" (afraid). "learning schem" (skiing). "teach mey" (me). "has my back" (idiom).
# - Vocabulary: "reliable", "gifted ability", "abroad".
# - Verdict: Band 8.5. Good flow and idioms.

# 15. reaDH_jQkxw_q04 (Band 8.5)
# Transcript: "dedicated his time... ski in a fun way... drwn in a like a ski slope... bad childood memory... thanks to my brother... hobes... br about it..."
# Analysis:
# - Grammar: "dedicated his time". "drwn" (thrown? down?). "hobes" (hobbies). "br about it" (brag).
# - Verdict: Band 8.5.

# 16. reaDH_jQkxw_q05 (Band 8.5)
# Transcript: "socialize with others... get along with their peers... educational materials... academic stuff... moral lessons... enroll a class... elderly who is not familiar... access to education..."
# Analysis:
# - Grammar: "get along with their peers" (good). "parents are more has the responsibility" (have). "enroll a class" (enroll in).
# - Vocabulary: "peers", "socialize", "moral lessons", "academic".
# - Verdict: Band 8.5.

# 17. reaDH_jQkxw_q06 (Band 8.5)
# Transcript: "YouTube is a great example... great platform for Education... keyword... advanced level... start out a new thing..."
# Analysis:
# - Grammar: "start out a new thing" (start a new thing).
# - Vocabulary: "platform", "keyword", "advanced level".
# - Verdict: Band 8.5.

# 18. aaRQJmv4-gc_q02 (Band 6.5)
# Transcript: "Romance Jour... enhance my imagination... more convenience and access accessible accessibility... environmental friendly..."
# Analysis:
# - Grammar: "it more convenience" (it is more convenient). "environmental friendly" (environmentally). "Romance Jour" (Genre?).
# - Vocabulary: "enhance", "accessibility" (struggled).
# - Verdict: Band 6.5.

# 19. aaRQJmv4-gc_q03 (Band 6.5)
# Transcript: "pop culture in Japan... get know more about them... dream destination... explore both the past and the future... top priority on my bual list..."
# Analysis:
# - Grammar: "get know more" (get to know). "bual list" (bucket list).
# - Vocabulary: "dream destination", "top priority".
# - Verdict: Band 6.5.

# 20. aaRQJmv4-gc_q04 (Band 6.5)
# Transcript: "attract a lot of visitors... demand is high... string or completely string ation... accompany us... deeply knowledge... wander around... speaking resource range..."
# Analysis:
# - Grammar: "string ation" (strange location?). "deeply knowledge" (deep). "wander around".
# - Vocabulary: "accompany", "wander".
# - Note: End of transcript has "speaking resource range...". Examiner/System text? The candidate speech ends at "thank you that is the end...".
# - Verdict: Band 6.5.

scored_samples = [
    {
        "id": 0, "sample_id": "Nj9xEQZbtYs_q04", "video_id": "Nj9xEQZbtYs",
        "part": 1,
        "question": "TV programs?",
        "transcript": "They would have to get into games and do different activities and then they will be scored at the very end and i always found that very interesting because they get put in situations where they would not know how to for example make pottery or how to act on the stage it depends what the activity is we always watch this program we found out about it from itv though advertising itv is our channel three in the uk and we we just love to sit around the television and watch that together as a family we find it most fun so i enjoy the activities that they do like i said they they get onto the stage they have to do an acting game or they will be maybe making a painting to see who could perform the painting better than the other and i always like the way the presenter hosts the show he is always very energetic and the way he addresses the candidates and then the way he talks to the audience it is always very theatrical and very friendly at the same time and then in between he he goes on about joking and trying to encourage other people to get up on the stage and get involved and sometimes he even picks on people in the audience so it is a very very fun show to watch another show I would like to talk about is cilla black's blind date and that is where she brings people on to actually match make people single people of course and then if they pick the hidden candidate and they like what the other person is saying then they will choose that person to maybe go on holiday that is that is the thing they will go on the trip and then they will come back next week.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["picks on people", "theatrical", "match make", "hidden candidate", "energetic"],
            "grammar_structures_used": ["complex_sentences", "phrasal_verbs"]
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
            "reason": "'match make' (matchmake). 'picks on people' (used playfully). 'making a painting' (painting)."
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
                "why_not_9": "'theatrical', 'picks on'. Native usage.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent natural expressions. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "Nj9xEQZbtYs_q07", "video_id": "Nj9xEQZbtYs",
        "part": 3,
        "question": "Viewing patterns?",
        "transcript": "Maybe sense a pattern of what they are watching so if it is young people they will be probably watching a drama related to action if it is if we are talking about boys males or men if we are talking about girls maybe the most likely to view romantic things romantic tv series and why do you think is that like why do they like to watch romantic movies i think lots of these issues are to do with hormones i mean i do not like to be nitpicky and definitely generalize on all these things but generally girls love to watch tv series or movies that are romantic and they have some kind of a sweet angle towards it boys because they they tend to be more energetic and again to do with the hormones they love to watch action and be entertained with all that gripping stuff thank you very much we are done with your speaking test for today now you can just relax and take a deep breath thanks yes great good so let us see what you did in your.",
        "word_count": 182,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["nitpicky", "gripping stuff", "sweet angle", "generalize", "hormones"],
            "grammar_structures_used": ["complex_sentences", "hedging"]
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
                "why_not_9": "'nitpicky', 'gripping stuff'. Excellent informal/natural vocab.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Highly natural ('nitpicky'). Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "dOVJbK6SWR4_q02", "video_id": "dOVJbK6SWR4",
        "part": 1,
        "question": "Writing preferences?",
        "transcript": "By yourself and it means that you are you you are already appreciate this this person do you prefer writing with a pen or using a computer I sometime it depends on the situation for example for my studies I prefer computer to type in computer but for my essays I prefer to write by pen why because I feel more comfortable when I when I try to explain my some things which I want to say it is more comfortable and easy to write it yourself do you write more now or less than you did a few years ago I think less because technology nowadays really go first so and do you like to write stories or poems not actually just I like to write my opinions my view for example about the world about animals about persons thank you.",
        "word_count": 145,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_order", "agreement"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["appreciate", "technology", "opinions", "comfortable"],
            "grammar_structures_used": ["simple_sentence", "compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["word_order_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'explain my some things' (explain some things). 'go first' (fast?). 'persons' (people)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "moderate",
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
                "why_not_7": "Frequent errors.",
                "why_not_5": "Understandable."
            },
            "vocabulary": {
                "why_not_7": "Basic range.",
                "why_not_5": "Sufficient for task."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Basic but adequate. Band 6.",
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "dOVJbK6SWR4_q05", "video_id": "dOVJbK6SWR4",
        "part": 3,
        "question": "Caring jobs?",
        "transcript": "Caring jobs yes I think the first of all so in the hospital nurses doctors they help people to to become healthy again what what sort of qualities does a person need to work in that sort of job you mean to become a doctor or not not qualifications but what kind of person is makes a a good nurse or a good doctor I think he or she should be very kind tolerant and Cooperative why why why tolerant tolerant because people need some help and people all people need the the same and they so people like nurses in that sort of job do you think that their salaries are too low maybe if the N nurses nurses I think not only nurses also teachers are get less salaries than other types of they should be paid more yeah I think think so because they do very great thing they help people to to become health and to to to to to get their confidence again and it is very great job I think",
        "word_count": 165,
        "analysis_metadata": {
            "grammar_error_patterns": ["structure", "word_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["tolerant", "cooperative", "salaries", "confidence"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["verb_form_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'become health' (healthy). 'are get less salaries' (get lower salaries). 'very great thing'."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
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
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex sentences attempted."
            },
            "vocabulary": {
                "why_not_7": "Limited range ('great thing').",
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
        "grammar_reason": "Frequent errors but clear meaning. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Xz0scl3ozAg_q02", "video_id": "Xz0scl3ozAg",
        "part": 1,
        "question": "Holidays?",
        "transcript": "There in your hometown yeah of course there are many vexillators such as cinema hospital and supermarkets and so on and also these days i like going to cafe because it is good to concentrate on my study okay very good very good so now we are going to talk about public holidays so how many public holidays are there in your country okay I am not sure but i think there are around 30 days per year in korea the big there are two big ones korean thanksgiving day and new year's day yeah and do you think people need more public holidays i do not think so because i lived in germany for 10 years and i felt that korea in korea there are enough public holidays but people do not have many very much or many paid holidays so i think they they do not need to extend the public holidays okay good and which holiday is your favorite yes my favorite one is korean thanksgiving day because I am foodie so i like eating many food and my mother always want to teach me how to cook various foods so i enjoy it a lot okay okay very good very good okay so that will do us for the first part of the test so.",
        "word_count": 204,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "article"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["paid holidays", "extend", "foodie", "concentrate"],
            "grammar_structures_used": ["complex_sentences", "comparatives"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'vexillators' (facilities?). 'many food' (much food). 'i am foodie' (a foodie). 'mother always want' (wants)."
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
                "why_not_7": "Agreement errors ('mother want').",
                "why_not_5": "Complex structures."
            },
            "vocabulary": {
                "why_not_7": "Errors ('many food', 'vexillators').",
                "why_not_5": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors present but good range. Band 6.",
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Xz0scl3ozAg_q03", "video_id": "Xz0scl3ozAg",
        "part": 2,
        "question": "Politician (Obama)?",
        "transcript": "Was 13 i have dreamed of being a politician in korea so today I am going to talk about president of the u.s as you might know barack obama is the former president of the u.s and it is about five years ago i attended his speech and it was really informative at the time he explained about his achievements and he looked very charismatic for example how could he reduce unemployment rates after a financial crisis in the u.s how could he finish the world in the iraq as well as that he improves the health welfare of the u.s so it was really impressive and moreover as i said previously i have dreamed of being a politician in korea and in my opinion he is the most successful politician who i have ever met and that is why i want to meet him in the future and i looked up to him a lot okay when i when i was in his speech he explained also about his own private life and",
        "word_count": 172,
        "analysis_metadata": {
            "grammar_error_patterns": ["tense", "word_order"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["charismatic", "unemployment rates", "financial crisis", "health welfare", "achievements"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["tense_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'finish the world' (war). 'improves the health' (improved). 'met' (seen/know)."
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
                "why_not_8": "Tense errors.",
                "why_not_6": "Good range."
            },
            "vocabulary": {
                "why_not_8": "Some inaccuracy.",
                "why_not_6": "Strong topic vocab."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Strong topic words ('financial crisis'). Band 7.",
        "grammar_reason": "Some errors but complex. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "Xz0scl3ozAg_q04", "video_id": "Xz0scl3ozAg",
        "part": 3,
        "question": "Fame disadvantages?",
        "transcript": "Be youtube star and on the streets in korea there are many people to do their own concert and also many people even if someone have talents in dance or singing then it is easy to be a famous i think okay okay good good and what do you think are some of the disadvantages of being a famous person i think the famous people like of their privacy for example if even though they just want to have a dinner or lunch in a restaurant many people might want want to be i want to take picture of them together so they can enjoy their normal life and yeah i think this is the biggest disadvantages of being famous okay good and do you think famous people have a responsibility to be friendly to their fans yes of course because it is obvious that the fans love love this famous person and also so that is why they can make profits and they can be keep be famous and even though they just make small mistakes on televisions or some public places even they if they if a famous person have has a lot of fun then i think it is hard to be be disliked by many people i think okay right very good very good and what influences can famous people have on society in society okay yeah well these days the governments want to alter other ties doing election by advertising the famous people for example in the u.s i heard that one famous singer i i cannot remember his name exactly but the rate of doing election was really a role but the u.s use a public sciences the.",
        "word_count": 274,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["privacy", "profits", "disadvantages"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["word_choice_error"],
            "vocabulary": ["meaning_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'like of their privacy' (lack). 'easy to be a famous' (famous). 'keep be famous' (remain). 'alter other ties' (advertise?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
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
                "why_not_7": "Key meaning errors ('like' for 'lack').",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors affect meaning ('like' vs 'lack'). Band 6.",
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "Xz0scl3ozAg_q05", "video_id": "Xz0scl3ozAg",
        "part": 3,
        "question": "Fame duration?",
        "transcript": "This problem by using a famous singer so i think it is the positive influence in the society yeah and how do you think celebrities influence teenagers teenagers yes i think youngsters always want to follow them so if they do like commit screening then it is there are many plus high possibility to mimic children to follow their behavior so yeah i think it depends on the behavior of the famous people okay good and why can some celebrities stay famous for a really long time and others do not okay okay when it comes to the famous the famous singer or actor for a long time i think they keep their activities or they are they are i think they always try to show their talents to the public and also these days many famous people donate to society so that is why they can be famous for a long time when it comes to the other people who are not famous maybe they commit maybe they commit criminals such as taking drugs and so on so that is why they cannot be famous or popular for a long time",
        "word_count": 184,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["donate to society", "positive influence", "mimic"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'commit screening' (?). 'commit criminals' (crimes). 'mimic children' (children mimic)."
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
                "why_not_7": "Errors affect clarity.",
                "why_not_5": "Good range."
            },
            "vocabulary": {
                "why_not_7": "Errors ('screening', 'criminals').",
                "why_not_5": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors ('commit criminals'). Band 6.",
        "grammar_reason": "Errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "kP31U0YoKr4_q02", "video_id": "kP31U0YoKr4",
        "part": 1,
        "question": "Movies?",
        "transcript": "And go to cinema my favorite movies Avengers okay very good very good and yeah in keeping with the topic of public holidays.",
        "word_count": 22,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["go to cinema"],
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
        "grammar_reason": "Basic. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "kP31U0YoKr4_q04", "video_id": "kP31U0YoKr4",
        "part": 3,
        "question": "Travel trends?",
        "transcript": "To travel rather than all the people so I think the more people likes to travel more time all of you / ok I mean do you think older people enjoy traveling these days or also all the people enjoying and likes to go travel but I think they do not have much time so I choose younger people okay good and do you think it is common for people to travel after they retire Yeah right after I retire they already got some money and there are over already ready to travel so I think they will go travel after every coin in Virginia all right very good very good and do you think these days there are fewer private cars on the road because of improved public transportation mmm yes it makes sense but I think private transport is more convenient and public trans person I think most people use ID card more why do you think is more convenient because people who who use private private transport -they do not need to wait this destination like pasta for example public transport there is always stalled and like Gangnam station in such was stationed at one gas station but if they use private transport taking over directly the destination okay yeah it is a big advantage yeah and what do you think needs to be improved in public transportation action I went France and England and China and Japan -lot of country and I experienced that country's public transport but I think in Korea our transport service and qualities the best so I do not think did we need more like service and quality in diamond okay you satisfied yeah i satisfy him how about in the other countries you into how today improve for example China when I was six.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement", "verb_form"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["convenient", "destination", "advantage"],
            "grammar_structures_used": ["simple_sentence", "compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement"],
            "vocabulary": ["unclear_meaning"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "low",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'coin in Virginia' (?). 'public trans person' (transport). 'likes to go travel' (like to travel). 'satisfy him' (satisfied)."
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
                "why_not_7": "Frequent errors.",
                "why_not_5": "Understandable."
            },
            "vocabulary": {
                "why_not_7": "Unclear meanings.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors and unclear parts. Band 6.",
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "kP31U0YoKr4_q05", "video_id": "kP31U0YoKr4",
        "part": 3,
        "question": "Young travel?",
        "transcript": "Or seven mmm-I went China and with my family and we use transfer our public transport but we we feel a little bit confused which part we which direction is right or not so yeah yeah streaky and raging okay okay good good and do you think it is important for younger people to travel for example University students or after high school is it important for them to travel abroad yeah of course because I heard in America day they are like culture like like to travel one year before to go university and I was surprised oh why why they have like that culture but now I can understand why they made like culture because they were you know more people need to watch more good things and for new new things they can they can spread their vision very good is there any negative point so that any negative points of traveling when you are just finishing high school native things actually I did not feel any negative things to travel but if I need to say something I will say and dangerous by accident as if they traveled with their friends with that age 19 20 very risky because some people could attack them or take their monies and just all ones ponies okay very",
        "word_count": 194,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_order", "tense"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["dangerous", "risky", "culture"],
            "grammar_structures_used": ["simple_sentence"]
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
            "reason": "'all ones ponies' (phones?). 'take their monies' (money). 'spread their vision' (horizon). 'streaky and raging' (?)."
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "high",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Frequent errors.",
                "why_not_5": "Understandable."
            },
            "vocabulary": {
                "why_not_7": "Confusion.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Confusion and errors. Band 6.",
        "grammar_reason": "Frequent errors. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "reaDH_jQkxw_q03", "video_id": "reaDH_jQkxw",
        "part": 2,
        "question": "Ski trip?",
        "transcript": "The problem was like I was it was my first time to ever go on a ski trip and I was really Afra R of learning schem from foreigners but then the real problem was learning from a foreign teacher to teach mey was the only option I had since we were abroad so like we were in this kind of trouble where I did not want to go like off to alesson with someone I do not know and like as a child I was really afraid of like being left alone with a forign teacher so like my brother decided to he would learn the skills first and then he would teach me how to do it and luckily my brother is a really has he has like some gifted ability in learning this sport really quick so he was able to like get the skills really quick and he delivered like what he learned from the teacher to me and we were able to enjoy this kid trip very happily so like he took me to AI real beginner courses and he told he told me that it is not something that you have to be afraid of and it is okay that he has my back for it and like it was like U I think basically the first time that I I have ever felt my brother so like as a reliable person because because he was a child himself by back then so he was like always like play playing tricks on me and he was always like more interested in going out with his friends so he I thought that as a child he was not doing much of his responsibility as.",
        "word_count": 277,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["has my back", "gifted ability", "reliable person", "playing tricks"],
            "grammar_structures_used": ["complex_sentences", "past_tense"]
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
            "complexity_level": "high",
            "accuracy_level": "high",
            "flexibility": "sustained",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Occasional hesitations ('Afra R' - afraid).",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "'has my back', 'playing tricks'. Natural.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent idiom use ('has my back'). Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "reaDH_jQkxw_q04", "video_id": "reaDH_jQkxw",
        "part": 2,
        "question": "Ski trip cont?",
        "transcript": "He as an older brother but then I felt really thankful that that he dedicated his time for me to teach me the skills how to how to ski in a fun way so this is like one of the most one of my favorite childhood memories of like being drwn in a like a ski slope in another country like being rescued by my brother like he told me how to enjoy skiing and without him like I would have been just been sitting somewhere like not being able to ski and that Sky trip would have been a like one of the worst could have turned out to be the very a very bad childood memory but thanks to my brother I could a I was able to enjoy the trip so since then skiing has been one of my hobes that I like to do in the winter time and until now I go skiing with my brother very often and we always talk about the time that how he like was a good brother to me and he always like br about it so it is I think it is a fun memory to me okay great all right great job so.",
        "word_count": 210,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["dedicated his time", "childhood memories", "rescued"],
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
            "complexity_level": "high",
            "accuracy_level": "high",
            "flexibility": "sustained",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Native flow.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "Natural.",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Natural. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "reaDH_jQkxw_q05", "video_id": "reaDH_jQkxw",
        "part": 3,
        "question": "Education roles?",
        "transcript": "Strangers If the child has not learned how to socialize with others in advance so like before school I think parents should like at least try to give as much opportunities for their children to to help to get along with their peers okay great and what is the difference between the roles of teachers and parents in education I would say the main difference is about like teaching the educational materials like for example like teachers I mostly think about learning like some really academic stuff like mathematics science or English that the educational materials that are really academic but then parents are more has the responsib ability of teaching their kids in some some education that can be done in house for example teach them some social rules or like moral lessons so I think that would be the whether it is academic or not whether the focus is on the academic or not I think that is the main difference okay very good and how do adults learn a new skill yeah personally I think it is it is quite a challenge for adults to learn a new skill but then if they wanted to like it would of course depend on what skill is it is it they want to learn but they can enroll a class easily nowadays there are all s sorts of classes that you can enroll to learn a new skill like for example like if you are an elderly who is not familiar with the recent Technologies for example like using the computer or phones there is like a class prepared for them and even the foreign languages like it is easy to have access to education if.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["socialize with others", "get along with their peers", "educational materials", "moral lessons"],
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
            "reason": "'parents are more has the responsibility' (have). 'enroll a class' (enroll in)."
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
                "why_not_9": "Agreement error ('parents has').",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "Precise terms ('peers', 'moral lessons').",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise. Band 9.",
        "grammar_reason": "Minor error. Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "reaDH_jQkxw_q06", "video_id": "reaDH_jQkxw",
        "part": 3,
        "question": "Internet learning?",
        "transcript": "A person wanted to really look for them okay great and is the internet good for learning new skills I I would absolutely say Yes for especially I think YouTube is a great example how it can be a great platform for Education like if you type in just like one simple keyword of like how to do like something there is like you can find hundreds of YouTube YouTubers who are ready to help for you like it would include include the most basic level to the advanced level and and yeah so I think internet can be a really great way for a person to start out a new thing okay very good so that is everything for the test today.",
        "word_count": 126,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["platform for education", "basic level", "advanced level"],
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
        "grammar_reason": "Good. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "aaRQJmv4-gc_q02",
        "video_id": "aaRQJmv4-gc",
        "part": 1,
        "question": "Reading?",
        "transcript": "Romance Romance Jour I found all of these jours quite entertaining and also quite interesting for me to enhance my imagination okay and do you prefer to read a newspaper or a magazine online or to buy a copy I would like to read it online because it more convenience and access accessible accessibility and also is more environmental friendly when compared to the offline version",
        "word_count": 68,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["enhance my imagination", "environmental friendly"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["word_form_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'Jour' (genre?). 'it more convenience' (it is more convenient). 'environmental friendly' (environmentally)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
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
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex attempts."
            },
            "vocabulary": {
                "why_not_7": "Errors ('Jour', 'environmental').",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors present. Band 6.",
        "grammar_reason": "Errors present. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "aaRQJmv4-gc_q03",
        "video_id": "aaRQJmv4-gc",
        "part": 2,
        "question": "Tokyo?",
        "transcript": "That also the culture and the pop culture in Japan in Tokyo makes me want to like be a part of them and like you know to to get know more about them and in conclusion I think Tokyo is a dream destination for you know all the Japan fan culture especially for me and it is a city where I can I think that I can explore both the past and the future in one extra in one journey and making it a top priority on my bual list in the future all right thank you you still have 10 seconds left would you like to say anything more I think it is the end of my speaking okay thank you now we are.",
        "word_count": 128,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form", "structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["dream destination", "pop culture", "top priority"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'bual list' (bucket list). 'get know more' (get to know)."
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
                "why_not_7": "Minor errors.",
                "why_not_5": "Good flow."
            },
            "vocabulary": {
                "why_not_7": "Pronunciation affects clarity ('bual').",
                "why_not_5": "Good range."
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
        "id": 0, "sample_id": "aaRQJmv4-gc_q04",
        "video_id": "aaRQJmv4-gc",
        "part": 3,
        "question": "Cities/Tours?",
        "transcript": "Location and they are they are going to like you know big city they going to attract a lot of visitors so like the demand is high so I think it is yeah and so do you think it is better to visit cities alone or in in a group with friends I think it depends on which like which where is that because when we visiting a string or completely string ation we need like I think we need someone to accompany us to know do not get lost around you know like the places the place but when I visit some kind of familiar place to me I rather go alone to explore some like to have like my own time so so would you recommend having a tour guide on when you visit New cities definitely yes because they would have more like you know deeply knowledge than me that I do not have to wander around and like maybe I will get lost in the strength place okay thank you that is the end of your speaking test today",
        "word_count": 185,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form", "structure"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["accompany us", "wander around", "attract visitors"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["word_form_error"],
            "vocabulary": ["meaning_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'deeply knowledge' (deep). 'string ation' (strange location?). 'strength place' (strange place?)."
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
                "why_not_7": "Frequent errors.",
                "why_not_5": "Complex structures."
            },
            "vocabulary": {
                "why_not_7": "Meaning errors.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Errors affect meaning. Band 6.",
        "grammar_reason": "Frequent errors. Band 6.",
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
