# 003 Xử lý lỗi ESP-IDF vi

---

Vì vậy, việc xử lý lỗi là điều quan trọng cần cân nhắc khi tạo một ứng dụng mạnh mẽ.

Và ở đây chúng tôi sẽ đề cập đến việc xử lý lỗi bằng cách sử dụng ESP ADF.

Và chúng ta sẽ bắt đầu với phần tổng quan về xử lý lỗi và sau đó chúng ta sẽ nói về mã lỗi, chuyển đổi

mã lỗi cho các thông báo lỗi bằng cách sử dụng macro Kiểm tra lỗi ESP và các mẫu hoặc chiến lược xử lý lỗi

mà bạn có thể muốn xem xét trong quá trình phát triển của mình.

Vì vậy, để bắt đầu, chúng ta hãy xem tài liệu ấn tượng.

Vì vậy, lỗi chúng ta đang thảo luận ở đây là lỗi thời gian chạy.

Và một lần nữa, xử lý những lỗi này là một khía cạnh quan trọng của việc phát triển các ứng dụng mạnh mẽ.

Và chúng ta có thể có một vài loại lỗi khác nhau.

Loại đầu tiên được đề cập ở đây được phân loại là các lỗi có thể phục hồi được, đó là các lỗi được biểu thị bằng

hoạt động thông qua các giá trị trả về hoặc mã lỗi.

Lỗi không thể khôi phục hoặc lỗi nghiêm trọng có thể xảy ra do xác nhận không thành công, chẳng hạn như sử dụng macro xác nhận

và các phương pháp tương đương.

Và nếu chúng ta theo liên kết xác nhận, bạn có thể quen với hàm khẳng định được xác định trong khẳng định

dấu chấm h, nhưng khi xác nhận giá trị thuộc loại esp thì loại lỗi bằng ESP OC.

Macro kiểm tra lỗi ESP được sử dụng thay vì khẳng định.

Và do đó, các ngoại lệ của CPU được coi là nghiêm trọng, có thể truy cập vào các vùng bộ nhớ được bảo vệ,

hướng dẫn bất hợp pháp, vv ..

Sau đó, bạn cũng có các kiểm tra cấp hệ thống như truy cập bộ nhớ đệm hết thời gian chờ của cơ quan giám sát, lỗi, tràn ngăn xếp,

ngăn xếp phá hủy đống tham nhũng, v.v. Và hướng dẫn này giải thích các cơ chế xử lý lỗi ESP IDF liên quan

để khắc phục các lỗi và cung cấp một số mẫu xử lý lỗi phổ biến.

Và tôi cũng sẽ chỉ cho bạn một số mẫu được sử dụng trong mã nguồn khóa học.

Và bạn luôn có thể xem liên kết này để biết hướng dẫn chẩn đoán lỗi không thể khôi phục.

Và bạn có thể muốn đánh dấu mục này là mục yêu thích trong tài nguyên ESP 32 của mình vì cuối cùng bạn buộc phải chạy

vào trình xử lý hoảng loạn để xử lý các lỗi nghiêm trọng này.

Vì vậy, hãy chuyển sang mã của chúng tôi.

Hầu hết các hàm cụ thể của ESP đều sử dụng loại lỗi ESP để trả về mã lỗi.

Và loại ESP được gán loại số nguyên, bạn có thể tìm thấy loại này trong tệp Esp h từ ESP và thành công

hoặc không có lỗi nào được biểu thị bằng mã ESP, được xác định bằng 0.

Và các mã lỗi phổ biến cho các lỗi chung như hết bộ nhớ, đối số không hợp lệ và hết thời gian chờ, v.v. là

cũng được định nghĩa ở đây.

Và bạn cũng có các mã lỗi khác được xác định trong các tệp tiêu đề ESP EDF khác nhau.

Đồng thời sử dụng bộ tiền xử lý để xác định bắt đầu bằng tiền tố ESP.

Ví dụ: có các mã lỗi liên quan đến NVS được xác định trong tệp lưu trữ không biến đổi và ở đây

Lỗi ESP Cơ sở NVS được định nghĩa là số bắt đầu cho các mã lỗi và sau đó là mỗi lỗi tiếp theo

mã được định nghĩa là phần bù từ cơ sở.

Và việc chuyển đổi mã thành thông báo lỗi cũng có thể hữu ích khi gỡ lỗi bằng cách hiển thị thông báo lỗi

dưới dạng chuỗi trên màn hình đầu cuối.

Điều này có thể thực hiện được đối với từng mã lỗi được xác định trong các thành phần ESP ADF và loại lỗi ESP có thể được chuyển đổi

đến tên mã lỗi bằng cách sử dụng lỗi ESP để đặt tên hoặc lỗi ESP để đặt tên gạch dưới các hàm của chúng tôi.

Ví dụ: chúng tôi sẽ sử dụng lỗi ESP để đặt tên cho các hàm lưu trữ bất biến của mình và trong ví dụ này

