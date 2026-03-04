import json

batch_num = 65
filename = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p1_06.jsonl"
start_id = 251
samples = []

# Batch 65: V8/G5(10) V6/G9(10) V9/G6(10) V5/G5(10) V6/G6(10) | IDs: 0251–0300

# V8 / G5 (Music and Concerts)
c1_t = [
    ("What genre of music do you typically listen to?", "Well, I predominantly gravitating toward complex, instrumental jazz compositions during my intense study sessions. The intricate melodic structures and unpredictable syncopation it providing an incredibly stimulating auditory backdrop. Because the lack of distracting lyrics it allowing me to concentrate fully on my demanding academic research. This sophisticated genre it definitely enhancing my overall cognitive focus significantly."),
    ("Have you ever attended a major music festival?", "I attending an absolutely phenomenal, multi-day music festival in the expansive countryside last summer. The electric, palpable energy radiating from the massive, euphoric crowd it being an incredibly unforgettable sensory experience. Even though the primitive camping conditions they leaving me completely exhausted, witnessing my favorite avant-garde musicians perform live it making the severe discomfort totally worthwhile."),
    ("Do you think musical education is crucial for children?", "I firmly believing that comprehensive musical instruction it representing an absolutely indispensable component of early childhood education. When young students they mastering a difficult instrument, they actively cultivating profound discipline and enhanced spatial-temporal reasoning. This vital cognitive development it permanently enriching their intellectual capacity far beyond the mere ability to accurately replicate a simple melody."),
    ("How does your mood dictate your musical choices?", "My specific emotional state it entirely dictating the precise genre of music I selecting to consume. If I experiencing profound melancholy, I deliberately immersing myself in deeply introspective, acoustic ballads to process those complex feelings. Conversely, when I needing a sudden surge of motivation, high-tempo, energetic electronic anthems they instantly elevating my overall psychological resilience."),
    ("Why are some vintage musical artists still incredibly popular today?", "Many vintage, legendary musicians they maintaining their immense popularity because their lyrical themes remain profoundly universally relevant. The raw, authentic emotional vulnerability expressed in their classic compositions it successfully transcending the superficial barriers of different historical generations. Consequently, their timeless, masterful artistry it continuing to deeply resonate with contemporary listeners who seeking genuine emotional connection."),
    ("Do you prefer intimate acoustic performances or massive stadium concerts?", "I overwhelmingly preferring the intimate, vulnerable atmosphere of a small acoustic performance over a chaotic stadium spectacle. The subtle, nuanced vocal inflections they being much more discernible without the overwhelming distortion of massive electronic amplifiers. In a small venue, the profound, unspoken connection between the talented artist and the attentive audience it feeling remarkably authentic and pure."),
    ("Has digital streaming negatively impacted independent musicians?", "The ubiquitous proliferation of digital streaming platforms it unfortunately devastating the financial stability of independent, niche musicians. Because the abysmal royalty payout structures they overwhelmingly favoring globally recognized pop stars, struggling artists they finding it nearly impossible to sustain a viable career. This ruthless corporate exploitation it severely threatening the continued existence of diverse, experimental musical genres."),
    ("What role does music play in your cultural heritage?", "Traditional, indigenous music it functioning as the vital, beating heart of my region's complex cultural heritage. The rhythmic, percussive melodies they historically accompanying our most sacred, ancestral harvest ceremonies for countless centuries. Whenever I hearing those ancient, resonant instruments, an overwhelming surge of profound ethnic pride it instantly welling up within my chest unconditionally."),
    ("Are you interested in learning a new musical instrument?", "I currently harboring an intense, lingering desire to meticulously master the classical cello. The profoundly rich, melancholic timbre it producing is absolutely mesmerizing to my ears. Although the initial, notoriously steep learning curve it frequently discouraging adult beginners, the eventual ability to effortlessly perform sophisticated classical sonatas it remaining a highly compelling personal ambition of mine."),
    ("How does background music affect your shopping experience?", "The strategic implementation of ambient background music it undeniably manipulating consumer psychology within large retail environments. When supermarkets they broadcasting slow, relaxing melodies, the unsuspecting shoppers they subconsciously reducing their walking pace and browsing more leisurely. This clever, invisible auditory manipulation it deliberately designed to significantly maximize their impulsive, unnecessary financial expenditures during a routine visit.")
]
for q, t in c1_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v8_g5_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 8, "grammar": 5, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR8] Wide range of sophisticated vocabulary used flexibly and precisely ('syncopation', 'auditory backdrop', 'spatial-temporal reasoning', 'ubiquitous proliferation').",
        "grammar_reason": "[GRA5] Attempts complex structures but shows frequent, systematic errors in basic verb forms (double subjects, missing copula: 'genre it definitely enhancing', 'I experiencing').",
        "micro_flaws": ["systematic missing copula: 'genre it enhancing'", "systematic double subjects: 'genre it'"],
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 8\n\n**Reasoning:** [LR8] Wide vocabulary range used readily and flexibly to convey precise meaning.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Attempts complex structures but shows frequent, systematic errors in basic verb forms (double subjects, missing copula)."
    })
    start_id += 1

