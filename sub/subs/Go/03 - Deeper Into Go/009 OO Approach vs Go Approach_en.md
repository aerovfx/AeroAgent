# 009 OO Cách tiếp cận vs Đi Cách tiếp cận vi

---

Người hướng dẫn: Bây giờ chúng ta đã có được cái nhìn tổng quan

của một số phần cú pháp rất cơ bản và đi

đã đến lúc bắt đầu dự án Thẻ của chúng tôi trong Earnest.

Trong video này trước tiên tôi muốn nói về

cách chúng tôi có thể tiếp cận dự án Cards

nếu chúng ta đang làm việc

với ngôn ngữ kiểu hướng đối tượng cổ điển

như nói Python hoặc Ruby hoặc Java.

Sau đó chúng ta sẽ tìm ra cách vẽ

một số phương pháp lập trình hướng đối tượng

qua để đi.

Và để thực sự rõ ràng

Go không phải là ngôn ngữ lập trình hướng đối tượng,

vì vậy không có ý tưởng nào về các lớp bên trong Go.

Vì vậy chúng ta hãy xem xét

về cách chúng tôi tiếp cận dự án Cards với một điều gì đó

như Python hoặc Ruby và sau đó thực hiện tổng quan nhanh

về cách chúng ta sẽ thực sự tiếp cận nó bằng cách sử dụng Go.

Được rồi, đây là cách chúng ta có thể làm

toàn bộ chương trình Cards này với lập trình hướng đối tượng.

Chúng ta có thể quyết định tạo ra một thứ gọi là lớp boong.

Một lớp boong là một loại bản thiết kế

có một số thuộc tính

và các phương pháp gắn liền với nó

mô tả một ví dụ

hoặc một bản sao của một bộ bài trông như thế nào.

Vì vậy chúng ta có thể sử dụng lớp boong đó

để sau đó tạo một phiên bản boong.

Một phiên bản bộ bài có thể có một thuộc tính được gọi là thẻ,

đó có thể là một chuỗi các chuỗi.

Sau đó chúng ta có thể sử dụng các hàm kèm theo

đến phiên bản boong được gọi là những thứ

như in hoặc xáo trộn hoặc lưu vào tập tin

để thao túng danh sách thẻ đó

được gắn vào phiên bản boong.

Và trong thế giới cờ vây

mọi thứ sẽ khác biệt đáng kể.

Vậy hãy nói về

cách chúng tôi sẽ tiếp cận vấn đề này với Go.

Được rồi, như bạn đã biết với Go

chúng tôi có sẵn một số loại dữ liệu rất cơ bản này.

Chúng tôi đã nói về các loại dữ liệu cốt lõi

như chuỗi, số nguyên và số float,

nhưng chúng tôi cũng đã nói về mảng và lát cắt,

về mặt kỹ thuật cũng là các loại dữ liệu bên trong Go.

Để thực hiện được ý tưởng này

của một boong bên trong của chúng tôi, xin lỗi,

ý tưởng về một bộ bài bên trong chương trình cờ vây của chúng tôi,

bạn và tôi sẽ định nghĩa một kiểu mới bên trong Go.

Chúng ta sẽ định nghĩa loại này

như được gọi là một loại bộ bài.

Và một loại bộ bài về cơ bản sẽ là

một đoạn dây.

Và trong lát dây đó,

chúng ta sẽ có danh sách các lá bài,

mỗi trong số đó sẽ là một chuỗi

giống như chúng ta đã thấy cho đến nay.

Bây giờ để đính kèm một số chức năng tùy chỉnh

hoặc một số chức năng để làm việc

với loại bộ bài tùy chỉnh này mà chúng tôi tập hợp lại,

chúng ta sẽ tạo ra một số chức năng

mà chúng tôi gọi là các chức năng với máy thu.

Và vì thế đừng lo lắng quá nhiều về việc chính xác

cái máy thu này bây giờ là gì.

Ngay bây giờ tôi thực sự muốn bạn nghĩ về

hoặc có thể hiểu được

là chúng ta sẽ sử dụng một loại hiện có

trong ngôn ngữ là một lát cắt,

và chúng tôi sẽ mở rộng chức năng của nó.

Chúng tôi sẽ thêm một số thuộc tính cho nó.

Chúng tôi sẽ thêm một số chức năng có thể sử dụng

thuộc loại mới này mà chúng tôi sắp tạo ra.

Và những gì chúng ta sẽ trải qua ở đây

sẽ là một mô hình rất phổ biến mà chúng ta sắp thấy

trong rất nhiều chương trình cờ vây khác nhau trong suốt khóa học này.

Được rồi, điều cuối cùng tôi muốn nói với bạn,

khi chúng ta bắt đầu đi sâu vào vấn đề này bằng cách sử dụng các loại

và tất cả những thứ này,

Tôi muốn suy nghĩ về cấu trúc dự án của chúng tôi một chút.

Vì vậy, tại thời điểm này chúng ta chỉ có tệp Dot Go chính đó,

nhưng tôi nghĩ có lẽ chúng ta nên tạo ra

một tập tin riêng gọi là deck dot Go

mô tả chính xác bộ bài là gì và nó hoạt động như thế nào.

Và sau đó về sau

khi chúng tôi cũng bắt đầu làm việc trên ứng dụng này

Tôi nghĩ có lẽ chúng ta nên tìm hiểu cách hoạt động của thử nghiệm.

Và vì vậy chúng ta cũng có thể có

một tập tin kiểm tra gạch dưới boong là tốt.

Vì vậy, ngay bây giờ, hãy tạo tập tin deck dot Go này

để chứa tất cả mã mô tả chính xác bộ bài là gì

và nó hành xử như thế nào.

Vì vậy, tôi sẽ quay lại trình soạn thảo mã của mình

và bên trong thư mục thẻ này

Tôi sẽ tạo một tập tin mới tên là deck dot Go.

Bây giờ hãy nhớ từng tệp bên trong một gói

và đây vẫn là một tập tin bên trong gói chính của chúng tôi

phải luôn khai báo tên gói ở trên cùng.

Và dòng mã đầu tiên

rằng tôi có thể đảm bảo với bạn rằng chúng tôi sẽ viết ở đây

sẽ là tên gói.

Được rồi, tôi nghĩ trước khi bắt đầu viết

một số mã thực sự ở đây,

có lẽ chúng ta nên tạm dừng nhanh

nên bài giảng này không kéo dài quá lâu.

Vậy hãy nghỉ ngơi nhanh và chúng ta sẽ quay lại

và bắt đầu tập hợp một số mã

bên trong tập tin dấu chấm Go của chúng tôi

để mô tả loại bộ bài mới mà chúng tôi sắp tạo ra.

Vậy tôi sẽ gặp bạn sau một phút nữa.