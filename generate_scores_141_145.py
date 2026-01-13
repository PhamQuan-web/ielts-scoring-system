import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 14201,
        "sample_id": "oF8TkzCKUHM_q14",
        "video_id": "oF8TkzCKUHM",
        "part": 3,
        "question": "Tell me Nam, do you think people rely too much on social media?",
        "transcript": "Yes, in my opinion, teenagers depend heavily on social media. Firstly, it is about their school. They have to update their, the news on their school page and they can, have, shown some clues to, to, to improve their self. but, however, elder people do not depend a lot on social media. They want to connect and face to face with another people. They like to do some garden, playing sports or playing chess. They do not like to surf the internet all the time.",
        "word_count": 91,
        "analysis_metadata": {
            "grammar_error_patterns": ["collocation_error", "verb_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["depend heavily", "face to face", "surf the internet"],
            "grammar_structures_used": ["complex_sentence_contrast", "gerund_list"]
        },
        "micro_flaws": {
            "grammar": ["improve_their_self_error", "connect_and_face_to_face_error"],
            "vocabulary": ["do_some_garden_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "good",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'Improve their self' (themselves). 'Face to face with another people' (face to face with other people / meet others face to face). 'Do some garden' (gardening).",
                "why_not_5": "Clear structure and contrast."
            },
            "vocabulary": {
                "why_not_7": "'Depend heavily' is good. 'Another people' is a common error (other people).",
                "why_not_5": "Adequate range."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Depend heavily'. 'Do some garden'. Justification: Band 6.",
        "grammar_reason": "Observation: Reflexive pronoun error. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 14301,
        "sample_id": "RZfjHEPcCXY_q02",
        "video_id": "RZfjHEPcCXY",
        "part": 1,
        "question": "What was your favorite subject at school?",
        "transcript": "my favorite subject was history. I really enjoy learning new things. And about our past and different civilization of their stories.",
        "word_count": 20,
        "analysis_metadata": {
            "grammar_error_patterns": ["sentence_fragment"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["favorite subject", "civilization"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["fragmented_sentence"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "simple",
            "accuracy_level": "moderate",
            "flexibility": "low",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "low",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'Different civilization of their stories' is grammatically unclear/fragmented.",
                "why_not_5": "Basic sentences correct."
            },
            "vocabulary": {
                "why_not_7": "Good word 'civilization' but context is weak.",
                "why_not_5": "Correct."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Mix of simple and complex.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Civilization'. Justification: Band 6.",
        "grammar_reason": "Observation: Fragmented thought. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 14302,
        "sample_id": "RZfjHEPcCXY_q03",
        "video_id": "RZfjHEPcCXY",
        "part": 1,
        "question": "Why history was your favorite subject?",
        "transcript": "Because it was interesting and I can learn new information about our culture and identity. And that is why this is my favorite subject.",
        "word_count": 23,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["culture and identity"],
            "grammar_structures_used": ["reason_clause"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
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
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Simple.",
                "why_not_6": "Error free."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Good collocation 'culture and identity'."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Culture and identity'. Justification: Band 7.",
        "grammar_reason": "Observation: Error free. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 14303,
        "sample_id": "RZfjHEPcCXY_q04",
        "video_id": "RZfjHEPcCXY",
        "part": 1,
        "question": "Is it important to study that subject?",
        "transcript": "Yes, definitely. studying stories helps us to understand our culture and identity and it also teaches us our critical thinking skills and source.",
        "word_count": 22,
        "analysis_metadata": {
            "grammar_error_patterns": ["word_choice"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["critical thinking skills", "culture and identity"],
            "grammar_structures_used": ["gerund_subject"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["stories_vs_history"]
        },
        "vocab_control": {
            "appropriateness": "mostly_accurate",
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
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'Studying stories' (history?). 'And source' is dangling.",
                "why_not_6": "Correct gerund."
            },
            "vocabulary": {
                "why_not_8": "'Critical thinking skills' is excellent.",
                "why_not_6": "Precise."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Critical thinking skills'. Justification: Band 7.",
        "grammar_reason": "Observation: Good gerund use. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 14304,
        "sample_id": "RZfjHEPcCXY_q05",
        "video_id": "RZfjHEPcCXY",
        "part": 1,
        "question": "Do you still have an interest in that subject now?",
        "transcript": "Yes, of course, in my free time I read stories books, history books, and watch documentaries, and, it is a subject, there is always something new to learn.",
        "word_count": 27,
        "analysis_metadata": {
            "grammar_error_patterns": ["run_on"],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["watch documentaries", "history books"],
            "grammar_structures_used": ["list", "compound_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": ["stories_books"]
        },
        "vocab_control": {
            "appropriateness": "accurate",
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
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "'Stories books' (story books/history books).",
                "why_not_6": "Error free."
            },
            "vocabulary": {
                "why_not_8": "Standard.",
                "why_not_6": "Good."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error free.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient."
        },
        "vocab_reason": "Observation: 'Documentaries'. Justification: Band 7.",
        "grammar_reason": "Observation: Correct. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 14305,
        "sample_id": "RZfjHEPcCXY_q06",
        "video_id": "RZfjHEPcCXY",
        "part": 1,
        "question": "Do you live in a flat or a house?",
        "transcript": "I live in an apartment with my family members. There are not so many members in my family, me and my parents.",
        "word_count": 21,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["family members", "apartment"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "simple",
            "accuracy_level": "high",
            "flexibility": "low",
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Simple.",
                "why_not_6": "Error free."
            },
            "vocabulary": {
                "why_not_8": "Basic.",
                "why_not_6": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Error free.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 6.",
        "grammar_reason": "Observation: Correct. Justification: Band 7.",
        "vocabulary": 6,
        "grammar": 7
    },
    {
        "id": 14306,
        "sample_id": "RZfjHEPcCXY_q07",
        "video_id": "RZfjHEPcCXY",
        "part": 1,
        "question": "What do you like about living there?",
        "transcript": "I love to live, I love to live in my apartment because it was so comfortable and I love enjoy my personal space. So I love to live in my own apartment What are the disadvantages of living there the one of the most disadvantage is there is no lift in my apartment and every time I have to go to up fifth floor and it was quite hard for me Would you prefer to live in a flat or a house in the future? There is no problem, there is no problem living in my apartment in future but there must be a leave service because my parents are getting old and they must be, they must, they must be, have leave service in our apartment.",
        "word_count": 122,
        "analysis_metadata": {
            "grammar_error_patterns": ["article_error", "verb_pattern", "word_form"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "adequate",
            "vocab_evidence": ["personal space", "lift", "fifth floor"],
            "grammar_structures_used": ["complex_sentence_reason", "modal_obligation"]
        },
        "micro_flaws": {
            "grammar": ["love_enjoy_error", "most_disadvantage_error"],
            "vocabulary": ["leave_service_error"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "extended",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "'I love enjoy' (love enjoying/love to enjoy). 'The one of the most disadvantage' (one of the biggest disadvantages). 'Go to up fifth floor' (go up to the fifth floor).",
                "why_not_5": "Complex structures present."
            },
            "vocabulary": {
                "why_not_7": "'Leave service' (lift service).",
                "why_not_5": "Meaning clear."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Personal space'. 'Leave' error. Justification: Band 6.",
        "grammar_reason": "Observation: 'Love enjoy'. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 14307,
        "sample_id": "RZfjHEPcCXY_q08",
        "video_id": "RZfjHEPcCXY",
        "part": 3,
        "question": "Why some people enjoy trying new things more than others?",
        "transcript": "People are so adventurous, so they want to learn new things day by day. The world changing constantly and, that is why people want to learn new things and they want to try new experience for their better life.",
        "word_count": 38,
        "analysis_metadata": {
            "grammar_error_patterns": ["missing_verb"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "good",
            "vocab_evidence": ["adventurous", "constantly", "new experience"],
            "grammar_structures_used": ["compound_sentence"]
        },
        "micro_flaws": {
            "grammar": ["missing_is_changing"],
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
                "why_not_7": "'The world changing constantly' (is changing).",
                "why_not_5": "Sentence structures are good."
            },
            "vocabulary": {
                "why_not_8": "'Adventurous' is good.",
                "why_not_6": "Accurate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items."
        },
        "vocab_reason": "Observation: 'Adventurous'. Justification: Band 7.",
        "grammar_reason": "Observation: Missing auxiliary. Justification: Band 6.",
        "vocabulary": 7,
        "grammar": 6
    },
    {
        "id": 14308,
        "sample_id": "RZfjHEPcCXY_q10",
        "video_id": "RZfjHEPcCXY",
        "part": 3,
        "question": "In what other ways do traditions prevent or stop people from trying new things?",
        "transcript": "People can, people, try some new things like they want to explore, many activities and they are so adventurous. They want to take risks. So, I would say that, people should prevent their, their new experience and their, their, their entire life experience with others.",
        "word_count": 43,
        "analysis_metadata": {
            "grammar_error_patterns": ["logic_flow"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["take risks", "explore activities"],
            "grammar_structures_used": ["modal_verb"]
        },
        "micro_flaws": {
            "grammar": ["cohesion_break"],
            "vocabulary": ["wrong_word_prevent"]
        },
        "vocab_control": {
            "appropriateness": "variable",
            "risk_level": "moderate",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "moderate",
            "accuracy_level": "moderate",
            "flexibility": "moderate",
            "error_density": "moderate"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "medium",
            "development_depth": "partial"
        },
        "band_boundary": {
            "grammar": {
                "why_not_7": "Logic is very confusing. 'People should prevent their new experience' seems to mean the opposite of what is intended or is a misuse of 'prevent' (maybe 'present'?).",
                "why_not_5": "Structures are grammatically formed."
            },
            "vocabulary": {
                "why_not_7": "'Prevent' used incorrectly.",
                "why_not_5": "Adequate."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 6,
            "grammar_text": "Errors occur.",
            "vocabulary_band": 6,
            "vocabulary_text": "Adequate."
        },
        "vocab_reason": "Observation: 'Take risks'. 'Prevent' error. Justification: Band 6.",
        "grammar_reason": "Observation: Coherence issue. Justification: Band 6.",
        "vocabulary": 6,
        "grammar": 6
    },
    {
        "id": 14309,
        "sample_id": "RZfjHEPcCXY_q11",
        "video_id": "RZfjHEPcCXY",
        "part": 3,
        "question": "How can globalization affect our culture to adopt new practices and ideas?",
        "transcript": "globalization affects our culture in many ways like I would like to say education. We, now we can use internet for our, education sites and we also use, for our, work. And, on the other hand, if we, if we, if I like to, say that, that is food, and there are so many, there are so, okay. that is the end of your speaking test.",
        "word_count": 67,
        "analysis_metadata": {
            "grammar_error_patterns": ["fragmented_speech"],
            "grammar_error_frequency": "frequent",
            "vocab_collocation_usage": "basic",
            "vocab_evidence": ["education sites"],
            "grammar_structures_used": ["simple_sentence"]
        },
        "micro_flaws": {
            "grammar": ["unfinished_sentences"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "accurate",
            "risk_level": "low",
            "overextension": False
        },
        "anti_overrating": {
            "triggered": False,
            "reason": "N/A"
        },
        "grammar_profile": {
            "complexity_level": "low",
            "accuracy_level": "low",
            "flexibility": "low",
            "error_density": "high"
        },
        "discourse_metrics": {
            "length_appropriateness": "short",
            "redundancy": "high",
            "development_depth": "minimal"
        },
        "band_boundary": {
            "grammar": {
                "why_not_6": "Very fragmented. 'If we, if we, if I like to'. Trails off.",
                "why_not_4": "Some correct simple sentences."
            },
            "vocabulary": {
                "why_not_6": "Limited range shown.",
                "why_not_4": "Relevant."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 5,
            "grammar_text": "Attempts basic sentences.",
            "vocabulary_band": 5,
            "vocabulary_text": "Limited."
        },
        "vocab_reason": "Observation: Basic. Justification: Band 5.",
        "grammar_reason": "Observation: Fragmented. Justification: Band 5.",
        "vocabulary": 5,
        "grammar": 5
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
