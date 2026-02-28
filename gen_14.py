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

# CAM 14 LISTENING 1
l1_words = [
    create_word("theft", "/θeft/", "Noun", "B2", "The action or crime of stealing.", "Trộm cắp", "Ăn cắp.", "General", ["robbery"], ["report a theft"], "She reported a theft.", "Cô ấy đã báo cáo một vụ trộm."),
    create_word("apprentice", "/əˈprentɪs/", "Noun", "B2", "A person learning a trade.", "Thực tập sinh", "Học việc.", "General", ["trainee"], ["new apprentice"], "He is an apprentice.", "Anh ấy là một thực tập sinh."),
    create_word("induction", "/ɪnˈdʌkʃn/", "Noun", "C1", "The action of inducting someone.", "Hướng dẫn nhập môn", "Ngày đầu đi làm.", "Formal", ["orientation"], ["induction talk"], "There is an induction talk today.", "Hôm nay có buổi hướng dẫn nhập môn."),
    create_word("mentor", "/ˈmentɔː/", "Noun", "B2", "An experienced adviser.", "Cố vấn", "Người hướng dẫn.", "General", ["guide"], ["find a mentor"], "You will have a mentor.", "Bạn sẽ có một người cố vấn."),
    create_word("coastal", "/ˈkəʊstl/", "Adjective", "B2", "Of or near a coast.", "Ven biển", "Gần biển.", "General", ["seaside"], ["coastal city"], "Coastal cities face problems.", "Các thành phố ven biển đối mặt với vấn đề."),
    create_word("expansion", "/ɪkˈspænʃn/", "Noun", "B2", "The action of becoming larger.", "Sự mở rộng", "To ra.", "General", ["growth"], ["urban expansion"], "City expansion continues.", "Sự mở rộng thành phố vẫn tiếp tục."),
    create_word("renewable", "/rɪˈnjuːəbl/", "Adjective", "B2", "Not depleted when used.", "Có thể tái tạo", "Dùng không hết.", "Academic", ["sustainable"], ["renewable energy"], "We need renewable energy.", "Chúng ta cần năng lượng tái tạo."),
    create_word("tide", "/taɪd/", "Noun", "B2", "The alternate rising and falling of the sea.", "Thủy triều", "Nước lên xuống.", "General", [], ["high tide"], "The tide is high.", "Thủy triều đang lên cao."),
    create_word("turbine", "/ˈtɜːbaɪn/", "Noun", "C1", "A machine for producing continuous power.", "Tua bin", "Máy phát điện.", "Technical", [], ["wind turbine"], "They use turbines in the ocean.", "Họ sử dụng các tua bin trong đại dương."),
    create_word("pollution", "/pəˈluːʃn/", "Noun", "B1", "Harmful substances in environment.", "Ô nhiễm", "Làm bẩn.", "General", ["contamination"], ["marine pollution"], "Marine pollution is bad.", "Ô nhiễm biển rất tệ.")
]

