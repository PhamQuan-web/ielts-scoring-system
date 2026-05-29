import json
import os

os.makedirs('output', exist_ok=True)

lesson_10 = {
    "lesson_id": "vocab_core_10",
    "title": "Core Vocabulary: Family & Lifestyle",
    "topic_snapshot": {
        "target_skills": ["Writing", "Speaking"],
        "description": "Vocabulary for discussing modern family structures, upbringing, daily habits, and work-life balance."
    },
    "key_vocabulary_bank": [
        {
            "word": "Upbringing",
            "phonetic": "/ˈʌpbrɪŋɪŋ/",
            "cefr_level": "B2",
            "meaning": "The treatment and instruction received by a child from its parents throughout its childhood.",
            "example": "His strict upbringing made him a very disciplined adult.",
            "image_url": "https://images.unsplash.com/photo-1511895426328-dc8714191300?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A warm photograph of parents teaching their young child how to ride a bicycle in a park."
        },
        {
            "word": "Extended family",
            "phonetic": "/ɪkˌstendɪd ˈfæməli/",
            "cefr_level": "B2",
            "meaning": "A family that extends beyond the nuclear family, including grandparents, aunts, uncles, and other relatives.",
            "example": "In many cultures, living with your extended family is still the norm.",
            "image_url": "https://images.unsplash.com/photo-1511895426328-dc8714191300?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A large, multi-generational family sitting together around a dining table laughing and eating."
        },
        {
            "word": "Sedentary",
            "phonetic": "/ˈsedntri/",
            "cefr_level": "C1",
            "meaning": "Tending to spend much time seated; somewhat inactive.",
            "example": "Modern lifestyles have become increasingly sedentary due to office work and technology.",
            "image_url": None,
            "image_prompt_fallback": "A person sitting on a couch for a long time watching TV with snacks around."
        }
    ],
    "collocation_builder": [
        {
            "collocation": "Nuclear family",
            "meaning": "A couple and their dependent children, regarded as a basic social unit.",
            "example": "The traditional nuclear family structure has changed significantly in recent decades."
        },
        {
            "collocation": "Close-knit community",
            "meaning": "A group of people bound together by strong relationships and common interests.",
            "example": "Growing up in a close-knit community gives children a strong sense of security."
        }
    ],
    "upgrade_section": [
        {
            "weak_phrase": "Raise a child",
            "better_upgrade": "Child-rearing / Bring up",
            "example": "Both parents should share the responsibilities of child-rearing equally."
        }
    ],
    "sentence_frames": [
        "The shift from [Noun Phrase] to [Noun Phrase] has significantly altered social dynamics.",
        "A healthy lifestyle is heavily dependent on [Noun Phrase]."
    ],
    "ielts_usage_examples": {
        "writing_example": "The shift from extended to nuclear families in urban areas has significantly altered child-rearing practices. Parents now often rely on paid childcare rather than the support of a close-knit community.",
        "speaking_example": "I had a very happy upbringing. My parents always encouraged me to pursue my passions, which really helped shape who I am today."
    },
    "common_mistakes": [
        "Confusing 'grow up' (what a child does) with 'bring up' (what a parent does). (e.g., 'My parents grew me up well' -> 'My parents brought me up well')."
    ],
    "quiz": [
        {
            "question": "Which term describes the instruction and treatment a child receives from their parents?",
            "options": {
                "A": "Sedentary",
                "B": "Upbringing",
                "C": "Nuclear",
                "D": "Extended"
            },
            "correct_answer": "B",
            "explanation": "'Upbringing' refers to how a child is raised. 'Nuclear' and 'Extended' describe family types, and 'Sedentary' is a lifestyle."
        }
    ]
}

