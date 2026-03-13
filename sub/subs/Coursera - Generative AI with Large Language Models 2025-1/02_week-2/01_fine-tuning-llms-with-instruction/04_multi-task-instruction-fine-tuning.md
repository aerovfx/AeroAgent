# 04 đa nhiệm-hướng dẫn-tinh chỉnh

---

Tinh chỉnh đa nhiệm

là một phần mở rộng

tinh chỉnh một nhiệm vụ,

đào tạo ở đâu

tập dữ liệu bao gồm

ví dụ đầu vào và đầu ra

cho nhiều nhiệm vụ.

Ở đây, tập dữ liệu

chứa các ví dụ

hướng dẫn người mẫu mang theo

thực hiện nhiều nhiệm vụ khác nhau,

bao gồm tóm tắt,

đánh giá đánh giá,

dịch mã và

nhận dạng thực thể.

Bạn huấn luyện mô hình trên

tập dữ liệu hỗn hợp này

rằng nó có thể cải thiện

hiệu suất của mô hình trên

tất cả các nhiệm vụ cùng một lúc,

do đó tránh được vấn đề

sự lãng quên thảm khốc.

Trải qua nhiều thời kỳ rèn luyện,

tổn thất được tính toán

qua các ví dụ

được sử dụng để cập nhật

trọng số của mô hình,

dẫn đến một hướng dẫn

mô hình điều chỉnh đã học

làm thế nào để giỏi nhiều thứ

nhiệm vụ khác nhau cùng một lúc.

Một nhược điểm của đa nhiệm

tinh chỉnh là nó

đòi hỏi rất nhiều dữ liệu.

Bạn có thể cần nhiều như

50-100.000 ví dụ

trong tập huấn luyện của bạn.

Tuy nhiên, nó có thể

thực sự đáng giá

và đáng nỗ lực

để tập hợp dữ liệu này.

Các mô hình kết quả

thường rất

có khả năng và phù hợp để sử dụng trong

tình huống ở đó

hiệu suất tốt

ở nhiều nhiệm vụ là mong muốn.

Chúng ta hãy nhìn vào một gia đình

của các mô hình đã được

được đào tạo sử dụng đa nhiệm

tinh chỉnh hướng dẫn.

Hướng dẫn phương sai mô hình

khác nhau dựa trên

các tập dữ liệu và nhiệm vụ

được sử dụng trong quá trình tinh chỉnh.

Một ví dụ là

Nhóm mô hình FLAN.

FLAN, viết tắt của

mạng lưới ngôn ngữ tinh chỉnh,

là một tập hợp cụ thể

hướng dẫn

dùng để tinh chỉnh

mô hình khác nhau.

Vì họ là FLAN

Tinh chỉnh là bước cuối cùng của

quá trình đào tạo

tác giả của bài báo gốc

gọi nó là

món tráng miệng ẩn dụ

khóa học chính của đào tạo trước

một cái tên khá phù hợp.

FLAN-T5, FLAN

hướng dẫn phiên bản của

mô hình nền tảng T5 trong khi

FLAN-PALM là

phiên bản cấu trúc làm phẳng

của mô hình nền cọ.

Bạn hiểu ý rồi,

FLAN-T5 là một vị tướng tuyệt vời

mô hình hướng dẫn mục đích

Tổng cộng thì đó là

đã được tinh chỉnh

473 bộ dữ liệu trên

146 loại nhiệm vụ.

Các tập dữ liệu đó được chọn từ

các mô hình khác và

giấy tờ như ở đây.

Đừng lo lắng về việc đọc

tất cả các chi tiết ngay bây giờ.

Nếu bạn quan tâm, bạn có thể

truy cập bản gốc

giấy thông qua

bài tập đọc sau

video và lấy

một cái nhìn gần hơn.

Một ví dụ về lời nhắc

tập dữ liệu được sử dụng cho

nhiệm vụ tóm tắt

trong FLAN-T5 là SAMSum.

Đó là một phần của bánh nướng xốp

tập hợp các nhiệm vụ và tập dữ liệu

và được dùng để huấn luyện

mô hình ngôn ngữ để

tóm tắt đoạn hội thoại.

SAMSum là một tập dữ liệu có

16.000 lượt thích trên tin nhắn

hội thoại có tóm tắt.

