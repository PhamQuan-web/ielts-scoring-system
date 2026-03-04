import json

batch_num = 66
filename = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p1_07.jsonl"
start_id = 301
samples = []

# Batch 66: V7/G7(10) V8/G8(10) V9/G9(10) V4/G5(10) V5/G4(10) | IDs: 0301–0350

# V7 / G7 (Reading and Writing)
c1_t = [
    ("Do you prefer writing emails or sending text messages?", "I typically prefer sending quick text messages for casual, immediate communication with my close friends. However, when I am addressing a professional colleague, I invariably choose to write a carefully structured email. Maintaining an appropriate level of professional formality is incredibly important in the corporate world."),
    ("What kind of things do you usually write during the day?", "Throughout the workday, I primarily write detailed analytical reports and comprehensive project summaries for my demanding manager. Once I finally return home, I occasionally write personal reflections in my private journal. This quiet journaling practice serves as an excellent method for organizing my scattered thoughts."),
    ("Did you enjoy writing essays when you were at school?", "I actually thoroughly enjoyed crafting long academic essays during my university years. The rigorous process of researching a complex historical topic and constructing a persuasive argument was highly intellectually stimulating. Although it frequently required many exhausting hours in the library, I always felt a profound sense of academic accomplishment."),
    ("Is your handwriting easy for other people to read?", "Unfortunately, my natural handwriting is notoriously messy and quite difficult for most people to decipher accurately. Because I became so entirely reliant on typing quickly on a computer keyboard, I rarely practice forming elegant physical letters anymore. My university professors frequently complained about my incredibly chaotic exam papers."),
    ("Do you think handwriting will become obsolete in the future?", "While digital typing has undeniably become the dominant method of modern communication, I doubt handwriting will become entirely obsolete. There is a deeply personal, intimate quality to receiving a handwritten birthday card that a cold digital message simply cannot replicate. It will likely survive as a specialized artistic craft."),
    ("What type of books do you enjoy reading the most?", "I consistently gravitate towards gripping psychological thrillers because the unpredictable plot twists keep me entirely captivated. The complex character development within these suspenseful narratives is usually far more intriguing than a simple, straightforward action story. Reading them provides a fantastic, thrilling escape from my ordinary, predictable daily routine."),
    ("Where is your favorite place to sit and read?", "My absolute favorite location for reading is the quiet, sunlit corner of my local independent bookshop. The subtle aroma of fresh coffee and the complete absence of loud digital distractions create an incredibly relaxing atmosphere. I can easily spend an entire Sunday afternoon there, completely absorbed in a fascinating novel."),
    ("Do you ever read the news on a physical newspaper?", "I honestly cannot remember the last time I purchased a physical, printed newspaper. Navigating through the massive, cumbersome pages on a crowded morning train is incredibly frustrating and inconvenient. I strongly prefer quickly scrolling through customized digital news feeds on my lightweight mobile phone during my daily commute."),
    ("How do you encourage young children to read more?", "To effectively encourage young children to read, parents must proactively surround them with beautifully illustrated, highly engaging storybooks from a very early age. Furthermore, if children consistently observe their own parents enjoying a physical book instead of constantly staring at a television, they will naturally mimic that positive intellectual behavior."),
    ("Have you ever tried reading a book in a foreign language?", "I recently attempted to read a contemporary Spanish novel to deliberately challenge my current linguistic proficiency. Although the sophisticated vocabulary initially proved quite frustrating, successfully comprehending the subtle cultural nuances without relying on a dictionary was incredibly rewarding. It is a fantastic strategy for achieving genuine language fluency.")
]
for q, t in c1_t:
    wc = len(t.split())
    # minor grammar slip for G7: 'parents must proactively surrounds', 'I typically prefers' -> no that's too much. Let's do 'I occasionally writes', 'if children consistently observes'
    t = t.replace("I occasionally write", "I occasionally writes")
    t = t.replace("children consistently observe", "children consistently observes")
    samples.append({
        "sample_id": f"syn_p1_v7_g7_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 7, "grammar": 7, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR7] Good range of less common vocabulary ('comprehensive', 'decipher', 'captivated', 'proficiency'). Paraphrasing is effective.",
        "grammar_reason": "[GRA7] Frequently produces error-free complex sentences. Minor slips in agreement ('I occasionally writes', 'children consistently observes') keep it at a 7.",
        "micro_flaws": ["agreement slip: 'I occasionally writes'", "agreement slip: 'children consistently observes'"],
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"},
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Good range of less common vocabulary used with flexibility and precision.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Produces frequent error-free complex sentences, but occasional minor slips occur."
    })
    start_id += 1

