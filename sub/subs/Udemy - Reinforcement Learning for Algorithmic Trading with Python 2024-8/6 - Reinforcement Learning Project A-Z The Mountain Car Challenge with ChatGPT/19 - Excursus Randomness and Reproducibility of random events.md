## Nội dung

### 00:00:00.000 - 00:00:05.400
Được rồi, trước khi tiếp tục cải tiến tác nhân học tăng cường, chúng ta phải

### 00:00:05.400 - 00:00:12.480
nói về tính ngẫu nhiên và khả năng tái tạo của các sự kiện ngẫu nhiên, cái gọi là hạt giống ngẫu nhiên.

### 00:00:12.480 - 00:00:15.720
Và trước hết, hãy để tôi giải thích vấn đề ở đây.

### 00:00:15.720 - 00:00:23.760
Vì vậy, bất cứ khi nào chúng ta chạy và huấn luyện tác nhân nhiều lần, điều này bao gồm một số sự kiện ngẫu nhiên.

### 00:00:23.760 - 00:00:29.280
Và các tác nhân được đào tạo, có thể nói, các bảng gợi ý sẽ hơi khác một chút.

### 00:00:29.280 - 00:00:34.840
Vì vậy, ngay cả khi bạn nói các thông số đào tạo giống hệt nhau, các tác nhân sẽ khác nhau.

### 00:00:34.840 - 00:00:39.600
Vì vậy, các bảng gợi ý, vì chúng là các sự kiện ngẫu nhiên.

### 00:00:39.600 - 00:00:45.880
Và điều này có nghĩa là các tác nhân cũng khác nhau về hiệu suất.

### 00:00:45.880 - 00:00:51.200
Và vấn đề bây giờ là khi tối ưu hóa một tác nhân bằng cách thay đổi các tham số huấn luyện

### 00:00:51.200 - 00:00:58.320
chẳng hạn như tốc độ học tập, vậy làm cách nào chúng ta có thể đánh giá xem sự khác biệt về hiệu suất có phải do những thay đổi siêu tham số gây ra không?

### 00:00:58.320 - 00:01:01.160
Hoặc những khác biệt này chỉ là sự khác biệt ngẫu nhiên?

### 00:01:01.160 - 00:01:05.520
Vì vậy, đây là một câu hỏi hay.

### 00:01:05.520 - 00:01:08.120
Và giải pháp có thể như sau.

### 00:01:08.120 - 00:01:10.480
Vì vậy, chúng ta nên làm như sau. đảm bảo rằng các sự kiện ngẫu nhiên liên quan có thể tái tạo được.

### 00:01:10.480 - 00:01:16.400
Vì vậy, vẫn ngẫu nhiên nhưng có thể tái tạo.

### 00:01:16.400 - 00:01:19.439
Và chúng ta nên luôn sử dụng cùng một số ngẫu nhiên, sử dụng cùng một hạt giống ngẫu nhiên để đảm bảo

### 00:01:19.439 - 00:01:26.879
rằng các sự kiện ngẫu nhiên có thể lặp lại.

### 00:01:26.879 - 00:01:30.239
Vì vậy, điều này nghe có vẻ phức tạp.

### 00:01:30.239 - 00:01:32.159
Nhưng hãy để tôi chứng minh điều này.

### 00:01:32.159 - 00:01:34.679
Vì vậy, hãy nhập vào đây, mờ và sần sùi và hãy tạo môi trường.

### 00:01:34.679 - 00:01:40.400
Và nếu chúng ta kiểm tra mã huấn luyện ở đây, thì chúng ta có thể tìm thấy một số phần hoặc sự kiện ngẫu nhiên

### 00:01:40.400 - 00:01:49.400
ví dụ: nếu chúng ta tạo tín hiệu ban đầu bảng, sau đó chúng tôi tạo các số ngẫu nhiên lấy

### 00:01:49.400 - 00:01:56.120
từ một phân bố đồng đều giữa trừ 1 và cộng 1 với np.random.uniform.

### 00:01:56.120 - 00:02:04.200
Và bất cứ khi nào chúng tôi chạy ở đây, mã và bất cứ khi nào chúng tôi tạo ở đây bảng gợi ý ban đầu, thì chúng tôi

### 00:02:04.200 - 00:02:12.759
sẽ nhận được một bảng gợi ý ban đầu khác.

