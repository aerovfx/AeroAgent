## Nội dung

### 00:00:00.000 - 00:00:06.560
Trong bài giảng trước, chúng ta đã thấy tác dụng của việc đào tạo tác nhân học tăng cường.

### 00:00:06.560 - 00:00:13.960
Vì vậy, bảng hàng đợi đã chuyển từ các giá trị ngẫu nhiên sang các mẫu rõ ràng với các hành động tối ưu cho

### 00:00:13.960 - 00:00:15.839
một trạng thái nhất định.

### 00:00:15.839 - 00:00:21.440
Bây giờ, quá trình cập nhật bảng hàng đợi có lẽ là phần phức tạp nhất trong một dự án học tập

### 00:00:21.440 - 00:00:22.760
tăng cường.

### 00:00:22.760 - 00:00:27.760
Vì vậy, hãy viết mã ngược lại và cũng để thực sự hiểu lý do căn bản đằng sau nó.

### 00:00:27.760 - 00:00:34.160
Và trong bài giảng này, chúng ta sẽ cố gắng hiểu cơ chế đằng sau việc cập nhật bảng hàng đợi.

### 00:00:34.160 - 00:00:38.359
Và chúng ta thực sự đang nói về điều sau đây code.

### 00:00:38.359 - 00:00:42.800
Vì vậy, một vài dòng này đang cập nhật bảng hàng đợi.

### 00:00:42.800 - 00:00:51.240
Vì vậy, khi chúng tôi đã thực hiện một hành động, ngẫu nhiên hoặc dựa trên dự báo tối đa

### 00:00:51.240 - 00:00:53.280
giá trị đó.

### 00:00:53.280 - 00:00:59.800
Vì vậy, dựa trên hành động này, chúng tôi xác định trạng thái tiếp theo và rời rạc hóa trạng thái.

### 00:00:59.800 - 00:01:10.599
Và sau đó chúng tôi thực sự cập nhật bảng hàng đợi và chỉ cần sao chép mã vào đây vào

### 00:01:10.599 - 00:01:22.399
chat GPT và chúng tôi thực sự có thể hỏi bạn câu hỏi sau.

### 00:01:22.399 - 00:01:27.479
Vì vậy, vui lòng giải thích mã sau đây và lý do đằng sau nó một cách đơn giản lời, đang cập nhật

### 00:01:27.479 - 00:01:29.439
bảng hàng đợi.

### 00:01:29.439 - 00:01:32.560
Vì vậy, hãy xem những gì chúng ta nhận được ở đây.

### 00:01:32.560 - 00:01:38.399
Bây giờ hãy kiểm tra xem phản hồi có chắc chắn hay không, hãy chia nhỏ đoạn mã được cung cấp.

### 00:01:38.400 - 00:01:42.040
Vì vậy, số một, tìm hành động tiếp theo tốt nhất.

### 00:01:42.040 - 00:01:49.800
Vì vậy, chúng ta xác định hành động tốt nhất cần thực hiện từ trạng thái tiếp theo với np.artmax tìm thấy

### 00:01:49.800 - 00:01:54.840
hành động có giá trị hàng đợi cao nhất cho trạng thái tiếp theo.

### 00:01:54.840 - 00:02:00.320
Vì vậy, điều này có nghĩa là nó tìm kiếm tất cả hành động có thể xảy ra từ trạng thái tiếp theo và chọn hành động đó có

### 00:02:00.320 - 00:02:04.560
phần thưởng ước tính cao nhất trong tương lai.

### 00:02:04.560 - 00:02:07.480
Và số hai tính toán mục tiêu TD.

### 00:02:07.480 - 00:02:10.879
Vì vậy, đó là mục tiêu chênh lệch tạm thời.

### 00:02:10.879 - 00:02:16.080
Và mục đích ở đây là tính toán giá trị mục tiêu được sử dụng để cập nhật giá trị hàng đợi cho cặp hành động ở trạng thái hiện tại

### 00:02:16.080 - 00:02:18.439
.

### 00:02:18.439 - 00:02:22.960
Và ở đây chúng ta thực sự có phần thưởng ngay lập tức nhận được sau khi thực hiện hành động.

### 00:02:22.960 - 00:02:28.920
Vì vậy, đối với hành động hiện tại, chúng ta có gamma siêu tham số là hệ số giảm giá

