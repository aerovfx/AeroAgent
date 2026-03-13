# 004 Cập nhật giá trị cấu trúc vi

---

Người hướng dẫn: Trong video cuối cùng,

chúng tôi đã xem xét hai cách khác nhau để khai báo một giá trị

thuộc loại người.

Vì vậy, trước tiên chúng tôi sử dụng dấu ngoặc nhọn

và sau đó chúng tôi chỉ liệt kê ra các giá trị

mà chúng tôi muốn đưa vào struct.

Vấn đề với cách tiếp cận đó là nó phụ thuộc hoàn toàn

theo thứ tự chúng tôi liệt kê các trường khác nhau

mà người này có.

Vì vậy, có một cách thực hiện dễ dàng hơn nhiều

là liệt kê tên thuộc tính, dấu hai chấm,

và sau đó là giá trị mà chúng ta muốn gán cho nó.

Bây giờ có một cách cuối cùng để khai báo một cấu trúc

mà tôi muốn bạn nhận thức được.

Vì vậy tôi sẽ xóa hai dòng này

mà chúng tôi đã tập hợp lại

và chúng ta sẽ viết ra cách thứ ba

khai báo một cấu trúc.

Vì vậy, đối với cách làm cuối cùng này

Tôi sẽ viết var alex thuộc loại người.

Bây giờ điều này khai báo một giá trị thuộc loại người ngay tại đây

và gán nó cho biến alex.

Bây giờ chúng ta đã tạo ra Alex,

Alex hoàn toàn chưa có tài sản nào được giao cho anh ấy.

Khi bạn tạo một biến trong Go

và bạn không thực sự gán bất kỳ giá trị nào cho nó,

hoặc thực ra bạn không biết,

điền trước các trường khác nhau này,

Go chỉ định những gì được gọi là giá trị 0

cho từng trường khác nhau bên trong cấu trúc.

Chúng ta hãy nhìn vào một sơ đồ

để hiểu rõ hơn giá trị 0 là gì.

Được rồi, tùy thuộc vào loại lĩnh vực khác nhau của bạn,

bạn sẽ kết thúc với một giá trị 0 hơi khác một chút.

Vì vậy, bên trong cấu trúc hiện tại của chúng ta, cấu trúc con người của chúng ta

chúng tôi có hai chuỗi khác nhau.

Vì vậy khi chúng ta nói var alex là kiểu người,

một cấu trúc được tạo ra,

và các trường họ và tên

được tự động gán giá trị của chuỗi trống.

Nếu chúng ta có bất kỳ loại kiểu số nào

bên trong cấu trúc, như int hoặc float 64

chúng sẽ được tự động gán giá trị bằng 0.

Và nếu chúng ta có một trường kiểu bool,

hoặc viết tắt của boolean, tất nhiên

giá trị trường sẽ được tự động mặc định

là sai.

Bây giờ điều này thực sự rất quan trọng để bạn hiểu

bởi vì đôi khi bạn có thể muốn

để thực sự mặc định những giá trị này cho một cái gì đó khác.

Và nếu bạn đến từ một ngôn ngữ khác

bạn có thể mong đợi rằng những giá trị trường này

sẽ được chỉ định một cái gì đó như nil hoặc không xác định,

đặc biệt nếu bạn đến từ JavaScript

hoặc có lẽ cả Ruby nữa.

Vì vậy trong Go, chúng ta không thực sự tự do gán giá trị nil

chỉ muốn dù muốn hay không ở khắp nơi.

Thay vào đó, chúng tôi sử dụng các giá trị 0 này.

Vì vậy, nếu chúng ta quay lại trình soạn thảo mã của mình ngay bây giờ

và đăng xuất Alex, rồi chạy chương trình này,

chúng ta sẽ thấy điều gì đó thú vị.

Vậy tôi sẽ nói Đi chạy chính đi.

Và bạn sẽ nhận thấy rằng về cơ bản chúng ta có một cấu trúc trống