### 00:02:12.759 - 00:02:15.960
Vì vậy, đây là những số cho lần chạy này, sau đó hãy tạo một số khác.

### 00:02:15.960 - 00:02:21.439
Và các số này khác nhau.

### 00:02:21.439 - 00:02:23.960
Vì vậy, đây chỉ là các số ngẫu nhiên giữa trừ 1 và 1.

### 00:02:23.960 - 00:02:28.240
Và chúng tôi luôn luôn như vậy bắt đầu với một bảng gợi ý ban đầu khác, tất nhiên điều này cũng ảnh hưởng đến

### 00:02:28.240 - 00:02:34.120
tác nhân cuối cùng.

### 00:02:34.120 - 00:02:35.920
Tuy nhiên, có một giải pháp để làm cho quá trình này vẫn ngẫu nhiên nhưng có thể tái tạo.

### 00:02:35.920 - 00:02:43.159
Và chúng ta có thể làm điều này bằng cách sử dụng np.random.seed.

### 00:02:43.159 - 00:02:47.479
Và chúng ta phải chuyển bất kỳ số nào, bất kỳ số nguyên nào ở đây để gieo hạt.

### 00:02:47.479 - 00:02:51.439
Và miễn là chúng ta sử dụng cùng một số, chúng ta sẽ nhận được các số ngẫu nhiên giống nhau.

### 00:02:51.439 - 00:02:57.840
Vì vậy, hãy thử ở đây, 1, 2, 3 và hãy tạo bảng gợi ý ở đây.

### 00:02:57.840 - 00:03:03.199
Và sau đó nếu chúng ta tạo bảng gợi ý một lần nữa với cùng một hạt giống ngẫu nhiên, khi đó bạn

### 00:03:03.199 - 00:03:08.199
có thể thấy các số giống hệt nhau, đúng như vậy.

### 00:03:08.199 - 00:03:12.400
Vì vậy, hãy chạy nó một lần nữa.

### 00:03:12.439 - 00:03:14.480
Vì vậy, bất cứ khi nào chúng ta tạo bảng gợi ý với hạt giống ngẫu nhiên, 1, 2, 3, chúng ta sẽ nhận được bảng gợi ý ban đầu rất giống nhau

### 00:03:14.480 - 00:03:20.520


### 00:03:20.520 - 00:03:23.159
Vì vậy, hãy làm cho bảng gợi ý có thể lặp lại, ngay cả khi nó vẫn ngẫu nhiên.

### 00:03:23.159 - 00:03:27.759
Vì vậy, những con số này được lấy từ phân bố đồng đều giữa âm 1 và 1.

### 00:03:27.759 - 00:03:35.480
Vậy đây là sự kiện ngẫu nhiên đầu tiên và sau đó chúng ta có quá trình tham lam và tuyệt đối ngẫu nhiên.

### 00:03:35.480 - 00:03:42.080
Vì vậy, hãy nhớ lại giai đoạn huấn luyện ở trên, chúng ta tạo ra một sự nổi ngẫu nhiên giữa

### 00:03:42.080 - 00:03:55.640
0 và 1 và nếu số float ngẫu nhiên nhỏ hơn epsilon thì chúng tôi thực hiện một hành động ngẫu nhiên.

### 00:03:55.640 - 00:04:04.360
Vì vậy, đây thực sự là hành động khám phá.

### 00:04:04.360 - 00:04:08.920
Và nếu số ngẫu nhiên ở đây lớn hơn epsilon thì chúng tôi sẽ thực hiện hành động tốt nhất.

### 00:04:08.920 - 00:04:16.560
Vậy được lấy từ bảng gợi ý.

### 00:04:16.560 - 00:04:18.520
Vì vậy, đây là cách khai thác và tất cả phụ thuộc ở đây vào số ngẫu nhiên mà chúng tôi tạo ở đây

### 00:04:18.520 - 00:04:26.720
với np.random.random.

### 00:04:26.720 - 00:04:28.720
Vì vậy, np.random.random là một sự kiện ngẫu nhiên.

### 00:04:34.360 - 00:04:42.600
Và ví dụ: nếu chúng ta tạo ở đây 10 số nguyên ngẫu nhiên từ 0 đến 1, chúng ta sẽ có chuỗi này

