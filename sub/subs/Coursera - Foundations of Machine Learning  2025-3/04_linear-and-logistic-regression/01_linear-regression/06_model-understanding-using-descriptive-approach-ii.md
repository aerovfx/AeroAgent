# 06 mô hình-hiểu-sử dụng-mô tả-cách tiếp cận-ii

---

Trong video cuối cùng của chúng tôi,

chúng tôi hiểu vai trò quan trọng của VIF

trong việc loại bỏ những tính năng dư thừa.

Nhưng hãy nhớ rằng, mô hình mạnh mẽ của chúng tôi chưa được xây dựng

chỉ về việc giải quyết vấn đề đa cộng tuyến,

có rất nhiều thứ khác

các tham số như giá trị p,

Durbin Watson,

phân phối chuẩn của phần dư, v.v.

Tất cả những điều này kết hợp với nhau để kết hợp và

vẽ nên một bức tranh toàn cảnh về

độ tin cậy và hiệu suất của mô hình.

Trong video này, chúng ta sẽ tìm hiểu

ý nghĩa của các thông số này.

Vì vậy, hãy bắt đầu.

Trong quá trình hồi quy tuyến tính, mô hình

xây dựng bằng phương pháp mô tả,

một khi vấn đề của

đa cộng tuyến được giải quyết

Bước tiếp theo là tập trung vào

ý nghĩa riêng của từng đặc điểm.

Đây là nơi giá trị p

đóng một vai trò quan trọng.

Giá trị p cho chúng ta biết liệu một

đặc điểm có ý nghĩa thống kê trong

dự đoán biến mục tiêu.

Nếu một tính năng không

có ý nghĩa thống kê,

đưa nó vào mô hình có thể giới thiệu

tiếng ồn không cần thiết, dẫn đến trang bị quá mức.

Theo quy ước, giá trị p thấp hơn

hơn 0,05 gợi ý rằng một tính năng là

có ý nghĩa thống kê ở

dự đoán biến mục tiêu.

Tuy nhiên, một lời cảnh báo,

chúng ta cần loại bỏ các tính năng dựa trên

giá trị p chỉ sau dữ liệu

không có hiện tượng đa cộng tuyến.

Bởi vì hiện tượng đa cộng tuyến có thể làm biến dạng

các giá trị p, làm cho chúng không đáng tin cậy.

Vì vậy, bước tiếp theo của chúng tôi là loại bỏ

các tính năng có giá trị p trên 0,05.

Hãy chuyển sang sổ ghi chép Jupyter và

thực hiện các bước này.

Đảm bảo chạy tất cả các ô

ở trên trước khi bạn bắt đầu.

Hãy lấy một bản tóm tắt chúng tôi thu được

ở cuối video trước.

Bạn có thể thấy rằng giá trị p của một số

các đặc điểm không đáng kể và

chúng ta có thể loại bỏ các tính năng này.

Bây giờ hãy xác định những đặc điểm

có giá trị p lớn hơn ngưỡng của chúng tôi.

Trước khi chúng tôi loại bỏ ít quan trọng hơn

tính năng, chúng tôi sẽ đảm bảo rằng

chúng tôi giữ lại hằng số hoặc đánh chặn như

nó là mấu chốt cho phương trình hồi quy của chúng tôi.

Đây là những tính năng không

đóng góp đáng kể cho mô hình của chúng tôi.

Bây giờ, hãy tiến hành loại bỏ các tính năng này.

Với bước này, chúng tôi đã tinh chỉnh dữ liệu của mình

chỉ bao gồm các tính năng có liên quan.

Chỉ còn một bước cuối cùng

trước khi chúng tôi xây dựng mô hình cuối cùng,

đây là bước tùy chọn

có thể giúp chúng ta hiểu

những tính năng nào quan trọng hơn đối với

mô hình học máy của chúng tôi.

Bước này đang mở rộng quy mô

các tính năng của dữ liệu.

Như bạn hiện có thể thấy, các tính năng

trong dữ liệu có phạm vi khác nhau.

Lưu lượng truy cập trang là hàng nghìn,

đơn giá có hai chữ số,

trong khi số lượng hình ảnh

chủ yếu ở dạng chữ số đơn.

Vì lý do này, chúng tôi không thể

so sánh các hệ số của một tính năng với

các hệ số của đặc tính khác.

Trong hồi quy tuyến tính, nếu tất cả các đặc trưng

nằm trong phạm vi tương tự, thì chúng ta có thể nói

rằng các đặc trưng có giá trị tuyệt đối lớn nhất

giá trị là những giá trị quan trọng nhất.

Mở rộng quy mô giúp chúng ta chuyển đổi tất cả

các tính năng nằm trong phạm vi tương tự.

Để làm điều này, hãy sử dụng một tiêu chuẩn

vô hướng từ Scikit-Learn.

Theo mặc định,

vô hướng tiêu chuẩn cho kết quả đầu ra trong

Mảng NumPy không có tên cột.

Để có thể giải nghĩa được,

chúng ta có thể chuyển đổi đầu ra trở lại

một khung dữ liệu và thêm tên cột.

Chúng ta hãy xem nhanh dữ liệu quy mô.

Như chúng ta có thể thấy, tất cả các tính năng khác nhau

hiện có phạm vi giá trị tương tự.

Với tất cả các bước tiền xử lý được thực hiện,

hãy xây dựng mô hình cuối cùng của chúng ta

bằng phương pháp miêu tả.

Trong mô hình cuối cùng, các hệ số có thể

được so sánh dựa trên giá trị tuyệt đối của chúng.

Vì tất cả các tính năng đều giống nhau

phạm vi giá trị, phân tích chúng

sẽ cung cấp những hiểu biết sâu sắc về người thân

