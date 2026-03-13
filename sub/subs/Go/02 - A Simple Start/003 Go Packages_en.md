# 003 Gói đi en

---

Giảng viên: Trong video trước chúng ta đã tìm ra

cách chạy mã bên trong dự án của chúng tôi.

Bây giờ chúng ta sẽ chuyển sang tìm hiểu

chính xác dòng mã đầu tiên đó là gì

bên trong tệp main.go của chúng tôi có nghĩa là,

cụ thể là dòng có nội dung package main.

Đầu tiên chúng ta sẽ nói về gói từ

và sau đó chúng ta sẽ nói về

tại sao chúng ta lại dùng từ chính ở đây.

Được rồi, để tôi vẽ sơ đồ.

Bắt đầu nào.

Vì vậy khi bạn nhìn thấy gói từ trong Go, bạn có thể nghĩ

của một gói giống như một dự án hoặc một không gian làm việc.

Một gói là một tập hợp các tệp mã nguồn phổ biến.

Vì vậy nếu bạn và tôi đang làm việc trên một ứng dụng kín đáo,

giống như hiện tại chúng tôi đang làm việc trên một ứng dụng,

theo truyền thống, chúng tôi sẽ tạo một gói duy nhất.

Vì vậy, một gói có thể có nhiều tệp liên quan bên trong nó,

mỗi tệp kết thúc bằng phần mở rộng tệp là .go.

Yêu cầu duy nhất đối với mọi tệp bên trong gói

đó có phải là dòng đầu tiên của mỗi tập tin

phải khai báo gói chứa nó.

Ví dụ: nếu ba tệp này ở đây

tất cả đều thuộc gói chính, sau đó mỗi tệp

cần phải có gói câu lệnh chính ở trên cùng,

giống như tệp main.go hiện tại của chúng tôi thực hiện ngay tại đây.

Vì vậy, nếu chúng ta có hai tệp khác trong dự án này

hoặc bên trong gói này, họ cũng sẽ cần

để khai báo gói chính ở trên cùng.

Bây giờ tôi muốn kể cho bạn nghe một chút về

chính xác lý do tại sao chúng tôi gọi gói của mình là main.

Bạn biết đấy, tại sao chúng ta gọi nó là chính?

Tại sao chúng ta không gọi nó là HELLOWORLD

đặt tên cho thư mục chứa nó?

Chà, bên trong Go, có

hai loại gói khác nhau.

Có một loại thực thi và một loại có thể tái sử dụng.

Một loại gói thực thi

là một cái mà khi biên dịch sẽ phun ra

một tệp có thể chạy thực tế hoặc một tệp thực thi,

giống như những gì chúng tôi đã thấy khi thực hiện

lệnh go build tại dòng lệnh của chúng tôi.

Hãy nhớ khi chúng ta chạy go build main.go như thế này nhé,

nó phun ra tập tin chính này ngay tại đây,

mà sau đó chúng tôi có thể chạy và thực thi.

Vì vậy, tập tin này ngay tại đây đã được tạo ra một cách cụ thể

bởi vì chúng tôi đã tạo một loại gói có thể thực thi được.

Các gói thực thi thường được sử dụng

vì thực sự đang làm điều gì đó

Và đó chủ yếu là những gì chúng tôi sẽ làm

sẽ làm trong khóa học này.

Bạn biết đấy, chúng tôi sẽ viết các chương trình có thể chạy

và chúng ta có thể sử dụng chúng để hoàn thành nhiệm vụ.

Chúng tôi cũng có quyền truy cập vào các gói có thể tái sử dụng.

Và bạn có thể coi những điều này giống như

phụ thuộc mã hoặc thư viện.

Đây là những gói không được sử dụng

để nói, thích, nhấp đúp vào và thực hiện.

Thay vào đó chúng tôi đưa vào rất nhiều logic có thể tái sử dụng

hoặc các chức năng hoặc nội dung trợ giúp sẽ chỉ giúp chúng ta

tái sử dụng một số mã cho các dự án tương lai trong tương lai.

Vì vậy, có thể bạn hơi tò mò, làm sao chúng tôi biết

liệu chúng ta đang tạo một gói thực thi hay một gói có thể tái sử dụng?

Vậy làm thế nào để chúng ta biết khi nào chúng ta đang làm cái này hay cái kia?

Nếu bạn nhìn vào tệp mã nguồn của chúng tôi,

rõ ràng là không có gì thực sự ở đây nói rằng,

ồ vâng, hãy đưa ra một số tệp thực thi khi bạn biên dịch tôi.

Vậy làm thế nào để chúng ta biết khi nào chúng ta đang làm cái này hay cái kia?

