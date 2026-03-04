import json

batch_num = 68
filename = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p1_09.jsonl"
start_id = 401
samples = []

# Batch 68: V7/G6(10) V8/G7(10) V4/G4(10) V5/G5(10) V6/G6(10) | IDs: 0401–0450

# V7 / G6 (Social Media and Communication)
c1_t = [
    ("How frequently do you update your social media profiles?", "I sporadically updating my professional social media profile, primarily when I successfully completing a major corporate project. However, I deliberately avoiding posting intimate, personal photographs on public platforms. Because the terrifying concept of permanent digital exposure it making me profoundly uncomfortable, I rigorously maintaining my essential privacy online."),
    ("Do you think social media has negatively impacted real-life communication?", "I strongly believing that the pervasive influence of social media it significantly deteriorating our capacity for genuine interpersonal communication. When close friends they sitting together at a restaurant, they frequently staring silently at their glowing screens instead of conversing. This undeniable digital addiction it effectively destroying the crucial emotional resonance of physical interaction."),
    ("What are the primary benefits of professional networking sites?", "The primary advantage of utilizing sophisticated networking platforms it being the unprecedented ability to instantly connect with industry leaders globally. If an ambitious graduate they meticulously crafting a compelling digital portfolio, they frequently attracting lucrative career opportunities completely organically. This powerful technological tool it practically eliminating the traditional barriers to professional advancement."),
    ("How do you manage the constant influx of digital notifications?", "To effectively manage the overwhelming barrage of digital notifications, I deliberately activating the 'do not disturb' function during my rigorous study hours. If I constantly responding to trivial text messages, my overall intellectual concentration it immediately fracturing into useless pieces. Establishing these strict technological boundaries it being absolutely necessary for preserving my sanity."),
    ("Why do some people prefer texting over calling?", "Many introverted individuals they overwhelmingly preferring the asynchronous nature of text messaging because it providing a protective psychological buffer. When you composing a text, you possessing the luxury of meticulously calculating your exact response before hitting send. Conversely, a sudden phone call it demanding immediate, spontaneous interaction, which frequently triggering severe social anxiety."),
    ("Have you ever participated in a massive online forum discussion?", "I occasionally participating in highly specialized, academic online forums to passionately debate complex historical theories with international scholars. Because these dedicated platforms they uniting people with incredibly niche intellectual interests, the resulting conversations they usually being remarkably illuminating. It providing a fantastic intellectual escape from my somewhat mundane, predictable daily routine."),
    ("Do you believe everything you read on the internet?", "I maintaining a remarkably skeptical attitude toward any unverified information I casually encountering on the internet. Because the rapid proliferation of sophisticated, malicious misinformation it severely polluting the digital landscape, I rigorously cross-referencing multiple reputable news sources before forming an opinion. Blindly trusting anonymous online articles it being an incredibly dangerous intellectual habit."),
    ("How has video calling changed your long-distance relationships?", "The widespread availability of high-definition video calling it completely revolutionizing how I effortlessly maintaining my crucial long-distance relationships. Being able to clearly observing my mother's subtle facial expressions while we talking it instantly bridging the massive geographical divide between us. This remarkable visual intimacy it completely transforming a cold phone call into a warm conversation."),
    ("What is the most annoying aspect of modern communication?", "The most profoundly irritating aspect of modern communication it definitely being the societal expectation of instantaneous availability. When a colleague they angrily demanding an immediate response to a late-night email, it completely violating the sacred boundary of personal relaxation time. This relentless, 'always-on' corporate culture it inevitably generating massive amounts of unnecessary psychological stress."),
    ("Do you think physical letters will completely disappear?", "Despite the overwhelming convenience of electronic mail, I strongly doubting that traditional, physical letters they completely disappearing in the near future. The meticulous effort required to handwrite a beautiful romantic letter it communicating a profound level of genuine emotional sincerity. A sterile digital text message it simply lacking that irreplaceable, deeply sentimental human touch.")
]
for q, t in c1_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v7_g6_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 7, "grammar": 6, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR7] Good range of less common vocabulary ('sporadically', 'asynchronous nature', 'psychological buffer'). Paraphrasing is effective.",
        "grammar_reason": "[GRA6] Uses a mix of simple and complex sentence forms. Noticeable and systematic errors in basic structures ('I sporadically updating', 'concept... it making').",
        "micro_flaws": ["systematic missing auxiliary: 'I updating', 'it making'", "double subjects: 'friends they'"],
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"},
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Good range of less common vocabulary used with some flexibility and style awareness.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Mix of simple and complex structures, but with frequent, noticeable errors that do not impede meaning."
    })
    start_id += 1

