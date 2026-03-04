import json

batch_num = 63
filename = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p1_04.jsonl"
start_id = 151
samples = []

# Batch 63: V9/G9(10) V5/G7(10) V7/G5(10) V6/G8(10) V8/G6(10) | IDs: 0151–0200

# V9 / G9 (Art and Literature)
c1_t = [
    ("How often do you visit art galleries or museums?", "I am a frequent patron of the local art galleries, making a concerted effort to visit at least twice a month. Immersing myself in contemporary exhibitions provides a profoundly stimulating intellectual escape from my rigorous academic schedule. I find that engaging with provocative visual art invariably revitalizes my creative energy."),
    ("What kind of art do you find most appealing?", "I am unequivocally drawn to the mesmerizing complexities of abstract expressionism. Unlike rigidly traditional portraiture, abstract art demands a highly subjective, emotional interpretation from the viewer. The bold, chaotic brushstrokes and stark color contrasts frequently evoke a visceral psychological response that I find incredibly compelling and intellectually demanding."),
    ("Did you enjoy painting or drawing when you were a child?", "As a child, I was absolutely captivated by the sheer creative freedom of painting with vivid watercolors. My parents actively nurtured this artistic inclination, transforming our modest kitchen table into a chaotic, brightly colored studio every weekend. Those early, uninhibited explorations undoubtedly laid the foundational bedrock for my lifelong appreciation of the visual arts."),
    ("Do you think it is important to have art in public spaces?", "The strategic integration of art within public spaces is absolutely essential for cultivating a vibrant, cohesive urban identity. A monumental sculpture or a striking mural can instantly transform a sterile, utilitarian plaza into a dynamic focal point that naturally encourages spontaneous civic interaction. It effectively democratizes artistic appreciation, making it accessible to everyone."),
    ("Who is your favorite author and why?", "My absolute favorite author is Gabriel García Márquez, primarily because his mastery of magical realism is completely unparalleled. His ability to seamlessly intertwine deeply moving historical tragedies with breathtakingly surreal elements creates a mesmerizing, dreamlike narrative texture. Reading his masterful prose is always a profoundly transformative literary experience for me."),
    ("Do you prefer reading fiction or non-fiction?", "While I certainly appreciate the meticulous factual rigor of historical non-fiction, I consistently gravitate toward sophisticated literary fiction. A brilliantly crafted novel possesses the unique capacity to foster profound empathy by allowing the reader to intimately inhabit a completely foreign psychological landscape. Fiction, paradoxically, often reveals deeper universal truths than mere facts ever could."),
    ("How has the internet changed the way you discover new books?", "The advent of the internet has unequivocally revolutionized my literary discovery process, entirely replacing my reliance on traditional bookstore displays. Highly sophisticated, algorithmic recommendation engines accurately predict my idiosyncratic reading preferences with astonishing precision. Furthermore, participating in passionate online literary forums allows me to unearth obscure, brilliant independent authors I would never have found otherwise."),
    ("Do you think reading poetry is still relevant today?", "I firmly maintain that reading poetry remains profoundly relevant, perhaps even more so in our chaotic, hyper-accelerated digital age. The meticulous distillation of complex human emotion into a few perfectly chosen, resonant words offers a crucial antidote to the superficial, fleeting communication we endure daily. Poetry forces us to drastically slow down and genuinely reflect."),
    ("Have you ever attempted to write a short story or poem?", "I occasionally attempt to write brief, contemplative poems when I am experiencing particularly intense emotional turbulence. While I harbor absolutely no illusions regarding my amateurish literary prowess, the sheer act of articulating my chaotic thoughts onto paper serves as a remarkably effective cathartic release. It is a strictly private, therapeutic creative outlet."),
    ("Why do you think some classic novels remain popular for centuries?", "Classic novels achieve enduring, multi-generational popularity because they brilliantly address the fundamental, immutable core of the human condition. Regardless of the archaic societal setting, the visceral themes of passionate love, crushing betrayal, and profound existential ambition resonate universally. These masterful narratives successfully transcend the superficial constraints of their specific historical epoch.")
]
for q, t in c1_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v9_g9_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 9, "grammar": 9, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR9] Exceptional, highly precise, and sophisticated vocabulary ('obsolescence', 'visceral', 'idiosyncratic', 'immutable'). Idiomatic language is natural and accurate.",
        "grammar_reason": "[GRA9] Flawless grammar with full flexibility. Uses advanced structures naturally and accurately.",
        "micro_flaws": ["none in grammar", "none in vocabulary"],
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"},
        "output": "## Vocabulary (Lexical Resource): Band 9\n\n**Reasoning:** [LR9] Uses vocabulary with full flexibility and precision in all topics.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 9\n\n**Reasoning:** [GRA9] Full mastery of complex structures. Flawless accuracy and natural flexibility."
    })
    start_id += 1

