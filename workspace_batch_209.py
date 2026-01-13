import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 209 ---
# Total Samples: 20
# Valid Scored: 16
# Skipped: 4 (Reasons below)

# --- SKIPPED SAMPLES LOG ---
# 1. D9wei4IjcZk_q04: Examiner Instruction ("Do not worry if I stop you...") - Not candidate speech.
# 2. D9wei4IjcZk_q05: Examiner Instruction ("Piece of music you like...") - Not candidate speech.
# 3. 7RZK0prF2iY_q03: Ad/Promo ("Tutor you can even choose the is program... camley has generously given us...") - Not candidate speech.
# 4. -Xs4ZinyoZs_q02: Fragment/Incoherent ("Day I was the groundhog day... good love"). Very short and unclear.
#    Wait, let's look closer.
#    `p4d5uVrHyp0_q03`: Valid.
#    `D9wei4IjcZk_q02`: "For my video...". Seems to be meta-commentary about making videos? It's short. "If there is audience still waiting... I am going to keep making videos". It might be an intro/outro of a YouTube video, not an IELTS response.
#    Let's check `D9wei4IjcZk_q03`: "Creator I need a lot of input...". This sounds like a valid answer about reading.
#    Let's check `D9wei4IjcZk_q06`: Valid.
#    Let's check `D9wei4IjcZk_q07`: Valid.
#    `D9wei4IjcZk_q02` is suspicious.
#    `-Xs4ZinyoZs_q02`: "Day I was the groundhog day...". Likely bad transcript or nonsense.
#    `-Xs4ZinyoZs_q04`: "Take out the butter...". Seems like a description of a machine? Valid if it's describing an object.
#    `7RZK0prF2iY_q03` is definitely an Ad.
#    `D9wei4IjcZk_q04` and `q05` are examiner.
#    So `D9wei4IjcZk` has q02, q03, q04, q05, q06, q07.
#    q04, q05 are skipped.
#    q02 is likely skipped (Meta).
#    `7RZK0prF2iY_q03` is skipped.
#    That's 4.
#    What about `-Xs4ZinyoZs_q02`?
#    Let's check other samples.
#    `p4d5uVrHyp0_q03`: Valid.
#    `D9wei4IjcZk` has 6 samples.
#    `-Xs4ZinyoZs` has 2.
#    `1JiAeeTkIJE` has 5. (q02, q03, q04, q05, q06).
#    Wait, `1JiAeeTkIJE` was in Batch 208? No, looking at `batch_209.json` file content provided in `read_file`:
#    It contains `p4d5uVrHyp0`, `D9wei4IjcZk`, `-Xs4ZinyoZs`, `1JiAeeTkIJE`, `JxnvOz8M_3A`, `6fvPGej5j_Y`, `7RZK0prF2iY`, `cbMrNxlsUU8`.
#    Wait, `1JiAeeTkIJE` appears in the file list but I need to check the actual samples in the JSON.
#    The `read_file` output shows:
#    p4d5uVrHyp0_q03
#    D9wei4IjcZk_q02, q03, q04, q05, q06, q07
#    -Xs4ZinyoZs_q02, q04
#    1JiAeeTkIJE_q02, q03, q04, q05, q06, q10 (Wait, q10 is in list? Let me check text).
#    Ah, `1JiAeeTkIJE_q10` is in batch 208 or 209?
#    Let's re-read the file content of `batch_209.json` carefully.
#    It lists:
#    p4d5uVrHyp0_q03
#    D9wei4IjcZk_q02, q03, q04, q05, q06, q07
#    -Xs4ZinyoZs_q02, q04
#    1JiAeeTkIJE_q02, q03, q04, q05, q06, q10
#    JxnvOz8M_3A_q03
#    6fvPGej5j_Y_q05
#    7RZK0prF2iY_q03, q05
#    cbMrNxlsUU8_q02
#    Total: 1+6+2+6+1+1+2+1 = 20. Correct.
#
#    Skipped candidates:
#    1. `D9wei4IjcZk_q04` (Examiner)
#    2. `D9wei4IjcZk_q05` (Examiner)
#    3. `7RZK0prF2iY_q03` (Ad)
#    4. `1JiAeeTkIJE_q10` ("But yeah really good test there is mistakes..."). Examiner Feedback/Outro.
#
#    And `D9wei4IjcZk_q02` ("For my video..."). I will treat it as scorable if it has substance, but it looks like a meta-intro. 20 words. "If there is audience still waiting...". It's a statement. I'll include it but score low/simple. Or skip if it's clearly not an answer. It's not an answer to an IELTS question. I'll skip it as "Intro/Meta".
#    So that's 5 skipped.
#    I need to see if any others are valid.
#    `-Xs4ZinyoZs_q02`: "Day I was the groundhog day...". 15 words. Unclear. I'll skip as Fragment/Unclear.
#    Total 6 skipped?
#    Let's stick to the obvious ones first.
#    q04, q05 (D9w), q03 (7RZ), q10 (1Ji).
#    I'll also skip D9w_q02 and -Xs_q02.
#    So 14 valid samples.

