import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch06.jsonl")

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

# --- BATCH 06 PART 2: SAMPLES 476-500 (25 Total) ---
# Combo: V7/G7

# Sample 476: V7/G7 - Topic: Health (Mental)
samples.append(create_sample(
    index=476,
    vocab_band=7,
    grammar_band=7,
    question="Why is mental health awareness increasing?",
    transcript="People are becoming more open about their struggles. High-profile celebrities sharing their stories has reduced the stigma. It has encouraged others to seek help. Also, the pressures of modern life, like social media and economic instability, have made mental health issues more visible. We now understand that mental well-being is as important as physical health.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'struggles', 'high-profile', 'stigma', 'encouraged', 'instability', 'visible', 'well-being'. >Band 6: Precise vocabulary. Not Band 8: Lacks idiomatic expressions.",
    grammar_reason="[GRA7] Gerund phrase: 'High-profile celebrities sharing their stories'. Comparison: 'as important as'. >Band 6: Frequent error-free sentences. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 477: V7/G7 - Topic: Environment (Recycling)
samples.append(create_sample(
    index=477,
    vocab_band=7,
    grammar_band=7,
    question="Is recycling the best way to help the environment?",
    transcript="It is helpful, but not the best way. Reducing consumption is far more effective. If we buy less, we create less waste. Recycling consumes energy and resources itself. It should be the last resort, not the first solution. We need to shift our focus to sustainability and durability, rather than just processing trash.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'consumption', 'effective', 'consumes', 'last resort', 'sustainability', 'durability', 'processing'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA7] Contrast: 'but not the best way'. Conditionals: 'If we buy less...'. >Band 6: Accurate grammar. Not Band 8: Sentences are somewhat standard.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 478: V7/G7 - Topic: Society (Media)
samples.append(create_sample(
    index=478,
    vocab_band=7,
    grammar_band=7,
    question="How does advertising influence children?",
    transcript="It targets them aggressively. Marketers know that children have 'pester power' over their parents. They use bright colors and catchy tunes to create desire. This can lead to materialism at a young age. Children might judge their self-worth by what they own. It is manipulative and potentially harmful. Regulations should be stricter to protect young minds.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'targets', 'aggressively', 'pester power', 'materialism', 'self-worth', 'manipulative', 'regulations'. >Band 6: Sophisticated terms. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA7] Reason: 'Marketers know that...'. Passive implied: 'should be stricter'. >Band 6: Good control. Not Band 8: Limited complexity.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 479: V7/G7 - Topic: Culture (Global)
samples.append(create_sample(
    index=479,
    vocab_band=7,
    grammar_band=7,
    question="Is it possible to have a global culture?",
    transcript="We are moving towards it, but distinct cultures still exist. The internet and travel have created a shared global consciousness. We watch the same movies and face similar challenges, like climate change. However, local languages and traditions remain strong in many places. I believe we will see a blend, a 'glocal' culture, rather than a single uniform one.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'distinct', 'consciousness', 'similar challenges', 'traditions', 'blend', 'glocal', 'uniform'. >Band 6: Advanced vocabulary. Not Band 8: Slightly academic.",
    grammar_reason="[GRA7] Contrast: 'However', 'but distinct cultures...'. Future tense: 'will see'. >Band 6: Accurate complex sentences. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 480: V7/G7 - Topic: Transport (Cities)
samples.append(create_sample(
    index=480,
    vocab_band=7,
    grammar_band=7,
    question="Why is urban planning important?",
    transcript="It determines the quality of life for residents. Good planning ensures that housing, work, and leisure are accessible. It integrates green spaces and efficient transport systems. Without planning, cities become chaotic and polluted. Sprawl increases commute times and reduces social interaction. A well-designed city fosters community and health.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'determines', 'residents', 'accessible', 'integrates', 'chaotic', 'sprawl', 'commute', 'fosters'. >Band 6: Precise vocabulary. Not Band 8: Lacks idiomatic usage.",
    grammar_reason="[GRA7] Reason: 'Without planning...'. Relative clause implied. >Band 6: Frequent error-free sentences. Not Band 8: Structure is standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 481: V7/G7 - Topic: Work (Job Satisfaction)
samples.append(create_sample(
    index=481,
    vocab_band=7,
    grammar_band=7,
    question="What makes a job meaningful?",
    transcript="It is the sense of contribution. Knowing that your work helps others or solves a problem is motivating. It goes beyond salary. Autonomy and mastery are also key factors. If you can grow and learn, the job feels worthwhile. Meaning is subjective, but it usually involves connecting with a larger purpose.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'contribution', 'motivating', 'autonomy', 'mastery', 'worthwhile', 'subjective', 'connecting'. >Band 6: Good range. Not Band 8: Lacks 'fulfillment', 'impact', 'vocational'.",
    grammar_reason="[GRA7] Gerund: 'Knowing that your work...'. Conditionals: 'If you can grow...'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 482: V7/G7 - Topic: Education (Technology)
samples.append(create_sample(
    index=482,
    vocab_band=7,
    grammar_band=7,
    question="Has technology improved education?",
    transcript="It has democratized access to information. Students can learn anything, anywhere. Interactive tools make complex subjects easier to understand. However, it can also be a distraction. Students might browse social media instead of studying. Also, not everyone has equal access to technology, which creates a digital divide. So, the impact is mixed.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'democratized', 'access', 'interactive', 'distraction', 'browse', 'digital divide', 'mixed'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA7] Contrast: 'However', 'but it can also...'. Relative clause: 'which creates...'. >Band 6: Good control. Not Band 8: Sentences are competent.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 483: V7/G7 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=483,
    vocab_band=7,
    grammar_band=7,
    question="Are zoos good for conservation?",
    transcript="Modern zoos play a significant role. They run breeding programs for endangered species, which can prevent extinction. They also educate the public about biodiversity. However, the quality of zoos varies. Some prioritize profit over animal welfare. Keeping intelligent animals in small enclosures is unethical. Conservation should focus on protecting natural habitats primarily.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'significant role', 'breeding programs', 'endangered', 'extinction', 'biodiversity', 'prioritize', 'welfare', 'unethical', 'habitats'. >Band 6: Advanced vocabulary. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA7] Relative clause: 'which can prevent'. Contrast: 'However'. >Band 6: Accurate complex sentences. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 484: V7/G7 - Topic: Technology (Space)
samples.append(create_sample(
    index=484,
    vocab_band=7,
    grammar_band=7,
    question="Should private companies explore space?",
    transcript="It brings innovation and speed. Private companies like SpaceX have reduced the cost of launching rockets. They are more agile than government agencies. However, their primary motive is profit. Space could become commercialized and exploited. We need international laws to regulate their activities. Space should remain a resource for all humanity, not just corporations.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'innovation', 'agile', 'agencies', 'motive', 'commercialized', 'exploited', 'regulate', 'humanity', 'corporations'. >Band 6: Sophisticated terms. Not Band 8: Slightly robotic.",
    grammar_reason="[GRA7] Comparison: 'more agile than'. Contrast: 'However'. >Band 6: Good control. Not Band 8: Sentences are standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 485: V7/G7 - Topic: Society (Volunteer)
samples.append(create_sample(
    index=485,
    vocab_band=7,
    grammar_band=7,
    question="Should everyone do voluntary work?",
    transcript="It would benefit society greatly. Volunteering builds empathy and understanding between different groups. It strengthens the community fabric. For the individual, it provides perspective and new skills. However, making it mandatory might cause resentment. It should remain a choice. We should encourage it by highlighting the value it brings to both the giver and receiver.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'benefit', 'empathy', 'fabric', 'perspective', 'mandatory', 'resentment', 'highlighting', 'giver and receiver'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'altruism', 'civic duty', 'solidarity'.",
    grammar_reason="[GRA7] Conditionals implied: 'making it mandatory might...'. Reason: 'For the individual...'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 486: V7/G7 - Topic: Culture (Global)
samples.append(create_sample(
    index=486,
    vocab_band=7,
    grammar_band=7,
    question="Is it important to preserve minority languages?",
    transcript="Yes, because language encodes culture. When a language dies, unique knowledge and traditions are lost. It diminishes global diversity. Minority languages give people a sense of identity and belonging. Preserving them respects human rights. Governments should support bilingual education to keep these languages alive. Diversity makes the world richer.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'encodes', 'unique', 'diminishes', 'diversity', 'identity', 'belonging', 'bilingual'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'linguistic', 'heritage', 'ancestral'.",
    grammar_reason="[GRA7] Reason: 'because language encodes'. Time clause: 'When a language dies'. >Band 6: Frequent error-free sentences. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 487: V7/G7 - Topic: Work (Job)
samples.append(create_sample(
    index=487,
    vocab_band=7,
    grammar_band=7,
    question="What makes a successful career?",
    transcript="Success is subjective. For some, it is reaching the top of the corporate ladder and earning a high salary. For others, it is about work-life balance and doing meaningful work. I think a successful career is one where you are constantly learning and growing. If you wake up excited to work, you are successful.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'subjective', 'corporate ladder', 'meaningful', 'constantly', 'excited'. >Band 6: Good range. Not Band 8: Lacks 'fulfillment', 'impact', 'legacy'.",
    grammar_reason="[GRA7] Conditionals: 'If you wake up...'. Relative clause: 'where you are constantly...'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 488: V7/G7 - Topic: Health (Diet)
samples.append(create_sample(
    index=488,
    vocab_band=7,
    grammar_band=7,
    question="Why are vegetarian diets becoming popular?",
    transcript="People are more health-conscious. They know that reducing meat consumption lowers the risk of heart disease. Also, there are ethical reasons. People are concerned about animal welfare in factory farms. Environmental awareness is another factor. Meat production creates high carbon emissions. Plant-based diets are seen as a sustainable choice for the future.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'health-conscious', 'consumption', 'ethical', 'animal welfare', 'factory farms', 'awareness', 'emissions', 'plant-based', 'sustainable'. >Band 6: Very good vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA7] Reason: 'because people are concerned...'. Passive: 'are seen as'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 489: V7/G7 - Topic: Transport (Cars)
samples.append(create_sample(
    index=489,
    vocab_band=7,
    grammar_band=7,
    question="Will self-driving cars be safe?",
    transcript="Theoretically, yes. They eliminate human error, which is the cause of most accidents. They don't get tired or distracted. They can communicate with each other to avoid collisions. However, the technology is not perfect yet. There are concerns about hacking and software glitches. We need rigorous testing before they become mainstream.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'theoretically', 'eliminate', 'distracted', 'collisions', 'hacking', 'glitches', 'rigorous', 'mainstream'. >Band 6: Advanced vocabulary. Not Band 8: Lacks 'liability', 'regulation', 'algorithm'.",
    grammar_reason="[GRA7] Relative clause: 'which is the cause'. Contrast: 'However'. >Band 6: Accurate grammar. Not Band 8: Sentences are somewhat short.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 490: V7/G7 - Topic: Technology (Communication)
samples.append(create_sample(
    index=490,
    vocab_band=7,
    grammar_band=7,
    question="How does social media affect self-esteem?",
    transcript="It often has a negative impact. People present a curated, perfect version of their lives online. When we scroll through our feeds, we compare ourselves to these unrealistic images. This leads to feelings of inadequacy and envy. Likes and comments become a measure of worth. We need to remember that social media is a highlight reel, not reality.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'negative impact', 'curated', 'unrealistic', 'inadequacy', 'envy', 'measure of worth', 'highlight reel'. >Band 6: Sophisticated terms. Not Band 8: Lacks natural flow.",
    grammar_reason="[GRA7] Time clause: 'When we scroll'. Reason: 'This leads to...'. >Band 6: Good control. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 491: V7/G7 - Topic: Environment (Water)
samples.append(create_sample(
    index=491,
    vocab_band=7,
    grammar_band=7,
    question="What causes water pollution?",
    transcript="Industrial waste is a major contributor. Factories often dump toxic chemicals into rivers. Agriculture also plays a part. Pesticides and fertilizers wash into the water supply. Plastic waste is another visible problem. It clogs waterways and harms marine life. We need stricter regulations and better waste management systems to protect our water sources.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'contributor', 'toxic chemicals', 'pesticides', 'fertilizers', 'clogs', 'marine life', 'regulations', 'waste management'. >Band 6: Specific vocabulary. Not Band 8: Lacks 'runoff', 'contaminants', 'ecosystem'.",
    grammar_reason="[GRA7] Reason: 'Factories often dump...'. Relative clause implied. >Band 6: Accurate grammar. Not Band 8: Simple sentence links.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 492: V7/G7 - Topic: Education (Skills)
samples.append(create_sample(
    index=492,
    vocab_band=7,
    grammar_band=7,
    question="Should schools teach financial literacy?",
    transcript="Absolutely. Money management is an essential life skill. Many young people graduate without knowing how to budget, save, or invest. They fall into debt easily. Understanding credit cards, loans, and taxes is crucial for independence. If schools teach this, students will make better financial decisions in the future. It empowers them.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'literacy', 'essential', 'budget', 'invest', 'debt', 'crucial', 'independence', 'empowers'. >Band 6: Relevant terms. Not Band 8: Lacks 'compound interest', 'mortgage', 'fiscal responsibility'.",
    grammar_reason="[GRA7] Conditionals: 'If schools teach this...'. Reason: 'Money management is...'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 493: V7/G7 - Topic: Society (Cities)
samples.append(create_sample(
    index=493,
    vocab_band=7,
    grammar_band=7,
    question="How can we reduce homelessness?",
    transcript="It requires a comprehensive strategy. First, we need more affordable housing. Shelters are temporary; people need permanent homes. Second, we must address the root causes, such as mental health issues and addiction. Providing support services is key. Employment programs can also help people get back on their feet. It is a complex social issue that needs compassion and funding.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'comprehensive strategy', 'affordable housing', 'temporary', 'root causes', 'addiction', 'support services', 'compassion'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'systemic', 'reintegration', 'marginalized'.",
    grammar_reason="[GRA7] Sequencing: 'First... Second...'. Relative clause: 'that needs compassion'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 494: V7/G7 - Topic: Culture (Art)
samples.append(create_sample(
    index=494,
    vocab_band=7,
    grammar_band=7,
    question="Why is art expensive?",
    transcript="The value of art is subjective. It depends on the reputation of the artist. If they are famous, the demand is high, so the price rises. Also, rarity plays a role. An original painting is unique. Art is also seen as an investment. Collectors buy it hoping the value will increase. It is a market driven by prestige and speculation.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'subjective', 'reputation', 'rarity', 'investment', 'collectors', 'prestige', 'speculation'. >Band 6: Sophisticated terms. Not Band 8: Lacks 'provenance', 'auction', 'masterpiece'.",
    grammar_reason="[GRA7] Conditionals: 'If they are famous...'. Passive: 'driven by prestige'. >Band 6: Good control. Not Band 8: Sentences are competent.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 495: V7/G7 - Topic: Work (Remote)
samples.append(create_sample(
    index=495,
    vocab_band=7,
    grammar_band=7,
    question="Will offices disappear in the future?",
    transcript="I doubt it. While remote work is popular, offices serve a purpose. They are hubs for collaboration and innovation. Face-to-face interaction builds company culture and trust. Some people also prefer the separation between work and home. Hybrid models will likely become the norm. Offices will change, becoming more flexible spaces, but they won't vanish completely.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'hubs', 'collaboration', 'innovation', 'interaction', 'company culture', 'hybrid models', 'norm', 'vanish'. >Band 6: Advanced vocabulary. Not Band 8: Lacks 'synergy', 'corporate', 'dynamic'.",
    grammar_reason="[GRA7] Contrast: 'While remote work is popular'. Future tense: 'will likely become'. >Band 6: Accurate complex sentences. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 496: V7/G7 - Topic: Technology (AI)
samples.append(create_sample(
    index=496,
    vocab_band=7,
    grammar_band=7,
    question="How will AI change healthcare?",
    transcript="It will revolutionize diagnosis and treatment. AI algorithms can analyze medical images with high accuracy, detecting diseases early. It can also personalize medicine, tailoring treatments to an individual's genetics. Robots might perform precise surgeries. However, the human touch is irreplaceable. Doctors and nurses provide empathy and care that machines cannot. AI will assist, not replace, medical professionals.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'revolutionize', 'diagnosis', 'algorithms', 'accuracy', 'detecting', 'personalize', 'tailoring', 'genetics', 'irreplaceable', 'empathy'. >Band 6: Very good vocabulary. Not Band 8: Lacks flow.",
    grammar_reason="[GRA7] Contrast: 'However'. Future tense: 'It will revolutionize'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 497: V7/G7 - Topic: Environment (Climate)
samples.append(create_sample(
    index=497,
    vocab_band=7,
    grammar_band=7,
    question="Is it too late to stop climate change?",
    transcript="It is not too late, but the window is closing. We have the technology and knowledge to solve it. Renewable energy is cheaper than ever. However, we lack political will. Governments delay action because of economic interests. If we act now, we can limit the damage. It requires a global effort and a shift in our consumption habits.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'window is closing' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'window', 'renewable', 'political will', 'delay', 'limit', 'consumption habits'. >Band 6: Strong vocabulary. Not Band 8: Lacks 'urgency', 'mitigation', 'catastrophic'.",
    grammar_reason="[GRA7] Conditionals: 'If we act now...'. Contrast: 'However'. >Band 6: Accurate grammar. Not Band 8: Simple sentence links.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 498: V7/G7 - Topic: Society (Family)
samples.append(create_sample(
    index=498,
    vocab_band=7,
    grammar_band=7,
    question="Why are families becoming smaller?",
    transcript="Economic factors are the main reason. Raising children is expensive. Housing, education, and childcare costs have risen. Also, women are prioritizing their careers. They marry later and have fewer children. Urbanization plays a role too. In cities, large families are impractical. People value quality over quantity, investing more resources in fewer children.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'economic factors', 'prioritizing', 'urbanization', 'impractical', 'value', 'resources'. >Band 6: Relevant vocabulary. Not Band 8: Lacks 'demographic', 'fertility rate', 'trend'.",
    grammar_reason="[GRA7] Reason: 'because raising children is expensive' (implied). List structure. >Band 6: Frequent error-free sentences. Not Band 8: Standard forms.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 499: V7/G7 - Topic: Transport (Safety)
samples.append(create_sample(
    index=499,
    vocab_band=7,
    grammar_band=7,
    question="How can we make air travel safer?",
    transcript="It is already statistically the safest mode of transport. However, improvements can be made. Better pilot training and mental health checks are crucial. Technology can help detect mechanical faults early. Stricter security screenings at airports prevent threats. International cooperation on safety standards ensures consistency. Safety is a continuous process of learning from past incidents.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'statistically', 'mode', 'crucial', 'detect', 'mechanical faults', 'screenings', 'consistency', 'incidents'. >Band 6: Precise terms. Not Band 8: Lacks 'aviation', 'protocols', 'rigorous'.",
    grammar_reason="[GRA7] Contrast: 'However'. Relative clause implied. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 500: V7/G7 - Topic: Education (Teacher)
samples.append(create_sample(
    index=500,
    vocab_band=7,
    grammar_band=7,
    question="Do teachers get enough respect?",
    transcript="In many societies, no. They are undervalued despite their crucial role. They shape the minds of the future but are often underpaid and overworked. Parents sometimes blame teachers for their children's behavior. This lack of respect leads to a teacher shortage. We need to restore the status of the teaching profession. They deserve our gratitude and support.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR7] Uses less common items: 'undervalued', 'crucial role', 'shape', 'underpaid', 'shortage', 'restore', 'status', 'profession', 'gratitude'. >Band 6: Strong vocabulary. Not Band 8: Slightly formal.",
    grammar_reason="[GRA7] Contrast: 'but are often underpaid'. Reason: 'This lack of respect leads to...'. >Band 6: Good control. Not Band 8: Sentences are competent.",
    idiom_present=False,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
