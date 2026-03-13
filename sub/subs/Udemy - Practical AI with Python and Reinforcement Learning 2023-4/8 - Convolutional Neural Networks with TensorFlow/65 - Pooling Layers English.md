# 65 - Lớp gộp tiếng Anh

---

Chào mừng trở lại, mọi người.

Trong bài giảng này, chúng ta sẽ thảo luận về các lớp tổng hợp, đây là khái niệm lý thuyết cuối cùng mà chúng ta cần

để trang trải trước khi nhảy vào và cắt mạng lưới thần kinh tích chập của chính chúng ta.

Ngay cả với kết nối cục bộ xảy ra trong lớp tích chập này khi xử lý hình ảnh màu và

có thể yêu cầu mạng của chúng tôi hàng chục hoặc hàng trăm bộ lọc, điều này không phải là hiếm, chúng tôi vẫn có

một lượng lớn các tham số.

Chúng ta có thể sử dụng các lớp tổng hợp để thực sự giảm thiểu điều này.

Kéo các lớp ngoại trừ các lớp chập làm đầu vào ở đây, chúng ta thấy một ví dụ rất đơn giản về việc lắp vào

hình ảnh đầu vào trực tiếp tới lớp chập và sau đó là kết quả của lớp chập tới lớp

lớp kéo.

Và như chúng ta vừa thảo luận, lớp tích chập có nhiều bộ lọc.

Và sau đó để xử lý hình ảnh màu, có một kênh lọc màu.

Vì vậy, chúng ta có được Tensas rất lớn ở đây trong lớp chập này.

Và ngay cả khi vẫn còn kết nối cục bộ để chuyển từ lớp đầu vào sang lớp tích chập, chúng ta vẫn có

rất nhiều thông số.

Vì vậy, như tôi đã đề cập ở đó, các luật sư phức tạp thường sẽ có nhiều bộ lọc ở đây, chúng tôi chỉ có một

bộ lọc duy nhất được hiển thị, nhưng trên thực tế, chúng tôi có nhiều bộ lọc và sau đó là bộ lọc cho mỗi kênh màu.

Và chúng tôi coi đây là những vật thể Tensas lớn.

Và chúng tôi muốn làm là giảm bớt điều này.

Vì vậy, hãy lấy một bộ lọc duy nhất và xem cách chúng ta áp dụng lớp kéo cho bộ lọc duy nhất.

Và cuối cùng điều này sẽ mở rộng ra nhiều bộ lọc.

Hiện nay có nhiều loại lớp kéo khác nhau và chúng sử dụng lấy mẫu phụ hoặc lấy mẫu xuống khác nhau

kỹ thuật, mà người ta thường gọi là các lớp kéo.

Họ sẽ gọi chúng là lấy mẫu phụ hoặc lấy mẫu xuống.

Và bạn sẽ thấy tại sao chỉ trong một giây.

Vì vậy, chúng ta sẽ giảm kích thước của bộ lọc 4x4 này bằng cách sử dụng lấy mẫu phụ.

Vì vậy, điều chúng ta sắp làm ở đây là chúng ta sẽ sử dụng lớp kéo tối đa và điều chúng ta phải quyết định

bật là kích thước cửa sổ và sau đó là độ dài sải chân hoặc số lượng sải chân.

Và những gì chúng tôi sắp làm về cơ bản rất giống với cách chúng tôi áp dụng một hình ảnh, thưa Đại tá,

hoặc bộ lọc hình ảnh trên đầu hình ảnh.

Chúng tôi áp dụng cửa sổ tổng hợp này lên trên bộ lọc này.

Vì vậy, chúng tôi có cửa sổ 2 x 2 này và chúng tôi sẽ chuyển nó dọc theo bộ lọc này

và sau đó lấy các giá trị tối đa ở đây.

Đây là Max đang kéo.

Vì vậy, trong số một, ba, hai và bốn, giá trị tối đa sử dụng bốn.

Và chúng tôi tiếp tục với điều này.

Đây là giá trị tối đa của chín.

Và cái này bốn x bốn, hai x hai và cái này hai x hai.

Và chúng tôi nhận được một lần nữa, giá trị tối đa là chín.

Và ở đây, phía dưới bên phải, giá trị tối đa là 3.

Và mặc dù chúng tôi có mất một số thông tin khi thực hiện việc này, nhưng bạn có thể thấy rằng hành vi chung thực sự đã

vẫn được giữ lại.

Thông tin chung của phía trên bên trái và phía dưới bên phải là các giá trị đó nằm dọc theo đường chéo,

dường như nhỏ hơn các đường chéo đi từ dưới cùng bên trái lên trên cùng bên phải.

Vì vậy, chúng tôi thực sự vẫn có thể giữ được thông tin đó.

Ngoại trừ việc bây giờ chúng ta chỉ đang xử lý bốn tham số thay vì 16 tham số trước đó, vì vậy chúng ta đã

giảm đáng kể số lượng tham số ở đây trong khi vẫn có thể giữ được thông tin chung.

Với lực kéo trung bình, bạn đã thực hiện quy trình tương tự, ngoại trừ trường hợp này, thay vì lấy

giá trị tối đa, bạn chỉ cần tính trung bình các giá trị đó.

