# 07 - Thử thách mô hình TensorFlow đầu tiên của tôi

---

(nhạc sôi động)

- [Người hướng dẫn] Wow, chúng ta đã học được rất nhiều kiến thức rồi

với học sâu với TensorFlow.

Tiếp theo, chúng ta sẽ thực hiện một thử thách mà bạn nhận được

để thực hành những bài học từ việc nhập thư viện

đến tiêu chuẩn hóa, tiền xử lý,

để tạo ra mô hình, đào tạo mô hình,

đánh giá mô hình,

và cuối cùng là tạo hình để xem kết quả

mô hình học sâu của chúng tôi.

Vì vậy, nếu bạn đã sẵn sàng, hãy gặp tôi trong không gian mã,

và từ khung bên trái, tìm thư mục SRC

và tìm tệp Python 03_07_challenge.

Vì vậy, trong tệp Python này, bạn sẽ thấy

rằng chúng tôi đã cài đặt sẵn các thư viện cho mình,

bao gồm các bộ dữ liệu TensorFlow, SK Learn,

Lựa chọn mô hình SK Learn, tiền xử lý SK Learn,

Mat Plot Lib, v.v.

Vì vậy, trong tập tin thử thách, chúng ta đã có thể thấy

rằng tập dữ liệu nhà ở California đã được tải sẵn cho chúng tôi

và được giao nhà ở.

Tiếp theo, tập dữ liệu của chúng tôi được chia thành chuỗi X, xác thực X,

Đào tạo Y và xác nhận Y cho chúng tôi.

Vì vậy, chúng ta sẽ tiếp tục và giải quyết vấn đề như sau.

Trước hết, nhiệm vụ của bạn sẽ bắt đầu

với việc chuẩn hóa dữ liệu.

Như bạn có thể thấy, chúng tôi có các phần được nhận xét,

và trong dung dịch,

những gì bạn định làm là bạn sẽ điền vào

sau những nhận xét này bằng mã của riêng bạn.

Vì vậy, bạn sẽ bắt đầu với việc chuẩn hóa dữ liệu.

Sau đó, bạn sẽ tiến hành xây dựng mô hình

với hai lớp ẩn và một lớp đầu ra.

Sau đó, bạn sẽ biên dịch mô hình, làm theo

bằng cách đào tạo mô hình,

sau đó đánh giá mô hình trên tập kiểm tra.

Cuối cùng, bạn sẽ lập kế hoạch đào tạo

và biểu đồ mất xác thực trong thư mục đầu ra, một

mà chúng tôi đang sử dụng ở đây cho phần đau bên trái.

Vì vậy, bây giờ là lúc để xem lại mọi thứ chúng ta đã học,

hãy tiếp tục và thử xem,

và tôi sẽ gặp bạn trong video giải pháp.