# V6 / G9 (Home and Accommodation)
c2_t = [
    ("Do you currently live in a house or an apartment?", "I currently reside in a rather modest apartment located squarely in the city center. Had I the financial resources, I would certainly prefer a spacious detached house, but the sheer convenience of my current location is undeniable. Not only does it reduce my daily commute, but it also places me near all the essential amenities."),
    ("What do you like most about your current neighborhood?", "What appeals to me most is the remarkably vibrant community atmosphere that permeates the local streets. Rarely have I lived in an area where the shop owners greet you by name and actively look out for one another. Provided that the rent remains affordable, I can easily envision myself staying here for the foreseeable future."),
    ("Is there anything you would change about your home?", "Were it entirely up to me, I would immediately expand the rather cramped kitchen area. Given that I thoroughly enjoy cooking elaborate meals on the weekends, the lack of adequate counter space occasionally proves to be a significant hindrance. Nevertheless, I have managed to organize the limited space quite efficiently using some clever storage solutions."),
    ("Do you prefer modern architecture or traditional housing?", "I am undoubtedly drawn to the charm and unique character of traditional housing. While modern apartments boast excellent energy efficiency, they frequently lack the interesting historical details, such as exposed brickwork or high ceilings, that make an older property feel genuinely welcoming. It is that sense of history that truly transforms a building into a home."),
    ("Have you ever shared an apartment with roommates?", "Yes, throughout my university years, I consistently shared accommodations with several close classmates. Although coordinating the cleaning schedule occasionally resulted in minor disputes, the constant social interaction effectively prevented any feelings of loneliness. Sharing the substantial utility bills also made living in the expensive capital city financially viable for struggling students like us."),
    ("What is your favorite room in your house?", "My absolute favorite space is the small, sunlit balcony attached to my bedroom. Only when I am sitting out there with a hot cup of coffee do I feel completely disconnected from the chaotic noise of the traffic below. It serves as a vital, peaceful sanctuary where I can peacefully read a book every Sunday morning."),
    ("Do you plan to move to a different city in the future?", "Should an exciting career opportunity present itself, I would be entirely open to relocating to a different city. However, unless the new position offered a significantly higher salary and better living conditions, I would be hesitant to abandon my established social circle here. Uprooting one's life requires incredibly careful consideration and meticulous planning."),
    ("What makes a house feel like a real home?", "I believe a house only truly becomes a home when it is filled with personal, meaningful items that reflect the owner's unique journey. Whether it be family photographs or souvenirs collected during memorable travels, these small details provide an essential layer of comfort. Without these personal touches, even the most expensive mansion feels somewhat sterile."),
    ("Do you think it is better to rent or buy property?", "Purchasing a property is generally considered a wiser long-term financial investment, provided you plan to remain in the same location for many years. However, for young professionals who value flexibility and might need to relocate suddenly for work, renting is arguably the much more pragmatic option. It entirely depends on an individual's specific career trajectory."),
    ("How do people in your country usually decorate their homes?", "In my country, interior decoration tends to emphasize creating a warm, highly welcoming environment for extended family gatherings. Consequently, you will frequently see large, comfortable sofas and heavily patterned rugs dominating the living rooms. While minimalist designs are slowly gaining popularity among the younger generation, traditional comfort remains the primary focus for most ordinary families.")
]
for q, t in c2_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v6_g9_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 6, "grammar": 9, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR6] Uses an adequate range of vocabulary ('essential amenities', 'cramped kitchen', 'pragmatic option'). Meaning is clear, but lacks the precision and flair of higher bands.",
        "grammar_reason": "[GRA9] Flawless grammar with full flexibility. Uses advanced structures naturally and accurately ('Had I the financial resources', 'Rarely have I lived', 'Were it entirely up to me').",
        "micro_flaws": ["none in grammar", "vocabulary is functional but safe"],
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"},
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Uses an adequate range of vocabulary with some less common items successfully.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 9\n\n**Reasoning:** [GRA9] Full mastery of complex structures. Flawless accuracy and natural flexibility."
    })
    start_id += 1

