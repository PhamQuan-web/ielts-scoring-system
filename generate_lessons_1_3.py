import json
import os

# Ensure output directory exists
os.makedirs('output', exist_ok=True)

lesson_1 = {
    "lesson_id": "vocab_core_01",
    "title": "Core Vocabulary: Education",
    "topic_snapshot": {
        "target_skills": ["Writing", "Speaking"],
        "description": "Essential vocabulary, collocations, and phrasing to discuss academic systems, learning methods, and educational challenges in IELTS."
    },
    "key_vocabulary_bank": [
        {
            "word": "Curriculum",
            "phonetic": "/kəˈrɪkjʊləm/",
            "cefr_level": "B2",
            "meaning": "The subjects comprising a course of study in a school or college.",
            "example": "The new national curriculum places a greater emphasis on science and technology.",
            "image_url": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A high-quality photograph of a diverse group of high school students studying together at a modern library table, surrounded by textbooks and laptops."
        },
        {
            "word": "Pedagogy",
            "phonetic": "/ˈpedəɡɒdʒi/",
            "cefr_level": "C1",
            "meaning": "The method and practice of teaching, especially as an academic subject or theoretical concept.",
            "example": "Modern pedagogy often focuses on interactive and student-centered learning rather than rote memorization.",
            "image_url": "https://images.unsplash.com/photo-1577896851231-70ef18881754?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A dynamic shot of a passionate teacher explaining a concept at a whiteboard to an engaged class, bright lighting."
        },
        {
            "word": "Bursary",
            "phonetic": "/ˈbɜːsəri/",
            "cefr_level": "C1",
            "meaning": "A grant, especially one awarded to someone to enable them to study at university or college.",
            "example": "She was awarded a full bursary to study engineering based on her outstanding academic record.",
            "image_url": None,
            "image_prompt_fallback": "A close-up of a smiling student proudly holding a scholarship award certificate or an acceptance letter, professional portrait style."
        },
        {
            "word": "Illiteracy",
            "phonetic": "/ɪˈlɪtərəsi/",
            "cefr_level": "B2",
            "meaning": "The inability to read or write.",
            "example": "The government has launched a campaign to eradicate adult illiteracy in rural areas.",
            "image_url": None,
            "image_prompt_fallback": "A poignant documentary-style photo of an adult learning to write for the first time, holding a pencil and tracing letters on paper."
        },
        {
            "word": "Extracurricular",
            "phonetic": "/ˌekstrəkəˈrɪkjʊlə/",
            "cefr_level": "B2",
            "meaning": "Pursued in addition to the normal course of study.",
            "example": "Universities often look for candidates who participate in extracurricular activities like sports or debate clubs.",
            "image_url": "https://images.unsplash.com/photo-1526676037777-05a232554f77?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A vibrant photograph of a school sports team playing football on a green field during sunset, emphasizing teamwork outside the classroom."
        }
    ],
    "collocation_builder": [
        {
            "collocation": "Pursue higher education",
            "meaning": "To continue studying at a university or college level.",
            "example": "Many high school graduates pursue higher education to improve their career prospects."
        },
        {
            "collocation": "Fall behind in studies",
            "meaning": "To fail to keep pace with the academic progress expected.",
            "example": "Students who miss classes frequently are likely to fall behind in their studies."
        },
        {
            "collocation": "Broaden one's horizons",
            "meaning": "To expand one's range of knowledge, interests, and experiences.",
            "example": "Studying abroad is an excellent way to broaden your horizons and learn about different cultures."
        },
        {
            "collocation": "Meet academic requirements",
            "meaning": "To fulfill the necessary standards or grades for a course.",
            "example": "Applicants must meet strict academic requirements to be accepted into the medical program."
        }
    ],
    "upgrade_section": [
        {
            "weak_phrase": "Learn by heart",
            "better_upgrade": "Rote memorization",
            "example": "Some critics argue that an over-reliance on rote memorization stifles critical thinking."
        },
        {
            "weak_phrase": "Go to university",
            "better_upgrade": "Pursue tertiary education",
            "example": "The government is offering incentives to encourage more young people to pursue tertiary education."
        },
        {
            "weak_phrase": "Good teachers",
            "better_upgrade": "Highly qualified educators",
            "example": "The success of the school is largely due to its team of highly qualified educators."
        }
    ],
    "sentence_frames": [
        "One of the primary benefits of [Noun Phrase] is that it allows students to [Verb Phrase].",
        "It is widely argued that [Subject] should prioritize [Noun Phrase] in order to [Verb Phrase].",
        "Despite the advantages of [Noun Phrase], a significant drawback is that [Clause]."
    ],
    "ielts_usage_examples": {
        "writing_example": "In contemporary society, it is widely argued that schools should prioritize practical skills over theoretical knowledge. While I acknowledge the value of subjects like mathematics and literature, I firmly believe that equipping students with vocational skills is crucial for their future career prospects.",
        "speaking_example": "Well, back when I was in high school, the curriculum was quite rigid and heavily focused on rote memorization. Looking back, I think a more interactive pedagogy would have been beneficial in helping us grasp complex concepts more effectively."
    },
    "common_mistakes": [
        "Using 'learn' instead of 'study'. (e.g., 'I learn biology at university' -> 'I study biology at university').",
        "Confusing 'education' (the process) with 'background' (personal history). (e.g., 'My education is very poor' -> 'My educational background is quite limited')."
    ],
    "quiz": [
        {
            "question": "Which of the following phrases best describes the inability to read or write?",
            "options": {
                "A": "Rote memorization",
                "B": "Illiteracy",
                "C": "Pedagogy",
                "D": "Extracurricular"
            },
            "correct_answer": "B",
            "explanation": "'Illiteracy' specifically refers to the inability to read or write. 'Rote memorization' is learning by repetition, 'pedagogy' is the method of teaching, and 'extracurricular' refers to activities outside the normal curriculum."
        }
    ]
}


