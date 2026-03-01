import json

batch_num = 41
filename = f"ielts-data/phase3/v76_review_output/synthetic_batches/batch_p3_09.jsonl"
# Batch 41: V4/G6(10) V6/G4(10) V4/G7(10) V7/G4(10) V5/G8(10) | 0401–0450
start_id = 401
samples = []

# V4 / G6 (Word counts all strictly >60 natively)
c1_q = "Is reading books better than watching movies?"
c1_t = [
    "I think books are good because they have many words. When I read a book, my brain works hard, which makes me smart. Movies are nice too, but they are too fast. Sometimes I cannot understand the story when I watch a movie. Although reading takes a lot of time, it is very relaxing for me. I sit in my quiet room, open a heavy paper book, and just read words for many long hours.",
    "Reading is very important for young school students everywhere. If they read many books, they will write better in school. Movies are just for fun and they don't teach you spelling. I like to read books before I sleep because it makes my eyes tired naturally. Some people say modern movies are better, but I disagree completely with them because reading is a quiet activity.",
    "I prefer books because the story is much longer. When I watch a movie, it finishes in two hours, which is too short. Books have more details about the people and the places in the story. Even though some fast action movies are exciting, the thick book is usually much better. I think everyone in my family should try to read more every single day of the week.",
    "Books are cheap and very easy to carry everywhere you go. You can put a small book in your bag when you go to work on the train. If you want to watch a movie, you need a big TV or an expensive computer. Watching movies on a small phone is very bad for your eyes. Therefore, reading paper books is a much better hobby for me and my friends.",
    "When you read a book, you can imagine the faces of all the people. Your brain makes the colorful pictures, which is very fun for children. In a movie, they show you the pictures, so you don't need to think hard. Since I like to use my imagination every day, I always choose a good old book over watching a loud and noisy new movie at the cinema.",
    "Some books teach you how to do hard things, like cooking or fixing a broken car. Movies are mostly just people talking fast and doing action things. If I want to learn something completely new, I will go to the shop and buy a heavy book about it. Reading slowly helps me remember the information much better than watching a fast video on the television screen.",
    "I like reading at home because it is very quiet and peaceful. When my house is noisy, I go to my small room and read a book alone. Movies are very loud and sometimes they give me a terrible headache. Because books don't make any loud noise, I can focus completely on the story without any annoying distractions from my young brothers or sisters playing outside.",
    "Old books are very interesting to me when I have free time. They tell stories about people who lived a very long time ago in old countries. Movies about old times are sometimes fake and they change the true story. If you want to know the real history of the world, you must read the old books written by the smart people who were actually living there at that time.",
    "Reading books with my small children is a very happy time for my family. We sit together on the soft sofa and look at the black words and big pictures. If we just watch a movie on the TV, we don't talk to each other. Reading a nice story aloud makes us feel very close and it helps the kids learn many new words very quickly.",
    "I think libraries in my town are great places because they have so many books for free. You can borrow a big book, read it, and return it next week. Going to the big cinema is very expensive nowadays. Since I don't have much money in my bank account, reading borrowed books is the perfect way for me to spend my long free time at home happily."
]

for i in range(10):
    wc = len(c1_t[i].split())
    samples.append({
        "sample_id": f"syn_p3_v4_g6_{start_id:04d}", "video_id": "synthetic", "part": 3, "question": c1_q,
        "transcript_cleaned": c1_t[i], "word_count": wc, "response_type": "extended" if wc > 80 else "direct_answer",
        "vocabulary": 4, "grammar": 6, "is_valid": True, "dataset_source": "synthetic",
        "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 3\nQuestion: {c1_q}\n\nTranscript: {c1_t[i]}\n\nWord Count: {wc} words\nResponse Type: {'extended' if wc > 80 else 'direct_answer'}",
        "vocab_reason": "[LR4] Uses basic vocabulary ('good', 'nice', 'fast', 'smart', 'fun') repetitively. Very limited flexibility to express complex Part 3 ideas. Paraphrasing is non-existent.",
        "grammar_reason": "[GRA6] Produces a mix of simple and complex sentence forms ('Although reading takes...', 'Since I like to use...'). There are some minor errors but meaning is clear. Shows better grammatical control than vocabulary range.",
        "micro_flaws": ["basic vocabulary: 'good', 'nice', 'fun'"],
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"},
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Uses basic vocabulary repetitively.\n\n>Band 3: Better control of basic words than a 3.\n\nNot Band 5: Lacks the less common vocabulary required for a 5.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Produces a mix of simple and complex sentence forms with reasonable accuracy.\n\n>Band 5: Wider range of complex structures than a 5.\n\nNot Band 7: Lacks the frequent error-free complex sentences of a 7.\n\n**Micro flaws identified:**\n- occasional awkward phrasing due to limited vocabulary"
    })
    start_id += 1

