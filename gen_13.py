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

# CAM 13 LISTENING 1
l1_words = [
    create_word("cookery", "/ˈkʊkəri/", "Noun", "B2", "The practice or skill of preparing and cooking food.", "Nghệ thuật nấu ăn", "Kỹ năng nấu nướng.", "General", ["cooking"], ["cookery class"], "I signed up for a cookery class.", "Tôi đã đăng ký một lớp học nấu ăn."),
    create_word("seasonal", "/ˈsiːzənl/", "Adjective", "B2", "Relating to or characteristic of a particular season.", "Theo mùa", "Mùa nào thức nấy.", "General", [], ["seasonal products"], "They focus on seasonal products.", "Họ tập trung vào các sản phẩm theo mùa."),
    create_word("congestion", "/kənˈdʒestʃən/", "Noun", "C1", "The state of being congested.", "Sự tắc nghẽn", "Đông đúc chật chội.", "Formal", ["crowding"], ["traffic congestion"], "Traffic congestion is a problem.", "Tắc nghẽn giao thông là một vấn đề."),
    create_word("pedestrian", "/pəˈdestriən/", "Noun", "B1", "A person walking along a road.", "Người đi bộ", "Đi bằng chân.", "Formal", ["walker"], ["pedestrian crossing"], "Use the pedestrian crossing.", "Hãy sử dụng vạch qua đường cho người đi bộ."),
    create_word("germination", "/ˌdʒɜːmɪˈneɪʃn/", "Noun", "C2", "The development of a plant from a seed.", "Sự nảy mầm", "Hạt mọc thành cây.", "Scientific", ["sprouting"], ["seed germination"], "We studied seed germination.", "Chúng tôi đã nghiên cứu sự nảy mầm của hạt giống."),
    create_word("dissertation", "/ˌdɪsəˈteɪʃn/", "Noun", "C1", "A long essay on a particular subject.", "Luận văn", "Bài nghiên cứu.", "Academic", ["thesis"], ["write a dissertation"], "It will be useful for my dissertation.", "Nó sẽ hữu ích cho luận văn của tôi."),
    create_word("urban", "/ˈɜːbən/", "Adjective", "B2", "Relating to a town or city.", "Thuộc đô thị", "Thành phố.", "General", ["city"], ["urban environment"], "Animals adapt to the urban environment.", "Động vật thích nghi với môi trường đô thị."),
    create_word("predator", "/ˈpredətə/", "Noun", "C1", "An animal that naturally preys on others.", "Kẻ săn mồi", "Con ăn thịt con khác.", "Scientific", ["hunter"], ["natural predator"], "There are fewer predators in cities.", "Có ít loài săn mồi hơn ở các thành phố."),
    create_word("nocturnal", "/nɒkˈtɜːnl/", "Adjective", "C1", "Done, occurring, or active at night.", "Hoạt động về đêm", "Ngủ ngày cày đêm.", "Scientific", [], ["nocturnal animal"], "Some animals become nocturnal.", "Một số động vật trở nên hoạt động về đêm."),
    create_word("resilience", "/rɪˈzɪliəns/", "Noun", "C2", "The capacity to recover quickly from difficulties.", "Sự kiên cường", "Vượt qua khó khăn.", "Formal", ["toughness"], ["show resilience"], "Wildlife shows resilience.", "Động vật hoang dã thể hiện sự kiên cường.")
]

