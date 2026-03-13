# 02 xác nhận bên ngoài

---

Để có thể đo lường mức độ khái quát

của một mô hình trên một quần thể mà nó chưa từng thấy,

chúng tôi muốn có thể đánh giá

trên tập kiểm tra từ quần thể mới.

Điều này được gọi là xác nhận bên ngoài.

Xác nhận bên ngoài có thể được đối chiếu

với xác nhận nội bộ, khi bộ kiểm tra

được rút ra từ cùng một phân phối

làm tập huấn luyện cho mô hình.

Và nếu chúng ta thấy rằng chúng ta không

khái quát hóa cho dân số mới,

sau đó chúng ta có thể lấy thêm một vài mẫu từ

dân số mới để tạo ra một lượng nhỏ

tập huấn luyện và xác nhận và

sau đó tinh chỉnh mô hình trên dữ liệu mới này.

Tất cả những nghiên cứu mà chúng ta đã nói chuyện

về việc làm việc với dữ liệu hồi cứu,

có nghĩa là họ đã sử dụng trong lịch sử

dữ liệu được dán nhãn để huấn luyện và kiểm tra các thuật toán.

Tuy nhiên, để hiểu được công dụng

của các mô hình AI trong thế giới thực,

chúng cần được áp dụng vào

dữ liệu thực tế hoặc dữ liệu tương lai.

Đối với mô hình chụp X-quang ngực, điều này có thể

có nghĩa là chúng tôi áp dụng một mô hình đã được huấn luyện

để diễn giải các hình chụp X-quang ngực như chúng

đang được thực hiện cho bệnh nhân mới.

Tại sao kết quả của mô hình có thể

trông khác nhau trên dữ liệu triển vọng?

Một lý do cho

đây là với dữ liệu hồi cứu,

thường có các bước được thực hiện để xử lý và

làm sạch dữ liệu, nhưng

trong thế giới thực,

mô hình phải làm việc với dữ liệu thô.

Như một ví dụ cụ thể về điều này,

tập dữ liệu bạn đã đào tạo mô hình của mình

đã được lọc thành chỉ

bao gồm chụp X-quang trán,

nơi chụp X-quang từ phía trước hoặc

lưng của bệnh nhân.

Tuy nhiên, trong thế giới thực,

người ta cũng thường lấy một phần của

X-quang từ phía bệnh nhân.

Chúng được gọi là chụp X-quang bên.

Trước khi mô hình của chúng tôi có thể được áp dụng vào

thế giới thực, chúng ta sẽ cần

để lọc những bức ảnh chụp X-quang ngực như vậy hoặc

điều chỉnh mô hình để làm việc trên chúng.