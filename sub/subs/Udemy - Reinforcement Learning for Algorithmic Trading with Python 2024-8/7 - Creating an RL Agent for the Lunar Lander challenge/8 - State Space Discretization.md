## Nội dung

### 00:00:00.000 - 00:00:08.000
Được rồi, chúng ta đang đến một khía cạnh quan trọng khác. Vì vậy, hãy kiểm tra lại một lần nữa, không gian quan sát.

### 00:00:08.000 - 00:00:16.000
Đây là các ngăn chứa tám biến trạng thái. Và ví dụ, chúng ta có thể đi vào phần đầu tiên.

### 00:00:16.000 - 00:00:23.000
Vậy tọa độ x giữa trừ một và cộng một. Vậy chúng ta có ở đây 15 thùng.

### 00:00:23.000 - 00:00:31.000
Vậy 15 thùng. Và sau đó một lần nữa chúng ta có thể tạo trạng thái ban đầu, thiết lập lại môi trường này.

### 00:00:31.000 - 00:00:42.000
Và ví dụ, đối với tọa độ x, chúng ta có âm 0,0069. Và bây giờ để học Q, chúng ta phải chuyển đổi các giá trị liên tục này.

### 00:00:42.000 - 00:00:51.000
Vì vậy, các trạng thái liên tục thành các trạng thái rời rạc. Và trong thử thách thẻ núi, chúng tôi sử dụng hàm trạng thái rời rạc.

### 00:00:51.000 - 00:00:57.000
Và nó thực sự hoạt động ở đây vì trong thử thách thẻ núi, chúng tôi có giới hạn rõ ràng.

### 00:00:57.000 - 00:01:08.000
Vậy từ âm 1,2 đến cộng 1,2 cho tọa độ x. Và không có ngoại lệ.

### 00:01:08.000 - 00:01:14.000
Và thành thật mà nói, hàm trạng thái rời rạc hơi đơn giản và đơn giản hóa.

### 00:01:14.000 - 00:01:26.000
Và nó phù hợp với thử thách thẻ leo núi. Vì vậy, nếu bạn chuyển trạng thái ban đầu ở đây, thì chúng ta sẽ có các thùng sau.

### 00:01:26.000 - 00:01:34.000
Nhưng sau đó nếu chúng ta sao chép và dán vào đây một số giá trị cực đoan hơn.

### 00:01:34.000 - 00:01:44.000
Vì vậy, hãy xác định ở đây mảng có nhiều mảng ngay bên trong.

### 00:01:44.000 - 00:01:48.000
Vì vậy, hãy chạy lại. Và tất nhiên, chúng ta vẫn có các thùng giống nhau.

### 00:01:48.000 - 00:01:55.000
Vì vậy, đối với tọa độ x, chúng ta đã xác định giá trị tối thiểu là âm một.

### 00:01:55.000 - 00:02:00.000
Và điều này sẽ cho số thùng bằng 0. Vì vậy, việc lập chỉ mục dựa trên số 0 được áp dụng ở đây.

### 00:02:00.000 - 00:02:08.000
Và đối với giá trị một, chúng ta sẽ nhận được thùng số 14. Vậy là số 15 đã có.

### 00:02:08.000 - 00:02:14.000
Bây giờ là vấn đề với hàm trạng thái rời rạc mà chúng ta sử dụng trong các thử thách thẻ núi.

### 00:02:14.000 - 00:02:20.000
Điều đó bây giờ nếu bạn di chuyển nhiều hơn sang trái hoặc sang phải tính từ giới hạn.

### 00:02:20.000 - 00:02:32.000
Vì vậy, nếu bạn có nhiều giá trị cực trị hơn như âm 1,2 hoặc bất kỳ giá trị nào, thì giá trị này sẽ không nằm trong thùng số 0.

### 00:02:32.000 - 00:02:37.000
Nhưng ở số thùng trừ một. Và điều này không có ý nghĩa gì ở đây.

### 00:02:37.000 - 00:02:48.000
Và điều này chắc chắn sẽ tạo ra vấn đề sau này. Và do đó, chúng ta nên đảm bảo rằng ngay cả khi có các giá trị dưới âm một.

### 00:02:48.000 - 00:02:56.000
Vì vậy, các giá trị này vẫn phải nằm trong thùng số 0. Và do đó chúng tôi phải điều chỉnh lại chức năng một chút.

### 00:02:56.000 - 00:03:04.000
Và tất nhiên, chúng tôi cũng có thể hỏi ở đây trò chuyện GPT. Nhưng về cơ bản có một sự bổ sung.

### 00:03:04.000 - 00:03:09.000
Vì vậy, ở đây chúng ta có dòng mã hóa sau đây trong hàm được cập nhật.

### 00:03:09.000 - 00:03:14.000
Và chúng ta đã lưu kết quả trung gian ở dạng số hóa.

### 00:03:14.000 - 00:03:22.000
Và sau đó chúng ta phải đảm bảo rằng đây là một phần được cắt bớt. Vậy sàn nhà là thùng số 0.

### 00:03:22.000 - 00:03:30.000
Và nắp là thùng số 14. Vậy tổng cộng có 15 thùng cho tọa độ X.

### 00:03:30.000 - 00:03:38.000
Vì vậy, cái này thực sự được thêm vào đây. Và sau đó chúng tôi nối thêm số hóa vào IDX trạng thái.

### 00:03:38.000 - 00:03:46.000
Vì vậy, đây là phần bổ sung. Và chúng tôi cần sự bổ sung này trong trường hợp tổng quát hơn của Thử thách người cho vay Luna.

### 00:03:46.000 - 00:03:51.000
Vì vậy, trong Thử thách người cho vay Luna, chúng tôi không có giới hạn rõ ràng và chúng tôi có các ngoại lệ.

### 00:03:51.000 - 00:03:56.000
Và do đó chúng ta phải sử dụng ở đây hàm trạng thái rời rạc được cập nhật một chút.

### 00:03:56.000 - 00:04:03.000
Và bây giờ nếu chúng ta kiểm tra ở đây giá trị ngoại lệ trừ một phẩy hai, thì nó vẫn nằm trong thùng số 0.

### 00:04:03.000 - 00:04:11.000
Chúng ta chỉ thấy trường hợp này. Vì vậy, điều này hoạt động. Và chúng ta sẽ tiếp tục ở đây với chức năng được cập nhật đôi chút này.

### 00:04:11.000 - 00:04:15.000
Cảm ơn các bạn đã theo dõi và hẹn gặp lại các bạn trong bài giảng tiếp theo. Tạm biệt.

