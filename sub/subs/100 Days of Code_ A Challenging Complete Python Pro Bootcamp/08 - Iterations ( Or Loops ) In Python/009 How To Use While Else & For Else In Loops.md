# 009 Cách sử dụng While Else & For Else trong vòng lặp

---

Xin chào tất cả mọi người.

Chào mừng trở lại.

Trong video này chúng ta sẽ nói về.

Cách sử dụng.

Trong khi đó và cho những người khác.

Trong các chương trình Python.

Các vòng lặp Python hỗ trợ một khối else tùy chọn.

Màu đen trong bối cảnh vòng lặp cung cấp mã để thực thi khi vòng lặp thoát.

Thông thường, nếu chúng ta nói điều này theo cách khác, mã trong vòng lặp màu đen khác sẽ không được thực thi.

Nếu vòng lặp kết thúc do có lệnh break.

Vì vậy đây là lợi thế.

Ồ, một khối khác có nghĩa là bất cứ khi nào.

Vòng lặp.

Phát hiện có nghĩa là khi luồng chương trình phát hiện câu lệnh break bên trong vòng lặp và nếu.

Vòng lặp bao gồm phần khác.

Sau đó, phần khác sẽ được đánh giá và luồng chương trình.

Sẽ không.

Bỏ qua phần khác.

Vì vậy, đây là ý nghĩa khi vòng lặp while thoát ra do điều kiện của nó sai trong quá trình kiểm tra thông thường.

Khối else liên quan của nó được thực thi.

Vì vậy, đây là ý nghĩa.

Điều này đúng ngay cả khi điều kiện của nó được phát hiện là sai trước khi phần thân của nó có cơ hội thực thi.

Chúng ta hãy xem thực tế cách thức hoạt động của while else và for else trong Python.

Nếu bạn nhìn vào ví dụ.

Mà chỉ tính những số dương.

Với số và tổng ban đầu bằng 0, trong khi số đếm nhỏ hơn năm.

Nhận giá trị từ người dùng.

Giá trị nhỏ hơn 0.

Phá vỡ.

Thực hiện các câu lệnh còn lại vì chúng ta đã sử dụng phần khác.

Phần này sẽ luôn được đánh giá, ngay cả khi luồng chương trình phát hiện câu lệnh break.

Vì vậy, thỉnh thoảng chúng ta hãy chạy mã này và xem nó hoạt động như thế nào.

Chúng ta hãy nhập các số dương hai và sáu.

Và một số âm là số âm.

Một.

Nhìn vào đây.

Số âm không được chấp nhận và chấm dứt.

Đây.

Chúng tôi chưa có được.

Trung bình bằng tổng theo số đếm.

Điều này là do.

Như chúng tôi đã nói trước đó, khi vòng lặp while thoát ra do điều kiện của nó sai trong quá trình kiểm tra thông thường.

Được rồi, bình thường, hãy kiểm tra khối else liên quan của nó sẽ thực thi.

Đây.

Đây không phải là kiểm tra thông thường.

Vì tôi đã nhập số âm trừ một nên câu lệnh phanh sẽ thoát ra khỏi vòng lặp.

Phần khác này sẽ đánh giá.

Và thực hiện các câu lệnh khi điều kiện sai.

Trong quá trình kiểm tra bình thường của nó.

Điều gì tạo nên sự kiểm tra bình thường đó?

Hãy để chúng tôi chạy lại mã này và kiểm tra xem nó hoạt động như thế nào.

Nhìn vào đây.

Tôi muốn vào.

Số sinh học.

Sau khi nhập năm số, giá trị đếm.

Trở thành số cộng một có nghĩa là sáu.

Khi số đếm trở thành sáu.

Điều kiện này trở thành sai.

Ngay cả điều kiện này cũng trở thành sai.

Phần khác này sẽ được đánh giá.

Đó không là gì ngoài việc kiểm tra thông thường.

Khi điều kiện sai trong quá trình kiểm tra thông thường, đó là ý nghĩa.

Hãy để chúng tôi.

Bắt đầu chỉ nhập số dương vào.

Ba.

ĐẾN.

Hai và hai.

Nhìn vào đây.

Sau khi kết thúc việc nhập năm số dương, đây là phép lặp bình thường.

Không có vấn đề kích hoạt câu lệnh ngắt vì tôi chỉ nhập số dương.

23222.

Số lượng sẽ tăng lên.

Đếm bằng đếm cộng một.

Nó sẽ đếm số lượng giá trị được người dùng nhập vào.

Khi tôi nhập số thứ năm.

Đếm trở thành đếm cộng một.

Đó là năm cộng một sáu.

Khi số đếm trở thành sáu, điều kiện while này trở thành sai.

Khi điều kiện while trở thành sai thông thường.

Sau đó, phần khác sẽ được đánh giá.

Khi điều kiện while trở thành sai thông thường thì chỉ khi đó phần else mới được đánh giá.

Có nghĩa là điều kiện phải trở thành sai.

Thông thường.

Nhưng nếu điều kiện không trở thành sai một cách bình thường và bên trong.

Nếu luồng chương trình hoặc luồng điều khiển phát hiện câu lệnh break thì luồng điều khiển sẽ chấm dứt.

Các câu lệnh còn lại của vòng lặp while, bao gồm cả phần else.

Có nghĩa là phần khác sẽ không được đánh giá.

Elsbeth sẽ chỉ được đánh giá nếu điều kiện trở thành sai.

Thông thường.

Có thể tự nhiên hơn khi đọc từ khóa LS cho câu lệnh while như thể không có câu lệnh break.

Nếu không nghỉ.

Tuyên bố.

Nếu không có nghĩa là ngắt, hãy thực thi mã trong khối khác.