chúng tôi gọi NVS Open, nó trả về trạng thái lỗi ESP.

Và nếu nó không trả về thành công hoặc ESP OC thì chúng ta có thể sử dụng lỗi ESP để đặt tên và hiển thị kết quả của nó

sử dụng print def hoặc esp log.

Vì vậy nếu bạn muốn tìm ra nguyên nhân chính xác khiến một hàm bị lỗi, hãy thử sử dụng các hàm này.

Và cách thức hoạt động của nó là tìm mã lỗi trong bảng tra cứu được tạo sẵn và trả về nó

biểu diễn chuỗi.

Và ở đây bạn có bảng tra cứu được xác định ở đây.

Trong đó mỗi mục trong bảng là một mã lỗi trong cặp thông báo và lỗi ESP đối với tên gạch dưới r có thể

được sử dụng khi bạn cũng cần xem xét mã lỗi hệ thống.

Vì vậy, ở đây, nếu không tìm thấy mã lỗi thì lỗi str gạch dưới r sẽ được sử dụng.

Vậy quay lại với macro kiểm tra air ESP, macro kiểm tra lỗi ESP kiểm tra giá trị loại lỗi ESP nhé

hơn trạng thái bò đực.

Và nếu đối số của việc kiểm tra lỗi ESP không bằng ESP thì thông báo lỗi sẽ được in trên

console và hàm hủy bỏ được gọi và trên console.

Thông báo lỗi của bạn sẽ trông như thế này.

Vì vậy, ở đây trong tài liệu có nói rằng nếu sử dụng màn hình ADF, các địa chỉ trong dấu vết quay lại sẽ

được chuyển đổi thành tên tập tin và số dòng.

Và dòng đầu tiên đề cập đến mã lỗi dưới dạng giá trị thập lục phân và mã định danh được sử dụng cho lỗi này

trong mã nguồn và các dòng tiếp theo hiển thị vị trí trong chương trình nơi Macro kiểm tra lỗi ESP

được gọi và biểu thức được chuyển tới macro dưới dạng đối số.

Sau đó, dấu vết quay lại được in ra, đây là một phần của đầu ra của trình xử lý hoảng loạn thường gặp đối với tất cả các lỗi nghiêm trọng.

Và nếu bạn không muốn hủy bỏ nhưng vẫn có được sự tiện lợi của macro này, bạn luôn có thể sử dụng

Kiểm tra lỗi ESP mà không hủy macro.

Bây giờ chúng ta hãy xem xét một số chiến lược để xử lý những lỗi này.

Vì vậy, tài liệu khuyến nghị các chiến lược sau.

Trước tiên bạn có thể cố gắng khôi phục.

Và tùy thuộc vào tình huống, chúng ta có thể muốn thử các phương pháp sau.

Bạn có thể thử lại cuộc gọi như bên dưới, nơi cuộc gọi hàm được thử lại trong khi kết quả là

đã hết thời gian.

Hoặc bạn có thể thử khởi tạo lại trình điều khiển và khởi động lại nó hoặc khắc phục tình trạng lỗi

sử dụng cơ chế out of band.

Ví dụ: đặt lại thiết bị ngoại vi bên ngoài không phản hồi và ví dụ về nơi chúng tôi cố gắng

để phục hồi từ các lỗi.

Tôi muốn cho bạn thấy khởi tạo nghịch đảo mà chúng tôi sử dụng trong main.

Vì vậy, ở đây, nếu hàm init flash NBS trả về với một trong các lỗi sau, thì chúng ta sẽ xóa

flash và khởi tạo lại nó.

Vì vậy, đây là một ví dụ về nỗ lực phục hồi và một phản ứng khả thi khác là lan truyền

lỗi cho người gọi.

Và đây là một ví dụ về điều đó.

Và cuối cùng, bạn có thể chỉ định một số chức năng nhất định là lỗi không thể phục hồi bằng cách sử dụng tính năng kiểm tra ESP.

Vì vậy, bạn sẽ cần phải tự quyết định xem khi nào sử dụng ESP hoặc kiểm tra xem ứng dụng của bạn có hợp lý hay không.

Như đã đề cập ở đây, nhiều ví dụ về ESP ADF và tôi thường tự mình làm việc này bằng cách sử dụng tính năng kiểm tra lỗi ESP để xử lý

lỗi từ nhiều API khác nhau và đây không phải là cách thực hành tốt nhất cho các ứng dụng và được thực hiện để làm ví dụ

mã ngắn gọn hơn để có thể thuận tiện khi sử dụng.

Tuy nhiên, bạn sẽ cần suy nghĩ nhiều hơn về việc xử lý lỗi và áp dụng cách xử lý lỗi thích hợp

các mẫu khi bạn cần chương trình cơ sở của mình sẵn sàng sản xuất.

Được rồi.

Vì vậy, đó là nó bây giờ.

Và hẹn gặp lại các bạn trong bài học tiếp theo.