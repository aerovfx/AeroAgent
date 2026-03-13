# 005 Hàm và kiểu trả về vi

---

Trong phần trước, chúng tôi đã giải quyết một số điều cơ bản về củng cố cờ.

Chúng tôi đã tìm hiểu về độ dài của công việc tạo ra biến thể, nhưng sau đó chúng tôi biết rằng chúng thông thường

tôi sẽ kết thúc bằng cách sử dụng cú pháp nén chặt chẽ này, nơi chúng tôi liệt kê tên của các biến mà chúng tôi nói là dấu hai chấm bằng,

sau đó là giá trị để gán cho biến đó.

Một lần nữa, dấu hai chấm cho biết rằng họ sắp tạo một biến mới hoặc khởi tạo một biến

Biến mới và công việc cần phải tìm loại dữ liệu chính xác mà biến cần.

Vì vậy, trong trường hợp này, GO sẽ suy nghĩ rằng chúng tôi muốn tạo một kiểu chuỗi biến thể ngay tại

đây.

Được rồi.

Chúng tôi sẽ thực hiện một chút việc dọn dẹp.

Vì vậy, tôi không thực sự muốn khai báo thêm ở đây.

Nó sẽ xóa nhận xét lớn và sau đó tôi không thực sự muốn gán lại giá trị cho thẻ, vì vậy

tôi cũng sẽ xóa nó.

Bây giờ tôi muốn tìm hiểu thêm một chút về những điều cơ bản của việc củng cố cờ.

Tôi muốn nói rằng có thể chúng tôi sẽ tự động gọi cho chúng tôi các chức năng chính, có thể chúng tôi không

biết ngay giá trị mà chúng tôi muốn phân bổ cho thẻ.

Vì vậy, tôi muốn thử xác định một chức năng riêng biệt.

Vì vậy, một chức năng đặc biệt ngoài Main.

Và bất cứ khi nào Main được thực thi, tôi muốn gọi hàm đó và trả về loại hoặc xin lỗi, tôi nên nói giá

giá trị của thẻ mà chúng tôi đang cố gắng tạo ra.

Vì vậy, về cơ bản, nó chỉ định trực tiếp giá trị của quân tại chủ bài cho quân bài

ngay tại đây, tôi muốn gọi một hàm sẽ trả về một chuỗi quân hoang.

Vì vậy, hãy bắt đầu bằng cách xác định một chức năng mới.

Việc xác định các hàm mới bên trong go sẽ sử dụng cùng một cú pháp tương tự như những gì chúng ta đã sử dụng cho hàm

chức năng chính ngay tại đây.

Vì vậy, tôi sẽ nói thẻ mới chức năng và sau đó xác định chức năng cơ thể bằng một tập hợp dấu ngoặc.

Bây giờ bên trong đây, chúng ta sẽ sử dụng một số cú pháp rất cơ bản để tạo một chuỗi mới hoặc một giá trị

new string and after that return it from function.

Bây giờ, cú pháp để làm điều đó với GO sẽ xem thực sự quen thuộc với việc bạn chọn dù bạn đến từ

bất kỳ trình cài đặt ngôn ngữ nào.

Vì vậy, bất cứ khi nào thẻ mới được gọi hoặc bất cứ khi nào nó được gọi, chúng tôi sẽ ngay lập tức trả lời về một chuỗi.

Vì vậy, tôi sẽ sử dụng lợi nhuận và sau đó chúng tôi sẽ nói, còn năm viên kim cương như vậy và như vậy thì sao?

Một lần nữa, không kể bạn đến từ bất kỳ trình cài đặt ngôn ngữ nào, vâng, lệnh trả lời

Hiện tại, điều này có vẻ khá quen thuộc để đảm bảo rằng khi chương trình của chúng được thực hiện, chúng ta gọi hàm thẻ

mới ở đó và phân bổ kết quả cho thẻ.

Ngay tại đây.

