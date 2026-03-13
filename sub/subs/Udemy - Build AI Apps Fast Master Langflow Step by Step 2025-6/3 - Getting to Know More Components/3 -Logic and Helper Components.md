# 3 -Dịch các thành phần logic và trợ giúp

---

Tiếp tục phân tích các thành phần có sẵn trong Lancthlo, đã đến lúc xem lại

một số phần tử liên quan đến Logic cũng như các thành phần hữu ích cho việc thực hiện

hoạt động hoặc cái gọi là các thành phần trợ giúp.

Các thành phần này nằm trong phần Logic.

Đầu tiên, chúng ta tìm thấy một thành phần có tên if else.

Chúng ta có thể thấy rằng mô tả cho biết thành phần này cho phép bạn định tuyến đầu vào

thông báo đến một đầu ra tương ứng dựa trên so sánh văn bản.

Kid, chúng ta có thể đánh giá một chuỗi bằng sap.

Kid, chúng ta có văn bản khớp, nghĩa là chuỗi bạn muốn so sánh.

Nếu hai chuỗi này trả về một kết quả bằng nhau, nghĩa là nếu cả hai văn bản đều giống nhau thì chuỗi

kết quả sẽ đúng.

Chúng ta có thể kiểm tra những điều này bằng cách chạy thành phần.

Và bạn sẽ nhận thấy rằng chưa có gì xảy ra cả, vì chúng ta vẫn cần hoàn thành tin nhắn

ở đây.

Tin nhắn chuỗi này, theo mô tả, sẽ được gửi qua bất kỳ tuyến đường nào.

Kid, chúng ta có thể sử dụng bất kỳ chuỗi nào, ví dụ: result.

Hãy chạy lại thành phần và bạn có thể thấy đầu ra này sáng lên với giá trị

các tập tin, vì văn bản đầu vào và văn bản mong đợi không giống nhau.

Nếu thay thế văn bản này bằng tập giá trị, chúng ta có thể thấy cả hai đều bằng nhau.

Vì vậy, nếu chúng ta chạy lại thành phần này, bạn có thể thấy rằng bây giờ chúng ta nhận được kết quả là true, kết quả này

hiển thị cho chúng tôi kết quả chuỗi, thông báo chúng tôi sẽ chuyển đi.

Về cơ bản, tin nhắn này được gửi nếu đáp ứng điều kiện đúng hoặc sai giữa hai điều kiện này

văn bản.

Đó là cách thành phần if else này hoạt động.

Các bạn có thể thấy trong thành phần này chúng ta chỉ có các trường nhập văn bản.

Chúng ta có các thành phần khác, chẳng hạn như thành phần listen, có thể được sử dụng để nhận

một thông báo.

Chúng tôi cũng có thành phần này được gọi là vòng lặp, chúng tôi đã xem xét trước đó và cho phép chúng tôi

nhập tập dữ liệu đó.

Chúng tôi có một đầu ra mục trích xuất một giá trị, một bản ghi từ bộ dữ liệu này

để xử lý.

Chúng tôi có nút này, cho phép chúng tôi lặp qua tập hợp dữ liệu, với đầu ra của nó được tích lũy

khi vòng lặp tiến triển.

Vào cuối chu trình, tại nút được gọi là done, chúng ta thu được kết quả cuối cùng của việc ghép nối

tất cả các phản hồi hoặc kết quả được tạo ra trong vòng lặp.

Những kết quả này về cơ bản giống với những kết quả mà chúng tôi đã nhập lại như một phần của nút vòng lặp này.

Chúng tôi cũng có một thành phần được gọi là thông báo, cho phép chúng tôi tạo thông báo, do đó, một thành phần khác

thành phần được cảnh báo.

Một thành phần rất hữu ích khác được gọi là pass, cho phép chúng ta chuyển tiếp đầu vào

tin nhắn mà không sửa đổi nó.

Chúng tôi có một thành phần rất hữu ích khác gọi là runflow, cho phép chúng tôi chọn một trong các luồng

trong thư mục hoặc từ tập hợp các luồng trong dự án để thực hiện một số quy trình tiền xử lý

khi cần thiết.

Điều này giúp tránh có một luồng quá dài hoặc phức tạp, bằng cách cho phép chúng ta chia nhỏ các luồng khác nhau

nhiệm vụ thành các luồng con mà sau đó chúng ta có thể kết nối.

Thành phần này rất hữu ích và nó thuộc danh mục được gọi là logic.

Chúng tôi cũng có một tập hợp các thành phần trong danh mục trợ giúp.

Ví dụ: cái này được gọi là chạy hàng loạt, cho phép chúng tôi chạy mô hình ngôn ngữ trên mỗi hàng của

cột văn bản của khung dữ liệu, trả về khung dữ liệu mới có ba cột, nhập văn bản,

