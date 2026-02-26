import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch14.jsonl")

def create_sample(index, vocab_band, grammar_band, question, transcript, response_type,
                  micro_flaws, grammar_profile, vocab_reason, grammar_reason,
                  idiom_present, risk_level):

    sample_id = f"syn_p3_v{vocab_band}_g{grammar_band}_{index:03d}"
    word_count = len(transcript.split())

    input_text = (
        f"Part: 3\n"
        f"Question: {question}\n\n"
        f"Transcript: {transcript}\n\n"
        f"Word Count: {word_count} words\n"
        f"Response Type: {response_type}"
    )

    output_text = (
        f"## Vocabulary (Lexical Resource): Band {vocab_band}\n\n"
        f"**Reasoning:** {vocab_reason}\n\n"
        f"**Idiom present:** {'Yes' if idiom_present else 'No'}\n"
        f"**Risk level:** {risk_level.capitalize()}\n\n"
        f"---\n\n"
        f"## Grammar (Grammatical Range & Accuracy): Band {grammar_band}\n\n"
        f"**Reasoning:** {grammar_reason}\n\n"
        f"**Micro flaws identified:**\n" +
        "\n".join([f"- {flaw}" for flaw in micro_flaws])
    )

    return {
        "sample_id": sample_id,
        "video_id": "synthetic",
        "part": 3,
        "question": question,
        "transcript_cleaned": transcript,
        "word_count": word_count,
        "response_type": response_type,
        "micro_flaws": micro_flaws,
        "grammar_profile": grammar_profile,
        "vocab_reason": vocab_reason,
        "grammar_reason": grammar_reason,
        "vocabulary": vocab_band,
        "grammar": grammar_band,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": idiom_present,
        "risk_level": risk_level,
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": input_text,
        "output": output_text
    }

samples = []

# --- BATCH 14 PART 3: SAMPLES 1245-1284 (40 Total) ---
# Combo: V4/G8 (Basic Vocab, Expert Grammar)
# Strategy: Use very simple words ("good", "bad", "happy", "big") but construct complex, error-free sentences (conditionals, relative clauses, passive voice).

