# 02 xây dựng-a-knn-phân loại-mô hình và đánh giá-nó

---

Trong video này chúng tôi sẽ

xây dựng mô hình ML đầu tiên của chúng tôi.

Hãy bắt đầu bằng việc giải quyết

báo cáo vấn đề phân loại cho

Giải pháp đồng bộ,

đó là xác định sản phẩm nào

sẽ bán được hơn nghìn chiếc.

Hãy bắt đầu bằng cách nhập

các thư viện cần thiết.

Thay đổi thư mục làm việc thành

nơi bạn đã lưu trữ tập dữ liệu.

Bây giờ, hãy đọc dữ liệu được xử lý trước và

có một cái nhìn nhanh chóng về nó

Bây giờ nếu chúng ta quan sát các cột ở trên,

chúng ta có thể thấy rằng dữ liệu cho

số lượng đơn vị đã bán cần thiết cho chúng tôi

mô hình phân loại đã có sẵn trong

đơn vị bán được nhiều hơn

hơn nghìn cột.

Chúng ta có thể xóa cột đơn vị đã bán

vì đây là vấn đề phân loại,

giữ biến mục tiêu hồi quy

sẽ cho chúng ta một kết quả không thực tế.

Vì mô hình sẽ đơn giản

nhìn vào cột đơn vị bán và

kiểm tra xem nó có lớn hơn không

hơn nghìn hay không.

Chúng ta có thể thấy rằng cột

không còn ở đó nữa.

Bây giờ chúng ta hãy thực hiện một số tính năng cơ bản

kỹ thuật để đạt được kết quả tốt hơn.

Như chúng tôi đã quan sát từ các biểu đồ trước đó trong

khóa học này, các cột xếp hạng trong dữ liệu này

bộ được tích lũy, trong khi phần còn lại của

các giá trị chỉ dành cho một tuần cụ thể.

Sự bất thường này sẽ tiêu cực

ảnh hưởng đến mô hình ML của chúng tôi.

Để mang lại nhiều giá trị hơn

của các cột xếp hạng,

chúng ta có thể có được tỷ lệ giữa tốt và

xếp hạng xấu.

Một tỷ lệ sẽ không được tích lũy và sẽ

hiển thị tỷ lệ đánh giá tốt trên

xếp hạng xấu chỉ trong một tuần cụ thể.

Hãy thêm xếp hạng bốn sao và

cột đánh giá năm sao để lấy tổng

xếp hạng tốt và xếp hạng một sao và

xếp hạng hai sao để có được

tổng số xếp hạng xấu.

Chúng ta có thể coi ba sao

đánh giá là trung lập và

không dùng nó để tính toán

đánh giá tốt bằng xấu.

Đối với điều này, chúng tôi sẽ tạo một cho

vòng lặp tính toán tỷ lệ tốt và

xếp hạng xấu.

Mã này hơi phức tạp và

chăm sóc các tình huống khác nhau

chẳng hạn như lỗi chia số không.

Lời giải thích chi tiết

vào mã được đưa ra dưới đây.

Bạn có thể tạm dừng video một lát và

nhìn vào lời giải thích của mã.

Bây giờ chúng ta có danh sách

tỷ lệ đánh giá đã sẵn sàng với chúng tôi.

Hãy thêm phần này vào khung dữ liệu của chúng tôi bên dưới

tên cột xếp hạng tốt theo đánh giá xấu.

Bây giờ chúng ta có tỷ lệ xếp hạng,

chúng ta hãy bỏ tất cả các cột liên quan đến

xếp hạng và sau đó kiểm tra lại dữ liệu.

Như chúng ta có thể thấy,

tất cả các cột xếp hạng đã bị loại bỏ.

Bây giờ, có một điều bạn phải luôn nhớ

có phải thư viện scikit-learn chỉ hoạt động

khi tất cả các biến trong của bạn

khung dữ liệu là số.

Trong trường hợp của chúng tôi, chúng tôi có cột phân khúc.

Hãy lấy các danh mục trong cột này.

Bây giờ chúng ta cần chuyển đổi các phân đoạn này trong

cột phân loại này thành số,

và quá trình này được gọi là mã hóa.

Về cơ bản, có hai

cách mã hóa một cột và

chúng là mã hóa một lần và

mã hóa nhãn.

Mã hóa một lần nóng tạo ra

cột nhị phân cho

mỗi danh mục chỉ có một trạng thái hoạt động.

Ví dụ: cột phân khúc của chúng tôi sẽ

đầu tiên được chia thành ba cột,

dưỡng da, trang điểm và chăm sóc tóc.

Khi cột chăm sóc da có một trong đó,

nó có nghĩa là sản phẩm thuộc về

vào danh mục chăm sóc da và

tự động hai cột còn lại,

chăm sóc tóc và trang điểm sẽ bằng không.

Mã hóa một lần nóng cho biết

rằng không có trật tự hoặc

