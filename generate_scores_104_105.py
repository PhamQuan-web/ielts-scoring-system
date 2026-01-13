import json

output_file = 'jules_scored_output_101-150.jsonl'

samples = [
    {
        "id": 10401,
        "sample_id": "D6zfs3X0uJA_q20",
        "video_id": "D6zfs3X0uJA",
        "part": 3,
        "question": "Is it good for people to be competitive?",
        "transcript": "It really depends. Some people are really competitive and they use that as a motivation to keep them going and just to strive for the best. but, other times it can be quite negative if you are too competitive and then you just beat yourself up for it if you do not win.",
        "word_count": 48,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["motivation", "strive for the best", "beat yourself up"],
            "grammar_structures_used": ["complex_sentence_condition"]
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
            "length_appropriateness": "adequate",
            "redundancy": "low",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Structures are solid but not exceptionally varied in this short sample.",
                "why_not_7": "Error free and uses complex conditionals effortlessly."
            },
            "vocabulary": {
                "why_not_9": "Good idioms ('beat yourself up') but scope is limited.",
                "why_not_7": "Natural use of 'strive for' and 'beat yourself up' indicates Band 8."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free sentences.",
            "vocabulary_band": 8,
            "vocabulary_text": "Skilful use of less common items."
        },
        "vocab_reason": "Observation: 'Beat yourself up'. Impact: Natural idiom. Justification: Band 8.",
        "grammar_reason": "Observation: Conditionals. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 10402,
        "sample_id": "D6zfs3X0uJA_q21",
        "video_id": "D6zfs3X0uJA",
        "part": 3,
        "question": "And do you think all competitions have good outcomes?",
        "transcript": "I do not think all competitions have good outcomes. It just, really depends as well. So, for example, like winning, a race and if you come in fourth or something, It can really like make you feel just really down and beat yourself up for it. So at the end of the day, it also depends on the person and how they take, like how they take not being the winner or just how they react to it as well. But yeah, it really depends on the situation.",
        "word_count": 87,
        "analysis_metadata": {
            "grammar_error_patterns": ["informal_fillers"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "idiomatic",
            "vocab_evidence": ["beat yourself up", "at the end of the day", "outcomes"],
            "grammar_structures_used": ["complex_sentence_condition", "noun_clause"]
        },
        "micro_flaws": {
            "grammar": ["informal_sentence_structure"],
            "vocabulary": ["repetition_of_idiom"]
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
            "error_density": "low"
        },
        "discourse_metrics": {
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "good"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Heavy use of 'like' and informal structure ('It can really like make you feel').",
                "why_not_7": "Structures are generally accurate."
            },
            "vocabulary": {
                "why_not_9": "Repetitive use of 'beat yourself up' (used in previous answer too) and 'depends'.",
                "why_not_7": "'At the end of the day' is a good discourse marker."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Good control but informal/spoken nature affects structure.",
            "vocabulary_band": 7,
            "vocabulary_text": "Less common items used with some repetition."
        },
        "vocab_reason": "Observation: 'Beat yourself up' (repeated). 'Outcomes'. Justification: Band 7 due to repetition.",
        "grammar_reason": "Observation: 'Like' used as filler disrupts structure. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 10501,
        "sample_id": "DpSGqFSufTM_q03",
        "video_id": "DpSGqFSufTM",
        "part": 1,
        "question": "Do you work or do you study?",
        "transcript": "I am a full-time university student at the University of Melbourne studying the Bachelor of Biomedicine.",
        "word_count": 15,
        "analysis_metadata": {
            "grammar_error_patterns": [],
            "grammar_error_frequency": "none",
            "vocab_collocation_usage": "precise",
            "vocab_evidence": ["full-time university student", "Bachelor of Biomedicine"],
            "grammar_structures_used": ["simple_sentence_expanded"]
        },
        "micro_flaws": {
            "grammar": [],
            "vocabulary": []
        },
        "vocab_control": {
            "appropriateness": "highly_accurate",
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
            "error_density": "none"
        },
        "discourse_metrics": {
            "length_appropriateness": "concise",
            "redundancy": "low",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Too short to judge full range.",
                "why_not_7": "Error free participial phrase 'studying...'."
            },
            "vocabulary": {
                "why_not_9": "Standard academic intro.",
                "why_not_7": "Precise proper nouns."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Error free.",
            "vocabulary_band": 8,
            "vocabulary_text": "Precise."
        },
        "vocab_reason": "Observation: 'Bachelor of Biomedicine'. Impact: Precise. Justification: Band 8.",
        "grammar_reason": "Observation: Correct. Justification: Band 8.",
        "vocabulary": 8,
        "grammar": 8
    },
    {
        "id": 10502,
        "sample_id": "DpSGqFSufTM_q04",
        "video_id": "DpSGqFSufTM",
        "part": 1,
        "question": "Can you tell me a bit more about that?",
        "transcript": "I do a Bachelor of Biomedicine. it is a pretty much set course, on either research, scientific research or medicine, medicine school in the future. But I still have not decided which path I might take, but at the moment I am majoring in genetics and I have a particular interest in genetics. And especially CRISPR technology, which allow us to edit genes and maybe cure disease like cancer, did like cancer in the future and all sorts of diseases that we are not able to cure at the moment.",
        "word_count": 94,
        "analysis_metadata": {
            "grammar_error_patterns": ["agreement_error", "verb_tense_error"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["scientific research", "CRISPR technology", "edit genes", "cure disease", "majoring in"],
            "grammar_structures_used": ["relative_clause", "complex_sentence_contrast"]
        },
        "micro_flaws": {
            "grammar": ["agreement_error_relative_clause"],
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
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Error: 'technology, which allow us' (should be 'allows'). Small slip.",
                "why_not_7": "Sentence structures are generally very complex and controlled."
            },
            "vocabulary": {
                "why_not_9": "Extremely precise scientific vocab ('CRISPR', 'edit genes').",
                "why_not_7": "Clearly Band 8+."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Majority of sentences error-free. Occasional unsystematic errors.",
            "vocabulary_band": 9,
            "vocabulary_text": "Precise and effective."
        },
        "vocab_reason": "Observation: 'CRISPR', 'edit genes'. Impact: Technical precision. Justification: Band 9.",
        "grammar_reason": "Observation: 'Which allow' error. Justification: Band 8.",
        "vocabulary": 9,
        "grammar": 8
    },
    {
        "id": 10503,
        "sample_id": "DpSGqFSufTM_q09",
        "video_id": "DpSGqFSufTM",
        "part": 1,
        "question": "Is what you wear important to you?",
        "transcript": "I actually spend way more than average time that I would spend on clothing today. Usually I do not really care too much about clothing as long as it is comfortable and as long as I am not in my pajamas I can just go to uni, spend the day there or at the library and then come home and then it will be easy and it will not be. I do not care too much about fashion but as long as it does not make me look bad or it is comfortable I am fine with it.",
        "word_count": 96,
        "analysis_metadata": {
            "grammar_error_patterns": ["awkward_phrasing"],
            "grammar_error_frequency": "occasional",
            "vocab_collocation_usage": "natural",
            "vocab_evidence": ["spend the day", "fine with it", "comfortable"],
            "grammar_structures_used": ["conditional_as_long_as"]
        },
        "micro_flaws": {
            "grammar": ["convoluted_sentence"],
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
            "length_appropriateness": "adequate",
            "redundancy": "medium",
            "development_depth": "adequate"
        },
        "band_boundary": {
            "grammar": {
                "why_not_8": "Sentence gets messy: 'spend way more than average time that I would spend'. 'It will be easy and it will not be' - trails off.",
                "why_not_6": "Uses 'as long as' correctly multiple times."
            },
            "vocabulary": {
                "why_not_8": "Basic vocabulary compared to previous scientific answer.",
                "why_not_6": "Natural."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 7,
            "grammar_text": "Produces good complexity but with some loss of coherence/accuracy.",
            "vocabulary_band": 7,
            "vocabulary_text": "Sufficient range."
        },
        "vocab_reason": "Observation: 'Pajamas', 'fine with it'. Impact: Natural. Justification: Band 7.",
        "grammar_reason": "Observation: Some awkward clauses. Justification: Band 7.",
        "vocabulary": 7,
        "grammar": 7
    },
    {
        "id": 10504,
        "sample_id": "DpSGqFSufTM_q14",
        "video_id": "DpSGqFSufTM",
        "part": 3,
        "question": "Why do people recycle?",
        "transcript": "I think a lot of people do not know too much about this topic and they do it because, well, the government or, like the officials tell them to, and it is sort of almost like a law and that we have to obey. But I think personally, it is, as I have said, it is about our future. Unlike something like coronavirus, like it is a, it is a pandemic that all lot, that will haunt us for three, two, three years and it will pass. But with global warming, it is an issue that is linked very closely to our future entirely. So if we do not do anything now, it means our future generations will not have a viable earth to live on. So I think it is important that we start changing the way we live and doing things sustainably so that we can have, We can provide a future for generations to come.",
        "word_count": 160,
        "analysis_metadata": {
            "grammar_error_patterns": ["hesitation"],
            "grammar_error_frequency": "rare",
            "vocab_collocation_usage": "sophisticated",
            "vocab_evidence": ["haunt us", "linked very closely", "viable earth", "future generations", "sustainably"],
            "grammar_structures_used": ["complex_sentence_contrast", "conditional_future", "purpose_clause"]
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
            "length_appropriateness": "extended",
            "redundancy": "low",
            "development_depth": "deep"
        },
        "band_boundary": {
            "grammar": {
                "why_not_9": "Minor hesitations/fillers ('like', 'sort of almost'). Structures themselves are Band 9 level.",
                "why_not_7": "Far superior control."
            },
            "vocabulary": {
                "why_not_9": "'Haunt us', 'viable earth'. Excellent.",
                "why_not_7": "Sophisticated."
            }
        },
        "ielts_descriptor_alignment": {
            "grammar_band": 8,
            "grammar_text": "Majority of sentences error-free.",
            "vocabulary_band": 9,
            "vocabulary_text": "Precise and flexible."
        },
        "vocab_reason": "Observation: 'Viable earth', 'haunt us'. Impact: Powerful. Justification: Band 9.",
        "grammar_reason": "Observation: Complex reasoning. Justification: Band 8.",
        "vocabulary": 9,
        "grammar": 8
    }
]

with open(output_file, 'a') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {output_file}")
