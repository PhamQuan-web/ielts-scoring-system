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

def build_file(id_str, title, desc, words):
    return {
        "id": id_str, "title": title, "description": desc,
        "wordCount": len(words), "category": "Listening" if "listening" in id_str else "Reading",
        "color": "from-teal-500 to-emerald-600" if "listening" in id_str else "from-red-500 to-orange-600",
        "isPro": True, "words": words
    }

# CAM 12 LISTENING 1
l1_words = [
    create_word("assistant", "/əˈsɪstənt/", "Noun", "A2", "A person who ranks below a senior person.", "Trợ lý", "Người giúp việc.", "General", ["helper"], ["kitchen assistant"], "I work as a kitchen assistant.", "Tôi làm trợ lý nhà bếp."),
    create_word("responsibility", "/rɪˌspɒnsəˈbɪləti/", "Noun", "B2", "The state of having a duty to deal with something.", "Trách nhiệm", "Việc phải làm.", "General", ["duty"], ["take responsibility"], "We might give you more responsibility.", "Chúng tôi có thể giao cho bạn nhiều trách nhiệm hơn."),
    create_word("footwear", "/ˈfʊtweə/", "Noun", "B1", "Outer coverings for the feet.", "Giày dép", "Đồ đi ở chân.", "Formal", ["shoes"], ["unsuitable footwear"], "None of you have unsuitable footwear.", "Không ai trong các bạn đi giày dép không phù hợp."),
    create_word("slippery", "/ˈslɪpəri/", "Adjective", "B2", "Difficult to hold firmly or stand on.", "Trơn trượt", "Dễ ngã.", "General", ["slick"], ["slippery floor"], "The floors can get very wet and slippery.", "Sàn nhà có thể rất ướt và trơn trượt."),
    create_word("bracelet", "/ˈbreɪslət/", "Noun", "A2", "An ornamental band, hoop, or chain worn on the wrist.", "Vòng đeo tay", "Trang sức cổ tay.", "General", ["bangle"], ["gold bracelet"], "Some of you'll need to remove your bracelets.", "Một số bạn sẽ cần phải tháo vòng tay ra."),
    create_word("hazard", "/ˈhæzəd/", "Noun", "B2", "A danger or risk.", "Mối nguy hiểm", "Cái có thể gây hại.", "General", ["danger"], ["safety hazard"], "They can be a safety hazard.", "Chúng có thể là một mối nguy hiểm về an toàn."),
    create_word("route", "/ruːt/", "Noun", "B1", "A way or course taken in getting from a starting point to a destination.", "Tuyến đường", "Đường đi.", "General", ["path"], ["bus route"], "What is the best route?", "Tuyến đường tốt nhất là gì?"),
    create_word("helmet", "/ˈhelmɪt/", "Noun", "A2", "A hard or padded protective hat.", "Mũ bảo hiểm", "Đội bảo vệ đầu.", "General", ["headgear"], ["wear a helmet"], "You must wear a helmet.", "Bạn phải đội mũ bảo hiểm."),
    create_word("excursion", "/ɪkˈskɜːʃn/", "Noun", "B2", "A short journey or trip.", "Chuyến dã ngoại", "Đi chơi ngắn.", "General", ["trip"], ["school excursion"], "We went on an excursion.", "Chúng tôi đã đi dã ngoại."),
    create_word("stadium", "/ˈsteɪdiəm/", "Noun", "A2", "A sports arena with tiers of seats for spectators.", "Sân vận động", "Chỗ xem thể thao.", "General", ["arena"], ["football stadium"], "The match is at the stadium.", "Trận đấu diễn ra tại sân vận động.")
]

