## Nội dung

### 00:00:00.000 - 00:00:01.000
Trong video này.

### 00:00:01.000 - 00:00:03.000
Chúng ta sẽ thực hiện phần đầu tiên.

### 00:00:05.000 - 00:00:07.000
Thuật toán củng cố.

### 00:00:10.000 - 00:00:15.000
Để làm điều đó, chúng ta sẽ tạo một hàm có tên Củng cố.

### 00:00:17.000 - 00:00:25.000
Và chức năng này sẽ lấy mạng lưới thần kinh chính sách của chúng tôi và một số tập cụ thể làm đầu vào

### 00:00:25.000 - 00:00:26.000
cũng như một giá trị cho Alpha.

### 00:00:28.000 - 00:00:30.000
Đó là tốc độ học tập của quy tắc cập nhật.

### 00:00:32.000 - 00:00:38.000
Và chúng ta sẽ khởi tạo giá trị này là dấu phẩy 0 0001.

### 00:00:40.000 - 00:00:44.000
Và tham số cuối cùng sẽ là gamma, như bạn đã biết, là hệ số chiết khấu.

### 00:00:48.000 - 00:00:50.000
Hãy tạo một số phòng.

### 00:00:53.000 - 00:00:58.000
Và bây giờ điều tiếp theo chúng ta sẽ làm là tạo đối tượng sẽ đảm nhiệm việc này.

### 00:00:59.000 - 00:01:02.000
Cập nhật các tham số của mạng nơ-ron.

### 00:01:04.000 - 00:01:10.000
Nó sẽ là một phiên bản của lớp Adam W, như bạn biết, là phiên bản cải tiến của lớp ngẫu nhiên

### 00:01:10.000 - 00:01:13.000
quy tắc cập nhật giảm độ dốc.

### 00:01:13.000 - 00:01:16.000
Đối với đối tượng này, chúng tôi sẽ chuyển dưới dạng đối số.

### 00:01:17.000 - 00:01:20.000
Một danh sách với các tham số của mạng lưới thần kinh.

### 00:01:24.000 - 00:01:29.000
Và một giá trị cho tốc độ học được áp dụng trong quy tắc cập nhật.

### 00:01:32.000 - 00:01:38.000
Điều tiếp theo chúng ta cần làm là khai báo một từ điển nơi chúng ta sẽ lưu trữ số liệu thống kê về việc thực thi

### 00:01:38.000 - 00:01:41.000
của thuật toán bên trong từ điển này.

### 00:01:41.000 - 00:01:48.000
Chúng tôi sẽ lưu trữ một mục nhập có tên khóa Los, nơi chúng tôi sẽ lưu trữ các giá trị của hàm chi phí sẽ được

### 00:01:48.000 - 00:01:49.000
được tối ưu hóa.

### 00:01:51.000 - 00:01:54.000
Và chúng ta sẽ khởi tạo mục này với một danh sách trống.

### 00:01:57.000 - 00:02:03.000
Và trong một mục khác, chúng tôi sẽ lưu trữ kết quả thu được trong mỗi tập.

### 00:02:04.000 - 00:02:08.000
Sau khi chạy thuật toán, chúng ta sẽ thấy các giá trị này bằng đồ họa.

### 00:02:10.000 - 00:02:14.000
Và bây giờ chúng ta có thể vào vòng lặp chính sẽ lặp lại trong một số tập.

### 00:02:34.000 - 00:02:41.000
Và để có thể theo dõi việc thực hiện vòng lặp này, chúng ta sẽ gói nó bằng hàm Tqdm sẽ

### 00:02:41.000 - 00:02:46.000
cung cấp cho chúng tôi một thanh tiến trình cho chúng tôi biết các lần lặp đã được thực hiện và những lần lặp còn lại.

### 00:02:49.000 - 00:02:55.000
Và điều tiếp theo chúng ta sẽ làm là sử dụng chính sách mạng nơ-ron để đối mặt với môi trường và thu thập

### 00:02:55.000 - 00:02:57.000
mẫu kinh nghiệm.

### 00:03:00.000 - 00:03:06.000
Chúng tôi sẽ thu thập một tập cho từng môi trường riêng lẻ trong môi trường song song.

### 00:03:11.000 - 00:03:15.000
Và để làm được điều đó, chúng ta sẽ khởi tạo môi trường song song.

### 00:03:16.000 - 00:03:22.000
Để nhận trạng thái ban đầu của từng môi trường riêng lẻ.

### 00:03:27.000 - 00:03:30.000
Sau đó chúng ta sẽ tạo một biến sẽ gọi.

### 00:03:31.000 - 00:03:32.000
Xong.

### 00:03:32.000 - 00:03:33.000
Là.

### 00:03:34.000 - 00:03:35.000
Thế là xong.

### 00:03:35.000 - 00:03:35.000
Hàng loạt.

### 00:03:39.000 - 00:03:44.000
Và trong biến này, chúng ta sẽ lưu trữ một vectơ cột chứa đầy các số 0.

