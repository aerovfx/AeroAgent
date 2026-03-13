## Nội dung

### 00:00:00.000 - 00:00:05.759
Bây giờ, hãy bắt đầu từ đây với việc đào tạo tác nhân học tăng cường cho thử thách Luna

### 00:00:05.759 - 00:00:12.200
Lander và khía cạnh quan trọng nhất ở đây là có được không gian quan sát phù hợp

### 00:00:12.200 - 00:00:17.960
 và sự rời rạc phù hợp của không gian quan sát.

### 00:00:17.960 - 00:00:22.839
Vì vậy, hãy nhớ lại rằng chúng ta có tám biến khác nhau trong không gian quan sát.

### 00:00:22.839 - 00:00:28.480
Vì vậy, đây là khá nhiều và điều này sẽ đưa phương pháp Qtables đến giới hạn của nó.

### 00:00:28.480 - 00:00:30.760
Vì vậy, chúng ta sẽ thấy điều này sau.

### 00:00:30.760 - 00:00:37.719
Nhưng trước hết, hãy kiểm tra quan sát ở đây không gian và chúng ta tạo ra môi trường ở đây và

### 00:00:37.719 - 00:00:43.399
sau đó chúng ta có thể có được không gian quan sát với không gian quan sát.

### 00:00:43.399 - 00:00:50.920
Và có vẻ như đối với các giá trị tọa độ x có thể nằm trong khoảng từ âm 90 đến cộng 90.

### 00:00:50.920 - 00:00:57.880
Và bây giờ nếu chúng ta rời rạc hóa tọa độ x dựa trên các giới hạn này thì chúng ta sẽ gặp rắc rối

### 00:00:57.880 - 00:01:03.719
rắc rối vì đây là những giới hạn sai hoặc không thực tế.

### 00:01:03.719 - 00:01:10.840
Vì vậy, có lẽ chúng ta sẽ không đạt tới âm 90 hoặc cộng 90 trong bất kỳ tập phim nào.

### 00:01:10.840 - 00:01:18.800
Vậy giá trị thấp thường quá thấp và giá trị cao quá cao ngoại trừ hai

### 00:01:18.800 - 00:01:19.800
quan sát cuối cùng.

### 00:01:19.800 - 00:01:21.960
Vậy là chân trái và chân phải.

### 00:01:21.959 - 00:01:27.280
Vì vậy, ở đây chúng ta chỉ có các giá trị 0 và 1.

### 00:01:27.280 - 00:01:31.479
Cho đến nay chạm đất và không chạm đất.

### 00:01:31.479 - 00:01:37.280
Và cách viết mã thông minh của chúng ta, chúng ta thực sự có thể thu thập và nhận được các phân phối giá trị thực tế

### 00:01:37.280 - 00:01:39.399
cho không gian quan sát.

### 00:01:39.399 - 00:01:46.919
Ví dụ: đối với tọa độ x và tôi đã sao chép ở đây mã cho nhiều tập

### 00:01:46.920 - 00:01:56.159
với kết xuất RGB và bây giờ chúng ta hãy thử lưu tất cả các trạng thái mà chúng ta tạo ở đây bằng

### 00:01:56.159 - 00:01:58.200
hành động của mình.

### 00:01:58.200 - 00:02:10.840
Vì vậy, chúng ta khởi tạo ở đây các trạng thái danh sách trống và sau đó chúng tôi nối từng trạng thái vào các trạng thái.

### 00:02:10.840 - 00:02:18.719
Và bây giờ hãy chạy chương trình này trong 1.000 tập và tổng cộng chúng tôi có 500 bước mỗi tập.

### 00:02:18.719 - 00:02:23.039
Vì vậy, tổng cộng chúng tôi sẽ có tới 500.000 trạng thái.

### 00:02:23.039 - 00:02:28.800
Vì vậy, điều này là đủ để thực sự phân tích không gian quan sát thực tế.

### 00:02:28.800 - 00:02:35.280
Vì vậy, tất nhiên ở đây chúng tôi có các hành động ngẫu nhiên và có thể một đặc vụ được đào tạo sẽ đạt đến các trạng thái

### 00:02:35.280 - 00:02:38.319
khác với chỉ một tác nhân ngẫu nhiên.

### 00:02:38.319 - 00:02:43.159
Nhưng tôi nghĩ sự khác biệt là không quá đáng kể.

### 00:02:43.159 - 00:02:46.319
Vì vậy chúng ta có thể làm điều này ở đây với tác nhân ngẫu nhiên.

### 00:02:46.319 - 00:02:53.680
Vì vậy, để nói như vậy, hãy thu thập nhiều trạng thái khác nhau và phân tích sự phân bố của các trạng thái.