### 00:04:42.600 - 00:04:51.920
ở đây.

### 00:04:51.920 - 00:04:52.920
Và nếu chạy lại, chúng ta sẽ có một chuỗi khác.

### 00:04:52.920 - 00:04:56.480
Vì vậy, mỗi khi chúng ta bắt đầu quá trình, chúng ta sẽ có các chuỗi khác nhau.

### 00:04:56.480 - 00:05:02.199
Và do đó, trong tác nhân học gợi ý của chúng ta, chúng ta nhận được các chuỗi hành động ngẫu nhiên khác nhau

### 00:05:02.199 - 00:05:10.800
và các hành động tối ưu theo bảng gợi ý và điều này chắc chắn ảnh hưởng đến bảng gợi ý.

### 00:05:10.800 - 00:05:18.120
Tuy nhiên, điều này chúng ta cũng có thể thực hiện có thể tái tạo bằng cách đặt chỗ ngồi ngẫu nhiên.

### 00:05:18.120 - 00:05:24.079
Vì vậy, ví dụ: cũng từ 1 đến 3 và miễn là chúng tôi có chỗ ngồi ngẫu nhiên này, chúng tôi luôn nhận được

### 00:05:24.079 - 00:05:30.599
trình tự rất giống nhau.

### 00:05:30.600 - 00:05:32.240
Vì vậy, hãy kiểm tra điều này.

### 00:05:32.240 - 00:05:33.840
Vì vậy, một lần chạy khác và một lần chạy khác.

### 00:05:33.840 - 00:05:38.560
Vậy là nó hoạt động.

### 00:05:38.560 - 00:05:40.560
Tiếp theo.

### 00:05:40.560 - 00:05:41.560
Vì vậy, khi tác nhân phải thực hiện một hành động ngẫu nhiên.

### 00:05:41.560 - 00:05:44.800
Vì vậy, theo định nghĩa, hành động ngẫu nhiên là ngẫu nhiên.

### 00:05:44.800 - 00:05:47.600
Vì vậy, hoặc chúng ta đi sang bên trái, chúng ta không làm gì cả.

### 00:05:47.600 - 00:05:50.000
Hoặc chúng ta tăng tốc sang bên phải.

### 00:05:50.000 - 00:05:52.600
Và đây cũng là một quá trình ngẫu nhiên.

### 00:05:52.600 - 00:05:55.480
Vì vậy, ví dụ: nếu chúng ta thực hiện một chuỗi gồm 10 hành động ngẫu nhiên với môi trường mẫu không gian hành động

### 00:05:55.480 - 00:06:01.759
, sau đó chúng ta có thể nhận được 10 hành động ngẫu nhiên.

### 00:06:01.759 - 00:06:06.920
Và khi chạy lại, chúng ta nhận được một chuỗi khác.

### 00:06:06.920 - 00:06:12.040
Vì vậy, đây chỉ là ngẫu nhiên.

### 00:06:12.040 - 00:06:14.040
Nhưng chúng ta có thể làm cho điều này có thể lặp lại bằng cách đặt chỗ ngồi với chỗ ngồi trong không gian hành động.

### 00:06:14.040 - 00:06:21.879
Và ở đây chúng ta cũng có thể sử dụng từ 1 đến 3.

### 00:06:21.879 - 00:06:24.000
Vì vậy, điều đó không thực sự quan trọng miễn là chúng ta sử dụng cùng một thứ tự cho tất cả các lần chạy.

### 00:06:24.000 - 00:06:29.439
Và bây giờ chúng ta có cùng một trình tự lặp đi lặp lại.

### 00:06:29.439 - 00:06:34.720
Vì vậy, chúng ta cũng có thể làm cho quá trình ngẫu nhiên này có thể lặp lại.

### 00:06:34.720 - 00:06:38.439
Vẫn ngẫu nhiên nhưng có thể lặp lại.

### 00:06:38.439 - 00:06:44.040
Và cuối cùng nhưng không kém phần quan trọng, hãy nhớ lại rằng chúng ta tạo ra một trạng thái ban đầu ngẫu nhiên.

### 00:06:44.040 - 00:06:49.720
Vì vậy, vị trí x của chiếc xe thay đổi từ tập này sang tập khác.

