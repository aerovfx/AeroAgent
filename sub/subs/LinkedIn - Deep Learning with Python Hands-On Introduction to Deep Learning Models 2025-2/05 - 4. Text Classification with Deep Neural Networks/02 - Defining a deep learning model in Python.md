# 02 - Xác định mô hình deep learning trong Python

---

- [Người hướng dẫn] Trong video này, bạn sẽ học cách

để xác định mô hình học sâu trong Python bằng Keras.

Tôi sẽ chạy mã hoàn chỉnh trong tệp điện tử 04_02.

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp B 04_02.

Lưu ý rằng đây là video thứ hai trong chuỗi ba video

nó dạy bạn cách xây dựng

một mô hình học sâu bằng Python sử dụng Keras.

Nếu chưa hãy xem video trước

để được giải thích chi tiết về mã trước đó.

Trước khi bắt đầu, hãy chạy mã chúng tôi đã tạo trong video đó

để môi trường của chúng ta tăng tốc.

Vì vậy tôi sẽ đến đây để giải mã.

Vì vậy, chúng ta sẽ chạy tiếp theo và nói Thực thi trên các ô.

Vì vậy, nó sẽ chạy mọi thứ ở trên.

Chúng ta sẽ đợi việc đó hoàn tất,

và khi việc đó hoàn tất, chúng ta có thể tiếp tục.

Các ô trước đó đã được thực hiện.

Được rồi, vậy chúng ta sẽ,

"Xác định kiến trúc mô hình."

Kiến trúc của mạng nơ-ron xác định cách truyền dữ liệu

thông qua mô hình, các lớp được kết nối như thế nào,

và những hoạt động nào được thực hiện.

Đối với mô hình của chúng tôi, chúng tôi sẽ sử dụng API tuần tự trong Keras,

cho phép chúng ta xây dựng các mô hình theo từng lớp.

Vì vậy, chúng ta bắt đầu bằng việc khởi tạo mô hình Tuần tự.

Vì vậy chúng ta sẽ gọi hàm Tuần tự

và điều đó khởi tạo mô hình của chúng tôi.

Sau đó chúng ta chỉ định hình dạng của dữ liệu đầu vào.

Điều này đại diện cho lớp đầu vào.

Vì vậy, chúng ta sẽ sử dụng phương thức model.add,

và chúng ta sẽ chỉ định hình dạng của dữ liệu đầu vào.

Vì vậy, chúng tôi sẽ chạy nó.

Tiếp theo, chúng tôi thêm hai lớp được kết nối đầy đủ hoặc dày đặc.

Lớp đầu tiên sẽ có 512 nơ-ron,

trong khi lớp thứ hai sẽ có 128 nơ-ron.

Chúng tôi cũng sẽ sử dụng Đơn vị tuyến tính chỉnh lưu

chức năng kích hoạt cho cả hai lớp này.

Vì vậy, hãy tiếp tục và chạy nó.

Được rồi, chúng tôi ở đây cũng ổn.

Thông báo cảnh báo này không sao cả nên đừng lo lắng về nó.

Đối với mô hình đơn giản này, chúng tôi sẽ giới hạn kiến trúc

thành hai lớp ẩn, đó là những gì chúng ta vừa thực hiện.

Vì vậy chúng ta hãy nhớ rằng đối với một số mô hình phức tạp

chúng ta có thể có nhiều lớp ẩn,

hai, ba, bốn, năm, vân vân.

Điều tiếp theo chúng ta sẽ làm

là chỉ định lớp đầu ra.

Lớp đầu ra chứa 10 nơ-ron tương ứng

đến 10 lớp, đó là các chữ số từ 0 đến 9.

Và chúng ta sẽ sử dụng chức năng kích hoạt softmax này, được chứ?

Vì vậy, hãy tiếp tục và chạy nó ở đây lần này.

Và hãy nhớ rằng softmax chuyển đổi điểm thô

đến xác suất.

Và chúng tôi đã học được một chút về điều đó

sớm hơn trong khóa học.

Được rồi, vậy là chúng ta đã trải qua quá trình

xác định từng lớp kiến trúc của chúng tôi.

Chúng tôi đã làm điều đó theo các bước khác nhau ở đây

trong vài ví dụ đầu tiên này.

Nhưng thay vì làm theo cách này,

chúng ta cũng có thể làm tất cả chỉ trong một đoạn mã.

Vì vậy, ví dụ ở đây mà tôi có ở đây

là cách chúng ta có thể làm điều tương tự như chúng ta vừa làm

từng bước ở trên trong một đoạn mã.

Vì vậy, ở đây tôi bắt đầu bằng cách chỉ định việc khởi tạo,

lớp đầu vào, lớp dày đặc đầu tiên,

lớp dày đặc thứ hai và lớp đầu ra.

Vì vậy hãy tiếp tục và chạy cái này,

và nó sẽ tạo ra kiến trúc giống hệt nhau

như chúng tôi đã làm trước đây.

Vì vậy, khi tôi chạy nó, chúng ta đã hoàn thành ở đó,

bây giờ chúng ta có thể xem bản tóm tắt về kiến trúc mô hình

bằng cách gọi phương thức tóm tắt của mô hình.

Vì vậy, hãy chạy nó và xem những gì chúng ta nhận được.

Vì vậy, ở đây, điều này bây giờ cho chúng ta thấy chính xác

các lớp dành cho mô hình của chúng tôi là gì.

Lớp dày đặc đầu tiên có 512 nơ-ron,

cái thứ hai có 128,

và lớp đầu ra có 10 nơ-ron.

Vì vậy, ở đây điều này cung cấp cho chúng tôi một số thông tin về

có bao nhiêu tham số có thể huấn luyện được.

Và khi chúng ta nói về các thông số có thể huấn luyện được,

chúng ta đang nói về trọng số và độ lệch

trên mạng của chúng tôi.

Vì vậy, ở đây chúng ta thấy rằng chúng ta có 468.874 tham số

phải được đào tạo để có thể xây dựng mô hình này.

Và ở đây tôi chia nhỏ thực ra điều đó là gì,

làm thế nào chúng tôi nghĩ ra con số đó.

Lớp ẩn đầu tiên, Lớp ẩn thứ hai

và Lớp đầu ra.

Và bằng trực quan, chúng tôi cũng có thể hiển thị,

vì vậy tôi thực sự đang cho bạn thấy một cách trực quan,

mạng của chúng ta sẽ trông như thế nào.

Vì vậy, chúng ta có lớp đầu vào với 784 nút,

và lớp ẩn đầu tiên có 512 nút,

lớp ẩn thứ hai với 128 nút,

và lớp đầu ra của chúng tôi với 10 nút.

Vậy là bạn đã có nó rồi,

chúng tôi đã xác định thành công các lớp

của mô hình học sâu trong Python sử dụng Keras.

Bước tiếp theo là biên dịch và huấn luyện mô hình.

Đó là những gì chúng ta sẽ làm trong video tiếp theo.

Hẹn gặp bạn ở đó.