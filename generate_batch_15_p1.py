import json
import os

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_15.jsonl"

# Samples 701-725 (V7/G7: 10, V8/G8: 10, V9/G9: 5)
samples = [
    # --- V7/G7 (701-710) ---
    {
        "sample_id": "syn_p2_v7_g7_0701",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book you loved as a child.",
        "transcript_cleaned": "I vividly remember reading 'Charlotte's Web' when I was a child, and it remains one of my favorite books. It is a heartwarming story about a pig named Wilbur and his unlikely friendship with a spider named Charlotte. The narrative explores deep themes of loyalty, mortality, and the cycle of life, which I found fascinating even at a young age. I was captivated by the anthropomorphic characters and their emotional depth. Charlotte, the spider, uses her web-spinning skills to save Wilbur from slaughter, displaying incredible intelligence and kindness. Her actions left a lasting impression on me about the power of friendship. The ending is bittersweet, as Charlotte passes away, but it teaches valuable lessons about sacrifice and continuity. It is a classic of children's literature that remains relevant today, and I still have my original copy on my bookshelf.",
        "word_count": 142,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] Flexible use of 'vividly remember', 'unlikely friendship', 'narrative', 'mortality', 'anthropomorphic'.",
        "grammar_reason": "[GRA7] Frequent error-free complex sentences. 'When I was a child' (Time), 'Which I found fascinating' (Relative).",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0702",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a city you would like to live in for a short time.",
        "transcript_cleaned": "I would love to live in Edinburgh for a few months because it seems like such a magical place. It is a city steeped in history, with a dramatic skyline dominated by an ancient castle that sits atop a volcanic rock. I am drawn to its Gothic architecture and the charming cobblestone streets of the Old Town. The city hosts the world's largest arts festival, the Edinburgh Fringe, which creates a vibrant atmosphere every summer. I imagine myself exploring the hidden closes and spending time in literary pubs where famous writers once sat. The combination of cultural richness and stunning scenery is very appealing to me. Although I have heard the weather can be gloomy, the warmth of the Scottish people makes up for it. It would be an inspiring environment.",
        "word_count": 141,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Steeped in history', 'dramatic skyline', 'dominated', 'Gothic architecture', 'vibrant atmosphere'.",
        "grammar_reason": "[GRA7] Complex structures: 'that sits atop' (Relative), 'which creates' (Relative), 'Although I have heard' (Concessive).",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0703",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party you organized.",
        "transcript_cleaned": "I organized a farewell party for a colleague who was moving abroad last year. It was a bittersweet occasion, mixed with joy for her new adventure and sadness that she was leaving. I booked a private room at a cozy restaurant and decorated it with photos and messages from the whole team. The planning required attention to detail, from selecting the menu to curating the music playlist. I wanted to create a memorable send-off for her. We shared funny anecdotes and toasted to her future success in her new job. Seeing her emotional reaction made all the effort worthwhile. It was a meaningful way to show our appreciation for her friendship and hard work, and everyone had a wonderful time celebrating together.",
        "word_count": 133,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Farewell party', 'bittersweet', 'curating', 'anecdotes', 'memorable send-off'.",
        "grammar_reason": "[GRA7] 'Who was moving' (Relative), 'sadness that she was leaving' (Noun clause), 'from selecting... to curating' (Parallel).",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0704",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a teacher who had a strong impact on you.",
        "transcript_cleaned": "I would like to talk about Mrs. Thompson, my high school art teacher, who truly changed my perspective on creativity. She was an eccentric and inspiring figure who always encouraged us to think outside the box. Unlike other teachers, she prioritized individual expression over strict rules, which allowed us to experiment. She introduced us to various artistic movements, from Impressionism to Surrealism, and explained the history behind them. I was fascinated by her passion for art history and her ability to engage the class. She taught me to see the world from different perspectives. Her constructive criticism helped me refine my skills and build confidence in my own abilities. Because of her influence, I decided to pursue a degree in graphic design.",
        "word_count": 133,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Eccentric', 'prioritized', 'individual expression', 'artistic movements', 'constructive criticism'.",
        "grammar_reason": "[GRA7] 'Who truly changed' (Relative), 'Unlike other teachers' (Contrast), 'Because of her influence' (Reason).",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0705",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of technology you couldn't live without.",
        "transcript_cleaned": "I could not live without my laptop, which is an essential tool for both my professional work and my leisure time. It is a sleek, high-performance machine that allows me to multitask efficiently throughout the day. I rely on it for drafting reports, attending virtual meetings, and managing my finances online. The portability means I can work from anywhere, whether at a cafe or on a train, which gives me great freedom. I also use it to stream movies and edit photos when I have free time. It stores all my important documents and cherished memories. Without it, I would feel disconnected and unproductive. It is the hub of my digital life, and I honestly don't know how I would manage without it.",
        "word_count": 136,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Essential tool', 'high-performance', 'multitask', 'virtual meetings', 'portability', 'hub'.",
        "grammar_reason": "[GRA7] 'Which is an essential tool' (Relative), 'whether at a cafe or' (Correlative), 'Without it, I would feel' (Conditional).",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0706",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe an exercise you do regularly.",
        "transcript_cleaned": "I regularly practice kickboxing to maintain my physical fitness and mental well-being. It is a high-intensity workout that combines martial arts techniques with fast-paced cardio. I attend classes at a local gym three times a week, where we practice in groups. The routine involves punching, kicking, and various defensive moves that require focus and agility. It is an excellent way to relieve stress and release aggression after a long day at work. I find it empowering to learn self-defense skills while getting fit. After each session, I feel exhausted but invigorated. It has improved my stamina and coordination significantly over the last few months. It is a challenging activity that keeps me motivated to stay healthy.",
        "word_count": 128,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'High-intensity', 'martial arts', 'cardio', 'defensive moves', 'relieve stress', 'invigorated'.",
        "grammar_reason": "[GRA7] 'That combines' (Relative), 'Where we practice' (Relative adverb), 'While getting fit' (Reduction).",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0707",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a biography you read.",
        "transcript_cleaned": "I read a fascinating biography of Albert Einstein, the renowned physicist, which left a strong impression on me. It detailed his early life, his struggles in school, and his groundbreaking scientific discoveries that changed the world. I was intrigued by his unconventional approach to problem-solving and his rebellious nature. The book explained his theory of relativity in a way that was accessible to laypeople, which I appreciated. It also delved into his personal life and humanitarian work, showing a different side of him. Reading about his persistence in the face of skepticism was inspiring. It gave me a deeper appreciation for his contributions to humanity. He was truly a genius who changed our understanding of the universe forever.",
        "word_count": 128,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Renowned physicist', 'groundbreaking', 'unconventional', 'laypeople', 'humanitarian', 'skepticism'.",
        "grammar_reason": "[GRA7] 'Which left a strong impression' (Relative), 'That changed the world' (Relative), 'Reading about... was' (Gerund subject).",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0708",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a place near water you like.",
        "transcript_cleaned": "I love visiting a serene lake located in the national park near my hometown. The water is pristine, reflecting the surrounding pine trees like a mirror on a calm day. I often go there to kayak or simply sit on the wooden dock to read a book. The tranquility of the place is a welcome respite from the noise of the city. I enjoy watching the wildlife, such as ducks and herons that live along the banks. In the autumn, the changing leaves create a spectacular display of colors that reflects in the water. It is a perfect spot for meditation and reflection. Being near the water always calms my mind and helps me recharge.",
        "word_count": 127,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Serene lake', 'pristine', 'tranquility', 'respite', 'spectacular display', 'meditation'.",
        "grammar_reason": "[GRA7] 'Located in the national park' (Participle), 'Reflecting the surrounding...' (Participle), 'That live along' (Relative).",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0709",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of work you did with others.",
        "transcript_cleaned": "I collaborated with two classmates on a science presentation last month about environmental issues. Our task was to explain the effects of global warming on marine life. We divided the work equally to ensure efficiency and fairness. I was responsible for researching the data and creating the visual slides. We met frequently to discuss our progress and rehearse our parts. It was challenging to coordinate our schedules, but we managed to find time. Working in a team taught me the value of compromise and clear communication. Our presentation was well-received by the teacher and the class, which made us very proud. I felt a sense of accomplishment knowing we had worked hard together to achieve a good result.",
        "word_count": 128,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Collaborated', 'ensure efficiency', 'coordinate schedules', 'compromise', 'well-received'.",
        "grammar_reason": "[GRA7] 'To explain the effects' (Infinitive), 'Responsible for researching' (Adj+Prep+Gerund), 'Knowing we had worked' (Participle).",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0710",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe an antique you like.",
        "transcript_cleaned": "I am fond of an antique vase that sits in our hallway and has been in our family for years. It is a porcelain vase from the Ming Dynasty, painted with delicate blue patterns that tell a story. My parents bought it at an auction because they loved its history. It has a graceful shape and a glossy finish that catches the light. I admire the artistry and skill required to create such an object without modern tools. It adds a touch of elegance to our home decor. We are very careful with it because it is fragile and valuable. It serves as a conversation starter when guests visit, as everyone is always drawn to its beauty.",
        "word_count": 128,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Fond of', 'porcelain', 'delicate patterns', 'artistry', 'elegance', 'conversation starter'.",
        "grammar_reason": "[GRA7] 'That sits in our hallway' (Relative), 'Painted with...' (Participle), 'Required to create' (Participle).",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    # --- V8/G8 (711-720) ---
    {
        "sample_id": "syn_p2_v8_g8_0711",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition you entered.",
        "transcript_cleaned": "I once entered a regional debating competition, which proved to be an incredibly stimulating experience. The topic was regarding the ethical implications of artificial intelligence, a subject I find particularly compelling. I spent weeks meticulously researching arguments and counter-arguments to ensure I was fully prepared. The atmosphere on the day was palpable with tension, as teams from various schools had gathered to compete. Although I felt a degree of apprehension, once I started speaking, the adrenaline kicked in. My team managed to articulate our points with clarity and conviction, ultimately securing second place. What I valued most was not the accolade, but the opportunity to hone my rhetoric and public speaking skills under pressure. It was a pivotal moment that boosted my confidence significantly.",
        "word_count": 129,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Stimulating experience', 'ethical implications', 'compelling', 'meticulously researching', 'palpable', 'apprehension', 'articulate', 'accolade', 'hone my rhetoric'.",
        "grammar_reason": "[GRA8] 'Which proved to be' (Relative), 'Regarding the ethical implications' (Participle), 'As teams... had gathered' (Reason + Past Perfect).",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0712",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you lost something.",
        "transcript_cleaned": "I remember a distressing incident when I misplaced my passport just hours before an international flight. I had been packing hurriedly and, in my chaotic state, I must have left it on the kitchen counter. The realization hit me when I arrived at the terminal, causing a wave of panic to wash over me. I frantically retraced my steps mentally, trying to deduce where it could be. Fortunately, my brother was still at home and was able to locate it and rush it to the airport. It was a nail-biting finish, but he arrived just as the check-in counters were closing. The experience served as a salutary lesson in the importance of being organized and checking essentials before departure.",
        "word_count": 128,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Distressing incident', 'misplaced', 'chaotic state', 'realization hit me', 'frantically retraced', 'deduce', 'nail-biting finish', 'salutary lesson'.",
        "grammar_reason": "[GRA8] 'Just hours before' (Time), 'Must have left' (Modal of deduction), 'Trying to deduce' (Participle phrase), 'Where it could be' (Embedded question).",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0713",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a creative person.",
        "transcript_cleaned": "My friend Julian is arguably the most creative individual I know. He is a graphic designer by trade, but his artistic flair extends far beyond his professional work. He has an uncanny ability to visualize concepts that others find abstract. For instance, he repurposes discarded materials into stunning sculptures, transforming what most would consider junk into art. His mind seems to operate on a different wavelength, constantly generating innovative ideas. I often find myself in awe of his ingenuity and his refusal to adhere to conventional norms. He inspires me to think more laterally and to appreciate the aesthetic potential in everyday objects. His creativity is not just a skill but a fundamental part of his identity.",
        "word_count": 126,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Arguably', 'artistic flair', 'uncanny ability', 'visualize concepts', 'repurposes', 'stunning sculptures', 'ingenuity', 'adhere to conventional norms', 'laterally'.",
        "grammar_reason": "[GRA8] 'By trade, but...' (Contrast), 'Transforming what most would consider' (Participle + Noun clause), 'Refusal to adhere' (Noun phrase), 'Not just... but' (Correlative).",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0714",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "One of the most arduous decisions I have had to make was choosing between two university offers. One was from a prestigious institution far from home, and the other was a local college with a scholarship. I was torn between the allure of a top-tier education and the financial security of staying nearby. I spent days weighing the pros and cons, seeking counsel from mentors and family. The dilemma caused me considerable anxiety, as I feared making the wrong choice. Ultimately, I opted for the distant university, believing it would foster greater personal growth. Looking back, I am convinced it was the correct trajectory, as it forced me to become independent and resilient.",
        "word_count": 124,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Arduous decisions', 'prestigious institution', 'torn between', 'allure', 'top-tier', 'weighing the pros and cons', 'seeking counsel', 'opted for', 'trajectory'.",
        "grammar_reason": "[GRA8] 'One of the most...' (Superlative), 'Choosing between' (Gerund), 'Believing it would foster' (Participle + Future in past), 'Forced me to become' (Causative).",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0715",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a noisy place.",
        "transcript_cleaned": "The central market in my city is undoubtedly one of the most cacophonous places imaginable. It is a sprawling labyrinth of stalls where vendors shout to advertise their wares. The auditory assault is constant, with the clattering of carts, the honking of delivery trucks, and the chatter of thousands of shoppers merging into a deafening roar. While some find this sensory overload overwhelming, I actually find it quite invigorating. There is a palpable energy there that reflects the vibrant pulse of the city. However, I can only tolerate it in small doses; after an hour or so, I usually need to retreat to a quieter environment to decompress and restore my equilibrium.",
        "word_count": 123,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Cacophonous', 'sprawling labyrinth', 'auditory assault', 'clattering', 'sensory overload', 'invigorating', 'palpable energy', 'vibrant pulse', 'equilibrium'.",
        "grammar_reason": "[GRA8] 'Undoubtedly one of the most' (Adverbial), 'Where vendors shout' (Relative), 'Merging into a deafening roar' (Participle), 'While some find... I find' (Contrast).",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0716",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a photo you like.",
        "transcript_cleaned": "I cherish a candid photograph taken during a family reunion five years ago. It captures a spontaneous moment where my grandfather is laughing uncontrollably at a joke my cousin told. The composition is far from perfect—it is slightly blurry and the lighting is dim—but the emotion it conveys is authentic and heartwarming. It encapsulates the joy of shared connection that defines our family gatherings. Every time I look at it, I am transported back to that evening on the patio. Since my grandfather passed away, this image has become a poignant reminder of his vibrant spirit. It serves as a testament to the idea that the best photos are often the unplanned ones.",
        "word_count": 124,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Cherish', 'candid photograph', 'spontaneous moment', 'uncontrollably', 'composition', 'conveys', 'authentic', 'encapsulates', 'poignant reminder', 'testament'.",
        "grammar_reason": "[GRA8] 'Taken during...' (Participle), 'Where my grandfather is laughing' (Relative), 'Far from perfect' (Idiomatic adj), 'Since my grandfather passed' (Time), 'Serves as a testament' (Collocation).",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0717",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a rule you agree with.",
        "transcript_cleaned": "I strongly advocate for the regulation banning smoking in public indoor spaces. This policy, implemented a decade ago, has had a transformative effect on public health. I recall how restaurants used to be filled with acrid smoke, which was not only unpleasant but also hazardous to non-smokers. The ban protects staff and patrons from the detrimental effects of second-hand smoke. Although there was initial resistance from some sectors, the consensus now is largely positive. It has created a more hygienic and welcoming atmosphere in social venues. I believe this rule strikes the right balance between individual liberty and collective well-being, prioritizing the health of the majority over the habits of a few.",
        "word_count": 123,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Advocate for', 'regulation', 'transformative effect', 'acrid smoke', 'hazardous', 'detrimental effects', 'consensus', 'hygienic', 'collective well-being'.",
        "grammar_reason": "[GRA8] 'Implemented a decade ago' (Participle), 'Which was not only... but also' (Relative + Correlative), 'Protects... from' (Verb pattern), 'Prioritizing the health' (Participle).",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0718",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a toy you liked as a child.",
        "transcript_cleaned": "As a child, I was inseparable from a complex construction set similar to Lego. It consisted of thousands of interlocking pieces, gears, and motors. While other children preferred action figures, I was fascinated by the mechanics of building structures. I would spend hours meticulously assembling intricate vehicles and robots, often ignoring the instructions to create my own designs. This toy sparked my interest in engineering and honed my spatial awareness. It was not merely a pastime but a tool that fostered creativity and patience. Even now, I look back on those hours of play as foundational to my problem-solving abilities. It taught me that with patience, small pieces can build something magnificent.",
        "word_count": 123,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Inseparable from', 'interlocking pieces', 'mechanics', 'meticulously assembling', 'intricate', 'sparked my interest', 'honed', 'spatial awareness', 'foundational'.",
        "grammar_reason": "[GRA8] 'Similar to Lego' (Adjective phrase), 'While other children preferred' (Contrast), 'Ignoring the instructions' (Participle), 'Not merely... but' (Correlative).",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0719",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a tradition in your country.",
        "transcript_cleaned": "In my country, we have a time-honored tradition of visiting ancestors' graves during the lunar new year. It is a solemn yet uplifting ritual that emphasizes filial piety and remembrance. Families gather to clean the tombstones, offer incense, and present food offerings. It serves as a bridge between the past and the present, reinforcing our lineage. I find it deeply moving to see generations of families united in this act of respect. It grounds us, reminding us of our roots in a fast-paced modern world. While some younger people may view it as archaic, I believe it is integral to preserving our cultural identity and social fabric.",
        "word_count": 120,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Time-honored tradition', 'solemn', 'filial piety', 'remembrance', 'reinforcing our lineage', 'united', 'grounds us', 'archaic', 'integral', 'social fabric'.",
        "grammar_reason": "[GRA8] 'Visiting ancestors' graves' (Gerund phrase), 'Yet uplifting' (Contrast), 'Serves as a bridge' (Metaphorical), 'Reminding us of our roots' (Participle).",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0720",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a website you use often.",
        "transcript_cleaned": "I am a frequent user of a particular educational platform called Coursera. It is an immense repository of online courses offered by top universities worldwide. I utilize it primarily to upskill in areas like data science and psychology. The interface is intuitive, and the content is curated to a very high standard. What I appreciate most is the flexibility it affords; I can learn at my own pace without the constraints of a physical classroom. It has democratized education, making knowledge accessible to anyone with an internet connection. For me, it has been an invaluable resource for continuous professional development, allowing me to remain competitive in the job market.",
        "word_count": 121,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Frequent user', 'immense repository', 'utilize', 'upskill', 'intuitive', 'curated', 'flexibility it affords', 'democratized', 'invaluable resource', 'continuous professional development'.",
        "grammar_reason": "[GRA8] 'Called Coursera' (Participle), 'Offered by top universities' (Participle), 'What I appreciate most is' (Cleft sentence), 'Without the constraints' (Prepositional phrase).",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    # --- V9/G9 (721-725) ---
    {
        "sample_id": "syn_p2_v9_g9_0721",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a famous athlete.",
        "transcript_cleaned": "I have always held Roger Federer in the highest esteem, not merely for his tennis prowess but for his exemplary conduct on and off the court. He is the quintessential sportsman, embodying grace, humility, and resilience. Watching him play is akin to witnessing an artist at work; his movements are fluid and seemingly effortless, disguising the immense physical exertion involved. Throughout his illustrious career, he has maintained a dignity that is rare in the hyper-competitive world of professional sports. Even in defeat, he is gracious, which I believe is the true mark of a champion. His philanthropic endeavors further cement his legacy as a role model. He has transcended the sport to become a global icon of excellence.",
        "word_count": 129,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 9,
        "vocab_reason": "[LR9] 'Highest esteem', 'prowess', 'exemplary conduct', 'quintessential sportsman', 'fluid', 'seemingly effortless', 'illustrious career', 'hyper-competitive', 'philanthropic endeavors', 'transcended'.",
        "grammar_reason": "[GRA9] 'Not merely... but' (Correlative), 'Akin to witnessing' (Idiomatic comparison), 'Disguising the immense...' (Participle), 'That is rare' (Relative). Full control.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g9_0722",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a garden you visited.",
        "transcript_cleaned": "I recall visiting the Kenroku-en Garden in Kanazawa, which is widely celebrated as one of Japan's most exquisite landscape gardens. The aesthetic philosophy behind its design focuses on the six attributes of a perfect garden, including spaciousness and seclusion. Wandering through its winding paths, I was struck by the meticulous attention to detail; every stone and pine tree seemed placed with deliberate intent. The interplay between the artificial water features and the natural vegetation created a harmonious atmosphere that was utterly beguiling. It was the height of cherry blossom season, and the petals falling on the ponds created a scene of ethereal beauty. It felt like stepping into a living painting, a sanctuary of peace.",
        "word_count": 128,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 9,
        "vocab_reason": "[LR9] 'Widely celebrated', 'exquisite landscape', 'aesthetic philosophy', 'seclusion', 'meticulous attention', 'deliberate intent', 'interplay', 'beguiling', 'ethereal beauty'.",
        "grammar_reason": "[GRA9] 'Which is widely celebrated' (Relative), 'Focuses on... including' (Participle), 'I was struck by' (Passive), 'Seemed placed' (Participle). Native-like flow.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g9_0723",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a goal you achieved.",
        "transcript_cleaned": "Completing my first marathon was an objective that required unwavering discipline and grit. For months, I adhered to a grueling training regimen, often waking before dawn to log miles in inclement weather. There were moments of profound doubt when my body ached, and the finish line felt like an impossible dream. However, the mental fortitude I developed was just as significant as the physical conditioning. Crossing that finish line was an indescribable feeling of euphoria and validation. It taught me that our perceived limits are often self-imposed constructs. The experience fundamentally shifted my mindset, proving that consistency and perseverance can surmount almost any obstacle.",
        "word_count": 118,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 9,
        "vocab_reason": "[LR9] 'Unwavering discipline', 'grit', 'grueling training regimen', 'inclement weather', 'profound doubt', 'mental fortitude', 'indescribable feeling', 'euphoria', 'self-imposed constructs', 'surmount'.",
        "grammar_reason": "[GRA9] 'That required...' (Relative), 'Often waking before dawn' (Participle), 'Just as significant as' (Comparative), 'Proving that...' (Participle). Flawless.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g9_0724",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a health problem you had.",
        "transcript_cleaned": "A few years ago, I suffered from a severe bout of insomnia that wreaked havoc on my daily life. It was a debilitating condition where sleep became an elusive adversary rather than a restorative process. The chronic fatigue impaired my cognitive function, making even trivial tasks feel Herculean. I tried every conventional remedy, from meditation to dietary changes, with little success. It was only when I addressed the underlying stress in my professional life that the symptoms began to subside. This episode was a wake-up call, forcing me to re-evaluate my work-life balance. I now prioritize sleep hygiene and mental well-being with a diligence I previously lacked.",
        "word_count": 121,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 9,
        "vocab_reason": "[LR9] 'Severe bout', 'wreaked havoc', 'debilitating condition', 'elusive adversary', 'restorative process', 'impaired', 'cognitive function', 'Herculean', 'subside', 'prioritize sleep hygiene'.",
        "grammar_reason": "[GRA9] 'Where sleep became' (Relative), 'Making even trivial tasks feel' (Causative/Participle), 'It was only when... that' (Cleft), 'With a diligence I previously lacked' (Reduced relative).",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g9_0725",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "The Pantheon in Rome stands as a monumental testament to the ingenuity of ancient Roman engineering. Despite being nearly two thousand years old, it remains the world's largest unreinforced concrete dome, a feat that baffles modern architects. Stepping inside, one is immediately awestruck by the oculus, the central opening that allows a shaft of natural light to illuminate the interior. The symmetry and proportion of the structure evoke a sense of divine harmony. It has served various purposes throughout history, from a pagan temple to a Christian church, ensuring its preservation. To me, it is not merely a relic of the past, but a symbol of endurance and architectural perfection.",
        "word_count": 123,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 9,
        "vocab_reason": "[LR9] 'Monumental testament', 'ingenuity', 'unreinforced concrete', 'baffles', 'awestruck', 'oculus', 'illuminate', 'symmetry', 'evoke', 'divine harmony', 'relic'.",
        "grammar_reason": "[GRA9] 'Stands as' (Idiom), 'Despite being' (Concessive), 'A feat that baffles' (Appositive + Relative), 'Ensuring its preservation' (Participle).",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    }
]

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for sample in samples:
        # Standard fields
        sample["dataset_source"] = "synthetic"
        sample["is_valid"] = True
        sample["idiom_present"] = False
        sample["risk_level"] = "low"
        sample["instruction"] = "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning."

        # Micro flaws (none for high bands)
        sample["micro_flaws"] = []

        # Input/Output construction
        sample["input"] = f"Part: {sample['part']}\nQuestion: {sample['question']}\n\nTranscript: {sample['transcript_cleaned']}\n\nWord Count: {sample['word_count']} words\nResponse Type: {sample['response_type']}"

        output_text = f"## Vocabulary (Lexical Resource): Band {sample['vocabulary']}\n\n**Reasoning:** {sample['vocab_reason']}\n\n>Band {sample['vocabulary']-1}: ...\n\nNot Band {sample['vocabulary']+1}: ...\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band {sample['grammar']}\n\n**Reasoning:** {sample['grammar_reason']}\n\n>Band {sample['grammar']-1}: ...\n\nNot Band {sample['grammar']+1}: ...\n\n**Micro flaws identified:**\n- None."

        sample["output"] = output_text

        f.write(json.dumps(sample) + '\n')
