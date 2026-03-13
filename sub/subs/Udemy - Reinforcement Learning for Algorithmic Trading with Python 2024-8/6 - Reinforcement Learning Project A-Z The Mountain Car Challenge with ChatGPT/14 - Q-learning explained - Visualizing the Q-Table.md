## Nội dung

### 00:00:00.000 - 00:00:04.799
Trong bài giảng trước, chúng ta đã biết rằng bảng hàng đợi chứa tất cả các cặp hành động trạng thái

### 00:00:04.799 - 00:00:10.359
 và các ngôi sao, do đó, phần thưởng tích lũy dự kiến trong tương lai cho mỗi cặp hành động trạng thái.

### 00:00:10.359 - 00:00:21.080
Vì vậy, trong trường hợp của chúng ta, chúng ta có tổng cộng 18 lần 14 trạng thái và 756 cặp hành động trạng thái.

### 00:00:21.080 - 00:00:27.800
Và bằng cách cập nhật không gian giá trị hàng đợi trên các trải nghiệm, tác nhân tìm hiểu chính sách tối ưu

### 00:00:27.800 - 00:00:31.519
chỉ định hành động tốt nhất nên thực hiện ở mỗi trạng thái.

### 00:00:31.519 - 00:00:37.280
Và chúng ta đã biết rằng trong thử thách thẻ núi, chúng ta bắt đầu với một bảng hàng đợi

### 00:00:37.280 - 00:00:40.079
với các giá trị ngẫu nhiên nhỏ.

### 00:00:40.079 - 00:00:46.760
Vì vậy, lấy từ sự phân bố đồng đều giữa trừ một và cộng một, và chúng ta cũng có thể

### 00:00:46.760 - 00:00:49.000
hình dung ở đây tính ngẫu nhiên.

### 00:00:49.000 - 00:00:56.120
Vì vậy, đây là bảng có nhiều số, nhưng thông thường, một biểu đồ hình ảnh cho biết

### 00:00:56.119 - 00:01:00.919
nhiều hơn hàng trăm hoặc hàng nghìn số.

### 00:01:00.919 - 00:01:05.759
Vì vậy, để hiểu đầy đủ về bảng hàng đợi, việc hình dung bảng hàng đợi chắc chắn rất hữu ích.

### 00:01:05.759 - 00:01:12.280
Ví dụ: trong bản đồ nhiệt và so sánh bản đồ nhiệt trước và sau đào tạo.

### 00:01:12.280 - 00:01:15.959
Và do đó chúng ta có thể tiếp tục với lời nhắc sau.

### 00:01:15.959 - 00:01:20.959
Vì vậy, hãy hình dung bảng hàng đợi trong bản đồ nhiệt dựa trên mã hiện có.

### 00:01:20.959 - 00:01:27.559
Vì vậy, bạn là mã và hãy đợi đề xuất ở đây.

### 00:01:27.559 - 00:01:32.559
Vì vậy, để trực quan hóa bảng hàng đợi bằng bản đồ nhiệt, chúng ta cần tập trung vào một hành động trạng thái cụ thể

### 00:01:32.559 - 00:01:35.199
biểu diễn cặp.

### 00:01:35.199 - 00:01:41.239
Và vì bảng hàng đợi có ba chiều, chúng ta sẽ đơn giản hóa việc hiển thị bằng cách chọn

### 00:01:41.239 - 00:01:46.599
một hành động cố định hoặc tổng hợp các giá trị hàng đợi theo các hành động.

### 00:01:46.599 - 00:01:54.719
Vì vậy, tùy chọn thú vị nhất và hữu ích nhất sẽ là thực sự hiển thị hành động tốt nhất.

### 00:01:54.719 - 00:01:59.039
Bây giờ chúng ta hãy kiểm tra mã ở đây và nó không sử dụng cốt truyện. và cả seaborn.

### 00:01:59.039 - 00:02:01.759
Vì vậy, có lẽ chúng ta cũng có thể làm điều này mà không cần seaborn.