# V8 / G8 (Sports and Health)
c2_t = [
    ("How important is it to maintain a balanced diet?", "Maintaining a meticulously balanced nutritional intake is absolutely paramount for sustaining long-term cognitive and physiological vitality. Whenever I inadvertently consume excessive quantities of heavily processed foods, I immediately experience a profound, detrimental crash in my afternoon energy levels. A wholesome diet undeniably functions as the fundamental cornerstone of proactive preventive healthcare."),
    ("Do you prefer exercising outdoors or inside a gym?", "I consistently gravitate toward the invigorating experience of exercising outdoors, specifically trail running through the nearby dense forest. The incredibly dynamic, uneven terrain provides a far more comprehensive physical challenge than a monotonous, predictable treadmill. Furthermore, inhaling the pristine, unpolluted air is immensely therapeutic for alleviating my accumulated corporate stress."),
    ("What was your favorite physical activity as a child?", "During my formative years, I was exceptionally passionate about participating in highly competitive amateur gymnastics. The grueling, disciplined training routines demanded an extraordinary degree of absolute physical flexibility and unwavering mental concentration. That rigorous early experience instilled a profound sense of resilient personal discipline that continues to benefit my professional life today."),
    ("How do you manage stress during a difficult week?", "To effectively mitigate the severe psychological pressure of a demanding work week, I rely heavily on the rigorous practice of mindfulness meditation. By deliberately isolating myself in a quiet room and focusing exclusively on my rhythmic breathing, I can successfully detach from my chaotic professional anxieties. This vital mental reset is incredibly restorative."),
    ("Do you think professional athletes deserve their massive salaries?", "While the sheer astronomical magnitude of their compensation often seems ethically disproportionate, one must acknowledge the incredibly short, highly precarious nature of their professional careers. Elite athletes subject their bodies to devastating, irreversible physical trauma for our fleeting entertainment. Consequently, their immense financial rewards essentially compensate for the immense, permanent physiological risks they willingly endure."),
    ("Have you ever suffered a sports-related injury?", "Unfortunately, I completely ruptured a crucial ligament in my left knee during a particularly aggressive amateur basketball match last winter. The subsequent surgical intervention and agonizingly slow, frustrating months of intensive physical rehabilitation were profoundly demoralizing. It served as a stark, painful reminder to always prioritize comprehensive warm-up stretches before engaging in explosive athletic movements."),
    ("How can cities encourage residents to be more physically active?", "Municipal governments could effectively encourage widespread physical activity by strategically investing in the massive expansion of dedicated, secure cycling infrastructure. If urban planners successfully prioritize the absolute safety of vulnerable cyclists over the overwhelming convenience of aggressive motorists, ordinary citizens would feel significantly more confident utilizing a bicycle for their daily metropolitan commute."),
    ("Do you enjoy watching international sporting competitions?", "I find watching premier international tournaments, such as the Olympic Games, to be incredibly compelling and profoundly unifying. Witnessing diverse athletes from historically antagonistic nations competing with absolute mutual respect and flawless sportsmanship is remarkably inspiring. These magnificent global spectacles temporarily transcend our bitter, petty geopolitical divisions through the universal language of physical excellence."),
    ("What are the potential drawbacks of extreme sports?", "The primary drawback of participating in extreme, adrenaline-fueled sports is the undeniable, ever-present risk of sustaining a catastrophic, life-altering physical injury. While the intense psychological rush of successfully skydiving is undoubtedly exhilarating, a single, momentary equipment failure can instantly result in absolute tragedy. Participants must rigorously weigh that immense psychological thrill against the severe existential danger."),
    ("Do you think traditional sports are losing popularity?", "I suspect that many traditional, slow-paced sports are gradually losing their historical dominance, particularly among the incredibly distracted younger generation. Because adolescents are constantly overstimulated by rapid, instant-gratification digital entertainment, they frequently lack the requisite patience to endure a five-day cricket match. Consequently, high-intensity, condensed athletic formats are rapidly surging in global popularity." )
]
for q, t in c2_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v8_g8_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 8, "grammar": 8, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR8] Wide range of sophisticated vocabulary ('physiological vitality', 'invigorating', 'existential danger'). Meaning is precise and flexible.",
        "grammar_reason": "[GRA8] Wide range of structures used flexibly and accurately ('Whenever I inadvertently consume', 'By deliberately isolating myself'). The majority of sentences are error-free.",
        "micro_flaws": ["none significant"],
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"},
        "output": "## Vocabulary (Lexical Resource): Band 8\n\n**Reasoning:** [LR8] Wide vocabulary range used readily and flexibly to convey precise meaning.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 8\n\n**Reasoning:** [GRA8] Wide range of structures used flexibly and accurately. The majority of sentences are error-free."
    })
    start_id += 1

