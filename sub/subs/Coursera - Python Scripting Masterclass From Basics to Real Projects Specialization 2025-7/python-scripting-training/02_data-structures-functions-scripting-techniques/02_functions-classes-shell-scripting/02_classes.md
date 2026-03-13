# 02 lớp

---

Python hỗ trợ khái niệm lập trình hướng đối tượng.

Since, we discussed in the first session that Python

là sự kết hợp của lập trình chức năng.

Lập trình chức năng được thực hiện với sự trợ giúp của biểu thức lambda.

Vì vậy, chúng tôi đã thấy một chức năng ẩn danh

đó là một ví dụ về lập trình chức năng. Phải?

Sau đó, chúng ta có một chương trình định hướng có cấu trúc

đó là chương trình định hướng thủ tục của bạn

và Python cũng hỗ trợ lập trình hướng đối tượng.

Vì vậy, khi chúng ta nói về lập trình hướng đối tượng,

cơ bản của lập trình hướng đối tượng là gì?

Nó chỉ đơn giản nói rằng mọi thứ được viết bên trong một lớp

và được truy cập bởi một đối tượng. Phải?

Vì vậy, Python cho phép bạn tạo các lớp

và truy cập chúng với sự trợ giúp của đối tượng.

Vì vậy, chúng ta hãy xem một ví dụ đơn giản dựa trên các lớp và đối tượng.

Được rồi?

Vì vậy, để xem xét điều này, hãy lấy một ví dụ.

Hãy lấy một ví dụ là chúng ta sẽ tạo một tệp khác.

Hãy nói tên này làm ví dụ về lớp.

Bây giờ, điều chúng ta sẽ làm là,

để làm việc với các lớp và đối tượng,

trước tiên hãy tạo một lớp học.

Vì vậy, tôi đang viết từ khóa lớp

và giả sử tôi đang đặt tên lớp là nhân viên.

Vì vậy, tôi có một lớp có tên là nhân viên.

Trong phần này, tôi có biến được gọi là empCount.

Được rồi?

Tương tự như vậy, lớp học là gì?

Làm thế nào chúng ta có thể định nghĩa một lớp?

Lớp học là một từ bắt nguồn từ từ phân loại

mà đơn giản có nghĩa là để phân loại các tuyên bố sau đây.

Bây giờ, hãy hiểu mô-đun của lớp,

lớp là tập hợp các biến thành viên

và các hàm hoặc phương thức thành viên.

So, you have methods, you have variables,

bạn có hàm tạo, bạn có rất nhiều dữ liệu

giống như các đối tượng trong một lớp duy nhất.

Phải?

Vì vậy, khi chúng ta nói về các lớp học,

lớp học sẽ có rất nhiều thứ.

Vì vậy, các lớp cũng có thể có hàm tạo, phải không?

Vì vậy, bất cứ khi nào chúng ta muốn tạo một hàm tạo,

chúng tôi luôn hiểu rằng để tạo một hàm tạo,

nó phải trùng tên với tên lớp, phải không?

Vì vậy, khi tôi viết nhân viên và khi tôi đưa ra dấu ngoặc này,

nhìn xem, bây giờ nó đang báo lỗi cho tôi

việc sử dụng bất hợp pháp các chú thích biến.

Vì vậy, bất cứ khi nào bạn muốn tạo một hàm tạo trong python,

bạn phải viết định nghĩa và bạn phải gọi init.

Bất cứ khi nào bạn gọi hàm băm xác định init,

điều đó có nghĩa là bạn đang tạo một hàm tạo trong python.

Được rồi, trong kịch bản python,

bất cứ khi nào bạn viết hàm băm xác định,

bạn đang tạo một hàm tạo.

Bây giờ, dựa trên hàm tạo này,

bạn có thể khởi tạo dữ liệu.

Vì vậy, giả sử nếu tôi đang khởi tạo ở đây

với sự trợ giúp của self dot emp id bằng 101.

Đó là dữ liệu mặc định mà tôi đang cố gắng nhập.

Tên emp tự chấm bằng với giả sử bản demo

và self dot emp lương bằng 0.

Vì vậy, những gì tôi đang làm bây giờ là

Tôi chỉ đưa ra dữ liệu mặc định trong hàm tạo mặc định này.

Bây giờ, tương tự như vậy để tạo một hàm tạo được tham số hóa,

bạn có thể viết định nghĩa,

bạn có thể gọi init,

nhưng khi bạn gọi init này,

bạn cần đề cập đến bản thân

và bạn cần đề cập đến các thông số.

Vì vậy, giả sử thông số của tôi là

lương tên id emp

và bây giờ bạn có thể xác định chúng bằng cách sử dụng

self dot emp id bằng với emp id.

Tên emp tự chấm bằng tên

và tự chấm emp lương bằng lương.

Vì vậy, như thế này bạn có thể khởi tạo dữ liệu.

Được rồi, vậy là chúng ta có hai cách khởi tạo.

Một là hàm tạo mặc định hoặc dữ liệu mặc định

và một là hàm tạo được tham số hóa.

Được rồi.

Bây giờ, bất cứ khi nào bạn lấy dữ liệu này,

những gì tôi sẽ làm ở đây là

