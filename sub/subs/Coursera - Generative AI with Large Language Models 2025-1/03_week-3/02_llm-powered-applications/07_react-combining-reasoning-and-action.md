# 07 phản ứng-kết hợp-lý luận và hành động

---

Trong video trước, bạn đã thấy cách

lời nhắc có cấu trúc có thể được sử dụng để

giúp LLM viết tập lệnh Python

để giải các bài toán phức tạp.

Một ứng dụng sử dụng PAL

có thể liên kết LLM với Python

trình thông dịch để chạy mã và

trả lại câu trả lời cho LLM.

Hầu hết các ứng dụng sẽ yêu cầu LLM để

quản lý quy trình công việc phức tạp hơn, có lẽ

bao gồm các tương tác với nhiều

nguồn dữ liệu bên ngoài và các ứng dụng.

Trong video này, bạn sẽ khám phá

một khung gọi là ReAct có thể

giúp LLM lập kế hoạch và

thực hiện các quy trình công việc này.

ReAct là một chiến lược thúc đẩy

kết hợp chuỗi suy nghĩ suy luận

với việc lập kế hoạch hành động.

Khung được đề xuất bởi các nhà nghiên cứu

tại Princeton và Google vào năm 2022.

Bài viết phát triển một loạt

ví dụ nhắc nhở phức tạp dựa trên

vấn đề từ QA Lẩu,

một tiêu chuẩn trả lời câu hỏi nhiều bước.

Điều đó đòi hỏi phải suy luận về hai hoặc

nhiều đoạn Wikipedia hơn và

cơn sốt, một điểm chuẩn sử dụng

Đoạn Wikipedia để xác minh sự thật.

Hình bên phải cho thấy một số ví dụ

gợi ý từ bài báo và chúng ta sẽ khám phá

một lát nữa thôi, vì vậy đừng lo lắng về việc đọc

các lời nhắc trên slide này bây giờ.

Bạn sẽ có thể nhìn vào hình

chi tiết hơn trong bài tập đọc

sau video.

ReAct sử dụng các ví dụ có cấu trúc để hiển thị

một mô hình ngôn ngữ lớn làm thế nào để suy luận

thông qua một vấn đề và quyết định hành động để

hãy đưa nó đến gần hơn với một giải pháp.

Lời nhắc ví dụ bắt đầu bằng một câu hỏi

điều đó sẽ yêu cầu nhiều bước để

câu trả lời.

Trong ví dụ này, mục tiêu là xác định

tạp chí nào trong hai tạp chí được tạo ra đầu tiên.

Ví dụ sau đó bao gồm

một hành động suy nghĩ liên quan

quan sát ba dây.

Suy nghĩ là một bước suy luận

chứng minh cho người mẫu biết cách

giải quyết vấn đề và

xác định một hành động cần thực hiện.

Trong ví dụ xuất bản báo,

lời nhắc chỉ rõ rằng mô hình

sẽ tìm kiếm cả tạp chí và

xác định cái nào được xuất bản đầu tiên.

Để mô hình có thể tương tác với

một ứng dụng bên ngoài hoặc nguồn dữ liệu,

nó phải xác định một hành động để

lấy từ một danh sách được xác định trước.

Trong trường hợp khung ReAct,

các tác giả đã tạo một API Python nhỏ

để tương tác với Wikipedia.

Ba hành động được phép là tìm kiếm,

tìm kiếm một mục Wikipedia về

tra cứu chủ đề cụ thể, tìm kiếm

cho một chuỗi trên trang Wikipedia.

Và kết thúc,

mà mô hình thực hiện khi nó

quyết định nó đã xác định được câu trả lời.

Như bạn đã thấy ở slide trước,

ý nghĩ trong lời nhắc được xác định

hai tìm kiếm để thực hiện một cho

từng tạp chí.

Trong ví dụ này, tìm kiếm đầu tiên

sẽ dành cho tạp chí của Arthur.

Hành động được định dạng bằng cách sử dụng cụ thể

ký hiệu dấu ngoặc vuông bạn thấy ở đây,