xếp hạng giữa các hạng mục

trong biến đó.

Mặt khác, mã hóa nhãn gán

một giá trị số cho mỗi danh mục duy nhất.

Nếu các phân đoạn được đặt theo thứ tự,

ví dụ,

chăm sóc da là phân khúc cao cấp nhất,

tiếp theo là chăm sóc tóc và sau đó là trang điểm.

Sau khi quá trình mã hóa nhãn hoàn tất,

nó sẽ chuyển đổi các giá trị này thành một,

hai và ba, ngụ ý chăm sóc da

vượt trội hơn việc chăm sóc tóc,

do đó vượt trội hơn so với trang điểm.

Mã hóa nhãn ngụ ý

rằng có một đơn đặt hàng hoặc

thứ hạng có thể được trao cho các danh mục.

Vì các danh mục trong các phân đoạn

trong dữ liệu của sức mạnh tổng hợp không có bất kỳ

thứ hạng hoặc thứ tự giữa họ,

chúng tôi sẽ thực hiện mã hóa một lần.

Chúng ta có thể sử dụng .get_dummies từ

Thư viện Pandas để biểu diễn

một mã hóa nóng.

Vì vậy, hãy làm điều đó.

Chúng ta có thể thấy rằng get_dummies đã tạo

hai cột có giá trị Boolean.

Ở đây true bằng một,

gợi ý rằng sản phẩm thuộc về

vào danh mục cụ thể đó.

Cũng quan sát rằng cột phân đoạn

đã biến mất và chỉ còn hai cột

thay vì ba ở đó, đó là

phân khúc trang điểm và phân khúc chăm sóc da.

Đó là vì chúng ta đã vượt qua

đối số giảm đầu tiên bằng đúng.

Đây là một trong những tính năng

để có được hình nộm.

Đây là một lập luận đáng khuyến khích vì nếu

chúng ta biết giá trị của n trừ 1 cột,

sau đó các cột bị thiếu

giá trị có thể được giả định.

Ví dụ, trong quan sát thứ năm

ở trên, cả phân khúc trang điểm và

phân khúc chăm sóc da là sai.

Điều này có nghĩa là sản phẩm thuộc về

loại thứ ba, chăm sóc tóc.

Loại bỏ thông tin dư thừa này

giúp chúng tôi tạo ra các mô hình ổn định hơn.

Vì vậy bây giờ chúng ta hãy thực hiện việc phân chia thử nghiệm tàu.

Nhưng trước khi làm điều đó, hãy tách ra

biến độc lập và biến mục tiêu cho

mô hình.

Đây là một thực hành tốt để đảm bảo

rằng biến mục tiêu không

trộn lẫn với các tính năng.

Ở đây, biến mục tiêu của chúng tôi hoặc

biến chúng tôi muốn dự đoán là

đơn vị bán được lớn hơn nghìn.

Hãy nhanh chóng kiểm tra hình dạng.

Bây giờ, hãy nhập phần tách thử nghiệm tàu và

kiểm tra hình dạng của cả đoàn tàu và

các giá trị thử nghiệm.

Trong đoạn mã trên, chúng tôi đã thực hiện 70

chia thành 30, trong đó 70% dữ liệu

thuộc về dữ liệu tàu và phần còn lại

của dữ liệu thuộc về dữ liệu thử nghiệm.

Và như đã giải thích trong mô-đun trước,

đảm bảo trạng thái ngẫu nhiên

độ tái lập của cùng một sự kết hợp

của bộ mẫu thử nghiệm tàu hỏa.

Khi đã làm xong việc đó,

bây giờ hãy đảm bảo dữ liệu của chúng tôi được thu nhỏ lại.

Việc chia tỷ lệ sẽ đảm bảo rằng biến

với cường độ cao hơn không ảnh hưởng

khoảng cách trong thuật toán KNN của chúng tôi.

Chúng ta hãy bắt đầu với việc nhập khẩu

lớp vô hướng tiêu chuẩn từ

mô-đun tiền xử lý

của thư viện scikit-learn.

Đại lượng vô hướng chuẩn là một công cụ

sẽ được sử dụng để chuẩn hóa dữ liệu,

đó là,

để điều chỉnh các tính năng của dữ liệu

rằng chúng có giá trị trung bình bằng 0 và

độ lệch chuẩn bằng một.

Bây giờ hãy tạo một đối tượng gọi là vô hướng

một tức thời của lớp vô hướng tiêu chuẩn.

Trong bước tiếp theo chúng tôi thực hiện

dữ liệu huấn luyện, x huấn luyện và

áp dụng hai bước cho nó, phù hợp và biến đổi.

Phương pháp phù hợp trong vô hướng,

tính giá trị trung bình và

độ lệch chuẩn cho

từng thuộc tính trong tập dữ liệu huấn luyện.

Và biến đổi sử dụng các giá trị này