lesson_11 = {
    "lesson_id": "vocab_core_11",
    "title": "Core Vocabulary: Urbanisation, Housing & Cities",
    "topic_snapshot": {
        "target_skills": ["Writing", "Speaking"],
        "description": "Vocabulary for discussing city life, urban sprawl, housing crises, and infrastructure."
    },
    "key_vocabulary_bank": [
        {
            "word": "Urbanization",
            "phonetic": "/ˌɜːbənaɪˈzeɪʃn/",
            "cefr_level": "B2",
            "meaning": "The process of making an area more urban; the shift of population from rural to urban areas.",
            "example": "Rapid urbanization has put enormous pressure on city infrastructure.",
            "image_url": "https://images.unsplash.com/photo-1449844908441-8829872d2607?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A time-lapse style photo showing a city skyline expanding rapidly."
        },
        {
            "word": "Congestion",
            "phonetic": "/kənˈdʒestʃən/",
            "cefr_level": "C1",
            "meaning": "The state of being crowded and full of traffic.",
            "example": "Traffic congestion in the city center is a major source of air pollution.",
            "image_url": "https://images.unsplash.com/photo-1507677918349-f02781b0a7db?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A massive traffic jam on a multi-lane highway during rush hour."
        },
        {
            "word": "Amenities",
            "phonetic": "/əˈmiːnətiz/",
            "cefr_level": "C1",
            "meaning": "A desirable or useful feature or facility of a building or place.",
            "example": "The new housing development is located near local amenities such as schools and parks.",
            "image_url": None,
            "image_prompt_fallback": "A map or overhead view of a neighborhood highlighting parks, schools, and hospitals."
        }
    ],
    "collocation_builder": [
        {
            "collocation": "Urban sprawl",
            "meaning": "The uncontrolled expansion of urban areas.",
            "example": "Urban sprawl is destroying surrounding agricultural land."
        },
        {
            "collocation": "Affordable housing",
            "meaning": "Housing units that are affordable by that section of society whose income is below the median household income.",
            "example": "There is a severe lack of affordable housing for young professionals in the capital."
        }
    ],
    "upgrade_section": [
        {
            "weak_phrase": "City center",
            "better_upgrade": "Central Business District (CBD) / Downtown",
            "example": "Rents in the Central Business District are astronomically high."
        }
    ],
    "sentence_frames": [
        "The influx of people into cities has exacerbated [Noun Phrase].",
        "To combat [Noun Phrase], urban planners must [Verb Phrase]."
    ],
    "ielts_usage_examples": {
        "writing_example": "The relentless pace of urbanization has undoubtedly brought economic prosperity, but it has also resulted in severe traffic congestion and a drastic shortage of affordable housing.",
        "speaking_example": "I live in the suburbs because the city center is just too noisy and crowded. However, the lack of local amenities nearby can be quite inconvenient."
    },
    "common_mistakes": [
        "Using 'in the countryside' vs 'in the nature' (e.g., 'I live in the nature' -> 'I live in the countryside')."
    ],
    "quiz": [
        {
            "question": "Which phrase describes the uncontrolled outward expansion of a city?",
            "options": {
                "A": "Affordable housing",
                "B": "Urban sprawl",
                "C": "Traffic congestion",
                "D": "Local amenities"
            },
            "correct_answer": "B",
            "explanation": "'Urban sprawl' specifically refers to the uncontrolled spread of urban development into neighboring regions."
        }
    ]
}

