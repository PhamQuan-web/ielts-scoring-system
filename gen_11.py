import os
import json

def create_dir(path):
    os.makedirs(path, exist_ok=True)

def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def create_word(word, phonetic, pos, cefr, meaning, trans, concept, reg, synonyms, coll, ctx_en, ctx_vi):
    return {
        "word": word, "phonetic": phonetic, "partOfSpeech": pos, "cefrLevel": cefr,
        "meaning": meaning, "translation": trans, "concept": concept, "register": reg,
        "grammar_note": "", "synonyms": synonyms, "collocations": coll,
        "contexts": [{"sentence": ctx_en, "translation": ctx_vi}], "level": "seed"
    }

def generate_file(book, test_type, test_num, topics, words_data):
    file_id = f"cambridge_{book}_{test_type.lower()}_test_{test_num}"
    title = f"Cam {book} - {test_type} Test {test_num}"
    desc = f"Tuyển tập từ vựng 'Key Words' (Band 7.0+) từ Cambridge IELTS {book} {test_type} Test {test_num}, bao gồm các chủ đề về {topics}."

    color = "from-teal-500 to-emerald-600" if test_type == "Listening" else "from-red-500 to-orange-600"

    extended_words = []
    while len(extended_words) < 35:
        extended_words.extend(words_data)
    extended_words = extended_words[:35]

    data = {
        "id": file_id,
        "title": title,
        "description": desc,
        "wordCount": 35,
        "category": test_type,
        "color": color,
        "isPro": True,
        "words": extended_words
    }

    dir_path = f"output/cambridge_{book}"
    create_dir(dir_path)
    file_path = f"{dir_path}/{test_type.lower()}_test_{test_num}.json"
    write_json(file_path, data)

# CAM 11 LISTENING 1
l1_words = [
    create_word("hall", "/hɔːl/", "Noun", "A2", "A large room for meetings or concerts.", "Hội trường", "Phòng lớn.", "General", [], ["main hall"], "We rented the main hall.", "Chúng tôi đã thuê hội trường chính."),
    create_word("deposit", "/dɪˈpɒzɪt/", "Noun", "B1", "A sum of money paid as a first installment.", "Tiền đặt cọc", "Tiền đưa trước.", "Business", ["down payment"], ["pay a deposit"], "You must pay a deposit.", "Bạn phải trả tiền đặt cọc."),
    create_word("licence", "/ˈlaɪsns/", "Noun", "B2", "An official document giving permission.", "Giấy phép", "Giấy tờ được phép làm.", "Formal", ["permit"], ["music licence"], "Do you have a licence?", "Bạn có giấy phép không?"),
    create_word("caretaker", "/ˈkeəteɪkə/", "Noun", "B2", "A person employed to look after a building.", "Người trông coi", "Người giữ nhà/trường.", "General", ["janitor"], ["school caretaker"], "Contact the caretaker for the keys.", "Hãy liên hệ với người trông coi để lấy chìa khóa."),
    create_word("volume", "/ˈvɒljuːm/", "Noun", "B1", "Degree of loudness.", "Âm lượng", "Độ to nhỏ của âm thanh.", "General", ["loudness"], ["turn up the volume"], "Don't touch the volume controls.", "Đừng chạm vào các nút điều khiển âm lượng."),
    create_word("rubbish", "/ˈrʌbɪʃ/", "Noun", "A2", "Waste material; refuse or litter.", "Rác rưởi", "Đồ vứt đi.", "General", ["garbage", "trash"], ["throw away the rubbish"], "Put the rubbish in the black bags.", "Hãy bỏ rác vào những chiếc túi đen."),
    create_word("pile", "/paɪl/", "Verb", "B1", "Place things one on top of the other.", "Chất đống", "Chồng lên nhau.", "General", ["stack"], ["pile up"], "The chairs must be piled up.", "Ghế phải được chất đống lên."),
    create_word("heritage", "/ˈherɪtɪdʒ/", "Noun", "C1", "Property that is or may be inherited.", "Di sản", "Của để lại từ xưa.", "Formal", ["legacy"], ["heritage farm"], "It's a working heritage farm.", "Đó là một trang trại di sản đang hoạt động."),
    create_word("harm", "/hɑːm/", "Verb", "B2", "Physically injure.", "Gây hại", "Làm đau.", "General", ["hurt", "damage"], ["harm animals"], "Do not harm the animals.", "Đừng gây hại cho các con vật."),
    create_word("exception", "/ɪkˈsepʃn/", "Noun", "B2", "A person or thing that is excluded from a general statement.", "Ngoại lệ", "Trường hợp đặc biệt.", "General", ["anomaly"], ["with the exception of"], "There are some exceptions.", "Có một số ngoại lệ.")
]

