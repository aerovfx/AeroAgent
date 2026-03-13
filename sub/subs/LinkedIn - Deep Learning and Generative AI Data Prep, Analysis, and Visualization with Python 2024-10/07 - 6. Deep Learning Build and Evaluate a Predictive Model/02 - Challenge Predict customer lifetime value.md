# 02 - Thử thách Dự đoán giá trị trọn đời của khách hàng

---

(nhạc sôi động)

- [Người hướng dẫn] Trong Phòng thí nghiệm Thử thách này,

chúng tôi thực sự sử dụng tất cả công việc khó khăn mà chúng tôi đã làm

để xử lý trước dữ liệu

và thực hiện phân tích dữ liệu thăm dò.

Bây giờ chúng tôi đã sẵn sàng cung cấp tệp eda_telecom.csv của mình

vào một mô hình học máy

để dự đoán giá trị trọn đời của khách hàng.

Để bắt đầu,

tải tệp sổ tay xuống rồi tải lên Colab.

Sau đó tải lên tập dữ liệu.

Là một mẹo nhanh,

bạn cũng có thể mở sổ ghi chép trực tiếp trong Colab

từ GitHub.

Lưu ý hộp màu đỏ xung quanh nút Mở trong Colab

ở góc trên bên phải.

Điều đầu tiên là nhập các thư viện cần thiết.

Sau đó xem lại và chạy tất cả các ô

cho đến khi bạn đến phần có tiêu đề

Sử dụng trực quan hóa dữ liệu để đánh giá hiệu suất của mô hình.

Sau đó xem lại và chạy tất cả các ô

cho đến khi bạn đến phần có tiêu đề

Sử dụng trực quan hóa dữ liệu để đánh giá hiệu suất của mô hình.

Ở đây, bạn có thể vẽ đồ thị.

Như một lời kêu gọi, trong bài tập số bốn,

bạn sử dụng khả năng sáng tạo của AI để tạo nội dung mới

và trả lời các câu hỏi bằng cách sao chép và dán bất kỳ hình ảnh nào

vào một chatbot AI.

Yêu cầu chatbot AI diễn giải hình ảnh.

Chatbot AI sẽ cung cấp phân tích chi tiết cho bạn,

một cái mà bạn có thể sử dụng cho bất kỳ báo cáo phân tích nào.

Các chatbot AI phổ biến bao gồm Gemini của Google

và ChatGPT của OpenAI.

Dưới đây là một ví dụ về đầu ra chatbot AI.

Hãy đến Phòng thí nghiệm thử thách ngay bây giờ

để biết hướng dẫn bắt đầu từ GitHub.

Được rồi, chúng ta đang ở trong GitHub,

và cuốn sổ bạn định sử dụng

vì Challenge Lab của bạn ở đây,

0602_bắt đầu,

và bạn muốn tải xuống tập tin sổ ghi chép này.

Vì vậy tôi sẽ đến đây và ở đây,

nơi nó nói Tải xuống tệp thô.

Sau khi tập tin được tải xuống,

bạn muốn tải tập tin đó lên

vào Notebook Jupyter của bạn trong Colab.

Bây giờ, có một lối tắt.

Bạn thực sự có thể đến đây để tìm nút này,

mở trong Colab và sổ ghi chép thực tế sẽ mở,

và sau đó bạn chỉ cần tiếp tục và tải tệp lên,

tập dữ liệu.

Tệp dữ liệu đó, nếu bạn chưa tải xuống,

ở dưới đây và tên là eda_telecom.csv.

Vì vậy, khi bạn đã tải tập tin đó lên

vào Notebook Jupyter của bạn,

sau đó bạn có thể bắt đầu bài tập của mình.

Bây giờ, trước tiên, hãy để tôi hướng dẫn bạn

một số điều cấp cao mà bạn nên biết.

Điều đầu tiên là bạn không cần phải viết mã tất cả những thứ này.

Chỉ cần chạy ô

để nhập các thư viện cần thiết của bạn,

và cuộn xuống đây.

Hãy tiếp tục và chạy ô để tải tập dữ liệu.

Hãy tiếp tục và chạy ô để hiển thị năm hàng đầu tiên

với df.head.

Hiển thị thông tin về khung dữ liệu tại đây.

Chạy ô đó.

Chạy ô cho các giá trị bị thiếu ở đây.

Được rồi, sau đó chỉ cần cuộn xuống,

và đây là nơi chúng tôi xây dựng và đào tạo

mô hình tuần tự Keras,

và đây thực sự là nơi làm việc chăm chỉ

