import json
import os

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_18_p2.jsonl"

samples = [
    # --- V6/G6 (876-880) ---
    {
        "sample_id": "syn_p2_v6_g6_0876",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a type of weather you like.",
        "transcript_cleaned": "I enjoy sunny weather the most, especially in spring. The temperature is mild, not too hot or cold. I like seeing blue skies and flowers blooming. It makes me feel cheerful and optimistic. When it is sunny, I can go outside and do activities. I often go for a bike ride or have a picnic in the park. The sunshine is good for health too. I prefer sunny days over rainy ones because I can be more active.",
        "word_count": 89,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 6,
        "vocab_reason": "[LR6] 'Mild', 'blooming', 'cheerful', 'optimistic', 'activities', 'picnic'. Good range.",
        "grammar_reason": "[GRA6] 'Seeing blue skies' (Gerund). 'Makes me feel' (Causative). 'Prefer... over' (Preposition). Correct simple/compound sentences.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v6_g6_0877",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a library you visit.",
        "transcript_cleaned": "I often go to the public library near my house. It is a quiet place with many shelves of books. I go there to study and borrow novels. The librarians are helpful if you need to find something. I like the atmosphere because everyone is reading. There are computers available for use too. I sometimes meet my friends there to work on group projects. It is free to join, which is great for students like me.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 6,
        "vocab_reason": "[LR6] 'Public library', 'shelves', 'librarians', 'atmosphere', 'projects', 'free to join'. Good range.",
        "grammar_reason": "[GRA6] 'If you need' (Conditional). 'Because everyone is reading' (Reason). 'Which is great' (Relative). Correct structures.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v6_g6_0878",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a polite person you know.",
        "transcript_cleaned": "My friend Sarah is very polite. She always says 'please' and 'thank you'. She respects older people and listens carefully when they speak. I remember one time she held the door open for a stranger carrying heavy bags. Everyone likes her because she has good manners. She never interrupts others during a conversation. I try to learn from her behavior. Being polite makes people feel comfortable around you. It is a good quality to have.",
        "word_count": 83,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 6,
        "vocab_reason": "[LR6] 'Respects', 'listens carefully', 'manners', 'interrupts', 'conversation', 'behavior', 'quality'. Good range.",
        "grammar_reason": "[GRA6] 'When they speak' (Time clause). 'Carrying heavy bags' (Participle). 'Makes people feel' (Causative). Correct structures.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v6_g6_0879",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task you finished.",
        "transcript_cleaned": "I had to write a long essay for my English class last month. The topic was about global warming, which was difficult. I spent many hours researching on the internet. I had to organize my ideas and write clearly. It took me a week to finish it. I was worried about my grammar, so I checked it many times. When I submitted it, I felt relieved. My teacher gave me a good grade. I was proud of my hard work.",
        "word_count": 89,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 6,
        "vocab_reason": "[LR6] 'Essay', 'global warming', 'researching', 'organize', 'submitted', 'relieved', 'grade'. Good range.",
        "grammar_reason": "[GRA6] 'Which was difficult' (Relative). 'Researching on' (Gerund). 'To finish it' (Infinitive). 'So I checked' (Result). Correct structures.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v6_g6_0880",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a crowded place you dislike.",
        "transcript_cleaned": "I really dislike going to the supermarket on weekends. It is always crowded with shoppers. The aisles are narrow, and people push their carts everywhere. It is noisy and stressful to find what I need. I often have to wait in long lines at the checkout. The staff looks tired and busy. I prefer shopping on weekdays when it is quieter. Crowded places make me feel anxious. I try to avoid them if possible.",
        "word_count": 83,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 6,
        "vocab_reason": "[LR6] 'Shoppers', 'aisles', 'carts', 'checkout', 'staff', 'quieter', 'anxious', 'avoid'. Good range.",
        "grammar_reason": "[GRA6] 'To find what I need' (Infinitive + Noun clause). 'When it is quieter' (Time clause). 'Make me feel' (Causative). Correct structures.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    # --- V7/G7 (881-890) ---
    {
        "sample_id": "syn_p2_v7_g7_0881",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a skill you learned.",
        "transcript_cleaned": "I learned how to edit videos last year, which has become a useful skill. I started by watching tutorials on YouTube. The software was complicated at first, with many tools and effects. I practiced editing clips from my holidays. I learned how to cut scenes, add music, and insert text. It requires creativity and attention to detail. Now I can make professional-looking videos for my social media. It is a time-consuming process, but the result is rewarding.",
        "word_count": 87,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Tutorials', 'complicated', 'clips', 'insert text', 'creativity', 'attention to detail', 'professional-looking', 'time-consuming'. Sophisticated.",
        "grammar_reason": "[GRA7] 'Which has become' (Relative). 'By watching tutorials' (Preposition + Gerund). 'How to cut' (Noun clause). Accurate complex sentences.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0882",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place.",
        "transcript_cleaned": "I visited the Great Wall of China a few years ago. It is an ancient fortification built to protect the empire. The structure is massive, stretching across mountains and valleys. Walking on the wall was physically demanding but exhilarating. The view from the watchtowers was breathtaking. I could imagine the soldiers who guarded it centuries ago. It is a symbol of Chinese history and perseverance. The preservation of such a site is remarkable. It was an unforgettable experience.",
        "word_count": 87,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Fortification', 'empire', 'massive', 'physically demanding', 'exhilarating', 'watchtowers', 'perseverance', 'preservation'. Sophisticated.",
        "grammar_reason": "[GRA7] 'Built to protect' (Participle). 'Stretching across' (Participle). 'Who guarded it' (Relative). Accurate complex sentences.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0883",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you gave.",
        "transcript_cleaned": "I gave a handmade photo album to my best friend for her wedding. I spent weeks collecting pictures of us from childhood to now. I decorated each page with stickers and wrote captions. I wanted it to be a sentimental gift that she could cherish. When she opened it, she started crying tears of joy. It was a meaningful gesture to show our friendship. Gifts don't have to be expensive to be valuable. Thoughtfulness matters more.",
        "word_count": 85,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Handmade', 'collecting', 'captions', 'sentimental', 'cherish', 'tears of joy', 'gesture', 'thoughtfulness'. Sophisticated.",
        "grammar_reason": "[GRA7] 'Collecting pictures' (Participle). 'That she could cherish' (Relative). 'When she opened it' (Time clause). Accurate complex sentences.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0884",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a famous person you admire.",
        "transcript_cleaned": "I admire Michelle Obama, the former First Lady of the United States. She is an intelligent and articulate woman who advocates for education and health. I read her autobiography, which was very inspiring. She overcame many obstacles to achieve success. Her speeches are powerful and motivate young girls around the world. I respect her dignity and grace under pressure. She uses her platform to make a positive impact. She is a role model for leadership and compassion.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Former First Lady', 'articulate', 'advocates', 'autobiography', 'inspiring', 'obstacles', 'dignity', 'platform', 'compassion'. Sophisticated.",
        "grammar_reason": "[GRA7] 'Who advocates for' (Relative). 'Which was very inspiring' (Relative). 'To achieve success' (Infinitive). Accurate complex sentences.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0885",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a noisy place you dislike.",
        "transcript_cleaned": "I dislike waiting at the train station during rush hour. It is incredibly noisy with announcements and crowds of commuters. The sound of trains arriving and departing is deafening. People are rushing everywhere, bumping into each other. It is chaotic and stressful. I often wear headphones to block out the noise. The lack of personal space makes me uncomfortable. I prefer traveling at off-peak times when it is quieter. Noise pollution is a real problem in cities.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Rush hour', 'commuters', 'deafening', 'chaotic', 'stressful', 'block out', 'personal space', 'off-peak times'. Sophisticated.",
        "grammar_reason": "[GRA7] 'Arriving and departing' (Participle). 'Bumping into each other' (Participle). 'When it is quieter' (Time clause). Accurate complex sentences.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0886",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a movie character.",
        "transcript_cleaned": "I like the character of Sherlock Holmes from the TV series. He is a brilliant detective with exceptional observation skills. He solves complex crimes that baffle the police. Although he can be arrogant and socially awkward, his intellect is undeniable. I enjoy watching how he deduces the truth from small details. His partnership with Dr. Watson adds a human element to the story. The character is fascinating because of his unique mind. He is iconic in literature and film.",
        "word_count": 87,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Brilliant detective', 'exceptional', 'baffle', 'arrogant', 'socially awkward', 'intellect', 'deduces', 'iconic'. Sophisticated.",
        "grammar_reason": "[GRA7] 'That baffle the police' (Relative). 'Although he can be' (Concessive). 'How he deduces' (Noun clause). Accurate complex sentences.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0887",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you were late.",
        "transcript_cleaned": "I was late for a job interview last month, which was a nightmare. I woke up on time, but there was a traffic jam on the highway. The cars were not moving for an hour. I felt panicked and stressed. I called the company to apologize and explain the situation. Thankfully, they were understanding and rescheduled the meeting. I arrived later, feeling embarrassed but relieved. I learned to always leave extra time for important appointments.",
        "word_count": 85,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Nightmare', 'traffic jam', 'panicked', 'apologize', 'rescheduled', 'embarrassed', 'relieved', 'appointments'. Sophisticated.",
        "grammar_reason": "[GRA7] 'Which was a nightmare' (Relative). 'To apologize' (Infinitive). 'Feeling embarrassed' (Participle). Accurate complex sentences.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0888",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of furniture.",
        "transcript_cleaned": "I have a comfortable armchair in my living room that I love. It is upholstered in soft velvet and has a high back. I bought it at a vintage store. It is the perfect spot for reading or taking a nap. The color is deep blue, which matches my curtains. It adds a touch of elegance to the room. I spend many evenings sitting there with a cup of tea. It is my favorite place to unwind.",
        "word_count": 87,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Upholstered', 'velvet', 'vintage', 'elegance', 'unwind'. Sophisticated.",
        "grammar_reason": "[GRA7] 'That I love' (Relative). 'Which matches my curtains' (Relative). 'Sitting there' (Participle). Accurate complex sentences.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0889",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a sport you played.",
        "transcript_cleaned": "I used to play basketball in high school. It is a team sport that requires coordination and stamina. We practiced three times a week after classes. I enjoyed the camaraderie with my teammates. We participated in local tournaments and won a few trophies. The game is fast-paced and exciting. It taught me the value of teamwork and discipline. Although I don't play much now, I still watch games on TV. It brings back fond memories.",
        "word_count": 83,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Coordination', 'stamina', 'camaraderie', 'tournaments', 'trophies', 'fast-paced', 'discipline', 'fond memories'. Sophisticated.",
        "grammar_reason": "[GRA7] 'That requires coordination' (Relative). 'After classes' (Prepositional). 'Although I don't play' (Concessive). Accurate complex sentences.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v7_g7_0890",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a website you like.",
        "transcript_cleaned": "I frequently use a website called Pinterest for inspiration. It allows users to pin images and create boards. I use it to find ideas for home decoration and recipes. The visual layout is very appealing and easy to navigate. I can spend hours scrolling through beautiful photos. It helps me organize my creative projects. I also share my own ideas with others. It is a great resource for anyone who likes design and crafts.",
        "word_count": 82,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 7,
        "vocab_reason": "[LR7] 'Inspiration', 'pin images', 'decoration', 'visual layout', 'appealing', 'navigate', 'resource'. Sophisticated.",
        "grammar_reason": "[GRA7] 'Called Pinterest' (Participle). 'To find ideas' (Infinitive). 'Who likes design' (Relative). Accurate complex sentences.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    # --- V8/G8 (891-900) ---
    {
        "sample_id": "syn_p2_v8_g8_0891",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a memorable event.",
        "transcript_cleaned": "Attending my graduation ceremony was a momentous occasion in my life. It marked the culmination of years of hard work and dedication. The atmosphere was electric with excitement and pride. Walking across the stage to receive my diploma felt surreal. I was surrounded by my family and friends who had supported me throughout. The speeches were inspiring, urging us to make a difference in the world. It was a bittersweet farewell to student life but an exciting beginning to my career. I will cherish that day forever.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Momentous occasion', 'culmination', 'dedication', 'electric', 'surreal', 'bittersweet farewell', 'cherish'. Very sophisticated.",
        "grammar_reason": "[GRA8] 'Walking across the stage' (Gerund subject). 'Who had supported me' (Relative + Past Perfect). 'Urging us to make' (Participle). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0892",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a creative person.",
        "transcript_cleaned": "I am constantly amazed by the creativity of my friend, Liam, who is a graphic designer. He has an innate ability to visualize abstract concepts. His designs are innovative and aesthetically pleasing. He can transform a simple idea into a visual masterpiece. I admire his proficiency with digital tools and his artistic flair. He is always experimenting with new techniques and styles. His work inspires me to think outside the box. He proves that creativity is not just a talent but a skill honed through practice.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Innate ability', 'visualize', 'abstract concepts', 'innovative', 'aesthetically pleasing', 'proficiency', 'artistic flair', 'honed'. Very sophisticated.",
        "grammar_reason": "[GRA8] 'Who is a graphic designer' (Relative). 'Transform... into' (Verb pattern). 'Not just... but' (Correlative). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0893",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a traditional meal.",
        "transcript_cleaned": "In my culture, we have a traditional dish called 'Biryani' which is a flavorful rice dish. It is prepared with aromatic spices, basmati rice, and marinated meat. The cooking process is intricate, involving layering the ingredients in a pot. The saffron gives it a distinct yellow color and fragrance. It is usually served at weddings and celebrations. Eating it evokes a sense of nostalgia and community. The blend of textures and tastes is exquisite. It is a culinary heritage passed down through generations.",
        "word_count": 91,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Flavorful', 'aromatic spices', 'marinated', 'intricate', 'layering', 'distinct', 'fragrance', 'nostalgia', 'exquisite', 'culinary heritage'. Very sophisticated.",
        "grammar_reason": "[GRA8] 'Called Biryani' (Participle). 'Involving layering' (Participle + Gerund). 'Passed down through' (Participle). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0894",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "Choosing to study abroad was a pivotal decision that shaped my trajectory. I was torn between staying in my comfort zone and exploring new horizons. The prospect of living alone in a foreign country was daunting. However, I realized the potential for personal growth was immense. I weighed the pros and cons meticulously before committing. Leaving my family was heart-wrenching, but necessary for my independence. Looking back, it was the most transformative experience of my life. It broadened my perspective and resilience.",
        "word_count": 91,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Pivotal decision', 'trajectory', 'torn between', 'comfort zone', 'horizons', 'daunting', 'meticulously', 'heart-wrenching', 'transformative', 'resilience'. Very sophisticated.",
        "grammar_reason": "[GRA8] 'Choosing to study' (Gerund subject). 'Staying... and exploring' (Gerunds). 'Living alone' (Gerund phrase). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0895",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of technology.",
        "transcript_cleaned": "My smartwatch has become an indispensable gadget in my daily life. It tracks my fitness metrics, such as heart rate and steps, with precision. I can receive notifications instantly without checking my phone. The sleek design and customizable interface are very appealing. It motivates me to stay active by setting daily goals. The integration with other devices is seamless. Although some may see it as a luxury, I find it to be a productivity tool. It has streamlined how I manage my time and health.",
        "word_count": 92,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Indispensable gadget', 'metrics', 'precision', 'sleek design', 'customizable interface', 'integration', 'seamless', 'productivity tool', 'streamlined'. Very sophisticated.",
        "grammar_reason": "[GRA8] 'Such as heart rate' (Appositive). 'Without checking' (Preposition + Gerund). 'By setting' (Preposition + Gerund). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0896",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a place near water.",
        "transcript_cleaned": "I find solace in visiting a secluded cove along the coastline. The rugged cliffs provide a dramatic backdrop to the azure waters. The rhythmic sound of waves crashing against the rocks is meditative. I often go there to reflect and escape the urban chaos. The salty sea breeze is invigorating and fresh. Sometimes I spot dolphins frolicking in the distance. It is a pristine environment untouched by commercial tourism. This connection with nature is essential for my mental well-being.",
        "word_count": 88,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Solace', 'secluded cove', 'rugged cliffs', 'dramatic backdrop', 'azure', 'rhythmic', 'meditative', 'invigorating', 'frolicking', 'pristine', 'untouched'. Very sophisticated.",
        "grammar_reason": "[GRA8] 'Crashing against the rocks' (Participle). 'To reflect and escape' (Infinitive). 'Untouched by commercial tourism' (Participle). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0897",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a rule you agree with.",
        "transcript_cleaned": "I strongly support the prohibition of smoking in public indoor spaces. This regulation has significantly improved public health by reducing exposure to second-hand smoke. It creates a more hygienic and pleasant environment for everyone. I recall how restaurants used to be filled with acrid smoke. Now, dining out is a much more enjoyable experience. While smokers may feel restricted, the collective well-being takes precedence. It is a logical and necessary measure to protect citizens from respiratory diseases. I believe it is a sign of a progressive society.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Prohibition', 'regulation', 'exposure', 'hygienic', 'acrid smoke', 'collective well-being', 'precedence', 'respiratory diseases', 'progressive'. Very sophisticated.",
        "grammar_reason": "[GRA8] 'By reducing exposure' (Preposition + Gerund). 'Used to be filled' (Passive). 'To protect citizens' (Infinitive). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0898",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a memorable photo.",
        "transcript_cleaned": "I treasure a candid photograph taken during a family reunion. It captures a spontaneous moment of laughter shared between four generations. The lighting is soft and natural, illuminating the joy on everyone's faces. It is not technically perfect, but the emotion it conveys is profound. Looking at it transports me back to that sunny afternoon. It serves as a poignant reminder of the passage of time. As family members age, this image becomes increasingly valuable. It encapsulates the essence of familial bond.",
        "word_count": 90,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Treasure', 'candid', 'spontaneous', 'illuminating', 'technically perfect', 'conveys', 'profound', 'transports', 'poignant reminder', 'encapsulates', 'familial bond'. Very sophisticated.",
        "grammar_reason": "[GRA8] 'Taken during...' (Participle). 'Shared between...' (Participle). 'Looking at it' (Gerund subject). 'As family members age' (Time clause). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0899",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical figure.",
        "transcript_cleaned": "I have great admiration for Mahatma Gandhi, a pivotal figure in the fight for India's independence. His philosophy of non-violent resistance inspired civil rights movements globally. He advocated for peace and unity in a time of great conflict. His humble lifestyle and dedication to truth were exemplary. He demonstrated that moral force is stronger than physical force. His legacy continues to influence political thought today. He is a symbol of resilience and integrity. His life teaches us the power of conviction.",
        "word_count": 89,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Admiration', 'pivotal figure', 'philosophy', 'non-violent resistance', 'advocated', 'exemplary', 'moral force', 'legacy', 'conviction'. Very sophisticated.",
        "grammar_reason": "[GRA8] 'In the fight for' (Prepositional). 'Demonstrated that...' (Noun clause). 'To influence' (Infinitive). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v8_g8_0900",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "My noise-canceling headphones are an incredibly useful tool for concentration. They use advanced technology to eliminate ambient noise. When I wear them, I can focus entirely on my work or studies. They are particularly helpful in noisy environments like cafes or airplanes. The audio quality is crisp and immersive. I also use them to listen to podcasts and audiobooks. They have become an essential part of my daily gear. Without them, I would find it difficult to maintain productivity in a distracting world.",
        "word_count": 91,
        "response_type": "long_turn",
        "vocabulary": 8, "grammar": 8,
        "vocab_reason": "[LR8] 'Noise-canceling', 'concentration', 'ambient noise', 'immersive', 'podcasts', 'essential part', 'productivity', 'distracting world'. Very sophisticated.",
        "grammar_reason": "[GRA8] 'To eliminate' (Infinitive). 'When I wear them' (Time clause). 'Like cafes' (Preposition). Error-free.",
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
