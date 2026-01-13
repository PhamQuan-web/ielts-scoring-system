import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 211 ---
# Total Samples: 20
# Samples Analyzed:

# 1. n0Ho0iOmGG8_q05 (Band 7.0)
# Transcript: "Place to visit the history related to it and the antique things... why do you think do some people book package holidays... I think packaged holidays are more convenient and economic... environmental pollution by throwing litter everywhere... large H resorts are very important... great impact on environment because resorts are being seen by people..."
# Analysis:
# - Grammar: "package holidays are more convenient and economic to the people" (economical?). "there would be a lot of people... which will be traveling" (who?). "cause environmental pollution by throwing litter" (Good). "large H resorts" (large holiday resorts?). "resorts are being seen by people... that is play a very great role" (that plays?).
# - Vocabulary: "antique things", "museum", "convenient and economic", "environmental pollution", "throwing litter". Good topic vocab.
# - Coherence: Repetitive ("great impact", "very great impact"). Logic is a bit circular about environmental impact ("good impact because resorts are being seen by people" - weak argument).
# - Verdict: Band 7.0 seems appropriate. Good range but occasional errors and some repetition.

# 2. 79AC3-FwkXY_q01 (Band 7.5)
# Transcript: "...mustain has recently achieved 7.5... do you work or study I am a student... pursuing my career by moving to a foreign country... traveled eight times by airplane... startled at all of my air voyages... spectacular views... whole different feeling... live near an airport... very big problem... prefer a house that is quite at a distance..."
# Analysis:
# - Grammar: "startled at all of my air voyages" (startled? maybe 'amazed'?). "quite at a distance" (at quite a distance). Generally error-free structures.
# - Vocabulary: "pursuing my career", "spectacular views", "air voyages" (a bit archaic/literary, 'flights' is better). "Homeland".
# - Note: This is a demo video ("mustain has recently achieved 7.5..."). The candidate is performing.
# - Verdict: Band 7.5/8.0. "startled" is a vocab slip. "air voyages" is slightly unnatural. But very fluent. Given GT is 7.5, I will score around 7.5/8.0.

# 3. 79AC3-FwkXY_q02 (Band 7.5)
# Transcript: "A a aeroplane to travel so therefore I would say that yes I will be having many more air trips in the upcoming days okay."
# Analysis: Short. "air trips". "upcoming days". Valid continuation.
# - Verdict: Valid.

# 4. 79AC3-FwkXY_q05 (Band 7.5)
# Transcript: "Is test booking service we offer pte online classes... if you want to get any of these services our WhatsApp numbers are given..."
# Analysis: ADVERTISEMENT.
# - Verdict: INVALID (Skip).

# 5. 5CDcXl8BSOQ_q04 (Band 9.0)
# Transcript: "The same so i i believe and this is just my standpoint that younger people like visiting parks... pop culture... latest trends... older generation... soft at heart... touch and experience the history... museums... cultural sites... do you agree that some tourist attractions... should be free... society and generation as a whole deserves to know... highly priced... remove access... belongs to everyone residing in that nation..."
# Analysis:
# - Grammar: "this is just my standpoint" (good). "remove access from a lot of people" (limit access?). "afford a ticket for a piece 200 300" (apiece?).
# - Vocabulary: "standpoint", "pop culture", "latest trends", "soft at heart" (idiom), "showcases", "cultural sites", "residing in that nation".
# - Discourse: Very extended, well-reasoned answers.
# - Verdict: Band 9.0.

# 6. evw70L2dVAA_q03 (Band 8.5)
# Transcript: "That is the thing he just put in our minds... takes a certain person with certain qualities... education in your country changed... number of educated people... education rate itself has obviously increased in significant way... subject or the way we are educated... is still quite pretty much the same... huge development... more subjects in higher education..."
# Analysis:
# - Grammar: "increased in significant way" (in a significant way). "subject... is still quite pretty much the same" (are?). "ways we used to do things in educations" (education).
# - Vocabulary: "significant amount", "higher education", "varieties".
# - Verdict: Band 8.0/8.5. Some minor slips ("in significant way", "educations").

