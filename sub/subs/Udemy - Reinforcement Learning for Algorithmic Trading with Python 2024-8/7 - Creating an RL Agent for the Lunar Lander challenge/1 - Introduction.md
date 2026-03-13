## Nội dung

### 00:00:00.000 - 00:00:06.080
Xin chào và chào mừng bạn đến với chương trình giới thiệu học tập người nhanh xanh thứ hai của chúng tôi Thử thách Luna Lander.

### 00:00:06.080 - 00:00:12.720
Và tại đây, trên trang web phòng tập thể dục, bạn có thể xem trực tiếp một số tập ngẫu nhiên của Thử thách Luna

### 00:00:12.720 - 00:00:14.439
Thử thách Lander.

### 00:00:14.439 - 00:00:21.320
Vì vậy, thông thường bạn sẽ thấy ở đây những sự cố nghiêm trọng như thế này ở đây.

### 00:00:21.320 - 00:00:28.719
Vì vậy, sẽ khó khăn hơn để có một tập thành công là hạ cánh an toàn và mềm mại

### 00:00:28.719 - 00:00:35.359
ở đây trong hai lá cờ.

### 00:00:35.359 - 00:00:42.479
Vì vậy, hãy đến phần môi trường và chúng ta sẽ tìm thấy điều này trên hộp 2D Chiều 2D

### 00:00:42.479 - 00:00:45.200
Luna Lander.

### 00:00:45.200 - 00:00:49.759
Vì vậy, trong dự án này, chúng ta sẽ thấy rằng ý tưởng chính đằng sau việc học của Green Fastman luôn là

### 00:00:49.759 - 00:00:51.239
giống nhau.

### 00:00:51.239 - 00:00:58.399
Vì vậy, chúng ta có một đặc vụ thực hiện các hành động trong một môi trường và nhận phần thưởng. Dựa vào đó, đặc vụ

### 00:00:58.399 - 00:01:04.719
cần tìm hiểu và tối ưu hóa chuỗi hành động trong môi trường nhất định để tối đa hóa

### 00:01:04.719 - 00:01:06.319
phần thưởng.

### 00:01:06.319 - 00:01:11.759
Vì vậy, Thử thách Luna Lander rất giống với thử thách thẻ leo núi và điểm khác biệt

### 00:01:11.759 - 00:01:17.920
 duy nhất là nó phức tạp hơn với không gian quan sát nhiều chiều hơn và một chút

### 00:01:17.920 - 00:01:23.640
không gian hành động phức tạp hơn và phần thưởng cũng phức tạp hơn một chút.

### 00:01:23.640 - 00:01:31.840
Vì vậy, môi trường là một vấn đề tối ưu hóa tên lửa cổ điển nên cố gắng hạ cánh dưới lực hấp dẫn

### 00:01:31.840 - 00:01:35.799
và tốt nhất là nổ hết ga hoặc tắt động cơ.

### 00:01:35.799 - 00:01:41.519
Vì vậy, đây là lý do tại sao môi trường này bật hoặc tắt động cơ xử lý đĩa

### 00:01:41.519 - 00:01:43.799
và chúng tôi có ba động cơ.

### 00:01:43.799 - 00:01:51.280
Vì vậy, chúng tôi có động cơ chính, động cơ bên trái và động cơ bên phải.

### 00:01:51.280 - 00:01:52.960
Vì vậy, đây là không gian hành động.

### 00:01:52.960 - 00:01:55.400
Dành cho đĩa. các thao tác chỉnh sửa không làm gì cả.

### 00:01:55.400 - 00:02:02.040
Cháy động cơ bên trái, chữa cháy động cơ chính và chữa cháy động cơ bên phải và không gian quan sát là

### 00:02:02.040 - 00:02:08.560
một vectơ tám chiều nên chúng ta có tám tọa độ.

### 00:02:08.560 - 00:02:14.240
Vì vậy, chúng ta có tám biến ở đây như tọa độ X và Y thì đó là vận tốc tuyến tính

### 00:02:14.240 - 00:02:17.240
theo hướng X và Y.

### 00:02:17.240 - 00:02:24.480
Đó là góc, đó là vận tốc góc và cuối cùng là hai Boolean để biểu thị xem mỗi chân

### 00:02:24.480 - 00:02:27.840
có tiếp xúc với mặt đất hay không.

