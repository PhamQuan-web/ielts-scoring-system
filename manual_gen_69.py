import json

batch_num = 69
filename = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p1_10.jsonl"
start_id = 451
samples = []

# Batch 69: V7/G7(10) V8/G8(10) V9/G9(13) | IDs: 0451–0483 (Total 33 samples)

# V7 / G7 (Weather and Seasons)
c1_t = [
    ("What is your favorite season?", "My absolute favorite season is early autumn, primarily because the oppressive humidity of summer finally begins to dissipate. The air becomes wonderfully crisp and refreshing, and the vibrant transition of the leaves turning golden brown is incredibly picturesque. It is the perfect weather for taking long, relaxing walks."),
    ("Do you prefer a hot or a cold climate?", "I strongly prefer residing in a cooler climate, despite the occasional inconvenience of heavy snowfall. The intense, sweltering heat of a tropical summer frequently leaves me feeling completely exhausted and unmotivated. Conversely, the brisk winter air feels remarkably invigorating and significantly improves my daily productivity."),
    ("How does the weather affect your daily mood?", "The prevailing weather conditions undeniably exert a significant influence on my overall emotional state. On a bright, sunlit morning, I naturally feel remarkably optimistic and eager to tackle my challenging workload. However, several consecutive days of gloomy, torrential rain inevitably make me feel slightly sluggish and somewhat melancholic."),
    ("Do you think the weather in your country has changed recently?", "I have definitely observed noticeable shifts in our traditional weather patterns over the past few years. The summer heatwaves seem substantially more intense, and the winter snowfall is becoming increasingly erratic and unpredictable. This growing environmental instability is a very concerning development for our local agricultural sector."),
    ("What do you usually do on a rainy day?", "When a sudden rainstorm completely disrupts my outdoor plans, I usually retreat to my comfortable living room with a dense novel. Listening to the rhythmic sound of raindrops hitting the windowpane creates an incredibly peaceful, cozy atmosphere. It provides a wonderful, unexpected excuse to simply relax indoors."),
    ("Do you like to check the weather forecast before you travel?", "I invariably check the detailed weather forecast before embarking on any significant journey. Being caught unprepared in a severe thunderstorm or a sudden blizzard can quickly transform a pleasant holiday into a miserable ordeal. Packing appropriate clothing based on reliable meteorological predictions is absolutely essential for comfort."),
    ("Have you ever experienced extreme weather conditions?", "Yes, several years ago, I vividly remember experiencing a terrifyingly powerful typhoon while vacationing on the southern coast. The sheer ferocity of the howling wind and the torrential rain was genuinely frightening. We were completely confined indoors for two entire days until the violent storm finally passed."),
    ("What is the best type of weather for outdoor sports?", "The ideal weather for rigorous outdoor sports is definitely a cool, slightly overcast spring morning. If the sun is blindingly bright and the temperature is too high, athletes quickly risk severe dehydration and dangerous heat exhaustion. A gentle breeze and moderate temperatures allow for maximum physical exertion."),
    ("Do you prefer wet or dry seasons?", "I generally lean towards preferring the dry season because it vastly simplifies daily logistical planning. Constant, heavy rainfall makes the daily commute incredibly frustrating and frequently causes major delays on the public transit system. A dry climate allows for much more reliable, spontaneous outdoor social activities."),
    ("How do people in your country celebrate the arrival of spring?", "In my country, the arrival of spring is enthusiastically celebrated with numerous vibrant outdoor festivals. Families traditionally gather in the sprawling local parks to admire the magnificent cherry blossoms and share elaborate, homemade picnics. It marks a joyous, communal transition from the dark, isolating winter months.")
]
for q, t in c1_t:
    wc = len(t.split())
    # Minor grammar slip for G7
    t = t.replace("Families traditionally gather", "Families traditionally gathers")
    samples.append({
        "sample_id": f"syn_p1_v7_g7_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 7, "grammar": 7, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR7] Good range of less common vocabulary ('oppressive humidity', 'sweltering heat', 'meteorological predictions'). Paraphrasing is effective.",
        "grammar_reason": "[GRA7] Frequently produces error-free complex sentences ('On a bright, sunlit morning...', 'When a sudden rainstorm...'). Minor slips in agreement ('Families traditionally gathers') keep it at a 7.",
        "micro_flaws": ["agreement slip: 'Families traditionally gathers'"],
        "grammar_profile": {"complexity": "high", "accuracy": "high", "flexibility": "high"},
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Good range of less common vocabulary used with flexibility and precision.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Produces frequent error-free complex sentences, but occasional minor slips occur."
    })
    start_id += 1

