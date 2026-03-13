# 1 -Công cụ tóm tắt văn bản được hỗ trợ bởi AI của Project 1 với DeepSeek AI.vi

---

Việc tóm tắt các văn bản dài là một nhiệm vụ

quan trọng trong Xử lý ngôn ngữ tự nhiên (NLP).

Trong video này, chúng tôi sẽ xây dựng một dự án trong đó có trình bày văn bản tóm tắt

AI sử dụng deep sky để tạo ra các bản tóm tắt ngắn gọn về bất kỳ văn bản đầu vào nào.

Các trường hợp sử dụng của bản tóm tắt văn bản do AI hỗ trợ bao gồm cả bản tóm tắt

tức, trong đó chúng tôi có thể nhanh chóng trích xuất các điểm chính từ nhiều bài báo.

pháp lý tài liệu.

Bản tóm tắt làm giảm sự hợp nhất

long long của các điều khoản cần thiết.

Tóm tắt báo cáo y tế nơi chúng tôi có thể trích xuất thông tin quan trọng từ các báo cáo y tế, báo cáo

kinh doanh và các bài báo nghiên cứu nơi chúng tôi có thể tạo ra các bản tóm tắt cho giám đốc điều hành.

Tóm tắt nội dung nơi chúng tôi có

có thể xử lý các bài viết và blog dài.

Vì vậy, nếu bạn thấy có rất nhiều trường hợp

use for they thì bây giờ như thế nào?

Tóm tắt văn bản thực thi hoạt động.

Có hai loại chính của

kỹ thuật tóm tắt văn bản.

Đầu tiên được gọi là summ Tắt Trích xuất chủ động, đây là

loại đơn vị lựa chọn các câu quan trọng nhất trực tiếp từ văn bản.

Và sau đó, chúng ta có tóm tắt Trừu tượng, đây là loại tạo

ra summilla mới tắt bằng cách sử dụng công nghệ tạo ngôn ngữ AI.

Hiện tại, AI sử dụng tóm tắt trích yếu

ứng dụng công nghệ tiếp theo, có nghĩa là tạo ra

bản tóm tắt rút gọn giống với người, không

đơn thuần là trích xuất những câu chủ yếu.

Chúng ta hãy cùng nhau

thiết lập trình đơn tắt AI.

Đầu tiên, hãy cài đặt

các thuộc tính của các thành phần phụ.

Chúng ta sẽ cài đặt yêu cầu

và Gradio nếu bạn chưa cài đặt.

Tiếp theo, chúng ta

will create Python command.

Chúng ta sẽ gọi tập lệnh đó là text summaryr.py

sau đó thêm một số mã vào đó và chạy.

Đó là bước ba, chạy lệnh và xem

tập lệnh có hoạt động hoàn hảo.

Hãy tiếp tục.

Bạn thấy đấy, tôi đã tạo một thư

mục dự án ở đây không có gì cả.

Tôi cũng đã mở project one in

IDE của tôi ở đây và tôi chắc chắn rằng

tôi đang ở thư mục dự án một, thư

Hiện tại mục này không có nội dung gì.

Vậy là tôi đang ở thư mục project

one ở đây và đây là dự án một của tôi.

Và như tôi đã đề cập, tôi

will create a new file here.

Tôi sẽ gọi tệp này là

text_summarizer.py.

Đó là tệp Python của tôi.

Tôi sẽ thêm một số mã vào đây.

Nhưng trước khi làm điều đó, hãy tiến hành và thực hiện

bước một của chúng tôi là yêu cầu cài đặt pip và gradio.

Vì vậy, lệnh này sẽ tiếp tục và nhanh chóng

cài đặt hai thư viện của tôi.

Một thư viện dành riêng cho yêu cầu.

Lời yêu cầu.

Như đã đề cập trước đó, request is one

thư viện để thực hiện HTTP yêu cầu.

Ví dụ gọi API, tải xuống các trang web.

Trong trường hợp cụ thể này, chúng tôi sẽ gọi API đến nơi

