## Nội dung

### 00:00:00.000 - 00:00:05.759
Được rồi, chúng ta sắp đến bước cuối cùng và có lẽ là bước hứa hẹn nhất, tăng khả năng rời rạc hóa không gian trạng thái

### 00:00:05.759 - 00:00:08.359
.

### 00:00:08.359 - 00:00:14.140
Vì vậy, hãy tăng độ chi tiết của các thùng và cho đến nay chúng ta đã làm việc với 18 thùng cho tham số vị trí

### 00:00:14.140 - 00:00:19.559
x và 14 thùng cho tham số vận tốc.

### 00:00:19.559 - 00:00:25.640
Và giờ đây, việc tăng số lượng thùng có thể cung cấp biểu diễn chi tiết hơn về không gian trạng thái

### 00:00:25.640 - 00:00:33.399
, do đó có khả năng dẫn đến các giá trị Q chính xác hơn và hiệu suất thậm chí còn tốt hơn của 

### 00:00:33.399 - 00:00:36.120
được đào tạo tác nhân học tăng cường.

### 00:00:36.120 - 00:00:44.760
Tuy nhiên, điều này cũng sẽ làm tăng kích thước của bảng Q và do đó điều này dẫn đến nhu cầu

### 00:00:44.760 - 00:00:47.320
 cao hơn về tài nguyên tính toán.

### 00:00:47.320 - 00:00:53.040
Vì vậy, có sự cân bằng rõ ràng giữa cách trình bày chi tiết hơn và độ chính xác cao hơn

### 00:00:53.039 - 00:01:00.000
 và tài nguyên tính toán cao hơn nên sẽ có nhiều tài nguyên cần thiết hơn ở đây.

### 00:01:00.000 - 00:01:05.680
Và tôi nói quy tắc chung là hãy tăng số lượng cặp hành động trạng thái theo hệ số

### 00:01:05.680 - 00:01:06.680
x.

### 00:01:06.680 - 00:01:13.239
Vì vậy, ví dụ, đối với yêu cầu tăng các giai đoạn đào tạo theo cùng một hệ số cho đến nay

### 00:01:13.239 - 00:01:15.120
chẳng hạn.

### 00:01:15.120 - 00:01:16.840
Và để tôi cho bạn một ví dụ ở đây.

### 00:01:16.840 - 00:01:27.180
Vì vậy, tôi đã tăng số lượng thùng từ 18 14 lên 180 nên 100 thùng cho tham số vị trí

### 00:01:27.180 - 00:01:32.680
 và 80 thùng cho tham số vận tốc.

### 00:01:32.680 - 00:01:38.159
Và do đó cần phải tăng số tập.

### 00:01:38.159 - 00:01:45.280
Và ví dụ: chúng ta có thể sử dụng CS6000, việc này cần một chút thời gian để huấn luyện.

### 00:01:45.280 - 00:01:54.879
Vì vậy, tùy thuộc vào sức mạnh của thiết bị của bạn và tôi đã tối ưu hóa ở đây một số thông số Q learning

### 00:01:54.879 - 00:01:55.879
.

### 00:01:55.879 - 00:02:05.319
Vì vậy, chúng tôi có hệ số alpha là 0,35 và tôi cũng tăng độ phân rã epsilon lên 99,95%.

### 00:02:05.319 - 00:02:12.000
Vì vậy, điều này sẽ dẫn đến sự phân rã chậm hơn vì chúng tôi có nhiều tập hơn.

### 00:02:12.000 - 00:02:18.960
Vì vậy, đây là những thay đổi lớn và chúng tôi vẫn đang sử dụng ở đây chiến lược phân rã epsilon mới thích ứng hơn

### 00:02:18.960 - 00:02:20.919
Và chúng tôi đang chạy ở đây hai phần nghiêm túc, mỗi phần có 30.000 tập.

### 00:02:20.919 - 00:02:29.240
Vì vậy, chúng tôi bắt đầu với phần đầu tiên epsilon là 0,9 và sau 30.000 tập, chúng tôi bắt đầu mới

### 00:02:29.240 - 00:02:38.159
với epsilon ban đầu là 0,9.

### 00:02:38.159 - 00:02:44.319
Vì vậy, điều này sẽ cho phép đặc vụ khám phá nhiều chiến lược hơn và nhiều mầm bệnh hơn để thực sự tiếp cận

### 00:02:44.319 - 00:02:51.120
mục tiêu với các bước cuối cùng.

### 00:02:51.120 - 00:02:56.719
Và bây giờ hãy chạy mã ở đây.

### 00:02:56.719 - 00:03:01.479
Và quá trình này rất có thể sẽ mất vài phút.

### 00:03:01.479 - 00:03:06.599
Và bây giờ chúng ta có ở đây 1000 tập đầu tiên.

### 00:03:06.599 - 00:03:10.799
Vì vậy, chúng ta đang in tập 1000, 2000, 3000, v.v.

### 00:03:10.799 - 00:03:15.879
Và hãy đợi cho đến khi chúng ta đạt được 6000 tập.

### 00:03:15.879 - 00:03:20.759
Được rồi, chúng ta đã đạt được 6000 tập huấn luyện các tập và tỷ lệ thành công là 96,94% và

### 00:03:20.759 - 00:03:29.959
tổng phần thưởng trung bình là 157.

### 00:03:29.960 - 00:03:34.439
Và bây giờ hãy chạy 2000 tập thử nghiệm.

### 00:03:34.439 - 00:03:39.280
Vì vậy, vẫn với chỗ ngồi ngẫu nhiên 100.

### 00:03:39.280 - 00:03:46.480
Vì vậy, việc này sẽ không mất quá nhiều thời gian ở đây.

