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

# CAM 10 LISTENING 1
l1_words = [
    create_word("accommodation", "/əˌkɒməˈdeɪʃn/", "Noun", "B1", "A room, group of rooms, or building in which someone may live or stay.", "Chỗ ở", "Nơi để ngủ.", "General", ["housing", "lodging"], ["book accommodation"], "The price includes accommodation.", "Giá bao gồm chỗ ở."),
    create_word("leisure", "/ˈleʒə/", "Noun", "B1", "Free time.", "Thời gian rảnh / Giải trí", "Lúc rảnh.", "General", ["recreation"], ["leisure club"], "They are improving the leisure club.", "Họ đang cải thiện câu lạc bộ giải trí."),
    create_word("facility", "/fəˈsɪləti/", "Noun", "B1", "A place, amenity, or piece of equipment provided for a particular purpose.", "Cơ sở vật chất", "Đồ dùng phục vụ.", "General", ["amenity"], ["sports facility"], "The facilities have been improved.", "Các cơ sở vật chất đã được cải thiện."),
    create_word("membership", "/ˈmembəʃɪp/", "Noun", "B1", "The state of being a member.", "Thẻ thành viên", "Tham gia hội.", "General", ["affiliation"], ["types of membership"], "There are different types of membership.", "Có các loại thẻ thành viên khác nhau."),
    create_word("competition", "/ˌkɒmpəˈtɪʃn/", "Noun", "A2", "The activity or condition of competing.", "Cuộc thi", "Đấu tài.", "General", ["contest"], ["design competition"], "It's a global design competition.", "Đó là một cuộc thi thiết kế toàn cầu."),
    create_word("innovation", "/ˌɪnəˈveɪʃn/", "Noun", "B2", "The action or process of innovating.", "Sự đổi mới", "Sáng tạo mới.", "General", ["novelty"], ["technological innovation"], "We are looking for innovation.", "Chúng tôi đang tìm kiếm sự đổi mới."),
    create_word("habitat", "/ˈhæbɪtæt/", "Noun", "B2", "The natural home or environment of an animal.", "Môi trường sống", "Chỗ ở của thú.", "General", ["environment"], ["maintain habitat"], "We must maintain the bear's habitat.", "Chúng ta phải duy trì môi trường sống của gấu."),
    create_word("expansion", "/ɪkˈspænʃn/", "Noun", "B2", "The action of becoming larger or more extensive.", "Sự mở rộng", "Làm to ra.", "General", ["growth"], ["habitat expansion"], "There needs to be an emphasis on expansion.", "Cần phải nhấn mạnh vào sự mở rộng."),
    create_word("survival", "/səˈvaɪvl/", "Noun", "B2", "The state or fact of continuing to live.", "Sự sinh tồn", "Sống sót.", "General", ["existence"], ["threat to survival"], "Their survival is threatened.", "Sự sinh tồn của chúng bị đe dọa."),
    create_word("preserve", "/prɪˈzɜːv/", "Verb", "B2", "Maintain something in its original state.", "Bảo tồn", "Giữ nguyên.", "General", ["conserve"], ["preserve nature"], "We need to preserve the forest.", "Chúng ta cần bảo tồn khu rừng.")
]