### 00:03:46.000 - 00:03:52.000
Vì nó là một vectơ cột nên chúng ta sẽ gán cho nó các kích thước bằng số đầu và một.

### 00:03:54.000 - 00:03:56.000
Và chúng ta sẽ biến nó thành một tenxơ boolean.

### 00:03:59.000 - 00:04:01.000
Nhưng tại sao chúng ta lại làm điều này?

### 00:04:02.000 - 00:04:10.000
Biến này sẽ giữ một giá trị boolean, cho chúng ta biết liệu mỗi môi trường riêng lẻ trong

### 00:04:10.000 - 00:04:15.000
môi trường song song đã kết thúc tập hoặc nếu tập vẫn tiếp tục chạy.

### 00:04:16.000 - 00:04:19.000
Sử dụng biến này, chúng ta sẽ thực thi một vòng lặp bên trong.

### 00:04:20.000 - 00:04:27.000
Chúng tôi sẽ thu thập trải nghiệm từ tất cả các môi trường cho đến khi tất cả các phần tử bên trong biến này

### 00:04:28.000 - 00:04:29.000
là đúng.

### 00:04:31.000 - 00:04:34.000
Đó là cho đến khi tất cả các tập phim kết thúc.

### 00:04:36.000 - 00:04:41.000
Điều tiếp theo chúng ta sẽ làm là tạo một danh sách lưu trữ các chuyển đổi trạng thái.

### 00:04:45.000 - 00:04:54.000
Sau đó, chúng tôi sẽ tạo một biến gọi là lợi nhuận theo tập, trong đó chúng tôi sẽ theo dõi lợi nhuận thu được

### 00:04:54.000 - 00:04:57.000
trong từng tập riêng biệt.

### 00:04:58.000 - 00:05:02.000
Rằng tác nhân đang phải đối mặt với từng môi trường.

### 00:05:02.000 - 00:05:09.000
Và chúng tôi sẽ theo dõi những kết quả trả về này bằng cách sử dụng vectơ cột sẽ khởi tạo với giá trị bằng 0.

### 00:05:12.000 - 00:05:16.000
Và cũng với kích thước num và một.

### 00:05:19.000 - 00:05:23.000
Và bây giờ chúng ta có thể bước vào vòng lặp bên trong, nơi chúng ta sẽ tạo ra quỹ đạo của trải nghiệm.

### 00:05:28.000 - 00:05:31.000
Chúng tôi sẽ viết trong khi chưa hoàn thành.

### 00:05:32.000 - 00:05:32.000
Tất cả.

### 00:05:36.000 - 00:05:40.000
Và phương pháp cũ này, chúng ta chỉ có thể gọi nó trên các tensor boolean.

### 00:05:40.000 - 00:05:42.000
Và chúng tôi sẽ trở lại.

### 00:05:43.000 - 00:05:47.000
Liệu tất cả các giá trị bên trong tensor boolean đó có đúng hay không.

### 00:05:50.000 - 00:05:55.000
Vì vậy, trong khi tất cả các tập chưa kết thúc, giá trị của nó sẽ là sai.

### 00:05:56.000 - 00:06:02.000
Điều tiếp theo chúng ta sẽ làm là thực hiện hành động trong từng môi trường, chuyển qua cột

### 00:06:02.000 - 00:06:04.000
vectơ của các trạng thái đối với chính sách.

### 00:06:04.000 - 00:06:11.000
Vì chúng ta đang truyền một vectơ cột nên chính sách sẽ tính toán xác suất cho mỗi hành động đối với

### 00:06:11.000 - 00:06:13.000
mỗi hàng của vectơ cột.

### 00:06:13.000 - 00:06:16.000
Đó là, đối với mỗi trạng thái riêng lẻ.

### 00:06:17.000 - 00:06:20.000
Và bây giờ là chọn một hành động sử dụng những xác suất đó.

### 00:06:21.000 - 00:06:24.000
Chúng ta sẽ gọi phương pháp đa thức.

### 00:06:26.000 - 00:06:27.000
Và chúng ta sẽ vượt qua nó.

### 00:06:27.000 - 00:06:32.000
Giá trị một vì chúng tôi muốn chọn một hành động duy nhất cho mỗi trạng thái.

### 00:06:35.000 - 00:06:43.000
Ví dụ: hãy tưởng tượng rằng xác suất thực hiện hành động ở trạng thái là 0,1.

### 00:06:44.000 - 00:06:46.000
0,3.

### 00:06:47.000 - 00:06:48.000
0,5.

### 00:06:49.000 - 00:06:51.000
Và 0,1.

### 00:06:52.000 - 00:06:54.000
Bằng cách gọi đa thức.

### 00:06:54.000 - 00:06:59.000
Những gì chúng ta sẽ làm là chọn một hành động dựa trên những xác suất đó.

### 00:06:59.000 - 00:07:04.000
Hành động sẽ được chọn thường xuyên nhất là hành động số hai.

### 00:07:05.000 - 00:07:11.000
Bởi vì xác suất của nó là cao nhất nhưng những cái khác cũng có thể được chọn.

