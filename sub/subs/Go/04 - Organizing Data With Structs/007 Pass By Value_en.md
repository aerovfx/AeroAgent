# 007 Truyền theo giá trị en

---

Giáo viên: Ở phần trước chúng ta đã tìm ra

cách xác định hàm lấy cấu trúc làm bộ thu.

Vì vậy, chúng tôi đã xác định chức năng in

và chức năng cập nhật tên,

cả hai đều có người nhận kiểu người.

Và vì vậy chúng tôi có thể gọi jim.updateName

và jim.print chỉ vì Jim thuộc loại người.

Sau đó chúng tôi chạy chức năng tên cập nhật này,

và chúng tôi thấy rằng nếu chúng tôi cố gắng cập nhật tên của Jim

ngay tại đây rồi in ra Jim,

ngay sau đó nó xuất hiện

rằng bản cập nhật không thực sự được giữ nguyên.

Vì vậy trong phần này chúng ta sẽ đi sâu

đi sâu vào vấn đề đó và cố gắng hiểu chính xác

tại sao việc cập nhật tên của Jim không thực sự có hiệu lực

bên trong ứng dụng của chúng tôi.

Bây giờ toàn bộ chủ đề này sẽ xoay vòng

xung quanh ý tưởng về con trỏ trong go.

Nếu bạn đã quen với con trỏ từ khi làm việc

với C, C++ hoặc bất kỳ loại ngôn ngữ nào khác,

ừ thì rất có thể

rằng bạn có thể không thích con trỏ lắm, nhưng đừng lo lắng.

Con trỏ và đi tương đối đơn giản

và thực sự không phải là điều tồi tệ nhất trên thế giới.

Vì vậy hãy nhảy vào vấn đề này

và hãy tìm hiểu chính xác chuyện gì đang xảy ra.

Được rồi, vậy chúng ta sẽ xem qua mã của chúng ta ở đây

từng dòng một, nhưng trước khi chúng tôi làm điều đó,

Tôi muốn cung cấp cho bạn một bản bồi dưỡng nhanh chóng

về cách RAM hoặc cách bộ nhớ hoạt động trên máy của bạn,

trên máy tính của bạn ngay bây giờ.

Bây giờ, khi chúng ta đang nói về RAM

Tôi sẽ cung cấp cho bạn một định nghĩa hơi phi khoa học.

Vì vậy tôi sẽ cung cấp cho bạn một số thông tin rất

tổng quan sâu rộng về cách hoạt động của RAM

bởi vì tôi muốn bạn suy nghĩ nhiều hơn

về những gì Go đang làm bây giờ

hơn là lặn 20 phút

về cách RAM hoạt động trên máy cục bộ của bạn.

Vì thế tất cả những gì tôi thực sự muốn bạn hiểu

về RAM lúc này là bộ nhớ đó

trên máy cục bộ của bạn có thể được nghĩ

giống như một đống khối nhỏ

hoặc một loạt các khe nhỏ hoặc một loạt các hộp nhỏ.

Mỗi ô trong bộ nhớ máy tính của bạn có thể lưu trữ một số dữ liệu

và mỗi chiếc hộp nhỏ này hoặc những giá trị nhỏ này

container có một số địa chỉ kín đáo.

Và vì vậy bất cứ khi nào chương trình của bạn nói,

ồ, tôi muốn lấy một số thông tin

từ bộ nhớ của máy tính,

nó nhìn, nó đi và tìm địa chỉ nào đó

và sau đó nó kéo giá trị ra khỏi đó.

Và mỗi chiếc hộp nhỏ ở đây

có thể chứa một số lượng thông tin.

Và đó thực sự là tất cả những gì tôi muốn nói đến đây

khi RAM hoạt động ngay bây giờ.

Chỉ cần tổng quan nhanh về chính xác cách thức hoạt động.

Được rồi, bây giờ chúng ta hãy tách chương trình của chúng ta ra từng bước một

và nghĩ xem chương trình của chúng tôi hoạt động như thế nào với RAM

trên máy cục bộ của chúng tôi.

Vì vậy, trước tiên chúng ta sẽ bắt đầu với dòng này

chúng ta tạo một cấu trúc mới kiểu người và gán nó

đến biến của Jim.

Vì vậy, khi chúng ta làm điều này, khi chúng ta tạo cấu trúc mới này

thuộc loại người Go sẽ tạo cấu trúc đó.

Sau đó nó sẽ đi vào bộ nhớ cục bộ trên máy tính xách tay của chúng ta