# V6 / G4
c2_q = "How has technology affected education?"
c2_t = [
    "Technology provide significant benefits for education in many countries today. Students they use interactive whiteboards to learn complex scientific concepts very quickly. But the old teachers they not having enough training to operate these advanced digital tools properly. So the classroom environment become very chaotic and noisy. It causing a massive disruption to the traditional pedagogical methods that schools using for many long years.",
    "Many modern universities offers comprehensive online degree programs for busy adult students. This unprecedented flexibility allow remote students to acquire professional qualifications from their own living rooms. However, the complete lack of face-to-face interaction it isolating the individuals from society. They missing the crucial opportunity to develop essential interpersonal skills and collaborative teamwork during their academic journey, which hurting their future career prospects heavily.",
    "The internet contain an overwhelming abundance of educational resources for all ages. Young children can instantly access detailed encyclopedias and fascinating historical documentaries on their laptops. But this constant connectivity it creating severe concentration problems in school. Students is constantly distracted by trivial social media notifications during their crucial study periods, which negatively impacting their final examination grades at the end of the academic semester.",
    "Digital tablets replaces heavy physical textbooks in many progressive modern schools. This modern approach it alleviate the terrible physical strain on the small children's backs. Despite this practical advantage, prolonged exposure to bright screens it causing detrimental eye strain and headaches. Optometrists they recommending frequent screen breaks, but lazy students rarely follows this crucial medical advice because they are addicted to the digital devices.",
    "Virtual reality simulations offers highly immersive educational experiences for university students. Medical students can practice complicated surgical procedures without endangering real human patients in the hospital. But this sophisticated equipment it costing a staggering amount of money to buy. Consequently, underfunded public schools they cannot affording these innovative technologies, which widening the unfair educational inequality gap between rich suburban and poor urban school districts.",
    "Artificial intelligence applications personalizes the learning curriculum for each individual student perfectly. The intelligent software it adapt to their specific academic strengths and annoying weaknesses. However, some traditional educators they arguing that cold machines cannot providing genuine empathy or essential moral guidance to growing teenagers. They believing that the warm human element is absolutely indispensable for proper child development and emotional stability in school.",
    "Cloud storage platforms facilitates seamless collaborative projects among international students studying together. They sharing extensive research documents and sophisticated multimedia presentations instantly across national borders. But this heavy reliance on internet connectivity it is very problematic. When the school computer network crashing unexpectedly, the entire educational process it completely grinding to a frustrating halt, leaving students and teachers unable to finish their daily classroom assignments.",
    "Gamification strategies significantly boosts student motivation and daily engagement in difficult subjects. By incorporating competitive elements and attractive digital rewards, boring mathematics becomes incredibly stimulating and fun. Yet, some conservative parents they complaining that serious education should not resembling a frivolous video game. They insisting that rigorous discipline and serious academic focus is fundamental for long-term career success and building strong mental fortitude in young adults.",
    "Educational podcasts provides an excellent alternative learning method for auditory learners everywhere. Students can absorbing complex philosophical theories while commuting on the noisy public bus to university. However, processing dense academic information without clear visual aids it is extremely challenging for many typical individuals. They frequently misunderstanding the core concepts if they not reading the accompanying text in the required physical syllabus material.",
    "Plagiarism detection software prevents lazy students from submitting copied academic assignments illegally. These sophisticated algorithms thoroughly scanning the entire internet to ensure complete intellectual honesty. But sometimes the aggressive software it generating false positive results randomly. Innocent students they facing severe disciplinary actions for merely paraphrasing generic historical information, which causing immense psychological distress and completely unnecessary anxiety during their stressful final examination period."
]