Vì vậy, bạn có thể biết rằng điều này sẽ làm giảm đáng kể số lượng tham số của chúng tôi, đó là lý do tại sao chúng tôi cung cấp dữ liệu tích chập

thành các lớp gộp.

Lớp tổng hợp này cuối cùng sẽ loại bỏ rất nhiều thông tin và thậm chí cả một hạt nhân kéo nhỏ gồm hai

bằng hai nếu cưỡi nó để loại bỏ khoảng 75 phần trăm dữ liệu được nhập vào nó.

Tuy nhiên, hy vọng những xu hướng chung đó vẫn đúng trong suốt lớp kéo.

Một kỹ thuật thực sự phổ biến khác để cố gắng giải quyết vấn đề về thời gian đào tạo và trang bị quá mức.

mạng lưới thần kinh tích chập có thể phải đối mặt là lớp bỏ học.

Chúng ta đã nói một chút về vấn đề này, nhưng việc bỏ học có thể được coi là một hình thức chính quy hóa

để tránh trang bị quá mức.

Và cách thức hoạt động là trong quá trình huấn luyện, các đơn vị sẽ bị loại bỏ ngẫu nhiên, về cơ bản chỉ có nghĩa là bạn

tắt chúng đi và điều bạn làm là cung cấp tỷ lệ phần trăm từ 0 đến 1.

Bạn có thể nói điều gì đó như 0,5.

Và điều đó có nghĩa là khi bạn trải qua quá trình huấn luyện một cách ngẫu nhiên, 50% số nơ-ron trong lớp đó

sẽ bị tắt để chúng không khớp quá nhiều với dữ liệu huấn luyện thực tế.

Vì vậy, một lần nữa, điều này giúp và ngăn các đơn vị thích nghi quá nhiều.

Bây giờ, tôi cũng nên chỉ ra rằng, một số kiến ​​trúc mạng nơ-ron tích chập thực sự nổi tiếng.

Có Linnett năm, Alex, có Google Net hoặc Google trong đó gây tiếng vang.

Và bạn có thể kiểm tra các liên kết tài nguyên tới các bài viết thảo luận về các kiến ​​trúc này.

Nhưng điều thực sự thú vị hiện nay là những gì bạn biết về lý thuyết đằng sau mạng lưới thần kinh tích chập,

bây giờ bạn có thể xem những hình ảnh mô tả mạng chập thực tế này và hiểu

chuyện gì đang xảy ra ở đó vậy

Về cơ bản chỉ là các thứ tự khác nhau của lớp gộp hoặc lớp chập hoặc lớp dày đặc

lớp được kết nối đầy đủ, v.v.

Vấn đề chỉ là kích thước của chúng, thứ tự của chúng và đó chính là mạng lưới.

Vì vậy, bạn có thể xem ở đây một ví dụ về Alex Net.

Và bạn cũng có thể thấy ở đây cách họ hình dung các lỗi tích chập.

Và khi bạn ngày càng tiến xa hơn trên mạng, chúng bắt đầu tìm hiểu các mẫu phức tạp hơn.

Và đây lại là Alex Net.

Và bạn có thể thấy ở đây chúng ta có các lớp kéo Max cùng với một số lớp dày đặc.

Ngoài ra còn có các lớp chập, v.v.

Về cơ bản, nó chỉ là kích thước, thứ tự và số lượng lớp quyết định sử dụng đã tạo nên những sản phẩm nổi tiếng này.

kiến trúc.

Họ có thể dễ dàng tra cứu trực tuyến.

Bây giờ, hãy nhớ rằng Convolutional biết rằng các công trình có thể có tất cả các loại kiến trúc, chúng tôi đã chỉ ra

ví dụ về việc chuyển từ đầu vào sang tích chập, lớp kéo, nhưng việc nạp dữ liệu cũng thực sự phổ biến

các lớp chập vào nhau, thành lớp kéo, v.v.

Hoặc có thể bạn quyết định đi.

Kéo chập, kéo chập.

Và điều đó thực sự hiệu quả cho hình ảnh của bạn.

Thực sự không có cách nào sai để chạy những thử nghiệm này về hình thức của mạng nơ-ron tích chập

thích.

Cách tốt nhất để tìm ra mạng tốt nhất cho bạn là thử các kết hợp khác nhau

và sau đó sử dụng số liệu của bạn để quyết định mạng nào hoạt động tốt hơn các mạng khác.

Bây giờ, hãy nhớ rằng, ở cuối tất cả các mạng này, bạn sẽ có một loại chức năng nào đó

kết nối đầy đủ các kết quả từ lớp trước và sau đó có lớp đầu ra có cùng số

của các nơron như một số lớp.

Vì vậy, ở đây có lẽ chúng ta có mạng lưới thần kinh tích chập đơn giản nhất.

Bạn có thể yêu cầu nó chỉ cần chuyển từ đầu vào sang tích chập rồi kéo sang một loại lớp được kết nối đầy đủ nào đó,

sau đó dẫn đến đầu ra.

Được rồi, bây giờ chúng ta đã tìm hiểu về các lớp tích chập và các lớp kéo cũng như cách các mạng này

tất cả đều hoạt động cùng nhau, hãy tiếp tục và cuối cùng cắt bỏ mạng lưới thần kinh tích chập của riêng chúng ta.

Tôi sẽ gặp bạn ở đó.