# V5 / G7 (Hobbies and Leisure)
c2_t = [
    ("What do you like to do when you have free time?", "When I have a little free time, I really enjoy baking sweet cakes in my small kitchen. Even though it takes a few hours to mix all the heavy ingredients, the delicious smell of warm chocolate makes me feel very relaxed. If my friends visit me, we always eat the fresh cake together."),
    ("Do you prefer relaxing at home or going out?", "I definitely prefer relaxing quietly at home after a long, difficult week at the university. Going to a crowded, noisy bar requires too much extra energy, which I usually don't have on a Friday night. I would rather wear my comfortable clothes and watch a simple, funny movie on my computer."),
    ("Have your hobbies changed much since you were a child?", "Yes, my hobbies have completely changed since I was a young student in primary school. Before, I used to play outside in the dirty mud with my little brother every afternoon. But now, since I have to study so much, my only hobby is reading simple English books inside my warm bedroom."),
    ("Is there a new hobby you would like to start?", "I would really like to start growing small, green plants on my apartment balcony next spring. Because I live in the gray city, having some beautiful, natural flowers would make my home look much more cheerful. Provided I can find the time, I will buy some cheap seeds from the local market."),
    ("Do you think it's important for people to have hobbies?", "It is absolutely vital for every person to have an interesting hobby to escape their normal daily stress. If someone only focuses on their boring office work, they will eventually become very sad and completely exhausted. A simple hobby like drawing or running gives your tired brain a much-needed, refreshing break."),
    ("How much time do you spend on your hobbies every week?", "I unfortunately don't have very much time to spend on my personal hobbies during the busy week. Because my strict boss makes me work late almost every evening, I only have about three hours on Sunday morning to relax. I really wish I could spend more time simply enjoying my favorite activities."),
    ("Do you like to share your hobbies with other people?", "I generally prefer to keep my hobbies completely private because I am quite a shy person. When I try to paint a picture, I don't want anyone looking over my shoulder and judging my simple mistakes. Enjoying an activity alone makes me feel much more peaceful and completely free from outside pressure."),
    ("What is a popular leisure activity in your hometown?", "In my hometown, gathering at the local park to play traditional board games is a very popular weekend activity. The older men sit under the big green trees for many hours, loudly laughing and drinking hot, sweet tea together. It is a very simple but incredibly important social tradition for the community."),
    ("Do you ever spend your free time doing outdoor activities?", "I occasionally try to do some outdoor activities, like walking slowly around the big lake near my house. However, if the weather becomes too hot and sunny, I quickly lose all my energy and feel very uncomfortable. I definitely prefer staying in an air-conditioned room when the summer temperature gets too high."),
    ("How do hobbies help people learn new skills?", "Hobbies naturally force people to learn completely new, unexpected skills without feeling like they are sitting in a strict school. For example, if you decide to build a wooden birdhouse, you must learn how to carefully measure the wood and safely use dangerous tools. This practical, hands-on experience makes learning very fun.")
]
for q, t in c2_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v5_g7_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 5, "grammar": 7, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR5] Vocabulary is adequate but relies heavily on simple, everyday terms ('sweet cakes', 'dirty mud', 'hot tea').",
        "grammar_reason": "[GRA7] Produces frequent error-free complex sentences ('Even though it takes...', 'If someone only focuses...'). Shows good flexibility with high accuracy despite simple vocabulary.",
        "micro_flaws": ["basic vocabulary limiting the expression of complex ideas"],
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"},
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Vocabulary is adequate but relies on basic, everyday terms.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Produces frequent error-free complex sentences. Shows good flexibility with high accuracy."
    })
    start_id += 1