Nếu việc thực thi mã của chương trình trong khối while không gặp phải câu lệnh break, thì

khối else là không cần thiết.

Chúng ta có thể sử dụng câu lệnh if else để đạt được hiệu quả tương tự.

Có nghĩa là chúng ta có thể thay thế phần else của vòng lặp while bằng câu lệnh if else.

Vì vậy, chúng tôi đang sử dụng câu lệnh if.

Thay vì phần khác.

Đến đây chương trình vẫn như cũ.

Nhưng bên trong phần else thay vì else, chúng ta đang sử dụng if else.

Tuyên bố.

Nếu số lượng ít hơn năm thì in số âm không được chấp nhận và chấm dứt.

Hét lên chạy nước rút.

Mức trung bình.

Hãy để chúng tôi chạy mã này và xem nó hoạt động như thế nào.

Hãy nhập các số dương vào.

Ba.

Năm.

Năm.

Khi tôi nhập năm số dương.

Cái.

Mỗi môn thể thao sẽ được đánh giá vì khi nào số lượng trở thành.

Lớn hơn năm.

Điều kiện này nếu điều kiện trở thành sai.

Nếu số lượng ít hơn năm.

Khi điều kiện if này trở thành sai, phần khác sẽ được đánh giá.

Tôi nghĩ đó là một.

Không cần thiết phải sử dụng phần if khác.

Nếu bạn muốn làm bất kỳ điều gì cụ thể.

Hoạt động.

Trước khi đến phần khác.

Chúng ta có thể sử dụng câu lệnh if else này.

Nếu không thì câu lệnh else này là vừa đủ.

Làm cụ thể.

Hoạt động trong vòng lặp while.

Tương tự như vòng lặp while ở câu lệnh đầu tiên.

Với một khối khác hoạt động.

Tương tự như câu lệnh while else.

Và chương trình này minh họa.

Cách khối else hoạt động với vòng lặp for.

Chúng ta đã biết cách đếm các nguyên âm trong bất kỳ chuỗi nào.

Ở đây chúng tôi chỉ sử dụng phần khác.

Để in.

Các nguyên âm đếm.

Thay vì chỉ sử dụng câu lệnh print, chúng ta đang sử dụng câu lệnh else và bên trong câu lệnh else

chúng tôi đang sử dụng.

Tuyên bố in.

Hãy để chúng tôi chạy mã này.

Và nhập vào.

Sợi dây.

Bạn có ba nguyên âm và A được lặp lại.

Thực ra nó cũng phải kiểm tra cho bạn nữa.

Xin lỗi vì sự bất tiện này.

A W.

Vậy là bốn nguyên âm và A đã được lặp lại.

Hãy để chúng tôi chạy lại mã này và.

Kiểm tra giá trị X.

Là nhiệm vụ của Jack thay vì G nên ta có X.

Vì vậy hãy nhìn vào đây.

X không được phép.

Câu lệnh in này nằm bên trong câu lệnh if đầu tiên đã được hiển thị.

Ơi tôi.

A.

Và.

Điều kiện ElseIf đang hiển thị.

X không được phép.

Nhưng những gì sẽ được tính là không được hiển thị?

Điều này là do khi chương trình tìm hoặc phát hiện X thì có sự kết thúc vòng lặp bất thường chứ không phải

chấm dứt vòng lặp bình thường.

Khi vòng lặp.

Phát hiện câu lệnh break.

Nó chấm dứt vòng lặp một cách bất thường.

Phần else này sẽ được đánh giá nếu không có câu lệnh break.

Đó là ý nghĩa.

Nếu không có câu lệnh break thì phần else sẽ được đánh giá theo cách khác để thực hiện lệnh break này

tuyên bố không hoạt động.

Giống như không có tuyên bố phá vỡ.

Chúng ta có thể tránh sử dụng

Những thứ kia.

Ví dụ: Word có chữ X.

Hãy để chúng tôi chạy lại điều này.

Và chỉ cần nhập này.

Pertwee có.

Bây giờ hãy nhìn vào đây.

Không có câu hỏi nào về X, chỉ có câu lệnh if này.

Tích cực.

Và câu lệnh này không hoạt động và câu lệnh break cũng không hoạt động.

Mặc dù các lần lặp đã được hoàn thành trong vòng lặp for nhưng khi tất cả các lần lặp đã được thực hiện

thông thường thì phần khác sẽ được đánh giá.

Vì vậy, bên trong phần chúng tôi đã hoan nghênh và câu lệnh in này sẽ hiển thị số lượng từ.

Vì vậy, đây là cách phần khác hoạt động.

Vòng lặp Python.

Phần khác sẽ chỉ được đánh giá nếu điều kiện trở thành sai.

Bình thường không có gì bất thường.

Bất thường có nghĩa là với câu lệnh break.

Thông thường có nghĩa là.

Sau tất cả các lần lặp hoặc không gặp câu lệnh break hoặc không gặp câu lệnh break

không có câu lệnh break, ngay cả khi có câu lệnh break, nó sẽ không hoạt động.

Nếu nó đang hoạt động thì phần khác sẽ bị bỏ qua.

Vì khi câu lệnh break được kích hoạt thì nó sẽ thoát khỏi vòng lặp.

Bất kể bên kia có mặt hay không.

Phần else sẽ chỉ được đánh giá và thực thi nếu không có câu lệnh break hoặc thậm chí nếu lệnh break

tuyên bố có mặt và nó không hoạt động.

Vì vậy, phải cẩn thận để thực hiện phần khác.

Khi chúng ta sử dụng câu lệnh break và đây là tất cả về cách hoạt động của phần else trong vòng lặp while và

vòng lặp for trong các bài học tiếp theo chúng ta sẽ thấy.

Vòng lặp vô hạn là gì và chúng hoạt động như thế nào