### 00:06:49.720 - 00:06:55.880
Nhưng chúng ta cũng có thể đặt ở đây một chỗ ngồi, ví dụ từ 1 đến 3.

### 00:06:55.880 - 00:07:00.800
Và điều này đảm bảo rằng chúng ta có cùng trạng thái ban đầu trong mỗi tập.

### 00:07:00.800 - 00:07:07.640
Vì vậy, hãy kiểm tra điều này.

### 00:07:07.640 - 00:07:09.640
Vì vậy, chúng ta có ở đây trừ 0,46.

### 00:07:09.640 - 00:07:13.240
Và lặp đi lặp lại.

### 00:07:13.240 - 00:07:15.560
Vì vậy, nếu bạn đặt chỗ ở đây, chúng ta sẽ có điểm xuất phát giống nhau.

### 00:07:15.560 - 00:07:19.440
Nhưng điều này cũng ảnh hưởng tiêu cực đến việc học và sự khái quát hóa.

### 00:07:19.439 - 00:07:24.240
Vì vậy, chúng ta không nên sử dụng chỗ ngồi ở đây vì nó gây hại cho việc học của chúng ta quá trình.

### 00:07:24.240 - 00:07:30.360
Nhưng có một cách giải quyết ở đây.

### 00:07:30.360 - 00:07:32.639
Vì vậy, ở đây chúng ta cũng có thể làm việc với np.random.uniform.

### 00:07:32.639 - 00:07:37.399
Và chúng ta thực sự có thể chuyển vào đây một số nguyên ngẫu nhiên cho tham số chỗ ngồi.

### 00:07:37.399 - 00:07:43.240
Vì vậy, ví dụ từ 1 đến 100.

### 00:07:43.240 - 00:07:50.639
Và bằng cách làm như vậy, chúng ta cũng có thể làm cho kết quả này có thể lặp lại.

### 00:07:50.639 - 00:07:55.400
Vì vậy, nếu bạn không đặt ở đây một chỗ ngồi ngẫu nhiên thì chúng ta sẽ có các trạng thái khác nhau.

### 00:07:55.400 - 00:08:00.639
Vì vậy, nếu bạn có ở đây một chuỗi gồm 10 trạng thái ban đầu thì nếu bạn không đặt chỗ ngồi thì

### 00:08:00.639 - 00:08:08.199
chúng tôi sẽ có một trình tự khác.

### 00:08:08.199 - 00:08:11.720
Nhưng chúng tôi có thể làm cho điều này có thể lặp lại bằng cách đặt một chỗ ngồi ngẫu nhiên.

### 00:08:11.720 - 00:08:16.760
Vì vậy, bây giờ các trạng thái ban đầu giống nhau.

### 00:08:16.760 - 00:08:22.120
Vì vậy, các trình tự đều giống nhau trong mọi lần chạy ở đây.

### 00:08:22.120 - 00:08:30.120
Bây giờ với các biện pháp này ở đây, chúng tôi có thể đảm bảo rằng chúng tôi nhận được cùng một tác nhân học tăng cường

### 00:08:30.120 - 00:08:37.960
tác nhân và bảng hàng đợi giống nhau hết lần này đến lần khác.

### 00:08:37.960 - 00:08:43.280
Vì vậy, đây lại là mã đào tạo đầy đủ.

### 00:08:43.280 - 00:08:49.360
Và ví dụ, chúng ta có thể đặt chỗ ngồi từ 1 đến 3 rồi chạy ở đây np.random.seed và

### 00:08:49.360 - 00:08:56.680
chỗ ngồi trong không gian hành động.

### 00:08:56.680 - 00:09:01.240
Và sau đó ở đây chúng ta có quy trình ngẫu nhiên đầu tiên.

### 00:09:01.240 - 00:09:04.800
Bây giờ chuyển sang một quy trình có thể lặp lại.

### 00:09:04.799 - 00:09:09.839
Và sau đó chúng ta có quy trình ngẫu nhiên thứ hai.

### 00:09:09.839 - 00:09:12.839
Vì vậy, việc tạo trạng thái ban đầu.

### 00:09:12.839 - 00:09:15.479
Và chúng ta chắc chắn nên sử dụng mã này chứ không phải mã này.

### 00:09:15.479 - 00:09:21.120
Vì nó luôn sử dụng cùng một trạng thái ban đầu và điều này gây hại cho việc học.

