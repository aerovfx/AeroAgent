# Tổng quan triển khai đèn LED RGB 001 vi

---

Xin chào, chào mừng mọi người trở lại.

Chúng ta sẽ bắt đầu phát triển ứng dụng mạng cục bộ không dây bằng cách triển khai

Trạng thái Ogbe dẫn đầu.

Ông sẽ xem xét ngắn gọn các chi tiết thực hiện.

Vì vậy, hãy xem tổng quan về việc triển khai của chúng tôi.

Chúng ta sẽ tạo ra các màu khác nhau bằng cách sử dụng máu để biểu thị trạng thái ứng dụng.

Trước hết, hãy tạo một chức năng để khởi tạo cài đặt đèn led Ogbe cho mỗi kênh.

GPIO được sử dụng cho mỗi kênh và cũng định cấu hình bộ hẹn giờ.

Chúng ta sẽ tạo một chức năng khác để cài đặt màu dựa trên chu kỳ nhiệm vụ cho từng kênh, mỗi kênh.

kênh là các kênh màu đỏ, xanh lục và xanh lam sau đó sẽ tạo các chức năng đặt màu của

ogbia được sử dụng làm chỉ báo trạng thái ứng dụng của chúng tôi.

Cuối cùng, chúng tôi sẽ kiểm tra các chức năng này trong tệp chính xem và chúng tôi sẽ thực sự sử dụng chúng sau này để

cho biết các trạng thái như ứng dụng Wi-Fi đã khởi động khi máy chủ khởi động và kết nối Wi-Fi.

Bây giờ, hãy nói về thành phần kiểm soát được cho là của ESB IDF.

Tôi khuyên bạn nên truy cập tài liệu ấn tượng tại đây về thành phần LED và tài liệu tham khảo API tại đây

bạn có thể tìm thấy tất cả những gì bạn cần biết về Leidy Control bằng IDF.

Bạn sẽ thấy rằng thành phần này được thiết kế chủ yếu để kiểm soát cường độ đạo trình và tạo tín hiệu GWM.

Vì vậy, chỉ cần duyệt qua đây nếu bạn có thể.

Ngoài ra, bạn sẽ thấy rằng cả hai kênh tốc độ cao và tốc độ thấp đều có sẵn và có 16 kênh

tổng cộng tám cho tốc độ cao và tám cho tốc độ thấp.

Các bước cấu hình của chúng tôi bao gồm ba phần chính, cấu hình bộ hẹn giờ và kênh.

Sau đó thiết lập và cập nhật chu kỳ nhiệm vụ.

Vì vậy, về bộ đếm thời gian.

Mỗi bộ đếm thời gian đếm ngược và các bit được xác định sẽ xác định số đếm trước khi nó đặt lại và tần số

xác định lượng thời gian cần thiết để đếm thành số.

Ví dụ: ba tám bit, số đếm là từ 0 đến 255 và đối với mười bit, nó sẽ từ

không đến một nghìn hai mươi ba.

Và bit, số và tần số là thành phần chính của đèn LED, hãy xem cấu trúc cấu hình bộ hẹn giờ

sẽ được thiết lập, bao gồm cả các thành phần khác như chế độ tốc độ và số hẹn giờ.

Và chúng ta sẽ chuyển thông tin này tới đèn LED xem chức năng cấu hình hẹn giờ để thiết lập cấu hình.

Đối với cấu hình kênh, chân GPIO mà P.W. và tín hiệu đầu ra xuất hiện trên một chỉ định

đến một kênh cụ thể cùng với bộ hẹn giờ sẽ đặt các thành viên của đèn LED xem cấu trúc cấu hình kênh

và chuyển cấu hình sang cấu hình kênh kế thừa.

Và tiếp theo, chúng ta có thể tạo ra các màu khác nhau bằng cách điều chỉnh chu kỳ nhiệm vụ, đó là khoảng thời gian

trong khoảng thời gian mà tín hiệu đầu ra GWM sẽ ở mức cao trước khi xuống mức thấp.

Và chúng ta sẽ thực hiện việc này bằng cách sử dụng chức năng nhiệm vụ cài đặt của đèn LED và chức năng nhiệm vụ cập nhật của đèn LED.

Bây giờ, chúng ta hãy nhanh chóng tìm hiểu các chức năng màu dẫn trạng thái sẽ tạo.

Việc bắt giữ sẽ có một chức năng đặt màu bằng cách cập nhật chu kỳ nhiệm vụ trên mỗi kênh.

Các kênh màu đỏ, xanh lá cây và xanh lam và sau đó là chức năng trạng thái sẽ chỉ gọi hàm màu đã đặt

theo chu kỳ nhiệm vụ mà chúng tôi đã chỉ định cho mỗi kênh, tùy thuộc vào màu sắc mà chúng tôi muốn.

Bạn có thể truy cập liên kết này tại đây hoặc bất kỳ trang web tương tự nào khác.

Chỉ cần tìm kiếm lựa chọn màu sắc của đèn led RGV và bạn có thể tùy chỉnh đèn LED trạng thái theo ý muốn.

Tuy nhiên, đối với ba trạng thái Wi-Fi đã khởi động, máy chủ HTTP đã khởi động và kết nối Wi-Fi.

Tôi đã chọn các giá trị sau.

Tại sao nếu tôi bắt đầu, màu này lại ở đây?

Và máy chủ FTP trông như thế này.

Còn vợ, tôi nối nhìn giống màu này đây.

Vì vậy, hãy thoải mái thiết lập màu sắc theo ý muốn.

Hoặc tốt hơn nữa, hãy tạo các chức năng thỏa mãn nhu cầu của riêng bạn khi chúng tôi phát triển ứng dụng hơn nữa.

Hãy nói ngắn gọn về các tùy chọn phần cứng.

Có nhiều hương vị khác nhau của chúng tôi.

Bạn có thể lấy loại gói trên PCB hoặc cực âm chung hoặc Loại A. chung.

Bất cứ điều gì bạn có được.

Hãy nhớ kiểm tra bảng dữ liệu và xác minh các giá trị điện trở cần thiết và bạn có thể thực hiện các kết nối

dựa trên GPIO như chúng tôi xác định.

Ngoài ra, nếu bạn đang sử dụng loại A. thông thường, loại cực âm thông thường, hãy nhớ làm theo sơ đồ và lưu ý

sự khác biệt chân dài mặt đất so với điện áp dương.

Được rồi, chúng ta hãy bắt đầu với việc lập trình trong bài học sắp tới nhé.