phản hồi mô hình và chỉ mục lô.

Trường hợp thực tế nào khi sử dụng tính năng chạy hàng loạt này?

Ví dụ: giả sử chúng ta có một thành phần URL, tôi sẽ kéo và thả nó, sau đó tôi sẽ

sao chép một trong các URL tôi đã cập nhật trước đó, tôi sẽ dán nó và giả sử bạn muốn

để xử lý từng URL này nhằm lấy một số thông tin hoặc để thực hiện một thao tác cụ thể

trên Junit bằng cách sử dụng hệ thống massage.

Những gì Junit cần làm là kết nối khung dữ liệu với khung dữ liệu đầu vào chạy hàng loạt, điều này sẽ

cho phép chúng tôi chạy một tập hợp các hoạt động trên nhiều bản ghi.

Chúng ta phải kết nối một mô hình trí tuệ nhân tạo.

Trong trường hợp này, tôi sẽ kết nối mô hình openAI.

Tôi đã cấu hình nó trước đó bằng khóa.

Tôi sẽ đặt GPD cho mô hình và kết nối nó với thành phần chạy hàng loạt.

Trong phần xoa bóp hệ thống, chúng tôi sẽ thêm hướng dẫn sẽ được thực thi trên các

tập hợp các bản ghi, trong trường hợp cụ thể này là các URL.

Vậy tôi muốn làm gì trong lời nhắc này?

Ví dụ, để tóm tắt văn bản trong một đoạn văn.

Tôi muốn mỗi văn bản đầu vào được tóm tắt trong một đoạn văn.

Hãy chạy thành phần này.

Hãy đợi một lát.

Hãy nhớ rằng, có thể mất nhiều thời gian hơn một chút vì nó thực hiện một thao tác với mô hình AI.

Nếu chúng tôi kiểm tra kết quả, bạn sẽ thấy rằng ở đây chúng tôi có văn bản đầu vào được trích xuất từ ​​

URL.

Trong phản hồi của mô hình, có phần tóm tắt văn bản do mô hình AI tạo ra bằng cách sử dụng

thông tin được cung cấp, rất hữu ích nếu bạn cần xử lý hàng loạt một tập hợp kết quả.

Đây là cách chạy hàng loạt hoạt động.

Nó cho phép chúng ta áp dụng một lệnh cho một tập hợp các bản ghi bằng mô hình AI.

Trong danh mục này, chúng tôi tìm thấy một số tiện ích bổ sung, chẳng hạn như tiện ích này cho phép chúng tôi

để có được ngày chữa bệnh.

Nếu chúng tôi chạy nó và quan sát kết quả, chúng tôi sẽ nhận được phản hồi về ngày và giờ xử lý,

có thể hữu ích để đưa ra hướng dẫn cho mô hình AI, chẳng hạn như xử lý dữ liệu

trong khoảng thời gian trước đó, chẳng hạn như một tháng trước ngày bảo dưỡng.

Chúng tôi cũng có các thành phần khác, chẳng hạn như trình tạo ID, cho phép bạn tạo các thành phần khác nhau

các giá trị duy nhất để đưa vào luồng của bạn.

Chúng tôi cũng có ở đây.

Thành phần đó gọi là lịch sử massage, cho phép chúng ta truy xuất các tin nhắn trò chuyện đã lưu trữ

trong bảng lưu lượng độ dài hoặc trong bộ nhớ ngoài.

Điều này cũng có thể được sử dụng với dịch vụ mát-xa được lưu trữ, phục vụ cho mục đích ngược lại.

Điều này cho phép chúng tôi lưu trữ thông tin massage trong một bảng lưu lượng chiều dài và lịch sử massage cho phép chúng tôi

lấy nó.

Làm thế nào chúng ta có thể kiểm tra điều này?

Đầu tiên, chúng ta sẽ sử dụng massage lưu trữ.

Tôi viết, ví dụ, xin chào thế giới.

Tôi sẽ chạy ghi chú này.

Bạn có thể thấy mọi thứ hoạt động chính xác.

Vì vậy, điều tôi làm tiếp theo là chạy thành phần này có tên là lịch sử massage.

Và nếu chúng tôi kiểm tra dữ liệu thu được, bạn có thể thấy đó là một phần của bản ghi duy nhất này,

văn bản bắt đầu có tên hello world xuất hiện.

Bằng cách này, chúng tôi đã lưu nội dung văn bản này trong một bảng lưu lượng độ dài và truy xuất nó.

Nó rất hữu ích để lưu một massage tạm thời mà bạn muốn giữ trong một khoảng thời gian nhất định

trong một cuộc trò chuyện chẳng hạn hoặc trong một số hoạt động khác.

Là một phần của danh mục công cụ mở rộng này, chúng tôi có một thành phần cuối cùng được gọi là đầu ra có cấu trúc,

