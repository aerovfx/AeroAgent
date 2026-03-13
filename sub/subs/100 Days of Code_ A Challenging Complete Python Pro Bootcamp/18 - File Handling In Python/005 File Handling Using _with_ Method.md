# 005 Xử lý tệp bằng phương pháp

---

Xin chào tất cả mọi người.

Chào mừng trở lại.

Trong bài học này, chúng ta sẽ xem cách sử dụng.

Phương pháp chiều rộng để xử lý.

Bất kỳ tập tin.

Chúng ta hãy bắt đầu với câu hỏi tại sao chúng ta sử dụng phương pháp nào để xử lý.

Bất kỳ tập tin.

Giả sử bạn đã mở một tệp bằng phương thức open.

Và.

Đã thực hiện một số hoạt động sau đó.

Bạn quên đóng file bằng phương pháp đóng dấu chấm.

Sau đó, ở chế độ nền, tập tin vẫn mở.

Và sau khi tắt máy tính hoặc tắt máy chủ hoặc.

Bất kỳ hệ thống nào thì tập tin có thể bị hỏng.

Vì vậy để tránh điều đó chúng ta sử dụng phương thức width với file đang mở as.

Tên tệp cho bộ đệm.

Trong trường hợp này, chúng tôi đang sử dụng tên tệp cho bộ đệm là tệp.

Chúng ta hãy sử dụng văn bản để chấm tệp txt ở chế độ đọc và ghi.

Là tệp có mở văn bản này thành tệp văn bản dưới dạng tệp ở chế độ đọc và ghi.

Vì vậy, đây là cách chúng ta có thể đọc cú pháp này với open.

Tệp dưới dạng tệp có chế độ đọc và ghi.

Hãy để chúng tôi mở tập tin và viết.

Một số dòng.

Leo lên cao và.

Trong.

Dòng thứ hai và thứ ba.

Tôi đang sử dụng.

Chào mừng bạn đến với Python dành cho các kỹ sư sử dụng phương pháp Writelines.

Chúng ta biết rằng phương thức Writelines sử dụng danh sách các dòng.

Và cuối cùng tôi đang đọc các dòng bằng phương pháp Readlines.

Sau khi đọc tập tin này mở.

Với phương thức open sẽ tự động đóng file lại.

Hãy thử sử dụng phương pháp dòng sau khi đóng tệp.

Bạn sẽ gặp lỗi.

Chúng tôi cũng có thể sử dụng.

Phương pháp đọc dấu chấm tập tin để đọc.

Nội dung bên trong tập tin.

Chúng ta có thể sử dụng câu lệnh in cho phép ngắt dòng tiếp theo, nghĩa là câu lệnh ngắt dòng và

hiển thị văn bản đẹp.

Bên trong bất kỳ tập tin.

Ví dụ: bên trong tệp Ext2 này, chúng ta có những dòng này.

Nếu chúng ta chỉ sử dụng .

Phương pháp đọc hoặc đọc dòng.

Những phương pháp đó sẽ hiển thị các bộ ngắt dòng.

Nhưng nếu bạn sử dụng câu lệnh print thì câu lệnh print này sẽ làm như vậy.

Bỏ qua dòng tiếp theo hoặc dấu ngắt dòng và hiển thị các dòng dưới dạng văn bản rõ ràng.

Và từng dòng một.

Chúng ta hãy sử dụng vòng lặp for để hiển thị từng dòng bằng câu lệnh print.

Tệp bằng để mở tệp ở chế độ đọc.

Đối với dòng trong tập tin.

Tên cho mỗi dòng trong tập tin.

Dòng in.

Do đó không có không gian.

Nhưng tập tin này có ngắt dòng.

Được rồi.

Và sau khi in từng dòng.

Chúng ta phải đóng tệp bằng cách sử dụng dấu chấm đóng tệp.

Hãy để chúng tôi chạy cái này.

Đây.

Chúng ta có thể thấy từng dòng bên trong tệp mà không cần ngắt dòng.

Và chúng ta hãy đóng tệp bằng cách sử dụng dấu chấm đóng tệp.

Vì vậy, đây là cách chúng ta có thể đọc từng dòng một bằng vòng lặp for.

Và với sự trợ giúp của câu lệnh in.

Tiếp theo chúng ta sẽ xem cách đọc một ký tự cụ thể trong file để đọc một ký tự cụ thể trong

tập tin.

Chúng ta có thể sử dụng.

Một giá trị số nguyên bên trong phương thức đọc.

Chúng ta hãy mở tệp văn bản hai chấm txt ở chế độ đọc.

Và chỉ đọc năm ký tự đầu tiên.

Tập tin chấm đọc.

Ở đây chúng ta có thể thấy năm ký tự đầu tiên để đọc phần còn lại của dòng.

Chúng ta có thể sử dụng phương pháp đọc dòng.

Phương pháp đọc dòng sẽ đọc phần còn lại của dòng.

Từ nơi nó dừng lại có nghĩa là từ nơi con trỏ nhấp nháy.

Sau khi đọc phương thức với năm ký tự, con trỏ sẽ.

Hãy chớp mắt ở vị trí này.

Để vượt qua các dòng còn lại hoặc để đọc phần còn lại.

Văn bản trong tập tin.

Khi chúng ta sử dụng phương pháp đọc dòng, phương pháp đọc dòng này sẽ phân tích văn bản từ đó.

Tệp mà con trỏ hiện đã sẵn sàng để đọc các dòng còn lại.

Vì vậy, sau phương thức đọc, con trỏ sẽ.

Ở vị trí này có nghĩa là sau này.

