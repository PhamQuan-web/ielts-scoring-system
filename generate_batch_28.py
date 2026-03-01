import json

OUTPUT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_28.jsonl"

samples = [
    # --- V6/G9 (1351-1360) ---
    {
        "sample_id": "syn_p2_v6_g9_1351",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a successful business.",
        "transcript_cleaned": "I would like to discuss a very popular local bakery that, having been established just a few years ago, has managed to completely dominate the market in my town. What is most interesting about this particular shop is the fact that it focuses entirely on traditional bread recipes, which many people thought would be a failing strategy in today's fast-paced world. Had the owners not been so determined to maintain high quality, the business would almost certainly have collapsed within its first six months. Not only do they produce delicious food, but they also offer exceptional customer service, making everyone feel welcome. By consistently listening to what their customers prefer, they have been able to adjust their daily production perfectly. Rarely do you see such dedication rewarded so quickly. It serves as an inspiring example of how doing simple things extremely well can still lead to massive success.",
        "word_count": 154,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 9,
        "vocab_reason": "[LR6] 'Popular local bakery', 'dominate the market', 'traditional bread recipes', 'failing strategy', 'fast-paced world', 'maintain high quality', 'collapsed', 'delicious food', 'exceptional customer service', 'daily production', 'dedication rewarded', 'inspiring example', 'massive success'. Good range, clear meaning.",
        "grammar_reason": "[GRA9] 'that, having been established... has managed to' (Relative/Perfect participle). 'What is most interesting... is the fact that' (Cleft/Noun clause). 'which many people thought would be' (Relative/Noun). 'Had the owners not been... the business would... have collapsed' (Third conditional inversion). 'Not only do they produce... but they also offer' (Negative inversion). 'By consistently listening... they have been able' (Preposition+Gerund). Error-free, native-like flexibility.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g9_1352",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe an important river.",
        "transcript_cleaned": "I am going to describe a wide river that runs directly through the center of the capital city, effectively dividing it into two distinct halves. Historically, it was primarily utilized as a major transport route for heavy goods, enabling the city to grow rapidly during the industrial period. What deeply concerns many local residents nowadays is the fact that the water level has been dropping steadily, largely due to reduced rainfall in the mountains. Were the government to ignore this pressing issue, it is highly probable that the city would face severe water shortages next summer. To combat this, they have recently introduced strict new rules regarding water usage, which, provided they are enforced properly, should help the situation. Furthermore, the riverbanks have been completely redeveloped into attractive public parks. It remains a vital feature of the city that demands our constant attention and careful protection.",
        "word_count": 153,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 9,
        "vocab_reason": "[LR6] 'Wide river', 'capital city', 'distinct halves', 'transport route', 'heavy goods', 'industrial period', 'local residents', 'dropping steadily', 'reduced rainfall', 'pressing issue', 'water shortages', 'strict new rules', 'water usage', 'redeveloped', 'attractive public parks', 'vital feature', 'careful protection'. Adequate vocabulary.",
        "grammar_reason": "[GRA9] 'that runs directly... effectively dividing' (Relative/Participle). 'What deeply concerns... is the fact that' (Cleft/Noun). 'Were the government to ignore... it is highly probable that... would face' (Second conditional inversion). 'which, provided they are enforced properly, should help' (Relative/Conditional). Error-free, highly flexible grammar.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g9_1353",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "A tough decision I had to make involved choosing whether to continue my studies at a local university or accept an exciting job offer abroad. Having spent my entire life in one town, the prospect of moving to a completely different country was both thrilling and terrifying. On the one hand, taking the job would provide me with immediate financial independence, which I desperately wanted at the time. On the other hand, rejecting the university place meant delaying my formal education, a choice that my parents were strongly against. After carefully weighing all the possible outcomes, I ultimately decided to take the job, realizing that such opportunities rarely present themselves twice. Had I chosen to stay and study, I might never have gained the practical experience I now possess. Looking back, it was undeniably the right choice, even though it caused some temporary family tension.",
        "word_count": 152,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 9,
        "vocab_reason": "[LR6] 'Tough decision', 'local university', 'job offer abroad', 'prospect', 'thrilling and terrifying', 'financial independence', 'delaying', 'formal education', 'weighing all the possible outcomes', 'opportunities', 'practical experience', 'possess', 'undeniably', 'temporary family tension'.",
        "grammar_reason": "[GRA9] 'choosing whether to continue... or accept' (Noun clause/Infinitive). 'Having spent my entire life... the prospect... was' (Perfect participle). 'taking the job would provide... which I desperately wanted' (Gerund subject/Relative). 'rejecting... meant delaying... a choice that' (Gerund subject/Appositive/Relative). 'After carefully weighing... I decided... realizing that' (Preposition+Gerund/Participle/Noun). 'Had I chosen... I might never have gained' (Third conditional inversion). Error-free, sophisticated control.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g9_1354",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a popular product.",
        "transcript_cleaned": "I would like to talk about the electric scooter, a product that has seen a massive surge in popularity across my city over the last twelve months. Unlike traditional methods of transport, these scooters offer a highly convenient way to navigate through heavy traffic, making them especially appealing to daily commuters. What makes them so universally attractive is the fact that they are relatively cheap to rent and require almost no physical effort to ride. Had the city council not built dedicated cycle lanes recently, riding them on the main roads would certainly have been far too dangerous. However, it must be said that they can occasionally be a nuisance for pedestrians, particularly when they are left parked carelessly on the pavements. Nevertheless, provided they are used responsibly, I believe they represent a fantastic, environmentally friendly solution to urban transport problems that will only grow in popularity.",
        "word_count": 156,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 9,
        "vocab_reason": "[LR6] 'Electric scooter', 'massive surge', 'popularity', 'traditional methods', 'convenient way', 'navigate', 'heavy traffic', 'daily commuters', 'universally attractive', 'physical effort', 'dedicated cycle lanes', 'main roads', 'dangerous', 'nuisance', 'pedestrians', 'carelessly', 'pavements', 'responsibly', 'environmentally friendly solution', 'urban transport problems'.",
        "grammar_reason": "[GRA9] 'a product that has seen' (Appositive/Relative). 'making them especially appealing' (Participle). 'What makes them so... is the fact that' (Cleft/Noun). 'Had the city council not built... riding them... would... have been' (Third conditional inversion/Gerund subject). 'it must be said that... particularly when they are left parked' (Passive/Noun/Time/Passive). 'provided they are used responsibly, I believe they represent' (Condition/Noun clause). Effortless complexity.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    {
        "sample_id": "syn_p2_v6_g9_1355",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a wild animal.",
        "transcript_cleaned": "I am going to describe the gray wolf, a highly intelligent predator that plays an absolutely crucial role in maintaining the balance of forest ecosystems. Typically living in tightly knit family groups known as packs, they are renowned for their complex social structures and highly effective cooperative hunting strategies. What I find most fascinating about wolves is their method of communication, utilizing a series of distinct howls to coordinate movements over vast distances. Unfortunately, having been hunted extensively for decades, their numbers dropped to dangerously low levels in many regions. Were it not for the strict conservation laws introduced recently, it is highly likely that they would have been driven to extinction in the wild. Thankfully, their populations are slowly beginning to recover, although they still face threats from habitat loss. They are truly magnificent creatures that command both fear and deep respect from those who understand them.",
        "word_count": 156,
        "response_type": "long_turn",
        "vocabulary": 6, "grammar": 9,
        "vocab_reason": "[LR6] 'Gray wolf', 'intelligent predator', 'crucial role', 'maintaining the balance', 'forest ecosystems', 'tightly knit family groups', 'packs', 'renowned', 'complex social structures', 'cooperative hunting strategies', 'fascinating', 'method of communication', 'distinct howls', 'coordinate movements', 'vast distances', 'hunted extensively', 'dangerously low levels', 'conservation laws', 'extinction', 'habitat loss', 'magnificent creatures', 'deep respect'.",
        "grammar_reason": "[GRA9] 'a highly intelligent predator that plays' (Appositive/Relative). 'Typically living in... they are renowned for' (Participle). 'What I find most fascinating... is their method... utilizing' (Cleft/Participle). 'having been hunted extensively... their numbers dropped' (Perfect passive participle). 'Were it not for... it is highly likely that they would have been' (Second conditional inversion/Noun clause/Passive). 'from those who understand them' (Relative). Complete control.",
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"}
    },
    # --- V9/G6 (1356-1365) ---
    {
        "sample_id": "syn_p2_v9_g6_1356",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I would like to expound upon an imposing medieval fortress that stands as a testament to unparalleled architectural ingenuity. This formidable citadel was strategically erected on a precipitous cliff to deter relentless marauders. The colossal stone ramparts and intricate subterranean dungeons are incredibly well-preserved, evoking a visceral sense of historical gravitas. I thoroughly enjoyed exploring the labyrinthine corridors and marveling at the ornate tapestries that adorn the banqueting hall. These artifacts vividly illustrating the opulent lifestyle of the erstwhile nobility. However, the relentless onslaught of inclement weather has steadily eroded the exterior facades, necessitating urgent, meticulous restoration efforts. It serves as an invaluable repository of regional heritage. I strongly advocate that the municipal authorities allocate substantial funding to safeguard this monumental edifice from irreversible dilapidation.",
        "word_count": 128,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 6,
        "vocab_reason": "[LR9] 'Expound upon', 'imposing medieval fortress', 'testament', 'unparalleled architectural ingenuity', 'formidable citadel', 'strategically erected', 'precipitous cliff', 'deter relentless marauders', 'colossal stone ramparts', 'intricate subterranean dungeons', 'visceral sense', 'historical gravitas', 'labyrinthine corridors', 'ornate tapestries', 'opulent lifestyle', 'erstwhile nobility', 'relentless onslaught', 'inclement weather', 'meticulous restoration', 'invaluable repository', 'municipal authorities', 'monumental edifice', 'irreversible dilapidation'. Wide range, precise.",
        "grammar_reason": "[GRA6] 'that stands as a testament' (Relative). 'was strategically erected... to deter' (Passive/Infinitive). 'evoking a visceral sense' (Participle). 'These artifacts vividly illustrating' (Error - Participle used as main verb). 'has steadily eroded... necessitating' (Present perfect/Participle). Mix of successful complex structures with some noticeable errors.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v9_g6_1357",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of technology.",
        "transcript_cleaned": "My indispensable lifeline to the modern world is an ultra-sleek, cutting-edge tablet that functions as a multifaceted productivity hub. Its ubiquitous presence in my daily routine has completely revolutionized my workflow, rendering obsolete many archaic organizational methods. The high-fidelity retina display and lightning-fast processing capabilities facilitate seamless multitasking and immersive media consumption. I utilize a plethora of sophisticated applications for digital illustration, which demands exceptional stylus responsiveness. The intuitive user interface empowering me to navigate complex software ecosystems with unprecedented fluidity. Unfortunately, the exorbitant initial investment and subsequent subscription models are financially draining. Furthermore, my heavy reliance on this device fostering a concerning degree of digital dependency. Nevertheless, its sheer versatility renders it an unparalleled asset in both my professional and personal endeavors.",
        "word_count": 130,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 6,
        "vocab_reason": "[LR9] 'Indispensable lifeline', 'ultra-sleek', 'cutting-edge', 'multifaceted productivity hub', 'ubiquitous presence', 'revolutionized my workflow', 'rendering obsolete', 'archaic organizational methods', 'high-fidelity retina display', 'seamless multitasking', 'immersive media consumption', 'plethora', 'sophisticated applications', 'digital illustration', 'exceptional stylus responsiveness', 'intuitive user interface', 'ecosystems', 'unprecedented fluidity', 'exorbitant initial investment', 'subscription models', 'financially draining', 'digital dependency', 'sheer versatility'.",
        "grammar_reason": "[GRA6] 'that functions as' (Relative). 'rendering obsolete many' (Participle). 'which demands' (Relative). 'interface empowering me' (Error - Participle used as main verb). 'reliance... fostering' (Error - Participle used as main verb). A mix of accurate simple and complex sentences, but with persistent structural flaws in participles.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v9_g6_1358",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a challenging task.",
        "transcript_cleaned": "Orchestrating a comprehensive overhaul of our corporate IT infrastructure was undeniably the most intellectually taxing undertaking of my career. The sheer magnitude of migrating terabytes of sensitive data to a cloud-based ecosystem without compromising operational continuity was staggeringly complex. The archaic legacy systems we inherited were notoriously volatile and prone to catastrophic failure. I meticulously coordinated a cross-functional team of specialized engineers to mitigate potential security vulnerabilities during the transition phase. We encountered unforeseen technical bottlenecks that necessitated rapid, high-stakes troubleshooting under immense pressure. The grueling hours and relentless stress inevitably taking a significant toll on our collective morale. However, the successful implementation ultimately streamlined our operational efficiency and fortified our cybersecurity posture. The entire ordeal proved to be an unparalleled crucible for developing robust leadership acumen.",
        "word_count": 135,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 6,
        "vocab_reason": "[LR9] 'Orchestrating', 'comprehensive overhaul', 'corporate IT infrastructure', 'intellectually taxing undertaking', 'magnitude', 'migrating terabytes', 'sensitive data', 'cloud-based ecosystem', 'operational continuity', 'staggeringly complex', 'archaic legacy systems', 'notoriously volatile', 'catastrophic failure', 'meticulously coordinated', 'cross-functional team', 'mitigate potential security vulnerabilities', 'unforeseen technical bottlenecks', 'high-stakes troubleshooting', 'grueling hours', 'collective morale', 'operational efficiency', 'fortified', 'cybersecurity posture', 'crucible', 'robust leadership acumen'.",
        "grammar_reason": "[GRA6] 'Orchestrating a comprehensive overhaul... was' (Gerund subject). 'The sheer magnitude of migrating... without compromising... was' (Complex prepositional subject). 'we inherited' (Relative clause omission). 'that necessitated' (Relative). 'The grueling hours... inevitably taking' (Error - Missing auxiliary/Participle as verb). Generally good control with occasional complex errors.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v9_g6_1359",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a traditional festival.",
        "transcript_cleaned": "The mesmerizing lantern festival is deeply embedded in our cultural psyche and serves as a poignant emblem of communal rejuvenation. The normally mundane cityscape undergoes a kaleidoscopic transformation, illuminated by myriad intricately crafted paper lanterns depicting mythical folklore. The meticulous culinary preparations, featuring an abundance of auspicious delicacies, are central to the festivities, symbolizing enduring prosperity. I anticipate the spectacular fireworks display, which orchestrates a deafening, yet exhilarating, sensory bombardment. These ancient rituals fostering a profound sense of generational continuity and shared heritage. Extended families congregate from disparate regions to partake in this joyous reunion. The palpable atmosphere of conviviality and mutual goodwill temporarily eclipsing the relentless pressures of contemporary life. It is an exquisitely vibrant manifestation of our indomitable cultural spirit.",
        "word_count": 128,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 6,
        "vocab_reason": "[LR9] 'Mesmerizing lantern festival', 'cultural psyche', 'poignant emblem', 'communal rejuvenation', 'mundane cityscape', 'kaleidoscopic transformation', 'myriad', 'intricately crafted', 'mythical folklore', 'meticulous culinary preparations', 'abundance', 'auspicious delicacies', 'enduring prosperity', 'spectacular fireworks', 'orchestrates', 'deafening', 'sensory bombardment', 'ancient rituals', 'generational continuity', 'shared heritage', 'disparate regions', 'partake', 'palpable atmosphere', 'conviviality', 'mutual goodwill', 'eclipsing', 'indomitable cultural spirit'.",
        "grammar_reason": "[GRA6] 'illuminated by myriad' (Participle phrase). 'featuring an abundance... symbolizing' (Participles). 'which orchestrates' (Relative). 'These ancient rituals fostering' (Error - Participle as verb). 'atmosphere... temporarily eclipsing' (Error - Participle as verb). Complex sentences attempted but accuracy is inconsistent.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    },
    {
        "sample_id": "syn_p2_v9_g6_1360",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a childhood memory.",
        "transcript_cleaned": "One of my most evocative childhood memories centers on the idyllic summers I spent foraging in a sprawling, sun-dappled forest near my ancestral home. The verdant canopy provided a serene sanctuary, teeming with an astonishing diversity of endemic flora and fauna. I accompanied my erudite grandfather, who possessed an encyclopedic knowledge of botany, on extended nature walks. He patiently elucidated the medicinal properties of obscure herbs and the intricate symbiotic relationships within the ecosystem. We collected an assortment of wild berries and fascinating geological specimens. The pungent aroma of damp soil and decaying leaves are indelibly imprinted on my olfactory memory. This immersive exposure to the natural world instilling in me a profound, lifelong reverence for environmental conservation. It was an era of unblemished innocence and unbridled curiosity.",
        "word_count": 131,
        "response_type": "long_turn",
        "vocabulary": 9, "grammar": 6,
        "vocab_reason": "[LR9] 'Evocative childhood memories', 'idyllic summers', 'foraging', 'sprawling, sun-dappled forest', 'ancestral home', 'verdant canopy', 'serene sanctuary', 'teeming with', 'endemic flora and fauna', 'erudite grandfather', 'encyclopedic knowledge', 'botany', 'elucidated', 'medicinal properties', 'obscure herbs', 'intricate symbiotic relationships', 'ecosystem', 'assortment', 'wild berries', 'geological specimens', 'pungent aroma', 'indelibly imprinted', 'olfactory memory', 'immersive exposure', 'reverence', 'conservation', 'unblemished innocence', 'unbridled curiosity'.",
        "grammar_reason": "[GRA6] 'I spent foraging' (Relative omission/Gerund). 'teeming with' (Participle phrase). 'who possessed' (Relative). 'aroma... are' (Error - Agreement). 'exposure... instilling' (Error - Participle as verb). Clear meaning, good complexity, but noticeable slips in grammar control.",
        "grammar_profile": {"complexity": "moderate", "accuracy": "controlled", "flexibility": "moderate"}
    }
]

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for sample in samples:
        sample["dataset_source"] = "synthetic"
        sample["is_valid"] = True
        sample["idiom_present"] = False
        sample["risk_level"] = "low"
        sample["instruction"] = "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning."
        sample["micro_flaws"] = []
        if sample["grammar"] <= 5:
             sample["micro_flaws"] = ["Basic sentence structures", "Frequent grammatical errors"]
        sample["word_count"] = len(sample["transcript_cleaned"].split())
        sample["input"] = f"Part: {sample['part']}\nQuestion: {sample['question']}\n\nTranscript: {sample['transcript_cleaned']}\n\nWord Count: {sample['word_count']} words\nResponse Type: {sample['response_type']}"
        output_text = f"## Vocabulary (Lexical Resource): Band {sample['vocabulary']}\n\n**Reasoning:** {sample['vocab_reason']}\n\n>Band {sample['vocabulary']-1}: ...\n\nNot Band {sample['vocabulary']+1}: ...\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band {sample['grammar']}\n\n**Reasoning:** {sample['grammar_reason']}\n\n>Band {sample['grammar']-1}: ...\n\nNot Band {sample['grammar']+1}: ...\n\n**Micro flaws identified:**\n- None."
        sample["output"] = output_text
        f.write(json.dumps(sample) + '\n')