### 00:02:01.759 - 00:02:06.959
Vì vậy, vì chúng ta phải cài đặt seaborn riêng.

### 00:02:06.959 - 00:02:12.639
Và ở đây chúng ta thực sự có sự trực quan hóa để tổng hợp các giá trị hàng đợi qua các hành động.

### 00:02:12.639 - 00:02:18.919
Vì vậy, giá trị hàng đợi trung bình, có thể không phải là tùy chọn thú vị nhất ở đây.

### 00:02:18.919 - 00:02:24.199
Vì vậy, chúng ta nên thực hiện hành động tốt nhất, hiện tại là hành động tốt nhất, ban đầu được chọn ngẫu nhiên

### 00:02:24.199 - 00:02:29.079
vì chúng ta có các giá trị ngẫu nhiên trong bảng hàng đợi.

### 00:02:29.079 - 00:02:33.599
Vì vậy, có thể hợp lý khi sử dụng hành động tốt nhất hiện tại là hành động tốt nhất, ban đầu được chọn ngẫu nhiên

### 00:02:33.599 - 00:02:37.959
vì chúng ta có các giá trị ngẫu nhiên trong bảng xếp hàng.

### 00:02:37.960 - 00:02:39.800
Vì vậy, có thể hợp lý khi sử dụng hành động tốt nhất hiện tại là hành động tốt nhất, ban đầu là ngẫu nhiên

### 00:02:39.800 - 00:02:44.960
được chọn vì chúng ta có các giá trị ngẫu nhiên trong bảng xếp hàng. theo lời nhắc.

### 00:02:44.960 - 00:02:53.680
Và chúng ta có thể nói ở đây như sau để bản đồ nhiệt sẽ hiển thị thông qua màu sắc tốt nhất

### 00:02:53.680 - 00:02:58.760
hành động cho từng trạng thái.

### 00:02:58.760 - 00:03:02.680
Vui lòng tạo một bản đồ nhiệt không có seaborn nếu có thể.

### 00:03:02.680 - 00:03:11.920
Và bây giờ không còn seaborn nữa ở đây trong mã của chúng ta.

### 00:03:11.920 - 00:03:13.560
Và hãy xem liệu tbd4 có làm đúng không.

### 00:03:13.560 - 00:03:17.879
Vì vậy, hãy chọn hành động tốt nhất và hình dung ra hành động tốt nhất.

### 00:03:17.879 - 00:03:23.120
Vì vậy, hoặc là 0 cho việc đi sang trái một là không làm gì và hai tăng tốc sang phải.

### 00:03:23.120 - 00:03:26.480
Bây giờ chúng ta hãy kiểm tra mã ở đây một lần nữa.

### 00:03:26.479 - 00:03:33.120
Vì vậy, dưới đây là mã cập nhật để tạo nhiệt bản đồ hiển thị hành động tốt nhất cho mỗi trạng thái

### 00:03:33.120 - 00:03:40.039
 chỉ sử dụng cốt truyện đó.

### 00:03:40.039 - 00:03:45.039
Và ở đây bên dưới, chúng ta có thể tìm thấy bảng hành động tốt nhất.

### 00:03:45.039 - 00:03:51.519
Vì vậy, với np.artmax, nó thực sự chọn hành động tốt nhất cho mỗi trạng thái cho mỗi trạng thái.

### 00:03:51.520 - 00:04:02.800
Và sau đó nó trực quan hóa hành động tốt nhất.

### 00:04:02.800 - 00:04:07.040
Vì vậy, bằng cách sử dụng cốt truyện đó và hàm imso.

### 00:04:07.040 - 00:04:16.199
Và thanh màu biểu thị hành động tốt nhất cho mỗi trạng thái cung cấp một biểu diễn trực quan rõ ràng.

### 00:04:16.199 - 00:04:22.959
Vì vậy, trước tiên chúng ta cần nhập metplotlib để có thể sao chép điều này ở đây.

### 00:04:22.959 - 00:04:31.719
Và sau đó chúng ta có thể sử dụng mã bên dưới.

