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

# CAM 15 LISTENING 1
l1_words = [
    create_word("recruitment", "/rɪˈkruːtmənt/", "Noun", "B2", "Action of finding new people to join.", "Tuyển dụng", "Tìm người.", "Business", ["hiring"], ["recruitment agency"], "I work for a recruitment agency.", "Tôi làm cho một đại lý tuyển dụng."),
    create_word("clerical", "/ˈklerɪkl/", "Adjective", "C1", "Concerned with office work.", "Hành chính", "Làm giấy tờ.", "Formal", ["administrative"], ["clerical work"], "They offer clerical jobs.", "Họ cung cấp các công việc văn thư."),
    create_word("temporary", "/ˈtemprəri/", "Adjective", "B1", "Lasting for a limited time.", "Tạm thời", "Không lâu dài.", "General", ["provisional"], ["temporary staff"], "I need temporary staff.", "Tôi cần nhân viên tạm thời."),
    create_word("sibling", "/ˈsɪblɪŋ/", "Noun", "C1", "Brother or sister.", "Anh chị em ruột", "Cùng cha mẹ.", "Formal", ["brother", "sister"], ["sibling rivalry"], "Birth order affects sibling rivalry.", "Thứ tự sinh ảnh hưởng đến sự ganh đua giữa anh chị em."),
    create_word("nurture", "/ˈnɜːtʃə/", "Verb", "C1", "Care for while growing.", "Nuôi dưỡng", "Chăm sóc.", "Formal", ["raise"], ["nature vs nurture"], "Parents nurture their children.", "Cha mẹ nuôi dưỡng con cái."),
    create_word("eucalyptus", "/ˌjuːkəˈlɪptəs/", "Noun", "C1", "Evergreen tree.", "Cây bạch đàn", "Cây gỗ.", "Technical", ["gum tree"], ["eucalyptus oil"], "Eucalyptus is common in Australia.", "Bạch đàn rất phổ biến ở Úc."),
    create_word("biodiversity", "/ˌbaɪəʊdaɪˈvɜːsəti/", "Noun", "C1", "Variety of life.", "Đa dạng sinh học", "Nhiều loài.", "Academic", [], ["protect biodiversity"], "It impacts biodiversity.", "Nó ảnh hưởng đến đa dạng sinh học."),
    create_word("indigenous", "/ɪnˈdɪdʒənəs/", "Adjective", "C2", "Native.", "Bản địa", "Gốc ở đó.", "Formal", ["native"], ["indigenous species"], "The tree is indigenous.", "Loài cây này là bản địa."),
    create_word("cultivation", "/ˌkʌltɪˈveɪʃn/", "Noun", "C1", "Action of cultivating land.", "Sự canh tác", "Trồng trọt.", "Formal", ["farming"], ["intensive cultivation"], "Cultivation has spread.", "Sự canh tác đã lan rộng."),
    create_word("disinfect", "/ˌdɪsɪnˈfekt/", "Verb", "C1", "Clean with a chemical.", "Khử trùng", "Làm sạch khuẩn.", "Medical", ["sterilize"], ["disinfect a wound"], "Leaves are used to disinfect.", "Lá được dùng để khử trùng.")
]