### 00:02:28.920 - 00:02:34.080
 và xác định tầm quan trọng của phần thưởng trong tương lai.

### 00:02:34.080 - 00:02:38.719
Và giá trị gần hơn một nghĩa là phần thưởng trong tương lai có giá trị cao.

### 00:02:38.719 - 00:02:44.840
Và sau đó, bảng xếp hàng ở trạng thái tiếp theo, hành động tiếp theo tốt nhất là giá trị hàng đợi của hành động tốt nhất

### 00:02:44.840 - 00:02:51.920
từ trạng thái tiếp theo biểu thị phần thưởng tối đa được mong đợi trong tương lai từ trạng thái tiếp theo.

### 00:02:51.920 - 00:02:58.840
Và mục tiêu chênh lệch tạm thời kết hợp phần thưởng ngay lập tức và phần thưởng tối đa được chiết khấu trong tương lai

### 00:02:58.840 - 00:03:06.200
mang lại cho chúng tôi tổng phần thưởng mong đợi khi thực hiện hành động hiện tại.

### 00:03:06.200 - 00:03:13.800
Vì vậy, chúng tôi không chỉ xem xét hành động hiện tại theo một cách riêng biệt mà còn kiểm tra phần thưởng dự kiến

### 00:03:13.800 - 00:03:19.120
trong tương lai từ follow về các hành động.

### 00:03:19.120 - 00:03:25.319
Và sau đó, chúng ta cập nhật giá trị hàng đợi của cặp hành động trạng thái hiện tại.

### 00:03:25.319 - 00:03:30.599
Vì vậy, hãy điều chỉnh giá trị hàng đợi dựa trên thông tin mới.

### 00:03:30.599 - 00:03:36.199
Và ở đây chúng ta cũng có alpha là tốc độ học tập và kiểm soát lượng giá trị hàng đợi

### 00:03:36.199 - 00:03:37.879
được cập nhật.

### 00:03:37.879 - 00:03:44.159
Vì vậy, alpha cao hơn có nghĩa là học nhanh hơn nhưng kém ổn định hơn.

### 00:03:44.159 - 00:03:50.519
Sau đó, trong dấu ngoặc ở đây, chúng ta có lỗi hoặc sự khác biệt giữa mục tiêu TD

### 00:03:50.520 - 00:03:53.400
 và giá trị hàng đợi hiện tại.

### 00:03:53.400 - 00:03:57.000
Và lỗi này chỉ ra cách thực hiện. nhiều ước tính hiện tại của chúng tôi.

### 00:03:57.000 - 00:04:05.600
Vì vậy, giá trị hàng đợi hiện tại khác với mục tiêu mới được tính toán.

### 00:04:05.600 - 00:04:10.960
Và sau đó thực tế alpha nhân với chênh lệch chia tỷ lệ lỗi này theo tốc độ học và

### 00:04:10.960 - 00:04:13.840
điều chỉnh giá trị hàng đợi cho phù hợp.

### 00:04:13.840 - 00:04:19.400
Vì vậy, nếu lỗi lớn, giá trị hàng đợi sẽ được điều chỉnh đáng kể.

### 00:04:19.399 - 00:04:20.879
Vì vậy, điều này chắc chắn có ý nghĩa.

### 00:04:20.879 - 00:04:30.079
Và sau đó chúng tôi ghi đè ở đây giá trị hiện tại và mức giảm tăng dần theo chênh lệch có trọng số

### 00:04:30.079 - 00:04:32.679
được tính theo trọng số của tốc độ học.

### 00:04:32.679 - 00:04:36.279
Và lý do căn bản đằng sau mã là lặp lại giá trị đó hạm đội.

### 00:04:36.279 - 00:04:42.319
Vì vậy, điều đó quan trọng lặp đi lặp lại qua nhiều bước và qua nhiều tập.

### 00:04:42.319 - 00:04:45.199
Cải thiện giá trị hàng đợi bắt đầu trong bảng hàng đợi.

### 00:04:45.199 - 00:04:54.519
Để chúng thể hiện chính xác hơn phần thưởng dự kiến trong tương lai cho mỗi cặp hành động ở trạng thái.

### 00:04:54.519 - 00:04:57.800
Và điều này được thực hiện bằng cách làm theo ba bước sau.