seq sâu của chúng tôi đang chạy hoặc Obama đang chạy.

Đó là lý do tại sao chúng ta cần điều đó.

Tiếp theo, Gradio là một thư viện để xây dựng các giao dịch

giao diện web dễ sử dụng cho các mô hình và ứng dụng máy học.

Và ứng dụng, và đó là lý do

tại sao chúng tôi có ứng dụng đó.

Và chúng tôi sẽ tạo một giao diện web.

Cho dự án này.

Bước tiếp theo của chúng tôi là Continue

và viết lệnh Python của mình tại đây.

Vì vậy, tôi sẽ tiếp tục và viết mã ở đây.

Chúng tôi sẽ bắt đầu bằng cách nhập các

thư viện bắt buộc mà chúng tôi vừa cài đặt.

Một yêu cầu đầu tiên.

Yêu cầu tiếp theo sẽ import Gradio là GR.

Vì vậy, request như tôi đã đề xuất được sử dụng

để gửi yêu cầu HTTP để giao tiếp với API deep sky.

Tiếp theo, Gradio của chúng tôi được sử dụng để tạo một giao diện người dùng dựa trên web cho chức năng tóm tắt và bạn sẽ làm như vậy

đã thấy sớm.

Vì thế tiếp theo được định nghĩa

API cuối cùng định nghĩa.

Vì thế tôi sẽ tạo API cuối cùng

Deep sea đang chạy trên Lama.

Vì thế url lama http localhost trên

cổng 11 434 tạo chéo API.

Bây giờ nếu bạn chưa xem video trước và trực tiếp chuyển đến

đây, tôi khuyên bạn nên xem trước để biết cách chúng tôi tạo ra điều này.

Vì thế một lần nữa đây là URL lưu trữ API cuối cùng mà ở đó hình ảnh AI

chuyên sâu chạy cục bộ và API lắng nghe trên cổng 11434, mặc định cho olama.

Bước tiếp theo của chúng tôi

được xác định cụ thể là chức năng tắt của summ.

Vì thế tôi sẽ tạo ra một chức năng

năng summ tắt như trước.

Chúng ta sẽ nói tóm tắt văn bản và nó

will use the text panel doing reference để tắt.

Chức năng sẽ gửi bản văn này đến seq

ai API và trả về bản tóm tắt do AI tạo ra.

Vì thế tôi sẽ nói tại đây.

Use this key for summ

vô hiệu hóa một bản văn bản tối đa.

Giống như một bình luận cho tôi biết chức năng

khả năng này thực hiện những gì trong tương lai.

Tiếp theo, tôi sẽ chuẩn bị API yêu cầu tải trọng cho tải trọng tôi sẽ sử dụng là mô

hình sâu seq R1.

Điều này được định nghĩa chỉ sử dụng bất kỳ AI mô hình nào trong

trường hợp của chúng tôi là Deep Sea Car one.

Nếu bạn muốn thay đổi nó thành một mô hình khác

Được hỗ trợ bởi Olama, bạn cũng có thể chạy mô hình đó.

Tiếp theo là câu lệnh tôi đang nói summar

tắt văn bản sau và tôi truyền tải văn bản tại đây.

Mũi.

Loại này.

Câu lệnh hướng dẫn cụ thể theo trình tự sâu mà tôi nên

làm theo, trong trường hợp chúng tôi là một món tóm tắt.

Tiếp theo, tôi sẽ phát trực tiếp bằng false.

Bây giờ điều này sẽ chọn API trả về toàn bộ bộ hồi phục

một lần thay vì phát trực tiếp phản hồi theo từng phần.

Vì vậy, đó là những gì nó làm.

Nếu bạn phát trực tuyến bằng true thì nó sẽ

cung cấp cho bạn dưới dạng từng phần.

Close không phải là điều chúng ta muốn.

Vì vậy, chúng tôi đang

Stream setting is false.

Bước tiếp theo là hãy tiếp tục

và thực hiện yêu cầu API đó.

