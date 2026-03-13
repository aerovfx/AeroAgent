## Nội dung

### 00:00:00.000 - 00:00:02.640
Bây giờ chúng ta đang đến một điểm quan trọng.

### 00:00:02.640 - 00:00:06.960
Chia tập dữ liệu thành tập huấn luyện và tập kiểm tra.

### 00:00:06.960 - 00:00:09.880
Như chúng ta đã thấy trước đây, có hai giai đoạn,

### 00:00:09.880 - 00:00:13.759
vì vậy, việc đào tạo tác nhân với các tập huấn luyện,

### 00:00:13.759 - 00:00:17.839
và sau đó kiểm tra tác nhân được đào tạo dựa trên các tập thử nghiệm.

### 00:00:17.839 - 00:00:21.679
Đó là lý do tại sao chúng ta cần chia tập dữ liệu ở đây thành

### 00:00:21.679 - 00:00:23.480
tập huấn luyện và kiểm tra.

### 00:00:23.480 - 00:00:29.760
Thông thường, hiệu suất của tác nhân trên tập huấn luyện sẽ tốt hơn so với khi kiểm tra. set.

### 00:00:29.760 - 00:00:34.399
Bởi vì tác nhân gần như phù hợp với dữ liệu huấn luyện,

### 00:00:34.399 - 00:00:39.760
nhưng cuối cùng, điều liên quan nhất đối với chúng tôi là hiệu suất trên dữ liệu mới chưa được xem,

### 00:00:39.760 - 00:00:41.439
nên tập thử nghiệm.

### 00:00:41.439 - 00:00:46.560
Bây giờ, nếu hiệu suất trên tập huấn luyện tốt hơn nhiều so với trên tập thử nghiệm,

### 00:00:46.560 - 00:00:50.000
thì đây là một chỉ báo rõ ràng về việc trang bị quá mức.

### 00:00:50.000 - 00:00:53.600
Vì vậy, tác nhân thiếu khả năng khái quát về dữ liệu mới,

### 00:00:53.600 - 00:00:57.439
và chúng ta sẽ tập trung vào vấn đề này sau trong khóa học này.

### 00:00:57.519 - 00:01:01.280
Nhưng hiện tại, hãy tạo tập huấn luyện và tập kiểm tra trước.

### 00:01:02.000 - 00:01:04.959
Và nguyên tắc chung là chia 80-20,

### 00:01:04.959 - 00:01:09.120
vì vậy 80% tập dữ liệu đầy đủ sẽ là tập huấn luyện,

### 00:01:09.120 - 00:01:11.840
và 20% là tập kiểm tra.

### 00:01:11.840 - 00:01:15.840
Bây giờ, trong trường hợp của chúng ta, chúng ta có 11.600 hàng,

### 00:01:16.560 - 00:01:23.359
và chỉ mẫu tiếp theo này, nên chúng ta có thể xác định rằng 10.000 đầu tiên là tập huấn luyện.

### 00:01:23.760 - 00:01:26.560
Nhưng tất nhiên, điều này rất linh hoạt,

### 00:01:26.560 - 00:01:30.959
và bạn có thể thử nghiệm ở đây với các tập huấn luyện và kiểm tra khác nhau.

### 00:01:32.000 - 00:01:35.039
Bây giờ, hai khía cạnh sau thậm chí còn quan trọng hơn.

### 00:01:35.039 - 00:01:38.239
Vì vậy, khi làm việc với dữ liệu chuỗi thời gian,

### 00:01:38.239 - 00:01:40.400
chúng ta không nên xáo trộn ngẫu nhiên,

### 00:01:40.400 - 00:01:45.359
và dữ liệu gần đây nhất phải là tập kiểm tra.

### 00:01:45.359 - 00:01:50.239
Bởi vì chúng ta muốn biết tác nhân sẽ hoạt động như thế nào trên dữ liệu gần đây nhất,

### 00:01:50.879 - 00:01:54.799
vì vậy ít nhất đó là chỉ báo tốt nhất có thể cho tương lai.

### 00:01:55.519 - 00:02:00.479
Vì vậy, hãy quyết định rằng chúng ta muốn có quy mô đào tạo là 10.000,

### 00:02:00.479 - 00:02:05.759
thì 10.000 hàng hoặc thanh đầu tiên sẽ là tập huấn luyện.

### 00:02:05.759 - 00:02:09.039
Và chúng ta có thể thực hiện điều này ở đây với bộ điều khiển logic mắt.

### 00:02:10.479 - 00:02:16.639
Vậy ở đây chúng ta có từ tháng 9 năm 2022 đến tháng 4 năm 2024.

### 00:02:17.199 - 00:02:20.879
Chúng ta có tập huấn luyện với 10.000 hàng,

### 00:02:20.879 - 00:02:26.159
và sau đó từ đó chúng tôi thực sự trích xuất tập thử nghiệm,

### 00:02:26.799 - 00:02:30.719
nên 1.600 hàng cuối cùng.

### 00:02:33.199 - 00:02:38.399
Vậy từ tháng 4 đến tháng 7 2024, dữ liệu gần đây nhất,

### 00:02:39.359 - 00:02:41.839
vì vậy đây hiện là tập huấn luyện và tập kiểm tra,

### 00:02:41.839 - 00:02:45.519
và chúng tôi sẽ chỉ đào tạo nhân viên trên tập huấn luyện,

### 00:02:45.600 - 00:02:48.159
và đó là kế hoạch cho các bài giảng tiếp theo.

### 00:02:48.159 - 00:02:50.800
Cảm ơn bạn đã xem và hẹn gặp lại bạn ở đó. Tạm biệt!

