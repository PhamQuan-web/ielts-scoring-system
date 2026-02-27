import json
import os

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_15_part2.jsonl"

# Samples 726-750 (V4/G5: 10, V5/G4: 10, V5/G5: 5)
samples = [
    # --- V4/G5 (726-735) ---
    {
        "sample_id": "syn_p2_v4_g5_0726",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a job you would like to do.",
        "transcript_cleaned": "I want to talk about be a teacher. It is a good job because I like help children. My mother, she is a teacher, and she tell me it is hard but fun. If I am teacher, I will teach math. Math is important subject. I study math in school and I am good at it. The teacher need to speak clear and be patient. Sometimes children are naughty, so teacher must be strong. I think teaching is a... a nice job for me. I want to work in my city near my house. It is... convenient. I hope I can do this job in future.",
        "word_count": 102,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 5,
        "vocab_reason": "[LR4] Basic vocab: 'good job', 'hard but fun', 'important', 'naughty', 'nice'. Repetitive.",
        "grammar_reason": "[GRA5] Basic sentences OK. 'If I am teacher' (Conditional attempt). 'My mother, she is' (Double subject). 'She tell me' (Agreement error).",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g5_0727",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a movie you watched recently.",
        "transcript_cleaned": "Last week I watch a movie called 'The Hero'. It is action movie. I watch with my friend at cinema. The movie is about a man who save the world. It is very exciting. There are many fight and explosion. I like the actor because he is very handsome and strong. The story is simple but good. We eat popcorn and drink cola when we watch. After movie, we go home happy. I want to watch it again because it is very... very good. I think everyone should see this movie. It is best movie I see this year.",
        "word_count": 101,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 5,
        "vocab_reason": "[LR4] Basic vocab: 'action movie', 'exciting', 'fight', 'handsome', 'good', 'happy'. Repetitive.",
        "grammar_reason": "[GRA5] Simple sentences mostly correct. 'Last week I watch' (Tense error). 'Man who save' (Relative clause attempt). 'Best movie I see' (Tense).",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g5_0728",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift you gave to someone.",
        "transcript_cleaned": "I give a gift to my sister for her birthday. I buy a bag for her. It is a red bag and it is very beautiful. She like red color very much. I go to the shop in the mall to buy it. It cost... not too much money. When I give her, she is very happy. She say thank you to me. She use the bag every day now. I am happy because she like it. Giving gift is good thing to do. It make people feel good. I want to give her more gift next time.",
        "word_count": 101,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 5,
        "vocab_reason": "[LR4] Basic vocab: 'gift', 'birthday', 'buy', 'bag', 'beautiful', 'happy', 'shop'. Repetitive.",
        "grammar_reason": "[GRA5] Basic sentences generally accurate. 'She like' (Agreement). 'It make people' (Agreement). 'When I give her' (Time clause attempt).",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g5_0729",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a journey you went on.",
        "transcript_cleaned": "I went to the beach last summer with family. We go by car. It take three hours to go there. The beach is very nice and blue. We swim in water and play sand. My father he drive the car. We eat seafood for lunch. It is delicious. We stay there for two days in a hotel. The hotel is clean and big. I take many photo with my phone. It is a good holiday. I want to go there again next year. Traveling is... fun for me. I like see new place.",
        "word_count": 96,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 5,
        "vocab_reason": "[LR4] Basic vocab: 'beach', 'summer', 'car', 'swim', 'sand', 'delicious', 'hotel', 'photo'. Repetitive.",
        "grammar_reason": "[GRA5] Simple past tense attempted but mixed ('We go', 'It take'). 'My father he drive' (Double subject). Basic connectors used.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g5_0730",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant in your country.",
        "transcript_cleaned": "In my country, we have many bamboo tree. Bamboo is very useful. People use it to make house and furniture. It is green and tall. It grow very fast. You can see it in village. I like bamboo because it look nice. Also, pandas eat bamboo. We also use bamboo to make chopstick for eating. It is important for our culture. My grandfather, he plant bamboo in his garden. I think bamboo is symbol of my country. It is strong plant. Everyone know bamboo.",
        "word_count": 84,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 5,
        "vocab_reason": "[LR4] Basic vocab: 'useful', 'furniture', 'green', 'tall', 'village', 'nice', 'strong'. Repetitive.",
        "grammar_reason": "[GRA5] 'We have many bamboo tree' (Plural error). 'It grow' (Agreement). 'My grandfather, he plant' (Double subject). Simple sentences OK.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g5_0731",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a website you like.",
        "transcript_cleaned": "I like use YouTube. It is a website for video. I watch many video on it every day. I watch music video and funny video. It is free to use. I can learn English on YouTube too. There are many teacher make video. I like it because it is interesting. I can see what happen in other country. Sometimes I watch movie trailer. It is easy to use on my phone. My friends also use YouTube. We talk about video we see. It is very popular website.",
        "word_count": 91,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 5,
        "vocab_reason": "[LR4] Basic vocab: 'website', 'video', 'watch', 'funny', 'free', 'learn', 'teacher'. Repetitive.",
        "grammar_reason": "[GRA5] 'I like use' (Verb pattern error). 'There are many teacher make video' (Run-on/Relative error). 'What happen' (Agreement).",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g5_0732",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a restaurant you like.",
        "transcript_cleaned": "I like a restaurant near my school. It sell pizza and pasta. The food is very tasty. I go there with my friends for lunch. The price is cheap, not expensive. The waiter is friendly. The restaurant is small but clean. I like the pizza with cheese. It is my favorite. We usually go there on Friday. Sometimes we have birthday party there. It is a happy place. I recommend this restaurant to everyone. The food is always hot and fresh. I like eat there very much.",
        "word_count": 89,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 5,
        "vocab_reason": "[LR4] Basic vocab: 'sell', 'tasty', 'lunch', 'cheap', 'expensive', 'friendly', 'small', 'clean'. Repetitive.",
        "grammar_reason": "[GRA5] 'It sell' (Agreement). 'I like eat' (Verb pattern). Simple sentences are correct. Connectors 'but', 'and' used.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g5_0733",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a song you like.",
        "transcript_cleaned": "I like a song called 'Happy'. It is by a singer name Pharrell. The song is very happy song. When I listen, I want to dance. The music is fast and good. I hear it on radio many times. The words are easy to remember. It make me feel good when I am sad. My friends also like this song. We sing together in karaoke. It is popular song in the world. I have it on my phone. I listen when I go to school.",
        "word_count": 87,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 5,
        "vocab_reason": "[LR4] Basic vocab: 'song', 'singer', 'happy', 'dance', 'music', 'fast', 'good', 'radio'. Repetitive.",
        "grammar_reason": "[GRA5] 'Singer name Pharrell' (Participle error). 'It make me feel' (Agreement). 'I listen when I go' (Time clause).",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g5_0734",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you were busy.",
        "transcript_cleaned": "Last week I was very busy. I have exam in school. I must study every day. I wake up early and sleep late. I study math and English. I not have time to play with friends. It is very tired for me. My mother help me cook food. I just eat and study. After exam, I am free. I sleep for long time. Being busy is not fun. I like to have free time to relax. But exam is important so I must work hard.",
        "word_count": 88,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 5,
        "vocab_reason": "[LR4] Basic vocab: 'busy', 'exam', 'study', 'early', 'late', 'tired', 'free', 'relax'. Repetitive.",
        "grammar_reason": "[GRA5] 'I have exam' (Article/Tense). 'I not have time' (Auxiliary error). 'It is very tired for me' (Adjective error).",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v4_g5_0735",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a famous person.",
        "transcript_cleaned": "I want to talk about Messi. He is football player. He is very famous in the world. He play for Argentina. He is small but he run very fast. He score many goal. I watch him on TV. He is very good at football. Many people like him. He has many fan. I think he is rich too. He help poor children also. He is a good man. I want to be like him. He is my hero. I buy his shirt to wear.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 4, "grammar": 5,
        "vocab_reason": "[LR4] Basic vocab: 'football player', 'famous', 'run', 'fast', 'goal', 'good', 'rich', 'poor'. Repetitive.",
        "grammar_reason": "[GRA5] 'He play' (Agreement). 'He score many goal' (Agreement/Plural). 'He has many fan' (Plural). Simple sentences mostly correct.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    # --- V5/G4 (736-745) ---
    {
        "sample_id": "syn_p2_v5_g4_0736",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a change in your life.",
        "transcript_cleaned": "I want talk about when I move house. Before, I live in small village. It was quiet. Then my father change job. So we move to big city. The city is very busy and noisy. At first, I don't like it. I miss my old friends. But now I habit to it. The city have many convenient shop and cinema. I can go many place easily. The transport is good. It was big change for me. I learn many new thing in city. My life is different now. I think it is better for my future.",
        "word_count": 97,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Move house', 'convenient', 'transport', 'future'. Better than band 4 but limited.",
        "grammar_reason": "[GRA4] 'I want talk' (Missing to). 'I live' (Tense). 'My father change job' (Tense/Agreement). 'I habit to it' (Wrong word class/Structure). 'City have' (Agreement).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0737",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a disagreement you had.",
        "transcript_cleaned": "I have disagreement with my friend. We want go to cinema. I want watch action movie. He want watch comedy. We argue about it. I say action is exciting. He say comedy is funny. We angry each other. We not talk for one hour. Then we decide to watch both movie. No, just kidding. We decide to eat instead. It was small problem. We are good friend. Sometimes we have different opinion. It is normal. We forget it quickly. Relationships is important than movie.",
        "word_count": 87,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Disagreement', 'comedy', 'argue', 'opinion', 'relationships'. Topic vocab present.",
        "grammar_reason": "[GRA4] 'We want go' (Missing to). 'I want watch' (Missing to). 'We angry each other' (Missing prep/verb). 'Different opinion' (Plural). 'Relationships is' (Agreement).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0738",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a wild animal.",
        "transcript_cleaned": "I like tiger. Tiger is big animal. It live in jungle. It has orange and black color. It is dangerous. It eat meat. I see tiger in zoo only. I never see in wild. It is beautiful but scary. Some people hunt tiger. That is bad. Tiger number is going down. We need protect them. If no tiger, the nature is not balance. I watching TV about tiger. They run very fast. They are strong. I hope tiger can live safe.",
        "word_count": 85,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Jungle', 'dangerous', 'hunt', 'protect', 'nature', 'balance'. Topic vocab present.",
        "grammar_reason": "[GRA4] 'It live' (Agreement). 'It eat meat' (Agreement). 'I never see' (Tense). 'Tiger number' (Phrasing). 'We need protect' (Missing to). 'If no tiger' (Fragment).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0739",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical event.",
        "transcript_cleaned": "I talk about independence day of my country. It happen many years ago. Before, we ruled by other country. But our people fight for freedom. There was war. Many people died. It was sad time. But finally we win. Now we are free country. We celebrate this day every year. We have parade and firework. It is important history. We remember the hero who save us. I learn this in history class. It make me feel proud of my country.",
        "word_count": 85,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Independence day', 'ruled', 'freedom', 'war', 'celebrate', 'parade', 'firework', 'proud'.",
        "grammar_reason": "[GRA4] 'It happen' (Tense). 'We ruled' (Passive error). 'Our people fight' (Tense). 'Finally we win' (Tense). 'It make me feel' (Agreement).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0740",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a TV program you like.",
        "transcript_cleaned": "I like watch 'MasterChef'. It is cooking competition program. Many people cook food there. There are three judge. They taste the food. If food is good, they stay. If bad, they go home. It is very nervous. I like see the delicious food. I learn how to cook from it. The winner get money and trophy. I watch it every week with family. Sometimes I hungry when I watch. It is entertaining show. I want to be chef maybe.",
        "word_count": 83,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Competition', 'judge', 'taste', 'nervous', 'delicious', 'winner', 'trophy', 'entertaining'.",
        "grammar_reason": "[GRA4] 'I like watch' (Missing to/ing). 'There are three judge' (Plural). 'The winner get' (Agreement). 'I hungry' (Missing verb).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0741",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a noisy neighbor.",
        "transcript_cleaned": "My neighbor is very noisy person. He live next door. He play loud music at night. I cannot sleep. It is disturbing. I tell him to stop, but he not listen. He also have dog. The dog bark all time. It is annoying. Sometimes he have party with many friends. They shout and laugh. I feel angry. I want to call police but I don't. I just put pillow on my head. I hope he move away soon. Silence is better.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Disturbing', 'bark', 'annoying', 'shout', 'silence'. Topic vocab present.",
        "grammar_reason": "[GRA4] 'He live' (Agreement). 'He not listen' (Auxiliary). 'He also have' (Agreement). 'Dog bark' (Agreement). 'I hope he move' (Agreement).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0742",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a park you visited.",
        "transcript_cleaned": "I went to City Park yesterday. It is in center of city. It is very big park. There are many trees and flowers. People go there to exercise. I saw people jogging and walking dog. There is a lake too. I sit on bench and relax. The atmosphere is peaceful. I forget my stress. Children play in playground. It is good place for picnic. The air is fresh. I like nature. I want go there every weekend to relax mind.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Center', 'exercise', 'jogging', 'bench', 'atmosphere', 'peaceful', 'playground', 'fresh'.",
        "grammar_reason": "[GRA4] 'In center of city' (Articles). 'I sit on bench' (Tense/Article). 'I want go' (Missing to). 'Walking dog' (Article).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0743",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a polite person.",
        "transcript_cleaned": "My friend Tom is polite person. He always say 'please' and 'thank you'. He open door for others. He never shout. He listen when people talk. He respect old people. He is gentleman. Everyone like him. He has good manners. One time, he help old lady cross street. It was very kind. I think being polite is important. It show you are good education. Rude people is bad. We should be nice to everyone. Tom is good example for me.",
        "word_count": 84,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Polite', 'respect', 'gentleman', 'manners', 'education', 'rude'. Topic vocab present.",
        "grammar_reason": "[GRA4] 'Polite person' (Article). 'He always say' (Agreement). 'He open door' (Agreement). 'He help old lady' (Tense). 'It show you are' (Agreement). 'Rude people is' (Agreement).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0744",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I had difficult task last month. I must fix my computer. It was broken. I don't know how to fix. It is complicated. I look on internet for help. There are many instruction. I try to follow but it is hard. I spend many hours. I feel frustrated. I want to give up. But I keep trying. Finally, I fix it. I feel very happy. It was challenge for me. I learn that I can do hard thing if I try.",
        "word_count": 87,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Fix', 'broken', 'complicated', 'instruction', 'frustrated', 'give up', 'challenge'.",
        "grammar_reason": "[GRA4] 'I had difficult task' (Article). 'I must fix' (Tense context). 'There are many instruction' (Plural). 'I try to follow' (Tense). 'I fix it' (Tense).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g4_0745",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a crowded place.",
        "transcript_cleaned": "I went to shopping mall on Sunday. It was very crowded. So many people there. It is difficult to walk. People push each other. It is noisy. I feel uncomfortable. I want to buy clothes but the line is long. I wait for 20 minutes. The air is hot. I don't like crowded place. It give me headache. I prefer quiet place. But the sale was good. So many people go. Next time I go on Monday. It is less people.",
        "word_count": 86,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 4,
        "vocab_reason": "[LR5] 'Shopping mall', 'crowded', 'uncomfortable', 'headache', 'prefer', 'sale'. Topic vocab present.",
        "grammar_reason": "[GRA4] 'So many people there' (Fragment). 'It is difficult' (Tense consistency). 'It give me headache' (Agreement). 'It is less people' (Grammar).",
        "grammar_profile": {"complexity": "basic", "accuracy": "variable", "flexibility": "limited"}
    },
    # --- V5/G5 (746-750) ---
    {
        "sample_id": "syn_p2_v5_g5_0746",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a time you helped someone.",
        "transcript_cleaned": "I helped my neighbor yesterday. She is old woman. She carry heavy bags from supermarket. I see her walking slowly. So I go to help her. I carry the bags to her house. She was very happy. She give me some candy. I feel good to help her. Helping people is important. We live in same community. My parents teach me to be kind. It was not big thing, but it mean a lot to her. I will help her again.",
        "word_count": 87,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Neighbor', 'heavy bags', 'community', 'kind', 'mean a lot'. Adequate.",
        "grammar_reason": "[GRA5] 'She is old woman' (Article). 'She carry' (Tense). 'I see her walking' (Tense). 'She give me' (Tense). Simple sentences mostly accurate.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0747",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a favorite season.",
        "transcript_cleaned": "My favorite season is winter. I like cold weather. In my country, it snow sometimes. The snow is white and beautiful. I like to wear jacket and scarf. It is comfortable. I also like Christmas holiday in winter. We get gifts and eat good food. Summer is too hot for me. I sweat and feel tired. But winter is fresh. I can sleep well at night. Winter is best time for me. I wait for winter every year.",
        "word_count": 84,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Season', 'weather', 'comfortable', 'sweat', 'fresh'. Adequate.",
        "grammar_reason": "[GRA5] 'It snow sometimes' (Agreement). 'Wear jacket' (Article). 'Winter is best time' (Article). Simple sentences generally correct.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0748",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a bad weather experience.",
        "transcript_cleaned": "I remember a big storm last year. It rain very hard. The wind was strong. I was at home. The electricity go off. It was dark. I was scared. The water come into the street. Trees fall down. We cannot go outside. We use candle for light. The storm last for one day. Next day, it was sunny. But the city was messy. It was dangerous experience. I hope no more storm like that. Nature is powerful.",
        "word_count": 84,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Storm', 'electricity', 'scared', 'candle', 'messy', 'powerful'. Adequate.",
        "grammar_reason": "[GRA5] 'It rain' (Tense). 'Electricity go off' (Tense). 'Water come' (Tense). 'Trees fall' (Tense). Simple past attempted but errors frequent.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0749",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a uniform you wore.",
        "transcript_cleaned": "I wore school uniform when I was student. It was white shirt and blue trouser. I must wear it every day. I don't like it much. It is not comfortable. And it is boring. Everyone look the same. But teacher say it is good for discipline. It show we are student of that school. On weekend, I wear my own clothes. I like jeans and t-shirt better. Uniform is strict rule. I am happy I don't wear it now.",
        "word_count": 85,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Uniform', 'trouser', 'comfortable', 'boring', 'discipline', 'strict rule'. Adequate.",
        "grammar_reason": "[GRA5] 'Blue trouser' (Plural). 'Everyone look' (Agreement). 'It show' (Agreement). Simple sentences mostly correct.",
        "grammar_profile": {"complexity": "basic", "accuracy": "controlled", "flexibility": "limited"}
    },
    {
        "sample_id": "syn_p2_v5_g5_0750",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a success you had.",
        "transcript_cleaned": "I succeed in passing my driving test. It was difficult for me. I practice driving for three months. My father teach me. I was nervous when I take test. The policeman sit next to me. He tell me where to go. I drive carefully. I park the car good. He say I pass. I was very happy. I get my license. Now I can drive car to work. It is convenient. It was big success for me because I try hard.",
        "word_count": 88,
        "response_type": "long_turn",
        "vocabulary": 5, "grammar": 5,
        "vocab_reason": "[LR5] 'Succeed', 'driving test', 'practice', 'nervous', 'license', 'convenient'. Adequate.",
        "grammar_reason": "[GRA5] 'My father teach me' (Tense). 'When I take test' (Tense). 'Park the car good' (Adverb). Simple sentences mostly correct.",
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
        if sample["grammar"] <= 5:
             sample["micro_flaws"] = ["Basic sentence structures", "Frequent grammatical errors", "Limited vocabulary range"]
        else:
             sample["micro_flaws"] = []

        # Input/Output construction
        sample["input"] = f"Part: {sample['part']}\nQuestion: {sample['question']}\n\nTranscript: {sample['transcript_cleaned']}\n\nWord Count: {sample['word_count']} words\nResponse Type: {sample['response_type']}"

        output_text = f"## Vocabulary (Lexical Resource): Band {sample['vocabulary']}\n\n**Reasoning:** {sample['vocab_reason']}\n\n>Band {sample['vocabulary']-1}: ...\n\nNot Band {sample['vocabulary']+1}: ...\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band {sample['grammar']}\n\n**Reasoning:** {sample['grammar_reason']}\n\n>Band {sample['grammar']-1}: ...\n\nNot Band {sample['grammar']+1}: ...\n\n**Micro flaws identified:**\n- " + "\n- ".join(sample["micro_flaws"])

        sample["output"] = output_text

        f.write(json.dumps(sample) + '\n')
