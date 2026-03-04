import json

def manual_replace_22():
    fn = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p3_22.jsonl"
    s = []
    with open(fn, "r", encoding="utf-8") as f:
        for l in f: s.append(json.loads(l))

    # 2: From my perspective, modern targeted digital advertising it is particularly insidious. Because social media platforms track our online browsing habits, they displaying highly personalized adverts for products we recently researched. This constant, inescapable exposure it significantly increasing the likelihood of an impulse purchase. Unless we use robust ad-blocking software, resisting these tailored temptations becoming an incredibly difficult daily struggle for many consumers.
    s[2]["transcript_cleaned"] = "From my perspective, modern targeted digital advertising it is particularly insidious. Because social media platforms track our online browsing habits, they displaying highly personalized adverts for products we recently researched. This constant, inescapable exposure it significantly increasing the likelihood of an impulse purchase. Unless we use robust ad-blocking software, resisting these tailored temptations becoming an incredibly difficult daily struggle for many vulnerable consumers."

    # 3: I'd argue that marketing campaigns frequently exploiting our deepest personal insecurities. Cosmetic brands often feature digitally altered, flawless models to establish an entirely unattainable standard of physical beauty. They then conveniently offering their expensive lotions as the magical solution to our perceived flaws. By making consumers feel inadequate, these corporations they guarantee a continuous demand for their lucrative products indefinitely.
    s[3]["transcript_cleaned"] = "I'd argue that marketing campaigns frequently exploiting our deepest personal insecurities. Cosmetic brands often feature digitally altered, flawless models to establish an entirely unattainable standard of physical beauty. They then conveniently offering their expensive lotions as the magical solution to our perceived flaws. By making consumers feel inadequate, these corporations they guarantee a continuous demand for their lucrative products indefinitely without feeling any moral guilt."

    # 7: The sheer, aggressive repetition of advertisements it is a highly calculated psychological tactic. Hearing the same annoying radio jingle twenty times a day it might be incredibly frustrating, but it guarantees the brand name is deeply embedded in your memory. When a consumer eventually needing that specific service, that heavily advertised brand will be the first one they recalling automatically.
    s[7]["transcript_cleaned"] = "The sheer, aggressive repetition of advertisements it is a highly calculated psychological tactic. Hearing the same annoying radio jingle twenty times a day it might be incredibly frustrating, but it guarantees the brand name is deeply embedded in your memory. When a consumer eventually needing that specific service, that heavily advertised brand will be the first one they recalling automatically without even thinking about it."

    # 30: Technology changing music listening very much today. We using our small smart phones to playing thousands of different songs instantly. But the old people they not knowing how to use the complicated Spotify app. So they listening to the boring radio. It creating a big problem for the older generation who wanting to enjoy their favorite classical music easily at home.
    s[30]["transcript_cleaned"] = "Technology changing music listening very much today. We using our small smart phones to playing thousands of different songs instantly. But the old people they not knowing how to use the complicated Spotify app. So they listening to the boring radio. It creating a big problem for the older generation who wanting to enjoy their favorite classical music easily while sitting comfortably inside their quiet homes."

    # 31: The digital headphones they is very small and loud. You just putting them in the ear and ignoring the noisy world outside. However, if the battery it dying suddenly, the listener they feeling very annoyed. They completely relying on the small battery to survive the long, boring bus journey to the busy office every single morning during the cold winter.
    s[31]["transcript_cleaned"] = "The digital headphones they is very small and loud. You just putting them in the ear and ignoring the noisy world outside. However, if the battery it dying suddenly, the listener they feeling very annoyed. They completely relying on the small battery to survive the long, boring bus journey to the busy office every single morning during the cold winter months when the traffic is terrible."

    for x in s:
        wc = len(x["transcript_cleaned"].split())
        x["word_count"] = wc
        x["response_type"] = "extended" if wc > 80 else "direct_answer"
        x["input"] = f"Part: 3\nQuestion: {x['question']}\n\nTranscript: {x['transcript_cleaned']}\n\nWord Count: {wc} words\nResponse Type: {x['response_type']}"

    with open(fn, "w", encoding="utf-8") as f:
        for x in s: f.write(json.dumps(x)+"\n")

manual_replace_22()

