# 03 - Hàm kích hoạt trong mạng nơ-ron

---

- [Người hướng dẫn] Ở video trước,

Tôi đã giới thiệu một thuật ngữ, chức năng kích hoạt.

Hãy nói thêm một chút về điều đó là gì.

Hàm kích hoạt là chìa khóa

thành phần của mạng nơ-ron.

Nó quyết định liệu một nơ-ron có nên được kích hoạt hay không

hoặc không dựa trên tổng trọng số của đầu vào.

Không có chức năng kích hoạt,

mạng lưới thần kinh về cơ bản sẽ chỉ thực hiện tuyến tính

biến đổi, hạn chế khả năng của họ

để mô hình hóa các mẫu phức tạp trong dữ liệu.

Mạng lưới thần kinh sử dụng nhiều loại chức năng kích hoạt khác nhau,

mỗi loại đều có những ưu điểm cụ thể và trường hợp sử dụng lý tưởng.

Việc lựa chọn chức năng kích hoạt thường phụ thuộc

về nhiệm vụ học tập cụ thể đang được giải quyết.

Chức năng kích hoạt ngưỡng hoặc bước uni

mà chúng ta đã thấy trước đó là một

trong số các hàm kích hoạt đơn giản nhất được sử dụng trong mạng lưới thần kinh,

đặc biệt là ở những mẫu đầu tiên như Perceptron.

Nó xuất ra một giá trị nhị phân bằng 0

hoặc một dựa trên việc đầu vào có vượt quá

một ngưỡng nhất định.

Ưu điểm của chức năng kích hoạt ngưỡng là

dễ hiểu và dễ sử dụng đối với các mô hình cơ bản,

và nó hoạt động tốt trong các tình huống có sự đồng ý nghiêm ngặt

hoặc không cần quyết định.

Tuy nhiên, những hạn chế là

rằng hàm số không khả vi tại X bằng 0,

làm cho nó không phù hợp với các mô hình học sâu, hiện đại

dựa vào tối ưu hóa dựa trên độ dốc.

Nó cũng thiếu tính linh hoạt

trong việc mô hình hóa các mẫu phi tuyến tính phức tạp.

Ví dụ, cố gắng xác định xem một điểm có nằm bên trong

hoặc bên ngoài một vòng tròn.

Hàm kích hoạt sigmoid ánh xạ các giá trị đầu vào vào một

nằm trong khoảng từ 0 đến 1,

làm cho nó đặc biệt hữu ích cho các mô hình

nơi đầu ra cần thể hiện xác suất.

Vì lý do này, nó thường được sử dụng trong lớp đầu ra

cho các nhiệm vụ phân loại nhị phân.

Những lợi thế bao gồm thực tế là sự trơn tru

và đầu ra liên tục nằm trong khoảng từ 0

và một điều khiến nó rất hữu ích

cho các dự đoán dựa trên xác suất.

Nó cũng phù hợp

cho các kỹ thuật tối ưu hóa cơ sở gradient.

Một hạn chế là đối với rất lớn

hoặc đầu vào rất nhỏ, gradient trở nên gần bằng 0,

điều có thể làm chậm lại

hoặc dừng việc học trong các mạng có nhiều lớp ẩn.

Một hạn chế khác là

rằng hàm sigmoid xuất ra các giá trị giữa 0

và một, có nghĩa là độ dốc đều có thể

tích cực hoặc hoàn toàn tiêu cực.

Làm chậm sự hội tụ,

đó là điểm trong quá trình tối ưu hóa

nơi mạng lưới thần kinh có trọng lượng

và các thành kiến được ổn định.

Tang hyperbol hay hàm kích hoạt Tánh

là một phiên bản thu nhỏ

của hàm sigmoid ánh xạ các giá trị đầu vào vào phạm vi

giữa âm một và một.

Bởi vì nó là không trung tâm,

nó thường cung cấp hiệu suất tốt hơn trong các lớp ẩn so với

hàm sigmoid.

Việc có đầu ra không tập trung cho phép mô hình

để học hiệu quả hơn bằng cách đảm bảo

kết quả đầu ra đều tích cực

và tiêu cực, giúp cải thiện cân nặng

điều chỉnh trong quá trình đào tạo.

Một lợi thế khác là

hàm kích hoạt Tánh có độ dốc lớn hơn

so với hàm sigmoid,

điều này thường dẫn đến việc học nhanh hơn.

Tuy nhiên, giống như hàm kích hoạt sigmoid,

hàm Tanh cũng có thể bị biến mất

vấn đề về độ dốc, đặc biệt là trong các mạng

với nhiều lớp ẩn.

Hàm kích hoạt đơn vị tuyến tính được chỉnh lưu, còn được gọi là

như ReLU, là hàm kích hoạt được sử dụng phổ biến nhất trong

học sâu, đặc biệt là ở các lớp ẩn.

Nó biến đổi tổng đầu vào

bằng cách đặt tất cả các giá trị âm về 0

và giữ nguyên các giá trị dương.

Ưu điểm chính của ReLU là

rằng nó có hiệu quả về mặt tính toán,

vì nó chỉ liên quan đến ngưỡng đơn giản.

Một ưu điểm khác là đối với đầu vào tích cực,

độ dốc vẫn lớn, cho phép nhanh hơn

và học tập hiệu quả hơn ở các lớp sâu hơn.

Tuy nhiên, với ReLU,

nếu tế bào thần kinh nhận được đầu vào tiêu cực một cách nhất quán,

chúng có thể trở nên không hoạt động và chết,

nghĩa là họ không còn đóng góp cho việc học

bởi vì sản lượng của họ luôn bằng không.

Leaky ReLU là một biến thể của ReLU được thiết kế

để giải quyết vấn đề ReLU đang chết dần.

Thay vì xuất ra số 0 cho đầu vào âm,

ReLU bị rò rỉ cho phép độ dốc âm nhỏ

cho các đầu vào tiêu cực, giữ cho tế bào thần kinh hoạt động một cách hiệu quả.

Một chức năng kích hoạt thường được sử dụng khác

là kích hoạt Softmax.

Nó biến đổi đầu ra thô

hoặc đăng nhập vào phân phối xác suất trong đó tổng

của tất cả các xác suất đầu ra bằng một.

Chức năng kích hoạt Softmax thường được sử dụng

trong lớp đầu ra cho các vấn đề phân loại nhiều lớp.

Trong những loại vấn đề này,

mỗi nơ-ron đầu ra tạo ra một logit hoặc điểm thô.

Chức năng kích hoạt Softmax chuyển đổi điểm số

đến xác suất dự đoán,

và lớp có xác suất cao nhất được chọn

như một dự đoán của mạng.

Ưu điểm chính của chức năng kích hoạt Softmax là

rằng nó cung cấp một phân bố xác suất rõ ràng

cho mỗi lớp, giúp dễ dàng

để giải thích các dự đoán

trong các nhiệm vụ phân loại nhiều lớp.

Một ưu điểm nữa là nó hoạt động tốt

với các kỹ thuật tối ưu hóa dựa trên độ dốc

giống như sự lan truyền ngược.

Hạn chế chính

của hàm kích hoạt Softmax là

rằng trong các mô hình quy mô lớn với nhiều lớp,

chức năng này có thể tốn kém về mặt tính toán do

đến nhu cầu tính toán số mũ cho mỗi lớp.