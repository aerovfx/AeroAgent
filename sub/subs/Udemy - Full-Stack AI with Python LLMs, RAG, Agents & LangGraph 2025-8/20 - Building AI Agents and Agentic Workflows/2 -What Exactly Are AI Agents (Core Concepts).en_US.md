# 2 - Tác nhân AI chính xác là gì (Khái niệm cốt lõi).en Hoa Kỳ

---

Được rồi, vậy đặc vụ AI là gì?

Và từ này có nghĩa là gì?

Khi nào chúng ta gọi LLM là đại lý?

Hãy hiểu điều đó.

Được rồi, vậy ngay bây giờ

hãy quên mọi thứ về AI đi.

Hãy nói rằng, chúng ta không biết

bất cứ điều gì về AI.

Hệ thống truyền thống hoạt động như thế nào?

Được rồi, theo cách truyền thống

hệ thống bạn có người dùng.

Được rồi, vậy hãy nói rằng đây là

người dùng ứng dụng của bạn.

Được rồi, điều đó thật tuyệt.

Những người dùng ứng dụng của bạn

nói chuyện với, với một máy chủ.

Được rồi, vậy hãy nói rằng bạn

có một số loại máy chủ.

Vậy hãy để tôi mang theo

trong một máy chủ ở đây.

Vì vậy, hãy nói rằng đây là của bạn

máy chủ và nếu bạn đang làm việc

trên kiến trúc microservice,

vậy về cơ bản bạn có rất nhiều

của máy chủ, giả sử rằng

đây là dịch vụ thanh toán của bạn

Được rồi, hãy đặt tên nó là khoản thanh toán.

SVC dành cho dịch vụ.

Được rồi, vậy tôi sẽ chỉ sử dụng

dạng ngắn ở đây.

Vì vậy, đây là dịch vụ thanh toán của bạn.

Giả sử đây là của bạn

dịch vụ xác thực.

Vậy đây là của bạn

dịch vụ xác thực.

Có lẽ đây là điều gì đó, bạn biết đấy,

một số dịch vụ cho đơn đặt hàng của bạn.

Được rồi, đây là đơn đặt hàng của bạn

dịch vụ nếu bạn đang xây dựng

một cái gì đó giống như Amazon, phải không?

Và sau đó bạn có một cái gì đó được gọi là,

giả sử, bạn biết đấy,

thanh toán được thực hiện, đơn đặt hàng được thực hiện.

Có lẽ đây là máy chủ vận chuyển của bạn.

Được rồi, dịch vụ vận chuyển.

Điều đó thật tuyệt.

Vì vậy theo truyền thống những gì đang xảy ra,

về cơ bản người dùng đang nói chuyện

với nhiều dịch vụ, phải không?

Vậy điều đó có nghĩa là bạn có một số

loại proxy ngược ở giữa, hoặc

chúng ta hãy tạo một kết nối trực tiếp.

Vì vậy, về cơ bản người dùng đang nói chuyện

tới máy chủ của bạn.

Và những máy chủ này, phải không?

Tất cả các máy chủ này đều nằm trong nội bộ

sử dụng một số cơ sở dữ liệu.

Vì vậy, giả sử trong hệ thống của bạn

bạn có một số cơ sở dữ liệu.

Vì vậy, hãy mang theo một số MongoDB.

Được rồi, vậy là bạn có MongoDB,

cơ sở dữ liệu đang chạy.

Vậy dịch vụ thanh toán đang tương tác

với MongoDB và dịch vụ đặt hàng là

cũng tương tác với MongoDB.

Giả sử tôi chỉ lấy,

bạn biết đấy, những ví dụ ngẫu nhiên.

Và sau đó hãy nói rằng bạn cũng vậy

có một postgres, bạn biết đấy, cơ sở dữ liệu

ở đâu, xác thực

dịch vụ thực sự đang sử dụng

điều đặc biệt này, postgres.

Giả sử dịch vụ vận chuyển là

cũng sử dụng cơ sở dữ liệu này.

Và Dịch vụ xác thực cũng sử dụng

MongoDB để làm điều gì đó.

Đây là hệ thống lưới điển hình của bạn

