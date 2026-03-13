# 04 - Đơn vị định kỳ có kiểm soát (GRU)

---

- [Người hướng dẫn] Ở video trước chúng ta đã học

mạng bộ nhớ ngắn hạn dài, LSDM, đã được giới thiệu

như một cách để giải quyết vấn đề độ dốc biến mất.

Mặc dù có hiệu quả cao nhưng LSDM rất phức tạp,

liên quan đến nhiều cổng

và một trạng thái tế bào riêng biệt,

có thể làm cho chúng tốn kém về mặt tính toán.

Để đơn giản hóa kiến trúc này,

các nhà nghiên cứu đã phát triển các đơn vị định kỳ có kiểm soát, GRU,

một sự thay thế hợp lý mà vẫn giữ được nhiều

về chức năng của LSTM, đồng thời giảm độ phức tạp.

GRU đơn giản hóa thiết kế bằng cách kết hợp một số

của các cổng được tìm thấy trong LSTM

và loại bỏ hoàn toàn trạng thái ô riêng biệt.

Mặc dù kiến trúc đơn giản hơn,

GRU có hiệu quả cao trong việc xử lý dữ liệu tuần tự,

đặc biệt khi hiệu quả tính toán là ưu tiên hàng đầu.

Hãy đi sâu vào chi tiết về cách GRU hoạt động,

và chúng khác với LSTM như thế nào.

Trọng tâm của GRU là hai loại thành phần.

Đầu tiên là trạng thái ẩn,

mang thông tin chuyển tiếp theo thời gian, các bước,

và loại bỏ sự cần thiết của một trạng thái tế bào riêng biệt.

Thứ hai là hai loại cổng: cổng reset,

quyết định lượng thông tin trong quá khứ cần quên,

và cổng cập nhật, quyết định số lượng

của thông tin hiện tại cần lưu giữ,

và bao nhiêu thông tin trong quá khứ cần chuyển tiếp.

Các cổng này phối hợp với nhau để điều tiết dòng chảy

thông tin, cho phép GRU nắm bắt cả ngắn hạn

và sự phụ thuộc lâu dài vào dữ liệu trình tự.

Dòng thông tin bắt đầu

với một cổng đặt lại, xác định số lượng

của thông tin quá khứ được lưu trữ

ở trạng thái ẩn nên bị lãng quên.

Điều này đặc biệt quan trọng để đảm bảo

rằng mô hình tập trung vào thông tin liên quan

đồng thời loại bỏ bối cảnh lỗi thời hoặc không liên quan.

Cổng reset lấy trạng thái ẩn trước đó

và đầu vào hiện tại,

và chuyển chúng thông qua hàm kích hoạt sigmoid.

Hàm sigmoid xuất ra các giá trị giữa 0

và một, trong đó các giá trị gần bằng 0 biểu thị thông tin

quên đi và những giá trị gần lại

để một chỉ ra thông tin để giữ lại.

Khi cổng đặt lại đã được áp dụng,

mạng tính toán trạng thái ẩn của ứng viên,

đại diện cho thông tin mới

được thêm vào ở bước thời gian hiện tại.

Nó thực hiện điều này trong hai bước.

Đầu tiên, đầu ra của cổng đặt lại được nhân với phần tử khôn ngoan

với trạng thái ẩn trước đó.

Điều này cho phép mô hình bỏ qua có chọn lọc các phần

của trạng thái ẩn trước đó,

dựa trên quyết định của cổng reset.

Thứ hai, kết quả được kết hợp với đầu vào hiện tại

và được chuyển qua hàm kích hoạt tan H

để tạo trạng thái ẩn ứng viên.

Trạng thái ẩn ứng viên nắm bắt thông tin mới

có thể được kết hợp

thành phiên bản cập nhật của trạng thái ẩn.

Tiếp theo là cổng cập nhật.

Cổng cập nhật xác định số lượng

thông tin hiện tại từ trạng thái ẩn của ứng viên

để kết hợp và bao nhiêu

thông tin trong quá khứ từ trạng thái ẩn trước đó

để giữ lại.

Cổng này có vai trò tương tự

đến các cổng nhập và quên kết hợp trong LSTM,

nhưng hiệu quả tính toán hơn.

Cổng cập nhật lấy trạng thái ẩn trước đó

và đầu vào hiện tại,

và chuyển chúng thông qua hàm kích hoạt sigmoid.

Đầu ra quyết định sự cân bằng

giữa trạng thái ẩn của ứng cử viên

và trạng thái ẩn trước đó.

Các đầu ra của cổng cập nhật có thể được giải thích

như một hệ số trọng số trong đó các giá trị gần bằng 1 biểu thị

thông tin mới cần được nhấn mạnh,

trong khi các giá trị gần bằng 0 biểu thị

thông tin quá khứ đó cần được giữ lại.

Cuối cùng, trạng thái ẩn mới được tính toán

bằng cách kết hợp trạng thái ẩn ứng viên

và trạng thái ẩn trước đó, sử dụng cổng cập nhật.

Điều này đạt được thông qua một khoản tiền có trọng số

nơi nhân kết quả đầu ra

của cổng cập nhật, với trạng thái ẩn ứng viên,

kết hợp các thông tin mới,

và nhân một trừ đi đầu ra của cổng cập nhật

với trạng thái ẩn trước đó vẫn có liên quan,

thông tin quá khứ.

Sự hòa trộn giữa quá khứ và hiện tại đảm bảo

rằng GRU có thể, một cách hiệu quả,

cân bằng duy trì bối cảnh lâu dài,

đồng thời kết hợp thông tin mới.

Bất chấp sự đơn giản hóa về mặt kiến trúc,

so với LSTM, GRU có khả năng cao

nắm bắt được sự phụ thuộc lâu dài, làm cho chúng trở nên hiệu quả

để mô hình hóa dữ liệu trình tự.

Hiệu quả tính toán của chúng cũng làm cho chúng,

đặc biệt, hấp dẫn đối với các ứng dụng

với nguồn lực hạn chế hoặc khi cần đào tạo nhanh hơn.