lesson_12 = {
    "lesson_id": "vocab_core_12",
    "title": "Core Vocabulary: Media, Advertising & Communication",
    "topic_snapshot": {
        "target_skills": ["Writing", "Speaking"],
        "description": "Vocabulary for discussing mass media, the influence of advertising, fake news, and digital communication."
    },
    "key_vocabulary_bank": [
        {
            "word": "Censorship",
            "phonetic": "/ˈsensəʃɪp/",
            "cefr_level": "C1",
            "meaning": "The suppression or prohibition of any parts of books, films, news, etc. that are considered obscene, politically unacceptable, or a threat to security.",
            "example": "There is an ongoing debate about the extent of internet censorship by the government.",
            "image_url": "https://images.unsplash.com/photo-1504711434969-e33886168f5c?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A newspaper page with thick black marker lines crossing out entire paragraphs of text."
        },
        {
            "word": "Manipulate",
            "phonetic": "/məˈnɪpjʊleɪt/",
            "cefr_level": "C1",
            "meaning": "Control or influence (a person or situation) cleverly, unfairly, or unscrupulously.",
            "example": "Advertising companies use psychological tactics to manipulate consumer behavior.",
            "image_url": None,
            "image_prompt_fallback": "A conceptual image of a hand moving a person like a puppet on strings."
        },
        {
            "word": "Sensationalism",
            "phonetic": "/senˈseɪʃənəlɪzəm/",
            "cefr_level": "C1",
            "meaning": "The use of exciting or shocking stories or language at the expense of accuracy, in order to provoke public interest or excitement.",
            "example": "Many tabloids rely on sensationalism rather than factual reporting to boost sales.",
            "image_url": None,
            "image_prompt_fallback": "A bright yellow newspaper front page with a massive, exaggerated headline."
        }
    ],
    "collocation_builder": [
        {
            "collocation": "Mass media",
            "meaning": "Any of the means of communication, as television or newspapers, that reach very large numbers of people.",
            "example": "The mass media plays a crucial role in shaping public opinion."
        },
        {
            "collocation": "Target audience",
            "meaning": "A particular group at which a film, book, advertising campaign, etc., is aimed.",
            "example": "The advertising campaign was specifically designed to appeal to its target audience of teenagers."
        }
    ],
    "upgrade_section": [
        {
            "weak_phrase": "Ads everywhere",
            "better_upgrade": "Ubiquitous advertising / Bombarded with advertisements",
            "example": "In today's digital age, consumers are constantly bombarded with ubiquitous advertising."
        }
    ],
    "sentence_frames": [
        "The primary purpose of [Noun Phrase] is to [Verb Phrase].",
        "It is highly concerning that [Noun Phrase] can be easily manipulated by [Noun Phrase]."
    ],
    "ielts_usage_examples": {
        "writing_example": "While advertising is essential for business growth, the ubiquitous nature of modern marketing often manipulates vulnerable consumers into purchasing goods they do not need.",
        "speaking_example": "I try to avoid reading tabloids because I dislike the sensationalism. I prefer getting my news from independent journalists who focus on facts rather than just trying to get clicks."
    },
    "common_mistakes": [
        "Using 'advices' or 'news' as countable nouns. (e.g., 'I have a good news' -> 'I have some good news')."
    ],
    "quiz": [
        {
            "question": "Which term refers to suppressing information that is considered unacceptable or threatening?",
            "options": {
                "A": "Manipulation",
                "B": "Censorship",
                "C": "Sensationalism",
                "D": "Target audience"
            },
            "correct_answer": "B",
            "explanation": "'Censorship' is the act of banning or deleting information. 'Sensationalism' is exaggerating it, and 'manipulation' is unfairly controlling someone."
        }
    ]
}

lesson_13 = {
    "lesson_id": "vocab_core_13",
    "title": "Core Vocabulary: Opinion Phrases for Writing and Speaking",
    "topic_snapshot": {
        "target_skills": ["Writing", "Speaking"],
        "description": "Essential functional language to clearly state, defend, and nuance your opinions in IELTS Tasks."
    },
    "key_vocabulary_bank": [
        {
            "word": "Advocate",
            "phonetic": "/ˈædvəkət/",
            "cefr_level": "C1",
            "meaning": "A person who publicly supports or recommends a particular cause or policy (noun); to publicly support (verb).",
            "example": "I strongly advocate for stricter environmental regulations.",
            "image_url": "https://images.unsplash.com/photo-1541872516-6c9053805b5f?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A confident person standing at a podium giving a passionate speech."
        },
        {
            "word": "Acknowledge",
            "phonetic": "/əkˈnɒlɪdʒ/",
            "cefr_level": "B2",
            "meaning": "Accept or admit the existence or truth of.",
            "example": "While I acknowledge the benefits of technology, we must also consider its drawbacks.",
            "image_url": None,
            "image_prompt_fallback": "Two people nodding in agreement during a serious discussion."
        }
    ],
    "collocation_builder": [
        {
            "collocation": "Firmly believe",
            "meaning": "To have a very strong conviction.",
            "example": "I firmly believe that education is the key to solving poverty."
        },
        {
            "collocation": "Widely recognized",
            "meaning": "Accepted by many people.",
            "example": "It is widely recognized that smoking causes severe health issues."
        }
    ],
    "upgrade_section": [
        {
            "weak_phrase": "I think",
            "better_upgrade": "I am of the opinion that / From my perspective",
            "example": "From my perspective, the disadvantages far outweigh the advantages."
        },
        {
            "weak_phrase": "Many people say",
            "better_upgrade": "It is often argued that / It is a common belief that",
            "example": "It is often argued that university education should be free for everyone."
        }
    ],
    "sentence_frames": [
        "While it is valid to argue that [Clause], I am of the opinion that [Clause].",
        "It is fundamentally important to recognize that [Clause]."
    ],
    "ielts_usage_examples": {
        "writing_example": "It is widely recognized that automation will displace many manual workers. While I acknowledge this challenge, I firmly believe that technology will ultimately create new, highly-skilled jobs.",
        "speaking_example": "From my perspective, working from home is fantastic. I mean, I acknowledge that you miss out on office banter, but the flexibility is just unbeatable."
    },
    "common_mistakes": [
        "Writing 'According to me' instead of 'In my opinion'. (Only use 'According to' for third-party sources)."
    ],
    "quiz": [
        {
            "question": "Which phrase is the most formal academic upgrade for 'Many people say'?",
            "options": {
                "A": "Lots of guys think",
                "B": "It is often argued that",
                "C": "They are saying",
                "D": "In my opinion"
            },
            "correct_answer": "B",
            "explanation": "'It is often argued that' is a highly formal, objective way to introduce a common opinion in an essay."
        }
    ]
}