# V9 / G9 (Art, Culture, Philosophy)
c3_t = [
    ("How does contemporary art reflect the anxieties of modern society?", "Contemporary art frequently serves as a remarkably poignant, visceral mirror reflecting the pervasive existential anxieties that plague our hyper-connected, yet profoundly isolated modern society. Many avant-garde installations deliberately utilize chaotic, fragmented visual motifs to eloquently critique the overwhelming sensory overload of the digital age. It represents a desperate, necessary search for genuine authenticity amidst synthetic commercialism."),
    ("Why is the preservation of intangible cultural heritage essential?", "Safeguarding our intangible cultural heritage, such as obscure oral traditions or ancestral musical forms, is absolutely essential for preserving the unique cognitive frameworks of diverse human populations. When an ancient, localized dialect inevitably slips into total obsolescence, we irretrievably lose a fundamentally unique philosophical perspective on the natural world. It constitutes an immeasurable intellectual tragedy for humanity."),
    ("Do you believe that exposure to foreign cultures increases empathy?", "I unequivocally believe that prolonged, authentic immersion in fundamentally foreign cultural paradigms is the most potent catalyst for developing profound human empathy. By directly navigating the bewildering nuances of an unfamiliar society, one is inherently forced to ruthlessly dismantle their own deeply ingrained, ethnocentric biases. This challenging intellectual friction ultimately yields a far more tolerant, cosmopolitan worldview."),
    ("How has the concept of privacy evolved in the digital era?", "The fundamental concept of personal privacy has undergone a radical, rather alarming devolution in our current era of ubiquitous digital surveillance. We have ostensibly traded our most intimate, confidential data for the superficial convenience of incredibly invasive social networking platforms. Tragically, this constant, voluntary self-exposure has completely normalized a pervasive culture of unabashed corporate and governmental voyeurism."),
    ("What role does architecture play in shaping urban psychology?", "The overarching aesthetic philosophy dictating our built environment exerts an undeniably profound, subconscious influence on the aggregate psychology of the urban populace. Monolithic, brutalist concrete structures frequently engender an atmosphere of severe civic alienation and creeping despair among the marginalized residents. Conversely, the strategic integration of biophilic design principles naturally fosters a highly reassuring sense of communal tranquility."),
    ("Why do historical museums remain relevant in the age of the internet?", "Despite the instantaneous availability of infinite digital information, physical historical museums remain profoundly relevant because they offer a uniquely visceral, tangible connection to our collective ancestral past. Standing inches away from a meticulously preserved, millennia-old artifact provokes a deeply resonant, emotional comprehension of human history that a sterile, illuminated computer screen simply cannot adequately replicate."),
    ("How does the relentless pursuit of economic growth affect environmental ethics?", "The current global paradigm's relentless, myopic fixation on infinite, exponential economic growth stands in absolute, fundamental opposition to basic environmental ethics. By systemically prioritizing immediate, lucrative corporate profits over the crucial necessity of long-term ecological sustainability, we are recklessly plundering the Earth's finite resources. This avaricious philosophy guarantees an utterly catastrophic environmental inheritance for all subsequent generations."),
    ("Do you prefer engaging in superficial small talk or deep philosophical discussions?", "I harbor an intense, almost visceral aversion to the agonizing superficiality of mundane small talk, strongly preferring to engage in deep, rigorous philosophical discourse. Exploring complex ethical dilemmas or debating the multifaceted nuances of global political theory is incredibly intellectually stimulating. I find that superficial pleasantries merely serve as an exhausting, necessary precursor to genuine, meaningful communication."),
    ("What constitutes a truly meaningful human life in your opinion?", "In my philosophical estimation, a truly meaningful existence is predicated not upon the relentless, exhausting accumulation of transient material wealth, but rather upon the cultivation of profound, empathetic interpersonal relationships. Furthermore, dedicating one's fleeting time to a purposeful, altruistic endeavor that tangibly alleviates the suffering of marginalized communities provides a lasting, deeply resonant sense of genuine fulfillment."),
    ("How does literature help us navigate complex moral dilemmas?", "Sophisticated literary fiction is unparalleled in its remarkable capacity to help us safely navigate the incredibly treacherous landscape of complex moral dilemmas. By intimately placing the reader within the subjective, conflicted psychological reality of a deeply flawed protagonist, literature brilliantly forces us to critically examine our own rigid ethical boundaries. It cultivates a crucial, deeply necessary intellectual humility.")
]
for q, t in c3_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v9_g9_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 9, "grammar": 9, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR9] Exceptional, highly precise, and sophisticated vocabulary ('visceral mirror', 'obsolescence', 'ethnocentric biases'). Idiomatic language is natural and accurate.",
        "grammar_reason": "[GRA9] Flawless grammar with full flexibility. Uses advanced structures naturally and accurately.",
        "micro_flaws": ["none in grammar", "none in vocabulary"],
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"},
        "output": "## Vocabulary (Lexical Resource): Band 9\n\n**Reasoning:** [LR9] Uses vocabulary with full flexibility and precision in all topics.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 9\n\n**Reasoning:** [GRA9] Full mastery of complex structures. Flawless accuracy and natural flexibility."
    })
    start_id += 1