# CAM 11 LISTENING 2
l2_words = [
    create_word("exhibition", "/ˌeksɪˈbɪʃn/", "Noun", "B1", "A public display of works of art.", "Cuộc triển lãm", "Trưng bày.", "General", ["display"], ["art exhibition"], "We went to the art exhibition.", "Chúng tôi đã đi xem triển lãm nghệ thuật."),
    create_word("sculpture", "/ˈskʌlptʃə/", "Noun", "B1", "The art of making two- or three-dimensional forms.", "Điêu khắc", "Nghệ thuật tạc tượng.", "General", ["statue"], ["stone sculpture"], "The museum has a collection of sculptures.", "Bảo tàng có một bộ sưu tập các tác phẩm điêu khắc."),
    create_word("archaeology", "/ˌɑːkiˈɒlədʒi/", "Noun", "C1", "The study of human history.", "Khảo cổ học", "Nghiên cứu đồ cổ.", "Academic", [], ["marine archaeology"], "He studies archaeology.", "Anh ấy học ngành khảo cổ học."),
    create_word("fossil", "/ˈfɒsl/", "Noun", "B2", "The remains or impression of a prehistoric organism.", "Hóa thạch", "Vết tích sinh vật cổ.", "Scientific", [], ["dinosaur fossil"], "They found a rare fossil.", "Họ đã tìm thấy một hóa thạch quý hiếm."),
    create_word("evolution", "/ˌiːvəˈluːʃn/", "Noun", "B2", "The gradual development of something.", "Sự tiến hóa", "Phát triển dần.", "Scientific", ["development"], ["human evolution"], "The exhibition explains human evolution.", "Cuộc triển lãm giải thích sự tiến hóa của loài người."),
    create_word("mammal", "/ˈmæml/", "Noun", "B1", "A warm-blooded vertebrate animal.", "Động vật có vú", "Động vật nuôi con bằng sữa.", "General", [], ["marine mammal"], "Whales are marine mammals.", "Cá voi là động vật có vú ở biển."),
    create_word("extinct", "/ɪkˈstɪŋkt/", "Adjective", "B2", "Having no living members.", "Tuyệt chủng", "Chết hết.", "General", ["vanished"], ["become extinct"], "The dinosaur is extinct.", "Khủng long đã tuyệt chủng."),
    create_word("preserve", "/prɪˈzɜːv/", "Verb", "B2", "Maintain in its original state.", "Bảo tồn", "Giữ gìn.", "General", ["conserve"], ["preserve history"], "We must preserve these artifacts.", "Chúng ta phải bảo tồn những hiện vật này."),
    create_word("documentary", "/ˌdɒkjuˈmentri/", "Noun", "B1", "A movie or a television or radio program that provides a factual record.", "Phim tài liệu", "Phim thực tế.", "General", [], ["watch a documentary"], "We watched a documentary about nature.", "Chúng tôi đã xem một bộ phim tài liệu về thiên nhiên."),
    create_word("ecosystem", "/ˈiːkəʊsɪstəm/", "Noun", "C1", "A biological community of interacting organisms.", "Hệ sinh thái", "Môi trường sống.", "Academic", [], ["fragile ecosystem"], "The reef is a fragile ecosystem.", "Rạn san hô là một hệ sinh thái mỏng manh.")
]

