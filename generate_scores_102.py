import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 10201,
        "sample_id": "O136QOYFAL4_q32",
        "video_id": "O136QOYFAL4",
        "part": 1,
        "question": "Do you work or study?",
        "transcript": "I do work and study I study a Bachelor of Commerce at university majoring in economics and management I really enjoy what I study I enjoy the quantitative side of economics and the qualitative side of management I also do work outside of university life as well I work at a high school as an academic advisor where I provide academic support for students in their final years of high school Wow well you told me what you study Do you enjoy studying this I really do enjoy study It is quite challenging the course since economics is no since economics is so broad it is quite challenging to grasp the concepts but once I do I really find it very rewarding and very fulfilling Great And what do you want to do in the future? In the future, I want to become a high school teacher. I want to use the knowledge that I gained from my undergraduate degree to someday pursue a Masters of Teaching degree, where I can use that knowledge to support young people and give them the chance to, fulfil their potential in finding their careers.",
        "word_count": 182,
        "analysis_metadata": {
            "grammar_error_patterns": ["self_correction"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["Bachelor of Commerce", "majoring in", "quantitative side", "academic advisor", "fulfil their potential", "grasp the concepts"],
            "grammar_structures_used": ["relative_clause", "complex_sentence_reason", "future_intention"]
        },
        "micro_flaws": {
            "grammar": ["hesitation_correction"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "highly_accurate",
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
            "error_density": "rare"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Slight hesitation/correction ('since economics is no since...'). Otherwise near perfect.",
                "why_not_7": "Structures are far more complex and accurate than Band 7."
            },
            "vocabulary": {
                "why_not_9": "Very strong, but perhaps a bit repetitive with 'study'/'work'.",
                "why_not_7": "Idiomatic usage 'fulfil their potential', 'grasp concepts' is Band 8+."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Uses a full range of structures naturally and appropriately.",
            "vocabulary_band": 9,
            "vocabulary_text": "Uses vocabulary with full flexibility and precision in all topics."
        },
        "vocab_reason": "Observation: 'Quantitative side', 'academic advisor', 'fulfil their potential'. Impact: Highly precise. Justification: Band 9 level precision.",
        "grammar_reason": "Observation: Complex sentences handled with ease. Justification: Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 10202,
        "sample_id": "O136QOYFAL4_q33",
        "video_id": "O136QOYFAL4",
        "part": 1,
        "question": "Do you like to plan things?",
        "transcript": "I do like to plan things out. I, sorry, I would say I am, I do like to plan things out. I, I say that I am less of a spontaneous person and more of an organized person. I like keeping things very organized. I like to have my own planner and account and a calendar on my phone to assign time, assign times for a study, times to meet up with people. And meetings and other events outside of work in uni.",
        "word_count": 86,
        "analysis_metadata": {
            "grammar_error_patterns": ["hesitation"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["plan things out", "spontaneous person", "organized person", "meet up with"],
            "grammar_structures_used": ["comparative_contrast"]
        },
        "micro_flaws": {
            "grammar": ["fluency_hesitation"],
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
            "accuracy_level": "high",
            "flexibility": "moderate",
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Several restarts/self-corrections affect the flow slightly, though structures are correct.",
                "why_not_7": "Accuracy is high."
            },
            "vocabulary": {
                "why_not_9": "Good but not fully flexible. 'Planner' and 'calendar' are standard.",
                "why_not_7": "'Spontaneous person' is a good collocation."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Majority of sentences are error-free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common and idiomatic items."
        },
        "vocab_reason": "Observation: 'Spontaneous vs organized'. Impact: Precise meaning. Justification: Band 8.",
        "grammar_reason": "Observation: Good contrast structure. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 10203,
        "sample_id": "O136QOYFAL4_q34",
        "video_id": "O136QOYFAL4",
        "part": 1,
        "question": "And do you like surprises?",
        "transcript": "Sometimes I do. I really, sometimes, it depends on what kind of surprises. it is, if it is, like a surprise test, I would feel a little, it would be a little bit less pleasant for me. But I do enjoy like a surprise birthday party or a surprise gift or a surprise outing. Though the fun, I like surprise, surprise, surprises that that have a joyful connotation to it and less of a negative connotation.",
        "word_count": 76,
        "analysis_metadata": {
            "grammar_error_patterns": ["hesitation_fragment"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["joyful connotation", "negative connotation", "pleasant"],
            "grammar_structures_used": ["conditional", "contrast"]
        },
        "micro_flaws": {
            "grammar": ["False_start"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "highly_accurate",
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
            "flexibility": "high",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Dysfluency ('I really, sometimes...') is noticeable. Structures themselves are complex.",
                "why_not_7": "Control of conditional 'if it is... I would feel' is excellent."
            },
            "vocabulary": {
                "why_not_9": "Repetition of 'surprise' is high, but 'connotation' is very high level.",
                "why_not_7": "Uses 'connotation' correctly in context."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Majority of sentences error-free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Precise and flexible."
        },
        "vocab_reason": "Observation: 'Joyful/Negative connotation'. Impact: Very precise academic vocabulary used naturally. Justification: Band 9 potential, safely 8.5/9. Giving 9 for precision.",
        "grammar_reason": "Observation: Conditional use. Justification: Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 10204,
        "sample_id": "O136QOYFAL4_q36",
        "video_id": "O136QOYFAL4",
        "part": 1,
        "question": "Do you own a bicycle?",
        "transcript": "I do not own a bicycle, but I do enjoy the leisure of cycling. I used, I did own a bike when I was quite young. I do not know, rode it when I was in my early childhood days, but I do not ride, I do not cycle anymore.",
        "word_count": 50,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["leisure of cycling", "early childhood days"],
            "grammar_structures_used": ["past_simple", "contrast"]
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
                "why_not_9": "Simple sentences mostly.",
                "why_not_7": "Error free."
            },
            "vocabulary": {
                "why_not_9": "Good but simple.",
                "why_not_7": "'Leisure of cycling' is nice."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use."
        },
        "vocab_reason": "Observation: 'Leisure of cycling'. Impact: Natural. Justification: Band 8.",
        "grammar_reason": "Observation: Error free. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 10205,
        "sample_id": "O136QOYFAL4_q37",
        "video_id": "O136QOYFAL4",
        "part": 1,
        "question": "Do you think you will have a bicycle in the future?",
        "transcript": "I do. I do hope I will have a bicycle in the future. Given the topic of climate change, I want to make sure that I contribute more to reducing CO2 emissions and hopefully choosing a more eco-friendly mode of transport. And not only is it more eco-friendly, it is also great for exercise and physical activity.",
        "word_count": 57,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["reducing CO2 emissions", "eco-friendly mode of transport", "physical activity"],
            "grammar_structures_used": ["participial_phrase", "inversion_emphasis"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "highly_accurate",
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
            "flexibility": "high",
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "optimal",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Excellent use of inversion 'not only is it...'.",
                "why_not_8": "Superior control."
            },
            "vocabulary": {
                "why_not_9": "Precise, topic-specific vocabulary ('CO2 emissions', 'eco-friendly').",
                "why_not_8": "Better than just skilful."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 9,
            "grammar_text": "Full range of structures naturally.",
            "vocabulary_band": 9,
            "vocabulary_text": "Full flexibility and precision."
        },
        "vocab_reason": "Observation: 'CO2 emissions', 'eco-friendly mode of transport'. Impact: Topic specific. Justification: Band 9.",
        "grammar_reason": "Observation: Inversion 'Not only is it'. Justification: Band 9.",
        "vocabulary": 9,
        "grammar": 9
    },
    {
        "id": 10206,
        "sample_id": "O136QOYFAL4_q24",
        "video_id": "O136QOYFAL4",
        "part": 3,
        "question": "And how does the weather affect outdoor activities?",
        "transcript": "I would say the weather greatly affects the way we look at outdoor activities. For example, on a very sunny day like this, we would feel, people tend to feel more motivated to step outdoors since the weather is a lot nicer, the breeze feels nice, and I would say the other way around. with, rainy, cloudy weather, people might not feel as motivated to step outside since, the weather is quite gloomy. Since they do not feel, there is not much of a positive connotation that is associated with, cloudy or sunny or cloudy or rainy weather when stepping, when doing outdoor activities.",
        "word_count": 106,
        "analysis_metadata": {
            "grammar_error_patterns": ["complex_sentence_structure"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["motivated to step outdoors", "positive connotation", "gloomy"],
            "grammar_structures_used": ["contrast", "complex_reason_clause"]
        },
        "micro_flaws": {
            "grammar": ["run_on_sentence"],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "highly_accurate",
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
            "flexibility": "moderate_high",
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "good",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "End of sentence gets a bit tangled/repetitive.",
                "why_not_7": "Control is very high."
            },
            "vocabulary": {
                "why_not_9": "Excellent word choice 'connotation', 'gloomy'.",
                "why_not_7": "Advanced."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Majority of sentences error-free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Precise and flexible."
        },
        "vocab_reason": "Observation: 'Gloomy', 'connotation'. Impact: Precise. Justification: Band 9.",
        "grammar_reason": "Observation: Complex sentences mostly well controlled. Justification: Band 8.",
        "vocabulary": 9,
        "grammar": 8
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
