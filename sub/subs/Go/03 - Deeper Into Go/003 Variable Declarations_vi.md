# 003 Khai báo biến vi

---

Trong phần cuối cùng, chúng tôi đã tạo một thư mục dự án mới.

Bây giờ chúng ta sẽ tìm hiểu về ngôn ngữ này một chút và hiểu rõ hơn về

một số cơ sở ngôn ngữ đặc biệt.

Chúng tôi cũng sẽ hiểu rõ hơn về những gì trình soạn thảo mã hóa VTS làm để giúp chúng tôi viết hiệu quả mã hóa hơn.

Vì vậy, với chức năng chính của chúng tôi, tôi muốn đặt một mục tiêu cực kỳ dễ dàng cho chúng tôi ngay bây giờ.

Tôi muốn nói rằng tôi muốn tạo một biến thể mới trong đây.

Tôi muốn tạo ra một biến thể mới và tôi muốn chỉ định nó một chuỗi đại diện cho một thẻ trí tuệ.

Sau đó, tôi muốn sử dụng gói FMT đó để ra chuỗi đó, về các cơ sở tương tự như chúng tôi đã làm trong dự án

trước của mình.

Vì vậy, hãy xem qua mã của chúng tôi.

Hãy viết ra và chúng tôi sẽ nói về chính xác những gì chúng tôi đang làm.

Vì vậy, bên trong hàm main của chúng ta, tôi sẽ bắt đầu bằng cách tạo một biến mới và gán một giá trị

cho nó.

Bây giờ, cách đầu tiên chúng ta sẽ viết ra biến thể này, cách đầu tiên chúng ta thực hiện công việc

chỉ định điều này sẽ dẫn đến một cảnh báo cảnh báo nhỏ.

Vì vậy, bạn có thể tìm thấy một cảnh báo nhỏ xuất hiện ở đây, nhưng cảnh báo đó hoàn toàn ổn.

Chúng ta sẽ nói về lý do tại sao chúng ta nhìn thấy nó chỉ sau một giây.

Vì vậy, tôi sẽ nói thẻ var.

Sau đó, tôi sẽ nói chuỗi bằng con át của quân tàn như vậy.

Và ngay bên dưới nó, tôi sẽ đưa ra các thẻ biến thể mà chúng tôi vừa tạo.

Vì vậy, tôi sẽ nói Fmt dot println và sau đó chuyển vào thẻ đó.

Bây giờ một điều thú vị mà tôi muốn cho bạn thấy trước khi chúng tôi bắt đầu đi sâu vào cú pháp ở đây.

Tôi sẽ lưu tệp này rất nhanh và khi tôi làm như vậy, bạn sẽ nhận thấy rằng câu lệnh này

ngay tại đây đã được tự động bổ sung cho tôi.

Và đó là một tính năng nhỏ của VTS mã hóa nên mã hóa nhận ra rằng chúng tôi đang cố gắng hết mình

sử dụng gói FMT và do đó nó tự động thêm một lệnh nhập vào tệp đầu tệp.

Vì vậy, đây chỉ là một trong số rất nhiều phần tích hợp nhỏ lạ mắt mà mã hóa VTS dành cho chúng ta.

Bây giờ chúng ta hãy phân tích câu lệnh này ngay tại đây, nơi chúng ta đã nói chuỗi thẻ var bằng con át của tiền bạc.

Dòng này ngay tại đây khai báo và gán giá trị cho một biến mà chúng ta gọi là thẻ.

Bây giờ, như tôi đã nói, bạn sẽ thấy dòng chữ ngoạc màu xanh lá cây này ngay tại đây và nếu chúng ta di chuột qua nó, nó

Sẽ cung cấp cho chúng tôi thông báo cảnh báo để biết nên phát hiện loại chuỗi, blah, blah, blah.

Một lần nữa, chúng tôi quên thông báo đó chỉ trong một giây.

Thay vào đó, hãy chia nhỏ toàn bộ cú pháp của dòng này ngay tại đây và hiểu rõ hơn về những gì nó