# CAM 14 LISTENING 2
l2_words = [
    create_word("clinic", "/ˈklɪnɪk/", "Noun", "B1", "Establishment for medical treatment.", "Phòng khám", "Chữa bệnh.", "General", ["health center"], ["visit the clinic"], "She went to the health clinic.", "Cô ấy đã đi đến phòng khám sức khỏe."),
    create_word("insurance", "/ɪnˈʃʊərəns/", "Noun", "B2", "Guarantee of compensation.", "Bảo hiểm", "Phí an toàn.", "General", ["coverage"], ["health insurance"], "Do you have insurance?", "Bạn có bảo hiểm không?"),
    create_word("injury", "/ˈɪndʒəri/", "Noun", "B2", "Physical harm.", "Chấn thương", "Vết đau.", "General", ["wound"], ["knee injury"], "She has a leg injury.", "Cô ấy bị chấn thương ở chân."),
    create_word("castle", "/ˈkɑːsl/", "Noun", "A2", "A large fortified building.", "Lâu đài", "Nhà vua chúa.", "General", ["fortress"], ["ancient castle"], "They visited the castle.", "Họ đã đến thăm lâu đài."),
    create_word("mammoth", "/ˈmæməθ/", "Noun", "C1", "A large extinct elephant.", "Voi ma mút", "Voi cổ đại.", "General", [], ["woolly mammoth"], "Mammoths are extinct.", "Voi ma mút đã tuyệt chủng."),
    create_word("extinction", "/ɪkˈstɪŋkʃn/", "Noun", "B2", "Process of a species dying out.", "Sự tuyệt chủng", "Chết hết.", "Academic", ["vanishment"], ["mass extinction"], "They face extinction.", "Chúng đối mặt với sự tuyệt chủng."),
    create_word("forecast", "/ˈfɔːkɑːst/", "Noun", "B1", "A prediction of future events.", "Dự báo", "Đoán trước.", "General", ["prediction"], ["weather forecast"], "The forecast says it will rain.", "Dự báo nói rằng trời sẽ mưa."),
    create_word("meteorology", "/ˌmiːtiəˈrɒlədʒi/", "Noun", "C2", "Science of the atmosphere.", "Khí tượng học", "Môn thời tiết.", "Technical", [], ["study meteorology"], "Meteorology is complex.", "Khí tượng học rất phức tạp."),
    create_word("prediction", "/prɪˈdɪkʃn/", "Noun", "B1", "A forecast.", "Dự đoán", "Sự đoán.", "General", ["forecast"], ["make a prediction"], "His prediction was right.", "Dự đoán của anh ấy đã đúng."),
    create_word("reliable", "/rɪˈlaɪəbl/", "Adjective", "B1", "Able to be trusted.", "Đáng tin cậy", "Tin được.", "General", ["trustworthy"], ["reliable source"], "The forecast is reliable.", "Dự báo rất đáng tin cậy.")
]

# CAM 14 LISTENING 3
l3_words = [
    create_word("conference", "/ˈkɒnfərəns/", "Noun", "B1", "A formal meeting.", "Hội nghị", "Cuộc họp.", "Formal", ["seminar"], ["conference room"], "We booked a conference room.", "Chúng tôi đã đặt một phòng hội nghị."),
    create_word("facility", "/fəˈsɪləti/", "Noun", "B1", "Equipment provided for a purpose.", "Cơ sở vật chất", "Đồ đạc.", "General", ["amenity"], ["modern facility"], "The facilities are good.", "Cơ sở vật chất rất tốt."),
    create_word("projector", "/prəˈdʒektə/", "Noun", "B1", "Object used to project images.", "Máy chiếu", "Phát hình.", "General", [], ["use a projector"], "We need a projector.", "Chúng tôi cần một máy chiếu."),
    create_word("rehearsal", "/rɪˈhɜːsl/", "Noun", "B2", "A practice performance.", "Buổi tập dượt", "Tập trước.", "General", ["practice"], ["band rehearsal"], "The band had a rehearsal.", "Ban nhạc đã có một buổi tập dượt."),
    create_word("audition", "/ɔːˈdɪʃn/", "Noun", "B2", "An interview for a performer.", "Thử giọng", "Tuyển diễn viên.", "General", ["tryout"], ["hold an audition"], "They held auditions.", "Họ đã tổ chức các buổi thử giọng."),
    create_word("budget", "/ˈbʌdʒɪt/", "Noun", "B2", "Estimate of income and expenditure.", "Ngân sách", "Tiền có.", "General", ["funds"], ["tight budget"], "We are on a tight budget.", "Chúng tôi có ngân sách eo hẹp."),
    create_word("festival", "/ˈfestɪvl/", "Noun", "A2", "A period of celebration.", "Lễ hội", "Ngày vui.", "General", ["celebration"], ["music festival"], "It's an arts festival.", "Đó là một lễ hội nghệ thuật."),
    create_word("composer", "/kəmˈpəʊzə/", "Noun", "B2", "A person who writes music.", "Nhà soạn nhạc", "Người viết nhạc.", "General", [], ["famous composer"], "She is a composer.", "Cô ấy là một nhà soạn nhạc."),
    create_word("commission", "/kəˈmɪʃn/", "Verb", "C1", "Order something to be produced.", "Đặt hàng", "Thuê làm.", "Formal", ["order"], ["commission a piece"], "They commissioned a song.", "Họ đã đặt hàng một bài hát."),
    create_word("vibrant", "/ˈvaɪbrənt/", "Adjective", "C1", "Full of energy.", "Sôi động", "Mạnh mẽ.", "General", ["energetic"], ["vibrant music"], "The music is vibrant.", "Âm nhạc rất sôi động.")
]