Vì vậy, tôi sẽ nói yêu cầu dot post để gửi yêu cầu đăng http

đến URL của tôi với payload là payload ở dưới dạng JSON.

Tại đây, API xử lý dữ liệu nhập và cài đặt phản hồi

Cũng như chỉ định nó cho phản hồi của biến phản hồi này.

Bước tiếp theo là quá trình xử lý phản hồi của API.

Một lần nữa, chúng ta sẽ

check xem có ổn không 200.

Close main là yêu cầu trạng thái mã hóa.

Trích xuất câu trả lời trích xuất

và trả về bản tóm tắt do AI tạo ra.

Vì vậy, đối với lệnh đó, tôi sẽ trả

đã nhận được JSON phản hồi lại.

Nếu có phản hồi.

Trong phản hồi đó, tôi sẽ nhận được phản hồi nằm trong khóa hoặc của tôi

Sẽ không nói bản tóm tắt nào được tạo nếu không có kết quả gì được trả về.

Vì vậy, đây là văn bản mặc định.

Nếu không có phản hồi, không

có gì được trả lại trong phản hồi.

Tiếp theo, tôi sẽ nói rằng nếu có

error thì return text dedecated failed.

Vì vậy, lệnh này sẽ trả lại thông tin

báo lỗi cho bất kỳ ai gọi hàm này.

Bây giờ, chúng ta hãy thực hiện một trường thử nghiệm hợp lệ

trải nghiệm tại đây, tôi sẽ nói bài kiểm tra tóm tắt.

If name __ name by __main, tôi sẽ nói văn bản mẫu là trống, ý tôi là

đoạn văn bản ở trên đảm bảo rằng lệnh chạy chỉ hợp các trường

thử nghiệm xem có thể chạy trực tiếp hay không chứ không phải khi được nhập vào mô-đun.

Vì vậy, đây là lý do tại sao

điều này rất quan trọng ở đây.

Vì vậy tôi sẽ tiếp tục và nói ví dụ về văn bản

bản tôi sẽ nhập một số văn bản tại đây.

Trí tuệ nhân tạo đang chuyển đổi

ngành công nghiệp trên toàn thế giới.

Các mô hình AI as deep

seq là một số trong đó.

Cho phép doanh nghiệp tự động hóa nhiệm vụ,

phân tích các dữ liệu lớn và tăng hiệu suất.

Với những tiến trình trong AI,

bao gồm tất cả các ứng dụng

hỗ trợ ảo cho dự án phân tích

mong đợi và xuất ra cá nhân hóa

Và tôi sẽ đóng văn bản ví dụ này ở đây.

Điều này chứa một đoạn

văn bản về AI sẽ bị tắt.

Tiếp theo hãy tiếp tục và

gọi hàm summarizing và in start.

Về điều đó, trước đây tôi sẽ nói

in summ tắt văn bản và tôi sẽ nói trong.

Tôi sẽ gọi hàm tắt văn bản

và truyền tải mẫu văn bản cho nó.

Và nó sẽ trả lại dữ liệu cho tôi.

Vì vậy, tôi sẽ lưu dự án này ở đây.

Quay trở lại đây.

Xóa nó.

Và nếu bạn thấy bây giờ

giờ tôi tắt văn bản.

Vì vậy, tôi sẽ nói văn bản Python

dấu gạch dưới tóm tắt dấu chấm p y.

Tôi sẽ chạy nó.

Nó sẽ thực hiện dự án và cung cấp cho

tôi viết văn bản tóm tắt bằng cách gọi URL đó.

Lúc này chúng tôi sẽ tiếp tục tiếp tục với gradio IO, chúng

ta sẽ sử dụng nó trong phần tiếp theo trong chốc lát nữa.

Nhưng trong khi nó thực hiện như

vậy, hoặc bạn làm như hướng dẫn.

Nó cung cấp cho tôi dữ liệu duy nhất để xem xét

bản tóm tắt về những gì mà tập lệnh thực hiện.

Nó đang kết nối với deep sea

trên localhost 1143 thông tin yêu cầu.