# V8 / G8 (Education and Learning)
c2_t = [
    ("What was your favorite subject in high school?", "My absolute favorite subject during high school was undeniably advanced literature, primarily because it constantly challenged my analytical capabilities. By meticulously dissecting complex narratives and interpreting subtle metaphorical themes, I significantly broadened my understanding of human psychology. This rigorous intellectual exercise proved to be incredibly stimulating and deeply rewarding."),
    ("Do you think practical skills should be taught more in schools?", "I vehemently agree that integrating practical, vocational skills into the standard academic curriculum is an absolute necessity. While mastering abstract mathematical theorems is undoubtedly valuable, equipping students with fundamental financial literacy or basic technological troubleshooting guarantees their immediate competence in the real world. A purely theoretical education is fundamentally incomplete."),
    ("How do you usually study for important exams?", "My typical preparation strategy involves systematically breaking down the dense syllabus into highly manageable, thematic sections several weeks in advance. By rigorously adhering to a disciplined revision schedule, I effectively circumvent the immense psychological pressure of last-minute cramming. This incredibly methodical approach ensures I retain the complex information thoroughly."),
    ("Did you prefer working in groups or studying alone?", "I consistently preferred the intense focus of solitary study sessions over the chaotic dynamics of collaborative group projects. When entirely isolated from the inevitable social distractions of my peers, my capacity for deep, uninterrupted conceptual analysis peaked remarkably. Group work frequently devolved into unproductive socializing rather than rigorous academic endeavor."),
    ("How important are good teachers for a student's success?", "The profound influence of an exceptionally dedicated, inspiring teacher cannot be overstated regarding a student's ultimate academic trajectory. A truly brilliant educator possesses the unique ability to ignite genuine intellectual curiosity, transforming an inherently tedious subject into a fascinating exploration. Conversely, a deeply unenthusiastic instructor can permanently extinguish a child's natural passion."),
    ("Do you plan to pursue further education in the future?", "I definitely harbor a strong, lingering ambition to eventually pursue a specialized postgraduate degree, likely a Master's in Business Administration. Given the incredibly competitive nature of the contemporary corporate landscape, continuously upgrading my professional qualifications seems absolutely essential. This advanced credential would theoretically unlock significantly more lucrative management opportunities."),
    ("How has the internet changed the way students learn?", "The unprecedented proliferation of the internet has fundamentally revolutionized traditional pedagogy by democratizing instantaneous access to global information. Students are no longer strictly confined to the limited perspectives of their local textbooks; they can instantly cross-reference diverse international research. This astonishing accessibility has exponentially accelerated the overall pace of independent learning."),
    ("What is the most difficult language to learn, in your opinion?", "From my limited perspective, I suspect that mastering an intricate tonal language like Mandarin presents the most formidable linguistic challenge. Because the exact identical syllable conveys entirely different meanings depending solely on the subtle vocal inflection, achieving genuine fluency requires absolute precision. The complex character-based writing system further exacerbates the difficulty."),
    ("Do you think physical books will eventually be replaced by digital tablets in schools?", "While digital tablets undeniably offer remarkable convenience and incredible multimedia interactivity, I highly doubt they will entirely eradicate traditional physical textbooks. The tactile sensation of physically highlighting text and the complete absence of distracting electronic notifications make printed books uniquely valuable for deep concentration. They will likely coexist symbiotically moving forward."),
    ("What skills are most important for young people entering the workforce today?", "Navigating the rapidly fluctuating modern economy absolutely demands that young professionals prioritize cultivating intense psychological adaptability. Because rapid technological innovations frequently render specific technical knowledge entirely obsolete, the underlying capacity to continuously learn and rapidly pivot is paramount. Emotional intelligence and robust interpersonal communication remain equally indispensable for long-term career success.")
]
for q, t in c2_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v8_g8_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 8, "grammar": 8, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR8] Wide range of sophisticated vocabulary ('meticulously dissecting', 'psychological pressure', 'unprecedented proliferation'). Meaning is precise and flexible.",
        "grammar_reason": "[GRA8] Wide range of structures used flexibly and accurately ('While mastering abstract mathematical theorems is...', 'When entirely isolated from'). The majority of sentences are error-free.",
        "micro_flaws": ["none significant"],
        "grammar_profile": {"complexity": "very_high", "accuracy": "high", "flexibility": "very_high"},
        "output": "## Vocabulary (Lexical Resource): Band 8\n\n**Reasoning:** [LR8] Wide vocabulary range used readily and flexibly to convey precise meaning.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 8\n\n**Reasoning:** [GRA8] Wide range of structures used flexibly and accurately. The majority of sentences are error-free."
    })
    start_id += 1