# V4 / G5 (Work and Study Basics)
c4_t = [
    ("Where do you usually study for your exams?", "I usually study in my small bedroom because it is very quiet. If I go to the big university library, I will talk with my friends and forget to read the books. I have a clean desk near the window, which helps me to see the paper clearly in the morning."),
    ("Do you like the subject you are studying?", "Yes, I really like my business subject very much. The teacher is very kind and he helps me when I have a difficult problem. Although the mathematics part is very hard for my brain, I think learning about money is very useful for my future job in the big city."),
    ("Is your university very far from your home?", "My university is quite far from my family home. I need to take the fast yellow bus for forty minutes every day. If the bad traffic is very heavy in the morning, I will be late for my important class. I wish I lived closer to the school gates."),
    ("Do you prefer to study alone or with other students?", "I prefer to study alone in my quiet room. When I try to study with a big group of students, they always make too much noise and laughing. Because I cannot focus on my difficult books, I must sit by myself to get the good grades from the strict teacher."),
    ("What do you usually do after your classes finish?", "After my classes finish, I usually walk to the small coffee shop near the school. I drink a hot sweet tea and eat a cheap sandwich because I feel very hungry. Then I take the bus home and sleep on my soft bed for one hour before dinner."),
    ("Do you use a computer for your studies?", "Yes, I use my old laptop computer every single day. I must type my long English essays on the keyboard and send them to the teacher on the internet. Because my handwriting is very messy and ugly, the computer makes my important work look much more clean and beautiful."),
    ("Have you ever failed an important exam?", "Yes, I failed a very difficult science exam last year. Because I played too many video games on my phone, I didn't read the heavy textbook enough. My parents were very angry with me. Now, I try to study much harder so I will never see a bad red mark again."),
    ("What is the most difficult part of your studies?", "The most difficult part is remembering all the strange English words for my vocabulary test. I write the new words on small pieces of paper and look at them every night. Even though I try very hard, my brain quickly forgets the long spelling the next morning in the classroom."),
    ("Do you want to get a job in another country?", "Yes, my biggest dream is to find a good job in a rich foreign country. I want to earn a lot of green money to send back to my poor family. If I can speak English perfectly, maybe a big international company will give me a nice office desk there."),
    ("How do you prepare for a big presentation?", "When I have a big presentation, I practice speaking in front of my bedroom mirror many times. I write the simple words on a small card so I don't forget my story. If I don't practice my loud voice, my hands will shake and I will feel very scared in class.")
]
for q, t in c4_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v4_g5_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 4, "grammar": 5, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR4] Uses only basic vocabulary ('small bedroom', 'big group', 'messy and ugly'). Very limited range. Cannot paraphrase.",
        "grammar_reason": "[GRA5] Produces basic sentences accurately ('I usually study in my small bedroom'). Attempts complex sentences ('If I go to the big university library...', 'Because I played too many video games...') with reasonable success, though lacking flexibility.",
        "micro_flaws": ["repetitive simple sentence structures"],
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Uses basic vocabulary exclusively. Cannot paraphrase effectively.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Produces basic sentences accurately. Attempts complex sentences with some success but limited flexibility."
    })
    start_id += 1

