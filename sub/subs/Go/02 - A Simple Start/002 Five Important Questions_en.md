# 002 Năm câu hỏi quan trọng vi

---

Giáo viên: Ở phần cuối,

chúng tôi ghép lại với nhau một cái rất nhỏ,

chương trình rất cơ bản, rất nhàm chán.

Và vì vậy, tôi sẽ không nói dối, vâng,

một chương trình kiểu hello world rất nhàm chán,

và tôi biết đó là điều mà bạn thực sự không

muốn xem trong một khóa học.

Bạn muốn thấy thứ gì đó hữu dụng hơn,

hào nhoáng hơn, thú vị hơn.

Tuy nhiên, tôi nghĩ bạn sẽ thực sự ngạc nhiên ở đây

bởi vì mặc dù đây là một chương trình rất nhàm chán,

chúng ta sẽ đi qua từng dòng một.

Và tôi nghĩ bạn sẽ rất ngạc nhiên

để xem chính xác bạn có thể thu được bao nhiêu kiến thức

bằng cách nghiên cứu từng dòng mã bên trong tệp này.

Vì vậy, trong video này và vài video tiếp theo,

chúng ta sẽ chia nhỏ vấn đề này ra từng dòng một

và sử dụng nó để xử lý tốt hơn nhiều

về một số khái niệm cơ bản cơ bản xung quanh cờ vây.

Bây giờ tôi đã lấy tự do

đã phân tích từng dòng bên trong đây

và sau khi tôi làm vậy,

Tôi nghĩ ra năm câu hỏi cơ bản mà chúng ta có thể sử dụng

để có được cảm giác tốt hơn

về chương trình đó đang làm gì.

Vì vậy, đây là năm câu hỏi cơ bản mà tôi muốn trả lời.

Và ngay khi chúng tôi trả lời những điều này,

chúng ta sẽ hiểu rõ hơn về các nguyên tắc cơ bản của cờ vây.

Vậy trước hết, làm cách nào để chạy mã bên trong dự án của chúng ta?

Giống như chúng tôi đã viết ra một số mã,

nhưng làm thế nào để chúng ta thực sự thực hiện nó?

Làm thế nào để chúng tôi chạy nó?

Tôi cũng muốn biết dòng đầu tiên là gì

của chương trình có nghĩa là,

cụ thể là dòng có nội dung package main.

Và vì vậy tôi muốn tìm hiểu, bạn biết đấy, gói hàng là gì?

chính nghĩa là gì?

Điều đó có ích lợi gì cho chúng ta?

Tiếp theo, tôi muốn tìm ra dòng tiếp theo, import fmt.

Tôi muốn tìm hiểu xem chức năng đó là gì

xuống phía dưới.

Và cuối cùng, có vẻ như đoạn mã bên trong

của tệp main.go đó được sắp xếp theo cách nào đó, phải không?

Bởi vì chúng tôi đặc biệt đặt gói main ở trên cùng,

sau đó chúng tôi nhập và viết một hàm.

Và vì thế, tôi muốn hiểu rõ hơn

về việc có hay không có một khuôn mẫu chung mà chúng ta muốn

để theo dõi bất cứ khi nào chúng tôi viết mã Go.

Được rồi, đây là năm câu hỏi

mà chúng tôi sẽ cố gắng trả lời bằng cách nghiên cứu mã

bên trong chương trình rất đơn giản, rất dễ hiểu này.

Vì vậy, hãy bắt đầu ngay bây giờ với câu hỏi số một.

Làm cách nào để chạy mã bên trong dự án của chúng tôi?

Chúng ta chạy mã như thế nào?

Tôi sẽ chuyển sang thiết bị đầu cuối của mình.

Đây là thiết bị đầu cuối của tôi và bạn sẽ nhận thấy

mà tôi đã điều hướng

vào thư mục dự án helloworld của tôi.

Bên trong đây, tôi có tệp main.go của mình.

Vì vậy, tại thời điểm này, bạn nên tạm dừng video thật nhanh.

Mở terminal của bạn và điều hướng

đến bất cứ nơi nào bạn đã tạo thư mục dự án đầu tiên của chúng tôi.

Bây giờ tôi đã ở trong đây, tôi sẽ tận dụng

của lệnh go mà chúng tôi đã thử nghiệm trước đó.

Hãy nhớ rằng, chúng tôi đã vào chỉ cần đi một mình,

và chúng tôi nhận được thông báo trợ giúp cũ kỹ ngay tại đây.

Hãy nhớ rằng lệnh go là một loại cổng thông tin của chúng tôi

để làm việc với mọi thứ trên máy cục bộ của chúng tôi.

Vì vậy lệnh go này cho chúng ta khả năng biên dịch

và thực hiện các dự án mà chúng tôi đã cùng nhau thực hiện.

Hãy tìm cách chạy tệp dự án đầu tiên của chúng ta, main.go.

Chúng ta sẽ viết go run main.go.

Khi làm như vậy chúng ta sẽ thấy ngay thông báo

Xin chào, được in ra trên màn hình.

