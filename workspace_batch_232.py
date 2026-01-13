import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'

# --- MANUALLY SCORED BATCH 232 ---
# Total Samples: 20
# Valid Samples: 10

scored_samples = [
    {
        "id": 0, "sample_id": "YlWTLyMd-HA_q39", "video_id": "YlWTLyMd-HA",
        "part": 1,
        "question": "Sleepy?",
        "transcript": "Yes, sometimes it happens. For example, today. My sisters and I did not take a nap today, so we are feeling a bit under the weather.",
        "word_count": 25,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["under the weather"],
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
        "vocab_reason": "Idiom usage. Band 6.",
        "grammar_reason": "Accurate. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "mMCYkjRlMO4_q02", "video_id": "mMCYkjRlMO4",
        "part": 1,
        "question": "Headphones?",
        "transcript": "Kind of headphones do you think are popular among young people well never thought about that but i think definitely the like high technology headphones are popular because nowadays we we have a amount of money to buy what we want so yeah all.",
        "word_count": 42,
        "analysis_metadata": {
            "grammar_error_patterns": ["articles", "phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["high technology"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["article_error"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'a amount of money' (an amount / enough money?)."
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
                "why_not_7": "Errors.",
                "why_not_5": "Complex."
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
        "grammar_reason": "Errors but communicative. Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 0, "sample_id": "zrBXg2KdrbU_q02", "video_id": "zrBXg2KdrbU",
        "part": 1,
        "question": "Volunteer important?",
        "transcript": "Important can you repeat the question what do you think volunteer work is important I think it helps you understand some of the workers that do the these jobs regularly for example if if it is a street cleaner it is a very tedious and a very hard job and I think it would help you appreciate them more so I think it is very important to do volunteer work to understand how people in this in this kind of field work and feel.",
        "word_count": 83,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["tedious", "appreciate them more", "street cleaner"],
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
        "vocab_reason": "Good words. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "zrBXg2KdrbU_q03",
        "video_id": "zrBXg2KdrbU",
        "part": 2,
        "question": "Volunteer experience?",
        "transcript": "Wore masks and Overcoat but I do not think that helped a lot we helped the workers there who works there daily on a daily basis who cleans the street and everything I think they had the whole day off where we worked instead of them that felt great I think they needed they deserve a break more than anything as they work under the Heat and they like it is a very tedious job right because there is a lot of dirt there is a lot of garbage and there is a lot of traffic that they always have to face so I think it was a really good thing that my school I and my team my team of volunteers that worked there so I to be honest it was probably one of the best things I had that I was helping someone or a group of people that earns their daily living their daily money or their monthly income through this kind of very hard and tedious job so it felt really nice and I felt great about myself and the one thing I learned that these jobs are very difficult you have to put on a lot of effort and you have to work a lot for long hours to finish what you have to do yet again on a daily basis okay I have some follow-up questions for you right what are some of the challenges or risks that you face in this project the challenges I faced the most was the dust I have a CV I have severe dust allergies and it caused a lot of issues I had to take appeal before and after I like I did the volunteer work and one of the most risky thing was the ongoing traffic we had.",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["tedious job", "severe dust allergies", "ongoing traffic", "daily basis"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error"],
            "vocabulary": ["word_choice_minor"]
        },
        "vocab_control": {
            "appropriateness": "precise",
            "risk_level": "high",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'workers there who works' (work). 'take appeal' (a pill)."
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
                "why_not_9": "Agreement error.",
                "why_not_7": "Superior."
            },
            "vocabulary": {
                "why_not_9": "ASR/Word error (appeal).",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "High level. Band 8.",
        "grammar_reason": "Strong. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "zrBXg2KdrbU_q04",
        "video_id": "zrBXg2KdrbU",
        "part": 2,
        "question": "Traffic stop?",
        "transcript": "To stop the ongoing traffic it was the main road so there was a huge traffic so we had to stop the traffic and then clean and then start traffic again people got impatient people started honking and people started even screaming at us we were probably at plus six or seven during that time and it was very very scary to stop people okay and how do you measure the impact or success of this project I think I would say that the most the most beneficial and successful thing that we did was industry and the amount of garbage that we picked from there and send it away to the gravity Warehouse so I think we could calculate that from there and the impact was that I think we learned a lot about people and how how hurt they have to work I think it gave us a good experience on how our life would be without them so I think that was a very powerful thing that a lot of us learned that day thank you thank you that is the end of part two may have the pencil sure thank you very much thank you card please.",
        "word_count": 182,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["impatient", "honking", "ongoing traffic", "beneficial"],
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
            "reason": "'gravity Warehouse' (Likely Garbage Warehouse?). 'industry' (in the street?). ASR errors."
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
            "development_depth": "extended"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Good.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "ASR garble.",
                "why_not_7": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "The majority of sentences are error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Good description. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "zrBXg2KdrbU_q05",
        "video_id": "zrBXg2KdrbU",
        "part": 3,
        "question": "Volunteer benefits?",
        "transcript": "Volunteer work for individuals in society for the individuals if you are a student then you can earn certificates there and for other people I think you get to meet a lot of people so the social aspect I think is a very good thing that you can like you can hope to achieve from volunteer work so let us say you are working under you are working under an organization with a lot of people from different cultures they might have different Hobbies they might have different way of life they might think of a different way of life right so I think you can learn a lot from them you can socialize you can make new friends if you want to I think that is a very good thing to do and you are helping others right so why not what are some of the challenges or difficulties of volunteer work the challenges and the or difficulties right so I think it is like there can be a like number of challenges right so some of them might be the environment you are working on the actual work if you are working outside and it is daytime the heat can be an issue that does the pollution and also the people that you are working you cannot mix with everyone right right you have you have a type of people that you would mix with so mixing like you know there can be people that you have difficulty like talking to or difficulty communicating so those are the issues that many people can face okay what personalities and qualities are required for being a volunteer I think the most important quality that you can have is that you have to be very open-minded and that you have to be open to communication",
        "word_count": 286,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["social aspect", "open-minded", "different way of life", "socialize"],
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
        "vocab_reason": "High level. Band 8.",
        "grammar_reason": "Error free. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "zrBXg2KdrbU_q06",
        "video_id": "zrBXg2KdrbU",
        "part": 3,
        "question": "Paid staff vs volunteers?",
        "transcript": "Friendly you have to be able to talk you want to talk to people because if you are just there and just you are sitting quietly people would get awkward because no one knows you there right so if you are open-minded if you are extroverted if you are friendly and if you are like you know if you are trying to encourage them as well they will do the same to you right can a volunteer be treated the same as paid staff in my opinion I do not think so because paid stuff you are paying them to do the work volunteers they are doing it themselves and so I think you would want to encourage the volunteers more and you would want to make sure that they are being treated a bit more differently than the patreon I am not saying that the Pacer should not be treated as good I am just saying that they should be different because they are taking time out of their weekdays or weekends to do the to do the volunteer work right so I think that should be treated a bit different and should be treated with a bit more encouragement and a bit for in a cheerful manner right how can people be encouraged to do more volunteer work well again back to the student part if you are a student just give them certificates I think that is the best way to get students to do the volunteer work and for other people I can think of two ways first can be advertisements obviously you advertise for your event you organize more events so that there are a lot of chance for volunteer for volunteering work and the other way can be again to organize more people to organize more events where people can join and if they see the volunteers they.",
        "word_count": 298,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["extroverted", "open-minded", "cheerful manner", "taking time out"],
            "grammar_structures_used": ["complex_sentences", "conditionals"]
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
            "reason": "'patreon' (paid one?). 'Pacer' (paid staff?)."
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
                "why_not_9": "ASR confusion.",
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
        "grammar_reason": "Strong. Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 0, "sample_id": "zrBXg2KdrbU_q07",
        "video_id": "zrBXg2KdrbU",
        "part": 3,
        "question": "Encourage volunteers?",
        "transcript": "Can they can be encouraged to participate as a volunteer next time right for example for me I want to be a volunteer at a marathon so because and I want to be there because I saw other volunteers do that and I saw it was a really fun and a very enjoyable thing to do right so I want to do that I think that is the best way to encourage more people to participate in volunteering work",
        "word_count": 76,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "error_free",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["participate in volunteering", "enjoyable thing"],
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
        "id": 0, "sample_id": "WBMu2HYFt-k_q02",
        "video_id": "WBMu2HYFt-k",
        "part": 1,
        "question": "Hometown?",
        "transcript": "Because you know taiwan's that on used to be how do I say that we used to be by Japanese government and we have the chain station the building is like a Japanese construction",
        "word_count": 33,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "phrasing"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": [],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["phrasing_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'chain station' (train station). 'that on' (Tainan?). 'used to be by' (occupied by/ruled by?)."
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "moderate",
            "development_depth": "basic"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Frequent breakdown.",
                "why_not_4": "Communicates."
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
        "id": 0, "sample_id": "WBMu2HYFt-k_q04",
        "video_id": "WBMu2HYFt-k",
        "part": 3,
        "question": "Reading habits?",
        "transcript": "Part of our interview today I will just ask you some questions and ask you some follow-up questions it is related to reading and other things related to Books Okay so do you think people read more now is no I do not think people spend much time on both this generation because the smartphone now is really really easy to get it and it is not really expensive now the smartphone and people spend much time on social media or on on YouTube some on media now so I think people spend less time on both definitely they spend less time on books but reading more social media right their friends stories and all that stuff right how about yourself do you read before going to bed like reading it is also social media or online article do you read before going to bed actually I spend much time on phone now and when I go on bed I my first time my first thing is not to sleep and is for spending much time on cell phone then I can fall asleep if if I do not use cell phone I will be keep thinking about other things can fall asleep right so do you think that is a good habit watching touching your smartphone before bed just like this all the time actually not I think that is not a good thing because I would force my sleep and but yes that is a bad habit it is okay I mean everyone has some habits that they do not like as well okay now in your opinion how do you think ebooks can affect paper books now do people read from their smartphone or from the computer and you have paper books.",
        "word_count": 290,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice", "phrasing"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["social media"],
            "grammar_structures_used": ["complex_sentences"]
        },
        "micro_flaws": {
            "grammar": ["phrasing_error"],
            "vocabulary": ["word_choice_error"]
        },
        "vocab_control": {
            "appropriateness": "basic",
            "risk_level": "moderate",
            "overextension": True
        },
        "anti_overrating": {
            "triggered": True,
            "reason": "'spend much time on both' (books). 'easy to get it' (get). 'force my sleep' (force myself to sleep?)."
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
                "why_not_6": "Frequent errors.",
                "why_not_4": "Sustained."
            },
            "vocabulary": {
                "why_not_6": "Basic with errors.",
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
