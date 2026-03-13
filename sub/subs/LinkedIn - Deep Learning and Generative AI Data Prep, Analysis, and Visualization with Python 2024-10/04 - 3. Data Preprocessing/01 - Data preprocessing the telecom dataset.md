# 01 - Tiền xử lý dữ liệu bộ dữ liệu viễn thông

---

- [Giảng viên] Trong bài học này,

chúng tôi đã xử lý trước dữ liệu viễn thông

cho trường hợp sử dụng giá trị trọn đời của khách hàng của chúng tôi.

Xin nhắc lại, quá trình tiền xử lý dữ liệu đề cập cụ thể đến

các bước thực hiện để chuẩn bị dữ liệu thô

để sử dụng trong mô hình học máy.

Như bạn nhớ lại, điều này liên quan đến các nhiệm vụ

như làm sạch dữ liệu, xử lý các giá trị còn thiếu

hoặc giá trị null, trùng lặp, kiểu dữ liệu không chính xác,

và các vấn đề dữ liệu lộn xộn khác mà dữ liệu thô có thể chứa đựng.

Dưới đây là các bước bạn đã thực hiện

trong quá trình kiểm tra dữ liệu ban đầu của bạn ở phòng thí nghiệm đầu tiên.

Hai bước mới này chuyển đổi dữ liệu thô

vào một cái gì đó khác nhau.

Bước 3.3.1 chuyển đổi tên cột thành chữ thường.

Bước 3.3.2 thay thế dấu cách bằng dấu gạch dưới.

Vì vậy, hãy tìm hiểu cách chúng ta có thể chuyển đổi

dữ liệu viễn thông thô thành thứ gì đó có ý nghĩa

để sau đó chúng tôi có thể thực hiện phân tích dữ liệu thăm dò,

mà chúng tôi sẽ đề cập trong chương tiếp theo.

Đây là quy trình xử lý trước dữ liệu mà chúng tôi sẽ sử dụng.

Lưu ý, quy trình làm việc này dựa trên kết quả

về khám phá ban đầu của bạn trong phòng thí nghiệm đầu tiên.

Dưới đây là các giá trị còn thiếu cho tập dữ liệu viễn thông của chúng tôi.

Mỗi tính năng, cột hiển thị ở đây phải có màu đen,

nhưng một số thì không.

Một số bị thiếu.

Trước khi điền các giá trị còn thiếu,

hiểu tại sao dữ liệu có thể bị thiếu.

Có một số phương pháp để xử lý các giá trị bị thiếu

chẳng hạn như tính toán trung bình/trung bình, điền tiến/lùi,

hoặc bỏ các giá trị còn thiếu.

Ví dụ hàng đầu ở đây cho thấy

mà chúng tôi đang điền vào các cột phân loại của mình,

cột ưu đãi và cột thanh toán có giá trị.

Các giá trị còn thiếu trong cột ưu đãi

sẽ được thay thế bằng Không.

Và các giá trị còn thiếu trong cột phương thức thanh toán

sẽ được thay thế bằng Thẻ tín dụng.

Đối với các cột số của chúng tôi, chúng tôi sẽ tính giá trị trung bình

hoặc gigabit và thu nhập

rồi điền giá trị trung bình đã tính vào các giá trị còn thiếu.

Mặc dù phương pháp này đơn giản nhưng

điều cần thiết là phải nhận thức được những hạn chế tiềm ẩn của nó.

Ví dụ: thay thế các giá trị bị thiếu

với ý nghĩa có thể bóp méo

sự phân bố ban đầu của dữ liệu,

đặc biệt nếu có một số lượng đáng kể

của các giá trị còn thiếu.

Chúng tôi không có hàng trùng lặp trong tập dữ liệu của mình,

nhưng hiểu tại sao các bản sao tồn tại là quan trọng.

Chúng có phải là bản sao thực sự với các hàng giống hệt nhau không

không có thông tin bổ sung?

Hoặc gần các bản sao có hàng có giá trị tương tự,

nhưng có sự khác biệt nhỏ?

Hoặc lỗi nhập dữ liệu với dữ liệu nhập sai?

Trong xử lý và phân tích dữ liệu,

Mã Zip thường không được coi là số nguyên

hoặc các giá trị số, mặc dù chúng bao gồm các số.

Mã Zip ở một số vùng,

