# 01 - Mạng nơ ron nhân tạo là gì

---

- [Người hướng dẫn] Hãy bắt đầu thảo luận về deep learning

bằng cách nói về mạng nơ-ron nhân tạo là gì

ở mức độ cao.

Mạng nơ-ron nhân tạo là một mô hình tính toán

lấy cảm hứng lỏng lẻo từ cấu trúc và chức năng

của các tế bào thần kinh sinh học trong não.

Mạng lưới phức tạp của các tế bào thần kinh được kết nối với nhau

trong bộ não con người tạo thành nền tảng

để xử lý thông tin phức tạp,

chức năng giao tiếp và nhận thức

làm nền tảng cho trí tuệ và hành vi của con người.

Một nơ-ron sinh học nhận các tín hiệu đến dưới dạng

xung điện hóa từ các tế bào thần kinh khác

thông qua các cấu trúc gọi là đuôi gai.

Các sợi nhánh đóng vai trò là kênh đầu vào của tế bào thần kinh

nơi các tín hiệu này được tích hợp và xử lý.

Nếu đầu vào tích lũy vượt quá một ngưỡng nhất định,

các tế bào thần kinh phát ra một xung điện,

còn được gọi là tiềm năng hành động.

Xung điện này truyền xuống sợi trục,

đó là kênh đầu ra của nơ-ron.

Sợi trục truyền tín hiệu đến các tế bào thần kinh khác

thông qua khớp thần kinh ở cuối

của sợi trục được gọi là đầu sợi trục,

nơi tín hiệu có thể lan truyền xa hơn

thông qua mạng lưới thần kinh.

Trong mạng nơ-ron nhân tạo, các nơ-ron

hoặc các nút là các đơn vị tính toán đơn giản hóa

sử dụng các hàm toán học

và các giá trị số để mô phỏng luồng thông tin.

Các nút này thường được tổ chức thành các lớp

xử lý dữ liệu theo cách có cấu trúc.

Lớp đầu vào bao gồm các nút đầu vào

nhận dữ liệu thô.

Mỗi nút đầu vào đại diện cho một tính năng của dữ liệu.

Ví dụ: trong nhiệm vụ phân loại hình ảnh,

mỗi pixel của hình ảnh có thể được chuyển đến nút đầu vào.

Lớp đầu ra chứa các nơ-ron

tạo ra dự đoán cuối cùng của mạng, ví dụ:

trong vấn đề phân loại hình ảnh,

giá trị của các nơ-ron đầu ra có thể tương ứng

vào nhãn của một hình ảnh, chẳng hạn như hình ảnh đó có phải là

của một con mèo hoặc một con chó.

Giữa các lớp đầu vào và đầu ra là một

hoặc nhiều lớp ẩn.

Các lớp ẩn là trái tim tính toán

của một mạng lưới thần kinh đã kích hoạt một mạng lưới thần kinh

để tìm hiểu cách biểu diễn phân cấp của dữ liệu đầu vào.

Lớp ẩn đầu tiên có thể phát hiện các mẫu đơn giản

trong dữ liệu, chẳng hạn như các cạnh trong một hình ảnh,

hoặc các cấu trúc ngữ pháp cơ bản trong văn bản.

Các lớp ẩn tiếp theo được xây dựng dựa trên những phát hiện trước đó

để nhận biết những đặc điểm phức tạp hơn.

Ví dụ: kết hợp các cạnh để phát hiện hình dạng

hoặc kết hợp các từ để hiểu cụm từ.

Mỗi lớp ẩn nắm bắt mức độ trừu tượng cao hơn,

chuyển từ các biểu diễn đơn giản sang phức tạp hơn.

Mỗi nút trong mạng lưới thần kinh nhân tạo của chúng tôi nhận được đầu vào

dưới dạng các giá trị số,

trực tiếp từ dữ liệu thô, đó là trường hợp

cho các nút trong lớp đầu vào

hoặc từ các nút ở lớp trước,

như trường hợp của các nút ở lớp ẩn và lớp đầu ra.

Khi một nút nhận đầu vào, mỗi đầu vào sẽ được nhân lên

bằng giá trị trọng số tương ứng.

Trọng lượng thể hiện tầm quan trọng đã học của

đầu vào đó trong việc xác định đầu ra của nơ-ron.

Trong quá trình đào tạo, mạng sẽ điều chỉnh các trọng số này

để cải thiện hiệu suất của nó, học cách ưu tiên đầu vào

phù hợp hơn với nhiệm vụ hiện tại.

Nút sau đó tính toán tổng trọng số của các đầu vào của nó,

thường thêm vào những gì được gọi là thuật ngữ sai lệch,

để dịch chuyển tổng các giá trị có trọng số lên hoặc xuống.

Tổng trọng số sau đó được chuyển

thông qua chức năng kích hoạt, xác định giá trị nào

để xuất hoặc chuyển tới các nút ở các lớp tiếp theo.

Hàm kích hoạt giới thiệu tính phi tuyến tính

vào mạng, cho phép nó mô hình hóa các mẫu phức tạp

trong dữ liệu.

Chúng tôi thảo luận chi tiết hơn về các chức năng kích hoạt

khi chúng ta xem video khóa học có tiêu đề

Chức năng kích hoạt trong mạng thần kinh.

Bằng cách bắt chước quá trình xử lý theo thứ bậc

thông tin trong não người,

mạng lưới thần kinh nhân tạo có thể học hỏi từ số lượng lớn

dữ liệu để thực hiện các nhiệm vụ như nhận dạng hình ảnh,

xử lý tiếng nói, hiểu ngôn ngữ tự nhiên,

và phân tích dự đoán với độ chính xác vượt trội.