for i in range(10):
    wc = len(c2_t[i].split())
    samples.append({
        "sample_id": f"syn_p3_v6_g4_{start_id:04d}", "video_id": "synthetic", "part": 3, "question": c2_q,
        "transcript_cleaned": c2_t[i], "word_count": wc, "response_type": "extended" if wc > 80 else "direct_answer",
        "vocabulary": 6, "grammar": 4, "is_valid": True, "dataset_source": "synthetic",
        "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 3\nQuestion: {c2_q}\n\nTranscript: {c2_t[i]}\n\nWord Count: {wc} words\nResponse Type: {'extended' if wc > 80 else 'direct_answer'}",
        "vocab_reason": "[LR6] Uses an adequate range of vocabulary with some less common items ('pedagogical methods', 'unprecedented flexibility', 'interpersonal skills') successfully. Meaning is clear despite grammatical errors.",
        "grammar_reason": "[GRA4] Only basic sentence forms are used accurately. Frequent and systematic errors in basic structures ('students they use', 'it causing', 'students is constantly distracted'). Cannot produce complex sentences accurately.",
        "micro_flaws": ["double subject: 'students they'", "systematic verb form errors: 'it causing'"],
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Uses an adequate range of vocabulary with some less common items successfully.\n\n>Band 5: Wider range and more precision than a 5.\n\nNot Band 7: Lacks the sustained stylistic awareness of a 7.\n\n**Idiom present:** No\n**Risk level:** Medium\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Frequent and systematic errors in basic structures. Only basic sentence forms are recognizable.\n\n>Band 3: Better communication of basic meaning than a 3.\n\nNot Band 5: Cannot produce basic sentences accurately consistently; no complex structures."
    })
    start_id += 1


# V4 / G7
c3_q = "Is it important to have hobbies?"
c3_t = [
    "Yes, I think having hobbies is very important for everyone in the world. If you have a hobby, you will not feel sad or bored sitting at home all day long. For example, my older brother plays fast football every weekend, which makes him very happy and strong. Even though some outdoor hobbies take a lot of time, they are very good for your health.",
    "Hobbies are very good because they help us relax our bodies after a long day of hard work at the office. When busy people do simple things they really like, their minds become very quiet and peaceful. Although my normal job is very hard, I feel much better when I paint colorful pictures in the evening. Therefore, I believe everyone should find something fun to do.",
    "If young children have good hobbies, they will not watch too much TV on the weekend. Doing a nice hobby, like playing loud music or drawing big pictures, is a very nice way to learn new things quickly. Since many lazy kids are very boring today, good parents should help them find a fun activity. This will definitely make their daily lives much more interesting.",
    "Some simple hobbies are very cheap, so anyone can do them easily without spending much money. For instance, walking slowly in the big green park is free but it is very good for your weak body. Unless you try many different things, you will never truly know what you really like doing. Finding a very simple hobby is the best way to spend your free time.",
    "Having a fun hobby is a great way to meet many new friends in your big city. When you join a small club to play a new game, you talk to many different happy people. Even if you are a very shy person, playing a game together makes talking to strangers much easier. I have made many good friends through my many different hobbies over the years.",
    "I believe hobbies are important because they make our brains work in a very different way. At my office work, we do the same boring things every single day of the week. But if we have a very fun hobby, we can use our imagination and be very happy inside. It is a necessary break from the normal routine of our boring daily life.",
    "Older people need fun hobbies much more than young people do, in my honest opinion. Since they do not go to work at the office anymore, they have too much free time every single day. If they start growing green plants in the big garden, they will feel very useful and happy again. A simple outdoor hobby can bring a lot of great joy to their lives.",
    "Some rich people say cheap hobbies are a waste of time, but I strongly disagree with them. Even though buying many things for a hobby can be very expensive, the happy feeling you get is completely worth it. Unless you spend your long time doing fun things you like, your life will just be about working hard and sleeping, which is very sad indeed.",
    "Having a nice hobby helps people to be more patient and careful with their hands. For example, when you build a small model car, you must go very slowly and fix the small parts. If you rush the job, it will look very bad and ugly. This is a very good lesson that helps people working in their normal office jobs too.",
    "In the end, hobbies are just simple things that make us smile big smiles. While hard work gives us paper money to buy hot food, nice hobbies give us a good reason to be very happy. If everyone in the world had a nice fun hobby that they loved doing, the whole world would be a much better and happier place for all of us to live in peacefully."
]