microservice của bạn.

Microservice, kiến ​​trúc.

Được rồi?

Bây giờ đột nhiên những gì xảy ra là.

Bây giờ chuyện gì xảy ra?

Mọi thứ đều hoạt động tốt.

Bạn có cơ sở dữ liệu, bạn có

máy chủ, bạn có người dùng.

Bây giờ doanh nghiệp nói, này, phải không?

Bây giờ hãy nói rằng bạn muốn

để thêm một hệ thống hỗ trợ.

Được rồi?

Vì vậy, trong các hệ thống truyền thống,

hệ thống hỗ trợ,

hệ thống hỗ trợ khách hàng là

ngay bây giờ được xử lý thủ công.

Điều bạn cần làm là bạn có

triển khai một số đại lý.

Được rồi?

Đây là những đại lý thực sự.

Tôi không nói về AI, tôi đang nói

về các tác nhân thực sự của con người.

Vì vậy, hãy nói rằng đây là bạn của bạn

biết đấy, những đặc vụ thực sự đang ngồi

trong một trung tâm cuộc gọi của Amazon.

Thế là bạn có một, bạn có hai,

bạn có ba và bạn có bốn.

Bây giờ điều xảy ra là khi ai đó

đối mặt với một vấn đề, với mệnh lệnh của họ,

với các khoản thanh toán của họ,

họ có thể liên hệ trực tiếp với họ.

Được rồi?

Bây giờ những gì các đại lý này

về cơ bản họ có quyền truy cập

vào hệ thống, phải không?

Họ có quyền truy cập vào đơn đặt hàng của bạn,

họ có quyền truy cập vào hồ sơ của bạn,

họ có quyền truy cập vào thông tin vận chuyển của bạn

thông tin cũng như các khoản thanh toán của bạn.

Vì vậy, việc truy cập các đơn đặt hàng này,

một dịch vụ và dịch vụ vận chuyển là

được trao cho các đại lý này

để họ có thể hỗ trợ bạn tốt hơn,

họ có thể hướng dẫn bạn tốt hơn.

Vì vậy có thể bạn đã gọi cho họ và bạn

hỏi, này, bạn biết đấy, tôi chỉ

đã đặt hàng và đơn hàng của tôi

vẫn chưa nhận được hay sao

tình trạng đơn hàng của tôi là gì?

Vì vậy, các đại lý hỗ trợ này là

về cơ bản chỉ là ngồi nhàn rỗi

bất cứ khi nào họ nhận được một truy vấn.

Họ sử dụng các dịch vụ này để truy cập

thông tin riêng tư của bạn

và sau đó họ có thể hỗ trợ bạn tốt hơn

này, chính xác thì chuyện gì đã xảy ra vậy?

Và trong một số trường hợp họ có thể

cũng thay đổi điều gì đó.

Có thể bạn đã gọi họ

và nói, này, tôi không cần thứ đó

thứ tự cụ thể, không còn nữa, vì vậy

bạn có thể vui lòng hủy đơn hàng của tôi được không?

Vì vậy, các đại lý hỗ trợ này có thể

thậm chí hủy đơn hàng của bạn

sử dụng những dịch vụ này phải không?

Tuyệt vời.

Vì vậy những gì tôi đã nói bạn là đúng

bây giờ những người này, nhóm này

của mọi người được gọi là

đại lý hỗ trợ hoặc hỗ trợ khách hàng.

Tại sao đây là những đại lý bởi vì

về mặt kỹ thuật họ được cung cấp một số

hướng dẫn rằng này, khi bạn

nhận được một cuộc gọi bạn phải lắng nghe

cho truy vấn người dùng đang làm gì.

Và dựa vào đó bạn có thể thực hiện

những hành động nhất định, bất cứ điều gì

bạn thích trên hệ thống này.

Được rồi, bây giờ mục tiêu chúng ta hướng tới

việc cần làm là chúng ta có thể tự động hóa không

thứ đặc biệt này.

Ý tôi là tất nhiên là chúng tôi, chúng tôi không muốn

để can thiệp vào thứ này.

Tất cả điều này đang hoạt động

