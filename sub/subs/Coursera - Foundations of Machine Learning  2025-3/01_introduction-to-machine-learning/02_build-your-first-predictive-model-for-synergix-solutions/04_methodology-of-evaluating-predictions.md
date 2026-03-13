# 04 phương pháp-đánh giá-dự đoán

---

Nó không đủ để chỉ

tạo ra các dự đoán.

Những dự đoán mà chúng tôi

tạo ra phải mạnh mẽ và

làm việc trong một kịch bản thực tế là tốt.

Vì điều đó,

chúng ta cần đánh giá những dự đoán của mình.

Có hai phương pháp chính để đánh giá

những dự đoán của mô hình của bạn.

Phương pháp đầu tiên là đánh giá

tính đúng đắn của dự đoán của bạn.

Và phương pháp thứ hai là hiểu

dự đoán của bạn đáng tin cậy đến mức nào

một tập dữ liệu chưa được nhìn thấy.

Trong video này, chúng ta hãy tập trung vào

hiểu tính đúng đắn của một mô hình.

Bây giờ, xét về mặt mô hình dự đoán,

độ chính xác được đo

sử dụng các thước đo đánh giá.

Một số đánh giá chung

số liệu là sai số tuyệt đối trung bình,

lỗi bình phương gốc,

độ chính xác, độ chính xác và thu hồi.

Trong video này, chúng ta hãy hiểu một trong những

các số liệu đánh giá có nghĩa là tuyệt đối

lỗi chi tiết với một ví dụ.

Hãy tưởng tượng bạn điều hành một kênh YouTube và

muốn dự đoán số lượng người đăng ký

bạn sẽ đạt được hàng ngày.

Bảng này mô tả số người đăng ký thực tế,

và các giá trị dự đoán cho

năm ngày tiếp theo.

Bước tiếp theo sẽ là

kiểm tra xem chúng tôi chính xác đến mức nào?

Điều đó có nghĩa là chúng ta sẽ cần

để tính toán sai số.

Lỗi không là gì ngoài sự khác biệt

giữa giá trị thực tế và

các giá trị dự đoán.

Sau khi hết lỗi mỗi ngày

tính toán, trực giác đầu tiên của chúng ta có thể là

thêm tất cả các lỗi để có được giá trị của

tổng số lỗi cho tất cả các ngày cộng lại.

Đợi một chút, bạn có nhận thấy điều đó không

các lỗi tích cực bị loại bỏ

những điều tiêu cực và

tổng lỗi thấp hơn dự kiến?

Chúng tôi biết rằng những sai sót,

bất kể dấu hiệu của chúng là dương hay

tiêu cực, vẫn còn sai sót.

Một trong những giải pháp có thể tránh

loại bỏ các lỗi là để tính toán

giá trị tuyệt đối của chúng cho mỗi ngày và

sau đó tính tổng sai số tuyệt đối.

Tính tuyệt đối của cả dương và

số âm là số dương.

Ở đây bạn nhận thấy rằng tổng tuyệt đối

lỗi cao hơn nhiều so với tổng

của các lỗi.

Điều này giúp nhưng

hãy tưởng tượng tổng thể tuyệt đối như thế nào

lỗi sẽ tăng lên khi

số ngày tăng lên.

Vì vậy, để hiểu rõ hơn về lỗi,

điều quan trọng là phải tính toán

giá trị trung bình của sai số tuyệt đối.

Giá trị trung bình của sai số tuyệt đối sẽ là

459 chia cho 5 bằng 91,8.

Sai số tuyệt đối trung bình cũng thường gặp

viết tắt và gọi là MAE.

MAE cho chúng ta biết rằng trung bình,

dự đoán số lượng người đăng ký

sai lệch so với số lượng thuê bao thực tế

với sai số xấp xỉ 92.

Giá trị của MAE càng thấp thì

thấp hơn là lỗi dự kiến

từ một hệ thống dự đoán.

Hãy tóm tắt nhanh các bước mà chúng ta

vừa đi qua để tính giá trị trung bình

lỗi tuyệt đối.

Bước đầu tiên là tính toán

các giá trị được dự đoán từ mô hình của bạn cho

mỗi điểm dữ liệu.

Sau đó trừ đi số thực tế tương ứng

giá trị từ các giá trị dự đoán.

Sau đó, chỉ cần chuyển đổi

sự khác biệt thành giá trị tuyệt đối.

Sau đó chúng ta tính tổng

về sự khác biệt tuyệt đối.

Bước cuối cùng là tính toán

giá trị trung bình của các giá trị tuyệt đối.

Bây giờ bạn đã hiểu các bước,

chúng ta hãy xem xét một phép toán đơn giản

công thức đại diện cho MAE.

Ở đây n đại diện cho số lượng

các điểm dữ liệu trong tập dữ liệu.

Bây giờ chúng ta đã hiểu một trong

số liệu đánh giá chúng ta có thể sử dụng

để đánh giá dự đoán của mô hình.

Trọng tâm của chúng tôi dành cho

video này là mô hình chính xác.

Trong video tiếp theo chúng ta sẽ chuyển

trọng tâm của chúng tôi là độ tin cậy của mô hình.