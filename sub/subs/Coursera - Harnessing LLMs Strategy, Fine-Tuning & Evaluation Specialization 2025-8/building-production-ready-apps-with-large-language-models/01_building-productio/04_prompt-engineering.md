

# 📘 BÀI HỌC: 04 KỸ THUẬT NHẮC NHỞ (PROMPT ENGINEERING)

## 1. Mục Tiêu Học Tập
*   Hiểu sâu về vai trò của kỹ thuật nhắc nhở (Prompt Engineering).
*   Phân biệt giữa thiết kế lời nhắc và kỹ thuật tối ưu hóa lời nhắc.
*   Làm chủ 6 loại lời nhắc phổ biến.
*   Nắm vững các nguyên tắc trách nhiệm và hạn chế của kỹ thuật.

## 2. Khái Niệm Cốt Lõi

### 2.1 Định Nghĩa & Vai Trò
*   **Kỹ thuật nhắc nhở (Prompt Engineering):** Tối ưu hóa các chiến lược lời nhắc khi đưa vào Hệ thống AI để cải thiện hiệu suất (chính xác, phù hợp).
*   **Vai trò:** Là cầu nối giao tiếp giữa con người và AI.
    *   *Không có chiến lược:* Kết quả mơ hồ, có nguy hiểm.
    *   *Có chiến lược:* Điều khiển tốt hơn, giải phóng tiềm năng AI.

### 2.2 Phân Biệt: Thiết kế vs. Kỹ thuật
*   **Thiết kế lời nhắc (Prompt Design):** Tạo ra các lời nhắc cụ thể cho các nhiệm vụ (ví dụ: "tóm tắt văn bản", "dịch sang tiếng Pháp").
*   **Kỹ thuật lời nhắc (Prompt Engineering):** Tối ưu hóa các lời nhắc để đạt hiệu suất cao hơn (ví dụ: thêm vai trò, ví dụ mẫu, chuỗi suy nghĩ).

---

## 3. 6 Loại Lời Nhắc & Kỹ Thuật Cụ Thể

| Loại Lời Nhắc | Mô Tả & Mục Đích | Ví Dụ Thực Tế |
| :--- | :--- | :--- |
| **1. Hướng dẫn (Instructional)** | Chỉ dẫn đơn giản, trực tiếp. | *"Tóm tắt văn bản này ngắn gọn."*<br>*"Dịch đoạn văn sang tiếng Pháp."* |
| **2. Từ khóa (Keyword)** | Sử dụng tín hiệu hữu ích để định hướng. | *"Giải thích các sự kiện theo thứ tự xảy ra của chúng."*<br>*(Dùng từ khóa "thứ tự", "quan trọng")* |
| **3. Miền (Domain)** | Sử dụng kiến thức chuyên môn/khái niệm. | *"Chẩn đoán y tế này sử dụng ngôn ngữ lâm sàng."*<br>*"Đánh giá hợp đồng pháp lý dùng khuôn khổ pháp lý."* |
| **4. Vai trò (Persona)** | Hướng dẫn AI chấp nhận một nhân cách cụ thể. | *"Trả lời như một chuyên gia kinh tế."*<br>*"Hoàn thành nhiệm vụ như một giáo viên tiếng Anh."* |
| **5. Chuỗi suy nghĩ (Chain of Thought)** | Chia nhỏ nhiệm vụ phức tạp thành các hành động. | Bước 1: Tóm tắt ý chính.<br>Bước 2: Giải thích quan điểm.<br>Bước 3: Phân tích quan trọng. |
| **6. Kỹ thuật Bắn (Shooting)** | Cung cấp ví dụ mẫu để AI học mẫu (Few-shot/Zero-shot). | - **Zero-shot:** Không có ví dụ.<br>- **One-shot:** 1 ví dụ mẫu.<br>- **Few-shot:** Nhiều ví dụ mẫu.<br>*"Viết một bài thơ ngắn về thiên nhiên (dùng ví dụ cây, rồi làm về đại dương)".* |

---

## 4. Nguyên Tắc Nhắc Nhở Có Trách Nhiệm (Responsible Prompting)

Dù có kỹ thuật tốt bao nhiêu, chúng ta cũng phải tuân thủ các nguyên tắc sau:

*   **Nhận diện giới hạn & Thiên kiến:** LLM có thiên kiến và hạn chế, không phải là "viên đạn bạc".
*   **Xác thực kết quả rủi ro cao:** Các thông tin về pháp lý, y tế cần được xác nhận bởi chuyên gia trước khi sử dụng.
*   **Kiểm tra trước khi triển khai:** Không đưa ứng dụng vào sản xuất nếu chưa thử nghiệm đầy đủ.
*   **Xác nhận bởi con người:** Kết quả đầu ra *luôn* cần sự xác nhận cuối cùng của con người (Human-in-the-loop), đặc biệt ở lĩnh vực rủi ro cao.
*   **Tối ưu hóa:** Lặp lại cẩn thận để tối ưu lời nhắc trước khi chạy thử.

---

## 5. Hạn Chế Của Kỹ Thuật Nhắc Nhở
1.  **Không phải viên đạn bạc:** Không thể ngăn chặn mọi hành vi bất ngờ của mô hình.
2.  **Giới hạn nhiệm vụ:** Một số nhiệm vụ vẫn vượt quá năng lực xử lý của mô hình hiện tại.
3.  **Cần hiểu mô hình:** Khó tối ưu nếu không hiểu mô hình hoạt động như thế nào và loại lời nhắc nào phù hợp.
4.  **Rủi ro:** Sức mạnh đi kèm trách nhiệm lớn lao.

---

## 6. Tổng Kết & Câu Hỏi
*   **Tóm lại:** Kỹ thuật nhắc nhở chiến lược giúp chúng ta chỉ đạo AI tốt hơn, đồng thời nhắc nhở một cách có trách nhiệm và đạo đức.
*   **Bài tập về nhà (Tư duy):**
    1.  Khi bạn cần AI tư vấn về sức khỏe, bạn sẽ thêm các yếu tố gì vào lời nhắc để đảm bảo an toàn (chuyên môn, cảnh báo)?
    2.  Hãy thử tìm hiểu về các thiên kiến (bias) thường thấy trong LLM và làm cách nào để giảm thiểu nó khi viết lời nhắc.

> 💡 **Lời khuyên:** Hãy kết hợp sáng tạo giữa **Kỹ thuật (Technique)** và **Đạo đức (Ethics)** để khai thác AI một cách hiệu quả nhất.