# CAM 15 LISTENING 2
l2_words = [
    create_word("amateur", "/ˈæmətə/", "Adjective", "B2", "Engaging on an unpaid basis.", "Nghiệp dư", "Làm vì đam mê.", "General", ["non-professional"], ["amateur group"], "They are an amateur theatre group.", "Họ là một nhóm kịch nghiệp dư."),
    create_word("demonstration", "/ˌdemənˈstreɪʃn/", "Noun", "B2", "Practical exhibition.", "Biểu diễn thử", "Làm mẫu.", "General", ["display"], ["craft demonstration"], "Watch a craft demonstration.", "Hãy xem một buổi biểu diễn thủ công."),
    create_word("commemorate", "/kəˈmeməreɪt/", "Verb", "C1", "Show respect in a ceremony.", "Tưởng niệm", "Kỷ niệm.", "Formal", ["honor"], ["commemorate a hero"], "The statue commemorates a hero.", "Bức tượng tưởng niệm một anh hùng."),
    create_word("adaptation", "/ˌædæpˈteɪʃn/", "Noun", "C1", "A film or play adapted from a written work.", "Tác phẩm chuyển thể", "Sách lên phim.", "Academic", ["version"], ["film adaptation"], "It's an adaptation of Dickens.", "Đó là bản chuyển thể từ Dickens."),
    create_word("satire", "/ˈsætaɪə/", "Noun", "C1", "Use of humor to expose stupidity.", "Châm biếm", "Cười nhạo.", "Academic", ["mockery"], ["political satire"], "The book is a satire.", "Cuốn sách là một tác phẩm châm biếm."),
    create_word("irrigation", "/ˌɪrɪˈɡeɪʃn/", "Noun", "C1", "Supply of water to crops.", "Thủy lợi", "Tưới tiêu.", "Technical", ["watering"], ["irrigation system"], "They built an irrigation system.", "Họ đã xây dựng một hệ thống tưới tiêu."),
    create_word("agriculture", "/ˈæɡrɪkʌltʃə/", "Noun", "B1", "Science of farming.", "Nông nghiệp", "Làm nông.", "Formal", ["farming"], ["modern agriculture"], "Agriculture is important.", "Nông nghiệp rất quan trọng."),
    create_word("livelihood", "/ˈlaɪvlihʊd/", "Noun", "C1", "Means of securing necessities.", "Sinh kế", "Cách kiếm sống.", "General", ["income"], ["earn a livelihood"], "Farming is their livelihood.", "Làm nông là sinh kế của họ."),
    create_word("cooperative", "/kəʊˈɒpərətɪv/", "Noun", "C1", "Business owned jointly.", "Hợp tác xã", "Làm chung.", "Business", ["partnership"], ["farmers' cooperative"], "They formed a cooperative.", "Họ đã thành lập một hợp tác xã."),
    create_word("infrastructure", "/ˈɪnfrəstrʌktʃə/", "Noun", "C1", "Basic physical structures.", "Cơ sở hạ tầng", "Đường sá.", "Formal", ["facilities"], ["improve infrastructure"], "We need better infrastructure.", "Chúng ta cần cơ sở hạ tầng tốt hơn.")
]

# CAM 15 LISTENING 3
l3_words = [
    create_word("initiative", "/ɪˈnɪʃətɪv/", "Noun", "C1", "A fresh approach.", "Sáng kiến", "Ý tưởng mới.", "Formal", ["plan"], ["council initiative"], "It is a new initiative.", "Đó là một sáng kiến mới."),
    create_word("closure", "/ˈkləʊʒə/", "Noun", "C1", "Act of closing.", "Sự đóng cửa", "Phong tỏa.", "Formal", ["shutdown"], ["road closure"], "They planned road closures.", "Họ đã lên kế hoạch đóng đường."),
    create_word("headline", "/ˈhedlaɪn/", "Noun", "B1", "Heading at the top of an article.", "Tiêu đề", "Tít báo.", "General", ["title"], ["newspaper headline"], "The headline attracts attention.", "Tiêu đề thu hút sự chú ý."),
    create_word("controversy", "/ˈkɒntrəvɜːsi/", "Noun", "C1", "Disagreement.", "Sự tranh cãi", "Bất đồng.", "Formal", ["dispute"], ["cause controversy"], "It created controversy.", "Nó tạo ra sự tranh cãi."),
    create_word("patronise", "/ˈpætrənaɪz/", "Verb", "C2", "Treat with apparent kindness that betrays superiority.", "Ra vẻ bề trên", "Coi thường.", "Formal", ["condescend"], ["patronising tone"], "Don't patronise the readers.", "Đừng tỏ ra bề trên với độc giả."),
    create_word("sanitation", "/ˌsænɪˈteɪʃn/", "Noun", "C1", "Conditions relating to public health.", "Vệ sinh môi trường", "Hệ thống sạch.", "Formal", ["hygiene"], ["poor sanitation"], "Sanitation improved health.", "Vệ sinh môi trường đã cải thiện sức khỏe."),
    create_word("hygiene", "/ˈhaɪdʒiːn/", "Noun", "B2", "Practices to maintain health.", "Vệ sinh cá nhân", "Giữ sạch sẽ.", "General", ["cleanliness"], ["personal hygiene"], "Hygiene is important.", "Vệ sinh cá nhân rất quan trọng."),
    create_word("luxury", "/ˈlʌkʃəri/", "Noun", "B1", "State of great comfort.", "Sự xa xỉ", "Đắt tiền.", "General", ["opulence"], ["luxury item"], "Soap was a luxury.", "Xà phòng từng là một sự xa xỉ."),
    create_word("repeal", "/rɪˈpiːl/", "Verb", "C2", "Revoke a law.", "Bãi bỏ", "Hủy luật.", "Legal", ["revoke"], ["repeal a tax"], "The tax was repealed.", "Thuế đã bị bãi bỏ."),
    create_word("ingredient", "/ɪnˈɡriːdiənt/", "Noun", "B1", "Foods combined to make a dish.", "Thành phần", "Nguyên liệu.", "General", ["component"], ["key ingredient"], "It is a key ingredient.", "Đó là một thành phần chính.")
]