# V9 / G6 (Work and Careers)
c3_t = [
    ("What are the primary responsibilities in your current profession?", "My current corporate role it necessitating the meticulous orchestration of highly complex, multifaceted international marketing campaigns. Because the volatile global market it demanding constant strategic pivoting, I continuously analyzing dense consumer metrics to optimize our brand positioning. This rigorous, high-stakes intellectual endeavor it requiring an unparalleled level of daily cognitive stamina and unwavering professional dedication."),
    ("How do you maintain a healthy work-life equilibrium?", "Maintaining an equitable work-life equilibrium it proving to be an exceptionally formidable challenge in the modern corporate paradigm. Unless I strictly delineating my professional hours from my personal sanctuary, the insidious creep of urgent administrative emails it inevitably eroding my crucial psychological downtime. Establishing these absolutely non-negotiable boundaries it being paramount for avoiding severe, irreversible burnout."),
    ("What intrinsically motivates you to succeed in your career?", "I am intrinsically propelled by a profound, insatiable desire to enact tangible, systemic improvements within the outdated healthcare sector. While the lucrative financial remuneration it certainly offering comfortable stability, the genuine opportunity to alleviate widespread bureaucratic inefficiencies it remaining my primary, overriding professional catalyst. This profound sense of altruistic purpose it constantly fueling my daily ambition."),
    ("Have you ever considered completely changing your career trajectory?", "I occasionally entertaining the radical notion of entirely abandoning the cutthroat corporate arena to pursue sustainable, regenerative agriculture. The incredibly appealing prospect of escaping the sterile, artificial office environment to cultivate organic produce it offering a remarkably grounding, visceral contrast to my current abstract duties. However, the staggering financial risks they currently precluding such a drastic transition."),
    ("How has rapid technological innovation altered your specific industry?", "The relentless, exponential acceleration of artificial intelligence it fundamentally disrupting the traditional operational bedrock of financial forecasting. As sophisticated algorithms they flawlessly automating the tedious, repetitive data extraction, human analysts they now required to focus exclusively on highly nuanced, predictive strategic interpretation. This massive technological paradigm shift it demanding constant, exhaustive professional retraining just to remain relevant."),
    ("Do you prefer collaborative teamwork or solitary, independent projects?", "While I certainly appreciating the dynamic, synergistic brainstorming that collaborative teamwork frequently generates, I overwhelmingly preferring the intensely focused autonomy of solitary projects. When I isolated from the incessant, chaotic distractions of the open-plan office, my capacity for deep, uninterrupted conceptual analysis it peaking remarkably. This uninterrupted isolation it consistently yielding my most innovative, highly refined solutions."),
    ("What is the most frustrating aspect of your daily professional routine?", "The most profoundly exasperating aspect of my routine it being the inescapable proliferation of entirely redundant, unproductive administrative meetings. These lengthy, agonizingly circular discussions they frequently paralyzing actual operational progress while successfully generating an astonishing volume of meaningless corporate jargon. If management they streamlining this archaic communication protocol, our overall departmental efficiency it skyrocketing immediately."),
    ("How do you effectively navigate intense conflicts with difficult colleagues?", "Whenever I encountering severe interpersonal friction with a recalcitrant colleague, I deliberately employing a strategy of de-escalation and empathetic active listening. By meticulously validating their underlying professional anxieties before asserting my own contradictory perspective, the hostile tension it frequently dissipating. Cultivating this sophisticated emotional intelligence it being absolutely crucial for maintaining a functional, harmonious corporate environment."),
    ("Do you believe formal university qualifications are essential for career success?", "While prestigious academic credentials they undeniably opening initial bureaucratic doors, I firmly maintaining that adaptable, practical resilience it ultimately superseding formal education. The incredibly rapid obsolescence of technical knowledge it dictating that an employee's intrinsic capacity to rapidly assimilate new paradigms is far more valuable. True professional mastery it born from relentless, hands-on experiential learning, not textbooks."),
    ("What advice would you give a young graduate entering your field?", "I would emphatically advising any ambitious novice to proactively cultivate a diverse, highly robust network of experienced industry mentors. The labyrinthine complexities of corporate politics they being completely unteachable in a traditional classroom setting. Furthermore, embracing constructive, harsh criticism without crippling defensive ego it serving as the most potent accelerator for genuine, long-term professional development.")
]
for q, t in c3_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v9_g6_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 9, "grammar": 6, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR9] Exceptional, highly precise, and sophisticated vocabulary ('multifaceted', 'cognitive stamina', 'altruistic purpose'). Idiomatic language is natural and accurate.",
        "grammar_reason": "[GRA6] Highly noticeable and systematic errors despite the advanced vocabulary. Uses 'subject + it/they + V-ing' repeatedly ('role it necessitating').",
        "micro_flaws": ["systematic missing copula: 'role it necessitating'", "systematic double subjects: 'role it'"],
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"},
        "output": "## Vocabulary (Lexical Resource): Band 9\n\n**Reasoning:** [LR9] Uses vocabulary with full flexibility and precision in all topics.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Uses a mix of simple and complex sentence forms, but makes frequent, systematic errors in basic structures (double subjects, missing 'be' verbs)."
    })
    start_id += 1

