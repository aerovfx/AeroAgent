# 4 -Yield From và Close the Generators.en US

---

Tiếp tục nào.

Hy vọng bạn có niềm vui trong việc này

Khóa học Python và hy vọng bạn có

đánh giá chúng tôi bằng những lời tốt đẹp của bạn.

Chúng tôi thực sự cần điều đó.

Vì vậy, trong phần này của Python

tất nhiên chúng ta sẽ làm việc đó

chúng ta thực sự có thể mang lại một số giá trị.

Trong trường hợp bạn nhớ từ

video cuối cùng của chúng ta

nói về máy phát điện.

Chúng ta đã thấy khá nhiều, khá nhiều

một chi tiết ẩn về họ.

Nhưng bây giờ chúng tôi muốn xem thêm hai

mọi thứ và đó là nó, đó

tất cả là về máy phát điện.

Một điều phổ biến

đôi khi máy phát điện

không tạo ra giá trị hoặc

tự nó mang lại giá trị.

Đôi khi nó mượn giá trị

từ một nơi khác.

Điều đó hoàn toàn có thể.

Chúng ta sẽ xem một ví dụ đúng

vì điều đó và đôi khi có thể

bạn không muốn tạo ra sự nghỉ ngơi

của các giá trị từ một trình tạo,

hoặc có thể đó là một máy phát điện vô hạn.

Chúng tôi không muốn giữ nó

trong ký ức mãi mãi.

Chúng tôi muốn đóng nó lại vì vậy

rằng nó đã bị xóa khỏi bộ nhớ

và chúng tôi hoàn thành công việc.

Đây là một kịch bản phổ biến

trong cơ sở dữ liệu.

Bất cứ khi nào một chức năng gọi

bạn mang lại một chuỗi kết nối

từ cơ sở dữ liệu.

Và một khi tất cả đã xong bạn

cuối cùng hãy cố gắng đóng cái này lại.

Mặc dù logic có chút

khác nhau trong cơ sở dữ liệu

nhưng bạn sẽ thấy phần nào đó tương tự

loại ví dụ xuất hiện.

Hãy để tôi đưa bạn lên màn hình

và điều tiếp theo chúng tôi muốn

để làm trong sản lượng này cũng giống như

chúng tôi đã làm việc về việc gửi dữ liệu,

bây giờ chúng tôi muốn làm việc dựa trên lợi nhuận từ

và chúng tôi cũng sẽ làm việc trên

đóng lại.

Vậy chúng ta thực hiện những điều này như thế nào?

Làm thế nào chúng ta có thể đạt được từ

và làm thế nào để chúng ta đóng cái này?

Nó thực sự cực kỳ dễ dàng nếu bạn

cứ tiếp tục và nhìn vào đây.

Vì vậy hãy tạo một mẫu

ví dụ cho việc này.

Tôi sẽ đóng mọi thứ chúng ta đã làm

khá nhiều và hãy tạo ra

một tập tin mới và chúng tôi sẽ viết cả hai

ví dụ trong cùng một tập tin.

Hãy gọi this1 là 04 đóng.

Jenny Raytor Chúng ta bắt đầu thôi.

Py.

Được rồi, những gì chúng ta sẽ làm,

trước hết tôi sẽ tắt AI của mình.

Nếu không thì tôi, tôi hầu như không sử dụng nó.

Tôi luôn giữ im lặng.

Nhưng tôi không biết tại sao.

Tôi có phần mở rộng này

kích hoạt trong này.

Có lẽ tôi sẽ thoát khỏi điều này.

Vì vậy hãy nói rằng chúng ta chỉ đơn giản là đi

phía trước và xác định một chai địa phương.

Vâng, chai là chủ đề

của toàn bộ khóa học này.

Chúng tôi sẽ không đi

để nó trở lại bất cứ lúc nào.

Thực ra nó rất vui.

Rất nhiều người yêu thích chai.

Hoặc bạn có thể thay thế bằng cà phê như

à trong trường hợp bạn là một fan hâm mộ lớn.

Và một khi chúng tôi hoàn thành việc này, chúng tôi

sẽ tiếp tục và nói năng suất.

Lần đầu tiên bạn gọi cái này, nó

nói rằng tôi sẽ mời bạn một chai masala.

Lần tiếp theo bạn tiếp tục

và gọi cái này, cái này sẽ xảy ra

để tặng bạn chai gừng.

Được rồi, đủ tốt, đủ công bằng.

Chúng tôi có một cái khác đó là

chai nhập khẩu.

Thế đấy.

Và cái này cũng mang lại kết quả.

Vì vậy chúng ta sẽ đầu hàng

và lần đầu tiên chúng ta sẽ

có một chai nhập khẩu.

Vì vậy tôi nghĩ Macha là một

của hàng nhập khẩu, rất nổi tiếng

của Nhật cũng vậy.

Và Oolong thực sự là

không phải từ Ấn Độ.

Vì vậy trà ô long được ưa chuộng

một lần nữa ở Đông Nam Á,

