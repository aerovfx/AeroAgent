# 005 Lý thuyết về cờ vây vi

---

Trong phần trước, chúng tôi đã bắt đầu nói về cách chúng tôi có thể khởi chạy một quy trình mới bên trong

chương trình của mình bằng cách đặt từ khóa bên trong bất kỳ lệnh gọi hàm nào.

Điều này tạo ra một quy trình mới và chúng tôi có thể nghĩ về quy trình

go like athứ gì đó bắt đầu loại bỏ hoặc thực thi các mã dòng từng dòng bên trong một hàm duy nhất.

Vì vậy, chúng tôi sẽ luôn sử dụng từ khóa đi bên trong hoặc ngay trước lệnh gọi hàm.

Bây giờ chúng ta đã có một ý tưởng hợp lý về thói quen đi là gì, chúng ta hãy bắt đầu nói về những gì thói quen đi

thực tế đang hoạt động trên máy của chúng ta hoặc trên hệ thống điều khiển của chúng ta khi chúng ta chạy.

Được chứ.

Vì vậy, trong sơ đồ này, chúng tôi đang cố gắng hiểu rõ hơn về tính chính xác của những gì sẽ xảy ra khi chúng tôi tạo ra nhiều quy trình

bên trong chương trình của mình.

Vì vậy, đằng sau hậu trường, có một thứ được gọi là Go Scheduler.

Ghost Scheduler hoạt động với một CPU trên máy cục bộ của chúng tôi.

Và như vậy, ngay khi bạn chạy một máy kép lõi theo mặc định, GO sẽ cố gắng chỉ sử dụng

sử dụng một CPU.

Chúng tôi sẽ nói về toàn bộ sơ đồ này trông như thế nào khi chúng tôi có nhiều CPU chỉ trong một giây.

Nhưng ngay lúc này, chúng ta hãy hiểu rõ hơn về những gì xảy ra với một CPU.

Vì vậy, điều quan trọng nhất cần hiểu ở đây là mặc dù chúng tôi đang khởi chạy nhiều quy trình truy cập,

Nhưng chỉ có một quy trình đang được thực thi hoặc chạy ở bất kỳ thời điểm nào.

Vì vậy, mục tiêu của lịch cài đặt này là để theo dõi quá trình chạy mã hóa của mỗi

quy trình này.

Ngay sau khi trình cài đặt này phát hiện ra rằng một quy trình đã hoàn tất việc chạy tất cả các mã hóa trong đó.

Vì vậy, hãy tải xuống cơ sở tất cả các mã bên trong một hàm nhất định hoặc khi lập lịch phát hiện đó

a function đã thực thi lệnh chặn như yêu cầu HTTP mà chúng ta đang thực hiện, thì it sẽ nói, đã được rồi, bạn biết không?

Bạn đi theo thói quen ngay tại đây.

Bạn nghĩ rằng nó vừa kết thúc hoặc có một số mã chặn đang được thực hiện?

Hiện tại bạn đã hoàn thành.

Chúng tôi sẽ tạm dừng bạn và thay vào đó chúng tôi sẽ bắt đầu thực hiện các quy trình khác.

Vì vậy, về cơ bản, mặc dù chúng tôi đang tạo ra nhiều quy trình hoạt động, nhưng chúng không thực sự được

thực thi cùng một lúc, bất kể khi nào chúng ta có CPU.

Vì vậy, CPU này chỉ chạy mã bên trong quy trình một lần tại một thời điểm.

Và chúng tôi dựa vào cài đặt lịch biểu này để quyết định quy trình nào đang được thực hiện.

Bây giờ, như tôi đã nói, tình hình hơi khác một chút khi chúng ta có nhiều CPU lõi trên máy cục bộ

của chính mình.

Vì vậy, một lần nữa tôi muốn làm rõ ở đây, theo mặc định, hãy cố gắng chỉ sử dụng một lõi

CPU.

Bây giờ chúng ta có thể dễ dàng thay đổi hành động này.

Thực hiện đơn giản để làm, nhưng theo mặc định, nó sẽ chỉ cố gắng sử dụng một lõi.

Bây giờ, nếu chúng tôi ghi đè cài đặt đó, thì cài đặt lịch ma sẽ hoạt động hơi

khác một chút.

Khi chúng tôi có nhiều CPU lõi, mỗi lõi có thể chạy một trình duy nhất tại một thời điểm.

Và vì vậy người thiết lập lịch đi có thể nói, Ồ, được rồi, chúng ta có ba quy trình đi đặc biệt và chúng