### 00:04:57.800 - 00:05:03.079
Vì vậy, hãy nhìn về phía trước, xác định kết quả tốt nhất có thể có từ trạng thái tiếp theo để xem xét phần thưởng trong tương lai

### 00:05:03.079 - 00:05:04.079
.

### 00:05:04.079 - 00:05:06.120
Vì vậy, điều đó rất quan trọng.

### 00:05:06.120 - 00:05:07.519
Thứ hai, kết hợp phiếu bầu của bạn.

### 00:05:07.519 - 00:05:14.360
Vì vậy, chúng tôi tính toán mục tiêu kết hợp phần thưởng trước mắt và phần thưởng tốt nhất trong tương lai.

### 00:05:14.360 - 00:05:16.520
Và thứ ba, cập nhật kiến thức.

### 00:05:16.520 - 00:05:22.040
Vì vậy, việc điều chỉnh giá trị hàng đợi hiện tại để tiến gần hơn đến mục tiêu này, giúp tinh chỉnh kiến thức

### 00:05:22.040 - 00:05:24.160
của tác nhân về môi trường.

### 00:05:24.160 - 00:05:29.960
Vì vậy, quy trình này được gọi là quy tắc cập nhật học tập hàng đợi đảm bảo rằng theo thời gian, giá trị hàng đợi

### 00:05:29.960 - 00:05:35.439
 chuyển đổi để thể hiện giá trị thực của việc thực hiện từng hành động trong mỗi trạng thái, cho phép

### 00:05:35.439 - 00:05:38.720
tác nhân thực hiện tối ưu quyết định.

### 00:05:38.720 - 00:05:42.600
Và chúng ta cũng có thể đi đến đây thông qua các phép tính.

### 00:05:42.600 - 00:05:51.320
Vì vậy, bắt đầu với một bảng xếp hàng ngẫu nhiên, và sau đó chúng ta có một trạng thái ban đầu mà chúng ta rời rạc hóa.

### 00:05:51.320 - 00:05:58.000
Sau đó, ban đầu chúng ta thực hiện các hành động ngẫu nhiên điển hình trong giai đoạn khám phá.

### 00:05:58.000 - 00:06:00.520
Vì vậy, hãy tăng tốc sang bên phải.

### 00:06:00.520 - 00:06:04.600
Và sau đó chúng ta thực hiện hành động và quan sát kết quả.

### 00:06:04.600 - 00:06:11.480
Và đây là trạng thái tiếp theo cũng là năm và sáu, vì vậy thùng số năm và thùng số sáu.

### 00:06:11.480 - 00:06:15.319
Và sau đó chúng ta có thể kiểm tra phần thưởng của cái tiếp theo. trạng thái.

### 00:06:15.319 - 00:06:23.160
Vì vậy, 0,7 để tăng tốc sang trái, 0,61 nếu không làm gì và 0,96 để tăng tốc sang

### 00:06:23.160 - 00:06:24.319
bên phải.

### 00:06:24.319 - 00:06:30.400
Vì vậy, hành động tiếp theo tốt nhất nên tăng tốc sang bên phải vì đây là giá trị cao nhất

### 00:06:30.400 - 00:06:32.560
to.

### 00:06:32.560 - 00:06:34.480
Vì vậy, hành động số hai.

### 00:06:34.480 - 00:06:38.280
Và sau đó chúng ta có thể xác định phần thưởng trong tương lai của hành động tiếp theo tốt nhất.

### 00:06:38.279 - 00:06:44.279
Vì vậy, chúng ta chuyển sang trạng thái tiếp theo và hành động tiếp theo tốt nhất.

### 00:06:44.279 - 00:06:47.519
Và tương lai của những gì đang diễn ra 0,96.

### 00:06:47.519 - 00:06:52.439
Và sau đó chúng tôi tính toán phần thưởng có trọng số của hành động hiện tại và hành động tiếp theo tốt nhất

### 00:06:52.439 - 00:06:56.199
Mục tiêu TD trừ 0,04.

### 00:06:56.199 - 00:07:02.919
Và bằng cách này, chúng tôi có thể cập nhật giá trị hàng đợi cho cặp hành động trạng thái hiện tại, trước đó

### 00:07:02.919 - 00:07:03.919
0,96.

