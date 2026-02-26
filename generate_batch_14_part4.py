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

# --- BATCH 14 PART 4: SAMPLES 1285-1325 (41 Total) ---
# Combo: V9/G5 (Expert Vocab, Basic Grammar)
# Strategy: Use Band 9 vocabulary (idiomatic, precise, sophisticated) but make frequent Band 5 grammar errors (basic errors, limited range).

topics_14_4 = [
    {
        "question": "Is sleep important?",
        "transcript": "Sleep is the bedrock of our physiological well-being. It rejuvenates the mind and body. However, chronic deprivation is rampant in modern society. We treats sleep as a luxury, not a necessity. This mindset are detrimental to our health. We must prioritizes our circadian rhythms. Only then can we functions optimally.",
        "micro_flaws": ["Subject-verb agreement error: 'We treats'", "Subject-verb agreement error: 'mindset are'", "Verb form error: 'must prioritizes'", "Verb form error: 'can we functions'"],
        "vocab_reason": "[LR9] Vocab: 'bedrock', 'physiological well-being', 'rejuvenates', 'chronic deprivation', 'rampant', 'luxury', 'detrimental', 'circadian rhythms'. >Band 8: Sophisticated.",
        "grammar_reason": "[GRA5] Errors: 'treats', 'are', 'prioritizes', 'functions'. >Band 4: Clear but flawed."
    },
    {
        "question": "Why travel?",
        "transcript": "Travel broadens the horizons and fosters cultural empathy. It allow us to escape the mundane. Immersing oneself in a foreign culture is transformative. However, tourism can leads to commodification. Authentic experiences is becoming rare. We should seeks to be travelers, not tourists.",
        "micro_flaws": ["Subject-verb agreement error: 'It allow'", "Verb form error: 'can leads'", "Subject-verb agreement error: 'experiences is'", "Verb form error: 'should seeks'"],
        "vocab_reason": "[LR9] Vocab: 'broadens the horizons', 'fosters', 'cultural empathy', 'mundane', 'transformative', 'commodification', 'authentic'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'allow', 'leads', 'is', 'seeks'. >Band 4: Frequent errors."
    },
    {
        "question": "Is inequality bad?",
        "transcript": "The chasm between the haves and have-nots is widening. Systemic inequity permeates every stratum of society. Meritocracy is largely a myth. Privilege bestow unfair advantages. We must dismantles these barriers. Egalitarianism should be our guiding principle. A fractured society cannot thrives.",
        "micro_flaws": ["Subject-verb agreement error: 'Privilege bestow'", "Verb form error: 'must dismantles'", "Verb form error: 'cannot thrives'"],
        "vocab_reason": "[LR9] Vocab: 'chasm', 'haves and have-nots', 'systemic inequity', 'permeates', 'stratum', 'meritocracy', 'egalitarianism'. >Band 8: Highly advanced.",
        "grammar_reason": "[GRA5] Errors: 'bestow', 'dismantles', 'thrives'. >Band 4: Clear meaning."
    },
    {
        "question": "Why read fiction?",
        "transcript": "Fiction serves as a vehicle for empathy. It enables us to inhabit the consciousness of others. Narrative complexity stimulate cognitive faculties. In a utilitarian world, art is undervalued. We needs stories to make sense of chaos. Literature illuminate the human condition.",
        "micro_flaws": ["Subject-verb agreement error: 'complexity stimulate'", "Subject-verb agreement error: 'We needs'", "Subject-verb agreement error: 'Literature illuminate'"],
        "vocab_reason": "[LR9] Vocab: 'vehicle for empathy', 'inhabit', 'consciousness', 'utilitarian', 'undervalued', 'illuminate', 'human condition'. >Band 8: Precise.",
        "grammar_reason": "[GRA5] Errors: 'stimulate', 'needs', 'illuminate'. >Band 4: Good vocab, bad grammar."
    },
    {
        "question": "Is plastic bad?",
        "transcript": "The ubiquity of plastic is an environmental scourge. It chokes our oceans and permeates the food chain. We has become addicted to convenience. Breaking this dependency require radical action. Biodegradable polymers offers a glimmer of hope. But legislative intervention are crucial.",
        "micro_flaws": ["Subject-verb agreement error: 'We has'", "Subject-verb agreement error: 'dependency require'", "Subject-verb agreement error: 'polymers offers'", "Subject-verb agreement error: 'intervention are'"],
        "vocab_reason": "[LR9] Vocab: 'ubiquity', 'scourge', 'permeates', 'dependency', 'radical action', 'biodegradable polymers', 'glimmer of hope'. >Band 8: Sophisticated.",
        "grammar_reason": "[GRA5] Errors: 'has', 'require', 'offers', 'are'. >Band 4: Frequent errors."
    },
    {
        "question": "Is change good?",
        "transcript": "Change is the only constant in the universe. Stagnation leads to atrophy. Embracing flux allow for growth. However, humans is creatures of habit. We resists the unknown. Adaptability is a prerequisite for survival. Those who evolves thrives.",
        "micro_flaws": ["Subject-verb agreement error: 'flux allow'", "Subject-verb agreement error: 'humans is'", "Subject-verb agreement error: 'We resists'", "Subject-verb agreement error: 'evolves thrives'"],
        "vocab_reason": "[LR9] Vocab: 'stagnation', 'atrophy', 'flux', 'creatures of habit', 'prerequisite'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'allow', 'is', 'resists', 'evolves'. >Band 4: Clear."
    },
    {
        "question": "Why work?",
        "transcript": "Work provides a sense of agency and purpose. It anchors us in reality. However, the gig economy has erode job security. Precarity is the new normal. We must reimagines the social contract. Universal basic income might be a panacea.",
        "micro_flaws": ["Verb form error: 'has erode'", "Verb form error: 'must reimagines'"],
        "vocab_reason": "[LR9] Vocab: 'agency', 'anchors', 'gig economy', 'precarity', 'social contract', 'panacea'. >Band 8: Advanced.",
        "grammar_reason": "[GRA5] Errors: 'erode', 'reimagines'. >Band 4: Errors persist."
    },
    {
        "question": "Is honesty best?",
        "transcript": "Veracity is the cornerstone of trust. Deceit corrodes relationships. While white lies is sometimes expedient, integrity is paramount. Radical honesty can be cathartic. We should values truth above all. A transparent life is a liberated one.",
        "micro_flaws": ["Subject-verb agreement error: 'lies is'", "Subject-verb agreement error: 'We should values'"],
        "vocab_reason": "[LR9] Vocab: 'veracity', 'cornerstone', 'corrodes', 'expedient', 'integrity', 'cathartic', 'liberated'. >Band 8: Precise.",
        "grammar_reason": "[GRA5] Errors: 'is' (plural), 'values'. >Band 4: Good range."
    },
    {
        "question": "Why explore space?",
        "transcript": "The cosmos beckons us with its infinite mysteries. Exploration is encoded in our DNA. Venturing into the void inspire awe. It puts our terrestrial squabbles into perspective. We must becomes a multi-planetary species. The survival of humanity depend on it.",
        "micro_flaws": ["Subject-verb agreement error: 'void inspire'", "Verb form error: 'must becomes'", "Subject-verb agreement error: 'humanity depend'"],
        "vocab_reason": "[LR9] Vocab: 'cosmos', 'beckons', 'encoded', 'terrestrial squabbles', 'perspective', 'multi-planetary'. >Band 8: Sophisticated.",
        "grammar_reason": "[GRA5] Errors: 'inspire', 'becomes', 'depend'. >Band 4: Frequent errors."
    },
    {
        "question": "Is music vital?",
        "transcript": "Music is a universal language that transcends barriers. It resonates with the deepest chords of our being. A melody can evokes memories long forgotten. It is a conduit for emotion. Society need this catharsis. Without music, life would be a mistake.",
        "micro_flaws": ["Verb form error: 'can evokes'", "Subject-verb agreement error: 'Society need'"],
        "vocab_reason": "[LR9] Vocab: 'transcends', 'resonates', 'chords of our being', 'conduit', 'catharsis'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'evokes', 'need'. >Band 4: Clear."
    },
    {
        "question": "Why learn history?",
        "transcript": "History is a repository of human wisdom. Ignorance of the past condemns us to repeat it. Historical literacy provide context for the present. We must scrutinizes the narratives we are told. Revisionism is a double-edged sword. Truth is often elusive.",
        "micro_flaws": ["Subject-verb agreement error: 'literacy provide'", "Verb form error: 'must scrutinizes'"],
        "vocab_reason": "[LR9] Vocab: 'repository', 'condemns', 'historical literacy', 'scrutinizes', 'revisionism', 'double-edged sword'. >Band 8: Advanced.",
        "grammar_reason": "[GRA5] Errors: 'provide', 'scrutinizes'. >Band 4: Good."
    },
    {
        "question": "Is competition good?",
        "transcript": "Competition drives innovation and excellence. It forces us to transcends our limits. However, hyper-competitiveness can be toxic. It breed animosity. Collaboration is often more fruitful. We should strikes a balance. Healthy rivalry is beneficial.",
        "micro_flaws": ["Verb form error: 'to transcends'", "Subject-verb agreement error: 'It breed'", "Verb form error: 'should strikes'"],
        "vocab_reason": "[LR9] Vocab: 'innovation', 'transcends', 'hyper-competitiveness', 'animosity', 'fruitful', 'rivalry'. >Band 8: Precise.",
        "grammar_reason": "[GRA5] Errors: 'transcends', 'breed', 'strikes'. >Band 4: Errors."
    },
    {
        "question": "Is silence golden?",
        "transcript": "In a cacophonous world, silence is a sanctuary. It allows for introspection and clarity. Constant noise bombard our senses. We has lost the ability to be still. Solitude is essential for mental hygiene. We must reclaims the quiet.",
        "micro_flaws": ["Subject-verb agreement error: 'noise bombard'", "Subject-verb agreement error: 'We has'", "Verb form error: 'must reclaims'"],
        "vocab_reason": "[LR9] Vocab: 'cacophonous', 'sanctuary', 'introspection', 'bombard', 'solitude', 'mental hygiene'. >Band 8: High level.",
        "grammar_reason": "[GRA5] Errors: 'bombard', 'has', 'reclaims'. >Band 4: Clear."
    },
    {
        "question": "Is anger bad?",
        "transcript": "Anger is a potent emotion that can spur action. Righteous indignation has fueled many revolutions. However, uncontrolled rage is destructive. It cloud judgment. We must learns to channel it constructively. Emotional intelligence is key.",
        "micro_flaws": ["Subject-verb agreement error: 'It cloud'", "Verb form error: 'must learns'"],
        "vocab_reason": "[LR9] Vocab: 'potent', 'righteous indignation', 'fueled', 'destructive', 'cloud judgment', 'constructively'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'cloud', 'learns'. >Band 4: Good."
    },
    {
        "question": "Is patience a virtue?",
        "transcript": "Patience is an antidote to our instant-gratification culture. It cultivates resilience. Waiting is often perceived as passive. But it is an active state of endurance. Impatience leads to rash decisions. We needs to slow down.",
        "micro_flaws": ["Subject-verb agreement error: 'We needs'"],
        "vocab_reason": "[LR9] Vocab: 'antidote', 'instant-gratification', 'cultivates', 'resilience', 'perceived', 'endurance'. >Band 8: Sophisticated.",
        "grammar_reason": "[GRA5] Errors: 'needs'. >Band 4: Clear."
    },
    {
        "question": "Why forgive?",
        "transcript": "Forgiveness is a liberation from the past. Holding grudges is toxic to the soul. It is an act of self-love, not weakness. Vindictiveness poison the mind. We must releases the burden of resentment. Peace is the ultimate goal.",
        "micro_flaws": ["Subject-verb agreement error: 'Vindictiveness poison'", "Verb form error: 'must releases'"],
        "vocab_reason": "[LR9] Vocab: 'liberation', 'grudges', 'vindictiveness', 'resentment', 'ultimate goal'. >Band 8: Precise.",
        "grammar_reason": "[GRA5] Errors: 'poison', 'releases'. >Band 4: Good."
    },
    {
        "question": "Is curiosity good?",
        "transcript": "Curiosity is the engine of discovery. It propels us into the unknown. An inquisitive mind is never bored. However, curiosity can killed the cat. We must balances it with caution. The thirst for knowledge is insatiable.",
        "micro_flaws": ["Verb form error: 'can killed'", "Verb form error: 'must balances'"],
        "vocab_reason": "[LR9] Vocab: 'engine of discovery', 'propels', 'inquisitive', 'insatiable', 'thirst for knowledge'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'killed', 'balances'. >Band 4: Clear."
    },
    {
        "question": "Is loyalty important?",
        "transcript": "Loyalty is the glue that binds relationships. It fosters a sense of security. Betrayal is a devastating blow. However, blind loyalty can be dangerous. It prevent critical thinking. We should questions our allegiances.",
        "micro_flaws": ["Subject-verb agreement error: 'It prevent'", "Verb form error: 'should questions'"],
        "vocab_reason": "[LR9] Vocab: 'glue', 'binds', 'devastating blow', 'blind loyalty', 'allegiances'. >Band 8: Precise.",
        "grammar_reason": "[GRA5] Errors: 'prevent', 'questions'. >Band 4: Good."
    },
    {
        "question": "Why dream?",
        "transcript": "Dreams are the blueprints of reality. They inspire us to strive for greatness. A visionary is someone who sees potential where others sees chaos. We must chases our aspirations. Without dreams, life is stagnant.",
        "micro_flaws": ["Subject-verb agreement error: 'others sees'", "Verb form error: 'must chases'"],
        "vocab_reason": "[LR9] Vocab: 'blueprints', 'strive', 'visionary', 'potential', 'stagnant', 'aspirations'. >Band 8: Advanced.",
        "grammar_reason": "[GRA5] Errors: 'sees', 'chases'. >Band 4: Clear."
    },
    {
        "question": "Is discipline key?",
        "transcript": "Discipline is the bridge between goals and accomplishment. Motivation is fleeting, but discipline is consistent. It requires self-mastery. We must adheres to a routine. Procrastination is the thief of time. Success require grit.",
        "micro_flaws": ["Verb form error: 'must adheres'", "Subject-verb agreement error: 'Success require'"],
        "vocab_reason": "[LR9] Vocab: 'bridge', 'fleeting', 'self-mastery', 'routine', 'procrastination', 'thief of time', 'grit'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'adheres', 'require'. >Band 4: Good."
    },
    {
        "question": "Is fear useful?",
        "transcript": "Fear is a primal mechanism for survival. It alerts us to danger. However, irrational fear is debilitating. It paralyze us. We must confronts our phobias. Courage is not the absence of fear, but triumph over it.",
        "micro_flaws": ["Subject-verb agreement error: 'It paralyze'", "Verb form error: 'must confronts'"],
        "vocab_reason": "[LR9] Vocab: 'primal mechanism', 'irrational', 'debilitating', 'phobias', 'triumph'. >Band 8: Precise.",
        "grammar_reason": "[GRA5] Errors: 'paralyze', 'confronts'. >Band 4: Clear."
    },
    {
        "question": "Why regret?",
        "transcript": "Regret is a painful teacher. It highlights our mistakes. Dwelling on the past is futile. We must learns from our missteps. Redemption is always possible. We should looks forward, not back.",
        "micro_flaws": ["Verb form error: 'must learns'", "Verb form error: 'should looks'"],
        "vocab_reason": "[LR9] Vocab: 'painful teacher', 'dwelling', 'futile', 'missteps', 'redemption'. >Band 8: Sophisticated.",
        "grammar_reason": "[GRA5] Errors: 'learns', 'looks'. >Band 4: Good."
    },
    {
        "question": "Is time money?",
        "transcript": "Time is the most finite resource we possess. Squandering it is a tragedy. Efficiency is prized in our society. However, we must not becomes slaves to the clock. Leisure is valuable. We needs to savor the moment.",
        "micro_flaws": ["Verb form error: 'must not becomes'", "Subject-verb agreement error: 'We needs'"],
        "vocab_reason": "[LR9] Vocab: 'finite resource', 'squandering', 'tragedy', 'efficiency', 'slaves to the clock', 'savor'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'becomes', 'needs'. >Band 4: Clear."
    },
    {
        "question": "Is love enough?",
        "transcript": "Love is a potent force, but it is not a panacea. Relationships requires work and compromise. Compatibility is essential. Passion fade over time. We must nurtures the bond. Respect is the foundation of love.",
        "micro_flaws": ["Subject-verb agreement error: 'Relationships requires'", "Subject-verb agreement error: 'Passion fade'", "Verb form error: 'must nurtures'"],
        "vocab_reason": "[LR9] Vocab: 'potent force', 'panacea', 'compromise', 'compatibility', 'nurtures', 'bond'. >Band 8: Precise.",
        "grammar_reason": "[GRA5] Errors: 'requires', 'fade', 'nurtures'. >Band 4: Good."
    },
    {
        "question": "Why be kind?",
        "transcript": "Kindness is a ripple effect. One act of benevolence can changes a life. It costs nothing but means everything. In a cruel world, kindness is an act of rebellion. We should spreads positivity. Empathy is contagious.",
        "micro_flaws": ["Verb form error: 'can changes'", "Verb form error: 'should spreads'"],
        "vocab_reason": "[LR9] Vocab: 'ripple effect', 'benevolence', 'rebellion', 'positivity', 'contagious'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'changes', 'spreads'. >Band 4: Clear."
    },
    {
        "question": "Is beauty truth?",
        "transcript": "Beauty is subjective. It lies in the eye of the beholder. Aesthetics can be misleading. Truth is often stark and unvarnished. We creates illusions to cope. We must seeks substance over style. Inner beauty is eternal.",
        "micro_flaws": ["Subject-verb agreement error: 'We creates'", "Verb form error: 'must seeks'"],
        "vocab_reason": "[LR9] Vocab: 'subjective', 'beholder', 'aesthetics', 'stark', 'unvarnished', 'substance over style'. >Band 8: Sophisticated.",
        "grammar_reason": "[GRA5] Errors: 'creates', 'seeks'. >Band 4: Good."
    },
    {
        "question": "Is happiness a choice?",
        "transcript": "Happiness is a state of mind, not a destination. External circumstances influences us, but we chooses our reaction. Gratitude is the key. We must focuses on the positive. Misery is optional. Joy is a practice.",
        "micro_flaws": ["Subject-verb agreement error: 'circumstances influences'", "Subject-verb agreement error: 'we chooses'", "Verb form error: 'must focuses'"],
        "vocab_reason": "[LR9] Vocab: 'state of mind', 'destination', 'external circumstances', 'gratitude', 'optional', 'practice'. >Band 8: Precise.",
        "grammar_reason": "[GRA5] Errors: 'influences', 'chooses', 'focuses'. >Band 4: Clear."
    },
    {
        "question": "Why write?",
        "transcript": "Writing is thinking on paper. It clarifies our thoughts. Words has power. They can inspires or destroy. We writes to leave a legacy. It is a form of immortality. The pen is mightier than the sword.",
        "micro_flaws": ["Subject-verb agreement error: 'Words has'", "Verb form error: 'can inspires'", "Subject-verb agreement error: 'We writes'"],
        "vocab_reason": "[LR9] Vocab: 'clarifies', 'legacy', 'immortality', 'mightier than the sword'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'has', 'inspires', 'writes'. >Band 4: Good."
    },
    {
        "question": "Is wisdom age?",
        "transcript": "Wisdom is accrued through experience, not just years. A young person can be wise beyond their years. Senility does not guarantee insight. We learns from our scars. Reflection is the catalyst for wisdom. It is a precious commodity.",
        "micro_flaws": ["Subject-verb agreement error: 'We learns'"],
        "vocab_reason": "[LR9] Vocab: 'accrued', 'wise beyond their years', 'senility', 'guarantee', 'catalyst', 'commodity'. >Band 8: Advanced.",
        "grammar_reason": "[GRA5] Errors: 'learns'. >Band 4: Clear."
    },
    {
        "question": "Why hope?",
        "transcript": "Hope is the light in the darkness. It keeps us going when all seems lost. Despair is a trap. We must holds onto hope. Optimism is a force multiplier. It shape our reality. Believe in the impossible.",
        "micro_flaws": ["Verb form error: 'must holds'", "Subject-verb agreement error: 'It shape'"],
        "vocab_reason": "[LR9] Vocab: 'light in the darkness', 'despair', 'trap', 'force multiplier', 'reality', 'impossible'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'holds', 'shape'. >Band 4: Good."
    },
    {
        "question": "Is freedom free?",
        "transcript": "Freedom comes at a cost. Vigilance is the price of liberty. We often takes it for granted. Oppression is always lurking. We must defends our rights. Autonomy is precious. It is worth fighting for.",
        "micro_flaws": ["Subject-verb agreement error: 'We often takes'", "Verb form error: 'must defends'"],
        "vocab_reason": "[LR9] Vocab: 'vigilance', 'liberty', 'granted', 'oppression', 'lurking', 'autonomy'. >Band 8: Sophisticated.",
        "grammar_reason": "[GRA5] Errors: 'takes', 'defends'. >Band 4: Clear."
    },
    {
        "question": "Why laugh?",
        "transcript": "Laughter is the best medicine. It relieves stress and bonds us. A sense of humor is a survival mechanism. It diffuses tension. We should laughs more often. Life is too short to be serious. Joy is essential.",
        "micro_flaws": ["Verb form error: 'should laughs'"],
        "vocab_reason": "[LR9] Vocab: 'best medicine', 'relieves', 'bonds', 'survival mechanism', 'diffuses', 'essential'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'laughs'. >Band 4: Good."
    },
    {
        "question": "Is peace possible?",
        "transcript": "Peace is an elusive ideal. Conflict seems intrinsic to human nature. However, diplomacy can yields results. Understanding is the bridge. We must strives for harmony. War is a failure of imagination. Peace begins within.",
        "micro_flaws": ["Verb form error: 'can yields'", "Verb form error: 'must strives'"],
        "vocab_reason": "[LR9] Vocab: 'elusive ideal', 'intrinsic', 'diplomacy', 'bridge', 'harmony', 'failure of imagination'. >Band 8: Advanced.",
        "grammar_reason": "[GRA5] Errors: 'yields', 'strives'. >Band 4: Clear."
    },
    {
        "question": "Why exist?",
        "transcript": "Existence is a mystery. We seeks meaning in a chaotic universe. Purpose is self-created. We are the architects of our destiny. Nihilism is a void. We must embraces life. To be is a miracle.",
        "micro_flaws": ["Subject-verb agreement error: 'We seeks'", "Verb form error: 'must embraces'"],
        "vocab_reason": "[LR9] Vocab: 'mystery', 'chaotic universe', 'architects', 'destiny', 'nihilism', 'void'. >Band 8: Philosophical.",
        "grammar_reason": "[GRA5] Errors: 'seeks', 'embraces'. >Band 4: Good."
    },
    {
        "question": "Is fate real?",
        "transcript": "Fate is a comforting narrative. It absolves us of responsibility. However, free will is empowering. We shapes our own path. Determinism is limiting. We must seized the day. The future is unwritten.",
        "micro_flaws": ["Subject-verb agreement error: 'We shapes'", "Verb form error: 'must seized'"],
        "vocab_reason": "[LR9] Vocab: 'comforting narrative', 'absolves', 'empowering', 'determinism', 'limiting', 'unwritten'. >Band 8: Sophisticated.",
        "grammar_reason": "[GRA5] Errors: 'shapes', 'seized'. >Band 4: Clear."
    },
    {
        "question": "Why create?",
        "transcript": "Creativity is the spark of divinity. It brings something new into existence. Innovation drives progress. We are born makers. We must nurtures our talents. Artistry is a gift. The world needs creators.",
        "micro_flaws": ["Verb form error: 'must nurtures'"],
        "vocab_reason": "[LR9] Vocab: 'spark of divinity', 'existence', 'innovation', 'makers', 'artistry'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'nurtures'. >Band 4: Good."
    },
    {
        "question": "Is nature conscious?",
        "transcript": "The interconnectedness of nature suggests a hive mind. Trees communicates via fungal networks. The earth is a living organism. Gaia theory is compelling. We must respects the web of life. We are not separate from it.",
        "micro_flaws": ["Subject-verb agreement error: 'Trees communicates'", "Verb form error: 'must respects'"],
        "vocab_reason": "[LR9] Vocab: 'interconnectedness', 'hive mind', 'fungal networks', 'living organism', 'Gaia theory'. >Band 8: Scientific/Advanced.",
        "grammar_reason": "[GRA5] Errors: 'communicates', 'respects'. >Band 4: Clear."
    },
    {
        "question": "Is tech good?",
        "transcript": "Technology is a double-edged sword. It connects and divides us. We are drowning in information but starving for wisdom. The digital realm is seductive. We must unplugs occasionally. Human connection is irreplaceable.",
        "micro_flaws": ["Verb form error: 'must unplugs'"],
        "vocab_reason": "[LR9] Vocab: 'double-edged sword', 'drowning', 'starving', 'seductive', 'irreplaceable'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'unplugs'. >Band 4: Good."
    },
    {
        "question": "Why vote?",
        "transcript": "Voting is a civic duty. It is the voice of the people. Apathy leads to tyranny. We must participates in democracy. Every vote counts. It is a privilege that we must not squanders.",
        "micro_flaws": ["Verb form error: 'must participates'", "Verb form error: 'must not squanders'"],
        "vocab_reason": "[LR9] Vocab: 'civic duty', 'apathy', 'tyranny', 'democracy', 'privilege', 'squanders'. >Band 8: Advanced.",
        "grammar_reason": "[GRA5] Errors: 'participates', 'squanders'. >Band 4: Clear."
    },
    {
        "question": "Is life fair?",
        "transcript": "Life is inherently unfair. Merit is not always rewarded. Fortune is capricious. However, we must plays the hand we are dealt. Resilience is our best defense. Bitterness is a poison. We must keeps going.",
        "micro_flaws": ["Verb form error: 'must plays'", "Verb form error: 'must keeps'"],
        "vocab_reason": "[LR9] Vocab: 'inherently unfair', 'merit', 'capricious', 'resilience', 'defense', 'bitterness'. >Band 8: Sophisticated.",
        "grammar_reason": "[GRA5] Errors: 'plays', 'keeps'. >Band 4: Good."
    },
    {
        "question": "Why art?",
        "transcript": "Art is the soul of a culture. It reflects our deepest fears and desires. It is a mirror held up to nature. We needs art to understand ourselves. It transcends language. It is eternal.",
        "micro_flaws": ["Subject-verb agreement error: 'We needs'"],
        "vocab_reason": "[LR9] Vocab: 'soul', 'deepest fears', 'mirror held up to nature', 'transcends', 'eternal'. >Band 8: Idiomatic.",
        "grammar_reason": "[GRA5] Errors: 'needs'. >Band 4: Clear."
    }
]

# Total 41 samples

start_index = 1285
for i, item in enumerate(topics_14_4):
    samples.append(create_sample(
        index=start_index + i,
        vocab_band=9,
        grammar_band=5,
        question=item["question"],
        transcript=item["transcript"],
        response_type="extended",
        micro_flaws=item["micro_flaws"],
        grammar_profile={"complexity": "low", "accuracy": "low", "flexibility": "low"},
        vocab_reason=item["vocab_reason"],
        grammar_reason=item["grammar_reason"],
        idiom_present=False,
        risk_level="medium"
    ))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