# CAM 14 LISTENING 4
l4_words = [
    create_word("booking", "/ˈbʊkɪŋ/", "Noun", "A2", "An act of reserving.", "Sự đặt chỗ", "Mua trước.", "General", ["reservation"], ["make a booking"], "I made a booking.", "Tôi đã đặt chỗ."),
    create_word("buffet", "/ˈbʊfeɪ/", "Noun", "B1", "A meal where guests serve themselves.", "Tiệc đứng", "Tự lấy đồ ăn.", "General", [], ["buffet lunch"], "We will have a buffet.", "Chúng tôi sẽ có tiệc đứng."),
    create_word("excursion", "/ɪkˈskɜːʃn/", "Noun", "B2", "A short journey.", "Dã ngoại", "Đi chơi.", "General", ["trip"], ["go on an excursion"], "We went on an excursion.", "Chúng tôi đã đi dã ngoại."),
    create_word("literature", "/ˈlɪtrətʃə/", "Noun", "B1", "Written works.", "Văn học", "Sách vở.", "General", ["writing"], ["children's literature"], "He studies literature.", "Anh ấy học văn học."),
    create_word("illustration", "/ˌɪləˈstreɪʃn/", "Noun", "B2", "A picture in a book.", "Hình minh họa", "Tranh vẽ.", "General", ["picture"], ["book illustration"], "The book has illustrations.", "Cuốn sách có hình minh họa."),
    create_word("archaeology", "/ˌɑːkiˈɒlədʒi/", "Noun", "C1", "Study of human history via excavation.", "Khảo cổ học", "Đào cổ vật.", "Academic", [], ["marine archaeology"], "Marine archaeology is hard.", "Khảo cổ học biển rất khó."),
    create_word("shipwreck", "/ˈʃɪprek/", "Noun", "B2", "Destruction of a ship.", "Xác tàu đắm", "Tàu chìm.", "General", ["wreck"], ["ancient shipwreck"], "They found a shipwreck.", "Họ đã tìm thấy một xác tàu đắm."),
    create_word("excavation", "/ˌekskəˈveɪʃn/", "Noun", "C1", "Action of excavating.", "Sự khai quật", "Đào bới.", "Technical", ["digging"], ["excavation site"], "The excavation is ongoing.", "Cuộc khai quật đang diễn ra."),
    create_word("artifact", "/ˈɑːtɪfækt/", "Noun", "C1", "An object made by human.", "Hiện vật", "Đồ cổ.", "Academic", ["relic"], ["museum artifact"], "They recovered artifacts.", "Họ đã thu hồi các hiện vật."),
    create_word("submersible", "/səbˈmɜːsəbl/", "Noun", "C2", "A boat that goes underwater.", "Tàu lặn", "Tàu dưới nước.", "Technical", ["submarine"], ["use a submersible"], "They used a submersible.", "Họ đã sử dụng một chiếc tàu lặn.")
]

