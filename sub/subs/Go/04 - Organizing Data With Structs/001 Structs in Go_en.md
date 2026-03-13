# 001 Cấu trúc trong Go en

---

Giảng viên: Thôi, đã đến lúc bắt đầu làm việc rồi

trong dự án tiếp theo của chúng tôi.

Đối với dự án tiếp theo này, chúng ta sẽ bắt đầu

bằng cách quay lại dự án bài của chúng ta, bộ bài,

và tôi muốn chỉ ra điều gì đó trong dự án đó

điều đó có thể hơi khó xử.

Vậy điều gì đó có thể đã xảy ra

một chút thử thách trên đường

nếu chúng tôi quyết định tiếp tục mở rộng dự án đó.

Một khi chúng ta nói về vấn đề đó là gì

và chúng tôi hiểu tại sao nó lại có thể là một vấn đề nhỏ,

sau đó chúng ta sẽ nói về một tính năng mới trong Go

điều đó sẽ giúp chúng ta giải quyết vấn đề đó

và sau đó chúng ta sẽ bắt đầu thực hiện chương trình nhỏ

để khám phá tính năng đó thêm một chút.

Vậy hãy bắt đầu bằng cách nói chuyện

về những gì có thể đã gây khó xử

về dự án thẻ đó.

Được rồi, trong dự án thẻ,

bạn sẽ nhớ lại rằng chúng tôi đang làm việc

với một đoạn dây

và mỗi chuỗi có ý nghĩa đại diện

một thẻ chơi duy nhất.

Vậy là chúng ta đã có một quân bài giống như quân át bích

hoặc hai bích hoặc ba bích.

Bây giờ, trong dự án đó, chúng tôi chưa bao giờ thực sự phải hỏi

bất kỳ lá bài cụ thể nào, chất của nó là gì hoặc giá trị của nó là bao nhiêu,

nhưng tôi chắc chắn bạn có thể dễ dàng tưởng tượng

rằng nếu chúng tôi muốn mở rộng dự án đó

và bắt đầu tập hợp những thứ như nói,

một trò chơi poker hoặc một trò chơi blackjack

hoặc đi câu cá hay gì đó tương tự,

tại một thời điểm nào đó,

chúng tôi thực sự muốn có thể

nhìn vào tấm thẻ và đặt câu hỏi một cách dễ dàng,

bộ đồ của lá bài này là gì

và giá trị của thẻ đó là bao nhiêu?

Vậy lý do khiến việc đó trở nên khó khăn đến vậy

với cách mà chúng tôi đã trình bày mọi thứ,

đó là để tìm ra bộ đồ nào

hoặc giá trị của bất kỳ thẻ nào đã cho là,

chúng ta sẽ phải thực hiện một chút thao tác với chuỗi.

Vì vậy chúng ta sẽ phải lấy sợi dây,

chia nó theo lời của

và sau đó rút ra giá trị

và bộ đồ ra khỏi đó.

Và vì vậy, bạn biết đấy, điều đó không phải là không thể.

Nó không nằm ngoài khả năng,

nhưng tôi nghĩ điều đó sẽ thực sự khó xử

để tập hợp một chương trình theo cách đó

và để nói rằng mãi mãi, vâng, một lá bài là một sợi dây.

Và vì vậy trong phần này,

chúng ta sẽ bắt đầu tìm kiếm

ở một cấu trúc dữ liệu khác trong Go mà lẽ ra chúng ta có thể sử dụng

để đại diện cho một thẻ chơi cá nhân.

Vì vậy chúng ta sẽ bắt đầu bằng cách nói về

cấu trúc dữ liệu đó là gì,

nó hoạt động như thế nào và sau đó chúng ta sẽ bắt đầu làm việc

một dự án nhỏ để khám phá

cấu trúc dữ liệu mới này hoạt động như thế nào.

Vì vậy, cấu trúc dữ liệu chúng ta sắp nói đến

là một cấu trúc.

Cấu trúc, và tôi đã nói cấu trúc ở đây,

cấu trúc thực sự độc đáo.

Struct là viết tắt của cấu trúc.

Nó là cấu trúc dữ liệu trong Go

và bạn có thể nghĩ nó giống như

một tập hợp các thuộc tính khác nhau

bằng cách nào đó có liên quan với nhau

hoặc có một số loại mục đích chung.

Và vì vậy nếu chúng ta nghĩ lại ví dụ về tấm thẻ ở đây,

chúng ta có thể đã tạo ra một cấu trúc cấu trúc dữ liệu

thuộc loại thẻ và sau đó được gán hai thuộc tính khác nhau

vào cấu trúc đó.

Vì vậy, chúng ta có thể nói rằng một cấu trúc thuộc loại thẻ,

có thể có một bộ đồ, được cho là một sợi dây.

Nó có thể có một giá trị, cũng được coi là một chuỗi.

Và sau đó là một triển khai thực tế

hoặc như một ví dụ, như một giá trị của loại thẻ,

chúng ta có thể có một bộ quân bích và quân Át.

Bây giờ tôi sẽ kể cho bạn nghe ngay bây giờ

ngay khi chúng ta bắt đầu xem xét cấu trúc,

nếu bạn có nền tảng về JavaScript,

bạn có thể coi cấu trúc giống như một vật thể đơn giản.

Và nếu bạn có nền tảng về Ruby,

hãy nghĩ về một cấu trúc tương tự như một hàm băm.

Và nếu bạn có nền tảng về Python,

hãy nghĩ về nó giống như một cuốn từ điển.

Bây giờ, đó không phải là một định nghĩa hoàn hảo thực sự chính xác

về cấu trúc là gì,

Tôi chỉ đang nói bây giờ ở mức độ rất cao,

bạn có thể nghĩ về một cấu trúc

giống như những kiểu cấu trúc dữ liệu đó.

Được rồi, tôi nghĩ đó là cách tốt nhất

để tìm ra chính xác cách thức hoạt động của cấu trúc,

là thực hiện một dự án mẫu nhỏ xung quanh nó

và do đó dự án này sẽ không hoàn toàn giống như vậy

ứng dụng đầy đủ tính năng với một mục đích,

thay vào đó, chúng ta sẽ viết ra

một chút mã cấu trúc

và sau đó hiểu rõ hơn về cách chúng hoạt động

và chúng ta có thể sử dụng chúng để làm gì.

Vì vậy hãy bắt đầu dự án đó ngay bây giờ

bằng cách tạo một thư mục dự án mới

và tạo một tệp main.go mới.

Vì vậy, tôi sẽ thay đổi trình soạn thảo mã của mình.

Tôi sẽ đi nộp hồ sơ.

Chúng ta sẽ mở một thư mục mới.

Vì vậy tôi sẽ tạo một thư mục mới

và tôi sẽ gọi nó một cách đơn giản là structs.

Chúng tôi sẽ mở thư mục này

và sau đó bên trong thư mục mới,

Tôi sẽ tạo một tệp mới có tên main.go.

Được rồi, vậy chúng ta hãy nghỉ ngơi nhanh thôi.

Chúng ta sẽ quay lại phần tiếp theo

và chúng ta sẽ bắt đầu làm việc

về một vài ví dụ để hiểu rõ hơn

về chính xác cấu trúc là gì.

Vậy nên hãy nghỉ ngơi nhanh và tôi sẽ gặp bạn sau một phút nữa.