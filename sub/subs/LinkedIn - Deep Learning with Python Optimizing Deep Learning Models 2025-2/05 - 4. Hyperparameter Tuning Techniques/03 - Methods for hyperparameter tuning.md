# 03 - Phương pháp điều chỉnh siêu tham số

---

- [Người hướng dẫn] Điều chỉnh siêu tham số là một bước quan trọng

trong đào tạo mô hình deep learning

vì nó liên quan đến việc tìm kiếm các cài đặt tối ưu

cho các siêu tham số kiểm soát quá trình đào tạo

và kiến trúc mô hình.

Không giống như các tham số mô hình,

được học tự động trong quá trình đào tạo,

siêu tham số phải được đặt trước khi bắt đầu đào tạo

và ảnh hưởng trực tiếp đến hiệu suất của mô hình,

khả năng hội tụ và khái quát hóa.

Quá trình điều chỉnh siêu tham số có thể gặp nhiều thách thức

vì không gian tìm kiếm siêu tham số thường rất rộng lớn,

và sự tương tác của chúng có thể phức tạp.

Tuy nhiên, một số phương pháp hiệu quả thường được sử dụng

để xác định các cấu hình siêu tham số tốt nhất

cho một vấn đề nhất định.

Một trong những cách đơn giản nhất

và phương pháp được sử dụng rộng rãi nhất là tìm kiếm lưới.

Trong tìm kiếm dạng lưới, một tập hợp giá trị được xác định trước được chỉ định

cho mỗi siêu tham số,

và giá trị thuật toán là hiệu suất của mô hình

cho tất cả các kết hợp có thể có của các giá trị này.

Việc tìm kiếm toàn diện này đảm bảo

cấu hình tối ưu đó

trong phạm vi quy định được xác định.

Ví dụ, chúng ta có thể chỉ định

năm tỷ lệ học tập được kiểm tra,

có giá trị từ 0,00001 đến 0,1,

cũng như năm lô có giá trị từ 32 đến 512.

Tìm kiếm lưới sẽ xây dựng một mô hình

cho tất cả 25 kết hợp kết quả để tìm ra kết quả tối ưu

hoặc kết hợp siêu tham số hoạt động tốt nhất.

Tìm kiếm dạng lưới cung cấp một cách tiếp cận toàn diện

bằng cách đánh giá toàn diện mọi sự kết hợp có thể

của các giá trị siêu tham số được chỉ định.

Điều này có nghĩa là chúng ta không bao giờ bỏ lỡ bất kỳ điểm nào trong không gian xác định,

cung cấp cho chúng tôi thông tin đầy đủ về tất cả các cấu hình ứng cử viên.

Ngoài ra, nó rất dễ sử dụng

và được hỗ trợ rộng rãi,

làm cho nó trở thành một phương pháp khởi đầu phổ biến.

Ý tưởng cơ bản rất đơn giản để hiểu,

và việc triển khai thường không gặp rắc rối

nhờ sự hỗ trợ của thư viện tiêu chuẩn.

Về nhược điểm,

sự kỹ lưỡng này có thể nhanh chóng trở thành gánh nặng

khi chúng tôi tăng số lượng siêu tham số

hoặc mở rộng phạm vi giá trị có thể của chúng,

lưới kết quả tăng theo cấp số nhân,

làm cho cách tiếp cận này trở nên cực kỳ tốn kém

về mặt thời gian và tính toán.

Hơn nữa, tìm kiếm dạng lưới thiếu tính linh hoạt.

Chúng ta phải cam kết đánh giá tất cả các kết hợp,

làm cho khó tập trung

trên các vùng hứa hẹn nhất của không gian siêu tham số

và tối ưu hóa việc phân bổ nguồn lực.

Tìm kiếm ngẫu nhiên có một cách tiếp cận khác.

Thay vì thử nghiệm mọi sự kết hợp,

nó lấy mẫu ngẫu nhiên các điểm từ một phạm vi xác định

cho mỗi siêu tham số.

Ví dụ, thay vì kiểm tra

mọi tốc độ học tập được xác định trước và kích thước lô,

tìm kiếm ngẫu nhiên có thể lấy mẫu ngẫu nhiên các giá trị

từ một phạm vi liên tục giữa 0,0001

và 0,1 cho tốc độ học tập,

