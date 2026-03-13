# 01 mạng lưới thần kinh-tổng quan

---

Chào mừng trở lại. Trong tuần này,

bạn đã học cách triển khai mạng lưới thần kinh.

Trước khi đi sâu vào chi tiết kỹ thuật,

Tôi muốn trong video này,

để cung cấp cho bạn cái nhìn tổng quan nhanh về nội dung bạn sẽ thấy trong các video tuần này.

Vì vậy, nếu bạn không làm theo tất cả các chi tiết trong video này,

đừng lo lắng về điều đó, chúng ta sẽ đi sâu vào chi tiết kỹ thuật trong một số video tiếp theo.

Nhưng bây giờ, hãy đưa ra một cái nhìn tổng quan nhanh về cách bạn triển khai mạng nơ-ron.

Tuần trước chúng ta đã nói về hồi quy logistic,

và chúng ta đã thấy mô hình này tương ứng như thế nào với bản dự thảo tính toán sau đây,

nơi bạn đặt các tính năng x và các thông số

w và b cho phép bạn tính z, sau đó được sử dụng để tính a,

và chúng tôi đã sử dụng thay thế cho nhau với

Kết quả này là y hat và sau đó bạn có thể tính hàm mất mát,

L. Mạng lưới thần kinh trông như thế này.

Như tôi đã ám chỉ trước đó,

bạn có thể hình thành một mạng lưới thần kinh bằng cách xếp chồng rất nhiều đơn vị sigmoid nhỏ lại với nhau.

Trong khi trước đây, nút này tương ứng với hai bước tính toán.

Đầu tiên là tính giá trị z,

thứ hai là nó tính toán giá trị này.

Trong mạng lưới thần kinh này,

chồng ghi chú này sẽ tương ứng với phép tính kiểu z như thế này,

cũng như một phép tính tương tự như thế.

Sau đó, nút đó sẽ tương ứng với một z khác và một phép tính tương tự khác.

Vì vậy, ký hiệu mà chúng tôi sẽ giới thiệu sau sẽ trông như thế này.

Đầu tiên, chúng ta sẽ nhập các tính năng, x,

cùng với một số tham số w và b,

và điều này sẽ cho phép bạn tính z một.

Vì vậy, ký hiệu mới mà chúng tôi sẽ giới thiệu là chúng tôi sẽ sử dụng

dấu ngoặc vuông siêu ký tự một để tham khảo

số lượng liên quan đến chồng nút này, nó được gọi là một lớp.

Sau đó, chúng ta sẽ sử dụng dấu ngoặc vuông chỉ số trên

hai để chỉ số lượng liên quan đến nút đó.

Đó được gọi là một lớp khác của mạng lưới thần kinh.

Dấu ngoặc vuông chỉ số trên,

như chúng ta có ở đây,

không được nhầm lẫn với

dấu ngoặc tròn chỉ số trên mà chúng tôi sử dụng để chỉ các ví dụ huấn luyện riêng lẻ.

Vì vậy, trong khi x dấu ngoặc tròn siêu ký tự tôi đề cập đến ví dụ đào tạo thứ i,

dấu ngoặc vuông một và hai chỉ số trên đề cập đến các lớp khác nhau này;

lớp một và lớp hai trong mạng lưới thần kinh này.

Nhưng cứ như vậy, sau khi tính toán z_1 tương tự như hồi quy logistic,

sẽ có một phép tính để tính a_1,

và đó chỉ là sigmoid của z_1,

rồi bạn tính z_2 bằng một phương trình tuyến tính khác rồi tính a_2.

A_2 là đầu ra cuối cùng

của mạng lưới thần kinh và cũng sẽ được sử dụng thay thế cho y-hat.

Vì vậy, tôi biết đó là rất nhiều chi tiết nhưng trực giác quan trọng để

bỏ đi điều đó trong khi đối với hồi quy logistic,

chúng tôi đã có z này theo sau là một phép tính.

Trong mạng lưới thần kinh này,

ở đây chúng tôi chỉ làm điều đó nhiều lần,

dưới dạng z theo sau là phép tính,

và a z theo sau là phép tính,

và cuối cùng bạn tính toán tổn thất ở cuối.

Bạn còn nhớ rằng đối với hồi quy logistic,

chúng tôi đã tính toán ngược lại để

để tính đạo hàm hoặc khi bạn tính d a,

dz và vân vân.

Vì vậy, theo cách tương tự,

mạng lưới thần kinh sẽ thực hiện một phép tính ngược trông giống như

phần này bạn kết thúc việc tính toán da_2,

dz_2, cho phép bạn tính dw_2,

db_2, v.v.

Tính toán lùi từ phải sang trái này được biểu thị bằng mũi tên màu đỏ.

Vì vậy, điều đó cung cấp cho bạn một cái nhìn tổng quan nhanh chóng về mạng lưới thần kinh trông như thế nào.

Về cơ bản, nó thực hiện hồi quy logistic và lặp lại hai lần.

Tôi biết có rất nhiều luật ký hiệu mới,

chi tiết mới, đừng lo lắng về việc lưu chúng,

hãy theo dõi mọi thứ, có lẽ chúng ta sẽ đi vào chi tiết trong một số video tiếp theo.

Vì vậy, chúng ta hãy chuyển sang video tiếp theo.

Chúng ta sẽ bắt đầu nói về cách biểu diễn mạng lưới thần kinh.