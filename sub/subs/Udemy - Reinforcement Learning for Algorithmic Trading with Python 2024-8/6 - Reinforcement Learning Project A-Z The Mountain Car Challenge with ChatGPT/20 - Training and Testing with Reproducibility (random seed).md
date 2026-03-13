## Nội dung

### 00:00:00.000 - 00:00:05.799
Bây giờ, hãy tóm tắt những gì chúng ta đã học về kiểm tra đào tạo và khả năng tái tạo.

### 00:00:05.799 - 00:00:12.480
Vì vậy, chúng ta bắt đầu ở đây với mã đào tạo 2000 tập và 500 bước và chúng ta đặt

### 00:00:12.480 - 00:00:14.519
một số chỗ ngồi ngẫu nhiên.

### 00:00:14.519 - 00:00:20.920
Vì vậy, chúng ta sử dụng ở đây chỗ ngồi 100 để nó có thể là bất kỳ chỗ ngồi nào.

### 00:00:20.920 - 00:00:29.800
Và sau đó, điều quan trọng nhất ở đây là chúng ta cũng tạo các trạng thái ban đầu ngẫu nhiên và không giống nhau.

### 00:00:30.800 - 00:00:36.799
Vì vậy, hãy đào tạo ở đây đặc vụ với một chỗ ngồi nhất định để 100.

### 00:00:36.799 - 00:00:49.799
Và bất cứ khi nào chúng tôi chạy ở đây hoặc bất cứ khi nào chúng tôi đào tạo ở đây đặc vụ với ghế 100, chúng tôi sẽ nhận được cùng một đặc vụ với cùng một bảng xếp hàng.

### 00:00:49.799 - 00:00:57.799
Vì vậy, hãy kiểm tra bảng xếp hàng ở đây và bây giờ chúng ta hãy đến đây để kiểm tra 2000 tập.

### 00:00:57.799 - 00:01:11.799
Và cũng ở đây chúng ta phải đặt một chỗ ngẫu nhiên để khi tạo trạng thái ban đầu, chúng ta phải sử dụng AC thật tốt để đảm bảo rằng thử nghiệm cũng có thể lặp lại.

### 00:01:11.799 - 00:01:20.799
Vì vậy, chúng ta có thể sử dụng ở đây 2000 tập là đủ để có kết quả rõ ràng.

### 00:01:20.799 - 00:01:27.799
Bây giờ chúng ta hãy chạy ở đây giai đoạn thử nghiệm để thử nghiệm tác nhân mà không có bất kỳ cập nhật nào.

### 00:01:30.799 - 00:01:45.799
Và chúng tôi có ở đây tỷ lệ thành công là 96,45% và tổng phần thưởng trung bình là 166,72% và bây giờ khía cạnh quan trọng là

### 00:01:45.799 - 00:01:54.799
bây giờ khi chúng tôi chạy lại mã hoặc nếu bạn chạy lại mã với cùng số chỗ thì bạn sẽ nhận được kết quả tương tự.

### 00:01:54.799 - 00:02:04.799
Vì vậy, hãy chạy Đây là mã lần thứ hai và bạn sẽ thấy rằng chúng ta có cùng một bảng hàng đợi.

### 00:02:04.799 - 00:02:15.800
Vì vậy, đây là bảng hàng đợi trong lần chạy đầu tiên và bây giờ hãy kiểm tra bảng hàng đợi trong lần chạy thứ hai và rõ ràng là chúng ta có ở đây những con số rất giống nhau.

### 00:02:15.800 - 00:02:22.800
Và giai đoạn thử nghiệm sẽ mang lại hiệu suất rất giống nhau.

### 00:02:22.800 - 00:02:31.800
Vì vậy, hãy nhớ lại tỷ lệ thành công 96,45% và tổng phần thưởng trung bình là 166,72%.

### 00:02:35.800 - 00:02:46.800
Và thực sự ở đây chúng tôi có những con số rất giống nhau nên điều này hoàn toàn có thể tái tạo và cuối cùng là một chuyến tham quan ngắn nên hãy để tôi nhấn mạnh thêm một điều nữa.

### 00:02:46.800 - 00:03:02.800
Vì vậy, hãy chuyển sang giai đoạn huấn luyện và bây giờ nếu chúng tôi sử dụng cùng một trạng thái ban đầu và lặp đi lặp lại thì trong giai đoạn huấn luyện, chúng tôi luôn bắt đầu với cùng một trạng thái ban đầu state.

### 00:03:03.800 - 00:03:16.800
Sau đó, rất có thể kết quả đào tạo sẽ tốt hơn, cao hơn 88% nhưng tác nhân có thể không khái quát hóa được.

### 00:03:16.800 - 00:03:29.800
Vì vậy, nếu tác nhân bắt đầu ở các trạng thái khác nhau thì nó có thể gặp rắc rối cho đến nay, hãy chỉ đào tạo tác nhân ở một trạng thái cụ thể để luôn có cùng trạng thái ban đầu.

### 00:03:32.800 - 00:03:55.800
Sau đó, hiệu suất đào tạo sẽ cao hơn, điều này hơi xảy ra nhưng bây giờ hãy kiểm tra kết quả thử nghiệm ở đây để trong giai đoạn thử nghiệm, chúng ta giả định rằng trạng thái ban đầu có thể thay đổi.

### 00:03:55.800 - 00:04:13.800
Và nếu điều này đúng trong trường hợp tác nhân sẽ hoạt động kém hơn nên dưới 96%, vì vậy hãy xem điều này trực tiếp.

### 00:04:14.800 - 00:04:36.800
Và ở đây, tỷ lệ thành công này chỉ là 86% và tổng phần thưởng trung bình là 207 nên tác nhân yếu hơn để khái quát nên nếu chúng ta bắt đầu với các trạng thái ban đầu mà tác nhân chưa thấy trong giai đoạn huấn luyện thì hiệu suất thực sự yếu hơn, không có gì đáng ngạc nhiên. rằng chúng tôi sử dụng cùng một hạt giống để có thể so sánh hiệu quả các siêu thông số khác nhau và các cài đặt khác nhau cho phần đào tạo của mình. Cảm ơn bạn đã theo dõi và mong được gặp bạn trong bài giảng tiếp theo.

### 00:04:36.800 - 00:05:04.800
So this is all you need to know about reproducibility and random seeds so to compare different settings for example hyper parameters we should make sure that we use the same seeds so that we can effectively compare different hyper parameters and different settings for our training part so thanks for watching and looking forward to seeing you in the next lecture.