### 00:07:04.920 - 00:07:07.400
Và sau khi cập nhật, nó thấp hơn một chút.

### 00:07:07.400 - 00:07:17.360
Vậy là 0,859 vì trong hành động hiện tại, chúng tôi nhận được phần thưởng âm.

### 00:07:17.360 - 00:07:21.920
Bây giờ có một câu hỏi cuối cùng, hơi thấp hơn một chút. phản trực giác.

### 00:07:21.920 - 00:07:24.520
Vì vậy, chúng ta hãy thử lời nhắc sau ở đây.

### 00:07:24.520 - 00:07:29.400
Vì vậy, đối với hầu hết các cặp hành động trạng thái này, phần thưởng ngay lập tức luôn là âm một.

### 00:07:29.400 - 00:07:33.560
Vì vậy, miễn là chúng ta không ở rất gần mục tiêu, chúng ta sẽ không

### 00:07:33.680 - 00:07:37.280
tiếp cận mục tiêu bằng một cặp hành động trạng thái.

### 00:07:37.280 - 00:07:40.360
Và do đó, phần thưởng luôn là âm một.

### 00:07:40.360 - 00:07:45.480
Vì chúng ta không đạt được mục tiêu bằng chính hành động đó, bạn có thể giải thích lý do và cách thức giá trị hàng đợi

### 00:07:45.480 - 00:07:50.959
 cho các hành động tối ưu tăng theo thời gian trong quá trình đào tạo quá trình?

### 00:07:50.959 - 00:07:54.240
Điều này có vẻ phản trực giác.

### 00:07:54.240 - 00:08:01.079
Vì vậy, không có gì ngạc nhiên khi tất cả đều liên quan đến phần thưởng trong tương lai và các hành động

### 00:08:01.079 - 00:08:02.079
tiếp theo.

### 00:08:02.079 - 00:08:09.279
Vì vậy, chúng tôi đã thấy rằng phần thưởng của các hành động trong tương lai cũng được tính đến

### 00:08:09.279 - 00:08:13.279
khi cập nhật các bước ngay lập tức.

### 00:08:13.279 - 00:08:20.439
Vì vậy, hãy yêu cầu ở đây giải thích điều này một lần nữa.

### 00:08:20.439 - 00:08:22.159
Vì vậy, hãy kiểm tra phản hồi của bạn.

### 00:08:22.159 - 00:08:27.279
Chắc chắn quá trình học hàng đợi thực sự có thể được nhìn thấy trong tài khoản trực quan lúc đầu,

### 00:08:27.279 - 00:08:32.559
đặc biệt là khi phần thưởng trước mắt luôn âm như trừ một cho bài toán

### 00:08:32.559 - 00:08:34.039
xe leo núi.

### 00:08:34.039 - 00:08:39.639
Tuy nhiên, việc học hàng đợi mơ hồ đảm bảo rằng giá trị hàng đợi cho các hành động tối ưu tăng

### 00:08:39.639 - 00:08:40.919
theo thời gian.

### 00:08:40.919 - 00:08:42.799
Vì vậy, hãy chia nhỏ nó ra ở đây.

### 00:08:42.799 - 00:08:45.839
Vì vậy, phần thưởng ngay lập tức và giá trị hàng đợi cập nhật.

### 00:08:45.839 - 00:08:51.679
Vì vậy, phần thưởng ngay lập tức là trừ một cho mỗi bước cho đến khi xe đạt được mục tiêu và

### 00:08:51.679 - 00:08:55.679
mục tiêu là đạt đến một vị trí nhất định trên đỉnh núi.

### 00:08:55.679 - 00:09:00.559
Và sau đó là khái niệm quan trọng của việc học khác biệt theo thời gian phát huy tác dụng.

### 00:09:00.559 - 00:09:04.319
Vì vậy, việc học hàng đợi dựa trên nguyên tắc học khác biệt theo thời gian, sử dụng

### 00:09:04.319 - 00:09:10.559
cả phần thưởng trước mắt và phần thưởng ước tính trong tương lai để cập nhật các giá trị hàng đợi.

### 00:09:10.559 - 00:09:15.839
Vì vậy, không chỉ phần thưởng trước mắt mà còn cả phần thưởng ước tính trong tương lai.

### 00:09:15.839 - 00:09:19.599
Và đây là cách giá trị hàng đợi tăng theo thời gian.