### 00:09:21.120 - 00:09:26.000
Vì vậy, tôi sẽ chứng minh điều này sau.

### 00:09:26.000 - 00:09:30.279
Và rồi ở đây chúng ta có sự kiện ngẫu nhiên thứ ba và tiếp theo là sự kiện ngẫu nhiên thứ tư.

### 00:09:30.279 - 00:09:36.879
Nhưng những thứ này được bao phủ ở đây bởi hai chỗ này.

### 00:09:36.879 - 00:09:44.279
Vì vậy, điều này chúng ta nên làm cho việc đào tạo tác nhân có thể tái tạo hoàn toàn.

### 00:09:44.279 - 00:09:49.919
Và bây giờ hãy kiểm tra điều này.

### 00:09:49.919 - 00:09:52.279
Vì vậy, hãy đào tạo tác nhân ở đây hai lần.

### 00:09:52.279 - 00:09:58.279
Hãy kiểm tra bảng hàng đợi và nó thực sự giống hệt nhau.

### 00:09:58.279 - 00:10:02.919
Vì vậy, bây giờ quá trình đào tạo bắt đầu.

### 00:10:02.919 - 00:10:11.120
Bây giờ, sau 2.000 tập, chúng tôi đã hoàn thành lượt chạy đầu tiên và chúng tôi có tổng phần thưởng trung bình

### 00:10:11.120 - 00:10:17.120
 là âm 242,98.

### 00:10:17.120 - 00:10:20.480
Và đây là bảng xếp hàng tương ứng.

### 00:10:20.480 - 00:10:23.799
Và bây giờ chúng tôi sẽ chạy quy trình đào tạo một lần nữa với những chỗ ngồi giống nhau.

### 00:10:23.799 - 00:10:28.959
Và chúng tôi sẽ nhận được số liệu thống kê hiệu suất giống nhau và bảng xếp hàng giống nhau.

### 00:10:28.959 - 00:10:38.159
Vì vậy, hãy kiểm tra lại điều này.

### 00:10:38.159 - 00:10:39.519
Vì vậy, tôi sẽ chạy khóa đào tạo ở đây một lần nữa với cùng một bảng giống nhau. chỗ ngồi.

### 00:10:39.519 - 00:10:47.679
Vậy là nó hiện đang chạy ở đây.

### 00:10:47.679 - 00:10:49.759
Và hãy đợi cho đến khi chúng ta đạt tới 2.000 tập.

### 00:10:49.759 - 00:10:53.960
Vì vậy, đây là số liệu thống kê hiệu suất rất giống nhau của lần chạy thứ hai.

### 00:10:53.960 - 00:10:58.759
Và chúng ta cũng hãy đến đây bảng hàng đợi và các số phải giống hệt nhau.

### 00:10:58.759 - 00:11:03.159
Vì vậy, bắt đầu ví dụ với 3,92 và ở giữa là trừ 4,277.

### 00:11:03.159 - 00:11:12.519
Vì vậy, đây là các bảng hàng đợi giống hệt nhau.

### 00:11:12.519 - 00:11:15.879
Và với điều này, chúng ta thực sự có thể đảm bảo khả năng tái tạo.

### 00:11:15.879 - 00:11:22.480
Và bây giờ nếu chúng ta thay đổi ở đây các siêu tham số của quá trình huấn luyện và sau đó nếu bạn quan sát thấy sự khác biệt

### 00:11:22.480 - 00:11:31.360
thống kê hiệu suất thì chúng tôi có thể chắc chắn rằng điều này là do siêu tham số và

### 00:11:31.360 - 00:11:38.559
không phải do các sự kiện ngẫu nhiên và tính ngẫu nhiên của quá trình đào tạo.

### 00:11:38.559 - 00:11:46.719
Vì vậy, đây là một phát hiện quan trọng ở đây.

### 00:11:46.719 - 00:11:48.879
Trước khi chúng tôi có thể tiếp tục điều chỉnh siêu tham số và hơn thế nữa, cảm ơn bạn đã xem và

### 00:11:48.879 - 00:11:53.479
mong được gặp bạn trong bài giảng tiếp theo.

### 00:11:53.479 - 00:11:56.199
Tạm biệt.

### 00:11:56.199 - 00:11:56.519
Bye.

