## Nội dung

### 00:00:00.000 - 00:00:05.320
Bây giờ chúng ta hãy tiếp tục rời rạc hóa không gian trạng thái, đây là một bước rất quan trọng

### 00:00:05.320 - 00:00:12.400
 khi làm việc với các bảng Q. Vậy là chúng ta đã thấy rằng thực tế chúng ta có hai thông số trạng thái

### 00:00:12.400 - 00:00:20.440
 trong thử thách xe leo núi. Vì vậy, chúng ta có tham số X hiển thị vị trí

### 00:00:20.440 - 00:00:28.240
 của ô tô trên trục X và chúng ta có tham số vận tốc và chúng ta có thể nhận được ở đây

### 00:00:28.239 - 00:00:35.320
không gian quan sát, giá trị thấp và giá trị cao. Vì vậy, giá trị X có thể nhận các giá trị trong khoảng

### 00:00:35.320 - 00:00:42.439
âm 1,2 ở bên trái và cộng 0,6 ở bên phải. Vì vậy, việc đạt được

### 00:00:42.439 - 00:00:50.000
mục tiêu của mục tiêu và vận tốc, chúng ta có các giá trị trong khoảng âm 0,07 nên đi sang trái

### 00:00:50.000 - 00:00:57.519
 và cộng 0,07 đi sang phải và đây thực sự là những giá trị liên tục. Vì vậy, chiếc xe có thể

### 00:00:57.520 - 00:01:04.439
nhận bất kỳ giá trị nào, bất kỳ giá trị liên tục nào giữa các giới hạn ở đây. Vì vậy, có vô số

### 00:01:04.439 - 00:01:10.760
trạng thái tiềm năng và chúng ta đã thấy rằng khi thiết lập lại môi trường, chúng ta sẽ trở về trạng thái ban đầu

### 00:01:10.760 - 00:01:21.159
. Vì vậy, ví dụ trừ 0,46 cho trạng thái X và vận tốc 0 và điều này có thể thay đổi bất cứ khi nào

### 00:01:21.159 - 00:01:30.599
chúng tôi đặt lại môi trường. Vì vậy, đây là các giá trị liên tục nhưng nếu chúng ta muốn làm việc với bảng Q

### 00:01:30.599 - 00:01:40.640
 và học Q, chúng ta phải rời rạc hóa các giá trị liên tục thành các giá trị rời rạc để thành các chân và ví dụ 

### 00:01:40.640 - 00:01:48.840
 chúng ta có thể chọn 18 chân cho tham số X và 14 chân cho tham số vận tốc. Vì vậy

### 00:01:48.840 - 00:01:55.200
đây chỉ là điểm khởi đầu và sau này chúng ta sẽ thấy việc thay đổi và tối ưu hóa các chân

### 00:01:55.200 - 00:02:02.480
là rất quan trọng nhưng để bắt đầu, hãy bắt đầu với 18 chân và 14 chân và vì vậy, chúng ta

### 00:02:02.480 - 00:02:11.240
thực sự có thể tạo không gian quan sát để các chân đi vào giới hạn và ví dụ ở đây chúng ta

### 00:02:11.240 - 00:02:18.439
có không gian quan sát nên các chân cho tham số X để chúng ta có chân đầu tiên từ âm 1,2

### 00:02:18.439 - 00:02:28.719
đến âm 1,09 sau đó chúng ta có chân thứ hai giữa hai giới hạn này và cuối cùng là chân cuối cùng bắt đầu tại

### 00:02:28.719 - 00:02:38.199
0,6 nên điều này sẽ đạt đến mục tiêu. Vì vậy, tổng cộng chúng ta có ở đây 18 chân có chiều rộng bằng nhau trong khoảng từ âm 1,2 đến 

### 00:02:38.199 - 00:02:45.479
0,6, đây thực sự là những gì NP dot linspace làm và chúng ta cũng có thể làm điều tương tự đối với vận tốc.

### 00:02:45.479 - 00:02:58.959
Vì vậy, bắt đầu với chân đầu tiên từ âm 0,07 đến âm 0,05, v.v. và sau đó chúng ta cần một hàm

### 00:02:58.959 - 00:03:06.879
có thể chuyển đổi các trạng thái liên tục thành trạng thái rời rạc và ở đây chúng ta có thể sử dụng trạng thái rời rạc do người dùng xác định

### 00:03:06.879 - 00:03:13.960
 nên tôi không muốn để đi vào chi tiết ở đây nhưng hãy để tôi chứng minh tác dụng

### 00:03:13.960 - 00:03:21.919
 của hàm này để bây giờ chúng ta thực sự có thể chuyển một trạng thái liên tục như ở đây, trạng thái này vào hàm

### 00:03:21.919 - 00:03:30.400
 và hàm trả về các chân tương ứng hoặc số của số thùng và trong trường hợp này là

### 00:03:30.400 - 00:03:43.400
đối với tham số X, đó là thùng số 7, để tôi kiểm tra nên đây là chốt đầu tiên thứ hai thứ ba thứ tư thứ năm thứ sáu thứ bảy

### 00:03:43.400 - 00:03:53.040
giữa hai số này, đây là thùng số 7 và về vận tốc thì đó là thùng số 6 nên vận tốc là 0 là

### 00:03:53.039 - 00:04:02.120
bin số 6 trên 14 và thực ra chúng ta có thể kiểm tra thêm điều này bằng một số ví dụ khác để chúng ta không thể lấy

### 00:04:02.120 - 00:04:12.759
các giá trị cực trị như âm 1,2 ở bên trái và vận tốc bằng 0 và sau đó chúng ta nhận được các thùng 0 và 6 vậy

### 00:04:12.759 - 00:04:22.279
Ngoài ra, ở đây áp dụng lập chỉ mục dựa trên thùng 0 nên thùng đầu tiên có số 0 và sau đó nếu bạn đi

### 00:04:22.279 - 00:04:31.159
 nhiều hơn về bên phải, ví dụ trừ 1,0 thì chúng ta có thùng số 1 nên thùng thứ hai và nếu bạn thay đổi

### 00:04:31.159 - 00:04:42.039
ở đây vận tốc thành 0,01 thì chúng ta đang ở thùng số 7, v.v. vì vậy đây là sự rời rạc hóa trạng thái

### 00:04:42.039 - 00:04:50.239
có nghĩa là chúng ta chuyển đổi các trạng thái liên tục thành trạng thái rời rạc với các thùng nên thực tế là như vậy tất cả

### 00:04:50.240 - 00:04:55.040
và chúng ta tiếp tục ở đây trong bài giảng tiếp theo, cảm ơn vì đã xem và hẹn gặp lại ở đó, tạm biệt