# V5 / G5 (Shopping and Presents)
c4_t = [
    ("Do you like to buy presents for your family?", "Yes, I really enjoying to buy the nice presents for my mother on her birthday. I usually going to the big jewelry shop to finding a beautiful silver necklace. When she opening the small box, she smiling very big. It making me feel very happy to see her looking so surprised and joyful."),
    ("Is it difficult to choose a good gift for a friend?", "It being very difficult to choose the perfect gift for my young friends. Because they already having many new video games and clothes, I not knowing what they needing. Sometimes I just giving them the paper money in an envelope. This way, they can buying exactly what they wanting from the store."),
    ("Do you prefer receiving expensive gifts or handmade gifts?", "I strongly preferring to receive the simple handmade gifts from my close friends. If someone they spending many hours painting a picture for me, it showing that they caring about me very much. The expensive gold watch it is nice, but it not having the warm personal feeling of a homemade birthday card."),
    ("Have you ever received a gift that you did not like?", "Last year, my aunt she giving me a very ugly green sweater for the winter. The wool material it being very scratchy and uncomfortable on my skin. I never wearing it outside, but I always saying thank you to her politely. I keeping it hidden in the back of my dark closet."),
    ("Do you like shopping for clothes in large malls?", "I not really liking the big shopping malls because they always being too crowded and noisy. The loud music in the fashion shops it giving me a terrible headache. I preferring to buy my simple t-shirts quickly from the small local market. It saving me a lot of time and expensive parking money."),
    ("How do you usually pay when you go shopping?", "I usually using my plastic credit card to pay for everything in the supermarket. Carrying the heavy metal coins in my pocket it being very annoying and loud. The card it is much faster when I waiting in the long line. Also, the bank application it tracking how much money I spending every week."),
    ("Do you ever buy things online?", "Yes, I frequently buying the thick study books from the internet websites. Because the local bookshop it not having the special academic titles I needing, the online delivery it being very convenient. The postman he bringing the heavy package directly to my door. It is a very easy way to getting what I want."),
    ("What do you do if an online product is broken?", "If the electronic product it arriving broken, I immediately taking a clear photo with my phone. Then I sending an angry email to the customer service department to complaining about the bad quality. They usually returning my money very quickly to stopping me from writing a bad review on their public website."),
    ("Do you think packaging makes a gift more special?", "The beautiful wrapping paper it definitely making the small present look much more exciting. If you wrapping a cheap book in the shiny red paper with a big bow, it looking very professional and expensive. The person they feeling very special before they even opening the box to seeing what is inside it."),
    ("Do you wait for sales before buying expensive items?", "I always waiting patiently for the big winter sale before I buying a new computer. Because the normal price it being too high for my small salary, the fifty percent discount it helping me very much. I marking the exact date on my calendar so I not missing the great opportunity to saving money.")
]
for q, t in c4_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v5_g5_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 5, "grammar": 5, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR5] Vocabulary is adequate but relies heavily on simple, everyday terms ('beautiful silver necklace', 'heavy package'). Lacks precision.",
        "grammar_reason": "[GRA5] Attempts complex structures but with frequent, systematic errors ('I really enjoying', 'It making me'). Relies heavily on using present participles without the auxiliary 'to be'.",
        "micro_flaws": ["systematic missing copula/auxiliary: 'I enjoying', 'It making'"],
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Vocabulary is adequate but relies on basic, everyday terms.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Attempts complex structures but shows frequent, systematic errors in basic verb forms."
    })
    start_id += 1