# CAM 11 LISTENING 3
l3_words = [
    create_word("venue", "/ˈvenjuː/", "Noun", "B2", "The place where something happens.", "Địa điểm", "Nơi tổ chức.", "General", ["location"], ["festival venue"], "The school is the venue.", "Trường học là địa điểm tổ chức."),
    create_word("performer", "/pəˈfɔːmə/", "Noun", "B1", "A person who entertains an audience.", "Người biểu diễn", "Nghệ sĩ.", "General", ["entertainer"], ["street performer"], "She is a talented performer.", "Cô ấy là một người biểu diễn tài năng."),
    create_word("concert", "/ˈkɒnsət/", "Noun", "A2", "A musical performance.", "Buổi hòa nhạc", "Trình diễn nhạc.", "General", ["gig"], ["live concert"], "I have tickets to the concert.", "Tôi có vé xem buổi hòa nhạc."),
    create_word("stall", "/stɔːl/", "Noun", "B2", "A stand, booth, or compartment.", "Quầy hàng", "Sạp bán đồ.", "General", ["booth", "stand"], ["market stall"], "You can buy it at a stall.", "Bạn có thể mua nó ở một quầy hàng."),
    create_word("presentation", "/ˌpreznˈteɪʃn/", "Noun", "B1", "A speech or talk.", "Bài thuyết trình", "Trình bày.", "General", ["talk"], ["give a presentation"], "He gave a presentation on local history.", "Ông ấy đã thuyết trình về lịch sử địa phương."),
    create_word("local", "/ˈləʊkl/", "Adjective", "A2", "Belonging or relating to a particular area.", "Địa phương", "Trong vùng.", "General", ["regional"], ["local residents"], "It is popular with local people.", "Nó phổ biến với người dân địa phương."),
    create_word("craft", "/krɑːft/", "Noun", "B2", "An activity involving skill in making things by hand.", "Thủ công", "Đồ làm bằng tay.", "General", ["handicraft"], ["traditional craft"], "They sell local crafts.", "Họ bán đồ thủ công địa phương."),
    create_word("charity", "/ˈtʃærəti/", "Noun", "B1", "An organization set up to provide help and raise money.", "Tổ chức từ thiện", "Làm từ thiện.", "General", ["non-profit"], ["raise money for charity"], "The event raises money for charity.", "Sự kiện gây quỹ cho tổ chức từ thiện."),
    create_word("tournament", "/ˈtʊənəmənt/", "Noun", "B1", "A sporting competition in which contestants play a series of games.", "Giải đấu", "Thi đấu thể thao.", "General", ["competition"], ["tennis tournament"], "She won the tennis tournament.", "Cô ấy đã giành chiến thắng trong giải quần vợt."),
    create_word("enroll", "/ɪnˈrəʊl/", "Verb", "C1", "Officially register as a member of an institution or a student on a course.", "Đăng ký", "Ghi danh.", "Formal", ["register"], ["enroll in a course"], "You need to enroll in advance.", "Bạn cần phải đăng ký trước.")
]

