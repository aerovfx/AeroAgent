# 002 Lập trình LED RGB

---

Được rồi.

Vì vậy, điều đầu tiên chúng ta cần làm ở đây là tạo hai tệp mới.

Vì vậy, hãy mở rộng thư mục dự án.

Và tại thư mục chính, nhấp chuột phải và chuyển đến tệp nguồn mới.

Và gọi nó là bóng bầu dục gạch dưới dẫn xem.

Và chọn mặc định.

Xem Nguồn.

Và bây giờ tạo phần đầu của tập tin.

Và gọi nó là đèn led gạch dưới bóng bầu dục và chọn mặc định.

Xem mẫu tiêu đề.

OC.

Tiếp theo chúng ta cần cập nhật file danh sách C và thêm file nguồn led GB nên chắc chắn đó là danh sách C

tập tin ở đây trên main.

Và thêm g B gạch dưới led C rồi lưu lại.

Vì vậy bây giờ chúng ta hãy chuyển sang tệp tiêu đề.

Vì vậy, ở đây trong tệp tiêu đề, chúng tôi sẽ định nghĩa GPO bóng bầu dục là số kênh bóng bầu dục, cấu hình

cấu trúc và nguyên mẫu cho các trạng thái màu sắc.

Vì vậy, hãy bắt đầu bằng cách xác định các GPO dẫn đầu môn bóng bầu dục.

Và chúng tôi sẽ nói xác định.

GP led đọc GPIO và sẽ sử dụng IO 21.

Bây giờ hãy xác định GPIO màu xanh lá cây dẫn bóng bầu dục.

Như tôi 22.

Vì vậy bây giờ hãy xác định màu xanh lam.

Và chúng ta có thể sử dụng 23.

Vì vậy, bây giờ ở đây chúng ta có thể xác định số lượng kênh.

Vì vậy, chúng tôi sẽ nói các kênh kết hợp màu sắc dẫn bóng bầu dục.

Và chúng tôi sẽ nói xác định.

G b led kênh số.

Và chúng ta sẽ có ba màu đỏ, xanh lá cây và xanh dương.

Vì vậy bây giờ hãy xác định cấu trúc cấu hình.

Chúng ta sẽ nói cấu hình led ruby.

Và chúng ta sẽ biến nó thành một cấu trúc typedef.

Và chúng ta sẽ có một kênh ở đây.

Nó có chế độ GPIO và INT.

Và chỉ số hẹn giờ.

Vì vậy bây giờ hãy gọi nó là thông tin ldl-c gạch dưới RT.

Bây giờ hãy sao chép cái này và chúng ta có thể tạo một mảng có cùng độ dài với số lượng kênh.

Chúng tôi có thể làm điều đó bằng cách sử dụng số kênh dẫn đầu GP của chúng tôi.

Được rồi, tuyệt vời.

Vì vậy bây giờ chúng ta cần nguyên mẫu cho các trạng thái màu sắc.

Vì vậy, điều đầu tiên chúng ta có thể làm là màu sắc để cho biết ứng dụng wi fi đã khởi động.

Vậy chúng ta hãy bình luận ở đây bằng màu sắc để biểu thị.

Ứng dụng WI fi đã bắt đầu.

Và giả sử ứng dụng wi fi void RG được dẫn dắt đã khởi động và không có tham số đầu vào.

Được rồi, màu tiếp theo sẽ là màu để cho biết máy chủ HTTP đã khởi động.

Và chúng tôi sẽ nói rằng máy chủ http dẫn đầu Gbps của chúng tôi đã bắt đầu.

Và điều này cũng vô hiệu.

Cuối cùng là màu để biểu thị rằng ESP 32 được kết nối với điểm truy cập.

Và điều này sẽ vô hiệu.

RG được dẫn wi fi kết nối và nó cũng vô hiệu.

Được rồi, thế thôi.

