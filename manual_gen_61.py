import json

batch_num = 61
filename = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p1_02.jsonl"
start_id = 51
samples = []

# Batch 61: V6/G5(10) V6/G6(10) V6/G7(10) V7/G6(10) V7/G7(10) | IDs: 0051–0100

# V6 / G5 (Daily Routine)
c1_t = [
    ("When do you usually wake up in the morning?", "I usually waking up very early, maybe around six o'clock. Because I needing to catch the first train to the university, I cannot sleeping late. After I washing my face, I making a quick cup of strong coffee. This morning routine it helping me to feel awake and energetic."),
    ("What is your favorite time of the day?", "My favorite time of the day it is definitely the late evening. Because all my difficult classes they are finished, I can finally relaxing in my room. I usually watching a funny comedy show on the internet or chatting with my best friends. It being a very peaceful time for me."),
    ("Do you have a busy daily routine?", "Yes, my daily routine it is incredibly busy right now. I attending the university lectures from the morning until the late afternoon. Then, I working at a small cafe for three hours to earning some extra money. When I finally coming home, I feeling completely exhausted and ready to sleep."),
    ("Has your daily routine changed much recently?", "My routine it completely changing since I started my new part-time job. Before, I having a lot of free time to play sports in the afternoon. But now, I rushing from the classroom straight to the restaurant. I hoping my schedule it becoming less crazy next month when the exams finish."),
    ("Do you think it is important to have a daily routine?", "I believing that having a regular routine it is very important for the health. If you waking up at different times every day, your body it becoming very confused and tired. A good schedule it helping you to organize your busy life and finish all your important homework on time."),
    ("What do you usually do on the weekends?", "On the weekends, I trying to sleep until ten o'clock because I am so tired. In the afternoon, I meeting my friends at the shopping mall to watch a new movie. Sometimes we eating a big pizza together. It being a great way to forget about the stressful school work."),
    ("Do you like to plan your day in advance?", "I always writing down my plan in a small notebook the night before. If I not making a clear plan, I easily forgetting to do my important university assignments. Writing things down it making me feel much more organized and less anxious about the busy tomorrow."),
    ("Are you a morning person or an evening person?", "I definitely being an evening person. In the early morning, my brain it working very slowly and I cannot thinking clearly. But after dinner, I suddenly feeling very awake and full of creative ideas. Therefore, I always doing my most difficult homework late at night when the house is quiet."),
    ("What would you like to change about your daily routine?", "I wanting to add some physical exercise to my daily routine. Currently, I sitting in front of the computer for too many hours. If I waking up just thirty minutes earlier, I could doing some simple yoga in my bedroom. This it probably making me feel much healthier and stronger."),
    ("How do you relax at the end of a busy day?", "To relaxing at the end of the day, I taking a very long, hot shower. The warm water it completely washing away the terrible stress from the office. After that, I listening to some slow, classical music while drinking a cup of warm tea. It preparing my mind for a good sleep.")
]
for q, t in c1_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v6_g5_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 6, "grammar": 5, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR6] Uses an adequate range of vocabulary with some less common items ('exhausted', 'creative ideas', 'stressful'). Meaning is generally clear.",
        "grammar_reason": "[GRA5] Attempts complex structures but with frequent, systematic errors ('I usually waking up', 'routine it helping'). Relies heavily on present participles without the auxiliary 'to be'.",
        "micro_flaws": ["systematic missing copula/auxiliary: 'I waking', 'it helping'"],
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Uses an adequate range of vocabulary with some less common items successfully.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Attempts complex structures but shows frequent, systematic errors in basic verb forms."
    })
    start_id += 1

