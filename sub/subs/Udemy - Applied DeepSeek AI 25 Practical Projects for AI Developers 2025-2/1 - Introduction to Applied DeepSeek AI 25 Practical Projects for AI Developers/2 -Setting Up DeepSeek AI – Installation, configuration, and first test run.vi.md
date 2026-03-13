# 2 -Thiết lập DeepSeek AI – Cài đặt, cấu hình và chạy thử lần đầu.vi

---

Cài đặt Deep Secchi.

Deep Secchi là mô hình AI nguồn mở mạnh mẽ giúp thực hiện nhiều ứng dụng

Xử lý ngôn ngữ tự nhiên như tóm tắt văn bản, tạo nội dung và phát triển chatbot.

Trong công cụ video này, chúng tôi sẽ cài đặt, cấu hình

màn hình và chạy Deep Secchi trên máy cục bộ của bạn.

Trước tiên, hãy xem hệ thống yêu cầu.

Trước khi cài đặt Deep Secchi, hãy đảm bảo hệ thống của bạn đáp ứng

những yêu cầu sau đây và đây là những yêu cầu tối thiểu đối với hệ điều hành.

Bạn cần có Windows, macOS hoặc Linux.

Your size RAM

must be 8 GB or high than.

Dung lượng đĩa của bạn phải là 10 GB để lưu trữ mô hình, chủ yếu là Python phiên bản 3.8 trở lên và bạn có

Có thể cần GPU, tùy chọn này không bắt buộc trong trường hợp này vì GPU được khuyến nghị để suy luận nhanh hơn.

Tiếp theo, hãy xem cách

cài đặt Deep Secchi local.

Hiện tại, Deep Secchi có thể chạy bộ công cụ cục bộ

thiết kế để quản lý và chạy các AI mô hình theo một cách hiệu quả nhất.

Bạn có thể sử dụng công cụ này hoặc không.

Tôi sẽ chỉ cho bạn bước đầu tiên về cách cài đặt Olama và

tôi sẽ chỉ cho bạn cách cài đặt cho macOS, Linux và Windows.

Sau khi cài đặt, bạn sẽ xác định được

xem Olama đang chạy hay không.

Sau đó, bước thứ hai được tải xuống

xuống và cài đặt Deep Seek AI.

Sau đó, bước thứ ba là

chạy Deep Seek ở địa phương.

Sau đó bắt đầu ngừng.

Tôi chỉ nói cho bạn tham khảo một chút thôi, nếu bạn không có Python hoặc bạn là người mới

sử dụng Python, chúng tôi đã có một video sau video này về cách sử dụng Python một chút,

Nhưng ở đây bạn có thể truy cập vào python.org, truy cập vào phần tải xuống và tải xuống Python.

Phiên bản mới nhất là 3.3.1.

Vào điểm ghi hình này, bạn có thể cài đặt

Windows, Linux, macOS tùy thuộc vào hệ thống mà bạn đang chạy.

Tôi đang sử dụng Mac OS nên có lẽ tôi sẽ chỉ chọn Mac OS cho bạn

Nhưng tôi cũng sẽ chỉ cho bạn các bước thực hiện trên Windows.

Nhưng dù sao đi nữa, đây

là nơi bạn có thể lấy Python.

Còn đây là trang web Biển sâu, trang web này

đã trở nên phổ biến trong vài tuần gần đây.

Bạn có thể truy cập vào trang web này

và tạo trải nghiệm tài khoản cũng như vậy.

Nhưng đó không phải

là điều chúng tôi mong muốn.

Vì vậy, tôi sẽ truy cập

trực tiếp vào Olama.

Bây giờ là Olama.

Bạn có thể tải trực tiếp từ đây.

Đây là phiên bản trực tiếp mà bạn có thể nhấp vào tải xuống và bạn có thể nói Mac OS, Linux hoặc Windows

Tùy thuộc vào loại máy bạn có, bạn có thể chọn loại máy đó.

Bây giờ, nếu bạn đang chạy Linux, bạn có thể chỉ cần sao chép dòng lệnh này

vào lệnh nhắc hoặc thiết bị cuối cùng của mình và lệnh sẽ hoạt động hoàn hảo.

Lệnh này cũng hoạt động trên Mac vì

về cơ sở của nó dựa trên nền tảng Linux.

Và đối với Windows, bạn có tùy chọn

chọn tải xuống cho Windows tại đây.

