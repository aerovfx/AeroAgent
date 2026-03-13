# 02 - Dữ liệu không có cấu trúc

---

- [Người hướng dẫn] Khi xử lý dữ liệu phi cấu trúc

có thể có giá trị rất cao,

phân tích nó đòi hỏi các bước xử lý bổ sung

rút ra ý nghĩa để sử dụng có hiệu quả.

Ví dụ: phân tích cảm xúc của khách hàng

từ các bài đăng trên mạng xã hội đòi hỏi phải có kỹ thuật

để chuyển đổi dữ liệu văn bản phi cấu trúc

thành một định dạng phù hợp để phân tích sâu hơn.

Dưới đây là một số loại dữ liệu phi cấu trúc phổ biến

theo kiểu dữ liệu.

Dữ liệu văn bản bao gồm email, tài liệu, bài đăng trên mạng xã hội,

nội dung web, tin nhắn trò chuyện và nhật ký.

Dữ liệu đa phương tiện bao gồm hình ảnh, tập tin âm thanh,

tập tin video và đồ họa.

Dữ liệu cảm biến bao gồm dữ liệu

từ Internet of Things hoặc thiết bị IoT,

dữ liệu đo từ xa và cảm biến môi trường.

Đo từ xa là quá trình thu thập dữ liệu

từ những nguồn xa xôi

và truyền nó đến một vị trí trung tâm

để theo dõi và phân tích.

Vì chúng ta sẽ làm việc với dữ liệu văn bản trong khóa học,

hãy xem một số ví dụ

từ tập dữ liệu Phản hồi Viễn thông của chúng tôi.

Hình ảnh hiển thị một đoạn dữ liệu văn bản dưới dạng JSON

hoặc Định dạng ký hiệu đối tượng JavaScript.

Trong ví dụ được đánh dấu,

Phản hồiText là một cặp giá trị khóa trong đối tượng đó.

Chìa khóa là Văn bản phản hồi,

và giá trị là văn bản thực tế của phản hồi,

nghĩa là "Tôi thường xuyên gặp phải tình trạng mất kết nối Internet

trong hai tuần qua."

Bây giờ hãy tạm dừng video và trả lời câu hỏi này.

Đây có phải là ví dụ về dữ liệu có cấu trúc hoặc không cấu trúc?

(nhạc sôi động)

(màn hình kêu vo vo)

Chà, mặc dù nó có chứa văn bản

trong trường Văn bản phản hồi,

dữ liệu tổng thể được cấu trúc

bởi vì nó có định dạng được xác định trước, JSON.

Mỗi phần thông tin có một nhãn hoặc khóa cụ thể.

Dữ liệu được tổ chức thành các cặp giá trị khóa.

Tạm dừng video và trả lời câu hỏi này.

Ví dụ này có cấu trúc hay không cấu trúc?

Lưu ý lý do tại sao nó có cấu trúc hoặc không có cấu trúc.

(nhạc sôi động)

(màn hình kêu vo vo)

Ví dụ này không có cấu trúc.

Thoạt nhìn, ví dụ này từ Giá trị được phân tách bằng dấu phẩy

hoặc tệp .csv có thể trông có cấu trúc.

Ý tôi là, sau tất cả ID, Mô tả, Ngày,

và các trường Ghi chú trong tệp CSV cung cấp cấu trúc

vào tập dữ liệu.

Nhưng ví dụ được coi là không có cấu trúc

do một số đặc điểm chính của dữ liệu.

Có nội dung không nhất quán.

Mỗi mục trong trường Mô tả

là một kiểu tương tác khác với khách hàng

với mức độ chi tiết và kết cấu khác nhau.

Nó chứa văn bản dạng tự do.

Văn bản là ngôn ngữ tự nhiên

và không tuân theo một định dạng được xác định trước.

Nó bao gồm các khiếu nại của khách hàng,

hỏi, phản hồi và yêu cầu.

Có nhiều loại dữ liệu khác nhau.

Văn bản có thể bao gồm nhiều yếu tố khác nhau,

chẳng hạn như các vấn đề cụ thể,

câu hỏi về kế hoạch, phản hồi dịch vụ,

hoặc yêu cầu thay đổi,

gây khó khăn cho việc phân loại một cách có hệ thống.

Ngoài ra còn thiếu các lĩnh vực nhất quán.

Ví dụ: khiếu nại về vấn đề kết nối

khác về nội dung với yêu cầu cập nhật và địa chỉ.

Văn bản được viết bằng ngôn ngữ tự nhiên,

đòi hỏi các phương pháp phân tích phức tạp,

như phân tích văn bản hoặc xử lý ngôn ngữ tự nhiên,

còn được gọi là NLP.

Và nó đòi hỏi điều này để rút ra những hiểu biết có ý nghĩa

hoặc xu hướng từ dữ liệu.

Tạm dừng video và trả lời câu hỏi này.

Ví dụ này có cấu trúc không,

bán cấu trúc hay không cấu trúc?

(nhạc sôi động)

(màn hình kêu vo vo)

Ví dụ này là bán cấu trúc.

The structured data is the ID, ImagePath,

và các trường DateCaptured

bởi vì chúng cung cấp một định dạng rõ ràng, nhất quán

để lập chỉ mục, truy cập và tham chiếu hình ảnh.

Dữ liệu phi cấu trúc là trường Mô tả và Thẻ

bởi vì chúng chứa văn bản dạng tự do

cung cấp ngữ cảnh hoặc siêu dữ liệu về hình ảnh,

nhưng thiếu một cấu trúc nhất quán.

Vì vậy, mặc dù bản thân tệp CSV có cấu trúc

xét về việc có cột và hàng,

nội dung trong các lĩnh vực nhất định,

như Mô tả và Thẻ, không có cấu trúc.

Chúng tôi vừa cung cấp cái nhìn tổng quan về cấu trúc,

dữ liệu bán cấu trúc và dữ liệu phi cấu trúc.

Bây giờ hãy tìm hiểu cách sử dụng Python để kiểm tra dữ liệu của bạn.