# 04 - Trung tâm Ôm Mặt

---

- [Người hướng dẫn] Hub ôm mặt

là một nền tảng mở và hợp tác

cung cấp một kho lưu trữ tập trung

để chia sẻ và truy cập các mô hình học máy,

tập dữ liệu và tập lệnh huấn luyện.

Nó phục vụ như một hệ sinh thái hướng đến cộng đồng

nơi các nhà nghiên cứu, nhà phát triển và người thực hành

có thể đóng góp, tải xuống và thử nghiệm

với các mô hình hiện đại trên nhiều lĩnh vực khác nhau.

Trung tâm có hơn 900.000 mô hình được đào tạo trước

cho các nhiệm vụ như phân loại bài kiểm tra, dịch ngôn ngữ,

phân đoạn hình ảnh và xử lý âm thanh, v.v.

Trung tâm cũng có hơn 200.000 bộ dữ liệu

bằng hơn 8.000 ngôn ngữ.

Bộ sưu tập dữ liệu khổng lồ này có thể dễ dàng được tải

sử dụng thư viện tập dữ liệu.

Chúng bao gồm các nhiệm vụ trong các lĩnh vực như thị giác máy tính,

xử lý ngôn ngữ tự nhiên và xử lý âm thanh.

Hugging Face Hub cũng là nơi chứa hơn 300.000 ứng dụng,

được gọi là không gian.

Không gian cung cấp một cách đơn giản để xây dựng, chia sẻ,

và triển khai các bản trình diễn máy học,

sử dụng các khuôn khổ như radio và Streamlet.

Cho dù bạn là người mới học sâu

hoặc là một học viên dày dạn kinh nghiệm,

Ôm mặt Hub cung cấp một cái gì đó cho tất cả mọi người.

Khi làm việc với các người mẫu được đào tạo trước trong Ôm mặt,

thư viện máy biến áp là vô giá,

và một trong những chức năng linh hoạt nhất

trong thư viện máy biến áp

là chức năng đường ống.

Chức năng đường ống cho phép chúng ta kết nối

và sử dụng bất kỳ mô hình được đào tạo trước nào từ trung tâm

đã được tinh chỉnh cho một nhiệm vụ cụ thể.

Ví dụ: để sử dụng mô hình được đào tạo trước

để phân tích tình cảm,

chúng tôi chỉ cần tạo một đường dẫn bằng cách chỉ định nhiệm vụ.

Sau đó, chúng tôi chuyển văn bản đầu vào vào đường dẫn.

Sau khi chúng tôi chỉ định một nhiệm vụ

và chuyển văn bản đến chức năng đường ống,

nó thực hiện ba việc đằng sau hậu trường cho chúng tôi.

Nó xử lý văn bản

thành một định dạng mà mô hình có thể hiểu được.

Các đầu vào được xử lý trước được chuyển đến mô hình,

đó thực hiện nhiệm vụ được chỉ định.

Kết quả đầu ra của mô hình được xử lý sau

và truyền lại cho chúng tôi.

Theo mặc định, chức năng đường ống quyết định

sử dụng mô hình được đào tạo trước nào dựa trên nhiệm vụ chúng tôi chỉ định.

Tuy nhiên, nếu chúng ta quyết định sử dụng một mô hình do chính chúng ta lựa chọn,

chúng ta có thể làm như vậy

Trong video tiếp theo,

chúng ta sẽ trải qua quá trình chọn mô hình phù hợp

từ Hugging Face Hub cho mọi tác vụ được hỗ trợ.

Các quy trình dành riêng cho nhiệm vụ có sẵn cho âm thanh,

thị giác máy tính, xử lý ngôn ngữ tự nhiên,

và các nhiệm vụ đa phương thức.

Một số tác vụ đường ống được sử dụng phổ biến nhất

để xử lý ngôn ngữ tự nhiên

bao gồm phân loại mã thông báo,

được sử dụng để nhận dạng thực thể được đặt tên,

và một phần của việc gắn thẻ bài phát biểu,

phân loại văn bản,

được sử dụng để phân tích tình cảm

và phân loại chủ đề,

tóm tắt, trả lời câu hỏi và dịch thuật.

Trong phần tiếp theo của khóa học,

chúng ta sẽ thực hành xây dựng quy trình Ôm Mặt

sử dụng một số tác vụ này.