# V8 / G7 (City and Environment)
c2_t = [
    ("What are the most significant advantages of residing in a metropolis?", "The most compelling advantage of residing within a bustling metropolis is the unparalleled access to a wildly diverse array of cultural institutions. Whether one desires to attend an avant-garde theatrical performance or sample incredibly authentic, obscure international cuisine, the urban landscape provides an absolute abundance of sophisticated options. This dynamic, cosmopolitan atmosphere is intellectually invigorating."),
    ("How does severe traffic congestion affect the quality of urban life?", "Severe, unrelenting traffic congestion significantly degrades the overall quality of urban life by inducing chronic psychological stress and massive economic inefficiency. Commuters frequently waste countless hours trapped in completely stationary vehicles, inhaling noxious, detrimental exhaust fumes. If municipal governments fail to aggressively expand sustainable public transit options, this suffocating paralysis will inevitably worsen."),
    ("Do you believe your city has adequate green spaces?", "Unfortunately, I believe my city suffers from a catastrophic deficiency of accessible, well-maintained public green spaces. The relentless, aggressive expansion of highly lucrative commercial real estate frequently necessitates the tragic demolition of our few remaining historic parks. We desperately require a comprehensive urban regeneration strategy that prioritizing the psychological necessity of natural environments."),
    ("What is the primary cause of air pollution in your hometown?", "The primary culprit responsible for the alarming air pollution in my hometown is undoubtedly the heavy concentration of outdated, incredibly inefficient industrial manufacturing plants. These unregulated factories continuously discharge massive quantities of toxic particulate matter into the fragile atmosphere, completely disregarding the severe respiratory consequences for the surrounding vulnerable residential communities."),
    ("How has the architecture of your city evolved over the last decade?", "Over the past decade, the architectural profile of my city has undergone a remarkably aggressive, somewhat controversial transformation. The charming, historical low-rise neighborhoods are being systematically eradicated and swiftly replaced by monolithic, incredibly sterile glass-and-steel skyscrapers. While this vertical expansion accommodates a surging population, it tragically obliterates our unique, irreplaceable civic heritage."),
    ("Is noise pollution a significant issue in your neighborhood?", "Noise pollution constitutes an incredibly pervasive, infuriating issue within my densely populated residential neighborhood. The unrelenting cacophony of blaring car horns, disruptive construction machinery, and late-night sirens makes achieving uninterrupted, restorative sleep virtually impossible. Implementing remarkably stricter municipal noise ordinances is absolutely paramount for protecting the fundamental mental health of the exhausted local residents."),
    ("What measures could the government take to encourage recycling?", "To significantly bolster recycling participation, the government must urgently implement a highly robust, financially incentivized deposit-return scheme for common packaging materials. If consumers actively received a tangible monetary reward for responsibly returning their plastic bottles, the current abysmal recycling rates would undoubtedly skyrocket. Relying solely on passive educational campaigns has proven remarkably ineffective historically."),
    ("Do you prefer the tranquil countryside or the vibrant city?", "I consistently gravitate toward the invigorating, relentless energy of the vibrant city despite its obvious logistical flaws. The tranquil countryside, while undeniably picturesque and peaceful for a brief weekend retreat, ultimately lacks the intense intellectual stimulation and professional networking opportunities I currently require. The profound isolation of rural life simply does not suit my ambitious personality."),
    ("How do massive shopping malls impact independent local businesses?", "The aggressive proliferation of massive, suburban shopping malls frequently exerts a devastating, predatory impact on independent local businesses. Because the colossal retail conglomerates can effortlessly leverage economies of scale to offer significantly lower prices, the charming, family-owned boutiques struggle desperately to remain financially viable. It represents a tragic, perhaps irreversible, homogenization of the traditional retail landscape."),
    ("What do you think your city will look like in fifty years?", "I envision that in fifty years, my city will be forced to undergo a radical, comprehensive ecological adaptation to survive severe climate change. We will likely witness the widespread integration of advanced vertical farming structures and massive, elevated pedestrian walkways completely replacing traditional congested roadways. The absolute necessity for environmental resilience will dictate all future architectural innovation.")
]
for q, t in c2_t:
    wc = len(t.split())
    # minor grammar slips for G7: 'strategy that prioritizing', 'factories continuously discharges'
    t = t.replace("factories continuously discharge", "factories continuously discharges")
    samples.append({
        "sample_id": f"syn_p1_v8_g7_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 8, "grammar": 7, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR8] Wide range of sophisticated vocabulary ('monolithic', 'unrelenting cacophony', 'homogenization'). Meaning is precise and flexible.",
        "grammar_reason": "[GRA7] Frequently produces error-free sentences. Minor slips in agreement/tense ('strategy that prioritizing', 'factories continuously discharges') cap the score at 7.",
        "micro_flaws": ["agreement slip: 'factories... discharges'"],
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"},
        "output": "## Vocabulary (Lexical Resource): Band 8\n\n**Reasoning:** [LR8] Wide vocabulary range used readily and flexibly to convey precise meaning.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Frequently produces error-free sentences and uses a range of complex structures, but occasional slips cap the score."
    })
    start_id += 1