ta có ba CPU lõi đặc biệt.

Vì vậy, hãy theo dõi từng hoạt động của quy trình và cố gắng chỉ chạy một quy trình tại một thời điểm, thay vào

ở đó, bộ cài đặt sẽ chỉ định một quy trình cho phần lõi này, phần lõi khác, phần lõi thứ hai và phần cuối cùng cho phần lõi

thứ ba.

Vì vậy, ngay khi chúng tôi có nhiều CPU lõi, chúng tôi đang nói về việc chạy nhiều

đoạn mã thực thi tương tự một lần.

Nếu không, chúng tôi chỉ có một CPU.

Chúng tôi chỉ chạy một quy trình tại một thời điểm.

Tất nhiên, hiện tại chúng tôi chỉ có một CPU.

Việc thực thi có thể thay đổi lại giữa các quy trình này trong nháy mắt.

Giống như chúng ta có thể chạy quy trình này ngay tại đây trong một phần nhỏ của một phần giây và sau đó nhảy

qua cái này và sau đó quay lại cái này.

Vì vậy, bộ lập lịch làm việc rất nhanh ở hậu trường và nó sẽ xử lý tất cả các thói quen

quen nhau điều này tốt nhất có thể và chuyển qua chúng rất rất nhanh.

Được chứ.

Bây giờ, toàn bộ cuộc thảo luận này về việc chạy quy trình từng lần một như trong trường hợp này, chúng ta chỉ

có một CPU lõi hoặc chạy nhiều lõi cùng một lúc như trong trường hợp chúng tôi có nhiều CPU lõi thực sự

là chủ đề của rất nhiều cuộc thảo luận trong thế giới đi.

Vì vậy, trên thế giới, ngay khi bạn bắt đầu xem qua một số tài liệu hoặc một số bài đăng trên blog,

bạn sẽ bắt đầu tìm thấy một biểu thức này được lặp đi lặp lại mọi lúc.

Và biểu thức đó, và thực sự có một số cuộc nói chuyện nổi tiếng về chủ đề đó là sự thật đồng thời

is not a song song.

Vì vậy, bạn sẽ tìm thấy cụm từ đó ở mọi nơi.

Bạn sẽ tìm thấy cụm từ này nói rằng đồng thời không phải là một bài hát thực sự.

Và vì vậy tôi chỉ muốn ghi nhanh vào đây.

Điều này không quá liên quan đến cuộc thảo luận của chúng tôi hoặc quá liên quan đến vấn đề mà chúng tôi đang cố gắng hết sức

giải pháp ở đây đã tìm được nhiều quyết định thứ hai một lần.

Nhưng nó thực sự có liên quan khi nói về nhiều CPU so với một lõi.

Vì vậy, chúng tôi sẽ nói nhanh sang một bên ở đây chỉ để giải quyết các chủ đề nhỏ này mà bạn sẽ thấy khi bắt đầu

read a number of post on blog.

OC Vì vậy, thuật ngữ hoặc kiểu lần ví của cụm từ là câu nói đồng thời so với bài hát là

nói về sự khác biệt giữa thời gian trong một chương trình và bài hát trong một chương trình.

Và vì vậy, bất cứ khi nào bạn thấy câu nói này, tất cả những gì họ thực sự

muốn nói là bất cứ khi nào chúng tôi nói rằng một chương trình đang chạy mã đồng thời hoặc chương trình của chúng tôi đang sử dụng đồng thời

Để làm điều đó, chúng tôi đang nói rằng một chương trình đang chạy đồng thời nếu nó có khả năng tải nhiều quy trình truy cập cùng một lúc.

Bây giờ, tất cả các quy trình này có thể vẫn chỉ chạy trên một nền tảng duy nhất.

Vì vậy, khi chúng tôi nói một cái gì đó vào thời điểm đó, chúng tôi chỉ đơn giản nói rằng chương trình của chúng tôi có khả năng

chạy những thứ khác nhau một lúc, nhưng không thực sự là cùng một lúc.

Bởi vì khi chúng tôi có một lõi, chúng tôi chỉ chọn một lượt đi.

Vì vậy, tất cả những gì chúng tôi đang nói với sự thật đồng thời là chúng tôi có thể lên lịch trình công việc được thực hiện Thông suốt

xen kẽ nhau.

Chúng tôi không nhất thiết phải mong đợi một lượt xem hoàn thành quy trình trước khi chuyển sang quy trình tiếp theo.