topics_14_3 = [
    {
        "question": "Is reading good?",
        "transcript": "Reading is good because it helps you learn. If you read a book, you can know many things. Although some books are hard, they are good for you. A person who reads is smart. I think that we should read more.",
        "vocab_reason": "[LR4] Simple words: 'good', 'learn', 'know', 'hard', 'smart'. >Band 3: Understandable. Not Band 5: Lacks 'educate', 'knowledge', 'challenging'.",
        "grammar_reason": "[GRA8] Complex structures: 'because it helps...', 'If you read...', 'Although some books...', 'person who reads'. Error-free. >Band 7: High accuracy."
    },
    {
        "question": "Is walking good?",
        "transcript": "Walking is the best way to go to places. If you walk, you do not need a car. Although it is slow, it is nice. People who walk are happy. It is good for your body to move.",
        "vocab_reason": "[LR4] Basic vocab: 'best way', 'go', 'car', 'slow', 'nice', 'happy'. >Band 3: Clear. Not Band 5: Lacks 'transport', 'healthy', 'exercise'.",
        "grammar_reason": "[GRA8] Conditional: 'If you walk...'. Contrast: 'Although it is...'. Relative clause: 'People who walk...'. Error-free. >Band 7: Sophisticated."
    },
    {
        "question": "Why save money?",
        "transcript": "Money is good to have. If you save money, you can buy things later. Although it is hard to save, it is important. A person with money is safe. We should put money in the bank.",
        "vocab_reason": "[LR4] Simple words: 'money', 'good', 'save', 'buy', 'hard', 'safe'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'financial', 'future', 'security'.",
        "grammar_reason": "[GRA8] Conditional: 'If you save...'. Contrast: 'Although it is...'. Modal: 'should put'. Error-free. >Band 7: Good control."
    },
    {
        "question": "Is water important?",
        "transcript": "Water is something we need to drink. If there is no water, we will be thirsty. Although the sea has water, we cannot drink it. We must be careful not to waste it. It is a good thing for life.",
        "vocab_reason": "[LR4] Basic vocab: 'drink', 'thirsty', 'sea', 'waste', 'good thing'. >Band 3: Understandable. Not Band 5: Lacks 'survive', 'essential', 'resource'.",
        "grammar_reason": "[GRA8] Relative clause: 'something we need...'. Conditional: 'If there is...'. Contrast: 'Although the sea...'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Are friends good?",
        "transcript": "Friends are people who like you. If you are sad, they make you happy. Although you might fight, they are good to have. A life with friends is fun. We should be nice to the people we know.",
        "vocab_reason": "[LR4] Simple words: 'like', 'sad', 'happy', 'fight', 'fun', 'nice'. >Band 3: Clear. Not Band 5: Lacks 'support', 'relationship', 'enjoyable'.",
        "grammar_reason": "[GRA8] Relative clause: 'people who like...'. Conditional: 'If you are...'. Contrast: 'Although you might...'. Error-free. >Band 7: High level."
    },
    {
        "question": "Why sleep?",
        "transcript": "Sleep is good for you. If you do not sleep, you get tired. Although we have work, we must rest. People who sleep well feel good. It is important to go to bed at night.",
        "vocab_reason": "[LR4] Basic vocab: 'good', 'tired', 'work', 'rest', 'bed', 'night'. >Band 3: Meaning clear. Not Band 5: Lacks 'energy', 'health', 'necessary'.",
        "grammar_reason": "[GRA8] Conditional: 'If you do not...'. Contrast: 'Although we have...'. Relative clause: 'People who sleep...'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Is music nice?",
        "transcript": "Music is something that everyone likes. If you listen to a song, you feel happy. Although some music is loud, it is fun. I think that music is the best thing. We should listen to it every day.",
        "vocab_reason": "[LR4] Simple words: 'likes', 'song', 'happy', 'loud', 'fun', 'best'. >Band 3: Understandable. Not Band 5: Lacks 'enjoy', 'melody', 'rhythm'.",
        "grammar_reason": "[GRA8] Relative clause: 'something that everyone likes'. Conditional: 'If you listen...'. Contrast: 'Although some music...'. Error-free."
    },
    {
        "question": "Why eat fruit?",
        "transcript": "Fruit is good to eat. If you eat an apple, you will be healthy. Although candy is sweet, fruit is better. People who eat fruit are not sick. It is a good food for your body.",
        "vocab_reason": "[LR4] Basic vocab: 'good', 'eat', 'apple', 'healthy', 'sweet', 'sick'. >Band 3: Clear. Not Band 5: Lacks 'nutritious', 'diet', 'vitamin'.",
        "grammar_reason": "[GRA8] Conditional: 'If you eat...'. Contrast: 'Although candy is...'. Relative clause: 'People who eat...'. Error-free. >Band 7: Good control."
    },
    {
        "question": "Is school hard?",
        "transcript": "School can be hard work. If you study, you will learn. Although tests are bad, they help you. A student who works hard is good. We should go to school to learn things.",
        "vocab_reason": "[LR4] Simple words: 'hard work', 'study', 'learn', 'tests', 'bad', 'student'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'education', 'difficult', 'knowledge'.",
        "grammar_reason": "[GRA8] Conditional: 'If you study...'. Contrast: 'Although tests are...'. Relative clause: 'student who works...'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Are dogs good?",
        "transcript": "Dogs are animals that live with us. If you are lonely, a dog is a friend. Although they bark, they are nice. People who have dogs are happy. It is good to play with a dog.",
        "vocab_reason": "[LR4] Basic vocab: 'animals', 'live', 'lonely', 'friend', 'bark', 'play'. >Band 3: Understandable. Not Band 5: Lacks 'pet', 'companion', 'loyal'.",
        "grammar_reason": "[GRA8] Relative clause: 'animals that live...'. Conditional: 'If you are...'. Contrast: 'Although they bark...'. Error-free. >Band 7: High level."
    },
    {
        "question": "Why work?",
        "transcript": "We work to get money. If we do not work, we cannot buy food. Although work is tiring, we must do it. A job that you like is good. We should try to find good work.",
        "vocab_reason": "[LR4] Simple words: 'money', 'buy', 'food', 'tiring', 'job', 'good'. >Band 3: Clear. Not Band 5: Lacks 'earn', 'salary', 'career'.",
        "grammar_reason": "[GRA8] Purpose: 'work to get...'. Conditional: 'If we do not...'. Contrast: 'Although work is...'. Relative clause: 'job that you like'. Error-free."
    },
    {
        "question": "Is rain bad?",
        "transcript": "Rain is water from the sky. If it rains, plants grow. Although it is wet, we need it. People who have gardens like rain. It is a good thing for the earth.",
        "vocab_reason": "[LR4] Basic vocab: 'water', 'sky', 'plants', 'grow', 'wet', 'gardens'. >Band 3: Meaning clear. Not Band 5: Lacks 'weather', 'nature', 'necessary'.",
        "grammar_reason": "[GRA8] Conditional: 'If it rains...'. Contrast: 'Although it is...'. Relative clause: 'People who have...'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Why help?",
        "transcript": "Helping is a nice thing to do. If you help someone, they are happy. Although it takes time, it is good. A person who helps is kind. We should help people when we can.",
        "vocab_reason": "[LR4] Simple words: 'nice', 'happy', 'time', 'good', 'kind'. >Band 3: Understandable. Not Band 5: Lacks 'support', 'assist', 'generous'.",
        "grammar_reason": "[GRA8] Conditional: 'If you help...'. Contrast: 'Although it takes...'. Relative clause: 'person who helps...'. Error-free. >Band 7: Good control."
    },
    {
        "question": "Is fire hot?",
        "transcript": "Fire is very hot. If you touch it, you will get hurt. Although it is dangerous, we use it to cook. Fire is something that gives light. We must be careful with it.",
        "vocab_reason": "[LR4] Basic vocab: 'hot', 'touch', 'hurt', 'dangerous', 'cook', 'light'. >Band 3: Clear. Not Band 5: Lacks 'heat', 'burn', 'energy'.",
        "grammar_reason": "[GRA8] Conditional: 'If you touch...'. Contrast: 'Although it is...'. Relative clause: 'something that gives...'. Error-free. >Band 7: High level."
    },
    {
        "question": "Why run?",
        "transcript": "Running makes you fast. If you run every day, you are strong. Although it is hard, it is fun. People who run have good legs. It is a good way to move.",
        "vocab_reason": "[LR4] Simple words: 'fast', 'strong', 'hard', 'fun', 'legs', 'move'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'exercise', 'speed', 'muscles'.",
        "grammar_reason": "[GRA8] Conditional: 'If you run...'. Contrast: 'Although it is...'. Relative clause: 'People who run...'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Is cold bad?",
        "transcript": "Cold weather is not bad. If you wear a coat, you are warm. Although I like the sun, snow is pretty. A day that is cold can be nice. We should go outside and play.",
        "vocab_reason": "[LR4] Basic vocab: 'weather', 'bad', 'coat', 'warm', 'sun', 'snow'. >Band 3: Understandable. Not Band 5: Lacks 'temperature', 'winter', 'clothing'.",
        "grammar_reason": "[GRA8] Conditional: 'If you wear...'. Contrast: 'Although I like...'. Relative clause: 'day that is cold'. Error-free. >Band 7: Good control."
    },
    {
        "question": "Why clean?",
        "transcript": "Cleaning makes the house nice. If it is dirty, it is bad. Although cleaning is boring, we must do it. A clean house is a happy place. We should clean our room every week.",
        "vocab_reason": "[LR4] Simple words: 'house', 'nice', 'dirty', 'bad', 'boring', 'room'. >Band 3: Clear. Not Band 5: Lacks 'tidy', 'messy', 'environment'.",
        "grammar_reason": "[GRA8] Conditional: 'If it is...'. Contrast: 'Although cleaning is...'. Modal: 'must do', 'should clean'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Is fish food?",
        "transcript": "Fish is food that comes from the sea. If you cook it, it tastes good. Although it smells, it is healthy. People who eat fish are strong. It is good to eat fish sometimes.",
        "vocab_reason": "[LR4] Basic vocab: 'food', 'sea', 'cook', 'tastes', 'smells', 'strong'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'seafood', 'nutrition', 'diet'.",
        "grammar_reason": "[GRA8] Relative clause: 'food that comes...'. Conditional: 'If you cook...'. Contrast: 'Although it smells...'. Error-free. >Band 7: High level."
    },
    {
        "question": "Why talk?",
        "transcript": "Talking helps us say things. If we do not talk, no one knows what we think. Although it can be loud, it is good. A person who talks a lot is funny. We should talk to our friends.",
        "vocab_reason": "[LR4] Simple words: 'say things', 'knows', 'think', 'loud', 'good', 'funny'. >Band 3: Understandable. Not Band 5: Lacks 'communicate', 'express', 'opinion'.",
        "grammar_reason": "[GRA8] Conditional: 'If we do not talk...'. Contrast: 'Although it can be...'. Relative clause: 'person who talks...'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Is time long?",
        "transcript": "Time can be long or short. If you are having fun, it is fast. Although a day is long, it goes by. Time is something that we cannot stop. We should use our time well.",
        "vocab_reason": "[LR4] Basic vocab: 'long', 'short', 'fun', 'fast', 'stop', 'use'. >Band 3: Clear. Not Band 5: Lacks 'duration', 'quickly', 'precious'.",
        "grammar_reason": "[GRA8] Conditional: 'If you are having...'. Contrast: 'Although a day is...'. Relative clause: 'something that we cannot...'. Error-free. >Band 7: Good control."
    },
    {
        "question": "Why smile?",
        "transcript": "A smile is a nice thing. If you smile, people like you. Although you might be sad, a smile helps. A face with a smile is pretty. We should smile at everyone we see.",
        "vocab_reason": "[LR4] Simple words: 'nice thing', 'like', 'sad', 'helps', 'face', 'pretty'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'gesture', 'friendly', 'expression'.",
        "grammar_reason": "[GRA8] Conditional: 'If you smile...'. Contrast: 'Although you might be...'. Relative clause: 'everyone we see'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Is tree big?",
        "transcript": "A tree is a big plant. If it grows for a long time, it gets tall. Although it does not move, it is alive. Trees are things that birds like. We should not cut them down.",
        "vocab_reason": "[LR4] Basic vocab: 'big', 'plant', 'grows', 'tall', 'move', 'alive'. >Band 3: Understandable. Not Band 5: Lacks 'nature', 'environment', 'protect'.",
        "grammar_reason": "[GRA8] Conditional: 'If it grows...'. Contrast: 'Although it does not...'. Relative clause: 'things that birds like'. Error-free. >Band 7: High level."
    },
    {
        "question": "Why cook?",
        "transcript": "We cook to make food hot. If we eat raw meat, we get sick. Although cooking takes time, it makes food good. A person who cooks is a cook. It is nice to eat a hot meal.",
        "vocab_reason": "[LR4] Simple words: 'hot', 'raw meat', 'sick', 'time', 'good', 'meal'. >Band 3: Clear. Not Band 5: Lacks 'prepare', 'ingredients', 'delicious'.",
        "grammar_reason": "[GRA8] Purpose: 'cook to make...'. Conditional: 'If we eat...'. Contrast: 'Although cooking takes...'. Relative clause: 'person who cooks...'. Error-free."
    },
    {
        "question": "Is bus fast?",
        "transcript": "A bus is big and slow. If there are many cars, the bus stops. Although it is not fast, it carries many people. A bus is a car for everyone. We should take the bus to school.",
        "vocab_reason": "[LR4] Basic vocab: 'big', 'slow', 'cars', 'stops', 'fast', 'school'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'transport', 'traffic', 'public'.",
        "grammar_reason": "[GRA8] Conditional: 'If there are...'. Contrast: 'Although it is not...'. Modal: 'should take'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Why sit?",
        "transcript": "We sit when we are tired. If we stand all day, our legs hurt. Although chairs are hard, they are good. Sitting is something we do a lot. It is good to sit down and rest.",
        "vocab_reason": "[LR4] Simple words: 'tired', 'stand', 'legs hurt', 'chairs', 'hard', 'rest'. >Band 3: Understandable. Not Band 5: Lacks 'relax', 'posture', 'comfortable'.",
        "grammar_reason": "[GRA8] Time clause: 'when we are...'. Conditional: 'If we stand...'. Contrast: 'Although chairs are...'. Relative clause: 'something we do'. Error-free."
    },
    {
        "question": "Is cat nice?",
        "transcript": "A cat is a small animal. If you pet it, it is soft. Although it has claws, it is cute. People who like cats are nice. It is a good pet for a house.",
        "vocab_reason": "[LR4] Basic vocab: 'small', 'animal', 'pet', 'soft', 'claws', 'cute'. >Band 3: Clear. Not Band 5: Lacks 'feline', 'domestic', 'companion'.",
        "grammar_reason": "[GRA8] Conditional: 'If you pet it...'. Contrast: 'Although it has...'. Relative clause: 'People who like...'. Error-free. >Band 7: Good control."
    },
    {
        "question": "Why swim?",
        "transcript": "Swimming is fun in the water. If you can swim, you are safe. Although the water is cold, it feels good. Swimming is a sport that I like. We should swim in the summer.",
        "vocab_reason": "[LR4] Simple words: 'fun', 'water', 'safe', 'cold', 'feels good', 'summer'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'exercise', 'pool', 'refreshing'.",
        "grammar_reason": "[GRA8] Conditional: 'If you can swim...'. Contrast: 'Although the water is...'. Relative clause: 'sport that I like'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Is dark scary?",
        "transcript": "The dark is when there is no sun. If it is dark, we cannot see. Although I am big, I do not like the dark. The dark is a place for sleep. We turn on the light.",
        "vocab_reason": "[LR4] Basic vocab: 'sun', 'see', 'big', 'sleep', 'turn on', 'light'. >Band 3: Understandable. Not Band 5: Lacks 'night', 'afraid', 'vision'.",
        "grammar_reason": "[GRA8] Time clause: 'when there is...'. Conditional: 'If it is...'. Contrast: 'Although I am...'. Error-free. >Band 7: High level."
    },
    {
        "question": "Why play?",
        "transcript": "Playing is what kids do. If you play, you are happy. Although games are just for fun, they are good. A game that you win is the best. We should play with our friends.",
        "vocab_reason": "[LR4] Simple words: 'kids', 'happy', 'games', 'fun', 'win', 'best'. >Band 3: Clear. Not Band 5: Lacks 'children', 'activity', 'enjoy'.",
        "grammar_reason": "[GRA8] Relative clause: 'what kids do'. Conditional: 'If you play...'. Contrast: 'Although games are...'. Relative clause: 'game that you win'. Error-free."
    },
    {
        "question": "Is cake good?",
        "transcript": "Cake is a sweet food. If you eat it, it tastes nice. Although it has sugar, I like it. A birthday is a day for cake. It makes people happy to eat cake.",
        "vocab_reason": "[LR4] Basic vocab: 'sweet', 'food', 'eat', 'nice', 'sugar', 'birthday'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'dessert', 'delicious', 'celebrate'.",
        "grammar_reason": "[GRA8] Conditional: 'If you eat...'. Contrast: 'Although it has...'. Infinitive: 'happy to eat'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Why love?",
        "transcript": "Love is a good feeling. If you love someone, you are nice to them. Although love can hurt, it is the best thing. A person in love is happy. We should love our family.",
        "vocab_reason": "[LR4] Simple words: 'good feeling', 'nice', 'hurt', 'best thing', 'happy'. >Band 3: Understandable. Not Band 5: Lacks 'emotion', 'relationship', 'care'.",
        "grammar_reason": "[GRA8] Conditional: 'If you love...'. Contrast: 'Although love can...'. Modal: 'should love'. Error-free. >Band 7: Good control."
    },
    {
        "question": "Is bird small?",
        "transcript": "A bird is a small animal that flies. If it has wings, it can fly. Although it is small, it sings loud. Birds are animals that live in trees. It is nice to hear a bird.",
        "vocab_reason": "[LR4] Basic vocab: 'small', 'animal', 'flies', 'wings', 'loud', 'hear'. >Band 3: Clear. Not Band 5: Lacks 'creature', 'soar', 'melody'.",
        "grammar_reason": "[GRA8] Relative clause: 'animal that flies'. Conditional: 'If it has...'. Contrast: 'Although it is...'. Relative clause: 'animals that live'. Error-free."
    },
    {
        "question": "Why buy?",
        "transcript": "We buy things we need. If we have money, we go to the shop. Although I want everything, I only buy food. Buying is something we do. It is good to have new things.",
        "vocab_reason": "[LR4] Simple words: 'need', 'money', 'shop', 'want', 'food', 'new'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'purchase', 'afford', 'consumer'.",
        "grammar_reason": "[GRA8] Relative clause: 'things we need'. Conditional: 'If we have...'. Contrast: 'Although I want...'. Relative clause: 'something we do'. Error-free."
    },
    {
        "question": "Is car fast?",
        "transcript": "A car goes fast on the road. If you drive fast, you get there soon. Although cars are dangerous, we like them. A fast car is fun. We should drive safe.",
        "vocab_reason": "[LR4] Basic vocab: 'fast', 'road', 'drive', 'soon', 'dangerous', 'safe'. >Band 3: Understandable. Not Band 5: Lacks 'speed', 'vehicle', 'carefully'.",
        "grammar_reason": "[GRA8] Conditional: 'If you drive...'. Contrast: 'Although cars are...'. Modal: 'should drive'. Error-free. >Band 7: High level."
    },
    {
        "question": "Why jump?",
        "transcript": "We jump to go up. If you jump high, you are strong. Although it is hard, kids like to jump. Jumping is a way to play. It is fun to be in the air.",
        "vocab_reason": "[LR4] Simple words: 'go up', 'high', 'strong', 'hard', 'kids', 'air'. >Band 3: Clear. Not Band 5: Lacks 'leap', 'exercise', 'activity'.",
        "grammar_reason": "[GRA8] Purpose: 'jump to go...'. Conditional: 'If you jump...'. Contrast: 'Although it is...'. Infinitive: 'fun to be'. Error-free."
    },
    {
        "question": "Is ball round?",
        "transcript": "A ball is round and rolls. If you kick it, it moves. Although it is just a toy, it is fun. Boys who play with balls are happy. It is good to play a game.",
        "vocab_reason": "[LR4] Basic vocab: 'round', 'rolls', 'kick', 'moves', 'toy', 'boys'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'sphere', 'sport', 'shape'.",
        "grammar_reason": "[GRA8] Conditional: 'If you kick...'. Contrast: 'Although it is...'. Relative clause: 'Boys who play...'. Error-free. >Band 7: Accurate."
    },
    {
        "question": "Why cry?",
        "transcript": "We cry when we are sad. If you hurt yourself, you cry. Although big boys do not cry, it is okay. Crying makes you feel better. We should not laugh at people who cry.",
        "vocab_reason": "[LR4] Simple words: 'sad', 'hurt', 'okay', 'feel better', 'laugh'. >Band 3: Understandable. Not Band 5: Lacks 'tears', 'upset', 'emotion'.",
        "grammar_reason": "[GRA8] Time clause: 'when we are...'. Conditional: 'If you hurt...'. Contrast: 'Although big boys...'. Relative clause: 'people who cry'. Error-free."
    },
    {
        "question": "Is sun hot?",
        "transcript": "The sun is very hot and big. If you look at it, your eyes hurt. Although it is far away, it keeps us warm. The sun is a star. It is good to see the sun.",
        "vocab_reason": "[LR4] Basic vocab: 'hot', 'big', 'look', 'eyes', 'far away', 'warm'. >Band 3: Clear. Not Band 5: Lacks 'heat', 'bright', 'energy'.",
        "grammar_reason": "[GRA8] Conditional: 'If you look...'. Contrast: 'Although it is...'. Infinitive: 'good to see'. Error-free. >Band 7: Good control."
    },
    {
        "question": "Why eat?",
        "transcript": "We eat because we are hungry. If we do not eat, we get sick. Although food costs money, we need it. Eating is something we do every day. It makes us strong.",
        "vocab_reason": "[LR4] Simple words: 'hungry', 'sick', 'costs money', 'every day', 'strong'. >Band 3: Meaning conveyed. Not Band 5: Lacks 'starve', 'nutrition', 'survive'.",
        "grammar_reason": "[GRA8] Reason: 'because we are...'. Conditional: 'If we do not...'. Contrast: 'Although food costs...'. Relative clause: 'something we do'. Error-free."
    },
    {
        "question": "Is snow cold?",
        "transcript": "Snow is cold and white. If it snows, we wear hats. Although it is cold, we play in it. Snow is water that is frozen. It is fun to make a snowman.",
        "vocab_reason": "[LR4] Basic vocab: 'cold', 'white', 'hats', 'play', 'water', 'snowman'. >Band 3: Understandable. Not Band 5: Lacks 'winter', 'temperature', 'ice'.",
        "grammar_reason": "[GRA8] Conditional: 'If it snows...'. Contrast: 'Although it is...'. Relative clause: 'water that is frozen'. Error-free. >Band 7: Accurate."
    }
]

# Total 40 samples

start_index = 1245
for i, item in enumerate(topics_14_3):
    samples.append(create_sample(
        index=start_index + i,
        vocab_band=4,
        grammar_band=8,
        question=item["question"],
        transcript=item["transcript"],
        response_type="extended",
        micro_flaws=[],
        grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
        vocab_reason=item["vocab_reason"],
        grammar_reason=item["grammar_reason"],
        idiom_present=False,
        risk_level="low"
    ))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
