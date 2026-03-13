# 8 -Actor Critic Model Architecture đã dịch

---

Được rồi, trong video này chúng ta sẽ xem xét kiến trúc mô hình mà chúng ta sẽ sử dụng cho

H2C. Đó là kiến ​​trúc mô hình H2C. Được rồi, lý do chúng ta cần làm điều này là vì cách chúng ta

thiết lập mọi thứ cho đến nay, cách thực hiện điều này khá mơ hồ, phải không? Chúng tôi có rất nhiều lựa chọn. Vậy chúng ta biết rằng

chúng tôi muốn lập mô hình chính sách và nếu chúng tôi đang thực hiện một nhà phê bình thực tế, chúng tôi cũng cần lập mô hình hàm giá trị. Vậy là bạn đã thấy

trước đây khi chúng ta muốn mô hình hóa một hàm giá trị, chúng ta sử dụng mạng lưới thần kinh. Và bạn có thể nghĩ nếu chúng ta muốn lập mô hình

chính sách nữa, rằng chúng ta có thể chỉ cần sử dụng một mạng lưới thần kinh khác. Và vì vậy đây là một giải pháp hợp lệ. Vì vậy, bạn có thể tưởng tượng chúng ta có một

mạng lưới thần kinh như thế này. Và đây là vì chính sách. Vì vậy, cái này lấy trạng thái S tạo ra pi của A cho trước S. Đúng, vậy đây sẽ là một

xác suất bằng một cho trước S. Giả sử, và đây sẽ là xác suất bằng 0 với S. Được rồi, vậy thì bạn có thể có

một mạng nơ-ron khác, được sử dụng để mô hình hóa hàm giá trị. Vì vậy, cái này cũng lấy S, nhưng cái này tạo ra V của S.

Và đây là một cách khả thi để thực hiện mọi việc. Vì vậy, khi chúng ta nói về kiến ​​trúc mô hình, một chủ đề liên quan là tổn thất là gì và làm cách nào để tối ưu hóa nó?

Và vì chúng ta có hai mạng nơ-ron riêng biệt nên trong trường hợp này, chúng ta cũng sẽ có hai hàm mất mát riêng biệt và hai bộ tối ưu hóa riêng biệt. Đúng vậy, tổn thất của chính sách như chúng ta đã thảo luận là,

thực ra chúng tôi chưa thảo luận về sự mất mát. Chúng ta đã thảo luận về mục tiêu, đó là thứ chúng tôi muốn tối đa hóa, bởi vì như bạn nhớ lại, cách chúng tôi xác định nó, nó bắt đầu bằng J bằng tổng số phần thưởng.

Vậy là G, omega.

Đúng vậy, nhưng bây giờ chúng ta cần nghĩ xem chúng ta sẽ triển khai điều này như thế nào trong mã? Vì vậy, trong thực tế, chúng tôi sẽ gọi đây là LP cho việc mất hợp đồng.

Điều này sẽ xảy ra, vì vậy chúng ta sẽ phủ nhận những gì chúng ta có trước đây, bởi vì bây giờ nó là thứ chúng ta muốn giảm thiểu chứ không phải tối đa hóa.

Và lý do là vì với các thư viện như TensorFlow và PyTorch, bạn luôn đưa ra những tổn thất mà bạn muốn giảm thiểu chứ không phải thứ bạn muốn tối đa hóa.

Vì vậy, đó chỉ là hành vi mặc định của các thư viện đó. Được rồi, giả sử chúng ta đã thực hiện mRollouts.

Vì vậy, chúng tôi đang lấy giá trị trung bình của m mẫu và sau đó chúng tôi tính tổng.

i bằng 1 đến m, và sau đó chúng ta có log pi, pi theta. Vì vậy các thông số của mạng này sẽ gọi chúng là theta.

Và sau đó là a, a, i, s, i. Vì vậy, thực ra, tôi cho nó trạng thái i, rồi nhân với lợi thế.

Tôi sẽ gọi nó là a, nhưng thực ra nó phải là, a, s, i, a, i.

Được rồi, nhưng có một điều quan trọng cần lưu ý, vì vậy hãy giả sử chúng ta đang sử dụng lỗi td để có lợi.

Và cái này hóa ra là, chẳng hạn, ri cộng gamma v. Vậy đây sẽ không phải là si, đây sẽ là, số nguyên tố i, và sau đó trừ v, si.

Vì vậy, một điều cần lưu ý về điều này là với hàm mất mát này, chúng ta không lấy gradient đối với lợi thế này.

Vì vậy, chúng ta coi nó như một hằng số, nghĩa là nó sẽ không được sử dụng để huấn luyện các tham số của v.

Và vì vậy bây giờ chúng ta sẽ gọi các tham số của v, giả sử là w. Và điều này sẽ có chức năng mất riêng của nó.