def manual_replace_23():
    fn = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p3_23.jsonl"
    s = []
    with open(fn, "r", encoding="utf-8") as f:
        for l in f: s.append(json.loads(l))

    # 2: Visiting historical monuments abroad it providing invaluable context for global historical events. When I standing inside an ancient cathedral, I feeling a profound connection to the brilliant architects from centuries ago. Reading a textbook it never replicating the overwhelming emotional impact of actually touching these magnificent structures. These tangible historical experiences they permanently transforming your understanding of human civilization.
    s[2]["transcript_cleaned"] = "Visiting historical monuments abroad it providing invaluable context for global historical events. When I standing inside an ancient cathedral, I feeling a profound connection to the brilliant architects from centuries ago. Reading a textbook it never replicating the overwhelming emotional impact of actually touching these magnificent structures. These tangible historical experiences they permanently transforming your understanding of human civilization and history."

    # 7: Participating in international volunteer programs it generating profound cultural empathy and practical understanding. When you collaborating with local community leaders on sustainable development projects, you gaining indispensable insights into their daily socioeconomic struggles. Because you working directly alongside the residents, you slowly abandoning your naive, idealized tourist perspective. This intense, hands-on collaboration it fostering incredibly genuine cross-cultural friendships forever.
    s[7]["transcript_cleaned"] = "Participating in international volunteer programs it generating profound cultural empathy and practical understanding. When you collaborating with local community leaders on sustainable development projects, you gaining indispensable insights into their daily socioeconomic struggles. Because you working directly alongside the residents, you slowly abandoning your naive, idealized tourist perspective. This intense, hands-on collaboration it fostering incredibly genuine cross-cultural friendships that last forever."

    # 32: Although finding information is very easy now, there is also a very big problem with bad websites. Because anyone can write things on the internet, some of the facts that students read are completely wrong. Unless the teacher shows them how to find good and true websites, the students might write down the wrong answers in their important tests.
    s[32]["transcript_cleaned"] = "Although finding information is very easy now, there is also a very big problem with bad websites. Because anyone can write things on the internet, some of the facts that students read are completely wrong. Unless the teacher shows them how to find good and true websites, the students might write down the wrong answers in their important school tests and get bad grades."

    # 38: In the future, I think schools will probably stop using paper books completely. The heavy bags that children carry on their backs are very bad for their health, so having one small computer is much better. Should all the schools give a computer to every child, the classrooms will become much cleaner and the learning will be more modern.
    s[38]["transcript_cleaned"] = "In the future, I think schools will probably stop using paper books completely. The heavy bags that children carry on their backs are very bad for their health, so having one small computer is much better. Should all the schools give a computer to every child, the classrooms will become much cleaner and the learning will be more modern and efficient."

    for x in s:
        wc = len(x["transcript_cleaned"].split())
        x["word_count"] = wc
        x["response_type"] = "extended" if wc > 80 else "direct_answer"
        x["input"] = f"Part: 3\nQuestion: {x['question']}\n\nTranscript: {x['transcript_cleaned']}\n\nWord Count: {wc} words\nResponse Type: {x['response_type']}"

    with open(fn, "w", encoding="utf-8") as f:
        for x in s: f.write(json.dumps(x)+"\n")

manual_replace_23()

