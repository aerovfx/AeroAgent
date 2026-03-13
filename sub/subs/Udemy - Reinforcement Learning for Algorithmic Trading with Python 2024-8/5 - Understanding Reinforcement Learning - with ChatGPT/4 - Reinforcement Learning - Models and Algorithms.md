## Nội dung

### 00:00:00.000 - 00:00:14.000
Bây giờ đây là bài giảng cuối cùng về lý thuyết đằng sau học tăng cường và sau đây chúng ta sẽ đi sâu hơn vào chi tiết của các thuật toán và hãy bắt đầu ở đây với gợi ý sau.

### 00:00:14.000 - 00:00:25.000
Vì vậy, vui lòng so sánh các thuật toán học tăng cường được sử dụng phổ biến nhất. Vì vậy, tồn tại nhiều thuật toán khác nhau và phác thảo các trường hợp sử dụng điển hình cho tất cả chúng.

### 00:00:25.000 - 00:00:32.000
Vì vậy, hãy bắt đầu từ đây với Q learning nhưng hãy chờ phản hồi đầy đủ ở đây.

### 00:00:32.000 - 00:00:42.000
Vì vậy, đây là so sánh một số thuật toán được sử dụng phổ biến nhất số một Q learning. Vì vậy, lý do này chúng ta sẽ chủ yếu làm việc với Q learning.

### 00:00:42.000 - 00:00:56.000
Vì vậy, đây là một mô hình không có thuật toán chính sách nhằm mục đích tìm hiểu hàm giá trị hành động tối ưu. Hàm Q cho tác nhân biết tiện ích mong đợi khi thực hiện một hành động nhất định ở một trạng thái nhất định.

### 00:00:56.000 - 00:01:04.000
Và thông thường, điều này hoạt động trong việc tạo ra môi trường có giá trị rời rạc thay vì giá trị liên tục.

### 00:01:04.000 - 00:01:22.000
Và các trường hợp sử dụng điển hình là các trò chơi đơn giản hơn. Và sau đó chúng ta cũng có mô hình Sasa. Vì vậy, tương tự như Q learning, là một thuật toán chính sách, nghĩa là nó học hàm giá trị hành động dựa trên chính sách hiện tại.

### 00:01:22.000 - 00:01:35.000
Sau đó, chúng ta có các mạng Q sâu và DQN kết hợp Q learning với deep learning. Vì vậy, việc sử dụng mạng thần kinh để ước tính hàm giá trị Q.

### 00:01:35.000 - 00:01:48.000
Và điều này cho phép nó xử lý các không gian trạng thái có chiều cao như hình ảnh và các trường hợp sử dụng thông thường, một số trò chơi phức tạp hơn, điều khiển robot lái xe tự động, v.v.

### 00:01:48.000 - 00:02:08.000
Và sau đó chúng tôi có thêm một số thuật toán ở đây. Vì vậy, tôi sẽ không đi qua tất cả. Học Q kép. Vì vậy, Q learning và Sasa là lựa chọn tốt nhất cho các môi trường rời rạc đơn giản, trong đó việc học từ một bảng giá trị Q là khả thi.

### 00:02:08.000 - 00:02:19.000
Và học Q sâu là lý tưởng cho các môi trường có không gian trạng thái nhiều chiều như đầu vào dựa trên hình ảnh mà việc học Q truyền thống sẽ thất bại.

### 00:02:19.000 - 00:02:32.000
Và không có gì ngạc nhiên khi mỗi thuật toán này đều có điểm mạnh và điểm yếu riêng. Và việc lựa chọn sử dụng cái nào phụ thuộc phần lớn vào những yêu cầu cụ thể này.

### 00:02:33.000 - 00:02:44.000
Vì vậy, tôi thực sự khuyên bạn nên bắt đầu với các ví dụ đơn giản và mô hình đơn giản như Q learning. Vì vậy, đó chắc chắn là điểm khởi đầu tốt nhất ở đây.

### 00:02:44.000 - 00:02:56.000
Và bây giờ chúng ta hãy đi vào chi tiết hơn. Vậy thuật toán đơn giản và dễ hiểu nhất là gì? Vì vậy, Q learning phải giải thích các khái niệm và ý tưởng chính đằng sau thuật toán một cách chi tiết hơn.

### 00:02:56.000 - 00:03:09.000
Không cần mã ở giai đoạn này. Vì vậy cách học đơn giản và dễ hiểu nhất là học Q. Và chúng ta hãy chờ đợi ở đây để có được phản hồi đầy đủ.

### 00:03:09.000 - 00:03:20.000
Vì vậy, Q learning là một thuật toán không có mô hình nền tảng, dễ hiểu và dễ triển khai, khiến nó trở thành điểm khởi đầu tuyệt vời cho người mới bắt đầu.

### 00:03:20.000 - 00:03:35.000
Và thực tế, hai khái niệm chính là tác nhân và môi trường. Vì vậy, tác nhân là người ra quyết định trong cài đặt học tăng cường và nó tương tác với môi trường bằng cách thực hiện các hành động.

### 00:03:35.000 - 00:03:45.000
Và môi trường là mọi thứ mà tác nhân tương tác và nó cung cấp phản hồi cho tác nhân dưới dạng phần thưởng và trạng thái mới.

### 00:03:45.000 - 00:03:57.000
Vì vậy, có một trạng thái và tác nhân thực hiện một hành động và dựa trên hành động mà tác nhân nhận được phần thưởng và chúng thay đổi trạng thái.

