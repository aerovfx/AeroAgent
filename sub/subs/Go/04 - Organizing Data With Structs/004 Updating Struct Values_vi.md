# 004 Cập nhật giá trị cấu trúc vi

---

Trong video trước, chúng tôi đã xem xét hai cách khác nhau để khai báo giá trị của loại người.

Vì vậy, trước tiên chúng tôi sử dụng dấu ngoặc nền và sau đó chúng tôi chỉ liệt kê các giá trị mà chúng tôi

muốn đưa vào cấu hình.

Vấn đề tiếp theo là nó phụ thuộc hoàn toàn vào thứ tự mà chúng tôi liệt kê các

các trường khác nhau mà người này có.

Vì vậy, một cách dễ dàng hơn để làm điều đó là liệt kê ra thuộc tính, đặt tên cho dấu hai chấm và sau đó là giá trị mà

chúng tôi muốn phân bổ nó.

Bây giờ, đã có cách cuối cùng để khai báo một cấu trúc mà tôi muốn bạn biết.

Vì vậy, tôi sẽ xóa hai dòng này mà chúng tôi đã đặt giống nhau và chúng tôi sẽ viết theo cách thứ hai

ba để khai báo một cấu trúc.

Vì vậy, để thực hiện điều này cuối cùng, tôi sẽ viết var.

Alex là một người tốt.

Bây giờ điều này khai báo một giá trị của loại người ngay tại đây và gán nó cho biến.

Alex.

Bây giờ chúng tôi đã tạo Alex, Alex hoàn toàn không có thuộc tính nào được phân bổ cho anh ta.

Khi bạn tạo một biến và chuyển đi và bạn không thực hiện phân bổ bất kỳ giá trị nào cho nó

hoặc bạn không thực sự điền trước các trường khác nhau này, hãy chỉ định những gì được gọi là giá trị 0 cho mỗi trường

các trường khác nhau trong cấu trúc.

Hãy xem sơ đồ để hiểu rõ hơn giá trị 0 là gì.

Vì vậy, tùy thuộc vào các loại trường khác nhau, bạn sẽ nhận được một giá trị 0 hơi

khác một chút.

Vì vậy, bên trong cấu trúc hiện tại của chúng tôi, cấu trúc người của chúng tôi, chúng tôi có hai chuỗi khác nhau.

Vì vậy, khi chúng ta nói var, Alex là loại người.

Một cấu trúc được tạo và các trường tên và chúng được tự động gán giá trị của

trống chuỗi.

Nếu chúng ta có bất kỳ loại số nào trong cấu trúc, hãy đưa ra giới hạn như int hoặc float 64, chúng

sẽ tự động được gán giá trị bằng 0.

Và sau đó, nếu chúng ta có một trường kiểu, bool hoặc viết tắt của boolean.

Tất cả các trường giá trị tự nhiên sẽ tự động được mặc định là sai.

Bây giờ điều này thực sự quan trọng mà bạn phải hiểu vì đôi khi bạn có thể muốn thực sự

mặc định giá trị này thành một thứ khác.

Và nếu bạn đến từ một ngôn ngữ khác, bạn có thể mong đợi rằng giá

trường giá trị này sẽ được chỉ định một cái gì đó bằng 0 hoặc không được xác định, đặc biệt nếu bạn đến từ JavaScript hoặc

có thể là Ruby.

Vì vậy, trong quá trình thực hiện, chúng tôi không thực sự tự phân bổ giá trị nil cho chỉ ở khắp mọi nơi.

Thay vào đó, chúng tôi sử dụng các giá trị 0 này.

Vì vậy, nếu chúng tôi quay lại trình soạn thảo của mình ngay bây giờ và đăng, Alex, và sau đó chạy chương trình này, chúng tôi sẽ

đã tìm thấy một điều gì đó thú vị.

Vì vậy, tôi sẽ nói đi, chạy, chính đi.

