# 05 - So sánh LLM

---

- [Người hướng dẫn] Hãy đi sâu vào các sắc thái

của các kiến trúc LLM khác nhau,

chỉ bộ mã hóa, chỉ bộ giải mã và bộ mã hóa-giải mã,

và thảo luận về phương pháp đào tạo và cách sử dụng cụ thể của họ.

Hãy trang bị cho bạn những kiến thức để lựa chọn mẫu mã phù hợp

cho nhiệm vụ của bạn

và lựa chọn công cụ hoàn hảo cho một món ăn dành cho người sành ăn.

Đầu tiên là các mẫu chỉ dành cho bộ mã hóa, chẳng hạn như BERT.

Các mô hình này tập trung vào việc phân tích

và hiểu dữ liệu đầu vào.

BERT được đào tạo về các nhiệm vụ như mô hình hóa ngôn ngữ đeo mặt nạ,

nơi nó học cách dự đoán những từ còn thiếu trong một câu.

Quá trình đào tạo này giúp mô hình nắm bắt được bối cảnh

từ cả hai hướng, trái sang phải và phải sang trái,

giống như một đầu bếp phó cần hiểu tất cả các nguyên liệu

và sự tương tác của chúng.

BERT và các biến thể của nó được sử dụng rộng rãi cho các nhiệm vụ

trong đó việc hiểu văn bản là rất quan trọng,

chẳng hạn như phân tích tình cảm hoặc trả lời câu hỏi.

Giống như có một nhà phê bình ẩm thực chuyên

trong việc mổ xẻ và tìm hiểu hương vị của một món ăn.

Tiếp theo, các mẫu chỉ có bộ giải mã,

giống như dòng GPT của OpenAI.

Những mô hình này vượt trội trong việc tạo văn bản

dựa trên đầu vào mà họ nhận được.

Ví dụ: GPT-3 sử dụng phương pháp tiếp cận

được gọi là mô hình ngôn ngữ tự hồi quy,

nơi nó dự đoán từ tiếp theo trong một chuỗi,

học từ mỗi từ nó đã dự đoán.

Hãy tưởng tượng một đầu bếp nấu hết món này đến món khác,

mỗi cái đều bị ảnh hưởng bởi cái cuối cùng

GPT-3 là một cỗ máy mạnh mẽ

trong các ứng dụng yêu cầu tạo nội dung,

từ viết bài đến soạn email.

Nó giống như một đầu bếp sáng tạo

người tạo ra các công thức nấu ăn mới dựa trên một số nguyên liệu nhất định.

Chuyển sang mô hình mã hóa-giải mã,

kết hợp các chức năng của hai cái đầu tiên,

T5, hoặc Biến áp chuyển văn bản thành văn bản,

minh hoạ cho kiến trúc này.

Nó được đào tạo trên cơ sở chuyển văn bản thành văn bản,

nơi mọi nhiệm vụ,

có thể là dịch thuật, phân loại hoặc tóm tắt,

được chuyển thành bài toán tạo văn bản.

Khả năng công cụ này cho phép chúng tôi

để hiểu và tạo ra văn bản,

giống như một đầu bếp vừa lên thực đơn vừa nấu bữa ăn.

T5 và các mẫu tương tự rất linh hoạt,

phù hợp cho một loạt các ứng dụng

trên các ngôn ngữ và nhiệm vụ khác nhau,

biến chúng thành những con dao quân đội Thụy Sĩ của thế giới LLM.

Hãy xem xét Llama 3 8B của Meta, một mô hình có 8 tỷ tham số.

Lưu trữ một mô hình như vậy cho các nhiệm vụ như kỹ thuật nhanh chóng

đòi hỏi nguồn lực tính toán đáng kể.

Cụ thể là mô hình tham số 8 tỷ

cần khoảng 32 gigabyte RAM chỉ cho trọng lượng của mô hình.

Bao gồm bộ nhớ bổ sung cho các hoạt động và truy vấn của người dùng,

đó là một yêu cầu đáng kể,

giống như cần không gian cho cả nguyên liệu và dụng cụ

trong căn bếp bận rộn.

Điều này nhấn mạnh sự cần thiết phải xem xét kích thước mô hình

khi kết hợp một mô hình với ngân sách của chúng tôi

và khả năng của cơ sở hạ tầng.

Tuy nhiên, các kỹ thuật như chắt lọc mô hình và lượng tử hóa

có thể giảm tải tính toán,

làm cho việc triển khai các mô hình mạnh mẽ này trở nên khả thi

trong các môi trường sản xuất.

Những kỹ thuật này,

mà chúng tôi sẽ đề cập chi tiết trong khóa học khác của tôi

liên quan đến phát triển và triển khai chatbot AI

trên LinkedIn Học tập,

sẽ giúp hợp lý hóa các mô hình

trong khi vẫn duy trì hiệu quả của chúng.

Để chọn LLM tốt nhất cho nhiệm vụ của bạn,

bắt đầu bằng cách xem xét bản chất của nhiệm vụ.

Đó là sự hiểu biết, sự phát sinh hay cả hai?

Nếu bạn tập trung vào việc hiểu hoặc phân tích văn bản,

mô hình chỉ có bộ mã hóa có thể đủ.

Để tạo nội dung, các mô hình chỉ có bộ giải mã được ưu tiên hơn.

Và đối với những nhiệm vụ yêu cầu cả hai,

xem xét các mô hình bộ mã hóa-giải mã.

Tiếp theo, đánh giá xem các mô hình hiện có có đáp ứng nhu cầu của bạn không

hoặc nếu cần tinh chỉnh.

Đối với các nhiệm vụ có sắc thái cụ thể cho dữ liệu của bạn,

tinh chỉnh có thể là cần thiết.

Xây dựng LLM từ đầu có thể tốn kém

như thành lập một nhà hàng cao cấp.

Nó đòi hỏi sự đầu tư đáng kể

về tài nguyên tính toán, dữ liệu và kiến thức chuyên môn.

Vì vậy, tận dụng các mô hình hiện có

và tập trung vào việc tinh chỉnh hoặc kỹ thuật kịp thời

thường thực tế hơn.