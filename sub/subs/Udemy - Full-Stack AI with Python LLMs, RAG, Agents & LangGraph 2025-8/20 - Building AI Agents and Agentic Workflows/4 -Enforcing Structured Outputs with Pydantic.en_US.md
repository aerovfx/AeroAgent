# 4 -Thực thi các kết quả đầu ra có cấu trúc với Pydantic.en US

---

Được rồi, tôi hy vọng rằng bạn

rất thích mã hóa tác nhân AI đầu tiên của bạn.

Nhưng có một lượng lớn

lỗi trong hệ thống của chúng tôi.

Lỗi trong hệ thống của chúng tôi là

về cơ bản thì bây giờ là gì

đang xảy ra là chúng ta đang dựa vào

trên đầu ra chuỗi, phải không?

Không có đầu ra có cấu trúc.

Hãy để tôi nói cho bạn biết ý tôi là gì.

Những gì chúng tôi đã nói ở đây là

định dạng phản hồi bằng

để gõ đối tượng JSON.

Chúng tôi chỉ dựa vào điều đó, bạn biết đấy,

nó sẽ cho tôi một đầu ra JSON.

Tại sao?

Vì tôi đã cho anh ấy

trong các ví dụ mà này, làm ơn,

làm ơn trả lời tôi cái này

một loại định dạng JSON, phải không?

Vào cuối ngày

nó chỉ là một chuỗi.

Hãy xem, LLM có thể phản hồi

với kiểu như, này, chắc chắn rồi,

đây là kết quả của bạn phải không?

Này, chắc chắn rồi, đây là của bạn

đây là kết quả của bạn

Hãy xem, LLM thậm chí có thể xuất ra

một cái gì đó như thế này

Và nếu bạn cố gắng phân tích

điều đặc biệt này như

một JSON, nó sẽ thất bại.

Vì vậy, vấn đề là bây giờ

không phải là một đầu ra có cấu trúc.

Chúng tôi gần như rất

lạc quan về điều đó

được rồi, nó sẽ cho tôi một JSON

đầu ra và bất cứ khi nào chúng tôi làm

thứ này, đó là JSON.loads,

nó thực sự hoạt động, phải không?

Nhưng bạn biết đấy, bạn thực sự có thể

nói cho AI biết LLM về cái gì

cấu trúc tôi cần câu trả lời.

Bạn thực sự có thể thực hiện xác nhận.

Bạn thực sự có thể làm điều gì đó

được gọi là đầu ra có cấu trúc.

Vì vậy, nếu bạn tìm kiếm có cấu trúc,

đầu ra mở, có cấu trúc,

không phải thứ này, hãy xuất OpenAI.

Vì vậy bạn có thể thấy rằng ở đó

là toàn bộ tài liệu

xung quanh nó nền tảng OpenAI.

Hãy đợi nó tải

kết quả đầu ra có cấu trúc.

Và về cơ bản điều này có nghĩa là

rằng những thứ này đáng tin cậy hơn

loại an toàn, từ chối rõ ràng

và nhắc nhở đơn giản hơn.

Vì vậy những gì chúng ta có thể làm bây giờ là

cái này chúng ta sẽ sử dụng một thư viện

cái đó được gọi là pydentic.

Được rồi, vậy chúng ta cần

để cài đặt pynte đầu tiên.

Vì vậy tôi sẽ chỉ nói pip.

Cài đặt PYENTIC và nhập.

Vì vậy, bạn có thể thấy pyntic ở đây.

Vì thế tôi chỉ có thể nói bây giờ,

từ, không phải từ.

Từ mô hình cơ sở nhập khẩu Pyentic.

Được rồi, và bây giờ tôi thực sự có thể

viết một lược đồ đầu ra.

Vì thế tôi sẽ chỉ nói ở đây,

được rồi, đó là LLM.

Bạn chỉ có thể đặt tên cho nó

bất cứ điều gì đầu ra LLM.

Nó cần phải là một lớp học.

Vì vậy, tôi sẽ chỉ nói định dạng đầu ra của tôi.

