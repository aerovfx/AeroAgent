# 02 - Tiền xử lý và cung cấp dữ liệu vào mạng của bạn

---

- [Giảng viên] Tiếp theo chúng ta sẽ chuyển sang một số chi tiết

với việc xử lý trước và cung cấp dữ liệu vào mạng của bạn.

Vậy chúng ta hãy tiếp tục

và mở tệp python 03_02_begin.

Vậy một lần nữa chúng ta sẽ bắt đầu

với việc nhập các thư viện cần thiết vào đây như thường lệ.

Sau đó chúng ta sẽ bình thường hóa dữ liệu.

Sau đó chúng ta sẽ đi tiếp

và hình dung một số hình ảnh như chúng ta thường làm.

Vì vậy, sau khi tải tập dữ liệu, chúng ta sẽ tiếp tục,

và in các hình dạng của tập dữ liệu để xác minh việc tải.

Vì vậy đây là thời điểm tuyệt vời để dừng lại

và nói về việc tăng cường dữ liệu và nó là gì,

và tại sao chúng tôi muốn kết hợp nó vào mã của mình.

Vì vậy, nó liên quan đến việc tạo ra các ví dụ đào tạo mới

bằng cách áp dụng các phép biến đổi ngẫu nhiên cho các hình ảnh hiện có.

Chà, tại sao chúng ta muốn biến đổi ngẫu nhiên cho hình ảnh của mình?

Chà, điều này giúp mô hình khái quát hóa tốt hơn

bằng cách xem nhiều ví dụ đa dạng hơn trong quá trình đào tạo.

Vì vậy, dữ liệu càng khác nhau,

những mô hình tốt hơn nhiều mà chúng ta có thể xây dựng với nó.

Vì vậy chúng ta sẽ tiếp tục và trực quan hóa dữ liệu

trước khi thực hiện bất kỳ thao tác nâng cao nào để xem hình ảnh gốc.

Sau đó, chúng tôi sẽ thiết lập tăng cường dữ liệu.

Chúng ta sẽ có dữ liệu gen,

và chúng ta sẽ có phạm vi xoay, phạm vi thay đổi chiều rộng,

phạm vi thay đổi độ cao, v.v. trong mã.

Sau đó, chúng tôi sẽ áp dụng phần tăng cường này cho hình ảnh của mình.

Chúng tôi sẽ tiếp tục và trực quan hóa dữ liệu tăng cường.

Sau khi chúng ta thực hiện chức năng tăng cường,

chúng tôi áp dụng nó trên hình ảnh của chúng tôi.

Chúng ta sẽ tiếp tục và xem những hình ảnh tăng cường

và xem những gì đã thay đổi.

Và cuối cùng, chúng ta sẽ kết luận,

và nhìn vào cả hình ảnh gốc và hình ảnh tăng cường,

và đánh giá cao sự đa dạng mà phần mở rộng đã giới thiệu

vào tập dữ liệu của chúng tôi, giúp cải thiện độ tin cậy

và khái quát hóa các mô hình của chúng tôi.

Đây là một bước rất quan trọng trong quá trình tiền xử lý,

đặc biệt là khi làm việc với dữ liệu hạn chế.

Chúng ta có thể tạo ra nhiều dữ liệu đa dạng hơn một cách giả tạo

sử dụng các kỹ thuật tăng cường.

Nó cho phép chúng tôi tạo ra một phong cách đa dạng hơn

và bộ đào tạo toàn diện,

cuối cùng dẫn đến các mô hình hoạt động tốt hơn.

Hãy thoải mái thử nghiệm

với các kỹ thuật tăng cường khác nhau

và quan sát tác động của nó lên tập dữ liệu của bạn.

Bây giờ chúng ta hãy quay lại mã.

Bây giờ chúng ta hãy tiếp tục

và thực hiện tất cả quá trình xử lý trước mã của chúng tôi như chúng tôi vẫn thường làm.

Và sau đó xác định một chức năng để hiển thị hình ảnh

trước khi tăng cường để chúng ta có một điểm tham chiếu

để so sánh hình ảnh trước và sau khi tăng cường.

Bây giờ, sau khi chúng tôi chỉnh sửa tất cả những điều đó,

bao gồm chức năng hiển thị hình ảnh,

và thư mục đầu ra của chúng tôi ở đâu,

nơi thư mục cốt truyện của chúng tôi giống như chúng tôi thường làm,

chúng ta sẽ tiếp tục và nói về cốt lõi của phần này,

đó là tăng cường dữ liệu.

Một lần nữa, nó liên quan đến việc tạo ra các ví dụ đào tạo mới

bằng cách áp dụng các phép biến đổi ngẫu nhiên cho các hình ảnh hiện có

để giúp mô hình khái quát hóa tốt hơn

bằng cách xem nhiều ví dụ đa dạng hơn trong quá trình đào tạo.