### 00:04:31.719 - 00:04:33.599
Vì vậy, trước hết hãy tìm bảng hành động tốt nhất.

### 00:04:33.599 - 00:04:38.759
Đây là bảng và chúng ta có hình dạng sau đây.

### 00:04:38.759 - 00:04:44.360
Vậy 18, 14, vậy trên trục x chúng ta có 18 giá trị và trên trục y 14 giá trị cho vị trí x

### 00:04:44.360 - 00:04:50.740
và vận tốc.

### 00:04:50.740 - 00:04:56.000
Và khi đó các con số đơn giản là những hành động tốt nhất hiện có trong bảng q ngẫu nhiên của chúng ta.

### 00:04:56.000 - 00:05:01.759
Vì vậy, số 0 để tăng tốc sang trái và hai để tăng tốc ở bên phải.

### 00:05:01.759 - 00:05:03.840
Và tốt nhất là hình dung điều này ở đây.

### 00:05:03.840 - 00:05:10.199
Vì vậy, đây là bảng q ngẫu nhiên và nó trông ngẫu nhiên.

### 00:05:10.199 - 00:05:17.599
Vì vậy, chúng ta có ở đây các thùng vận tốc, các thùng gấp trên trục x và các thùng vị trí

### 00:05:17.599 - 00:05:19.839
trên trục y.

### 00:05:19.839 - 00:05:28.800
Và ở đây chúng ta có các số 0 màu tím nên điều này có nghĩa là tăng tốc sang trái.

### 00:05:28.800 - 00:05:30.279
Sau đó, chúng ta có một lần màu xanh lá cây không làm gì cả và màu vàng tăng tốc sang phải và

### 00:05:30.279 - 00:05:32.719
thực tế không có mô hình nào đây.

### 00:05:32.719 - 00:05:39.839
Đó chỉ là một hành động ngẫu nhiên trong bảng q và tôi nghi ngờ rằng việc huấn luyện sẽ thay đổi

### 00:05:39.839 - 00:05:46.759
hình ảnh ở đây.

### 00:05:46.759 - 00:05:55.439
Vì vậy, chúng ta sẽ thấy một số mẫu.

### 00:05:55.439 - 00:06:02.399
Và bây giờ chúng ta hãy quay lại đây với phần đào tạo ban đầu của chúng ta.

### 00:06:02.399 - 00:06:08.159
Vì vậy, với 2000 tập, hãy chạy phần đào tạo ở đây một lần nữa.

### 00:06:08.160 - 00:06:13.080
Và sau đó hãy hình dung bảng q đã được huấn luyện và tôi đoán chúng ta sẽ thấy một số mẫu.

### 00:06:13.080 - 00:06:14.580
Vậy là chúng ta có tỷ lệ thành công ở đây là 88%.

### 00:06:14.580 - 00:06:22.680
Bây giờ hãy hình dung bảng q một lần nữa.

### 00:06:22.680 - 00:06:29.000
Vì vậy, đây có thể không phải là hoàn hảo và bảng q tốt nhất, nhưng vẫn có một số nội dung đào tạo

### 00:06:29.000 - 00:06:32.320
bao gồm.

### 00:06:32.320 - 00:06:35.560
Vì vậy, nó có thể lên tới đỉnh núi trong khoảng 100 bước.

### 00:06:35.560 - 00:06:40.480
Và ở đây chúng ta có thể thấy một số mô hình và khu vực nơi tốt hơn là nên tăng tốc sang bên trái

### 00:06:40.480 - 00:06:46.660
và các khu vực khác mà tăng tốc sang bên phải sẽ tốt hơn.

### 00:06:46.660 - 00:06:49.199
Nhưng vẫn có rất nhiều sự ngẫu nhiên.

### 00:06:49.199 - 00:06:51.439
Và tất nhiên, chúng ta có thể cải thiện hơn nữa việc đào tạo đặc vụ.

### 00:06:51.439 - 00:06:51.639
Vì vậy, có một số cấp độ và các biện pháp sẽ giúp chúng tôi cải thiện hơn nữa việc đào tạo

