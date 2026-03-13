## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong video này, chúng ta sẽ làm quen với kỹ thuật cuối cùng mà chúng ta sẽ áp dụng để cải thiện

### 00:00:04.000 - 00:00:06.000
quá trình học tập chính sách của chúng tôi.

### 00:00:07.000 - 00:00:14.000
Kỹ thuật này liên quan đến việc sử dụng entropy của chính sách để duy trì việc khám phá môi trường.

### 00:00:14.000 - 00:00:21.000
Bằng cách sử dụng thuật toán gradient chính sách, chúng tôi cũng muốn tác nhân của mình duy trì việc khám phá môi trường

### 00:00:22.000 - 00:00:27.000
để chúng ta có thể tìm cho mỗi hành động xác suất được chọn tối ưu.

### 00:00:27.000 - 00:00:33.000
Tuy nhiên, chúng tôi không có cơ chế như khi sử dụng các phương pháp dựa trên giá trị trong đó chính sách

### 00:00:33.000 - 00:00:37.000
hàm đã chọn một hành động ngẫu nhiên với một xác suất nhất định.

### 00:00:37.000 - 00:00:40.000
Bây giờ mạng lưới thần kinh là chính sách.

### 00:00:40.000 - 00:00:45.000
Vậy làm cách nào chúng ta có thể kết hợp cơ chế khám phá bên trong mạng lưới thần kinh của mình?

### 00:00:46.000 - 00:00:53.000
Chà, những gì chúng ta sắp làm là khuyến khích mạng lưới thần kinh giữ entropy trong xác suất của nó

### 00:00:53.000 - 00:00:54.000
vectơ cao.

### 00:00:54.000 - 00:00:56.000
Nhưng entropy là gì?

### 00:00:57.000 - 00:01:04.000
Well, it's a concept of information theory, different from the concept of entropy in physics that

### 00:01:04.000 - 00:01:08.000
đo lường mức độ không chắc chắn của một biến ngẫu nhiên.

### 00:01:08.000 - 00:01:15.000
Nghĩa là, hãy tưởng tượng rằng chúng ta có một biến ngẫu nhiên cho trước và chúng ta muốn lấy một mẫu có giá trị của nó.

### 00:01:15.000 - 00:01:22.000
Nếu chúng ta có thể biết trước các giá trị mà biến ngẫu nhiên sẽ nhận, thì biến ngẫu nhiên đó

### 00:01:22.000 - 00:01:25.000
biến có entropy thấp.

### 00:01:25.000 - 00:01:32.000
Nếu chúng ta không thể dự đoán trước giá trị sẽ lấy mẫu từ biến ngẫu nhiên này thì đó là

### 00:01:32.000 - 00:01:34.000
entropy sẽ cao.

### 00:01:34.000 - 00:01:41.000
Về mặt toán học đơn giản là số âm của tổng này và nó bao gồm xác suất của biến ngẫu nhiên

### 00:01:41.000 - 00:01:46.000
lấy giá trị đó nhân với logarit của xác suất đó.

### 00:01:46.000 - 00:01:47.000
Hãy xem nó với một ví dụ.

### 00:01:48.000 - 00:01:50.000
Hãy tưởng tượng rằng chúng ta có một đồng xu.

### 00:01:50.000 - 00:01:57.000
Biến ngẫu nhiên là kết quả của việc tung đồng xu đó và các giá trị có thể có của nó là mặt ngửa hoặc mặt ngửa.

### 00:01:57.000 - 00:02:03.000
Bây giờ hãy tưởng tượng rằng đồng xu đã được nạp và bất cứ khi nào chúng ta tung nó lên, nó luôn xuất hiện mặt ngửa và không bao giờ xuất hiện.

### 00:02:03.000 - 00:02:04.000
đuôi.

### 00:02:04.000 - 00:02:10.000
Khi đó entropy sẽ là số âm của xác suất nhận được mặt ngửa.

### 00:02:10.000 - 00:02:16.000
Đó là một lần logarit của xác suất nhận được mặt ngửa, cộng với xác suất nhận được

### 00:02:16.000 - 00:02:18.000
đuôi nhân logarit của nó.

### 00:02:18.000 - 00:02:26.000
Nghĩa là, entropy sẽ bằng 0 vì chúng ta biết trước điều gì sắp xảy ra có thể làm chúng ta ngạc nhiên.

### 00:02:26.000 - 00:02:28.000
Bây giờ chúng ta hãy nhìn vào một đồng tiền khác.

### 00:02:28.000 - 00:02:34.000
Lần này sẽ là một đồng xu bình thường với xác suất nhận được mặt ngửa là 50% và xác suất

### 00:02:34.000 - 00:02:37.000
khả năng nhận được mặt sấp cũng là 50%.

### 00:02:38.000 - 00:02:43.000
Trong trường hợp này, entropy của đồng xu sẽ âm với xác suất nhận được số lần ngửa

### 00:02:43.000 - 00:02:49.000
logarit của nó, cộng với xác suất có mặt sấp nhân với logarit của nó, sẽ gần bằng giá trị này

