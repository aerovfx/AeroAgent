## Nội dung

### 00:00:00.000 - 00:00:06.120
Được rồi, trong bài giảng trước, chúng tôi đã đào tạo đặc vụ của mình với 5.000 tập và hiệu suất

### 00:00:06.120 - 00:00:14.599
 trên tập huấn luyện khá ấn tượng. Vậy đây là phần trả về hay hồ sơ phần thưởng

### 00:00:14.599 - 00:00:22.760
 của tập cuối. Tuy nhiên, hiệu suất của tác nhân trên

### 00:00:22.760 - 00:00:28.600
tập huấn luyện không nhất thiết giống như trên tập kiểm tra và chúng tôi có thể

### 00:00:28.600 - 00:00:36.039
nghi ngờ rằng ở đây có hiện tượng trang bị quá mức và chúng tôi phải kiểm tra điều này và chúng tôi chỉ có thể

### 00:00:36.039 - 00:00:42.560
 kiểm tra điều này bằng cách thực sự kiểm tra tác nhân. Vì vậy, việc kiểm tra tác nhân được đào tạo trên

### 00:00:42.560 - 00:00:50.400
bộ kiểm tra và do đó hãy nhập vào đây bộ kiểm tra với 1.600 hàng và

### 00:00:50.400 - 00:00:55.920
hãy lấy tổng dấu thời gian trong bộ kiểm tra ở đây và chúng ta vẫn có

### 00:00:55.920 - 00:01:00.719
 lưu ở đây bảng hàng đợi để bảng xếp hàng được đào tạo và sau đó chúng ta có thể xác định

### 00:01:00.719 - 00:01:08.320
số tập kiểm tra. Vì vậy, ví dụ 1.000 và ở đây chúng tôi đặt kích thước của một tập

### 00:01:08.320 - 00:01:16.480
 tập là 250 và sau đó ở đây chúng tôi có mã giai đoạn thử nghiệm nên ở đây chúng tôi

### 00:01:16.480 - 00:01:22.719
khởi tạo một danh sách trống nơi chúng tôi lưu trữ tất cả phần thưởng cho tất cả các tập, sau đó chúng tôi

### 00:01:22.719 - 00:01:28.799
cũng tính vào số lần thành công và sau đó cũng ở đây chúng tôi đặt chỗ ngẫu nhiên thành

### 00:01:28.799 - 00:01:34.959
và khả năng tái tạo, sau đó chúng tôi lặp lại các tập và chúng tôi chọn một

### 00:01:34.959 - 00:01:41.640
bắt đầu ngẫu nhiên và sau đó phần còn lại thực sự là ở đây giống như trong giai đoạn đào tạo

### 00:01:41.640 - 00:01:49.400
sau đó, hãy thực hiện các bước ở đây và thực hiện hành động tốt nhất theo

### 00:01:49.400 - 00:01:53.960
bảng xếp hàng. Đó là một trong những khác biệt chính giữa giai đoạn huấn luyện

### 00:01:53.960 - 00:02:03.440
 và giai đoạn thử nghiệm để không có epsilon và không có khám phá, sau đó chúng tôi

### 00:02:03.440 - 00:02:08.960
thực hiện hành động mà chúng tôi thực sự cập nhật vị trí mà chúng tôi nhận được ở hàng tiếp theo, v.v.

### 00:02:08.960 - 00:02:15.920
và cuối cùng, chúng tôi thêm tổng phần thưởng của tập thử nghiệm vào danh sách và chúng tôi

### 00:02:15.919 - 00:02:22.679
cũng kiểm tra xem tập đó có thành công hay không rồi in ra. Hãy

### 00:02:22.679 - 00:02:31.359
ở đây chạy thử nghiệm trên 1.000 tập và chúng ta có thể thấy ở đây rằng tổng

### 00:02:31.359 - 00:02:41.119
phần thưởng thấp hơn và đôi khi âm nên tổng phần thưởng trung bình chỉ là 7,16

### 00:02:41.120 - 00:02:50.400
 và tỷ lệ thành công là 62% và con số này thấp hơn đáng kể so với hiệu suất

### 00:02:50.400 - 00:02:56.800
 trên tập huấn luyện vì vậy hãy đạt hiệu suất ở đây một lần nữa để phần thưởng trung bình

### 00:02:56.800 - 00:03:06.640
là 87 và bây giờ thấp hơn 90% và điều này chỉ đơn giản là do trang bị quá mức

### 00:03:06.639 - 00:03:12.759
vì vậy tác nhân đã học được các mẫu của tập huấn luyện không nhất thiết

### 00:03:12.759 - 00:03:20.319
các mẫu giống nhau trên tập kiểm tra và tác nhân thực sự không thể khái quát hóa dữ liệu mới tuy nhiên chúng tôi vẫn có tỷ lệ thành công lớn hơn 50 nên