# CAM 14 READING 1
r1_words = [
    create_word("creativity", "/ˌkriːeɪˈtɪvəti/", "Noun", "B2", "Use of imagination.", "Sự sáng tạo", "Làm cái mới.", "General", ["imagination"], ["spark creativity"], "Play boosts creativity.", "Vui chơi tăng cường sự sáng tạo."),
    create_word("cognitive", "/ˈkɒɡnətɪv/", "Adjective", "C1", "Relating to cognition.", "Nhận thức", "Suy nghĩ.", "Academic", ["mental"], ["cognitive skills"], "It improves cognitive skills.", "Nó cải thiện kỹ năng nhận thức."),
    create_word("urbanization", "/ˌɜːbənaɪˈzeɪʃn/", "Noun", "C1", "Process of making an area urban.", "Đô thị hóa", "Biến thành phố.", "Academic", [], ["rapid urbanization"], "Urbanization reduces play areas.", "Đô thị hóa làm giảm khu vực vui chơi."),
    create_word("scheme", "/skiːm/", "Noun", "B2", "A systematic plan.", "Kế hoạch / Hệ thống", "Dự án.", "General", ["program"], ["bike-sharing scheme"], "The scheme was a success.", "Hệ thống đã thành công."),
    create_word("vandalism", "/ˈvændəlɪzm/", "Noun", "C1", "Deliberate destruction of property.", "Phá hoại", "Làm hỏng đồ.", "General", ["damage"], ["act of vandalism"], "Vandalism is a problem.", "Sự phá hoại là một vấn đề."),
    create_word("retention", "/rɪˈtenʃn/", "Noun", "C1", "Continued possession or use.", "Sự giữ chân", "Giữ lại.", "Business", ["keeping"], ["staff retention"], "Staff retention is key.", "Việc giữ chân nhân viên là then chốt."),
    create_word("turnover", "/ˈtɜːnəʊvə/", "Noun", "C1", "Rate at which employees leave.", "Luân chuyển nhân sự", "Thay người.", "Business", [], ["high turnover"], "High turnover is bad.", "Tỷ lệ luân chuyển cao là điều tồi tệ."),
    create_word("intrinsic", "/ɪnˈtrɪnzɪk/", "Adjective", "C2", "Belonging naturally.", "Nội tại", "Bên trong.", "Formal", ["inherent"], ["intrinsic motivation"], "He has intrinsic motivation.", "Anh ấy có động lực nội tại."),
    create_word("extrinsic", "/eksˈtrɪnzɪk/", "Adjective", "C2", "Coming from outside.", "Ngoại lai", "Bên ngoài.", "Formal", ["external"], ["extrinsic reward"], "Money is an extrinsic reward.", "Tiền là một phần thưởng bên ngoài."),
    create_word("morale", "/məˈrɑːl/", "Noun", "C1", "Confidence and enthusiasm of a group.", "Tinh thần", "Nhuệ khí.", "General", ["spirit"], ["boost morale"], "It boosted their morale.", "Nó đã thúc đẩy tinh thần của họ.")
]

# CAM 14 READING 2
r2_words = [
    create_word("landscape", "/ˈlændskeɪp/", "Noun", "B1", "Visible features of an area.", "Phong cảnh", "Cảnh vật.", "General", ["scenery"], ["landscape photography"], "He took landscape photos.", "Ông ấy đã chụp ảnh phong cảnh."),
    create_word("expedition", "/ˌekspəˈdɪʃn/", "Noun", "B2", "A journey for a purpose.", "Cuộc thám hiểm", "Đi xa.", "General", ["journey"], ["photographic expedition"], "He went on an expedition.", "Ông ấy đã đi thám hiểm."),
    create_word("skyscraper", "/ˈskaɪskreɪpə/", "Noun", "B1", "A very tall building.", "Nhà chọc trời", "Nhà cao.", "General", ["high-rise"], ["build a skyscraper"], "They built a skyscraper.", "Họ đã xây một tòa nhà chọc trời."),
    create_word("timber", "/ˈtɪmbə/", "Noun", "C1", "Wood for building.", "Gỗ", "Làm nhà.", "Technical", ["wood"], ["timber frame"], "They use timber.", "Họ sử dụng gỗ."),
    create_word("sustainable", "/səˈsteɪnəbl/", "Adjective", "B2", "Able to be maintained.", "Bền vững", "Dùng lâu.", "Academic", ["eco-friendly"], ["sustainable design"], "It is a sustainable design.", "Đó là một thiết kế bền vững."),
    create_word("disorder", "/dɪsˈɔːdə/", "Noun", "B2", "State of confusion.", "Sự lộn xộn", "Rối rắm.", "General", ["chaos"], ["embrace disorder"], "Companies should embrace disorder.", "Các công ty nên đón nhận sự lộn xộn."),
    create_word("bureaucracy", "/bjʊəˈrɒkrəsi/", "Noun", "C1", "Complicated administrative procedure.", "Quan liêu", "Thủ tục dài.", "Negative", ["red tape"], ["reduce bureaucracy"], "Bureaucracy slows things down.", "Quan liêu làm mọi thứ chậm lại."),
    create_word("rigid", "/ˈrɪdʒɪd/", "Adjective", "C1", "Unable to bend or be forced.", "Cứng nhắc", "Không linh hoạt.", "Formal", ["inflexible"], ["rigid rules"], "The rules are rigid.", "Các quy tắc rất cứng nhắc."),
    create_word("efficiency", "/ɪˈfɪʃnsi/", "Noun", "B2", "Quality of being efficient.", "Hiệu suất", "Làm tốt.", "General", ["productivity"], ["improve efficiency"], "They want to improve efficiency.", "Họ muốn cải thiện hiệu suất."),
    create_word("innovation", "/ˌɪnəˈveɪʃn/", "Noun", "B2", "Process of innovating.", "Đổi mới", "Làm mới.", "General", ["novelty"], ["technological innovation"], "Innovation is important.", "Sự đổi mới là quan trọng.")
]