### 00:02:49.000 - 00:02:50.000
giá trị.

### 00:02:52.000 - 00:02:53.000
Lần này.

### 00:02:53.000 - 00:03:00.000
Nếu chúng ta cố đoán thì kết quả của việc tung đồng xu sẽ đoán sai khoảng 50%.

### 00:03:00.000 - 00:03:06.000
Vì thế kết quả của việc tung đồng xu này thường sẽ khiến chúng ta bất ngờ, khiến dự đoán của chúng ta thất bại.

### 00:03:07.000 - 00:03:09.000
Bây giờ hãy nhìn vào biểu đồ này.

### 00:03:09.000 - 00:03:15.000
Nó cho thấy entropy của việc tung một đồng xu khi chúng ta thay đổi xác suất để đồng xu đó ngửa.

### 00:03:16.000 - 00:03:23.000
Nếu xác suất là 0 hoặc 1 thì entropy bằng 0 vì chúng ta biết chính xác kết quả của lần lật

### 00:03:23.000 - 00:03:23.000
sẽ được.

### 00:03:24.000 - 00:03:29.000
Khi xác suất đạt tới 50%, entropy tăng lên.

### 00:03:29.000 - 00:03:36.000
Nếu xác suất mặt ngửa là 20% thì chúng ta vẫn có thể dự đoán kết quả chính xác 80%.

### 00:03:36.000 - 00:03:38.000
Nếu chúng ta đặt cược vào mặt sấp.

### 00:03:38.000 - 00:03:45.000
Tuy nhiên, khi xác suất tiến gần đến 50%, độ tin cậy của chúng ta vào dự đoán sẽ giảm xuống.

### 00:03:46.000 - 00:03:51.000
Entropy đạt mức cao nhất khi xác suất ra được mặt ngửa là 50%.

### 00:03:51.000 - 00:03:57.000
Bởi vì đây là loại tiền mà chúng ta ít tin tưởng nhất vào dự đoán của mình.

### 00:03:57.000 - 00:04:00.000
Nhưng làm thế nào chúng ta có thể sử dụng khái niệm này trong chính sách của mình?

### 00:04:01.000 - 00:04:07.000
Chà, bây giờ biến ngẫu nhiên là hành động mà chính sách sẽ chọn trong một trạng thái và entropy

### 00:04:07.000 - 00:04:15.000
được tính bằng cách nhân xác suất chọn từng hành động với logarit của nó và cộng tổng

### 00:04:15.000 - 00:04:17.000
kết quả rồi đổi dấu.

### 00:04:17.000 - 00:04:18.000
Tất nhiên rồi.

### 00:04:20.000 - 00:04:25.000
Hãy tưởng tượng rằng chúng ta có sẵn bốn hành động và các thanh trên biểu đồ này biểu thị các xác suất

### 00:04:25.000 - 00:04:27.000
được chọn trong một tiểu bang.

### 00:04:27.000 - 00:04:33.000
Chính sách này sẽ có entropy thấp vì nó khá rõ ràng hành động nào sẽ được chọn trong hầu hết các

### 00:04:33.000 - 00:04:34.000
thời gian.

### 00:04:34.000 - 00:04:41.000
Tuy nhiên, chính sách khác này có entropy cao vì chúng ta không thể dự đoán trước hành động nào sẽ

### 00:04:41.000 - 00:04:42.000
được chọn.

### 00:04:42.000 - 00:04:49.000
Để làm cho tác nhân khám phá môi trường, chúng ta phải giữ entropy của chính sách ở mức cao và

### 00:04:49.000 - 00:04:54.000
Điều chúng ta sắp làm để kết hợp entropy vào quy tắc học của mình là thêm entropy vào

### 00:04:54.000 - 00:04:59.000
hiệu suất chính sách được ước tính để độ dốc tăng dần cố gắng giữ ở mức cao.

### 00:05:00.000 - 00:05:05.000
Kỹ thuật này sẽ mang lại cho chúng ta một số lợi ích khi tối ưu hóa chính sách.

### 00:05:05.000 - 00:05:08.000
Đầu tiên là khám phá môi trường.

### 00:05:09.000 - 00:05:13.000
Một lợi ích khác là nó sẽ làm cho thuật toán của chúng tôi mạnh mẽ hơn.

### 00:05:13.000 - 00:05:20.000
Nghĩa là, nó sẽ làm cho các thuật toán của chúng tôi có khả năng xử lý các trạng thái mà chúng chưa từng thấy trước đây mà không cần

### 00:05:20.000 - 00:05:23.000
nó có sự sụt giảm đáng kể về hiệu suất của họ.

### 00:05:23.000 - 00:05:29.000
Và cuối cùng, khi chính sách đang tìm kiếm các giá trị tối ưu thì thuật toán khó có thể cải thiện

### 00:05:29.000 - 00:05:32.000
1% cuối cùng đó làm cho nó tốt hơn.

### 00:05:32.000 - 00:05:38.000
Entropy sẽ giúp chúng ta tinh chỉnh những chi tiết nhỏ đó bằng cách thử các hành động khác nhau.