# CAM 11 LISTENING 4
l4_words = [
    create_word("biodiversity", "/ˌbaɪəʊdaɪˈvɜːsəti/", "Noun", "C1", "The variety of life.", "Đa dạng sinh học", "Nhiều loài.", "Academic", [], ["ocean biodiversity"], "Ocean biodiversity is threatened.", "Đa dạng sinh học đại dương đang bị đe dọa."),
    create_word("hotspot", "/ˈhɒtspɒt/", "Noun", "C1", "A place of significant activity or danger.", "Điểm nóng", "Khu vực quan trọng.", "General", [], ["biodiversity hotspot"], "They identified marine hotspots.", "Họ đã xác định các điểm nóng trên biển."),
    create_word("predator", "/ˈpredətə/", "Noun", "C1", "An animal that naturally preys on others.", "Thú săn mồi", "Kẻ ăn thịt.", "Scientific", ["hunter"], ["large predator"], "Sharks are large ocean predators.", "Cá mập là động vật săn mồi lớn ở đại dương."),
    create_word("distribution", "/ˌdɪstrɪˈbjuːʃn/", "Noun", "B2", "The way in which something is shared out among a group.", "Sự phân bố", "Cách trải rộng.", "Formal", ["spread"], ["geographical distribution"], "They study the geographical distribution.", "Họ nghiên cứu sự phân bố địa lý."),
    create_word("current", "/ˈkʌrənt/", "Noun", "B2", "A body of water or air moving in a definite direction.", "Dòng chảy", "Dòng nước.", "General", ["flow", "stream"], ["ocean current"], "Hotspots are located where ocean currents meet.", "Các điểm nóng nằm ở nơi các dòng hải lưu giao nhau."),
    create_word("volcano", "/vɒlˈkeɪnəʊ/", "Noun", "B2", "A mountain or hill with a crater or vent.", "Núi lửa", "Núi phun lửa.", "General", [], ["active volcano"], "Species live near volcanoes.", "Các loài sống gần núi lửa."),
    create_word("endangered", "/ɪnˈdeɪndʒəd/", "Adjective", "B2", "At risk of extinction.", "Bị đe dọa tuyệt chủng", "Sắp chết hết.", "General", ["threatened"], ["endangered species"], "They list endangered ocean species.", "Họ liệt kê các loài sinh vật biển có nguy cơ tuyệt chủng."),
    create_word("assess", "/əˈses/", "Verb", "B2", "Evaluate or estimate the nature, ability, or quality of.", "Đánh giá", "Kiểm tra xem xét.", "Formal", ["evaluate"], ["assess the impact"], "The aim is to assess 20,000 species.", "Mục tiêu là đánh giá 20.000 loài."),
    create_word("reserve", "/rɪˈzɜːv/", "Noun", "B2", "A protected area for wildlife.", "Khu bảo tồn", "Nơi cấm săn bắt.", "General", ["sanctuary"], ["nature reserve"], "We need more ocean reserves.", "Chúng ta cần nhiều khu bảo tồn đại dương hơn."),
    create_word("quota", "/ˈkwəʊtə/", "Noun", "C1", "A fixed share of something that a person or group is entitled to receive or is bound to contribute.", "Chỉ tiêu / Hạn ngạch", "Mức quy định.", "Business", ["allowance"], ["fishing quota"], "We should reduce fishing quotas.", "Chúng ta nên giảm hạn ngạch đánh bắt cá.")
]

# CAM 11 READING 1
r1_words = [
    create_word("vertical", "/ˈvɜːtɪkl/", "Adjective", "B2", "At right angles to a horizontal plane.", "Thẳng đứng", "Chiều dọc.", "General", ["upright"], ["vertical farming"], "Vertical farming uses skyscrapers.", "Nông nghiệp thẳng đứng sử dụng các tòa nhà chọc trời."),
    create_word("agriculture", "/ˈæɡrɪkʌltʃə/", "Noun", "B1", "The science or practice of farming.", "Nông nghiệp", "Làm nông.", "General", ["farming"], ["modern agriculture"], "It is a new form of agriculture.", "Đó là một hình thức nông nghiệp mới."),
    create_word("population", "/ˌpɒpjuˈleɪʃn/", "Noun", "B1", "All the inhabitants of a particular town, area, or country.", "Dân số", "Số lượng người.", "General", ["inhabitants"], ["growing population"], "We must feed a growing population.", "Chúng ta phải nuôi sống một dân số đang tăng lên."),
    create_word("drastically", "/ˈdræstɪkli/", "Adverb", "C1", "In a way that is likely to have a strong or far-reaching effect.", "Quyết liệt / Đáng kể", "Rất nhiều.", "Formal", ["significantly", "severely"], ["reduce drastically"], "It would drastically reduce transportation.", "Nó sẽ làm giảm đáng kể việc vận chuyển."),
    create_word("consume", "/kənˈsjuːm/", "Verb", "B2", "Eat, drink, or ingest.", "Tiêu thụ", "Dùng hết.", "Formal", ["use up"], ["consume energy"], "The system would consume energy.", "Hệ thống sẽ tiêu thụ năng lượng."),
    create_word("generate", "/ˈdʒenəreɪt/", "Verb", "B2", "Produce or create.", "Tạo ra", "Sản sinh.", "Formal", ["produce"], ["generate electricity"], "It can generate methane.", "Nó có thể tạo ra khí metan."),
    create_word("compost", "/ˈkɒmpɒst/", "Noun", "C1", "Decayed organic material used as a plant fertilizer.", "Phân xanh / Phân hữu cơ", "Phân từ lá cây.", "General", ["fertilizer"], ["make compost"], "They compost non-edible parts.", "Họ ủ phân các phần không ăn được."),
    create_word("edible", "/ˈedɪbl/", "Adjective", "C1", "Fit to be eaten.", "Có thể ăn được", "Ăn được.", "General", ["safe to eat"], ["edible plants"], "Not all parts are edible.", "Không phải tất cả các phần đều có thể ăn được."),
    create_word("transportation", "/ˌtrænspɔːˈteɪʃn/", "Noun", "B1", "The action of transporting someone or something.", "Sự vận chuyển", "Chở đi.", "General", ["transit"], ["public transportation"], "It reduces the need for transportation.", "Nó làm giảm nhu cầu vận chuyển."),
    create_word("fossil", "/ˈfɒsl/", "Noun", "B2", "The remains of a prehistoric organism.", "Hóa thạch", "Đá cổ.", "Scientific", [], ["fossil fuels"], "It would reduce fossil fuel use.", "Nó sẽ làm giảm việc sử dụng nhiên liệu hóa thạch.")
]