# V4 / G4 (Friends and Family)
c3_t = [
    ("Do you have a large family?", "Yes, my family it is very big. I having three loud brothers and two small sisters. We all living together in one small house. Sometimes it being very noisy when the children they playing the games. But I loving my family very much because we always helping each other."),
    ("Who are you closest to in your family?", "I being closest to my older brother. He always teaching me how to fix the broken computer. When I feeling sad about the difficult school, he buying me the sweet ice cream. We talking about many things every night before we sleeping in our shared bedroom."),
    ("How often do you see your friends?", "I seeing my good friends maybe two times every week. Because we studying at the different universities, we not having much free time. When we meeting on Sunday, we usually walking in the green park and drinking the hot coffee. It making me feel very happy and relaxed."),
    ("Do you prefer spending time with family or friends?", "I liking to spend time with my friends more. When I am with my strict parents, they always asking me about the boring homework. But my friends they just wanting to talk about the funny movies and play sports. It being much more fun and easy for me."),
    ("What do you usually do with your family on weekends?", "On the weekend, my whole family we driving to the big supermarket together. My mother she buying the fresh meat and green vegetables for the whole week. After that, we eating the lunch at the small noodle restaurant. It is a very simple but nice tradition for us."),
    ("Is it easy to make friends in your city?", "No, I thinking it is very difficult to making new friends here. The people in the big city they walking very fast and never looking at you. Everyone they always looking down at their smart phone. You must joining a special club if you wanting to meet nice people."),
    ("Do you have any childhood friends?", "Yes, I still talking to my best friend from the primary school. We knowing each other for fifteen years already. Even though he moving to a different city for his job, we still calling on the phone every month. We remembering the funny old stories from our childhood."),
    ("What is the best thing about your best friend?", "The best thing about my friend it is that he is very funny. When I crying or feeling angry, he always telling a silly joke to make me smile. He never getting angry at me when I making a bad mistake. He being a very kind and good person."),
    ("Do you often visit your grandparents?", "I visiting my old grandparents in the country village every summer holiday. Their house it is very quiet and peaceful, far away from the noisy cars. My grandmother she always cooking the traditional sweet cake for me. I really loving to sit in their beautiful green garden."),
    ("How do people in your country celebrate family events?", "In my country, the big family they always having a massive dinner party for a birthday. We cooking many heavy dishes and sitting around the round table. The children they singing the happy songs loudly. It being a very warm and loud celebration that continuing late into the dark night.")
]
for q, t in c3_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v4_g4_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 4, "grammar": 4, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR4] Uses basic vocabulary exclusively ('big family', 'loud brothers', 'boring homework'). Cannot paraphrase effectively.",
        "grammar_reason": "[GRA4] Frequent and systematic errors in basic structures ('I having', 'family it is', 'they just wanting'). Only basic sentence forms are recognizable.",
        "micro_flaws": ["systematic missing copula/auxiliary: 'I having', 'it being'", "double subjects: 'friends they'"],
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Uses basic vocabulary exclusively. Cannot paraphrase effectively.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Frequent and systematic errors in basic structures. Only basic sentence forms are recognizable."
    })
    start_id += 1