để mở rộng quy mô dữ liệu huấn luyện.

Trừ giá trị trung bình và chia cho

độ lệch chuẩn cho từng đặc tính.

Kết quả là có phiên bản mới

của dữ liệu huấn luyện,

trong đó mỗi tính năng hiện có một ý nghĩa

bằng 0 và độ lệch chuẩn bằng 1.

Dữ liệu thang đo này được lưu trữ

trong x_train_scaled.

Hãy để chúng tôi xem dữ liệu quy mô một lần.

Và bây giờ chúng ta hãy biến đổi

dữ liệu thử nghiệm bằng cách sử dụng .transform.

Điều này lấy dữ liệu thử nghiệm, x test,

và chia tỷ lệ bằng cách sử dụng giá trị trung bình và

giá trị độ lệch chuẩn

tính toán từ dữ liệu huấn luyện.

Điều quan trọng cần lưu ý là

chúng tôi chỉ chuyển đổi bài kiểm tra

dữ liệu mà không phù hợp với đại lượng vô hướng cho nó.

Điều này là do dữ liệu thử nghiệm nên

được thu nhỏ bằng cách sử dụng các tham số từ

dữ liệu huấn luyện để đảm bảo

tính nhất quán và ngăn ngừa rò rỉ dữ liệu.

Với điều đó chúng tôi đã sẵn sàng để xây dựng

mô hình ML đầu tiên của chúng tôi sử dụng KNN.

Chúng ta sẽ bắt đầu với việc nhập

lớp liên quan và

mô-đun từ thư viện scikit-learn.

Trong trường hợp của chúng tôi,

chúng tôi nhập Kneighborclassified

lớp từ mô-đun của hàng xóm.

Bây giờ hãy tạo một instance

của mô hình KNN chứa

thông tin về giá trị của K hoặc

số lượng hàng xóm.

Theo mặc định,

số lượng hàng xóm là năm.

Bây giờ, chúng ta hãy sử dụng mặc định

giá trị của năm lân cận.

Bây giờ chúng ta hãy sử dụng hàm fit để huấn luyện

mô hình của chúng tôi bằng cách sử dụng dữ liệu đào tạo được chia tỷ lệ.

Bây giờ bạn đã chạy mã này,

một mô hình KNN đã học được các quy tắc hoặc

các mẫu từ dữ liệu tàu được chia tỷ lệ.

Bây giờ, chúng ta hãy sử dụng những kiến thức này để thực hiện

dự đoán trên cùng một dữ liệu huấn luyện.

Điều này sẽ giúp chúng ta đánh giá

mô hình tốt thế nào

thực hiện trên dữ liệu mà nó đã học được.

Bây giờ, hãy sử dụng lại chức năng dự đoán

để đưa ra những dự đoán về cái mới hoặc

dữ liệu không nhìn thấy, đó là dữ liệu được chia tỷ lệ

phiên bản thử nghiệm được chia tỷ lệ x_test_scaled.

Dự đoán trên dữ liệu thử nghiệm mang lại

chúng tôi cảm nhận được mô hình này tốt như thế nào

có thể khái quát hóa dữ liệu mới

rằng nó chưa được đào tạo.

Đây là một bước quan trọng

trong học máy,

vì nó giúp đánh giá hiệu suất của mô hình

và liệu nó có khả năng hoạt động tốt trên

dữ liệu thực tế bên ngoài

của tập huấn luyện.

Vì vậy, hãy tiếp tục và chạy ô này.

Và là bước cuối cùng của cuốn sổ này,

chúng ta hãy đánh giá mô hình.

Chúng tôi sẽ sử dụng độ chính xác,

đó là một trong những cách đơn giản nhất và

thước đo đánh giá được sử dụng nhiều nhất cho

mô hình phân loại.

Độ chính xác đơn giản là số lượng đúng

dự đoán chia cho tổng số

số dự đoán.

Hãy nhập điểm chính xác từ

mô-đun ma trận của thư viện scikit-learn.

Bây giờ, chúng ta hãy lấy điểm chính xác cho

cả tập dữ liệu huấn luyện và tập dữ liệu kiểm tra.

Chức năng tính điểm chính xác,

lấy các giá trị dự đoán và

các giá trị thực tế làm đầu vào.

Như chúng ta có thể thấy, khi K hoặc

số lượng hàng xóm bằng năm,

chúng tôi nhận được điểm chính xác là 88,7% cho

dữ liệu huấn luyện và 82,8% cho dữ liệu thử nghiệm.

Đây có phải là hiệu suất mô hình tốt nhất

mà chúng ta có thể đạt được bằng cách sử dụng KNN?

Câu trả lời là chúng ta vẫn chưa biết.

Một trong những siêu tham số quan trọng của

KNN là số lượng hàng xóm.

Trong video tiếp theo,

chúng ta hãy thử chơi với số lượng

hàng xóm để tìm ra mô hình tốt nhất.