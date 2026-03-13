# 01-bắt đầu với gradio

---

[ÂM NHẠC]

Chào mừng bạn đến với Bắt đầu với Gradio.

Sau khi xem video này, bạn sẽ

có thể mô tả Gradio là gì và

giải thích cách thiết lập Gradio

Giao diện tương tác mô hình.

Gradio là một mã nguồn mở

thư viện python cho

tạo tùy chỉnh

giao diện người dùng dựa trên web.

Nó được thiết kế để dễ sử dụng,

đặc biệt là đối với các mô hình học máy và

các công cụ tính toán.

Hãy thực hiện từng bước một

hãy nhìn vào cách nó hoạt động.

Đầu tiên bạn viết mã Python vào

xác định các chức năng và logic cho

ứng dụng của bạn.

Tiếp theo bạn dùng Gradio để tạo

giao diện cho các chức năng này.

Ở đây bạn sử dụng lớp giao diện của Gradio

để xác định đầu vào và đầu ra cho

chức năng của bạn.

Sau đó cấu hình giao diện để xác định cách

người dùng sẽ tương tác với ứng dụng của bạn.

Bước tiếp theo là khởi chạy Gradio

máy chủ bằng phương pháp khởi chạy.

Điều này khởi động một máy chủ cục bộ trên của bạn

máy tạo giao diện web cho

ứng dụng của bạn.

Bước cuối cùng, bạn có quyền truy cập vào

giao diện web thông qua một địa phương hoặc

URL công khai do Gradio cung cấp.

Người dùng có thể tương tác với

giao diện cung cấp đầu vào và

nhận đầu ra trong thời gian thực.

Đầu tiên, bạn cần cài đặt

gói Gradio sử dụng PIP.

Sau khi cài đặt,

bạn có thể nhập gradio dưới dạng gr.

Bây giờ hãy code một giao diện Gradio đơn giản

có trường nhập văn bản và

sau đó hiển thị văn bản đã nhập dưới dạng đầu ra.

Hàm gr.Interface là cốt lõi

thành phần của thư viện Gradio.

Nó tạo ra các giao diện web tương tác cho

Các hàm Python có thể tùy chỉnh

thành phần đầu vào và đầu ra.

Sau đó, bạn xác định hàm là

được thực hiện khi người dùng nhập truy vấn.

Ở đây bạn có thể xác định bất kỳ chức năng nào

theo trường hợp sử dụng, trong trường hợp này,

bạn vừa trả lại văn bản nhập.

gr.Textbox được sử dụng để tạo văn bản

hộp trong đó bạn cũng có thể xác định

nhãn tùy chỉnh cho hộp văn bản.

Tương tự, bạn tạo một hộp văn bản cho

đầu ra.

Sử dụng khởi động,

sau đó bạn có thể chạy giao diện.

Đây là giao diện Gradio

bạn nhận được từ mã.

Như bạn có thể thấy ở đây, có hai văn bản

hộp, một cho đầu vào và một cho đầu ra.

Hãy xem làm thế nào bạn có thể có nhiều

đầu vào trong giao diện Gradio.

Giống như gr.Textbook được sử dụng để tạo

một trường văn bản, theo cách tương tự gr.Number là

được sử dụng để tạo một trường số.

Bạn có thể chuyển gr.Number và

gr.Textbook dưới dạng danh sách đầu vào.

Tương tự, nếu bạn muốn thêm nhiều đầu vào hơn

bạn có thể thêm chúng vào đây trong danh sách đầu vào.

Bây giờ, hãy xem đầu ra

từ mã được tạo ra.

Bạn có thể nhận thấy rằng bây giờ bạn có hai

các loại đầu vào, một cho văn bản và

một cho các giá trị số.

Bạn cũng có thể tạo tùy chọn để tải lên hoặc

thả tập tin bằng Gradio.

Đây là đoạn mã để đếm số lượng

các tập tin được người dùng tải lên. gr.File cho phép

người dùng tải tập tin lên trong giao diện web.

Nó hỗ trợ tải lên nhiều tập tin và

cung cấp đường dẫn đến các tập tin được tải lên cho

xử lý tiếp ở

chức năng phụ trợ.

Sau đó bạn xác định các tập tin đếm để

tính số lượng tập tin được tải lên bởi

người dùng.

Khi bạn khởi chạy mã,

nó tạo ra một liên kết giao diện web độc đáo

có thể được sử dụng từ bất cứ đâu

cho đến khi phiên chạy.

Bây giờ bạn có tùy chọn tải lên hoặc

thả các tập tin thông qua một giao diện web.

Hãy tóm tắt lại, trong video này bạn đã học được

rằng Gradio là một Python mã nguồn mở

thư viện để tạo tùy chỉnh

giao diện người dùng dựa trên web.

Để thiết lập nó, bạn phải viết Python

mã, tạo giao diện Gradio,

khởi chạy máy chủ Gradio

sử dụng phương pháp khởi chạy và

truy cập giao diện web thông qua một địa phương

hoặc URL công khai do Gradio cung cấp.

Bạn đã học được cách viết mã một văn bản đơn giản

đầu vào và đầu ra với giao diện Gradio,

bạn có thể sử dụng chức năng giao diện Gradio.

Cuối cùng, bạn đã học được rằng để tải lên hoặc

thả tập tin bằng Gradio vào giao diện web,

bạn có thể sử dụng gr.File.

[ÂM NHẠC]