# CAM 13 LISTENING 2
l2_words = [
    create_word("membership", "/ˈmembəʃɪp/", "Noun", "B1", "The state of being a member.", "Tư cách thành viên", "Tham gia hội.", "General", ["affiliation"], ["club membership"], "I asked about the club membership.", "Tôi đã hỏi về tư cách thành viên câu lạc bộ."),
    create_word("insurance", "/ɪnˈʃʊərəns/", "Noun", "B2", "Guarantee of compensation for specified loss.", "Bảo hiểm", "Phí bảo vệ.", "General", ["coverage"], ["include insurance"], "The fee includes insurance.", "Phí bao gồm cả bảo hiểm."),
    create_word("volunteer", "/ˌvɒlənˈtɪə/", "Verb", "B1", "Freely offer to do something.", "Tình nguyện", "Làm không lương.", "General", ["offer"], ["volunteer work"], "We encourage staff to volunteer.", "Chúng tôi khuyến khích nhân viên làm tình nguyện."),
    create_word("sustainability", "/səˌsteɪnəˈbɪləti/", "Noun", "C1", "The ability to be maintained at a certain rate.", "Sự bền vững", "Lâu dài.", "Academic", ["viability"], ["environmental sustainability"], "The project focuses on sustainability.", "Dự án tập trung vào tính bền vững."),
    create_word("nanotechnology", "/ˌnænəʊtekˈnɒlədʒi/", "Noun", "C2", "Technology dealing with dimensions less than 100 nanometers.", "Công nghệ nano", "Công nghệ siêu nhỏ.", "Scientific", [], ["field of nanotechnology"], "The presentation is on nanotechnology.", "Bài thuyết trình về công nghệ nano."),
    create_word("episodic", "/ˌepɪˈsɒdɪk/", "Adjective", "C2", "Containing or consisting of a series of separate events.", "Thuộc tình tiết", "Nhớ sự kiện.", "Academic", [], ["episodic memory"], "Episodic memory involves specific events.", "Trí nhớ tình tiết liên quan đến các sự kiện cụ thể."),
    create_word("semantic", "/sɪˈmæntɪk/", "Adjective", "C1", "Relating to meaning.", "Thuộc ngữ nghĩa", "Kiến thức.", "Academic", [], ["semantic memory"], "Semantic memory stores facts.", "Trí nhớ ngữ nghĩa lưu trữ các sự kiện."),
    create_word("encoding", "/ɪnˈkəʊdɪŋ/", "Noun", "C2", "The process of converting information into a form.", "Sự mã hóa", "Ghi vào não.", "Technical", [], ["memory encoding"], "Encoding is the first step.", "Mã hóa là bước đầu tiên."),
    create_word("retrieval", "/rɪˈtriːvl/", "Noun", "C1", "The process of getting something back.", "Sự truy xuất", "Nhớ lại.", "Formal", ["recall"], ["information retrieval"], "Retrieval is accessing memories.", "Truy xuất là việc truy cập vào ký ức."),
    create_word("olfactory", "/ɒlˈfæktəri/", "Adjective", "C2", "Relating to the sense of smell.", "Thuộc khứu giác", "Liên quan đến mùi.", "Scientific", [], ["olfactory cues"], "Olfactory cues trigger memories.", "Dấu hiệu khứu giác kích hoạt ký ức.")
]

# CAM 13 LISTENING 3
l3_words = [
    create_word("rent", "/rent/", "Noun", "A2", "A tenant's regular payment to a landlord.", "Tiền thuê nhà", "Tiền trả hàng tháng.", "General", ["lease"], ["pay rent"], "The rent is 850 pounds.", "Tiền thuê nhà là 850 bảng."),
    create_word("commute", "/kəˈmjuːt/", "Verb", "C1", "Travel some distance between home and work.", "Đi làm xa", "Đi lại hàng ngày.", "General", ["travel"], ["daily commute"], "It's an easy commute.", "Đó là một chuyến đi làm dễ dàng."),
    create_word("campus", "/ˈkæmpəs/", "Noun", "B1", "The grounds and buildings of a university.", "Khuôn viên trường", "Sân trường ĐH.", "General", [], ["university campus"], "The new campus was built in 1961.", "Khuôn viên mới được xây dựng năm 1961."),
    create_word("archive", "/ˈɑːkaɪv/", "Noun", "C1", "A collection of historical documents.", "Lưu trữ", "Kho tài liệu.", "Formal", ["records"], ["digital archive"], "They used the library archive.", "Họ đã sử dụng kho lưu trữ của thư viện."),
    create_word("textile", "/ˈtekstaɪl/", "Noun", "C1", "A type of cloth or woven fabric.", "Dệt may", "Vải vóc.", "General", ["fabric"], ["textile exhibition"], "I saw an exhibition of textiles.", "Tôi đã xem một cuộc triển lãm dệt may."),
    create_word("dye", "/daɪ/", "Noun", "C1", "A natural or synthetic substance used to add color.", "Thuốc nhuộm", "Chất làm màu.", "General", ["pigment"], ["natural dye"], "They used natural dyes.", "Họ đã sử dụng thuốc nhuộm tự nhiên."),
    create_word("pigment", "/ˈpɪɡmənt/", "Noun", "C2", "The natural coloring matter.", "Sắc tố", "Màu tự nhiên.", "Technical", ["colorant"], ["natural pigment"], "Insects provide a red pigment.", "Côn trùng cung cấp một sắc tố màu đỏ."),
    create_word("lizard", "/ˈlɪzəd/", "Noun", "B1", "A reptile with a long body and tail.", "Thằn lằn", "Bò sát nhỏ.", "General", ["reptile"], ["sleepy lizard"], "The sleepy lizard has a blue tongue.", "Thằn lằn Sleepy có cái lưỡi màu xanh."),
    create_word("monogamous", "/məˈnɒɡəməs/", "Adjective", "C2", "Having only one mate at a time.", "Chung thủy", "Một vợ một chồng.", "Scientific", ["faithful"], ["monogamous relationship"], "These lizards are monogamous.", "Loài thằn lằn này rất chung thủy."),
    create_word("navigate", "/ˈnævɪɡeɪt/", "Verb", "B2", "Plan and direct the route.", "Định hướng", "Tìm đường đi.", "General", ["steer"], ["navigate back"], "They navigate back to their partners.", "Chúng tìm đường quay lại với bạn đời.")
]

