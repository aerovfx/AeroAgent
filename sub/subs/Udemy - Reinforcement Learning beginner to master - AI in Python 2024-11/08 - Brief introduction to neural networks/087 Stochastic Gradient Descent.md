## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong video này, chúng ta sẽ xem cách giảm thiểu hàm chi phí.

### 00:00:04.000 - 00:00:09.000
Chúng ta sẽ thực hiện điều đó bằng một thuật toán gọi là giảm độ dốc ngẫu nhiên.

### 00:00:09.000 - 00:00:12.000
Thuật toán này hoạt động như sau.

### 00:00:12.000 - 00:00:18.000
Đầu tiên, chúng ta sẽ ước tính giá trị của hàm chi phí bằng cách sử dụng phần thưởng thu được từ

### 00:00:18.000 - 00:00:22.000
môi trường và ước tính mạng lưới thần kinh.

### 00:00:22.000 - 00:00:25.000
Để thực hiện thuật toán đó sẽ thực hiện các bước sau.

### 00:00:26.000 - 00:00:32.000
Đầu tiên, chúng ta sẽ ước tính giá trị của hàm chi phí bằng cách sử dụng phần thưởng thu được từ

### 00:00:32.000 - 00:00:35.000
môi trường và ước tính mạng lưới thần kinh.

### 00:00:36.000 - 00:00:42.000
Khi chúng ta có ước tính của hàm này, chúng ta sẽ tìm vectơ gradient của nó.

### 00:00:42.000 - 00:00:50.000
Vectơ gradient rõ ràng là một vectơ trong đó mỗi phần tử là đạo hàm riêng của giá trị ước lượng

### 00:00:50.000 - 00:00:56.000
hàm chi phí đối với từng tham số của mạng nơ-ron.

### 00:00:56.000 - 00:00:58.000
Điều này có nghĩa là gì?

### 00:00:58.000 - 00:01:06.000
Vâng, gradient là một vectơ chỉ hướng mà mỗi tham số của mạng nơ-ron

### 00:01:06.000 - 00:01:12.000
phải được sửa đổi để hàm chi phí tăng lên càng nhiều càng tốt.

### 00:01:13.000 - 00:01:17.000
Đừng lo lắng, vì chúng ta sẽ không tính vectơ này bằng tay.

### 00:01:17.000 - 00:01:19.000
Chúng tôi sẽ sử dụng thư viện PyTorch.

### 00:01:19.000 - 00:01:20.000
Điều đó sẽ làm điều đó cho chúng tôi.

### 00:01:20.000 - 00:01:25.000
Vectơ gradient được tính toán bằng thuật toán gọi là lan truyền ngược.

### 00:01:26.000 - 00:01:31.000
Chúng tôi sẽ không trình bày chi tiết vì nó không liên quan chặt chẽ đến học tăng cường.

### 00:01:31.000 - 00:01:37.000
Nhưng nếu bạn tò mò về cách hoạt động của thuật toán này, bạn có thể tìm thấy nó trong liên kết bên dưới.

### 00:01:37.000 - 00:01:42.000
Khi chúng ta có vectơ gradient này, chúng ta sẽ thực hiện quy tắc cập nhật.

### 00:01:42.000 - 00:01:47.000
Như bạn có thể thấy, nó rất giống với quy tắc cập nhật mà chúng ta đã sử dụng với các phương pháp dạng bảng.

### 00:01:47.000 - 00:01:55.000
Nhưng thay vì cập nhật các giá trị được lưu trữ trong bảng, chúng tôi đang cập nhật các tham số của mạng nơ-ron.

### 00:01:55.000 - 00:02:01.000
Và các tham số này thể hiện cường độ kết nối giữa các nơ-ron trong quy tắc cập nhật này

### 00:02:01.000 - 00:02:03.000
về các giá trị trước đó.

### 00:02:03.000 - 00:02:09.000
Đối với các tham số, chúng tôi trừ phần trăm alpha nhân với độ dốc của hàm chi phí.

### 00:02:09.000 - 00:02:17.000
Điều này có nghĩa là chúng ta sẽ di chuyển các tham số theo hướng ngược lại với hướng cực đại

### 00:02:17.000 - 00:02:19.000
sự tăng trưởng của hàm chi phí.

### 00:02:20.000 - 00:02:27.000
Nghĩa là, chúng ta sẽ tìm các tham số sẽ tạo ra giá trị thấp nhất cho hàm chi phí bằng cách đi tới

### 00:02:27.000 - 00:02:32.000
theo hướng ngược lại với hướng ước tính của mức tăng trưởng tối đa.

### 00:02:32.000 - 00:02:36.000
Bây giờ chúng ta hãy xem trực quan cách hoạt động của việc giảm độ dốc ngẫu nhiên.

### 00:02:37.000 - 00:02:40.000
Chúng ta hãy xem nó qua hai ví dụ về hàm chi phí mà chúng ta đã thấy trước đó.

### 00:02:41.000 - 00:02:47.000
Hãy nhớ rằng đây là một ví dụ đơn giản về hàm chi phí trong đó chỉ có hai tham số