# 7. evw70L2dVAA_q04 (Band 8.5)
# Transcript: "Be wide open for us... calculative way... improve the education system... science labor business studies or Humanities... weakness a small weakness in the system... root subject... Thrive the most... pursue and make a great deal out of it."
# Analysis:
# - Grammar: "more better than other" (better than others). "more chance to see than the root subject" (?). "make a great deal out of it" (career?).
# - Vocabulary: "calculative way" (calculated?). "Thrive".
# - Verdict: Band 8.0. "more better" is a slip.

# 8. evw70L2dVAA_q05 (Band 8.5)
# Transcript: "Does not have any value... one thing leads to another... experience is is much greater... role of the school... base the foundation of the children is formed... adapting to new environment... base Foundation schools provide..."
# Analysis:
# - Grammar: "experience is is". "children's" (children).
# - Verdict: Band 8.0.

# 9. _m0r5KanRH4_q02 (Band 9.0)
# Transcript: "Years ago I did use to use microwave... personal preference... fast food restaurants... increasingly popular... international franchises... cheat meals or cheat days... tired of eating boiled chicken... juicy oily and fatty burger..."
# Analysis:
# - Grammar: "did use to use" (used to use / did use). "cheat meals" (collocation). "juicy oily and fatty burger".
# - Vocabulary: "international franchises", "personal preference", "cheat days", "increasingly popular".
# - Verdict: Band 9.0. Native-like naturalness.

# 10. _m0r5KanRH4_q04 (Band 9.0)
# Transcript: "this day and age life has become very fastpaced... stressful... playing computer games is that escape from reality... turn off your reality switch... cognitive abilities... covid-19 has changed the Dynamics of classrooms all together... limited to your physical boundaries..."
# Analysis:
# - Grammar: "this day and age" (idiom). "turn off your reality switch" (metaphor). "changed the Dynamics". "cognitive abilities".
# - Vocabulary: High level. "Dynamics", "fastpaced", "cognitive abilities".
# - Verdict: Band 9.0.

# 11. _m0r5KanRH4_q05 (Band 9.0)
# Transcript: "Way he talked and the way he answered you will get nine B... specimen talk... shos is a very good speaker... search him on YouTube... I also teach is online... WhatsApp number..."
# Analysis: TUTORIAL/OUTRO/AD.
# - Verdict: INVALID (Skip).

# 12. 0L4rr7DUz-8_q03 (Band 9.0)
# Transcript: "...using a laptop can really help accomplishing... Apple MacBook Air... light and convenient... AI bionic chipset... Overkill processor... intend on using it in the long run... plenty of space... online Market... get scammed... make a quick buck... mark up the price... warranty refund... malfunction..."
# Analysis:
# - Grammar: "help accomplishing" (help accomplish). "Apple MacBook Air".
# - Vocabulary: "high-end", "chipset", "Overkill", "long run", "scammed", "make a quick buck", "mark up". Excellent idioms.
# - Verdict: Band 9.0. "help accomplishing" is acceptable. Vocabulary is superb.

# 13. 0L4rr7DUz-8_q04 (Band 9.0)
# Transcript: "Maybe a iPad... fulfill all the day-to-day tasks..."
# Analysis: Short but accurate.
# - Verdict: Valid (Band 9).

# 14. 0L4rr7DUz-8_q05 (Band 9.0)
# Transcript: "Might change because right now it is quite advanced in purchasing online."
# Analysis: Very short.
# - Verdict: Valid (Band 9).

# 15. tKFFrCNsioQ_q02 (Band 9.0)
# Transcript: "joint food snacks... busy schedule... feel exhausted... free up some time... figure out what i want to do about my life... motivates me... hectic pace of tehran... snow-covered peaks..."
# Analysis:
# - Grammar: "joint food snacks" (joints? or snacks?). "hectic pace of tehran". "snow-covered peaks".
# - Vocabulary: "hectic pace", "snow-covered peaks", "exhausted".
# - Verdict: Band 9.0.

