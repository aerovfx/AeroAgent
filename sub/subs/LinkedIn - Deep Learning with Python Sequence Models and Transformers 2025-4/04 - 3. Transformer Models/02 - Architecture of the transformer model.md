# 02 - Kiến trúc mô hình máy biến áp

---

- [Người hướng dẫn] Máy biến áp là thiết bị mã hóa-giải mã

kiến trúc mạng lưới thần kinh

sử dụng sự chú ý của bản thân và mã hóa vị trí

để xử lý dữ liệu tuần tự song song,

loại bỏ sự cần thiết của cách tiếp cận đệ quy

được sử dụng bởi các kiến trúc dựa trên RNN.

Máy biến áp thường được chia

thành hai thành phần chính,

thành phần mã hóa và thành phần giải mã.

Thành phần mã hóa chấp nhận một chuỗi đầu vào

và chuyển nó thành một bản tóm tắt

đại diện liên tục

nắm bắt được ý nghĩa thiết yếu

hoặc ngữ cảnh của từng mã thông báo trong chuỗi.

Thành phần giải mã lấy biểu diễn liên tục

từ thành phần mã hóa

và tạo ra một chuỗi đầu ra một mã thông báo tại một thời điểm.

Lưu ý rằng không giống như kiến trúc dựa trên RNN,

xử lý một chuỗi đầu vào một phần tử tại một thời điểm.

Máy biến áp chấp nhận toàn bộ chuỗi đầu vào cùng một lúc.

Họ đạt được điều này thông qua một cơ chế

được gọi là mã hóa vị trí,

tiêm thông tin đặt hàng

vào chuỗi đầu vào.

Cả hai thành phần mã hóa và giải mã

được cấu tạo từ nhiều lớp,

thường được gọi là khối hoặc ngăn xếp,

mỗi lớp chứa các lớp con.

Mỗi bộ mã hóa trong ngăn xếp

xử lý trình tự đầu vào

qua hai lớp cơ bản,

một lớp tự chú ý và một lớp tiếp liệu.

Lớp tự chú ý

cho phép mỗi mã thông báo hoặc từ trong chuỗi đầu vào

để xem xét các vị trí khác trong chuỗi

để xác định thông tin nào là phù hợp nhất.

Bằng cách xem xét tất cả các từ cùng một lúc,

mô hình xây dựng sự hiểu biết theo ngữ cảnh mạnh mẽ.

Lớp Feedforward là một mạng nơ-ron được kết nối đầy đủ

lấy đầu ra của lớp tự chú ý

và áp dụng các phép biến đổi bổ sung,

cho phép mô hình tìm hiểu các mẫu phức tạp hơn

và các mối quan hệ trong dữ liệu.

Bộ giải mã phản ánh cấu trúc của bộ mã hóa,

nhưng bao gồm lớp chú ý của bộ giải mã được mã hóa

bên cạnh sự chú ý đến bản thân

và các lớp con tiếp liệu.

Lớp tự chú ý

cho phép bộ giải mã tập trung vào các phần khác nhau

của đầu ra đã được tạo ra,

giúp nó xác định

mỗi vị trí liên quan như thế nào với những vị trí khác.

Lớp chú ý của bộ giải mã được mã hóa

căn chỉnh trình tự đầu vào

với trình tự đầu ra

hướng dẫn người giải mã hiểu

phần nào của đầu vào

có liên quan nhất ở mỗi bước của thế hệ.

Trong các nhiệm vụ như dịch ngôn ngữ,

lớp này giúp mô hình ánh xạ các từ

từ ngôn ngữ nguồn sang các từ tương ứng

trong ngôn ngữ đích.

Chúng ta đã thấy một ví dụ về điều này trong video trước.

Cuối cùng, lớp tiếp liệu

áp dụng các phép biến đổi bổ sung

để tinh chỉnh việc biểu diễn bộ giải mã

trước khi tạo đầu ra

bằng cách xử lý song song toàn bộ chuỗi,

nắm bắt các mối quan hệ phức tạp

thông qua việc sử dụng sự tự chú ý

và học các biểu diễn đầu vào liên tục,

máy biến áp đã cách mạng hóa việc xử lý dữ liệu tuần tự,

cho phép thực hiện hiện đại

trong xử lý ngôn ngữ tự nhiên và hơn thế nữa.