### 00:03:20.319 - 00:03:26.119
vẫn có hiệu suất tích cực của tác nhân trên tập kiểm tra nên không phải vậy

### 00:03:26.119 - 00:03:32.039
chỉ là giao dịch ngẫu nhiên nhưng ít thành công hơn và chúng tôi cũng có thể tạo biểu đồ

### 00:03:32.039 - 00:03:37.560
với phần thưởng thử nghiệm để chúng tôi có một số tập tiêu cực và một số

### 00:03:37.560 - 00:03:43.879
tích cực và chúng tôi cũng có thể phân tích tập cuối làm ví dụ nên ở đây chúng tôi

### 00:03:43.879 - 00:03:52.319
có lợi nhuận là 14 và thay đổi vị trí đào tạo và đây là

### 00:03:52.319 - 00:03:58.799
lợi nhuận hoặc phần thưởng tích lũy theo thời gian nên nó vẫn tăng nhưng không

### 00:03:58.800 - 00:04:05.000
ổn định nên chúng tôi có một số nhược điểm ở đây và ở đây bây giờ câu hỏi là làm thế nào chúng tôi có thể

### 00:04:05.000 - 00:04:10.640
giảm trang bị quá mức và chúng ta sẽ tập trung vào vấn đề này trong một trong những bài giảng tiếp theo nhưng với

### 00:04:10.640 - 00:04:16.480
một số biện pháp đầu tiên, chúng ta thực sự nên giảm số tập xuống

### 00:04:16.480 - 00:04:24.480
ví dụ 1.200, vì vậy hãy thử điều này và có lẽ chúng ta cũng nên giảm phân rã epsilon

### 00:04:24.480 - 00:04:31.520
để có nhiều hành động và đặc điểm ngẫu nhiên hơn trong giai đoạn huấn luyện để

### 00:04:31.520 - 00:04:39.920
khái quát hóa tốt hơn nên hãy chạy đến đây một lần nữa và xem liệu chúng ta có thể tăng

### 00:04:39.920 - 00:04:45.480
hiệu suất trên tập kiểm tra hay không nên rất có thể chúng ta sẽ giảm hiệu suất

### 00:04:45.480 - 00:04:51.680
 trên tập huấn luyện nhưng đó thực sự là kết quả mong muốn để

### 00:04:51.680 - 00:04:59.120
hiệu suất trên tập huấn luyện và tập kiểm tra sẽ tiến gần hơn nên ở đây chúng ta có tổng phần thưởng trung bình

### 00:04:59.120 - 00:05:04.680
 là 18,11 và tỷ lệ thành công là 79%, vì vậy hãy chạy lại phần này trên

### 00:05:04.680 - 00:05:15.800
tập huấn luyện trên tập kiểm tra nên đây là hiệu suất trên tập kiểm tra

### 00:05:15.800 - 00:05:23.040
 và hãy kiểm tra xem liệu chúng ta có thể thu hẹp khoảng cách hay không và thực sự chúng ta có thể tăng

### 00:05:23.040 - 00:05:30.920
tổng phần thưởng trung bình và cũng tăng tỷ lệ thành công này nên hiện tại chúng

### 00:05:30.920 - 00:05:35.840
ít trang bị quá mức hơn trong mô hình nhưng vẫn hiệu suất trên tập kiểm tra

### 00:05:35.840 - 00:05:42.759
có thể tốt hơn vì vậy hãy kiểm tra lại tập cuối cùng, điều này ổn nhưng không

### 00:05:42.759 - 00:05:53.719
hoàn hảo nhưng bây giờ chúng ta có một tác nhân cũng thực hiện trên tập kiểm tra nên

### 00:05:53.719 - 00:06:02.079
với tỷ lệ thành công cao hơn 50% nên đây không chỉ là đào tạo ngẫu nhiên mà còn một

### 00:06:02.079 - 00:06:08.240
còn một vấn đề nữa nên vấn đề chi phí giao dịch cho đến nay chúng tôi không

### 00:06:08.240 - 00:06:15.480
tính đến chi phí giao dịch và vì chúng tôi có nhiều thay đổi trong vị thế giao dịch

### 00:06:15.480 - 00:06:19.920
 nên chúng tôi chắc chắn nên làm điều này vậy còn chi phí giao dịch thì sao và chúng tôi sẽ

### 00:06:19.920 - 00:06:25.840
tính đến chi phí giao dịch trong các bài giảng tiếp theo cảm ơn vì đã xem

### 00:06:25.840 - 00:06:30.280
bạn ở đó tạm biệt

### 00:06:30.280 - 00:06:32.960
you there bye

