# 005 Lý thuyết về các thói quen đi vi

---

Giảng viên: Ở phần trước chúng ta đã bắt đầu nói chuyện

về cách chúng ta có thể khởi động một quy trình đi mới

bên trong chương trình của chúng tôi

bằng cách đặt từ khóa go bên trong bất kỳ lệnh gọi hàm nào.

Việc làm này sẽ tạo ra một thói quen đi mới.

Và chúng ta có thể coi thói quen đi như một điều gì đó

bắt đầu nhai hoặc thực thi các dòng mã

từng dòng một bên trong một hàm duy nhất.

Vì vậy, chúng tôi sẽ luôn sử dụng từ khóa go

bên trong hoặc ngay trước lệnh gọi hàm.

Bây giờ chúng ta đã có một ý tưởng hợp lý

về thói quen đi lại là gì, hãy bắt đầu nói về

những gì các quy trình đang thực sự thực hiện trên máy của chúng tôi

hoặc trên hệ điều hành của chúng tôi khi chúng tôi chạy chúng.

Được rồi, trong sơ đồ này,

chúng tôi đang cố gắng hiểu rõ hơn

về chính xác những gì xảy ra khi chúng ta sinh sản

nhiều quy trình đi bên trong chương trình của chúng tôi.

Vậy đằng sau hậu trường, có một thứ gọi là

bộ lập lịch đi.

Bộ lập lịch hoạt động với một CPU trên máy cục bộ của chúng tôi.

Và vì vậy, ngay cả khi bạn đang chạy máy lõi kép,

theo mặc định, go sẽ cố gắng chỉ sử dụng một CPU.

Chúng ta sẽ nói về toàn bộ sơ đồ này trông như thế nào

khi chúng ta có nhiều CPU hơn chỉ trong một giây.

Nhưng hiện tại, hãy hiểu rõ hơn

về những gì xảy ra với một CPU.

Vì vậy, điều quan trọng nhất cần hiểu ở đây là,

mặc dù chúng tôi đang triển khai nhiều quy trình đi,

chỉ có một cái đang được thực thi hoặc đang chạy tại bất kỳ thời điểm nào.

Vì vậy, mục đích của công cụ lập lịch trình này là để

theo dõi mã đang chạy

bên trong mỗi thói quen này.

Ngay khi bộ lập lịch này phát hiện

rằng một quy trình đã chạy xong tất cả mã

bên trong nó, vì vậy về cơ bản tất cả mã

bên trong một hàm nhất định,

hoặc khi bộ lập lịch phát hiện ra rằng một chức năng đã được thực hiện

một cuộc gọi chặn, như yêu cầu HTTP mà chúng tôi đang thực hiện,

sau đó nó nói, được rồi, bạn biết gì không?

Bạn, hãy làm việc bình thường ngay tại đây,

bạn, thứ vừa hoàn thành hoặc có mã chặn nào đó

việc đó đang được thực thi, bạn đã hoàn tất ngay bây giờ.

Chúng tôi sẽ tạm dừng bạn và thay vào đó

chúng ta sẽ bắt đầu thực hiện quy trình đi khác này.

Vì vậy, về cơ bản, mặc dù chúng ta đang sinh sản

thực hiện nhiều thói quen, chúng không thực sự

được thực hiện thực sự cùng một lúc

bất cứ khi nào chúng ta có một CPU.

Vậy CPU này chỉ chạy mã

bên trong một thói quen tại một thời điểm

và chúng tôi dựa vào công cụ lập lịch trình này để quyết định

thủ tục nào đang được thực thi.

Bây giờ, như tôi đã nói, tình hình có một chút

khác khi chúng ta có nhiều lõi CPU

trên máy cục bộ của chúng tôi.

Một lần nữa, có một điều tôi muốn làm rõ ở đây,

theo mặc định, hãy cố gắng chỉ sử dụng một lõi CPU.

Bây giờ chúng ta có thể dễ dàng thay đổi hành vi này,

thực sự đơn giản để làm, nhưng theo mặc định

nó sẽ chỉ cố gắng sử dụng một lõi.

Bây giờ, nếu chúng tôi ghi đè cài đặt đó,

sau đó bộ lập lịch đi sẽ hoạt động

hơi khác một chút.

Khi chúng ta có nhiều lõi CPU, mỗi lõi có thể chạy

thực hiện một thói quen tại một thời điểm.

Và người lên lịch trình có thể nói, ồ được rồi,