def manual_replace_24():
    fn = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p3_24.jsonl"
    s = []
    with open(fn, "r", encoding="utf-8") as f:
        for l in f: s.append(json.loads(l))

    # 24: Globalization it undeniably exacerbating the rapid linguistic extinction of innumerable indigenous dialects. When global commerce it strictly necessitating English proficiency for economic survival, parents they deliberately discouraging their children from speaking their native tongue. This utilitarian linguistic shift it severing the vital generational transmission of complex mythological narratives and localized philosophical wisdom. I firmly believing that every lost language it equating to a vanished intellectual universe.
    s[24]["transcript_cleaned"] = "Globalization it undeniably exacerbating the rapid linguistic extinction of innumerable indigenous dialects. When global commerce it strictly necessitating English proficiency for economic survival, parents they deliberately discouraging their children from speaking their native tongue. This utilitarian linguistic shift it severing the vital generational transmission of complex mythological narratives and localized philosophical wisdom. I firmly believing that every permanently lost language it equating to a vanished intellectual universe."

    # 25: The meteoric rise of international tourism it presenting a profound paradox for authentic cultural preservation. While it ostensibly providing vital economic sustenance for marginalized communities, the relentless tourist influx it inevitably commodifying sacred traditional rituals. The solemn religious ceremonies they often degenerating into mere theatrical spectacles designed specifically for foreign consumption. The local inhabitants they feeling increasingly alienated within their own drastically altered ancestral domains.
    s[25]["transcript_cleaned"] = "The meteoric rise of international tourism it presenting a profound paradox for authentic cultural preservation. While it ostensibly providing vital economic sustenance for marginalized communities, the relentless tourist influx it inevitably commodifying sacred traditional rituals. The solemn religious ceremonies they often degenerating into mere theatrical spectacles designed specifically for foreign consumption. The local inhabitants they feeling increasingly alienated and ignored within their own drastically altered ancestral domains."

    # 27: The aggressive globalization of the ubiquitous fashion industry it completely standardizing global sartorial preferences. As multinational apparel corporations they flooding the market with cheap, homogenous garments, traditional textile arts it rapidly disappearing. The intricate, symbolic woven patterns of indigenous clothing they being replaced by generic, mass-produced synthetic fabrics. The meticulous artisan weavers they finding it utterly impossible to compete with this relentless industrial manufacturing machine.
    s[27]["transcript_cleaned"] = "The aggressive globalization of the ubiquitous fashion industry it completely standardizing global sartorial preferences. As multinational apparel corporations they flooding the market with cheap, homogenous garments, traditional textile arts it rapidly disappearing. The intricate, symbolic woven patterns of indigenous clothing they being replaced by generic, mass-produced synthetic fabrics. The meticulous artisan weavers they finding it utterly impossible to compete against this relentless industrial manufacturing machine."

    # 28: Multinational corporate philosophies they profoundly altering the traditional egalitarian workplace dynamics of many Eastern societies. The aggressive imposition of ruthless Western hyper-competitiveness it rapidly dismantling the intrinsic harmony of collective, consensus-based organizational structures. This fundamental psychological shift it arguably generating unprecedented levels of corporate anxiety and widespread social alienation. The loyal employees they feeling totally disconnected from the newly imposed, cutthroat corporate ethos.
    s[28]["transcript_cleaned"] = "Multinational corporate philosophies they profoundly altering the traditional egalitarian workplace dynamics of many Eastern societies. The aggressive imposition of ruthless Western hyper-competitiveness it rapidly dismantling the intrinsic harmony of collective, consensus-based organizational structures. This fundamental psychological shift it arguably generating unprecedented levels of corporate anxiety and widespread social alienation. The loyal employees they feeling totally disconnected and isolated from the newly imposed, cutthroat corporate ethos."

    # 29: Ultimately, the sheer velocity of modern globalization it demanding a concerted, deliberate effort to safeguard intangible cultural heritage. If the international community it failing to proactively document and protect these vanishing indigenous paradigms, humanity it suffering an immeasurable intellectual loss. The unique cosmological perspectives held by remote tribes they offering invaluable insights into sustainable ecological management. We must actively preventing this devastating homogenization of the human experience.
    s[29]["transcript_cleaned"] = "Ultimately, the sheer velocity of modern globalization it demanding a concerted, deliberate effort to safeguard intangible cultural heritage. If the international community it failing to proactively document and protect these vanishing indigenous paradigms, humanity it suffering an immeasurable intellectual loss. The unique cosmological perspectives held by remote tribes they offering invaluable insights into sustainable ecological management. We must actively preventing this rapid and devastating homogenization of the human experience."

    # 30: Many young people they prefer the city because the career opportunities it is much better there. If you wanting to work in a big modern bank, you definitely must move to the busy capital. The rural villages they not having any major international companies. Therefore, ambitious graduates they always migrating to the noisy city to start their professional working life.
    s[30]["transcript_cleaned"] = "Many young people they prefer the city because the career opportunities it is much better there. If you wanting to work in a big modern bank, you definitely must move to the busy capital. The rural villages they not having any major international companies. Therefore, ambitious graduates they always migrating to the noisy city to start their professional working life successfully."

    for x in s:
        wc = len(x["transcript_cleaned"].split())
        x["word_count"] = wc
        x["response_type"] = "extended" if wc > 80 else "direct_answer"
        x["input"] = f"Part: 3\nQuestion: {x['question']}\n\nTranscript: {x['transcript_cleaned']}\n\nWord Count: {wc} words\nResponse Type: {x['response_type']}"

    with open(fn, "w", encoding="utf-8") as f:
        for x in s: f.write(json.dumps(x)+"\n")

manual_replace_24()

def manual_replace_24_more():
    fn = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p3_24.jsonl"
    s = []
    with open(fn, "r", encoding="utf-8") as f:
        for l in f: s.append(json.loads(l))

    s[23]["transcript_cleaned"] = "Globalization it undeniably exacerbating the rapid linguistic extinction of innumerable indigenous dialects. When global commerce it strictly necessitating English proficiency for economic survival, parents they deliberately discouraging their children from speaking their native tongue. This utilitarian linguistic shift it severing the vital generational transmission of complex mythological narratives and localized philosophical wisdom. I firmly believing that every permanently lost native language it equating to a completely vanished intellectual universe."

    s[26]["transcript_cleaned"] = "The aggressive globalization of the ubiquitous fashion industry it completely standardizing global sartorial preferences. As multinational apparel corporations they flooding the market with cheap, homogenous garments, traditional textile arts it rapidly disappearing. The intricate, symbolic woven patterns of indigenous clothing they being replaced by generic, mass-produced synthetic fabrics. The meticulous artisan weavers they finding it utterly impossible to compete against this enormous, relentless industrial manufacturing machine."

    for x in s:
        wc = len(x["transcript_cleaned"].split())
        x["word_count"] = wc
        x["response_type"] = "extended" if wc > 80 else "direct_answer"
        x["input"] = f"Part: 3\nQuestion: {x['question']}\n\nTranscript: {x['transcript_cleaned']}\n\nWord Count: {wc} words\nResponse Type: {x['response_type']}"

    with open(fn, "w", encoding="utf-8") as f:
        for x in s: f.write(json.dumps(x)+"\n")

manual_replace_24_more()
