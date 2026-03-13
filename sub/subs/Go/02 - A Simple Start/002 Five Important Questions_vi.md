# 002 Năm câu hỏi quan trọng vi

---

Trong phần cuối, chúng tôi đã tổng hợp lại một chương trình rất nhỏ, rất cơ bản, rất công phu.

Và vì vậy tôi sẽ không nói dối.

Đúng.

Một chương trình phong cách giới giới cực kỳ chán nản.

Và tôi biết đó là điều mà bạn không thực sự muốn tìm thấy trong khóa học.

Bạn muốn tìm thấy một cái gì đó hữu ích hơn, hào phóng hơn, thú vị hơn.

Tuy nhiên, tôi nghĩ rằng bạn sẽ thực sự ngạc nhiên ở đây bởi vì mặc dù đây là một chương

trình diễn cực kỳ chán nản, chúng ta sẽ xem xét từng dòng một.

Và tôi nghĩ rằng bạn sẽ rất ngạc nhiên khi biết chính xác về lượng kiến thức mà bạn có thể thu được bằng cách nghiên cứu

love từng dòng mã bên trong tệp này.

Vì vậy, trong video này và một vài video tiếp theo, chúng ta sẽ chia nhỏ điều này từng dòng một

và sử dụng nó để xử lý tốt hơn một số khái niệm cơ bản xung quanh.

Bây giờ, tôi đã tự động phân tích mọi dòng trong đây.

Và sau khi làm như vậy, tôi đã nghĩ ra câu hỏi cơ bản trong năm mà chúng ta có thể sử dụng để hiểu

hơn về những gì chương trình đó đang làm.

Vì vậy, đây là câu hỏi cơ bản mà tôi muốn trả lời.

Và ngay sau khi chúng tôi trả lời những điều này, chúng tôi sẽ hiểu rõ hơn về các nguyên tắc cơ bản của hoạt động.

Vì vậy, trước tiên, hãy làm cách nào để chúng tôi chạy mã hóa trong dự án của chúng tôi?

Giống như chúng ta đã viết ra một số đoạn mã, nhưng chúng ta thực sự thực thi nó như thế nào?

Làm cách nào để chúng tôi chạy nó?

Tôi cũng muốn biết dòng đầu tiên của chương trình có nghĩa là gì, cụ thể là dòng có

nội dung Gói Main.

Và vì vậy tôi muốn tìm hiểu gói đó là gì?

Nghĩa chính là gì?

Điều đó tốt cho chúng ta là gì?

Tiếp theo, tôi muốn tìm dòng tiếp theo khi nhập Fmt.

Tôi muốn tìm hiểu xem cái thứ chức năng đó ở bên dưới là gì.

Và cuối cùng, có vẻ như mã bên trong tệp chính được sắp xếp theo cách nào đó.

Đúng vậy, bởi vì chúng tôi đặc biệt đặt gói chính ở trên cùng, sau đó chúng tôi đã nhập và sau đó chúng tôi

viết một hàm.

Và vì vậy tôi muốn hiểu rõ hơn về công việc có hay không có một mẫu chung nào mà chúng tôi muốn đưa ra theo bất kỳ

bất cứ khi nào chúng ta viết mã go.

Vì vậy, đây là năm câu hỏi mà chúng tôi sẽ cố gắng trả lời bằng cách nghiên cứu mã bên trong

của chương trình rất đơn giản, rất dễ hiểu điều này.

Vì vậy, chúng tôi bắt đầu ngay bây giờ với câu hỏi số một.

Làm thế nào để chúng tôi chạy mã hóa trong dự án của chúng tôi?

Làm cách nào để chúng tôi chạy mã hóa?

Tôi sẽ chuyển sang thiết bị cuối cùng của mình.

Vì vậy, đây là thiết bị đầu tiên của tôi và bạn sẽ nhận thấy rằng tôi đã hướng dẫn dự án của mình.

Thư mục của Hello World.

Bên trong đây, tôi có tệp chính của mình.

Vì vậy, tại thời điểm này, bạn nên tạm dừng video thật nhanh, mở thiết bị đầu cuối của bạn và điều hướng đến bất kỳ nơi nào

bạn đã tạo dự án thư mục đầu tiên của chúng tôi.

Bây giờ tôi đang ở đây, tôi sẽ sử dụng lệnh go mà chúng tôi đã thử nghiệm trước đó.

Xin hãy nhớ rằng, chúng tôi đã tham gia chỉ một mình và chúng tôi đã nhận được thông báo trợ giúp cũ rất lớn ngay tại đây.

Hãy nhớ rằng lệnh go là loại cổng thông tin của chúng ta để làm việc với tất cả thứ trên bộ máy cục bộ của chúng ta.

Vì vậy, lệnh này cung cấp cho chúng tôi khả năng biên dịch và thực hiện các dự án mà chúng tôi tổng hợp lại với nhau.

Hãy tìm cách chạy tệp chính đầu tiên.

Chúng ta sẽ viết Run, Go, Run, Main Go.

Khi chúng tôi làm như vậy, chúng tôi sẽ ngay lập tức thấy thông báo.