một cách rất tốt đẹp.

Bằng cách nào đó chúng ta có thể thay thế những người này

với AI về cơ bản là của bạn

AI tác nhân tham gia vào cuộc chơi.

Bây giờ vấn đề là như vậy

bây giờ giả sử bạn có bằng LLM,

bạn có LLM từ OpenAI.

Được rồi, đây là LLM,

OpenAI là một LLM, được chứ?

Họ có GPT và tất cả.

Giả sử bạn cũng có Song Tử.

Vì vậy, hãy mời cả Song Tử nữa.

Bây giờ đây là những gì

hai cái này là gì vậy?

Hai cái này về cơ bản là

mô hình LLM của bạn.

Giả sử đây là Song Tử, đây

là GPT4O của bạn và chúng là

ngồi, bạn biết đấy, ở một máy chủ nào đó

của OpenAI và Google.

Và khi bạn cho họ một ít,

đầu vào, họ cung cấp cho bạn một đầu ra.

Bạn nói xin chào, bạn sẽ quay lại

xin chào, bạn nói gì đó,

bạn sẽ nhận được phản hồi.

Vì vậy đây là những điển hình

Các mô hình từ A đến T, tức là

mô hình văn bản thành văn bản.

Mục đích chung của các mô hình này là

rằng bạn đưa cho tôi một số mã thông báo đầu vào.

Bạn đưa cho tôi mã thông báo đầu vào và tôi sẽ

dự đoán, được rồi, tôi sẽ dự đoán,

dự đoán bộ mã thông báo đầu ra tiếp theo.

Đó là toàn bộ động cơ

của các mô hình LLM này.

Bây giờ, bây giờ chỉ cần nghĩ về điều này.

Làm thế nào những văn bản này có thể dự đoán được

người mẫu thay thế những kẻ này?

OpenAI của tôi có thể truy cập máy chủ không?

Không, nó không thể.

OpenAI của tôi có thể làm được gì không

theo những mệnh lệnh này?

Không, nó không thể.

Vậy vấn đề là ở chỗ đó

họ không thể làm bất cứ điều gì.

Họ thật ngu ngốc.

Được rồi?

Hiện tại những mô hình LLM này,

nếu chúng ta chỉ làm nổi bật chúng.

Vì vậy nếu tôi phải viết một định nghĩa

theo cách nói của tôi thì đây là,

bọn này ngu ngốc, được chứ?

Đoạn mã ngu ngốc, được chứ?

Đoạn mã ngồi

trong một máy chủ, được chứ?

Lấy văn bản làm đầu vào

và đưa ra văn bản làm đầu ra.

Vậy đây là định nghĩa đúng

cho những mô hình LLM này phải không?

Bạn chỉ có thể đọc nó

đây, tôi sẽ chỉ đặt ở đây.

Vì vậy, chỉ cần đi qua điều này

định nghĩa cụ thể.

Bây giờ, với tư cách là một nhà phát triển, điều chúng tôi có thể làm là

chúng ta có thể chuyển đổi những LLM này, những

đoạn mã ngu ngốc thành một đại lý.

Làm sao?

Tôi sẽ chỉ cho bạn một bước

từng bước, hướng dẫn.

Vì vậy điều tôi có thể làm là

Tôi có thể làm một số phép thuật.

Giả sử tôi có thể viết một số mã

và chuyển đổi chúng thành một đại lý.

Được rồi?

Bây giờ khi bạn chuyển đổi những thứ này

cho các đại lý, bây giờ những LLM này

bằng cách nào đó sẽ có khả năng

để truy cập vào các máy chủ.

Làm sao?

Chút nữa tôi sẽ kể cho cậu nghe, được chứ?

Nó sẽ có quyền truy cập

đến dịch vụ AUTH.

Nó cũng sẽ có quyền truy cập để xem

đưa một cái gì đó vào cơ sở dữ liệu.

Nó cũng sẽ có khả năng

để nói chuyện với người dùng.

Vậy điều đó có nghĩa là những gì bạn đã làm là

sử dụng một số lớp ma thuật ở giữa.

Bạn đã biến LLM này thành một khả năng