ý nghĩa của những yếu tố dự báo này.

Ở đây bạn có thể xem trang

giao thông có mức cao nhất

giá trị tuyệt đối với

hệ số 255,56.

Điều này biểu thị rằng như

lưu lượng truy cập trang tăng lên,

có một lượng đáng kể

tăng số lượng đơn vị bán ra.

Điều này được mong đợi trong thời đại kỹ thuật số,

và Synergic nên tiến tới

cải thiện lưu lượng truy cập trang cho

các sản phẩm đa dạng của nó.

Trong khi lưu lượng truy cập trang có

tác động tích cực đến số lượng đơn vị bán ra,

đơn giá có số âm

ảnh hưởng đến đơn vị được bán.

Nó có giá trị tuyệt đối cao thứ hai

các giá trị của hệ số,

biến nó thành thứ hai

tính năng quan trọng nhất.

Hệ số là -105,93 và

giá trị âm của hệ số

chỉ ra rằng với sự gia tăng

đơn giá, đơn vị bán giảm.

Đó là một lời nhắc nhở rằng trong khi tăng

giá có thể là một chiến lược cho

cải thiện doanh thu,

có một sự cân bằng tinh tế để tấn công.

Tương tự, còn rất nhiều

các tính năng có trong bản tóm tắt mô hình.

Để hiểu rõ hơn về họ

tác động lên mô hình,

cố gắng phân tích sự tuyệt đối của họ

các giá trị của hệ số.

Cho đến nay trong mô-đun của chúng tôi,

chúng tôi đã xây dựng một mô hình mô tả

bằng cách giải quyết các mối quan tâm như

đa cộng tuyến và giá trị p.

Nhưng trong hồi quy tuyến tính,

có một số giả định.

Hãy xem xét các giả định quan trọng

điều đó xảy ra có liên quan

đến phần dư.

Đầu tiên, phần dư nên

được phân phối bình thường.

Phần dư của hồi quy sẽ

tuân theo mô hình phân phối chuẩn.

Nếu không, điều đó cho thấy

các vấn đề tiềm ẩn với mô hình hoặc

sự hiện diện của các ngoại lệ.

Có nhiều cách

để kiểm tra tính bình thường của

phần dư sử dụng phương pháp thống kê

phương pháp omnibus hoặc thử nghiệm Jarque-Bera.

Những thử nghiệm này cung cấp một cách để

kiểm tra tính chuẩn tắc của phần dư.

Một giá trị gần bằng 0 đối với

những thử nghiệm này chỉ ra rằng dư lượng

thường được phân phối.

Đối với mô hình của chúng tôi,

cả hai giá trị đều trên 100,

điều đó gợi ý rằng phần dư có thể

không được phân phối chuẩn hoàn hảo.

Ngoài các giá trị thử nghiệm,

chúng ta cũng có thể thấy độ lệch và độ nhọn,

điều đó cho chúng ta biết về đặc điểm

sự phân bố của phần dư.

Giá trị bằng 0 cho

độ lệch biểu thị sự đối xứng hoàn hảo.

Trong mô hình của chúng tôi, giá trị độ lệch là 0,068,

chỉ ra rằng phần dư

gần như được phân bố đối xứng,

đó là một dấu hiệu tích cực.

Kurtosis là thước đo của đỉnh cao

của sự phân phối phần dư.

Giá trị bằng ba cho biết

đỉnh cao hoàn hảo.

Đối với mô hình của chúng tôi, giá trị là 3,388,

cho thấy phần dư

có thể có đỉnh cao hơn một chút.

Thứ hai, phần dư nên

không được tự tương quan.

Không nên có khuôn mẫu nào trong các lỗi.

Nếu phần dư tự tương quan

nó cho thấy phần dư không

độc lập với nhau.

Để kiểm tra,

chúng ta có thể sử dụng số liệu thống kê của Durbin Watson.

Thống kê này có giá trị từ 0 đến

4, với giá trị lý tưởng là 2.

Trong mô hình của chúng tôi,

số liệu thống kê của Durbin Watson là 2,007,

điều đó chỉ ra rằng có rất ít

không có bằng chứng về sự tự tương quan,

phù hợp tốt với các giả định

của mô hình hồi quy tuyến tính của chúng tôi.

Chúng tôi đã giải quyết vấn đề này rồi

về đa cộng tuyến trong mô hình của chúng tôi,

điều này cũng có thể được xác nhận bởi

một số liệu gọi là số có điều kiện.

Một số có điều kiện dưới đây

30 biểu thị mức không đáng kể hoặc

không có sự tương quan giữa các đặc điểm.

Số có điều kiện của mô hình của chúng tôi là 5,57,

đó là trong ngưỡng.

Con số này cao hơn đáng kể

khi chúng tôi xây dựng mô hình đầu tiên của mình.

Bạn có thể so sánh con số này từ

bản tóm tắt thu được trước và

sau khi phương pháp này được thực hiện.

Điều này nhấn mạnh tầm quan trọng

loại bỏ một cách thận trọng những thứ dư thừa

tính năng thông qua các phương pháp như VIF và

đánh giá giá trị p.

Những biện pháp thống kê này cho chúng ta hiểu biết sâu sắc

hiểu biết sâu sắc về đặc điểm và

các vấn đề tiềm ẩn của mô hình hồi quy của chúng tôi.

Điều quan trọng là phải chú ý đến những điều này

giá trị trong phương pháp mô tả

hiểu ý nghĩa của chúng và

để đảm bảo rằng mô hình của chúng tôi

giả định được đáp ứng.

Trong video tiếp theo, chúng ta hãy tiếp tục và

xây dựng hồi quy đa tuyến tính

mô hình sử dụng phương pháp dự đoán.