chúng tôi có ba thói quen đi riêng biệt

và chúng tôi có ba lõi CPU riêng biệt.

Vì vậy, thay vì theo dõi từng thói quen đi

và cố gắng chỉ chạy một lần một lần,

thay vào đó, bộ lập lịch sẽ chỉ định một quy trình cho lõi này,

một cái khác đến lõi thứ hai,

và cái cuối cùng đến lõi thứ ba.

Vì vậy ngay khi chúng ta có nhiều lõi CPU,

sau đó chúng ta đang nói về việc chạy nhiều khối

mã thực sự cùng một lúc.

Mặt khác, khi chúng ta chỉ có một CPU,

chúng tôi chỉ chạy một quy trình tại một thời điểm.

Tất nhiên là bây giờ khi chúng ta chỉ có một CPU,

việc thực hiện có thể thay đổi qua lại

giữa những thói quen này trong chớp mắt.

Giống như chúng ta có thể chạy quy trình này ngay tại đây

trong một phần của một phần giây,

và sau đó chuyển sang cái này,

và sau đó nhảy trở lại cái này.

Vì vậy bộ lập lịch hoạt động rất nhanh

đằng sau hậu trường và nó sẽ được xử lý

tất cả những thói quen khác nhau này diễn ra tốt nhất có thể

và quay vòng qua chúng rất, rất nhanh.

Được rồi, bây giờ toàn bộ cuộc thảo luận về

chạy từng bước một,

như trong trường hợp này khi chúng ta chỉ có một lõi CPU,

hoặc chạy nhiều lần cùng một lúc, như trong trường hợp

rằng chúng ta có nhiều lõi CPU,

thực sự là chủ đề của rất nhiều cuộc thảo luận

trong thế giới cờ vây.

Vì vậy, trong thế giới cờ vây, ngay khi bạn bắt đầu

tìm hiểu kỹ một số tài liệu hoặc một số bài đăng trên blog,

bạn sẽ bắt đầu thấy biểu hiện này

lặp đi lặp lại mọi lúc.

Và biểu hiện đó, và thực sự có một số bài phát biểu nổi tiếng

về chủ đề này, đó là sự đồng thời không phải là sự song song.

Vì vậy, bạn sẽ thấy cụm từ đó ở khắp mọi nơi.

Bạn sẽ thấy cụm từ này có nội dung

đồng thời không phải là song song.

Và vì vậy, tôi chỉ muốn viết một ghi chú nhanh vào đây.

Điều này không liên quan lắm đến cuộc thảo luận của chúng ta

hoặc siêu liên quan để thích vấn đề

chúng tôi đang cố gắng giải quyết việc tìm nạp ở đây

nhiều thứ cùng một lúc,

nhưng nó thực sự có liên quan để nói về

nhiều lõi CPU so với một lõi.

Vì vậy chúng ta sẽ nói nhanh sang một bên ở đây chỉ để

giải quyết chủ đề nhỏ này mà bạn sẽ thấy

khi bạn bắt đầu đọc một số bài đăng trên blog.

Được rồi, vậy thuật ngữ hoặc kiểu chuyển cụm từ

hoặc câu nói đồng thời so với song song

đang nói về sự khác biệt giữa

đồng thời bên trong một chương trình

so với tính song song trong một chương trình.

Và vì vậy, bất cứ khi nào bạn nhìn thấy câu nói,

tất cả những gì họ thực sự muốn nói là,

bất cứ khi nào chúng tôi nói rằng một chương trình đang chạy mã

đồng thời hoặc chương trình của chúng tôi đang sử dụng đồng thời

để làm điều gì đó, chúng ta đang nói rằng một chương trình

là đồng thời, nếu nó có khả năng tải lên

nhiều thói quen đi cùng một lúc.

Hiện tại, tất cả các quy trình hoạt động này có thể vẫn chỉ đang chạy

trên một lõi duy nhất.

Vì vậy, khi chúng ta nói điều gì đó xảy ra đồng thời, chúng ta chỉ đơn giản nói

rằng chương trình của chúng tôi có khả năng chạy nhiều thứ khác nhau

gần như cùng một lúc, nhưng thực tế không phải cùng một lúc.

Bởi vì khi chúng ta có một lõi,

chúng tôi chỉ chọn một thói quen đi.

Vì vậy, tất cả những gì chúng tôi đang nói với sự đồng thời là chúng tôi có thể