để nói chuyện với máy chủ của bạn, để tạo API

gọi đến máy chủ của bạn, để truy cập

cơ sở dữ liệu và nói chuyện với con người.

Bây giờ những gì đã xảy ra là bởi vì

nó có khả năng

để làm một nlp, được chứ?

Đó là xử lý ngôn ngữ tự nhiên.

Nó có thể thấy những gì bạn đang yêu cầu.

Dựa vào đó, được chứ?

Trên cơ sở đó, các mô hình này có thể

truy cập vào máy chủ, lấy

một số thông tin về đơn đặt hàng của bạn,

làm điều gì đó cho bạn

đặt hàng và hỗ trợ bạn tốt hơn.

Vì vậy đây là nơi chúng tôi gọi điều đó.

Bây giờ nó là một đại lý, được chứ?

Bây giờ nó là một đại lý.

Tôi sẽ cho bạn một ví dụ thực tế.

Được rồi?

Hãy nói với tôi một điều thôi.

Đây là cái gì?

Đây là bộ não phải không?

Mọi người đều có nó, bạn có nó.

Tôi cũng có nó phải không?

Bộ não là quan trọng nhất

một phần cơ thể của chúng ta.

Toàn bộ cơ thể tôi, bàn tay của tôi, của tôi.

Mọi thứ đang được kiểm soát

bởi bộ não này.

Được rồi?

Nhưng hãy nói với tôi một điều.

Nếu tôi cho bạn một bộ não,

được rồi, được giữ trong một cái hộp, đầy đủ

hoạt động được, nó có thể làm được gì không?

Bộ não này có thể dạy bạn không?

Bộ não này có thể mã hóa được không?

Bộ não này có thể giúp được gì không?

bạn với bất cứ điều gì?

Không, bởi vì bộ não này có thể

quá trình, nó có thể lấy đầu vào, nó có thể

đưa ra tín hiệu như một đầu ra.

Nhưng vấn đề là bộ não này

cần một cơ thể, được chứ?

Bộ não này cần một cơ thể

thực sự, thực sự

thực hiện, thực hiện một số công việc.

Đó là điều chính.

Vì vậy về cơ bản bộ não là

về cơ bản giống như LLM, được chứ?

Bộ não cũng giống như một LLM vậy.

Được rồi, đó là một chiếc LLM không có phần thân.

Bây giờ với tư cách là nhà phát triển, điều chúng tôi có thể làm là

chúng ta có thể sử dụng bộ não này, được chứ?

Chúng ta có thể sử dụng bộ não này và chúng ta

có thể cho anh ta một cơ thể.

Một cơ thể về cơ bản có nghĩa là những gì tôi

sẽ làm là tôi sẽ đưa cái này

bộ não cụ thể là một số cánh tay, được chứ?

Cánh tay và bạn biết đấy, bàn tay, được rồi.

Vì vậy xin hãy thứ lỗi cho bức vẽ của tôi,

nhưng vâng, tôi sẽ đưa cái này

đặc biệt là não vài cái chân, được chứ?

Vì vậy hãy nói, này, bây giờ

bạn cũng có chân.

Và bây giờ tại thời điểm đặc biệt này

điểm, trí thông minh của não

đã ở đó rồi.

Tôi đã cho anh ấy khả năng

để di chuyển xung quanh.

Bây giờ điều này đã trở thành một đại lý.

Bây giờ nó là một đại lý.

Được rồi?

Đại lý.

Vâng.

Vì vậy, điều đó có nghĩa là LLM với

chân và tay và bàn tay

và thân được gọi là tác nhân.

Được rồi?

Vì vậy đây là một mức độ rất cao

tổng quan về đại lý là gì

Vì vậy, từ video tiếp theo trở đi, chúng tôi

sẽ mã hóa các đại lý của chúng tôi

sử dụng Open Air LLM hoặc Gemini LLM.

Và bạn sẽ biết được điều đó

cơ thể này thực sự được tạo ra như thế nào.

Vì vậy, bạn sẽ hiểu rằng những gì

Ý tôi là qua cơ thể này, làm thế nào để xây dựng

một phần thân và gắn nó vào LLM.