### 00:02:53.680 - 00:02:58.920
Vậy hãy chạy ở đây 1.000 tập ngẫu nhiên.

### 00:02:59.919 - 00:03:04.679
Chúng ta đã học trước rằng chúng ta có các biến trạng thái sau.

### 00:03:04.679 - 00:03:12.399
Vì vậy, chúng ta có tọa độ x, tọa độ y, vận tốc x, vận tốc y, góc, góc

### 00:03:12.399 - 00:03:16.039
vận tốc và chân trái và chân phải.

### 00:03:16.039 - 00:03:20.479
Vì vậy, hãy lưu cái này vào nhãn.

### 00:03:20.479 - 00:03:30.479
Bây giờ chúng ta thực sự có các trạng thái danh sách chứa rất nhiều trạng thái mảng có nhiều mảng.

### 00:03:30.479 - 00:03:39.719
Vì vậy, hãy kiểm tra độ dài ở đây.

### 00:03:39.719 - 00:03:46.839
Vậy là chúng ta có gần 100.000 trạng thái ở đây được lưu dưới dạng mảng có nhiều mảng.

### 00:03:46.840 - 00:03:48.520
Và bây giờ chúng ta có thể làm như sau.

### 00:03:48.520 - 00:03:51.360
Vì vậy, chúng ta cũng có thể nhập metplot lib.

### 00:03:51.360 - 00:03:59.400
Và sau đó chúng ta có thể lặp qua tất cả các biến và biến đầu tiên chúng ta chuyển đổi trạng thái danh sách thành

### 00:03:59.400 - 00:04:01.159
một mảng có nhiều mảng.

### 00:04:01.159 - 00:04:06.640
Và sau đó chúng ta có biến trạng thái đầu tiên, biến trạng thái thứ hai, biến thứ ba, v.v. on.

### 00:04:06.640 - 00:04:13.159
Và sau đó chúng tôi tạo một biểu đồ có 100 thùng cho tất cả tám biến trạng thái.

### 00:04:13.560 - 00:04:16.600
Và chúng ta cũng đính kèm một tiêu đề.

### 00:04:16.600 - 00:04:21.319
Vì vậy, với nhãn tọa độ x, tọa độ y, v.v.

### 00:04:21.319 - 00:04:27.560
Và bằng cách đó, chúng ta sẽ tìm hiểu thêm về sự phân bố của các trạng thái.

### 00:04:27.560 - 00:04:36.639
Vì vậy, ở đây chúng ta có tọa độ x và chúng ta đã thấy rằng chính thức là các không gian quan sát

### 00:04:36.639 - 00:04:43.839
giữa âm 90 và cộng 90 nhưng trên thực tế, các giá trị nằm trong khoảng từ âm một đến cộng

### 00:04:43.839 - 00:04:46.879
một cho tọa độ x.

### 00:04:46.879 - 00:04:53.919
Sau đó, đối với tọa độ y, chúng ta có các giá trị từ âm 0,5 đến dương hai.

### 00:04:53.919 - 00:04:58.680
Sau đó, chúng ta có vận tốc x giữa âm hai và cộng hai.

### 00:04:58.680 - 00:05:05.240
Và vận tốc y giữa âm hai và cộng 0,5.

### 00:05:05.240 - 00:05:09.040
Và ở đây chúng ta có góc giữa âm hai và cộng hai.

### 00:05:09.040 - 00:05:14.920
Nhưng chúng ta vẫn không nên quên rằng có các ngoại lệ ở đây ở bên trái và bên phải.

### 00:05:14.920 - 00:05:23.480
Vì vậy, nó không phải là nắp hay sàn, mà chỉ là sự phân bố mà hầu hết các giá trị ở đây

### 00:05:23.480 - 00:05:26.879
ví dụ như giữa âm hai và cộng hai.

### 00:05:26.879 - 00:05:28.920
Nhưng vẫn tồn tại các giá trị.

### 00:05:28.920 - 00:05:33.240
Ví dụ: khoảng âm bốn hoặc cộng bốn.

### 00:05:33.240 - 00:05:36.199
Và ở đây cũng là vận tốc góc.

### 00:05:36.199 - 00:05:39.720
Vì vậy, các giá trị thông thường nằm trong khoảng từ âm hai đến cộng hai.

### 00:05:39.720 - 00:05:42.560
Nhưng có các giá trị ngoại lệ ở bên trái và bên phải.

### 00:05:42.560 - 00:05:51.360
Nhưng khi rời rạc hóa biến này ở đây, việc cắt bỏ không thực sự hợp lý,

### 00:05:51.360 - 00:05:55.840
giả sử có 10 hoặc 15 thùng trong phân phối đầy đủ.

### 00:05:55.839 - 00:06:02.959
Vì vậy, ở đây chúng ta nên tập trung vào các giá trị có khả năng xảy ra nhất giữa âm hai và cộng hai.

