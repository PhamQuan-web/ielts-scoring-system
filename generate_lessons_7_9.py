import json
import os

os.makedirs('output', exist_ok=True)

lesson_7 = {
    "lesson_id": "vocab_core_07",
    "title": "Core Vocabulary: Government & Public Services",
    "topic_snapshot": {
        "target_skills": ["Writing", "Speaking"],
        "description": "Essential vocabulary for discussing state responsibilities, taxation, infrastructure, and public policy."
    },
    "key_vocabulary_bank": [
        {
            "word": "Infrastructure",
            "phonetic": "/ˈɪnfrəstrʌktʃə/",
            "cefr_level": "B2",
            "meaning": "The basic physical and organizational structures and facilities (e.g., buildings, roads, power supplies) needed for the operation of a society.",
            "example": "The government has pledged to invest heavily in modernizing the country's aging infrastructure.",
            "image_url": "https://images.unsplash.com/photo-1541888086425-d81bb19240f5?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A complex highway interchange with multiple levels of roads, bridges, and traffic flowing smoothly."
        },
        {
            "word": "Allocate",
            "phonetic": "/ˈæləkeɪt/",
            "cefr_level": "C1",
            "meaning": "Distribute resources or duties for a particular purpose.",
            "example": "A significant portion of the state budget must be allocated to public education.",
            "image_url": None,
            "image_prompt_fallback": "A pie chart showing government spending being divided into different sectors like health, education, and defense."
        },
        {
            "word": "Bureaucracy",
            "phonetic": "/bjʊəˈrɒkrəsi/",
            "cefr_level": "C1",
            "meaning": "A system of government or business in which most of the important decisions are taken by state officials rather than by elected representatives; excessively complicated administrative procedure.",
            "example": "Many small business owners complain about the endless bureaucracy involved in getting a permit.",
            "image_url": None,
            "image_prompt_fallback": "A massive stack of paperwork and forms sitting on a messy desk with a frustrated worker behind it."
        },
        {
            "word": "Subsidize",
            "phonetic": "/ˈsʌbsɪdaɪz/",
            "cefr_level": "C1",
            "meaning": "Support an organization or activity financially.",
            "example": "To encourage the use of public transport, the local council subsidizes bus fares for students.",
            "image_url": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A person handing cash over a counter or paying digitally for a bus ticket at a heavily discounted rate."
        }
    ],
    "collocation_builder": [
        {
            "collocation": "Implement policies",
            "meaning": "To put a decision or plan into effect.",
            "example": "The new administration plans to implement policies that reduce carbon emissions."
        },
        {
            "collocation": "Levy taxes",
            "meaning": "To impose or collect a tax.",
            "example": "Governments levy taxes on citizens to fund public services like healthcare and roads."
        },
        {
            "collocation": "Public expenditure",
            "meaning": "Money spent by the government on public services.",
            "example": "There has been a sharp debate over whether to increase public expenditure during the recession."
        }
    ],
    "upgrade_section": [
        {
            "weak_phrase": "Make a rule",
            "better_upgrade": "Enact legislation",
            "example": "The parliament voted to enact legislation restricting the sale of tobacco to minors."
        },
        {
            "weak_phrase": "Give money to",
            "better_upgrade": "Provide funding for",
            "example": "The state must provide funding for low-income housing projects."
        }
    ],
    "sentence_frames": [
        "It is the primary responsibility of the government to [Verb Phrase].",
        "By [Gerund Phrase], authorities can effectively address the issue of [Noun Phrase].",
        "A common criticism of current public policy is that it fails to [Verb Phrase]."
    ],
    "ielts_usage_examples": {
        "writing_example": "It is often argued that the government should be solely responsible for providing free healthcare. While private clinics have a role to play, I believe it is the primary responsibility of the state to allocate sufficient tax revenues to subsidize public medical services, ensuring equal access for all citizens.",
        "speaking_example": "Well, in my country, the public transport infrastructure is quite well-developed because the government heavily subsidizes it. However, the bureaucracy involved in getting anything built or repaired can be extremely frustrating and slow."
    },
    "common_mistakes": [
        "Using 'governments' unnecessarily when referring to the concept of the state. (e.g., 'Governments should help the poor' -> 'The government should help the poor').",
        "Confusing 'politics' (the activities of government) with 'policy' (a specific plan of action). (e.g., 'The government made a new politics' -> 'The government implemented a new policy')."
    ],
    "quiz": [
        {
            "question": "Which word describes the complex administrative procedures often associated with government departments?",
            "options": {
                "A": "Infrastructure",
                "B": "Bureaucracy",
                "C": "Expenditure",
                "D": "Legislation"
            },
            "correct_answer": "B",
            "explanation": "'Bureaucracy' refers to the excessively complicated administrative procedures or the officials who run government departments. 'Infrastructure' means physical facilities, 'expenditure' is spending, and 'legislation' refers to laws."
        }
    ]
}