# CAM 15 LISTENING 4
l4_words = [
    create_word("satisfaction", "/ˌsætɪsˈfækʃn/", "Noun", "B2", "Fulfillment of wishes.", "Sự hài lòng", "Vui vẻ.", "General", ["contentment"], ["customer satisfaction"], "We measure customer satisfaction.", "Chúng tôi đo lường sự hài lòng của khách hàng."),
    create_word("occupation", "/ˌɒkjuˈpeɪʃn/", "Noun", "B1", "A job.", "Nghề nghiệp", "Việc làm.", "Formal", ["job", "profession"], ["state your occupation"], "What is your occupation?", "Nghề nghiệp của bạn là gì?"),
    create_word("upgrade", "/ˌʌpˈɡreɪd/", "Verb", "B2", "Raise to a higher standard.", "Nâng cấp", "Làm tốt hơn.", "General", ["improve"], ["upgrade facilities"], "They will upgrade the park.", "Họ sẽ nâng cấp công viên."),
    create_word("invasive", "/ɪnˈveɪsɪv/", "Adjective", "C1", "Tending to spread harmfully.", "Xâm lấn", "Lan tràn.", "Technical", ["intrusive"], ["invasive species"], "Invasive species cause problems.", "Loài xâm lấn gây ra các vấn đề."),
    create_word("refrigeration", "/rɪˌfrɪdʒəˈreɪʃn/", "Noun", "C1", "Process of cooling.", "Sự làm lạnh", "Giữ lạnh.", "Technical", ["cooling"], ["domestic refrigeration"], "Refrigeration changed our diet.", "Việc làm lạnh đã thay đổi chế độ ăn của chúng ta."),
    create_word("perishable", "/ˈperɪʃəbl/", "Adjective", "C1", "Likely to decay quickly.", "Dễ hỏng", "Thiu nhanh.", "Formal", ["decomposable"], ["perishable goods"], "Meat is perishable.", "Thịt là hàng hóa dễ hỏng."),
    create_word("consumerism", "/kənˈsjuːmərɪzm/", "Noun", "C2", "Promotion of consumers' interests.", "Chủ nghĩa tiêu dùng", "Mua sắm.", "Academic", [], ["rise of consumerism"], "Consumerism increased.", "Chủ nghĩa tiêu dùng gia tăng."),
    create_word("revolution", "/ˌrevəˈluːʃn/", "Noun", "B2", "Overthrow of social order.", "Cách mạng", "Thay đổi lớn.", "General", ["transformation"], ["industrial revolution"], "The industrial revolution changed everything.", "Cách mạng công nghiệp đã thay đổi mọi thứ."),
    create_word("urbanisation", "/ˌɜːbənaɪˈzeɪʃn/", "Noun", "C1", "Making area urban.", "Đô thị hóa", "Biến thành phố.", "Academic", [], ["rapid urbanisation"], "Urbanisation is happening.", "Đô thị hóa đang diễn ra."),
    create_word("disposable", "/dɪˈspəʊzəbl/", "Adjective", "C1", "Intended to be thrown away.", "Dùng một lần", "Vứt đi.", "General", ["throwaway"], ["disposable income"], "People had more disposable income.", "Mọi người có nhiều thu nhập khả dụng hơn.")
]