lesson_2 = {
    "lesson_id": "vocab_core_02",
    "title": "Core Vocabulary: Work & Career",
    "topic_snapshot": {
        "target_skills": ["Writing", "Speaking"],
        "description": "Crucial terminology for discussing employment, career progression, workplace environments, and job market trends."
    },
    "key_vocabulary_bank": [
        {
            "word": "Lucrative",
            "phonetic": "/ˈluːkrətɪv/",
            "cefr_level": "C1",
            "meaning": "Producing a great deal of profit; well-paid.",
            "example": "He decided to pursue a highly lucrative career in investment banking.",
            "image_url": "https://images.unsplash.com/photo-1565514020179-026b92b84bb6?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A professional in a sharp suit standing in a modern high-rise office overlooking a city skyline, checking financial charts on a tablet."
        },
        {
            "word": "Remuneration",
            "phonetic": "/rɪˌmjuːnəˈreɪʃn/",
            "cefr_level": "C1",
            "meaning": "Money paid for work or a service; salary and benefits.",
            "example": "They are demanding adequate remuneration for the extra hours they have worked.",
            "image_url": None,
            "image_prompt_fallback": "A close up of a stylized salary slip and a pen resting on top of a modern office desk."
        },
        {
            "word": "Redundant",
            "phonetic": "/rɪˈdʌndənt/",
            "cefr_level": "B2",
            "meaning": "No longer in employment because there is no more work available (often used in 'to be made redundant').",
            "example": "Due to the economic downturn, thousands of factory workers were made redundant.",
            "image_url": None,
            "image_prompt_fallback": "A documentary-style photo of a person packing a cardboard box at their office desk, looking somber."
        },
        {
            "word": "Entrepreneur",
            "phonetic": "/ˌɒntrəprəˈnɜː/",
            "cefr_level": "B2",
            "meaning": "A person who sets up a business or businesses, taking on financial risks in the hope of profit.",
            "example": "A successful entrepreneur needs not only a good idea but also the resilience to face setbacks.",
            "image_url": "https://images.unsplash.com/photo-1556761175-4b46a572b786?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A young, confident business owner standing inside their newly opened modern cafe, smiling warmly at the camera."
        },
        {
            "word": "Burnout",
            "phonetic": "/ˈbɜːnaʊt/",
            "cefr_level": "C1",
            "meaning": "Physical or mental collapse caused by overwork or stress.",
            "example": "Employees experiencing severe burnout are more likely to take extended sick leave.",
            "image_url": "https://images.unsplash.com/photo-1498677231914-50efa696e615?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "An exhausted office worker rubbing their eyes in front of a glowing computer screen late at night in a dark office."
        }
    ],
    "collocation_builder": [
        {
            "collocation": "Climb the corporate ladder",
            "meaning": "To advance in one's career within a company.",
            "example": "He is highly ambitious and is determined to climb the corporate ladder as quickly as possible."
        },
        {
            "collocation": "Strike a work-life balance",
            "meaning": "To maintain a healthy division between professional responsibilities and personal life.",
            "example": "It can be difficult to strike a work-life balance when working in a highly competitive industry."
        },
        {
            "collocation": "Heavy workload",
            "meaning": "A large amount of work that needs to be done.",
            "example": "The heavy workload is causing a lot of stress among the teaching staff."
        },
        {
            "collocation": "Job satisfaction",
            "meaning": "The feeling of pleasure and achievement that you experience in your job.",
            "example": "For many people, job satisfaction is just as important as a high salary."
        }
    ],
    "upgrade_section": [
        {
            "weak_phrase": "Get a job",
            "better_upgrade": "Secure employment",
            "example": "University graduates are finding it increasingly difficult to secure employment in their chosen fields."
        },
        {
            "weak_phrase": "Hard-working",
            "better_upgrade": "Industrious / Diligent",
            "example": "She is an exceptionally diligent employee who consistently exceeds expectations."
        },
        {
            "weak_phrase": "Lose a job",
            "better_upgrade": "Be made redundant / Dismissed",
            "example": "During the recession, many middle managers were made redundant to cut costs."
        }
    ],
    "sentence_frames": [
        "In today's competitive job market, it is essential for individuals to [Verb Phrase].",
        "A growing number of professionals prioritize [Noun Phrase] over [Noun Phrase].",
        "From an economic perspective, fostering [Noun Phrase] can lead to [Noun Phrase]."
    ],
    "ielts_usage_examples": {
        "writing_example": "It is often argued that a high salary is the most important factor when choosing a career. However, I believe that job satisfaction and a healthy work-life balance are equally, if not more, significant for long-term well-being and productivity.",
        "speaking_example": "Currently, I'm working as a software engineer. It's quite a demanding role with a heavy workload, but the remuneration is excellent. In the future, I hope to climb the corporate ladder and eventually move into a management position."
    },
    "common_mistakes": [
        "Using 'work' as a plural countable noun. (e.g., 'I have many works to do' -> 'I have a lot of work to do' or 'I have many tasks').",
        "Confusing 'job' (a specific role) with 'career' (long-term professional journey). (e.g., 'I want a job in medicine for my whole life' -> 'I want a career in medicine')."
    ],
    "quiz": [
        {
            "question": "If someone loses their job because the company no longer needs that position, they are:",
            "options": {
                "A": "Remunerated",
                "B": "Lucrative",
                "C": "Redundant",
                "D": "Burned out"
            },
            "correct_answer": "C",
            "explanation": "To be 'made redundant' means to lose your job because the work is no longer needed or the company is downsizing. 'Remunerated' means paid, 'lucrative' means profitable, and 'burned out' refers to exhaustion from overwork."
        }
    ]
}


