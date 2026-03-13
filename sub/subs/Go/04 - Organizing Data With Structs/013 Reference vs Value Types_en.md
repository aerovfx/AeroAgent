# 013 Tham chiếu và các loại giá trị vi

---

Giáo viên: Ở phần cuối,

chúng tôi tập hợp một đoạn mã nhỏ để chứng minh

một số hành vi khá thú vị hoặc đáng ngạc nhiên.

Chúng tôi đã tạo ra một lát cắt hoàn toàn mới,

chúng tôi đã chuyển nó sang chức năng lát cập nhật.

Sau đó chúng tôi đã cập nhật lát cắt

rồi in ra bản gốc.

Khi chúng tôi in lát cắt gốc này ngay tại đây,

chúng tôi thấy phần tử đầu tiên đã được thay đổi

bằng chức năng lát cập nhật,

điều đó hoàn toàn trái ngược

từ những gì chúng ta đã thấy với một cấu trúc.

Vì vậy hãy nhớ với cấu trúc của chúng tôi

khi chúng tôi chuyển nó vào hàm,

Đi nội bộ tạo một bản sao của toàn bộ cấu trúc.

Và vì vậy khi chúng tôi sửa đổi nó trong hàm

chúng tôi đang sửa đổi bản sao chứ không phải cấu trúc gốc.

Và do đó có vẻ như lát cắt đang hoạt động

khác biệt đáng kể.

Vì vậy, hãy tìm hiểu chính xác những gì đang xảy ra ở đây.

Bây giờ chúng ta sẽ xem xét một vài sơ đồ khác nhau

và điều đầu tiên chúng ta sẽ tìm hiểu

sự khác biệt là gì

giữa một mảng và một lát cắt trong Go.

Vì vậy, đây sẽ là một tiếp tuyến một chút

nhưng tin tôi đi, tất cả đều liên quan đến con trỏ này.

Vì vậy tại thời điểm này trong khóa học

chúng tôi chỉ sử dụng trực tiếp các lát cắt,

nhưng để rõ ràng 100%,

Go có quyền truy cập vào cả lát và mảng.

Chúng tôi hiếm khi sử dụng mảng trực tiếp

bởi vì nó được coi là một cấu trúc dữ liệu rất nguyên thủy,

chủ yếu là do không thể thay đổi kích thước mức tăng lương.

Vì vậy, không phải lúc nào chúng ta cũng muốn

lập danh sách các mục có độ dài cố định.

Thông thường chúng ta muốn lập một danh sách các mục

có thể tăng hoặc giảm theo thời gian theo yêu cầu của mã của chúng tôi.

Vì vậy 99% thời gian chúng ta luôn tận dụng

của các lát cắt và chúng tôi hiếm khi tạo mảng một cách trực tiếp.

Bây giờ bạn có thể coi một slice giống như một mảng lạ mắt,

và sự thật đằng sau hậu trường,

một lát thực sự là một mảng.

Vì vậy, khi bạn và tôi tạo ra một lát cắt,

Đi nội bộ đang tạo hai cấu trúc dữ liệu riêng biệt

cho chúng tôi.

Vì vậy, trong slide này ngay tại đây,

ở trên cùng, chúng ta có nơi chúng ta đã khai báo lát cắt mới của mình

của chuỗi.

Đây là lời tuyên bố ngay tại đây.

Vì vậy, khi chúng ta tạo một lát chuỗi,

Đi nội bộ đang tạo hai cấu trúc dữ liệu riêng biệt.

Đầu tiên là những gì chúng tôi gọi là lát cắt.

Slice là một cấu trúc dữ liệu có ba phần tử

bên trong nó.

Nó có một con trỏ, số dung lượng và số độ dài.

Độ dài đại diện cho bao nhiêu phần tử

hiện đang tồn tại bên trong slice.

Dung lượng là hiện tại nó có thể chứa bao nhiêu phần tử.

Và con trỏ này ngay tại đây