# CAM 10 LISTENING 2
l2_words = [
    create_word("dentist", "/ˈdentɪst/", "Noun", "A2", "A person qualified to treat the diseases and conditions that affect the teeth.", "Nha sĩ", "Bác sĩ răng.", "General", [], ["visit the dentist"], "I have an appointment at the dentist.", "Tôi có một cuộc hẹn ở nha sĩ."),
    create_word("lighting", "/ˈlaɪtɪŋ/", "Noun", "B1", "Equipment in a room, building, or street for producing light.", "Hệ thống ánh sáng", "Đèn đóm.", "General", ["illumination"], ["poor lighting"], "The street needs better lighting.", "Đường phố cần hệ thống chiếu sáng tốt hơn."),
    create_word("initiative", "/ɪˈnɪʃətɪv/", "Noun", "C1", "An act or strategy intended to resolve a difficulty.", "Sáng kiến", "Ý tưởng mới.", "Formal", ["plan", "scheme"], ["new initiative"], "The idea for these initiatives came from the public.", "Ý tưởng cho các sáng kiến này xuất phát từ công chúng."),
    create_word("consultation", "/ˌkɒnslˈteɪʃn/", "Noun", "C1", "The action or process of formally consulting or discussing.", "Sự tham vấn", "Hỏi ý kiến.", "Formal", ["discussion"], ["public consultation"], "They conducted an extensive consultation.", "Họ đã tiến hành một cuộc tham vấn rộng rãi."),
    create_word("renowned", "/rɪˈnaʊnd/", "Adjective", "C1", "Known or talked about by many people; famous.", "Nổi tiếng / Danh tiếng", "Được biết đến nhiều.", "Formal", ["famous", "celebrated"], ["internationally renowned"], "She is an internationally renowned architect.", "Bà là một kiến trúc sư nổi tiếng thế giới."),
    create_word("architect", "/ˈɑːkɪtekt/", "Noun", "B1", "A person who designs buildings.", "Kiến trúc sư", "Người vẽ nhà.", "General", ["designer"], ["famous architect"], "The architect designed the new pool.", "Kiến trúc sư đã thiết kế hồ bơi mới."),
    create_word("feature", "/ˈfiːtʃə/", "Noun", "B2", "A distinctive attribute or aspect of something.", "Đặc điểm / Tính năng", "Điểm nổi bật.", "General", ["characteristic"], ["modern features"], "It has up-to-the-minute features.", "Nó có những tính năng hiện đại nhất."),
    create_word("recycling", "/ˌriːˈsaɪklɪŋ/", "Noun", "B1", "The action or process of converting waste into reusable material.", "Sự tái chế", "Dùng lại đồ cũ.", "General", ["reusing"], ["recycling system"], "It uses a unique recycling system.", "Nó sử dụng một hệ thống tái chế độc đáo."),
    create_word("seawater", "/ˈsiːwɔːtə/", "Noun", "B1", "Water from a sea or ocean.", "Nước biển", "Nước mặn.", "General", ["salt water"], ["use seawater"], "The pool enables seawater to be used.", "Hồ bơi cho phép sử dụng nước biển."),
    create_word("chlorine", "/ˈklɔːriːn/", "Noun", "C1", "A toxic, irritant, pale green gas used for water purification.", "Clo", "Hóa chất làm sạch.", "Technical", [], ["chlorine smell"], "The pool uses less chlorine.", "Hồ bơi sử dụng ít clo hơn.")
]