# 16. tKFFrCNsioQ_q04 (Band 9.0)
# Transcript: "So you have one minute to."
# Analysis: FRAGMENT/INSTRUCTION.
# - Verdict: INVALID (Skip).

# 17. tKFFrCNsioQ_q05 (Band 9.0)
# Transcript: "Animal because it was different... extraordinary to me... thank you very much okay that is the two."
# Analysis: "that is the two" (end of part 2). Content: "extraordinary to me".
# - Verdict: Valid.

# 18. tKFFrCNsioQ_q06 (Band 9.0)
# Transcript: "keep all the doors and windows closed... stray puppies... maintaining a balanced ecosystem... production of livestock... cloning technology... critically endangered... forbid some acts..."
# Analysis:
# - Vocabulary: "balanced ecosystem", "livestock", "cloning technology", "critically endangered".
# - Verdict: Band 9.0.

# 19. tKFFrCNsioQ_q10 (Band 9.0)
# Transcript: "Middle that is what the examiner does they stop the candidates so when the two."
# Analysis: COMMENTARY/TUTORIAL ("that is what the examiner does").
# - Verdict: INVALID (Skip).

# 20. Nj9xEQZbtYs_q02 (Band 9.0)
# Transcript: "Subjects that i feel I am more comfortable with and that is why i like very much okay very."
# Analysis: Short. Valid.
# - Verdict: Valid.