Và bạn sẽ thấy rằng cơ sở của chúng ta có một cấu trúc trống.

Nhưng trong thực tế, người đầu tiên hoặc tôi, họ và tên đều được xác định, nhưng giá trị của

chúng là chuỗi trống.

Và vì vậy, ký tự lệnh này có thể được hiểu là trống.

Chuỗi trống, vì họ và tên đều là chuỗi trống.

Bây giờ, có một cách khác để xác thực điều đó là về cấu trúc theo một phong cách hơi khác.

Vì vậy, có một nhật ký khác hoặc một lệnh khác mà chúng ta có thể sử dụng để đăng xuất

cấu trúc và danh sách ra từng trường tên cũng như giá trị được phân bổ cho từng trường.

Vì vậy, ngay bên dưới dòng lệnh trong này, tôi sẽ bổ sung thêm

in định dạng f. set a format nhận dạng số

nhỏ sau đó được điền vào với một giá trị thực tế.

Vì vậy, tôi sẽ chuyển một chuỗi thành phần trăm cộng với V.

Và sau đó như một đối số thứ hai cho hàm mà tôi sẽ truyền trong Alex như vậy phần trăm cộng với V ngay tại

Đây sẽ là tất cả các trường tên khác nhau và giá trị của chúng từ Alex.

Vì vậy, hãy lưu nó và chạy lại và xem những gì chúng tôi nhận được.

Vì vậy, tôi sẽ chạy lại.

Và bây giờ, chúng tôi có thể tìm thấy tên của những gì trông giống như không có gì nhưng thực tế là một chuỗi trống thực sự

sự thật và sau đó là chuỗi trống của họ.

Vì vậy, đó là cách thứ ba để khai báo một cấu trúc mới và bắt đầu.

Bạn sẽ thấy tùy chọn này ngay tại đây được sử dụng đôi khi, đặc biệt nếu bạn muốn có quyền truy cập hoặc bạn muốn cụ

có thể để có giá trị 0 tại chỗ.

Nhưng nói chung, đối với rất nhiều đoạn mã mà chúng ta sẽ viết, chúng ta sẽ sử dụng

sử dụng loại thuộc tính tên, cú pháp giá trị dấu hai chấm mà chúng ta đã thấy chỉ một lần trước đó.

Vì vậy, điều cuối cùng tôi muốn xem xét trong phần này là cách làm để chúng tôi cập nhật các thuộc tính hoặc các trường

trên một cấu trúc?

Chà, điều này sẽ cảm thấy rất giống các ngôn ngữ khác mà chúng ta có thể đã quen.

Vì vậy, bên dưới Tuyên bố về Alex của chúng tôi, chúng tôi có thể nói một cách đơn giản, Alex chấm tên bằng cách sử dụng và sau đó là giá trị

mà chúng tôi muốn phân bổ.

Vì vậy, chúng tôi sẽ nói với Alex, có thể là Alex Dot họ Anderson.

Như vậy.

Vì vậy, hiện tại chúng tôi có thể lưu tệp này.

Chạy lại mã của chúng tôi và chúng tôi quay lại với Alex Anderson.

Và đây là cách thay thế để đưa ra một cấu trúc ngay tại đây, nơi chúng ta có thể thấy

xóa tên của Alex, họ của Anderson.

Vì vậy, một lần nữa, một cách rất phổ biến để cập nhật cấu trúc cú pháp dấu chấm mà bạn có thể đã quen

với nhiều ngôn ngữ khác nhau.

Vì vậy, chúng tôi đã tìm hiểu thêm một chút về cấu trúc và cách chúng hoạt động.

Vui lòng tiếp tục trong phần tiếp theo và chúng tôi sẽ có thêm một số kiến thức nhỏ về một số cách

sử dụng phức tạp hơn của cấu hình.

Vì vậy, hãy nhanh chóng nghỉ ngơi và tôi sẽ gặp bạn chỉ sau một phút.