lesson_14 = {
    "lesson_id": "vocab_core_14",
    "title": "Core Vocabulary: Cause and Effect Language",
    "topic_snapshot": {
        "target_skills": ["Writing", "Speaking"],
        "description": "Functional vocabulary to accurately describe the reasons behind issues and their subsequent impacts."
    },
    "key_vocabulary_bank": [
        {
            "word": "Catalyst",
            "phonetic": "/ˈkætəlɪst/",
            "cefr_level": "C1",
            "meaning": "A person or thing that precipitates an event.",
            "example": "The invention of the microchip acted as a catalyst for the digital revolution.",
            "image_url": None,
            "image_prompt_fallback": "A conceptual image of a small domino knocking over increasingly larger dominoes."
        },
        {
            "word": "Stem from",
            "phonetic": "/stem frɒm/",
            "cefr_level": "C1",
            "meaning": "Originate in or be caused by.",
            "example": "Much of the city's crime stems from high unemployment rates.",
            "image_url": None,
            "image_prompt_fallback": "A plant growing out of a cracked piece of concrete, symbolizing origin."
        }
    ],
    "collocation_builder": [
        {
            "collocation": "Root cause",
            "meaning": "The fundamental reason for the occurrence of a problem.",
            "example": "We must address the root cause of the issue rather than just treating the symptoms."
        },
        {
            "collocation": "Knock-on effect",
            "meaning": "A secondary, indirect, or cumulative effect.",
            "example": "The strike by transport workers had a knock-on effect on local businesses."
        }
    ],
    "upgrade_section": [
        {
            "weak_phrase": "Because of",
            "better_upgrade": "As a direct result of / Due primarily to",
            "example": "The species went extinct as a direct result of habitat destruction."
        },
        {
            "weak_phrase": "Leads to",
            "better_upgrade": "Results in / Gives rise to",
            "example": "Poor diet gives rise to numerous health complications."
        }
    ],
    "sentence_frames": [
        "The primary catalyst for [Noun Phrase] is [Noun Phrase].",
        "Consequently, this phenomenon has resulted in [Noun Phrase]."
    ],
    "ielts_usage_examples": {
        "writing_example": "The severe flooding in the region stems directly from rampant deforestation. As a direct result of losing tree cover, the soil can no longer absorb heavy rainfall, which gives rise to catastrophic landslides.",
        "speaking_example": "I think a lot of stress nowadays stems from social media. People constantly compare themselves to others online, and that has a massive knock-on effect on their self-esteem."
    },
    "common_mistakes": [
        "Confusing 'affect' (verb) and 'effect' (noun). (e.g., 'It had a bad affect' -> 'It had a bad effect')."
    ],
    "quiz": [
        {
            "question": "Which phrasal verb means 'to be caused by'?",
            "options": {
                "A": "Give rise to",
                "B": "Stem from",
                "C": "Lead to",
                "D": "Result in"
            },
            "correct_answer": "B",
            "explanation": "'Stem from' points backward to the cause (e.g., The problem stems from poverty). The others point forward to the effect."
        }
    ]
}