# V9 / G9 (Society and Culture)
c3_t = [
    ("How does urbanization affect traditional community structures?", "The relentless trajectory of urbanization frequently exerts a profoundly fragmenting effect on established, traditional community structures. As individuals migrate toward anonymous metropolitan centers, the deep, multi-generational interdependencies characteristic of rural life are frequently severed. Consequently, we witness the tragic erosion of organic social cohesion, replaced by a pervasive sense of profound civic alienation."),
    ("What is the significance of preserving local dialects?", "Meticulously preserving obscure local dialects is absolutely paramount because a language encapsulates the unique cognitive framework and complex mythology of its native speakers. When a dialect is permitted to vanish into total obsolescence, humanity suffers an irrecoverable loss of localized ecological wisdom and philosophical perspective. It constitutes a devastating intellectual tragedy."),
    ("How has globalization impacted the culinary traditions of your country?", "While globalization undeniably introduces an exciting influx of exotic flavors, it simultaneously threatens the absolute integrity of our indigenous culinary traditions. As ubiquitous international fast-food conglomerates aggressively saturate the market, complex, labor-intensive ancestral recipes are rapidly being abandoned by the younger demographic. This insidious homogenization represents an incalculable cultural impoverishment."),
    ("Do you believe that art should necessarily serve a social purpose?", "I firmly maintain that while art undeniably possesses the profound capacity to articulate powerful social critique, mandating a utilitarian purpose fundamentally corrupts the creative impulse. True artistic expression must remain entirely unencumbered by rigid ideological agendas to genuinely explore the chaotic depths of the human condition. Didactic art frequently devolves into mere propaganda."),
    ("How does the design of a city influence its residents' behavior?", "The overarching architectural philosophy dictating an urban environment exerts an undeniably profound, subconscious influence on the aggregate behavior of the populace. Monolithic, brutalist concrete structures inevitably foster a highly oppressive atmosphere of pervasive anxiety and social withdrawal. Conversely, strategically integrating biophilic design elements naturally engenders a deeply reassuring sense of communal tranquility."),
    ("What role do public libraries play in modern society?", "Despite the instantaneous availability of infinite digital data, physical public libraries remain profoundly indispensable as egalitarian bastions of intellectual accessibility. They provide crucial, unhindered access to sophisticated educational resources for marginalized demographics who cannot afford expensive technology. Furthermore, their tranquil atmosphere offers a necessary sanctuary for focused, rigorous academic contemplation."),
    ("How is the concept of privacy evolving in the digital age?", "The fundamental concept of personal privacy has undergone a radical, alarming devolution in our current era of ubiquitous digital surveillance. We have ostensibly traded our most intimate, confidential data for the superficial convenience of incredibly invasive social networking platforms. This constant, voluntary self-exposure has completely normalized a culture of unabashed corporate voyeurism."),
    ("Do you think historical monuments should be restored or left as ruins?", "Navigating the restoration of ancient monuments involves an incredibly complex ethical calculus. While complete reconstruction risks crossing into blatant historical forgery, leaving structures as rapidly deteriorating ruins guarantees their eventual total erasure. The most prudent approach involves meticulous, transparent stabilization—arresting further decay while ensuring modern interventions remain visually distinct from the original fabric."),
    ("How does international travel broaden an individual's worldview?", "Prolonged, authentic immersion in fundamentally foreign cultural paradigms is undeniably the most potent catalyst for developing profound human empathy. By directly navigating the bewildering nuances of an unfamiliar society, one is inherently forced to ruthlessly dismantle their own deeply ingrained, ethnocentric biases. This challenging intellectual friction ultimately yields a far more tolerant, cosmopolitan perspective."),
    ("What defines a successful society, in your opinion?", "In my philosophical estimation, a truly successful society is not defined solely by the relentless accumulation of transient macroeconomic wealth, but rather by its unwavering commitment to equitable social justice. A civilization that fiercely protects its most vulnerable, marginalized demographics while actively fostering robust intellectual freedom has achieved genuine, enduring greatness."),
    ("Do you feel that traditional music is losing its relevance?", "Although it currently lacks the massive commercial appeal of highly synthesized pop, traditional folk music remains viscerally relevant as the enduring auditory archive of our national history. The haunting melodies chronically the profound struggles and triumphs of our ancestors. Whenever performed authentically, it evokes an incredibly powerful, almost genetic sense of identity."),
    ("How do social media influencers impact consumer behavior?", "The unprecedented rise of sophisticated social media influencers has fundamentally disrupted traditional marketing, essentially weaponizing parasocial relationships to drive immense consumer spending. By carefully cultivating an aura of intimate authenticity, these individuals can seamlessly integrate lucrative corporate endorsements into their personal narratives. Their followers, mistaking this calculated marketing for genuine advice, blindly mimic their purchases."),
    ("Why is it important to support independent local businesses?", "Vigorously supporting independent, locally-owned businesses is absolutely crucial for preventing the complete, sterile homogenization of our commercial landscapes. These unique enterprises frequently source their materials regionally, injecting vital capital directly back into the immediate community. When we patronize them, we actively rebel against the predatory, monopolistic practices of massive multinational retail conglomerates.")
]
for q, t in c3_t:
    wc = len(t.split())
    samples.append({
        "sample_id": f"syn_p1_v9_g9_{start_id:04d}", "video_id": "synthetic", "part": 1, "question": q,
        "transcript_cleaned": t, "word_count": wc, "response_type": "direct_answer" if wc <= 50 else "extended",
        "vocabulary": 9, "grammar": 9, "is_valid": True, "dataset_source": "synthetic", "idiom_present": False, "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": f"Part: 1\nQuestion: {q}\n\nTranscript: {t}\n\nWord Count: {wc} words\nResponse Type: {'direct_answer' if wc <= 50 else 'extended'}",
        "vocab_reason": "[LR9] Exceptional, highly precise, and sophisticated vocabulary ('obsolescence', 'utilitarian purpose', 'parasocial relationships'). Idiomatic language is natural and accurate.",
        "grammar_reason": "[GRA9] Flawless grammar with full flexibility. Uses advanced structures naturally and accurately.",
        "micro_flaws": ["none in grammar", "none in vocabulary"],
        "grammar_profile": {"complexity": "very_high", "accuracy": "near_perfect", "flexibility": "very_high"},
        "output": "## Vocabulary (Lexical Resource): Band 9\n\n**Reasoning:** [LR9] Uses vocabulary with full flexibility and precision in all topics.\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 9\n\n**Reasoning:** [GRA9] Full mastery of complex structures. Flawless accuracy and natural flexibility."
    })
    start_id += 1

with open(filename, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')
print(f"Batch {batch_num} written natively.")