Chào bạn.

In it ra màn hình.

Vì vậy, đó là một cách dễ dàng để chạy mã.

Trong dự án của chúng tôi, chúng tôi viết Go Run và sau đó là tên của tệp mà chúng tôi muốn thực hiện.

Rõ ràng là hiện tại, tôi muốn bạn biết thêm nhiều điều về cách chúng tôi chạy mã hóa trong dự án của mình.

Vì vậy, chúng tôi hãy chia nhỏ lệnh này ngay tại đây và tìm ra những gì nó thực sự có thể làm cho chúng ta.

Được rồi.

Vì vậy, chúng tôi sẽ đưa ra một sơ đồ ở đây.

Chúng ta bắt đầu.

Và đây là sơ đồ của một số lệnh khác có sẵn cho chúng ta với dòng giao diện

command or go CLI.

Vì vậy, chúng tôi vừa thử nghiệm lệnh, đi, chạy, chạy, có thể lấy một hoặc hai hoặc ba hoặc bốn, một

một số ít tệp.

Nó biên dịch tất cả mã hóa trong các tệp đó và sau đó thực hiện kết quả ngay lập tức.

Vì vậy, bất cứ khi nào chúng ta có một hoặc hai tệp, chúng ta nói Chạy đi, sau đó nói tên của tệp, một hoặc nhiều tệp mà

chúng tôi muốn biên dịch và thực thi và rơi vào cuộc đua chúng ta đi.

Mặt khác, chúng tôi cũng có một lệnh gọi là Go Build, Go Build rất giống Go Run.

Và đó là lý do tại sao tôi muốn dành một chút thời gian để đảm bảo rằng có sự khác biệt giữa hai người

ít nhất rõ ràng một cách hợp lý.

Vì vậy, Go Run được sử dụng để biên dịch và thực hiện ngay lập tức một chương trình.

Mặt khác, Go Build được sử dụng để biên dịch một chương trình.

Vì vậy, Go Build chỉ cần biên dịch nó và nó không thực thi nó.

Nếu chúng tôi lặp lại lệnh của mình và chạy, hãy bắt đầu xây dựng chính sách.

Bạn sẽ thấy rằng chúng tôi không thể nhận được bất kỳ điều gì.

Xin chào, in ra màn hình.

Nhưng nếu bây giờ chúng tôi liệt kê tất cả các tệp và thư mục bên trong thư mục này, bạn sẽ tìm thấy một tệp

mới có tên là Main.

Nếu bạn đang ở trên windows, bạn có thể thấy điều này được phản ánh dưới dạng XY chính.

Vì vậy, đây là một tệp thực tế được tạo từ nguồn mã chính của chúng tôi.

Nếu bạn đang sử dụng windows hoặc nếu bạn đang sử dụng Mac, thì bây giờ bạn có thể chạy tệp này bằng cách chạy dấu gạch chéo chính

và nếu bạn đang ở trên windows, bạn có thể chạy chính XY để thực thi tệp này.

Vì vậy, một lần nữa, có sự khác biệt giữa chạy và đi, xây dựng, xây dựng, biên dịch tệp dịch, đi, chạy, biên dịch

và thực thi nó.

Bây giờ một số công cụ phổ biến khác được đính kèm với go cli.

Chúng tôi sẽ tiến hành rất nhanh.

Chúng tôi cũng sẽ đề cập đến một số vấn đề sau trong khóa học.

Format Go được sử dụng để tự động định dạng tất cả các mã hóa trong tất cả các tệp khác của chúng tôi.

Chúng tôi sẽ tìm thấy một ví dụ khá hay về dạng Go ngay khi chúng tôi bắt đầu làm việc với dự án đầu

Đầu tiên, cài đặt và Go Get là hai lệnh được sử dụng để xử lý các phụ thuộc trong dự án của chúng ta.

Vì vậy, nếu chúng tôi muốn sử dụng mã do người khác viết, chúng tôi có thể sử dụng các lệnh này để truy cập vào

nó trong các dự án cá nhân của chúng ta.

Cuối cùng, hãy thực hiện kiểm tra được sử dụng để chạy và thực hiện bất kỳ thử nghiệm tệp nào được liên kết với hiện tại dự án và chắc chắn chúng ta

cũng sẽ tìm thấy một ví dụ điển hình về lệnh này.

Được rồi.

Vì vậy, tôi nghĩ rằng loại câu trả lời là câu hỏi số một ở đây.

Làm thế nào để chúng tôi chạy mã hóa trong dự án của chúng tôi?

Chúng tôi sử dụng lệnh go tool.

Chúng tôi có thể chạy tệp cài đặt ngay lập tức hoặc chúng tôi có thể xây dựng nó và sau đó chạy nó trong tương lai tại bất kỳ thời điểm nào của chính chúng.

Tôi nghĩ đó là câu trả lời câu hỏi số một.

Chúng tôi hãy giải lao nhanh chóng và sau đó tiếp tục trả lời câu hỏi tiếp theo của chúng tôi trong video tiếp theo.

Vì vậy, tôi sẽ gặp bạn chỉ sau một phút.