hoặc máy cục bộ của chúng ta và nó sẽ thử

để tìm một số thùng chứa hoặc một số chỗ miễn phí

và có khả năng chấp nhận một số dữ liệu.

Vì vậy, chúng ta có thể tưởng tượng rằng nó sẽ chở chiếc xe tải này ngay tại đây,

nó cứ đi mãi và tìm thấy chút không gian

hoặc vị trí nào đó để đặt cấu trúc đó, và sau đó nó đẩy

dữ liệu đó vào thùng chứa nhỏ này ngay tại đây.

Và chúng ta có thể tưởng tượng rằng cấu trúc Jim này ngay tại đây

hoặc người này đang ngồi ở địa chỉ 0001.

Và vì vậy bất cứ khi nào chúng ta nhìn vào biến Jim,

Jim đang chỉ thẳng

tại cái thùng chứa nhỏ này ngay tại đây.

Và nếu chúng ta in ra giá trị của Jim,

chúng ta sẽ luôn thấy chính xác giá trị này ngay tại đây.

Được rồi, với ý nghĩ đó, bây giờ chúng ta hãy nghĩ

về điều gì sẽ xảy ra khi chúng ta gọi jim.updateName bằng Jimmy.

Và tôi cũng muốn nghĩ một chút về chiếc ống nghe đó

mà chúng tôi đã tạo trên hàm cập nhật tên ngay tại đây.

Vậy là chúng ta vẫn còn Jim ở đây phải không?

Jim vẫn ở số 001 và nó vẫn có cấu trúc chính xác như vậy.

Bây giờ đây là nơi mọi thứ thực sự diễn ra,

thực sự thú vị với Go.

Go là những gì chúng tôi gọi là ngôn ngữ truyền qua giá trị.

Truyền theo giá trị có nghĩa là bất cứ khi nào chúng ta truyền một giá trị nào đó

vào một hàm, Go sẽ lấy giá trị đó

hoặc lấy cấu trúc đó,

nó sẽ sao chép tất cả dữ liệu đó

bên trong cấu trúc đó và sau đó đặt nó vào bên trong cấu trúc mới

một số vùng chứa mới bên trong bộ nhớ máy tính của chúng tôi.

Vì vậy, khi chúng tôi chuyển Jim vào hàm cập nhật tên này,

Jim vẫn tồn tại một mình với cấu trúc này,

với tên đầu tiên của Jim tại địa chỉ 0001.

Nhưng Go sao chép giá trị đó,

nó tìm thấy một số thùng chứa khác trống rỗng,

và nó nhét bản sao đó vào thùng chứa đó

và sau đó nó chạy mã bên trong

tên cập nhật với người nhận P này trỏ vào bản sao đó.

Và vì vậy khi bạn và tôi sửa đổi trường tên đó,

bên trong hàm đó, khi chúng tôi chạy mã này

ngay đây, ghi tên P

sẽ là tên mới,

chúng tôi không cập nhật cấu trúc ban đầu của Jim

chúng tôi đang cập nhật bản sao vừa được tạo

cho lệnh gọi hàm cụ thể của chúng tôi.

Bây giờ điều này nghe có vẻ, trước hết, nó có thể gây nhầm lẫn

điều đó hoàn toàn ổn, hoàn toàn có thể mong đợi được.

Và thứ hai, có vẻ điên rồ như tại sao

trên thế giới Go có làm được điều này không?

Tại sao lại tạo một bản sao khi nó truyền dữ liệu này

tắt chức năng khác này?

Chà, có rất nhiều lý do chính đáng cho điều đó

và chúng ta sẽ tìm hiểu thêm về một số lý do đó.

Nhưng hiện tại, tôi muốn tập trung trước tiên

về cách chúng tôi khắc phục vấn đề này?

Rõ ràng là tại một thời điểm nào đó,

bên trong một trong những chương trình của chúng tôi, chúng tôi chắc chắn

sẽ muốn làm điều gì đó chính xác như thế này

ngay tại đây phải không?

Chúng ta chắc chắn sẽ muốn định nghĩa một hàm

điều đó cần một số tranh luận

và sau đó cập nhật cấu trúc mà hàm đang chấp nhận

với tư cách là người nhận.

Vì vậy chúng ta hãy nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay lại phần tiếp theo

và chúng ta sẽ tìm hiểu

chính xác cách chúng ta sử dụng con trỏ để giải quyết vấn đề này.

Vậy nên hãy nghỉ ngơi nhanh và tôi sẽ gặp bạn sau một phút nữa.