lesson_8 = {
    "lesson_id": "vocab_core_08",
    "title": "Core Vocabulary: Crime & Law",
    "topic_snapshot": {
        "target_skills": ["Writing", "Speaking"],
        "description": "Vocabulary for discussing the justice system, types of crime, punishment, and rehabilitation."
    },
    "key_vocabulary_bank": [
        {
            "word": "Deterrent",
            "phonetic": "/dɪˈterənt/",
            "cefr_level": "C1",
            "meaning": "A thing that discourages or is intended to discourage someone from doing something.",
            "example": "Many argue that the death penalty is not an effective deterrent to violent crime.",
            "image_url": "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A stern judge holding a wooden gavel in a courtroom."
        },
        {
            "word": "Rehabilitation",
            "phonetic": "/ˌriːhəˌbɪlɪˈteɪʃn/",
            "cefr_level": "C1",
            "meaning": "The action of restoring someone to health or normal life through training and therapy after imprisonment.",
            "example": "Prisons should focus more on the rehabilitation of offenders rather than just punishment.",
            "image_url": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A group therapy session with people sitting in a circle, talking and supporting each other."
        },
        {
            "word": "Juvenile",
            "phonetic": "/ˈdʒuːvənaɪl/",
            "cefr_level": "B2",
            "meaning": "Relating to young people; a young person who commits a crime.",
            "example": "There has been a worrying increase in juvenile delinquency in urban areas.",
            "image_url": None,
            "image_prompt_fallback": "A hooded teenager standing alone in an alleyway at night, looking defiant."
        },
        {
            "word": "Perpetrator",
            "phonetic": "/ˈpɜːpətreɪtə/",
            "cefr_level": "C1",
            "meaning": "A person who carries out a harmful, illegal, or immoral act.",
            "example": "The perpetrators of this cyber-attack have not yet been identified by the authorities.",
            "image_url": None,
            "image_prompt_fallback": "A shadowy figure in a dark room typing intensely on a laptop computer."
        }
    ],
    "collocation_builder": [
        {
            "collocation": "Commit a crime",
            "meaning": "To do something illegal.",
            "example": "Poverty is often a driving factor that pushes people to commit a crime."
        },
        {
            "collocation": "Serve a sentence",
            "meaning": "To spend time in prison as a punishment.",
            "example": "He is currently serving a ten-year sentence for armed robbery."
        },
        {
            "collocation": "Law-abiding citizens",
            "meaning": "People who obey the law.",
            "example": "The new security measures are designed to protect law-abiding citizens from terrorism."
        }
    ],
    "upgrade_section": [
        {
            "weak_phrase": "Break the law",
            "better_upgrade": "Violate / Infringe the law",
            "example": "Companies that violate environmental laws should face severe financial penalties."
        },
        {
            "weak_phrase": "Punish people",
            "better_upgrade": "Impose penalties / Sanctions",
            "example": "The judge decided to impose harsh penalties on the organized crime syndicate."
        }
    ],
    "sentence_frames": [
        "While strict punishments act as a deterrent, they do not address the root causes of [Noun Phrase].",
        "Rather than focusing solely on retribution, the justice system should prioritize [Noun Phrase].",
        "It is highly debatable whether [Noun Phrase] is an effective strategy for reducing crime rates."
    ],
    "ielts_usage_examples": {
        "writing_example": "Many believe that imposing longer prison sentences is the best way to reduce crime rates. However, I argue that while harsh punishments act as a deterrent, a justice system that prioritizes the rehabilitation of offenders through education and job training is far more effective at preventing reoffending.",
        "speaking_example": "In my opinion, juvenile delinquency is usually a result of poor upbringing or peer pressure. Instead of sending young offenders straight to prison, I think society should focus on rehabilitating them so they can become law-abiding citizens in the future."
    },
    "common_mistakes": [
        "Using 'make a crime' instead of 'commit a crime'. (e.g., 'If you make a crime' -> 'If you commit a crime').",
        "Confusing 'rob' (stealing from a person/place) with 'steal' (taking an object). (e.g., 'He robbed my phone' -> 'He stole my phone' OR 'He robbed the bank')."
    ],
    "quiz": [
        {
            "question": "Which of the following terms refers to restoring an offender to normal life through therapy and training?",
            "options": {
                "A": "Deterrent",
                "B": "Rehabilitation",
                "C": "Perpetrator",
                "D": "Juvenile"
            },
            "correct_answer": "B",
            "explanation": "'Rehabilitation' is the process of helping an inmate or offender reintegrate into society. A 'deterrent' is something that stops crime, a 'perpetrator' is the criminal, and 'juvenile' means young."
        }
    ]
}

