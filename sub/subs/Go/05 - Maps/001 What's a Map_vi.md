# 001 Bản đồ là gì vi

---

Được rồi, đã đến lúc chuyển sang các tính năng tiếp theo của chúng tôi trong Go.

Tôi rất hứng thú với chủ đề tiếp theo vì nó sẽ là một thứ có thể so sánh được

và lập luận với một trong những đặc điểm trước đây mà chúng tôi vừa nói đến, đó là Starbucks.

Vì vậy, trong phần này, chúng tôi sẽ nói về bản đồ.

Vì vậy, bản đồ cuối cùng sẽ rất giống với Starbucks.

Nhưng tôi chắc chắn rằng chúng tôi chỉ có nhiều điểm khác biệt giữa hai người.

Và Go a map là tập hợp các cặp giá trị chính.

Và vì vậy, nếu bạn đã quen với các ngôn ngữ khác như Ruby JavaScript, Python, bạn có thể nghĩ rằng một

bản đồ tương tự như hàm băm và Ruby là một đối tượng trong JavaScript hoặc một dict hoặc từ điển trong Python.

Bây giờ bạn sẽ nhớ lại rằng trong các loại bộ sưu tập video trước đó, tôi đã nói rằng cấu hình

trúc rất giống với những đối tượng chính này.

Và bây giờ tôi muốn nói, tốt, đây là thứ hai đặc biệt này rất giống với một

hàm băm và một đối tượng trong từ điển.

Vì vậy, trước tiên chúng tôi sẽ nói một chút về bản đồ chính xác là gì và một vài đặc điểm xung quanh

chúng.

Và sau đó, tôi sẽ cho bạn biết rất chi tiết về chúng khác với cấu trúc như thế nào và đi đến đâu cũng như nơi chúng tôi chọn để sử dụng

sử dụng cái này so với cái kia.

Vì vậy, điều đầu tiên tôi muốn bạn hiểu về bản đồ là cả khóa và giá trị đều được

nhập tĩnh.

Vì vậy, bất cứ khi nào chúng tôi thêm một số phím vào bản đồ và đi, tất cả chúng đều phải giống nhau về loại chính xác.

Và sau đó tất cả các giá trị khác nhau mà chúng tôi thêm vào cũng phải cùng loại.

Hiện tại, bản thân các khóa và giá trị không phải là cùng loại thiết bị, chỉ cần tất cả các giá trị

khác nhau.

Vì vậy, về cơ bản, chúng tôi đã nhận được một tập hợp các loại ở đây và sau đó là tập hợp các loại khác ở

đây ở phía chính.

Bây giờ, đối với bản đồ, thực tế không có gì thay thế cho công việc đó.

Một đoạn mã nhỏ hoặc chỉ được chơi với chúng.

Vì vậy, hãy chuyển sang mã thảo luận của chúng tôi và chúng tôi sẽ thực hiện một dự án nhỏ để

hiểu rõ hơn về cách chúng tôi tạo một bản đồ và cách chúng tôi vận hành chúng.

Vì vậy, tôi sẽ thay đổi điều chỉnh mã soạn thảo của mình và chúng tôi sẽ tạo một dự án thư mục

mới cho ví dụ mới này.

Vì vậy, tôi sẽ mở tệp.

Tôi sẽ tạo một thư mục mới có tên là Bản đồ và sau đó tôi sẽ mở thư mục đó.

Bây giờ bên trong đây, chúng tôi sẽ bắt đầu bằng cách tạo một tệp mới.

Vì vậy, dấu chấm chính sẽ đi và sau đó chúng tôi sẽ thiết lập sẵn bảng thông tin để bắt đầu tệp.

Vì vậy, chúng tôi cũng sẽ nói gói main và func main ở cùng.

Bây giờ tôi hy vọng sẽ phải ra một vài dòng mã khác nhau ở đây để chúng tôi có thể kiểm tra bản

đồ thị và tìm cách hoạt động chính xác của nó.

Vì vậy, tôi cũng sẽ nhập gói FMT ngay lập tức.

Được rồi.

Bây giờ có nhiều cách để khai báo một bản đồ và đi.

Vì vậy, chúng tôi sẽ bắt đầu bằng cách xem xét một số cách khai báo các bản đồ khác nhau.

Vì vậy, điều đầu tiên chúng ta sẽ xem xét là cú pháp theo nghĩa đen, rất đơn giản.

Vì vậy, chúng tôi sẽ tạo một bản đồ có tên là màu sắc và chúng tôi sẽ nói rằng cả khóa và giá trị

