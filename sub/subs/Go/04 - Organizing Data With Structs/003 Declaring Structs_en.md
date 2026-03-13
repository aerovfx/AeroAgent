# 003 Khai báo cấu trúc vi

---

Người hướng dẫn: Trong video cuối cùng,

chúng tôi tập hợp lại định nghĩa về cấu trúc của một người.

Vì thế chúng tôi đã bảo Go

rằng sắp có một loại tùy chỉnh mới

bên trong ứng dụng của chúng ta về con người.

Nó sẽ là một cấu trúc có khả năng ghi lại

cả họ và tên của một người.

Vì vậy, bây giờ chúng ta hãy tiếp tục bên trong chức năng chính của chúng ta

và tìm ra tất cả các cách khác nhau

rằng chúng ta có thể tạo ra một con người mới.

Vì vậy trước tiên chúng ta hãy bắt đầu

bằng cách tạo ra một người mới mà chúng ta sẽ gọi là Alex.

Vì vậy có lẽ chúng ta sẽ đặt cho họ cái tên Alex

và họ của tôi thì tôi không biết,

Anderson, đại loại như thế.

Vì vậy, trước tiên chúng ta sẽ tạo một biến

rằng chúng tôi sẽ gọi cho Alex và chúng tôi sẽ đảm bảo

rằng chúng tôi sử dụng cú pháp dấu hai chấm bằng ở đây

bởi vì chúng ta đều đang khai báo, khởi tạo,

và gán một giá trị tất cả trong một bước.

Sau đó, để tạo một giá trị kiểu người

chúng ta sẽ đặt tên loại, đó là người.

Chúng ta sẽ đặt một bộ dấu ngoặc nhọn

và sau đó chúng ta sẽ đặt tên

và họ dưới dạng chuỗi.

Vì vậy chúng ta sẽ nói Alex và sau đó là Anderson, như vậy.

Vì vậy, đây là một trong nhiều cách khác nhau

của việc tạo ra một cấu trúc mới.

Bạn sẽ nhận thấy rằng chúng tôi không thực sự nói điều đó.

Này, Alex sẽ là cái tên đầu tiên

và Anderson sẽ là họ.

Vậy cách Go diễn giải điều này

là chúng tôi đã liệt kê tên thuộc tính đầu tiên

là tên và sau đó là họ.

Vì vậy, vì chúng tôi đặt tên đầu tiên,

và sau đó là họ,

Go cho rằng vì chúng ta đặt Alex ở đây trước,

chúng tôi muốn sử dụng Alex làm tên

và Anderson là họ.

Bây giờ cách tiếp cận này thuộc loại dựa vào

theo thứ tự định nghĩa của các trường là một cái gì đó

rằng cá nhân tôi không thể đứng về phía Go.

Tôi không thể chịu được cú pháp ở đây,

mặc dù bạn sẽ thấy rất nhiều cách sử dụng mã rất chính thức

kiểu tiếp cận này

nơi bạn đang tin tưởng một trăm phần trăm

theo thứ tự các trường của bạn để phân công ở đây.

Và lý do khiến tôi nghĩ điều này thật điên rồ

đó là, à, chuyện gì sẽ xảy ra nếu chúng ta đi cùng

rồi vô tình tráo đổi thứ tự của 2 trường này?

Nếu chúng ta làm điều này, chúng ta sẽ kết thúc với Alex

có họ Alex

và tên đầu tiên của Anderson.

Và vì vậy tôi chỉ cho bạn thấy cú pháp ở đây,

nhưng cá nhân tôi thực sự không thể giới thiệu nó

vì một lần nữa, nếu bạn phải đổi thứ tự

trong lĩnh vực của mình, bạn sẽ ở trong một thế giới đầy tổn thương.

Vậy hãy nhìn theo cách khác

về việc tạo ra một cấu trúc mới của kiểu người.

Vì vậy, cách tiếp theo chúng ta có thể làm là chuyển vào

một tập hợp các loại tên thuộc tính, dấu hai chấm,

và sau đó là giá trị chúng ta muốn gán cho nó.

Vì vậy, cách khác để xác định hoặc tạo ra một con người mới

là đặt dấu ngoặc nhọn vào,

chúng ta sẽ nói tên bằng dấu hai chấm, điền một dấu cách vào,

và sau đó là giá trị mà chúng ta muốn gán cho nó.

Và sau đó chúng ta sẽ làm điều tương tự cho mọi thứ

cho cả họ nữa.

Vậy họ là đại tá Anderson.

Vì vậy, đây là cách khác để xác định cấu trúc mới.

Bây giờ khi chúng ta làm điều này ngay tại đây,

bạn sẽ nhận thấy rằng khi tôi lưu tập tin,

vâng, tôi gặp lỗi.

Nhưng đó là lỗi rất kinh điển mà chúng ta thấy rất nhiều

đó là chúng tôi đã khai báo Alex, nhưng chúng tôi chưa bao giờ sử dụng nó.

Vì vậy, chúng ta có thể bỏ qua điều đó trong một giây.

Vì vậy, cá nhân tôi thích cú pháp này hơn rất nhiều

bởi vì điều đó có nghĩa là chúng ta luôn có thể thay đổi thứ tự

của các cánh đồng ở đây.

Chúng ta có thể thêm vào, làm bất cứ điều gì chúng ta muốn

và chúng ta sẽ luôn biết

rằng chúng ta đang định nghĩa cấu trúc

với thứ tự đúng của các trường.

Được rồi, đó là hai cách để xác định một cấu trúc.

Có một phần ba mà chúng ta sẽ xem xét ngay sau đây,

nhưng bây giờ, hãy cùng tìm hiểu

chính xác là cách chúng tôi in ra tất cả thông tin

được chứa trong cấu trúc này.

Bây giờ tôi sẽ tắt trình thám hiểm ở bên cạnh đây

để bạn có thể xem toàn bộ tập tin của tôi.

Bây giờ, ngay bên dưới tuyên bố của chúng tôi về điều này, Alex,

hãy thêm vào một tuyên bố in

chỉ cần in ra người này và xem họ trông như thế nào

khi chúng tôi in chúng ra ở dòng lệnh.

Vì vậy chúng ta sẽ nói FMT in dòng ln.

Chúng ta sẽ chuyển Alex vào.

Được rồi, khi lưu nó, chúng ta sẽ thấy lỗi biến mất

và bây giờ chúng ta sẽ nhập gói FMT.

Vì vậy bây giờ chúng ta hãy chuyển sang dòng lệnh của chúng ta

và chạy chương trình này và xem Alex trông như thế nào

khi chúng tôi in chúng ra.

Vì vậy, tôi đã thay đổi thư mục cấu trúc dự án của mình

và chúng ta sẽ chạy tệp bằng lệnh go run main.go.

Và khi chúng tôi in nó ra,

nó in ra rất rõ ràng, Alex Anderson.

Được rồi, tôi nghĩ chúng ta đã học được hai cách khác nhau

để khai báo một cấu trúc

và chúng tôi cũng đã học được điều đó, đúng vậy, giống như những sợi dây

chúng ta có thể dễ dàng in chúng ra bằng dòng lệnh.

Chúng ta hãy nghỉ ngơi nhanh chóng và sau đó quay lại và xem xét

ở một số tính năng phức tạp khác xung quanh cấu trúc.

Vậy nên hãy nghỉ ngơi nhanh và tôi sẽ gặp bạn sau một phút nữa.