loại lịch trình công việc phải được thực hiện lẫn nhau.

Chúng ta không nhất thiết phải chờ đợi một lần

để kết thúc trước khi chuyển sang phần tiếp theo.

Bây giờ, mặt trái của điều này là sự song song.

Chúng tôi chỉ nhận được sự song song khi chúng tôi bắt đầu bao gồm

nhiều lõi CPU vật lý trên máy của chúng tôi.

Với sự song song, chúng tôi thực sự đang nói rằng

chúng ta có thể làm nhiều việc cùng lúc như nano giây.

Và vì vậy, với sự song song chúng ta có thể nói

rằng chúng ta có một lõi ở đây.

Nó phải chọn một trong những thủ tục này để thực thi.

Nhưng trong khi việc này diễn ra thường xuyên ở đây

có thể được thực thi, lõi khác này

đồng thời cũng có thể bắt đầu nhai kỹ

một số mã bên trong quy trình khác này.

Vì vậy xin nhắc lại, bất cứ khi nào bạn nhìn thấy thuật ngữ này

đồng thời so với song song, với đồng thời,

chúng tôi chỉ nói rằng chúng tôi có thể lên lịch làm việc

và sự thay đổi nhanh chóng giữa chúng.

Với sự song song, chúng tôi đang nói rằng chúng tôi có thể thực sự

làm nhiều việc cùng một lúc.

Vì vậy, lõi này có thể chạy một quy trình vào cùng một thời điểm chính xác

lõi này chạy một quy trình khác.

Được rồi, có lẽ đó là rất nhiều về thói quen cờ vây.

Bây giờ, có một điều cuối cùng tôi muốn chỉ ra

gửi cho bạn thật nhanh, vì ngay khi chúng ta bắt đầu

để triển khai các quy trình đi bên trong chương trình của chúng tôi,

chúng ta sẽ thấy lỗi thực sự thú vị này xuất hiện

gần như ngay lập tức.

Vì vậy có một điều tôi muốn chỉ ra ở đây,

và chúng ta sẽ quay lại sơ đồ này

ngay khi chúng tôi gặp phải lỗi này,

Tôi chỉ muốn bạn hiểu rằng, khi chúng tôi chạy một chương trình,

giống như khi chúng ta thực thi nó ở dòng lệnh,

chúng tôi luôn tạo một thói quen mặc định này cho chúng tôi.

Vì vậy, đây giống như thói quen chính.

Đây là thứ đã được tạo ra

cho mọi chương trình mà chúng tôi đã tạo

trong khóa học này cho đến nay.

Và đó là thứ bắt đầu chạy tất cả mã

bên trong tệp .go chính của chúng tôi.

Bây giờ khi chúng ta bắt đầu khởi chạy các quy trình bên trong mã của mình,

tất cả những thói quen đi khác đó là những gì chúng tôi đề cập đến

khi còn nhỏ đi theo thói quen.

Và vì vậy, tất cả chúng đều được tạo bằng cách sử dụng từ khóa go đó.

Bây giờ, những thói quen đi lại của trẻ này không hoàn toàn

được tôn trọng ở mức độ như nhau,

Tôi đoán vì thiếu một thuật ngữ tốt hơn, chúng ta sẽ nói sự tôn trọng,

như thói quen chính là.

Và vì vậy, chúng ta phải vẽ kiểu như

một đường thực tế trên cát

giữa thói quen chính của chúng ta và thói quen của trẻ em này.

Hiện tại, tất cả những điều này có vẻ thực sự bí truyền.

Nhưng ngay khi chúng ta bắt đầu thêm vào các thói quen

trong video tiếp theo, chúng ta sẽ quay lại ngay

sang phần này và chúng ta sẽ hiểu rõ hơn

về những gì tôi đang nói về điều nhỏ bé này ngay tại đây.

Một lần nữa, chúng ta sẽ gặp phải một lỗi ngay lập tức

và tất cả đều liên quan đến thực tế này là chúng ta có

một thói quen đi chính, và sau đó là một loạt các thói quen trẻ em.

Được rồi, với ý nghĩ đó, chúng ta hãy nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay lại ở phần tiếp theo

và chúng tôi sẽ bắt đầu thêm hỗ trợ

để thực hiện các quy trình cho chương trình của chúng tôi.

Vậy nên hãy nghỉ ngơi nhanh và tôi sẽ gặp bạn sau một phút nữa.