tôi đang làm emp

đếm cộng một.

Tôi sẽ thêm một dữ liệu vào đó.

Được rồi.

Hoặc có thể bạn có thể viết cộng bằng một.

Vì vậy, chúng tôi chỉ bao gồm một bổ sung.

Vì vậy, chúng ta có thể có được số lượng nhân viên.

Vì vậy, hãy tự chấm

hoặc có thể thay vì bản thân,

bạn cũng có thể viết

số chấm nhân viên cộng với bằng một

và chúng ta cũng hãy làm điều đó ở đây.

Số chấm emp của nhân viên bằng cộng bằng một.

Được rồi.

Bây giờ, đây là hàm tạo.

Bây giờ, để tạo ra các phương thức,

để xác định các phương pháp,

vì vậy chúng tôi sẽ nói xác định.

Giả sử hiển thị

nhân viên là một phương pháp sẽ được hiển thị

mọi chi tiết của nhân viên.

Vì vậy, chúng ta có thể viết ở đây

in id emp

và chúng ta có thể gọi id ở đây.

Tự chấm emp id.

Sau đó, hãy đặt tên.

Vì vậy, gạch chéo n cho dòng mới.

Tên

tự chấm tên emp.

Rồi lương.

Chúng ta sẽ nói tự chấm lương.

Được rồi.

Được rồi.

Vì vậy, đây là điều mà chúng tôi muốn làm ở đây.

Vì vậy, tôi sẽ tạo thêm một phương thức nữa là xác định

tổng số

nhân viên

và chức năng này sẽ có

tổng số nhân viên

và số chấm emp của nhân viên.

Vì vậy, đây là định nghĩa đơn giản của chúng ta về lớp

nơi tôi đã tạo một lớp có

một hàm tạo mặc định, hàm tạo được tham số hóa

và hai phương pháp khác nhau.

Được rồi.

Bây giờ, để truy cập vào lớp này

hoặc để tạo đối tượng của lớp này

những gì chúng ta có thể làm ở đây là

bây giờ hãy xem xét một ví dụ nếu tôi muốn gọi

hàm tạo mặc định.

Vì vậy, tôi đang tạo đối tượng emp1

ngang bằng với nhân viên

và đây là điều tôi đang làm.

Thế thôi.

Bây giờ emp1 chấm

bạn muốn gọi gì?

Bạn muốn gọi phương thức nhân viên hiển thị

và emp1 chấm

phương pháp đếm hiển thị

Vì vậy, bây giờ tôi chỉ gọi thế này thôi

và chỉ chạy phần mã này.

Vì vậy, bạn có thể thấy

Tôi đang gặp lỗi

trong đó nói rằng init yêu cầu ba tham số khác nhau

không có sẵn.

Vì vậy, chúng ta không thể gọi định nghĩa này là init, phải không?

Bây giờ, nếu tôi loại bỏ cái này ngay bây giờ

hoặc có lẽ chúng ta hãy loại bỏ cái này ngay bây giờ

và chỉ cần chạy mã này.

Vâng, nó đang bị xử tử, phải không?

Điều đó có nghĩa là nếu tôi đang cố gắng gọi

hàm tạo mặc định, các tham số init mặc định

nó không truy cập được

hoặc nếu tôi tạm thời loại bỏ cái này

Vâng.

Điều đó có nghĩa là bạn không thể có hai tham số init khác nhau

một lúc phải không?

Vì vậy, hãy loại bỏ một từ này.

Bây giờ chúng ta sẽ đưa ra các thông số.

Giả sử các tham số là 101

tên là Tracy

và mức lương giả sử là 35000.

Và khi tôi gọi emp1 dot

tổng số nhân viên

nó hiển thị cho tôi tổng số hiện tại là 1.

Giả sử nếu tôi làm emp2

ngang bằng với nhân viên

đó là 102

tên của nhân viên hãy nói là Victor

và mức lương giả sử là 40000.

Và bây giờ nếu tôi làm nhân viên hiển thị dấu chấm emp2

sau đó tôi nhận được hai dữ liệu

và tổng số nhân viên là hai

bởi vì khi chúng ta sử dụng tên lớp này, dấu chấm

tên biến hoặc tên đối tượng

chúng tôi đang gọi một loại dữ liệu tĩnh.

Đây là lý do tại sao chúng tôi đã tạo ra như thế này.

Chúng tôi không có quyền sử dụng bản thân

bởi vì khi tôi sử dụng bản thân nó giống như một dữ liệu cục bộ.

Nhưng tôi đã tạo cái này ở dạng tĩnh

vì vậy nó có thể truy cập dữ liệu theo cách tĩnh.

Được rồi.

Vì vậy, đây là ví dụ đơn giản về lớp viết

hoặc truy cập các lớp trong tập lệnh python của chúng tôi.

Bây giờ bạn có thể làm nhiều việc như truy cập

bạn có thể tạo getter setters

bạn có thể sử dụng dữ liệu tích hợp của các lớp.

Phải.

Vì vậy có thể làm được rất nhiều việc

nhưng chỉ để hiểu ngay bây giờ

chúng ta vừa thực hiện một ví dụ đơn giản về các lớp.