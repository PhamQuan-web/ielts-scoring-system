import json
import os

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_16_p2.jsonl"

samples = [
    # --- V7/G8 (776-780) ---
    {
        "sample_id": "syn_p2_v7_g8_0776",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a place you go to relax.",
        "transcript_cleaned": "My favorite place to relax is a small park near the river in my hometown. It is a tranquil spot surrounded by willow trees that sway in the breeze. I go there to escape the noise and pollution of the city. I often bring a blanket and a book, enjoying the peaceful atmosphere. The sound of the flowing water is incredibly soothing and helps me clear my mind. Sometimes, I watch the boats passing by, imagining where they are going. It is my personal sanctuary where I can rejuvenate my spirit.",
        "word_count": 96,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 8,
        "vocab_reason": "[LR7] 'Tranquil spot', 'sway in the breeze', 'escape', 'pollution', 'soothing', 'sanctuary', 'rejuvenate'.",
        "grammar_reason": "[GRA8] 'Surrounded by willow trees' (Participle). 'That sway' (Relative). 'Enjoying the peaceful atmosphere' (Participle). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v7_g8_0777",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place you visited.",
        "transcript_cleaned": "Last year, I visited the ancient ruins of Machu Picchu in Peru. It was a breathtaking experience to see the stone structures built on top of the mountains. The guide explained how the Incas constructed the city without modern tools. I was amazed by the precision of the stonework and the complex terracing system. The view of the surrounding peaks was absolutely spectacular. Walking through the ruins felt like stepping back in time. It made me appreciate the ingenuity of ancient civilizations. It is a memory I will cherish forever.",
        "word_count": 97,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 8,
        "vocab_reason": "[LR7] 'Ancient ruins', 'breathtaking', 'constructed', 'precision', 'terracing system', 'spectacular', 'ingenuity', 'civilizations'.",
        "grammar_reason": "[GRA8] 'Built on top' (Participle). 'How the Incas constructed' (Noun clause). 'Walking through the ruins' (Gerund subject). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v7_g8_0778",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a skill you want to learn.",
        "transcript_cleaned": "I have always wanted to learn how to play the piano. I love the sound of classical music, especially pieces by Chopin and Beethoven. I think being able to create such beautiful melodies would be very fulfilling. It requires a lot of discipline and practice to master the technique. I plan to take lessons once I have more free time. I know it will be challenging to coordinate my hands, but I am determined. Playing an instrument is also a great way to relieve stress and express emotions.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 8,
        "vocab_reason": "[LR7] 'Classical music', 'fulfilling', 'discipline', 'master the technique', 'coordinate', 'determined', 'relieve stress', 'express emotions'.",
        "grammar_reason": "[GRA8] 'Being able to create' (Gerund phrase). 'Especially pieces by' (Appositive). 'Once I have' (Time clause). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v7_g8_0779",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a memorable journey.",
        "transcript_cleaned": "A journey I will never forget was a road trip across the United States. We drove from New York to California, passing through diverse landscapes. I saw vast deserts, majestic mountains, and endless cornfields. We stopped at many national parks to hike and camp. The most memorable part was seeing the Grand Canyon at sunrise. The colors of the rocks were changing every minute. It was a humbling experience to witness the scale of nature. The trip taught me to appreciate the beauty of the world and the joy of exploration.",
        "word_count": 99,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 8,
        "vocab_reason": "[LR7] 'Road trip', 'diverse landscapes', 'vast deserts', 'majestic', 'humbling experience', 'scale of nature', 'exploration'.",
        "grammar_reason": "[GRA8] 'Passing through diverse landscapes' (Participle). 'To hike and camp' (Infinitive). 'Seeing the Grand Canyon' (Gerund phrase). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v7_g8_0780",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend you like to spend time with.",
        "transcript_cleaned": "I love spending time with my best friend, Sarah, who is incredibly funny and supportive. We have known each other since elementary school and share many common interests. She always knows how to make me laugh when I am feeling down. We enjoy going to cafes, watching movies, and just talking about life. She is a great listener and gives honest advice. I value her friendship because she is loyal and trustworthy. Even if we don't see each other for a while, our bond remains strong. She is like a sister to me.",
        "word_count": 101,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 8,
        "vocab_reason": "[LR7] 'Supportive', 'common interests', 'feeling down', 'loyal', 'trustworthy', 'bond remains strong'.",
        "grammar_reason": "[GRA8] 'Who is incredibly funny' (Relative). 'Since elementary school' (Time phrase). 'When I am feeling down' (Time clause). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    # --- V8/G7 (781-790) ---
    {
        "sample_id": "syn_p2_v8_g7_0781",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a conversation you had.",
        "transcript_cleaned": "I had a stimulating conversation with a professor about climate change last week. We discussed the catastrophic impact of global warming on coastal cities. He articulated his points with great clarity, explaining the scientific consensus. I found his insights to be profound and alarming. We debated the efficacy of renewable energy solutions like solar and wind power. Although the topic was grim, the exchange of ideas was intellectually invigorating. It made me realize the urgency of the situation. I left the discussion feeling more informed and determined to reduce my carbon footprint.",
        "word_count": 99,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 7,
        "vocab_reason": "[LR8] 'Stimulating', 'catastrophic impact', 'articulated', 'consensus', 'profound', 'efficacy', 'invigorating', 'carbon footprint'. sophisticated.",
        "grammar_reason": "[GRA7] 'Explaining the scientific consensus' (Participle). 'I found his insights to be' (Infinitive). Generally error-free complex structures.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v8_g7_0782",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of news you heard.",
        "transcript_cleaned": "I recently heard a heartwarming news story about a community rallying to save a local library. The library was facing closure due to budget cuts, which caused an outcry among residents. People organized fundraising events and started a petition to convince the council. It was inspiring to witness the collective effort of ordinary citizens. Eventually, they raised enough funds to keep the library open for another year. This demonstrates the power of grassroots activism. It restored my faith in humanity and the importance of preserving public institutions.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 7,
        "vocab_reason": "[LR8] 'Rallying', 'facing closure', 'budget cuts', 'outcry', 'petition', 'collective effort', 'grassroots activism', 'institutions'. sophisticated.",
        "grammar_reason": "[GRA7] 'Due to budget cuts' (Prepositional). 'Which caused an outcry' (Relative). 'To convince the council' (Infinitive). Generally accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v8_g7_0783",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a meal you had.",
        "transcript_cleaned": "I enjoyed a sumptuous meal at a new restaurant that specializes in molecular gastronomy. The dishes were visually stunning, resembling works of art rather than food. One course involved edible foam that tasted like sea spray. The flavors were exquisite and unexpected, challenging my palate. The chef used innovative techniques to transform familiar ingredients into something novel. It was a culinary adventure that engaged all my senses. Although it was exorbitant, the experience was worth every penny. It redefined my understanding of what fine dining can be.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 7,
        "vocab_reason": "[LR8] 'Sumptuous', 'molecular gastronomy', 'visually stunning', 'exquisite', 'palate', 'innovative techniques', 'culinary adventure', 'exorbitant'. sophisticated.",
        "grammar_reason": "[GRA7] 'That specializes in' (Relative). 'Resembling works of art' (Participle). 'Transform... into' (Verb pattern). Generally accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v8_g7_0784",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a subject you studied.",
        "transcript_cleaned": "I studied psychology at university, which I found to be a fascinating discipline. It delves into the complexities of human behavior and cognitive processes. We explored theories regarding personality, memory, and social interaction. I was particularly intrigued by abnormal psychology and mental disorders. The coursework involved conducting experiments and analyzing statistical data. It required critical thinking and empathy to understand the human mind. This knowledge has been invaluable in my personal and professional life. It helps me interpret the actions of others with greater nuance and compassion.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 7,
        "vocab_reason": "[LR8] 'Discipline', 'delves into', 'complexities', 'cognitive processes', 'intrigued', 'abnormal psychology', 'invaluable', 'nuance', 'compassion'. sophisticated.",
        "grammar_reason": "[GRA7] 'Which I found to be' (Relative). 'Regarding personality' (Participle). 'Involved conducting' (Gerund). Generally accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v8_g7_0785",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a challenge you faced.",
        "transcript_cleaned": "Facing a fear of public speaking was a formidable challenge I had to overcome. I used to suffer from debilitating anxiety whenever I had to present in front of an audience. My heart would palpitate and my mind would go blank. To conquer this, I joined a local toastmasters club. It provided a supportive environment to practice and receive constructive feedback. Gradually, through exposure and preparation, I desensitized myself to the fear. Now, I can deliver speeches with poise and confidence. It was a transformative journey of self-improvement.",
        "word_count": 97,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 7,
        "vocab_reason": "[LR8] 'Formidable challenge', 'debilitating anxiety', 'palpitate', 'conquer', 'supportive environment', 'constructive feedback', 'desensitized', 'poise', 'transformative'. sophisticated.",
        "grammar_reason": "[GRA7] 'I had to overcome' (Relative). 'Whenever I had to present' (Time clause). 'To conquer this' (Infinitive). Generally accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v8_g7_0786",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe an animal you like.",
        "transcript_cleaned": "I am captivated by the majestic nature of the African elephant. They are sentient beings with complex social structures and deep emotional bonds. I read that they mourn their dead, which indicates a high level of consciousness. Their intelligence is remarkable; they can use tools and solve problems. Unfortunately, they are vulnerable to poaching for their ivory tusks. Conservation efforts are crucial to prevent their extinction. Observing them in the wild would be a profound privilege. They embody strength and wisdom in the animal kingdom.",
        "word_count": 91,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 7,
        "vocab_reason": "[LR8] 'Captivated', 'majestic', 'sentient beings', 'emotional bonds', 'mourn', 'consciousness', 'vulnerable', 'poaching', 'conservation', 'profound privilege'. sophisticated.",
        "grammar_reason": "[GRA7] 'Which indicates' (Relative). 'To prevent their extinction' (Infinitive). 'Observing them... would be' (Gerund subject). Generally accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v8_g7_0787",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a movie character you like.",
        "transcript_cleaned": "I admire the character of Atticus Finch from the movie 'To Kill a Mockingbird'. He is a principled lawyer who defends a wrongly accused man in the segregated South. His integrity and moral courage are exemplary. He stands up for justice despite the overwhelming prejudice of his community. I find his calm demeanor and wisdom very compelling. He teaches his children valuable lessons about empathy and tolerance. His character represents the best of humanity. Watching him on screen is a poignant reminder of the importance of doing what is right.",
        "word_count": 98,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 7,
        "vocab_reason": "[LR8] 'Principled', 'wrongly accused', 'segregated', 'integrity', 'moral courage', 'exemplary', 'prejudice', 'demeanor', 'compelling', 'poignant reminder'. sophisticated.",
        "grammar_reason": "[GRA7] 'Who defends' (Relative). 'Despite the overwhelming prejudice' (Prepositional phrase). 'Watching him... is' (Gerund subject). Generally accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v8_g7_0788",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical period you like.",
        "transcript_cleaned": "I am fascinated by the Renaissance period in Europe, which was a time of cultural rebirth. It witnessed an explosion of artistic and scientific innovation. Figures like Da Vinci and Michelangelo produced masterpieces that are still revered today. The shift from medieval dogmas to humanism profoundly changed society. It laid the foundation for the modern world. I love studying the architecture and literature of that era. The intellectual curiosity of the time is inspiring. It was a golden age of creativity and exploration.",
        "word_count": 91,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 7,
        "vocab_reason": "[LR8] 'Fascinated', 'cultural rebirth', 'witnessed', 'explosion', 'innovation', 'masterpieces', 'revered', 'dogmas', 'humanism', 'foundation'. sophisticated.",
        "grammar_reason": "[GRA7] 'Which was a time' (Relative). 'That are still revered' (Relative). 'Shift from... to' (Noun phrase). Generally accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v8_g7_0789",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a sport you watch.",
        "transcript_cleaned": "I avidly follow tennis, especially the Grand Slam tournaments. It is a sport that demands exceptional physical endurance and mental fortitude. The strategic duel between two players is captivating to watch. I admire the precision of their shots and their agility on the court. Matches can last for hours, testing the limits of human capability. The etiquette and sportsmanship in tennis are also commendable. Witnessing a comeback from a losing position is exhilarating. It is a graceful yet intense spectacle.",
        "word_count": 89,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 7,
        "vocab_reason": "[LR8] 'Avidly follow', 'endurance', 'mental fortitude', 'strategic duel', 'captivating', 'precision', 'agility', 'capability', 'etiquette', 'commendable', 'exhilarating'. sophisticated.",
        "grammar_reason": "[GRA7] 'Especially the Grand Slam' (Appositive). 'That demands' (Relative). 'Testing the limits' (Participle). Generally accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v8_g7_0790",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a creative activity you do.",
        "transcript_cleaned": "I engage in photography as a creative outlet to express my perspective. I enjoy capturing candid moments and the interplay of light and shadow. It requires a keen eye for composition and detail. Editing the photos allows me to enhance the mood and aesthetic. I often wander through the city streets looking for interesting subjects. It is a meditative process that helps me slow down and observe the world. Sharing my work with others and receiving feedback is gratifying. It transforms mundane scenes into something meaningful.",
        "word_count": 93,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 7,
        "vocab_reason": "[LR8] 'Engage in', 'creative outlet', 'perspective', 'candid moments', 'interplay', 'keen eye', 'composition', 'aesthetic', 'meditative', 'gratifying', 'mundane'. sophisticated.",
        "grammar_reason": "[GRA7] 'Looking for interesting subjects' (Participle). 'Allows me to enhance' (Infinitive). 'Sharing my work... is' (Gerund subject). Generally accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    # --- V8/G9 (791-800) ---
    {
        "sample_id": "syn_p2_v8_g9_0791",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a famous scientist.",
        "transcript_cleaned": "I have immense respect for Marie Curie, a pioneer in the field of radioactivity. Her dedication to science was unparalleled, often working in hazardous conditions. She was the first woman to win a Nobel Prize, which was a monumental achievement in a male-dominated era. Her discoveries revolutionized medicine, particularly in the treatment of cancer. I admire her tenacity and intellect. She sacrificed her health for the advancement of knowledge. Her legacy continues to inspire generations of female scientists. She is a true icon of perseverance.",
        "word_count": 93,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 9,
        "vocab_reason": "[LR8] 'Immense respect', 'pioneer', 'radioactivity', 'unparalleled', 'hazardous', 'monumental achievement', 'revolutionized', 'tenacity', 'legacy', 'perseverance'. sophisticated.",
        "grammar_reason": "[GRA9] 'Often working in...' (Participle). 'To win a Nobel Prize' (Infinitive). 'Which was a monumental achievement' (Relative). Flawless.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g9_0792",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a polluted place.",
        "transcript_cleaned": "I once visited an industrial city that was notorious for its air pollution. A thick smog blanketed the skyline, obscuring the sun. The air quality was hazardous, causing respiratory issues for the inhabitants. It was disheartening to see the environmental degradation caused by unregulated factories. The river was also contaminated with toxic waste. The government has since implemented stricter regulations to mitigate the damage. It served as a stark warning about the consequences of industrialization without sustainability. We must prioritize the health of our planet.",
        "word_count": 92,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 9,
        "vocab_reason": "[LR8] 'Notorious', 'smog', 'blanketed', 'obscuring', 'hazardous', 'respiratory issues', 'disheartening', 'degradation', 'unregulated', 'contaminated', 'mitigate', 'sustainability'. sophisticated.",
        "grammar_reason": "[GRA9] 'That was notorious' (Relative). 'Obscuring the sun' (Participle). 'Caused by unregulated factories' (Participle). Flawless.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g9_0793",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a performance you watched.",
        "transcript_cleaned": "I attended a ballet performance of 'Swan Lake' that was absolutely mesmerizing. The choreography was intricate, requiring immense physical strength and grace. The prima ballerina executed her movements with flawless precision. I was captivated by the emotive power of the music and the storytelling. The costumes and set design were opulent, adding to the magical atmosphere. It was a transcendent experience that evoked deep emotions. The dedication of the dancers was evident in every step. It remains one of the most memorable cultural events I have ever witnessed.",
        "word_count": 95,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 9,
        "vocab_reason": "[LR8] 'Mesmerizing', 'choreography', 'intricate', 'prima ballerina', 'executed', 'flawless precision', 'emotive power', 'opulent', 'transcendent', 'evoked'. sophisticated.",
        "grammar_reason": "[GRA9] 'That was absolutely mesmerizing' (Relative). 'Requiring immense physical strength' (Participle). 'Adding to the magical atmosphere' (Participle). Flawless.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g9_0794",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a successful business.",
        "transcript_cleaned": "I admire a local bakery that has become a thriving business in my community. It started as a small family venture but has expanded due to its reputation for quality. They use organic ingredients and traditional baking methods. The aroma of fresh bread entices customers from down the street. Their success is attributed to their customer-centric approach and innovation. They recently launched a delivery service, which boosted their revenue. It is a testament to how passion and hard work can lead to prosperity. They support the local economy significantly.",
        "word_count": 97,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 9,
        "vocab_reason": "[LR8] 'Thriving business', 'venture', 'reputation', 'organic ingredients', 'entices', 'attributed to', 'customer-centric', 'innovation', 'revenue', 'testament', 'prosperity'. sophisticated.",
        "grammar_reason": "[GRA9] 'That has become' (Relative). 'Started as... but has expanded' (Contrast). 'Which boosted their revenue' (Relative). Flawless.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g9_0795",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a law you would change.",
        "transcript_cleaned": "If I could, I would amend the laws regarding plastic packaging usage. Currently, there is excessive waste generated by single-use plastics in supermarkets. I would propose a legislation that mandates biodegradable alternatives. This would significantly reduce the burden on landfills and our oceans. Although it might incur higher costs for manufacturers, the environmental benefits are paramount. We need to enforce stricter penalties for non-compliance. It is an urgent issue that requires legislative intervention. Promoting a circular economy is essential for a sustainable future.",
        "word_count": 91,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 9,
        "vocab_reason": "[LR8] 'Amend', 'excessive waste', 'single-use plastics', 'legislation', 'mandates', 'biodegradable', 'landfills', 'paramount', 'non-compliance', 'intervention', 'circular economy'. sophisticated.",
        "grammar_reason": "[GRA9] 'If I could, I would amend' (Conditional). 'Generated by single-use plastics' (Participle). 'That mandates' (Relative). Flawless.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g9_0796",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a memorable dinner.",
        "transcript_cleaned": "I recall a memorable dinner I had on a rooftop restaurant in Paris. The panoramic view of the illuminated city was enchanting. We savored a multi-course meal featuring delicacies like foie gras and escargot. The sommelier paired each dish with the perfect wine, enhancing the flavors. The conversation flowed effortlessly, accompanied by the gentle sound of a violin. It was an evening of indulgence and romance. The impeccable service made us feel like royalty. It was a gastronomic experience that satisfied both the stomach and the soul.",
        "word_count": 95,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 9,
        "vocab_reason": "[LR8] 'Panoramic view', 'illuminated', 'enchanting', 'savored', 'delicacies', 'sommelier', 'impeccable', 'gastronomic experience'. sophisticated.",
        "grammar_reason": "[GRA9] 'I had on a rooftop' (Relative). 'Featuring delicacies' (Participle). 'Enhancing the flavors' (Participle). 'Accompanied by...' (Participle). Flawless.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g9_0797",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a valuable item.",
        "transcript_cleaned": "My most valuable possession is a vintage watch inherited from my grandfather. It is a Swiss timepiece with intricate mechanics and a leather strap. Beyond its monetary worth, it holds immense sentimental value. It symbolizes the passage of time and family legacy. I wear it only on special occasions to preserve its condition. The craftsmanship is exquisite, a reminder of a bygone era. It connects me to my roots and history. I intend to pass it down to my children one day, continuing the tradition.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 9,
        "vocab_reason": "[LR8] 'Vintage watch', 'inherited', 'timepiece', 'intricate mechanics', 'monetary worth', 'sentimental value', 'craftsmanship', 'exquisite', 'bygone era'. sophisticated.",
        "grammar_reason": "[GRA9] 'Inherited from my grandfather' (Participle). 'Beyond its monetary worth' (Prepositional phrase). 'Continuing the tradition' (Participle). Flawless.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g9_0798",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a surprising event.",
        "transcript_cleaned": "I was completely taken aback when my friends organized a surprise birthday party for me. I had expected a quiet evening at home, so walking into a room full of people was a shock. They had decorated the house with balloons and streamers. The effort they put into the planning was heartwarming. I felt overwhelmed with gratitude and love. We danced and laughed until the early hours of the morning. It was a delightful deviation from my routine. The spontaneity of the event made it even more special.",
        "word_count": 97,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 9,
        "vocab_reason": "[LR8] 'Taken aback', 'shock', 'heartwarming', 'overwhelmed', 'gratitude', 'delightful deviation', 'routine', 'spontaneity'. sophisticated.",
        "grammar_reason": "[GRA9] 'When my friends organized' (Time clause). 'Had expected... so walking' (Past Perfect + Gerund). 'Put into the planning' (Relative). Flawless.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g9_0799",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical figure.",
        "transcript_cleaned": "I am intrigued by the life of Nelson Mandela, a global icon of peace and reconciliation. He spent decades in prison for fighting against apartheid in South Africa. His resilience in the face of oppression is awe-inspiring. Upon his release, he advocated for forgiveness rather than revenge. He became the first black president of his nation, uniting a divided people. His leadership style was characterized by humility and wisdom. He demonstrated that love is more powerful than hate. His legacy serves as a beacon of hope for the world.",
        "word_count": 97,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 9,
        "vocab_reason": "[LR8] 'Intrigued', 'global icon', 'reconciliation', 'apartheid', 'resilience', 'oppression', 'awe-inspiring', 'advocated', 'uniting', 'beacon of hope'. sophisticated.",
        "grammar_reason": "[GRA9] 'Fighting against apartheid' (Gerund). 'Upon his release' (Prepositional phrase). 'Characterized by humility' (Passive). Flawless.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g9_0800",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a beautiful garden.",
        "transcript_cleaned": "The Botanical Gardens in Singapore is a horticultural masterpiece that I adore. It features a vast array of tropical plants and exotic orchids. The layout is meticulously designed to create a sense of harmony with nature. Walking through the lush greenery is a sensory delight. I particularly enjoy the symphony stage, located on a lake. The vibrant colors and fragrances are intoxicating. It is a UNESCO World Heritage site, recognized for its cultural and scientific value. It provides a green lung in the heart of a bustling metropolis.",
        "word_count": 96,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 9,
        "vocab_reason": "[LR8] 'Horticultural masterpiece', 'adore', 'vast array', 'exotic orchids', 'meticulously designed', 'lush greenery', 'sensory delight', 'intoxicating', 'bustling metropolis'. sophisticated.",
        "grammar_reason": "[GRA9] 'That I adore' (Relative). 'Designed to create' (Infinitive). 'Located on a lake' (Participle). 'Recognized for...' (Participle). Flawless.",
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

        # Micro flaws
        sample["micro_flaws"] = []

        # Input/Output construction
        sample["input"] = f"Part: {sample['part']}\nQuestion: {sample['question']}\n\nTranscript: {sample['transcript_cleaned']}\n\nWord Count: {sample['word_count']} words\nResponse Type: {sample['response_type']}"

        output_text = f"## Vocabulary (Lexical Resource): Band {sample['vocabulary']}\n\n**Reasoning:** {sample['vocab_reason']}\n\n>Band {sample['vocabulary']-1}: ...\n\nNot Band {sample['vocabulary']+1}: ...\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band {sample['grammar']}\n\n**Reasoning:** {sample['grammar_reason']}\n\n>Band {sample['grammar']-1}: ...\n\nNot Band {sample['grammar']+1}: ...\n\n**Micro flaws identified:**\n- None."

        sample["output"] = output_text

        f.write(json.dumps(sample) + '\n')