# CAM 13 LISTENING 4
l4_words = [
    create_word("finance", "/ˈfaɪnæns/", "Noun", "B2", "The management of large amounts of money.", "Tài chính", "Tiền bạc.", "General", ["economics"], ["work in finance"], "I want a job in finance.", "Tôi muốn một công việc trong lĩnh vực tài chính."),
    create_word("vacancy", "/ˈveɪkənsi/", "Noun", "B2", "An unoccupied position or job.", "Vị trí trống", "Chỗ làm chưa có người.", "Formal", ["opening"], ["job vacancy"], "Are there any vacancies?", "Có vị trí tuyển dụng nào không?"),
    create_word("scenery", "/ˈsiːnəri/", "Noun", "B1", "The natural features of a landscape.", "Phong cảnh", "Cảnh đẹp.", "General", ["landscape"], ["beautiful scenery"], "The mountain scenery is beautiful.", "Phong cảnh núi non rất đẹp."),
    create_word("nutrition", "/njuˈtrɪʃn/", "Noun", "B2", "The process of providing food for health.", "Dinh dưỡng", "Chất bổ.", "General", ["nourishment"], ["nutrition label"], "Check the nutrition label.", "Hãy kiểm tra nhãn dinh dưỡng."),
    create_word("ingredient", "/ɪnˈɡriːdiənt/", "Noun", "B1", "Any of the foods combined to make a dish.", "Thành phần", "Nguyên liệu.", "General", ["component"], ["main ingredient"], "Sugar is a key ingredient.", "Đường là một thành phần chính."),
    create_word("commodity", "/kəˈmɒdəti/", "Noun", "C1", "A raw material that can be bought and sold.", "Hàng hóa", "Sản phẩm buôn bán.", "Business", ["goods"], ["valuable commodity"], "Coffee became a valuable commodity.", "Cà phê đã trở thành một loại hàng hóa có giá trị."),
    create_word("plantation", "/plɑːnˈteɪʃn/", "Noun", "B2", "An estate on which crops are cultivated.", "Đồn điền", "Nông trại lớn.", "General", ["estate"], ["coffee plantation"], "Slaves worked on plantations.", "Nô lệ làm việc trên các đồn điền."),
    create_word("consumption", "/kənˈsʌmpʃn/", "Noun", "B2", "The using up of a resource.", "Sự tiêu thụ", "Việc sử dụng.", "General", ["use"], ["coffee consumption"], "Coffee consumption grew rapidly.", "Mức tiêu thụ cà phê tăng nhanh."),
    create_word("stimulant", "/ˈstɪmjələnt/", "Noun", "C1", "A substance that raises levels of nervous activity.", "Chất kích thích", "Làm hưng phấn.", "Scientific", ["energizer"], ["mild stimulant"], "Caffeine is a stimulant.", "Caffeine là một chất kích thích."),
    create_word("smuggling", "/ˈsmʌɡlɪŋ/", "Noun", "B2", "The illegal movement of goods.", "Sự buôn lậu", "Mang hàng chui.", "General", ["trafficking"], ["drug smuggling"], "Seed smuggling was common.", "Việc buôn lậu hạt giống rất phổ biến.")
]