# CAM 12 LISTENING 2
l2_words = [
    create_word("conflict", "/ˈkɒnflɪkt/", "Noun", "B2", "A serious disagreement or argument.", "Sự xung đột", "Cãi vã gay gắt.", "General", ["dispute"], ["resolve a conflict"], "Conflict at work can cause stress.", "Xung đột tại nơi làm việc có thể gây căng thẳng."),
    create_word("executive", "/ɪɡˈzekjətɪv/", "Noun", "C1", "A person with senior managerial responsibility.", "Giám đốc điều hành", "Sếp lớn.", "Business", ["manager"], ["chief executive"], "Chief executives face a lot of pressure.", "Các giám đốc điều hành phải đối mặt với nhiều áp lực."),
    create_word("anxiety", "/æŋˈzaɪəti/", "Noun", "B2", "A feeling of worry, nervousness, or unease.", "Sự lo âu", "Cảm giác bồn chồn.", "General", ["worry"], ["feel anxiety"], "Many managers suffer from anxiety.", "Nhiều người quản lý bị lo âu."),
    create_word("structure", "/ˈstrʌktʃə/", "Noun", "B1", "The arrangement of and relations between the parts or elements of something complex.", "Cấu trúc", "Cách tổ chức.", "Academic", ["organization"], ["company structure"], "The company has a rigid structure.", "Công ty có một cấu trúc cứng nhắc."),
    create_word("minimize", "/ˈmɪnɪmaɪz/", "Verb", "C1", "Reduce to the smallest possible amount or degree.", "Giảm thiểu", "Làm cho ít nhất.", "Formal", ["reduce"], ["minimize risk"], "We need to minimize conflict.", "Chúng ta cần giảm thiểu xung đột."),
    create_word("resolve", "/rɪˈzɒlv/", "Verb", "B2", "Settle or find a solution to.", "Giải quyết", "Tìm ra cách giải.", "Formal", ["settle"], ["resolve an issue"], "They hired someone to resolve the conflicts.", "Họ đã thuê người để giải quyết các xung đột."),
    create_word("uncertainty", "/ʌnˈsɜːtnti/", "Noun", "B2", "The state of being uncertain.", "Sự không chắc chắn", "Không biết rõ.", "General", ["doubt"], ["feeling of uncertainty"], "Changes create a feeling of uncertainty.", "Những thay đổi tạo ra cảm giác không chắc chắn."),
    create_word("borrow", "/ˈbɒrəʊ/", "Verb", "A2", "Take and use with the intention of returning it.", "Mượn", "Mượn tạm.", "General", ["loan"], ["borrow a book"], "He will borrow a book from Beth.", "Anh ấy sẽ mượn một cuốn sách từ Beth."),
    create_word("source", "/sɔːs/", "Noun", "B1", "A place, person, or thing from which something comes.", "Nguồn", "Nơi bắt đầu.", "Academic", ["origin"], ["source material"], "He needs to read some source material.", "Anh ấy cần đọc một số tài liệu tham khảo (nguồn)."),
    create_word("category", "/ˈkætəɡəri/", "Noun", "B2", "A class or division of people or things.", "Hạng mục / Thể loại", "Nhóm cùng loại.", "Academic", ["class"], ["general category"], "It falls into the general category.", "Nó rơi vào hạng mục chung.")
]