### 00:09:19.599 - 00:09:24.799
Vì vậy, ban đầu, các giá trị hàng đợi thường được khởi tạo với các giá trị ngẫu nhiên.

### 00:09:24.799 - 00:09:31.319
Sau đó, tác nhân khám phá các hành động thường nhận được phần thưởng ngay lập tức là âm một và

### 00:09:31.319 - 00:09:33.159
sau đó học từ quá trình chuyển đổi.

### 00:09:33.159 - 00:09:38.439
Vì vậy, khi tác nhân thực hiện một hành động ở trạng thái s dẫn đến trạng thái tiếp theo, nó sẽ nhận được phần thưởng r ngay lập tức

### 00:09:38.439 - 00:09:46.359
 và giá trị hàng đợi cho hành động được thực hiện và trạng thái s được cập nhật bằng phương trình Bell

### 00:09:46.359 - 00:09:48.879
Man.

### 00:09:48.879 - 00:09:53.719
Vì vậy, chúng ta đã thấy điều này trong mã.

### 00:09:53.720 - 00:09:59.720
Và quan trọng nhất, việc cập nhật phụ thuộc rất nhiều vào ước tính chiết khấu của phần thưởng trong tương lai

### 00:09:59.720 - 00:10:03.720
.

### 00:10:03.720 - 00:10:09.879
Và nếu trạng thái tiếp theo gần mục tiêu hơn thì phần thưởng trong tương lai dự kiến sẽ là cao hơn.

### 00:10:09.879 - 00:10:14.920
Và qua nhiều tập khi tác nhân thỉnh thoảng đạt được mục tiêu.

### 00:10:14.920 - 00:10:22.040
Vì vậy, điều quan trọng là chúng tôi thỉnh thoảng đạt được mục tiêu trong tốc độ khám phá.

### 00:10:22.039 - 00:10:27.399
Và giá trị hàng đợi cho các trạng thái gần mục tiêu tăng lên vì chúng được theo sau bởi các phần thưởng

### 00:10:27.399 - 00:10:28.719
cao.

### 00:10:28.719 - 00:10:31.360
Vì vậy, cuối cùng, việc đạt được mục tiêu.

### 00:10:31.360 - 00:10:34.599
Và sau đó chúng tôi truyền bá các giá trị cao ngược lại.

### 00:10:34.599 - 00:10:36.240
Vì vậy, điều đó cũng quan trọng.

### 00:10:36.240 - 00:10:42.000
Vì vậy, khi tác nhân thỉnh thoảng đạt được mục tiêu, giá trị hàng đợi cho các cặp hành động ở trạng thái mục tiêu

### 00:10:42.000 - 00:10:45.240
được cập nhật với phần thưởng dương cao.

### 00:10:45.240 - 00:10:48.399
Vì vậy, thường là 0 để đạt được mục tiêu.

### 00:10:48.399 - 00:10:53.639
Và giá trị cao này sau đó được truyền ngược về các trạng thái trước đó.

### 00:10:53.639 - 00:10:56.759
Vì vậy, điều đó rất quan trọng.

### 00:10:56.759 - 00:11:02.360
Và ví dụ: nếu trạng thái s chỉ cách mục tiêu một bước thì giá trị hàng đợi

### 00:11:02.360 - 00:11:07.639
sẽ bắt đầu phản ánh các giá trị cao từ trạng thái tiếp theo.

### 00:11:07.639 - 00:11:09.840
Và tất cả đều tăng dần cải tiến.

### 00:11:09.840 - 00:11:12.720
Vì vậy, chúng tôi cần nhiều bước và nhiều tập.

### 00:11:12.720 - 00:11:19.879
Vì vậy, qua nhiều tập, mặc dù phần thưởng trước mắt là âm một, nhưng giá trị hàng đợi cho các trạng thái

### 00:11:19.879 - 00:11:25.200
dẫn đến mục tiêu bắt đầu phản ánh phần thưởng tích lũy trong tương lai.

### 00:11:25.200 - 00:11:31.840
Và đặc vụ biết rằng thực hiện một số hành động nhất định ở một số trạng thái nhất định sẽ dẫn đến kết quả lâu dài

### 00:11:31.840 - 00:11:33.680
tốt hơn.

