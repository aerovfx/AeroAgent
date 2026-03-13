# 01 - Phân tích dữ liệu thăm dò (EDA)

---

- [Người hướng dẫn] Trong video này,

chúng ta sẽ đi sâu vào phân tích dữ liệu thăm dò.

Trong chương trước, chúng ta đã kiểm tra dữ liệu ban đầu

và một số phân tích dữ liệu thăm dò sơ bộ.

EDA sơ bộ của chúng tôi đã kiểm tra tập dữ liệu viễn thông của chúng tôi

để hiểu cấu trúc, nội dung và các vấn đề tiềm ẩn của nó.

EDA sơ bộ này cho phép chúng tôi xử lý trước dữ liệu

và giải quyết một số vấn đề.

EDA cũng có thể hướng dẫn việc tạo ra các tính năng mới

từ dữ liệu hiện có

hoặc sự chuyển đổi của các tính năng hiện có

để cải thiện hiệu suất của mô hình.

Bằng cách hiểu rõ hơn về dữ liệu,

bạn có thể hiểu rõ hơn lý do tại sao một mô hình

đưa ra những dự đoán nhất định,

hỗ trợ trong việc giải thích hành vi của nó.

Hãy nhớ lại rằng chúng tôi đang sử dụng Python

với các thư viện rất hữu ích của nó,

như Pandas, NumPy, Matplotlib và Scikit-learn.

Vậy giá trị của việc xử lý trước dữ liệu đối với EDA là gì?

Chà, phương thức thanh toán ban đầu là một tính năng phân loại

với ba giá trị:

thẻ tín dụng, rút tiền ngân hàng và kiểm tra thư.

Nhưng chúng tôi không có cách nào để phân tích dữ liệu

trong tính năng phân loại này

bởi vì nó chứa các từ chứ không phải số.

Phương thức thanh toán được mã hóa một lần

và bây giờ chứa các giá trị số 0, 1 và 2.

Trục y biểu thị tần số,

tài khoản quan sát của chúng tôi đối với từng giá trị phương thức thanh toán,

và trục x biểu thị phương thức thanh toán.

Sức mạnh của EDA là bằng cách lập bản đồ

các giá trị số cho nhãn,

chúng ta có thể thu thập được cái nhìn sâu sắc hơn từ dữ liệu.

Ví dụ: thẻ tín dụng là phương tiện thường xuyên nhất

phương thức thanh toán với khoảng 4.000 lần xuất hiện.

Rút tiền ngân hàng là lần thường xuyên thứ hai

với khoảng 3.000 lần xuất hiện.

Kiểm tra thư là ít thường xuyên nhất

với khoảng 500 lần xuất hiện.

Đây là một ví dụ khác

giá trị của việc xử lý trước dữ liệu đối với EDA.

Mã zip là một mã định danh.

Nó trông giống như một con số trong dữ liệu thô

và nó được liệt kê dưới dạng số nguyên.

Chúng tôi đã sửa kiểu dữ liệu và sau khi thực hiện việc đó,

sau đó chúng ta có thể sử dụng nó để phân tích địa lý.

Ví dụ: có bốn nhóm khách hàng riêng biệt

được biểu thị bằng màu sắc khác nhau.

Mỗi cụm đại diện cho một nhóm khách hàng

những người ở gần nhau về mặt địa lý.

Cụm số 0 hoặc màu xanh tập trung

ở vùng cực nam của California,

trong khi cụm màu xanh lá cây trải rộng

khắp vùng cực bắc của California.

Chiến lược tiếp thị có thể được điều chỉnh

phù hợp với nhu cầu và sở thích cụ thể của từng nhóm.

Trong phòng thí nghiệm,

bạn sẽ có ví dụ về từng hình ảnh trực quan được hiển thị ở đây.

Biểu đồ hình tròn cho thấy hiệu suất mạnh mẽ

cho các hợp đồng hàng tháng giữa các khách hàng

với một phần đáng kể cũng chọn thời hạn một năm

và hợp đồng hai năm.

Thông tin này có thể được sử dụng

để phát triển các chiến lược tiếp thị mục tiêu

và cải thiện nỗ lực giữ chân khách hàng.

Biểu đồ phân tán của chúng tôi trực quan hóa mối quan hệ

giữa thời gian sử dụng của khách hàng theo tháng và tổng doanh thu.

Khách hàng lâu năm

có xu hướng tạo ra tổng doanh thu nhiều hơn,

nhưng có sự khác biệt đáng kể,

đặc biệt là những người có thâm niên lâu năm.

Điều này nhấn mạnh tầm quan trọng của việc giữ chân khách hàng

và tiềm năng cho các chiến lược tiếp thị mục tiêu

để tối đa hóa doanh thu từ cả khách hàng mới và khách hàng hiện tại.

Biểu đồ của chúng tôi với ước tính mật độ hạt nhân, KDE, biểu đồ

trực quan hóa việc phân bổ chi phí hàng tháng

cho khách hàng trong tập dữ liệu.

Ví dụ: đỉnh đầu tiên của chúng xảy ra ở khoảng $20,

cho thấy một lượng lớn khách hàng

có chi phí hàng tháng thấp.

Đỉnh thứ hai xảy ra quanh phạm vi $80,

chỉ ra một nhóm khách hàng quan trọng khác

với mức phí hàng tháng cao hơn.

Hãy nhớ rằng, mục tiêu chính của EDA

là để hiểu dữ liệu,

làm quen với cấu trúc dữ liệu,

loại và phân bố,

khám phá các mô hình, xác định xu hướng, mối tương quan,

và sự bất thường trong dữ liệu,

và kiểm tra các giả định

nơi bạn xác minh các giả định cơ bản

cho các mô hình thống kê

Bây giờ chúng ta hãy bắt tay vào thực hành thử thách.