Vì vậy, bạn có thể tải xuống từ đây.

Tôi sẽ vào đây và tải xuống

Phiên bản này dành cho Mac OS.

Hiện tại hệ thống đang tải xuống.

Vì vậy, tôi sẽ đến một lúc nào đó

đến khi tải xuống hệ thống.

Vì vậy, khi quá trình tải xuống

hoàn tất, tôi sẽ mở thư mục đó.

Nếu bạn thấy tệp được tải xuống

có tên là Allama Darwin unzip.

Vì vậy, ZIP.

Vì vậy, tôi sẽ giải nén tệp đó

và tệp sẽ được sử dụng ngay tại đây.

Khi tôi nhấp vào tệp đó, tệp sẽ mở ra.

Allama, tôi đã cài đặt Allama trước đây, nhưng phần mềm sẽ hỏi liệu tôi đang cố gắng

Hãy mở phần mềm đó và chuyển phần mềm đó vào ứng dụng hay không.

Vì vậy, tôi sẽ chọn chuyển đổi

phần mềm đó vào các ứng dụng.

Trên Windows.

Bạn không phải thực hiện

hiện tất cả những điều đó.

Bạn có thể trực tiếp mở Allama và

giữ nó ở bất kỳ nơi nào bạn muốn lưu.

Vì vậy, khi Allama được

open ra, tức là nó đang chạy.

Bạn có thể tiếp tục

Tôi sẽ tiến hành và thoát khỏi

thiết bị đầu cuối của mình và mở lại.

Tôi sẽ chuyển đến màn hình nền vì trên

màn hình nền của tôi, nếu bạn thấy tôi có

một thư mục tìm kiếm chi tiết nơi tôi

có thể giữ toàn bộ các dự án của mình.

Nếu tôi chuyển đến Deep Seek, tôi

Sẽ thấy thư mục này trống ngay bây giờ.

Đó là dự án thư mục ngay bây giờ.

Vì vậy, các thư mục trống và chúng

tôi chưa tạo ra bất kỳ điều gì ở đây.

Tôi có thể kiểm tra phiên bản

Allama dash dash và nó hiển thị phiên bản

bản Allama là 0,57, điều đó có

nghĩa là cài đặt tốt của tôi có chức năng.

Tôi đã chạy Allama và điều đó thật tuyệt vời.

Ngoài ra, một cách khác để kiểm tra

tra llama là bạn có thể thực hiện truy cập

truy cập trình duyệt, mở một cửa sổ

new and enter address localhost: 11434.

Đó là cổng mà Osama đang chạy.

Osama không có gì ngoài một máy chủ

local, it will run at a port cụ thể.

Hãy thử và cho tôi biết

mọi diễn đàn thứ như thế nào.

Nếu bạn gặp bất kỳ vấn đề nào khi chạy

phần này, hãy nhắn tin và tôi sẽ phản hồi bạn.

Nhưng một lần nữa, sau phần

this run and you knowned version

llama hiện lên, điều đó có ý nghĩa

là bạn đã thiết lập mọi thứ ổn thỏa.

Bước tiếp theo của chúng ta là

tải xuống và cài đặt deep Sky.

Lúc này, bạn có thể vào trang

web llama và tìm Deep Seek R1.

Này.

Và trong trường hợp tương lai

thay đổi, tôi chỉ cho bạn cách tôi tìm

ra phần này và bạn có thể tải xuống

bất kỳ phiên bản nào bạn muốn từ đây.

Một lựa chọn khác mà tôi có thể sao chép

phần này và chạy trên máy tính cục bộ của chính mình.

Tôi có thể nói hoặc nói llama Pull

sâu, tìm R1 và nó sẽ tải xuống.

Có thể mất một khoảng thời gian nhỏ

dung lượng 4,7 GB nên có thể

mất khá lâu khi bạn chạy lần đầu

lần đầu tiên nhưng lần thứ hai sẽ nhanh hơn

hơn nhiều vì nó đã được cài đặt

trước đó, vì vậy sẽ không có vấn đề gì.

Vì vậy, nó sẽ tải xuống mô hình

có dung lượng 4,7 GB tại đây.

Nó sẽ lưu trữ cục bộ và sử dụng vào những lần

chạy sau, cũng như chuẩn bị để sử dụng ngay lập tức.

Thì chúng ta có biển carbon