# V7 / G5 (Food and Restaurants)
c3_t = [
    ("What is your favorite type of food?", "I absolutely loving the authentic, spicy cuisine from the southern region of my country. The incredibly complex flavors they stimulating my taste buds in a very exciting way. Whenever I feeling slightly miserable, eating a massive bowl of that fiery noodle soup it immediately lifting my spirits and making me feel entirely rejuvenated."),
    ("Do you often eat out at restaurants?", "I frequently eating out at small, independent bistros during the busy work week. Because my exhausting corporate job it leaving me with zero energy to cook, I heavily relying on the convenience of local chefs. However, the exorbitant cumulative cost of dining out it severely impacting my ability to save any money."),
    ("What do you consider when choosing a restaurant?", "The paramount factor I considering is the overall authenticity and hygiene of the establishment. If the dining room it looking somewhat dilapidated or the staff they seeming unenthusiastic, I immediately walking away. A welcoming, meticulously clean ambiance it being just as crucial as the actual quality of the culinary dishes they serving."),
    ("Have you ever tried cooking foreign food at home?", "I recently attempting to prepare an elaborate, traditional Italian risotto in my own kitchen. Unfortunately, the delicate arborio rice it burning completely because I accidentally leaving the stove unattended for a few minutes. It being a very humbling, frustrating culinary disaster that proving I desperately needing more practical experience."),
    ("Do you prefer eating spicy or sweet foods?", "I strongly preferring intensely savory and spicy foods over anything overly sweet. The cloying sweetness of rich chocolate desserts it frequently overwhelming my palate entirely. Conversely, the sharp, vibrant heat of fresh chili peppers it providing a thrilling gastronomic experience that I constantly craving when I ordering my lunch."),
    ("Is healthy eating important to you?", "Maintaining a highly nutritious, balanced diet it becoming an absolute priority for me recently. I actively avoiding heavily processed, artificial ingredients because they inevitably causing me to feel incredibly sluggish. Incorporating an abundance of fresh, organic vegetables it significantly boosting my daily cognitive focus and overall physical vitality immensely."),
    ("What is a traditional dish from your hometown?", "My coastal hometown it being internationally famous for a deeply fragrant, slow-cooked seafood stew. The local fishermen they catching the magnificent ingredients early in the morning, guaranteeing absolute freshness. Every time I tasting that rich, complex broth, it immediately evoking a profound, nostalgic longing for my childhood memories by the sea."),
    ("Do you like to try new and unusual foods?", "I possessing a very adventurous palate, so I enthusiastically embracing any opportunity to sample highly unusual delicacies. When I traveling abroad, tasting the bizarre, unfamiliar street food it acting as the ultimate cultural immersion. Even if the strange texture it initially repulsing me, I appreciating the bold, educational experience."),
    ("How has the popularity of fast food changed diets in your country?", "The relentless proliferation of ubiquitous fast-food chains it tragically destroying our traditional dietary habits. Because the younger generation they constantly consuming these cheap, highly addictive meals, the alarming rate of childhood obesity it skyrocketing uncontrollably. This severe nutritional crisis it demanding immediate, robust government intervention to educate the vulnerable public."),
    ("Do you ever watch cooking shows on television?", "I occasionally watching the intense, highly competitive culinary programs on the television. Observing the phenomenal, Michelin-starred chefs they miraculously transforming raw ingredients into exquisite artistic masterpieces it being incredibly fascinating. However, their incredibly sophisticated techniques they being far too intimidating for an amateur cook like me to actually replicate at home.")
]
for q, t in c3_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v7_g5_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 7, "grammar": 5, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR7] Good range of less common vocabulary ('authentic', 'exorbitant cumulative cost', 'dilapidated', 'gastronomic experience').",
        "grammar_reason": "[GRA5] Attempts complex structures but with frequent, systematic errors ('I absolutely loving', 'flavors they stimulating', 'job it leaving'). Relies heavily on incorrect present participle forms without the auxiliary verb and double subjects.",
        "micro_flaws": ["systematic missing auxiliary: 'I eating'", "double subjects: 'job it', 'staff they'"],
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Good range of less common vocabulary used with some flexibility and style awareness.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Attempts complex structures but shows frequent, systematic errors in basic verb forms."
    })
    start_id += 1