là một con trỏ tới mảng cơ bản

đại diện cho danh sách thực tế của các mục.

Một lần nữa, khi chúng ta cắt một miếng,

chúng tôi nhận được cả cấu trúc dữ liệu lát

và Go cũng tạo một mảng nội bộ

để đại diện cho tất cả các mặt hàng khác nhau của chúng tôi.

Vì vậy, đó là loại yếu tố số một cần hiểu,

chúng tôi nhận được cả cấu trúc dữ liệu lát cắt và mảng

bất cứ lúc nào chúng tôi thực hiện một lát.

Bây giờ chúng ta hãy dành một phút để suy nghĩ về

tất cả dữ liệu này sẽ được lưu trữ trong bộ nhớ như thế nào.

Vì vậy chúng ta sẽ nhìn vào sơ đồ này ngay tại đây.

Bây giờ, giống như khi chúng ta nói về con trỏ

cách đây không lâu, sơ đồ này về cách bộ nhớ

trên máy của chúng tôi đang hoạt động không chính xác 100%,

nhưng vì mục đích của cuộc thảo luận này,

chắc chắn là đủ để truyền tải

điều chúng tôi đang cố gắng nói ở đây.

Vì vậy chúng ta có thể tưởng tượng

rằng bất cứ khi nào chúng ta tạo một slice trong Go,

Go sẽ tự động tạo lát cắt nhỏ đó

Cấu trúc dữ liệu có độ dài, dung lượng,

và một con trỏ tới mảng tại một địa chỉ trong bộ nhớ.

Và sau đó cấu trúc dữ liệu đó sẽ có một con trỏ

qua mảng cơ bản thực tế,

cái mà nó sẽ tồn tại

tại một địa chỉ hoàn toàn riêng biệt trong bộ nhớ.

Bây giờ, biến lát cắt của tôi ở đây

không trỏ vào mảng cơ bản.

Bất cứ khi nào chúng tôi đề cập đến mySlice,

nó thực sự đang trả về cấu trúc dữ liệu lát cắt,

không phải mảng.

Và vì vậy tôi muốn bạn suy nghĩ một chút

về điều gì xảy ra khi chúng ta gọi một hàm

và chuyển mySlice vào đó.

Vâng, khi chúng ta gọi một hàm và truyền mySlice vào đó.

Go vẫn hoạt động như một ngôn ngữ truyền qua giá trị.

Vì vậy Go vẫn đang tạo một bản sao của giá trị đó.

Vì vậy khi chúng ta gọi hàm cập nhật lát

và chuyển vào lát cắt của chúng tôi, chúng tôi lấy cấu trúc dữ liệu lát cắt

và sao chép nó sang một địa chỉ khác trong bộ nhớ.

Nhưng đây mới là mấu chốt.

Đây là điều thực sự điên rồ.

Đây là điều rất quan trọng.

Mặc dù cấu trúc dữ liệu lát được sao chép,

nó vẫn đang trỏ vào mảng ban đầu trong bộ nhớ

bởi vì cấu trúc dữ liệu lát

và cấu trúc dữ liệu mảng là hai phần tử riêng biệt

trong bộ nhớ.

Vâng, chúng tôi đang sao chép lát cắt,

nhưng nó vẫn trỏ vào cùng một mảng.

Vì vậy, khi chúng ta sửa đổi mảng này hoặc khi chúng ta ở trong hàm

khi chúng tôi cố gắng sửa đổi lát cắt,

đó là điều tôi muốn nói,

chúng tôi vẫn đang sửa đổi cùng một mảng

mà cả hai bản sao của lát cắt hiện đang trỏ đến.

Bây giờ đây mới là vấn đề thực sự.

Trong Go, các lát cắt không phải là cấu trúc dữ liệu duy nhất

cư xử theo cách này.

Thực tế có một số loại phần tử khác

hành xử theo cách giống hệt như vậy

