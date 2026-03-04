import json

def fix_batch(num, fn):
    samples = []
    with open(fn, "r", encoding="utf-8") as f:
        for line in f:
            samples.append(json.loads(line))

    # Remove ANY programmatic padding that might have been added
    # The padding was:
    pad1 = " I really believe that this is true for every normal workplace in the whole world today."
    pad2 = " I personally observing this ongoing global phenomenon over the past several decades with great interest."
    pad3 = " This represents a very interesting aspect of modern society."

    for s in samples:
        t = s["transcript_cleaned"]
        if t.endswith(pad1): t = t.replace(pad1, "")
        if t.endswith(pad2): t = t.replace(pad2, "")
        if t.endswith(pad3): t = t.replace(pad3, "")
        s["transcript_cleaned"] = t
        s["word_count"] = len(t.split())

    # Now I will MANUALLY replace the short transcripts with longer, authentic, non-repetitive paragraphs entirely.
    if num == 54:
        # V6/G4 (Indices 30-39)
        # Check lengths
        for i in range(50):
            if samples[i]["word_count"] < 60:
                print(f"Batch 54 short at {i}: {samples[i]['word_count']}")

        # L34 (idx 33): People they not buying physical CD albums anymore...
        samples[33]["transcript_cleaned"] = "People they not buying physical CD albums anymore. They paying a small monthly fee to streaming all the music in the world. Because the plastic CD it becoming old and useless very fast. But the internet connection it sometimes failing during bad weather. Then the music stopping completely and you sitting in the quiet room feeling very frustrated and angry. The digital format it simply not providing a completely reliable listening experience."

        # L35 (idx 34): The new wireless speakers...
        samples[34]["transcript_cleaned"] = "The new wireless speakers they playing music incredibly loud in the house. This advanced technology it saving a lot of space in the small living room. But playing the heavy bass music it annoying the angry neighbors next door. The loud sound it causing a very terrible argument between the people living in the same apartment building. Eventually, the local police they arriving to stop the disturbing noise late at night."

        # L36 (idx 35): Artificial intelligence it will completely changing...
        samples[35]["transcript_cleaned"] = "Artificial intelligence it will completely changing how we find new music. The smart computer it analyzing your favorite songs and suggesting perfect new bands for you. However, many music fans they not trusting the invisible machine algorithm. They fearing that the computer it will making them listen to bad commercial pop music instead of authentic underground rock. They preferring the personal recommendations from their close human friends."

        # L37 (idx 36): The digital music files...
        samples[36]["transcript_cleaned"] = "The digital music files they destroying the traditional record shop business completely. Because the phone download it is much cheaper and faster, everyone choosing to use it. The poor shop owners they losing their important jobs and closing their doors forever. The government they struggling to help these small local businesses survive this rapidly changing situation. It creating a massive economic crisis for the independent music retail sector."

        # L38 (idx 37): Smart watches it allowing runners...
        samples[37]["transcript_cleaned"] = "Smart watches it allowing runners to listen to music without carrying a heavy phone. You just tapping your wrist and the fast running song starting immediately. It is a very easy and light way to exercising in the public park. But it never replacing the actual feeling of reading the beautiful paper booklet inside a real vinyl record cover. The physical connection to the album art it completely disappearing."

        # L39 (idx 38): Modern concerts they using advanced digital screens...
        samples[38]["transcript_cleaned"] = "Modern concerts they using advanced digital screens and lasers to entertain the massive crowd. You just looking at the bright stage and dancing to the perfect electronic sound. This modern technology it making the live show very spectacular. But many purists they arguing that the musicians using too much computer help instead of playing real physical instruments. The live performance it losing its raw, authentic musical soul."

        # Any others? I'll just check length again after replacing.

    elif num == 55:
        # Check lengths
        for i in range(50):
            if samples[i]["word_count"] < 60:
                print(f"Batch 55 short at {i}: {samples[i]['word_count']}")

        # idx 3, 4, 8, 33, 39
        # idx 3 (V7/G5): Engaging in meaningful conversations... (59 words)
        samples[3]["transcript_cleaned"] = "Engaging in meaningful conversations with foreign residents it breaking down artificial linguistic barriers. Even if you struggling with the basic vocabulary, the genuine effort to communicate it demonstrating profound respect for their culture. The hospitable locals I meeting usually appreciating this sincere attempt to integrate. This mutual linguistic exchange it building vital bridges of international empathy and tolerance. Over time, these brief interactions they completely reshaping your worldview."

        # idx 4 (V7/G5): Attending authentic traditional festivals... (58)
        samples[4]["transcript_cleaned"] = "Attending authentic traditional festivals it offering a spectacular window into the local collective consciousness. The vibrant costumes and rhythmic ceremonial dances they symbolizing deeply rooted spiritual beliefs and historical triumphs. When I participating in a remarkable local harvest festival, I feeling totally overwhelmed by their unified community spirit. These incredibly dynamic cultural celebrations they uniting diverse populations through shared human joy. The profound emotional resonance of these events it lingering indefinitely."

        # idx 8 (V7/G5): The sheer necessity of adapting... (58)
        samples[8]["transcript_cleaned"] = "The sheer necessity of adapting to different social etiquette it challenging your ingrained behavioral norms. For example, understanding the subtle nuances of formal greetings it preventing embarrassing cultural misunderstandings. If a traveler completely ignoring these vital social conventions, they inadvertently causing deep offense to their gracious hosts. Learning and respecting these intricate customs it demonstrating a sophisticated level of cultural intelligence. Such conscientious behavior it absolutely guaranteeing a welcoming reception abroad."

        # idx 33 (V5/G8): The way we talk to other students has also changed a lot... (59)
        samples[33]["transcript_cleaned"] = "The way we talk to other students has also changed a lot because of the internet. When a group of friends needs to do a big project together, they no longer need to sit in the same room. By using video calls, they can easily talk and share their work from their own bedrooms, which saves a lot of time and travel money. This convenient digital collaboration is incredibly efficient for academic studies."

        # idx 39 (V5/G8): Ultimately, the internet has made the whole world feel like one giant classroom... (59)
        samples[39]["transcript_cleaned"] = "Ultimately, the internet has made the whole world feel like one giant classroom. No matter where you live, you can find out what is happening in a different country right now. By reading the news online every morning, students become much smarter about the world, which is just as important as the things they learn in their normal school classes. This constant stream of global information creates a deeply informed younger generation."

    elif num == 56:
        for i in range(50):
            if samples[i]["word_count"] < 60:
                print(f"Batch 56 short at {i}: {samples[i]['word_count']}")

    # Update word counts and fields
    for s in samples:
        wc = len(s["transcript_cleaned"].split())
        s["word_count"] = wc
        s["response_type"] = "extended" if wc > 80 else "direct_answer"
        s["input"] = f"Part: 3\nQuestion: {s['question']}\n\nTranscript: {s['transcript_cleaned']}\n\nWord Count: {wc} words\nResponse Type: {s['response_type']}"

    with open(fn, "w", encoding="utf-8") as f:
        for s in samples:
            f.write(json.dumps(s) + "\n")

fix_batch(54, "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p3_22.jsonl")
fix_batch(55, "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p3_23.jsonl")
fix_batch(56, "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p3_24.jsonl")