Được rồi, vậy này, đó là một điều dễ dàng.

Để chạy mã trong dự án của chúng tôi, chúng tôi viết go run

và sau đó là tên của tệp mà chúng tôi muốn thực thi.

Bây giờ, rõ ràng là tôi muốn kể cho bạn nhiều điều hơn nữa

về cách chúng tôi chạy mã bên trong dự án của mình.

Vì vậy, hãy chia nhỏ lệnh go này ngay tại đây

và tìm hiểu xem nó thực sự có thể làm gì cho chúng ta.

Được rồi, chúng ta sẽ vẽ sơ đồ ở đây.

Bắt đầu nào.

Được rồi. Và đây là sơ đồ của một số

trong số các lệnh khác nhau có sẵn cho chúng tôi

với Go CLI hoặc giao diện dòng lệnh.

Vì vậy, chúng tôi vừa thử nghiệm lệnh chạy.

Chạy có thể mất một hoặc hai hoặc ba hoặc bốn,

một số tập tin.

Nó biên dịch tất cả mã trong các tệp đó

và sau đó thực hiện ngay kết quả.

Vì vậy, bất cứ khi nào chúng tôi có một hoặc hai tệp,

chúng tôi nói hãy chạy và sau đó là tên của các tập tin,

một hoặc nhiều mà chúng tôi muốn biên dịch

và thực hiện và bùng nổ, bắt đầu cuộc đua mà chúng tôi tham gia.

Bây giờ, mặt khác,

chúng tôi cũng có một lệnh gọi là go build.

Go build rất giống go run

và đó là lý do tại sao tôi muốn dành một chút

thời gian để đảm bảo rằng sự khác biệt

giữa hai điều này ít nhất là rõ ràng một cách hợp lý.

Vì vậy go run được sử dụng để biên dịch

và thực hiện ngay một chương trình.

Mặt khác,

go build được sử dụng để biên dịch một chương trình.

Vì vậy, hãy xây dựng chỉ cần biên dịch nó

và nó không thực sự thực hiện nó.

Nếu chúng ta quay lại dòng lệnh của mình

và chạy go build main.go, bạn sẽ thấy

rằng chúng tôi không nhận được bất kỳ lời chào nào được in ra trên màn hình.

Nhưng nếu bây giờ chúng ta liệt kê tất cả các tập tin và thư mục

bên trong thư mục này,

you're gonna see a new file called main.

Nếu bạn đang dùng Windows,

bạn có thể sẽ thấy điều này được phản ánh dưới dạng main.exe.

Vì vậy, đây là một tập tin thực thi thực tế đã được xây dựng

nằm ngoài mã nguồn main.go của chúng tôi.

Nếu bạn đang dùng Windows hoặc xin lỗi nếu bạn đang dùng Mac,

bây giờ bạn có thể chạy tệp này bằng cách chạy ./main.

Và nếu bạn đang dùng Windows,

bạn có thể chạy main.exe để thực thi tệp này.

Được rồi, một lần nữa, sự khác biệt giữa go run và go build.

Go build biên dịch tập tin.

Chạy biên dịch và thực thi nó.

Bây giờ, một số công cụ thông dụng khác được đính kèm

tới Go CLI, chúng ta sẽ thực hiện rất nhanh.

Chúng tôi sẽ đề cập đến một vài trong số này sau

trong khóa học là tốt.

Định dạng Go được sử dụng để tự động định dạng

tất cả mã bên trong

của tất cả các tập tin khác nhau của chúng tôi.

Chúng ta sẽ sớm thấy một ví dụ khá hay về định dạng cờ vây

khi chúng tôi bắt đầu thực hiện dự án đầu tiên của mình.

Go install và go get là hai lệnh được sử dụng

để xử lý các phần phụ thuộc bên trong các dự án của chúng tôi.

Vì vậy, nếu chúng ta muốn sử dụng mã đã được viết

bởi người khác, chúng ta có thể sử dụng các lệnh này để có quyền truy cập

để nó vào các dự án cá nhân của chúng tôi.

Cuối cùng, go test được sử dụng để chạy và thực thi bất kỳ file test nào

có liên quan đến dự án hiện tại,

và chúng ta chắc chắn sẽ thấy một ví dụ điển hình

của lệnh này là tốt.

Được rồi, tôi nghĩ kiểu đó

câu trả lời cho câu hỏi số một ở đây.

Làm cách nào để chạy mã bên trong dự án của chúng tôi?

Chúng tôi sử dụng công cụ dòng lệnh Go.

Chúng tôi có thể chạy tệp ngay lập tức hoặc chúng tôi có thể xây dựng nó

và sau đó tự mình chạy nó trong tương lai vào một thời điểm nào đó.

Vì vậy, tôi nghĩ sẽ trả lời câu hỏi số một.

Hãy nghỉ ngơi nhanh chóng và sau đó tiếp tục

với câu hỏi tiếp theo của chúng tôi trong video tiếp theo.

Vậy tôi sẽ gặp bạn sau một phút nữa.