# CAM 10 LISTENING 3
l3_words = [
    create_word("pollution", "/pəˈluːʃn/", "Noun", "B1", "The presence of a substance that has harmful effects.", "Sự ô nhiễm", "Làm bẩn môi trường.", "General", ["contamination"], ["marine pollution"], "Dolphins suffer from pollution.", "Cá heo bị ảnh hưởng bởi ô nhiễm."),
    create_word("threat", "/θret/", "Noun", "B2", "A person or thing likely to cause damage or danger.", "Mối đe dọa", "Nguy hiểm.", "General", ["danger", "menace"], ["pose a threat"], "Pollution is a major threat.", "Ô nhiễm là một mối đe dọa lớn."),
    create_word("charity", "/ˈtʃærəti/", "Noun", "B1", "An organization set up to provide help and raise money for those in need.", "Tổ chức từ thiện", "Hội giúp người.", "General", ["non-profit"], ["animal charity"], "It's a fast-growing animal charity.", "Đây là một tổ chức từ thiện vì động vật đang phát triển nhanh."),
    create_word("education", "/ˌedʒuˈkeɪʃn/", "Noun", "B1", "The process of receiving or giving systematic instruction.", "Sự giáo dục", "Việc dạy học.", "General", ["teaching"], ["work in education"], "We are proud of our work in education.", "Chúng tôi tự hào về công việc của mình trong lĩnh vực giáo dục."),
    create_word("campaign", "/kæmˈpeɪn/", "Noun", "B2", "An organized course of action to achieve a goal.", "Chiến dịch", "Hoạt động chung.", "General", ["movement"], ["support a campaign"], "The charity supports campaigns.", "Tổ chức từ thiện hỗ trợ các chiến dịch."),
    create_word("policy", "/ˈpɒləsi/", "Noun", "B2", "A course or principle of action.", "Chính sách", "Đường lối.", "Formal", ["strategy"], ["fishing policy"], "We want changes in fishing policy.", "Chúng tôi muốn thay đổi chính sách đánh bắt cá."),
    create_word("expertise", "/ˌekspɜːˈtiːz/", "Noun", "C1", "Expert skill or knowledge in a particular field.", "Chuyên môn", "Kỹ năng giỏi.", "Formal", ["skill", "knowledge"], ["dolphin expertise"], "They need a biologist with dolphin expertise.", "Họ cần một nhà sinh vật học có chuyên môn về cá heo."),
    create_word("monitor", "/ˈmɒnɪtə/", "Verb", "B2", "Observe and check the progress or quality of something.", "Giám sát / Theo dõi", "Xem xét.", "Formal", ["observe", "track"], ["monitor populations"], "We need to monitor dolphin populations.", "Chúng ta cần theo dõi quần thể cá heo."),
    create_word("voluntary", "/ˈvɒləntri/", "Adjective", "B2", "Done, given, or acting of one's own free will.", "Tự nguyện", "Tự làm không ép.", "General", ["optional"], ["voluntary basis"], "People give their services on a voluntary basis.", "Mọi người cung cấp dịch vụ của họ một cách tự nguyện."),
    create_word("observation", "/ˌɒbzəˈveɪʃn/", "Noun", "B2", "The action or process of observing.", "Sự quan sát", "Theo dõi.", "General", ["monitoring"], ["field observation"], "Volunteers work in observation.", "Các tình nguyện viên làm công việc quan sát.")
]

# CAM 10 LISTENING 4
l4_words = [
    create_word("appliance", "/əˈplaɪəns/", "Noun", "B2", "A device or piece of equipment designed to perform a specific task.", "Thiết bị", "Máy móc trong nhà.", "General", ["device", "gadget"], ["domestic appliance"], "Design a new domestic kitchen appliance.", "Thiết kế một thiết bị nhà bếp gia dụng mới."),
    create_word("innovative", "/ˈɪnəveɪtɪv/", "Adjective", "B2", "Featuring new methods; advanced and original.", "Đổi mới / Sáng tạo", "Mới mẻ.", "General", ["inventive", "original"], ["innovative approach"], "We must adopt an innovative approach.", "Chúng ta phải áp dụng một cách tiếp cận đổi mới."),
    create_word("existing", "/ɪɡˈzɪstɪŋ/", "Adjective", "B2", "In existence or operation at the time under consideration.", "Hiện có", "Đang có sẵn.", "General", ["current", "present"], ["existing technology"], "Use existing technology in a new way.", "Sử dụng công nghệ hiện có theo một cách mới."),
    create_word("expansion", "/ɪkˈspænʃn/", "Noun", "B2", "The action of becoming larger.", "Sự mở rộng", "Phát triển to ra.", "General", ["growth"], ["sudden expansion"], "What caused the port's sudden expansion?", "Điều gì đã gây ra sự mở rộng đột ngột của bến cảng?"),
    create_word("decline", "/dɪˈklaɪn/", "Verb", "B2", "Become smaller, fewer, or less; decrease.", "Suy tàn / Giảm sút", "Kém đi.", "General", ["decrease", "deteriorate"], ["port declined"], "The port declined in the twentieth century.", "Bến cảng đã suy tàn vào thế kỷ 20."),
    create_word("exhibition", "/ˌeksɪˈbɪʃn/", "Noun", "B1", "A public display of items.", "Triển lãm", "Trưng bày.", "General", ["display"], ["special exhibition"], "There is a special exhibition.", "Có một cuộc triển lãm đặc biệt."),
    create_word("nanotechnology", "/ˌnænəʊtekˈnɒlədʒi/", "Noun", "C2", "The branch of technology dealing with dimensions less than 100 nanometers.", "Công nghệ nano", "Công nghệ siêu nhỏ.", "Scientific", [], ["field of nanotechnology"], "The lecture is about nanotechnology.", "Bài giảng nói về công nghệ nano."),
    create_word("particle", "/ˈpɑːtɪkl/", "Noun", "C1", "A minute portion of matter.", "Hạt / Phần tử", "Cái cực nhỏ.", "Scientific", ["speck", "fragment"], ["nano particle"], "It involves manipulating particles.", "Nó liên quan đến việc thao tác các hạt."),
    create_word("application", "/ˌæplɪˈkeɪʃn/", "Noun", "B2", "The practical use or relevance of something.", "Ứng dụng", "Đem vào thực tế.", "Formal", ["use", "implementation"], ["practical application"], "What are the applications of this?", "Ứng dụng của điều này là gì?"),
    create_word("molecule", "/ˈmɒlɪkjuːl/", "Noun", "C1", "A group of atoms bonded together.", "Phân tử", "Nhóm nguyên tử.", "Scientific", [], ["water molecule"], "They work at the level of molecules.", "Họ làm việc ở cấp độ phân tử.")
]