# V5 / G4 (Home and Living Basics)
c5_t = [
    ("What does the outside of your house look like?", "My house it looking very simple and old. It having the white walls and a small red roof. In the front, my father he planting many yellow flowers in the dirt. Because the street it is very narrow, we not having a big garage for the heavy car."),
    ("Is your neighborhood very noisy at night?", "Yes, my neighborhood it being extremely noisy when the dark night comes. The wild dogs they barking loudly at the moon outside my thin window. Also, the young boys they driving their fast motorbikes down the street very quickly. It making my sleep very bad and tired."),
    ("What is your favorite furniture in your living room?", "My favorite furniture it is the big brown sofa in the middle of the room. It being very soft and comfortable for my tired back. When I finishing my dinner, I always sitting there to watch the funny television. My lovely cat she also sleeping on the sofa with me."),
    ("Who usually cleans the house in your family?", "My mother she usually doing all the difficult cleaning in our big house. Every Sunday morning, she sweeping the dirty floor and washing the windows with the wet cloth. I sometimes helping her to wash the small dishes after we eating the lunch. But I being very lazy usually."),
    ("Do you prefer living in a high apartment or a low house?", "I preferring to live in the low house on the ground. Because I having a terrible fear of the high places, looking out the tall apartment window it making me feel very sick and dizzy. In the low house, I can walking straight into the green garden easily."),
    ("Is there a good park near your home?", "Yes, there being a very nice green park just five minutes from my front door. It having a small blue lake and many tall trees for the shadow. On the weekend, many happy families they going there to play with the plastic ball and eat the sweet ice cream."),
    ("Have you ever painted the walls of your room?", "I trying to paint my bedroom walls blue last summer with my best friend. But we making a very big, terrible mess on the brown carpet. The wet paint it dripping everywhere and my hands they becoming completely blue. My angry father he having to finish the difficult job for us."),
    ("Do you like having guests visit your home?", "I really liking when my good friends they coming to visit my house. We sitting in my warm bedroom and playing the loud music on the computer. My mother she always bringing us the fresh fruit and cold water. It making the quiet house feel very happy and alive."),
    ("What do you see when you look out your bedroom window?", "When I opening my window, I seeing a very tall, gray office building across the busy street. I cannot seeing the beautiful sky or the green trees because the big concrete building it blocking everything. I wishing I could seeing the peaceful ocean instead of the ugly city cars."),
    ("Will you stay in this house for a long time?", "I not thinking I will stay in this old house forever. When I finishing the university and getting a good job, I wanting to buy a modern apartment in the busy center. Because this old house it needing too many expensive repairs, the roof it always leaking the rain water.")
]
for q, t in c5_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v5_g4_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 5, "grammar": 4, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR5] Vocabulary is adequate but relies on simple, everyday terms ('white walls', 'brown sofa', 'wet paint').",
        "grammar_reason": "[GRA4] Frequent and systematic errors in basic structures ('My house it looking', 'It having', 'mother she usually doing'). Relies heavily on using present participles without the auxiliary 'to be' and double subjects.",
        "micro_flaws": ["systematic missing copula/auxiliary: 'it looking', 'she sweeping'", "frequent double subjects: 'house it', 'mother she'"],
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Vocabulary is adequate but relies on basic, everyday terms.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Frequent and systematic errors in basic structures. Only basic sentence forms are recognizable."
    })
    start_id += 1

with open(filename, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
print(f"Batch {batch_num} written natively.")