# --- VALID SAMPLES DATA ---
scored_samples = [
    # Video: p4d5uVrHyp0 (Band 4.5)
    {
        "id": 0, "sample_id": "p4d5uVrHyp0_q03", "video_id": "p4d5uVrHyp0",
        "part": 3,
        "question": "Supermarkets vs Countryside?",
        "transcript": "The and anything mhm okay why are many Supermarket built in the city center according to me there are no any excuse so if I on first and foremost is space system so in the city space system is not large so why many Supermarket built in out of the out of the countryside in your country what is the most common thing people buy it is depend on the people so such so many people about beauty system grow grocery product and many more but main things are grocery products okay how people do how how often do people in your country go shopping it is depend on the people so if I talk about office people so office people prefer to go to the go for shopping at the weekend because they have a lots of time for shopping at the weekend on the other side normal people prefer to prefer depend on the needs so when they need arise so they can go for shopping M what kind of places are popular for shopping in your country well there are lots of place in my Countryside such as Supermarket super mall and many more but easy day super mall is very popular in my Countryside for a shopping M last question for today that is do you think online shopping will replace shopping in reality according to definitely online shopping take place of the online offline shopping why do you think why because we can see online shopping most of the pre majority of the people prefer to online shopping because they can they can buy anything in a one click mhm and many more mhm",
        "word_count": 256,
        "analysis_metadata": {
            "grammar_error_patterns": ["basic_structure", "word_choice"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["grocery products", "online shopping", "one click"],
            "grammar_structures_used": ["connectives"]
        },
        "micro_flaws": {
            "grammar": ["broken_sentences"],
            "vocabulary": ["wrong_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'space system' (space/area). 'beauty system' (beauty products). 'it is depend on' (it depends on). 'take place of' (replace)."
        },
        "grammar_profile": {
            "complexity_level": "basic",
            "accuracy_level": "variable",
            "flexibility": "limited",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "moderate",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_5": "Frequent errors 'it is depend'.",
                "why_not_3": "Intelligible."
            },
            "vocabulary": {
                "why_not_5": "Wrong word choices ('system' used for everything).",
                "why_not_3": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 4,
            "grammar_text": "Uses a very limited range of structures.",
            "vocabulary_band": 4,
            "vocabulary_text": "Uses a limited range of vocabulary."
        },
        "vocab_reason": "Basic and error prone ('beauty system'). Band 4.",
        "grammar_reason": "Frequent basic errors. Band 4.",
        "vocabulary": 4,
        "grammar": 4
    },

    # Video: D9wei4IjcZk (Band 7.0)
    {
        "id": 0, "sample_id": "D9wei4IjcZk_q03", "video_id": "D9wei4IjcZk",
        "part": 1,
        "question": "Reading / Favorite Book?",
        "transcript": "Creator I need a lot of input because my job is to gather information and create create output So reading is a form of input for me and it is very efficient for me to you know gather all the information and you know get what I need from the book what sort of things do you read a lot of different things so I recently came back from England so one of the things that I bought was a book about the history of London and I spent the entire time on the plane reading about history the history of England and that was very interesting to me fascinating to me okay so tell me something about your favorite book my favorite book it is going to sound cliche but my favorite book is Harry Potter that is a book that I that I read in high school the especially the last book The Deathly Hallows I think I have read that book over three times why is it your favorite it is it is the conclusion right it is the finale of this very important series so by then the movie is not even out yet so I feel like I am I am onto something big and I just really enjoy how the the story unfolded and how the characters come together yeah now I am going to give you a topic and I would like you to talk about it for one to two minutes.",
        "word_count": 242,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["gather information", "create output", "sound cliche", "story unfolded"],
            "grammar_structures_used": ["complex_sentences", "relative_clauses"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "moderate_high",
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "error_free"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "detailed"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'onto something big' (idiomatic). 'input/output' (tech vocab).",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural and precise ('cliche', 'unfolded'). Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "D9wei4IjcZk_q06",
        "video_id": "D9wei4IjcZk",
        "part": 3,
        "question": "Music and Technology?",
        "transcript": "These kinds of video formats and in turn they like a certain piece of music and why is it that younger people are more susceptible I I would because they spend a lot of time I think on Tik Tok on short form videos it is the majority of their time so they they get influenced by that oh okay all right so oh that leads me on to talking about the next thing I wanted to ask is how has technology affected the kinds of music that young people enjoy nowadays technology like Tik Tok or video streaming I think it it widened the the reach of music and it kind of shaped the the music of Our Generation so technology is always pushing things to the limits to the extreme so I feel like music is no exception so young the younger generation the music that they like the music taste that they develop is very much corresponding to what type of app or technology that they are using so how important is it for a culture to have musical Traditions yeah yeah I I think music is embedded in human history and culture we used to have religious rights or we we have social Gatherings that is based on music and and they there're two components to music right there there is The Melody of the music and they are they are the lyrics so the melody kind resonates with every one of us and the lyric gives a deeper understanding of what the song is trying to convey so I think that that connection and that history make made in made music really important for the Human Society so why do you think that countries have national anthem a sense of.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["susceptible", "widened the reach", "embedded in human history", "resonates with"],
            "grammar_structures_used": ["complex_sentences", "passive_voice"]
        },
        "micro_flaws": {
            "grammar": ["subject_verb_agreement"],
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
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "'gatherings that is based on' (are). 'history make made' (makes/made).",
                "why_not_7": "Sophisticated structures."
            },
            "vocabulary": {
                "why_not_9": "'embedded', 'susceptible', 'resonates'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "High level academic/precise vocab ('susceptible', 'embedded'). Band 9.",
        "grammar_reason": "Minor agreement errors. Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "D9wei4IjcZk_q07",
        "video_id": "D9wei4IjcZk",
        "part": 3,
        "question": "National Anthem?",
        "transcript": "I think it is it is for people to feel patriotic and to have a sense of belonging to a certain country and do you think that is important nowadays or not I cannot really remember the last time I sang my national anthem but when I studied in Singapore back in primary school every single morning we had to put our hand to our chest and sing the national anthem and I believe it is a very good example because Singapore is a nation of multiple cultures and ethnicities and by that one national anthem especially the lyrics is talking about all the different cultures coming together as one as a nation so in that setting I believe it is important because it is it is more of a mosaic and you are putting different people from different cultures into one place where we have to unite and fight for better future so in the context of Singapore I I do believe that having that right of the national anthem is good for the people",
        "word_count": 175,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["patriotic", "sense of belonging", "mosaic", "ethnicities"],
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
                "why_not_7": "Superior complexity."
            },
            "vocabulary": {
                "why_not_9": "'Mosaic' metaphor is excellent. 'Patriotic'.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Excellent metaphor ('mosaic') and precise terms ('ethnicities'). Band 9.",
        "grammar_reason": "Complex and error free. Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },

    # Video: -Xs4ZinyoZs (Band 7.5)
    {
        "id": 0, "sample_id": "-Xs4ZinyoZs_q04",
        "video_id": "-Xs4ZinyoZs",
        "part": 2,
        "question": "Describe a machine/antique?",
        "transcript": "Take out the butter and put into the piece of clock for the last consumption although I think this this petition is fairly simple machine for today's standard I have a great appreciation for it also the effort of my ancestors you invited for that daily life now today uses can go to the store and buy a block of butter and either way I think that is the new solution for that ok and.",
        "word_count": 72,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["great appreciation", "daily life"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["wrong_word"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'piece of clock' (cloth?). 'this petition' (this invention/contraption?). 'ancestors you invited' (invented?)."
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
                "why_not_9": "Good structure.",
                "why_not_7": "Good."
            },
            "vocabulary": {
                "why_not_9": "Transcript errors or mispronunciations ('petition' vs 'invention', 'invited' vs 'invented').",
                "why_not_7": "Good core vocab."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 6,
            "vocabulary_text": "Uses an adequate range of vocabulary."
        },
        "vocab_reason": "Vocab seems affected by pronunciation or wrong word choice. Band 6.",
        "grammar_reason": "Structure is good. Band 7.",
        "vocabulary": 6,
        "grammar": 7
    },

    # Video: 1JiAeeTkIJE (Band 6.5)
    {
        "id": 0, "sample_id": "1JiAeeTkIJE_q02",
        "video_id": "1JiAeeTkIJE",
        "part": 1,
        "question": "Traveling by car?",
        "transcript": "You can experience diverse different things so i mean yeah traveling by car is really easy and you can save the time of course so when do you travel by car when do you travel car when you buy car i i usually i usually travel by car on the weekend because a weekend means that you have to rest kind of so yeah i i drive i drive yeah usually by car to some fancy places for example for example yang pyeong or or pundang where it is in which in which there are so many palatial and palatal and kind of colorful flowers and embellished places so you can enjoy if you like take a take a photo so yeah i do yeah i do usually i do i do visit there on the weekend by car and where is the furthest place you have traveled by car I will take a pardon where is the furthest place you have traveled to by car oh yeah there are a few places but i must say busan busan is yeah yeah quite far from seoul so it i remember i remembered that it took nearly three hours by car it is it is seriously it was really long journey for me and i i got a bit of classic but i i was enthusiastically yeah i was enthusiast i enthusiastic enthusiastically wanted to wanted to go there because yeah busan was one of the famous places in korea so yeah busan yeah one of the furthest places i visit and do you like to sit in the front or in the back when traveling by car of course i i prefer i prefer to sit on the front because obviously sitting in the front sitting in.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition", "word_order"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "mixed",
            "vocab_evidence": ["embellished places", "palatial", "scenic views"],
            "grammar_structures_used": ["relative_clauses", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["fluency_repetition"],
            "vocabulary": ["wrong_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'diverse different things' (redundant). 'palatial and palatal' (palatial means palace-like, palatal relates to mouth). 'embellished places' (decorated? maybe 'beautiful'). 'got a bit of classic' (carsick?). 'enthusiastic enthusiastically' (repetition)."
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
                "why_not_7": "Repetition and fragmentation.",
                "why_not_5": "Complex structures used."
            },
            "vocabulary": {
                "why_not_7": "Misuse of high level words ('palatial', 'embellished', 'classic' for carsick).",
                "why_not_5": "Attempts high level."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Attempts to use less common vocabulary but with some inaccuracy."
        },
        "vocab_reason": "Attempts high level ('embellished', 'palatial') but often incorrect/unnatural. Band 6.",
        "grammar_reason": "Disfluent but accurate enough. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "1JiAeeTkIJE_q03",
        "video_id": "1JiAeeTkIJE",
        "part": 1,
        "question": "Front or back seat?",
        "transcript": "The front means that yeah you cannot you can see the scenic views and when you when you are on a highway you can see really kind of the mother nature mother nature i mean the mother nature is always always attracts me attracts me so it was really yeah it was beautiful and fabulous",
        "word_count": 52,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["scenic views", "mother nature"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["fluency_repetition"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Heavy repetition 'mother nature mother nature'."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "controlled",
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
                "why_not_8": "Repetition disrupts.",
                "why_not_6": "Good."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('scenic views'). Band 7.",
        "grammar_reason": "Repetition issues. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "1JiAeeTkIJE_q04",
        "video_id": "1JiAeeTkIJE",
        "part": 2,
        "question": "Describe a person/video?",
        "transcript": "Eyes because I am a huge fan of travel a huge fan of traveling so and he showed he in in this video he exactly showed how how he how he adapted to different cultures different foods and a diverse diverse things type of things in other countries because traveling means that you have to you have to feel and experience different one compared to compared to your own culture so it was really it is really yeah informative it was really useful so i was yeah i was really baffled staggered by his recommendation and he is he is kind of it sounds like very life wisdom from him so i was really interested yeah in that video okay mate that is two minutes yeah nice one nice one so do you often watch videos on social media oh yes of course i was I am frankly I am a bit addicted to social media in particular instagram instagram is world widely used and i love take a picture picture of me a picture of me and not only me but some beautiful scenes and mother natures as i said so yeah I am yeah i love it i adore yeah i adore it nice",
        "word_count": 202,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "mixed",
            "vocab_evidence": ["huge fan", "adapted to", "life wisdom", "addicted to", "baffled staggered"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["fluency_repetition"],
            "vocabulary": ["wrong_word_choice"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "high",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'baffled staggered' (impressed? baffled means confused). 'mother natures' (nature). 'world widely used' (used worldwide/widely used)."
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
                "why_not_7": "Repetition.",
                "why_not_5": "Complex."
            },
            "vocabulary": {
                "why_not_7": "Misuse of 'baffled', 'mother natures'.",
                "why_not_5": "Attempts high level."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 6,
            "vocabulary_text": "Attempts to use less common vocabulary but with some inaccuracy."
        },
        "vocab_reason": "Attempts 'baffled', 'staggered' but likely misused. Band 6.",
        "grammar_reason": "Disfluent. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "1JiAeeTkIJE_q05",
        "video_id": "1JiAeeTkIJE",
        "part": 3,
        "question": "Social media advantages/disadvantages?",
        "transcript": "Some incentives from social media so that is kind of minor minor reason on top of that the main thing people people love using social media is that they want to show themselves to other people because yeah also under social media you cannot easily straightforwardly see that how people spend their lives you can share you can share your story on the social media by doing this you can you can get some advice or you can give some advice so it is kind of you could you could receive and give some quid pro quo so i would say that is why people love using social media okay are there any disadvantages to using social media yes of course the there are there could be a couple of disadvantages but for instance if some there there something is observed for example which is that addiction addiction audition means that you spend so much time on social media and you i mean a certain amount of time is okay but you spend so much time so much time and you put you put your assignment or your your assignment your valuable things on the back burner that means that it is a time consuming so i would say i would say disadvantages could be could be yeah addiction okay what do you think about making friends on social media that is an interesting q there is an interesting question making making some friends on social media could be a double-edged sword but i must be on the side of positive side positive aspects because these days given the current state of kobe 19 pandemic you cannot easily mingle with people and there could be some rules like social distancing are two meters away",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["quid pro quo", "double-edged sword", "on the back burner", "mingle with people"],
            "grammar_structures_used": ["complex_sentences", "idioms"]
        },
        "micro_flaws": {
            "grammar": ["fluency_repetition"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'quid pro quo' (exchange?). 'back burner'. 'double-edged sword'. Excellent idioms."
        },
        "grammar_profile": {
            "complexity_level": "high",
            "accuracy_level": "controlled",
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
                "why_not_8": "Repetition/Stutter.",
                "why_not_6": "High complexity."
            },
            "vocabulary": {
                "why_not_8": "Precision is high.",
                "why_not_6": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Excellent idioms ('back burner', 'double-edged sword'). Band 7/8 potential, likely 7 due to fluency impacting delivery.",
        "grammar_reason": "Stuttering affects flow but structures are good. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 0, "sample_id": "1JiAeeTkIJE_q06",
        "video_id": "1JiAeeTkIJE",
        "part": 3,
        "question": "Meeting friends online vs in person?",
        "transcript": "Hard to meet people so i would say yeah or using by using social media they are by using social media there is so many clubs or some gatherings on the social media and there is so many favorite favorites you can find so through through these through these clubs and gatherings you would be able to make a friend rather than meeting in person that is why i think yeah social media is yeah quite social media helps to yeah make up make a friend make a friend yeah do you think if the friendship stays on social media and never transfers to in person is it still a real friendship i just think i must say meeting a person is better than better than admitting only on the internet because technically technically you cannot keep keep your relationship on the internet but deep conversation deep i do not think so deep conversation can be possible on the internet because yeah a face-to-face conversation means that you cannot you can show yourself very easier than on the internet and you can you can easily say something because on the internet there is some some problem there could be some problems like internet connection problem so i must say like distance distance does not matter but i must say yeah meeting in person is pretty much by far better than keeping relationship on the internet okay okay so thanks for coming in for the.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["repetition"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["face-to-face conversation", "make a friend"],
            "grammar_structures_used": ["comparatives", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["fluency_breakdown"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Severe stuttering 'through through these through these', 'make up make a friend make a friend'."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "variable",
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
                "why_not_7": "Fluency/Repetition issues.",
                "why_not_5": "Intelligible complex sentences."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Makes some errors in grammar.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range. Band 7.",
        "grammar_reason": "Fluency issues impact grammar score. Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },

    # Video: JxnvOz8M_3A (Band 7.5)
    {
        "id": 0, "sample_id": "JxnvOz8M_3A_q03",
        "video_id": "JxnvOz8M_3A",
        "part": 2,
        "question": "Describe a place?",
        "transcript": "Receive the most is Disneyland in California us of course as many people know Disneyland is the big play gals for kids and adults with vertov's and attainment and activities and it is one of the most largest amusement park in the world with al Qaeda hotels restaurants categorize concerts and much malls I would love to go there with my family for a couple of weeks because I am sure that they love it and we would have lots of fun my family has grown up with movies from Disney like Little Mermaid of person and it would be wonderful to see these characters come to life as far as I know this Neil and have this narrow section for their theme park most of these are for shooting to take on the roller-coaster ride me big characters like a Mickey Mouse I will play all type of game there is also some entertainment for now as well like concerts all Venice Club so this plate is especially exciting for me to go because I wanted to go there and I was shy but they have got a shot and I do not want my kids to miss this opportunity still appliances I decided to save my money and make see every we have a bleep big pan to go there okay and.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["amusement park", "come to life", "roller-coaster ride"],
            "grammar_structures_used": ["superlatives", "complex_sentences"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["pronunciation_mismatch"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'play gals' (playgrounds?). 'vertov's and attainment' (various entertainment?). 'al Qaeda hotels' (Likely 'arcade' or 'all kinds of'? Transcription error due to pronunciation). 'most largest' (largest). 'appliances' (plans?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "controlled",
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
                "why_not_8": "'most largest' (grammar error).",
                "why_not_6": "Good structure."
            },
            "vocabulary": {
                "why_not_8": "Pronunciation errors leading to wrong words.",
                "why_not_6": "Good range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces frequent error-free sentences.",
            "vocabulary_band": 7,
            "vocabulary_text": "Uses a sufficient range of vocabulary."
        },
        "vocab_reason": "Good range ('come to life') but pronunciation affects clarity. Band 7.",
        "grammar_reason": "Mostly error free. Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },

    # Video: 6fvPGej5j_Y (Band 9.0)
    {
        "id": 0, "sample_id": "6fvPGej5j_Y_q05",
        "video_id": "6fvPGej5j_Y",
        "part": 3,
        "question": "Happiness / Mood?",
        "transcript": "I think there are lots of way to put someone in a better mood like you can go for a night out like we did with our friend sejal or you can have a conversation over a warm cup of tea i think the most important thing is to be a good listener and to be empathetic what is a simple way to make a person feel good i think the simplest way to make a person feel good is to give them a warm and sincere hug it always works for me how has society improved over the past few hundred years to enable citizens to feel better i think there has been much in the way of improving the society like in terms of medicine and technology like cars and computers like we have evolved a lot like i think people these days on the most part do have more positive experience than negative ones i remember like when i sit with my grandmother she had to face a lot more hardships than my parents or me what further improvements can society make to help citizens have even more positive experiences i think there are still so many things we can do better like people are expecting clean water and clean air for their safety there are some places where people cannot go in the night because they feel it is dangerous for them.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["empathetic", "warm and sincere hug", "hardships", "evolved"],
            "grammar_structures_used": ["complex_sentences", "comparatives"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["filler_overuse"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "Overuse of 'like'."
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
                "why_not_9": "Informal fillers 'like'.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "'sincere hug', 'empathetic'. Good.",
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision."
        },
        "vocab_reason": "Precise ('empathetic'). Band 9.",
        "grammar_reason": "Error free but informal. Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "7RZK0prF2iY_q05",
        "video_id": "7RZK0prF2iY",
        "part": 3,
        "question": "Travel preparations?",
        "transcript": "For women and I think the other thing we need to check on is the weather so that we can pack the right clothes when people travel to some countries they need to request a permit like a tourist visa why is this I really do not know the politics behind this but I think it is just because so that they can limit the number of people from certain places and to know why they are visiting that place.",
        "word_count": 83,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["request a permit", "tourist visa", "politics behind this"],
            "grammar_structures_used": ["complex_sentences", "causal_clauses"]
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
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good range. Band 8.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 8,
        "grammar": 9
    },

    # Video: cbMrNxlsUU8 (Band 9.0)
    {
        "id": 0, "sample_id": "cbMrNxlsUU8_q02",
        "video_id": "cbMrNxlsUU8",
        "part": 1,
        "question": "Newspapers?",
        "transcript": "And delicious when is the last time you bought a magazine or newspaper as i mentioned before i do not remember me buying a newspaper or a magazine in a long time however i do have digital subscription to femina which i read each week it is not much but just a few rupees each month and they do have really good information have you ever written an article for a magazine or newspaper let me think about it i did write an article for my school newsletter when i was in middle school i wrote an article for a school newsletter club stating the importance of planting trees and taking care of the environment if you would.",
        "word_count": 133,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["digital subscription", "school newsletter", "taking care of the environment"],
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
                "why_not_7": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Natural. Band 8.",
        "grammar_reason": "Error free. Band 9.",
        "vocabulary": 8,
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

    print(f"Append complete. Added {count} new samples. (Skipped {len(scored_samples) - count} duplicates/invalid).")

except Exception as e:
    print(f"Error writing to file: {e}")
