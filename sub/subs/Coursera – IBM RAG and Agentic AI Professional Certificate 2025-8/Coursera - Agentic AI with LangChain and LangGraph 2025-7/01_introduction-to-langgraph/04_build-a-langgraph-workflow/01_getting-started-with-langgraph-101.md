# 01-bắt đầu với langgraph-101

---

Chào mừng bạn đến với video này về Bắt đầu với LangGraph 101.

Trong video này, bạn sẽ khám phá cách LangGraph sử dụng biểu đồ để thể hiện quy trình làm việc của tổng đài viên.

Bạn sẽ sử dụng các khả năng mạnh mẽ, chẳng hạn như vòng lặp và phân nhánh có điều kiện, những tính năng cần thiết

cho quy trình làm việc năng động. Bạn cũng sẽ xây dựng một ứng dụng LangGraph và trực quan hóa LangGraph

thực hiện quy trình làm việc và tiến triển trạng thái.

LangGraph là một khung mạnh mẽ dành cho các ứng dụng đa tác nhân có trạng thái. Bạn sẽ xây dựng một

bộ đếm để hiểu các thành phần chính, bắt đầu từ 1, tăng giá trị của nó, tạo ra

ký tự ngẫu nhiên và in kết quả cho đến 13.

Với LangGraph, bạn có thể xây dựng và quản lý các cấu trúc trạng thái phức tạp, đa chiều.

Ví dụ, một bộ đếm. Nó bao gồm một số nguyên và một chữ cái ngẫu nhiên. Trạng thái thường được xác định

với TypedDict, nhưng có thể là danh sách, cấu trúc lồng nhau hoặc chuỗi thông báo, giữ

tất cả các đầu vào, giá trị trung gian và đầu ra của đồ thị.

Trong LangGraph, bạn có thể xác định các biến trạng thái, chẳng hạn như 'n' và 'letter', bằng cách sử dụng lớp TypedDict.

Sử dụng mô-đun gõ để chỉ định loại biến.

Lớp này, một kiểu con TypedDict, hoạt động như một từ điển với thông tin được đánh máy. trong vòng

lớp này, định nghĩa 'n' là số nguyên và 'chữ cái' là một chuỗi. Tạo một đối tượng trạng thái chuỗi,

về cơ bản là một từ điển đánh máy. Điều này đại diện cho một hàng trong bảng của bạn và hỗ trợ

các loại phức tạp.

Các nút LangGraph liên kết đến các chức năng xử lý trạng thái. Hàm ví dụ này có một chuỗi

state, là một từ điển có các phím và chữ cái được gõ làm đầu vào. Bên trong, nó tạo ra

một chữ cái viết thường ngẫu nhiên. Câu lệnh return sử dụng dấu sao đôi để giải nén bản gốc

từ điển, tăng 'n' lên 1 và gán chữ cái mới cho trường chữ cái.

Kết quả là một đối tượng trạng thái chuỗi.

Không phải lúc nào bạn cũng cần giải nén toàn bộ đối tượng trạng thái nhưng sẽ trả về các khóa và giá trị

rất quan trọng.

LangGraph hỗ trợ nhiều loại biểu đồ khác nhau, mỗi loại có các quy tắc riêng biệt để cập nhật trạng thái, cho dù

nó yêu cầu trả về đầy đủ, tự động hợp nhất các bản cập nhật hoặc loại bỏ các trường bị thiếu. Luôn tư vấn

tài liệu cho loại biểu đồ cụ thể của bạn.

Hàm này lấy một đối tượng trạng thái chuỗi làm đầu vào và in các giá trị 'n' và 'letter'.

Nó trả về trạng thái không thay đổi, chỉ được sử dụng cho các tác dụng phụ hoặc in ấn, thay vì

sửa đổi dữ liệu. Thông thường, các nút được thiết kế để sửa đổi dữ liệu.

Bước đầu tiên là tạo một đối tượng biểu đồ trạng thái với lớp trạng thái chuỗi của bạn. LangGraph

quy trình làm việc bao gồm các nút chứa logic để xử lý trạng thái và các cạnh xác định

chuyển tiếp giữa các nút dựa trên các điều kiện.

Một trạng thái khác là trạng thái kết thúc, một đối tượng báo hiệu cho LangGraph rằng quy trình làm việc

đã hoàn tất.

Đầu tiên, kết hợp hàm thêm vào biểu đồ trạng thái bằng phương thức thêm nút. các

phương thức có hai đối số, tên của nút và hàm.

Tiếp theo, thêm nút in vào đầu vào và in biến trạng thái.

Tên nút có thể khác với tên hàm. Điều này là do tên nút là định danh và

có thể khác với tên hàm.

Tiếp theo, thêm một cạnh giữa các nút add và print_out bằng phương thức add_edge. đầu tiên

tham số chỉ định nút bắt đầu và tham số thứ hai xác định đích

nút. Sau khi thêm trạng thái tăng nút, trạng thái cập nhật sẽ tự động chuyển sang trạng thái in.

