# 002 Cách đọc và ghi tệp hiện có hoặc tệp mới bằng Python

---

Xin chào tất cả mọi người.

Chào mừng trở lại.

Trong bài học này, chúng ta sẽ thấy.

Các phương pháp khác nhau để đọc và ghi các tập tin hiện có hoặc mới.

Ở bài trước chúng ta đã mở file rồi viết hai dòng.

Đây là dòng đầu tiên.

Trong văn bản một tệp và đây là một tệp văn bản dòng thứ hai.

Giả sử nếu chúng ta mở tệp ở chế độ chỉ đọc.

Và nếu bạn cố viết thì chúng ta sẽ gặp lỗi.

Ví dụ: chúng ta hãy mở tệp văn bản một dấu chấm txt ở chế độ chỉ đọc.

Và sử dụng phương thức read để đọc nội dung trong file.

Và nếu cố gắng viết đúng phương pháp thì chúng ta sẽ gặp lỗi.

Không thể ghi vì nó ở chế độ chỉ đọc.

Trước đó.

Chúng tôi đã mở tệp ở chế độ chỉ ghi và cố gắng đọc và gặp lỗi.

Bây giờ chúng ta đã mở file ở chế độ chỉ đọc.

Chế độ chỉ đọc.

Và.

Chúng tôi đang viết, đang cố gắng viết.

Vì thế.

Chúng tôi đang gặp lỗi, không thể ghi được.

Hãy để chúng tôi đóng tập tin này.

Như một kết luận.

Nếu chúng ta mở file ở chế độ chỉ đọc.

Nó sẽ chỉ cho phép đọc tập tin.

Mặt khác, nếu bạn mở tệp ở chế độ chỉ ghi.

Trình thông dịch sẽ chỉ cho phép ghi tập tin.

Không đáng đọc để làm cho trình thông dịch cho phép cả đọc và viết.

Chúng ta phải sử dụng chế độ đọc và viết.

Với sự trợ giúp của biểu tượng dấu cộng.

Những gì tôi đã đề cập ở bài học trước.

Đọc rồi viết.

Biểu tượng dấu cộng này được sử dụng cho.

Cả quyền truy cập đọc và ghi.

Nếu bạn dùng W thay vì R thì nghĩa của W và plus là đúng và đọc r plus có nghĩa là đọc và viết.

Đọc rồi viết.

W có nghĩa là ưu tiên cho việc viết và ưu tiên tiếp theo là cho việc đọc.

W có nghĩa là viết và dấu cộng có nghĩa là đọc.

Nếu chúng ta sử dụng dấu cộng trước R thì dấu chấm đầu tiên dành cho việc đọc và dấu chấm thứ hai dành cho việc ghi.

Đọc và viết.

Hãy để chúng tôi sử dụng cái này.

Hơn.

Để đọc tệp hiện có là văn bản một dấu chấm txt.

Và ở đây chúng ta có thể thấy hai đường thẳng không có khoảng cách nào.

Đây là dòng đầu tiên.

Và đây là dòng thứ hai.

Bây giờ chúng ta hãy viết một dòng.

Đối với tệp hiện có này với nội dung hiện có bằng cách sử dụng dòng mới.

Ký tự có dấu gạch chéo ngược n.

Điều này còn được gọi là ngắt dòng.

Hãy để chúng tôi nhập dòng.

Đây là dòng thứ ba sử dụng đúng phương pháp.

Và chúng ta hãy đọc.

Cái gì?

Ở đây chúng ta có thể thấy.

Không có gì.

Để đọc được, trước tiên chúng ta phải đóng tập tin.

Chúng ta chỉ cần đóng nó lại là đã đóng thành công.

Bây giờ chúng ta hãy mở tập tin.

Và sau đó đọc bằng phương thức open.

Vì vậy, ở đây chúng ta có thể thấy.

Ba dòng.

Dòng đầu tiên.

Dòng thứ hai.

Sau đó.

Đây là dòng thứ ba.

Phương pháp đọc này sẽ bao gồm ngắt dòng hoặc ký tự dòng mới.

Trong khi đọc nội dung của tập tin.

Nhưng nếu chúng ta sử dụng câu lệnh print thì câu lệnh print sẽ hiển thị.

Dòng thứ ba bên dưới hai dòng này vì câu lệnh print sẽ phát hiện dòng mới hoặc dấu ngắt dòng

bất cứ nơi nào chúng tôi sử dụng.

Và hiển thị các dòng.

Theo cách tiêu chuẩn.

Hãy để chúng tôi đóng tập tin này.

Bây giờ.

Chúng tôi đã thấy làm thế nào để.

Đọc và viết.

Sử dụng phương pháp R cộng.

Bây giờ chúng ta hãy xem cách viết và đọc bằng cách sử dụng.

Chế độ W cộng.

Phương thức W plus sẽ ghi đè lên dữ liệu hiện có rồi ghi đè lại file từ đầu.

Nó cho phép cả viết và đọc, nhưng ghi đè lên dữ liệu hiện có.

Vì vậy chúng ta phải cẩn thận về phương pháp này có nghĩa là chúng ta phải cẩn thận khi sử dụng phương pháp này.

Mặt khác, phương thức write và read sẽ đọc và ghi dữ liệu ở cuối nội dung.

Như vậy chúng ta đã thấy sau khi vào dòng thứ 3 thì đã có dòng.

Được chèn vào cuối nội dung nhưng trong phương thức WLS nó sẽ ghi đè lên dữ liệu hiện có.

Ví dụ: nếu chúng ta cố gắng viết dòng.

Đây là Portland ở dòng tiếp theo sử dụng ký tự ngắt dòng.

Sau đó chúng ta sẽ chỉ thấy dòng này.

Đây là dòng thứ tư.