Nó có định dạng văn bản thành

nhắc nhở tóm tắt rồi gửi đến API.

Nó lấy ra một tập hợp tắt được AI tạo ra,

trả về và kết quả ngay tại đây.

Khi tập lệnh được chạy.

Vì vậy, một lần nữa, điều này xác nhận rằng mọi thứ đang hoạt động tốt nếu

tôi quay lại đây, nếu bạn thấy bản tóm tắt hiển thị ngay tại đây, nó cũng sẽ như vậy

show cho tôi suy nghĩ khi đang summ tắt dựa trên văn bản mà tôi cung cấp.

Và chúng tôi đã tắt ngay tại đây.

Bước tiếp theo là xây dựng một

ứng dụng web cho Summarizer.

Hiện tại chúng tôi đã có Gradio,

tại sao không sử dụng nó?

Giờ đây chúng ta hãy xây dựng một ứng dụng web đơn giản bằng cách sử dụng Gradio để

người dùng có thể tương tác với Summarizer qua giao diện web thay vì lệnh nhắc.

Ví dụ như, nếu tôi đưa ứng dụng này cho mẹ tôi, bà sẽ không hiểu mình phải làm gì nên tại sao không cung cấp

cấp cho bà một giao diện web cho ứng dụng đó?

Đầu tiên tôi sẽ tiến hành và tạo một giao dịch

giao diện Gradio, sau đó tôi sẽ chạy ứng dụng web.

Vì vậy, để thay đổi điều đó, tôi phải thực hiện

trong dự án hiện tại, tôi sẽ chuyển đến đây.

Tôi sẽ xóa phần văn bản tóm tắt ở dưới đây.

Hoặc tôi sẽ tiến hành bình luận thảo luận về nó.

Tiếp theo, ở đây, tôi sẽ bổ sung thêm một

mã số trước đó để tạo Gradio giao diện.

Tôi sẽ tiến hành và nói giao tiếp

giao diện bằng chào mừng giao diện.

Đây là cách bạn tạo nó.

Và giao diện này cần một

một loạt các mục khác nhau.

Web giao diện cần có nhiều tham số khác nhau.

Đầu tiên là FN tương thích.

Tóm tắt văn bản với chức năng công cụ này có thể là tóm tắt các đầu vào văn bản mà tôi sẽ cung cấp là tôi cần

hộp văn bản GR văn bản dòng bằng mười và ký hiệu đóng thế trên đó phải là văn bản nhập để tắt.

Đầu ra tiếp theo

đương nhiên với GR hộp văn bản.

Một văn bản hộp thư khác ở bên phải để hiển thị

cho tôi đầu ra của bản tóm tắt văn bản.

Tiếp theo tôi sẽ nói tiêu đề bằng mô

Trình bày văn bản tóm tắt được hỗ trợ AI.

Tôi sẽ nhập văn bản dài và biển sâu.

Tôi sẽ tạo một đoạn tóm tắt ngắn gọn.

Tôi sẽ đóng cái này và sẽ

tạo giao diện của chúng ta.

Chỉ thế thôi.

Vì vậy, hãy tiếp tục và khởi chạy ứng dụng web bằng cách nói nếu tên

dấu gạch dưới dấu gạch dưới dấu gạch nối chính dưới dấu gạch chéo.

Tôi khởi động nó bằng cách

nói về khởi động giao diện.

Tôi sẽ lưu nó.

Và bây giờ chúng ta hãy

continue and run cái này.

Tôi sẽ xóa cái này.

Tôi chạy lại.

Trình tóm tắt văn bản Python sẽ tắt

run on a web tool name name.

Chào bạn ạ.

Nó đã chọn URL của tôi ở đây.

Đây là nơi nó đang chạy.

Mở trình duyệt của tôi và mở URL này.

Và nếu bạn thấy tôi có đầu

to and print this text.

Bây giờ nếu tôi làm việc đó

lớn hơn nó sẽ quay lại các cạnh nhau.

Nó cũng thân thiện với

