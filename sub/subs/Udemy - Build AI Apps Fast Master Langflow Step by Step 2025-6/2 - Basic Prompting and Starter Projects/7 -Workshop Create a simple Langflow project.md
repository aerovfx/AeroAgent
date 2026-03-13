# 7 -Workshop Tạo dự án Langflow đơn giản đã dịch

---

Đã đến lúc tạo dự án thực tế đầu tiên của chúng ta.

Dự án này sẽ cho phép người dùng tải lên tệp PDF hoặc loại tệp khác và từ đó

tài liệu, ai đó sẽ có thể đặt câu hỏi.

Tuy nhiên, câu trả lời sẽ tập trung vào việc được giải thích theo cách mà trẻ mẫu giáo

có thể dễ dàng hiểu được.

Dự án sẽ được gọi là người bạn thông thái của tôi.

Hãy bắt đầu dự án này bằng cách tạo một luồng mới trong thư mục luồng khóa học.

Hãy tạo một dự án.

Chúng tôi sẽ chỉ định rằng chúng tôi muốn bắt đầu với một luồng trống.

Chúng tôi sẽ làm những gì chúng tôi đã thực hành cho đến nay.

Chúng tôi sẽ thêm đầu vào trò chuyện.

Ngoài ra, đối với đầu ra, chúng tôi sẽ thêm thành phần đầu ra trò chuyện.

Cuối cùng, hãy thêm mô hình OpenAI, mặc dù bạn cũng có thể chọn mô hình khác nếu có

truy cập vào một.

Chúng ta sẽ kết nối đầu vào trò chuyện với đầu vào thích hợp và cuối cùng, đầu ra này

tin nhắn được gọi đến đầu ra trò chuyện.

Với điều này, chúng ta có một quy trình tương tự như những gì chúng ta đã thấy trong các bài học trước.

Như tôi đã đề cập trước đây, chúng tôi muốn câu trả lời phải dễ hiểu đối với trẻ mẫu giáo.

Do đó, chúng tôi sẽ sửa đổi thuộc tính này được gọi là thông báo hệ thống để nó phù hợp với những gì chúng tôi cần.

Chúng ta sẽ thực hiện việc này bằng cách sử dụng thành phần nhập văn bản.

Bây giờ, chúng ta hãy đến phần nhập liệu, kéo thành phần nhập văn bản vào và sửa đổi văn bản.

Tôi sẽ dán lời nhắc tôi đã viết trước đó, trong đó nói rằng bạn là chuyên gia viết lách

thực tế cho trẻ mầm non.

Việc sử dụng câu hỏi chặt chẽ hơn nên được tạo ra một cách đơn giản bằng cách sử dụng các phép loại suy, các câu chuyện,

và những câu chuyện văn học hoặc những phương pháp khác mà bất kỳ đứa trẻ nào cũng có thể hiểu được.

Chúng tôi sẽ gán văn bản này cho thành phần này và sau khi được xác định, chúng tôi sẽ kết nối thành phần này

được gọi là nhập văn bản với thông báo hệ thống.

Bằng cách này, phản hồi chúng tôi nhận được từ mô hình OpenAI sẽ luôn bị ảnh hưởng bởi điều này

thông báo hệ thống mà không cần sửa đổi kiểu nhập văn bản của người dùng.

Bây giờ, chúng tôi cần thông tin theo ngữ cảnh để tạo phản hồi, nghĩa là tôi ghi lại hoặc

thành phần cho phép chúng tôi nhận một tệp và yêu cầu mô hình chỉ phản hồi dựa trên đó

phần tử.

Và để làm được điều này, trong phần này chúng ta có trong các chuyên mục, có một phần tên là

giữa dấu ngoặc kép, dữ liệu, nơi chúng ta có thể thấy các thành phần khác nhau cho phép chúng ta nhập thông tin người dùng

thông tin.

Chúng tôi quan tâm đến việc có thể đọc một tài liệu.

Trong trường hợp này, chúng tôi sẽ sử dụng thành phần này có tên file.

Thành phần này cho phép chúng ta chọn một tập tin.

Hãy nhấp vào phần này có nội dung tập tin.

Trước đây, tôi đã tạo hoặc tải xuống một tài liệu có tên burnout.pdf.

Tôi sẽ chọn nó.

Và bạn có thể thấy rằng tài liệu được tải lên chính xác.

Bây giờ chúng ta đã có thành phần này sẵn sàng, cho phép chúng ta đọc thông tin từ tài liệu này tới

hỏi những câu hỏi khác nhau.

Bạn có thể thấy rằng thành phần này có một số đầu ra, một đầu ra gọi là dữ liệu, một đầu ra khác gọi là

khung dữ liệu và một tin nhắn khác được gọi là.

Hãy chạy thành phần này để xem những gì được tạo ra từ tài liệu.

Là một phần của đầu ra được gọi là dữ liệu này, bạn có thể thấy rằng chúng tôi có một số thuộc tính như

tập tin pad và văn bản.

Là một phần của đầu ra khung dữ liệu, chúng tôi có các thuộc tính tương tự.

Và trong phần này được gọi là tin nhắn, bạn tìm thấy nội dung của tệp PDF.

Đây thực sự là điều chúng tôi quan tâm, chỉ là nội dung của tài liệu.

