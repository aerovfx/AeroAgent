## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong video này, chúng ta sẽ khám phá phương pháp đầu tiên của họ gradient chính sách mà chúng ta đang sử dụng.

### 00:00:05.000 - 00:00:06.000
sắp thực hiện.

### 00:00:06.000 - 00:00:08.000
Thuật toán này được gọi là củng cố.

### 00:00:09.000 - 00:00:14.000
Thuật toán là sự kết hợp giữa phương pháp gradient chính sách và phương pháp Monte Carlo.

### 00:00:14.000 - 00:00:21.000
Trong đó, đặc vụ sẽ phải đối mặt với nhiệm vụ hoàn thành một tập phim để thu thập kinh nghiệm và khi kết thúc

### 00:00:21.000 - 00:00:26.000
tập phim sẽ cập nhật mạng lưới thần kinh bằng cách sử dụng tất cả kinh nghiệm thu thập được.

### 00:00:26.000 - 00:00:33.000
Để thực hiện việc này, chúng tôi sẽ thực hiện bước tăng dần độ dốc ngẫu nhiên cho từng hành động được thực hiện trong tập

### 00:00:33.000 - 00:00:40.000
để chính sách cải thiện việc ra quyết định dựa trên kết quả của từng hành động.

### 00:00:40.000 - 00:00:46.000
Để làm như vậy, chúng tôi sẽ ước tính mức độ hiệu quả của chính sách dựa trên trải nghiệm mà

### 00:00:46.000 - 00:00:47.000
đại lý thu thập.

### 00:00:47.000 - 00:00:53.000
Nhờ định lý gradient chính sách, chúng ta biết biểu thức nào chúng ta phải xấp xỉ.

### 00:00:53.000 - 00:00:58.000
Với kinh nghiệm đó, phương pháp monte Carlo sẽ xấp xỉ biểu thức đó.

### 00:00:58.000 - 00:01:00.000
Sử dụng công thức này.

### 00:01:00.000 - 00:01:06.000
Ở đây GD là lợi nhuận thực tế thu được bắt đầu từ thời điểm t của tập phim.

### 00:01:07.000 - 00:01:09.000
Ở đây không có bootstrapping.

### 00:01:09.000 - 00:01:15.000
Thay vào đó, tất cả phần thưởng nhận được cho đến cuối tập sẽ được dùng để tính tiền lãi,

### 00:01:15.000 - 00:01:17.000
như phương pháp Monte Carlo vẫn làm.

### 00:01:17.000 - 00:01:24.000
Giá trị bạn nhìn thấy ở đây là Gamma, hệ số chiết khấu trong biểu thức It được nâng lên T, tức là

### 00:01:24.000 - 00:01:30.000
thời điểm mà hành động mà chúng tôi muốn sử dụng để cập nhật chính sách được thực hiện.

### 00:01:30.000 - 00:01:37.000
Nhân biểu thức với giá trị này sẽ mang lại nhiều trọng số hơn cho các cập nhật tương ứng với giá trị ban đầu

### 00:01:37.000 - 00:01:39.000
hành động và ít trọng lượng hơn cho những hành động cuối cùng.

### 00:01:39.000 - 00:01:46.000
Điều đó quan trọng vì những hành động ban đầu có ảnh hưởng lớn hơn đến kết quả của nhiệm vụ.

### 00:01:46.000 - 00:01:52.000
Vì một hành động xấu ở đầu tập phim có thể dẫn đặc vụ đến trạng thái không thể

### 00:01:52.000 - 00:01:53.000
hồi phục.

### 00:01:53.000 - 00:01:59.000
Và cuối cùng, giá trị cuối cùng ở đây là độ dốc của xác suất chọn hành động mà chúng ta

### 00:01:59.000 - 00:02:04.000
đã thực hiện chia cho xác suất chọn hành động đó.

### 00:02:05.000 - 00:02:11.000
Quy tắc cập nhật nói lên rằng chúng ta muốn tăng xác suất thực hiện hành động lên một

### 00:02:11.000 - 00:02:15.000
tỷ lệ thuận với lợi nhuận mà nó đạt được.

### 00:02:15.000 - 00:02:23.000
Nếu kết quả trả về là âm, biểu tượng dấu cộng ở đây sẽ trở thành dấu trừ và do đó chúng ta sẽ giảm

### 00:02:23.000 - 00:02:25.000
xác suất thực hiện hành động đó.

### 00:02:26.000 - 00:02:27.000
Có ý nghĩa, phải không?

### 00:02:28.000 - 00:02:34.000
Và hơn thế nữa, xác suất thực hiện hành động đó tăng tỉ lệ nghịch với xác suất

### 00:02:34.000 - 00:02:38.000
rằng mạng lưới thần kinh phải chọn hành động đó ngay bây giờ.

### 00:02:38.000 - 00:02:45.000
Điều đó có nghĩa là nếu mạng lưới thần kinh chọn hành động này thì xác suất của nó thường tăng lên.

### 00:02:45.000 - 00:02:48.000
sẽ nhỏ hơn nếu xác suất đó thấp.

### 00:02:48.000 - 00:02:56.000
Lưu ý rằng nếu hành động được chọn, thông thường nó cũng sẽ được cập nhật thường xuyên hơn và điều đó có thể gây ra

### 00:02:56.000 - 00:03:02.000
xác suất của nó tăng rất nhanh và khiến chúng ta ngừng khám phá những hành động còn lại.

### 00:03:02.000 - 00:03:08.000
Để tránh điều này, chúng tôi chia gradient cho xác suất của nó.

### 00:03:08.000 - 00:03:11.000
Bây giờ chúng ta chỉ cần thực hiện một thay đổi nhỏ cho quy tắc cập nhật.

### 00:03:12.000 - 00:03:19.000
Biểu thức này ở đây, trùng hợp thay, lại giống với việc lấy gradient của logarit của

### 00:03:19.000 - 00:03:21.000
xác suất lựa chọn hành động đó.

### 00:03:22.000 - 00:03:28.000
Và vì chúng ta muốn sử dụng biểu thức đơn giản nhất có thể để thực hiện việc tăng độ dốc, nên chúng ta sẽ thay thế

### 00:03:28.000 - 00:03:30.000
giá trị này vào công thức.

### 00:03:31.000 - 00:03:36.000
Đây sẽ là quy tắc cập nhật sẽ được thực hiện.