nhưng không hẳn là ở Ấn Độ.

Bạn cũng có một số kiến ​​thức về chai.

Vì vậy chúng ta sẽ định nghĩa một cách đơn giản

menu đầy đủ trong menu đầy đủ này.

Và cách thức hoạt động của toàn bộ menu

là chúng ta sẽ lấy dữ liệu

một chút từ chai địa phương, một chút

từ cái nhập khẩu.

Vậy cách chúng tôi làm điều đó,

thực sự khá dễ dàng.

Chúng ta có thể sử dụng năng suất, nhưng không chỉ

chỉ cần năng suất, chúng ta thực sự có thể sử dụng

một cú pháp khác bắt nguồn từ đó.

Nó gần giống như khi

bạn thực sự viết

ở trên cùng từ tập tin này.

Tôi muốn nhập chức năng này.

Nó gần như giống hệt nhau.

Tất cả những gì bạn phải làm là có địa phương này

chai và đảm bảo rằng đây là

một lỗi kinh điển mà bạn mắc phải

muốn gọi hàm ở đây.

Tương tự trong dòng này chúng tôi muốn

tiếp tục lần này chúng tôi muốn

để có chai nhập khẩu.

Vì vậy hãy chắc chắn rằng bạn thực hiện điều đó

và đó là nó.

Đó là tất cả những gì bạn có.

Để thấy được điều này như thế nào

chức năng thực sự hoạt động, chúng ta chỉ có thể

hãy tiếp tục và nói cho chai đầy đủ

thực đơn, giống như thế này và chúng ta sẽ bắt đầu

nhường một lần.

Chúng tôi sẽ không sử dụng tiếp theo

tiếp theo, tiếp theo bạn biết cú pháp

của nó nếu nó được yêu cầu.

Nhưng trong trường hợp này tôi sẽ chỉ

hãy tiếp tục và nói chúng ta hãy

in giá trị chai ở đây.

Khá dễ dàng.

Không đến nỗi tệ, không đến nỗi tệ.

Tôi sẽ tiếp tục và nói,

này con trăn, hãy chạy 04 đi

và thế là chúng ta thấy

chai masala, chai gừng.

Vì vậy sau đó chúng tôi đã nhận được

matcha và ô long.

Hay quá, khá vui

rằng chúng tôi đã nhập khẩu thứ đó.

Và một khi bạn thấy lợi nhuận, nó thực sự

tiếp tục và làm tất cả công việc.

Bây giờ chúng ta hãy tiếp tục và xem liệu chúng ta

có thể vượt qua cách chúng ta thực sự có thể

kết thúc nửa chừng mọi việc.

Vâng, điều đó hoàn toàn có thể.

Tôi sẽ chỉ cho bạn một ví dụ.

Giả sử chúng ta có một gian hàng chai

và cái này khá thú vị

một vì chúng ta sẽ đi

để sử dụng cú pháp khác là Try

Catch hay còn gọi là Try Accept.

Trong thế giới Python, chúng tôi gọi nó là

như Hãy thử và chấp nhận, nhưng trong hầu hết

của thế giới lập trình khác

ngôn ngữ được gọi là Try Catch.

Vì vậy, đừng nhầm lẫn với điều đó.

Bất cứ khi nào tôi nói Hãy thử bắt hoặc bất cứ ai

người khác nói Hãy thử bắt điều đó có nghĩa là

thực hiện cú pháp thử ngoại trừ.

Đó là một cú pháp hợp lệ, có sẵn

Trong Java, JavaScript,

Swift, hầu hết mọi ngôn ngữ.

Vì vậy chúng ta sẽ tiếp tục và nói

chúng tôi muốn thử một cái gì đó

Tôi sẽ viết pass trong giây lát

và sau đó chúng tôi thực sự tiếp tục

và điền vào đó bằng chấp nhận.

Tôi sẽ tiếp tục và chấp nhận,

cứ như thế này và chúng ta sẽ nói vượt qua.

Vì vậy, đây là một cú pháp cơ bản.

Bây giờ chúng ta sẽ nghiên cứu thêm về

điều này, mặc dù chúng ta không cần phải làm vậy.

Đây là tất cả về cú pháp.

Nếu có lỗi

trong khối thử, bạn thử

để thực thi một số đoạn mã.

Nếu có vấn đề,

nó được xử lý trong giấy chấp nhận

hoặc giai đoạn ngoại lệ.

Nhưng dù sao tôi cũng sẽ tiếp tục và nói

trong khi đúng, vì vậy chúng tôi đang tạo ra

một hằng số, chúng tôi sẽ giữ

một đơn đặt hàng và đơn đặt hàng này thực sự là

tăng lên từ sản lượng.

Và chúng tôi cũng sẽ chuyển đi một thông điệp

trong đó nói đang chờ gọi chai.

Một cú pháp thú vị khác.

Vâng, tôi biết.

Và sau khi chúng ta xong việc ở đây,

chúng tôi đang nhận được đơn đặt hàng,