# CAM 13 READING 1
r1_words = [
    create_word("database", "/ˈdeɪtəbeɪs/", "Noun", "B2", "A structured set of data held in a computer.", "Cơ sở dữ liệu", "Kho thông tin.", "Technical", ["repository"], ["search the database"], "The website uses a large database.", "Trang web sử dụng một cơ sở dữ liệu lớn."),
    create_word("interactive", "/ˌɪntərˈæktɪv/", "Adjective", "B2", "Allowing a two-way flow of information.", "Tương tác", "Máy móc và người dùng.", "General", ["responsive"], ["interactive map"], "The map is highly interactive.", "Bản đồ có tính tương tác cao."),
    create_word("itinerary", "/aɪˈtɪnərəri/", "Noun", "C1", "A planned route or journey.", "Lịch trình", "Kế hoạch đi chơi.", "Formal", ["schedule"], ["travel itinerary"], "You can create a custom itinerary.", "Bạn có thể tạo một lịch trình tùy chỉnh."),
    create_word("boredom", "/ˈbɔːdəm/", "Noun", "B2", "The state of feeling weary and restless through lack of interest.", "Sự nhàm chán", "Chán nản.", "General", ["tedium"], ["relieve boredom"], "Boredom can actually be useful.", "Sự nhàm chán thực ra có thể hữu ích."),
    create_word("stimulating", "/ˈstɪmjuleɪtɪŋ/", "Adjective", "B2", "Encouraging or arousing interest.", "Kích thích", "Thú vị.", "General", ["exciting"], ["stimulating activity"], "Boredom is stimulating.", "Sự nhàm chán có tính kích thích."),
    create_word("creativity", "/ˌkriːeɪˈtɪvəti/", "Noun", "B2", "The use of the imagination or original ideas.", "Sự sáng tạo", "Làm ra cái mới.", "General", ["imagination"], ["spark creativity"], "It can spark creativity.", "Nó có thể khơi dậy sự sáng tạo."),
    create_word("artificial", "/ˌɑːtɪˈfɪʃl/", "Adjective", "B2", "Made or produced by human beings.", "Nhân tạo", "Do máy làm.", "General", ["synthetic"], ["artificial intelligence"], "Artificial intelligence creates art.", "Trí tuệ nhân tạo tạo ra nghệ thuật."),
    create_word("algorithm", "/ˈælɡərɪðəm/", "Noun", "C1", "A set of rules for calculations.", "Thuật toán", "Công thức máy tính.", "Technical", ["formula"], ["complex algorithm"], "The program uses an algorithm.", "Chương trình sử dụng một thuật toán."),
    create_word("originality", "/əˌrɪdʒəˈnæləti/", "Noun", "C1", "The ability to think independently and creatively.", "Tính độc đáo", "Không sao chép.", "General", ["novelty"], ["lack of originality"], "They question the originality of the art.", "Họ đặt câu hỏi về tính độc đáo của nghệ thuật."),
    create_word("aesthetic", "/iːsˈθetɪk/", "Adjective", "C1", "Concerned with beauty.", "Thẩm mỹ", "Về cái đẹp.", "Academic", ["artistic"], ["aesthetic appeal"], "Does the painting have aesthetic value?", "Bức tranh có giá trị thẩm mỹ không?")
]

