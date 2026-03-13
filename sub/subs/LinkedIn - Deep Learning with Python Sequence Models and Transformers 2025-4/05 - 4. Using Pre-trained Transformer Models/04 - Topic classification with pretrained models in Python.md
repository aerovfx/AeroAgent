# 04 - Phân loại chủ đề bằng các mô hình được đào tạo trước trong Python

---

- [Người hướng dẫn] Trong ví dụ này, chúng ta sẽ sử dụng

một người mẫu được đào tạo trước từ trung tâm Ôm Mặt

để phân loại chủ đề.

Phân loại chủ đề là một kỹ thuật được sử dụng để gán

các chủ đề hoặc danh mục được xác định trước như thời tiết, thể thao,

tài chính và nhiều hơn nữa cho một đoạn văn bản nhất định.

Hãy bắt đầu bằng cách chọn kernel.

Sau đó, chúng tôi giảm thiểu hoặc giảm mức độ dài dòng của nhật ký.

Vì vậy, bây giờ, chúng ta đã sẵn sàng khởi tạo một quy trình

để phân loại chủ đề.

Vì vậy, trung tâm Ôm Mặt không có đường dẫn chuyên dụng

được đặt tên để phân loại chủ đề.

Tuy nhiên, chúng ta vẫn có thể sử dụng chung

đường dẫn phân loại văn bản cho mục đích này.

Nhưng để điều này xảy ra, chúng ta sẽ cần sử dụng

một mô hình được đào tạo đặc biệt để phân loại chủ đề.

Trong ví dụ này, chúng ta sẽ sử dụng

bộ phân loại chủ đề-tin tức-IPTC-đa ngôn ngữ.

Để sử dụng mô hình này, chúng tôi bắt đầu bằng cách nhập

chức năng đường ống từ gói máy biến áp.

Chúng tôi chỉ định tên của mô hình của chúng tôi và chúng tôi khởi tạo

một đường dẫn mới gọi là chủ đề.

Trong chức năng đường ống,

chúng tôi chỉ định nhiệm vụ, đó là phân loại văn bản,

và sau đó chúng tôi chỉ định tên của mô hình.

Vì vậy chúng ta hãy tiếp tục và chạy cái này.

Vì vậy trong khi cái này đang chạy,

chúng ta thấy một vài thứ hiển thị trên màn hình ở đây.

Vậy tất cả điều này đang nói với chúng ta rằng

môi trường của chúng tôi không được tối ưu hóa để sử dụng GPU,

điều đó ổn với những gì đang diễn ra ở đây ngày hôm nay.

Lưu ý khác mà chúng ta cũng thấy ở đây

là thông tin về cấp phát bộ nhớ.

Vì vậy, gói hoặc mô hình chúng tôi thực sự đang sử dụng ở đây

là một mô hình khá lớn và khá nhiều

thông tin này cho chúng ta biết rằng mô hình này

có nhiều bộ nhớ hơn dự đoán ban đầu,

điều đó cũng được, nên chúng tôi ổn.

Vậy là quá trình đã hoàn tất.

Việc tiếp theo chúng ta cần làm bây giờ là

để chạy Phân loại chủ đề trên một số văn bản mẫu.

Vì vậy điều tôi đã làm ở đây là tạo ra một danh sách các câu

và chúng tôi sẽ thử xem mô hình, quy trình của chúng tôi,

phân loại chủ đề cho từng câu này.

Vì vậy, chúng tôi có một cái như Chính phủ thông báo

kế hoạch kích thích kinh tế mới để thúc đẩy nhiều doanh nghiệp hơn.

Một cái khác, nó nói, đội bóng đá địa phương giành chiến thắng quốc gia

chức vô địch sau trận chung kết đầy gay cấn.

Vì vậy chúng ta hãy tiếp tục và chạy cái này.

Và sử dụng danh sách các câu này, chúng ta sẽ tiếp tục

và chạy một vòng lặp đi qua từng câu này

vào hệ thống của chúng tôi và sau đó chúng tôi đưa ra kết quả.

Vì vậy, hãy xem những gì chúng ta nhận được ở đây.

Vì vậy, chúng tôi có nó.

Bạn thấy rằng văn bản đầu tiên,

Chính phủ công bố gói kích thích kinh tế mới

được dán nhãn là kinh tế, kinh doanh và tài chính

với số điểm 0,997,

và cái tiếp theo được dán nhãn là Thể thao;

thứ ba là khoa học và công nghệ,

thứ tư là khoa học và công nghệ,

và thứ năm là môi trường.

Vì vậy, một lần nữa, khi bạn đọc văn bản và thấy các nhãn

được gán cho mỗi câu này,

nó có ý nghĩa, hãy ghi nhớ

rằng những chủ đề này đến từ một danh sách được xác định trước

mà mô hình mà chúng tôi đã chọn có.

Vì vậy, những nhãn mà chúng ta có ở đây sẽ chỉ là

những thứ có sẵn từ mô hình mà chúng tôi đã chỉ định.

Nếu chúng ta chọn một mô hình khác,

nó có thể có một danh sách các chủ đề khác.