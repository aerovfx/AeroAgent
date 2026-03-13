# 1 -Giới thiệu về project.en US

---

WEBVTT

Chào các bạn.

Vì vậy, trong dự án này, chúng tôi sẽ xây dựng một mô hình deep learning được đào tạo về tập dữ liệu văn bản để

dự đoán chuỗi từ tiếp theo.

Sau đó, chúng tôi sẽ chuẩn bị trang web của riêng mình, trang web này sẽ được xây dựng bằng khung Django và sẽ

được lưu trữ trên AWS.

Vì vậy, hãy bắt đầu.

Vì vậy, điều đầu tiên tôi sẽ làm là tìm hiểu nội dung của dự án, đúng không.

Tôi sẽ giải thích hoặc giới thiệu cho bạn về dự án, những gì chúng tôi đang xây dựng, chúng tôi hoạt động như thế nào

sẽ làm điều đó, chúng tôi sẽ sử dụng mô hình nào, chúng tôi sẽ sử dụng nền tảng nào.

Phải.

Sau đó, chúng ta sẽ đi sâu vào cụ thể mô hình mà chúng ta sẽ xây dựng và đào tạo, sau đó tạo ra

Dự án Django, tức là xây dựng trang web và cuối cùng là lưu trữ trang web đó trên AWS.

Bây giờ trong dự án này, chúng ta sẽ làm việc trên tập dữ liệu Văn bản, đây là một cuốn sách được viết bởi Plato, The Republic.

Vậy tập dữ liệu văn bản của chúng ta sẽ là những từ bên trong cuốn sách Republic, phải không?

Chúng tôi xử lý trước dữ liệu thành định dạng dễ sử dụng hơn và huấn luyện mô hình LSTM học sâu của mình.

Mô hình này dựa trên kiến trúc mạng nơ-ron và cung cấp hiệu suất rất cao theo trình tự

dựa trên tập dữ liệu, vì nó có cấu trúc phản hồi giúp mô hình ghi nhớ chuỗi dữ liệu

đầu vào và những thay đổi đang diễn ra theo từng lớp.

Sau đó, chúng tôi tạo một dự án Django trở thành trang web cơ sở của chúng tôi và trang web đó sẽ được lưu trữ trên

AWS.

Bây giờ đang xây dựng mô hình LSTM.

Vì vậy, mạng LSTM thực sự được thiết kế đặc biệt để khắc phục vấn đề phụ thuộc lâu dài gặp phải

bởi RNN do vấn đề độ dốc biến mất.

Vì vậy, các LSTM có các kết nối phản hồi làm cho chúng khác biệt với các mạng nơ-ron truyền thống hơn.

mạng.

Hiện tại, thuộc tính này cũng cho phép LSTM xử lý toàn bộ chuỗi dữ liệu mà không cần xử lý từng chuỗi.

điểm trong chuỗi một cách độc lập mà giữ lại thông tin hữu ích về dữ liệu trước đó

từ các lớp trước đó trong chuỗi để giúp xử lý dữ liệu mới hoặc điểm dữ liệu mới.

Phải.

Vì vậy, việc tạo dự án Django.

Khi chúng tôi nói dự án Django, chúng tôi thực sự muốn nói đến một trang web, phải không?

Sử dụng khung Django.

Bây giờ Django là một khung ứng dụng web nguồn mở và miễn phí được viết bằng Python và nó bao gồm các tính năng nâng cao

chức năng như xác thực, quản lý hỗ trợ và bảng quản trị, biểu mẫu liên hệ, hộp nhận xét,

hệ thống tải lên tập tin, và nhiều hơn nữa.

Vì vậy, khi chúng ta nói về biểu mẫu liên hệ và hộp nhận xét, về cơ bản chúng ta muốn nói đến việc xử lý giao diện người dùng.

trang, phục vụ các trang giao diện người dùng, truy xuất và gửi dữ liệu từ phía sau lên phía trước

kết thúc.

Phải.

Vì vậy, ở một mức độ nào đó, điều đó chỉ được xử lý bởi Django.

Nói cách khác, nếu bạn định tạo một trang web từ đầu, bạn sẽ cần phát triển các thành phần này

bởi chính bạn.

Nhưng khi sử dụng framework này, các thành phần này đã được tích hợp sẵn.

Bạn chỉ cần cấu hình chúng đúng cách và có thể gọi một số chức năng liên quan đến chúng để phù hợp với nhu cầu của bạn.

trang web.

Phải.

Bây giờ đây là phần cuối cùng mà chúng ta sẽ lưu trữ trang web của mình trên AWS, phải không?

Vì vậy, chúng tôi sẽ sử dụng phiên bản EC2 là micro T2 để lưu trữ trang web và hiểu cách thức

chính xác các máy chủ ảo đã được thiết lập.

Và hệ thống đám mây hoạt động đúng không.

Khi việc này hoàn tất, chúng tôi sẽ có thể truy cập trang web của mình và chạy mô hình từ mọi nơi trên toàn thế giới.

internet.

Bây giờ, trong tương lai, trước tiên chúng ta sẽ xem cách chúng ta sẽ xây dựng và đào tạo mô hình LSTM của mình.