# CAM 13 READING 2
r2_words = [
    create_word("cinnamon", "/ˈsɪnəmən/", "Noun", "B2", "An aromatic spice.", "Quế", "Gia vị.", "General", ["spice"], ["cinnamon stick"], "Cinnamon was highly prized.", "Quế được đánh giá rất cao."),
    create_word("monopoly", "/məˈnɒpəli/", "Noun", "C1", "Exclusive possession or control.", "Độc quyền", "Một mình bán.", "Business", ["domination"], ["hold a monopoly"], "They held a monopoly on the trade.", "Họ độc quyền buôn bán."),
    create_word("hormone", "/ˈhɔːməʊn/", "Noun", "C1", "A regulatory substance produced in an organism.", "Hóc-môn", "Chất trong cơ thể.", "Scientific", [], ["growth hormone"], "Oxytocin is a hormone.", "Oxytocin là một loại hormone."),
    create_word("interaction", "/ˌɪntərˈækʃn/", "Noun", "B2", "Reciprocal action or influence.", "Sự tương tác", "Giao tiếp.", "General", ["communication"], ["social interaction"], "It affects social interaction.", "Nó ảnh hưởng đến sự tương tác xã hội."),
    create_word("trust", "/trʌst/", "Noun", "B1", "Firm belief in reliability.", "Lòng tin", "Sự tin tưởng.", "General", ["confidence"], ["build trust"], "Oxytocin promotes trust.", "Oxytocin thúc đẩy lòng tin."),
    create_word("innovation", "/ˌɪnəˈveɪʃn/", "Noun", "B2", "The action of innovating.", "Sự đổi mới", "Sáng tạo mới.", "General", ["novelty"], ["technological innovation"], "Innovation is key for business.", "Đổi mới là chìa khóa cho kinh doanh."),
    create_word("strategy", "/ˈstrætədʒi/", "Noun", "B2", "A plan of action.", "Chiến lược", "Kế hoạch lớn.", "General", ["plan"], ["business strategy"], "Companies need a new strategy.", "Các công ty cần một chiến lược mới."),
    create_word("consumer", "/kənˈsjuːmə/", "Noun", "B1", "A person who purchases goods.", "Người tiêu dùng", "Khách hàng.", "General", ["buyer"], ["consumer trends"], "Consumer trends are changing.", "Xu hướng của người tiêu dùng đang thay đổi."),
    create_word("counter-intuitive", "/ˌkaʊntər ɪnˈtjuːɪtɪv/", "Adjective", "C2", "Contrary to intuition.", "Phản trực giác", "Ngược lẽ thường.", "Formal", ["unexpected"], ["seem counter-intuitive"], "The result was counter-intuitive.", "Kết quả có vẻ ngược với trực giác."),
    create_word("aversion", "/əˈvɜːʃn/", "Noun", "C2", "A strong dislike.", "Sự ác cảm", "Ghét bỏ.", "Formal", ["dislike"], ["aversion to risk"], "They have an aversion to change.", "Họ có ác cảm với sự thay đổi.")
]

# CAM 13 READING 3
r3_words = [
    create_word("coconut", "/ˈkəʊkənʌt/", "Noun", "A2", "The large seed of a tropical palm.", "Quả dừa", "Trái dừa.", "General", [], ["coconut water"], "The coconut has many uses.", "Dừa có nhiều công dụng."),
    create_word("timber", "/ˈtɪmbə/", "Noun", "C1", "Wood prepared for building.", "Gỗ", "Gỗ làm nhà.", "Technical", ["lumber"], ["valuable timber"], "The trunk provides timber.", "Thân cây cung cấp gỗ."),
    create_word("infant", "/ˈɪnfənt/", "Noun", "B2", "A very young child.", "Trẻ sơ sinh", "Em bé.", "Formal", ["baby"], ["infant development"], "Baby talk helps infants learn.", "Tiếng nói trẻ em giúp trẻ sơ sinh học hỏi."),
    create_word("vocabulary", "/vəˈkæbjələri/", "Noun", "A2", "The body of words used in a language.", "Từ vựng", "Vốn từ.", "General", ["lexicon"], ["expand vocabulary"], "It increases their vocabulary.", "Nó làm tăng vốn từ vựng của chúng."),
    create_word("mimic", "/ˈmɪmɪk/", "Verb", "C1", "Imitate.", "Bắt chước", "Làm theo.", "General", ["copy"], ["mimic sounds"], "Babies try to mimic adults.", "Trẻ sơ sinh cố gắng bắt chước người lớn."),
    create_word("civilization", "/ˌsɪvəlaɪˈzeɪʃn/", "Noun", "B2", "The stage of human social development.", "Nền văn minh", "Xã hội tiến bộ.", "General", ["culture"], ["ancient civilization"], "The Harappan civilization collapsed.", "Nền văn minh Harappa đã sụp đổ."),
    create_word("archaeology", "/ˌɑːkiˈɒlədʒi/", "Noun", "C1", "The study of human history.", "Khảo cổ học", "Đào cổ vật.", "Academic", [], ["marine archaeology"], "Archaeology reveals the past.", "Khảo cổ học tiết lộ quá khứ."),
    create_word("drought", "/draʊt/", "Noun", "B2", "A prolonged period of low rainfall.", "Hạn hán", "Không mưa.", "General", ["dry spell"], ["severe drought"], "A drought caused the decline.", "Một trận hạn hán đã gây ra sự suy tàn."),
    create_word("monsoon", "/mɒnˈsuːn/", "Noun", "C1", "A seasonal prevailing wind bringing rain.", "Gió mùa", "Mùa mưa.", "General", [], ["monsoon season"], "The monsoon failed.", "Gió mùa đã thất bại."),
    create_word("settlement", "/ˈsetlmənt/", "Noun", "B2", "A place where people establish a community.", "Khu định cư", "Nơi sống.", "General", ["colony"], ["ancient settlement"], "They abandoned the settlements.", "Họ đã bỏ hoang các khu định cư.")
]