Tôi sẽ xóa Ace of Spades và thay thế nó bằng một lệnh gọi đến chức năng mới mà chúng tôi vừa tạo.

Vì vậy, giả sử thẻ mới như vậy bây giờ tôi sẽ lưu trữ tệp này và khi tôi làm như vậy, mã hóa sẽ tìm thấy dữ liệu mà chúng tôi không có

có bất kỳ lỗi nào trong tệp hiện tại hay không.

Và có vẻ như, vâng, chúng tôi đã có một cái gì đó nói ở đây.

Vì vậy, hãy di chuột qua lệnh return ở đây và tìm hiểu điều gì đang xảy ra.

Vì vậy, lỗi đã biết quá nhiều đối số để trả về chuỗi trống muốn hoặc không có gì.

Và do đó, thông báo về cơ sở cho chúng ta biết rằng chúng ta vừa viết một hàm được mong đợi là không

trả về bất kỳ dữ liệu nào, nhưng chúng tôi đã viết trong một lệnh trả về một chuỗi giá trị.

Vì vậy, chúng ta cần cập nhật khai báo hàm của mình ngay tại đây để thông báo cho trình biên dịch đi rằng

bất kể thẻ mới nào được thực thi, nó sẽ trả về một chuỗi giá trị để làm như vậy.

Ngay sau dấu ngoặc đơn ở đây, chúng ta sẽ đặt một khoảng trắng và sau đó ngay trong

from string.

Và sau đó sẽ lưu tệp.

Và khi tôi làm như vậy, tôi sẽ tìm thấy thông báo lỗi có thể bị mất.

Vì vậy, hãy nói về chính xác những gì chúng tôi làm.

Lỗi mà chúng tôi thấy rằng hàm mà chúng tôi viết ra ở đây đang cố gắng hoàn trả một giá

kiểu chuỗi giá trị khi chúng tôi đã nói rằng không có gì sẽ được trả lại để nói thêm một chút về hàm

chúng tôi vừa thực hiện.

Câu hỏi mà chúng tôi phải luôn rõ ràng và cho nó biết chính xác loại dữ liệu mà chúng tôi sẽ trả lời từ bất kỳ

bất kỳ chức năng nào đã được chọn.

Vì vậy, bằng cách đóng dấu ngoặc đơn ngay tại đây và sau đó viết ra chuỗi từ ngay sau đó

cho trình biên dịch đi rằng bất cứ khi nào thẻ mới được gọi hoặc bất cứ khi nào nó được gọi, nó

will return a string type value.

Vì vậy, hiện tại khi chúng tôi gọi thẻ mới ngay tại đây, nếu chúng tôi di chuột qua nó, bạn sẽ thấy ghi chú giải công

Công cụ nhỏ này và nó đã được biết, rồi, thẻ mới là một hàm và không trả về chuỗi giá trị.

Và vì vậy GO vẫn có thể suy ra.

Nó vẫn có thể tìm ra toán tử bằng dấu hai chấm nhỏ ngay tại đây rằng giá trị hoặc

tôi nên nói biến, xin lỗi, thẻ biến sẽ thuộc loại chuỗi vì tôi biết rằng việc làm

thẻ mới sẽ luôn trả về một biến của chuỗi loại.

Và vì vậy, nếu chúng ta di chuột qua thẻ, bạn sẽ thấy rằng nó vẫn được gắn nhãn là thẻ, thuộc loại chuỗi.

Vì vậy, về cơ bản, bạn có thể bắt đầu nhanh chóng để tìm thấy mô hình ở đây mà tại một số thời điểm

mong đợi chúng tôi gắn các loại dữ liệu nhãn đang được trao đổi xung quanh các chức năng khác của chúng tôi

bên trong chương trình của chúng tôi.

Bây giờ, chỉ cần một lần cuối cùng để thực hiện việc đưa nó về nhà, bởi vì chúng ta sẽ thấy cú pháp này nhiều lần