Vì vậy, bây giờ chúng ta có thể chuyển sang phần triển khai và tệp GB LMDC.

Được rồi.

Vì vậy, trước tiên hãy bao gồm std bool.

Và sau đó cũng bao gồm trình điều khiển cho DCH.

Và đây là dành cho trình điều khiển cũ.

Và cũng bao gồm tệp tiêu đề đèn LED bóng bầu dục ở đây.

Vì vậy, trước tiên chúng ta cần tạo một chức năng khởi tạo cài đặt đèn led bóng bầu dục cho mỗi kênh.

Bao gồm GPIO cho từng màu.

Chế độ và thời gian cấu hình.

Vì vậy, đây sẽ là một hàm tĩnh, nghĩa là nó bị hạn chế đối với tệp này và nó trả về void.

Gọi nó là rg be led p w m trong đó và nó trống rỗng.

Và ở đây tôi sẽ xác định một biến mà chúng ta sẽ sử dụng để lặp qua các kênh bóng bầu dục và có thể

là một int, gọi nó là dấu gạch dưới bóng bầu dục.

Và tại thời điểm này, chúng ta có thể định cấu hình cấu trúc kênh bóng bầu dục.

Chúng ta hãy đọc đầu tiên ở đây.

Vậy đó là dấu gạch dưới C, c.

H.

Đó là mảng mà chúng tôi đã tạo trong tệp tiêu đề.

Vì vậy, ở vị trí đầu tiên, hãy cập nhật kênh.

Và từ các nước LDC.

LÁI XE Chúng tôi sẽ sử dụng Kênh Zero.

Được rồi.

Vì vậy hãy chọn Kênh Zero.

Và hãy sao chép cái này.

Cập nhật GPIO khi RG được dẫn, đọc GPIO và đặt chế độ.

Đây là chế độ tốc độ cao.

Và đồng hồ bấm giờ.

Sẽ là thời gian hoặc bằng không.

Được rồi, vậy hãy chọn thời gian hoặc số không.

Bây giờ chúng ta có thể chăm sóc Kênh Xanh.

Vì vậy, đối với Kênh Xanh, đây sẽ là Kênh một.

Vì vậy hãy cập nhật tất cả các thành viên lên kênh một.

Và đó sẽ là Kênh EDC.

Và GPIO phải có màu xanh.

Vì vậy, tiếp theo, hãy cập nhật kênh màu xanh.

Và đây là câu chuyện tương tự ở đây.

Vì vậy hãy cập nhật kênh cho từng thành viên cấu trúc.

Số kênh cũng nên được chuyển đến.

GPIO có màu xanh lam.

Và tại thời điểm này, chúng ta có thể cấu hình bộ hẹn giờ.

Vì vậy, hãy cấu hình bộ đếm thời gian bằng không.

Và sẽ chỉ định cấu hình cấu hình bộ đếm thời gian.

Từ trình điều khiển LMDC.

Được rồi.

Và gọi nó là bộ đếm thời gian gạch dưới EDC.

Và chúng tôi sẽ cập nhật nghị quyết về nghĩa vụ thành viên đầu tiên.

Như la bộ đếm thời gian EDC.

Tám bit.

Và bây giờ là thành viên tần số ở đây, 100 hertz là đủ nhanh.

Và đối với chế độ tốc độ.

Sử dụng chế độ tốc độ cao LED DC.

Và thời gian là một con số.

Sẽ được dẫn DC Hẹn giờ số 0.

Được rồi, đó là tất cả cho bộ đếm thời gian.

Và bây giờ chúng ta có thể gọi cấu hình bộ đếm thời gian EDC.

Cái này ở đây và sau đó chuyển một tham chiếu đến cấu trúc.

Được rồi.

Vì vậy, cuối cùng, hãy định cấu hình các kênh dựa trên cài đặt kênh bóng bầu dục mà chúng ta vừa thực hiện.