# CAM 15 READING 1
r1_words = [
    create_word("monopoly", "/məˈnɒpəli/", "Noun", "C1", "Exclusive control.", "Sự độc quyền", "Một mình.", "Business", ["domination"], ["hold a monopoly"], "The Dutch wanted a monopoly.", "Hà Lan muốn sự độc quyền."),
    create_word("lucrative", "/ˈluːkrətɪv/", "Adjective", "C1", "Producing profit.", "Có lợi nhuận cao", "Béo bở.", "Formal", ["profitable"], ["lucrative trade"], "The spice trade was lucrative.", "Buôn bán gia vị rất béo bở."),
    create_word("commodity", "/kəˈmɒdəti/", "Noun", "C1", "A raw material.", "Hàng hóa", "Đồ bán.", "Business", ["goods"], ["valuable commodity"], "Spices were a commodity.", "Gia vị là một mặt hàng."),
    create_word("autonomous", "/ɔːˈtɒnəməs/", "Adjective", "C1", "Navigated by a computer.", "Tự hành", "Tự chạy.", "Technical", ["self-driving"], ["autonomous vehicle"], "Autonomous vehicles are coming.", "Xe tự hành đang đến."),
    create_word("collision", "/kəˈlɪʒn/", "Noun", "B2", "Striking violently.", "Sự va chạm", "Tai nạn.", "General", ["crash"], ["avoid collision"], "Cars can avoid collisions.", "Xe hơi có thể tránh va chạm."),
    create_word("instinct", "/ˈɪnstɪŋkt/", "Noun", "C1", "Innate pattern of behavior.", "Bản năng", "Sinh ra đã có.", "General", ["intuition"], ["human instinct"], "Exploration is an instinct.", "Khám phá là một bản năng."),
    create_word("frontier", "/ˈfrʌntɪə/", "Noun", "C1", "Extreme limit of understanding.", "Biên giới", "Nơi mới.", "Formal", ["boundary"], ["new frontier"], "Space is a new frontier.", "Vũ trụ là một biên giới mới."),
    create_word("intrinsic", "/ɪnˈtrɪnzɪk/", "Adjective", "C2", "Belonging naturally.", "Bản chất / Cốt lõi", "Vốn có.", "Formal", ["inherent"], ["intrinsic value"], "It is intrinsic to humans.", "Nó là bản chất cốt lõi của con người."),
    create_word("bias", "/ˈbaɪəs/", "Noun", "C1", "Prejudice.", "Thiên kiến", "Thiên vị.", "Formal", ["prejudice"], ["cultural bias"], "Explorers had cultural bias.", "Các nhà thám hiểm có thiên kiến văn hóa."),
    create_word("alien", "/ˈeɪliən/", "Adjective", "B2", "Belonging to a foreign place.", "Xa lạ", "Lạ lẫm.", "General", ["foreign"], ["alien environment"], "The environment was alien.", "Môi trường thật xa lạ.")
]