# CAM 12 LISTENING 3
l3_words = [
    create_word("migratory", "/maɪˈɡreɪtəri/", "Adjective", "C1", "Relating to the regular seasonal movement of animals.", "Di cư", "Chuyển chỗ theo mùa.", "Scientific", ["nomadic"], ["migratory birds"], "Many birds are migratory.", "Nhiều loài chim là loài di cư."),
    create_word("mercury", "/ˈmɜːkjəri/", "Noun", "C1", "A heavy silvery-white metal that is liquid at ordinary temperatures.", "Thủy ngân", "Kim loại lỏng độc.", "Scientific", ["quicksilver"], ["mercury poisoning"], "Mercury is highly toxic.", "Thủy ngân rất độc hại."),
    create_word("contaminated", "/kənˈtæmɪneɪtɪd/", "Adjective", "C1", "Having been made impure by exposure to or addition of a poisonous or polluting substance.", "Bị ô nhiễm", "Nhiễm bẩn.", "Formal", ["polluted"], ["contaminated site"], "The birds fed at a contaminated site.", "Lũ chim đã ăn ở một địa điểm bị ô nhiễm."),
    create_word("implication", "/ˌɪmplɪˈkeɪʃn/", "Noun", "C1", "The conclusion that can be drawn from something.", "Hệ quả / Ý nghĩa", "Điều sẽ xảy ra.", "Academic", ["consequence"], ["important implication"], "What are the implications for humans?", "Những hệ quả đối với con người là gì?"),
    create_word("substantial", "/səbˈstænʃl/", "Adjective", "B2", "Of considerable importance, size, or worth.", "Đáng kể", "Nhiều, lớn.", "Formal", ["significant"], ["substantial amount"], "The effects can be quite substantial.", "Các tác động có thể khá đáng kể."),
    create_word("emission", "/ɪˈmɪʃn/", "Noun", "C1", "The production and discharge of something, especially gas or radiation.", "Sự phát thải", "Xả khí ra.", "Technical", ["discharge"], ["carbon emission"], "There are new regulations for mercury emissions.", "Có những quy định mới về phát thải thủy ngân."),
    create_word("implement", "/ˈɪmplɪment/", "Verb", "B2", "Put (a decision, plan, agreement, etc.) into effect.", "Thực hiện / Áp dụng", "Làm theo kế hoạch.", "Formal", ["execute"], ["implement a policy"], "It will cost billions to implement.", "Sẽ tốn hàng tỷ đô la để thực hiện."),
    create_word("wildlife", "/ˈwaɪldlaɪf/", "Noun", "B1", "Wild animals collectively.", "Động vật hoang dã", "Thú rừng.", "General", ["fauna"], ["protect wildlife"], "Some argue it's too much to pay to protect wildlife.", "Một số người lập luận rằng trả quá nhiều tiền để bảo vệ động vật hoang dã là không đáng."),
    create_word("magazine", "/ˌmæɡəˈziːn/", "Noun", "A2", "A periodical publication containing articles and illustrations.", "Tạp chí", "Báo nhiều trang.", "General", ["journal"], ["read a magazine"], "There is a seating area with magazines.", "Có một khu vực ghế ngồi với các tạp chí."),
    create_word("community", "/kəˈmjuːnəti/", "Noun", "B1", "A group of people living in the same place or having a particular characteristic in common.", "Cộng đồng", "Người cùng khu.", "General", ["society"], ["community room"], "There is a community room for meetings.", "Có một phòng sinh hoạt cộng đồng để họp.")
]

# CAM 12 LISTENING 4
l4_words = [
    create_word("acoustics", "/əˈkuːstɪks/", "Noun", "C1", "The properties or qualities of a room or building that determine how sound is transmitted in it.", "Âm học", "Khoa học âm thanh.", "Technical", [], ["study of acoustics"], "This lecture is about the science of acoustics.", "Bài giảng này sẽ về khoa học âm học."),
    create_word("decibel", "/ˈdesɪbel/", "Noun", "B2", "A unit used to measure the intensity of a sound.", "Đề-xi-ben", "Đơn vị đo tiếng ồn.", "Technical", [], ["sound in decibels"], "We measure sound levels in decibels.", "Chúng ta đo mức âm thanh bằng decibel."),
    create_word("soundscape", "/ˈsaʊndskeɪp/", "Noun", "C2", "The sounds heard in a particular location, considered as a whole.", "Cảnh quan âm thanh", "Toàn bộ âm thanh một nơi.", "Academic", [], ["urban soundscape"], "Researching urban soundscapes used to be simple.", "Việc nghiên cứu cảnh quan âm thanh đô thị từng rất đơn giản."),
    create_word("annoying", "/əˈnɔɪɪŋ/", "Adjective", "B1", "Causing irritation.", "Gây khó chịu", "Làm bực mình.", "General", ["irritating"], ["find it annoying"], "At what level does the sound become annoying?", "Ở mức độ nào thì âm thanh trở nên khó chịu?"),
    create_word("variation", "/ˌveəriˈeɪʃn/", "Noun", "B2", "A change or difference in condition.", "Sự biến đổi", "Sự khác biệt.", "Academic", ["fluctuation"], ["temperature variation"], "Maps can't capture the variation of sound.", "Bản đồ không thể nắm bắt được sự biến đổi của âm thanh."),
    create_word("perception", "/pəˈsepʃn/", "Noun", "B2", "The ability to see, hear, or become aware of something.", "Sự nhận thức / Cảm nhận", "Cách nhìn nhận.", "General", ["awareness"], ["public perception"], "People vary in their perceptions of noise.", "Mọi người có cảm nhận khác nhau về tiếng ồn."),
    create_word("crude", "/kruːd/", "Adjective", "C1", "Constructed in a rudimentary or makeshift way.", "Thô sơ / Sơ sài", "Làm qua loa.", "Formal", ["basic", "rough"], ["crude map"], "These noise maps are fairly crude.", "Những bản đồ tiếng ồn này khá thô sơ."),
    create_word("interrupted", "/ˌɪntəˈrʌptɪd/", "Adjective", "B2", "Stopped from continuing.", "Bị gián đoạn", "Bị cắt ngang.", "General", ["broken"], ["interrupted sleep"], "City-dwellers suffer from interrupted sleep.", "Cư dân thành phố thường bị mất ngủ (giấc ngủ bị gián đoạn)."),
    create_word("stress", "/stres/", "Noun", "B1", "A state of mental or emotional strain.", "Căng thẳng", "Áp lực tâm lý.", "General", ["tension"], ["levels of stress"], "Noise can lead to a rise in stress.", "Tiếng ồn có thể làm tăng mức độ căng thẳng."),
    create_word("composition", "/ˌkɒmpəˈzɪʃn/", "Noun", "C1", "The nature of something's ingredients.", "Thành phần", "Cấu tạo.", "Academic", ["makeup"], ["blood composition"], "Noise affects the composition of the blood.", "Tiếng ồn ảnh hưởng đến thành phần của máu.")
]

