# 02 - Lựa chọn mô hình học chuyển tiếp

---

- [Giảng viên] Vậy là chúng ta đã biết học chuyển tiếp là gì rồi.

Bây giờ hãy khám phá cách chọn mô hình tốt nhất

để chuyển giao học tập,

đặc biệt là khi xử lý các tập dữ liệu khan hiếm.

Chúng tôi xem xét ba ví dụ cụ thể,

bao gồm cả nhiệm vụ phát hiện bệnh viêm phổi cổ điển

sử dụng VGG-19.

Lựa chọn mô hình chuyển tiếp phù hợp

liên quan đến việc xem xét một số yếu tố.

Tiêu chí chính bao gồm sự tương đồng

của các nhiệm vụ nguồn và đích,

quy mô và chất lượng của mô hình được đào tạo trước,

và khả năng tương thích với các yêu cầu cụ thể của bạn.

Đầu tiên, hãy xem xét một kịch bản chăm sóc sức khỏe

phát hiện viêm phổi qua chụp X-quang ngực.

Đây là một ví dụ điển hình về việc học chuyển tiếp tỏa sáng

do sự khan hiếm của hình ảnh y tế có chú thích.

VGG-19 là mạng nơ-ron tích chập sâu

đã được đào tạo trước trên tập dữ liệu ImageNet,

chứa hàng triệu hình ảnh được dán nhãn

trên một ngàn danh mục.

Mặc dù các loại này rất đa dạng,

các tính năng cấp thấp mà VGG-19 học được,

chẳng hạn như các cạnh và kết cấu,

có thể chuyển sang nhiệm vụ chụp ảnh y tế.

Ở đây, những gì chúng ta làm là thêm một lớp dày đặc mới

trên đỉnh đế VGG-19

phân loại ảnh X-quang

thành các loại viêm phổi hoặc không viêm phổi.

Đóng băng các lớp cơ sở

đảm bảo rằng trọng lượng được đào tạo trước được giữ lại,

làm cho mô hình trở nên hiệu quả ngay cả với một tập dữ liệu nhỏ.

Lưu ý rằng trước tiên chúng ta tải xuống base_model,

và sau đó điều chúng ta sẽ làm là làm phẳng đầu ra

và thêm một lớp dày đặc đơn giản lên trên nó.

Cuối cùng, chúng tôi thực hiện lớp phân loại dày đặc cuối cùng của mình.

Chúng tôi tạo mô hình và đặt base_model là không thể đào tạo được.

Chúng tôi biên dịch với các tham số cổ điển

đối với những loại mô hình này,

và thế là xong.

Mô hình này sẽ học từ tập dữ liệu về bệnh viêm phổi

cách phân loại bệnh viêm phổi

ngay cả khi VGG-19 chưa bao giờ được chụp X-quang

trong toàn bộ cuộc đời của nó.

Bây giờ, hãy xem xét phân tích tình cảm

trên một tập dữ liệu hạn chế về đánh giá sản phẩm.

Đối với nhiệm vụ này, BERT là một mô hình mạnh mẽ.

BERT đã được đào tạo trước trên một kho văn bản lớn

và có hiệu quả cao

trong việc hiểu các sắc thái của ngôn ngữ.

Điều này làm cho nó trở nên lý tưởng cho các nhiệm vụ như phân tích tình cảm,

trong đó bối cảnh và sự tinh tế trong văn bản là rất quan trọng.

Bằng cách tận dụng sự hiểu biết ngôn ngữ được đào tạo trước của BERT,

chúng tôi có thể tinh chỉnh nó trên một tập dữ liệu nhỏ về đánh giá sản phẩm

để thực hiện phân tích tình cảm.

Cách tiếp cận này sẽ tối đa hóa tiện ích của dữ liệu hạn chế.

Để làm điều đó, chúng ta sẽ sử dụng BertTokenizer,

như chúng tôi đã làm trước đây, để mã hóa dữ liệu,

và bây giờ chúng ta sẽ sử dụng TFBert

để phân loại trình tự,

đó là một loại mô hình ô tô

thêm một lớp lên trên BERT để phân loại.

Sau đó, ví dụ: chúng tôi có thể mã hóa một bài đánh giá, bất kỳ bài đánh giá nào,

biên dịch một mô hình và chúng ta có thể điều chỉnh nó hoặc chỉ sử dụng nó,

và nó sẽ hoạt động.

Đây là vẻ đẹp của việc học chuyển giao.

Ví dụ thứ ba của chúng tôi liên quan đến

phát hiện bệnh cây trồng qua hình ảnh

sử dụng một tập dữ liệu khan hiếm về hình ảnh lá cây.

MobileNet, một mạng nơ ron tích chập nhẹ,

rất phù hợp cho nhiệm vụ này.

MobileNet, đã được đào tạo trước về ImageNet,

được tối ưu hóa cho các ứng dụng bệnh nhân di động và nhúng.

Kiến trúc của nó cân bằng giữa độ chính xác và hiệu quả,

làm cho nó trở nên lý tưởng cho các kịch bản

với nguồn lực tính toán và dữ liệu hạn chế.

Bằng cách thêm lớp phân loại mới vào MobileNet

và đóng băng các lớp nền như chúng ta đã làm trước đây,

chúng tôi sẽ điều chỉnh mô hình để xác định những bệnh thực vật đó

bằng cách sử dụng bộ hình ảnh được gắn nhãn có giới hạn đó.

Một lần nữa, chúng ta sẽ sử dụng MobileNet,

chúng ta sẽ sử dụng nó làm mô hình cơ sở,

sau đó chúng tôi lấy đầu ra của nó.

Chúng tôi sẽ thực hiện một cuộc tổng hợp

chỉ để lấy thêm thông tin từ các tính năng.

Chúng tôi tạo một lớp dày đặc, phần đầu cơ bản và sau đó là các dự đoán.

Trong trường hợp này, chúng ta có 10 khả năng gây bệnh cho cây trồng,

và thế là xong.

Chúng tôi tạo ra mô hình,

chúng tôi đặt base_model là không thể đào tạo được và thế là xong.

Chúng tôi có thể biên dịch và phù hợp.

Và điều này sẽ phát hiện bệnh thực vật.

Đây là cách mà, ví dụ,

một số ứng dụng hoạt động mà bạn phải chụp ảnh,

và họ sẽ cho bạn biết đó là cây gì

và bạn nên làm gì với nó.

Tóm lại, lựa chọn mô hình chuyển tiếp phù hợp

liên quan đến việc đánh giá sự giống nhau giữa các nhiệm vụ,

các khả năng của mô hình được đào tạo trước,

và các ràng buộc về tập dữ liệu cụ thể của bạn.

VGG cho hình ảnh y tế, BERT cho nhiệm vụ ngôn ngữ,

và MobileNet cho các ứng dụng thị giác tiết kiệm tài nguyên,

chứng minh cách học chuyển giao có thể được áp dụng một cách hiệu quả

trên các miền khác nhau.