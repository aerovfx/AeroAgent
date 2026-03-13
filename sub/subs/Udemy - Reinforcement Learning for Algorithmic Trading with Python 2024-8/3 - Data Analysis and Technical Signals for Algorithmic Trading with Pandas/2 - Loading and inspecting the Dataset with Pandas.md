## Nội dung

### 00:00:00.000 - 00:00:06.839
Bây giờ, hãy bắt đầu ở đây với dữ liệu tài chính và tín hiệu kỹ thuật, Jupyter Notebook.

### 00:00:06.839 - 00:00:11.560
Và trước hết hãy tải và kiểm tra tập dữ liệu được lưu trữ ở đây trong tệp CSV

### 00:00:11.560 - 00:00:14.200
findata.csv.

### 00:00:14.200 - 00:00:20.320
Và đối với bài giảng này và các bài giảng tiếp theo, chúng ta sẽ cần pandas và cả madplotlib để trực quan hóa

### 00:00:20.320 - 00:00:22.120
tập dữ liệu.

### 00:00:22.120 - 00:00:29.000
Và sau đó chúng ta có thể đọc tệp CSV thành gấu trúc với pandas.reads.csv.

### 00:00:29.000 - 00:00:34.840
Và chúng ta phải chỉ định ở đây tên tệp của findata.csv.

### 00:00:34.840 - 00:00:41.880
Và chúng tôi muốn đảm bảo rằng chỉ mục của khung dữ liệu của chúng tôi là cột ngày giờ.

### 00:00:41.880 - 00:00:44.840
Vì vậy, hãy tạo ở đây khung dữ liệu df.

### 00:00:44.840 - 00:00:48.039
Và ở đây ở phía bên trái chúng tôi có chỉ mục.

### 00:00:48.039 - 00:00:56.920
Vì vậy, đây là dữ liệu hàng giờ từ tháng 9 năm 2022 và tháng 7 năm 2024.

### 00:00:56.920 - 00:01:02.800
Và ở đây chúng tôi có dữ liệu hàng giờ bắt đầu vào buổi sáng lúc 8 giờ 9, 10, v.v. trên.

### 00:01:02.800 - 00:01:08.760
Và tất nhiên đây chỉ là giờ giao dịch của công cụ tài chính của chúng tôi.

### 00:01:08.760 - 00:01:12.439
Vì vậy, đó là đồng euro của người đóng thuế.

### 00:01:12.439 - 00:01:16.400
Vì vậy, đó là giá của một euro của bạn bằng đô la Mỹ.

### 00:01:16.400 - 00:01:24.760
Vì vậy, ví dụ ở đây vào ngày 29 tháng 7 năm 2024, nó là 1,082603.

### 00:01:24.760 - 00:01:27.600
Ồ, đô la Mỹ trên một euro.

### 00:01:27.600 - 00:01:33.640
Vì vậy, đây là cách bạn có thể hiểu ở đây về cặp tiền tệ.

### 00:01:33.640 - 00:01:38.640
Vì vậy, ở phía bên trái, chúng ta có cột ngày giờ làm chỉ mục.

### 00:01:38.640 - 00:01:40.920
Và sau đó chúng ta có một vài cột.

### 00:01:40.920 - 00:01:45.600
Vì vậy, chúng ta có giá mở cửa cao thấp, đóng cửa và không có gì ngạc nhiên.

### 00:01:45.600 - 00:01:52.760
Vì vậy, giá mở cửa cho giá ở đầu giá thanh giờ.

### 00:01:52.760 - 00:01:57.000
Vậy là bắt đầu.

### 00:01:57.000 - 00:02:04.080
Và sau đó chúng ta có giá cao nhất trong thanh một giờ, giá thấp nhất và cũng là giá đóng cuối cùng.

### 00:02:04.080 - 00:02:09.920
Vì vậy, đây là ví dụ: thanh bắt đầu lúc 8 giờ và đây là giá mở cửa lúc 8 giờ.

### 00:02:09.920 - 00:02:19.360
Sau đó, chúng ta có giá đóng cửa lúc 9 giờ, sau đó là giá cao nhất và giá thấp nhất trong khoảng thời gian một giờ này.

### 00:02:19.360 - 00:02:25.680
Và sau đó chúng ta cũng có ở đây giá đóng cửa đã điều chỉnh mà chúng ta có thể bỏ qua và cả khối lượng giao dịch. là.

### 00:02:25.680 - 00:02:34.440
Tôi nghĩ nó không đúng nhưng nguồn dữ liệu của chúng ta ở đây nên Yahoo Finance đã giảm một lượng bằng 0.

### 00:02:34.440 - 00:02:39.160
Và sau đó ở bên phải đây chúng ta có một số chỉ báo và tín hiệu kỹ thuật.

### 00:02:39.160 - 00:02:42.320
Và trong bài giảng tiếp theo, tôi thấy chúng ta sẽ đi sâu vào chi tiết hơn.

### 00:02:42.359 - 00:02:53.759
Vì vậy, đối với tỷ lệ SMA, biểu đồ MACD và RSI cũng như sự khác biệt của chỉ báo dao động yếu như thế nào.

