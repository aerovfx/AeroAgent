# 2 -Tìm hiểu Giao thức bối cảnh mô hình (MCP) là gì.en Hoa Kỳ

---

Được rồi các bạn, bây giờ

hãy hiểu

MCP cố gắng giải quyết điều gì?

Được rồi, vậy tôi muốn

chia video cụ thể này

thành hai phần.

Số một, nơi tôi cố gắng

để giải thích cho bạn vấn đề

tuyên bố rằng cái gì

là tuyên bố vấn đề

đằng sau MCP đó

đang cố gắng giải quyết.

Và sau đó chúng ta sẽ

đi sâu vào cấu trúc

định nghĩa của mô hình

giao thức ngữ cảnh

chính xác đây là gì

Được rồi, vậy chúng ta hãy

làm một việc

Chỉ cần cho tôi một chút thời gian để thực hiện

bạn hiểu đó là gì

vấn đề lớn hiện nay?

Bạn biết đấy, cái gì

một đại lý phải không?

Vì vậy, hãy nói rằng bạn có

một bộ não, bạn có một LLM

người mẫu, và bạn biết điều đó

Các mô hình LLM duy nhất và duy nhất

giỏi hoàn thành

trong việc dự đoán các token tiếp theo.

Trong thực tế, họ làm

không có gì khác ngoài

dự đoán các token tiếp theo.

Vì vậy, điều đó có nghĩa là như một.

Chỉ một LLM là không có ích gì.

Đó là nơi các nhà phát triển

giống như chúng tôi đi vào

bức tranh và họ làm

LLM này thành một đại lý.

Bây giờ, đại lý là gì?

Về cơ bản, LLM

cùng với, cùng với

tools về cơ bản là một tác nhân.

Vì vậy, về cơ bản khi bạn tạo một

LLM cho một trường hợp sử dụng cụ thể,

có thể bạn đang xây dựng một

đại lý mã hóa, có thể bạn là

xây dựng một đại lý nấu ăn, và

bạn đính kèm một số công cụ có liên quan

mang lại khả năng,

tới LLM này để thực hiện một số

nhiệm vụ.

Đây là những gì về cơ bản

được biết đến như một đại lý, phải không?

Bây giờ thông thường nếu chúng ta thấy

lớp tác nhân này bạn

biết đại lý là gì.

Bây giờ nếu chúng ta thấy điều này

lớp cụ thể, ở đó

là hai thành phần

Một là LLM,

một là công cụ.

Bây giờ thành phần này, cái này

Thành phần LLM là một cái gì đó

mà tôi nói là không đổi.

Đây là điều mà chúng tôi

không thể làm được gì nhiều phải không?

Các công ty như OpenAI,

Claude, Nhân chủng học, Song Tử,

đây là những công ty

đang làm việc ngày đêm để

xây dựng mô hình đặc biệt này

hiệu quả hơn, nhiều hơn

thông minh hơn, lớn hơn trong

kích thước bối cảnh.

Vì vậy đây là một cái gì đó mà

là một hạn chế liên tục

cho mỗi công ty.

Nếu bạn đang xây dựng

một đặc vụ AI, tôi là

xây dựng một tác nhân AI.

Cả hai chúng tôi đều đang sử dụng

GPT, giả sử là 5.1.

Không có sự khác biệt, phải không?

Chúng tôi thực sự không thể cải thiện

hiệu suất, nhưng nơi của chúng tôi

đại lý thực sự tỏa sáng là ở

công cụ, bạn sử dụng công cụ gì

cung cấp, lời nhắc của hệ thống

bạn cung cấp cho LLM của bạn là

điều gì khiến nó trở nên độc đáo

các công ty khác, từ các công ty khác

đại lý.

Vì vậy công cụ này rất

phần quan trọng phải không?

Và làm thế nào để kết hợp cả hai là

cũng là một phần rất quan trọng.

Bạn đang đi thế nào

để kết hợp công cụ này

với mô hình về cơ bản là

một phần thiết yếu phải không?

Nếu bạn đã xem hướng dẫn này

ngay từ đầu bạn đã biết điều đó

chúng tôi đã thực hiện một dự án con trỏ,

một dự án con trỏ nhỏ, phải không?