Vì vậy, chúng ta sẽ lấy biến này ở đây và sẽ sử dụng nó để tăng dần qua các kênh.

Vì vậy, ở đây chúng tôi sẽ nói cấu hình các kênh.

Và giả sử biến FF bằng 0.

Bốn kênh bóng bầu dục ít hơn tổng số kênh.

Chúng tôi sẽ tăng dần thông qua các kênh.

Và ở đây chúng ta cần cập nhật cấu hình kênh EDC từ trình điều khiển.

Và gọi nó là kênh.

Và chúng tôi sẽ cập nhật thành viên kênh.

Sử dụng biến tăng đó.

Giống như vậy.

Và đối với nghĩa vụ, chúng ta có thể để nó bằng 0.

Và đối với thành viên điểm H, chúng ta cũng có thể tính số 0 đó.

Và tiếp theo, chúng ta có thể cập nhật số GPIO bằng cách sử dụng cài đặt của mình và biến tăng dần.

Và loại ngắt phải bị tắt, chúng ta có thể lấy từ trình điều khiển.

Ngắt, vô hiệu hóa.

OC và đối với chế độ tốc độ, chúng tôi cũng có thể lấy chế độ đó từ cài đặt của mình.

Sử dụng biến kênh bóng bầu dục.

Ngoài ra bốn giờ chọn.

Điều này có thể được cập nhật bằng cách sử dụng cài đặt của chúng tôi ở trên.

Từ chỉ số hẹn giờ.

Được rồi, tuyệt vời.

Như vậy bây giờ chúng ta có thể gọi hàm cấu hình kênh DC.

Và sau đó chuyển một tham chiếu đến cấu trúc.

Điều này sẽ được thực hiện cho mỗi lần lặp qua vòng lặp và tiếp theo sẽ xử lý việc khởi tạo các kênh p w m GB của chúng tôi.

Vì vậy, tiếp theo chúng ta sẽ xử lý chức năng thiết lập màu sắc.

Vì vậy, hãy đưa ra một bình luận ở đây.

Đặt màu bóng bầu dục.

Được rồi, đây là khoảng trống tĩnh.

Bộ màu đèn led bóng bầu dục và đó là loại UNT tám cho màu đỏ cũng như cho các kênh màu xanh lá cây và xanh lam

cũng vậy.

Vì vậy, ở đây chúng tôi đã chỉ định loại đầu vào khi bạn tiến hành tám vì chúng tôi đã chỉ định độ phân giải nhiệm vụ là

tám bit.

Do đó, giá trị chu kỳ nhiệm vụ có thể nằm trong khoảng từ 0 đến 255.

Được rồi.

Vì vậy, hãy đưa ra một bình luận ở đây.

Giá trị nên được.

0 đến 255 cho số 8 bit.

Và chúng ta sẽ sử dụng hàm nhiệm vụ đặt D.C.

Từ người lái xe và người vượt tốc độ, hãy xem Kênh Zero.

Đối với chế độ tốc độ và EDC Channel Zero.

Là kênh.

Và đây là Kênh Đỏ.

OC nên bây giờ hãy gọi cho DC.

Nhiệm vụ cập nhật từ tài xế.

Và về tốc độ, hãy xem lại Channel Zero.

Và hãy xem.

Kênh số 0 cho kênh đó.

Được rồi.

Vì vậy, chỉ cần sao chép hai dòng này và chúng ta có thể chăm sóc Kênh một và chỉ cần cập nhật tham số màu

màu xanh lá cây và sau đó kênh là một.

Vì vậy bây giờ hãy làm tương tự cho kênh màu xanh.

Thay đổi kênh này thành kênh hai.

Và bây giờ đây là màu xanh lam.

Được rồi, đó là chức năng màu được thiết lập GB của chúng tôi.

Bây giờ hãy tạo màu trạng thái mà chúng ta sẽ sử dụng trong ứng dụng.

Vì vậy, hãy đi đến phần đầu của tập tin.