# CAM 15 READING 2
r2_words = [
    create_word("choreography", "/ˌkɒriˈɒɡrəfi/", "Noun", "C2", "Sequence of dance steps.", "Biên đạo múa", "Sắp xếp múa.", "Technical", [], ["dance choreography"], "Urban engineers study choreography.", "Các kỹ sư đô thị nghiên cứu biên đạo múa."),
    create_word("synchronization", "/ˌsɪŋkrənaɪˈzeɪʃn/", "Noun", "C1", "Operation at the same time.", "Đồng bộ hóa", "Làm cùng lúc.", "Technical", ["coordination"], ["perfect synchronization"], "Traffic needs synchronization.", "Giao thông cần sự đồng bộ."),
    create_word("improvisation", "/ˌɪmprəvaɪˈzeɪʃn/", "Noun", "C2", "Action of improvising.", "Sự ứng biến", "Ngẫu hứng.", "Formal", ["spontaneity"], ["skillful improvisation"], "Pedestrians use improvisation.", "Người đi bộ sử dụng sự ứng biến."),
    create_word("revival", "/rɪˈvaɪvl/", "Noun", "C1", "Improvement in condition.", "Sự hồi sinh", "Sống lại.", "General", ["resurgence"], ["revival project"], "It is a revival project.", "Đó là một dự án hồi sinh."),
    create_word("clone", "/kləʊn/", "Verb", "C1", "Propagate as a clone.", "Nhân bản", "Tạo bản sao.", "Technical", ["replicate"], ["clone an animal"], "They want to clone it.", "Họ muốn nhân bản nó."),
    create_word("permafrost", "/ˈpɜːməfrɒst/", "Noun", "C2", "Subsurface layer of soil frozen.", "Băng vĩnh cửu", "Đất đóng băng.", "Technical", [], ["melting permafrost"], "Permafrost is melting.", "Băng vĩnh cửu đang tan."),
    create_word("ethical", "/ˈeθɪkl/", "Adjective", "B2", "Relating to moral principles.", "Thuộc đạo đức", "Đúng sai.", "Formal", ["moral"], ["ethical concerns"], "There are ethical concerns.", "Có những lo ngại về đạo đức."),
    create_word("incongruity", "/ˌɪnkɒŋˈɡruːəti/", "Noun", "C2", "State of being incongruous.", "Sự phi lý", "Không khớp.", "Formal", ["incompatibility"], ["sense of incongruity"], "Humor relies on incongruity.", "Hài hước dựa trên sự phi lý."),
    create_word("contagious", "/kənˈteɪdʒəs/", "Adjective", "C1", "Spread from one to another.", "Dễ lây", "Lan truyền.", "General", ["infectious"], ["contagious laughter"], "Laughter is contagious.", "Tiếng cười dễ lây lan."),
    create_word("superiority", "/suːˌpɪəriˈɒrəti/", "Noun", "C1", "State of being superior.", "Sự ưu việt", "Hơn người.", "Formal", ["supremacy"], ["feeling of superiority"], "Jokes create superiority.", "Những câu chuyện cười tạo ra cảm giác ưu việt.")
]

# CAM 15 READING 3
r3_words = [
    create_word("sculpture", "/ˈskʌlptʃə/", "Noun", "B1", "Art of making forms.", "Điêu khắc", "Tượng.", "General", ["statue"], ["modern sculpture"], "He is known for his sculptures.", "Ông ấy nổi tiếng với các tác phẩm điêu khắc."),
    create_word("abstract", "/ˈæbstrækt/", "Adjective", "B2", "Existing in thought.", "Trừu tượng", "Không rõ hình.", "Academic", ["conceptual"], ["abstract art"], "His art is abstract.", "Nghệ thuật của ông ấy mang tính trừu tượng."),
    create_word("commission", "/kəˈmɪʃn/", "Verb", "C1", "Order something to be produced.", "Ủy nhiệm / Đặt làm", "Thuê.", "Formal", ["order"], ["commission a statue"], "He was commissioned.", "Ông ấy đã được ủy nhiệm."),
    create_word("desalination", "/ˌdiːsælɪˈneɪʃn/", "Noun", "C2", "Process of removing salt.", "Khử muối", "Lọc nước.", "Technical", [], ["solar desalination"], "Desalination provides water.", "Khử muối cung cấp nước."),
    create_word("scarcity", "/ˈskeəsəti/", "Noun", "C1", "State of being scarce.", "Sự khan hiếm", "Thiếu.", "Formal", ["shortage"], ["water scarcity"], "Water scarcity is an issue.", "Khan hiếm nước là một vấn đề."),
    create_word("portable", "/ˈpɔːtəbl/", "Adjective", "B2", "Easily carried.", "Di động", "Dễ mang.", "General", ["mobile"], ["portable device"], "It is a portable device.", "Đó là một thiết bị di động."),
    create_word("folklore", "/ˈfəʊklɔː/", "Noun", "C1", "Traditional beliefs.", "Văn hóa dân gian", "Truyện xưa.", "Academic", ["mythology"], ["local folklore"], "Fairy tales are folklore.", "Truyện cổ tích là văn hóa dân gian."),
    create_word("gruesome", "/ˈɡruːsəm/", "Adjective", "C2", "Causing repulsion.", "Kinh khủng", "Đáng sợ.", "Literary", ["ghastly"], ["gruesome details"], "The stories were gruesome.", "Các câu chuyện rất rùng rợn."),
    create_word("variant", "/ˈveəriənt/", "Noun", "C1", "A form that differs.", "Biến thể", "Bản khác.", "Formal", ["version"], ["regional variant"], "There are many variants.", "Có nhiều biến thể."),
    create_word("archetype", "/ˈɑːkitaɪp/", "Noun", "C2", "A typical example.", "Nguyên mẫu", "Mẫu gốc.", "Academic", ["prototype"], ["hero archetype"], "The wolf is an archetype.", "Sói là một nguyên mẫu.")
]