Được rồi, và điều này cần

để trở thành một mô hình cơ sở.

Và sau đó tôi có thể chỉ

kể tất cả các lĩnh vực.

Ví dụ tôi cần một bước

đó là một chuỗi, được chứ?

Và sau đó bạn có thể thực hiện

nó tương đương với một trường.

Vì vậy, hãy nhập trường này.

Được rồi tôi sẽ chỉ nói

này, tôi cần một cánh đồng.

Vì vậy, mặc định.

Và sau đó bạn có thể chỉ cần đưa ra

Một mô tả đó là

tên, ID của bước.

Ví dụ.

Bạn chỉ có thể viết một ví dụ ở đây.

Đó là nó có thể được lập kế hoạch, nó có thể

là đầu ra, nó có thể là công cụ, v.v.

Được rồi, v.v.

Vậy về cơ bản bạn đang nói,

được rồi, cần phải có một bước,

sau đó bạn cần phải đưa ra

nội dung của họ là bước nào.

Được rồi, về cơ bản thì nội dung là

một chuỗi tùy chọn.

Vì vậy, từ kiểu nhập nhập tùy chọn.

Được rồi, từ việc gõ import

tùy chọn, vì vậy nó là tùy chọn

chuỗi, chuỗi tùy chọn.

Lại là một lĩnh vực nơi

giá trị mặc định là không có.

Mô tả là chuỗi,

nội dung chuỗi tùy chọn,

chuỗi tùy chọn

nội dung cho bước này.

Được rồi, về cơ bản thì đây là

một mô tả nhỏ

Được rồi, thế là xong.

Điều này đã được thực hiện.

Sau đó, có một công cụ.

Ồ, điều đó cũng tốt.

Vì vậy, về cơ bản, công cụ công cụ lại là một lần nữa

một chuỗi tùy chọn, được rồi, tùy chọn.

Và sau đó bạn có thể có

trường này không có mô tả

ID của công cụ cần gọi.

Được rồi, điều đó cũng đã xong.

Và sau đó bạn có một công cụ ở đó.

Sau đó, bạn có đầu vào.

Được rồi, đầu vào lại là

tùy chọn dưới dạng một chuỗi.

Và sau đó bạn có thể chỉ cần nói này,

nó cũng là một cánh đồng, không có gì cả.

Và sau đó bạn chỉ có thể nói

các thông số đầu vào cho cả hai.

Bây giờ về cơ bản đây là cách bạn muốn

cấu trúc được xuất ra.

Bây giờ bạn biết điều bạn có thể làm là

thay vì nói trước

trên hết, định dạng phản hồi.

Được rồi, vậy là có một vài

những điều chúng ta cần thay đổi ngay bây giờ.

Thứ nhất, chúng ta cần gọi cho khách hàng,

dấu chấm, hoàn thành phân tích dấu chấm.

Được rồi, đây là những gì

chúng ta cần gọi.

Và bây giờ tôi có thể trực tiếp đưa ra điều này

định dạng đầu ra của tôi mà chúng tôi

được định nghĩa ở đây là một định dạng phản hồi.

Bây giờ thay vì làm điều này, chúng ta

thực sự có thể gọi phân tích cú pháp.

Được rồi, bạn có thứ gì đó

được gọi là phân tích cú pháp.

Vì vậy, điều này thực sự sẽ

trực tiếp cung cấp cho bạn một kết quả được phân tích cú pháp.

Điều này đang trực tiếp đi

để cung cấp cho bạn một kết quả phân tích cú pháp.

Vì vậy nếu bạn nói nội dung, được thôi, nếu

bạn nói là nội dung, thực ra đây là

kết quả thô, kết quả phân tích cú pháp.

không cần thiết

thực hiện tải dấu chấm JSON.

Bạn chỉ cần nói này, tôi sẽ chỉ

sao chép thứ này và phân tích cú pháp dấu chấm.

Bây giờ phần tốt nhất là

khi bạn phân tích kết quả,