Và sao chép những nguyên mẫu này.

Và sau đó dán chúng vào tập tin C.

Hãy loại bỏ những nhận xét này vì chúng đã có trong tệp tiêu đề nên chúng tôi không cần chúng ở đây.

Vì vậy, để bắt đầu wi fi, chúng tôi sẽ gọi hàm GB led p w init của mình.

Và sau đó chúng ta sẽ thiết lập màu sắc.

Tôi đã đề cập trong video giới thiệu và đó là 250 5102 và 255.

Đó là loại màu đỏ tươi mà tôi đã giới thiệu.

Và hàm này chúng ta chỉ cần gọi nó một lần.

Vì vậy, chúng ta cần một biến toàn cục để cho biết liệu nó đã được khởi tạo hay chưa.

Vì vậy chúng ta sẽ nói xử lý cho RGV.

Dẫn P.W. và trong đó.

Và nói bull và gọi nó là g, gạch dưới p w và nó xử lý và khởi tạo nó thành false.

Và hãy sử dụng cái này ở đây và đặt nó thành true trước khi hàm này hoàn thành.

Được rồi.

Và sau đó hãy quay lại đây.

Và kiểm tra xem nó chưa được khởi tạo hay chưa.

Và nếu không?

Sau đó chúng ta sẽ tiếp tục và khởi tạo bằng cách gọi hàm.

Vì vậy, sao chép tương tự và làm điều này cho máy chủ http bắt đầu.

Và sau đó cập nhật màu sắc theo ý muốn.

Tôi sẽ sử dụng màu hơi vàng mà tôi đã trình bày trước đó.

Lại.

Đặt màu kết nối Wi-Fi của bạn.

Tôi sẽ sử dụng màu hơi xanh lục mà tôi đã trình bày trước đó.

Được rồi.

Đúng.

Thế là xong.

Bạn có thể xác định một số macro cho các giá trị màu này khi bạn biết mình muốn gì, chỉ để bạn

không sử dụng những con số kỳ diệu này như chúng ta đang làm ở đây.

Vì vậy, bây giờ, hãy kiểm tra những điều này trong tệp chính.

Và để làm được điều đó, chúng ta sẽ cần đưa vào file GP led.

Và chỉ cần đặt chức năng trạng thái ở đây.

Nói rg được dẫn wi fi lên bắt đầu.

Và thay đổi độ trễ thành 1000 mili giây.

Và bây giờ chúng ta có thể khởi động máy chủ HTTP dẫn đầu GP.

Và sau đó thêm một độ trễ khác.

Và sau đó chúng tôi cũng muốn kiểm tra chức năng kết nối wi fi của đèn led bóng bầu dục.

Và chúng ta có thể thêm vào đây một độ trễ khác.

Vì vậy, màu sắc sẽ thay đổi ở khoảng thời gian này.

Vì vậy bây giờ hãy tiếp tục và xây dựng dự án.

Và chỉ cần cho nó một phút.

Vì vậy, sau khi quá trình xây dựng hoàn tất, chúng ta hãy flash bộ công cụ phát triển.

Và tôi đã cắm cổng của mình vào một cổng khác nhưng đó không phải là vấn đề.

Tôi có thể cập nhật nó dễ dàng bằng cách lên đây và sau đó thay đổi cổng từ bộ rover của mình.

Và sau đó chúng ta có thể nhấn flash lại.

Được rồi, bây giờ chúng ta hãy kiểm tra đèn led bóng bầu dục.

Mát mẻ.

Vậy là chúng ta đã bắt đầu kết nối Wi-Fi, máy chủ web đã khởi động và trạng thái kết nối Wi-Fi đều sáng, vì vậy

đèn LED trạng thái của chúng tôi sẽ phù hợp để sử dụng trong phần tiếp theo.

Hãy thiết lập và chạy Wi Fi.

Vậy tôi sẽ gặp bạn ở đó.