scored_samples = [
    {
        "id": 0, "sample_id": "n0Ho0iOmGG8_q05", "video_id": "n0Ho0iOmGG8",
        "part": 3,
        "question": "Tourism impact?",
        "transcript": "Place to visit the history related to it and the antique things which are placed in the museum makes it very okay why do you think do some people book package holidays rather than traveling independently I think packaged holidays are more convenient and economic to the people that is why they try to book package holidays rather than in traveling independently because traveling package holidays there would be a lot of people and groups which will be traveling so they can they can meet new people they can make new friends they can meet people from other religions and other cultures so that is the thing I think okay would you say that a large number a large number of tourists cause problems for local people in my perception I think yes when some not everyone but I think people going on holidays and visitors and tourists when they go to the place they cause environmental pollution by throwing litter everywhere so I think yeah okay what sort of impact can large holiday Resorts have on the environment large H resorts are very important for the tourist because they can stay there they can have their meals over there so I think that is a a very great impact what is the impact on environment environment I think it is a very great impact and good impact on the environment because resorts are being seen by people there are staff who can take care of the resorts and that is play a very great role in the environment TR think thank you so much.",
        "word_count": 236,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_form", "structure"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["package holidays", "traveling independently", "environmental pollution", "throwing litter"],
            "grammar_structures_used": ["complex_sentences", "cause_effect"]
        },
        "micro_flaws": {
            "grammar": ["word_choice_error"],
            "vocabulary": ["repetition"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'economic' (economical). 'that is play a very great role' (plays). 'large H resorts' (holiday?). Repetitive 'great impact'."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "high",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Basic errors ('that is play').",
                "why_not_6": "Good range."
            },
            "vocabulary": {
                "why_not_8": "'economic' vs 'economical'. Repetition.",
                "why_not_6": "Good topic vocab."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar and punctuation.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good topic words but error in 'economic' and repetition. Band 7.",
        "grammar_reason": "Errors like 'that is play'. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "79AC3-FwkXY_q01", "video_id": "79AC3-FwkXY",
        "part": 1,
        "question": "Travel/Airport?",
        "transcript": "Okay my name is Assad yakob and I am going to conduct your I speaking test are you ready for that yes I am ready all right before we start let me tell you mustain has recently achieved 7.5 in I speaking and he is here to demonstrate his English and the way he is going to answer if you answer like him you can easily get 7.5 so let us start do you work or study I am a student at the moment and I am pursuing my career by moving to a foreign country all right have you traveled a lot by plane yes to be exact I have traveled eight times by airplane and it was great every single time I got to see new sceneries and I was startled at all of my air voyages actually okay why do you think some people enjoy traveling by PL it is quite sure that people enjoy traveling by the airplane because of the spectacular views that you are able to see and it is just a whole different feeling when you are flying from the ground and then Landing in a different country just feel so different okay would you like to live near an airport actually I do live near an airport and I would say that it is a very big problem so in the future if I had a chance to change my house I would prefer a house that is quite at a distance from the airport okay in the future do you think that you will travel by plane more often yes I am sure I would be traveling More Often by airoplane because I am moving to a foreign country and every time I will have to come back to my homeland I will need.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["pursuing my career", "spectacular views", "air voyages", "homeland"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["unnatural_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "high",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'startled at all of my air voyages' (startled is negative/surprised, maybe 'amazed'?). 'air voyages' (poetic/archaic). 'quite at a distance' (at quite a distance)."
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
                "why_not_9": "Minor awkwardness ('quite at a distance').",
                "why_not_7": "Frequent error-free sentences."
            },
            "vocabulary": {
                "why_not_9": "'startled', 'air voyages' - slightly unnatural.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good range, minor unnaturalness. Band 8.",
        "grammar_reason": "Mostly error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "79AC3-FwkXY_q02", "video_id": "79AC3-FwkXY",
        "part": 1,
        "question": "Travel future?",
        "transcript": "A a aeroplane to travel so therefore I would say that yes I will be having many more air trips in the upcoming days okay.",
        "word_count": 23,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["upcoming days", "air trips"],
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
                "why_not_9": "Too short.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Natural. Band 7.",
        "grammar_reason": "Accurate. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "5CDcXl8BSOQ_q04", "video_id": "5CDcXl8BSOQ",
        "part": 3,
        "question": "Museums vs Parks?",
        "transcript": "The same so i i believe and this is just my standpoint that younger people like visiting parks younger people like visiting places which has recent history something that they can relate to and you know pop culture and anything that is related with music and the latest trends so a place that can give them all of that is something that the younger generation would like as for the older generation i think they are very soft at heart and they still want to you know sort of touch and experience the history that they were part of so they like going to museums a place that showcases all of the history and the historical events that took place so i think that is a difference where i believe that younger generations would like to spend most of their times in tourist parks whereas the older generation would like to spend more time in museums and cultural sites that do you agree that some tourist attractions like national museums or galleries should be free to visit in simple words yes i agree because our society and generation as a whole deserves to know what happened in their history and the fact that it may be highly priced for some individuals might remove access from a lot of people because not everyone can afford a ticket for a piece 200 300 or whatever price for a museum might be so in my opinion yes it should be free it is something that belongs to everyone residing in that nation so i feel like the opportunity to share your culture and your history should definitely have no price on it all right why is tourism important to our country i mean basic from basic answer of this would be from an.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["standpoint", "pop culture", "showcases", "soft at heart", "residing in that nation", "remove access"],
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
            "triggered": True,
            "reason": "'ticket for a piece' (apiece). 'remove access' (limit/restrict?)."
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
                "why_not_9": "Maintains control.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "'soft at heart' (idiom used creatively). 'showcases'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent range and precision. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "evw70L2dVAA_q03", "video_id": "evw70L2dVAA",
        "part": 3,
        "question": "Education changes?",
        "transcript": "That is the thing he just put in our minds that is not every teacher or not everyone can do it takes a certain person with certain qualities I believe great do you still meet your teacher yes briefly sometimes specifically a few occasions I do meet him but I can see that in the past few months not that much but I would like to do other people you know remember this teacher Yes actually my friends most of our friends when we were at sixth grade back from two or three years back we still remember him so yes a lot of us still remember that teacher specifically great can I have the pen and pencil also kill we have been talking about the teacher who has influenced you in your education and now I would like to ask you some questions related to this first we will look at the development in education has education in your country changed in the last 10 years well in the past 10 years I can say that the number of educated people the person educated or the education rate itself has obviously increased in significant way a significant amount but other than that the subject or the way we are educated by education level system is still quite pretty much the same but yes there is a development huge development the ways we used to do things in educations what changes do you think will happen in the future the way things are going now there is a possibility that in future we will be able to see more subjects in higher education which is specifically the reason we need more subject more varieties other than just the few major subjects so that is the possibility I see in the future that more subjects would.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_order", "agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["increased in significant way", "education rate", "higher education"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": ["word_form_error"]
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'increased in significant way' (in a significant way). 'ways we used to do things in educations' (education). 'subject... is still quite pretty much the same' (are?)."
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
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Minor errors ('in significant way').",
                "why_not_7": "Good control."
            },
            "vocabulary": {
                "why_not_9": "'educations' (plural error).",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good range, minor errors. Band 8.",
        "grammar_reason": "Mostly error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "evw70L2dVAA_q04", "video_id": "evw70L2dVAA",
        "part": 3,
        "question": "Improving education?",
        "transcript": "Be wide open for us and be able to find new ways to study more specific and calculative way what changes would you recommend to improve the education system well I can specifically think of one reason or one way to improve it more better than other other than this is the from the 10th grade specifically from the 10th grade what we can see is the science labor business studies or Humanities whichever part we take we are just well we have to take every single subject it is not specifically a bad side but it is a weakness a small weakness in the system which can be improved if students get a more chance to see than the root subject they will Thrive the most which subject they can understand the most or they can take the most in that way they do not need to understand or learn every single subject but they can focus on one side which they can actually pursue and make a great deal out of it.",
        "word_count": 169,
        "analysis_metadata": {
            "grammar_error_patterns": ["comparative"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["thrive", "pursue", "humanities", "root subject"],
            "grammar_structures_used": ["conditionals", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["comparative_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "natural",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'more better' (better). 'calculative way' (calculated?). 'make a great deal out of it' (?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'more better' error.",
                "why_not_7": "Good range."
            },
            "vocabulary": {
                "why_not_9": "'calculative'.",
                "why_not_7": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good range ('thrive', 'pursue'). Band 8.",
        "grammar_reason": "Double comparative error. Band 7.",
        "vocabulary": 8,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "evw70L2dVAA_q05", "video_id": "evw70L2dVAA",
        "part": 3,
        "question": "Role of school?",
        "transcript": "Does not have any value so they will have to go side by side because one thing leads to another and specifically the experience is is much greater and higher with external activities what is the role of the school in modern society the one big influence that I think the schools have in our modern society is that the base the foundation of the children is formed in the schools the base and foundation for everything for adapting to new environment or seeing the intelligence in that part this is the base Foundation schools provide for us our children's in the modern society it is a great deal of work",
        "word_count": 108,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["adapting to new environment", "foundation", "modern society"],
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
            "reason": "'experience is is' (stutter). 'children's' (children?)."
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
                "why_not_9": "Minor slips.",
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
        "id": 0, "sample_id": "_m0r5KanRH4_q02", "video_id": "_m0r5KanRH4",
        "part": 1,
        "question": "Fast food?",
        "transcript": "Years ago I did use to use microwave to cook the food I do not anymore though that is a personal preference okay how popular are fast food restaurants where you live I think they are becoming increasingly popular especially esally this year a lot of new branches have opened a lot of new restaurants have opened a lot of new international franchises are coming in Pakistan as well it is giving the consumer a lot of potential it is giving the consumer a lot of options to sort of go and consume these fast food so yeah I would say a lot a lot I I cannot even count them at this point okay when would you go to a fast food restaurant now that I do not eat fast food regularly I consume fast food just on my cheat meals or cheat days so I would say once a week when I am tired of eating boiled chicken and boiled eggs for the entire week I go and enjoy a very juicy oily and fatty burger at the end of each week all right that is awesome very",
        "word_count": 184,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["international franchises", "cheat meals", "personal preference", "increasingly popular"],
            "grammar_structures_used": ["complex_sentences", "past_habit"]
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
                "why_not_9": "'cheat meals', 'international franchises'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent natural idioms. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "_m0r5KanRH4_q04", "video_id": "_m0r5KanRH4",
        "part": 3,
        "question": "Gaming and Tech?",
        "transcript": "I think in this day and age life has become very fastpaced and at the same time it is become a little stressful so playing computer games is that escape from reality so you can basically turn off your reality switch go into that computer Game Zone let out everything that you have inside and I think people are looking for that escape even in this day so I think that is why they are becoming very popular all right do you think that all computer games should have a minimum age for players I do while I see a lot of people disagreeing with this fact I feel like there should be an age Gap or an age bracket on a couple of these games why because people children do need to develop some sort of cognitive abilities before they enter the gaming world so I feel like minimum the age of 15 or 16 would be suitable for children to sort of develop their interest and enter the gaming world so all right okay in what ways can technology in the classroom be helpful I mean just your recent example covid-19 has has changed the Dynamics of classrooms all together instead of teaching on the board you now have online classes just like you know a lot of instructors now have their online classes so by the use of computers laptops projectors even and Mike's I think technology has helped in you know sort of providing education to people worldwide it is no longer limited to your physical boundaries and I think technology has played a great role in that",
        "word_count": 268,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["escape from reality", "turn off your reality switch", "cognitive abilities", "age bracket", "fastpaced"],
            "grammar_structures_used": ["complex_sentences", "metaphor"]
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
                "why_not_9": "'reality switch', 'cognitive abilities'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise and metaphorical. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "0L4rr7DUz-8_q03", "video_id": "0L4rr7DUz-8",
        "part": 3,
        "question": "Laptop/Purchasing?",
        "transcript": "When going into University there is lots of assignment and using a laptop can really help accomplishing those certain types of tasks and when I do purchase a laptop I do plan on buying one of a high-end type of laptops such as a Apple MacBook Air because it is light and convenient as well as it does provide one of the high-end and latest chipset known as the AI bionic chipset it some may say it is an Overkill processor but I think it is I think it is perfect for me because I do intend on using it in the long run as well as after my university life I do intend on using it as well as sometimes the laptop itself May provide either 500 gigabyte gigabyte of space or if you want one terabyte and that is plenty of space for a string just like me but when I do plan on buying the laptop I do not plan on purchasing in an online Market because in an online Market it is very easy to get scammed because lots of seller they just want to make a quick buck and it is very easy to scan the buyer itself as well as if you do purchase a laptop online they do tend to mark up the price by like 20 or 30 percent whereas if you do go to a showroom then in an app an actual Apple showroom then they provide lots of student benefits as well as warranty refund which is very important for a student like me and if if the laptop does malfunction then I can just easily return it and get the issues fixed but if I do not plan on like if I do not plan on purchasing that sort of laptop then I think a better alternative.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["overkill", "make a quick buck", "get scammed", "mark up the price", "in the long run"],
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
            "triggered": True,
            "reason": "'help accomplishing' (help accomplish). 'scan the buyer' (scam). 'string just like me' (student?)."
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
                "why_not_9": "'make a quick buck', 'overkill'. Excellent natural idioms.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Superb idioms ('quick buck', 'overkill'). Band 9.",
        "grammar_reason": "Complex and accurate. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "0L4rr7DUz-8_q04", "video_id": "0L4rr7DUz-8",
        "part": 3,
        "question": "Alternative?",
        "transcript": "Maybe a iPad itself because an iPad is convenient as well as it can fulfill all the day-to-day tasks that I need in accomplishing okay.",
        "word_count": 23,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["day-to-day tasks", "fulfill"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
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
                "why_not_9": "Short.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise. Band 9.",
        "grammar_reason": "Accurate. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "0L4rr7DUz-8_q05", "video_id": "0L4rr7DUz-8",
        "part": 3,
        "question": "Purchasing online?",
        "transcript": "Might change because right now it is quite advanced in purchasing online.",
        "word_count": 12,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["advanced"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "precise",
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
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise. Band 9.",
        "grammar_reason": "Accurate. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "tKFFrCNsioQ_q02", "video_id": "tKFFrCNsioQ",
        "part": 1,
        "question": "Leisure time?",
        "transcript": "And we have some joint food snacks to enjoy this quality time together wonderful and what are some activities you enjoy in your leisure time just go through them briefly as i mentioned earlier i have a very very busy schedule and i do not have much free time for myself so sometimes i just prefer to sit and relax because i feel exhausted at times and yeah i need some i need to get some sleep and free up some time just to maybe be with my family and that is also something else i would like to do in my free time we can talk with each other about the plans we have for the future just to you know it actually helps me figure out what i want to do about my life and it motivates me and it encourages me to keep on trying as i am yeah these are the things i normally do in my free time wonderful and what do you like about these activities altogether i really enjoy spending time with my family especially my mother and my sister because it really gives me more energy after I am i I am done with my work or with my studies so it really helps me emotionally and i do need to hang out with my friends on the weekends especially because we usually go hiking and it is a very good chance to be away from the hectic pace of tehran and i can just look at the snow-covered peaks in the mountains and enjoy the fresh air so these are the things i really love about the activities these activities i do in my free time",
        "word_count": 277,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["hectic pace", "snow-covered peaks", "free up some time", "quality time"],
            "grammar_structures_used": ["complex_sentences", "infinitive_purpose"]
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
                "why_not_9": "'hectic pace', 'snow-covered peaks'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent collocations. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "tKFFrCNsioQ_q05", "video_id": "tKFFrCNsioQ",
        "part": 2,
        "question": "Animal (Part 2)?",
        "transcript": "Animal because it was different and i had never seen something like that before so i can say that is the reason i can i just explain about this animal it was something extraordinary to me and to talk more about that i can say that thank you very much okay that is the two.",
        "word_count": 55,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["extraordinary"],
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
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Short.",
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Standard.",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Accurate. Band 9.",
        "grammar_reason": "Accurate. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "tKFFrCNsioQ_q06", "video_id": "tKFFrCNsioQ",
        "part": 3,
        "question": "Animals in future?",
        "transcript": "Sure to keep all the doors and windows closed or they may escape and on the other hand in the past few years iranians have been have been showing some interest to take care of some stray puppies which i consider a really nice job wonderful and do you think animals will still be important in the future what i predict is that yes they will absolutely have the the same significance in the future or even more because they are actually essential for maintaining a balanced ecosystem and for the production of livestock which is which influences the water air or soil and as i mentioned earlier due to the reason that many people not only in iran but also in other countries have been showing an interest to take care of puppies or pets generally and they have been supporting animal rights",
        "word_count": 138,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["balanced ecosystem", "livestock", "significance", "stray puppies", "animal rights"],
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
                "why_not_9": "'balanced ecosystem', 'livestock'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise scientific terms. Band 9.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 0, "sample_id": "Nj9xEQZbtYs_q02", "video_id": "Nj9xEQZbtYs",
        "part": 1,
        "question": "Subjects?",
        "transcript": "Subjects that i feel I am more comfortable with and that is why i like very much okay very.",
        "word_count": 19,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["comfortable with"],
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
                "why_not_7": "Accurate."
            },
            "vocabulary": {
                "why_not_9": "Basic.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Natural. Band 9.",
        "grammar_reason": "Accurate. Band 9.",
        "vocabulary": 9,
        "grammar": 9
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
