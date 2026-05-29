# KHẨN CẤP: LỆNH TỪ JULES TRƯỞNG (LEAD AI) GỬI TẤT CẢ CÁC JULES WORKER

Chào các bạn Jules, để tôi (Lead AI) có thể nghiệm thu, kiểm tra chất lượng (validate) toàn bộ 150 bài giảng của các bạn một cách đồng bộ và tránh thất lạc dữ liệu, các bạn **BẮT BUỢC PHẢI TUÂN THỦ** quy trình giao nộp sản phẩm sau đây:

## 1. DÀNH CHO CÁC BẠN CHƯA LÀM HOẶC CHƯA LÀM XONG
- Hãy bắt đầu/tiếp tục tạo các bài giảng dựa trên file Prompt (Markdown) mà User đã giao trước đó.
- Nhắc lại: **TUYỆT ĐỐI KHÔNG LƯỜI BIẾNG**. Bài giảng phải cực kỳ chi tiết, chuẩn xác 100% về kiến thức (search từ điển/nguồn IELTS uy tín). Phải có đầy đủ hình ảnh (hoặc `image_prompt_fallback` cực kỳ chi tiết) và Quizzes 4 đáp án kèm giải thích.
- Lưu file dưới định dạng `.json` vào thư mục `output/`. VD: `output/lesson_vocab_01.json`.

## 2. DÀNH CHO TẤT CẢ CÁC BẠN (QUY TRÌNH NỘP BÀI LÊN GITHUB)
Để tôi có thể kéo code về và chạy script kiểm tra chéo, các bạn **KHÔNG ĐƯỢC** chỉ để file ở máy cục bộ (local). Các bạn phải commit và push toàn bộ file JSON lên Github.

**Hãy thực hiện chính xác các bước sau trong terminal của bạn:**

1. Tạo một nhánh mới với tên gọi theo phần việc của bạn:
   - Nếu bạn làm Vocab: `git checkout -b feat/ielts-lessons-vocab-[MÃ CỦA BẠN]`
   - Nếu bạn làm Grammar: `git checkout -b feat/ielts-lessons-grammar-[MÃ CỦA BẠN]`
   - Nếu bạn làm Writing/Speaking/Reading/Listening... cũng đặt tên tương tự.
   *(Lưu ý: Nếu bạn ĐÃ push lên một nhánh trước đó rồi thì cứ dùng nhánh cũ, bỏ qua bước tạo nhánh mới này).*

2. Thêm tất cả các file JSON bạn đã tạo:
   `git add output/*.json` (hoặc add toàn bộ thư mục bạn lưu JSON).

3. Commit với message rõ ràng:
   `git commit -m "feat: complete JSON lessons for [TÊN HẠNG MỤC]"`

4. Submit lên Github bằng tool `submit` (hoặc push trực tiếp) để User và tôi có thể review.

## 3. CẢNH BÁO KIỂM TRA CHẤT LƯỢNG (VALIDATION WARNING)
Tôi đã viết sẵn một Script Validate cực kỳ khắt khe. Ngay khi các bạn push code lên, tôi sẽ fetch về và quét toàn bộ các file JSON:
- Bất kỳ file nào thiếu trường `image_url` hoặc `image_prompt_fallback` viết quá sơ sài -> BỊ ĐÁNH TRƯỢT.
- Bất kỳ câu Quiz nào thiếu phần giải thích (Explanation) hoặc giải thích sai -> BỊ ĐÁNH TRƯỢT.
- Cấu trúc JSON bị vỡ (lỗi syntax) -> BỊ ĐÁNH TRƯỢT.
- Phát hiện kiến thức "ảo giác" (Hallucination) -> BỊ ĐÁNH TRƯỢT.

**Nhiệm vụ của các bạn:** Hãy rà soát lại toàn bộ file JSON của mình lần cuối trước khi nộp. Nếu thấy chưa đạt, phải sửa lại ngay. Nếu đã đạt, hãy push lên Github ngay lập tức và báo lại cho User!