### 00:03:46.480 - 00:03:49.920
Và bây giờ chúng ta có tỷ lệ thành công của anh ấy là 100 và tổng phần thưởng trung bình khá thấp.

### 00:03:49.920 - 00:03:56.600
Vì vậy, trung bình chúng ta lên đến đỉnh núi trong 103 bước và tập hay nhất là 85

### 00:03:56.599 - 00:04:04.919
và tệ nhất là 143.

### 00:04:04.919 - 00:04:08.120
Vì vậy đây là một đặc vụ khá có năng lực ở đây cho thử thách thẻ leo núi của chúng ta.

### 00:04:08.120 - 00:04:14.039
Và ở đây cũng rất hợp lý khi tạo ra một số âm mưu.

### 00:04:14.039 - 00:04:18.240
Vì vậy, hãy hình dung phần thưởng đào tạo theo thời gian.

### 00:04:18.240 - 00:04:22.279
Và ở đây chúng ta có thể thấy hai loạt phim.

### 00:04:22.279 - 00:04:24.559
Vậy tổng cộng chúng ta có 60.000 tập.

### 00:04:24.559 - 00:04:28.559
Và chúng ta có thể thấy ở đây sự cải thiện mạnh mẽ của đặc vụ trong vòng đầu tiên khoảng 15 hoặc

### 00:04:28.559 - 00:04:35.959
20.000 tập.

### 00:04:35.959 - 00:04:37.799
Và sau đó chúng tôi bắt đầu mới với epsilon là 0,9.

### 00:04:37.799 - 00:04:43.239
Và ví dụ, như bạn có thể thấy ở đây, vì vậy ở đây chúng ta đạt đến trạng thái ổn định về hiệu suất và sau đó đột nhiên

### 00:04:43.239 - 00:04:49.919
chúng ta thực sự có thể tiến lên và có thể xảy ra trường hợp đó một lần nữa, chúng ta có thể tiến lên đây với

### 00:04:49.920 - 00:04:58.040
nhiều tập hơn.

### 00:04:58.040 - 00:04:59.720
Vì vậy, đây không phải là sự kết thúc của quá trình tối ưu hóa.

### 00:04:59.720 - 00:05:03.360
Nó có thể chỉ là sự khởi đầu.

### 00:05:03.360 - 00:05:06.480
Tiếp theo, chúng ta cũng có thể hình dung bảng xếp hàng bằng một bản đồ nhiệt.

### 00:05:06.480 - 00:05:10.160
Vì vậy, một bản đồ nhiệt chi tiết hơn ở đây.

### 00:05:10.160 - 00:05:13.800
Và ở đây chúng ta có thể thấy rõ một số mẫu.

### 00:05:13.800 - 00:05:16.319
Vì vậy, trên trục x, chúng ta có các thùng vận tốc và trên trục y, các thùng vị trí và 

### 00:05:16.319 - 00:05:23.399
 màu vàng có nghĩa là tăng tốc về bên phải.

### 00:05:23.399 - 00:05:26.560
Và màu xanh đậm hoặc màu tím có nghĩa là tăng tốc về bên trái.

### 00:05:26.560 - 00:05:33.560
Vì vậy, có các mẫu rõ ràng nhưng nó vẫn không tối ưu.

### 00:05:33.560 - 00:05:37.439
Vì vậy, chúng tôi có thể tinh chỉnh thêm ở đây vatigee này và bảng hàng đợi.

### 00:05:37.439 - 00:05:43.560
Và ở đây, tại giới hạn, bạn có thể thấy các vị trí mà rất có thể chúng tôi sẽ không bao giờ đạt tới và do đó

### 00:05:43.560 - 00:05:51.680
chúng tôi không thể xác định ở đây a vatigee.

### 00:05:51.680 - 00:05:57.000
Vì vậy, bản đồ nhiệt ở đây cũng là một chỉ số rõ ràng rằng chúng tôi đã tạo và đào tạo một đặc vụ khá giỏi

### 00:05:57.000 - 00:06:03.920
và cuối cùng nhưng không kém phần quan trọng.

### 00:06:03.920 - 00:06:07.720
Hãy hình dung lại có thể năm hoặc mười tập thử nghiệm với đặc vụ đã được đào tạo.

### 00:06:07.720 - 00:06:18.360
Vì vậy, chúng ta cần xác định ở đây chế độ ngẫu nhiên.

### 00:06:18.360 - 00:06:24.880
Và nó phải là con người.

### 00:06:24.880 - 00:06:28.320
Vì vậy, hãy chạy ở đây và chúng ta cũng có thể xác định rằng chúng ta muốn in kết quả cho mỗi

### 00:06:28.320 - 00:06:34.680
và mọi tập.

### 00:06:34.680 - 00:06:38.600
Vì vậy, hãy chạy ở đây.

### 00:06:38.600 - 00:06:42.480
Và đây là phần trình bày bằng đồ họa.

### 00:06:42.480 - 00:06:47.519
Vì vậy, nó khá nhanh ở đây.

### 00:06:47.519 - 00:06:50.759
Ví dụ: 87 bước 143.

### 00:06:50.759 - 00:06:54.759
187.

### 00:06:54.759 - 00:07:01.759
188.

### 00:07:01.759 - 00:07:06.759
92.

### 00:07:06.759 - 00:07:10.759
94.

### 00:07:10.759 - 00:07:14.759
Và 133.

### 00:07:14.759 - 00:07:20.680
Vì vậy, đây hiện là một tác nhân học tập củng cố khá tốt cho thử thách xe leo núi.

### 00:07:20.680 - 00:07:25.639
Cảm ơn bạn đã xem và mong được gặp bạn trong bài giảng tiếp theo.

### 00:07:25.639 - 00:07:29.600
Tạm biệt.

### 00:07:29.600 - 00:07:29.800
Bye.