# V5 / G5 (Food and Cooking Basics)
c4_t = [
    ("What is your favorite food?", "My favorite food is the hot chicken pizza. I really love the melted cheese and the spicy tomato sauce on top. Whenever I feel hungry after a long day at the university, I order a large pizza for my dinner. It is very delicious and makes me feel completely satisfied."),
    ("Do you know how to cook?", "I only know how to cook very simple things like boiling eggs or making the hot instant noodles. Because my mother always cooked for me when I was young, I never learned how to make the difficult traditional dishes. I really need to practice more in the kitchen soon."),
    ("Do you prefer eating at home or at a restaurant?", "I prefer eating at a small restaurant because it is much more convenient for me. Cooking the dinner takes a very long time, and then you have to wash all the dirty plates afterwards. In the restaurant, you just sit down, eat the nice food, and then go home to sleep."),
    ("What is the most popular food in your country?", "The most popular food in my country is definitely the white rice with fried fish. People eat it almost every single day for their lunch and dinner. It is a very cheap meal, but it gives the hard workers a lot of necessary energy to finish their difficult jobs."),
    ("Do you eat a lot of fruit?", "Yes, I try to eat a lot of fresh fruit every morning. I usually buy sweet bananas and green apples from the local market because they are very healthy. Eating fruit stops me from buying the bad chocolate candy when I feel hungry in the late afternoon."),
    ("What kind of food did you like when you were a child?", "When I was a child, I only liked eating the sweet strawberry ice cream and the salty fried potatoes. I completely hated all the green vegetables because they tasted very bitter to me. My parents were always angry because I refused to eat my healthy dinner properly."),
    ("Do you think breakfast is important?", "I think eating a big breakfast is the most important part of the whole day. If you go to school with an empty stomach, your brain will feel very slow and tired. Drinking hot milk and eating bread gives you the strong energy to concentrate on the difficult lessons."),
    ("Have you ever tried cooking for your friends?", "Yes, I tried to cook a simple pasta dinner for my close friends last month. Unfortunately, I put too much salt in the hot water, so the food tasted incredibly terrible. My friends laughed very loud, and we eventually had to order a fast pizza from the internet instead."),
    ("Do you like trying new kinds of food?", "I am actually quite scared of trying the strange new foods from foreign countries. I strongly prefer eating the normal local dishes that I already know are very safe and delicious. Once I tried a very spicy Indian curry, and my stomach hurt very badly for the next two days."),
    ("What do you usually drink with your meals?", "I usually just drink a big glass of cold water when I am eating my dinner. Sometimes, if the weather is very hot, I might drink some sweet orange juice with ice. I completely avoid drinking the dark soda because my dentist told me it destroys the white teeth.")
]
for q, t in c4_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v5_g5_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 5, "grammar": 5, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR5] Vocabulary is adequate but relies on basic, everyday terms ('hot chicken pizza', 'dirty plates', 'bad chocolate candy').",
        "grammar_reason": "[GRA5] Produces basic sentences accurately. Attempts complex sentences ('Because my mother always cooked...', 'If you go to school...') with some success, though lacks overall flexibility.",
        "micro_flaws": ["repetitive simple structures"],
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Vocabulary is adequate but relies on basic, everyday terms.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Produces basic sentences accurately. Attempts complex sentences with some success but limited flexibility."
    })
    start_id += 1