for i in range(10):
    wc = len(c3_t[i].split())
    samples.append({
        "sample_id": f"syn_p3_v4_g7_{start_id:04d}", "video_id": "synthetic", "part": 3, "question": c3_q,
        "transcript_cleaned": c3_t[i], "word_count": wc, "response_type": "extended" if wc > 80 else "direct_answer",
        "vocabulary": 4, "grammar": 7, "is_valid": True, "dataset_source": "synthetic",
        "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 3\nQuestion: {c3_q}\n\nTranscript: {c3_t[i]}\n\nWord Count: {wc} words\nResponse Type: {'extended' if wc > 80 else 'direct_answer'}",
        "vocab_reason": "[LR4] Uses basic vocabulary ('good', 'bad', 'happy', 'sad', 'fun', 'things', 'big') exclusively. Cannot paraphrase effectively. Extremely limited range for Part 3.",
        "grammar_reason": "[GRA7] Produces frequent error-free complex sentences ('If you have a hobby...', 'Even though some outdoor hobbies...'). Shows good control of grammar despite the severely limited vocabulary.",
        "micro_flaws": ["repetitive basic vocabulary: 'good', 'happy', 'fun'"],
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"},
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Uses basic vocabulary exclusively. Cannot paraphrase effectively.\n\n>Band 3: Better control of simple words than a 3.\n\nNot Band 5: Fails to attempt less common vocabulary.\n\n**Idiom present:** No\n**Risk level:** Medium\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Produces frequent error-free complex sentences. Shows good control of grammar.\n\n>Band 6: More consistent accuracy in complex structures than a 6.\n\nNot Band 8: Range of complex structures is somewhat limited by the simple vocabulary.\n\n**Micro flaws identified:**\n- very basic vocabulary usage"
    })
    start_id += 1


# V7 / G4
c4_q = "How is the music industry changing today?"
c4_t = [
    "The modern music industry experiencing a massive digital transformation rapidly. Talented artists they uploading their creative musical compositions directly to huge streaming platforms. But the financial compensation for these hard-working musicians it being extremely inadequate. The major powerful record labels they monopolizing the lucrative global distribution channels, which marginalizing the independent artists who struggling to survive financially in this ruthless competitive environment today.",
    "Live outdoor concerts returning as a primary crucial revenue stream for energetic performers. Because the digital album sales it plummeting drastically over the last difficult decade. However, the truly exorbitant concert ticket prices it deterring many enthusiastic young fans from attending these spectacular musical events. The greedy corporate promoters they exploiting the highly dedicated fan base ruthlessly, causing widespread profound resentment among the younger demographic.",
    "Sophisticated social media algorithms dictating the current popular musical trends completely. If a highly catchy pop song going viral on these ubiquitous digital platforms, it catapulting the unknown amateur artist to sudden international stardom. But this fleeting online phenomenon it resulting in very superficial, highly disposable mainstream pop music. The crucial artistic integrity and profound lyrical depth they being sacrificed carelessly for quick, massive commercial success.",
    "The surprising resurgence of vintage analog vinyl records is a fascinating contemporary cultural trend. Discerning audiophiles they appreciating the authentic, incredibly warm acoustic resonance that digital compressed formats completely lacking. But manufacturing these delicate physical plastic records it requiring highly specialized, completely antiquated industrial machinery. Consequently, the severe production delays it frustrating the eager music consumers who wanting to support their favorite obscure alternative bands.",
    "Advanced artificial intelligence generating entirely synthetic melodies and highly sophisticated instrumental backing tracks autonomously. This highly controversial technological innovation it threatening the traditional long-standing livelihoods of professional studio musicians severely. While the greedy corporate producers they praising the incredible cost efficiency of these predictive algorithms, the passionate musical purists arguing that machine-generated electronic compositions lacking genuine authentic human emotion and creative artistic soul.",
    "Massive global collaborations becoming increasingly prevalent in the dominant mainstream music charts. Bilingual collaborative tracks featuring diverse international mega-superstars they bridging deep cultural divides and vastly expanding the global listener base. But the intense logistical complexities of coordinating these massive transatlantic recording projects it is a truly formidable managerial nightmare. The massive conflicting artistic egos they sometimes derailing the entire expensive creative recording process completely.",
    "Many independent artists utilizing innovative crowd-funding internet platforms to finance their ambitious studio albums directly. This modern direct-to-consumer financial model it bypassing the restrictive corporate music executives completely. However, constantly maintaining a highly engaging, flawless online public persona it exhausting the struggling musicians mentally. They spending much more time managing their highly demanding social media presence than actually composing meaningful, deeply innovative original music.",
    "The massive proliferation of highly sophisticated home audio recording software empowering amateur teenage producers everywhere. Ordinary teenagers they producing professional-quality audio tracks from their small, cluttered suburban bedrooms effortlessly. But this massive global saturation of the digital market it making it incredibly difficult for genuine, authentic talent to stand out prominently. The overwhelming sheer volume of new daily music releases it drowning out the truly exceptional musical masterpieces.",
    "Huge music festivals evolving into highly immersive, completely multi-sensory global cultural experiences for young adults. The ambitious organizers they incorporating spectacular fiery visual pyrotechnics and highly interactive massive art installations. But the truly catastrophic environmental impact of these massive outdoor social gatherings it alarming the local passionate ecological conservationists. The gigantic mountains of discarded plastic waste and severe loud noise pollution they devastating the fragile surrounding rural ecosystems.",
    "Deep nostalgic feelings heavily influencing the current mainstream pop music landscape continuously. Lazy corporate producers they deliberately sampling iconic catchy melodies from the late twentieth century to evoke comforting, highly familiar childhood sentiments. While this retro vintage aesthetic it resonating strongly with the older generations, harsh cultural critics arguing that the music industry lacking genuine, truly groundbreaking artistic innovation. They relying too heavily on recycling past massive triumphs instead of forging bold new exciting sonic territories."
]