để mô hình sẽ định dạng

sự hoàn thành của nó theo cách tương tự.

Trình thông dịch Python tìm kiếm

mã này để kích hoạt các hành động API cụ thể.

Phần cuối cùng của lời nhắc

mẫu là sự quan sát,

đây là nơi có thông tin mới

được cung cấp bởi tìm kiếm bên ngoài là

đưa vào bối cảnh của lời nhắc.

Để mô hình diễn giải lời nhắc

sau đó lặp lại chu kỳ nhiều lần

những lúc cần thiết để

có được câu trả lời cuối cùng.

Trong ý nghĩ thứ hai, lời nhắc nêu rõ

năm đầu tiên của tạp chí Arthur và

xác định bước tiếp theo

cần thiết để giải quyết vấn đề.

Hành động thứ hai là tìm kiếm đầu tiên

dành cho phụ nữ, và quan sát thứ hai

bao gồm văn bản cho biết ngày bắt đầu

của ấn phẩm, trong trường hợp này là năm 1989.

Lúc này, mọi thông tin

cần thiết để trả lời câu hỏi đã biết.

Ý nghĩ thứ ba nói lên sự bắt đầu

năm đầu tiên dành cho phụ nữ và sau đó cho

logic rõ ràng được sử dụng để xác định

tạp chí nào được xuất bản đầu tiên.

Hành động cuối cùng là kết thúc chu kỳ

và gửi lại câu trả lời cho người dùng.

Điều quan trọng cần lưu ý là

trong khuôn khổ ReAct,

LLM chỉ có thể chọn từ một số giới hạn

số hành động được xác định bởi

một bộ hướng dẫn đó là

được đặt trước văn bản nhắc ví dụ.

Toàn văn của

các hướng dẫn được hiển thị ở đây.

Đầu tiên, nhiệm vụ được xác định,

yêu cầu người mẫu trả lời

một câu hỏi sử dụng cấu trúc gợi ý

bạn vừa khám phá chi tiết.

Tiếp theo, hướng dẫn chi tiết hơn

về ý nghĩa của suy nghĩ và

sau đó chỉ định rằng bước hành động

chỉ có thể là một trong ba loại.

Đầu tiên là hành động tìm kiếm,

tìm kiếm

Các mục Wikipedia liên quan

tới thực thể được chỉ định.

Thứ hai là hành động tra cứu,

lấy câu tiếp theo

có chứa từ khóa được chỉ định.

Hành động cuối cùng là kết thúc, trả về

câu trả lời và kết thúc nhiệm vụ.

Điều quan trọng là phải xác định một tập hợp

các hành động được phép khi sử dụng LLM để lập kế hoạch

các nhiệm vụ sẽ cung cấp năng lượng cho các ứng dụng.

LLM rất sáng tạo và

họ có thể đề xuất thực hiện các bước không

thực sự tương ứng với một cái gì đó

mà ứng dụng có thể làm được.

Câu cuối cùng trong hướng dẫn

cho LLM biết rằng một số

ví dụ sẽ đến tiếp theo

trong văn bản nhắc nhở.

Được rồi, vậy hãy đặt tất cả các mảnh

cùng nhau để suy luận.

Bạn sẽ bắt đầu với

lời nhắc ví dụ ReAct.

Lưu ý rằng tùy thuộc vào LLM bạn

làm việc cùng, bạn có thể thấy rằng bạn

cần bao gồm nhiều hơn một ví dụ và

thực hiện suy luận trong tương lai.

Tiếp theo, bạn sẽ gửi trước hướng dẫn

ở đầu ví dụ và

sau đó chèn câu hỏi bạn

muốn trả lời ở cuối.

Lời nhắc đầy đủ bây giờ bao gồm tất cả

của những phần riêng lẻ này, và

nó có thể được chuyển đến LLM để suy luận.

Khung ReAct cho thấy

một cách để sử dụng LLM

để cấp nguồn cho một ứng dụng thông qua

lý luận và lập kế hoạch hành động.

Chiến lược này có thể được mở rộng cho