Chiều sâu đã có sẵn trên máy của chúng ta rồi.

Tôi phải khởi động biển sâu.

Bạn có thể thực hiện các bước chạy

theo hướng dẫn ở đây, chạy vùng biển sâu carbon.

Tôi sẽ tiếp tục và xóa trước đó.

Run olama với nghĩa là chạy biển carbon

sâu bằng cách nói sâu biển carbon.

Nó sẽ khởi động và cung cấp

cấp cho lời nhắc của tôi.

Điều này sẽ khởi động một phiên trò chuyện dựa trên CLI, tại đó bạn có

có thể tương tác với AI mô hình và không cần trực tuyến cho trường hợp này.

Bạn chỉ cần nói như: chào bạn,

hôm nay mình có thể giúp gì cho bạn?

Ý tôi là, có thể ra phải hỏi tôi, nhưng tôi

đang nhập và nó cho thấy suy nghĩ, suy nghĩ.

Xin chào, hôm nay tôi có thể giúp gì cho bạn?

Vì vậy, nó hỏi tôi, tôi có thể nói hãy viết một câu chuyện

ngắn về cuộc tìm kiếm sâu và nó sẽ tiếp tục và đồng ý.

Vì vậy, user đã yêu cầu viết.

Nó sẽ cho tôi biết suy nghĩ của nó.

Và bạn có thể thấy nó

nằm trong thẻ suy nghĩ.

Và nó đang viết một số nội dung.

Cũng tương tự như khi bạn đi đến đây để tìm

trang sâu và tôi sẽ bắt đầu ngay bây giờ.

Và ở đây, tôi viết một câu chuyện

rút gọn và đưa ra một câu chuyện ngắn.

Hãy suy nghĩ về điều đó

chính là điều nó đang nghĩ.

Và viết một câu chuyện ngắn cho tôi.

Hãy để tôi quay lại đây.

Và như bạn đã thấy, it đã nghĩ về nó và nó nói chắc chắn

chắn, đây là một câu chuyện ngắn về tìm kiếm sâu.

Và nó nói ở một khu vực sôi động của thành phố

Phố Biển và Suy nghĩ cho tôi câu chuyện đó.

Sau đó là xong.

Đó là những gì chúng ta có.

Tôi chỉ có thể nói đường chéo

và đóng cái này lại và xin chúc mừng.

Bạn đã cài đặt thành công Deep Sky

local và nó có sẵn local để bạn chạy.

Bây giờ bước tiếp theo.

Hãy cùng xem.

Chạy lệnh kiểm tra đầu tiên của bạn.

Bây giờ hãy thử Deep Sky bằng cách

gửi cho nó một bản văn bản tóm tắt yêu cầu.

Chúng tôi đã chạy và nhận thấy rằng nó đã cung cấp cho tôi

một câu chuyện, nhưng chúng ta hãy nói về bánh tóm tắt.

Đầu tiên, hãy chạy Deep Sky ở chế độ

CLI mode của bạn, mode mà bạn đã biết.

Đó là những gì chúng tôi sẽ làm.

Bước thứ hai là một mẫu lệnh.

Đó là những gì chúng tôi sẽ làm.

Vì vậy tôi sẽ thực hiện tiếp

ở đây và xóa cái này.

Sẽ một lần nữa, nếu bạn nhớ để chạy Olama, bạn chỉ cần chạy deep seek và Olama, bạn có thể

Olama chạy deep seek R1 được thấy, đó là bước đầu tiên của chúng ta, đó là chạy deep seek và CLI mode.

Bước tiếp theo của chúng tôi là tôi muốn tóm tắt văn bản

bản, vì vậy tôi sẽ nói rằng tóm tắt văn bản sau đây.

Và tôi sẽ nói trí tuệ nhân tạo đã thay đổi thế giới bằng cách tự động hóa tác nghiệp, cải tiến

thiện ra quyết định và tạo ra các khả năng mới trong chăm sóc sức khỏe, tài chính và giáo dục.

Tôi sẽ nhấn enter và nó sẽ tiếp tục.

Hãy suy nghĩ về điều đó.

Nó sẽ nói hãy nói ra.

Của những gì?

Hoặc nói với những gì tôi đã cung cấp.

Và nó sẽ thực hiện điều đó và

sum họp lại cho tôi trong vài giây.

Và bạn đã thấy đấy.

Bạn đã thấy đấy.

Nó là một bản tóm tắt.