### 00:02:47.000 - 00:02:55.000
W1 và W2, đồng thời trục tung hiển thị giá trị của hàm chi phí cho mỗi kết hợp có thể có

### 00:02:55.000 - 00:02:58.000
của W1 và W2.

### 00:02:59.000 - 00:03:04.000
Trong biểu đồ bên phải, chúng ta thấy hàm chi phí tương tự ở trên để thấy rõ hơn.

### 00:03:05.000 - 00:03:10.000
Các mũi tên mà bạn nhìn thấy ở đây là giá trị âm của gradient của hàm chi phí.

### 00:03:11.000 - 00:03:17.000
Nghĩa là, chúng là những mũi tên chỉ hướng giảm tối đa của hàm chi phí.

### 00:03:18.000 - 00:03:24.000
Lưu ý rằng chúng là độ dốc của hàm chi phí thực, không phải của các ước tính sẽ tạo ra

### 00:03:24.000 - 00:03:26.000
dựa trên kinh nghiệm mà đại lý thu thập.

### 00:03:27.000 - 00:03:30.000
Bây giờ hãy xem thuật toán giảm độ dốc hoạt động như thế nào.

### 00:03:30.000 - 00:03:34.000
Khi chúng ta khởi tạo mạng nơron, các tham số sẽ có giá trị ngẫu nhiên.

### 00:03:34.000 - 00:03:41.000
Trong trường hợp này, đây là giá trị ban đầu của các tham số dựa trên kinh nghiệm mà tác nhân

### 00:03:41.000 - 00:03:41.000
thu thập.

### 00:03:41.000 - 00:03:48.000
Tương tác với môi trường sẽ tính toán ước tính hàm chi phí và vectơ độ dốc.

### 00:03:48.000 - 00:03:53.000
Nó tiêu cực, đó là điều chúng ta quan tâm, chỉ theo hướng này.

### 00:03:53.000 - 00:03:59.000
Đây là một xấp xỉ tương đối tốt nhưng không hoàn hảo với độ dốc thực của hàm chi phí.

### 00:03:59.000 - 00:04:00.000
Dựa trên tham số alpha.

### 00:04:00.000 - 00:04:07.000
Chúng ta sẽ thực hiện một bước theo hướng này và các tham số của mạng nơ-ron sẽ thay đổi thành các giá trị này.

### 00:04:07.000 - 00:04:14.000
Chúng ta sẽ lặp lại quá trình này cho đến khi ước tính của hàm chi phí ngừng giảm và tại thời điểm đó

### 00:04:14.000 - 00:04:20.000
chúng tôi sẽ giả định rằng chúng tôi đã đạt đến giá trị tối ưu hoặc gần tối ưu cho các tham số.

### 00:04:21.000 - 00:04:28.000
Bây giờ chúng ta hãy xem hàm chi phí phức tạp hơn, các hàm chi phí mà mạng nơ-ron của chúng ta sẽ tạo ra

### 00:04:28.000 - 00:04:34.000
sẽ phức tạp hơn nhiều so với những cái bạn thấy ở đây, vì chúng có một số lượng lớn các tham số và

### 00:04:34.000 - 00:04:36.000
biểu thị những hiện tượng phức tạp.

### 00:04:36.000 - 00:04:39.000
Hãy lặp lại quá trình giảm độ dốc.

### 00:04:39.000 - 00:04:45.000
Hãy tưởng tượng rằng các giá trị ban đầu của mạng nơ-ron là các giá trị W2 và W1.

### 00:04:45.000 - 00:04:52.000
Sau đó, bắt đầu từ thời điểm này, chúng ta sẽ sử dụng các mẫu kinh nghiệm để tính toán ước tính của hàm chi phí.

### 00:04:52.000 - 00:05:00.000
Độ dốc ước tính và sau đó chúng tôi sẽ theo dõi âm của độ dốc theo tỷ lệ phần trăm alpha và

### 00:05:00.000 - 00:05:04.000
chúng ta sẽ di chuyển các tham số của mạng lưới thần kinh ở đây.

### 00:05:04.000 - 00:05:09.000
Chúng tôi sẽ tiếp tục làm như vậy cho đến khi đạt đến điểm tối thiểu cục bộ.

### 00:05:10.000 - 00:05:13.000
Bây giờ hãy tưởng tượng rằng điểm ban đầu là điểm này.

### 00:05:13.000 - 00:05:19.000
Sau đó, theo quá trình giảm độ dốc, chúng ta sẽ đạt đến mức tối thiểu cục bộ này.

### 00:05:19.000 - 00:05:25.000
Như bạn có thể thấy, các giá trị ban đầu của mạng lưới thần kinh có ảnh hưởng đến quá trình học tập.

### 00:05:26.000 - 00:05:28.000
Hãy xem ví dụ thứ ba.

### 00:05:28.000 - 00:05:34.000
Nếu các giá trị ban đầu của mạng nơ-ron là những giá trị này thì thuật toán giảm độ dốc ngẫu nhiên

### 00:05:34.000 - 00:05:39.000
sẽ đưa chúng ta đến mức tối thiểu cục bộ này, trên thực tế là mức tối thiểu toàn cầu.

