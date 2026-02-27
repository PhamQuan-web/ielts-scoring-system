import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_16_p1.jsonl"

samples = [
    # --- V6/G7 (751-760) ---
    {
        "sample_id": "syn_p2_v6_g7_0751",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a public garden you visited.",
        "transcript_cleaned": "I visited a nice public garden in the city center last summer. It was a very big place with many green trees and colorful flowers. Although the weather was hot, the garden had plenty of shade, which made it comfortable to walk around. I remember seeing a small lake in the middle where people were feeding ducks. What impressed me the most was the design of the garden, which was very organized and clean. I sat on a bench for a while to enjoy the fresh air. If I had more time, I would have stayed longer to read my book. It is a popular place for families to relax on weekends.",
        "word_count": 108,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 7,
        "vocab_reason": "[LR6] Adequate range: 'shade', 'comfortable', 'organized', 'fresh air'. Meaning clear but lacks precision.",
        "grammar_reason": "[GRA7] Frequent error-free complex structures: 'Although the weather was hot', 'Where people were feeding', 'What impressed me the most', 'If I had more time'.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v6_g7_0752",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of advice you gave someone.",
        "transcript_cleaned": "I gave advice to my younger brother about his school work. He was having trouble with math, and he felt very stressed. I told him that he should practice more every day instead of playing video games. I suggested that he ask his teacher for extra help if he didn't understand something. It was important for him to know that hard work brings good results. After listening to me, he started to study harder. I was happy when he passed his exam with a good score. Giving advice is not easy, but it can be very helpful if the person listens.",
        "word_count": 102,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 7,
        "vocab_reason": "[LR6] Adequate range: 'trouble', 'stressed', 'suggested', 'extra help', 'results'. Functional.",
        "grammar_reason": "[GRA7] Complex structures: 'That he should practice', 'If he didn't understand', 'It was important for him to know'. Good control.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v6_g7_0753",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a painting you like.",
        "transcript_cleaned": "I like a painting that hangs in my living room. It is a picture of a mountain landscape with a river flowing through it. My father bought it many years ago from a local artist. The colors are very bright and realistic, which makes the room look lively. Every time I look at it, I feel calm and relaxed. It reminds me of a holiday we took when I was a child. Although it is not a famous painting, it has a lot of meaning for my family. The artist used a special technique that makes the water look like it is moving.",
        "word_count": 106,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 7,
        "vocab_reason": "[LR6] Adequate range: 'landscape', 'flowing', 'realistic', 'lively', 'technique'. Clear meaning.",
        "grammar_reason": "[GRA7] Complex structures: 'That hangs in my living room', 'Which makes the room look', 'Every time I look', 'Although it is not'. Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v6_g7_0754",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a street market you visited.",
        "transcript_cleaned": "I went to a busy street market in Thailand during my vacation. There were many small stalls selling food, clothes, and souvenirs. The atmosphere was very noisy but exciting because there were so many people. I tried some local street food which was spicy but delicious. The sellers were friendly and tried to talk to us in English. While we were walking, I bought a nice t-shirt for a cheap price. I think street markets are a good place to learn about the local culture. It was a fun experience that I will remember for a long time.",
        "word_count": 100,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 7,
        "vocab_reason": "[LR6] Adequate range: 'stalls', 'souvenirs', 'atmosphere', 'local culture', 'cheap price'. Standard topics.",
        "grammar_reason": "[GRA7] Complex structures: 'Which was spicy', 'Because there were', 'While we were walking', 'That I will remember'. Good control.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v6_g7_0755",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you were late.",
        "transcript_cleaned": "I remember a time when I was late for an important meeting. It happened last month on a Monday morning. I woke up late because my alarm clock did not ring. I quickly got dressed and ran to the bus station, but I missed the bus. I had to wait for the next one, which took twenty minutes. By the time I arrived at the office, the meeting had already started. I felt very embarrassed and apologized to my boss. He was not happy, but he understood my situation. Since then, I always set two alarms to make sure I wake up on time.",
        "word_count": 107,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 7,
        "vocab_reason": "[LR6] Adequate range: 'important meeting', 'alarm clock', 'missed the bus', 'embarrassed', 'apologized'.",
        "grammar_reason": "[GRA7] Complex structures: 'Time when I was late', 'Because my alarm clock', 'Which took twenty minutes', 'Had already started' (Past Perfect).",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v6_g7_0756",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a modern building you like.",
        "transcript_cleaned": "I really like the new library building in my city. It is a very modern structure made of glass and steel. The design is unique because it looks like an open book. Inside, there are many floors with comfortable seating areas and computers. The best part is the roof garden, where you can see the whole city view. It was built two years ago to encourage people to read more. Whenever I go there, I feel inspired to study. It is a great example of modern architecture that is both useful and beautiful.",
        "word_count": 95,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 7,
        "vocab_reason": "[LR6] Adequate range: 'structure', 'unique', 'comfortable seating', 'encourage', 'architecture', 'inspired'.",
        "grammar_reason": "[GRA7] Complex structures: 'Made of glass', 'Because it looks like', 'Where you can see', 'To encourage people'. Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v6_g7_0757",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a game you played as a child.",
        "transcript_cleaned": "When I was a child, I used to play a game called hide and seek with my neighbors. We played it in the park near my house almost every evening. One person had to count to ten while the others hid behind trees or bushes. It was very exciting trying not to be found. I was good at hiding because I was small and could fit in small places. Sometimes we played until it got dark and our parents called us home. It is a simple game, but it gave us a lot of joy and happy memories.",
        "word_count": 100,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 7,
        "vocab_reason": "[LR6] Adequate range: 'hide and seek', 'neighbors', 'exciting', 'fit in', 'memories'. Functional.",
        "grammar_reason": "[GRA7] Complex structures: 'While the others hid', 'Trying not to be found', 'Until it got dark', 'But it gave us'. Good control.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v6_g7_0758",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a quiet place you like.",
        "transcript_cleaned": "A quiet place I enjoy visiting is the small library in my university. It is located in the basement, so it is very silent away from the noisy streets. There are many old books and comfortable chairs where I can sit for hours. I usually go there when I need to concentrate on my studies or prepare for an exam. The lighting is soft and warm, which helps me relax. Unlike the main library, not many people know about this place. It is like a secret spot where I can escape from the busy world and find some peace.",
        "word_count": 102,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 7,
        "vocab_reason": "[LR6] Adequate range: 'located', 'basement', 'concentrate', 'lighting', 'escape', 'peace'. Clear meaning.",
        "grammar_reason": "[GRA7] Complex structures: 'Where I can sit', 'When I need to concentrate', 'Which helps me relax', 'Unlike the main library'. Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v6_g7_0759",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you helped a child.",
        "transcript_cleaned": "I remember helping my niece with her bicycle last weekend. She is five years old and she was learning how to ride it for the first time. She was afraid of falling, so I held the back of the seat to support her. I encouraged her to keep pedaling and look forward. After a few tries, she started to balance by herself. I ran beside her to make sure she was safe. When she finally rode without my help, she was so happy and proud. It was a rewarding moment for me to see her succeed and overcome her fear.",
        "word_count": 102,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 7,
        "vocab_reason": "[LR6] Adequate range: 'pedaling', 'balance', 'support', 'encouraged', 'overcome', 'rewarding'. Functional.",
        "grammar_reason": "[GRA7] Complex structures: 'Learning how to ride', 'So I held', 'To make sure she was safe', 'When she finally rode'. Good control.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v6_g7_0760",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plan for the future.",
        "transcript_cleaned": "I have a plan to learn a new language in the near future. I am thinking about studying Spanish because I want to travel to South America one day. I plan to enroll in an online course next month. I know it will be difficult to learn grammar and vocabulary, but I am motivated. I think knowing a second language is very useful for traveling and making new friends. If I study hard every day, I hope to be able to speak basic sentences within six months. It is a big challenge, but I am looking forward to it.",
        "word_count": 101,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 7,
        "vocab_reason": "[LR6] Adequate range: 'enroll', 'online course', 'motivated', 'challenge', 'looking forward'. Clear meaning.",
        "grammar_reason": "[GRA7] Complex structures: 'Because I want to travel', 'Knowing a second language is', 'If I study hard', 'To be able to speak'. Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    # --- V7/G6 (761-770) ---
    {
        "sample_id": "syn_p2_v7_g6_0761",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a pet you would like to have.",
        "transcript_cleaned": "I would really love to own a Golden Retriever dog. They are renowned for their gentle temperament and loyalty. I have read that they are excellent companions for families. The reason I want this breed is because they are intelligent and easy to train. I would take it for long walks in the park, which is good for my health too. However, I know that having a dog require a lot of responsibility. I must to feed it and clean it every day. Also, the veterinary costs can be expensive. Despite the challenges, I think the companionship is priceless.",
        "word_count": 101,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 6,
        "vocab_reason": "[LR7] flexible use: 'renowned', 'temperament', 'companions', 'breed', 'intelligent', 'responsibility', 'veterinary', 'priceless'.",
        "grammar_reason": "[GRA6] Mix of simple/complex. Errors in complex: 'Having a dog require' (Agreement). 'Must to feed' (Modal error). Meaning clear.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v7_g6_0762",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a job you would not like to do.",
        "transcript_cleaned": "I definitely would not like to work as a surgeon in a hospital. Although it is a prestigious profession with a high salary, the pressure is overwhelming. Surgeons must have steady hands and incredible focus during operations. One mistake can be fatal, which is too much stress for me. Also, the working hours is very long and irregular. I value my work-life balance and I enjoy having free time. I admire people who do this job, but I don't think I am suitable for it. The emotional burden of dealing with life and death situations are too heavy.",
        "word_count": 102,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 6,
        "vocab_reason": "[LR7] flexible use: 'prestigious', 'profession', 'overwhelming', 'steady hands', 'fatal', 'irregular', 'work-life balance', 'emotional burden'.",
        "grammar_reason": "[GRA6] Mix of structures. Errors: 'Working hours is' (Agreement). 'Situations are too heavy' (Agreement error with burden). Meaning clear.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v7_g6_0763",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a prize you won.",
        "transcript_cleaned": "I won a first prize in a painting competition when I was in high school. It was a regional contest and many students participated. I painted a landscape using watercolors, depicting a sunset over the ocean. I was absolutely thrilled when the judges announced my name. The prize was a set of professional art supplies, which I used for a long time. It gave me a huge sense of accomplishment and validated my artistic skills. Before that, I wasn't sure if I was good enough. Winning that prize encourage me to continue painting as a serious hobby.",
        "word_count": 100,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 6,
        "vocab_reason": "[LR7] flexible use: 'regional contest', 'participated', 'depicting', 'thrilled', 'judges', 'professional art supplies', 'accomplishment', 'validated'.",
        "grammar_reason": "[GRA6] Mix of structures. Errors: 'Prize encourage me' (Tense). 'Participated' ok. Some simple sentences. Meaning clear.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v7_g6_0764",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a practical skill you learned.",
        "transcript_cleaned": "I learned how to repair basic electronics from my uncle. He is an electrical engineer and he taught me how to fix broken devices. The most useful thing I learned was how to solder wires together. It requires precision and patience. I remember fixing my old radio which stopped working. When I heard the sound again, I felt very satisfied. This skill has been incredibly beneficial because I don't have to throw away things immediately. I can try to repair them first. However, sometimes the problem is too complex and I don't know what to do it.",
        "word_count": 100,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 6,
        "vocab_reason": "[LR7] flexible use: 'repair', 'electronics', 'engineer', 'solder wires', 'precision', 'patience', 'beneficial', 'complex'.",
        "grammar_reason": "[GRA6] Mix of structures. Errors: 'What to do it' (Structure). 'Radio which stopped' ok. Meaning clear.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v7_g6_0765",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a library you visited.",
        "transcript_cleaned": "I visited the National Library in the capital city last year. It is a magnificent building with impressive architecture. The collection of books is vast, covering every subject imaginable. I was looking for some reference materials for my thesis. The atmosphere was incredibly quiet and studious, which helped me focus. I spent the whole afternoon browsing through the shelves. They also have a digital archive which is very convenient. I was amazed by the sheer volume of information available. The only problem was that the air conditioning were too cold, so I had to wear my jacket inside.",
        "word_count": 100,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 6,
        "vocab_reason": "[LR7] flexible use: 'magnificent', 'architecture', 'vast', 'imaginable', 'reference materials', 'thesis', 'studious', 'browsing', 'archive'.",
        "grammar_reason": "[GRA6] Mix of structures. Errors: 'Air conditioning were' (Agreement). 'Covering every subject' (Participle). Meaning clear.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v7_g6_0766",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a type of music you like.",
        "transcript_cleaned": "I am a big fan of jazz music, which originated in America. I love the improvisation and the complex rhythms. It is very relaxing to listen to after a stressful day. The combination of saxophone, piano, and double bass create a unique sound. My favorite artist is Miles Davis because his melodies are soulful and expressive. I often listen to jazz when I am cooking or reading. It creates a sophisticated ambiance in my home. Some people find it chaotic, but I find it harmonious. I think you need to have a good ear to appreciate the nuances of jazz.",
        "word_count": 103,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 6,
        "vocab_reason": "[LR7] flexible use: 'improvisation', 'complex rhythms', 'stressful', 'unique sound', 'soulful', 'expressive', 'sophisticated ambiance', 'chaotic', 'harmonious', 'nuances'.",
        "grammar_reason": "[GRA6] Mix of structures. Errors: 'Combination... create' (Agreement). 'Originated in' ok. Meaning clear.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v7_g6_0767",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you saved money.",
        "transcript_cleaned": "I decided to save money to buy a new laptop for my studies. I realized I was spending too much on unnecessary things like coffee and takeout food. So, I created a strict budget and stuck to it. I cooked my own meals and stopped buying clothes for six months. It was difficult at first because I felt deprived. However, watching my savings grow was very motivating. Finally, I had enough money to purchase the model I wanted. It was a high-spec machine that helped me with my assignments. I learned that financial discipline is essential for achieving goals.",
        "word_count": 102,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 6,
        "vocab_reason": "[LR7] flexible use: 'unnecessary', 'strict budget', 'deprived', 'motivating', 'purchase', 'high-spec', 'financial discipline', 'achieving goals'.",
        "grammar_reason": "[GRA6] Mix of structures. Errors: 'Stuck to it' ok. 'Difficult at first' ok. Simple sentences mostly. Meaning clear.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v7_g6_0768",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a forest you visited.",
        "transcript_cleaned": "I went hiking in a dense forest near my hometown last autumn. The scenery was breathtaking, with tall trees and colorful leaves covering the ground. The air was crisp and fresh, smelling of pine and earth. We walked along a winding trail that led to a waterfall. The sound of the rushing water was very therapeutic. I saw some squirrels and birds, which was delightful. Being surrounded by nature helped me disconnect from my daily worries. It was a rejuvenating experience. I think it is important to preserve these natural habitats for future generations to enjoy.",
        "word_count": 99,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 6,
        "vocab_reason": "[LR7] flexible use: 'dense forest', 'breathtaking', 'crisp', 'winding trail', 'therapeutic', 'delightful', 'disconnect', 'rejuvenating', 'preserve', 'habitats'.",
        "grammar_reason": "[GRA6] Mix of structures. Errors: 'Which was delightful' (Refers to plural events, maybe ok). generally accurate but simple connectors. Meaning clear.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v7_g6_0769",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a cafe you like.",
        "transcript_cleaned": "I frequently visit a cozy cafe called 'The Bean' which is just around the corner from my office. It has a rustic interior with wooden furniture and soft lighting. The barista makes excellent cappuccino with intricate latte art. I usually go there to work on my laptop because they have fast Wi-Fi. The pastries are also delicious, especially the almond croissants. The staff are attentive and friendly, remembering my order every time. It is a great place to unwind and people-watch. The ambiance is very welcoming, making it my favorite spot to escape the hustle and bustle.",
        "word_count": 101,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 6,
        "vocab_reason": "[LR7] flexible use: 'frequently', 'rustic interior', 'barista', 'intricate', 'pastries', 'attentive', 'unwind', 'ambiance', 'hustle and bustle'.",
        "grammar_reason": "[GRA6] Mix of structures. Errors: 'Which is just around' ok. 'Staff are' ok. Simple sentences dominant. Meaning clear.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v7_g6_0770",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a rule at your school.",
        "transcript_cleaned": "In my high school, there was a strict rule about mobile phones. We were prohibited from using them during class hours. If a teacher saw a phone, they would confiscate it immediately. This rule was implemented to minimize distractions and ensure students focused on learning. I remember one time my phone rang during a test, and I was terrified. I understand why the rule existed, but sometimes it felt too rigid. Nowadays, phones are used for educational purposes, so the rules might have changed. Discipline is important, but flexibility is also needed in modern education.",
        "word_count": 100,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 6,
        "vocab_reason": "[LR7] flexible use: 'prohibited', 'confiscate', 'implemented', 'minimize distractions', 'terrified', 'rigid', 'educational purposes', 'flexibility'.",
        "grammar_reason": "[GRA6] Mix of structures. Errors: 'Rules might have changed' ok. 'Discipline is important' ok. generally correct. Meaning clear.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    # --- V7/G8 (771-775) ---
    {
        "sample_id": "syn_p2_v7_g8_0771",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a traditional festival.",
        "transcript_cleaned": "I would like to describe the Lantern Festival, which is celebrated in my country. It marks the end of the Lunar New Year festivities. During this time, people hang colorful lanterns in the streets and parks. It is a symbol of letting go of the past and welcoming the new future. Families gather to eat sweet rice balls, which signify reunion and harmony. I particularly enjoy the dragon dances, which are performed with great energy and skill. The atmosphere is festive and vibrant. It is a time when the community comes together to celebrate our heritage. I believe such traditions are vital for preserving our cultural identity.",
        "word_count": 108,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 8,
        "vocab_reason": "[LR7] 'Festivities', 'symbol', 'harmony', 'dragon dances', 'vibrant', 'heritage', 'preserving'. Good range.",
        "grammar_reason": "[GRA8] 'Which is celebrated' (Relative). 'Marks the end' (Simple present). 'Letting go of...' (Gerund phrase). 'Which signify reunion' (Relative). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v7_g8_0772",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a choice you made.",
        "transcript_cleaned": "I had to make a significant choice when I finished high school regarding my major. I was torn between studying engineering and literature. My parents wanted me to choose engineering because of the job prospects. However, I have always been passionate about reading and writing. After much contemplation, I decided to follow my heart and study literature. It was a risky decision, but I do not regret it. The course has been intellectually stimulating and has broadened my horizons. I believe that enjoying what you study is crucial for success. This choice has shaped who I am today.",
        "word_count": 100,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 8,
        "vocab_reason": "[LR7] 'Significant choice', 'torn between', 'prospects', 'passionate', 'contemplation', 'intellectually stimulating', 'broadened my horizons'.",
        "grammar_reason": "[GRA8] 'Regarding my major' (Participle). 'Wanted me to choose' (Verb pattern). 'After much contemplation' (Prepositional phrase). 'Crucial for success' (Adj phrase). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v7_g8_0773",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a family member you admire.",
        "transcript_cleaned": "I greatly admire my grandfather, who is the most resilient person I know. He grew up in a very poor village and had to work from a young age. Despite the hardships, he never complained and always prioritized his family. He taught himself how to read and write, eventually becoming a successful businessman. His determination and work ethic are truly inspiring to me. He is also very generous, always helping neighbors in need. Whenever I face a challenge, I think of his struggles and it gives me strength. He is the pillar of our family.",
        "word_count": 99,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 8,
        "vocab_reason": "[LR7] 'Resilient', 'hardships', 'prioritized', 'determination', 'work ethic', 'inspiring', 'generous', 'pillar'.",
        "grammar_reason": "[GRA8] 'Who is the most...' (Relative). 'Despite the hardships' (Concessive). 'Eventually becoming' (Participle). 'Whenever I face' (Time clause). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v7_g8_0774",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a game you played with others.",
        "transcript_cleaned": "I used to play a board game called Monopoly with my siblings every weekend. It is a game of strategy and luck where you buy and trade properties. We often got very competitive, which sometimes led to arguments. However, it was all in good fun. The game taught me basic financial concepts like budgeting and investment. I remember feeling triumphant when I won and frustrated when I went bankrupt. It was a great way to bond with my family without using technology. Those game nights are some of my fondest childhood memories.",
        "word_count": 96,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 8,
        "vocab_reason": "[LR7] 'Strategy', 'competitive', 'financial concepts', 'budgeting', 'investment', 'triumphant', 'bankrupt', 'bond'.",
        "grammar_reason": "[GRA8] 'Called Monopoly' (Participle). 'Where you buy' (Relative). 'Which sometimes led' (Relative). 'Without using technology' (Preposition + Gerund). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v7_g8_0775",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a painting or photo in your house.",
        "transcript_cleaned": "There is a large oil painting in our hallway that depicts a storm at sea. It shows a small boat battling huge waves under a dark, cloudy sky. The artist used dark colors to create a mood of danger and drama. I am fascinated by the detail of the water and the expression of the sailors. It was a gift from my uncle who is an art collector. To me, the painting symbolizes resilience in the face of adversity. It reminds me that even in difficult times, we must keep going. It is a very powerful image.",
        "word_count": 100,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 8,
        "vocab_reason": "[LR7] 'Depicts', 'battling', 'mood', 'drama', 'fascinated', 'collector', 'symbolizes resilience', 'adversity'.",
        "grammar_reason": "[GRA8] 'That depicts a storm' (Relative). 'Battling huge waves' (Participle). 'To create a mood' (Infinitive). 'Who is an art collector' (Relative). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
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

        # Micro flaws
        sample["micro_flaws"] = []

        # Input/Output construction
        sample["input"] = f"Part: {sample['part']}\nQuestion: {sample['question']}\n\nTranscript: {sample['transcript_cleaned']}\n\nWord Count: {sample['word_count']} words\nResponse Type: {sample['response_type']}"

        output_text = f"## Vocabulary (Lexical Resource): Band {sample['vocabulary']}\n\n**Reasoning:** {sample['vocab_reason']}\n\n>Band {sample['vocabulary']-1}: ...\n\nNot Band {sample['vocabulary']+1}: ...\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band {sample['grammar']}\n\n**Reasoning:** {sample['grammar_reason']}\n\n>Band {sample['grammar']-1}: ...\n\nNot Band {sample['grammar']+1}: ...\n\n**Micro flaws identified:**\n- None."

        sample["output"] = output_text

        f.write(json.dumps(sample) + '\n')
