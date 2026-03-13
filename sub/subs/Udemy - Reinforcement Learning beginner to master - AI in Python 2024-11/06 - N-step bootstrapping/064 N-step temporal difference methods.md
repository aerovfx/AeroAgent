## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong video này, chúng ta sẽ tìm hiểu về nhóm thuật toán nằm giữa Montecarlo và

### 00:00:04.000 - 00:00:06.000
các phương pháp khác nhau theo thời gian.

### 00:00:06.000 - 00:00:09.000
Chúng được gọi là phương pháp sai phân thời gian n bước.

### 00:00:10.000 - 00:00:17.000
Các thuật toán này học dựa trên kinh nghiệm và sử dụng một kỹ thuật được gọi là khởi động n bước.

### 00:00:18.000 - 00:00:25.000
Để giải thích quá trình khởi động n bước là gì, chúng ta hãy xem nhanh quy tắc cập nhật của thuật toán SARSA,

### 00:00:25.000 - 00:00:27.000
mà chúng ta đã thấy ở phần trước.

### 00:00:28.000 - 00:00:36.000
Mỗi lần chúng tôi cập nhật ước tính giá trị q, chúng tôi sẽ đẩy ước tính hiện tại theo hướng mục tiêu.

### 00:00:37.000 - 00:00:39.000
Với số lượng tỷ lệ thuận với alpha.

### 00:00:41.000 - 00:00:49.000
Mục tiêu này là phần thưởng thu được sau khi thực hiện hành động tại thời điểm 't' cộng với giá trị q ước tính của lần tiếp theo.

### 00:00:49.000 - 00:00:54.000
trạng thái và hành động được chọn ở trạng thái tiếp theo đó.

### 00:00:55.000 - 00:01:00.000
Hãy nhớ lại rằng giá trị q là kỳ vọng về phần thưởng trong tương lai khi thực hiện một hành động.

### 00:01:01.000 - 00:01:11.000
Vì vậy, ở đây Q thay thế phần thưởng trong tương lai bằng ước tính và sử dụng ước tính để cập nhật ước tính khác

### 00:01:12.000 - 00:01:14.000
là những gì chúng ta gọi là bootstrapping.

### 00:01:17.000 - 00:01:23.000
Ưu điểm của việc sử dụng ước tính để cập nhật ước tính khác là chúng ta không phải đợi cho đến khi

### 00:01:23.000 - 00:01:29.000
cuối tập để nhận được phần thưởng còn lại vì chúng tôi sử dụng ước tính để thay thế chúng.

### 00:01:31.000 - 00:01:39.000
Trong trường hợp này, chúng tôi đang thực hiện khởi động một bước vì chúng tôi đang sử dụng một phần thưởng thực tế và chúng tôi

### 00:01:39.000 - 00:01:41.000
ước tính phần còn lại.

### 00:01:42.000 - 00:01:51.000
Vì vậy, chúng tôi đang áp dụng ước tính của mình cho một bước trong tương lai, nhưng chúng tôi cũng có thể thực hiện một hành động khác,

### 00:01:51.000 - 00:01:58.000
thu được một phần thưởng thực tế khác, tương tác với môi trường và ước tính phần còn lại bằng cách thay thế

### 00:01:58.000 - 00:02:08.000
chúng với ước tính giá trị q của trạng thái và hành động được chọn trong hai bước trong tương lai hoặc thậm chí thu thập

### 00:02:08.000 - 00:02:15.000
ba phần thưởng và ước tính những phần thưởng còn lại hoặc thậm chí là 'n' phần thưởng.

### 00:02:16.000 - 00:02:20.000
Tất cả những biểu thức này đều là ước tính hợp lệ về sự trở lại của tập phim.

### 00:02:20.000 - 00:02:27.000
Sự khác biệt là chúng bao gồm bao nhiêu phần thưởng thực tế và số lượng chúng tôi ước tính bằng cách sử dụng giá trị q.

### 00:02:29.000 - 00:02:35.000
Khi chúng tôi đưa phần thưởng 'n' thu được từ môi trường vào ước tính, chúng tôi gọi đó là lợi nhuận n bước

### 00:02:35.000 - 00:02:36.000
ước lượng.

### 00:02:38.000 - 00:02:44.000
Và chúng ta sẽ viết nó như thế này: G từ 't' đến 't+n'.

### 00:02:46.000 - 00:02:53.000
Chà, khởi động n bước bao gồm việc thay thế phần thưởng còn lại sau chữ 'n' đầu tiên

### 00:02:53.000 - 00:02:55.000
khen thưởng với một ước tính.

### 00:02:57.000 - 00:03:04.000
Và nếu chúng tôi sử dụng ước tính lợi nhuận n bước làm mục tiêu cập nhật thì biểu thức này vẫn đúng

### 00:03:05.000 - 00:03:11.000
và là quy tắc cập nhật của họ phương pháp mới này được gọi là phương pháp sai phân thời gian n bước.

### 00:03:13.000 - 00:03:20.000
Bằng cách sử dụng các phương pháp này, chúng ta sẽ phải đợi 'n' bước trong tương lai để cập nhật ước tính giá trị q của

### 00:03:20.000 - 00:03:27.000
trạng thái hiện tại, bởi vì chúng tôi sẽ phải thu thập những phần thưởng đó để có thể tính toán ước tính

### 00:03:27.000 - 00:03:28.000
của sự trở lại.