Hoặc một đại lý CLI nơi chúng tôi có

đã xây dựng một trình soạn thảo mã hóa

nơi chúng tôi có một số công cụ như,

Thực thi lệnh, phải không?

Bạn nhớ điều đó chứ?

Vậy là chúng ta đã có một công cụ như Thực thi

Command và chúng tôi đã xây dựng

một đặc vụ AI có khả năng

để thực hiện một số lệnh.

Và bạn làm một số việc

trên hệ thống của tôi.

Các bạn, hãy nói với tôi một điều thôi.

Đó có phải là một cách tiếp cận có cấu trúc?

Ý tôi là, nếu tôi nhanh chóng mở

lên mã cụ thể đó.

Vì vậy, đây là mã

trước mặt tôi.

Vì vậy nếu tôi chỉ mở nó

mã hơi nhanh.

Vì vậy, đây là mã của chúng tôi.

Và nếu tôi đi vào

lời nhắc, phải không?

Nếu tôi nhớ chính xác.

Vì vậy, nhanh chóng.

Và nếu tôi đi vào cũi.

Đây là nơi chúng tôi đã ở

đang thực hiện cuộc gọi, phải không?

Đây là nơi chúng tôi đã ở

thực hiện cuộc gọi.

Vì vậy, nếu bạn nhớ,

chúng tôi đã có một ít, bạn biết đấy,

bạn nói gì?

Chúng tôi đã có một số công cụ ở đây.

Cái đó ở đâu

lời nhắc cụ thể?

Tôi chỉ muốn.

Tôi không thể nhìn thấy điều đó.

Tôi nghĩ nó ở trong

tác nhân thời tiết.

Vâng, nó đã ở trong

tác nhân thời tiết.

Vì vậy, đây là một, phải không?

Bạn đã có lệnh chạy đó.

Bạn có công cụ đặc biệt này

và cách bạn đã cho đi,

cấp quyền truy cập vào nó.

Bạn chỉ đang cho nó, sử dụng

lời nhắc của hệ thống này phải không?

Bạn đang nói rằng bạn có

hai công cụ để sử dụng.

Và sau đó nếu tôi đi xuống, điều này

bạn đã như thế nào

phối hợp, hoặc đây là cách

bạn đang gọi công cụ này.

Bây giờ, điều này có hiệu quả phải không?

Cách tiếp cận này hoạt động.

Chúng tôi đã thấy điều đó.

Nhưng liệu đây có thực sự là

một cách tiếp cận có cấu trúc?

Không, phải không?

Đây là cách của chúng tôi để làm điều đó.

Vậy mcp về cơ bản là gì

đang cố gắng làm, nó nói

cái đó, này, tại sao không

chúng ta tiêu chuẩn hóa thứ này?

Bởi vì đây là một cái gì đó

mọi công ty sẽ sử dụng.

Bạn xây dựng công cụ của mình,

bạn có một đại lý.

Cách kết nối công cụ này

cho đại lý là

một vấn đề phổ quát, mà.

Phải.

Chúng tôi đã thực hiện nó theo một cách nào đó.

Bạn có thể đã làm nó

theo một cách nào đó khác.

Vậy điều họ đang cố gắng

việc cần làm là họ nói, này, chúng tôi

sẽ xây dựng một USB C.

Bây giờ, USB C là gì?

Mọi người đều biết phải không?

USB C, kiểu như vậy

một cáp phổ quát.

iPhone của bạn, máy tính xách tay của bạn,

MacBook của bạn, Android của bạn

thiết bị, có thể là một số

thiết bị IoT khác, Alexa của bạn,

mọi thứ đều sử dụng USB C

để tự sạc, được chứ?

Để tự tính phí.

Và mọi người đều sử dụng USB C

thậm chí thực hiện chuyển dữ liệu.

Vì thế nó giống như một điều bình thường

cáp phải không?

Nếu tôi muốn kết nối

điện thoại của tôi với máy tính xách tay,

Tôi có thể sử dụng USB C.

Nếu tôi muốn tính phí

cùng một chiếc điện thoại, tôi có thể

sử dụng cùng một USB C.

Vậy về cơ bản chúng là gì

đang cố gắng xây dựng họ

xây dựng một USB C nơi bạn

