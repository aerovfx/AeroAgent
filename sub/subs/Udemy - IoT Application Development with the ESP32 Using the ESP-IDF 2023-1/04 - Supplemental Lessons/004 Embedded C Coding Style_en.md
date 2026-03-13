# 004 Kiểu mã hóa C nhúng vi

---

Trước khi chúng ta bước vào các bài học lập trình C, tôi nghĩ bạn nên xem nhanh cách viết mã C

phong cách mà tôi sẽ sử dụng trong suốt khóa học.

Nhiều công ty và cá nhân lập trình viên có phong cách viết mã ưa thích, vì vậy phong cách mà tôi sử dụng

trong khóa học này có thể phù hợp hoặc không phù hợp với phong cách bạn đã quen, đó là lý do cho điều này

bài học ngắn gọn.

Vì vậy, trước tiên hãy tập trung vào phần đầu của kiểu mã hóa tệp Dot H.

Và thông tin đầu tiên mà chúng tôi sẽ đưa vào tiêu đề, nếu được yêu cầu hoặc bao gồm bất kỳ thông tin nào.

Và ví dụ này tôi đã thêm ESP nếu Dot H.

Tiếp theo sẽ bao gồm bất kỳ macro và định nghĩa nào, sau đó chúng ta có thể bao gồm bất kỳ biến bên ngoài nào rồi nhập

các mẹo liên quan đến loại thiết bị sẽ cung cấp mô tả cho loại def và thêm bất kỳ ghi chú đặc biệt nào nếu

cần thiết.

Ngoài ra, chúng tôi muốn đặt hậu tố E NUM bằng dấu gạch dưới E.

Và tương tự, đối với các cấu trúc def kiểu, chúng ta sẽ thêm dấu gạch dưới T vào sau chúng và ở cuối

các tệp tiêu đề sẽ bao gồm mọi nguyên mẫu hàm công khai.

Chúng tôi sẽ thêm nhận xét cho từng nguyên mẫu bao gồm mô tả và bất kỳ ghi chú nào nếu cần.

Ngoài ra, chúng tôi sẽ bao gồm mô tả cho từng tham số hàm cũng như kết quả trả về.

Nếu có kết quả trả về và đó là hàm không có giá trị.

Tiếp theo, chúng ta hãy xem phong cách mã hóa cho các tệp nguồn C.

Vì vậy, ở đầu tệp, chúng tôi sẽ cung cấp mọi phần bổ sung cần thiết cho tệp nguồn.

Trước hết, hãy bao gồm mọi tệp tiêu đề thư viện tiêu chuẩn, chẳng hạn như bool tiêu chuẩn cho tiêu chuẩn Boolean

ale cho print def và những thứ tương tự trong chuỗi ngày chẳng hạn.

Tiếp theo sẽ bao gồm mọi tệp tiêu đề bắt buộc từ ESP IDF.

Các ví dụ tôi đã sử dụng ở đây là ESP Log Duddridge, được sử dụng để ghi thông báo vào thiết bị đầu cuối,

Lỗi ESB do xử lý lỗi và flash đáng ghen tị đối với bộ nhớ không ổn định.

Sau đó, chúng ta có thể đưa các tệp ứng dụng của mình vào đây làm ví dụ.

Chúng tôi có tiêu đề h kiểu mã hóa.

Theo sau bao gồm.

Chúng tôi có thể liệt kê bất kỳ biến toàn cục nào và chúng tôi sẽ xác định chúng bằng tiền tố gạch dưới và sử dụng static

từ khóa.

Nếu biến bị hạn chế chỉ sử dụng trong cùng một tệp và vì vậy nếu có biến toàn cục

dự định được sử dụng bên ngoài tệp này thì chúng tôi sẽ không sử dụng từ khóa tĩnh.

Tiếp theo, trong các tệp nguồn sẽ bao gồm mọi hàm riêng tư hoặc tĩnh, là các hàm được

bị hạn chế sử dụng trong tệp nơi chúng được xác định.

Chúng tôi sẽ bao gồm một nhận xét cho từng định nghĩa hàm tĩnh và chỉ định tính thẩm mỹ của hàm.

Chúng tôi sẽ sử dụng từ khóa tĩnh như được hiển thị.

Ngoài ra, tôi nên đề cập rằng nếu bạn muốn gọi các hàm tĩnh trong tệp trước định nghĩa của chúng,

thì bạn sẽ cần đưa vào các nguyên mẫu cho chúng.

Tuy nhiên, tôi sẽ không làm điều này vì đây chỉ là phong cách mà tôi đã quen.

Hoàn toàn ổn khi bao gồm các nguyên mẫu cho các hàm tĩnh và nhiều lập trình viên thực sự thích

nó.

Và một khía cạnh khác của phong cách mã hóa là sẽ thêm tiền tố tên tệp vào tên hàm.

Ví dụ: tên tĩnh kiểu mã hóa được hiển thị ở đây.

Ngoài ra, trong phần nhận xét về định nghĩa hàm tĩnh, chúng tôi sẽ cung cấp mô tả

cho các tham số cũng như kết quả trả về nếu hàm không có giá trị.

Cuối cùng, bên dưới các hàm tĩnh sẽ bao gồm mọi định nghĩa hàm công khai và đối với các hàm này, có

không cần mô tả vì nó đã có trong tệp tiêu đề.

Được rồi, vậy là xong phần tóm tắt về phong cách viết mã được sử dụng và tôi sẽ gặp bạn trong bài học tiếp theo.