# CAM 12 READING 1
r1_words = [
    create_word("bark", "/bɑːk/", "Noun", "C1", "The tough protective outer sheath of the trunk.", "Vỏ cây", "Lớp ngoài của cây.", "Technical", ["covering"], ["tree bark"], "The cork oak has thick bark.", "Cây sồi bần có vỏ dày."),
    create_word("synthetic", "/sɪnˈθetɪk/", "Adjective", "C1", "Made by chemical synthesis.", "Tổng hợp / Nhân tạo", "Do con người làm ra.", "Scientific", ["artificial"], ["synthetic cork"], "Scientists developed a synthetic cork.", "Các nhà khoa học đã phát triển một loại nút bần tổng hợp."),
    create_word("cellular", "/ˈseljələ/", "Adjective", "C1", "Consisting of living cells.", "Thuộc tế bào", "Cấu tạo từ tế bào.", "Scientific", [], ["cellular structure"], "It has the same cellular structure.", "Nó có cùng cấu trúc tế bào."),
    create_word("harvest", "/ˈhɑːvɪst/", "Verb", "B2", "Gather a crop.", "Thu hoạch", "Gặt hái.", "General", ["reap"], ["annual harvest"], "Trees must be left for 25 years before the second harvest.", "Cây phải được để yên 25 năm trước lần thu hoạch thứ hai."),
    create_word("atmospheric", "/ˌætməsˈferɪk/", "Adjective", "C1", "Relating to the atmosphere of the earth.", "Thuộc khí quyển", "Liên quan đến không khí.", "Technical", [], ["atmospheric pressure"], "Bark should be stripped in dry atmospheric conditions.", "Vỏ cây nên được tước trong điều kiện khí quyển khô ráo."),
    create_word("fascinating", "/ˈfæsɪneɪtɪŋ/", "Adjective", "B2", "Extremely interesting.", "Hấp dẫn / Lôi cuốn", "Rất hay.", "General", ["captivating"], ["find it fascinating"], "Psychologists find collecting fascinating.", "Các nhà tâm lý học thấy việc sưu tập rất hấp dẫn."),
    create_word("variety", "/vəˈraɪəti/", "Noun", "B1", "The quality or state of being different.", "Sự đa dạng", "Nhiều loại khác nhau.", "General", ["diversity"], ["wide variety"], "It is one of the most varied activities.", "Nó là một trong những hoạt động đa dạng nhất."),
    create_word("purpose", "/ˈpɜːpəs/", "Noun", "B1", "The reason for which something is done.", "Mục đích", "Lý do làm việc gì.", "General", ["aim"], ["main purpose"], "What is the purpose of gaining knowledge?", "Mục đích của việc tiếp thu kiến thức là gì?"),
    create_word("knowledge", "/ˈnɒlɪdʒ/", "Noun", "A2", "Facts, information, and skills acquired through experience.", "Kiến thức", "Sự hiểu biết.", "General", ["understanding"], ["gain knowledge"], "Gaining knowledge is important.", "Tiếp thu kiến thức là điều quan trọng."),
    create_word("advantage", "/ədˈvɑːntɪdʒ/", "Noun", "B1", "A condition or circumstance that puts one in a favorable position.", "Lợi thế", "Điểm mạnh.", "General", ["benefit"], ["distinct advantage"], "What are the advantages of cork?", "Những lợi thế của nút bần là gì?")
]

