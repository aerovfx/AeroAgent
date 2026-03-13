## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong video này, chúng ta sẽ khám phá cách triển khai chính sách của mình bằng mạng thần kinh.

### 00:00:05.000 - 00:00:10.000
Nhưng trước đó, hãy tìm hiểu tổng quan ngắn gọn về cách hoạt động của mạng lưới thần kinh.

### 00:00:11.000 - 00:00:18.000
Nếu bạn còn nhớ, mạng nơ-ron bao gồm các nơ-ron nhân tạo lấy đầu vào từ các nơ-ron

### 00:00:18.000 - 00:00:19.000
mà chúng được kết nối.

### 00:00:20.000 - 00:00:28.000
Chúng tổng hợp và biến đổi đầu vào đó trước khi chuyển nó đến các nơ-ron khác để thu được các giá trị mà chúng

### 00:00:28.000 - 00:00:30.000
một lớp sẽ lan truyền về phía trước.

### 00:00:30.000 - 00:00:37.000
Chúng tôi thực hiện phép nhân ma trận vectơ trong đó vectơ bao gồm các đầu ra của lớp trước

### 00:00:37.000 - 00:00:42.000
của mạng lưới thần kinh và ma trận biểu thị cường độ kết nối giữa các nơ-ron.

### 00:00:43.000 - 00:00:47.000
Cột đầu tiên thể hiện các kết nối của nơron đầu tiên.

### 00:00:47.000 - 00:00:53.000
Cái thứ hai đại diện cho các kết nối của cái thứ hai, v.v.

### 00:00:53.000 - 00:01:00.000
Với kết quả của phép nhân này, chúng ta sẽ áp dụng hàm kích hoạt để biến đổi các giá trị

### 00:01:00.000 - 00:01:03.000
trước khi truyền chúng sang lớp tiếp theo.

### 00:01:04.000 - 00:01:11.000
Mạng nơ-ron có thể được xem như một hàm trong đó y là đầu ra được tính toán bởi mạng nơ-ron.

### 00:01:11.000 - 00:01:15.000
X là đầu vào nhận được thông qua lớp đầu vào.

### 00:01:15.000 - 00:01:20.000
Và điều xảy ra khi mạng nơ-ron nhận được những đầu vào đó là chúng sẽ được nhân lên thông qua

### 00:01:20.000 - 00:01:24.000
ma trận kết nối đến lớp ẩn đầu tiên.

### 00:01:24.000 - 00:01:31.000
Khi đó hàm kích hoạt sẽ được áp dụng cho kết quả của các thao tác đó và sau đó là kết quả thu được

### 00:01:31.000 - 00:01:36.000
vectơ sẽ được nhân với ma trận kết nối của lớp đầu ra.

### 00:01:37.000 - 00:01:44.000
Và sau đó, hàm kích hoạt cuối cùng sẽ được áp dụng trước khi tạo ra các giá trị kết quả làm đầu ra.

### 00:01:46.000 - 00:01:53.000
Bằng cách thay đổi ma trận của tham số W1 và W2, chúng ta có thể sửa đổi mạng nơ-ron để xấp xỉ

### 00:01:53.000 - 00:01:55.000
chức năng mà chúng ta quan tâm.

### 00:01:57.000 - 00:02:00.000
Mã hóa Mạng lưới thần kinh trông như thế này.

### 00:02:00.000 - 00:02:06.000
Hoạt động đầu tiên thực hiện phép nhân ma trận giữa đầu vào và lớp ẩn.

### 00:02:06.000 - 00:02:11.000
Phép toán thứ hai biến đổi kết quả của phép toán trước và phép toán thứ ba nhân lên

### 00:02:11.000 - 00:02:17.000
đầu ra của lớp ẩn bằng ma trận kết nối với lớp đầu ra.

### 00:02:18.000 - 00:02:24.000
Trong các thuật toán trước, hàm kích hoạt của lớp đầu ra là hàm nhận dạng,

