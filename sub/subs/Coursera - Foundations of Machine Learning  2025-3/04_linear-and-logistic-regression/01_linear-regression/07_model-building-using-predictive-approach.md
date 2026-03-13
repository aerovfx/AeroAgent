# 07 phương pháp xây dựng mô hình sử dụng dự đoán

---

Cho đến nay trong bài học này chúng ta có

tập trung vào

phương pháp miêu tả.

Cách tiếp cận này đã giúp

chúng tôi hiểu

những giả định khác nhau của

mô hình hồi quy tuyến tính.

Trong video cuối cùng này

của bài học,

chúng tôi sẽ chuyển số sang

tập trung vào

cách tiếp cận mang tính dự đoán.

Chúng tôi sẽ chủ yếu tập trung

về cách dự đoán trên

linh hồn đơn vị sẽ hoạt động

trên tập dữ liệu chưa nhìn thấy.

Tôi chắc chắn bạn sẽ có

nhận thấy rằng chúng tôi đã làm

không chia tập dữ liệu trong

phương pháp miêu tả đó.

Trong phương pháp dự đoán,

chúng ta sẽ chia tay

tập dữ liệu và phù hợp

mô hình của chúng tôi chỉ trên

tập huấn luyện sao cho

chúng ta có thể sử dụng những dự đoán

trên bộ xác nhận để có được

ước tính của

hiệu suất của

mô hình trên tập dữ liệu chưa nhìn thấy.

Điều này sẽ rất giống với

cách chúng tôi xây dựng mô hình của mình bằng cách sử dụng

KNN trong mô-đun trước đó.

Hãy bắt đầu.

Hãy bắt đầu bằng cách nhập

các thư viện cần thiết

và tải tập dữ liệu.

Bây giờ chúng ta sẽ bỏ

đơn vị bán được lớn hơn

1.000 cột như chúng tôi đã làm

trong các video trước.

Trong bước tiếp theo, chúng tôi sẽ

chuyển đổi tính năng phân khúc thành

kiểu số sử dụng

một mã hóa nóng và

hàm Lambda,

giống như chúng tôi đã làm trong

video trước đó.

Bạn có thể thấy rằng các giá trị

bây giờ được chuyển đổi thành

dạng số.

Bây giờ khi đã thực hiện xong các bước này,

chúng tôi đã sẵn sàng để xây dựng mô hình.

Để bắt đầu, chúng tôi

tách dữ liệu của chúng tôi thành

giá trị dự đoán x và

biến mục tiêu y.

Ở đây, df_encoded là

tập dữ liệu được mã hóa của chúng tôi.

Đơn vị được bán ở đâu

biến mục tiêu của chúng tôi,

đó là số lượng đơn vị

đã bán mà chúng tôi muốn dự đoán.

Chúng tôi đang loại bỏ nó khỏi x vì

đó là biến chúng tôi

đang hướng tới việc dự đoán.

Khi chúng tôi đã sẵn sàng dữ liệu,

bước tiếp theo là chia nó

vào đào tạo và

bộ xác thực.

Sử dụng sklearn train_test_split,

chúng tôi phân bổ 70% dữ liệu của mình cho

đào tạo và còn lại

30% để xác nhận.

Bằng cách thiết lập một trạng thái ngẫu nhiên,

chúng tôi đảm bảo rằng

sự chia tách có thể tái tạo được.

Các hình dạng của chúng tôi

x_train và x_test

cho chúng tôi một ý tưởng về

có bao nhiêu mẫu nằm trong của chúng tôi

tập dữ liệu huấn luyện và kiểm tra.

Bây giờ dữ liệu của chúng tôi đã sẵn sàng,

đã đến lúc xây dựng bội số của chúng ta

mô hình hồi quy tuyến tính.

Đầu tiên chúng ta khởi tạo mô hình

sử dụng hồi quy tuyến tính.

Sau khi khởi tạo, chúng ta

đào tạo mô hình của chúng tôi bằng cách sử dụng

phương pháp phù hợp trong quá trình đào tạo của chúng tôi

dữ liệu, x_train và y_train.

Sau khi mô hình được huấn luyện,

chúng tôi sử dụng nó để dự đoán

đơn vị biến mục tiêu

bán trên cả đào tạo

và tập dữ liệu thử nghiệm.

Sau đó chúng tôi đánh giá độ chính xác của

mô hình của chúng tôi sử dụng giá trị r^2.

Ở đây chúng ta có thể quan sát

đó là

không đáng kể

sự khác biệt giữa

giá trị huấn luyện và kiểm tra r^2.

Điểm r^2 là 0,46 trên cả hai

bộ huấn luyện và kiểm tra

chỉ ra rằng mô hình r

nhất quán trong

hiệu suất của nó

trên cả hai hiện trường

và những dữ liệu chưa được nhìn thấy.

Đây là một dấu hiệu tốt vì nó

có nghĩa là mô hình

không trang bị quá mức.

Hãy so sánh hiệu suất của

hồi quy tuyến tính này

mô hình chống lại

mô hình KNN trong

mô-đun trước đó.

Có thể thấy rõ rằng

giá trị r^2 thu được cho

vấn đề hồi quy

đáng kể

lớn hơn số thu được

bằng phương pháp KNN.

Tuy nhiên, vẫn còn một

rất nhiều phòng cải tiến.

Có thể chỉ ra một số

mức độ không phù hợp.

Nó có thể có lợi cho

thử các mô hình khác nhau,

thêm dữ liệu bổ sung

và tiến hành

kỹ thuật tính năng.

Chúng tôi sẽ thử các tùy chọn này trong

các mô-đun và khóa học sau này.

Trước khi chúng ta kết thúc,

điều quan trọng là phải lưu mô hình,

vì việc lưu mô hình cho phép

chúng tôi sử dụng lại mô hình

mà không cần đào tạo lại và tái tạo

kết quả tương tự vào thời gian sau đó.

Hãy lưu lại

mô hình sử dụng joblib.