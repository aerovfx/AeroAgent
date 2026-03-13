## Nội dung

### 00:00:01.000 - 00:00:04.000
Bây giờ, hãy xem liệu thuật toán có khả năng tìm ra chính sách tối ưu hay không.

### 00:00:07.000 - 00:00:11.000
Chúng ta hãy hiển thị bảng q sau khi nó được sửa đổi bằng thuật toán này.

### 00:00:14.000 - 00:00:15.000
Và nó đây.

### 00:00:17.000 - 00:00:22.000
Hãy chú ý đến thực tế là các trạng thái không nằm trong đường dẫn tối ưu.

### 00:00:23.000 - 00:00:25.000
Thực tế đã bị bỏ qua.

### 00:00:29.000 - 00:00:36.000
Một trong những lợi ích của việc sử dụng các phương pháp học tập dựa trên kinh nghiệm là chúng ta có thể tập trung nỗ lực

### 00:00:36.000 - 00:00:40.000
về các trạng thái và hành động dẫn chúng ta đến việc giải quyết nhiệm vụ một cách tối ưu.

### 00:00:41.000 - 00:00:43.000
Và đó là những gì đã xảy ra trong trường hợp này.

### 00:00:43.000 - 00:00:50.000
Thuật toán của chúng tôi đã không dành nhiều thời gian và công sức trong việc tinh chỉnh các ước tính về những trạng thái không

### 00:00:50.000 - 00:00:51.000
dẫn tới mục tiêu.

### 00:00:52.000 - 00:00:58.000
Tuy nhiên, đối với những trạng thái dẫn chúng ta đến mục tiêu, như bạn có thể thấy, những hành động tối ưu có

### 00:00:58.000 - 00:00:59.000
những giá trị cao nhất.

### 00:00:59.000 - 00:01:05.000
Nếu bạn nhìn vào trạng thái, hành động tối ưu sẽ giảm xuống, giống như ở trạng thái này và tất cả các trạng thái

### 00:01:05.000 - 00:01:08.000
của cột đầu tiên cho đến cột này.

### 00:01:09.000 - 00:01:12.000
Một khi chúng ta đã xuống tới đây, hành động tối ưu là di chuyển sang phải.

### 00:01:12.000 - 00:01:15.000
Như bạn có thể thấy, đó là cái có giá trị cao nhất.

### 00:01:17.000 - 00:01:20.000
Vì vậy, chính sách đang bảo chúng ta đi theo con đường tối ưu này.

### 00:01:23.000 - 00:01:28.000
Hoặc cái này đây. Điều tiếp theo mà chúng ta sẽ kiểm tra là liệu chính sách mà thuật toán có

### 00:01:28.000 - 00:01:32.000
cho chúng tôi là một trong những tối ưu.

### 00:01:32.000 - 00:01:39.000
Như bạn có thể thấy, trong đường dẫn tối ưu, chính sách quy định các hành động

### 00:01:39.000 - 00:01:43.000
dẫn chúng tôi đến mục tiêu trong khi ở các bang còn lại

### 00:01:43.000 - 00:01:50.000
như chúng tôi đã nói trước đây, thuật toán chưa đặt nhiều nỗ lực và do đó giá trị của chúng chưa được tinh chỉnh.

### 00:01:50.000 - 00:01:55.000
Không biết bạn có nhớ phần về quy hoạch động không, nhưng trong phần đó chúng ta đã làm gì

### 00:01:55.000 - 00:02:00.000
đang quét qua toàn bộ không gian của các tiểu bang, cải thiện từng tiểu bang.

### 00:02:02.000 - 00:02:09.000
Mặc dù điều đó mang lại cho chúng ta chính sách tối ưu và bảng giá trị q, nhưng nó cực kỳ kém hiệu quả vì chúng ta

### 00:02:09.000 - 00:02:13.000
lãng phí rất nhiều thời gian vào những trạng thái không giúp chúng ta đạt được mục tiêu của mình.

### 00:02:17.000 - 00:02:24.000
Điều cuối cùng mà chúng tôi sẽ kiểm tra là liệu tác nhân tuân theo chính sách này có khả năng giải quyết

### 00:02:24.000 - 00:02:26.000
nhiệm vụ. Hãy chạy tế bào

### 00:02:27.000 - 00:02:29.000
và có vẻ như vậy.

### 00:02:47.000 - 00:02:52.000
Như bạn có thể thấy, trong phần này, chúng ta đã có thể giải quyết một nhiệm vụ kiểm soát thông qua kinh nghiệm.

### 00:02:52.000 - 00:02:56.000
Và không chỉ vậy, chúng tôi còn thực hiện điều đó bằng hai chiến lược riêng biệt.

### 00:02:58.000 - 00:03:04.000
Một trong số họ sử dụng một chính sách duy nhất mà chúng tôi đã sửa đổi, để đôi khi chọn các hành động ngẫu nhiên và chính sách kia

### 00:03:04.000 - 00:03:10.000
one, cái mà chúng tôi vừa triển khai sử dụng các chính sách riêng biệt để khám phá và cải tiến.