lesson_15 = {
    "lesson_id": "vocab_core_15",
    "title": "Core Vocabulary: Advantages and Disadvantages Language",
    "topic_snapshot": {
        "target_skills": ["Writing", "Speaking"],
        "description": "Functional vocabulary for evaluating the pros and cons of a situation, essential for balanced essays."
    },
    "key_vocabulary_bank": [
        {
            "word": "Beneficial",
            "phonetic": "/ˌbenɪˈfɪʃl/",
            "cefr_level": "B2",
            "meaning": "Favorable or advantageous; resulting in good.",
            "example": "Regular exercise is highly beneficial to both physical and mental health.",
            "image_url": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A person smiling and stretching outdoors in the morning sun."
        },
        {
            "word": "Drawback",
            "phonetic": "/ˈdrɔːbæk/",
            "cefr_level": "B2",
            "meaning": "A feature that renders something less acceptable; a disadvantage or problem.",
            "example": "The main drawback of living in the city center is the noise pollution.",
            "image_url": None,
            "image_prompt_fallback": "A scale with gold on one side heavily outweighing a pile of rocks on the other."
        }
    ],
    "collocation_builder": [
        {
            "collocation": "Double-edged sword",
            "meaning": "Something that has or can have both favorable and unfavorable consequences.",
            "example": "The internet is a double-edged sword; it provides information but also spreads fake news."
        },
        {
            "collocation": "Outweigh the disadvantages",
            "meaning": "To be more significant or important than the negative aspects.",
            "example": "In my view, the economic benefits of tourism far outweigh the environmental disadvantages."
        }
    ],
    "upgrade_section": [
        {
            "weak_phrase": "Good points and bad points",
            "better_upgrade": "Merits and demerits / Pros and cons",
            "example": "We must carefully weigh the merits and demerits of nuclear power."
        },
        {
            "weak_phrase": "Is a good thing",
            "better_upgrade": "Is highly advantageous",
            "example": "Learning a second language is highly advantageous in today's globalized job market."
        }
    ],
    "sentence_frames": [
        "While there are evident drawbacks to [Noun Phrase], I believe the benefits are far more significant.",
        "One of the primary merits of [Gerund Phrase] is that [Clause]."
    ],
    "ielts_usage_examples": {
        "writing_example": "While globalization is often viewed as a double-edged sword, I firmly believe that its merits far outweigh its demerits. Although it can lead to cultural homogenization, it is highly advantageous for economic growth and international cooperation.",
        "speaking_example": "Well, studying abroad is definitely a double-edged sword. It's incredibly beneficial for your independence and language skills, but the main drawback is homesickness."
    },
    "common_mistakes": [
        "Saying 'The advantages are more than the disadvantages' instead of 'The advantages outweigh the disadvantages'."
    ],
    "quiz": [
        {
            "question": "Which idiom refers to something that has both positive and negative consequences?",
            "options": {
                "A": "Root cause",
                "B": "Knock-on effect",
                "C": "Double-edged sword",
                "D": "Outweigh the disadvantages"
            },
            "correct_answer": "C",
            "explanation": "A 'double-edged sword' cuts both ways, meaning it has both good and bad effects. 'Outweigh' means the good is heavier than the bad."
        }
    ]
}

with open('output/lesson_vocab_10.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_10, f, indent=2, ensure_ascii=False)

with open('output/lesson_vocab_11.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_11, f, indent=2, ensure_ascii=False)

with open('output/lesson_vocab_12.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_12, f, indent=2, ensure_ascii=False)

with open('output/lesson_vocab_13.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_13, f, indent=2, ensure_ascii=False)

with open('output/lesson_vocab_14.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_14, f, indent=2, ensure_ascii=False)

with open('output/lesson_vocab_15.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_15, f, indent=2, ensure_ascii=False)

print("Generated remaining files successfully.")