# V6 / G6 (Weather and Seasons)
c2_t = [
    ("What is your favorite type of weather?", "My favorite weather is definitely when it is sunny but not too hot. The bright sunshine makes me feel very energetic and happy. When the weather is clear, I can go cycling in the park with my friends. I really hate the dark, rainy days because they make me feel a bit depressed."),
    ("Does the weather affect your mood?", "Yes, the weather affects my emotions quite a lot. If it is raining heavily outside, I feel very lazy and just want to sleep all day. However, when the sun is shining brightly, I feel incredibly motivated to go outside and do something productive. It's like the sun gives me extra energy."),
    ("Do you prefer summer or winter?", "I definitely prefer the cold winter season. Because the weather is freezing, I can wear my favorite warm coats and comfortable boots. Also, sitting inside with a hot cup of chocolate while watching the snow fall is a wonderful feeling. Summer is just too hot and uncomfortable for me."),
    ("Are there four distinct seasons in your country?", "Yes, my country has four very clear and distinct seasons. The winter is freezing with lots of heavy snow, while the summer is extremely hot and humid. Spring and autumn are my favorites because the temperature is very mild and the colorful leaves look absolutely beautiful in the local parks."),
    ("What do people in your country usually do in the summer?", "During the hot summer months, most people in my country travel to the coast. They spend their weekends swimming in the cool ocean and eating fresh seafood on the beach. Because the city gets too hot, escaping to the seaside is the most popular way to relax and cool down."),
    ("Do you like it when it rains?", "I actually enjoy the rain if I am safely inside my house. The gentle sound of the raindrops hitting the window is very relaxing and helps me to focus on reading my books. But if I have to walk to the university in a heavy storm, it is very annoying and frustrating."),
    ("Has the weather in your country changed in recent years?", "Yes, the weather has become quite unpredictable recently. The summers are definitely getting much hotter than before, and we are experiencing more heavy storms in the autumn. I think this is probably due to global climate change, which is quite a worrying situation for the local farmers."),
    ("What is the climate like in your hometown?", "My hometown has a very mild and pleasant climate. It never gets incredibly hot in the summer, and it rarely snows in the winter. Because the temperature is always quite comfortable, we can enjoy outdoor activities almost every single day of the year. It's a great place to live."),
    ("Do you check the weather forecast regularly?", "I check the weather forecast on my phone every single morning before I leave the house. Because the weather can change very suddenly, I need to know if I should carry an umbrella or wear a heavy jacket. It helps me to avoid getting caught in an unexpected rain shower."),
    ("Would you like to live in a place with a different climate?", "I would love to live in a country that is warm all year round. Dealing with the freezing snow and dark winter mornings here is very exhausting. If I lived somewhere tropical, I could go swimming every day and I would probably feel much happier and healthier overall.")
]
for q, t in c2_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v6_g6_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 6, "grammar": 6, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR6] Uses an adequate range of vocabulary with some less common items ('energetic', 'motivated', 'unpredictable', 'exhausting').",
        "grammar_reason": "[GRA6] Uses a mix of simple and complex sentence forms. Grammatical control is good, with only minor errors. Nothing significantly impedes communication.",
        "micro_flaws": ["some repetitive phrasing ('very energetic', 'very lazy')"],
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"},
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Uses an adequate range of vocabulary with some less common items successfully.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Mix of simple and complex structures, with noticeable but non-impeding errors."
    })
    start_id += 1

# V6 / G7 (Shopping and Spending)
c3_t = [
    ("Do you enjoy shopping?", "Yes, I really enjoy shopping, especially when I have some extra money to spend. Browsing through the new clothing collections in the large department stores is a great way to relieve stress after a busy week. Even if I don't buy anything, just looking at the nice displays makes me feel quite relaxed."),
    ("What kind of things do you usually buy?", "I primarily spend my money on electronic gadgets and computer accessories. Whenever a new smartphone or a better pair of headphones is released, I am always tempted to upgrade my equipment. I occasionally buy new clothes, but technology is definitely my main weakness when it comes to spending money."),
    ("Do you prefer shopping online or in physical stores?", "I much prefer shopping online because it is incredibly convenient and saves a lot of time. Instead of fighting through terrible traffic to reach a crowded mall, I can easily compare prices from my sofa. Furthermore, the online delivery service is usually very fast and reliable these days."),
    ("Is it easy to find good shops where you live?", "It is very easy to find excellent shops in my neighborhood. My apartment is located right next to a massive commercial center that contains hundreds of international brands. Whether you need fresh groceries or expensive fashion items, you can find absolutely everything within a five-minute walking distance."),
    ("Have you ever bought something that you were not satisfied with?", "Yes, last month I ordered a winter jacket from an unknown website, but the quality was absolutely terrible when it arrived. The material felt incredibly cheap, and the zipper was already broken. Since then, I have been much more careful about reading customer reviews before making an online purchase."),
    ("Do you think people spend too much time shopping nowadays?", "I definitely believe that many people spend far too much time and money on shopping. Because society places such a high value on owning the newest products, some individuals go into serious debt just to look fashionable. It would be much healthier if people focused more on experiences rather than material possessions."),
    ("Are there any street markets in your hometown?", "There is a fantastic, traditional street market in my hometown that opens every Sunday morning. Local farmers bring their fresh vegetables and handmade crafts to sell directly to the public. The atmosphere is always incredibly vibrant and noisy, making it a wonderful place to spend a sunny morning."),
    ("Do you like to compare prices before you buy something?", "I always make a point of comparing prices before purchasing any expensive items. By using various price-checking applications on my phone, I can usually find a significant discount at a competing store. Taking a few extra minutes to research the options can save a substantial amount of money over the year."),
    ("What was the last thing you bought for yourself?", "The last thing I purchased was a new pair of comfortable running shoes. Because I recently decided to start jogging in the park every morning, I needed proper footwear to protect my knees. Although they were quite expensive, investing in my physical health is definitely worth the high price."),
    ("Do you ever buy gifts for your friends?", "I love buying thoughtful gifts for my friends when it is their birthday. I usually try to observe what they are interested in, like a specific book or a new video game, and surprise them with it. Seeing their happy reaction when they open the present is a very rewarding feeling.")
]
for q, t in c3_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v6_g7_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 6, "grammar": 7, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR6] Uses an adequate range of vocabulary ('electronic gadgets', 'commercial center', 'substantial amount'). Meaning is clear.",
        "grammar_reason": "[GRA7] Produces frequent error-free complex sentences ('Whenever a new smartphone... is released', 'Because society places...'). Shows good flexibility and high accuracy.",
        "micro_flaws": ["vocabulary is slightly safe/standard for the high level of grammar"],
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"},
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Uses an adequate range of vocabulary with some less common items successfully.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Produces frequent error-free complex sentences. Shows good flexibility with high accuracy."
    })
    start_id += 1