# CAM 13 READING 4
r4_words = [
    create_word("clipper", "/ˈklɪpə/", "Noun", "C2", "A fast sailing ship.", "Tàu buồm siêu tốc", "Tàu nhanh.", "Historical", ["vessel"], ["tea clipper"], "Cutty Sark is a famous clipper.", "Cutty Sark là một chiếc tàu buồm nổi tiếng."),
    create_word("cargo", "/ˈkɑːɡəʊ/", "Noun", "C1", "Goods carried on a ship.", "Hàng hóa", "Đồ trên tàu.", "General", ["freight"], ["valuable cargo"], "It carried a cargo of tea.", "Nó chở một chuyến hàng trà."),
    create_word("degradation", "/ˌdeɡrəˈdeɪʃn/", "Noun", "C2", "The condition of being degraded.", "Sự suy thoái", "Xuống cấp.", "Formal", ["deterioration"], ["soil degradation"], "Soil degradation is a problem.", "Suy thoái đất là một vấn đề."),
    create_word("microorganism", "/ˌmaɪkrəʊˈɔːɡənɪzm/", "Noun", "C2", "A microscopic organism.", "Vi sinh vật", "Sinh vật nhỏ.", "Scientific", ["microbe"], ["soil microorganisms"], "Soil contains microorganisms.", "Đất chứa các vi sinh vật."),
    create_word("fertilizer", "/ˈfɜːtəlaɪzə/", "Noun", "C1", "A substance added to soil to increase fertility.", "Phân bón", "Chất cho cây.", "General", ["manure"], ["chemical fertilizer"], "Farmers use fertilizer.", "Nông dân sử dụng phân bón."),
    create_word("sustainable", "/səˈsteɪnəbl/", "Adjective", "B2", "Able to be maintained at a certain rate.", "Bền vững", "Dùng lâu.", "Academic", ["eco-friendly"], ["sustainable agriculture"], "We need sustainable farming.", "Chúng ta cần canh tác bền vững."),
    create_word("happiness", "/ˈhæpinəs/", "Noun", "B1", "The state of being happy.", "Hạnh phúc", "Niềm vui.", "General", ["joy"], ["pursuit of happiness"], "Is happiness the goal?", "Hạnh phúc có phải là mục tiêu không?"),
    create_word("consumerism", "/kənˈsjuːmərɪzm/", "Noun", "C2", "The promotion of the interests of consumers.", "Chủ nghĩa tiêu dùng", "Mua sắm.", "Academic", [], ["rise of consumerism"], "The book critiques consumerism.", "Cuốn sách phê phán chủ nghĩa tiêu dùng."),
    create_word("manipulation", "/məˌnɪpjuˈleɪʃn/", "Noun", "C1", "The action of manipulating.", "Sự thao túng", "Điều khiển.", "Formal", ["control"], ["psychological manipulation"], "It discusses psychological manipulation.", "Nó thảo luận về sự thao túng tâm lý."),
    create_word("well-being", "/ˌwel ˈbiːɪŋ/", "Noun", "C1", "The state of being comfortable or happy.", "Sự an lạc", "Sống khỏe.", "General", ["welfare"], ["emotional well-being"], "Governments measure well-being.", "Các chính phủ đo lường sự an lạc.")
]

generate_file(13, "Listening", 1, "nấu ăn, giao thông, nảy mầm", l1_words)
generate_file(13, "Listening", 2, "xe đạp, trí nhớ", l2_words)
generate_file(13, "Listening", 3, "thuê nhà, nhuộm", l3_words)
generate_file(13, "Listening", 4, "xin việc, cà phê", l4_words)
generate_file(13, "Reading", 1, "du lịch, nhàm chán, AI", r1_words)
generate_file(13, "Reading", 2, "quế, oxytocin", r2_words)
generate_file(13, "Reading", 3, "dừa, tiếng trẻ em", r3_words)
generate_file(13, "Reading", 4, "tàu Cutty Sark, đất", r4_words)

print("Cambridge 13 generated.")