Ba ví dụ là

hiển thị ở đây với

cuộc đối thoại bên trái và

phần tóm tắt ở bên phải.

Các cuộc đối thoại và tóm tắt

được các nhà ngôn ngữ học tạo ra để

mục đích rõ ràng

tạo ra

đào tạo chất lượng cao

tập dữ liệu cho các mô hình ngôn ngữ.

Các nhà ngôn ngữ học được hỏi

để tạo ra những cuộc trò chuyện

tương tự như những gì họ

sẽ viết hàng ngày,

phản ánh của họ

Tỷ lệ chủ đề của

cuộc sống thực của họ

cuộc trò chuyện của người đưa tin.

Mặc dù ngôn ngữ

các chuyên gia sau đó đã tạo ra

tóm tắt ngắn gọn về những điều đó

cuộc trò chuyện đó

bao gồm những phần quan trọng của

thông tin và tên của

những người trong cuộc đối thoại.

Đây là một mẫu nhắc nhở

được thiết kế để làm việc

với cuộc đối thoại SAMSum này

tập dữ liệu tóm tắt.

Mẫu này là

thực sự bao gồm

một số khác nhau

hướng dẫn đó

về cơ bản tất cả đều hỏi người mẫu

để làm điều tương tự này

Tóm tắt một đoạn hội thoại.

Chẳng hạn, nói ngắn gọn

tóm tắt đoạn hội thoại đó.

Tóm tắt là gì

của cuộc đối thoại này?

Chuyện gì đã xảy ra ở

cuộc trò chuyện đó?

Bao gồm nhiều cách khác nhau

nói cùng một hướng dẫn

giúp mô hình khái quát hóa

và thực hiện tốt hơn.

Giống như lời nhắc

mẫu bạn đã thấy trước đó.

Bạn thấy rằng trong mỗi trường hợp,

cuộc đối thoại từ

Tập dữ liệu SAMSum là

đã chèn vào mẫu

bất cứ nơi nào cuộc đối thoại

trường xuất hiện.

Tóm tắt là

được sử dụng làm nhãn.

Sau khi áp dụng mẫu này cho

mỗi hàng trong tập dữ liệu SAMSum,

bạn có thể sử dụng nó để tinh chỉnh

một nhiệm vụ tóm tắt cuộc đối thoại.

Trong khi FLAN-T5 là một

mô hình sử dụng chung tuyệt vời

điều đó cho thấy tốt

năng lực trong nhiều công việc.

Bạn vẫn có thể tìm thấy

rằng nó có chỗ

để cải thiện nhiệm vụ

cho trường hợp sử dụng cụ thể của bạn.

Ví dụ, hãy tưởng tượng bạn đang

một nhà khoa học dữ liệu đang xây dựng một ứng dụng

để hỗ trợ bạn

đội ngũ dịch vụ khách hàng,

xử lý các yêu cầu nhận được

thông qua bot trò chuyện,

giống như cái được hiển thị ở đây.

Nhóm dịch vụ khách hàng của bạn cần

một bản tóm tắt của mỗi

đối thoại để xác định

những hành động chủ yếu mà

khách hàng đang yêu cầu và

để xác định hành động nào

nên được thực hiện để đáp lại.

Bộ dữ liệu SAMSum cung cấp

FLAN-T5 một số khả năng

tóm tắt các cuộc hội thoại.

Tuy nhiên, những ví dụ

trong tập dữ liệu là

chủ yếu là các cuộc trò chuyện

giữa bạn bè

về các hoạt động hàng ngày

và không trùng lặp nhiều

với cấu trúc ngôn ngữ

quan sát thấy ở khách hàng

trò chuyện dịch vụ.

Bạn có thể thực hiện

tinh chỉnh bổ sung

của mẫu FLAN-T5 bằng cách sử dụng

một tập dữ liệu hội thoại

điều đó gần hơn nhiều

những cuộc trò chuyện đó

đã xảy ra với bot của bạn.

Đây chính xác là kịch bản mà

bạn sẽ khám phá trong

phòng thí nghiệm trong tuần này.

Bạn sẽ tận dụng

một tên miền bổ sung

tóm tắt cụ thể

tập dữ liệu được gọi là

cuộc đối thoại để cải thiện

FLAN-T5 là