### 00:02:24.000 - 00:02:28.000
điều đó có nghĩa là lớp kích hoạt không áp dụng bất kỳ thay đổi nào.

### 00:02:29.000 - 00:02:35.000
Đó là vì chúng tôi đang tính toán các giá trị Q và các giá trị Q không bị giới hạn trong một phạm vi cụ thể

### 00:02:35.000 - 00:02:36.000
của các giá trị.

### 00:02:37.000 - 00:02:43.000
Tuy nhiên, bây giờ đầu ra của mạng nơron sẽ là một vectơ xác suất, do đó đầu ra của

### 00:02:43.000 - 00:02:48.000
mỗi nơ-ron ở lớp đầu ra phải có giá trị từ 0 đến 1.

### 00:02:48.000 - 00:02:51.000
Và tổng của các kết quả đầu ra phải là một.

### 00:02:51.000 - 00:02:56.000
Sở dĩ như vậy là vì tất cả các xác suất phải có tổng bằng 100%.

### 00:02:56.000 - 00:03:01.000
Vì vậy, bây giờ chúng ta sẽ cần một hàm kích hoạt trong lớp đầu ra để tạo ra những kết quả đó

### 00:03:01.000 - 00:03:06.000
và hàm kích hoạt đó sẽ là hàm softmax.

### 00:03:06.000 - 00:03:09.000
Ở đây bạn có thể thấy biểu thức toán học của nó.

### 00:03:09.000 - 00:03:18.000
Hàm Softmax sẽ chọn một hành động bằng cách khuếch đại đầu ra của nơ-ron và ức chế đầu ra

### 00:03:18.000 - 00:03:19.000
của phần còn lại.

### 00:03:19.000 - 00:03:26.000
Để làm điều đó, chúng ta sẽ tính giá trị của từng nơ-ron khi e nâng lên giá trị tổng hợp của nơ-ron đó

### 00:03:26.000 - 00:03:33.000
chia cho tổng của e nâng lên giá trị tổng hợp của mỗi nơ-ron.

### 00:03:33.000 - 00:03:35.000
Ở đây bạn có thể thấy rõ hơn.

### 00:03:35.000 - 00:03:42.000
Đầu vào là một vectơ có các giá trị tổng hợp của mỗi nơ-ron và đầu ra là kết quả của việc áp dụng

### 00:03:42.000 - 00:03:46.000
hàm softmax cho từng giá trị tổng hợp đó.

### 00:03:47.000 - 00:03:49.000
Và tổng của chúng, như chúng tôi đã nói, là một.

### 00:03:49.000 - 00:03:55.000
Về mặt đồ họa, các nơ-ron của lớp đầu ra tạo ra một vectơ giá trị.

### 00:03:55.000 - 00:04:02.000
Hàm softmax làm tăng sự khác biệt giữa các giá trị đó và chuẩn hóa chúng.

### 00:04:02.000 - 00:04:06.000
Và kết quả là một vector giống như cái bạn thấy ở bên phải.

### 00:04:07.000 - 00:04:13.000
Đây là một ví dụ trong đó mạng nơ-ron chọn hành động thứ hai, mang lại cho nó phần lớn

### 00:04:13.000 - 00:04:14.000
xác suất được chọn.

### 00:04:15.000 - 00:04:20.000
Các hành động còn lại sẽ có xác suất được chọn là 1%.

### 00:04:21.000 - 00:04:27.000
Đây là một ví dụ khác trong đó hàm gán lượng xác suất lớn nhất cho số đầu tiên.

### 00:04:27.000 - 00:04:34.000
hành động, mà cả hành động thứ hai cũng sẽ có xác suất được chọn là 39%.

### 00:04:35.000 - 00:04:41.000
Tóm lại, hàm Softmax là công cụ hoàn hảo cho mạng nơ-ron cần tạo ra xác suất

### 00:04:41.000 - 00:04:42.000
vectơ.