và từ 32 đến 5 12 cho cỡ lô.

Theo thời gian, nó khám phá một phần không gian siêu tham số

với ít giả định hơn

về những giá trị tốt nhất của họ có thể nằm ở đâu.

Tìm kiếm ngẫu nhiên có cách tiếp cận linh hoạt hơn

hơn tìm kiếm dạng lưới,

thường cho phép chúng ta khám phá các giải pháp tốt nhanh hơn.

Bởi vì nó không cam kết

để kiểm tra một cách có hệ thống mọi sự kết hợp có thể,

tìm kiếm ngẫu nhiên có thể tập trung vào các cấu hình đầy hứa hẹn

mà không lãng phí công sức vào các thông số ít ảnh hưởng hơn.

Cách tiếp cận này cũng có quy mô trơn tru.

Nếu chúng ta có đủ nguồn lực,

chúng ta có thể đơn giản chạy nhiều thử nghiệm ngẫu nhiên hơn

để tăng cơ hội tìm thấy cài đặt tối ưu.

Tuy nhiên, sự linh hoạt này đi kèm với một sự đánh đổi lớn.

Nếu không có sự đảm bảo có hệ thống về phạm vi bảo hiểm,

tìm kiếm ngẫu nhiên có thể bỏ qua

các phần của không gian siêu tham số

chứa các giải pháp hiệu suất cao.

Mặc dù tìm kiếm dạng lưới và ngẫu nhiên có vai trò của chúng,

các phương pháp tiên tiến hơn đã xuất hiện

để điều hướng không gian siêu tham số một cách thông minh.

Ví dụ, tối ưu hóa Bayes

cung cấp một khung xác suất để điều chỉnh siêu tham số.

Không giống như tìm kiếm theo lưới hoặc ngẫu nhiên,

Tối ưu hóa Bayes xây dựng mô hình thay thế

của hàm mục tiêu cố gắng dự đoán

siêu tham số khác nhau như thế nào

có thể ảnh hưởng đến hiệu suất của mô hình.

Sau mỗi lần thử,

mô hình thay thế này được sử dụng để xác định

tập hợp siêu tham số tiếp theo để đánh giá,

cân bằng việc thăm dò các khu vực mới

trong không gian tìm kiếm

với việc khai thác các vùng

đã cho thấy kết quả đầy hứa hẹn.

Theo thời gian, tối ưu hóa Bayes hội tụ

đến các giá trị siêu tham số tối ưu.

Bạn có thể coi nó giống như một cuộc săn tìm kho báu

với một trợ lý thông minh

ai, sau mỗi bài kiểm tra,

đoán tốt hơn kho báu có thể nằm ở đâu.

Tối ưu hóa Bayes cung cấp một cách thông minh hơn

để điều hướng không gian siêu tham số.

Thay vì thăm dò các giá trị một cách ngẫu nhiên,

nó học hỏi từ những đánh giá trước đó

và sử dụng kiến thức đó để hướng dẫn chúng ta hướng tới những giải pháp tốt hơn

với ít đánh giá hơn so với tìm kiếm theo lưới hoặc ngẫu nhiên.

Tuy nhiên, thông tin bổ sung này xuất hiện

với độ phức tạp ngày càng tăng.

Tối ưu hóa Bayes yêu cầu xây dựng

và duy trì một mô hình phức tạp để cung cấp thông tin cho việc tìm kiếm,

có thể vừa tốn nhiều công sức tính toán

và thách thức để thực hiện.

Trong thực tế, việc lựa chọn phương pháp điều chỉnh siêu tham số

phụ thuộc vào độ phức tạp của mô hình,

kích thước của không gian tìm kiếm,

và các tài nguyên tính toán sẵn có.

Tìm kiếm dạng lưới và viết trên tìm kiếm đều phù hợp

cho không gian tìm kiếm nhỏ hoặc khi việc chia tỷ lệ là quan trọng.

Trong khi tối ưu hóa Bayes phù hợp hơn

cho các nhiệm vụ phức tạp và tốn nhiều tài nguyên hơn.

Kết hợp các phương pháp này

với kiến thức và công cụ miền

có thể hợp lý hóa quá trình đào tạo,

đảm bảo rằng một mô hình đạt được hiệu suất tốt nhất có thể

với chi phí tính toán tối thiểu.