# 02 - Mạng lưới thần kinh đưa ra dự đoán như thế nào

---

- [Người hướng dẫn] Quy trình tổng hợp có trọng số

và kích hoạt tín hiệu

trên nhiều nút được kết nối với nhau

cho phép mạng lưới thần kinh nhân tạo

để tìm hiểu các mô hình phức tạp và đưa ra dự đoán

dựa trên dữ liệu đầu vào.

Để hiểu cách mạng lưới thần kinh đưa ra dự đoán,

hãy xem qua một ví dụ đơn giản

nơi mạng lưới thần kinh được sử dụng để dự đoán

liệu một khách hàng của ngân hàng có khả năng vỡ nợ hay không

dựa trên ba đặc điểm:

số tiền vay, số tiền khách hàng vay,

hạng cho vay, đánh giá chất lượng khoản vay

với các giá trị A, B hoặc C,

và mục đích vay, lý do vay

với những giá trị như mua một chiếc ô tô, sửa sang nhà cửa,

hoặc bắt đầu kinh doanh.

Ba đặc điểm này độc lập

hoặc các biến dự đoán,

trong khi biến phụ thuộc hoặc biến kết quả

là liệu khách hàng có vỡ nợ hay không

với giá trị có hoặc không.

Trong ví dụ này, chúng tôi sẽ sử dụng

một loại mạng lưới thần kinh nhân tạo rất đơn giản

được gọi là perceptron.

Perceptron là một dạng cơ bản của mạng nơ-ron

chỉ bao gồm hai lớp:

một lớp đầu vào và một lớp đầu ra.

Trong các mô hình phức tạp hơn,

có thêm các lớp ẩn giữa hai lớp này,

như chúng ta đã nói ở video trước.

Nhưng bây giờ chúng ta sẽ tập trung vào perceptron.

Mạng lưới thần kinh chỉ có thể xử lý dữ liệu bằng số.

Vì vậy, bất kỳ biến phân loại nào,

chẳng hạn như cấp độ khoản vay hoặc mục đích vay,

phải được chuyển đổi thành số.

Quá trình này được gọi là mã hóa.

Ví dụ: chúng ta có thể mã hóa các giá trị của mức cho vay

vì A bằng một, B bằng hai và C bằng ba.

Các giá trị của mục đích vay có thể được mã hóa

như ô tô bằng một, sửa nhà bằng hai,

và bắt đầu kinh doanh với tư cách là ba người.

Cuối cùng, giá trị của biến phụ thuộc

có thể được mã hóa thành một cho có và không cho không.

Sau khi mã hóa, dữ liệu đầu vào có thể trông như thế này.

Dữ liệu được mã hóa được đưa vào các nút đầu vào của mạng

với mỗi nút đại diện cho một tính năng trong dữ liệu đầu vào.

Mỗi tín hiệu đầu vào được nhân với trọng số,

cho biết tầm quan trọng của đầu vào đó

trong việc dự đoán khả năng vỡ nợ.

Mạng sau đó tính toán tổng trọng số của các đầu vào

như được hiển thị ở đây.

Để tăng tính linh hoạt của mô hình,

một số hạng sai lệch được thêm vào tổng có trọng số.

Độ lệch cho phép mô hình dịch chuyển đầu ra

bất kể giá trị đầu vào,

giúp mạng phù hợp hơn với dữ liệu.

Để đơn giản, hãy giả sử độ lệch trong trường hợp này

là âm 750.

Tổng mới trở thành 749,8

cộng trừ 750, bằng âm 0,2.

Tổng trọng số này sau đó được chuyển

thông qua chức năng kích hoạt.

Hàm kích hoạt xác định

liệu một tế bào thần kinh có nên kích hoạt hay không

và tạo ra đầu ra cuối cùng.

Đối với thiết bị nhận cảm này,

giả sử rằng chúng ta sử dụng

một hàm kích hoạt bước đơn vị cơ bản,

còn được gọi là hàm kích hoạt ngưỡng.

Đầu ra của hàm kích hoạt bước đơn vị bằng 0

nếu tổng tín hiệu đầu vào nhỏ hơn 0

hoặc một nếu tổng tín hiệu đầu vào bằng 0 hoặc nhiều hơn.

Trong ví dụ của chúng tôi, tổng của đầu vào có trọng số và độ lệch

là âm 0,2, nhỏ hơn 0.

Do đó, Perceptron xuất ra số 0,

dự đoán rằng khách hàng này sẽ không vỡ nợ.

Nói cách khác, perceptron dự đoán

rằng một khách hàng có khoản vay hạng A

người vay 15.000 USD để mua ô tô có thể sẽ không

vỡ nợ đối với khoản vay của họ.

Bây giờ hãy xem nhà mạng dự đoán điều gì

cho một khách hàng có đặc điểm khác nhau.

Giả sử khách hàng này được cấp khoản vay loại C trị giá 40.000 USD

để cải thiện nhà.

Tổng có trọng số, bao gồm cả độ lệch,

sẽ là 1.249,3.

Vì tổng lớn hơn 0 nên

chức năng kích hoạt bước đơn vị xuất ra một,

dự đoán rằng khách hàng này có khả năng

vỡ nợ trong khoản vay.

Ví dụ này cho thấy ngay cả một perceptron đơn giản

có thể đưa ra dự đoán dựa trên các tính năng đầu vào

bằng cách học các mẫu trong dữ liệu

thông qua tổng hợp có trọng số và kích hoạt.

Khi chúng ta tiến về phía trước,

chúng ta sẽ khám phá cách xây dựng mạng lưới thần kinh phức tạp hơn

dựa trên những nguyên tắc nền tảng này

để xử lý các tập dữ liệu phức tạp

và đưa ra những dự đoán chính xác hơn nữa.