Các cạnh đặc biệt kiểm soát quá trình xử lý nút tiếp theo. Chúng được chỉ đạo bởi các chức năng đánh giá

tình trạng hiện tại. Ví dụ: kiểm tra xem 'n' có lớn hơn hoặc bằng 13 hay không và trả về

đúng hay sai.

Bạn có thể chèn một cạnh có điều kiện bằng phương thức add_conditional_edges.

Đối số đầu tiên là tên nút trước khi đánh giá điều kiện. Vào thời điểm đó,

trạng thái có giá trị như 'n' bằng 10 và chữ cái bằng 's'.

Đối số thứ hai là hàm xác định nút nào sẽ đi tới tiếp theo, trong trường hợp này là

dừng_điều kiện. Hàm này lấy trạng thái đầu vào từ nút có tên print

và trả về một boolean điều khiển luồng của biểu đồ.

Đối số tiếp theo là một từ điển trong đó các khóa là đầu ra stop_condition. Giá trị

là các nút đích. Nếu stop_condition trả về true, đồ thị sẽ chuyển tiếp

để kết thúc. Nếu sai thì tiếp tục cộng.

Sử dụng từ điển để ánh xạ các giá trị là hữu ích. Ví dụ: định tuyến đầu ra số nguyên của nút

1 đến nút_1, 2 đến nút_2 và 3 đến kết thúc.

Ngoài ra, hãy thiết kế nút có điều kiện để trả về trực tiếp tên nút tiếp theo dựa trên

trên tiểu bang. Đối với Should_continue, nếu 'n' lớn hơn 13 từ nút in, hãy trả về

kết thúc. Nếu không, hãy quay lại để thêm. Điều này có thể hoán đổi với ánh xạ từ điển.

Chỉ ra nút xử lý đầu tiên bằng phương thức set_entry_point.

Tên chỉ định nút bắt đầu của biểu đồ để xử lý trạng thái. Sự khởi đầu này được thể hiện một cách trực quan.

Sau khi kết nối tất cả các nút, hãy gọi biên dịch để xây dựng ứng dụng có thể chạy được. Sử dụng ứng dụng này bằng cách vượt qua

một trạng thái khởi đầu. Nó sẽ thực hiện quy trình công việc. Gọi đối tượng ứng dụng bằng cách gọi gọi bằng

một từ điển trạng thái ban đầu. Ví dụ: 'n' bằng 1 và một chuỗi trống cho chữ cái.

Khi luồng công việc chạy, trạng thái sẽ di chuyển qua biểu đồ và trạng thái cuối cùng được trả về

vào biến kết quả.

Trạng thái đầu tiên được chuyển tới nút thêm, tại đây nó được xử lý bằng cách tăng 'n' và tạo ra

một chữ cái ngẫu nhiên Trạng thái cập nhật sau đó chuyển đến nút in. Trong nút in,

các biến trạng thái được in ra.

Trạng thái chuyển sang hàm stop_condition, kiểm tra xem 'n' có lớn hơn hoặc không

bằng 13. Nếu sai, trạng thái sẽ chuyển sang nút thêm. Nút thêm cập nhật 'n' và tạo

một lá thư. Trạng thái được cập nhật sau đó chuyển đến nút in, tại đó các biến trạng thái

được in.

Sau khi lặp lại, 'n' được tăng lên, một chữ cái mới được tạo ra và kết quả được in ra.

Khi stop_condition đánh giá đúng, điều kiện kết thúc sẽ kích hoạt việc hoàn thành

quy trình làm việc.

Biến kết quả lưu trữ giá trị trạng thái cuối cùng sau khi hoàn thành quy trình làm việc.

Trong video này, bạn đã học được rằng

Trạng thái trong LangGraph là một bộ nhớ phức tạp, đang phát triển, chứa tất cả các đầu vào, giá trị trung gian,

và đầu ra.

Các nút là các chức năng xử lý trạng thái hiện tại. Một số nút sửa đổi trạng thái, trong khi

những người khác được sử dụng cho các tác dụng phụ.

Các cạnh xác định cách thức thực thi giữa các nút, chuyển trạng thái cập nhật từ một nút

bước tiếp theo.

Các cạnh có điều kiện cho phép quy trình làm việc đưa ra các quyết định linh hoạt, định tuyến trạng thái tới các trạng thái khác nhau

nút.

Chạy ứng dụng LangGraph bao gồm việc tạo một đối tượng biểu đồ trạng thái, kết hợp các nút,

kết nối chúng, đặt điểm vào và sau đó biên dịch biểu đồ thành một ứng dụng có thể chạy được.

Việc chạy quy trình làm việc LangGraph được thực hiện bằng cách gọi ứng dụng đã biên dịch với trạng thái ban đầu.

Trực quan hóa quy trình làm việc giúp hiểu được quy trình thực thi và trạng thái tiến triển như thế nào

thông qua các nút khác nhau.