of it đều thuộc loại chuỗi.

Vì vậy, để nói rằng chúng tôi sẽ nói màu sắc sẽ được xác định cụ thể, bản đồ giá trị sẽ đóng dấu ngoặc vuông, chuỗi, chúng tôi sẽ đóng

chúng tôi quay lại và sau đó nói chuỗi thứ hai.

Bây giờ, điều này ngay tại đây nói rằng chúng tôi đang khai báo một bản đồ trong đó tất cả các khóa

trong bản đồ đều thuộc loại chuỗi và tất cả các loại chuỗi giá trị cũng thuộc loại.

Vì vậy, hãy tìm cách chúng tôi có thể thêm một số giá trị vào thứ này khi chúng tôi tạo bản đồ lần đầu tiên.

Vì vậy, tôi sẽ cung cấp cho nó một chuỗi làm chìa khóa màu đỏ.

Chúng tôi sẽ đặt dấu hai chấm và sau đó là giá trị mà chúng tôi muốn đặt giá trị này bằng cách sử dụng.

Vì vậy, hãy tưởng tượng trong vài giây lát rằng bản đồ của màu này sẽ bằng cách liên hệ tên của một

color with the hex code of the cùng màu đó.

Vì vậy, nếu bạn không quen thuộc với các mã màu hex, thì nó thực sự không tệ lắm.

Chúng ta có thể nói Mã hex đỏ và Google và nó sẽ cho chúng ta biết, đây, màu mã hex cho màu đỏ là f000.

Được rồi, hãy quay lại và nhập nó vào đây.

Vì vậy, nói f0000.

Bây giờ, chỉ cần rõ ràng, loại sinh vật màu đỏ này, mã màu của màu này chỉ là một ví dụ ở đây.

Tôi chỉ đang tưởng tượng rằng có lẽ chúng tôi muốn một loại bản đồ nào đó được tìm thấy, được đặt tên màu cho mã

hex của nó.

Vì vậy, không có công cụ thực sự nào có thể xảy ra ở đây.

Tôi chỉ muốn một ví dụ tốt.

Bây giờ chúng ta có thể thêm bao nhiêu cặp giá trị chính vào tùy chọn bản đồ này.

Chúng tôi chỉ cần phân tách từng mục nhập bằng comma để có thể đặt comma xuống và sau đó chúng có thể đạt được

muốn thêm màu xanh lục vào.

Và điều đó có thể tôi không biết, tôi chỉ tạo ra 745 ở đây.

Điều đó sẽ, điều đó sẽ hoạt động.

Và sau đó không giống như các ngôn ngữ khác và chúng tôi đã tìm thấy điều này với cấu trúc chỉ một giây trước đó, mỗi khóa giá trị cặp

đơn lẻ mà chúng ta thêm vào, chúng ta sẽ đặt dấu comma sau đó như vậy.

Vì vậy, điều này khai báo một bản đồ trong đó tất cả các khóa khác nhau đều là chuỗi và tất cả các giá trị cũng là chuỗi.

Vì vậy, bây giờ chúng tôi hãy sử dụng bản đồ này và chỉ cần xem điều gì sẽ xảy ra.

Vì vậy, tôi sẽ nói dòng FM màu tương tự, sau đó chúng tôi sẽ lưu tệp và chúng tôi sẽ chuyển sang thiết bị đầu cuối của chúng tôi và chạy điều

điều này và chỉ cần xem điều gì sẽ xảy ra.

Vì vậy, tôi sẽ thay đổi bản đồ.

Chúng tôi có tệp và chúng tôi sẽ chạy, chạy.

Dấu chấm chính, dấu chấm chính.

Đi.

Chúng ta bắt đầu.

Vì vậy, họ biết rằng đó là một bản đồ.

Chúng tôi có hai cặp giá trị chính.

Đầu tiên là màu đỏ.

Đây là giá trị.

Thứ hai là cây xanh lá và đây cũng là giá trị của màu đó.

Vì vậy, tôi nghĩ rằng họ đã có ít nhất một ý tưởng về cách họ tạo một bản đồ ở đây bằng cách sử dụng một cú đánh nhỏ

this first time.

Vì vậy, chúng tôi tạm thời nghỉ ngơi một chút, quay trở lại trong phần tiếp theo và chúng

ta cũng sẽ xem xét bổ sung hai cách khai báo và phân bổ bản đồ.

Vì vậy, hãy nhanh chóng nghỉ ngơi và tôi sẽ gặp bạn chỉ sau một phút.