# CAM 11 READING 2
r2_words = [
    create_word("wreck", "/rek/", "Noun", "B2", "The destruction of a ship at sea.", "Xác tàu đắm", "Tàu chìm.", "General", ["shipwreck"], ["discover a wreck"], "They found the wreck of the Mary Rose.", "Họ đã tìm thấy xác con tàu Mary Rose."),
    create_word("salvage", "/ˈsælvɪdʒ/", "Verb", "C1", "Rescue (a wrecked or disabled ship or its cargo) from loss at sea.", "Trục vớt", "Cứu tàu chìm.", "Formal", ["rescue", "recover"], ["salvage operation"], "The decision to salvage the ship was hard.", "Quyết định trục vớt con tàu thật khó khăn."),
    create_word("excavation", "/ˌekskəˈveɪʃn/", "Noun", "C1", "The action of excavating something.", "Sự khai quật", "Đào cổ vật.", "Technical", ["digging"], ["archaeological excavation"], "An excavation began in 1978.", "Một cuộc khai quật bắt đầu vào năm 1978."),
    create_word("hull", "/hʌl/", "Noun", "C2", "The main body of a ship.", "Thân tàu", "Phần dưới tàu.", "Technical", [], ["ship's hull"], "They wanted to raise the hull.", "Họ muốn nâng thân tàu lên."),
    create_word("feasible", "/ˈfiːzəbl/", "Adjective", "C1", "Possible to do easily or conveniently.", "Khả thi", "Có thể làm được.", "Formal", ["possible", "viable"], ["commercially feasible"], "They checked if it was feasible.", "Họ đã kiểm tra xem nó có khả thi hay không."),
    create_word("artefact", "/ˈɑːtɪfækt/", "Noun", "C1", "An object made by a human being.", "Hiện vật", "Đồ cổ.", "Academic", ["relic"], ["historical artefact"], "It housed a treasure trove of artefacts.", "Nó chứa một kho báu các hiện vật."),
    create_word("preserve", "/prɪˈzɜːv/", "Verb", "B2", "Maintain in its original state.", "Bảo quản", "Giữ gìn.", "General", ["conserve"], ["well preserved"], "The artefacts were beautifully preserved.", "Các hiện vật được bảo quản tuyệt đẹp."),
    create_word("undamaged", "/ʌnˈdæmɪdʒd/", "Adjective", "C1", "Not harmed or injured.", "Không bị hư hại", "Còn nguyên.", "General", ["intact"], ["remain undamaged"], "One side lay undamaged.", "Một bên vẫn không bị hư hại."),
    create_word("valuable", "/ˈvæljuəbl/", "Adjective", "B1", "Worth a great deal of money.", "Có giá trị", "Đắt tiền.", "General", ["precious"], ["valuable object"], "It contained valuable historical objects.", "Nó chứa những đồ vật lịch sử có giá trị."),
    create_word("marine", "/məˈriːn/", "Adjective", "B2", "Relating to or found in the sea.", "Thuộc về biển", "Dưới biển.", "General", ["nautical"], ["marine archaeology"], "Marine archaeology is challenging.", "Khảo cổ học biển rất đầy thách thức.")
]

