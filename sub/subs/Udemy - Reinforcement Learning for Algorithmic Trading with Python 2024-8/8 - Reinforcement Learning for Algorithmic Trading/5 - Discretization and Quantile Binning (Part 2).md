## Nội dung

### 00:00:00.000 - 00:00:07.960
Bây giờ, trong bài giảng trước, chúng ta đã rời rạc hóa và trở thành tính năng trả về trong khung dữ liệu huấn luyện

### 00:00:07.960 - 00:00:09.960
.

### 00:00:09.960 - 00:00:15.560
Và bây giờ chúng ta phải sử dụng các cạnh bin giống nhau để thực sự rời rạc hóa cả tính năng

### 00:00:15.560 - 00:00:17.519
 và tập kiểm tra.

### 00:00:17.519 - 00:00:22.240
Vì vậy, ý tưởng cơ bản là chúng ta nên sử dụng các cạnh thùng giống nhau cho tập kiểm tra như

### 00:00:22.240 - 00:00:23.240
tốt.

### 00:00:23.240 - 00:00:29.160
Và mặt khác, nếu chúng ta sử dụng dữ liệu huấn luyện và kiểm tra cùng nhau để xác định các cạnh thùng,

### 00:00:29.160 - 00:00:33.079
và rò rỉ dữ liệu sẽ là hiện tại.

### 00:00:33.079 - 00:00:38.880
Vì vậy, rò rỉ dữ liệu có nghĩa là chúng tôi sử dụng dữ liệu tập kiểm tra thực sự không xác định trong tương lai trong giai đoạn huấn luyện

### 00:00:38.880 - 00:00:40.039
.

### 00:00:40.039 - 00:00:43.600
Và điều này có thể dẫn đến hiệu suất kiểm tra sai lệch.

### 00:00:43.600 - 00:00:48.840
Vì vậy, thông thường, đó là hiệu suất kiểm tra hai tích cực, hai tốt.

### 00:00:48.840 - 00:00:51.960
Và chúng ta chắc chắn nên tránh điều này.

### 00:00:51.960 - 00:00:56.480
Và do đó, ở đây, chúng ta hãy áp dụng ở đây các cạnh thùng cũng cho bộ kiểm tra.

### 00:00:56.480 - 00:00:58.280
Và chúng ta cần một numpy.

### 00:00:58.280 - 00:01:00.840
Chúng ta có khung dữ liệu thử nghiệm.

### 00:01:00.840 - 00:01:09.159
Và sau đó chúng ta có thể tạo cột bổ sung trả về thùng cho khung dữ liệu thử nghiệm.

### 00:01:09.159 - 00:01:12.519
Và chúng tôi sử dụng ở đây pd.cat.

### 00:01:12.519 - 00:01:18.640
Và chúng tôi chuyển ở đây khung dữ liệu thử nghiệm trả về.

### 00:01:18.640 - 00:01:22.359
Và sau đó, dưới dạng thùng, chúng tôi sử dụng các cạnh thùng giống nhau.

### 00:01:22.359 - 00:01:28.000
Nhưng quan trọng nhất là đối với các quan sát thấp hơn âm 1,3%.

### 00:01:28.000 - 00:01:30.760
Chúng ta nên sử dụng số cạnh của thùng bằng 0.

### 00:01:30.760 - 00:01:35.200
Và đối với các quan sát tốt hơn cộng 1,7%.

### 00:01:35.200 - 00:01:37.960
Chúng ta nên sử dụng sử dụng thùng cạnh số 10.

### 00:01:37.960 - 00:01:45.000
Và do đó, chúng tôi đảm bảo rằng ngay cả khi các quan sát tiến đến âm vô cực hoặc cộng vô cực, chúng ta nên

### 00:01:45.000 - 00:01:50.319
sử dụng thùng bên trái hoặc thùng ngoài cùng bên phải.

### 00:01:50.319 - 00:01:51.920
Vì vậy, đây là cách nó có ý nghĩa.

### 00:01:51.920 - 00:01:58.760
Và chúng ta chỉ cần thêm cột bổ sung vào đây vào khung dữ liệu thử nghiệm.

### 00:01:58.760 - 00:02:05.480
Vì vậy, bây giờ ở bên phải, chúng ta có tính năng trả về dưới dạng thùng hoặc tính năng rời rạc.

### 00:02:05.480 - 00:02:12.840
Và không có gì ngạc nhiên bây giờ trong tập thử nghiệm, kích thước của các thùng không được giống nhau hoặc bằng nhau.

### 00:02:12.840 - 00:02:16.599
Vì vậy, chúng tôi có các kích thước khác nhau.

### 00:02:16.599 - 00:02:22.400
Ngoài ra, dữ liệu của tập thử nghiệm cũng hoạt động hơi khác so với dữ liệu của tập huấn luyện.

### 00:02:22.400 - 00:02:29.599
Vì vậy, các mô hình giá và mô hình trong các chỉ báo kỹ thuật có thể và chúng sẽ thay đổi theo thời gian.

### 00:02:29.599 - 00:02:35.240
Và do đó, chúng tôi không có các ngăn có kích thước bằng nhau ở đây.

### 00:02:35.240 - 00:02:42.359
Và đây là một ví dụ hoặc một lý do tại sao hiệu suất của một tác nhân được đào tạo trên tập thử nghiệm

### 00:02:42.359 - 00:02:46.560
sẽ yếu hơn so với trên tập huấn luyện.

### 00:02:46.599 - 00:02:52.680
Bởi vì tập thử nghiệm tất nhiên không hoàn toàn giống với tập huấn luyện.

### 00:02:52.680 - 00:02:56.759
Vậy có các mẫu khác nhau và quan trọng nhất.

### 00:02:56.759 - 00:03:03.719
Vì vậy, tác nhân cần được đào tạo trên tập huấn luyện để có thể khái quát hóa tập thử nghiệm

### 00:03:03.719 - 00:03:06.400
 và tránh trang bị quá mức.

### 00:03:06.400 - 00:03:09.159
Vì vậy, điều đó quan trọng ở đây.

### 00:03:09.159 - 00:03:15.240
Vì vậy, bây giờ chúng ta đã biết cách tách rời và phân loại một tính năng cho tập huấn luyện và tập kiểm tra

### 00:03:15.240 - 00:03:16.240
set.

### 00:03:16.240 - 00:03:20.240
Và bây giờ trong bước tiếp theo, chúng ta nên thực hiện điều này cho tất cả năm tính năng liên tục trong tập huấn luyện

### 00:03:20.240 - 00:03:22.320
và cả trong tập kiểm tra.

### 00:03:22.320 - 00:03:24.840
Và đó là kế hoạch cho bài giảng tiếp theo.

### 00:03:24.840 - 00:03:27.000
Cảm ơn bạn đã xem và hẹn gặp lại ở đó.

### 00:03:27.000 - 00:03:27.159
Tạm biệt.

