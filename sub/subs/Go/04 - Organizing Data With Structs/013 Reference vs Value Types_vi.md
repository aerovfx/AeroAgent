# 013 Tham chiếu và Loại giá trị vi

---

Trong phần cuối cùng, chúng tôi đã tập hợp một đoạn mã nhỏ có thể hiện một số hành động

khá thú vị hoặc đáng ngạc nhiên.

Chúng tôi đã tạo ra một lát hoàn toàn mới.

Chúng tôi đã chuyển nó sang các chức năng cập nhật.

Sau đó, chúng tôi cập nhật phần này và sau đó là phần gốc.

Khi chúng tôi tìm thấy phần gốc này ngay tại đây, chúng tôi thấy rằng phần tử đầu tiên đã có

được thay đổi bằng cách cập nhật phần chức năng, điều này hoàn toàn trái ngược với những gì chúng tôi đã tìm thấy trong một cấu trúc.

Vì vậy, hãy nhớ cấu hình của chúng tôi khi chúng tôi chuyển nó cho hàm, truy cập nội bộ, tạo một bản sao

của toàn bộ cấu trúc.

Và vì vậy khi chúng tôi sửa đổi nó trong hàm, chúng tôi đang sửa đổi bản sao, không phải cấu hình ban đầu.

Và làm điều đó, có vẻ như cắt cắt hoạt động khác đi đáng kể.

Vì vậy, hãy tìm hiểu chính xác những gì đang xảy ra ở đây.

Bây giờ chúng ta sẽ xem xét một số biểu thức khác nhau và

điều đầu tiên chúng ta sẽ tìm thấy sự khác biệt giữa một mảng và một lát cắt.

Vì vậy, điều này sẽ hơi rối một chút, nhưng hãy tận dụng tôi, tất cả đều liên quan đến thứ con trỏ này.

Vì vậy, tại thời điểm này trong khóa học, chúng tôi chỉ sử dụng trực tiếp các lát, nhưng để rõ ràng

100%, hãy truy cập vào cả các mảng và mảng.

Chúng tôi rất ngạc nhiên khi sử dụng mảng trực tiếp vì nó được xem như một phần lớn dữ liệu cấu trúc

do array không thể thay đổi kích thước.

Và vì vậy, không có nhiều khi chúng tôi muốn thiết lập một danh sách các mục có độ dài cố định.

Thông thường, chúng tôi muốn tạo một danh sách các mục có thể phát triển hoặc thu nhỏ theo thời gian theo yêu cầu của mã hóa của chúng tôi.

Vì vậy, 99% thời gian chúng tôi luôn sử dụng các lát cắt và chúng tôi hiếm khi tạo ra một giải pháp trực tiếp.

Bây giờ bạn có thể nghĩ về một lát cắt giống như một mảng lạ mắt.

Và sự thật, đằng sau hậu trường, một lát cắt thực sự là một mảng.

Vì vậy, khi bạn và tôi tạo một lát cắt, hãy đi vào nội bộ để tạo ra hai dữ liệu cấu trúc riêng biệt cho chúng ta.

Vì vậy, trong slide này ngay trên cùng, chúng tôi đã có nơi chúng tôi khai báo phần chuỗi mới của mình.

Đây là tuyên bố ngay tại đây.

Vì vậy, khi chúng tôi thực hiện lát chuỗi này trong bộ nội bộ để tạo ra hai dữ liệu cấu trúc riêng biệt.

Đầu tiên là những gì chúng tôi gọi là cắt cắt.

Slice là một dữ liệu cấu trúc có ba phần tử bên trong nó.

Nó có một con trỏ, số lượng và số chiều dài.

Chiều dài biểu thị số lượng phần tử hiện đang tồn tại bên trong phần cắt.

Dung lượng là bao nhiêu phần tử có thể chứa tại.

Và con trỏ này ngay tại đây là một con trỏ tới mảng bên dưới đại diện cho danh sách thực tế của

các mục.

Vì vậy, một lần nữa, khi chúng tôi tạo một lát cắt, chúng tôi đã nhận được lát dữ liệu cấu trúc và cũng tạo một mảng bên trong để đại diện cho giao diện

Tất cả các mục khác nhau của chúng ta.

Vì vậy, đây là loại phần tử số một để hiểu rằng chúng tôi đã nhận được cả một phần cắt, dữ liệu cấu trúc và một mảng

bất kỳ khi nào chúng tôi tạo một lát cắt.

Bây giờ chúng ta hãy dành một phút để suy nghĩ về cách tất cả dữ liệu này sẽ được lưu trữ trong bộ nhớ.

Vì vậy, chúng tôi sẽ xem xét sơ đồ này ngay tại đây.

Bây giờ, giống như khi chúng tôi nói về con trỏ cách đây một chút, sơ đồ này về cách nhớ trên

máy của chúng tôi đang hoạt động không chính xác 100%.

Nhưng đối với mục tiêu của cuộc thảo luận này, nó chắc chắn đủ để truyền đạt những gì chúng tôi đang cố gắng nói

ở đây.

Vì vậy, chúng tôi có thể tưởng tượng rằng bất cứ khi nào chúng tôi tạo một lát cắt đi, go sẽ tự động tạo cấu trúc

cắt nhỏ dữ liệu có độ dài, dung lượng và con trỏ đến mảng ở một địa chỉ

bộ nhớ.

Và sau đó, dữ liệu cấu trúc sẽ có một con trỏ đến mảng cơ sở thực tế, mảng này sẽ

tồn tại ở một địa chỉ hoàn toàn riêng biệt trong bộ nhớ.

Bây giờ, các biến cắt của chúng tôi ở đây không chỉ vào mảng bên dưới.