lesson_3 = {
    "lesson_id": "vocab_core_03",
    "title": "Core Vocabulary: Technology",
    "topic_snapshot": {
        "target_skills": ["Writing", "Speaking"],
        "description": "Advanced vocabulary for discussing digital innovation, the impact of the internet, automation, and tech dependency."
    },
    "key_vocabulary_bank": [
        {
            "word": "Breakthrough",
            "phonetic": "/ˈbreɪkθruː/",
            "cefr_level": "B2",
            "meaning": "A sudden, dramatic, and important discovery or development.",
            "example": "The invention of the internet was a major technological breakthrough that changed the world.",
            "image_url": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A futuristic glowing microchip being held by a robotic arm, symbolizing a scientific discovery, cinematic lighting."
        },
        {
            "word": "Obsolete",
            "phonetic": "/ˈɒbsəliːt/",
            "cefr_level": "C1",
            "meaning": "No longer produced or used; out of date.",
            "example": "Rapid advancements in technology quickly render older devices obsolete.",
            "image_url": None,
            "image_prompt_fallback": "A dusty pile of old, outdated electronics like floppy disks, cassette tapes, and bulky CRT monitors."
        },
        {
            "word": "Automation",
            "phonetic": "/ˌɔːtəˈmeɪʃn/",
            "cefr_level": "C1",
            "meaning": "The use of largely automatic equipment in a system of manufacturing or other production process.",
            "example": "Increased automation in manufacturing has led to a significant loss of traditional factory jobs.",
            "image_url": "https://images.unsplash.com/photo-1563914841804-06d27163821a?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A highly automated modern car manufacturing assembly line with bright orange robotic arms welding a car chassis."
        },
        {
            "word": "Cutting-edge",
            "phonetic": "/ˌkʌtɪŋ ˈedʒ/",
            "cefr_level": "B2",
            "meaning": "Highly advanced; innovative or pioneering.",
            "example": "The company specializes in developing cutting-edge software for artificial intelligence.",
            "image_url": None,
            "image_prompt_fallback": "A sleek, futuristic smartphone or device glowing with abstract digital data projections in a dark room."
        },
        {
            "word": "Cybersecurity",
            "phonetic": "/ˌsaɪbəsɪˈkjʊərəti/",
            "cefr_level": "B2",
            "meaning": "The state of being protected against the criminal or unauthorized use of electronic data.",
            "example": "With the rise of online banking, banks are investing heavily in cybersecurity measures.",
            "image_url": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?q=80&w=800&auto=format&fit=crop",
            "image_prompt_fallback": "A glowing digital padlock symbol overlaying binary code on a computer monitor, representing data protection."
        }
    ],
    "collocation_builder": [
        {
            "collocation": "Technological advancements",
            "meaning": "Progress or improvements in technology.",
            "example": "Recent technological advancements have revolutionized the way we communicate."
        },
        {
            "collocation": "Become overly reliant on",
            "meaning": "To depend too much on something.",
            "example": "Critics argue that teenagers have become overly reliant on their smartphones for social interaction."
        },
        {
            "collocation": "Bridge the digital divide",
            "meaning": "To reduce the gap between people who have access to modern technology and those who do not.",
            "example": "Governments must invest in rural infrastructure to bridge the digital divide."
        },
        {
            "collocation": "Surf the net",
            "meaning": "To spend time browsing the internet.",
            "example": "In my free time, I often surf the net to read news articles or watch videos."
        }
    ],
    "upgrade_section": [
        {
            "weak_phrase": "New technology",
            "better_upgrade": "Cutting-edge / State-of-the-art technology",
            "example": "The hospital is equipped with state-of-the-art technology for diagnosing rare diseases."
        },
        {
            "weak_phrase": "Old technology",
            "better_upgrade": "Obsolete / Outdated technology",
            "example": "Many schools are struggling to replace their outdated technology."
        },
        {
            "weak_phrase": "Fix computer problems",
            "better_upgrade": "Troubleshoot technical issues",
            "example": "The IT department is responsible for troubleshooting technical issues across the company."
        }
    ],
    "sentence_frames": [
        "The proliferation of [Noun Phrase] has fundamentally transformed the way we [Verb Phrase].",
        "While [Noun Phrase] offers numerous conveniences, it also poses significant challenges, such as [Noun Phrase].",
        "Looking ahead, it is inevitable that [Noun Phrase] will continue to [Verb Phrase]."
    ],
    "ielts_usage_examples": {
        "writing_example": "The proliferation of smartphones has undeniably brought unprecedented convenience to our daily lives. However, I believe that society has become overly reliant on these devices, leading to a decline in face-to-face communication and an increase in sedentary lifestyles.",
        "speaking_example": "I'm quite interested in technology, particularly artificial intelligence. The recent breakthroughs in this field are fascinating. However, I do worry about the ethical implications and how automation might make certain jobs obsolete in the future."
    },
    "common_mistakes": [
        "Using 'informations' (Information is uncountable). (e.g., 'The internet provides many informations' -> 'The internet provides a lot of information').",
        "Using 'equipments' (Equipment is uncountable). (e.g., 'We need new equipments' -> 'We need new equipment')."
    ],
    "quiz": [
        {
            "question": "Which term describes technology that is highly advanced and innovative?",
            "options": {
                "A": "Obsolete",
                "B": "Automation",
                "C": "Cutting-edge",
                "D": "Cybersecurity"
            },
            "correct_answer": "C",
            "explanation": "'Cutting-edge' refers to the newest, most advanced stage in the development of something. 'Obsolete' means outdated, 'automation' is using machines to do work, and 'cybersecurity' is data protection."
        }
    ]
}


with open('output/lesson_vocab_01.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_1, f, indent=2, ensure_ascii=False)

with open('output/lesson_vocab_02.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_2, f, indent=2, ensure_ascii=False)

with open('output/lesson_vocab_03.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_3, f, indent=2, ensure_ascii=False)

print("Generated files successfully.")