# CAM 10 READING 1
r1_words = [
    create_word("stepwell", "/ˈstepwel/", "Noun", "C2", "A well or pond in which the water is reached by descending a set of steps.", "Giếng bậc thang", "Giếng có bậc thang xuống.", "Technical", [], ["ancient stepwell"], "Stepwells are unique to India.", "Giếng bậc thang là độc nhất ở Ấn Độ."),
    create_word("groundwater", "/ˈɡraʊndwɔːtə/", "Noun", "C1", "Water held underground in the soil or in pores and crevices in rock.", "Nước ngầm", "Nước dưới đất.", "Technical", [], ["access groundwater"], "They needed access to clean groundwater.", "Họ cần tiếp cận nguồn nước ngầm sạch."),
    create_word("irrigation", "/ˌɪrɪˈɡeɪʃn/", "Noun", "C1", "The supply of water to land or crops to help growth.", "Sự tưới tiêu", "Dẫn nước vào ruộng.", "Technical", ["watering"], ["irrigation system"], "Water was used for irrigation.", "Nước được dùng để tưới tiêu."),
    create_word("utilitarian", "/ˌjuːtɪlɪˈteəriən/", "Adjective", "C2", "Designed to be useful or practical rather than attractive.", "Thực dụng", "Có ích là chính.", "Formal", ["practical", "functional"], ["utilitarian application"], "Its significance goes beyond its utilitarian application.", "Ý nghĩa của nó vượt xa ứng dụng thực dụng."),
    create_word("architecturally", "/ˌɑːkɪˈtektʃərəli/", "Adverb", "C1", "In terms of architecture or the design of buildings.", "Về mặt kiến trúc", "Liên quan đến thiết kế.", "Formal", ["structurally"], ["architecturally complex"], "They are architecturally complex.", "Chúng phức tạp về mặt kiến trúc."),
    create_word("monument", "/ˈmɒnjumənt/", "Noun", "B2", "A statue, building, or other structure erected to commemorate a notable person or event.", "Đài kỷ niệm / Di tích", "Công trình ghi nhớ.", "General", ["memorial"], ["ancient monument"], "Many of these monuments have been saved.", "Nhiều di tích này đã được cứu vãn."),
    create_word("ingenuity", "/ˌɪndʒəˈnjuːəti/", "Noun", "C2", "The quality of being clever, original, and inventive.", "Sự khéo léo / Tài tình", "Trí thông minh sáng tạo.", "Formal", ["inventiveness", "creativity"], ["human ingenuity"], "They serve as a reminder of human ingenuity.", "Chúng đóng vai trò như một lời nhắc nhở về sự khéo léo của con người."),
    create_word("overbearing", "/ˌəʊvəˈbeərɪŋ/", "Adjective", "C2", "Unpleasantly or arrogantly domineering.", "Hống hách / Độc đoán", "Bắt người khác nghe theo.", "Formal", ["domineering", "bossy"], ["overbearing leader"], "It can happen when the leader is overbearing.", "Nó có thể xảy ra khi người lãnh đạo hống hách."),
    create_word("interchange", "/ˈɪntətʃeɪndʒ/", "Noun", "C1", "The action of sharing or exchanging ideas or information.", "Sự trao đổi", "Trao đổi ý kiến.", "Formal", ["exchange", "sharing"], ["free interchange of ideas"], "It encouraged a free interchange of ideas.", "Nó khuyến khích sự trao đổi ý tưởng tự do."),
    create_word("revolutionise", "/ˌrevəˈluːʃənaɪz/", "Verb", "C1", "Change (something) radically or fundamentally.", "Cách mạng hóa", "Thay đổi hoàn toàn.", "Formal", ["transform"], ["revolutionise an industry"], "They revolutionised attitudes to design.", "Họ đã cách mạng hóa thái độ đối với thiết kế.")
]