thiết bị di động một chút.

Nó không giúp được gì.

Và nếu bạn thấy rằng đây là đầu vào của chúng tôi khi bạn tìm thấy hộp văn bản

đầu vào dòng này bằng mười và tôi xuất ra đầu ra có sẵn ngay tại đây.

Bây giờ tôi có thể lấy cùng một văn bản

bản mà tôi có ở đây và thêm nó vào đây.

Hãy đảm bảo không có ghi chú thứ hai.

Cùng xem nào.

Vì vậy, tôi đã thêm bản văn của

mình tại đây và tôi sẽ ấn vào gữi.

Nó sẽ gọi API đó và

đưa lại dữ liệu cho tôi.

Kết quả của văn bản tóm tắt

bản sẽ hiển thị tại đây.

Vì vậy, bất kỳ điều gì chúng tôi đã làm trong lệnh nhắc nhở ở

ở đây trước đó, thì chúng ta đều sẽ làm thông tin qua giao diện web này.

Bây giờ, nếu tôi đưa cái này cho

mẹ tôi, có lẽ bà ấy sẽ hiểu được.

Ồ, đây là bản văn được hỗ trợ bởi AI.

Công cụ tóm tắt cần nhập một đoạn văn bản dài vào đây và khi tôi gửi đi, tôi sẽ

đã nhận lại được dữ liệu hoặc bản tóm tắt văn bản ngay tại đây, mặc dù bà không hiểu nó.

Nhưng một lần nữa, điều này cung cấp cho bạn một ý tưởng về cách chúng ta có thể tạo giao diện

web một cách nhanh chóng chỉ với một vài mã dòng, chẳng hạn như mã sáu dòng, chúng ta có thể tạo ra nó.

Tạo một giao diện web ngay tại đây.

Bước tiếp theo là nâng cao công cụ Tóm tắt.

Có rất nhiều công việc mà chúng tôi có thể làm.

Đầu tiên, chúng ta có thể

điều chỉnh bản tóm tắt dài.

Vì vậy, nếu bạn còn nhớ ở đây chúng tôi đã làm

gì vậy, chúng ta nói tóm tắt văn bản sau đây.

Bây giờ thay vì tóm tắt đoạn văn bản sau, những gì tôi có thể làm là tôi có thể thay đổi điều này thành được phép

tôi chỉ xóa điều này và nói là đoạn văn bản tóm tắt sau trong một câu.

Vì vậy, tôi chỉ nhận được một câu.

Một điều khác mà bạn có thể làm là nếu bạn muốn có một chi

chi tiết, ừm, chẳng hạn như các dòng đầu dòng và tất cả những thứ đó.

Tôi có thể thay đổi điều này.

Và thay vì nói một câu, tôi có thể nói tóm tắt

đoạn văn bản sau trong dòng đầu dòng.

Vì vậy, đó là một điều khác mà tôi có thể làm.

Bạn cũng có thể thực hiện

hiện tắt nhiều tài liệu.

Bạn có thể đọc các tệp và thêm các tệp đó.

Tóm tắt nhiều tài liệu những gì bạn có thể làm là bạn có thể đồng ý, tôi nghĩ mình đã làm ở đây,

Những gì bạn có thể làm là hãy nói rằng tôi có một dấu gạch nối dưới đây hợp nhất văn bản bằng doc một cộng.

Vì vậy, tôi có một tài liệu và tôi muốn có dữ liệu

data from a other document, gạch ngang và dấu n.

Và ở đây tôi sẽ nói cộng với tài liệu hai.

Vì vậy, tôi cung cấp các tài liệu

this data làm tham số đầu vào.

Và sau đó, tôi đưa ra và tôi gọi là tóm tắt văn bản dựa trên

Đây là bản kết hợp văn bản mà tôi dựa trên các tài liệu khác nhau.

Một điều khác mà tôi có thể làm

được cải thiện kỹ thuật tạo lời nhắc.

Có những phong cách khác

nhau để cải thiện bản tóm tắt.