# CAM 12 READING 2
r2_words = [
    create_word("vulnerable", "/ˈvʌlnərəbl/", "Adjective", "C1", "Susceptible to physical or emotional attack or harm.", "Dễ bị tổn thương", "Dễ bị hại.", "Formal", ["susceptible"], ["highly vulnerable"], "Food production is highly vulnerable.", "Sản xuất thực phẩm rất dễ bị tổn thương."),
    create_word("volatility", "/ˌvɒləˈtɪləti/", "Noun", "C2", "Liability to change rapidly and unpredictably.", "Sự biến động / Dễ thay đổi", "Lên xuống thất thường.", "Business", ["instability"], ["price volatility"], "Farmers face price volatility.", "Nông dân phải đối mặt với sự biến động giá cả."),
    create_word("mitigate", "/ˈmɪtɪɡeɪt/", "Verb", "C1", "Make less severe.", "Giảm nhẹ", "Làm cho đỡ tồi tệ.", "Formal", ["alleviate"], ["mitigate risk"], "Governments can help mitigate risks.", "Chính phủ có thể giúp giảm nhẹ rủi ro."),
    create_word("procurement", "/prəˈkjʊəmənt/", "Noun", "C2", "The action of obtaining equipment or supplies.", "Sự thu mua / Mua sắm", "Mua hàng hóa.", "Business", ["purchasing"], ["procurement of stock"], "The procurement of stocks can help.", "Việc thu mua hàng dự trữ có thể giúp ích."),
    create_word("ecosystem", "/ˈiːkəʊsɪstəm/", "Noun", "C1", "A biological community.", "Hệ sinh thái", "Môi trường sống.", "Academic", [], ["damaged ecosystem"], "Rewilding means restoring ecosystems.", "Tái hoang dã có nghĩa là khôi phục các hệ sinh thái."),
    create_word("restoration", "/ˌrestəˈreɪʃn/", "Noun", "C1", "Returning something to a former condition.", "Sự phục hồi", "Sửa lại như cũ.", "Formal", ["recovery"], ["mass restoration"], "It involves the restoration of damaged land.", "Nó liên quan đến việc phục hồi vùng đất bị hư hại."),
    create_word("predator", "/ˈpredətə/", "Noun", "C1", "An animal that preys on others.", "Thú săn mồi", "Con ăn thịt.", "Scientific", ["hunter"], ["large predator"], "Ecosystems without large predators behave differently.", "Các hệ sinh thái không có loài săn mồi lớn cư xử khác biệt."),
    create_word("governance", "/ˈɡʌvənəns/", "Noun", "C1", "The action or manner of governing.", "Sự quản trị", "Cách quản lý công ty/đất nước.", "Formal", ["administration"], ["corporate governance"], "There were failures of corporate governance.", "Đã có những thất bại trong quản trị doanh nghiệp."),
    create_word("meltdown", "/ˈmeltdaʊn/", "Noun", "C2", "A disastrous collapse or breakdown.", "Sự sụp đổ", "Hỏng bét.", "General", ["collapse"], ["financial meltdown"], "The 2008 financial meltdown caused problems.", "Sự sụp đổ tài chính năm 2008 đã gây ra nhiều vấn đề."),
    create_word("scrutiny", "/ˈskruːtəni/", "Noun", "C1", "Critical observation or examination.", "Sự giám sát kỹ lưỡng", "Nhìn rất kỹ.", "Formal", ["inspection"], ["intense scrutiny"], "Companies are under intense scrutiny.", "Các công ty đang bị giám sát chặt chẽ.")
]