# V6 / G6 (Public Transport and Commuting)
c5_t = [
    ("How do you travel to work every day?", "I always take the local bus to travel to my office in the city center. The bus stop is conveniently located right outside my apartment building, which saves me a lot of walking in the morning. Even though the bus is often crowded, it is the most practical way for me to commute daily."),
    ("Is the public transportation in your city expensive?", "The price of public transport in my city is actually quite reasonable compared to other places. A monthly train pass costs about fifty dollars, which allows me to travel anywhere without paying extra money. Because the government provides financial support, ordinary workers can easily afford to use the system every single day."),
    ("Do you ever travel by taxi?", "I occasionally use a taxi when I am carrying heavy shopping bags from the supermarket. If it is raining heavily and I cannot find an empty bus, the warm taxi is a very comfortable alternative. However, I avoid using them frequently because the metered fare is much too expensive for my limited student budget."),
    ("How could your city improve its transportation system?", "I think the city urgently needs to build more dedicated lanes for the public buses. Currently, the buses get stuck in the exact same terrible traffic jams as the private cars, making them very slow. If the buses could move faster, I am sure that many more people would choose to leave their cars at home."),
    ("Do you prefer sitting or standing on a long bus journey?", "I strongly prefer sitting down, especially if the bus journey takes more than an hour. When the bus turns a sharp corner or stops suddenly, standing up can be quite dangerous and uncomfortable. If I manage to find a window seat, I can relax and read my book peacefully while enjoying the view outside."),
    ("What do you usually do while traveling on the train?", "While sitting on the train, I usually listen to educational podcasts on my mobile phone. It is a fantastic way to learn something new about history or science during an otherwise boring commute. Sometimes, if I am feeling particularly tired, I simply close my eyes and try to sleep until I reach my final destination."),
    ("Have you ever missed a train or a bus?", "Yes, I completely missed my very important train last week because my alarm clock failed to ring. I had to wait alone on the cold platform for over an hour until the next one finally arrived. It was an incredibly frustrating experience that made me completely late for my morning university lecture."),
    ("Do you think driving a car is better than using public transport?", "Driving a car provides a wonderful sense of personal freedom, but it is not always the best choice in a busy city. Finding a secure parking space is incredibly stressful, and sitting in heavy traffic makes me feel very angry. For daily city travel, a reliable subway train is definitely much faster and more efficient."),
    ("Are bicycles a popular mode of transport where you live?", "Bicycles are becoming extremely popular in my neighborhood, especially among the younger university students. The local council recently built several new cycle paths, which makes riding on the roads feel much safer than before. It is a fantastic, healthy way to travel short distances while completely avoiding the polluted, crowded buses."),
    ("How do traffic jams affect your daily mood?", "Being stuck in a massive traffic jam negatively affects my mood for the entire day. Sitting in a stationary vehicle while watching the clock slowly tick away makes me feel incredibly anxious and completely powerless. By the time I finally arrive at my destination, my stress levels are already uncomfortably high.")
]
for q, t in c5_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v6_g6_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 6, "grammar": 6, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR6] Uses an adequate range of vocabulary with some less common items ('financial support', 'dedicated lanes', 'stationary vehicle'). Meaning is clear.",
        "grammar_reason": "[GRA6] Uses a mix of simple and complex sentence forms. Grammatical control is good, with only minor errors. Nothing significantly impedes communication.",
        "micro_flaws": ["none significant, safe language"],
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"},
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Uses an adequate range of vocabulary with some less common items successfully.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Mix of simple and complex structures, with noticeable but non-impeding errors."
    })
    start_id += 1

with open(filename, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
print(f"Batch {batch_num} written natively.")