### 00:03:57.000 - 00:04:09.000
Vì vậy, từ môi trường và dựa vào đó, tác nhân sẽ thực hiện hành động tiếp theo. Vì vậy, trạng thái là sự thể hiện tình huống hoặc cấu hình hiện tại trong môi trường.

### 00:04:09.000 - 00:04:23.000
Và ví dụ: trong trò chơi thế giới lưới, một trạng thái có thể đại diện cho vị trí hiện tại của tác nhân trên lưới và khi đó hành động là lựa chọn của tác nhân có ảnh hưởng đến môi trường.

### 00:04:23.000 - 00:04:33.000
Và ví dụ: trong trò chơi thế giới lưới, các hành động có thể di chuyển lên, di chuyển xuống, di chuyển sang trái hoặc di chuyển để di chuyển sang phải. Đây là một không gian hành động đơn giản.

### 00:04:33.000 - 00:04:46.000
Và sau đó chúng ta có số cho phần thưởng. Vì vậy, đó là phản hồi từ môi trường sau khi tác nhân thực hiện một hành động và nó cho biết giá trị buổi lễ cho biết lợi ích hoặc chi phí trước mắt của hành động đó.

### 00:04:46.000 - 00:04:53.000
Và mục tiêu cuối cùng của tác nhân là tối đa hóa phần thưởng tích lũy theo thời gian.

### 00:04:55.000 - 00:05:08.000
Và sau đó chúng ta có giá trị q, giá trị hành động và bảng q, đồng thời chúng ta sẽ đi sâu hơn vào chi tiết trong khóa học này. Vì vậy, các phần tiếp theo ngoài thao tác chuông.

### 00:05:09.000 - 00:05:29.000
Và khám phá và khai thác cũng là một khái niệm quan trọng. Vì vậy, thông thường trong một môi trường mới, đặc vụ bắt đầu khám phá nên thử các hành động mới và ngẫu nhiên để khám phá các hiệu ứng và điều này có thể dẫn đến phần thưởng lâu dài tốt hơn.

### 00:05:29.000 - 00:05:41.000
Và một khi đặc vụ biết và hiểu rõ hơn về môi trường, nó thực sự khai thác kiến ​​thức của mình để chọn hành động được biết là mang lại phần thưởng cao nhất.

### 00:05:42.000 - 00:05:58.000
Vì vậy, nó có thể tương tự như huấn luyện trong bóng tối nên ban đầu khi bóng tối còn rất trẻ, anh ta thử mọi thứ. Và dựa trên hành động của mình, anh ta nhận được phần thưởng tích cực và tiêu cực và sau đó bóng tối có thể điều chỉnh hành động của anh ta.

### 00:05:58.000 - 00:06:08.000
Vì vậy, tại một thời điểm nào đó, anh ta có thể khai thác kinh nghiệm và kiến ​​thức của mình để thực sự nhận được càng nhiều bánh quy càng tốt.

### 00:06:10.000 - 00:06:27.000
Vì vậy, quá trình học tập số chín chúng ta sẽ đi sâu hơn vào chi tiết trong các phần tiếp theo. Vì vậy, q learning là một thuật toán đơn giản nhưng mạnh mẽ giúp tác nhân học cách đưa ra quyết định tối ưu thông qua thử và sai.

### 00:06:28.000 - 00:06:40.000
Và tác nhân duy trì một bảng q ước tính phần thưởng dự kiến ​​của các hành động ở mỗi trạng thái và các bảng được cập nhật lặp đi lặp lại dựa trên kinh nghiệm của tác nhân.

### 00:06:42.000 - 00:06:53.000
Và thông qua quá trình này, tác nhân dần dần học được những hành động tốt nhất cần thực hiện trong bất kỳ trạng thái nhất định nào để tối đa hóa phần thưởng dài hạn. Vì vậy, điều này nghe có vẻ hợp lý.

### 00:06:53.000 - 00:07:06.000
Và cuối cùng nhưng không kém phần quan trọng, thuật toán này đặc biệt rất phù hợp với các môi trường có trạng thái và hành động rời rạc trong đó số lượng các cặp hành động trạng thái có thể có thể quản lý được.

### 00:07:07.000 - 00:07:16.000
Vì vậy, điều này rất quan trọng nhưng nó cũng có thể xử lý các ngày liên tục bằng cách rời rạc hóa các trạng thái liên tục.

### 00:07:16.000 - 00:07:30.000
Vì vậy, chúng ta cũng sẽ thấy điều này sau trong khóa học nhưng hiện tại chúng ta đã đi đến cuối phần lý thuyết. Vì vậy, bây giờ chúng ta nên biết và hiểu rõ hơn lý do tại sao, cách thức và thời điểm chúng ta thực sự nên sử dụng học tăng cường.

### 00:07:31.000 - 00:07:41.000
Và chúng ta sẽ thấy và hiểu rõ hơn về điều này trong các ví dụ sắp tới. Vì vậy, chúng ta sẽ có thử thách thẻ núi Thử thách người cho vay Lula.

### 00:07:41.000 - 00:07:58.000
Và cuối cùng là giao dịch với ví dụ giao dịch Algo và sau đó bạn chắc chắn sẽ hiểu rõ hơn về lý do căn bản và cơ chế đằng sau việc học tăng cường và đặc biệt là học q.

### 00:07:58.000 - 00:08:02.000
Cảm ơn bạn đã xem và mong được gặp bạn trong các phần tiếp theo bởi