nơi cấu trúc dữ liệu cơ bản

hoặc giá trị mà chúng tôi tạo ra

là loại này, cái mà chúng tôi gọi là loại tham chiếu.

Vì vậy, cấu trúc dữ liệu lát cắt ngay tại đây

là những gì chúng tôi gọi là loại tham chiếu

bởi vì nó là một tài liệu tham khảo

sang cấu trúc dữ liệu khác trong bộ nhớ.

Và vì vậy sẽ hoàn toàn ổn nếu chúng tôi tạo một bản sao của tài liệu tham khảo này

trong ký ức bởi vì nó vẫn luôn như vậy

trỏ lại cùng một nguồn dữ liệu thực sự cơ bản.

Vì vậy, trong Go, các lát cắt là thứ mà chúng tôi gọi là kiểu tham chiếu.

Bây giờ có một số loại tài liệu tham khảo khác

mà chúng ta sẽ sử dụng theo thời gian.

Vì vậy, bản đồ là thứ mà chúng ta vẫn chưa nói tới.

Các kênh mà chúng ta chưa nói đến.

Con trỏ là một kiểu tham chiếu

và chúng tôi đã và đang sử dụng chúng.

Và chúng ta vẫn chưa thấy nó,

nhưng các hàm có thể được truyền đi khắp nơi dưới dạng đối số

cho một hàm và đó cũng là một loại tham chiếu.

Tại thời điểm này, chúng ta đang làm việc với int, float,

chuỗi, boolean và cấu trúc

và tất cả đều hoạt động như các loại giá trị.

Nói cách khác, nếu bạn truyền một int,

một kiểu số một boolean hoặc một cấu trúc của một hàm,

điều đó có nghĩa là bạn muốn nghĩ về

tất cả những thứ về con trỏ mà chúng ta đã thảo luận.

Nhưng nếu bạn đang sử dụng một trong những loại tham chiếu ở đây,

chúng ta không phải lo lắng về con trỏ

bởi vì bất cứ khi nào chúng ta chuyển những loại giá trị này đi khắp nơi,

Go đang định nói, ồ

à, đây là loại tham chiếu, vẫn sẽ tạo bản sao.

Nhưng họ vẫn đang tham chiếu đến cùng một cơ sở

như cấu trúc giá trị trong bộ nhớ.

Vì vậy, đây là vấn đề lớn.

Đây là phần rất khó hiểu.

Nếu tôi là bạn,

Có lẽ tôi sẽ chụp ảnh màn hình danh sách này ngay tại đây

hoặc tôi không biết, hãy viết nó ra, ghi chép vài điều,

bởi vì thành thật mà nói bạn có thể sẽ gặp phải

vấn đề này rất nhiều lần

khi bạn bắt đầu chạy một số mã.

Vì vậy, tất cả những gì bạn phải nhớ là những loại cơ bản này

cộng với cấu trúc.

Chúng ta phải lo lắng về con trỏ

nếu chúng ta muốn thay đổi giá trị cơ bản,

nhưng nếu chúng ta đang làm việc với các lát cắt, bản đồ hoặc kênh,

thì không cần phải thực sự xem xét con trỏ trong những trường hợp này.

Được rồi, đó là vấn đề lớn.

Hy vọng nó không quá điên rồ.

Một lần nữa, điều cần ghi nhớ ở đây là vâng,

Go vẫn đang tạo một bản sao của biến

hoặc thứ mà chúng ta đang chuyển sang chức năng khác này,

nhưng thứ mà chúng tôi đang sao chép

vẫn đang tham chiếu cùng một nguồn cơ bản

dữ liệu trong bộ nhớ, đó là lý do tại sao chúng ta có thể tự do thay đổi nó

và xem mảng đó thực sự được cập nhật.

Được rồi, vậy là khá nhiều cho vấn đề lớn rồi.

Hãy tiếp tục với chủ đề tiếp theo của chúng ta

trong phần tiếp theo.