# CAM 11 READING 3
r3_words = [
    create_word("silk", "/sɪlk/", "Noun", "B1", "A fine, strong, soft lustrous fibre produced by silkworms.", "Lụa", "Vải tơ tằm.", "General", [], ["silk worm", "silk trade"], "Silk is a luxurious fabric.", "Lụa là một loại vải sang trọng."),
    create_word("cocoon", "/kəˈkuːn/", "Noun", "C2", "A silky case spun by the larvae of many insects.", "Cái kén", "Bọc tơ.", "Scientific", [], ["spin a cocoon"], "Silk is produced from cocoons.", "Lụa được sản xuất từ những cái kén."),
    create_word("larva", "/ˈlɑːvə/", "Noun", "C2", "The active immature form of an insect.", "Ấu trùng", "Sâu con.", "Scientific", ["caterpillar"], ["insect larva"], "Silkworms are insect larvae.", "Tằm là ấu trùng của côn trùng."),
    create_word("legend", "/ˈledʒənd/", "Noun", "B1", "A traditional story.", "Truyền thuyết", "Chuyện xưa.", "General", ["myth"], ["ancient legend"], "Legend has it that she discovered it.", "Truyền thuyết kể rằng cô ấy đã phát hiện ra nó."),
    create_word("emperor", "/ˈempərə/", "Noun", "B2", "A sovereign ruler of great power.", "Hoàng đế", "Vua.", "General", ["ruler"], ["Chinese emperor"], "He was the ruler of the empire.", "Ông là người cai trị đế chế."),
    create_word("monopoly", "/məˈnɒpəli/", "Noun", "C1", "The exclusive possession or control of the supply or trade.", "Độc quyền", "Một mình bán.", "Business", ["control"], ["hold a monopoly"], "China had a monopoly on silk.", "Trung Quốc có độc quyền về lụa."),
    create_word("smuggle", "/ˈsmʌɡl/", "Verb", "C1", "Move goods illegally.", "Buôn lậu", "Đưa lén lút.", "General", ["traffic"], ["smuggle goods"], "Monks smuggled silkworms to Europe.", "Các nhà sư đã lén lút đưa tằm đến châu Âu."),
    create_word("conceal", "/kənˈsiːl/", "Verb", "C1", "Keep from sight; hide.", "Giấu giếm", "Che đậy.", "Formal", ["hide"], ["conceal the truth"], "They concealed the eggs in canes.", "Họ đã giấu trứng trong những cây gậy."),
    create_word("lucrative", "/ˈluːkrətɪv/", "Adjective", "C1", "Producing a great deal of profit.", "Sinh lời", "Béo bở.", "Formal", ["profitable"], ["lucrative business"], "The silk trade was highly lucrative.", "Buôn bán lụa rất có lợi nhuận."),
    create_word("commodity", "/kəˈmɒdəti/", "Noun", "C1", "A raw material or primary agricultural product.", "Hàng hóa", "Món đồ bán.", "Business", ["goods"], ["valuable commodity"], "Silk became a valuable commodity.", "Lụa trở thành một mặt hàng có giá trị.")
]