### 00:02:27.840 - 00:02:34.080
Vì vậy, chúng ta có ở đây chân trái và chân phải và chúng ta kiểm tra ở đây xem chúng có tiếp xúc không

### 00:02:34.080 - 00:02:36.879
với mặt đất hay không.

### 00:02:36.879 - 00:02:43.280
Vì vậy, đây là không gian quan sát và phần thưởng phức tạp hơn một chút nên sau mỗi bước

### 00:02:43.280 - 00:02:49.759
 một phần thưởng được trao và tổng phần thưởng của một tập là tổng số phần thưởng.

### 00:02:49.759 - 00:02:56.159
Và ví dụ với mỗi bước, phần thưởng sẽ tăng lên khi tàu đổ bộ càng gần đường hạ cánh

### 00:02:56.159 - 00:03:04.520
 nên điều này không có gì đáng ngạc nhiên và nó cũng tăng khi tàu đổ bộ di chuyển chậm hơn

### 00:03:04.520 - 00:03:11.039
và nó giảm khi tàu đổ bộ càng nghiêng nên góc không nằm ngang.

### 00:03:11.039 - 00:03:18.039
Và hơn nữa, nó tăng thêm 10 điểm cho mỗi chân tiếp xúc với mặt đất

### 00:03:18.039 - 00:03:25.840
 và giảm 0,03 điểm cho mỗi khung hình mà động cơ phụ đang hoạt động nên lựa chọn tốt nhất

### 00:03:25.840 - 00:03:33.840
là chỉ bắn động cơ chính và cũng giảm 0,03 điểm mỗi khung hình

### 00:03:33.840 - 00:03:37.639
động cơ chính đang hoạt động.

### 00:03:37.639 - 00:03:43.079
Và cuối cùng và quan trọng nhất là tập phim nhận được phần thưởng bổ sung là âm 200

### 00:03:43.079 - 00:03:52.559
hoặc cộng 200 điểm vì bị rơi nên bị trừ 100 hoặc hạ cánh cộng 100 một cách an toàn.

### 00:03:52.559 - 00:03:59.439
Và thực sự, một tập phim được coi là một giải pháp nếu nó có tổng ít nhất 200 điểm.

### 00:03:59.439 - 00:04:05.239
Và tàu đổ bộ bắt đầu ở chính giữa trên cùng của khung nhìn với một lực ban đầu ngẫu nhiên tác dụng

### 00:04:05.240 - 00:04:18.280
 lên tâm khối của nó nên nó luôn bắt đầu ở đây phía trên với một lực ngẫu nhiên.

### 00:04:18.280 - 00:04:23.439
Và cuối cùng tập phim kết thúc nếu tàu đổ bộ gặp sự cố nên thân tàu đổ bộ tiếp xúc

### 00:04:23.439 - 00:04:29.280
với mặt trăng hoặc tàu đổ bộ ra ngoài khung nhìn nên các máy điều khiển lớn hơn

### 00:04:29.280 - 00:04:33.920
hơn một hoặc tàu đổ bộ không tỉnh táo.

### 00:04:33.920 - 00:04:42.480
Vì vậy, đây là thử thách của tàu đổ bộ mặt trăng vẫn khá đơn giản nhưng phức tạp hơn rất nhiều với

### 00:04:42.480 - 00:04:45.600
không gian quan sát tám chiều.

### 00:04:45.600 - 00:04:53.360
Và cuối cùng chúng ta hãy xem một số tập phim thành công để biết một đặc vụ được đào tạo nên trông như thế nào

### 00:04:53.360 - 00:05:03.200
 và một đặc vụ khéo léo nên trông như thế nào có thể thực sự hạ cánh tàu đổ bộ một cách an toàn.

### 00:05:03.199 - 00:05:12.279
Vì vậy, hãy kiểm tra ở đây một số tập thành công để nó từ từ hạ cánh xuống nơi hạ cánh

### 00:05:12.279 - 00:05:15.680
.

### 00:05:15.680 - 00:05:23.879
Vì vậy, đây cũng sẽ là một giải pháp và cuối cùng là tập thứ ba thành công nên hạ cánh chậm

### 00:05:23.879 - 00:05:28.480
cảm ơn vì đã xem và chúng tôi rất mong được gặp bạn trong các bài giảng tiếp theo.

### 00:05:28.480 - 00:05:28.680
Tạm biệt.