# CAM 10 READING 2
r2_words = [
    create_word("application", "/ˌæplɪˈkeɪʃn/", "Noun", "B1", "A formal request to an authority for something.", "Đơn xin / Hồ sơ", "Giấy xin xỏ.", "General", ["request", "claim"], ["application form"], "Fill out the application form.", "Hãy điền vào mẫu đơn xin."),
    create_word("photocopy", "/ˈfəʊtəʊkɒpi/", "Noun", "A2", "A photographic copy of a printed or written document.", "Bản sao", "Tờ giấy copy.", "General", ["copy", "duplicate"], ["submit photocopies"], "Photocopies are acceptable.", "Các bản sao được chấp nhận."),
    create_word("processing", "/ˈprəʊsesɪŋ/", "Noun", "B2", "The series of operations performed in the making or treatment of a product.", "Quá trình xử lý", "Giải quyết giấy tờ.", "Formal", ["handling"], ["processing time"], "It will affect processing time.", "Nó sẽ ảnh hưởng đến thời gian xử lý."),
    create_word("compensation", "/ˌkɒmpenˈseɪʃn/", "Noun", "C1", "Something, typically money, awarded to someone as a recompense for loss, injury, or suffering.", "Sự bồi thường", "Đền bù thiệt hại.", "Formal", ["recompense", "damages"], ["claim compensation"], "You can claim compensation for lost items.", "Bạn có thể yêu cầu bồi thường cho các mặt hàng bị mất."),
    create_word("receipt", "/rɪˈsiːt/", "Noun", "B1", "A written or printed statement acknowledging that something has been paid for or that goods have been received.", "Biên lai", "Giấy báo nhận tiền.", "General", ["voucher", "slip"], ["keep the receipt"], "Send us the original receipt.", "Hãy gửi cho chúng tôi biên lai gốc."),
    create_word("evidence", "/ˈevɪdəns/", "Noun", "B2", "The available body of facts or information indicating whether a belief or proposition is true or valid.", "Bằng chứng", "Chứng cứ.", "Formal", ["proof"], ["provide evidence"], "Provide photographs as evidence.", "Cung cấp hình ảnh làm bằng chứng."),
    create_word("retain", "/rɪˈteɪn/", "Verb", "C1", "Continue to have (something); keep possession of.", "Giữ lại", "Không vứt đi.", "Formal", ["keep", "maintain"], ["retain packaging"], "Please retain the original packaging.", "Vui lòng giữ lại bao bì gốc."),
    create_word("inspect", "/ɪnˈspekt/", "Verb", "C1", "Look at (someone or something) closely, typically to assess their condition or to discover any shortcomings.", "Kiểm tra / Thanh tra", "Xem kỹ.", "Formal", ["examine", "check"], ["inspect the damage"], "We may need to inspect the items.", "Chúng tôi có thể cần phải kiểm tra các mặt hàng."),
    create_word("restriction", "/rɪˈstrɪkʃn/", "Noun", "B2", "A limiting condition or measure, especially a legal one.", "Sự hạn chế / Quy định giới hạn", "Sự cấm cản.", "Formal", ["limitation", "constraint"], ["time restriction"], "There are time restrictions on claims.", "Có những hạn chế về thời gian đối với các yêu cầu bồi thường."),
    create_word("recipient", "/rɪˈsɪpiənt/", "Noun", "C1", "A person or thing that receives or is awarded something.", "Người nhận", "Kẻ được cho.", "Formal", ["receiver"], ["recipient of the item"], "The claim can be made by the recipient.", "Người nhận có thể đưa ra yêu cầu bồi thường.")
]