Hãy để chúng tôi mở tập tin này đầu tiên.

Chúng tôi đã mở.

Hãy để chúng tôi viết dòng.

Đây là dòng thứ tư sử dụng đúng phương pháp.

Vì vậy chúng tôi đã viết dòng này.

Đây là dòng thứ tư.

Chúng ta hãy thử đọc.

Tệp sử dụng phương thức đọc.

Vì vậy chúng ta không thể nghiền ngẫm được vì phải đóng file lại rồi mới đọc.

Hãy để chúng tôi đóng lại.

Và sau đó.

Bây giờ chúng ta hãy mở tập tin.

Sử dụng phương pháp đọc này.

Và đọc tập tin.

Như vậy ở đây các bạn có thể thấy chúng ta chỉ có một dòng duy nhất vì dữ liệu hiện có đã bị ghi đè.

Đây là cách phương pháp cộng hoạt động.

Vì vậy chúng ta phải hết sức cẩn thận khi sử dụng phương pháp này.

Thêm vào đó.

Được rồi.

Hãy để chúng tôi đóng tập tin.

Vì vậy, chúng tôi đã đóng cửa.

Và cuối cùng, chúng ta chỉ có dòng thứ tư này là dòng thứ tư trong tệp văn bản của chúng ta.

Vì vậy hãy nhìn vào đây.

Đây là dòng thứ tư chúng tôi chỉ có.

Dòng này trong tập tin văn bản của chúng tôi.

Và nó nằm ở dòng tiếp theo vì chúng ta đã sử dụng dấu ngắt dòng.

Vì vậy, không phải ở dòng đầu tiên.

Nó nằm ở dòng thứ hai.

Ký tự chuỗi là dòng thứ tư này, nằm ở dòng thứ hai thay vì dòng đầu tiên vì

ngắt dòng mới.

Chúng ta đã thấy cách đọc và viết, cách viết và đọc.

Bây giờ chúng ta hãy xem.

Cách đọc từ đầu trong file.

Để đọc từ đầu.

Chúng ta cần di chuyển con trỏ đến điểm bắt đầu.

Vì lý do đó, chúng tôi sử dụng hai phương pháp đặc biệt có sẵn để xử lý tệp đó là phương pháp tìm kiếm và cho biết.

Phương thức tìm kiếm sẽ theo mặc định.

Giữ con trỏ ở đầu.

Nội dung tập tin.

Trong khi đó phương thức Tell sẽ cho chúng ta biết con trỏ ở đâu trong tệp tìm kiếm.

Tìm kiếm phương pháp sẽ.

Giữ con trỏ ở vị trí cụ thể.

Theo mặc định ở đầu tập tin.

Nếu bạn sử dụng bất kỳ giá trị số nguyên nào bên trong phương thức tìm kiếm này thì.

Con trỏ sẽ được đặt ở vị trí byte hoặc vị trí ký tự cụ thể đó.

Chúng ta hãy mở tệp văn bản một dấu chấm txt trong phương thức đọc và ghi và sử dụng phương thức .

phương pháp file.tel để xem ở đâu.

Con trỏ đang nhấp nháy.

Vì vậy hãy nhìn vào đây.

Hiện tại, con trỏ đang nhấp nháy ở vị trí byte thứ 0.

Chúng ta hãy đọc tập tin bằng phương thức read.

Chúng tôi đã thành công.

Đọc tập tin.

Bây giờ chúng ta hãy sử dụng phương thức Tell để xem con trỏ đang nhấp nháy ở đâu.

Vì vậy hãy nhìn vào đây.

Con trỏ nhấp nháy ở vị trí byte thứ 18 nghĩa là ở ký tự thứ 18.

Không một, hai, ba, bốn, năm, sáu, bảy, tám, chín, mười, 11, 12, 13, 14, 15, 16,

17, 18.

Chúng ta hãy sử dụng phương pháp tìm kiếm để đưa con trỏ của chúng ta đến.

Vị trí thứ 18.

Trở lại với.

Vị trí bắt đầu.

Bởi vì.

Mở tập tin văn bản.

Đóng cái này và mở tập tin.

Nhắn tin lại một tập tin.

Ở đây tôi đang sử dụng chuột để đặt con trỏ theo cách thủ công.

Nhưng.

Đây là.

Không phải.

Phương pháp xem con trỏ đang nhấp nháy ở đâu.

Phương pháp thực tế là hoặc thực sự là trình thông dịch.

Sẽ giữ con trỏ.

Sau khi đọc nội dung trong file chứ không phải từ chuột.

Được rồi, hãy ghi nhớ.

Bây giờ trong tệp text1 trình thông dịch đang lưu giữ.

Văn hóa ở vị trí thứ tám.

Chúng ta hãy sử dụng phương pháp tìm kiếm.

Để giữ con trỏ của chúng tôi trở lại vị trí bắt đầu.

Bằng cách chèn số 0 vào bên trong.

Phương pháp tìm kiếm.

Bây giờ con trỏ ở vị trí thứ 0.

Chúng ta hãy sử dụng phương pháp đuôi để.

Xem con trỏ ở đâu.

Vì vậy hãy nhìn vào đây.

Con trỏ bây giờ ở vị trí thứ 0.

Hãy để chúng tôi đóng tập tin bằng phương pháp đóng.

Vì vậy, đây là cách sử dụng phương pháp tìm kiếm và nói.

Sẽ cho chúng tôi biết về.

Vị trí con trỏ ở bên trong tập tin.

Điều này rất hữu ích khi viết một dòng mới bên trong tệp hoặc đọc từ vị trí cụ thể đó.

Cảm ơn đã xem bài học này.

Trong bài học tiếp theo chúng ta sẽ tiếp tục.

Đang làm việc.

Việc xử lý tập tin với các phương pháp khác nhau.