# CAM 12 READING 3
r3_words = [
    create_word("reintroduction", "/ˌriːɪntrəˈdʌkʃn/", "Noun", "C1", "The action of putting a species back into a former habitat.", "Sự đưa trở lại tự nhiên", "Thả về rừng.", "Formal", [], ["airborne reintroduction"], "The reintroduction program helped tortoises.", "Chương trình đưa rùa trở lại tự nhiên đã giúp ích."),
    create_word("endangered", "/ɪnˈdeɪndʒəd/", "Adjective", "B2", "Seriously at risk of extinction.", "Bị đe dọa tuyệt chủng", "Sắp tuyệt chủng.", "General", ["threatened"], ["endangered species"], "The Galapagos tortoise is an endangered species.", "Rùa Galapagos là một loài có nguy cơ tuyệt chủng."),
    create_word("inhospitable", "/ˌɪnhɒˈspɪtəbl/", "Adjective", "C1", "(of an environment) harsh and difficult to live in.", "Khắc nghiệt / Không thân thiện", "Khó sống.", "Formal", ["harsh", "hostile"], ["inhospitable environment"], "They live in an inhospitable environment.", "Chúng sống trong một môi trường khắc nghiệt."),
    create_word("exploitation", "/ˌeksplɔɪˈteɪʃn/", "Noun", "C1", "The action of making use of and benefiting from resources.", "Sự khai thác", "Tận dụng tài nguyên.", "Academic", ["utilization"], ["historical exploitation"], "Whaling ships began the exploitation of tortoises.", "Các tàu săn cá voi đã bắt đầu việc khai thác rùa."),
    create_word("exacerbate", "/ɪɡˈzæsəbeɪt/", "Verb", "C2", "Make (a problem, bad situation, or negative feeling) worse.", "Làm trầm trọng thêm", "Làm cho tệ hơn.", "Formal", ["worsen", "aggravate"], ["exacerbate the problem"], "This exploitation was exacerbated by settlers.", "Sự khai thác này càng trở nên tồi tệ hơn bởi những người định cư."),
    create_word("intersection", "/ˌɪntəˈsekʃn/", "Noun", "C1", "A point at which two or more things intersect.", "Sự giao thoa", "Nơi gặp nhau.", "Formal", ["junction"], ["intersection of science and geography"], "The passage discusses the intersection of health and geography.", "Bài đọc thảo luận về sự giao thoa giữa y tế và địa lý."),
    create_word("geography", "/dʒiˈɒɡrəfi/", "Noun", "A2", "The study of the physical features of the earth.", "Địa lý", "Môn địa lý.", "General", [], ["health geography"], "Geography impacts public health.", "Địa lý ảnh hưởng đến sức khỏe cộng đồng."),
    create_word("disease", "/dɪˈziːz/", "Noun", "B1", "A disorder of structure or function.", "Căn bệnh", "Ốm đau.", "General", ["illness"], ["spread of disease"], "They track the spread of disease.", "Họ theo dõi sự lây lan của dịch bệnh."),
    create_word("prevalence", "/ˈprevələns/", "Noun", "C1", "The fact or condition of being prevalent; commonness.", "Sự phổ biến / Tỷ lệ mắc bệnh", "Có nhiều nơi.", "Formal", ["commonness"], ["disease prevalence"], "They map the prevalence of asthma.", "Họ lập bản đồ tỷ lệ mắc bệnh hen suyễn."),
    create_word("correlation", "/ˌkɒrəˈleɪʃn/", "Noun", "C1", "A mutual relationship or connection.", "Sự tương quan", "Có liên quan.", "Academic", ["connection"], ["positive correlation"], "There is a correlation between pollution and health.", "Có một sự tương quan giữa ô nhiễm và sức khỏe.")
]

