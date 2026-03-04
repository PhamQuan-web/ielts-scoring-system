import json

# PART 1 BATCHES START HERE
# Word count rule for Part 1: 25 - 80 words. (If V4, under 25 is minimal, but safe is 25-50 for direct_answer, 50-80 extended)
# I will aim for ~40-60 words to safely fit in the Part 1 band constraints.

batch_num = 60
filename = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p1_01.jsonl"
start_id = 1
samples = []

# Batch 60: V4/G4(10) V4/G5(10) V5/G4(10) V5/G5(10) V5/G6(10) | IDs: 0001–0050

# V4 / G4 (Home / Hometown)
c1_t = [
    ("Do you live in a house or an apartment?", "I live in small apartment in the big city. It have two rooms and one small kitchen. My apartment it is very nice but a little noisy. The traffic outside it make much loud sound every night. But I like my home because it near my office job."),
    ("Who do you live with?", "I living with my family now. My mother she cook very good food for me everyday. My father he working in the hospital. I also have one small brother, he playing football all the time. We are very happy family together in our small house."),
    ("What is your favorite room in your home?", "My favorite room it is my bedroom. Because I have my computer and big bed inside. When I finish the work, I go to my room and playing games. It is very quiet and peaceful place for me. I sleeping very well there every night."),
    ("How long have you lived there?", "I living there for five years already. Before, I live in different small town. But I move here for my university study. Now I knowing the area very well. I have many good friends living near my apartment block."),
    ("Do you plan to live there in the future?", "No, I not plan to live there forever. In the future, I wanting to buy a big house with a garden. Because I want to have a dog. My apartment it is too small for big animal. I need more money first to buy it."),
    ("What is your hometown like?", "My hometown it is very beautiful and small. It have a big green mountain and long river. Many people they visiting my town to take nice photos. The weather it is always warm and sunny. I missing my hometown very much when I stay in the city."),
    ("Is your hometown a good place for young people?", "No, I think my hometown it not good for young people. It very boring because it no have big cinema or shopping mall. The young people they want to finding good jobs, but my town only have small farms. So everyone they moving away to the capital city quickly."),
    ("What is the oldest part of your hometown?", "The oldest part it is the small stone bridge over the river. My grandfather he tell me it build many hundred years ago. People they still walking on it today. It look very old but it still very strong. We taking many wedding photos there."),
    ("Has your hometown changed much since you were a child?", "Yes, my hometown it changing very much now. Before, it have many green trees and empty space. But now, they building many tall apartments and big supermarkets. The traffic it becoming very bad and noisy. I liking the old quiet town much better than today."),
    ("What do you like most about your hometown?", "I liking the friendly people most. In my hometown, everyone they knowing each other's name. When you walking in the street, the people they always smiling and saying hello. It feeling very warm and safe, like one very big happy family living together.")
]
for q, t in c1_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v4_g4_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 4, "grammar": 4, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR4] Uses basic vocabulary exclusively ('small apartment', 'big city', 'good food'). Extremely limited range. Cannot paraphrase.",
        "grammar_reason": "[GRA4] Frequent and systematic errors in basic structures ('It have', 'I living', 'My mother she cook'). Only basic sentence forms are recognizable.",
        "micro_flaws": ["systematic missing auxiliary: 'I living'", "frequent double subjects: 'mother she', 'traffic it'", "agreement: 'It have'"],
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Uses basic vocabulary exclusively. Cannot paraphrase effectively.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Frequent and systematic errors in basic structures. Only basic sentence forms are recognizable."
    })
    start_id += 1