đang làm.

Được rồi, vậy là chúng ta bắt đầu.

Vì vậy, đây là dòng mà chúng tôi vừa bổ sung vào.

Tôi đã chia nhỏ nó ra từng từ một.

Từ đầu tiên ở đây của var là viết tắt của biến.

Nó thông báo rằng họ sắp tạo một biến thể mới ngay sau từ var.

Sau đó họ khai báo tên của biến.

Và tôi đã nói, đây, lời chào này.

Điều chỉnh đó không chính xác.

Nó sẽ là thẻ.

Vì vậy, chúng tôi đang tạo một biến mới có tên là tag.

Bây giờ, hai lần đầu tiên ở đây, không kể bạn đến từ bất kỳ trình cài đặt ngôn ngữ nào,

có thể hợp lý 100%.

Điều bắt đầu có vẻ lạ là từ thứ ba của chuỗi.

Chuỗi từ ngay tại đây nói với trình biên dịch rằng chỉ một giá trị của chuỗi sẽ được nhận

phân bổ cho biến này.

Sau đó, ở phía bên kia của dấu bằng, chúng tôi tạo một chuỗi mới.

Nó chứa một quân giá trị của quân đội và được phân bổ cho giá trị hoặc lỗi, cho thẻ biến

ngay tại đây.

Vì vậy, tại thời điểm này, tôi muốn dành một phút để nói thêm một chút về lý do tại sao chúng ta đặt chuỗi từ

ngay tại đây.

Vì vậy, tôi sẽ kéo lên một sơ đồ khác.

Được chứ.

Chúng ta bắt đầu.

Go a ngôn ngữ được đánh máy tĩnh.

Ngôn ngữ nhập tĩnh có thể khác với bạn nếu bạn đến từ thế này

giới hạn JavaScript.

Ruby hoặc Python.

JavaScript, Ruby và Python là tất cả các ví dụ về ngôn ngữ được nhập vào.

Ngôn ngữ được nhập vào là ngôn ngữ mà bạn và tôi, những nhà phát triển, về cơ sở không quan tâm đến những giá trị nào mà họ

tôi đang chỉ định bất kỳ biến thể nào.

Vì vậy, ví dụ: tôi sẽ mở bảng điều khiển chrome của mình ngay tại đây, điều này sẽ cho

cho phép tôi viết một chút JavaScript rất nhanh.

Bây giờ tôi muốn bạn xem một ví dụ về điều tôi sắp nói.

Var number bằng một, hai, ba, và sau đó ngay bên dưới mà tôi sẽ nói số bằng ABCD bên

in a such string.

Và vì vậy bây giờ nếu tôi có nhiều, tôi sẽ nhận được chuỗi ABCD.

Đây là một ví dụ về ngôn ngữ được nhập động.

Ví dụ hoàn hảo về it.

Tôi muốn nói rằng với JavaScript, trình dịch thông tin không được quan tâm nếu chúng tôi định nghĩa một biến và phân bổ cho nó một số nguyên và sau đó phân bổ cho

no a string, đó là những gì chúng tôi đang làm ngay tại đây.

Với các ngôn ngữ như Java, C ++, hoặc đặc biệt là trong các trường hợp hợp của chúng tôi với Go Right Here khi thực hiện một thao tác như vậy,

chúng tôi sẽ gặp lỗi thực thi thông báo với Go.

Bất cứ khi nào chúng tôi xác định một biến, chúng tôi sẽ chỉ định cho nó một kiểu.

Vì vậy, chúng tôi có thể nói, giống như trong đoạn mã mà chúng tôi đã tìm thấy trong trình soạn thảo của mình,

thẻ biến luôn chứa một chuỗi.

Nó sẽ không bao giờ chứa một số, nó sẽ không bao giờ đạt được chứa một đối tượng hoặc bất kỳ loại dữ liệu nào

khác.

