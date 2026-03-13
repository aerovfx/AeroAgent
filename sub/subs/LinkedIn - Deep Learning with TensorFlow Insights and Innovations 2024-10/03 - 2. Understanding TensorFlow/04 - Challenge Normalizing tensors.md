# 04 - Thử thách chuẩn hóa tensor

---

(nhạc sôi động)

- [Giảng viên] Trong phần này,

chúng ta sẽ đi sâu vào thử thách viết mã thực hành

điều đó sẽ giúp củng cố sự hiểu biết của chúng ta

của hoạt động TensorFlow.

Vì vậy, trọng tâm ở đây sẽ là việc chuẩn hóa tensor

và tính toán các số liệu thống kê cơ bản như giá trị trung bình

và độ lệch chuẩn.

Vì vậy, hãy mở không gian mã trên trình duyệt web,

và bạn sẽ thấy một màn hình như thế này.

Sau đó ở khung bên trái,

hãy tiếp tục và phóng to thư mục SRC,

và mở tệp Python 02_04_challenge.

Vì vậy chúng ta sẽ tiếp cận thử thách đặc biệt này,

giống như bài tập về nhà,

và sau đó chúng ta sẽ cùng nhau tìm hiểu giải pháp.

Bài tập này sẽ cho bạn trải nghiệm thực tế

trong việc điều khiển tensor

và sử dụng TensorFlows để ánh xạ các hàm.

Vì vậy hãy tiếp tục và thu nhỏ khung bên trái

bằng cách nhấp vào Explorer,

và bạn sẽ thấy cửa sổ bên trái sẽ biến mất

để chúng ta có thể xem thêm mã.

Vì vậy, hãy bắt đầu với thử thách của chúng tôi.

Hãy tưởng tượng bạn được tặng một tensor,

một mảng số hai chiều,

và nó chứa đầy những số nguyên ngẫu nhiên,

giữa số không và chín.

Vì vậy nhiệm vụ của bạn là chuẩn hóa tensor này

sao cho tất cả các giá trị nằm trong khoảng từ 0 đến một.

Một lần nữa, hãy nhớ lại lý do tại sao chúng ta làm điều đó,

bởi vì các giá trị rất khác nhau trong tập dữ liệu của chúng tôi,

ảnh hưởng tiêu cực đến các mô hình học máy.

Vì vậy, bằng cách bình thường hóa các giá trị giữa 0 và 1,

chúng tôi giới thiệu một số loại tiêu chuẩn hóa trong dữ liệu của mình

để thuật toán học máy của chúng tôi hoạt động tốt hơn.

Vì vậy nhiệm vụ của chúng ta ở đây là chuẩn hóa tensor này

sao cho tất cả các giá trị nằm trong khoảng từ 0 đến 1,

nhưng đó không phải là tất cả.

Sau khi chuẩn hóa tensor,

bạn cũng sẽ cần phải tính giá trị trung bình

và độ lệch chuẩn của các giá trị

trong tensor chuẩn hóa này.

Vì vậy, trong mã thử thách này,

chúng ta có tensor chuẩn hóa là không có.

Vì vậy, bạn sẽ tiếp tục và thay thế nó bằng mã của mình

có các giá trị từ 0 đến 1.

Sau đó bạn sẽ tiếp tục và tính giá trị trung bình

và độ lệch chuẩn của tensor chuẩn hóa.

Vì vậy, ngay bây giờ, chúng ta có một phần giữ chỗ,

nghĩa là bằng không,

và độ lệch chuẩn bằng không.

Vì vậy, những thứ này sẽ được thay thế bằng mã của bạn.

Vì vậy, hãy chia nhỏ thử thách này yêu cầu chúng ta làm gì.

Hãy tiếp tục và chạy mã thử thách này trước

bằng cách tìm góc ba nhỏ ở phía trên bên phải,

và hãy phóng to cửa sổ terminal.

Các cảnh báo là ổn cho trường hợp này,

và chúng chỉ ra rằng chúng tôi không sử dụng tất cả

về các chức năng mà TensorFlow cung cấp, và điều đó không sao cả.

Vì thế khi chúng ta tan vỡ

thử thách này yêu cầu chúng ta làm gì,

số một là việc tạo tensor.

Vì vậy, chúng tôi bắt đầu bằng cách tạo một TensorFlow có kích thước bốn x bốn

với số nguyên ngẫu nhiên.

Chúng ta có thể thấy một ví dụ trong cửa sổ terminal ngay bây giờ.

Vì vậy, tensor TensorFlow chứa đầy các số nguyên ngẫu nhiên,

trong trường hợp này, và nó là 4 x 4,

phạm vi số nguyên từ 0 đến 9.

Nhưng đây là một điểm quan trọng.

Tenxor được tạo dưới dạng tenxơ số nguyên,

và các hoạt động TensorFlow rất nhạy cảm với các loại dữ liệu.

Tiếp theo là chuẩn hóa, như chúng ta có thể thấy trong bản in

mà chúng tôi đã tạo trong thiết bị đầu cuối.

Vì vậy tensor chuẩn hóa vẫn chưa được tính toán.

Thử thách yêu cầu chúng ta bình thường hóa các giá trị tensor,

vì vậy tất cả chúng đều nằm trong khoảng từ 0 đến 1.

Để làm điều này, chúng ta sẽ cần phải chia tỷ lệ các giá trị

bằng cách chia chúng cho giá trị lớn nhất có thể,

trong trường hợp này là chín.

Tuy nhiên, vì chúng ta đang chia,

chúng ta cần đảm bảo tensor của chúng ta thuộc loại dấu phẩy động,

có nghĩa là số có dấu thập phân.

Nếu không, chúng ta sẽ gặp vấn đề

vì chia số nguyên,

có thể không mang lại cho chúng ta kết quả mà chúng ta mong đợi.

Sau khi chuẩn hóa tensor,

chúng ta cần tính toán hai thước đo thống kê.

Đó là những gì?

Họ là những kẻ hèn hạ,

cho chúng ta giá trị trung bình của các phần tử tensor,

và độ lệch chuẩn,

cho chúng ta biết các giá trị sai lệch bao nhiêu so với giá trị trung bình.

Vì vậy, ngay bây giờ, khung mã có phần giữ chỗ

giải pháp của bạn sẽ đi đến đâu.

Họ không được đánh dấu bởi ai cả.

Vì vậy, thách thức của bạn là lấp đầy những khoảng trống này.

Hãy tiếp tục và thử xem.