trong suốt khóa học này.

Tôi muốn chia nhỏ cú pháp của hàm đó.

Vì vậy, chúng tôi đã khai báo một hàm mới bằng cách sử dụng chức năng từ khóa.

Hàm có một thẻ tên mới và sau đó chúng tôi thông báo rằng bất cứ khi nào chức năng này được thực thi, nó sẽ trả lời

một chuỗi giá trị bằng cách viết chuỗi từ ngay tại đây.

Bây giờ hãy nhớ rằng, cờ vây có nhiều loại cơ sở khác nhau liên quan đến nó.

Vì vậy, trong trường hợp này, chúng tôi đã nói rằng hàm này sẽ trả về một chuỗi, nhưng

chúng tôi có thể dễ dàng nói rằng nó sẽ trả về một loại giá trị, ví dụ như int hoặc float 64 hoặc boolean.

Vì vậy, bạn có thể thực hiện nhanh chóng, hãy thử thay thế kiểu chuỗi bằng kiểu int.

Vì vậy, hãy quay lại thẻ mới Funk ngay tại đây, tôi sẽ tìm loại chuỗi.

Tôi sẽ nói, điều này, bạn biết không?

Bây giờ điều này sẽ trả về một loại giá trị, int hoặc số nguyên để thay thế.

Bây giờ, nếu tôi lưu tệp một lần nữa, chúng tôi sẽ thấy thông báo lỗi này bật lên.

Và nếu chúng ta di chuột qua nó, nó sẽ nói: Này, bạn đang cố gắng sử dụng giá trị của năm thành viên kim

cương, là một chuỗi dưới dạng số nguyên như một kết quả trả về.

Vì vậy, điều cần tìm kiếm nhanh chóng ở đây là các lỗi thông báo mà bạn nhận được rất thường xuyên

hữu ích trong công việc giúp bạn tìm ra điều gì đang xảy ra.

Vì vậy, đừng nhìn vào thông báo lỗi và nói, Ồ, có gì không ổn.

Tôi cần phải truy cập cái này của Google, đọc thông báo lỗi và cố gắng tìm ra những gì nó thực sự nói với

chúng tôi.

Điều này nói lên rằng chúng tôi đang cố gắng tận dụng giá trị của năm viên kim cương làm kiểu int, nhưng rõ ràng ở đây không

phải là số nguyên, đây là một chuỗi.

Và vì vậy, chúng tôi có thể sửa lỗi này bằng cách trả số nguyên 12.

Vì vậy, hiện tại nếu tôi lưu điều này, thông báo lỗi sẽ biến mất.

Nếu bây giờ tôi di chuột qua thẻ, bạn sẽ thấy thẻ đó bây giờ được suy ra là một số nguyên chứ không phải

is string like before that.

Vì vậy, một lần nữa, chỉ là một ví dụ nhỏ về việc sử dụng các kiểu trả tiền khác ở đây.

Tất nhiên, hiện tại chúng tôi thực sự muốn làm việc với chuỗi vì tất cả các thẻ của chúng tôi

base base will be string.

Vì vậy, tôi sẽ hoàn thành việc thay đổi mã nhỏ đó và tôi sẽ lưu tệp.

Vì vậy, hiện tại chúng tôi có một phần nhỏ khác của cú pháp cơ sở dưới vành đai của chúng ta.

Chúng tôi đã tìm cách xóa, cách khai báo các hàm đặc biệt và cách phân bổ các kiểu trả lời cho chúng.

Vậy nên chúng ta cùng nghỉ nhé, tiếp tục ở phần tiếp theo.

Và có một chủ đề nhỏ cuối cùng mà tôi muốn thảo luận trước khi chúng tôi thực sự bắt tay vào phát triển khai dự án

Thẻ của chính mình.

Vì vậy, hãy nhanh chóng nghỉ ngơi và tôi sẽ gặp bạn chỉ sau một phút.