# CAM 12 READING 4
r4_words = [
    create_word("archaeologist", "/ˌɑːkiˈɒlədʒɪst/", "Noun", "B2", "A person who studies human history through excavation.", "Nhà khảo cổ học", "Người đào đồ cổ.", "General", [], ["famous archaeologist"], "Archaeologists found ancient glass.", "Các nhà khảo cổ đã tìm thấy thủy tinh cổ."),
    create_word("glaze", "/ɡleɪz/", "Noun", "C1", "A vitreous substance fused on to the surface of pottery.", "Lớp men", "Lớp phủ bóng ngoài.", "Technical", ["coating"], ["glass glaze"], "Glass took the form of glazes.", "Thủy tinh có dạng như lớp men."),
    create_word("impurity", "/ɪmˈpjʊərəti/", "Noun", "C1", "The quality or condition of being impure.", "Tạp chất", "Chất bẩn lẫn vào.", "Technical", ["contaminant"], ["remove impurities"], "The colour was due to impurities in the material.", "Màu sắc là do các tạp chất trong vật liệu."),
    create_word("synthetic", "/sɪnˈθetɪk/", "Adjective", "C1", "Made by chemical synthesis.", "Tổng hợp / Nhân tạo", "Làm bằng hóa chất.", "Scientific", ["artificial"], ["synthetic material"], "They created synthetic colors.", "Họ đã tạo ra các màu sắc tổng hợp."),
    create_word("automated", "/ˈɔːtəmeɪtɪd/", "Adjective", "B2", "Operated by largely automatic equipment.", "Được tự động hóa", "Chạy bằng máy.", "Technical", ["automatic"], ["automated process"], "It became a fully automated process.", "Nó đã trở thành một quá trình hoàn toàn tự động."),
    create_word("refractive", "/rɪˈfræktɪv/", "Adjective", "C2", "Relating to the bending of light.", "Khúc xạ", "Bẻ cong ánh sáng.", "Scientific", [], ["refractive index"], "They studied the refractive index of glass.", "Họ nghiên cứu chỉ số khúc xạ của thủy tinh."),
    create_word("milestone", "/ˈmaɪlstəʊn/", "Noun", "C1", "A significant event or stage in the life, progress, or development of a person, nation, etc.", "Cột mốc quan trọng", "Dấu mốc đáng nhớ.", "General", ["landmark"], ["major milestone"], "This invention was a milestone.", "Phát minh này là một cột mốc quan trọng."),
    create_word("collapse", "/kəˈlæps/", "Verb", "B2", "Fall down or in; give way.", "Sụp đổ", "Đổ sụp.", "General", ["fall down"], ["economic collapse"], "The glass industry collapsed.", "Ngành công nghiệp thủy tinh đã sụp đổ."),
    create_word("craftsman", "/ˈkrɑːftsmən/", "Noun", "B2", "A worker skilled in a particular craft.", "Thợ thủ công", "Người làm đồ tay.", "General", ["artisan"], ["skilled craftsman"], "Venetian craftsmen were highly skilled.", "Những thợ thủ công Venice có tay nghề rất cao."),
    create_word("widespread", "/ˈwaɪdspred/", "Adjective", "B2", "Found or distributed over a large area or number of people.", "Rộng khắp / Phổ biến", "Lan rộng.", "General", ["extensive", "common"], ["widespread use"], "Glass became widespread in Europe.", "Thủy tinh trở nên phổ biến ở châu Âu.")
]

create_dir("output/cambridge_12")

write_json("output/cambridge_12/listening_test_1.json", build_file("cambridge_12_listening_test_1", "Cam 12 - Listening Test 1", "Từ vựng về trợ lý nhà bếp, leo núi.", l1_words))
write_json("output/cambridge_12/listening_test_2.json", build_file("cambridge_12_listening_test_2", "Cam 12 - Listening Test 2", "Từ vựng về quản lý xung đột, viết báo cáo.", l2_words))
write_json("output/cambridge_12/listening_test_3.json", build_file("cambridge_12_listening_test_3", "Cam 12 - Listening Test 3", "Từ vựng về ảnh hưởng thủy ngân, động vật.", l3_words))
write_json("output/cambridge_12/listening_test_4.json", build_file("cambridge_12_listening_test_4", "Cam 12 - Listening Test 4", "Từ vựng về âm học, tiếng ồn đô thị.", l4_words))

write_json("output/cambridge_12/reading_test_1.json", build_file("cambridge_12_reading_test_1", "Cam 12 - Reading Test 1", "Từ vựng về sồi bần, sở thích sưu tập.", r1_words))
write_json("output/cambridge_12/reading_test_2.json", build_file("cambridge_12_reading_test_2", "Cam 12 - Reading Test 2", "Từ vựng về nông nghiệp, quản trị, tái hoang dã.", r2_words))
write_json("output/cambridge_12/reading_test_3.json", build_file("cambridge_12_reading_test_3", "Cam 12 - Reading Test 3", "Từ vựng về rùa Galapagos, địa lý y tế.", r3_words))
write_json("output/cambridge_12/reading_test_4.json", build_file("cambridge_12_reading_test_4", "Cam 12 - Reading Test 4", "Từ vựng về lịch sử thủy tinh.", r4_words))

print("Cambridge 12 generated.")