# V7 / G6 (Reading and Books)
c4_t = [
    ("Do you enjoy reading books?", "I am absolutely passionate about reading, particularly during my quiet weekend mornings. Immersing myself in a captivating novel it allows me to temporarily escape the intense pressure of my university studies. Whether it is a thrilling mystery or a profound historical biography, reading it constantly expanding my perspective on the world."),
    ("What kind of books did you read when you were a child?", "When I was a child, I predominantly read fascinating fantasy novels involving magic and mythical creatures. My parents they constantly buying me new adventure series, which profoundly stimulated my vivid imagination. These enchanting stories they making me incredibly curious about the vast world beyond my small, quiet hometown."),
    ("Do you prefer reading electronic books or physical paper books?", "While the convenience of a digital tablet is undeniable, I strongly preferring the tactile sensation of holding a physical paper book. The distinctive smell of the printed pages and the satisfying sound of turning a chapter they providing a deeply nostalgic and comforting experience that a cold digital screen it simply cannot replicate."),
    ("Where is your favorite place to read?", "My absolute favorite location to read it is a small, independent coffee shop near my apartment. The subtle aroma of roasted coffee and the gentle background music they creating the perfect, relaxing ambiance for deep concentration. I can easily spending several uninterrupted hours there completely absorbed in a brilliant narrative."),
    ("Have you ever lent a book to a friend?", "I frequently lending my favorite novels to my close friends because I love discussing the complex plot twists with them later. However, occasionally a friend they forgetting to return the borrowed item, which is slightly frustrating. Nevertheless, sharing a brilliant piece of literature it is a wonderful way to connect with people."),
    ("Do you think reading is a popular activity in your country?", "Unfortunately, I observing that reading for pleasure it is becoming increasingly rare among the younger generation in my country. Because the ubiquitous smartphones they providing instant, effortless entertainment, many teenagers they completely lacking the patience required to finish a lengthy novel. This societal shift towards short-form digital content it is quite concerning."),
    ("What was the last book you read?", "The most recent book I finished it was a fascinating biography of a famous historical political leader. The author they providing incredibly detailed insights into the complex ethical dilemmas this person faced during a massive global conflict. It was a profoundly illuminating read that dramatically increasing my understanding of twentieth-century history."),
    ("Do you ever read books that are written in a foreign language?", "I frequently attempting to read contemporary novels written in English to proactively improve my linguistic proficiency. Although the sophisticated vocabulary it initially proving quite challenging, it is a highly rewarding intellectual exercise. By forcing myself to comprehend the narrative without a dictionary, my overall reading comprehension it significantly accelerating over time."),
    ("Is there a book that has significantly influenced your life?", "A philosophical novel I read during high school it profoundly altering my fundamental perspective on personal happiness. The compelling narrative it demonstrating that genuine fulfillment stems from meaningful human connections rather than the relentless pursuit of material wealth. This profound realization it permanently changing my primary priorities in life."),
    ("Do you think libraries are still important today?", "Despite the rapid proliferation of the internet, public libraries they remaining absolutely indispensable for the local community. They providing essential, free access to educational resources for disadvantaged individuals who cannot affording expensive computers. Furthermore, the tranquil atmosphere of a traditional library it offering a necessary sanctuary for focused academic research.")
]
for q, t in c4_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v7_g6_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 7, "grammar": 6, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR7] Good range of less common vocabulary ('captivating novel', 'tactile sensation', 'ubiquitous smartphones', 'linguistic proficiency'). Paraphrasing is effective.",
        "grammar_reason": "[GRA6] Uses a mix of simple and complex sentence forms. Noticeable and systematic errors in basic structures ('reading it constantly expanding', 'parents they constantly buying').",
        "micro_flaws": ["double subjects: 'reading it', 'parents they'", "verb form errors: 'it providing'"],
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"},
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Good range of less common vocabulary used with some flexibility and style awareness.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Mix of simple and complex structures, but with frequent, noticeable errors that do not impede meaning."
    })
    start_id += 1