điều này rất hữu ích vì nó cho phép bạn chuyển đổi phản hồi từ mô hình NE thành có cấu trúc

định dạng dữ liệu lý tưởng để trích xuất thông tin cụ thể hoặc tạo ra một định dạng nhất quán

kết quả.

Điều này đề cập đến điều gì?

Một điều tôi thực sự thích ở thành phần này là nó cho phép bạn tạo đầu ra

để LLM hoặc mô hình có thể tạo ra phản hồi mới.

Ý tôi là gì?

Bây giờ hãy thêm một trường văn bản mới vào luồng.

Thêm một phần của quy trình này và truy cập git.com và mở một trong những cuốn sách được bao gồm

trong kho lưu trữ độ dài chính thức.

Tôi sao chép tất cả thông tin trên văn bản và dán nó như một phần nội dung.

Vì vậy, khi tôi chỉnh sửa xong, điều tôi đang tìm kiếm là từ thông tin này hoặc từ

văn bản được trích xuất, ví dụ: tôi có thể lấy ID sách, trong trường hợp này là 8118.

Tôi cũng muốn lấy tiêu đề, mô tả cuốn sách và nhấn vào đó để tạo ra một số loại tóm tắt hoặc

tổng hợp cùng với các chi tiết khác.

Vì vậy, để điều này hoạt động chính xác, chúng ta cần kết nối một thành phần của mô hình AIA.

Trong trường hợp này, tôi sẽ kết nối Open AIA1.

Tôi sẽ liên kết mô hình ngôn ngữ với thành phần đầu ra có cấu trúc này và đầu ra

tin nhắn xuất phát từ tin nhắn git.com.

Thông báo vấn đề git.com, tôi sẽ kết nối với thông báo đầu vào.

Bây giờ, điều quan trọng ở đây là cấu hình lược đồ đầu ra.

Để làm được điều đó, chúng ta có tùy chọn mở một bảng nơi chúng ta có thể chỉ định tên của trường

chúng tôi muốn tạo ra.

Mô tả mà chúng tôi muốn lấy từ thông tin hoặc văn bản đầu vào, loại và liệu chúng tôi có muốn

nó có lấy được nhiều bản ghi hay không.

Chúng ta cấu hình nó như thế nào?

Ví dụ: hãy viết git.help.issue và ở đây chúng ta có thể chỉ định mô tả của trường

cho những gì chúng tôi đang mong đợi.

Tại đây, chúng ta có thể tạo hoặc viết lời nhắc để lấy thông tin hoặc dữ liệu cụ thể.

Bạn có thể mô hình hóa điều này theo cách bạn thích.

Ví dụ: bắt đầu từ một mã định danh, bạn có thể tạo một mã định danh mới và duy nhất.

Vì vậy, nếu bạn có ngôn ngữ ở định dạng ISO, bạn có thể lấy tên đầy đủ của ngôn ngữ tương ứng

tới bản ghi đó.

Nó có thể là bất cứ điều gì bạn muốn.

Bằng cách viết hướng dẫn cho mô hình AIA, bạn có thể nhận được thông tin mình cần.

Trong trường hợp này, tôi sẽ chỉ ra rằng đây là ID vấn đề.

Tôi sẽ chỉ rõ rằng mã định danh này, ví dụ, là số và nó không phải là bội số.

Vì đây là một ID duy nhất nên ở đây chúng ta có thể thêm nhiều số nhận dạng hơn hoặc thậm chí nhiều trường hơn.

Ví dụ: ở đây, tiêu đề gạch dưới git.cuff.

Hãy đặt cái này bằng với tiêu đề vấn đề.

Và khi chúng ta có cặp bản ghi này, đây sẽ là lược đồ đầu ra, chúng ta sẽ lưu các thay đổi

và chạy thành phần để xem kết quả được tạo ra.

Sau vài giây, chúng ta có thể thấy rằng quá trình chạy đã thành công.

Hãy nhìn vào kết quả.

Bạn có thể thấy rằng lược đồ đã được tạo chính xác, giống như chúng tôi đã chỉ định git.cuff

vấn đề và tiêu đề git.cuff.

Nhóc, chúng ta đã có ID phát hành cũng như tiêu đề của nó.

Vì vậy, đây là thành phần mà tôi thấy cực kỳ hữu ích để tạo ra kết quả đầu ra mà chúng ta cần

từ một tin nhắn đầu vào.

Tôi thấy nó rất hữu ích vì với điều này chúng ta có thể định dạng, tạo mẫu cho lời nhắc

và dễ dàng tạo ra phản hồi hoặc lược đồ mà chúng tôi cần.

Về cơ bản, đây là các thành phần logic và các thành phần kiểu trợ giúp có thể giúp

chúng tôi trong quy trình làm việc của chúng tôi trong langflow.