Bất cứ khi nào chúng tôi tham khảo phần cắt của tôi, nó thực sự đang trả lời về cấu trúc dữ liệu của phần cắt chứ không phải mảng.

Và vì vậy tôi muốn bạn suy nghĩ một chút về điều gì sẽ xảy ra khi chúng tôi gọi một hàm và chuyển cắt của

tôi vào đó.

Chà, khi họ gọi hàm và chuyển lát cắt của tôi vào đó, vẫn hoạt động như một ngôn ngữ truyền đạt giá trị.

Vì vậy, Go vẫn đang tạo một bản sao của cơ sở giá trị đó.

Vì vậy, khi chúng tôi gọi hàm cắt cắt cập nhật và truyền tải các lát cắt của mình, chúng tôi lấy được cấu trúc cắt cắt dữ liệu

và sao chép nó sang một địa chỉ khác trong bộ nhớ.

Nhưng đây đã là thời gian.

Đây là điều thực sự điên cuồng.

Đây là điều rất quan trọng.

Ngay khi sao chép dữ liệu cấu trúc ngay lập tức, nó vẫn chỉ được cấm vào mảng đầu trong bộ nhớ vì dữ liệu cấu trúc

cut and array data config là hai phần tử riêng biệt trong bộ nhớ.

Đúng vậy, chúng tôi đang sao chép phần cắt, nhưng nó vẫn đang di chuyển vào cùng một mảng.

Vì vậy, khi chúng ta sửa đổi mảng này hoặc khi chúng ta ta bên trong hàm, khi chúng ta cố gắng chuyến đi

sửa đổi cắt cắt, ý tôi muốn nói rằng chúng tôi vẫn đang sửa đổi cùng một mảng mà cả hai bản sao của cắt cắt hiện

đang trỏ đến.

Bây giờ đây là gotcha thực sự đang được sử dụng.

Đây không phải là hoạt động duy nhất của dữ liệu cấu trúc theo loại này.

Trên thực tế, có một số loại hoạt động khác của phần tử theo cùng một cách trong cơ sở dữ liệu cấu trúc

bản giá hoặc giá trị mà chúng tôi tạo ra là loại mà chúng tôi gọi là loại tham chiếu.

Vì vậy, cấu trúc cắt dữ liệu ngay ở đây là những gì chúng ta gọi là một kiểu tham chiếu vì nó là một tham chiếu

reference to a other data config trong bộ nhớ.

Và vì vậy, hoàn toàn không sao nếu chúng tôi tạo một bản sao của tham chiếu này trong bộ nhớ

bởi vì nó vẫn luôn hiển thị cùng một nguồn cơ sở dữ liệu.

Vì vậy, cắt cắt là những gì chúng tôi đề cập đến như một loại tham khảo.

Bây giờ có một số loại tham chiếu khác sẽ được sử dụng theo thời gian.

Vì vậy, bản đồ, thứ mà chúng ta vẫn chưa nói đến, các kênh mà chúng ta chưa nói

đến, con trỏ là loại tham chiếu và chúng tôi đã sử dụng chúng và sau đó chúng tôi vẫn chưa được tìm thấy

nó.

Nhưng các hàm có thể được truyền xung quanh dưới dạng các đối số cho một hàm và chúng cũng là một kiểu tham chiếu.

Bây giờ tại thời điểm này, chúng tôi đã làm việc với int, float, string, boolean và struct, và tất cả chúng

đều hoạt động như các giá trị loại.

Vì vậy, nói cách khác, nếu bạn đang chuyển một int, một số, boolean hoặc một cấu trúc cho một hàm, điều đó có nghĩa là bạn muốn

suy nghĩ về tất cả những thứ mà chúng tôi đã thảo luận về con trỏ này.

Nhưng nếu bạn đang sử dụng một trong những loại tham khảo này ở đây, chúng tôi không phải lo lắng về con trỏ vì bất cứ điều gì

Khi chúng tôi chuyển các loại giá trị này xung quanh, bạn sẽ nói, Ồ, đây là một loại tham chiếu,

vẫn sẽ tạo bản sao, nhưng chúng vẫn được tham chiếu đến cùng một cơ sở cấu trúc giống như giá trị cấu trúc trong

bộ nhớ.

Vì vậy, đây là một điều đáng chú ý.

Đây là phần rất khó hiểu.

Nếu tôi là bạn, chắc chắn tôi sẽ chụp ảnh màn hình danh sách này ngay tại đây hoặc tôi không biết thì

hãy viết nó ra, ghi chú lại, vì thành thật mà nói, bạn có thể sẽ gặp phải vấn đề này rất nhiều

lần. khi bạn bắt đầu chạy một số mã.

Vì vậy, tất cả những gì bạn phải nhớ đều là những loại cơ sở cộng với cấu trúc.

Chúng ta phải lo lắng về các con trỏ nếu chúng ta muốn thay đổi cơ sở giá trị.

Nhưng nếu họ đang làm việc với các lát cắt, bản đồ hoặc kênh thì không cần thiết phải xem xét các con trỏ trong

những trường hợp này.

Vì vậy, đó là một điều lớn lao.

Hy vọng rằng nó không quá điên cuồng.

Một lần nữa, điều cần ghi nhớ ở đây là Yeah, go vẫn đang tạo một bản sao của biến hoặc thứ

chúng tôi đang chuyển sang một hàm khác.

Nhưng thứ yếu là chúng tôi đang tạo bản sao vẫn được tham chiếu đến cùng một cơ sở dữ liệu nguồn

Trong bộ nhớ, đó là lý do tại sao chúng tôi có thể tự động thay đổi nó và xem mảng thực sự đã được cập nhật.

Được rồi.

Vì vậy, có khá nhiều thứ cho bạn nhận được.

Hãy tiếp tục với các chủ đề tiếp theo của chúng tôi trong phần tiếp theo.