Bây giờ chúng ta hãy tiếp tục

và bắt đầu mã hóa phần cốt lõi của phân khúc của chúng tôi tại đây,

đó là chức năng tăng cường.

Vì vậy, hãy để tôi bình luận điều này bằng cách nói rằng đây là hình ảnh

tăng cường dữ liệu,

và sau đó chúng ta sẽ tiếp tục tạo một gen dữ liệu.

Nó sẽ bằng hình ảnh

bộ tạo dữ liệu.

Vì vậy, đây là nơi chúng tôi tạo ra dữ liệu,

and then we will apply all sorts of transformations starting

với phạm vi quay bằng 15.

Đây là cách xoay hình ảnh lên tới 15 độ

và hãy nhớ chỉnh sửa dấu phẩy.

Tiếp theo chúng ta sẽ có phạm vi dịch chuyển chiều rộng

tức là bằng 0,1.

Và ý nghĩa của nó là nó dịch chuyển hình ảnh theo chiều ngang

lên đến 10%.

Một lần nữa, hãy bao gồm dấu phẩy của chúng tôi ở đây.

Tiếp theo, hãy tiếp tục và chuyển đổi hình ảnh theo chiều cao.

Vì vậy, phạm vi thay đổi độ cao lại bằng 0,

làm dịch chuyển hình ảnh theo chiều dọc lên tới 10%.

Tiếp theo, chúng ta hãy thêm thao tác lật ngang.

Và lật ngang qua phương tiện

rằng nó lật hình ảnh theo chiều ngang.

Hãy thêm zoom theo phạm vi điểm ở đây

bằng 0,2.

Và điều này là phóng to hình ảnh lên tới 20%.

Phạm vi dịch chuyển kênh tiếp theo

bằng không một,

và đó là sự thay đổi ngẫu nhiên độ sáng của hình ảnh.

Chúng ta hãy tiếp tục và bao gồm phạm vi tuyệt đối

và hình ảnh tuyệt đối.

Shear thực sự làm mờ hình ảnh lên

đến 20% khi chúng tôi cho nó 0,0.

Sau đó, chúng tôi điều chỉnh trình tạo dữ liệu cho dữ liệu huấn luyện

để thực hiện tất cả những chuyển đổi này như vậy.

Vì vậy, chúng tôi tiếp tục và nói datagen.fit

X_train.

Sau đó để xem tác dụng của những sự tăng cường này,

chúng tôi hình dung một số hình ảnh tăng cường.

Rất giống với hình dung trước đây của chúng tôi

gọi là hình ảnh hiển thị.

Chúng ta sẽ tiếp tục và thêm vào đây hàm

để hình dung những hình ảnh ở đây.

Vì nó có chức năng tương tự,

Tôi sẽ tiếp tục và chèn cái này vào đây,

và bạn cũng có thể xem lại nó.

Nó tương tự như chức năng hiển thị hình ảnh ban đầu.

Rồi cuối cùng chúng ta cũng đi tiếp

và xác định tập tin pad để lưu các ô.

Sau đó chúng ta sẽ ổn thôi.

Chúng ta sẽ có tất cả dữ liệu đa dạng được chuyển đổi đẹp mắt này

rằng chúng ta có thể làm cho mô hình của mình ngày càng tốt hơn.

Vì vậy nếu bạn đi theo tôi,

tuyệt vời, hãy tiếp tục và chạy nó.

Nếu bạn chỉ muốn đảm bảo hoặc so sánh mã của mình,

chỉ cần tìm 03_02_end,

và tiếp tục nhấp vào chạy mã này.

Và nó thực sự chỉ mất một vài giây.

Và sau đó nó cho chúng ta hình đoàn tàu X, đoàn tàu Y,

và hình chữ X, hình chữ Y.

Và nó cho chúng ta những âm mưu

và được lưu trong thư mục đầu ra, lô,

cả ảnh gốc và ảnh tăng cường.

Vậy tóm lại, việc tăng cường giúp chúng ta đa dạng hóa hình ảnh

và giúp chúng tôi cải thiện hiệu suất của mô hình

bởi vì chúng tôi có nhiều hình ảnh đa dạng hơn.

Nhân tiện, nếu bạn muốn xem hình ảnh,

chúng được lưu ở đầu ra, sơ đồ và hình ảnh tăng cường 03_02,

và 03 dưới 02 ảnh gốc.

Bởi vì những sự tăng cường mà chúng tôi đã thực hiện rất tinh vi,

chúng ta có thể thấy sự gia tăng ở đây.

Nhưng nếu bạn muốn thấy sự thay đổi mạnh mẽ hơn nữa,

hãy tiếp tục và chơi với các phần tăng cường,

có thể tăng số lượng, tăng sự biến đổi,

và xem chúng trông như thế nào.