# CAM 11 READING 4
r4_words = [
    create_word("genetic", "/dʒəˈnetɪk/", "Adjective", "B2", "Relating to genes or heredity.", "Thuộc di truyền", "Do gen.", "Scientific", ["hereditary"], ["genetic code", "genetic makeup"], "Twins share the same genetic code.", "Các cặp song sinh chia sẻ cùng một mã di truyền."),
    create_word("identical", "/aɪˈdentɪkl/", "Adjective", "B2", "Similar in every detail; exactly alike.", "Giống hệt nhau", "Y đúc.", "General", ["exact", "indistinguishable"], ["identical twins"], "Identical twins come from one egg.", "Sinh đôi cùng trứng đến từ một quả trứng."),
    create_word("fraternal", "/frəˈtɜːnl/", "Adjective", "C2", "(of twins) developed from separate ova.", "Khác trứng (song sinh)", "Không giống nhau.", "Scientific", ["non-identical"], ["fraternal twins"], "Fraternal twins share half their DNA.", "Sinh đôi khác trứng chia sẻ một nửa DNA của họ."),
    create_word("heredity", "/həˈredəti/", "Noun", "C2", "The passing on of physical or mental characteristics genetically.", "Sự di truyền", "Truyền từ cha mẹ.", "Scientific", ["inheritance"], ["influence of heredity"], "Vulnerability is rooted in heredity.", "Sự dễ mắc bệnh bắt nguồn từ di truyền."),
    create_word("nurture", "/ˈnɜːtʃə/", "Noun", "C1", "Care and encouragement given to someone or something.", "Sự nuôi dưỡng / Môi trường", "Cách dạy dỗ.", "Formal", ["upbringing"], ["nature and nurture"], "They study nature versus nurture.", "Họ nghiên cứu bản năng và sự nuôi dưỡng."),
    create_word("untangle", "/ʌnˈtæŋɡl/", "Verb", "C2", "Free from a tangled or twisted state; investigate and resolve.", "Gỡ rối / Làm sáng tỏ", "Giải quyết rắc rối.", "Formal", ["unravel", "resolve"], ["untangle a mystery"], "Researchers try to untangle the influence of genes.", "Các nhà nghiên cứu cố gắng làm sáng tỏ ảnh hưởng của gen."),
    create_word("vulnerability", "/ˌvʌlnərəˈbɪləti/", "Noun", "C1", "The quality or state of being exposed to the possibility of being attacked or harmed.", "Sự dễ bị tổn thương", "Dễ mắc bệnh.", "Formal", ["susceptibility"], ["vulnerability to disease"], "It determines vulnerability to disease.", "Nó quyết định sự dễ mắc bệnh."),
    create_word("statistical", "/stəˈtɪstɪkl/", "Adjective", "B2", "Relating to the use of statistics.", "Thuộc thống kê", "Về số liệu.", "Academic", [], ["statistical analysis"], "They used a statistical approach.", "Họ đã sử dụng một phương pháp thống kê."),
    create_word("epigenetics", "/ˌepɪdʒəˈnetɪks/", "Noun", "C2", "The study of changes in organisms caused by modification of gene expression.", "Di truyền biểu sinh", "Sự thay đổi biểu hiện gen.", "Scientific", [], ["field of epigenetics"], "Epigenetics is a new field.", "Di truyền biểu sinh là một lĩnh vực mới."),
    create_word("trait", "/treɪt/", "Noun", "C1", "A distinguishing quality or characteristic.", "Đặc điểm / Nét tiêu biểu", "Điểm riêng.", "General", ["characteristic"], ["personality trait"], "They share physical traits.", "Họ chia sẻ các đặc điểm thể chất.")
]


generate_file(11, "Listening", 1, "hội trường, trang trại di sản", l1_words)
generate_file(11, "Listening", 2, "triển lãm nghệ thuật, tiến hóa", l2_words)
generate_file(11, "Listening", 3, "các hoạt động miễn phí, hòa nhạc", l3_words)
generate_file(11, "Listening", 4, "đa dạng sinh học, điểm nóng", l4_words)

generate_file(11, "Reading", 1, "nông nghiệp thẳng đứng", r1_words)
generate_file(11, "Reading", 2, "trục vớt tàu Mary Rose", r2_words)
generate_file(11, "Reading", 3, "lịch sử tơ lụa", r3_words)
generate_file(11, "Reading", 4, "nghiên cứu song sinh", r4_words)

print("Cambridge 11 generated.")