### 00:06:02.959 - 00:06:06.799
Và nếu không chúng ta sẽ đi vào rắc rối.

### 00:06:06.799 - 00:06:08.359
Và đây là điều không cần bàn cãi ở đây.

### 00:06:08.359 - 00:06:12.000
Vì vậy, đối với chân trái, chúng ta chỉ có các giá trị 0 và 1.

### 00:06:12.000 - 00:06:14.000
Và đối với chân phải.

### 00:06:14.000 - 00:06:17.679
Vì vậy, đây là một phát hiện quan trọng ở đây.

### 00:06:17.679 - 00:06:21.239
Và bây giờ khi nói về số lượng thùng.

### 00:06:21.240 - 00:06:36.000
Vì vậy, nếu bây giờ bạn hỏi trò chuyện GPT hoặc duyệt web thì chúng ta sẽ thấy rằng các giá trị điển hình là 15 thùng cho bốn biến đầu tiên.

### 00:06:36.000 - 00:06:38.079
Vì vậy, đây là những giá trị quan trọng nhất các biến.

### 00:06:38.079 - 00:06:41.639
Vậy tọa độ x và y cũng như vận tốc.

### 00:06:41.639 - 00:06:46.800
Và sau đó, ví dụ 10 thùng cho góc và vận tốc góc.

### 00:06:46.800 - 00:06:53.439
Và cuối cùng, tất nhiên là hai thùng cho chân trái và chân phải.

### 00:06:53.439 - 00:06:56.360
Vì vậy, đây có thể là điểm khởi đầu tốt ở đây.

### 00:06:56.360 - 00:07:00.000
Và điều này sẽ tạo ra một bảng xếp hàng khá lớn.

### 00:07:00.000 - 00:07:01.439
Vì vậy, chúng ta sẽ thấy điều này.

### 00:07:01.439 - 00:07:04.120
Vì vậy, hãy tạo một số thùng.

### 00:07:04.120 - 00:07:06.920
Và sau đó chúng ta phải xác định dịch vụ không gian quan sát,

### 00:07:06.920 - 00:07:08.920
np.lin space.

### 00:07:08.920 - 00:07:12.120
Vậy chúng ta đã thấy cho x phối hợp.

### 00:07:12.120 - 00:07:16.319
Chúng ta chỉ nên tính đến các giá trị trong khoảng từ âm 1 đến 1.

### 00:07:16.319 - 00:07:21.360
Sau đó chia phần này thành 15 thùng.

### 00:07:21.360 - 00:07:27.519
Và chúng ta sẽ làm tương tự với tọa độ y, v.v.

### 00:07:27.519 - 00:07:34.959
Vì vậy, dựa vào điều này, chúng ta có thể tạo một bảng hàng đợi và bảng hàng đợi ban đầu với các giá trị ngẫu nhiên.

### 00:07:34.959 - 00:07:38.000
Bằng cách chuyển vào đây số lượng thùng và không gian hành động.

### 00:07:38.000 - 00:07:40.840
Vì vậy, chúng ta có bốn hành động khác nhau.

### 00:07:40.839 - 00:07:45.239
Và điều này sẽ cung cấp cho chúng ta một bảng hàng đợi có hình dạng như sau.

### 00:07:45.239 - 00:07:47.639
Vậy là chúng ta có chín chiều.

### 00:07:47.639 - 00:07:54.120
Và các kích thước chiều là 15, 15, 15, 10, 10, 22 và 4.

### 00:07:54.120 - 00:07:59.919
Và điều này sẽ cung cấp cho chúng ta số cặp hành động trạng thái sau.

### 00:07:59.919 - 00:08:06.079
Vậy 81 triệu cặp hành động trạng thái, là một bảng hàng đợi khá lớn.

### 00:08:06.079 - 00:08:08.239
Và về mặt bộ nhớ,

### 00:08:08.280 - 00:08:11.160
cái này vẫn sẽ ở dưới một gigabyte.

### 00:08:11.160 - 00:08:16.000
Vì vậy, tôi nghĩ nó nằm trong khoảng từ 600 đến 700 megabyte.

### 00:08:16.000 - 00:08:18.560
Và cái này đã khá lớn rồi.

### 00:08:18.560 - 00:08:25.639
Vì vậy, chúng ta nên bắt đầu làm việc với một bảng xếp hàng như thế này ở đây.

### 00:08:25.639 - 00:08:28.160
Và chúng ta sẽ tiếp tục ở đây trong bài giảng tiếp theo.

### 00:08:28.160 - 00:08:30.360
Cảm ơn bạn đã xem và hẹn gặp lại bạn ở đó.

### 00:08:30.360 - 00:08:31.519
Tạm biệt.