# V6 / G8 (Travel and Holidays)
c4_t = [
    ("Do you prefer traveling alone or in a group?", "I definitely prefer traveling with a small group of highly organized friends. Provided that everyone agrees on the itinerary beforehand, sharing the unpredictable adventure makes the entire trip significantly more memorable. Were I to travel completely alone, I would likely feel quite isolated and anxious when trying to navigate unfamiliar city streets."),
    ("What was the most interesting place you have visited?", "The most fascinating destination I have ever explored was a tiny, ancient village hidden deep in the northern mountains. Because the local residents had preserved their traditional way of life so perfectly, stepping into their community felt exactly like traveling back in time. It was a profoundly educational and humbling cultural experience."),
    ("How do you usually plan your holidays?", "I always plan my holidays meticulously by reading countless online travel blogs several months in advance. Unless I book the hotel and flight tickets very early, the exorbitant prices will completely ruin my strict budget. Having a detailed, reliable schedule ensures that I don't waste any valuable time wandering around aimlessly upon arrival."),
    ("Do you like taking photographs while traveling?", "I used to take hundreds of quick photographs, but I recently realized that staring through a camera lens prevents me from genuinely experiencing the beautiful moment. Nowadays, I only take a few essential pictures, strongly preferring to absorb the vibrant atmosphere and commit the stunning scenery to my own natural memory."),
    ("What is the longest journey you have ever taken?", "The absolute longest journey I ever undertook was a grueling, twenty-hour train ride across the entire country. Had I not brought several thick novels and a comfortable pillow, I would have undoubtedly gone completely insane from the severe boredom. Although the beautiful window scenery was spectacular, my back was incredibly painful afterwards."),
    ("Do you think tourism is beneficial for local communities?", "Tourism is generally highly beneficial for local communities, provided that the government regulates the industry responsibly. While the influx of foreign money creates essential new jobs, an overwhelming number of tourists can easily destroy the fragile natural environment. Striking a careful balance between economic profit and ecological preservation is absolutely paramount for success."),
    ("What are the main difficulties you face when traveling abroad?", "The most significant challenge I consistently face is the frustrating language barrier when visiting rural foreign towns. Even if I try to use a digital translation application, ordering a simple meal at a local restaurant can suddenly become a highly complicated, embarrassing negotiation. It definitely requires a massive amount of patience and good humor."),
    ("Have you ever experienced culture shock?", "I experienced severe culture shock when I initially moved to a massive, bustling metropolis in Asia. Because the fast-paced, highly competitive lifestyle was completely different from my quiet, relaxed hometown, I felt entirely overwhelmed for the first few weeks. However, as I slowly adapted to the intense rhythm, I eventually learned to enjoy it."),
    ("Do you prefer relaxing on a beach or exploring a city?", "I much prefer actively exploring a vibrant, historical city rather than simply lying on a quiet beach all day. Wandering through intricate ancient museums and tasting completely unfamiliar street food stimulates my intellectual curiosity far more effectively. While a relaxing beach is nice for a day, I quickly become extremely restless and bored."),
    ("Would you like to work in the tourism industry?", "I would absolutely hate working in the high-pressure tourism industry because dealing with angry, demanding travelers seems incredibly exhausting. If a flight is suddenly canceled due to bad weather, the stressed staff must immediately solve the massive problem while remaining perfectly polite. That intense level of constant customer service would completely drain my energy.")
]
for q, t in c4_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v6_g8_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 6, "grammar": 8, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR6] Uses an adequate range of vocabulary with some less common items ('itinerary', 'exorbitant prices', 'ecological preservation'). Meaning is clear, but lacks the precision of higher bands.",
        "grammar_reason": "[GRA8] Wide range of structures used flexibly and accurately ('Provided that everyone agrees', 'Were I to travel', 'Had I not brought'). The majority of sentences are error-free.",
        "micro_flaws": ["basic vocabulary limiting expression of complex ideas"],
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"},
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Uses an adequate range of vocabulary with some less common items successfully.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 8\n\n**Reasoning:** [GRA8] Wide range of structures used flexibly and accurately. The majority of sentences are error-free."
    })
    start_id += 1