# V4 / G5 (Work / Study)
c2_t = [
    ("Do you work or are you a student?", "I am a student right now. I study the business at the university. I go to the class from Monday to Friday. I really liking my teachers because they are very nice to me. I hope I can finish my school next year successfully."),
    ("Why did you choose that subject?", "I choose to study business because I want to make a lot of money. My father has a small shop, and I want to help him. If I learn how to manage the money, our shop will become very big and famous in the future."),
    ("Do you like your university?", "Yes, I really like my big university. It has a very nice library where I can read books quietly. Also, the food in the cafeteria is very cheap and good. I have made many happy friends there since I started my study last year."),
    ("Is there anything you dislike about your studies?", "The thing I don't like is the homework. The teachers give us too much difficult homework every weekend. I must sit in my room for many hours to read the heavy books. Sometimes I feel very tired and I want to sleep instead of working."),
    ("What do you want to do after you graduate?", "After I finish my school, I want to find a good job in a big company. I want to work in an office with a computer. If I work very hard, maybe I can travel to other countries for my work. That is my big dream."),
    ("What is your current job?", "I work in a small restaurant near my house. I am a waiter there. I take the food to the tables and clean the dirty plates. It is a very busy job, but I like talking to the hungry customers every day."),
    ("Do you have to work with other people?", "Yes, I must work with a big team. We have three cooks in the kitchen and four waiters outside. We must help each other when the restaurant is full of people. If we don't work together, the customers will be very angry and sad."),
    ("Do you think you will change jobs in the future?", "Yes, I think I will change my job later. Being a waiter is very hard for my legs because I stand all day. I want to find an easy office job where I can sit down. I am studying English now to get a better job."),
    ("What is the most interesting part of your work?", "The most interesting part is meeting new people from different countries. Sometimes tourists come to eat our local food. I try to speak simple English with them. They are very friendly and they smile at me. It makes my hard work feel much better."),
    ("Is your job very popular in your country?", "Yes, working in a restaurant is very popular for young people. Many university students do this job in the evening to get some extra money. Because you don't need a special certificate to be a waiter, it is very easy to find this kind of work.")
]
for q, t in c2_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v4_g5_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 4, "grammar": 5, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR4] Uses only basic vocabulary ('big company', 'good job', 'heavy books', 'dirty plates'). Very limited range.",
        "grammar_reason": "[GRA5] Produces basic sentences accurately ('I am a student right now', 'I work in a small restaurant'). Attempts complex sentences ('Because you don't need...', 'If we don't work together...') with reasonable success, though some errors persist.",
        "micro_flaws": ["verb form slip: 'I really liking'", "basic vocabulary choices"],
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 4\n\n**Reasoning:** [LR4] Uses basic vocabulary exclusively. Cannot paraphrase effectively.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Produces basic sentences accurately. Attempts complex sentences with some success."
    })
    start_id += 1

# V5 / G4 (Free time / Hobbies)
c3_t = [
    ("What do you usually do in your free time?", "In my free time, I usually playing the computer games with my friends online. We talking on the headphone and laughing very loud. Sometimes I also watching the funny videos on my phone. It helping me to relaxing after the difficult school day."),
    ("Do you prefer spending your free time alone or with others?", "I preferring to spend time with my friends. Because when I am alone, I feeling very bored and sad. If we going to the cinema together, it is much more exciting. We eating the popcorn and talking about the movie. It making me very happy."),
    ("Has your free time changed since you were a child?", "Yes, it changing a lot. When I was a small child, I playing outside with the ball everyday. But now I having too much homework from the university. So I only staying inside my bedroom to studying. I not having much free time now."),
    ("Is there any new hobby you would like to try?", "I wanting to try learning the guitar in the future. Because I thinking the music it sound very beautiful and romantic. But the guitar it is very expensive to buy in the shop. Maybe if I saving my money, I can buying one next year."),
    ("Do you like reading books in your free time?", "No, I not liking reading the books very much. The words they making my eyes very tired and sleepy. I preferring to watch the fast movies instead. The television it is much easier to understand than the long, boring paper book."),
    ("How do people in your country usually relax?", "In my country, the people they usually going to the coffee shop to relaxing. They sitting outside on the small chairs and drinking the strong black coffee. They talking with their neighbors for many hours in the evening. It being a very slow and peaceful tradition."),
    ("Do you think it is important to have free time?", "Yes, having free time it is absolutely necessary for the healthy life. If a person he working all the time without resting, his brain it becoming very stressed and sick. We needing the free time to sleep and enjoy the simple things with our family."),
    ("What did you do last weekend?", "Last weekend, I going to the big shopping mall with my young sister. We buying some new clothes for the winter season. Then we eating the spicy pizza in the food court. After that, we taking the bus home because it raining very heavily outside."),
    ("Do you like outdoor activities?", "I liking the outdoor activities when the weather it is nice and sunny. Going to the green park to having a picnic is very fun. But if it is very hot and sweating, I preferring to stay inside the room with the cold air conditioning."),
    ("Do you play any sports in your free time?", "I sometimes playing the badminton in the park near my house. I playing with my father every Sunday morning. It making me run very fast and jump high. But I not being a professional player, I just doing it for the fun exercise.")
]
for q, t in c3_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v5_g4_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 5, "grammar": 4, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "medium",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR5] Vocabulary is adequate but relies on simple, everyday terms ('computer games', 'funny videos', 'boring paper book').",
        "grammar_reason": "[GRA4] Frequent and systematic errors in basic structures ('I usually playing', 'It helping me', 'I preferring'). Relies heavily on using present participles without the auxiliary 'to be'.",
        "micro_flaws": ["systematic missing copula/auxiliary: 'I playing', 'It helping'"],
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Vocabulary is adequate but relies on basic, everyday terms.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 4\n\n**Reasoning:** [GRA4] Frequent and systematic errors in basic structures. Only basic sentence forms are recognizable."
    })
    start_id += 1

