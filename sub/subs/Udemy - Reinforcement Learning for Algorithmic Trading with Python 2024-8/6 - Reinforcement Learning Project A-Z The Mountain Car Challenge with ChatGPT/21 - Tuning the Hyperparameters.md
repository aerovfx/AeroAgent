## Nội dung

### 00:00:00.000 - 00:00:04.160
Được rồi, hãy bắt đầu cải thiện và tối ưu hóa tác nhân.

### 00:00:04.160 - 00:00:08.040
Và ví dụ: chúng ta có thể bắt đầu với các siêu tham số.

### 00:00:08.040 - 00:00:16.120
Và chúng ta đã thấy trước đây, chatGPT có một số đề xuất cho chúng ta về các siêu tham số.

### 00:00:16.120 - 00:00:21.080
Vì vậy, chúng ta nên tăng epsilon ban đầu để bắt đầu với tốc độ khám phá cao hơn.

### 00:00:21.080 - 00:00:25.800
Vì vậy, ví dụ: 50% hoặc thậm chí 90%.

### 00:00:25.800 - 00:00:32.120
Vì vậy, hãy bắt đầu ở đây với 90%.

### 00:00:32.120 - 00:00:35.760
Và sau đó quá trình phân rã epsilon vẫn tiếp tục 99,5%.

### 00:00:35.760 - 00:00:48.600
Và epsilon tối thiểu là 0,01, thì chúng ta có thể giảm tỷ lệ học xuống 0,05.

### 00:00:48.600 - 00:00:57.840
Và chúng ta nên giữ giá trị gamma, là 0,99.

### 00:00:57.840 - 00:01:01.480
Và bây giờ hãy chạy chương trình đào tạo thêm một lần nữa.

### 00:01:01.480 - 00:01:06.560
Vậy là chúng ta vẫn còn 2.000 tập.

### 00:01:06.560 - 00:01:10.359
Và thực sự hiệu suất đào tạo không quan trọng lắm.

### 00:01:10.359 - 00:01:16.560
Vì vậy, nó thực sự phụ thuộc vào hiệu suất kiểm tra.

### 00:01:16.560 - 00:01:21.640
Và thực ra tôi cũng thêm nó vào đây trong bản in là epsilon, nên epsilon theo thời gian.

### 00:01:21.640 - 00:01:25.920
Vậy nó giảm dần do sự phân rã của epsilon.

### 00:01:25.920 - 00:01:31.480
Vì vậy, bắt đầu với 90% tại đây.

### 00:01:31.480 - 00:01:38.439
Và sau 900 tập, chúng tôi đạt đến giá trị tối thiểu, nên chỉ 1%.

### 00:01:38.439 - 00:01:42.280
Và ở đây chúng tôi có số liệu thống kê hiệu suất cho giai đoạn đào tạo.

### 00:01:42.280 - 00:01:47.400
Vì vậy, chúng tôi có tỷ lệ thành công thấp hơn một chút là 79%.

### 00:01:47.400 - 00:01:52.879
Nhưng một lần nữa, điều quan trọng hơn là kiểm tra hiệu suất thử nghiệm.

### 00:01:52.879 - 00:01:59.520
Và thực tế không có thay đổi nào đối với mã thử nghiệm.

### 00:01:59.520 - 00:02:07.000
Vì vậy, hãy chạy ở đây chẳng hạn, 2.000 tập.

### 00:02:07.000 - 00:02:12.360
Và ở đây chúng tôi có hiệu suất và bây giờ chúng tôi có tỷ lệ thành công là 100%.

### 00:02:12.360 - 00:02:17.120
Và tổng phần thưởng trung bình là 162.

### 00:02:17.120 - 00:02:22.560
Vì vậy, đây là một sự cải thiện rõ ràng so với cài đặt ban đầu.

### 00:02:22.560 - 00:02:27.039
Vì vậy, bằng cách điều chỉnh, thay đổi và tối ưu hóa các siêu tham số, chúng tôi có thể cải thiện ở đây

### 00:02:27.039 - 00:02:29.039
hiệu suất.

### 00:02:29.039 - 00:02:33.360
Vì vậy, hiệu suất kiểm tra, không phải hiệu suất huấn luyện.

### 00:02:33.360 - 00:02:39.760
Vì vậy, hiệu suất kiểm tra nhanh là quan trọng hơn.

### 00:02:39.760 - 00:02:46.920
Và tất nhiên chúng ta có thể điều chỉnh thêm ở đây các siêu tham số và cả thực hiện nhiều hơn

### 00:02:46.920 - 00:02:52.120
điều chỉnh siêu tham số hệ thống, điều mà tôi sẽ không trình bày ở đây.

### 00:02:52.120 - 00:03:00.600
Bởi vì bây giờ chúng ta cũng nên tập trung vào các biện pháp khác để cải thiện hiệu suất của tác nhân.

### 00:03:00.599 - 00:03:04.840
Vì vậy, điều chỉnh siêu tham số số một, chúng tôi đã thực hiện điều này.

### 00:03:04.840 - 00:03:11.319
Và sau đó tăng các giai đoạn đào tạo và rời rạc hóa không gian trạng thái là hai điểm quan trọng khác

### 00:03:11.319 - 00:03:13.240
Và chúng ta sẽ tiếp tục ở đây trong bài giảng tiếp theo.

### 00:03:13.240 - 00:03:15.680
Cảm ơn bạn đã theo dõi và hẹn gặp lại bạn ở đó.

### 00:03:15.680 - 00:03:17.759
Tạm biệt.

### 00:03:17.759 - 00:03:18.039
Bye.