# V6 / G6 (Travel Basics)
c5_t = [
    ("Do you like traveling?", "Yes, I really enjoy traveling to new places whenever I have the opportunity. Exploring a completely different city and trying their unique local food is a very exciting experience for me. It provides a wonderful, necessary break from my normal, boring routine at the office."),
    ("What is the most beautiful place you have ever visited?", "The most beautiful place I have visited is a large, quiet lake situated deep in the mountains. The water was incredibly clear and blue, perfectly reflecting the tall pine trees around it. Sitting on the peaceful shore there made me feel completely relaxed and very close to nature."),
    ("Do you prefer traveling by train or by plane?", "I definitely prefer traveling by train because it is a much more relaxing experience overall. When you are on a train, you have plenty of space to stretch your legs and watch the beautiful countryside passing by the large window. Flying is usually too cramped and stressful for me."),
    ("Who do you usually travel with?", "I usually travel with my older sister because we share very similar interests and budgets. We both enjoy visiting historic museums and walking slowly through the old city streets. Traveling with someone who understands your personal travel style makes the entire holiday much more enjoyable and entirely stress-free."),
    ("What do you always take with you when you travel?", "I always make absolutely sure to pack my digital camera and a very comfortable pair of walking shoes. Because I plan to explore the city on foot all day, hurting my feet would completely ruin the exciting trip. The camera is essential for capturing all the beautiful memories."),
    ("Do you prefer visiting cities or the countryside?", "While I appreciate the quiet nature, I strongly prefer visiting vibrant, busy cities during my holidays. I love the intense energy of walking through a crowded night market and seeing massive, historic buildings. The countryside is beautiful, but I usually get a bit bored after just two quiet days."),
    ("Have you ever traveled to a foreign country?", "Yes, last summer I traveled to France for a short two-week holiday with my university friends. It was a fantastic experience to finally see the famous Eiffel Tower in person. Although I could not speak the language, the local people were surprisingly friendly and helped us find our hotel."),
    ("What is the worst part of traveling?", "The absolute worst part of traveling is definitely the exhausting process of packing and unpacking the heavy suitcase. Furthermore, waiting in the incredibly long security lines at the crowded airport makes me feel very anxious and annoyed. I wish the transportation part of the holiday was much faster."),
    ("Do you like to buy souvenirs when you travel?", "I occasionally buy small, cheap souvenirs like a colorful magnet or a simple postcard to remember the nice trip. However, I actively try to avoid buying large, expensive items because I don't have enough space in my small apartment. The photographs I take are usually the best memories."),
    ("Where would you like to travel in the future?", "I would absolutely love to travel to Japan sometime in the near future. I have always been deeply fascinated by their unique culture and the beautiful cherry blossom trees in the spring. Experiencing their traditional tea ceremony in a historic garden is my biggest travel dream right now.")
]
for q, t in c5_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v6_g6_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 6, "grammar": 6, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR6] Uses an adequate range of vocabulary with some less common items ('situated', 'vibrant', 'fascinated'). Meaning is clear.",
        "grammar_reason": "[GRA6] Uses a mix of simple and complex sentence forms. Grammatical control is good, with only minor errors. Nothing significantly impedes communication.",
        "micro_flaws": ["none significant, slightly functional vocabulary"],
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"},
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Uses an adequate range of vocabulary with some less common items successfully.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Mix of simple and complex structures, with noticeable but non-impeding errors."
    })
    start_id += 1

with open(filename, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
print(f"Batch {batch_num} written natively.")