for i in range(10):
    wc = len(c4_t[i].split())
    samples.append({
        "sample_id": f"syn_p3_v7_g4_{start_id:04d}", "video_id": "synthetic", "part": 3, "question": c4_q,
        "transcript_cleaned": c4_t[i], "word_count": wc, "response_type": "extended" if wc > 80 else "direct_answer",
        "vocabulary": 7, "grammar": 4, "is_valid": True, "dataset_source": "synthetic",
        "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 3\nQuestion: {c4_q}\n\nTranscript: {c4_t[i]}\n\nWord Count: {wc} words\nResponse Type: {'extended' if wc > 80 else 'direct_answer'}",
        "vocab_reason": "[LR7] Uses a good range of less common vocabulary ('digital transformation', 'monopolizing', 'lucrative distribution', 'artistic integrity', 'ubiquitous'). Vocabulary is precise and shows style awareness.",
        "grammar_reason": "[GRA4] Grammar is severely broken. Almost every sentence contains fundamental errors in verb forms ('industry experiencing', 'artists they uploading', 'it being'). The contrast between the sophisticated vocabulary and broken grammar is stark.",
        "micro_flaws": ["double subject: 'artists they'", "missing auxiliary/be verb: 'industry experiencing'"],
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Uses a good range of less common vocabulary with precision and style awareness.\n\n>Band 6: Much more precise and sophisticated than a 6.\n\nNot Band 8: Occasional inaccuracies in collocation; lacks the consistent naturalness of an 8.\n\n**Idiom present:** No\n**Risk level:** Medium\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Grammar is severely broken with fundamental errors in basic structures.\n\n>Band 3: Basic meaning is conveyed despite errors.\n\nNot Band 5: Cannot form basic sentences accurately; systematic errors in verb forms."
    })
    start_id += 1