chúng ta sẽ tiếp tục và in

đây là một tin nhắn đơn giản có nội dung

gian hàng đóng cửa, không còn chai nữa.

Vì vậy trong trường hợp có điều gì đó xảy ra

sai rồi, chúng ta đi như vậy.

Bây giờ kết thúc ở đâu

cú pháp trong tất cả những điều này?

Đừng lo lắng, có

kiên nhẫn, tôi sẽ cho bạn thấy.

Trước hết, hãy nói rằng chúng tôi mang đến

lên một quầy hàng và quầy hàng đó đến

từ quầy hàng chai, cứ như thế.

Để có thể tiến về phía trước

và bắt đầu việc này, chúng ta sẽ đi

để tiếp tục và in cái này.

Tôi sẽ nói nó như thế này.

Tôi sẽ sử dụng cú pháp tiếp theo và trong

cú pháp tiếp theo tôi sẽ chuyển sang

đi trước và vượt qua gian hàng này.

Được rồi.

Khá dễ dàng.

Đẹp.

Được rồi, giờ hãy xem nào

xảy ra nếu tôi tiếp tục và chạy

phần lớn mã này.

Điều này thật thú vị.

Thực ra nếu tôi chạy thông báo này ở đây,

nó bảo đang chờ gọi chai.

Không còn trật tự nào nữa.

Chúng tôi chỉ đơn giản nói gian hàng

đóng lại, không còn chai nữa.

Được rồi, nhưng không sao, đó là

chính xác những gì chúng tôi muốn đi cùng

đó là vì chúng ta đã không vượt qua

bất kỳ giá trị nào, chúng tôi đã không gửi bất cứ thứ gì,

nhớ cú pháp gửi.

Nhưng thật thú vị là bạn thực sự có thể

hãy tiếp tục và đóng nó lại một cách duyên dáng

chỉ bằng cách sử dụng lệnh đóng Chạy cái này.

Đó là nó.

Bây giờ điều gì xảy ra khi tôi chạy cái này?

Điều đó thật thú vị.

Lưu ý ở đây.

Hoàn toàn giống nhau.

Và đây có lẽ là lý do

tại sao nhiều người

không thực sự đóng nó.

Họ chỉ chờ đợi thôi, này, nó

có thể sẽ tự động đóng,

đó không phải là một ý tưởng tốt

Bạn phải luôn có trách nhiệm

để đóng máy phát điện của bạn.

Và mọi chuyện diễn ra như thế này.

Điều này được gọi là nó kích hoạt

một phương pháp thoát máy phát điện

thực sự chịu trách nhiệm cho việc này.

Vì vậy, điều này không chỉ đóng cái này,

đây thực sự là một sự dọn dẹp.

Bạn đang dọn dẹp bộ nhớ của mình

và điều này nên được thực hiện.

Điều này rất quan trọng.

Vì thế.

Được rồi.

Hy vọng bạn có được điều này.

Hãy để tôi cung cấp cho bạn một bản tóm tắt nhanh chóng

bởi vì này, chúng tôi đã nghiên cứu rất nhiều.

Vì vậy điều đầu tiên mà chúng tôi

đã nghiên cứu là cú pháp lợi nhuận.

Đây là một điều rất, rất

cú pháp thú vị.

Nó làm gì nó tạm dừng và tiếp tục

việc thực hiện một chức năng.

Đây là nhân vật chính

chịu trách nhiệm về

chuyển đổi thành máy phát điện.

Sau đó chúng tôi nghiên cứu về cú pháp tiếp theo

đó là nhận phần tiếp theo theo cách thủ công

giá trị nào, tùy theo máy phát điện

sẽ nhường bước cho tôi.

Sau đó chúng tôi cũng đi lên và nghiên cứu

cú pháp gửi thực sự là

gửi dữ liệu vào máy phát điện.

Chúng tôi cũng đã đi lên và nghiên cứu

cú pháp của năng suất từ.

Và đó chỉ đơn giản là nhận được

từ một máy phát điện khác

hoặc ủy quyền cho trình tạo phụ

hoặc lặp lại bất kỳ nhiệm vụ nào.

Nó không chỉ luôn luôn

nhận được giá trị.

Đôi khi bạn muốn ủy thác một số việc

nhiệm vụ này, bạn sẽ làm nhiệm vụ đó.

Vì vậy, chúng ta thực sự có thể đi

phía trước và làm điều đó.

Và cuối cùng nhưng không kém phần quan trọng

một cái gần gũi.

Đây thường là việc dọn dẹp.

Điều này duyên dáng dừng lại

máy phát điện lại, nó dừng

tự động là tốt.

Nhưng chúng tôi thực sự muốn

dừng máy phát điện một cách duyên dáng để

không có rò rỉ bộ nhớ.

Chương trình của bạn hoạt động tốt.

Không có sự cố bộ nhớ, rất nhiều lợi thế.

Chúng ta hãy tiếp tục và bắt

lên trong video tiếp theo.