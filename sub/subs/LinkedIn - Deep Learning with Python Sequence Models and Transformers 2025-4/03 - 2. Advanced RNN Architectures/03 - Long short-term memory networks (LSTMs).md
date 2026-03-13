# 03 - Mạng bộ nhớ ngắn hạn dài (LSTM)

---

- [Giảng viên] Một trong những hạn chế chính

của mạng lưới thần kinh hồi quy tiêu chuẩn là chúng không có khả năng

để nắm bắt sự phụ thuộc lâu dài trong dữ liệu trình tự.

Điều này xuất phát từ vấn đề độ dốc biến mất

nơi độ dốc co lại khi chúng được truyền bá

ngược thời gian, khiến cho các đầu vào trước đó có ít

không ảnh hưởng đến dự đoán của mạng.

Kết quả là khi xử lý một câu dài

RNN có thể gặp khó khăn trong việc kết nối nghĩa của một từ

ở cuối câu với ngữ cảnh

được cung cấp bởi các từ ở đầu.

Để giải quyết thách thức này, các mạng bộ nhớ ngắn hạn dài,

còn được gọi là LSTM, đã được phát triển.

LSTM giới thiệu một cơ chế nội bộ tinh vi

được thiết kế để điều chỉnh luồng thông tin,

cho phép họ duy trì sự phụ thuộc lâu dài một cách hiệu quả.

Hai thành phần chính trong LSTM cho phép chúng thực hiện được điều này.

Đầu tiên là trạng thái tế bào, hoạt động như một đường cao tốc

để truyền thông tin xuyên suốt chuỗi.

Thứ hai là một bộ cổng kiểm soát dòng chảy

thông tin vào, ra và bên trong trạng thái tế bào.

Những cổng này, bản thân chúng là những mạng lưới thần kinh nhỏ,

xác định thông tin nào được thêm vào, giữ lại,

hoặc bị loại bỏ khỏi trạng thái tế bào.

Luồng thông tin trong LSTM bắt đầu bằng cổng quên,

quyết định thông tin nào từ trạng thái ô trước đó

nên bị loại bỏ và nên được chuyển tiếp.

Điều này đặc biệt quan trọng để lọc ra

thông tin không liên quan hoặc lỗi thời.

Cổng quên lấy trạng thái ẩn trước đó

và đầu vào hiện tại, kết hợp chúng,

và chuyển chúng thông qua hàm kích hoạt sigmoid.

Hàm sigmoid xuất ra các giá trị từ 0 đến 1,

trong đó các giá trị gần bằng 0 biểu thị thông tin

điều đó nên bị lãng quên và có giá trị gần bằng một

cho biết thông tin cần được giữ lại.

Để biết thêm thông tin về chức năng kích hoạt sigmoid

và các chức năng kích hoạt khác

thường được sử dụng trong học sâu

xem video "Chức năng kích hoạt trong mạng thần kinh",

là một phần của Deep Learning với Python

khóa học nền tảng.

Tiếp theo là cổng đầu vào.

Cổng đầu vào xác định thông tin mới nào

từ đầu vào hiện tại sẽ được thêm vào trạng thái ô.

Điều này cho phép mô hình cập nhật bộ nhớ của nó

với dữ liệu liên quan từ bước thời gian hiện tại.

Nó thực hiện điều này trong ba bước.

Đầu tiên, trạng thái ẩn trước đó và đầu vào hiện tại

được truyền qua hàm sigmoid.

Các đầu vào tương tự cũng được chuyển qua một tanh

hàm kích hoạt để tạo một vectơ ứng cử viên

của các giá trị mới được chia tỷ lệ giữa âm một và một.

Sau đó, đầu ra của hàm sigmoid và tanh

được nhân theo từng phần tử,

cho phép đầu ra sigmoid hoạt động như một bộ lọc

xác định phần nào của vectơ ứng viên

được thêm vào trạng thái ô.

Khi cổng quên và đầu ra của cổng đầu vào được tính toán

trạng thái ô được cập nhật.

Điều này liên quan đến việc nhân trạng thái ô hiện tại

bởi vectơ quên, là đầu ra của cổng quên

để loại bỏ những thông tin không liên quan,

và thêm vectơ ứng cử viên từ cổng đầu vào

đến trạng thái tế bào.

Quá trình này đảm bảo rằng trạng thái tế bào được giữ lại

thông tin phù hợp nhất

đồng thời loại bỏ những dữ liệu không cần thiết.

Cổng đầu ra xác định thông tin nào

từ trạng thái ô nên được đưa vào trạng thái ẩn,

được sử dụng để đưa ra dự đoán

và chuyển ngữ cảnh sang bước thời gian tiếp theo.

Nó cũng thực hiện điều này theo ba bước.

Đầu tiên, trạng thái ẩn trước đó và đầu vào hiện tại

được truyền qua hàm sigmoid

để tạo một bộ lọc sẽ xác định phần nào

của trạng thái ô sẽ đóng góp vào trạng thái ẩn mới.

Sau đó, trạng thái ô cập nhật được chuyển

thông qua hàm tanh để chia tỷ lệ các giá trị của nó

giữa âm một và một.

Cuối cùng, đầu ra của hàm sigmoid và tanh

được nhân lên để tạo ra trạng thái ẩn mới.

Trạng thái ẩn mới này sau đó được chuyển sang bước thời gian tiếp theo,

cùng với trạng thái ô được cập nhật.

Sự kết hợp của các cổng quên, đầu vào và đầu ra

cho phép LSTM quản lý luồng một cách linh hoạt

thông tin trong suốt một chuỗi.

Điều này làm cho chúng có hiệu quả cao trong việc xử lý

sự phụ thuộc lâu dài, vì họ có thể giữ lại một cách có chọn lọc

bối cảnh có liên quan trong khi loại bỏ

dữ liệu không liên quan hoặc lỗi thời.