### 00:02:53.759 - 00:02:57.159
Và cũng có kết quả trả về đơn giản.

### 00:02:57.159 - 00:03:02.240
Vì vậy, tôi sẽ giải thích điều này sau trong một số bài giảng tiếp theo.

### 00:03:02.240 - 00:03:06.159
Nhưng bây giờ, hãy lấy một số thông tin đa phương tiện trên khung dữ liệu.

### 00:03:06.159 - 00:03:09.879
Vì vậy, phương pháp thông tin là một trong những phương pháp quan trọng nhất.

### 00:03:09.919 - 00:03:12.799
Và ở đây chúng ta có thể kiểm tra một số thông tin đa phương tiện.

### 00:03:12.799 - 00:03:19.240
Vì vậy, ví dụ ở đây chúng ta có tất cả các cột, số lượng giá trị bị thiếu là không thiếu giá trị.

### 00:03:19.240 - 00:03:25.079
Vậy rõ ràng là chúng ta có 11.619 hàng.

### 00:03:25.079 - 00:03:29.599
Vậy là 11.619 giờ.

### 00:03:29.599 - 00:03:32.599
Và có vẻ như chúng ta không thiếu giá trị nào.

### 00:03:32.599 - 00:03:39.759
Sau đó, ở bên phải, chúng ta có thể tìm thấy kiểu dữ liệu và chúng ta có số float ngoại trừ khối lượng mà chúng ta có.

### 00:03:39.759 - 00:03:44.359
Số nguyên nhưng dù sao thì các giá trị ở đây vẫn bằng 0.

### 00:03:44.359 - 00:03:47.079
Và sau đó chúng ta có thêm một số thông tin về chỉ mục.

### 00:03:47.079 - 00:03:52.280
Vì vậy, nó chỉ là một chỉ mục có các giá trị chuỗi.

### 00:03:52.280 - 00:03:57.479
Và việc có chỉ số ban ngày thực sự là điều mong muốn và hữu ích hơn.

### 00:03:57.479 - 00:04:03.879
Vì vậy, hiện tại đây là các chuỗi và chúng ta nên chuyển đổi chỉ mục ở đây thành chỉ mục ban ngày.

### 00:04:03.919 - 00:04:08.280
Và chúng ta có thể làm điều này ở đây với pandas thành ban ngày.

### 00:04:08.280 - 00:04:12.879
Và chúng ta ghi đè chỉ mục ở đây và bây giờ chúng ta có chỉ mục ban ngày ở đây.

### 00:04:12.879 - 00:04:26.360
Vì vậy, bắt đầu từ 8 giờ sáng ngày 13 tháng 9 năm 2022 cho đến 10 giờ tối ngày 29 tháng 7 năm 2024.

### 00:04:26.360 - 00:04:33.639
Và sau đó chúng ta có thể chỉ cần chọn các cột cũng là các hàng có logaccessor.

### 00:04:33.680 - 00:04:35.560
Vì vậy, chúng ta cần đặt dấu ngoặc vuông.

### 00:04:35.560 - 00:04:43.479
Và ví dụ: chúng ta chỉ có thể chọn dấu thời gian trong tháng 3 năm 2024 và chỉ cột đóng.

### 00:04:43.479 - 00:04:51.399
Vì vậy, ở đây chúng ta có giá đóng cửa từ ngày đầu tiên của tháng 3 cho đến ngày 31.

### 00:04:51.399 - 00:04:57.120
Đây là chuỗi gấu trúc có một chỉ mục và một cột.

### 00:04:57.120 - 00:05:02.639
Và cuối cùng, chúng ta có thể nhận được một số thống kê tóm tắt hơn, chẳng hạn như các cột số.

### 00:05:02.639 - 00:05:04.959
Vậy là phương pháp được mô tả.

### 00:05:04.959 - 00:05:08.319
Vì vậy, chúng ta có số giá trị không thiếu.

### 00:05:08.319 - 00:05:12.360
Sau đó, chúng ta có giá trị trung bình, giá trị tối thiểu.

### 00:05:12.360 - 00:05:19.159
Vậy giá thấp nhất là 0,95 và giá cao nhất là 1,12.

### 00:05:19.159 - 00:05:25.079
Và ví dụ: trung vị và người thứ 25 Thái Lan, v.v.

### 00:05:25.079 - 00:05:27.399
Vậy đây là độ lệch chuẩn.

### 00:05:27.399 - 00:05:30.199
Vì vậy, đây là lần kiểm tra dữ liệu đầu tiên.

### 00:05:30.199 - 00:05:38.479
Vì vậy, ở đây chúng ta có một bộ dữ liệu chứa dữ liệu giá hàng giờ cho cặp Forex euro đô la Mỹ,

### 00:05:38.479 - 00:05:43.439
bao gồm một số chỉ báo kỹ thuật hoặc một số tín hiệu kỹ thuật.

### 00:05:43.439 - 00:05:46.279
Và chúng ta sẽ tiếp tục ở đây trong bài giảng tiếp theo.

### 00:05:46.279 - 00:05:48.279
Cảm ơn bạn đã xem và hẹn gặp lại bạn ở đó.

### 00:05:48.279 - 00:05:49.279
Tạm biệt.