lesson_9 = {
    "lesson_id": "vocab_core_09",
    "title": "Core Vocabulary: Economy & Money",
    "topic_snapshot": {
        "target_skills": ["Writing", "Speaking"],
        "description": "Terminology to discuss personal finance, national economies, globalization, and consumerism."
    },
    "key_vocabulary_bank": [
        {
            "word": "Consumerism",
            "phonetic": "/kənˈsjuːmərɪzəm/",
            "cefr_level": "C1",
            "meaning": "The preoccupation of society with the acquisition of consumer goods.",
            "example": "Modern consumerism has led to a massive increase in waste and environmental degradation.",
            "image_url": "https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A crowded shopping mall with people carrying dozens of shopping bags from luxury brands."
        },
        {
            "word": "Inflation",
            "phonetic": "/ɪnˈfleɪʃn/",
            "cefr_level": "B2",
            "meaning": "A general increase in prices and fall in the purchasing value of money.",
            "example": "High inflation means that the cost of living has skyrocketed over the past year.",
            "image_url": "https://images.unsplash.com/photo-1580519542036-ed47f3e42f9b?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A close-up of a price tag showing a dramatically high price on a basic loaf of bread."
        },
        {
            "word": "Recession",
            "phonetic": "/rɪˈseʃn/",
            "cefr_level": "C1",
            "meaning": "A period of temporary economic decline during which trade and industrial activity are reduced.",
            "example": "Many small businesses went bankrupt during the global economic recession of 2008.",
            "image_url": None,
            "image_prompt_fallback": "A red downward-trending line graph displayed on a digital stock market board."
        },
        {
            "word": "Disparity",
            "phonetic": "/dɪˈspærəti/",
            "cefr_level": "C1",
            "meaning": "A great difference or inequality.",
            "example": "The growing economic disparity between the rich and the poor is a major cause for concern.",
            "image_url": None,
            "image_prompt_fallback": "A split-screen image showing a luxurious mansion on one side and an impoverished slum on the other."
        }
    ],
    "collocation_builder": [
        {
            "collocation": "Standard of living",
            "meaning": "The degree of wealth and material comfort available to a person or community.",
            "example": "The main goal of economic development is to raise the standard of living for all citizens."
        },
        {
            "collocation": "Cost of living",
            "meaning": "The level of prices relating to a range of everyday items.",
            "example": "The high cost of living in major cities makes it difficult for young people to save money."
        },
        {
            "collocation": "Disposable income",
            "meaning": "Income remaining after deduction of taxes and other mandatory charges, available to be spent or saved.",
            "example": "With rising rents, many families have very little disposable income left at the end of the month."
        }
    ],
    "upgrade_section": [
        {
            "weak_phrase": "Poor people",
            "better_upgrade": "Disadvantaged / Impoverished citizens",
            "example": "The charity provides essential support to impoverished citizens in rural areas."
        },
        {
            "weak_phrase": "Rich countries",
            "better_upgrade": "Developed / Affluent nations",
            "example": "Affluent nations have a moral obligation to assist developing countries in times of crisis."
        }
    ],
    "sentence_frames": [
        "The primary driver of [Noun Phrase] in today's economy is [Noun Phrase].",
        "While a free market economy encourages [Noun Phrase], it can also lead to significant [Noun Phrase].",
        "To ensure economic stability, the government must regulate [Noun Phrase]."
    ],
    "ielts_usage_examples": {
        "writing_example": "The rapid spread of consumerism in affluent nations has undoubtedly raised the standard of living for many. However, this insatiable desire for goods has also created a throwaway culture that severely damages the environment and exacerbates the economic disparity between classes.",
        "speaking_example": "Recently, inflation has been a massive issue here. The cost of living has gone up so much that most people's disposable income has practically vanished. It feels like we are on the brink of an economic recession."
    },
    "common_mistakes": [
        "Confusing 'economic' (relating to the economy) with 'economical' (giving good value, saving money). (e.g., 'Hybrid cars are very economic' -> 'Hybrid cars are very economical').",
        "Using 'incomes' when referring to a general sum. 'Income' is usually uncountable unless referring to different types of revenue. (e.g., 'My incomes are low' -> 'My income is low')."
    ],
    "quiz": [
        {
            "question": "Which term specifically describes a period of temporary economic decline?",
            "options": {
                "A": "Inflation",
                "B": "Consumerism",
                "C": "Recession",
                "D": "Disparity"
            },
            "correct_answer": "C",
            "explanation": "A 'recession' is an economic decline. 'Inflation' is the rise in prices, 'consumerism' is the focus on buying goods, and 'disparity' means inequality."
        }
    ]
}


with open('output/lesson_vocab_07.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_7, f, indent=2, ensure_ascii=False)

with open('output/lesson_vocab_08.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_8, f, indent=2, ensure_ascii=False)

with open('output/lesson_vocab_09.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_9, f, indent=2, ensure_ascii=False)

print("Generated files successfully.")
