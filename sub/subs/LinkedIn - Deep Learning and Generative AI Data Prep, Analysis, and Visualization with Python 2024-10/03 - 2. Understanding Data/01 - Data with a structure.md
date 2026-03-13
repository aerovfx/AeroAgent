# 01 - Dữ liệu có cấu trúc

---

- [Người hướng dẫn] Có ba loại dữ liệu,

dữ liệu có cấu trúc,

dữ liệu bán cấu trúc,

và dữ liệu phi cấu trúc.

Dữ liệu có cấu trúc là thông tin được sắp xếp gọn gàng

phù hợp với các danh mục được xác định trước,

như hàng và cột trong cơ sở dữ liệu hoặc bảng tính.

Điều này giúp dễ dàng tìm kiếm, phân tích và sử dụng

cho các nhiệm vụ như quản lý khách hàng hoặc báo cáo tài chính.

Ví dụ: cơ sở dữ liệu khách hàng có các cột tên,

địa chỉ và lịch sử mua hàng là dữ liệu có cấu trúc.

Dữ liệu bán cấu trúc có một số cấu trúc tổ chức,

nhưng không cứng nhắc như dữ liệu có cấu trúc.

Dữ liệu bán cấu trúc có thể chứa thẻ hoặc nhãn

để phân loại thông tin,

làm cho nó dễ dàng xử lý hơn dữ liệu phi cấu trúc.

Một ví dụ về dữ liệu phi cấu trúc là một bài đăng trên mạng xã hội.

Nó chứa văn bản, hình ảnh và đôi khi là video,

nhưng nó không vừa khít với các hàng và cột,

như dữ liệu có cấu trúc.

Dữ liệu phi cấu trúc không có thứ tự cụ thể.

Mặc dù nó có thể có giá trị,

nó đòi hỏi nỗ lực nhiều hơn để sắp xếp và hiểu.

Hãy tưởng tượng bạn đang cố gắng tìm một cuốn sách cụ thể

trong một đống sách khổng lồ.

Dữ liệu phi cấu trúc bao gồm các tài liệu văn bản,

hình ảnh và video.

Trong dữ liệu có cấu trúc,

dữ liệu số đại diện cho số lượng

và có thể được đo hoặc đếm,

Ví dụ: độ tuổi, thu nhập,

giá cả, khoảng cách.

Dữ liệu phân loại thể hiện chất lượng hoặc phân loại

và không thể đặt hàng trực tiếp

hoặc vận hành toán học trên,

Ví dụ: màu sắc, đỏ, xanh dương, xanh lá cây,

hoặc danh mục sản phẩm, đồ điện tử, quần áo hoặc sách.

Nếu dữ liệu có thể được biểu diễn bằng số,

thì nó là số

và có thể kín đáo,

như một số hoặc một số nguyên,

nghĩa là chúng ta có thể đếm nó,

hoặc liên tục, nghĩa là chúng ta có thể đo nó trên thang đo.

Giá trị số được biểu diễn bằng số nguyên,

phân số hoặc tỷ lệ phần trăm.

Các đặc tính số có thể là giá nhà,

số từ trong một tài liệu,

thời gian cần thiết để đi du lịch đâu đó, ví dụ,

và trong tập dữ liệu viễn thông của chúng tôi,

chúng ta có thể tính phí hàng tháng và tổng số cuộc gọi,

nhưng chúng ta không thể đếm cường độ tín hiệu,

vì vậy cường độ tín hiệu được coi là liên tục.

Cường độ tín hiệu thường được đo bằng decibel milliwatts,

và biểu thị cường độ tín hiệu nhận được

bởi thiết bị của khách hàng từ các tháp của mạng viễn thông.

Nếu dữ liệu không thể được biểu diễn bằng số,

sau đó nó là phân loại

và có thể là danh nghĩa, nghĩa là chúng ta có thể đặt tên cho nó,

hoặc thứ tự, nghĩa là chúng ta có thể xếp hạng nó.

Trong bộ dữ liệu viễn thông của chúng tôi,

chúng ta có thể đặt tên cho phương thức thanh toán,

thẻ tín dụng, thẻ ghi nợ hoặc chuyển khoản ngân hàng.

Và chúng ta có thể xếp hạng mức độ hài lòng của khách hàng,

hài lòng, phần nào hài lòng hoặc không hài lòng.

Vì vậy, trong khi dữ liệu số đại diện cho dữ liệu định lượng,

dữ liệu phân loại đại diện cho dữ liệu định tính.

Dưới đây là một số tính năng từ tập dữ liệu viễn thông của chúng tôi.

Trạng thái rời bỏ là số hay phân loại?

Nếu bạn trả lời phân loại, bạn đã đúng

bởi vì bạn có thể nhóm trạng thái rời bỏ

thành hai loại hoặc nhóm, có hoặc không.

Những tính năng khác là phân loại?

Có, nhóm tuổi và phân khúc khách hàng.

Trong ví dụ này, giá trị số duy nhất

dường như là điểm hài lòng của khách hàng.

Hãy đi sâu vào một bài tập thực hành.

Chúng ta sẽ bắt đầu bằng cách tải bộ dữ liệu viễn thông

để khám phá các ví dụ về số

và dữ liệu có cấu trúc phân loại,

và trên đường đi, bạn sẽ nhặt được một số thứ cần thiết,

mã Python dễ học để kiểm tra chất lượng dữ liệu,

bước quan trọng đầu tiên trong bất kỳ hành trình xử lý trước dữ liệu nào.