Trí tuệ nhân tạo đã thay đổi thế giới bằng cách tự động hóa các tác vụ, cải thiện quá

trình ra quyết định, tạo ra các cơ sở mới trong chăm sóc sức khỏe, tài chính và giáo dục.

Bây giờ bạn có thể thử nhiều đoạn văn bản dài hơn này, bất cứ điều gì bạn có và cố gắng đảm bảo rằng bạn có thể tóm tắt

điều đó bằng các biển sâu.

Thế là xong rồi đó.

Chúng ta đã hoàn thành điều đó rồi.

Close time.

Bạn chỉ cần gạch ngang

bằng và tôi sẽ thoát khỏi trang.

Tiếp theo, chúng ta hãy cùng xem

cách tích hợp deep sky vào Python.

Bây giờ để sử dụng deep sky trong

Python, chúng tôi sẽ gửi yêu cầu qua API.

Đầu tiên, hãy thực hiện yêu cầu trong Python, nếu bạn đã từng xây dựng bất kỳ dự án nào trước đó

yêu cầu thư viện được sử dụng để thực hiện cuộc gọi API và như tôi đã đề cập trước đó, Deep

Seek đang chạy local trên port cụ thể này, điều đó có nghĩa là tôi có thể gửi yêu cầu tới URL này.

Vì vậy, trước đây, tôi

phải chắc chắn rằng.

Để tôi xóa phần này và yêu cầu cài đặt.

Nếu bạn không có thì nếu bạn chưa từng sử dụng

it trước đây, bạn có thể phải cài đặt nó.

Vì vậy, tôi sẽ đưa ra yêu cầu.

Nếu khả thi, nó sẽ rất nhanh.

Nó sẽ nói rằng yêu cầu đã được đáp ứng.

Nếu không, nó sẽ tải xuống cho bạn.

Tiếp theo, tôi sẽ xóa nó.

Tôi sẽ đi vào bên trong tìm kiếm sâu thư mục và bên trong và sử dụng tệp mở này bên trong đây,

Sublime Text hoặc bất kỳ ID nào bạn thích.

Click chuột phải.

Tôi sẽ tạo một tệp mới và tôi sẽ

lưu tệp này dưới dạng deep seek.py.

Đó là phần mở rộng của tệp Python.

Nếu bạn chưa biết thì đây là cách bạn làm.

Bây giờ bước tiếp theo là tôi sẽ thực hiện

thực hiện từng bước và viết một đoạn mã cụ thể.

Tôi sẽ bắt đầu bằng cách nhập thư

yêu cầu mà chúng tôi vừa cài đặt.

Yêu cầu thư viện được nhập vào đây, được phép

chúng tôi gửi HTTP yêu cầu để tương tác với API.

Nếu bạn chưa cài đặt

request thì hãy làm như sau.

Đi vào terminal và nhập yêu cầu cài đặt pip.

Tiếp theo, API URL định nghĩa lịch sử

bộ trên cổng 1143 mà chúng tôi đã tìm thấy.

Nếu bạn nhớ điều này, chúng tôi đã có

open it and it run on it port.

Vì vậy, tôi sẽ lấy URL đó.

Tôi sẽ nói URL của mình bằng http dấu gạch chéo dấu gạch chéo

localhost dấu hai chấm 11434 gạch chéo API tạo dấu gạch chéo.

Đó là nơi có sẵn API cho

chúng tôi ở dưới dạng URL llama.

URL này là nơi chứa API.

Như đã đề cập, llama đang

chạy local trên cổng 11434.

Show Olama is a allow open source code frame

bạn chạy các mô hình trên máy cục bộ của mình.

Vì vậy, chúng tôi chuyển sang bước tiếp theo là tôi sẽ tạo ra một hàm gọi là

truy vấn deep seek và truyền tải hàm đó một cách nhắc nhở dưới dạng số.

Bây giờ, hàm truy vấn deep seek này sẽ nhận được một đầu vào

văn bản, đó là lời nhắc mà chúng tôi muốn xử lý bằng mô hình AI.

Tiếp theo, chúng tôi sẽ tạo payload.

Vì vậy, payload là dữ liệu

tài liệu mà chúng tôi sẽ gửi.

Và tải trong đó có một mô hình.

Vì vậy, đây là một từ điển Python tải quan trọng ở đây

được tạo ra để lưu trữ dữ liệu sẽ được gửi đến API.