Bây giờ, mặt trái của điều này là một bài hát thực sự.

Chúng tôi chỉ nhận được bài hát khi chúng tôi bắt đầu bao gồm nhiều vật liệu CPU cốt lõi trên máy tính của chúng tôi

bài hát, bài hát.

Theo nghĩa đen, chúng tôi đang nói rằng chúng tôi có thể làm nhiều việc cùng một lúc, dù chỉ trong khoảng thời gian ngắn như nano giây.

Và vì vậy, với bài hát, chúng ta có thể nói rằng chúng ta có một cốt lõi ở đây.

Nó phải chọn một trong những quy trình này để thực hiện.

Nhưng trong khi quy trình truy cập này ở đây có thể được thực thi thì phần cốt lõi này cũng ở một thời điểm chính xác

có thể bắt đầu xử lý một số mã hóa trong quá trình truy cập khác của quy trình này.

Vì vậy, chỉ để nhắc lại, bất cứ khi nào bạn thấy thuật ngữ này đồng thời với bài hát với đồng

Hiện tại, chúng tôi chỉ nói rằng chúng tôi có thể nâng cao lịch làm việc và thay đổi chúng giữa một cách nhanh chóng với bài hát.

Chúng tôi đang nói rằng chúng tôi có thể làm nhiều công việc cùng một lúc theo đúng nghĩa.

Vì vậy, cốt lõi này có thể chạy một quy trình tương tự với một thời điểm xác định mà cốt lõi này có thể chạy một quy trình khác.

Vì vậy, có thể có rất nhiều về thói quen đi.

Bây giờ, có một điều cuối cùng mà tôi muốn chỉ ra cho bạn rất nhanh, bởi vì ngay sau khi chúng tôi bắt

đầu phát triển các quy trình trong chương trình của mình, chúng tôi sẽ tìm thấy lỗi khi thực hiện điều thú vị này

hiện tại gần như ngay lập tức.

Vì vậy, một điều tôi chỉ muốn ra ở đây và chúng tôi sẽ quay lại

sơ đồ này ngay khi gặp lỗi này, tôi chỉ muốn bạn hiểu rằng khi chúng chạy một chương trình tương tự như khi chúng

ta thực thi nó ở dòng lệnh , chúng tôi luôn nhận được một quy trình mặc định được tạo cho chúng tôi.

Vì vậy, đây giống như một thói quen thông thường.

Đây là thứ đã được tạo cho tất cả các chương trình mà chúng tôi đã tạo trong khóa học này cho đến nay.

Và nó là thứ bắt đầu chạy tất cả các mã hóa trong tệp chính của chúng ta.

Bây giờ, khi chúng tôi bắt đầu khởi chạy các quy trình bên trong mã của chúng tôi, tất cả các hoạt động quy trình khác đều là những

chúng tôi gọi là thói quen đi trẻ em.

Và tất cả chúng đều được tạo ra bằng cách sử dụng từ khóa đó.

Bây giờ những thói quen đi lại của trẻ em này không hoàn toàn được tôn trọng như nhau, tôi mong đợi, vì thiếu một thuật ngữ tốt

hơn, chúng ta sẽ nói sự tôn trọng như một thói quen chính.

Vì vậy, họ phải vẽ một đường thẳng trên cát giữa thói quen chính của chúng và những thói quen

quen trẻ em này.

Bây giờ, tất cả những điều này có vẻ như thực sự bí mật được truyền tải ngay bây giờ, nhưng ngay sau đó chúng tôi bắt đầu bổ sung thêm các quy trình vào

Trong video tiếp theo, chúng tôi sẽ quay lại phần này ngay lập tức và chúng tôi sẽ hiểu rõ hơn về

những gì tôi đang nói với điều nhỏ bé này ngay tại đây.

Một lần nữa, chúng tôi sẽ gặp lỗi ngay lập tức.

Và tất cả đều liên quan đến thực tế này là chúng ta có một thói quen quen thuộc chính và sau đó là một loạt các thói quen quen thuộc.

Vì vậy, với suy nghĩ đó, chúng ta hãy nghỉ ngơi nhanh chóng.

Chúng tôi sẽ quay lại phần tiếp theo và chúng tôi sẽ bắt đầu hỗ trợ bổ sung về quá trình làm quen lại cho

chương trình của chúng ta.

Vì vậy, hãy nhanh chóng nghỉ ngơi và tôi sẽ gặp bạn chỉ sau một phút.