tiền xử lý dữ liệu và EDA được thực hiện.

Nếu bạn muốn biết thêm về cách thức hoạt động của tất cả những điều này

xét về các chi tiết cơ bản của mạng lưới thần kinh,

vui lòng xem khóa học của tôi, Nền móng nhân tạo,

Giới thiệu về mạng lưới thần kinh.

Ở cấp độ cao, những gì chúng tôi đang làm ở đây

về cơ bản là tách các biến của chúng ta ra,

các tính năng của chúng tôi từ những cái đó

mà chúng ta sẽ đưa vào mô hình

dựa trên việc đó có phải là mục tiêu hay không,

đó là giá trị lâu dài của khách hàng,

hay chúng là những giá trị x sẽ được đưa vào

để dự đoán giá trị trọn đời của khách hàng.

Sau đó chúng ta sẽ chia dữ liệu

vào một tập huấn luyện và kiểm tra.

Sau đó chúng ta sẽ chuẩn hóa dữ liệu.

Chúng ta sẽ xây dựng mô hình.

Về cơ bản, chúng tôi sẽ xây dựng một mô hình tuần tự Keras,

một mô hình rất đơn giản để xây dựng bằng cách thêm các lớp.

Chúng tôi sẽ biên dịch mô hình.

Số liệu của chúng tôi sẽ là sai số bình phương trung bình.

Chúng tôi sẽ sử dụng tính năng dừng sớm để tránh trang bị quá mức.

Chúng ta sẽ đào tạo người mẫu.

Và sau đó chúng ta sẽ đánh giá mô hình,

dự đoán giá trị trọn đời của khách hàng,

và sau đó in bản tóm tắt mô hình.

Một lần nữa, tất cả những gì bạn phải làm chỉ đơn giản là chạy ô.

Và khi bạn chạy ô, quá trình đào tạo sẽ bắt đầu.

Và sau khi đào tạo xong,

sau đó bạn có thể hình dung đồ thị của mình.

Vì vậy, bạn sẽ sử dụng trực quan hóa dữ liệu

để đánh giá hiệu quả của mô hình.

Bài tập đầu tiên của bạn là thực sự vẽ đồ thị

các đường cong mất mát đào tạo và xác nhận.

Và mã cho điều đó sẽ ở đây.

Bài tập số hai của bạn

là vẽ đồ thị phân phối phần dư.

Và mã đó sẽ đi tới đây.

Sau đó bạn đang thực hiện bài tập thứ ba để vẽ đồ thị

giá trị dự đoán so với giá trị thực tế.

Và mã đó sẽ đi tới đây.

Khi tôi cuộn xuống, tôi sẽ chuyển ô CLV dự đoán

nơi chúng tôi dự đoán giá trị lâu dài của khách hàng.

Bảng này cho thấy thực tế so với dự đoán

giá trị trọn đời của khách hàng.

Và sau đó khi tôi cuộn xuống đây,

phần này ở đây, chúng ta sẽ sử dụng AI tổng hợp

để phân tích các hình ảnh trực quan.

Vì vậy, ở đây chúng ta sẽ sử dụng khả năng của AI tổng hợp

để tạo nội dung mới và trả lời các câu hỏi

bằng cách sao chép và dán bất kỳ hình ảnh nào vào chatbot AI.

Hãy để tôi cho bạn một ví dụ.

Vì vậy mình sẽ đi đến file giải pháp ở đây, 0603 end.

Và tôi sẽ cuộn xuống mọi thứ ở đây,

tất cả mã và tất cả đầu ra của tệp giải pháp.

Và một lần nữa, xin vui lòng tham khảo tập tin này

khi bạn đang thực hiện thử thách của mình.

Vì vậy, mô hình đang được đào tạo và đây là đường cong đầu tiên của chúng tôi.

Đây là đường cong mất mát đào tạo và xác nhận.

Tôi chỉ cần nhấp chuột phải vào hình ảnh này,

sao chép hình ảnh này, đi vào Gemini.

Tôi sẽ dán hình ảnh này.

Và để được gợi ý, tôi chỉ đơn giản viết,

giải thích điều này.

Và sau đó tôi sẽ nộp.

Và bạn có thể thấy rằng mô hình đang cho tôi một cái nhìn tổng quan.

Nó mang lại cho tôi thông tin về mất mát đào tạo.

Thông tin mất xác nhận và giải thích.

Nó mang lại cho tôi sự cải thiện ban đầu,

khả năng trang bị quá mức, lợi nhuận giảm dần.

Và nó cũng đang đưa ra khuyến nghị.