# CAM 10 READING 3
r3_words = [
    create_word("tourism", "/ˈtʊərɪzəm/", "Noun", "A2", "The commercial organization and operation of vacations and visits to places of interest.", "Ngành du lịch", "Việc đi chơi xa.", "General", ["travel industry"], ["mass tourism"], "Tourism is a major industry.", "Du lịch là một ngành công nghiệp lớn."),
    create_word("traverse", "/trəˈvɜːs/", "Verb", "C2", "Travel across or through.", "Đi ngang qua", "Băng qua.", "Formal", ["cross", "navigate"], ["traverse great distances"], "Early man traversed great distances.", "Người nguyên thủy đã đi qua những khoảng cách rất lớn."),
    create_word("conviction", "/kənˈvɪkʃn/", "Noun", "C1", "A firmly held belief or opinion.", "Niềm tin", "Sự tin tưởng mạnh mẽ.", "Formal", ["belief", "certainty"], ["religious conviction"], "They travelled for religious conviction.", "Họ đi du lịch vì niềm tin tôn giáo."),
    create_word("aristocrat", "/ˈærɪstəkræt/", "Noun", "C1", "A member of the aristocracy.", "Nhà quý tộc", "Người thuộc tầng lớp cao.", "Historical", ["noble"], ["wealthy aristocrat"], "Wealthy aristocrats travelled for pleasure.", "Những nhà quý tộc giàu có đi du lịch để giải trí."),
    create_word("phenomenon", "/fəˈnɒmɪnən/", "Noun", "C1", "A fact or situation that is observed to exist or happen.", "Hiện tượng", "Sự việc đáng chú ý.", "Academic", ["occurrence"], ["twentieth-century phenomenon"], "Mass tourism is a modern phenomenon.", "Du lịch đại chúng là một hiện tượng hiện đại."),
    create_word("advent", "/ˈædvent/", "Noun", "C1", "The arrival of a notable person, thing, or event.", "Sự xuất hiện / Kỷ nguyên", "Lúc bắt đầu.", "Formal", ["arrival", "emergence"], ["advent of mass tourism"], "The advent of the jet aircraft changed things.", "Sự ra đời của máy bay phản lực đã thay đổi mọi thứ."),
    create_word("subsequent", "/ˈsʌbsɪkwənt/", "Adjective", "C1", "Coming after something in time; following.", "Tiếp theo / Xảy ra sau", "Cái đến sau.", "Formal", ["following", "successive"], ["subsequent development"], "The subsequent development led to rapid growth.", "Sự phát triển tiếp theo dẫn đến sự tăng trưởng nhanh chóng."),
    create_word("expansion", "/ɪkˈspænʃn/", "Noun", "B2", "The action of becoming larger or more extensive.", "Sự mở rộng", "Làm to ra.", "General", ["growth", "increase"], ["expansion of international travel"], "This signalled the expansion of travel.", "Điều này báo hiệu sự mở rộng của việc đi lại."),
    create_word("segment", "/ˈseɡmənt/", "Noun", "C1", "Each of the parts into which something is or may be divided.", "Mảng / Phân khúc", "Một phần nhỏ.", "Business", ["part", "section"], ["market segment"], "It is a large segment of the service industry.", "Nó là một mảng lớn của ngành dịch vụ."),
    create_word("commodity", "/kəˈmɒdəti/", "Noun", "C1", "A raw material or primary agricultural product that can be bought and sold.", "Hàng hóa", "Món đồ bán ra tiền.", "Business", ["goods"], ["largest commodity"], "Tourism has become the largest commodity.", "Du lịch đã trở thành loại hàng hóa lớn nhất.")
]