# CAM 15 READING 4
r4_words = [
    create_word("restoration", "/ˌrestəˈreɪʃn/", "Noun", "C1", "Returning to former condition.", "Sự phục hồi", "Sửa lại.", "Formal", ["repair"], ["ecological restoration"], "Restoration is important.", "Việc phục hồi là quan trọng."),
    create_word("deforestation", "/ˌdiːfɒrɪˈsteɪʃn/", "Noun", "B2", "Clearing of trees.", "Phá rừng", "Chặt cây.", "Academic", ["logging"], ["widespread deforestation"], "Deforestation is bad.", "Phá rừng là điều tồi tệ."),
    create_word("fertility", "/fəˈtɪləti/", "Noun", "C1", "Quality of being fertile.", "Sự màu mỡ", "Đất tốt.", "Formal", ["richness"], ["soil fertility"], "It improves soil fertility.", "Nó cải thiện độ màu mỡ của đất."),
    create_word("indigenous", "/ɪnˈdɪdʒənəs/", "Adjective", "C2", "Native.", "Bản địa", "Gốc ở đó.", "Formal", ["native"], ["indigenous tree"], "The tree is indigenous.", "Cây là loài bản địa."),
    create_word("erosion", "/ɪˈrəʊʒn/", "Noun", "C1", "Process of eroding.", "Sự xói mòn", "Mất đất.", "Technical", ["wearing away"], ["soil erosion"], "It prevents erosion.", "Nó ngăn chặn xói mòn."),
    create_word("whistle", "/ˈwɪsl/", "Verb", "B1", "Emit a high-pitched sound.", "Huýt sáo", "Thổi sáo.", "General", ["blow"], ["whistling language"], "They whistle to communicate.", "Họ huýt sáo để giao tiếp."),
    create_word("terrain", "/təˈreɪn/", "Noun", "C1", "Stretch of land.", "Địa hình", "Đất đai.", "Formal", ["landscape"], ["rough terrain"], "The terrain is difficult.", "Địa hình rất khó khăn."),
    create_word("greenwashing", "/ˈɡriːnwɒʃɪŋ/", "Noun", "C2", "Disinformation about environmental image.", "Tẩy xanh", "Giả vờ xanh.", "Business", [], ["corporate greenwashing"], "Companies use greenwashing.", "Các công ty sử dụng chiêu bài tẩy xanh."),
    create_word("scrutiny", "/ˈskruːtəni/", "Noun", "C1", "Critical observation.", "Sự giám sát", "Nhìn kỹ.", "Formal", ["inspection"], ["intense scrutiny"], "They face scrutiny.", "Họ đối mặt với sự giám sát."),
    create_word("transparent", "/trænsˈpærənt/", "Adjective", "B2", "Open to public scrutiny.", "Minh bạch", "Rõ ràng.", "General", ["clear"], ["transparent process"], "Business must be transparent.", "Kinh doanh phải minh bạch.")
]

generate_file(15, "Listening", 1, "tuyển dụng, bạch đàn", l1_words)
generate_file(15, "Listening", 2, "lễ hội, Mozambique", l2_words)
generate_file(15, "Listening", 3, "việc làm, báo chí", l3_words)
generate_file(15, "Listening", 4, "công viên, tủ lạnh", l4_words)

generate_file(15, "Reading", 1, "nhục đậu khấu, xe tự lái", r1_words)
generate_file(15, "Reading", 2, "voi ma mút, tiếng cười", r2_words)
generate_file(15, "Reading", 3, "Henry Moore, lọc nước", r3_words)
generate_file(15, "Reading", 4, "cây Huarango, huýt sáo", r4_words)

print("Cambridge 15 generated.")
