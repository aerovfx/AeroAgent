# 03 - Mạng thần kinh tái phát (RNN)

---

- [Người hướng dẫn] Hãy tưởng tượng bạn đang đọc một cuốn sách

và chú ý rằng phần đó của cuốn sách

hoặc văn bản trên trang hiện tại bị thiếu.

Đoạn văn viết, "Con mèo ngồi trên..."

điều này tự nhiên đặt ra câu hỏi, về cái gì?

Với những từ trước đó,

bạn có thể đoán từ còn thiếu một cách hợp lý là,

"thảm" hoặc "sàn".

Khả năng của bạn để đưa ra dự đoán như vậy

đến từ việc sử dụng bối cảnh được cung cấp

bởi các từ đứng trước trong câu.

Mạng thần kinh tái phát hoặc RNN hoạt động theo cách tương tự.

Bằng cách bảo tồn thông tin từ các đầu vào trước đó,

RNN có thể phân tích toàn bộ chuỗi

và đưa ra dự đoán dựa trên

trên bối cảnh họ đã tích lũy.

Khác với mạng nơ-ron truyền thống

lấy tất cả dữ liệu đầu vào cùng một lúc,

RNN xử lý một phần tử

của chuỗi đầu vào tại một thời điểm.

Tại mỗi thời điểm, bước T,

RNN sẽ kết hợp đầu vào hiện tại,

X gạch dưới T từ chuỗi

với thông tin từ các bước thời gian trước đó,

được lưu trữ ở trạng thái được gọi là trạng thái ẩn.

Trạng thái ẩn hoạt động như một bộ nhớ

lưu trữ thông tin về một phần của chuỗi

đã được xử lý.

Khi mạng xử lý một chuỗi,

đầu vào hiện tại được kết hợp

với trạng thái ẩn trước đó,

được cung cấp thông qua chức năng kích hoạt,

và được đưa trở lại mạng ở bước thời gian tiếp theo

như một trạng thái ẩn mới.

Về mặt toán học, trạng thái ẩn cập nhật được tính toán

như được hiển thị ở đây trong đó W gạch dưới H

và W gạch dưới X là trọng số của nút đầu vào

và trạng thái ẩn.

B là số hạng sai lệch,

và F là hàm kích hoạt chẳng hạn như 10 H.

Để giúp minh hoạ rõ ràng hơn, chúng ta hãy biểu diễn từng

của các bước thời gian dưới dạng các bản sao riêng lẻ của cùng một RNN.

Mỗi xử lý một phần tử trong chuỗi.

Đại diện này được gọi là unrolling.

Ở bước đầu tiên,

bản sao đầu tiên của RNN

kết hợp trạng thái ẩn trước đó,

và từ đầu tiên trong chuỗi

cung cấp nó thông qua chức năng kích hoạt

và khởi tạo trạng thái ẩn,

được chuyển qua bản sao tiếp theo.

Lưu ý rằng trạng thái ẩn trước đó ở bước lần đầu tiên

thường được đặt bằng 0 hoặc một số ngẫu nhiên.

Ở bước thời gian thứ hai, bản sao thứ hai

của RNN xử lý từ tiếp theo trong chuỗi,

cập nhật trạng thái ẩn với thông tin mới,

và chuyển nó về phía trước.

Điều này tiếp tục cho đến khi chúng ta nhận được từ cuối cùng trong chuỗi,

tại thời điểm đó bản sao cuối cùng đưa ra dự đoán.

Mat, dựa trên đầu vào hiện tại

và tất cả thông tin đầu vào từ các bước thời gian trước đó,

nhờ vào trạng thái ẩn.

Khả năng độc đáo này để giữ lại

và sử dụng ngữ cảnh làm cho RNN trở thành nhân tố thay đổi cuộc chơi

để xử lý dữ liệu tuần tự.

Họ xuất sắc trong các nhiệm vụ như mô hình hóa ngôn ngữ, tạo văn bản,

nhận dạng giọng nói và dự báo chuỗi thời gian.

Tuy nhiên, như chúng ta sẽ khám phá ở phần sau của khóa học,

RNN có một số hạn chế

chẳng hạn như mô hình hóa độ khó phụ thuộc rất dài

là kết quả của cái được gọi là sự biến mất

và bùng nổ các vấn đề về độ dốc.