Bây giờ, chúng ta cần xử lý cả ngữ cảnh hoặc nội dung của tài liệu PDF, điều này sẽ phục vụ

làm tài liệu tham khảo để trả lời truy vấn của người dùng và truy vấn thực tế của người dùng.

Như vậy chúng ta có thể đặt câu hỏi về file mình đã upload.

Như chúng ta đã thấy trước đây, thành phần sẽ cho phép chúng ta sửa đổi truy vấn cho mô hình A&M

được gọi là nhắc nhở.

Vì vậy, hãy đi tới phần lời nhắc, kéo thành phần lời nhắc và sửa đổi mẫu để chỉ định

rằng nó nên sử dụng nguồn thông tin sau đây làm nguồn duy nhất để trả lời

bạn đã nói câu hỏi.

Nếu không tìm thấy điều gì đó trong văn bản hoặc tài liệu, bạn nên từ chối câu hỏi một cách dứt khoát.

Đầu tiên, chúng ta phải chỉ định nguồn thông tin làm tham số.

Hãy tạo một biến đầu tiên có tên là source.

Nơi nội dung của tài liệu PDF sẽ được lưu trữ trong trường hợp cụ thể này.

Tiếp theo, chúng ta sẽ tạo phần thứ hai gọi là truy vấn của người dùng, phần này xác định truy vấn của người dùng.

Điều này sẽ thể hiện những gì người dùng nhập vào trong cửa sổ trò chuyện hoặc cửa sổ trò chuyện.

Với điều này, chúng tôi đã tạo thành phần của mình và chúng tôi sẵn sàng nhận cả thành phần của người dùng.

truy vấn và nguồn dữ liệu.

Chúng ta sẽ chỉ ra rằng đầu ra của thành phần tệp, như bạn đã nhớ,

là văn bản được đọc từ tài liệu, sẽ là nguồn cho lời nhắc.

Tiếp theo, chúng ta sẽ chọn thành phần có tên là đầu vào trò chuyện, thành phần này đã được kết nối trước đó với

thành phần OpenAI.

Hãy xóa liên kết trước đó và gán kiểu nhập văn bản cho truy vấn.

một phần của thành phần nhắc nhở.

Bằng cách này, bây giờ chúng ta đã có sẵn thành phần nhắc nhở và điều chúng ta sẽ làm tiếp theo là

lấy đầu ra của thành phần đó trở thành đầu vào cho mô hình AI.

Vì vậy, với điều này, chúng tôi đã sẵn sàng dán dòng chúng tôi đã tạo.

Hãy bắt đầu cách giải quyết và đặt câu hỏi đầu tiên, chẳng hạn như hỏi Marty McFly là ai.

Hãy gửi yêu cầu.

Trong trường hợp này, nó cho tôi biết rằng tôi cần định cấu hình thành phần OpenAI vì chưa có khóa nào

đã vào.

Tôi sẽ nhập nó một cách nhanh chóng.

Khi khóa được khởi động lại, tôi kiểm tra lại truy vấn của mình.

Sau vài giây, chúng ta có thể thấy mô hình đã phản hồi chính xác.

Và điều bạn có thể nhận thấy là ở đây câu trả lời cho chúng ta biết không có thông tin

về nhân vật này.

Điều này là do chính sách mà chúng tôi đã thêm vào như một phần của lời nhắc hoặc hướng dẫn về cách

mô hình phải được thanh toán khi đưa ra phản hồi cho chúng tôi.

Nó hỏi liệu chúng ta có muốn thực hiện một truy vấn khác không.

Vì vậy, hãy đặt một câu hỏi liên quan đến tài liệu chúng tôi đã thêm.

Trong trường hợp này là về sự kiệt sức.

Như bạn có thể thấy, sau vài giây, chúng ta đã có câu trả lời.

Nhóc à, chúng ta có câu trả lời về tình trạng kiệt sức bằng cách sử dụng một số ví dụ tương tự như một món đồ chơi chạy

hết pin hoặc PCB quá mệt mỏi để tiếp tục hoạt động.

Điều này tuân theo các quy tắc chúng tôi đã đặt ra cho cả lời nhắc và massage hệ thống.

Hãy kiểm tra nó bằng một câu hỏi cuối cùng.

Làm thế nào ai đó có thể phục hồi sau khi kiệt sức?

Sau vài giây, chúng ta sẽ thấy câu trả lời và một lần nữa nhận thấy một số phép loại suy như

sử dụng một tên Benny đang rảnh rỗi.

Nhóc à, nó có nhắc đến một số thông tin liên quan đến bộ râu tên Benny và những gì nên làm với nó.

vượt qua sự kiệt sức.

Vì vậy, chúng tôi thấy rằng nó đang thực hiện chính xác những gì chúng tôi đã chỉ định.

Nó không phản hồi với bất kỳ điều gì không liên quan đến tài liệu PDF và nó cũng trả lời bằng

một cách tự do và dễ hiểu bằng cách sử dụng các phép loại suy, các câu chuyện và câu chuyện tùy thuộc vào những gì người dùng yêu cầu.

Vì vậy, trẻ mẫu giáo không thể hiểu được các khái niệm khác nhau ngay cả khi chúng rất

phức tạp.

Bằng cách này, chúng ta sẽ hoàn thành dự án đầu tiên rất thú vị của mình và tôi hy vọng điều đó

sẽ hữu ích cho bạn trong tương lai.