trường hợp sử dụng cụ thể bằng cách tạo ví dụ

hoạt động thông qua các quyết định và

hành động sẽ thực hiện

đặt trong ứng dụng của bạn.

May mắn thay, khuôn khổ cho

phát triển các ứng dụng được cung cấp bởi

mô hình ngôn ngữ đang được phát triển tích cực.

Một giải pháp đang được áp dụng rộng rãi

được thông qua có tên là LangChain,

khung LangChain cung cấp cho bạn

với các phần mô-đun có chứa

các thành phần cần thiết

làm việc với LLM.

Các thành phần này bao gồm các mẫu nhắc nhở

cho nhiều trường hợp sử dụng khác nhau

bạn có thể sử dụng để định dạng cả đầu vào

ví dụ và hoàn thành mô hình.

Và bộ nhớ mà bạn có thể sử dụng để

lưu trữ các tương tác với LLM.

Khung này cũng bao gồm các bản dựng sẵn

công cụ cho phép bạn thực hiện

nhiều nhiệm vụ khác nhau, bao gồm cả các cuộc gọi

đến các bộ dữ liệu bên ngoài và các API khác nhau.

Kết nối sự lựa chọn của những cá nhân này

các thành phần với nhau tạo thành một chuỗi.

Những người tạo ra LangChain đã phát triển

một tập hợp các chuỗi được xác định trước

đã được tối ưu hóa cho

trường hợp sử dụng khác nhau,

và bạn có thể sử dụng những thứ này để

nhanh chóng thiết lập và chạy ứng dụng của bạn.

Đôi khi quy trình làm việc ứng dụng của bạn

có thể đi nhiều đường tùy theo

trên thông tin người dùng cung cấp.

Trong trường hợp này,

bạn không thể sử dụng chuỗi được xác định trước, nhưng

thay vào đó chúng ta sẽ cần sự linh hoạt

để quyết định những hành động cần thực hiện

người dùng di chuyển qua quy trình làm việc.

LangChain định nghĩa một cấu trúc khác,

được biết đến như một đại lý,

mà bạn có thể sử dụng để giải thích

đầu vào từ người dùng và

xác định công cụ nào hoặc

công cụ sử dụng để hoàn thành nhiệm vụ.

LangChain hiện bao gồm các đại lý cho

cả PAL và ReAct, trong số những thứ khác.

Các đại lý có thể được kết hợp vào

chuỗi để thực hiện một hành động hoặc kế hoạch và

thực hiện một loạt hành động.

LangChain đang được phát triển tích cực và

các tính năng mới liên tục được bổ sung,

như khả năng kiểm tra và

đánh giá sự hoàn thành của LLM

trong suốt quá trình làm việc.

Đó là một khuôn khổ thú vị có thể

giúp bạn tạo mẫu nhanh và

triển khai và

có khả năng trở thành một công cụ quan trọng trong

hộp công cụ AI tổng quát của bạn trong tương lai.

Điều cuối cùng cần ghi nhớ khi bạn

phát triển ứng dụng bằng LLM là

khả năng suy luận tốt của người mẫu

và lập kế hoạch hành động phụ thuộc vào quy mô của nó.

Các mô hình lớn hơn thường

sự lựa chọn tốt nhất của bạn cho

các kỹ thuật sử dụng lời nhắc nâng cao,

như PAL hoặc ReAct.

Các mô hình nhỏ hơn có thể gặp khó khăn để hiểu

các nhiệm vụ trong lời nhắc có cấu trúc cao và

có thể yêu cầu bạn thực hiện thêm

tinh chỉnh để cải thiện khả năng của họ

để suy luận và lập kế hoạch.

Điều này có thể làm chậm lại

quá trình phát triển của bạn.

Thay vào đó, nếu bạn bắt đầu với một số lượng lớn,

mô hình có khả năng và

thu thập nhiều dữ liệu người dùng khi triển khai,

bạn có thể sử dụng nó để đào tạo và

tinh chỉnh một mô hình nhỏ hơn mà bạn

có thể chuyển sang sau.