# V5 / G5 (Music / Entertainment)
c4_t = [
    ("What kind of music do you like listening to?", "I really enjoy listening to pop music from my country. It has a very fast beat and makes me want to dance. When I feel sad, I play my favorite songs loudly in my room. The simple lyrics always make my mood much better."),
    ("Do you play any musical instruments?", "No, I don't know how to play any instruments. When I was young, I tried to learn the piano, but my fingers were too slow. I think you need to practice for many hours every day to be good. I didn't have enough patience for it."),
    ("Have you ever been to a live concert?", "Yes, I went to a big music concert last year with my best friend. The famous singer sang all of our favorite songs on a bright stage. There were thousands of noisy people jumping and shouting. It was a very amazing and crazy experience for us."),
    ("When do you usually listen to music?", "I usually listen to music when I am traveling on the bus to my office. The journey takes almost an hour, so the music helps me to not feel bored. I put on my headphones and close my eyes to relax before my busy workday starts."),
    ("Do you think music is important in schools?", "Yes, I think music is a very important subject for young children. It helps them to be more creative and happy in the classroom. Singing songs together is much more fun than just reading numbers from a math book. It gives them a nice break."),
    ("What kind of movies do you enjoy watching?", "I prefer watching action movies with many fast cars and explosions. They are very exciting and keep my attention the whole time. I don't really like romantic movies because they are too slow and sometimes make me feel sleepy. Action films are definitely my favorite choice."),
    ("Do you prefer watching movies at home or at the cinema?", "I prefer going to the big cinema to watch a new movie. The huge screen and the loud sound system make the film feel very real. Also, eating the hot popcorn in the dark room is a special feeling that you cannot get in your small living room."),
    ("How often do you go to the cinema?", "I go to the cinema maybe once a month. Because the tickets are quite expensive, I only go when a very famous blockbuster movie is showing. Most of the time, I just use the internet to watch normal television shows on my computer to save my money."),
    ("Who is your favorite actor or actress?", "My favorite actor is very famous for doing his own dangerous stunts. He jumps from tall buildings and drives motorcycles very fast. I respect him because he works very hard to make the action look real. His movies are always very successful in my country."),
    ("Have your movie tastes changed as you got older?", "Yes, my taste has changed a little bit. When I was a teenager, I only watched silly comedies and cartoons. But now, I sometimes enjoy watching serious historical dramas. I like to learn about real events from the past, which I found very boring when I was younger.")
]
for q, t in c4_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v5_g5_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 5, "grammar": 5, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR5] Vocabulary is adequate but relies heavily on simple, everyday terms ('pop music', 'fast beat', 'big cinema', 'silly comedies').",
        "grammar_reason": "[GRA5] Produces basic sentences accurately. Attempts complex sentences but lacks flexibility. Very straightforward and simple construction throughout.",
        "micro_flaws": ["repetitive simple sentence structures"],
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"},
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Vocabulary is adequate but relies on basic, everyday terms.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Produces basic sentences accurately. Attempts complex sentences with some success but limited flexibility."
    })
    start_id += 1