mang dụng cụ của bạn và tiêm

và, bạn biết đấy, kết nối với

LLM của bạn sử dụng như USB C

giao diện.

Bây giờ những gì có thể xảy ra là hãy xem

Google với tư cách là một công ty có thể xây dựng

có thể là 40 đến 50 công cụ phải không?

Rất nhiều công cụ họ có thể xây dựng.

Vì vậy, họ có thể xây dựng các công cụ như

bạn biết đấy, đọc email.

Vì vậy họ đã xây dựng một công cụ

như đọc email,

gửi email vì bạn biết đấy,

Gmail, Google có Gmail.

Họ có những công cụ thích hợp, phải không?

Họ có thể, họ có

thứ Gmail này.

Có thể ví dụ như Twitter.

Được rồi, hãy lấy một ví dụ

của Twitter, mà

Nhân tiện, bây giờ là X.

Vì vậy, về cơ bản họ có thể xây dựng

công cụ, thứ gì đó giống như bạn

biết đấy, đăng tweet, được thôi, họ

có thể thích đăng lại

tweet và họ có thể có các công cụ.

Về cơ bản họ có thể làm những điều này

các công ty chỉ

công cụ xây dựng, phải không?

Họ có thể xây dựng một công cụ

ví dụ có thể

trả lời một tweet.

Vì vậy bạn có thể thấy tất cả những thứ lớn lao này

các công ty có thể đi và chỉ

tiếp tục xây dựng những công cụ này

như một lớp MCP, được chứ?

Trên cơ sở giao thức MCP.

Bây giờ LLM của tôi có thể làm gì, hãy cùng

nói rằng tôi có một đại lý LLM

sử dụng đó có thể là OpenAI

GPT3, giả sử là GPT 4.1.

Vì vậy điều tôi có thể làm là tôi chỉ có thể

nói điều đó đi anh bạn, sử dụng MCP

xin vui lòng mô hình giao thức ngữ cảnh

vui lòng kết nối với những công cụ này

kết nối với các công cụ này.

Và thế là xong.

Sử dụng mcp, một điều phổ biến

giao diện kết nối

những loại công cụ này,

Tôi có thể tận dụng các công cụ được tạo sẵn

để kết nối với mô hình của tôi

một cách chuẩn hóa.

Từ tiêu chuẩn hóa

là rất quan trọng.

Được rồi, tương tự hãy nói một

của bạn bạn cũng vậy

sử dụng một số mô hình khác.

Có lẽ anh ấy đang lợi dụng Gemini.

Được rồi, hãy lấy

một ví dụ về Song Tử.

Bây giờ anh ấy đang sử dụng Gemini 2.5

Người mẫu chuyên nghiệp.

Bây giờ điều anh ấy có thể làm là bởi vì,

bởi vì đó là một MCP, anh ấy

cũng có thể kết nối các công cụ này.

Anh ấy cũng có thể đi trước

và kết nối những công cụ này

bởi vì một lần nữa USB C là phổ biến.

Cho dù bạn đang ở trên Apple

hệ sinh thái, bạn đang sử dụng Android

hệ sinh thái, bạn đang ở trên Samsung

hệ sinh thái, USB C cũng vậy.

Vậy đây là cách MCP hoạt động

và đây chính xác là vấn đề

mà MCP đang cố gắng giải quyết.

Về cơ bản nó chỉ là

như API REST, phải không?

Bạn có API REST.

Những công ty lớn này phơi bày

điểm cuối API của họ, phải không?

Họ tiết lộ API của họ,

họ tiết lộ API của họ.

Và sử dụng API REST,

điều đó có nghĩa là làm cho có được

yêu cầu, đăng yêu cầu,

những yêu cầu kiểu này.

Về cơ bản chúng ta có thể truy cập

API và thực hiện một số nội dung.

Vì vậy, về cơ bản nó giống như

API REST, giống như

một giao thức nhưng dành cho AI.

Vậy đó là mcp của bạn.

Vậy ra đây chỉ là phần giới thiệu

hoặc một tuyên bố vấn đề của mcp.

Trong video cụ thể tiếp theo,

chúng ta hãy nhìn vào MCP

từ tiêu chuẩn

quan điểm tài liệu.