Nếu bạn biết về kỹ thuật tạo nhanh thì có thể

chia làm 2 phong cách: thường ngày và kỹ thuật.

Nếu tôi muốn tạo một

phong cách ngày thường.

Tôi có thể nói thế này: Tôi có thể bỏ phần này và

nói giải thích đoạn văn bản này bằng từ dễ hiểu.

Đây là phong cách thường ngày.

Tiếp theo, nếu bạn muốn theo hướng kỹ năng

thuật hơn, bạn có thể tạo kỹ năng tóm tắt.

Đây sẽ mang lại bản tóm tắt kỹ thuật

hơn là dựa trên thông tin bạn đưa ra.

Một lần nữa, đây là những cách khác nhau dành cho bạn

cải thiện trải nghiệm dựa trên người dùng của mình.

Tôi nghĩ bạn chỉ cần thử những điều đó

cách này rồi cho tôi biết kết quả.

Tiếp theo chúng ta sẽ thảo luận

về việc phát triển công cụ Tóm tắt.

Hiện tại bạn đã tạo ứng dụng.

Ứng dụng nằm trên local của bạn.

Nhưng sẽ thế nào nếu bạn phát triển

khai báo bằng Flask hoặc API nhanh chóng?

Sau khi được thử nghiệm, bạn có thể phát triển khai báo

sử dụng Flask, API nhanh hoặc Streamlit để sản xuất.

Đây là những cách khác nhau mà

các nhà phát triển đang thực hiện.

Tôi sẽ chỉ cho bạn một số trong số đó.

Tôi sẽ chỉ cho bạn cách

khai triển sử dụng API nhanh.

Vì vậy, chúng tôi sẽ thực hiện

thực hiện theo ba bước sau.

Đầu tiên, chúng tôi sẽ cài đặt API nhanh.

Sau đó, chúng tôi sẽ tạo

một ứng dụng tệp cho API đó.

Và sau đó chúng tôi có thể chạy API.

Chúng ta cùng bắt đầu.

Tôi sẽ tiếp tục và tạo một tệp

khác trong dự án chính của mình.

Tôi sẽ tạo ứng dụng chấm Pi.

Một lần nữa, những tệp này đã có sẵn

cho bạn trong tài nguyên thư mục để bạn

có thể tải xuống trong phần tài liệu

nguyên video. Tôi sẽ đóng cái này ở đây.

Xóa nó đi.

Và đầu tiên ở đây tôi sẽ nhập

pip cài đặt API nhanh và Uvicorn.

Vì vậy, đây là những trợ giúp cài đặt

chúng tôi phát triển các ứng dụng này.

Vì vậy, sau khi cài đặt

xong, tôi đã cài đặt chúng.

Bước tiếp theo là tạo ứng dụng Dot Pi này.

Và ở đây tôi sẽ viết một số mã dựa trên

những gì chúng tôi học cho đến hiện tại.

Vì vậy, trước tiên đối với fast API, message

kho mà chúng tôi đã nhập đã được cài đặt.

Chúng ta tiếp tục và nhập cái đó.

Tôi sẽ nhập API nhanh từ thư

API nhanh mà chúng tôi vừa cài đặt.

Tiếp theo tôi sẽ nói yêu cầu nhập khẩu.

Chúng tôi cần tôi tạo một ứng dụng gọi là và

use API đầu tiên ở lớp, sau đó gọi.

Điều này sẽ tạo đối tượng

API đầu tiên của tôi tại đây.

Sau đó, tôi sẽ đặt URL của mình.

Đây là URL của tôi, URL này sẽ chọn

tôi là một loại trong localhost 11 434.

Các mô hình của tôi sẽ được sử dụng tại đây.

Tiếp theo, tôi sẽ nói

ứng dụng tóm tắt ứng dụng.

Vì vậy, nếu bạn gọi API này trong

tuyến đường tóm tắt, tôi sẽ nói tóm tắt văn bản.

Đây là chức năng tôi cần chạy

và đây là văn bản bạn cần truyền tải.