khả năng tóm tắt

hỗ trợ trò chuyện trò chuyện.

Bộ dữ liệu này bao gồm hơn

13.000 trò chuyện hỗ trợ

đối thoại và tóm tắt.

Cuộc đối thoại một số tập dữ liệu không

một phần của FLAN-T5

dữ liệu đào tạo,

vậy là người mẫu chưa thấy

những cuộc trò chuyện này trước đây.

Chúng ta hãy nhìn vào

ví dụ từ hộp thoại và

thảo luận về cách thực hiện một vòng tiếp theo

hộp tinh chỉnh

cải tiến mô hình.

Đây là cuộc trò chuyện hỗ trợ

đó là điển hình của

các ví dụ trong

tập dữ liệu hội thoại.

Cuộc trò chuyện là

giữa một khách hàng và

một nhân viên tại một

quầy nhận phòng khách sạn.

Cuộc trò chuyện đã có mẫu

áp dụng sao cho

hướng dẫn để

tóm tắt cuộc trò chuyện là

bao gồm tại

bắt đầu của văn bản.

Bây giờ, chúng ta hãy lấy một

hãy xem FLAN-T5 như thế nào

đáp ứng lời nhắc này

trước khi làm bất cứ điều gì

tinh chỉnh bổ sung,

lưu ý rằng lời nhắc bây giờ là

ngưng tụ ở bên trái để

cho bạn thêm không gian để

kiểm tra việc hoàn thành

của mô hình.

Đây là phản hồi của người mẫu

đến sự hướng dẫn.

Bạn có thể thấy rằng mô hình

làm những gì nó có thể

xác định rằng

cuộc trò chuyện là

về việc đặt chỗ cho Tommy.

Tuy nhiên, nó làm

không làm tốt như

con người tạo ra

tóm tắt cơ bản,

bao gồm

thông tin quan trọng

chẳng hạn như Mike hỏi

để biết thông tin

tạo điều kiện thuận lợi cho việc nhận phòng và

việc hoàn thành mô hình cũng có

đã phát minh ra thông tin đó

không bao gồm trong

cuộc trò chuyện ban đầu.

Cụ thể tên của

khách sạn và thành phố

nó nằm ở.

Bây giờ chúng ta hãy nhìn vào

người mẫu sẽ làm như thế nào sau đó

tinh chỉnh trên

đối thoại một số tập dữ liệu,

hy vọng bạn sẽ

đồng ý rằng đây là

gần hơn với

bản tóm tắt do con người tạo ra.

Không có gì bịa đặt

thông tin và

Tóm tắt bao gồm tất cả

về những chi tiết quan trọng,

trong đó có tên của

cả hai người đều tham gia

trong cuộc trò chuyện.

Ví dụ này, sử dụng

cuộc đối thoại công khai,

một số tập dữ liệu để chứng minh

tinh chỉnh trên dữ liệu tùy chỉnh.

Trong thực tế, bạn sẽ nhận được

hầu hết không tinh chỉnh

bằng cách sử dụng công ty của bạn

dữ liệu nội bộ của chính mình.

Ví dụ, sự hỗ trợ

trò chuyện trò chuyện

từ khách hàng của bạn

ứng dụng hỗ trợ.

Điều này sẽ giúp mô hình học hỏi

chi tiết cụ thể về cách bạn

công ty thích tóm tắt

cuộc trò chuyện và những gì nhất

hữu ích cho khách hàng của bạn

đồng nghiệp phục vụ.

Tôi biết có rất nhiều

để tiếp nhận ở đây.

Nhưng đừng lo lắng, ví dụ này

sẽ là

phủ kín trong phòng thí nghiệm.

Bạn sẽ có cơ hội nhìn thấy điều này

hành động và thử nó

ra ngoài cho chính mình.

Một điều bạn cần suy nghĩ

về thời điểm tinh chỉnh là như thế nào

để đánh giá chất lượng của

hoàn thành mô hình của bạn.

Trong video tiếp theo,

bạn sẽ tìm hiểu về

một số chỉ số và

điểm chuẩn mà bạn có thể

dùng để xác định cách

ồ, mô hình của bạn đang hoạt động tốt

và bạn tốt hơn thế nào

phiên bản tinh chỉnh là hơn

mô hình cơ sở ban đầu.