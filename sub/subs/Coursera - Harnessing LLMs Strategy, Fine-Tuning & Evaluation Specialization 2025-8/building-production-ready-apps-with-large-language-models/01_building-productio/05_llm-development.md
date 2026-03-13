# 📘 BÀI HỌC: 05 PHÁT TRIỂN LLM (LLM DEVELOPMENT)

## 1. Mục Tiêu Học Tập
*   So sánh sự khác biệt giữa phát triển Học máy truyền thống và Phát triển LLM.
*   Phân biệt 3 loại mô hình LLM phổ biến dựa trên chức năng.
*   Hiểu rõ khái niệm **Chuỗi suy nghĩ suy luận (Chain of Thought)**.
*   Nắm vững các nguyên tắc thiết kế lời nhắc hiệu quả.

---

## 2. Phát Triển LLM vs. Học Máy Truyền Thống

| Đặc Điểm | Học Máy Truyền Thống | Phát Triển LLM |
| :--- | :--- | :--- |
| **Yêu cầu kỹ thuật** | Cần chuyên môn kỹ thuật sâu rộng. | **Không cần nền tảng kỹ thuật phức tạp.** |
| **Trọng tâm** | Dữ liệu đào tạo lớn, đào tạo mô hình phức tạp, quản lý phần cứng. | **Thiết kế lời nhắc (Prompts) hiệu quả.** |
| **Độ phức tạp** | Nhiều chi tiết, sắc thái về kiến trúc mô hình. | **Rõ ràng, ngắn gọn**, tập trung vào nội dung lời nhắc. |
| **Tài nguyên** | Quản lý tài nguyên máy tính chuyên sâu. | Tập trung vào tối ưu hóa đầu ra (Output). |

---

## 3. 3 Loại Mô Hình LLM Dựa Trên Chức Năng

| Loại Mô Hình | Mô Tả | Khả Năng | Ví Dụ |
| :--- | :--- | :--- | :--- |
| **1. Chung Chung (General)** | Dự đoán từ tiếp theo dựa trên dữ liệu huấn luyện. | Tự động hoàn thành, viết tiếp câu. | "Viết tiếp đoạn văn này..." |
| **2. Điều Chỉnh Theo Hướng Dẫn (Instruction Tuned)** | Phản hồi dựa trên hướng dẫn cụ thể trong lời nhắc. | Tóm tắt, sáng tác thơ, phân tích cảm xúc. | "Tóm tắt văn bản", "Dịch sang tiếng Pháp". |
| **3. Điều Chỉnh Đối Thoại (Conversation Tuned)** | Chuyên biệt cho tương tác đàm thoại. | Chatbot, trợ lý ảo, tương tác đa vòng. | *Loại mà khóa học này sử dụng.* |

> 💡 **Lưu ý:** Mô hình **Chung** học từ dữ liệu (predictive), trong khi **Instruction Tuned** học theo chỉ dẫn (compliance).

---

## 4. Khái Niệm: Chuỗi Suy Tư Suy Luận (Chain of Thought)

### 4.1 Định Nghĩa
*   **Cơ chế:** Mô hình AI tạo ra một chuỗi lý luận/bước suy nghĩ **trước khi** đưa ra kết luận cuối cùng.
*   **Mục đích:** Tăng cường khả năng giải quyết vấn đề phức tạp một cách có hệ thống.

### 4.2 Ví Dụ Minh Họa
*   **Tình huống:** Xây dựng mô hình liên quan đến *các tòa nhà minh bạch* (như trong transcript).
*   **Bước 1:** Mô hình phân tích các khía cạnh:
    *   **Mối quan hệ:** Minh bạch & Sự riêng tư.
    *   **Vấn đề:** Tiêu thụ ánh sáng & Năng lượng.
    *   **Giao diện:** Thẩm mỹ & Không khí đô thị.
    *   **Hậu quả:** An toàn & Bảo mật.
*   **Bước 2:** LLM đưa ra phản hồi cho từng khía cạnh.
*   **Bước 3:** Kết hợp tất cả thông tin để tạo ra phản hồi **Toàn diện**.

> ✅ **Lợi ích:** Giảm lỗi logic, tăng tính mạch lạc và chính xác của câu trả lời.

---

## 5. Nguyên Tắc Tạo Lời Nhắc (Prompt) Hiệu Quả

Để khai thác sức mạnh của LLM, hãy tuân thủ các nguyên tắc sau:

1.  **Rõ Ràng & Ngắn Gọn:**
    *   Khung nhắc nhở nên hướng dẫn chính xác mô hình, tránh lan man.
2.  **Hiểu Sức Mạnh & Hạn Chế:**
    *   Không yêu cầu mô hình điều không thể làm được (như truy cập internet offline nếu mô hình không có quyền truy cập).
3.  **Bắt Đầu Đơn Giản:**
    *   Thử nghiệm các lời nhắc đơn giản trước, sau đó tăng dần độ phức tạp.
4.  **Thử Nghiệm & Tối Ưu:**
    *   "Vòng lặp thử nghiệm" giúp học cách diễn đạt và cấu trúc hoạt động tốt hơn (Iterative Process).

---

## 6. Tổng Kết Bài Học

1.  **Sự Khác Biệt:** Phát triển LLM khác với máy học truyền thống bởi việc ưu tiên **lời nhắc chất lượng** thay vì chuyên sâu về kỹ thuật xây dựng mô hình.
2.  **3 Loại LLM:** Chung chung, Điều chỉnh theo hướng dẫn, Điều chỉnh đối thoại.
3.  **Chuỗi Suy Tư:** Giúp LLM xử lý vấn đề logic tốt hơn bằng cách phân tách vấn đề thành các bước nhỏ.
4.  **Prompting:** Cần sự sáng tạo, thử nghiệm và rõ ràng để nhận được kết quả tốt nhất.

---

## 7. Bài Tập Về Nhà (Homework)

*Hãy thực hiện bài tập sau để củng cố kiến thức:*

1.  **Tạo một lời nhắc (Prompt)** cho một mô hình LLM để giải quyết một vấn đề có nhiều khía cạnh (ví dụ: kế hoạch sự kiện).
    *   Yêu cầu mô hình phải liệt kê các yếu tố: Chi phí, Đối tượng tham gia, Địa điểm, và Kế hoạch khẩn cấp.
    *   Sau đó, yêu cầu mô hình suy luận từng điểm trước khi chốt danh sách.
2.  **Thử nghiệm:** So sánh kết quả giữa một lời nhắc đơn giản (1 câu) và một lời nhắc có cấu trúc từng bước (Chain of Thought).