### 00:11:33.680 - 00:11:39.560
Vì vậy, ngay cả khi phần thưởng trước mắt là âm một, thì đó là lý do đằng sau việc học hàng đợi

### 00:11:39.560 - 00:11:40.639
ở đây.

### 00:11:40.639 - 00:11:42.480
Và hãy lấy một ví dụ đơn giản.

### 00:11:42.480 - 00:11:48.720
Vì vậy, ban đầu tất cả các giá trị hàng đợi có thể bắt đầu từ 0 và các hành động được thực hiện từ bất kỳ trạng thái nào

### 00:11:48.720 - 00:11:50.240
đến âm một.

### 00:11:50.240 - 00:11:54.159
Vì vậy, các cập nhật ban đầu sẽ giảm nhẹ giá trị hàng đợi.

### 00:11:54.159 - 00:12:00.879
Và sau đó, khi thỉnh thoảng chúng tôi đã đạt được mục tiêu lần đầu tiên, thì các bước cuối cùng gần mục tiêu

### 00:12:00.879 - 00:12:08.600
 giờ đây đã cập nhật các giá trị hàng đợi phản ánh phần thưởng trước mắt cộng với phần thưởng dự kiến trong tương lai.

### 00:12:08.600 - 00:12:14.920
Và sau đó, những giá trị cao này được truyền ngược.

### 00:12:14.920 - 00:12:17.080
Và cuối cùng, tất cả là về việc tiếp tục học hỏi.

### 00:12:17.080 - 00:12:24.399
Vậy là kết thúc theo thời gian, tác nhân sẽ tinh chỉnh các giá trị hàng đợi của nó.

### 00:12:24.399 - 00:12:29.120
Vì vậy, để tổng hợp bộ đếm và mức tăng tích lũy trong các giá trị hàng đợi, mặc dù phần thưởng ngay lập tức âm

### 00:12:29.120 - 00:12:36.279
 xảy ra do việc học hàng đợi cập nhật các giá trị hàng đợi dựa trên tổng phần thưởng dự kiến trong tương lai

### 00:12:36.279 - 00:12:37.720
.

### 00:12:37.720 - 00:12:42.639
Và thông qua việc khám phá và học hỏi nhiều lần các giá trị hàng đợi cho các hành động dẫn đến mục tiêu

### 00:12:42.639 - 00:12:49.919
đã phản ánh lợi ích tích lũy của việc đạt được mục tiêu chứ không chỉ là phần thưởng bước ngay lập tức.

### 00:12:49.919 - 00:12:54.600
Vì vậy, đây là lý do cơ bản đằng sau việc học hàng đợi.

### 00:12:54.600 - 00:12:58.919
Và đây cũng là điểm mạnh của học tăng cường.

### 00:12:58.919 - 00:13:09.039
Vì vậy, tác nhân học cách thực hiện một chuỗi các hành động để đạt được mục tiêu cuối cùng, ngay cả khi các bước hoặc hành động trung gian

### 00:13:09.039 - 00:13:16.799
 không có lợi, nhưng cuối cùng, các bước đó phải thực hiện

### 00:13:16.799 - 00:13:19.079
cuối cùng mới đạt được mục tiêu.

### 00:13:19.079 - 00:13:22.399
Vì vậy, học tăng cường là một công cụ khá mạnh mẽ.

### 00:13:22.399 - 00:13:29.959
Và chúng tôi muốn đào tạo một tác nhân có nhiều bước tuần tự và nhiều quyết định

### 00:13:29.959 - 00:13:33.799
 tuần tự được thực hiện để đạt được mục tiêu cuối cùng.

### 00:13:33.799 - 00:13:35.720
Và đó là tóm tắt.

### 00:13:35.720 - 00:13:41.720
Tại sao chúng ta nên quan tâm đến việc học tăng cường và tại sao chúng ta nên xây dựng các kỹ năng học tập củng cố của riêng mình

### 00:13:41.720 - 00:13:43.279
.

### 00:13:43.279 - 00:13:47.759
Vì vậy, trong tất cả các ví dụ, chúng ta đưa ra nhiều quyết định tuần tự.

### 00:13:47.759 - 00:13:51.679
Vì vậy, cảm ơn bạn đã theo dõi và mong được gặp bạn trong bài giảng tiếp theo.

### 00:13:51.679 - 00:13:51.879
Tạm biệt.