### 00:07:14.000 - 00:07:21.000
Vì chúng ta sẽ chọn nhiều hành động như các môi trường riêng lẻ mà chúng ta có, nên các hành động sẽ là

### 00:07:21.000 - 00:07:22.000
một vectơ cột.

### 00:07:24.000 - 00:07:26.000
Với hình dạng sau.

### 00:07:36.000 - 00:07:41.000
Trong đó mỗi hàng chứa hành động được thực hiện trong từng môi trường riêng lẻ.

### 00:07:45.000 - 00:07:50.000
Và đối với tensor hành động, chúng ta phải gọi phương thức tách rời.

### 00:07:52.000 - 00:08:00.000
Điều đó sẽ đảm bảo rằng PyTorch sẽ không đưa biến này vào quá trình truyền ngược.

### 00:08:00.000 - 00:08:02.000
sử dụng để cập nhật mạng lưới thần kinh.

### 00:08:04.000 - 00:08:10.000
Bây giờ, như mọi khi, những gì chúng ta phải làm là thực thi hành động này trong môi trường.

### 00:08:12.000 - 00:08:15.000
Và nhận được ngày tiếp theo và phần thưởng tương ứng.

### 00:08:16.000 - 00:08:22.000
Chúng ta sẽ gọi phương thức bước trên môi trường song song và chuyển nó thành tensor hành động.

### 00:08:25.000 - 00:08:28.000
Sau đó, chúng tôi sẽ lưu trữ quá trình chuyển đổi trạng thái này.

### 00:08:30.000 - 00:08:32.000
Trong danh sách chuyển tiếp.

### 00:08:36.000 - 00:08:38.000
Và chúng ta sẽ làm điều đó theo cách này.

### 00:08:50.000 - 00:08:52.000
Tại sao chúng ta lưu trữ phần thưởng theo cách này?

### 00:08:54.000 - 00:09:02.000
Chà, hãy nhớ rằng khi tập phim kết thúc, phần thưởng sau trạng thái kết thúc luôn bằng 0.

### 00:09:02.000 - 00:09:07.000
Biểu tượng này ở đây sẽ lật tensor donb.

### 00:09:07.000 - 00:09:11.000
Nghĩa là, nó sẽ làm cho các giá trị đúng là sai và các giá trị sai là đúng.

### 00:09:12.000 - 00:09:20.000
Và tác dụng của phép nhân này sẽ là chuyển thành số 0 tất cả các phần thưởng tương ứng với

### 00:09:20.000 - 00:09:23.000
môi trường có tập đã kết thúc.

### 00:09:23.000 - 00:09:29.000
Đó là môi trường có giá trị donbe là đúng.

### 00:09:31.000 - 00:09:34.000
Đây chỉ đơn giản là một điều chỉnh nhỏ mà chúng ta phải thực hiện.

### 00:09:35.000 - 00:09:40.000
Để có thể làm việc với nhiều môi trường cùng một lúc.

### 00:09:40.000 - 00:09:48.000
Điều tiếp theo chúng ta cần làm là cập nhật giá trị trả về để phản ánh phần thưởng mà chúng ta vừa thu thập được.

### 00:09:52.000 - 00:09:56.000
Và sau đó chúng ta sẽ cập nhật giá trị của biến donbe.

### 00:09:58.000 - 00:10:00.000
Và chúng ta sẽ thực hiện điều đó với thao tác này.

### 00:10:05.000 - 00:10:14.000
Đây là phép toán logic hoặc trả về true nếu giá trị của một hoặc giá trị của B là đúng.

### 00:10:16.000 - 00:10:24.000
Đó là những gì chúng tôi đang làm là cập nhật biến Don B để phản ánh các môi trường mà tập phim có

### 00:10:24.000 - 00:10:26.000
đã kết thúc sau động thái này.

### 00:10:27.000 - 00:10:31.000
Ví dụ: nếu môi trường thứ ba được thực hiện.

### 00:10:33.000 - 00:10:33.000
Sẽ sửa đổi.

### 00:10:33.000 - 00:10:38.000
Đừng để giá trị thứ ba của vectơ cột là đúng.

### 00:10:39.000 - 00:10:45.000
Bằng cách này, khi tất cả các giá trị trong Don B đều đúng, chúng ta biết rằng tất cả các môi trường.

### 00:10:45.000 - 00:10:47.000
Sẽ hoàn thành tập phim của họ.

### 00:10:51.000 - 00:10:54.000
Sau đó chúng ta sẽ cập nhật biến trạng thái.

### 00:10:56.000 - 00:10:57.000
Để trở thành trạng thái tiếp theo.

### 00:11:00.000 - 00:11:05.000
Và bây giờ chúng tôi đã hoàn thành việc thu thập kinh nghiệm từ tất cả các môi trường.

### 00:11:06.000 - 00:11:12.000
Trong video tiếp theo, chúng ta sẽ xem cách sử dụng trải nghiệm này để cải thiện chính sách mạng thần kinh.

### 00:11:12.000 - 00:11:13.000
Tôi sẽ gặp bạn ở đó.

