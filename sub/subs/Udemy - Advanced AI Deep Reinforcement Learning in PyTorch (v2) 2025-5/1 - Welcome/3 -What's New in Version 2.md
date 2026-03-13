# 3 -Có gì mới ở phiên bản 2 đã dịch

---

Bạn sẽ nhận thấy rằng khóa học này có V2, nghĩa là phiên bản 2 trong tiêu đề.

Đó là bởi vì khóa học này là lần lặp lại thứ hai của khóa học này.

Phiên bản đầu tiên đã được phát hành cách đây đã lâu, gần một thập kỷ và kể từ thời điểm đó mọi thứ

đã thay đổi một chút.

Tôi vui mừng thông báo rằng phiên bản này của khóa học giúp mọi việc trở nên dễ dàng hơn nhiều

về mã hóa và kết nối lý thuyết với mã.

Đầu tiên, bây giờ chúng ta sẽ sử dụng PyTorch.

Khi khóa học này được phát hành lần đầu tiên, TensorFlow và Theano là những khóa học sâu phổ biến nhất

thư viện, vì vậy đó là những gì chúng tôi đã sử dụng.

Theano hiện không còn tồn tại và TensorFlow nổi tiếng là chậm và liên tục bị lỗi.

được cập nhật với những thay đổi đột phá.

Việc sử dụng PyTorch giúp khóa học này trở nên phù hợp hơn với tương lai và đảm bảo chúng tôi đang sử dụng các công cụ hiện đại.

Thứ hai, hiện nay có rất nhiều thư viện học tăng cường.

Phổ biến nhất là StableBaseLines3.

StableBaseLines3 bắt nguồn từ các đường cơ sở của OpenAI, đúng như tên gọi của nó, đã được phát triển

của OpenAI.

Thật không may, nó đã sử dụng TensorFlow một cách ngầm định và OpenAI đã ngừng duy trì nó sau đó.

một lúc.

StableBaseLines3 rất hữu ích cho chúng tôi vì nó cung cấp mã, giống như trình bao bọc môi trường,

môi trường vectơ và bộ đệm phát lại mà chúng ta không nhất thiết phải quan tâm đến

khi trọng tâm của chúng ta là tìm hiểu về các thuật toán, như DQN và A2C.

Điều này giúp bạn thoải mái hơn khi tập trung vào chi tiết của các thuật toán này thay vì lãng phí

thời gian gỡ lỗi bộ đệm phát lại của bạn và tự hỏi tại sao bạn lại hết RAM.

May mắn thay, vì thư viện này là nguồn mở nên bạn luôn có thể xem mã nguồn nếu bạn

muốn hiểu những thứ đó hoạt động như thế nào.

Ngoài ra, StableBaseLines3 còn triển khai DQN và A2C, do đó bạn luôn có thể tận dụng

triển khai nếu bạn cần gỡ lỗi.

Cuối cùng, mã trong khóa học này được cải thiện đáng kể so với phiên bản đầu tiên, cả

về hiệu suất và sự dễ hiểu.