luôn luôn là 100% thời gian sẽ chứa một chuỗi.

Bây giờ Go có sẵn rất nhiều loại cơ sở dữ liệu khác nhau.

Vì vậy, đây là một số loại rất cơ bản có sẵn cho chúng tôi.

Vì vậy, chúng tôi chỉ sử dụng một chuỗi, về cơ bản là một ký tự chuỗi.

Chúng tôi cũng có quyền truy cập vào bool, viết tắt của boolean, vì vậy giá trị sẽ giống như giá trị đúng hoặc sai.

Chúng tôi có quyền truy cập vào kiểu int, là một số nguyên có thể giống như số 0 9000, bất cứ điều gì khác.

Và sau đó, chúng tôi cũng có quyền truy cập vào số float 64, về cơ bản bạn có thể coi nó là một số có

phân tích chữ số sau nó.

Bây giờ đây không phải là một danh sách đầy đủ các loại cơ sở ngay tại đây.

Có rất nhiều loại khác nhau có sẵn cho chúng tôi khi di chuyển.

Nhưng đây là một số cái mà chúng tôi sẽ sử dụng thường xuyên nhất trong suốt khóa học này.

Một lần nữa, tôi muốn nhấn mạnh một điều là đây là một số loại cơ bản hoặc rất cơ bản có

đặt sẵn cho chúng ta.

Có những loại dữ liệu khác phức tạp hơn nhiều, nhưng bạn có thể coi chúng là những thứ thứ hai

rất cơ bản giống như gốc rễ trong lòng đất, một loại bên trong ngôn ngữ.

Bây giờ, hãy còn lại quá trình thảo mã của chúng tôi và xem xét tuyên bố của chúng tôi ngay tại đây.

Một lần nữa, một thẻ var chuỗi.

Vì vậy, một lần nữa, bằng cách cài đặt chuỗi từ ngay tại đây, chúng tôi thông báo rằng

chỉ một chuỗi sẽ được chỉ định cho thẻ biến.

Nhưng như chúng ta đã thấy, có vẻ như có một chút thông báo cảnh báo ở đây nói rằng nên bỏ qua chuỗi

loại bỏ khai báo của thẻ var và sau đó cụ thể là nó nói rằng nó sẽ bị suy ra từ

right right.

Vì vậy, như tôi đã nói, đây là một cách để xác định một biến mới trong hoạt động.

Đây giống như một phương pháp biểu hiện mẫu rất dài.

Nó nói rất rõ ràng.

Những gì chúng tôi đang cố gắng thực hiện.

Lý do mà chúng tôi nhìn thấy thông báo lỗi này ở đây là chúng tôi đang nghĩ, Này, bạn biết gì không?

Dựa trên mã mà bạn đã viết ở đây, bạn không thực sự phải viết ra chuỗi từ.

Tôi có thể tìm thấy những gì bạn đang cố gắng làm với thẻ ở đây để bạn không cần phải viết ra chuỗi.

Vì vậy, một cách thay thế để viết ra dòng mã này và tôi sẽ bình luận về điều đó.

Một cách thay thế để viết ra dòng mã đó sẽ chỉ đơn giản là nói thẻ, dấu hai chấm bằng và

sau đó là bài chủ.

Bây giờ hai dòng mã ngay tại đây tương thích 100%.

Cả hai đều xác định một biến được gọi là thẻ và sau đó cả hai đều thông báo rằng biến đó sẽ

chứa một chuỗi kiểu dữ liệu.

Trong trường hợp thứ hai ngay tại đây, chúng tôi đang dựa vào trình biên dịch để chỉ ra các loại thẻ

được cho chứa một chuỗi.

Nó thực hiện điều đó bằng cách đọc bằng dấu hai chấm toán tử này ngay tại đây.

Vì vậy, về cơ bản ở đây là nói đi, chúng tôi muốn tạo một thẻ biến được gọi là thẻ và bạn cần

tìm ra loại dữ liệu nào sẽ được chỉ định cho nó.

