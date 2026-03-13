# 03 cách-model-quyết định-dòng-phù hợp nhất

---

Xin chào và chào mừng trở lại.

Ở phần trước

video, chúng tôi đã hình dung

tầm quan trọng của

độ dốc và chặn với

các giá trị khác nhau của M và C. Chúng tôi

quan sát cách điều chỉnh những điều này

các giá trị biến đổi dòng của chúng tôi,

nhưng ở đây có một

câu đố quan trọng.

Làm sao chúng ta tìm được

một dòng đó

nổi bật giữa những người khác

trong việc dự đoán doanh số bán hàng,

đó là đơn vị được bán dưới dạng

chính xác nhất có thể?

Hoặc để diễn đạt lại?

Làm thế nào chúng ta tìm được

giá trị đúng của M và C,

điều đó sẽ cho chúng ta

dòng phù hợp nhất?

Trong video này, chúng tôi

sẽ học

một cách tiếp cận chung để

tìm ra dòng phù hợp nhất.

Dòng phù hợp nhất là gì?

Dòng phù hợp nhất, như

cái tên gợi ý,

là dòng phù hợp với chúng tôi

điểm dữ liệu tốt nhất.

Nó giảm thiểu sai sót giữa

giá trị dự đoán và thực tế

của một biến phụ thuộc,

đảm bảo rằng mô hình của chúng tôi là

chính xác nhất có thể.

Hãy hiểu làm thế nào để

tìm ra dòng phù hợp nhất.

Ở nhiều máy

học thuật toán,

kỹ thuật tối ưu hóa được sử dụng

để tìm ra điều tốt nhất

tập hợp các tham số.

Các kỹ thuật tối ưu hóa này

tìm thông số tốt nhất

cho một mô hình giảm thiểu

hàm mất mát.

Một hàm mất mát cho chúng ta biết

về những sai sót của

dự đoán của mô hình.

Trong trường hợp hồi quy tuyến tính,

tổng các sai số bình phương là

một hàm mất mát phổ biến.

Phương pháp được sử dụng để giảm thiểu

hàm mất mát này là

thường được gọi là bình thường

phương pháp bình phương tối thiểu.

Hãy hiểu bình thường

phương pháp bình phương tối thiểu,

hoặc phương pháp OLS.

Để hiểu làm thế nào

giảm thiểu tổng của

lỗi bình phương giúp chúng tôi trong

xác định đường phù hợp nhất.

Chúng ta hãy nhìn vào một biểu đồ cho thấy

đơn vị được bán dựa trên lưu lượng truy cập trang.

Chúng ta thấy hai dòng có điểm khác nhau

độ dốc và điểm chặn.

Mục tiêu của chúng tôi là tìm

dòng nào trong hai dòng

phù hợp hơn thông qua của chúng tôi

ba điểm dữ liệu màu xanh.

Chúng ta hãy đi sâu vào một chút toán học.

Hãy đánh giá đường màu đỏ,

A. Hãy nhìn vào 0,1.

Giá trị thực tế là 500,

nhưng dự đoán

giá trị là 1.000

Điều đó mang lại cho chúng tôi lỗi 500.

Về mặt toán học, chúng ta có thể

lỗi ghi bằng nhau

y thực tế trừ y dự đoán,

nhưng nếu bạn nhìn vào 0,2,

chúng ta có thể thấy rằng

giá trị dự đoán là

1.500 và thực tế

giá trị là 2000,

cho chúng tôi lỗi -500.

Nếu chúng ta cộng hai lỗi đó lại,

chúng sẽ triệt tiêu lẫn nhau.

Để tránh phải đối mặt với

giá trị âm,

chúng tôi bình phương các lỗi.

Lỗi trở thành y thực tế

trừ y dự đoán bình phương.

Ý tưởng là tìm

dòng cung cấp cho chúng tôi

tổng sai số nhỏ nhất của

tất cả các điểm, không chỉ một.

Để làm như vậy, chúng ta chỉ cần cộng

tất cả các lỗi bình phương

cho mọi điểm.

Chúng tôi nhận được một cái gì đó như thế này.

Đây là hàm mất mát

được sử dụng trong phương pháp OLS.

Để tìm được mẫu phù hợp nhất,

chúng ta phải tìm giá trị

của các hệ số và

chặn sẽ cung cấp cho chúng tôi

giá trị nhỏ nhất của

hàm mất mát.

Như đã thảo luận trước đó, điều này

được thực hiện thông qua

các kỹ thuật tối ưu hóa.

Một tối ưu hóa rất phổ biến

kỹ thuật là giảm độ dốc,

nhưng chúng ta không phải lo lắng về

kỹ thuật này

bởi vì các thư viện

mà chúng ta sẽ sử dụng,

chẳng hạn như mô hình thống kê và

nhà tâm linh sẽ chăm sóc

phần tối ưu hóa cho chúng tôi.

Với điều này, chúng tôi đã đề cập đến

toán học cơ bản đằng sau

điều bình thường nhất

phương pháp hình vuông.

Trước khi chúng tôi chuyển sang

video tiếp theo,

Hãy để tôi hỏi bạn một câu hỏi.

OLS này phải không

công thức trông quen quen?

Nếu câu trả lời của bạn là có,

hãy vỗ nhẹ vào lưng mình.

Nếu chúng ta chia công thức này cho n,

số lượng

những quan sát chúng tôi nhận được,

sai số bình phương trung bình,

cái nào phổ biến

thước đo đánh giá

mà chúng tôi đã học về

trong mô-đun trước.

Với điều này, chúng tôi đã đến

đến cuối video này.

Hãy áp dụng những bài học này

trong video tiếp theo và tạo

hồi quy tuyến tính đơn giản

mô hình dự đoán đơn vị

được bán cho các sản phẩm dựa trên

đặc điểm đã được xác định,

đó là lưu lượng truy cập trang.