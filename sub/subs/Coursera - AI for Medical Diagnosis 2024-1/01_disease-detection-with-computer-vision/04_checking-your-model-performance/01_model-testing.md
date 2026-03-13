# 01 mẫu thử nghiệm

---

Bây giờ bạn đã thấy bạn sẽ làm thế nào

đi đào tạo người mẫu cho y tế

chẩn đoán, hãy nói về cách

bạn sẽ tiến hành thử nghiệm một mô hình như vậy.

Bạn sẽ tìm hiểu về việc sử dụng hợp lý

tập huấn luyện, xác nhận và kiểm tra.

Và về sự cần thiết của nền tảng vững chắc

sự thật để đánh giá mô hình của bạn.

Khi chúng tôi áp dụng máy

học tập dữ liệu, chúng ta thường

chia nó thành một khóa đào tạo và

một bộ thử nghiệm.

Tập huấn luyện của chúng tôi được sử dụng cho

phát triển và lựa chọn các mô hình và thử nghiệm của chúng tôi

thiết lập cho

báo cáo cuối cùng về kết quả của chúng tôi.

Trong thực tế, tập dữ liệu huấn luyện là

tiếp tục chia thành đào tạo

bộ và bộ xác nhận, trong đó quá trình đào tạo

tập hợp được sử dụng để tìm hiểu một mô hình và

bộ xác nhận được sử dụng cho

điều chỉnh siêu tham số và

đưa ra ước lượng của mô hình

hiệu suất trên tập thử nghiệm.

Đôi khi việc chia thành một khóa đào tạo và

bộ xác nhận được thực hiện nhiều lần

trong một phương pháp gọi là xác nhận chéo

để giảm bớt sự biến đổi trong

ước tính hiệu quả của mô hình.

Những bộ này cũng có tên khác nhau

đôi khi như xác nhận có thể được gọi

tập điều chỉnh hoặc độ sâu, tập huấn luyện

có thể được gọi là tập phát triển, và

bộ kiểm tra có thể được thực hiện bằng cách nắm giữ hoặc

thậm chí còn khó hiểu hơn bộ xác nhận.

Chúng tôi sẽ tuân thủ các điều khoản đào tạo,

xác nhận và bộ thử nghiệm cho mục đích của chúng tôi.

Chúng tôi sẽ giải quyết ba thách thức khi xây dựng

những bộ này trong bối cảnh y học.

Thử thách đầu tiên liên quan đến việc làm thế nào

chúng tôi làm cho các bộ thử nghiệm này trở nên độc lập,

thứ hai liên quan đến cách chúng tôi lấy mẫu chúng,

và

thứ ba liên quan đến cách

chúng tôi thiết lập sự thật nền tảng.

Hãy giải quyết vấn đề

của bệnh nhân chồng chéo đầu tiên.

Giả sử một bệnh nhân đến khám hai lần trong một

chụp x-quang, một lần vào tháng 6 và một lần vào tháng 11.

Cả hai lần, họ đều đeo một chiếc vòng cổ

khi họ chụp X-quang.

Một trong những bức ảnh chụp X-quang của họ được lấy mẫu

như một phần của tập huấn luyện và phần còn lại

như một phần của bài kiểm tra.

Chúng tôi đào tạo mô hình học sâu của mình và

thấy rằng nó dự đoán chính xác bình thường cho

tia X trong bộ thử nghiệm.

Vấn đề là nó có thể

mà người mẫu thực sự đã ghi nhớ

để xuất ra bình thường khi nó nhìn thấy

bệnh nhân đeo vòng cổ.

Đây không phải là giả thuyết,

mô hình học sâu

có thể vô tình ghi nhớ đào tạo

dữ liệu và mô hình có thể ghi nhớ những dữ liệu hiếm hoặc

khía cạnh dữ liệu đào tạo độc đáo của

bệnh nhân, chẳng hạn như chiếc vòng cổ,

điều có thể giúp nó có được câu trả lời đúng

khi thử nghiệm trên cùng một bệnh nhân.

Điều này sẽ dẫn đến tình trạng quá

hiệu suất tập kiểm tra lạc quan,

nơi chúng tôi nghĩ rằng mô hình của chúng tôi

là tốt hơn thực tế nó là.