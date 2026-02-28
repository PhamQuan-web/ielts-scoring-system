import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch08.jsonl")

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

# --- BATCH 08 PART 1: SAMPLES 651-670 (20 Total) ---
# Combo: V8/G8 (Very Good Vocab, Very Good Grammar)

# Sample 651: V8/G8 - Topic: Environment (Sustainability)
samples.append(create_sample(
    index=651,
    vocab_band=8,
    grammar_band=8,
    question="Why is sustainable development important?",
    transcript="It is imperative for the longevity of our planet. If we continue to deplete finite resources at the current rate, we jeopardize the well-being of future generations. Sustainable development strikes a balance between economic growth and environmental preservation. It ensures that we meet our current needs without compromising the ability of our descendants to meet theirs. Transitioning to a green economy is not merely an option; it is a necessity.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'imperative', 'longevity', 'deplete', 'finite', 'jeopardize', 'strikes a balance', 'compromising', 'descendants'. >Band 7: Precise and varied. Not Band 9: Lacks full native-like flow.",
    grammar_reason="[GRA8] Wide range: 'If we continue to...', 'It ensures that we meet...', 'Transitioning... is not merely...'. Error-free. >Band 7: High level of accuracy and complexity.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 652: V8/G8 - Topic: Technology (AI)
samples.append(create_sample(
    index=652,
    vocab_band=8,
    grammar_band=8,
    question="Will AI surpass human intelligence?",
    transcript="It is a distinct possibility that has experts divided. While AI currently excels at specialized tasks, achieving general artificial intelligence remains elusive. However, the exponential growth in computing power suggests we might reach a singularity sooner than anticipated. If machines develop consciousness, the implications for humanity would be profound. We must tread carefully, ensuring that ethical frameworks evolve alongside technological advancements.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'distinct possibility', 'excels', 'elusive', 'exponential growth', 'singularity', 'anticipated', 'consciousness', 'implications', 'tread carefully'. >Band 7: Advanced vocabulary used naturally. Not Band 9: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'While AI currently excels...', 'If machines develop...', 'ensuring that...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 653: V8/G8 - Topic: Education (University)
samples.append(create_sample(
    index=653,
    vocab_band=8,
    grammar_band=8,
    question="Is the cost of university education justified?",
    transcript="It is a contentious issue. Proponents argue that the return on investment, in terms of lifetime earnings and personal development, warrants the expense. However, the spiraling cost of tuition has left many graduates saddled with debilitating debt. This financial burden can stifle their future prospects, delaying milestones like home ownership. Ideally, education should be a public good, funded by the state to ensure equal access for all.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'contentious', 'proponents', 'return on investment', 'warrants', 'spiraling', 'saddled with', 'debilitating', 'stifle', 'milestones'. >Band 7: Precise and effective. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'Proponents argue that...', 'leaving many graduates...', 'Ideally, education should be...'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 654: V8/G8 - Topic: Society (Inequality)
samples.append(create_sample(
    index=654,
    vocab_band=8,
    grammar_band=8,
    question="Can we eradicate poverty?",
    transcript="Eradicating poverty is a monumental challenge, but not an insurmountable one. It requires a multifaceted approach involving systemic change. Wealth redistribution, accessible education, and healthcare are fundamental pillars. Furthermore, empowering marginalized communities to participate in the economy is crucial. While complete eradication might be utopian, significant reduction is within our grasp if there is sufficient political will and global cooperation.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'monumental', 'insurmountable', 'multifaceted', 'systemic', 'redistribution', 'pillars', 'empowering', 'marginalized', 'utopian', 'within our grasp'. >Band 7: Strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'but not an insurmountable one', 'While complete eradication might be...', 'if there is sufficient...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 655: V8/G8 - Topic: Culture (Globalization)
samples.append(create_sample(
    index=655,
    vocab_band=8,
    grammar_band=8,
    question="How can we preserve cultural heritage?",
    transcript="Preservation requires a proactive effort to safeguard intangible assets like language and folklore, not just physical monuments. Digital archiving can play a pivotal role in recording dying traditions for posterity. Moreover, integrating cultural education into school curricula ensures that the younger generation appreciates their roots. We must also resist the homogenizing force of globalization by celebrating local distinctiveness. It is about keeping the flame of tradition alive.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'proactive', 'safeguard', 'intangible assets', 'folklore', 'archiving', 'pivotal', 'posterity', 'curricula', 'homogenizing', 'distinctiveness'. Idiom: 'keeping the flame alive'. >Band 7: Precise terms. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'not just physical monuments', 'integrating... ensures that...', 'by celebrating...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 656: V8/G8 - Topic: Work (Job)
samples.append(create_sample(
    index=656,
    vocab_band=8,
    grammar_band=8,
    question="What makes a company successful?",
    transcript="Beyond financial profitability, a successful company cultivates a positive corporate culture. Employees who feel valued and empowered are more innovative and productive. Adaptability is also a key determinant; companies must pivot quickly in response to market shifts. Furthermore, ethical practices build brand loyalty and trust. Ultimately, success stems from a combination of visionary leadership, a dedicated workforce, and a commitment to excellence.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'profitability', 'cultivates', 'corporate culture', 'empowered', 'innovative', 'adaptability', 'determinant', 'pivot', 'market shifts', 'visionary'. >Band 7: Strong vocabulary. Not Band 9: Slightly business-speak.",
    grammar_reason="[GRA8] Wide range: 'Employees who feel...', 'companies must pivot...', 'success stems from...'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 657: V8/G8 - Topic: Transport (Cities)
samples.append(create_sample(
    index=657,
    vocab_band=8,
    grammar_band=8,
    question="How will urban transport evolve?",
    transcript="We are on the cusp of a transportation revolution. The convergence of electric propulsion and autonomous driving will transform urban mobility. We will likely see a shift from private ownership to shared mobility-as-a-service models. This would alleviate congestion and reduce the carbon footprint of cities. However, realizing this vision requires substantial investment in infrastructure and a robust regulatory framework.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'cusp', 'revolution', 'convergence', 'propulsion', 'autonomous', 'mobility-as-a-service', 'alleviate', 'carbon footprint', 'regulatory framework'. >Band 7: Technical/formal. Not Band 9: Lacks idiomatic usage.",
    grammar_reason="[GRA8] Wide range: 'The convergence... will transform...', 'shift from... to...', 'realizing this vision requires...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 658: V8/G8 - Topic: Health (Exercise)
samples.append(create_sample(
    index=658,
    vocab_band=8,
    grammar_band=8,
    question="Why do people struggle to maintain a healthy lifestyle?",
    transcript="The ubiquity of processed foods and the sedentary nature of modern work create an 'obesogenic' environment. We are biologically wired to seek high-calorie foods, a survival mechanism that is maladaptive in the modern world. Furthermore, the frantic pace of life leaves little time for exercise or meal preparation. Breaking these ingrained habits requires significant willpower and, ideally, systemic changes to make healthy choices the path of least resistance.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'ubiquity', 'sedentary', 'obesogenic', 'biologically wired', 'maladaptive', 'frantic', 'ingrained', 'willpower', 'path of least resistance'. >Band 7: Advanced vocabulary. Not Band 9: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'create an obesogenic environment', 'a survival mechanism that is...', 'Breaking these habits requires...'. Error-free. >Band 7: High level of accuracy.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 659: V8/G8 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=659,
    vocab_band=8,
    grammar_band=8,
    question="Why is poaching still a problem?",
    transcript="It is driven by the lucrative black market for animal parts. Despite international bans, demand for ivory, rhino horn, and other products persists, particularly in parts of Asia. Poaching syndicates are often highly organized and well-funded, making enforcement difficult. Additionally, poverty in range states drives locals to participate in illegal hunting. Eradicating poaching requires a two-pronged strategy: strict law enforcement and demand reduction campaigns.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'lucrative', 'black market', 'persists', 'syndicates', 'enforcement', 'range states', 'eradicating', 'two-pronged strategy'. >Band 7: Strong vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'Despite international bans...', 'making enforcement difficult', 'drives locals to participate'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 660: V8/G8 - Topic: Education (Reading)
samples.append(create_sample(
    index=660,
    vocab_band=8,
    grammar_band=8,
    question="How does reading benefit critical thinking?",
    transcript="Reading, particularly complex texts, demands sustained attention and cognitive effort. It forces the reader to analyze arguments, identify biases, and synthesize information. Unlike passive media consumption, reading is an active process that strengthens neural pathways. It exposes us to diverse viewpoints, challenging our preconceived notions. Consequently, avid readers are often better equipped to navigate nuance and ambiguity in the real world.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'sustained attention', 'cognitive effort', 'synthesize', 'passive', 'neural pathways', 'preconceived notions', 'avid', 'navigate', 'ambiguity'. >Band 7: Precise terms. Not Band 9: Slightly robotic.",
    grammar_reason="[GRA8] Wide range: 'It forces the reader to...', 'Unlike passive media...', 'challenging our preconceived notions'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 661: V8/G8 - Topic: Technology (Data)
samples.append(create_sample(
    index=661,
    vocab_band=8,
    grammar_band=8,
    question="Is data privacy a lost cause?",
    transcript="It certainly feels precarious. We leave a digital footprint with every click, which corporations harvest and monetize. The sheer volume of data makes anonymity almost impossible. However, declaring it a lost cause is defeatist. We are seeing a backlash in the form of stricter regulations like GDPR. Privacy enhancing technologies are also emerging. The battle for privacy is ongoing, and awareness is our best defense.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'precarious', 'digital footprint', 'harvest', 'monetize', 'anonymity', 'defeatist', 'backlash', 'regulations', 'emerging'. >Band 7: Strong vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'which corporations harvest...', 'declaring it a lost cause is...', 'The battle... is ongoing'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 662: V8/G8 - Topic: Society (Volunteer)
samples.append(create_sample(
    index=662,
    vocab_band=8,
    grammar_band=8,
    question="Should volunteering be incentivized?",
    transcript="While incentives might boost participation rates, they could undermine the altruistic spirit of volunteering. If people volunteer solely for rewards, the intrinsic value of the act is diminished. However, acknowledging contributions through recognition or accreditation can be beneficial. It validates the volunteer's effort without commodifying it. The ideal approach balances encouragement with the preservation of the genuine desire to serve the community.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'incentives', 'undermine', 'altruistic', 'intrinsic value', 'diminished', 'acknowledging', 'accreditation', 'commodifying', 'preservation'. >Band 7: Precise terms. Not Band 9: Slightly academic.",
    grammar_reason="[GRA8] Wide range: 'While incentives might...', 'If people volunteer...', 'without commodifying it'. Error-free. >Band 7: Complex structures used naturally.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 663: V8/G8 - Topic: Culture (Art)
samples.append(create_sample(
    index=663,
    vocab_band=8,
    grammar_band=8,
    question="How does art influence society?",
    transcript="Art is a catalyst for social change. It has the power to provoke thought, challenge the status quo, and amplify marginalized voices. Through visual or performative mediums, artists can highlight injustice and inspire collective action. Moreover, art fosters empathy by allowing us to experience the world through another's eyes. It is not merely decoration; it is a vital component of a reflective and progressive society.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'catalyst', 'provoke', 'status quo', 'amplify', 'marginalized', 'mediums', 'collective action', 'fosters', 'reflective', 'progressive'. >Band 7: Strong vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'It has the power to...', 'by allowing us to...', 'It is not merely..., it is...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 664: V8/G8 - Topic: Work (Gender)
samples.append(create_sample(
    index=664,
    vocab_band=8,
    grammar_band=8,
    question="What obstacles do women face in the workplace?",
    transcript="Despite progress, the 'glass ceiling' remains a formidable barrier. Women are often bypassed for leadership roles due to unconscious bias or outdated stereotypes. The burden of unpaid care work also disproportionately falls on women, hindering their career progression. Furthermore, workplace cultures can be exclusionary or even hostile. Achieving true equality requires dismantling these systemic obstacles and fostering an inclusive environment where meritocracy prevails.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'glass ceiling' (idiom/term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'formidable barrier', 'bypassed', 'unconscious bias', 'outdated stereotypes', 'disproportionately', 'hindering', 'exclusionary', 'systemic', 'meritocracy'. Idiom: 'glass ceiling'. >Band 7: Advanced terms. Not Band 9: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'Despite progress...', 'due to...', 'Achieving true equality requires...'. Error-free. >Band 7: Complex sentence structures.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 665: V8/G8 - Topic: Transport (Flying)
samples.append(create_sample(
    index=665,
    vocab_band=8,
    grammar_band=8,
    question="Are budget airlines good for the industry?",
    transcript="They have certainly democratized air travel, making it accessible to a broader demographic. This has stimulated tourism and economic growth in many regions. However, the race to the bottom on price often comes at the expense of service quality and employee conditions. Furthermore, the low cost encourages excessive flying, exacerbating the environmental crisis. While beneficial for consumers' wallets, the long-term sustainability of this model is questionable.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'race to the bottom' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'democratized', 'demographic', 'stimulated', 'expense', 'excessive', 'exacerbating', 'sustainability', 'questionable'. Idiom: 'race to the bottom'. >Band 7: Strong vocabulary. Not Band 9: Slightly robotic.",
    grammar_reason="[GRA8] Wide range: 'making it accessible...', 'However, the race...', 'While beneficial..., the...'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 666: V8/G8 - Topic: Education (Technology)
samples.append(create_sample(
    index=666,
    vocab_band=8,
    grammar_band=8,
    question="Does technology hinder learning?",
    transcript="It can contain potential distractions, but 'hinder' is too strong a word. When used indiscriminately, devices can divert attention from the lesson. However, technology also provides unparalleled access to information and interactive learning tools. The key is integration. If technology is woven seamlessly into the curriculum to enhance, rather than replace, traditional methods, it becomes a powerful asset. It requires disciplined usage.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'indiscriminately', 'divert', 'unparalleled', 'interactive', 'integration', 'woven', 'seamlessly', 'enhance', 'asset', 'disciplined'. >Band 7: Precise terms. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'When used indiscriminately...', 'If technology is woven...', 'rather than replace...'. Error-free. >Band 7: Accurate complex sentences.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 667: V8/G8 - Topic: Society (Housing)
samples.append(create_sample(
    index=667,
    vocab_band=8,
    grammar_band=8,
    question="Is home ownership a realistic goal for young people?",
    transcript="For many, it is becoming an elusive dream. Skyrocketing property prices and stagnant wages have created a massive affordability gap. The requirement for a substantial deposit is a significant barrier to entry. Consequently, an entire generation is being dubbed 'Generation Rent'. Unless there is a market correction or significant government intervention to increase supply, owning a home will remain a privilege of the wealthy.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'elusive dream', 'skyrocketing', 'stagnant', 'affordability gap', 'substantial', 'barrier to entry', 'dubbed', 'correction', 'intervention'. >Band 7: Strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA8] Wide range: 'For many, it is...', 'Consequently, an entire generation...', 'Unless there is...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 668: V8/G8 - Topic: Environment (Trees)
samples.append(create_sample(
    index=668,
    vocab_band=8,
    grammar_band=8,
    question="How can we prevent deforestation?",
    transcript="We need a multi-pronged strategy. Firstly, we must enforce stricter regulations against illegal logging. Secondly, we should incentivize sustainable forestry practices, such as selective logging and replanting. Consumer pressure is also vital; boycotting products linked to deforestation sends a strong signal. Finally, empowering local communities to manage their forests has proven effective. It requires global cooperation and a shift away from exploitative economics.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'multi-pronged', 'enforce', 'incentivize', 'forestry', 'selective logging', 'boycotting', 'empowering', 'exploitative'. >Band 7: Advanced vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA8] Wide range: 'such as...', 'sends a strong signal', 'has proven effective'. Error-free. >Band 7: Varied and accurate.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 669: V8/G8 - Topic: Technology (Social Media)
samples.append(create_sample(
    index=669,
    vocab_band=8,
    grammar_band=8,
    question="Is social media addictive?",
    transcript="It is engineered to be so. Platforms utilize algorithms designed to trigger dopamine release, keeping users engaged for as long as possible. Features like infinite scroll and push notifications exploit our psychological vulnerabilities. This constant need for validation and fear of missing out (FOMO) creates a compulsive loop. Recognizing these manipulative design patterns is the first step towards regaining control over our digital lives.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'fear of missing out' (FOMO)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'engineered', 'algorithms', 'trigger', 'dopamine', 'infinite scroll', 'vulnerabilities', 'compulsive loop', 'manipulative'. Term: 'FOMO'. >Band 7: Precise terms. Not Band 9: Slightly technical.",
    grammar_reason="[GRA8] Wide range: 'designed to trigger...', 'keeping users engaged...', 'Recognizing... is the first step'. Error-free. >Band 7: Sophisticated control.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 670: V8/G8 - Topic: Work (Job Hopping)
samples.append(create_sample(
    index=670,
    vocab_band=8,
    grammar_band=8,
    question="Does job hopping look bad on a resume?",
    transcript="It used to be a red flag, signaling instability. However, the stigma has faded. Employers now recognize that diverse experience can be an asset. It demonstrates adaptability and a willingness to learn. That said, serial hopping without staying long enough to make an impact can still be detrimental. The key is to frame the changes as a coherent narrative of career progression and skill acquisition.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'red flag' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "high"},
    vocab_reason="[LR8] Uses sophisticated items: 'instability', 'stigma', 'asset', 'demonstrates', 'adaptability', 'serial', 'detrimental', 'coherent narrative', 'acquisition'. Idiom: 'red flag'. >Band 7: Strong vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA8] Wide range: 'It used to be..., signaling...', 'without staying long enough...', 'The key is to...'. Error-free. >Band 7: Sophisticated structures.",
    idiom_present=True,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Generated {len(samples)} samples in {OUTPUT_FILE}")