Nơi tôi đang nói mô hình là giải quyết biển sâu.

Và điều này AI mô hình chỉ định

đang được sử dụng làm hóa chất sâu.

Một lần nữa, thiệp mời là lời nhắc mà người dùng đã yêu cầu bản văn này sẽ

được xử lý theo mô hình, chúng tôi đã nhập bản văn này ở đây trước đó trong lời nhắc.

Tiếp theo, chúng tôi có luồng sai.

Điều này có nghĩa là phản hồi sẽ được trả về theo

từng lô chứ không phải theo thời gian thực hiện.

Bước tiếp theo chúng ta hãy lấy phản hồi.

Vì vậy, khi chúng tôi thực hiện yêu cầu của chúng

ta sẽ làm ở đây, Chúng ta nói yêu cầu chấm bài.

Chúng tôi đã vượt qua URL nơi chúng tôi muốn

kết thúc tải là JSON bằng tải.

Bây giờ hàm request.post một lần nữa gửi yêu cầu

post http đến một URL được tải xuống dưới dạng JSON.

Hiện tại đã phản hồi từ API

lưu trữ bên trong phản hồi này.

Vì vậy, khi tôi đưa ra yêu cầu, không chấp nhận

bất kỳ văn bản nào được tạo sẽ được lưu ở đây.

Tiếp theo hãy tiếp tục

và xử lý API hồi phục.

Vì vậy, tôi sẽ nói nếu có phản hồi

mã trạng thái dấu chấm bằng 200.

Bây giờ mã trạng thái giống như những

điều gì đã xảy ra khi tôi thực hiện một yêu cầu.

Máy chủ phản hồi như thế nào nếu nó cho tôi mã trạng thái phản hồi

Hồi 200, có nghĩa là mọi thứ đều ổn định và hoạt động như mong đợi.

Nếu là 404, nghĩa là URL này mà tôi

cung cấp đã không được tìm thấy trên máy chủ.

Nếu đó là bất kỳ lỗi nào 500,

có nghĩa là có vấn đề ở đâu đó.

Vì vậy, tôi chỉ tìm kiếm trạng thái 200.

Tôi sẽ nói câu trả lời dot JSON dot

get reply không tạo ra bất kỳ đầu ra nào.

If bằng Bằng với 200.

Nếu không tôi sẽ báo lỗi return f.

Vì vậy, tôi đang tạo một chuỗi f ở đây nói rằng

phản hồi văn bản dấu chấm dựa trên văn bản lỗi là gì.

Vì vậy, đó là lý do tại sao

tôi lại chỉ định lại phản hồi.

Mã trạng thái được kiểm tra ở đây, nơi tôi đang kiểm tra

tra xem nó phải là 200 hay không, tức là được.

Chuyển đổi phản hồi sang định dạng JSON và dấu chấm phản hồi

JSON và truy xuất giá trị của phản hồi khóa bên trong phản hồi.

Nếu không có phản hồi, nó sẽ trả về việc không tạo ra

đầu ra nào, vì điều gì sẽ xảy ra nếu nó trống rỗng từ đó.

Vì vậy, khi đó không có đầu ra

cái nào được tạo ra đang quay trở lại.

Và nếu có lỗi, văn bản dấu chấm phản hồi thông báo lỗi sẽ được trả về

và đưa ra chương trình cụ thể này hoặc bất kỳ ai gọi hàm này.

Vì vậy, hãy tiếp tục và kiểm tra hàm này.

Vì vậy, tôi sẽ tạo một loại phương thức

check tra bằng cách nói test nhắc bằng nhau.

Tóm tắt hoạt động kinh doanh của tôi được phép tự động

Tự động hóa có chiều sâu và nâng cao quyết định.

Và sau đó tôi nói trong câu hỏi.

Tôi sẽ gọi truy vấn này là hàm tìm kiếm

search deep and redirect this to function.

Bây giờ, trong trường hợp cụ thể này, chúng tôi đã tạo một

kiểm tra văn bản đầu vào uh, với một công cụ yêu cầu tóm tắt.

Bây giờ, hàm truy vấn sâu uh tìm kiếm lời nhắc

kiểm tra điều này được gọi và đầu ra được in ra.

Vì vậy, bất cứ điều gì nó trả về, cho dù là

lỗi hay phản hồi thực tế sẽ được đưa ra cho tôi.