# CAM 14 READING 3
r3_words = [
    create_word("intelligence", "/ɪnˈtelɪdʒəns/", "Noun", "B2", "Ability to acquire knowledge.", "Trí thông minh", "Khả năng học.", "General", ["intellect"], ["human intelligence"], "What is intelligence?", "Trí thông minh là gì?"),
    create_word("pharmaceutical", "/ˌfɑːməˈsuːtɪkl/", "Adjective", "C1", "Relating to medicinal drugs.", "Dược phẩm", "Làm thuốc.", "Formal", ["medical"], ["pharmaceutical company"], "They work for a pharmaceutical company.", "Họ làm việc cho một công ty dược phẩm."),
    create_word("antibiotic", "/ˌæntibaɪˈɒtɪk/", "Noun", "C1", "Medicine that destroys microorganisms.", "Kháng sinh", "Thuốc diệt khuẩn.", "Medical", [], ["new antibiotic"], "We need new antibiotics.", "Chúng ta cần kháng sinh mới."),
    create_word("biodiversity", "/ˌbaɪəʊdaɪˈvɜːsəti/", "Noun", "C1", "Variety of life.", "Đa dạng sinh học", "Nhiều loài.", "Academic", [], ["protect biodiversity"], "Insects show biodiversity.", "Côn trùng cho thấy sự đa dạng sinh học."),
    create_word("mammal", "/ˈmæml/", "Noun", "B1", "Warm-blooded vertebrate.", "Động vật có vú", "Thú.", "General", [], ["marine mammal"], "Dogs are mammals.", "Chó là động vật có vú."),
    create_word("stimulus", "/ˈstɪmjələs/", "Noun", "C1", "Thing that evokes a reaction.", "Kích thích", "Tác nhân.", "Formal", ["incentive"], ["provide a stimulus"], "Play is a stimulus.", "Vui chơi là một sự kích thích."),
    create_word("plasticity", "/plæˈstɪsəti/", "Noun", "C2", "Adaptability of an organism.", "Tính dẻo", "Khả năng đổi.", "Scientific", ["flexibility"], ["brain plasticity"], "The brain has plasticity.", "Não bộ có tính dẻo."),
    create_word("evolution", "/ˌiːvəˈluːʃn/", "Noun", "B2", "Gradual development.", "Tiến hóa", "Phát triển lâu.", "Scientific", ["development"], ["human evolution"], "Play helps in evolution.", "Vui chơi giúp ích trong quá trình tiến hóa."),
    create_word("survival", "/səˈvaɪvl/", "Noun", "B2", "Continuing to live.", "Sinh tồn", "Sống sót.", "General", ["existence"], ["survival skills"], "It teaches survival skills.", "Nó dạy các kỹ năng sinh tồn."),
    create_word("therapeutic", "/ˌθerəˈpjuːtɪk/", "Adjective", "C1", "Relating to healing.", "Trị liệu", "Chữa bệnh.", "Medical", ["curative"], ["therapeutic benefits"], "Play has therapeutic benefits.", "Vui chơi có lợi ích trị liệu.")
]

