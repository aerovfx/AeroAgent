# 06 xây dựng-điểm chuẩn-mô hình-và-đánh giá-nó

---

Chúng ta hãy bắt đầu với việc nhập khẩu

các thư viện cần thiết.

NumPy và Pandas là

thư viện cơ bản cho dữ liệu

thao tác và phân tích.

Thư viện hệ điều hành trong Python

cung cấp công cụ để tương tác

với hệ điều hành,

cho phép quản lý hệ thống tập tin,

kiểm soát quá trình, và nhiều hơn nữa.

Matplotlib được sử dụng để

vẽ đồ thị khác nhau.

Bây giờ thay đổi cách làm việc

thư mục đến nơi bạn có

đã lưu trữ tập dữ liệu

sử dụng os.chdir.

Điều này đảm bảo rằng

thao tác tập tin tiếp theo

sẽ diễn ra ở

thư mục này.

Bây giờ hãy tải tập dữ liệu có tên

posample.xlsx thành một

Pandas DataFrame có tên pos.

Bạn có thể thay đổi đường dẫn

theo nơi bạn

đã lưu trữ tập dữ liệu.

Xin lưu ý rằng mẫu pos là

chỉ là một mẫu nhỏ hơn của

tập dữ liệu mà chúng tôi có.

Chúng ta cũng có thể thấy

năm hàng đầu tiên

của DataFrame bằng cách sử dụng

chức năng đầu.

Chúng ta có thể kiểm tra

hình dạng của tư thế

DataFrame bằng cách sử dụng

thuộc tính hình dạng,

chúng tôi có gần 4.000

hàng và bốn cột.

Bây giờ dựa trên những gì chúng tôi

đã học trước đó,

chúng tôi sẽ làm theo

các bước dưới đây để xây dựng

một cơ sở trung bình và một quy tắc

mô hình dự đoán dựa trên

Chúng ta sẽ bắt đầu bằng việc chia

các tập dữ liệu vào

đào tạo và tập dữ liệu hợp lệ sau đó

chúng tôi sẽ thực hiện dựa trên giá trị trung bình

và dự đoán dựa trên quy tắc.

Cuối cùng, chúng tôi sẽ đánh giá

độ chính xác của mô hình sử dụng MA.

Hãy bắt đầu với

chia tập dữ liệu.

Đối với điều này, chúng tôi sẽ sử dụng

bài kiểm tra tàu được tách ra từ

thư viện scikit-lean.

Scikit-learn hoặc SK-learn,

là một thư viện quan trọng trong Python

hệ sinh thái khoa học dữ liệu,

cung cấp các công cụ đa năng

cho việc học máy.

Nó toàn diện

bộ thuật toán

để phân loại,

hồi quy, phân cụm,

và tính chiều

giảm kết hợp với

tiện ích dữ liệu

tiền xử lý và

đánh giá mô hình,

làm cho nó không thể thiếu đối với

cả người mới bắt đầu và chuyên gia.

Khả năng tương thích của nó với khác

các thư viện như NumPy và

Gấu trúc hơn nữa

củng cố vị trí của nó

như một nền tảng cho

khoảng thời gian học máy.

Tiếp theo chúng ta sẽ chia

khung dữ liệu pos vào

tập hợp con đào tạo và xác nhận

sử dụng bài kiểm tra tàu hỏa

chức năng phân chia.

Phân bổ 20% dữ liệu

đến bộ xác thực

pos hợp lệ và phần còn lại để

tập huấn luyện pos train.

Chúng ta sẽ tìm hiểu về

thích hợp

tỷ lệ chia sau

trong khóa học này,

nhưng phổ biến

quy ước là 80 đến

20 70 là 30 và 75 là 25.

Xin lưu ý rằng bài kiểm tra tàu

chia nhỏ xáo trộn dữ liệu

ngẫu nhiên trước khi gán nó

để huấn luyện và xác nhận các tập hợp.

Bây giờ một điều cần lưu ý là khi

bạn sử dụng tàu hỏa

phân chia thử nghiệm bằng Python,

dữ liệu của bạn bị xáo trộn

ngẫu nhiên trước khi nó tách ra.

Mỗi lần bạn chạy sổ ghi chép,

bạn sẽ có một bộ khác

dữ liệu huấn luyện và xác nhận.

Để tránh điều này, chúng tôi

sử dụng trạng thái ngẫu nhiên.