Vậy bây giờ chúng ta

Hãy tiếp tục và lưu lại.

Đến lệnh command hoặc

thiết bị cuối cùng của tôi.

Và ở đây tôi sẽ nói cho tôi

biết chúng ta có những gì.

Chúng tôi có tệp này mà chúng tôi đã có

tạo và tôi sẽ nói với Python deep seek.py run.

Nó sẽ gọi URL đó.

Nó sẽ tiếp tục tạo văn bản

và nó sẽ lấy lại dữ liệu cho tôi.

Vì vậy, không mất một vài giây.

Và sau đó, một lần nữa, tìm sâu cần suy nghĩ về nó,

summ tắt nó và nó cung cấp cho tôi giá trị mà nó đã nghĩ đến.

Và đây là bản tóm tắt dựa trên

câu hỏi mà chúng tôi đã cung cấp.

Vậy là bạn có nó rồi.

Chúng tôi đã có thể gọi thành công

công cụ này API và lấy lại dữ liệu.

Tôi hy vọng bạn đã có thể

theo dõi và đưa ra kết quả này.

Nếu không, hãy cho tôi biết ngay bây giờ trong tin nhắn và tôi sẽ trả lời bạn về những vấn đề bạn đang gặp phải

phải.

Một lần nữa, chỉ tóm tắt lại, chúng tôi

đã cài đặt các gói cần thiết theo yêu cầu.

Tiếp theo, chúng tôi đã tạo một Python command và chúng

tôi đã chạy lệnh đó và nó đã hoạt động thành công.

Nhưng một lần nữa nếu bạn gặp sự cố khi thiết lập

bầu trời sâu thẳm, đây là một số cách giải quyết phổ biến.

Vấn đề đầu tiên có thể là lệnh không được tìm thấy, tức là bạn

phải đảm bảo Allama đã được cài đặt và bổ sung vào đường dẫn.

Nếu không, chỉ cần tiếp tục và

khởi động lại hệ thống của bạn.

Đôi khi điều đó cũng hữu ích.

Vấn đề tiếp theo mà chúng ta

sẽ thấy Allama chạy chậm.

Tìm kiếm R1 treo.

Khởi động lại thiết bị đầu cuối và thử lại.

Đây là điều thường xảy ra nhất với tôi.

Tiếp theo là deep sky Slow.

Trong trường hợp cụ thể này, bạn sẽ phải nâng cấp Ram hoặc GPU hoặc giảm

kích thước mô hình của mình vì bạn đã tìm thấy trên trang web, nếu bạn nhớ từ sâu.

Tìm kiếm.

Ở đây hay không.

Có.

Xin lỗi.

Trong này.

Bạn thấy đấy, có nhiều phiên bản khác nhau.

Bạn cũng có thể chuyển

sang phiên bản nhỏ hơn.

Sẽ như vậy.

Nó sẽ tốt, nhưng lớn hơn nhiều.

Dữ liệu được đào tạo trên hình ảnh

càng tốt thì mô hình càng nhỏ lại.

Điều này không hữu ích gì nếu bạn chỉ

đang học hoặc nhỏ hơn sẽ không ảnh hưởng.

Tiếp theo, tôi sẽ tiếp tục và nói về

kết nối bị từ chối trên API cuộc gọi.

Bây giờ khi bạn gọi API đó trong mã, chúng tôi chắc chắn rằng mã đang chạy

bằng cách chạy sâu, hãy tìm R1 theo lệnh nhắc của bạn, đảm bảo rằng nó đang chạy.

Vậy thì bây giờ điều

điều gì sẽ xảy ra tiếp theo?

Bây giờ, khi deep sky đã được thiết lập và chạy, chúng

tôi đã sẵn sàng để xây dựng các AI hỗ trợ ứng dụng.

Chương tiếp theo của chúng tôi sẽ đề cập đến văn bản Trình tóm tắt

AI được hỗ trợ phiên bản này, trình tắt này sẽ tắt các tài liệu bằng AI.

Bây giờ, nếu bạn cần bất kỳ trợ giúp nào với Python, thì có một

video mà tôi đã tải lên sẽ giúp bạn hiểu rõ hơn về Python.

Nhưng dù sao, chúng ta sẽ chuyển sang chương trình tiếp theo và sau

ở đó tôi sẽ xem từng bước cho từng mã mà tôi sẽ viết một cách chi tiết.