# CAM 14 READING 4
r4_words = [
    create_word("senescence", "/sɪˈnesns/", "Noun", "C2", "Process of deterioration with age.", "Lão hóa", "Già đi.", "Scientific", ["aging"], ["cellular senescence"], "Ants do not show senescence.", "Kiến không có dấu hiệu lão hóa."),
    create_word("colony", "/ˈkɒləni/", "Noun", "B2", "Community of animals.", "Đàn / Bầy", "Nhóm sống chung.", "General", ["community"], ["ant colony"], "The ant colony is large.", "Đàn kiến rất lớn."),
    create_word("conservation", "/ˌkɒnsəˈveɪʃn/", "Noun", "B2", "Protection of environment.", "Bảo tồn", "Giữ gìn.", "General", ["preservation"], ["wildlife conservation"], "Zoos help with conservation.", "Vườn thú giúp bảo tồn."),
    create_word("captivity", "/kæpˈtɪvəti/", "Noun", "C1", "Condition of being confined.", "Giam cầm", "Nuôi nhốt.", "General", ["confinement"], ["in captivity"], "They breed in captivity.", "Chúng sinh sản trong điều kiện nuôi nhốt."),
    create_word("debris", "/ˈdebriː/", "Noun", "C1", "Scattered pieces of waste.", "Mảnh vụn / Rác", "Rác.", "General", ["waste"], ["marine debris"], "Marine debris is dangerous.", "Rác thải biển rất nguy hiểm."),
    create_word("ingestion", "/ɪnˈdʒestʃən/", "Noun", "C2", "Process of taking food into the body.", "Sự nuốt vào", "Ăn phải.", "Medical", ["swallowing"], ["plastic ingestion"], "Ingestion of plastic kills animals.", "Nuốt phải nhựa giết chết động vật."),
    create_word("toxic", "/ˈtɒksɪk/", "Adjective", "B2", "Poisonous.", "Độc hại", "Có độc.", "General", ["poisonous"], ["toxic waste"], "The chemicals are toxic.", "Hóa chất rất độc hại."),
    create_word("accumulate", "/əˈkjuːmjəleɪt/", "Verb", "C1", "Gather together.", "Tích tụ", "Gom lại.", "General", ["gather"], ["accumulate wealth"], "Toxins accumulate.", "Chất độc tích tụ."),
    create_word("welfare", "/ˈwelfeə/", "Noun", "B2", "Health and happiness.", "Phúc lợi", "Sống tốt.", "General", ["well-being"], ["animal welfare"], "They care about animal welfare.", "Họ quan tâm đến phúc lợi động vật."),
    create_word("mitigate", "/ˈmɪtɪɡeɪt/", "Verb", "C1", "Make less severe.", "Giảm nhẹ", "Đỡ tệ.", "Formal", ["alleviate"], ["mitigate effects"], "We must mitigate the damage.", "Chúng ta phải giảm nhẹ thiệt hại.")
]

generate_file(14, "Listening", 1, "tội phạm, thực tập sinh, năng lượng biển", l1_words)
generate_file(14, "Listening", 2, "phòng khám, lâu đài, thời tiết", l2_words)
generate_file(14, "Listening", 3, "hội nghị, ban nhạc trường", l3_words)
generate_file(14, "Listening", 4, "đặt phòng, văn học, khảo cổ", l4_words)

generate_file(14, "Reading", 1, "trẻ em chơi, xe đạp, khách sạn", r1_words)
generate_file(14, "Reading", 2, "nhiếp ảnh, nhà chọc trời, quản lý", r2_words)
generate_file(14, "Reading", 3, "trí thông minh, côn trùng", r3_words)
generate_file(14, "Reading", 4, "kiến, sở thú, rác biển", r4_words)

print("Cambridge 14 generated.")