Vì vậy chúng ta có thể nói Lv. Vậy hàm mất mát cho hàm giá trị, chúng ta sẽ gọi nó là Lv.

Điều này chỉ bằng sai số bình phương giữa ri.

Và điều này bạn cũng có thể đo theo nhiều cách khác nhau, trừ v. Vì vậy, chúng ta sẽ chỉ số dưới với w, nghĩa là nó phụ thuộc vào w.

Và trạng thái si, tất cả đều bình phương.

Được rồi, và trong trường hợp này, g có thể là nhiều thứ.

Và một lần nữa, chúng ta không xét bất kỳ gradient nào đối với g. Chúng ta giả sử g là hằng số.

Chúng tôi coi g là hằng số, giống như cách chúng tôi làm với q learning và deep q learning.

Được rồi, vậy g sẽ bằng, giả sử, chẳng hạn, chỉ r i cộng gamma v bằng số nguyên tố i.

Một lần nữa, lỗi td mà chúng ta gặp phải ở trên.

Nhưng như đã đề cập trong các bài giảng trước, bạn cũng có thể sử dụng phương pháp n bước hoặc bất kỳ phương pháp nào khác để ước tính giá trị này.

Được rồi, đây là một cách để làm điều đó.

Nhưng tôi nên đề cập rằng đây không phải là điều chúng tôi sắp triển khai.

Và không phải những gì thường được triển khai khi triển khai 2c, mặc dù tôi cũng đã thấy điều này.

Vì vậy, với phương pháp này, bạn sẽ có hai mạng nơ-ron riêng biệt, hai tổn thất riêng biệt và hai bộ tối ưu hóa riêng biệt.

Và bạn thậm chí có thể, giả sử, trong trình tối ưu hóa của bạn, chọn một tốc độ học khác, các siêu tham số khác, v.v.

Đối với mỗi mạng.

Nhưng trong thực tế, điều chúng ta sắp làm là chúng ta sẽ làm điều gì đó như thế này, ở nơi chúng ta có, để trạng thái chuyển sang

mạng lưới thần kinh nào đó của cơ thể, nên gọi nó là cơ thể.

Và mạng lưới thần kinh của cơ thể này, có thể chỉ là một lớp được kết nối đầy đủ như chúng ta có ở đây.

Ví dụ, nó có thể là nhiều chuỗi lớp.

Vì vậy, tích chập, kéo, định mức lô, tích chập, kéo, định mức lô, v.v.

Tùy thuộc vào nhiệm vụ trước mắt.

Vậy vấn đề là đây là một cơ thể chung.

Và sau đó chúng ta có nhiều cái đầu.

Vì vậy, một trong những cái đầu, và thông thường đây chỉ là những lớp dày đặc.

Cái này xuất ra pi của một s nhất định, và sau đó một đầu khác xuất ra v của s.

Được rồi, đó là cùng một mạng lưới thần kinh, nhưng có hai cái đầu khác nhau.

Và điều này cũng xuất hiện trong các ứng dụng khác của deep learning.

Vì vậy, ví dụ, với tính năng phát hiện đối tượng, có nhiều việc phải làm.

Vì vậy, mô hình phải xuất ra, cho dù có tìm thấy đối tượng hay không,

đối tượng đó thuộc lớp nào và sau đó là tọa độ của đối tượng đó.

Vì vậy, có ba điều mà một mô hình phải đưa ra khi phát hiện đối tượng.

Và cùng một mạng sẽ được sử dụng để xuất ra cả ba thứ đó.

Tương tự như vậy, chúng ta có cùng một mạng lưới hoặc cùng một cơ thể được sử dụng để dự đoán hai điều.

Và điều này thực sự có ích vì nó có nghĩa là phần thân của mạng lưới thần kinh

đang học từ nhiều nguồn khác nhau cùng một lúc.

Được rồi, và trong trường hợp này, hàm mất mát,

thực ra chúng ta kết hợp hàm mất mát thành một mất mát duy nhất,

và sau đó tối ưu hóa tất cả cùng với cùng một trình tối ưu hóa.

Vậy sự mất mát cho việc này, điều chúng ta thường làm là chúng ta có,

chúng ta bắt đầu với việc mất hợp đồng.

Và sau đó chúng ta có thể thêm hàm mất giá trị.

Nhưng chúng ta có quyền lựa chọn về việc chúng ta quan tâm đến từng tổn thất đến mức nào.

Vì vậy, chúng tôi có một hệ số mà chúng tôi có thể thêm vào để cho chúng tôi biết phải đợi mất bao nhiêu giá trị

liên quan đến tổn thất chính sách.

Được rồi, và khi tôi quên một điều ở đây, về việc mất giá trị,

cụ thể là ở đây.

Vì vậy, đây sẽ là mức trung bình trong số lần triển khai m.

Được rồi, thế là xong phần kiến ​​trúc mô hình.