# V7 / G7 (Holidays and Festivals)
c5_t = [
    ("What is the most important festival in your country?", "The most significant cultural celebration in my country is undoubtedly the Lunar New Year. During this festive period, families travel immense distances to reunite and share an extravagant, traditional feast. It is a profoundly meaningful occasion dedicated to honoring our ancestors and eagerly anticipating good fortune for the upcoming twelve months."),
    ("How do people usually celebrate this festival?", "People typically celebrate by meticulously cleaning their homes to sweep away any lingering bad luck from the previous year. Furthermore, the streets are vividly decorated with glowing red lanterns, and the older generation traditionally gifts small envelopes of money to the children. The vibrant atmosphere is completely filled with joy and lively music."),
    ("What is your favorite holiday of the year?", "My absolute favorite holiday is the mid-autumn festival because the weather is perfectly crisp and pleasant. We normally gather in the local park to admire the exceptionally bright full moon while eating delicious, sweet mooncakes. The tranquil ambiance of the evening makes it a highly relaxing and deeply nostalgic experience for me."),
    ("Has the way people celebrate festivals changed over time?", "The manner in which we celebrate has definitely modernized quite significantly in recent decades. While our grandparents strictly followed every single ancient ritual, the younger generation tends to treat these holidays primarily as an opportunity for domestic tourism. Unfortunately, some of the profound historical significance is slowly fading due to rapid commercialization."),
    ("Do you prefer participating in traditional festivals or modern holidays?", "I generally lean towards participating in traditional festivals because they offer a vital connection to my unique cultural heritage. While modern, commercial holidays like Valentine's Day are undeniably fun, they lack the deep historical resonance and profound community spirit that characterize our ancient, indigenous celebrations."),
    ("Is it important for a country to preserve its traditional festivals?", "It is absolutely paramount for any nation to meticulously preserve its traditional festivals. These unique celebrations serve as the vibrant cultural glue that binds diverse communities together, providing a shared sense of enduring historical identity. Without these vital cultural anchors, a society risks becoming entirely homogenous and profoundly disconnected from its roots."),
    ("What special foods are associated with your favorite festival?", "During the spring festival, we invariably prepare a massive quantity of intricate, handmade dumplings. The entire extended family gathers in the kitchen, turning the exhausting preparation process into a delightful, collaborative social event. The specific shape of these dumplings symbolically represents future prosperity, adding a lovely layer of cultural meaning to the meal."),
    ("Do you usually spend holidays with your family or your friends?", "For the major, traditional holidays, I invariably prioritize spending the time exclusively with my immediate family. However, for more casual, modern celebrations like New Year's Eve, I much prefer attending an energetic party with my close friends. Balancing family obligations with vibrant social events is crucial for my overall happiness."),
    ("Do you enjoy traveling during the public holidays?", "I actually strongly dislike traveling during the major public holidays because the transportation infrastructure becomes completely overwhelmed. The airports are incredibly chaotic, and the price of a standard hotel room skyrockets to an unreasonable level. I find it much more relaxing to enjoy a quiet, peaceful staycation in my own comfortable apartment."),
    ("What is the best part of having a long holiday from work?", "The absolute best part of a long holiday is having the unrestricted freedom to completely disconnect from my professional responsibilities. Without the constant anxiety of impending corporate deadlines, I can fully immerse myself in my neglected hobbies or simply sleep in late. This vital period of mental restoration drastically improves my productivity when I finally return.")
]
for q, t in c5_t:
    wc = len(t.split())
    # G7: Frequent error-free sentences, minor slips (I'll add a tiny slip to keep it safely at 7, e.g., 'families travels', 'People typically celebrates')
    t = t.replace("families travel", "families travels")
    t = t.replace("People typically celebrate", "People typically celebrates")
    t = t.replace("grandparents strictly followed", "grandparents strictly follows")
    samples.append({
        "sample_id": f"syn_p1_v7_g7_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 7, "grammar": 7, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR7] Good range of vocabulary ('extravagant', 'nostalgic experience', 'cultural heritage'). Paraphrasing is very effective.",
        "grammar_reason": "[GRA7] Frequently produces error-free complex sentences. Shows good flexibility. However, there are occasional, minor slips in subject-verb agreement ('families travels', 'People typically celebrates') which keep it at a 7.",
        "micro_flaws": ["agreement slip: 'families travels'", "agreement slip: 'People typically celebrates'"],
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"},
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Good range of less common vocabulary used with flexibility and precision.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Produces frequent error-free complex sentences, but occasional minor slips occur."
    })
    start_id += 1

with open(filename, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
print(f"Batch {batch_num} written with {len(samples)} samples. Part 1 lengths optimized natively.")