nhưng trên thực tế, ngôi thứ nhất, hoặc thứ lỗi cho tôi, tên

và họ đều được xác định,

nhưng giá trị của chúng là chuỗi rỗng.

Và vì vậy báo cáo nhật ký này ngay tại đây

thực sự có thể được hiểu là chuỗi rỗng chuỗi rỗng,

vì họ và tên đều là chuỗi rỗng.

Bây giờ có một cách khác để thực sự xác nhận điều đó

là in ra cấu trúc theo một cách hơi khác.

Vì vậy, có một nhật ký khác hoặc một câu lệnh in khác

mà chúng ta có thể sử dụng để đăng xuất khỏi cấu trúc

và liệt kê từng tên trường và giá trị

cái đó cũng được gán cho mỗi người.

Vì vậy, ngay bên dưới dòng lệnh in này

Tôi sẽ thêm vào định dạng Printf.

Bây giờ chúng ta đã thấy Printf trước đó rất lâu rồi

và chúng tôi đã nói rằng chúng tôi có thể sử dụng Printf

với kiểu như cú pháp nội suy

nơi chúng tôi đặt một số nhận dạng nhỏ

sau đó được điền vào với một giá trị thực tế.

Vì vậy, tôi sẽ chuyển một chuỗi cho thứ này theo phần trăm cộng v

và sau đó làm đối số thứ hai cho hàm

Tôi sẽ chuyển Alex vào, như vậy.

Phần trăm cộng với v ngay đây sẽ in ra

tất cả các tên trường khác nhau

và giá trị của chúng từ alex.

Vì vậy, hãy lưu cái này và chạy lại và xem những gì chúng ta nhận được.

Vậy tôi sẽ chạy lại

và bây giờ chúng ta có thể thấy tên của một thứ trông như chẳng có gì

nhưng thực sự là chuỗi rất trống rỗng.

Và sau đó là họ của chuỗi trống.

Được rồi, đó là cách thứ ba

để khai báo một cấu trúc mới trong Go.

Bạn sẽ thấy tùy chọn này đôi khi được sử dụng ở đây

đặc biệt nếu bạn muốn truy cập vào

hoặc bạn muốn cụ thể có những giá trị 0 đó.

Nhưng nói chung, đối với rất nhiều mã

rằng chúng ta sẽ viết

chúng ta sẽ sử dụng loại tên thuộc tính đó

cú pháp giá trị dấu hai chấm mà chúng ta vừa thấy cách đây không lâu.

Được rồi, điều cuối cùng tôi muốn xem xét trong phần này

là làm cách nào để chúng tôi cập nhật các thuộc tính

hoặc các trường trên một cấu trúc?

Chà, điều này sẽ có cảm giác rất giống với các ngôn ngữ khác

mà chúng ta có thể đã quen.

Vì vậy, bên dưới tuyên bố của chúng tôi về Alex

chúng ta có thể nói đơn giản là tên alex.first bằng

và sau đó là giá trị mà chúng ta muốn gán.

Vì vậy, chúng ta sẽ nói Alex, có thể là alex.họ Anderson, như vậy.

Vì vậy, bây giờ chúng ta có thể lưu tệp này, chạy lại mã của mình,

và chúng ta quay lại với Alex Anderson.

Và đây là cách thay thế

in ra một cấu trúc ngay tại đây

nơi chúng ta có thể thấy rõ ràng tên của Alex,

họ của Anderson.

Một lần nữa, cách cập nhật cấu trúc rất phổ biến

cú pháp dấu chấm mà bạn có thể đã quen

bằng nhiều ngôn ngữ khác nhau rồi.

Được rồi, vậy là chúng ta đã tìm hiểu thêm một chút về cấu trúc

và cách chúng hoạt động.

Hãy tiếp tục ở phần tiếp theo

và chúng ta sẽ có thêm một chút kiến thức

về một số cách sử dụng phức tạp hơn của cấu trúc.

Vậy nên hãy nghỉ ngơi nhanh và tôi sẽ gặp bạn sau một phút nữa.