Và tôi sẽ nói tải màn hình

DeepSea quan trọng một cách nhanh chóng.

Tóm tắt bất kỳ văn bản nào được truyền tải

cho tôi và tôi sẽ nói trực tuyến là sai.

Tiếp theo, tôi sẽ phản biện bằng cách phản hồi

với tải trọng JSON của url đăng nhập được yêu cầu.

Điều này sẽ thực hiện

yêu cầu và nhận phản hồi.

Và cuối cùng, tôi sẽ trả lời về việc thu thập JSON phản hồi

Phản hồi nếu đã có phản hồi hoặc không thể tạo tóm tắt.

Bây giờ chúng ta có thể chạy lệnh này

bằng cách nói Uvicorn app tải lại ứng dụng.

Đây là cách bạn có thể chạy ứng dụng này.

Tôi sẽ sao chép nội dung này.

Lưu tệp này.

Vào đây và chạy ứng dụng.

Bây giờ ứng dụng sẽ chạy ở đây.

Bây giờ cần một bài viết.

Vì vậy, điều tôi sẽ làm là mở

người đưa thư, tạo một yêu cầu mới.

If chưa được cài đặt

người đưa thư, bạn có thể cài đặt.

Đây chỉ là để thử nghiệm API.

Tôi sẽ viết URL ở đó.

Và nếu bạn nhớ đường dẫn, hãy tắt lại.

Vì vậy, tôi sẽ nói summ

tắt và được yêu cầu Đăng ký.

Bởi vì như tôi đã đề cập, đó là một bài

đăng tóm tắt ở URL này và tôi sẽ nói khóa.

Như bạn thấy, tôi cần văn bản.

Tôi sẽ nói.

Hãy chọn cho tôi một câu chuyện về điều đó.

Thực ra tôi đã nói tóm tắt.

Vì vậy, nó sẽ cố gắng đi hết điều này.

Vì vậy, tôi sẽ lưu giữ như vậy và

nói gửi và xem nó hoạt động như thế nào.

Bạn có thể đưa ra bất kỳ văn bản nào

vào đây và nó sẽ tắt văn bản này.

Vì vậy, nó sẽ gọi API đó bằng cách sử dụng ở đây

cách thực hiện cuộc gọi tới Allama.

Và nó sẽ cung cấp cho tôi cơ sở phản hồi về những gì máy chủ trả lại

dưới dạng API và bạn có thể phát triển điều này ở bất kỳ nơi nào bạn muốn.

Nhưng một lần nữa, bạn biết đấy, bạn cũng phải đảm bảo rằng bạn phát triển khai mô hình thực tế để tạo ra các

thứ.

Và một lần nữa, bạn sẽ được.

Đúng, nó đang nghĩ về điều đó.

Nó đã nghĩ đến điều đó rồi.

Và sau đó, tôi sẽ rất vui để tạo ra

một câu chuyện ngắn cho bạn.

Bạn có thể xác định được mong muốn của mình

loại câu chuyện nào không?

Vì vậy, nó cùng lúc cung cấp cho tôi một số nền văn bản dựa trên nền tảng

nó, nó đủ thông tin để biết tôi đang tìm kiếm điều gì dựa trên câu hỏi mà tôi đã có

truyền tải và nó đang hỏi tôi những câu hỏi bổ sung liên quan đến bối cảnh này.

Vì vậy, tôi hy vọng bạn

có thể xem qua phần này.

Và để tắt công cụ này ngay lúc này, chúng ta

đã xây dựng một bản tóm tắt văn bản tắt nhờ AI.

Chúng tôi đã tạo một

ứng dụng web để tắt.

Chúng tôi đã khám phá điều chỉnh nhắc nhở và tóm tắt nhiều tài khoản

liệu, đồng thời chúng tôi đã tìm hiểu cách phát triển khai báo tóm tắt như một API.

Bây giờ chương trình tiếp theo là tạo bản văn

dựa trên AI tự động hóa công việc tạo nội dung.

Hãy theo dõi.