# CAM 10 READING 4
r4_words = [
    create_word("drought", "/draʊt/", "Noun", "B2", "A prolonged period of abnormally low rainfall.", "Hạn hán", "Trời không mưa.", "General", ["dry spell"], ["severe drought"], "Drought makes fires worse.", "Hạn hán làm cho hỏa hoạn tồi tệ hơn."),
    create_word("menace", "/ˈmenəs/", "Noun", "C1", "A person or thing that is likely to cause harm; a threat or danger.", "Mối đe dọa", "Cái nguy hiểm.", "Formal", ["threat", "danger"], ["increasing menace"], "Wildfires are an increasing menace.", "Cháy rừng đang là một mối đe dọa ngày càng tăng."),
    create_word("erratically", "/ɪˈrætɪkli/", "Adverb", "C2", "In a manner that is not even or regular in pattern or movement; unpredictably.", "Một cách thất thường", "Không theo quy luật.", "Formal", ["unpredictably"], ["spread erratically"], "Fires spread more erratically now.", "Hỏa hoạn lan rộng một cách thất thường hơn bây giờ."),
    create_word("precipitation", "/prɪˌsɪpɪˈteɪʃn/", "Noun", "C2", "Rain, snow, sleet, or hail that falls to the ground.", "Lượng mưa", "Nước rơi từ trời xuống.", "Scientific", ["rainfall"], ["normal precipitation"], "The region has below normal precipitation.", "Khu vực này có lượng mưa dưới mức bình thường."),
    create_word("eradication", "/ɪˌrædɪˈkeɪʃn/", "Noun", "C2", "The complete destruction of something.", "Sự tiêu diệt / Loại bỏ", "Phá sạch.", "Formal", ["elimination", "destruction"], ["natural eradication"], "They halted the natural eradication of underbrush.", "Họ đã ngăn chặn sự loại bỏ tự nhiên của tầng cây bụi."),
    create_word("underbrush", "/ˈʌndəbrʌʃ/", "Noun", "C2", "Shrubs and small trees forming the undergrowth in a forest.", "Tầng cây bụi / Cỏ dại", "Cây thấp trong rừng.", "Technical", ["undergrowth"], ["burn the underbrush"], "Underbrush is the primary fuel for fires.", "Tầng cây bụi là nhiên liệu chính cho các vụ cháy."),
    create_word("throwback", "/ˈθrəʊbæk/", "Noun", "C2", "A reversion to an earlier ancestral characteristic.", "Sự đảo ngược / Trở lại đặc điểm tổ tiên", "Giống tổ tiên xa xưa.", "Scientific", ["reversion"], ["evolutionary throwback"], "Some traits are evolutionary throwbacks.", "Một số đặc điểm là sự đảo ngược tiến hóa."),
    create_word("reversible", "/rɪˈvɜːsəbl/", "Adjective", "C1", "Able to be turned the other way around.", "Có thể đảo ngược", "Làm ngược lại được.", "Formal", [], ["reversible process"], "Is evolution reversible?", "Tiến hóa có thể đảo ngược không?"),
    create_word("ancestor", "/ˈænsestə/", "Noun", "B2", "A person, typically one more remote than a grandparent, from whom one is descended.", "Tổ tiên", "Người đời trước.", "General", ["forefather"], ["human ancestor"], "Lizards had toeless ancestors.", "Thằn lằn có tổ tiên không có ngón chân."),
    create_word("embryo", "/ˈembriəʊ/", "Noun", "C1", "An unborn or unhatched offspring in the process of development.", "Phôi thai", "Mầm sống ban đầu.", "Scientific", [], ["human embryo"], "Traits appear in embryos.", "Các đặc điểm xuất hiện ở phôi thai.")
]

generate_file(10, "Listening", 1, "tự lái xe ở Mỹ, câu lạc bộ giải trí, loài gấu", l1_words)
generate_file(10, "Listening", 2, "nha khoa, hồ bơi nước mặn", l2_words)
generate_file(10, "Listening", 3, "bảo tồn cá heo", l3_words)
generate_file(10, "Listening", 4, "công ty xây dựng, cảng công nghiệp, công nghệ nano", l4_words)

generate_file(10, "Reading", 1, "giếng bậc thang, tâm lý đổi mới", r1_words)
generate_file(10, "Reading", 2, "đơn khiếu nại, quy định bưu điện", r2_words)
generate_file(10, "Reading", 3, "lịch sử ngành du lịch", r3_words)
generate_file(10, "Reading", 4, "cháy rừng ở California, sự đảo ngược tiến hóa", r4_words)

print("Cambridge 10 generated.")