đặc biệt là ở vùng đông bắc Hoa Kỳ,

có thể bắt đầu bằng số không.

Nếu Mã Zip được lưu trữ dưới dạng số nguyên hoặc số,

những số 0 nghiêng này sẽ bị mất,

điều đó sẽ làm hỏng dữ liệu

và có khả năng gây ra vấn đề

trong việc xử lý và phân tích dữ liệu.

Hãy coi Mã Zip là mã định danh.

Chúng không có giá trị số.

Bạn không thể cộng, trừ hoặc lấy trung bình mã zip.

Tiếp theo, chuyển đổi cột zip_code

tới một đối tượng hoặc chuỗi .astype.

Sau đó sử dụng .dtype để kiểm tra kiểu dữ liệu

của cột zip_code.

Khi bạn đã thực hiện xong việc này, nó sẽ hiển thị đối tượng dưới dạng kiểu dữ liệu.

Một ngoại lệ là một điểm dữ liệu trong tập dữ liệu

khác xa với tất cả các quan sát khác.

Nó nằm ngoài sự phân bố tổng thể của tập dữ liệu.

Điểm z là một khái niệm quan trọng trong thống kê

bởi vì nó giúp chúng tôi hiểu liệu một giá trị dữ liệu

lớn hơn hoặc nhỏ hơn mức trung bình hoặc trung bình

và nó cách giá trị trung bình bao xa.

Cụ thể hơn, điểm z cho chúng ta biết

có bao nhiêu độ lệch chuẩn

a data point is from the mean.

Mã này ở bên trái tạo ra điểm z

cho cột tổng_doanh thu.

Đầu ra được hiển thị bên phải.

Nhưng đầu tiên ở bên trái, chúng tôi nhập scipy

với câu lệnh thống kê nhập từ scipy,

và đó là vì scipy là thư viện Python

được sử dụng cho tính toán khoa học và kỹ thuật.

Nó cung cấp các thói quen thực sự hiệu quả

để tích hợp số, tối ưu hóa,

đại số tuyến tính và thống kê.

Vì vậy, bằng cách sử dụng scipy, chúng ta có thể kiểm tra các hàng

với điểm z trên 3.

Có năm hàng.

Và sau đó chúng tôi xóa bất kỳ hàng nào có điểm z trên 3,

và chúng tôi giữ các hàng có điểm z nhỏ hơn 3.

Đó là một phương pháp để xử lý các ngoại lệ.

Ô mã này hiển thị tất cả các cột phân loại của chúng tôi.

Mỗi cột có giá trị

đó là chuỗi chứ không phải số.

Hầu hết các thuật toán học máy đều yêu cầu

dữ liệu số làm đầu vào.

Các tính năng phân loại, đại diện cho danh mục hoặc nhãn,

ví dụ: dịch vụ điện thoại, nhiều đường dây,

hoặc dịch vụ internet, không thể xử lý trực tiếp

bởi các thuật toán này.

Nói cách khác, làm thế nào để chúng ta đi từ các cột có

hoặc không có giá trị nào cho các cột có số 1 và số 0?

Để làm điều này, chúng ta cần mã hóa các cột phân loại của mình.

Mã hóa là quá trình chuyển đổi dữ liệu phân loại

sang định dạng số mà mô hình có thể hiểu được.

Scikit's learn LabelEncode chuyển đổi dữ liệu phân loại,

nhãn văn bản thành nhãn số.

Nó thực hiện điều này bằng cách gán một số nguyên duy nhất

cho từng danh mục trong dữ liệu.

Như bạn có thể thấy, hình ảnh trước hiển thị

các cột đối tượng nơi kiểu dữ liệu

cho các cột phân loại được hiển thị dưới dạng đối tượng.

Nhưng hình ảnh bên phải không hiển thị vật thể nào,

chỉ là số nguyên hoặc số float dưới dạng kiểu dữ liệu.

Và ở đây hình ảnh hiển thị các cột đối tượng

với giá trị là 1 hoặc 0.

Khi chúng tôi đã xử lý các vấn đề tiền xử lý dữ liệu

đối với trường hợp sử dụng của chúng tôi, chúng tôi lưu tệp bằng tên mới.

Sau đó chúng tôi sẽ tải lên cái mới này đã được làm sạch

và xử lý tệp vào Notebook Jupyter

để bắt đầu phân tích dữ liệu thăm dò.