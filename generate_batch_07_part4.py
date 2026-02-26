import json
import os

OUTPUT_DIR = "ielts-data/phase3/v76_review_output/jules2"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jules2_batch07.jsonl")

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

# --- BATCH 07 PART 4: SAMPLES 626-650 (25 Total) ---
# Combo: V8/G7

# Sample 626: V8/G7 - Topic: Education (University)
samples.append(create_sample(
    index=626,
    vocab_band=8,
    grammar_band=7,
    question="Why are humanities subjects declining?",
    transcript="There is a pervasive belief that they lack utility. Students are gravitating towards STEM fields due to the perceived employability and salary prospects. Humanities are often dismissed as 'soft' subjects. However, this is a myopic view. Subjects like history and philosophy cultivate critical reasoning and ethics, which are indispensable in a complex world. Neglecting them impoverishes our intellectual landscape.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'pervasive', 'gravitating', 'employability', 'prospects', 'dismissed', 'myopic', 'cultivate', 'indispensable', 'impoverishes'. >Band 7: Advanced vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA7] Contrast: 'However'. Relative clause: 'which are indispensable'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 627: V8/G7 - Topic: Society (Friendship)
samples.append(create_sample(
    index=627,
    vocab_band=8,
    grammar_band=7,
    question="Is friendship different in the digital age?",
    transcript="Profoundly so. Digital platforms facilitate connectivity but often at the expense of depth. We accumulate hundreds of 'friends' online, yet true intimacy remains elusive. The curated nature of social media creates a facade of connection. We perform friendship rather than experience it. While technology bridges geographical gaps, it cannot replicate the nuance of physical presence.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'expense of depth' (collocation)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'profoundly', 'facilitate', 'connectivity', 'accumulate', 'intimacy', 'elusive', 'curated', 'facade', 'replicate', 'nuance'. >Band 7: Strong vocabulary. Not Band 9: Lacks idiomatic flow.",
    grammar_reason="[GRA7] Contrast: 'yet true intimacy...', 'While technology bridges...'. >Band 6: Good control. Not Band 8: Sentences are competent.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 628: V8/G7 - Topic: Work (Leadership)
samples.append(create_sample(
    index=628,
    vocab_band=8,
    grammar_band=7,
    question="What is the hardest part of being a leader?",
    transcript="Making unpopular decisions is arguably the most challenging aspect. Leaders must often prioritize the long-term viability of the organization over short-term popularity. This can lead to alienation and dissent among staff. Additionally, the burden of responsibility is immense. Every failure is ultimately scrutinized. Maintaining resilience in the face of criticism requires a thick skin and unwavering vision.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'thick skin' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'arguably', 'prioritize', 'viability', 'alienation', 'dissent', 'burden', 'scrutinized', 'resilience', 'unwavering'. Idiom: 'thick skin'. >Band 7: Precise terms. Not Band 9: Slightly academic.",
    grammar_reason="[GRA7] Reason: 'This can lead to...'. Passive: 'is ultimately scrutinized'. >Band 6: Accurate complex sentences. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 629: V8/G7 - Topic: Environment (Wildlife)
samples.append(create_sample(
    index=629,
    vocab_band=8,
    grammar_band=7,
    question="Can we save endangered species?",
    transcript="It is contingent on our collective will. Conservation efforts have had sporadic successes, but the trajectory is worrying. Habitat loss and poaching are formidable enemies. To reverse the trend, we need robust international legislation and enforcement. We must also address the underlying economic drivers of exploitation. Saving species is not just biology; it is a battle against greed and apathy.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'contingent', 'collective will', 'sporadic', 'trajectory', 'formidable', 'robust', 'legislation', 'enforcement', 'underlying', 'apathy'. >Band 7: Very strong vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA7] Contrast: 'but the trajectory is...'. Purpose: 'To reverse the trend'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structure.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 630: V8/G7 - Topic: Culture (Art)
samples.append(create_sample(
    index=630,
    vocab_band=8,
    grammar_band=7,
    question="Why is art funding often cut?",
    transcript="Because it is viewed as a dispensable luxury during austerity. Governments prioritize tangible sectors like healthcare and defense. The benefits of art are intangible and hard to quantify, making it an easy target for budget cuts. However, this is short-sighted. Art fosters innovation and social cohesion. Neglecting the cultural sector erodes the spirit of the nation.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'dispensable', 'austerity', 'tangible', 'intangible', 'quantify', 'short-sighted', 'fosters', 'cohesion', 'neglecting', 'erodes'. >Band 7: Precise vocabulary. Not Band 9: Slightly robotic.",
    grammar_reason="[GRA7] Reason: 'Because it is viewed...'. Contrast: 'However'. >Band 6: Good control. Not Band 8: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 631: V8/G7 - Topic: Technology (Space)
samples.append(create_sample(
    index=631,
    vocab_band=8,
    grammar_band=7,
    question="Will we ever colonize other planets?",
    transcript="It is a distinct possibility, perhaps even an inevitability. As Earth's resources dwindle, looking to the stars becomes a survival imperative. Mars is the most viable candidate. However, the technological and physiological hurdles are monumental. Radiation and isolation pose existential threats. While colonization is a captivating dream, we are centuries away from it becoming a sustainable reality.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'distinct possibility', 'inevitability', 'dwindle', 'imperative', 'viable', 'hurdles', 'monumental', 'physiological', 'existential', 'captivating'. >Band 7: Advanced terms. Not Band 9: Lacks idiomatic usage.",
    grammar_reason="[GRA7] Time clause: 'As Earth's resources...'. Contrast: 'However', 'While colonization is...'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 632: V8/G7 - Topic: Society (Cities)
samples.append(create_sample(
    index=632,
    vocab_band=8,
    grammar_band=7,
    question="What is the impact of gentrification?",
    transcript="It is a double-edged sword. On one hand, it revitalizes neglected neighborhoods, bringing investment and safety. On the other, it displaces long-standing communities. As property values soar, original residents are priced out, leading to social fragmentation. The local character is often erased, replaced by generic chains. It is development, but at a significant social cost.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'priced out' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'revitalizes', 'neglected', 'investment', 'displaces', 'soar', 'fragmentation', 'erased', 'generic'. Idioms: 'double-edged sword', 'priced out'. >Band 7: Strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA7] Time clause: 'As property values soar'. Contrast: 'On one hand... On the other'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structure.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 633: V8/G7 - Topic: Health (Mental)
samples.append(create_sample(
    index=633,
    vocab_band=8,
    grammar_band=7,
    question="Does social media cause depression?",
    transcript="There is a compelling correlation. Platforms are designed to be addictive, fostering a culture of comparison. Users curate idealized versions of their lives, leading to feelings of inadequacy in others. This 'highlight reel' effect can trigger anxiety and low self-esteem. Furthermore, the constant need for validation through 'likes' creates a fragile sense of worth. It is a digital toxicity.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'highlight reel' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'compelling', 'correlation', 'addictive', 'fostering', 'curate', 'idealized', 'inadequacy', 'validation', 'fragile', 'toxicity'. >Band 7: Precise terms. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA7] Reason: 'leading to feelings...'. Passive implied: 'platforms are designed'. >Band 6: Accurate grammar. Not Band 8: Sentences are competent.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 634: V8/G7 - Topic: Transport (Cars)
samples.append(create_sample(
    index=634,
    vocab_band=8,
    grammar_band=7,
    question="Why do people still buy cars despite the cost?",
    transcript="The allure of autonomy is powerful. A car represents freedom and independence, a private sanctuary in a chaotic world. Public transport, while cheaper, often entails inconvenience and discomfort. For many, the car is a status symbol, an extension of their identity. Despite the financial burden and environmental guilt, the convenience and prestige are too seductive to resist.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'allure', 'autonomy', 'sanctuary', 'chaotic', 'entails', 'inconvenience', 'status symbol', 'extension', 'burden', 'seductive'. >Band 7: Very good range. Not Band 9: Slightly poetic.",
    grammar_reason="[GRA7] Contrast: 'while cheaper'. Appositive: 'a private sanctuary...'. >Band 6: Good control. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 635: V8/G7 - Topic: Environment (Climate)
samples.append(create_sample(
    index=635,
    vocab_band=8,
    grammar_band=7,
    question="Is recycling enough to save the planet?",
    transcript="Regrettably, no. It is a palliative measure, not a cure. The sheer volume of waste we produce overwhelms recycling infrastructure. We must tackle the root of the problem: overconsumption. The 'throwaway culture' must be dismantled. We need a paradigm shift towards circularity, where products are designed for longevity and repair. Recycling is the last line of defense, not the first.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'throwaway culture' (specific term)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'regrettably', 'palliative', 'sheer volume', 'overwhelms', 'infrastructure', 'overconsumption', 'dismantled', 'paradigm shift', 'circularity', 'longevity'. >Band 7: Advanced vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA7] Contrast: 'not a cure'. Passive: 'must be dismantled', 'are designed'. >Band 6: Accurate complex sentences. Not Band 8: Standard forms.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 636: V8/G7 - Topic: Education (Online)
samples.append(create_sample(
    index=636,
    vocab_band=8,
    grammar_band=7,
    question="What is the future of education?",
    transcript="It will likely be hybrid and personalized. Technology allows for adaptive learning, where the curriculum adjusts to the student's pace. This moves away from the 'one-size-fits-all' model. Virtual reality could offer immersive experiences, like visiting historical sites. However, the role of the teacher as a mentor will remain pivotal. Technology facilitates learning, but human connection inspires it.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'one-size-fits-all' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'hybrid', 'personalized', 'adaptive', 'curriculum', 'immersive', 'mentor', 'pivotal', 'facilitates', 'inspires'. Idiom: 'one-size-fits-all'. >Band 7: Strong vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA7] Relative clause: 'where the curriculum adjusts'. Contrast: 'However', 'but human connection...'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 637: V8/G7 - Topic: Culture (Global)
samples.append(create_sample(
    index=637,
    vocab_band=8,
    grammar_band=7,
    question="Is cultural diversity important?",
    transcript="It is the bedrock of a vibrant society. Diversity introduces a kaleidoscope of perspectives, fostering innovation and creativity. Homogenous societies tend to be stagnant. Exposure to different customs and beliefs cultivates tolerance and empathy. In a globalized world, the ability to navigate cultural nuances is a critical skill. Diversity is not a threat; it is our greatest asset.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'bedrock', 'vibrant', 'kaleidoscope', 'homogenous', 'stagnant', 'cultivates', 'navigate', 'nuances', 'asset'. >Band 7: Sophisticated vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA7] Reason: 'fostering innovation...'. Contrast: 'not a threat; it is...'. >Band 6: Frequent error-free sentences. Not Band 8: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 638: V8/G7 - Topic: Work (Job)
samples.append(create_sample(
    index=638,
    vocab_band=8,
    grammar_band=7,
    question="Why is work-life balance important?",
    transcript="Without it, burnout is inevitable. Chronic stress from overwork depletes our mental and physical reserves. It strains relationships and diminishes our quality of life. Maintaining a healthy equilibrium ensures sustainability in one's career. It allows time for rejuvenation and personal growth. Employers are realizing that rested employees are more productive. Balance is not a luxury; it is a necessity for longevity.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'burnout', 'inevitable', 'chronic', 'depletes', 'reserves', 'strains', 'diminishes', 'equilibrium', 'sustainability', 'rejuvenation', 'longevity'. >Band 7: Precise terms. Not Band 9: Slightly academic.",
    grammar_reason="[GRA7] Reason: 'Without it...'. Relative clause: 'that rested employees are...'. >Band 6: Accurate grammar. Not Band 8: Limited complexity.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 639: V8/G7 - Topic: Society (Cities)
samples.append(create_sample(
    index=639,
    vocab_band=8,
    grammar_band=7,
    question="How can we solve urban sprawl?",
    transcript="We must embrace high-density living. Vertical expansion is more sustainable than horizontal spread. Building upwards preserves the surrounding countryside and reduces commute times. We also need to revitalize city centers to make them attractive places to live. Mixed-use developments, combining housing and commerce, create vibrant communities. Containing sprawl requires strict zoning laws and a vision for compact, efficient cities.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'embrace', 'high-density', 'expansion', 'preserves', 'revitalize', 'mixed-use', 'commerce', 'containing', 'zoning laws', 'compact'. >Band 7: Advanced vocabulary. Not Band 9: Lacks idiomatic usage.",
    grammar_reason="[GRA7] Comparison: 'more sustainable than'. Participle phrase: 'combining housing...'. >Band 6: Good control. Not Band 8: Sentences are competent.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 640: V8/G7 - Topic: Technology (Communication)
samples.append(create_sample(
    index=640,
    vocab_band=8,
    grammar_band=7,
    question="Is face-to-face communication dying?",
    transcript="It is certainly under siege. Digital interfaces have become the default mode of interaction for many. We text rather than talk; we email rather than meet. This erosion of physical presence weakens our social bonds. We miss the non-verbal cues that convey true meaning. While it won't die completely, the art of conversation is atrophying. We must make a conscious effort to reclaim it.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'under siege' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'interfaces', 'default', 'erosion', 'bonds', 'convey', 'atrophying', 'conscious', 'reclaim'. Metaphor: 'under siege'. >Band 7: Strong vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA7] Comparison: 'rather than talk'. Relative clause: 'that convey true meaning'. >Band 6: Accurate grammar. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 641: V8/G7 - Topic: Environment (Plastic)
samples.append(create_sample(
    index=641,
    vocab_band=8,
    grammar_band=7,
    question="What is the solution to plastic pollution?",
    transcript="Innovation is the answer. We need to develop biodegradable alternatives that mimic the utility of plastic without the permanence. Bioplastics made from algae or starch are promising. Simultaneously, we must eliminate single-use culture. A circular economy where materials are indefinitely recycled is the goal. Cleaning up the oceans is vital, but turning off the tap of production is paramount.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'turning off the tap' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'innovation', 'biodegradable', 'mimic', 'utility', 'permanence', 'promising', 'eliminate', 'indefinitely', 'paramount'. Idiom: 'turning off the tap'. >Band 7: Precise terms. Not Band 9: Slightly formal.",
    grammar_reason="[GRA7] Relative clause: 'that mimic...'. Contrast: 'vital, but turning off...'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structure.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 642: V8/G7 - Topic: Health (Children)
samples.append(create_sample(
    index=642,
    vocab_band=8,
    grammar_band=7,
    question="Why is childhood anxiety increasing?",
    transcript="It is a multifaceted issue. Academic pressure has intensified; children are tested relentlessly. Social media exacerbates this by fostering constant comparison and cyberbullying. The world feels more unstable, with climate change and political unrest looming. Children absorb this anxiety. Furthermore, the decline of unstructured play has removed a vital coping mechanism. We have created a high-pressure environment for our youth.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'multifaceted', 'intensified', 'relentlessly', 'exacerbates', 'fostering', 'unstable', 'looming', 'absorb', 'unstructured', 'coping mechanism'. >Band 7: Very strong vocabulary. Not Band 9: Lacks flow.",
    grammar_reason="[GRA7] Reason: 'by fostering...'. Relative clause implied. >Band 6: Good control. Not Band 8: Sentences are somewhat standard.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 643: V8/G7 - Topic: Society (Wealth)
samples.append(create_sample(
    index=643,
    vocab_band=8,
    grammar_band=7,
    question="Should the rich help the poor?",
    transcript="Ethically, yes. Extreme wealth accumulation while others starve is morally indefensible. Philanthropy can address gaps in state welfare. However, charity is not a substitute for justice. Systemic inequality requires structural reform, such as progressive taxation. The wealthy benefit from societal infrastructure; therefore, they have an obligation to contribute back. It is about creating a more equitable society for everyone.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'accumulation', 'morally indefensible', 'philanthropy', 'welfare', 'systemic', 'structural reform', 'progressive taxation', 'obligation', 'equitable'. >Band 7: Advanced vocabulary. Not Band 9: Slightly academic.",
    grammar_reason="[GRA7] Contrast: 'However'. Reason: 'therefore, they have...'. >Band 6: Accurate complex sentences. Not Band 8: Limited variety.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 644: V8/G7 - Topic: Culture (Tradition)
samples.append(create_sample(
    index=644,
    vocab_band=8,
    grammar_band=7,
    question="Why do we need traditions?",
    transcript="Traditions provide an anchor in a turbulent world. They offer a sense of continuity and belonging. Participating in shared rituals strengthens communal bonds and reinforces identity. They connect us to our lineage. While blind adherence to obsolete customs is harmful, adapting traditions to modern values keeps them alive. They are the threads that weave the tapestry of culture.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'weave the tapestry' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'anchor', 'turbulent', 'continuity', 'rituals', 'communal bonds', 'reinforces', 'lineage', 'adherence', 'obsolete'. Metaphor: 'weave the tapestry'. >Band 7: Precise terms. Not Band 9: Slightly poetic.",
    grammar_reason="[GRA7] Contrast: 'While blind adherence...'. Reason: 'They offer a sense...'. >Band 6: Frequent error-free sentences. Not Band 8: Standard structure.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 645: V8/G7 - Topic: Transport (Cities)
samples.append(create_sample(
    index=645,
    vocab_band=8,
    grammar_band=7,
    question="What is the future of urban transport?",
    transcript="It will be defined by integration and automation. Mobility-as-a-Service (MaaS) will replace private ownership. We will use apps to seamlessly switch between autonomous pods, trains, and bikes. This ecosystem will be electric and data-driven, optimizing flow to eliminate congestion. The focus will shift from moving vehicles to moving people efficiently. It promises a cleaner, quieter urban environment.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'defined by', 'integration', 'automation', 'seamlessly', 'autonomous', 'ecosystem', 'data-driven', 'optimizing', 'eliminate'. >Band 7: Technical vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA7] Future forms: 'Will replace', 'Will use'. Participle phrase: 'optimizing flow'. >Band 6: Accurate grammar. Not Band 8: Sentences are competent.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 646: V8/G7 - Topic: Education (University)
samples.append(create_sample(
    index=646,
    vocab_band=8,
    grammar_band=7,
    question="Why are some degrees more popular?",
    transcript="It is driven by market forces. Degrees with a clear vocational path, like engineering or medicine, are perceived as safe bets. They offer tangible ROI (Return on Investment). Conversely, humanities are often deemed impractical. However, this utilitarian view is shortsighted. Popularity is cyclical. As AI automates technical tasks, the creative and critical skills fostered by the humanities may become the most coveted assets.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'safe bets' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'vocational', 'perceived', 'tangible', 'utilitarian', 'shortsighted', 'cyclical', 'automates', 'fostered', 'coveted'. Idiom: 'safe bets'. >Band 7: Advanced vocabulary. Not Band 9: Slightly academic.",
    grammar_reason="[GRA7] Reason: 'It is driven by...'. Contrast: 'However'. Time clause: 'As AI automates...'. >Band 6: Good control. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 647: V8/G7 - Topic: Work (Leadership)
samples.append(create_sample(
    index=647,
    vocab_band=8,
    grammar_band=7,
    question="Can anyone be a leader?",
    transcript="In theory, yes, but it requires a specific disposition. Leadership is not about authority; it is about influence. While skills like public speaking can be taught, traits like empathy, integrity, and resilience are harder to instill. Some are naturally predisposed to lead, while others flourish in support roles. True leadership is a burden that not everyone is willing or able to shoulder.",
    response_type="extended",
    micro_flaws=[],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'disposition', 'authority', 'influence', 'integrity', 'instill', 'predisposed', 'flourish', 'burden', 'shoulder'. >Band 7: Precise terms. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA7] Contrast: 'In theory, yes, but...'. Relative clause: 'that not everyone is...'. >Band 6: Accurate complex sentences. Not Band 8: Standard structures.",
    idiom_present=False,
    risk_level="medium"
))

# Sample 648: V8/G7 - Topic: Society (Media)
samples.append(create_sample(
    index=648,
    vocab_band=8,
    grammar_band=7,
    question="Is the media too negative?",
    transcript="There is a definite negativity bias. 'If it bleeds, it leads' is the industry mantra. Sensationalism grabs attention and drives ad revenue. Positive stories are often relegated to the sidelines. This constant barrage of doom and gloom distorts our perception of reality, leading to 'mean world syndrome'. While we need to be informed, the media's focus on catastrophe creates unnecessary anxiety and cynicism.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'If it bleeds, it leads' (idiom/quote)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'negativity bias', 'mantra', 'sensationalism', 'revenue', 'relegated', 'barrage', 'distorts', 'perception', 'catastrophe', 'cynicism'. Idiom: 'If it bleeds, it leads'. >Band 7: Strong vocabulary. Not Band 9: Lacks natural flow.",
    grammar_reason="[GRA7] Reason: 'because sensationlism grabs...' (implied). Contrast: 'While we need...'. >Band 6: Frequent error-free sentences. Not Band 8: Limited complexity.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 649: V8/G7 - Topic: Environment (Climate)
samples.append(create_sample(
    index=649,
    vocab_band=8,
    grammar_band=7,
    question="Why is international cooperation on climate difficult?",
    transcript="Because national interests often conflict with global necessity. Developing nations argue they need to burn fossil fuels to grow, while developed nations are reluctant to compromise their lifestyle. There is also the 'free-rider' problem; countries wait for others to act first. Trust is lacking. Achieving consensus among diverse political and economic systems is a diplomatic herculean task. Yet, isolationism is a death sentence for the planet.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'herculean task' (idiom)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'necessity', 'reluctant', 'compromise', 'free-rider', 'consensus', 'diverse', 'diplomatic', 'isolationism'. Idiom: 'herculean task'. >Band 7: Advanced vocabulary. Not Band 9: Slightly formal.",
    grammar_reason="[GRA7] Reason: 'Because national interests...'. Contrast: 'while developed nations...'. >Band 6: Accurate grammar. Not Band 8: Sentences are somewhat standard.",
    idiom_present=True,
    risk_level="medium"
))

# Sample 650: V8/G7 - Topic: Technology (Privacy)
samples.append(create_sample(
    index=650,
    vocab_band=8,
    grammar_band=7,
    question="Is privacy dead?",
    transcript="It is certainly on life support. In the digital panopticon, every click and movement is tracked. We trade privacy for convenience, often unwittingly. Surveillance is ubiquitous, from CCTV to cookies. The notion of a private life is becoming an anachronism. However, a pushback is beginning. Encryption and data protection laws are fighting to reclaim some territory. Privacy is not dead, but it is under siege.",
    response_type="extended",
    micro_flaws=[
        "phrase error: 'on life support' (metaphor)"
    ],
    grammar_profile={"complexity": "high", "accuracy": "high", "flexibility": "moderate"},
    vocab_reason="[LR8] Uses sophisticated items: 'panopticon', 'unwittingly', 'ubiquitous', 'notion', 'anachronism', 'pushback', 'encryption', 'reclaim', 'siege'. Metaphor: 'on life support'. >Band 7: Very strong vocabulary. Not Band 9: Lacks idiomatic flair.",
    grammar_reason="[GRA7] Passive: 'is tracked'. Contrast: 'However', 'but it is under siege'. >Band 6: Good control. Not Band 8: Limited variety.",
    idiom_present=True,
    risk_level="medium"
))

with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s) + '\n')

print(f"Appended {len(samples)} samples to {OUTPUT_FILE}")