Và như vậy, nếu bạn đã quen với việc sử dụng các ngôn ngữ như C ++ hoặc Java và bạn cảm thấy mệt mỏi

với việc nhập loại công cụ của mỗi biến thì thực sự tuyệt vời vì nó sẽ làm suy giảm các loại ở một mức độ

cho bạn.

Bây giờ một điều tôi muốn chỉ ra ở đây, đây là một lỗi rất phổ biến mà tôi đảm bảo

rằng bạn sẽ mắc phải mọi lúc khi bắt đầu.

Chúng tôi chỉ sử dụng cú pháp dấu chấm này khi chúng tôi xác định một biến mới.

Nếu chúng ta đang phân bổ lại một biến hiện có, một giá trị mới, thì chúng ta không cần phải sử dụng dấu hai chấm nữa.

Vì vậy, ví dụ, nếu chúng tôi xác định được quân bài bằng quân át của quân tiền tại đây, thì sau đó chúng tôi

định rất nhanh sau đó, bạn quyết định đấy, tôi nghĩ lá bài thực sự nên chứa năm viên kim cương.

Chúng tôi sẽ nói rằng thẻ tương thích với số lượng thành viên kim cương.

Vì vậy, hãy lưu ý rằng tôi đã không sử dụng dấu chấm trong trường hợp này.

Vì vậy, chúng tôi chỉ phải sử dụng dấu hai chấm khi tạo giá trị lần đầu tiên.

Vì vậy, đây là lệnh khởi động ngay tại đây.

Biến đã được tạo, nhưng sau đó chúng ta không còn phải khởi động nữa.

Chúng tôi có thể chỉ định một thẻ mới có giá trị ngay bây giờ để thực hiện một đoạn kiểm tra chất lượng mã hóa.

Tôi sẽ lưu tệp này bằng cách nhấn lệnh.

Có vẻ như tất cả các thông báo lỗi và cảnh báo đều bị mất.

Bạn có thể tìm thấy một cái gì đó thú vị ở đây.

Và một lần nữa, đây là một cảnh báo bạn sẽ thấy nhiều lần khi bắt đầu viết mã.

Vì vậy, nếu tôi đã làm, nhầm lẫn, vô tình, nếu tôi đặt thẻ, dấu hai chấm một lần nữa ngay tại đây và sau đó

lưu lại tệp, tôi sẽ thấy một thông báo lỗi được bật lên.

Và vì điều đó nói lên rằng đây không phải là một biến mới.

Bạn đặt dấu chấm bằng để biết rằng đây sẽ là một biến mới, nhưng không phải là

một biến mới.

Bạn đã khai báo điều đó trước đây.

Và vì vậy, về cơ bản trình biên dịch đang nói với chúng tôi rằng, hãy bỏ dấu hai chấm, bạn chỉ đang cố gắng thực hiện một nhiệm vụ.

Vì vậy, điều đó tốt hơn nhiều.

Được rồi.

Trong phần này, chúng tôi đã nói một chút về cách chúng tôi khai báo biến thể với GO.

Chúng tôi có sẵn biểu mẫu này rất dài cho chúng tôi ngay tại đây khi chúng tôi nói thẻ var, chúng tôi chỉ định loại của nó

và sau đó gán cho nó một giá trị.

Và sau đó, chúng tôi cũng có thể sử dụng cú pháp viết tắt này, trong đó chúng tôi nói đơn giản tên của dấu hai chấm bằng cách sử dụng

và sau đó là giá trị mà chúng tôi muốn phân bổ cho nó.

Sau đó, họ có thể chỉ định các giá trị mới cho một biến hiện có bằng cách chỉ cần nói tên biến và sau đó bất cứ thứ gì

Chúng tôi đang cố gắng chuyển đi những gì.

Bây giờ, chúng ta hãy giải lao nhanh và chúng ta sẽ tiếp tục phần tiếp theo và nói thêm một chút về những điều đó

điều chỉnh cơ sở của cờ.