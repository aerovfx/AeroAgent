# 05 giới thiệu-phân-dữ liệu

---

Có nhiều phương pháp khác nhau để đánh giá

độ tin cậy của dự đoán của chúng tôi

Một số phương pháp kiểm tra

độ tin cậy của dự đoán của chúng tôi là đào tạo

xác nhận, xác nhận chéo,

bỏ-Một-Out, v.v.

Những phương pháp này đi theo

tiêu đề của Phòng dữ liệu.

Trong số nhiều cách

để chia tập dữ liệu.

Trong video này, chúng tôi sẽ tập trung vào

cách tiếp cận phổ biến nhất để chia,

nghĩa là, Train xác thực sự phân chia.

Trong các phần sau của khóa học này,

chúng tôi cũng sẽ giới thiệu cái khác

các phương pháp phân chia dữ liệu

Vậy hãy bắt đầu.

Giả sử hộp đen này tượng trưng

bộ dữ liệu Synergic Solutions và

chúng ta cần dự đoán số lượng hàng đã bán

ở đây trong tập dữ liệu có sẵn,

chúng ta biết cả các biến đầu vào và

các đơn vị đã bán.

Nhưng đối với tập dữ liệu chưa thấy hoặc dữ liệu trong tương lai

nơi chúng ta cần dự đoán số lượng sản phẩm đã bán,

chúng tôi chỉ có thông tin

về các biến đầu vào.

Giả sử chúng ta sử dụng giá trị trung bình của các đơn vị

được bán từ tập dữ liệu có sẵn và

sử dụng điều đó làm dự đoán cho

những dữ liệu chưa được nhìn thấy

Chúng ta hãy tạm dừng ở đây một lát.

Bạn có nghĩ rằng bạn sẽ có thể

Dự đoán hiệu suất của mô hình trên

tập dữ liệu chưa nhìn thấy?

Vâng, không.

Điều này là do chúng tôi chưa bao giờ kiểm tra

hiệu suất của mô hình này trước đó và

chúng tôi không biết số lượng thực tế đã bán

tập dữ liệu chưa được nhìn thấy.

Đây là nơi tàu hỏa

xác thực sự phân chia có thể giúp chúng tôi.

Trong phương pháp này, chúng tôi chia sẵn

dữ liệu thành hai phần có sẵn một và

có sẵn hai.

Sự phân chia này có thể tuần tự hoặc

ngẫu nhiên tùy theo lời giải của bài toán.

Trong thế giới khoa học dữ liệu, chúng tôi gọi

có sẵn một dữ liệu dưới dạng dữ liệu đào tạo và

có sẵn hai dữ liệu làm dữ liệu xác nhận.

Trong kịch bản này, chúng tôi biết đầu vào

biến và đơn vị được bán cho

cả dữ liệu huấn luyện và dữ liệu xác nhận, vì những dữ liệu này

là tập hợp con của tập dữ liệu có sẵn.

Bây giờ chúng ta xây dựng một mô hình

trên tập dữ liệu tàu.

Tức là chúng ta chỉ sử dụng giá trị trung bình

từ tập dữ liệu tàu và

sử dụng giá trị đó làm giá trị dự đoán cho

tập dữ liệu xác thực.

Xin lưu ý dữ liệu xác nhận sẽ

không được tiếp xúc với người mẫu.

Điều đó có nghĩa là nó sẽ không được sử dụng

trong khi tính giá trị trung bình.

Cuối cùng, chúng tôi sẽ kiểm tra hiệu suất

của mô hình trên dữ liệu xác nhận

trước khi sử dụng nó trên dữ liệu chưa nhìn thấy.

Với cách tiếp cận này, chúng ta sẽ có thể

dự đoán kết quả của mô hình

trước khi thực sự sử dụng

nó trên tập dữ liệu chưa nhìn thấy.

Nếu mô hình chính xác 77%

trên tập dữ liệu xác thực,

thì chúng ta có thể dự đoán tương tự

hiệu suất trên tập dữ liệu không nhìn thấy là tốt.

Đây là cách phân chia dữ liệu giúp chúng ta

Kiểm tra độ tin cậy của mô hình trên

tập dữ liệu chưa nhìn thấy hoặc trong tương lai.

>> Người nói 2: Vậy,

bất cứ khi nào bạn xây dựng một mô hình,

luôn đảm bảo rằng bạn chuẩn bị

bộ xác thực cho độ tin cậy của mô hình.

Sau đó chọn thước đo đánh giá phù hợp để

kiểm tra tính đúng đắn của dự đoán bằng

ghi nhớ thông tin đó, hãy thực hiện

những khái niệm chúng ta đã học cho đến nay.

trên tập dữ liệu mẫu cho Synergy.