Chà, thực sự thì nó có một chút khó khăn.

Hãy nhớ rằng chúng ta đã gọi gói của mình bằng tên main.

Vì vậy, dòng đầu tiên dành cho chúng ta

bên trong tệp của chúng tôi có ghi gói main.

Thực ra đó là tên của gói

mà bạn sử dụng sẽ xác định liệu bạn có đang thực hiện

một gói loại thực thi hoặc phụ thuộc.

Vì vậy, cụ thể từ chính được sử dụng

để tạo một gói loại thực thi.

Vì vậy, chúng tôi lấy gói chính, chạy và xây dựng trên đó,

và nó phun ra một tập tin có tên là main

hoặc main.exe nếu bạn đang dùng Windows.

Nếu chúng tôi đã sử dụng bất kỳ tên nào khác cho gói của mình ngoài tên chính,

nên nếu chúng ta gọi nó là gói blahblah,

rồi chạy go build thì nó không hiện ra

một tập tin thực thi thực tế.

Cho nên từ gói chính là thiêng liêng.

Đó là thứ chúng tôi chỉ sử dụng khi chúng tôi thực hiện

một gói mà chúng tôi muốn tạo ra một số tệp có thể chạy được.

Trong suốt phần còn lại của khóa học này,

bạn và tôi sẽ thực hiện các dự án

chủ yếu sử dụng gói tên main

bởi vì chúng tôi thường luôn muốn tạo ra

thứ gì đó mà chúng tôi có thể chạy và kiểm tra ngay lập tức.

Tuy nhiên, nếu chúng ta đang cố gắng tạo ra

một số thư viện mã có thể tái sử dụng hoặc nếu chúng tôi muốn tạo

một số dự án mà chúng ta có thể chia sẻ

với bạn bè của chúng tôi để họ có thể sử dụng mã của chúng tôi

trong dự án riêng của họ, đó là lúc chúng tôi bắt đầu

sử dụng tên gói chuyên biệt hơn.

Bây giờ để tóm tắt, về cơ bản bất cứ khi nào chúng ta thấy

từ gói chính có nghĩa là

chúng tôi đang tạo một gói thực thi.

Bất kỳ tên nào khác có nghĩa là chúng tôi đang tạo ra một sản phẩm có thể tái sử dụng

hoặc gói loại phụ thuộc.

Bây giờ điều cuối cùng tôi muốn nói với bạn về điều này,

điều cuối cùng là bất cứ lúc nào chúng ta thực hiện

một gói thực thi thì nó phải luôn có

một hàm bên trong nó cũng được gọi là main.

Vì vậy, nếu chúng ta quay lại trình soạn thảo mã của mình,

đó chính là nội dung của tuyên bố này.

Chúng tôi đã nói func main.

Vì vậy, chúng tôi đặc biệt tạo ra một hàm gọi là main

bởi vì chúng tôi đã gọi gói chính ở đây,

tạo một gói loại thực thi.

Bây giờ, để cung cấp cho bạn bản demo nhanh về điều này,

Tôi sẽ đi đến dòng mã đầu tiên ở đây

và tôi sẽ đổi tên gói của mình thành apple.

Bây giờ tôi sẽ quay trở lại thiết bị đầu cuối của mình.

Nếu tôi liệt kê tất cả các tập tin và thư mục của mình,

bạn sẽ thấy rằng tôi vẫn có tệp thực thi chính ngay tại đây.

Vì vậy tôi sẽ loại bỏ nó thật nhanh chóng.

Bây giờ tôi chỉ quay lại main.go.

Nếu bây giờ tôi tạo tệp này bằng tên gói khác

rồi liệt kê tất cả các tập tin và thư mục của tôi, bạn sẽ thấy điều đó

Tôi không nhận được một thứ thực sự có thể thực thi được ở đây.

Vì vậy, rõ ràng tên của gói có vấn đề.

Bây giờ tôi sẽ thay đổi lại

với tên gói chính như vậy.

Tôi sẽ quay lại, xây dựng lại dự án của mình,

và bây giờ tôi thấy rằng tôi đã lấy lại được tệp thực thi ở đây.

Được rồi, tôi nghĩ thế là đủ

cho các gói ngay bây giờ.

Một lần nữa, chúng ta sẽ có thêm nhiều kinh nghiệm

với các gói trong tương lai.

Vì vậy, ngay bây giờ, chúng ta hãy tập trung vào

câu hỏi tiếp theo mà chúng ta muốn tìm hiểu

chính xác dòng mã tiếp theo có ý nghĩa gì.

Vì vậy, hãy nghỉ ngơi nhanh chóng và bắt đầu nói về

câu lệnh nhập đó trong phần tiếp theo.