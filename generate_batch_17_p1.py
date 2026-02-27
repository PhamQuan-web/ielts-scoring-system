import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_17_p1.jsonl"

samples = [
    # --- V9/G8 (801-810) ---
    {
        "sample_id": "syn_p2_v9_g8_0801",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a wild animal you would like to see.",
        "transcript_cleaned": "I have an unquenchable desire to observe a snow leopard in its natural habitat, specifically in the Himalayas. This elusive predator, often dubbed the 'ghost of the mountains', is a masterpiece of evolution. Its camouflage is impeccable, blending seamlessly with the rocky, snow-dusted terrain. I am fascinated by its solitary nature and the sheer resilience required to survive in such an inhospitable environment. Although sightings are notoriously rare, the prospect of witnessing such a majestic creature in the wild is exhilarating. It would be a profound privilege to see it prowling the crags, embodying the raw, untamed spirit of the wilderness.",
        "word_count": 105,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 8,
        "vocab_reason": "[LR9] 'Unquenchable desire', 'elusive predator', 'dubbed', 'masterpiece of evolution', 'impeccable', 'seamlessly', 'inhospitable', 'notoriously rare', 'profound privilege', 'prowling', 'untamed spirit'. Native-like.",
        "grammar_reason": "[GRA8] 'Often dubbed...' (Participle). 'Blending seamlessly with...' (Participle). 'Required to survive' (Participle). 'Although sightings are...' (Concessive). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g8_0802",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a meaningful conversation.",
        "transcript_cleaned": "I vividly recall a philosophical discourse I had with my grandfather about the concept of legacy. We were sitting on the porch at twilight, which added a contemplative atmosphere to our exchange. He posited that true wealth lies not in material accumulation but in the impact one has on others. His insights were incredibly poignant, stemming from a lifetime of experience. He articulated his thoughts with such eloquence that I was left spellbound. That conversation fundamentally shifted my paradigm, prompting me to re-evaluate my own priorities. It was an ephemeral moment that left an indelible mark on my consciousness.",
        "word_count": 101,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 8,
        "vocab_reason": "[LR9] 'Philosophical discourse', 'twilight', 'contemplative', 'posited', 'material accumulation', 'poignant', 'articulated', 'eloquence', 'spellbound', 'paradigm', 'ephemeral', 'indelible mark'. Native-like.",
        "grammar_reason": "[GRA8] 'Discourse I had' (Relative). 'Which added...' (Relative). 'Lies not in... but in' (Correlative). 'Prompting me to...' (Participle). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g8_0803",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a technological innovation.",
        "transcript_cleaned": "I am astounded by the rapid advancement of CRISPR gene-editing technology. It represents a quantum leap in our ability to manipulate the building blocks of life. The potential to eradicate hereditary diseases is nothing short of revolutionary. However, the ethical ramifications are equally staggering, raising questions about 'designer babies' and playing god. I find the duality of this innovation—its promise and its peril—to be intellectually stimulating. It forces us to confront the boundaries of science and morality. To witness such a paradigm shift in my lifetime is both awe-inspiring and slightly terrifying.",
        "word_count": 96,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 8,
        "vocab_reason": "[LR9] 'Astounded', 'quantum leap', 'manipulate', 'hereditary diseases', 'revolutionary', 'ramifications', 'staggering', 'duality', 'peril', 'intellectually stimulating', 'paradigm shift'. Native-like.",
        "grammar_reason": "[GRA8] 'Raising questions about' (Participle). 'Nothing short of' (Idiom). 'To witness... is' (Infinitive subject). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g8_0804",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building you admire.",
        "transcript_cleaned": "The Taj Mahal in India is an architectural marvel that transcends mere stone and mortar. It is a poignant symbol of eternal love, commissioned by an emperor for his favorite wife. The symmetry of the white marble structure is flawless, especially when reflected in the pool. The intricate inlay work of semi-precious stones is a testament to the artisans' dexterity. Viewing it at sunrise, when the marble takes on a pinkish hue, is an ethereal experience. It stands as an enduring legacy of the Mughal era, evoking a sense of wonder and melancholy.",
        "word_count": 96,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 8,
        "vocab_reason": "[LR9] 'Architectural marvel', 'transcends', 'poignant symbol', 'commissioned', 'symmetry', 'flawless', 'intricate inlay work', 'dexterity', 'ethereal', 'enduring legacy', 'evoking'. Native-like.",
        "grammar_reason": "[GRA8] 'Commissioned by...' (Participle). 'Especially when reflected' (Elliptical). 'Viewing it... is' (Gerund subject). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g8_0805",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a frightening experience.",
        "transcript_cleaned": "I once found myself in a perilous situation while hiking in the Alps when a sudden blizzard descended. The visibility dropped to zero within minutes, disorienting me completely. The howling wind was deafening, and the temperature plummeted precipitously. I was engulfed by a sense of dread, realizing how vulnerable I was against the elements. I had to seek shelter in a small crevice and wait it out, shivering uncontrollably. The sheer unpredictability of nature was a humbling realization. Surviving that ordeal instilled in me a profound respect for the mountains and their capacity for fury.",
        "word_count": 97,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 8,
        "vocab_reason": "[LR9] 'Perilous situation', 'blizzard descended', 'disorienting', 'plummeted precipitously', 'engulfed', 'dread', 'vulnerable', 'unpredictability', 'humbling realization', 'ordeal', 'capacity for fury'. Native-like.",
        "grammar_reason": "[GRA8] 'While hiking' (Elliptical). 'Realizing how vulnerable' (Participle). 'Had to seek' (Modal). 'Surviving that ordeal instilled' (Gerund subject). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g8_0806",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a childhood friend.",
        "transcript_cleaned": "My childhood companion, Lucas, was a mischievous yet endearing character. We were inseparable, united by a shared penchant for adventure. He possessed an innate charisma that drew people to him effortlessly. Whether we were building treehouses or exploring the woods, his imagination knew no bounds. He had an uncanny ability to talk his way out of trouble, a skill I often envied. Although our paths have diverged in adulthood, the bond we forged is unbreakable. Looking back, he was the catalyst for many of my most cherished memories, adding color to my formative years.",
        "word_count": 96,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 8,
        "vocab_reason": "[LR9] 'Mischievous', 'endearing', 'inseparable', 'penchant for adventure', 'innate charisma', 'uncanny ability', 'diverged', 'catalyst', 'cherished memories', 'formative years'. Native-like.",
        "grammar_reason": "[GRA8] 'United by...' (Participle). 'Whether we were...' (Correlative). 'Paths have diverged' (Present Perfect). 'Adding color to...' (Participle). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g8_0807",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a law you agree with.",
        "transcript_cleaned": "I am a staunch supporter of the legislation regarding data privacy protection. In an era where digital footprints are ubiquitous, safeguarding personal information is paramount. This law compels corporations to be transparent about how they harvest and utilize user data. It empowers individuals to reclaim sovereignty over their digital identities. While some argue it stifles innovation, I believe the preservation of privacy is a fundamental human right. The rampant exploitation of data for commercial gain had gone unchecked for too long. This regulation serves as a necessary check on the power of tech giants.",
        "word_count": 96,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 8,
        "vocab_reason": "[LR9] 'Staunch supporter', 'ubiquitous', 'safeguarding', 'paramount', 'compels', 'transparent', 'harvest', 'sovereignty', 'stifles innovation', 'rampant exploitation', 'unchecked'. Native-like.",
        "grammar_reason": "[GRA8] 'Regarding data privacy' (Participle). 'Where digital footprints are' (Relative). 'How they harvest' (Noun clause). 'While some argue' (Concessive). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g8_0808",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of furniture.",
        "transcript_cleaned": "I have a deep affection for an antique mahogany writing desk that has been in my family for generations. Its surface is scarred with scratches and ink stains, each marking a chapter of its history. The craftsmanship is exquisite, featuring cabriole legs and brass handles that have developed a rich patina. It is not merely a functional object but a repository of memories. Sitting at it, I feel a tangible connection to my ancestors who penned letters and dreams on the same wood. It exudes a sense of permanence in a disposable world.",
        "word_count": 96,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 8,
        "vocab_reason": "[LR9] 'Deep affection', 'mahogany', 'scarred', 'craftsmanship', 'exquisite', 'cabriole legs', 'patina', 'repository', 'tangible connection', 'exudes', 'permanence', 'disposable world'. Native-like.",
        "grammar_reason": "[GRA8] 'That has been' (Relative). 'Featuring cabriole legs' (Participle). 'Not merely... but' (Correlative). 'Sitting at it' (Participle). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g8_0809",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a stressful day.",
        "transcript_cleaned": "I remember a particularly harrowing day during my final university exams. The pressure was palpable, and I was running on caffeine and adrenaline. To make matters worse, my laptop crashed, potentially erasing weeks of research. The panic that set in was visceral. I had to scramble to retrieve the data, racing against the clock. It was a perfect storm of technical failure and academic stress. Although I eventually managed to submit the assignment, the emotional toll was significant. That day taught me the hard way about the necessity of backing up files.",
        "word_count": 93,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 8,
        "vocab_reason": "[LR9] 'Harrowing', 'palpable', 'adrenaline', 'visceral', 'scramble', 'retrieve', 'racing against the clock', 'perfect storm', 'emotional toll', 'necessity'. Native-like.",
        "grammar_reason": "[GRA8] 'To make matters worse' (Idiomatic). 'Potentially erasing' (Participle). 'That set in' (Relative). 'Although I eventually managed' (Concessive). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v9_g8_0810",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of clothing you like.",
        "transcript_cleaned": "I cherish a bespoke trench coat that I purchased in London. It is tailored to perfection, hugging my frame while allowing freedom of movement. The fabric is a durable gabardine in a classic beige hue. What I love most is its versatility; it effortlessly elevates a casual outfit and complements formal attire. It has weathered many storms, quite literally, yet retains its elegance. Wearing it gives me a sense of sophistication and confidence. It is a timeless staple in my wardrobe that defies fleeting fashion trends, embodying quality over quantity.",
        "word_count": 93,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 8,
        "vocab_reason": "[LR9] 'Bespoke', 'tailored to perfection', 'freedom of movement', 'gabardine', 'hue', 'versatility', 'effortlessly elevates', 'complements', 'weathered many storms', 'timeless staple', 'defies fleeting trends'. Native-like.",
        "grammar_reason": "[GRA8] 'That I purchased' (Relative). 'Hugging my frame' (Participle). 'What I love most is' (Cleft). 'Yet retains' (Contrast). Error-free.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"}
    },
    # --- V5/G7 (811-820) ---
    {
        "sample_id": "syn_p2_v5_g7_0811",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a crowded place you visited.",
        "transcript_cleaned": "I went to a big market in the city last Sunday. It was very crowded with many people buying things. Although I don't like noisy places, I needed to buy a gift for my friend. The market sells clothes, food, and other stuff. While I was walking, I saw a shop that had nice bags. The price was cheap, so I decided to buy one. It was difficult to move because there were too many people. If I had known it was so busy, I would have gone on a different day. However, I am happy I found a good gift.",
        "word_count": 104,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 7,
        "vocab_reason": "[LR5] 'Big market', 'buying things', 'noisy', 'stuff', 'nice bags', 'price was cheap', 'difficult to move'. Basic/Functional.",
        "grammar_reason": "[GRA7] 'Although I don't like' (Concessive). 'While I was walking' (Time clause). 'That had nice bags' (Relative). 'If I had known... I would have gone' (Third Conditional). Accurate complex structures.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v5_g7_0812",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult thing you did.",
        "transcript_cleaned": "I tried to learn how to swim last summer, which was very hard for me. I am afraid of water, so it was a big challenge. I took a class at the sports center near my house. My teacher was kind and helped me a lot. At first, I could not float, but I practiced every day. Even though I was scared, I did not give up. After two weeks, I could swim a little bit. It is good for my health to swim. I am proud that I tried something new, even if it was difficult.",
        "word_count": 100,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 7,
        "vocab_reason": "[LR5] 'Hard', 'afraid of water', 'big challenge', 'kind', 'float', 'practiced', 'scared', 'give up', 'proud'. Basic/Functional.",
        "grammar_reason": "[GRA7] 'Which was very hard' (Relative). 'So it was' (Result). 'At first... but' (Contrast). 'Even though I was scared' (Concessive). 'Even if it was' (Concessive). Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v5_g7_0813",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a helpful person.",
        "transcript_cleaned": "My neighbor is a very helpful person who always assists others. One day, I lost my key and could not open my door. I was worried because it was late at night. My neighbor saw me and offered to help. He called a man to fix the lock for me. While we waited, he gave me some tea. He is a kind man who lives alone. I think it is important to have good neighbors. If he needs help in the future, I will definitely help him. People like him make the world a better place.",
        "word_count": 98,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 7,
        "vocab_reason": "[LR5] 'Helpful', 'assists', 'lost my key', 'worried', 'fix the lock', 'kind', 'lives alone', 'better place'. Basic/Functional.",
        "grammar_reason": "[GRA7] 'Who always assists' (Relative). 'Because it was late' (Reason). 'While we waited' (Time clause). 'If he needs help... I will' (First Conditional). Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v5_g7_0814",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a famous building.",
        "transcript_cleaned": "I want to talk about the Eiffel Tower, which is in Paris. It is a very famous tower made of metal. Many people visit it every year to take photos. I went there with my family when I was young. The tower is very tall, and you can see the whole city from the top. Although it was windy, the view was beautiful. At night, there are lights on the tower that look nice. It is a symbol of France. I think everyone knows this building because it is on TV and in movies often.",
        "word_count": 98,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 7,
        "vocab_reason": "[LR5] 'Famous tower', 'metal', 'take photos', 'tall', 'view', 'lights', 'symbol', 'movies'. Basic/Functional.",
        "grammar_reason": "[GRA7] 'Which is in Paris' (Relative). 'Made of metal' (Participle). 'When I was young' (Time clause). 'Although it was windy' (Concessive). 'Because it is' (Reason). Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v5_g7_0815",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a bad service you received.",
        "transcript_cleaned": "I went to a restaurant last week where the service was very bad. We waited for a long time to get our food. The waiter was rude and did not smile. When the food came, it was cold, which made me angry. I asked to speak to the manager, but he was not there. We decided to leave and not pay for the food. It was a bad experience because we were hungry. Companies should train their workers to be polite. If the service is bad, customers will not come back again.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 7,
        "vocab_reason": "[LR5] 'Service', 'rude', 'smile', 'cold', 'angry', 'manager', 'polite', 'customers'. Basic/Functional.",
        "grammar_reason": "[GRA7] 'Where the service was' (Relative). 'To get our food' (Infinitive). 'Which made me angry' (Relative). 'If the service is bad... will not' (First Conditional). Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v5_g7_0816",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a funny TV show.",
        "transcript_cleaned": "I like a TV show called 'Friends', which is very funny. It is about six friends who live in New York. They talk and do funny things together. I watch it every day after work to relax. The characters are interesting, and they make many jokes. My favorite character is Joey because he is silly. Even though I have seen it many times, I still laugh. It makes me feel happy when I am sad. I think good comedy shows are important for people to enjoy life.",
        "word_count": 89,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 7,
        "vocab_reason": "[LR5] 'Funny', 'jokes', 'silly', 'relax', 'characters', 'laugh', 'comedy'. Basic/Functional.",
        "grammar_reason": "[GRA7] 'Called Friends' (Participle). 'Which is very funny' (Relative). 'Who live in New York' (Relative). 'Even though I have seen' (Concessive). Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v5_g7_0817",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you were sick.",
        "transcript_cleaned": "I was sick last month with a bad flu. I had a fever and my head hurt a lot. I could not go to work, so I stayed in bed for three days. My mother came to my house to take care of me. She cooked soup and gave me medicine. I felt very weak and tired. It is boring to stay home when you are sick. I slept a lot to get better. After a few days, I felt strong again. Being healthy is the most important thing in life.",
        "word_count": 94,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 7,
        "vocab_reason": "[LR5] 'Sick', 'flu', 'fever', 'hurt', 'medicine', 'weak', 'boring', 'healthy'. Basic/Functional.",
        "grammar_reason": "[GRA7] 'With a bad flu' (Prepositional). 'So I stayed' (Result). 'To take care of me' (Infinitive). 'When you are sick' (Time clause). Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v5_g7_0818",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you want to receive.",
        "transcript_cleaned": "I really want to get a new phone for my birthday. My old phone is slow and the battery is bad. If I get a new one, I can take better photos and play games. I like the one that is black and big. It is expensive, so I cannot buy it myself. I told my parents that I want it. I hope they will give it to me. receiving gifts makes me feel special. A new phone would be very useful for my daily life.",
        "word_count": 89,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 7,
        "vocab_reason": "[LR5] 'Birthday', 'slow', 'battery', 'expensive', 'useful', 'daily life'. Basic/Functional.",
        "grammar_reason": "[GRA7] 'If I get... I can take' (First Conditional). 'The one that is black' (Relative). 'So I cannot buy' (Result). 'That I want it' (Noun clause). Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v5_g7_0819",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party you went to.",
        "transcript_cleaned": "I went to a wedding party for my cousin last year. It was in a big hotel with many guests. The room was decorated with flowers, which looked beautiful. We ate a lot of good food and drank juice. There was music, and everyone danced. I met some family members who I had not seen for a long time. It was a happy day for everyone. The bride and groom looked very nice. I took many photos to remember the day. Parties are good because people can have fun together.",
        "word_count": 92,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 7,
        "vocab_reason": "[LR5] 'Wedding', 'guests', 'decorated', 'flowers', 'bride', 'groom', 'fun'. Basic/Functional.",
        "grammar_reason": "[GRA7] 'With many guests' (Prepositional). 'Which looked beautiful' (Relative). 'Who I had not seen' (Relative + Past Perfect). 'To remember the day' (Infinitive). Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    {
        "sample_id": "syn_p2_v5_g7_0820",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a website you use for work or study.",
        "transcript_cleaned": "I use Google every day to help me with my studies. It is a search website where you can find information about anything. If I have a question, I type it in the box. It gives me many answers quickly. I use it to find pictures and read articles. It is very useful because it saves time. Without this website, it would be hard to do my homework. I also use it to translate words I don't know. It is the most important tool on the internet for me.",
        "word_count": 91,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 7,
        "vocab_reason": "[LR5] 'Search website', 'information', 'type', 'articles', 'useful', 'saves time', 'translate'. Basic/Functional.",
        "grammar_reason": "[GRA7] 'Where you can find' (Relative). 'If I have... I type' (First Conditional). 'Because it saves time' (Reason). 'Words I don't know' (Reduced relative). Accurate.",
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"}
    },
    # --- V7/G5 (821-825) ---
    {
        "sample_id": "syn_p2_v7_g5_0821",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a local business.",
        "transcript_cleaned": "I go to a local bakery that is famous for artisan bread. The aroma is very enticing when you walk in. They use organic ingredients and traditional methods. The quality is superior to the supermarket. However, the price are a bit high. I usually buying a loaf on weekends. The owner is friendly and he know my name. He work very hard every day. It is important to support local business in our community. I hope it stay open for a long time.",
        "word_count": 84,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 5,
        "vocab_reason": "[LR7] 'Artisan bread', 'enticing', 'organic ingredients', 'traditional methods', 'superior', 'support local business'. Good range.",
        "grammar_reason": "[GRA5] 'Price are' (Agreement). 'I usually buying' (Tense). 'He know' (Agreement). 'He work' (Agreement). 'It stay' (Agreement). Complex vocab, broken grammar.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v7_g5_0822",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a famous person you like.",
        "transcript_cleaned": "I admire Elon Musk because he is a visionary entrepreneur. He found companies like Tesla and SpaceX. He want to colonize Mars, which is ambitious. His innovation has revolutionized the electric car industry. I think he is genius. But sometimes he say crazy things on internet. I following him on Twitter. He work all the time and never sleep. His determination is inspiring for young people. Even if he fail, he keep trying. He has make a big impact on the world.",
        "word_count": 82,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 5,
        "vocab_reason": "[LR7] 'Visionary entrepreneur', 'colonize', 'ambitious', 'innovation', 'revolutionized', 'industry', 'determination', 'impact'. Good range.",
        "grammar_reason": "[GRA5] 'He found' (should be founded). 'He want' (Agreement). 'He say' (Agreement). 'I following' (Tense). 'He work' (Agreement). 'He has make' (Tense).",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v7_g5_0823",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical event in your country.",
        "transcript_cleaned": "I remember learning about the revolution that happened in my country. It was a pivotal moment in our history. The citizens fought against oppression and tyranny. They wanted democracy and freedom. The conflict lasted for many years and many people die. Finally, the government collapse and we become free. We celebrate this anniversary every year with parades. It signifies our independence and resilience. My grandfather tell me stories about it. It is crucial to remember the sacrifice of the past.",
        "word_count": 80,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 5,
        "vocab_reason": "[LR7] 'Pivotal moment', 'oppression', 'tyranny', 'democracy', 'conflict', 'anniversary', 'signifies', 'resilience', 'sacrifice'. Good range.",
        "grammar_reason": "[GRA5] 'People die' (Tense). 'Government collapse' (Tense). 'We become' (Tense). 'Grandfather tell' (Agreement). Basic grammar errors.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v7_g5_0824",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you were angry.",
        "transcript_cleaned": "I was furious when my flight was cancelled without notice. I had a connecting flight that I missed. The airline staff was unhelpful and rude. I felt frustrated and helpless. I demanded a refund but they refuse. It was a chaotic situation at the airport. I have to sleep on the floor. It was unacceptable treatment. I missed an important conference because of this. I filed a complaint later. Incompetence makes me very angry. I will never flying with them again.",
        "word_count": 83,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 5,
        "vocab_reason": "[LR7] 'Furious', 'cancelled', 'connecting flight', 'unhelpful', 'frustrated', 'helpless', 'demanded', 'refund', 'chaotic', 'unacceptable', 'incompetence'. Good range.",
        "grammar_reason": "[GRA5] 'They refuse' (Tense). 'I have to sleep' (Tense). 'Never flying' (Verb form). Good vocab, bad grammar.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v7_g5_0825",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of art.",
        "transcript_cleaned": "I saw a sculpture in a museum that was mesmerizing. It was made of bronze and depicted a human figure. The texture was smooth and the details was incredible. It conveyed a sense of sorrow and despair. The artist used abstract forms to express emotion. I stared at it for long time. It provoke deep thought in me. I am not expert on art, but I appreciate the creativity. The aesthetic was unique. Art like this enrich our lives.",
        "word_count": 80,
        "response_type": "long_turn",
        "vocabulary": 7, "grammar": 5,
        "vocab_reason": "[LR7] 'Sculpture', 'mesmerizing', 'bronze', 'depicted', 'texture', 'conveyed', 'sorrow', 'despair', 'abstract', 'aesthetic', 'enrich'. Good range.",
        "grammar_reason": "[GRA5] 'Details was' (Agreement). 'For long time' (Article). 'It provoke' (Agreement). 'Not expert' (Article). 'Enrich our lives' (Agreement).",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
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