Trạng thái ngẫu nhiên đảm bảo mã của bạn

là nhất quán và có thể tái tạo.

Điều này có nghĩa là mỗi lần

bạn chạy mã,

dữ liệu của bạn được xáo trộn trong

cùng một cách và bạn

nhận được kết quả tương tự.

Trong trường hợp của chúng tôi, chúng tôi đang thiết lập

trạng thái ngẫu nhiên là chín.

Bạn có thể thử nhiều số khác nhau

ở cuối video này.

Bây giờ chúng ta hãy kiểm tra hình dạng của

cả việc đào tạo

và bộ xác thực.

Trong mô hình đầu tiên của chúng tôi,

chúng tôi tính toán giá trị trung bình tổng thể của

cột đơn vị bán

trong tập dữ liệu huấn luyện.

Điều này cung cấp một giá trị trung bình

có thể được sử dụng như một

dự đoán điểm chuẩn.

Chúng tôi nhận được 1157 đơn vị

được bán theo giá trị.

Lưu ý rằng chúng tôi đã sử dụng

hàm int ở trên để có được

giá trị số nguyên như

đơn vị bán không thể

một số thập phân.

Bây giờ hãy tạo một cột

trước đó có nghĩa là đơn vị đã bán,

và thêm giá trị trung bình

của đơn vị được bán cho

đào tạo dữ liệu như giá trị dự đoán

của đơn vị được bán cho

dữ liệu xác thực.

Bây giờ chúng ta hãy chuyển sang

đánh giá mô hình.

Tất cả các số liệu trong scikit-learn

có thể được sử dụng thông qua

Số liệu SK-learn.

Nhập lỗi tuyệt đối trung bình

từ thư viện SK-learn,

sau đó tính toán

có nghĩa là sai số tuyệt đối

giữa thực tế và dự đoán

giá trị của các đơn vị đã bán.

Chúng tôi có MAE là

khoảng 307 in

dữ liệu xác nhận của chúng tôi.

Điều này cho thấy rằng khi chúng ta sử dụng

mô hình này trên dữ liệu chưa nhìn thấy

hoặc dữ liệu thế giới thực,

chúng ta nên mong đợi một lỗi

trung bình là 307 đơn vị.

Bây giờ bạn có

hiểu làm thế nào để

tạo và đánh giá

một mô hình dựa trên giá trị trung bình,

hãy tạo một mô hình dựa trên quy tắc.

Để đơn giản, chúng ta hãy có

một quy tắc duy nhất đó là,

thay vì sử dụng

toàn bộ trung bình của đơn vị

bán theo dự đoán

trên dữ liệu xác nhận,

sử dụng giá trị trung bình của đơn vị

được bán theo phân khúc từ

huấn luyện dữ liệu dưới dạng dự đoán

cho dữ liệu xác nhận.

Chúng tôi bắt đầu với việc sử dụng

Nhóm Pi để tính

ý nghĩa khôn ngoan của phân khúc

đơn vị được bán từ dữ liệu tàu.

Như có thể thấy, chúng ta có

ba phân đoạn với

phương tiện tương ứng của họ.

Bây giờ chúng ta hãy sử dụng

chức năng bản đồ để lập bản đồ

những phương tiện này để xác nhận

dữ liệu và xem xét chúng.

Chúng ta có thể thấy rằng giá trị trung bình của

dữ liệu xác nhận đã được

được lập bản đồ theo

phân đoạn mà mỗi SCID thuộc về.

Hãy đánh giá một quy tắc

dựa trên mô hình ngay bây giờ và xem liệu

MAE đã được cải thiện trong

so sánh với

mô hình dựa trên trung bình

Chúng ta có thể thấy rằng có

một sự cải thiện nhỏ trong

mô hình với MAE

cải thiện 0,6,

Tại sao bạn không thử đóng khung

quy tắc của riêng bạn để xem

mô hình thực hiện như thế nào?

Có thể tạo một

mô hình dựa trên trung vị,

hoặc thử tạo quy tắc

mô hình dựa trên nơi bạn sử dụng

sản phẩm có ý nghĩa khôn ngoan như

giá trị dự đoán cho

dữ liệu xác nhận.

Đó là nó. Trong video tiếp theo,

hãy hiểu

những nhược điểm của

mô hình dựa trên quy tắc và cách thức

học máy có thể

khắc phục những nhược điểm này.