# 02 - Xây dựng lời nhắc hiệu quả

---

- [Người hướng dẫn] Cùng khám phá nhé

các mẫu phổ biến cho thiết kế kịp thời

và các khía cạnh chính cần xem xét,

đảm bảo sự tương tác của bạn với các mô hình AI này

đều hiệu quả và năng suất.

Hãy nghĩ về kỹ thuật nhanh chóng như chế tạo một chiếc chìa khóa

điều đó giải phóng toàn bộ tiềm năng

của một bộ não AI phức tạp.

Thiết kế kịp thời là rất quan trọng

Vì nó ảnh hưởng trực tiếp đến chất lượng

và mức độ liên quan của các phản hồi bạn nhận được từ LLM.

Lời nhắc được thiết kế tốt phải rõ ràng,

ngắn gọn, cụ thể.

Nó sẽ cung cấp đủ bối cảnh

để hướng dẫn phản ứng của người mẫu,

nhưng không nhiều đến mức nó lấn át nó

hoặc làm nhầm lẫn mô hình.

Một số mẫu, đặc biệt là những mẫu nhỏ hơn như T5,

có các mẫu lời nhắc cụ thể được tối ưu hóa

cho việc đào tạo của họ.

Ví dụ: T5 chuyển đổi mọi nhiệm vụ

sang định dạng chuyển văn bản thành văn bản,

thường bắt đầu bằng từ khóa báo hiệu loại nhiệm vụ,

chẳng hạn như dịch, tóm tắt hoặc đặt câu hỏi

để trả lời câu hỏi.

Cách tiếp cận tiêu chuẩn hóa này giúp mô hình

nhanh chóng nhận ra một nhiệm vụ

và áp dụng quy trình và chiến lược thích hợp.

Bây giờ chúng ta đã biết những điều cơ bản,

chúng ta hãy đi sâu vào ba mẫu chính

để có kỹ thuật nhanh chóng có thể giúp bạn tối đa hóa

hiệu quả tương tác của bạn với LLM:

kiểu bắn vài phát, kiểu xác minh nhận thức,

và mẫu sàng lọc câu hỏi.

Đầu tiên là mô hình vài cú đánh.

Điều này liên quan đến việc cung cấp một số ví dụ về nhiệm vụ hiện tại

trước khi trình bày mô hình với một trường hợp mới để giải quyết.

Ví dụ: nếu bạn đang dạy mô hình

để xác định tên động vật trong văn bản,

bạn có thể đưa ra ví dụ với các loài động vật được dán nhãn

trước khi yêu cầu nó xác định các con vật trong một câu mới.

Ví dụ: đưa ra lời nhắc:

"Con cáo nâu nhanh nhẹn nhảy qua con chó lười"

chúng tôi đặt nhận dạng là cáo và chó.

Sau đó, chúng tôi thêm lời nhắc thực sự:

"Một con cừu và một con sói không thể trở thành đôi bạn thân thiết."

Khi chúng tôi yêu cầu xác định danh tính con vật,

LLM sẽ có nhiều thông tin hơn

về định dạng của đầu ra.

Tiếp theo, chúng ta có mẫu xác minh nhận thức,

điều này cực kỳ hữu ích khi bạn cần một cách tiếp cận đúng đắn

đến một chủ đề và không chắc chắn liệu chúng ta có đang giải quyết tất cả

các góc của nó.

Bằng cách sử dụng mẫu này,

LLM tăng độ tin cậy của đầu ra

bằng cách kiểm tra thông tin cần thiết

trước phản hồi cuối cùng.

Nó thực sự hữu ích khi nó quan trọng

để có thông tin đáng tin cậy và trung thực

để giải quyết một vấn đề.

Ví dụ: lời nhắc chung bắt đầu cuộc trò chuyện

nên là: Bất cứ khi nào tôi đặt câu hỏi,

chỉ hỏi tôi để biết thêm thông tin

để làm rõ những gì tôi đang hỏi trước khi đưa ra câu trả lời cuối cùng.

Hãy kết hợp tất cả các câu trả lời của tôi.

Lời nhắc như vậy sẽ kích hoạt một bộ câu hỏi

để tinh chỉnh thêm những gì chúng tôi đang tìm kiếm.

Tôi khuyến khích bạn dùng thử nó trong chatbot tốt nhất của bạn

sự lựa chọn của bạn.

Cuối cùng, mẫu sàng lọc câu hỏi được sử dụng

để LLM tinh chỉnh hoặc làm rõ một câu hỏi

trước khi trả lời nó.

LLM đặt câu hỏi bổ sung

để có thêm thông tin hoặc bối cảnh,

mà sau đó nó sử dụng để cung cấp thông tin chính xác hơn

hoặc câu trả lời có liên quan.

Lời nhắc ban đầu của cuộc trò chuyện như vậy sẽ là:

Bất cứ khi nào tôi đặt câu hỏi,

hỏi tôi thêm câu hỏi để làm rõ điều tôi đang hỏi

trước khi bạn đưa ra câu trả lời.

Khi bạn thử nghiệm những mẫu này,

bạn sẽ thấy điều đó theo cách bạn diễn đạt một lời nhắc

có thể thay đổi đáng kể kết quả bạn đạt được với LLM.

Thử nghiệm các phương pháp khác nhau, tinh chỉnh lời nhắc của bạn

dựa trên các câu trả lời và liên tục học hỏi

từ sự tương tác của họ.