# V5 / G6 (Transport / Travel)
c5_t = [
    ("How do you usually travel to work or school?", "I usually take the underground train to get to my university every morning. It is much faster than taking the local bus because it completely avoids the terrible traffic jams on the roads. Although it gets very crowded during the rush hour, it is still the most reliable way to travel."),
    ("What is the public transportation like in your city?", "The public transportation in my city is quite good but it can be very expensive. We have many new buses and a large subway network that connects all the important areas. However, the ticket prices keep going up every year, which makes it difficult for poor students like me to afford."),
    ("Do you prefer using public transport or driving a car?", "If I had a choice, I would definitely prefer driving my own car. Having a private car gives you the freedom to go anywhere at any time without checking a bus schedule. Unfortunately, finding a parking space in the busy city center is almost impossible, so I am forced to use the train."),
    ("How has transportation changed in your city recently?", "In recent years, the government has introduced many electric bicycles and scooters on the streets. People can easily rent them using their smart phones for short journeys. This new technology has made traveling short distances much more convenient, and it also helps to reduce the dirty pollution in the air."),
    ("Do you often travel long distances?", "I don't travel long distances very often because I am too busy with my studies. Maybe once a year, I take a long train ride to visit my grandparents in the countryside. The journey takes about five hours, but I enjoy looking at the beautiful green fields through the window."),
    ("What is your favorite mode of transport for long trips?", "For long trips, I definitely prefer flying in an airplane. It is incredibly fast and saves you a lot of valuable time. Even though the security checks at the airport are very annoying and slow, arriving in a different country in just two hours is absolutely amazing to me."),
    ("Do you ever ride a bicycle?", "Yes, I ride my bicycle in the park on weekends when the weather is warm. It is a great way to get some fresh air and exercise my legs. I never ride my bicycle on the main roads, though, because the fast cars and trucks make it far too dangerous."),
    ("Would you like to learn how to drive?", "I already learned how to drive last year, and I have my official license. The driving lessons were quite difficult at first, especially learning how to park the car backwards. But once I practiced with my father for a few weeks, I became much more confident behind the steering wheel."),
    ("Are there traffic problems in your hometown?", "Yes, the traffic jams in my hometown are becoming a very serious problem. Because everyone wants to drive their own car to the office, the main bridge is always completely blocked in the morning. Unless the city builds wider roads, this frustrating situation will only get worse in the future."),
    ("How do you think people will travel in the future?", "I imagine that in the future, we will have flying cars that can avoid the roads entirely. This sounds like science fiction, but technology is advancing very quickly. If we have flying taxis, we won't need to worry about traffic jams or red lights ever again, making life much simpler.")
]
for q, t in c5_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v5_g6_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 5, "grammar": 6, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR5] Vocabulary is adequate but relies on basic, everyday terms ('terrible traffic jams', 'dirty pollution', 'fast cars').",
        "grammar_reason": "[GRA6] Uses a mix of simple and complex sentence forms ('Although it gets very crowded...', 'Unless the city builds...'). Grammatical control is reasonably good, better than the vocabulary range.",
        "micro_flaws": ["vocabulary is noticeably simpler than the grammar structures used"],
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"},
        "output": "## Vocabulary (Lexical Resource): Band 5\n\n**Reasoning:** [LR5] Vocabulary is adequate but relies on basic, everyday terms.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Mix of simple and complex structures, with noticeable but non-impeding errors."
    })
    start_id += 1

with open(filename, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
print(f"Batch {batch_num} written with {len(samples)} samples. Native manual generation applied.")