được rồi, phân tích dấu chấm kết quả.

Bạn có thể thấy bạn có tất cả mọi thứ.

Vì vậy khi bạn gọi,

khi bạn chỉ có thể nói bước.

Xem bạn có thuộc tính bước.

Tất cả các tài sản đều

gõ an toàn bây giờ, được chứ?

Và bạn biết điều gì xảy ra khi

bây giờ bạn cung cấp định dạng này cho LLM của bạn

thực sự sẽ đọc tất cả mọi thứ

Tôi có thể xuất ra, loại gì

và mô tả là gì.

Vì vậy, nó giống như tuyệt vời hơn để có.

Vì vậy không cần thiết

để làm điều này có được điều

Bây giờ tôi chỉ có thể nói trực tiếp Step.

Được rồi, tôi chỉ có thể nói bước chấm.

Và vâng, nó biết rằng bước

thực sự là một chuỗi.

Vì vậy, tôi thậm chí có thể loại bỏ

phần đặc biệt này.

Được rồi, để tôi chỉ

thay thế nó thật nhanh chóng.

Sao chép.

Và tôi sẽ chỉ dán nó ở đây.

Tôi sẽ chỉ dán nó ở đây.

Vậy đây là một điều

mà chúng ta cần phải làm.

Một điều nữa chúng ta cần làm là

trong mỗi bước đều có

không cần phải làm việc này.

Tôi chỉ có thể nói nội dung dấu chấm.

Phải?

Vì vậy, điều này có ý nghĩa hơn.

Được rồi.

Nội dung chấm.

Bây giờ cái này có thể ở đó,

điều này không thể có ở đó.

Không sao đâu.

Thậm chí điều này sẽ được chuyển đổi

đến một thứ được gọi là công cụ chấm.

Điều này sẽ được chuyển đổi thành một cái gì đó

như, bạn biết đấy, thứ này.

Và tất cả đều tốt.

Tất cả đều tốt.

Tất cả điều này cũng tốt.

Đúng vậy, thế này là thế này

tất cả cũng được thực hiện ở đây.

Ngoài ra chúng ta có thể loại bỏ điều này.

Được rồi, việc lập kế hoạch và chỉ

đặt một dấu chấm ở đây và thậm chí ở đây.

Ngoài ra chúng ta có thể loại bỏ điều này.

Đặt một dấu chấm và loại bỏ điều này.

Đẹp.

Bây giờ chúng ta hãy kiểm tra

việc thực hiện của chúng tôi.

Nếu mọi thứ đều hoạt động tốt,

thời tiết hiện tại thế nào?

Thời tiết hãy nói

Delhi và Hyderabad.

Được rồi.

Có vẻ như mọi thứ

đang hoạt động tốt.

Vâng.

Vì vậy, bạn có thể thấy mọi thứ hoạt động tốt.

Vì vậy, điều này về cơ bản đã được biết đến

như các đầu ra có cấu trúc.

Vì vậy, tiến về phía trước tôi thích

để sử dụng kết quả đầu ra có cấu trúc

bởi vì điều này mang lại cho tôi nhiều quyền kiểm soát hơn

về định dạng đầu ra tôi cần.

Bạn biết đấy, thực ra đây là

ít bị lỗi hơn.

Vì vậy, lỗi sẽ ít hơn bởi vì, bạn

biết đấy, chúng ta đang cho một vật rắn cố định

cấu trúc cho LLM của chúng tôi rằng, này, tôi

chỉ cần đầu ra ở định dạng này.

Được rồi.

Vì vậy đây là những gì chúng ta đang đi

để sử dụng di chuyển về phía trước.

Rất ít thứ.

Chúng ta cần tạo ra một mô hình

chúng ta cần gọi phân tích cú pháp.

Chúng ta có thể trực tiếp đưa ra câu trả lời

định dạng và chúng ta có thể sử dụng một định dạng được phân tích cú pháp,

property để có được kết quả phân tích cú pháp.

Không còn JSON.loads hoặc

một cái gì đó như thế