# V8 / G6 (Nature and Environment)
c5_t = [
    ("How often do you spend time in nature?", "I actively attempting to immerse myself in pristine natural environments every single weekend. Because the unrelenting cacophony of the metropolitan area it completely draining my psychological reserves, escaping to a secluded forest it acting as a vital therapeutic reset. The profound tranquility of the wilderness it immediately alleviating my severe, accumulated corporate stress."),
    ("Do you prefer the mountains or the ocean?", "I overwhelmingly favoring the majestic, rugged terrain of the towering mountains over the expansive ocean. The exhilarating, strenuous physical exertion required to conquer a steep summit it providing me with a remarkably profound sense of personal accomplishment. Furthermore, the breathtaking, panoramic vistas visible from the peak they being absolutely unparalleled in their sublime beauty."),
    ("What environmental problems are most pressing in your country?", "The incredibly rapid, unchecked industrialization it precipitating a catastrophic deterioration of our urban air quality. The ubiquitous manufacturing plants they continuously spewing noxious particulate matter into the fragile atmosphere without any regulatory oversight. Consequently, a massive, terrifying epidemic of chronic respiratory illnesses it currently devastating the vulnerable populations residing in the densely packed city centers."),
    ("Do you think individuals can make a difference in protecting the environment?", "I firmly believing that individual, conscientious consumer choices they possessing the immense cumulative power to enact tangible environmental reform. If the ordinary citizens they systematically boycotting corporations that utilize ecologically destructive packaging, the massive profit-driven companies they inevitably forced to adopt sustainable, biodegradable alternatives. Grassroots activism it remaining a incredibly potent catalyst for necessary change."),
    ("How has the natural landscape of your hometown changed?", "The pristine, idyllic natural landscape of my youth it completely vanishing beneath a relentless wave of aggressive suburban sprawl. The dense, verdant woodlands where I played as a child they being systematically eradicated to construct generic, massive shopping complexes. This devastating, irreversible ecological destruction it breaking my heart every time I returning to visit."),
    ("Do you enjoy watching documentaries about wildlife?", "I finding highly sophisticated, high-definition wildlife documentaries to be absolutely mesmerizing and profoundly educational. Observing the incredibly intricate, instinctual hunting strategies of apex predators they instilling a deep, abiding reverence for the delicate equilibrium of the global ecosystem. These brilliant cinematic productions they successfully bridging the massive disconnect between modern urbanites and the untamed wilderness."),
    ("What can schools do to teach children about environmental conservation?", "Educational institutions they must urgently implementing comprehensive, hands-on ecological curriculums for the impressionable youth. Instead of merely memorizing abstract, boring scientific facts, the students they should actively participating in local reforestation initiatives or ambitious community recycling programs. This visceral, practical engagement it guaranteeing that the next generation they developing a profound, lifelong environmental stewardship mentality."),
    ("Are there any national parks near where you live?", "Fortunately, an incredibly expansive, meticulously protected national park it bordering the northern edge of my bustling city. This magnificent, sprawling sanctuary it boasting a remarkably diverse array of indigenous flora and fauna. The local residents they fiercely defending this invaluable green lung from the constant, greedy encroachment of ambitious commercial real estate developers."),
    ("How do changing seasons affect the natural environment around you?", "The cyclical, dramatic transition of the distinct seasons it completely metamorphosing the fundamental character of the surrounding landscape. During the vibrant spring, the dormant, barren branches they suddenly erupting with an astonishing explosion of vivid, fragrant blossoms. This miraculous, inevitable annual resurrection it serving as a profound, beautiful testament to nature's incredible inherent resilience."),
    ("Do you think climate change is taken seriously enough by the public?", "Despite the overwhelming, undeniable empirical evidence, a terrifyingly large segment of the general public they remaining dangerously apathetic regarding climate change. Because the impending catastrophic consequences they often feeling geographically distant or temporally remote, many individuals they prioritizing immediate economic convenience over essential, long-term ecological sustainability. This widespread, willful ignorance it being absolutely disastrous for humanity.")
]
for q, t in c5_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v8_g6_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 8, "grammar": 6, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR8] Wide vocabulary range used readily and flexibly ('cacophony', 'therapeutic reset', 'noxious particulate matter').",
        "grammar_reason": "[GRA6] Highly noticeable and systematic errors despite the advanced vocabulary. Uses 'subject + it/they + V-ing' repeatedly ('area it completely draining').",
        "micro_flaws": ["systematic missing copula: 'area it draining'", "systematic double subjects: 'plants they'"],
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"},
        "output": "## Vocabulary (Lexical Resource): Band 8\n\n**Reasoning:** [LR8] Wide vocabulary range used readily and flexibly to convey precise meaning.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Uses a mix of simple and complex sentence forms, but makes frequent, systematic errors in basic structures (double subjects, missing 'be' verbs)."
    })
    start_id += 1

with open(filename, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
print(f"Batch {batch_num} written natively without padding.")