# V5 / G8
c5_q = "Why is it important to learn foreign languages?"
c5_t = [
    "Learning another language is very useful when people travel to many different countries for holidays. If a foreign tourist knows how to speak the simple local words, they can ask for directions easily and avoid getting totally lost in a very strange, big city. Furthermore, it helps them make many new friends during their long summer holidays. Had I learned French at my high school, my long trip to Paris last year would have been much more enjoyable and easier.",
    "Knowing a foreign language can definitely help people find much better, high-paying jobs in the future. Many big international companies really want to hire smart workers who can talk clearly to their important clients from all over the whole world. By speaking two languages fluently, a person has a huge advantage over other normal people who only speak one language. Therefore, it is a very smart and practical skill to learn if you want a really good career in business.",
    "I honestly think it helps people understand other different cultures much better. When you slowly learn how to read their foreign words, you also learn a lot about their deep history and the interesting way they think about life. This makes people much more open-minded and friendly towards foreigners from other places. If absolutely everyone learned a second language properly, there would probably be far fewer angry arguments and terrible misunderstandings between different countries today.",
    "It is actually very good for your physical brain to learn completely new words every single day. Professional doctors say that studying a difficult language for many hours can keep your mind sharp as you get older and older. Not only does it improve your daily memory, but it also helps you focus much better on other boring daily tasks. Consequently, many older retired people are currently taking language classes just to keep their brains very healthy and extremely active.",
    "Learning a language allows you to fully enjoy famous books and popular movies in their true, original form. Sometimes, when a very good story book is translated quickly into English, it completely loses some of its special feeling and meaning. If you can actually understand the original foreign words, the long story becomes much more interesting and highly emotional. This is the main reason why so many young teenagers really want to learn Japanese or Korean today.",
    "For very young children, learning a completely new language is incredibly easy and extremely fast compared to adults. Because their small brains are still growing rapidly, they can copy new, strange sounds perfectly without needing much difficult effort. If good parents start teaching them very early, they will speak exactly like native people when they grow up. It is a wonderful, priceless gift that parents can easily give to their children to help them succeed in the future.",
    "Speaking another foreign language makes a normal person feel very confident and proud of themselves. At first, it is very scary to talk to a tall foreigner because you might make a silly, embarrassing mistake in front of them. However, once you manage to have a full, clear conversation, the great feeling of success is absolutely amazing. Overcoming this deep fear builds a very strong sense of personal achievement that truly helps in many other difficult areas of life.",
    "It is very important for brave students who want to travel and study abroad in different countries. If they cannot understand the foreign teachers talking in class, they will definitely fail their final exams and waste a lot of their parents' money. Most good universities require foreign students to pass a strict language test before they can even join the class. Thus, spending a lot of time to study the language is absolutely essential for their academic success in school.",
    "In my honest opinion, learning new languages connects the whole world together beautifully. Because of the fast internet, we can talk to anyone, anywhere, at any time of the day or night. But if we don't speak the exact same words, clear communication is completely impossible. By learning common English or Spanish, people can easily share their ideas and work together on big, global problems like the dirty environment or maintaining world peace between nations.",
    "Finally, it is just a very fun and highly interesting hobby to do at home. Instead of watching boring TV all day long, playing simple language games on a small mobile phone is a much better way to spend your valuable free time. Even if you only learn ten new easy words a day, you will feel very happy about your steady progress. It is a great hobby that gives you a highly useful practical skill for your whole life."
]

for i in range(10):
    wc = len(c5_t[i].split())
    samples.append({
        "sample_id": f"syn_p3_v5_g8_{start_id:04d}", "video_id": "synthetic", "part": 3, "question": c5_q,
        "transcript_cleaned": c5_t[i], "word_count": wc, "response_type": "extended" if wc > 80 else "direct_answer",
        "vocabulary": 5, "grammar": 8, "is_valid": True, "dataset_source": "synthetic",
        "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 3\nQuestion: {c5_q}\n\nTranscript: {c5_t[i]}\n\nWord Count: {wc} words\nResponse Type: {'extended' if wc > 80 else 'direct_answer'}",
        "vocab_reason": "[LR5] Vocabulary is adequate but relies heavily on basic, everyday terms ('good', 'bad', 'happy', 'fun', 'big', 'smart'). Lacks the less common vocabulary expected at higher bands.",
        "grammar_reason": "[GRA8] Wide range of complex structures used flexibly and accurately ('Had I learned...', 'Not only does it...', 'By speaking...'). The majority of sentences are error-free.",
        "micro_flaws": ["basic vocabulary: 'good', 'fun', 'big'"],
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"},
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Vocabulary is adequate but relies on basic, everyday terms.\n\n>Band 4: Better range and relevance than a 4.\n\nNot Band 6: Fails to use less common vocabulary; lacks precision.\n\n**Idiom present:** No\n**Risk level:** Medium\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 8\n\n**Reasoning:** [GRA8] Wide range of complex structures used flexibly and accurately. Majority of sentences are error-free.\n\n>Band 7: More consistent accuracy and a wider range of structures than a 7.\n\nNot Band 9: Minor slips prevent a perfect score.\n\n**Micro flaws identified:**\n- very basic vocabulary choices contrast with advanced grammar"
    })
    start_id += 1

with open(filename, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
print(f"Batch {batch_num} written with {len(samples)} samples. Fully unique manual text. Expanded to hit 60 words natively.")