Tuyên bố.

Từ đây trở đi, phương thức Lines màu đỏ sẽ đọc toàn bộ văn bản.

Và.

Đọc các dòng.

Như một danh sách các dòng.

Hãy để chúng tôi đóng bằng cách sử dụng phương pháp đóng.

Chúng ta hãy xem cách đọc tệp với sự trợ giúp của phương thức ReadLine.

Và cũng có thể.

Để kiểm tra xem tập tin có thể đọc được hay không bằng phương pháp có thể đọc được.

Phương thức có thể đọc được này trả về true nếu đối tượng có thể đọc được.

Có nghĩa là nếu đó là một tập tin văn bản, có thể.

Đọc nếu đó là tệp hình ảnh chỉ có các giá trị nhị phân mà chúng tôi không thể đọc được.

Chúng ta hãy xem các phương thức có thể đọc, ghi và tìm kiếm này hoạt động như thế nào trên các tệp.

Hãy để chúng tôi mở tệp bằng phương thức mở ở chế độ đọc.

Và bây giờ áp dụng phương pháp có thể đọc được trên tệp này.

Trả về việc đối tượng có được mở để đọc hay không.

Nếu những bức tường.

Đọc sẽ tăng lên.

Một lỗi.

Đúng vậy.

Có nghĩa là chúng ta có thể đọc tệp vì tệp bao gồm các ký tự văn bản.

Bên trong đường màu đỏ nếu bạn sử dụng.

Kích thước bằng âm một.

Nó sẽ đọc và trả về một dòng từ chuỗi.

Nếu trang web được chỉ định ở hầu hết các trang web, byte sẽ được đọc.

Hãy để chúng tôi sử dụng.

Tập tin dấu chấm.

Đọc dòng.

Với n bằng trừ một hoặc kích thước bằng trừ một.

Vậy là chúng ta đã có được ký tự ở dòng đầu tiên.

Chúng ta hãy đọc các dòng còn lại bằng cách sử dụng phương thức dòng màu đỏ dòng chấm đọc tệp.

Đây là dòng thứ tư.

Tập tin tiếp theo chấm đọc dòng.

Đây là dòng thứ năm.

Tập tin tiếp theo chấm đọc dòng.

Dòng thứ sáu.

File tiếp theo Chấm dòng đọc.

Dòng thứ bảy.

Tập tin tiếp theo.

Chấm đọc dòng.

Dòng thứ tám.

Tập tin tiếp theo chấm đọc dòng.

PY và sau đó tập tin dot đọc dòng.

Chào mừng đến với Python.

Và tương tự, nếu chúng ta sử dụng thêm một phương pháp đọc dòng nữa, nó sẽ đọc cho các kỹ sư.

Chúng ta thử sử dụng lại phương thức ReadLine thì sẽ được.

Một chuỗi trống vì sau khi đọc hết nội dung.

Nó nằm trong tập tin văn bản.

Sau đó, phương thức dòng màu đỏ sẽ hiển thị.

Một chuỗi trống.

Hãy để chúng tôi xem.

Phương pháp cáp C trên tệp.

Phương thức có thể tìm kiếm này trả về true nếu tệp.

Luồng hỗ trợ truy cập ngẫu nhiên.

Nó trả về true nếu đối tượng hỗ trợ truy cập ngẫu nhiên.

Nếu tìm kiếm sai và cắt bớt sẽ gây ra lỗi.

Hãy để chúng tôi sử dụng phần tiếp theo trên tập tin này.

Chúng tôi đã đúng.

Có nghĩa là chúng ta có thể sử dụng phương thức tìm kiếm để đặt con trỏ ở một vị trí cụ thể.

Và cuối cùng chúng ta có phương pháp bảng phù hợp.

Phương thức này trả về việc đối tượng có được mở để ghi hay không.

Nếu sai, viết sẽ tăng lên.

Lỗi thiên vị.

Trong trường hợp này, chúng tôi đã mở tệp cho.

Phương thức chỉ đọc có nghĩa là chúng tôi đã mở tệp theo phương thức chỉ đọc.

Với more as hoặc nếu chúng ta cố gắng ghi tập tin này, chúng ta sẽ gặp lỗi.

Vì vậy phương thức Writeable sẽ kiểm tra xem file có thể được ghi hay không.

Nếu không viết được thì nó sẽ báo lỗi.

Hãy để chúng tôi chạy cái này.

Tệp dòng chấm có thể đọc được và xem sai có nghĩa là gì.

Chúng tôi không thể ghi vào tệp vì nó chỉ mở để đọc.

Chúng ta hãy thử viết một số nội dung.

Giống.

Dòng tiếp theo.

Đây là dòng cuối cùng.

Chúng tôi có thể gặp lỗi và chắc chắn chúng tôi sẽ gặp lỗi vì không thể ghi được vì đã có thể ghi được

phương pháp đã hiển thị lỗi ở dạng sai.

Có nghĩa là chúng tôi không thể ghi nội dung này vào tệp chỉ mở ở chế độ đọc.

Vì vậy, đây là cách chúng ta có thể làm việc với tệp.

Và đây là tất cả về cách xử lý tệp và tệp trong Python.

Tuy nhiên, chúng tôi có một số phương pháp xử lý tệp này.

Có nghĩa là các phương pháp tiên tiến.

Bạn sẽ thấy tất cả các phương pháp này khi làm việc với các dự án Python và chúng tôi sẽ giải thích tất cả

các phương pháp còn lại từng bước một mà không bỏ bất kỳ bước nào.

Hẹn gặp lại các bạn ở phần tiếp theo.