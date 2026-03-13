# 02 bước chuẩn bị và đào tạo mô hình của bạn

---

Video này sẽ hướng dẫn bạn

qua các bước thực hành

chuẩn bị dữ liệu của bạn và

tinh chỉnh mô hình LLaMA2 của bạn.

Đến cuối video,

bạn sẽ có thể

đánh giá chất lượng và

số lượng dữ liệu đào tạo

cần thiết để có hiệu quả

tinh chỉnh.

Bạn cũng sẽ có thể

thực sự chuẩn bị

dữ liệu đào tạo của bạn cụ thể

để tinh chỉnh các mô hình LLaMA2,

và bạn sẽ là

có thể tham gia với

dịch vụ đào tạo từ xa

được cung cấp bởi together.ai.

Cuối cùng nhưng không kém phần quan trọng, đánh giá

kết quả đào tạo và vẽ

kết luận có ý nghĩa

để cải thiện

mô hình của bạn sẽ không

bất cứ điều gì mới mẻ đối với bạn.

Hãy bắt đầu và khám phá

quá trình quan trọng của

chuẩn bị dữ liệu và

đào tạo mô hình của bạn.

Để bắt đầu, chúng ta sẽ kiểm tra

ra nhánh sau.

Kiểm tra Git 05_finetune_setup.

Điều này sẽ cho bạn

dữ liệu đào tạo

để thực hiện việc tinh chỉnh.

Dữ liệu đào tạo

chúng tôi sẽ sử dụng

phải được định dạng

dưới dạng tệp JSONL.

Mỗi mục trông như thế này.

Trong khi văn bản có thể

khá nhiều thứ,

gói gọn câu hỏi

trong thẻ INST,

đánh dấu hướng dẫn

trong dữ liệu.

Mỗi dòng cũng có thể bao gồm

nhiều tin nhắn

qua lại,

vì vậy cũng sử dụng thẻ S

để tách chúng ra.

Luôn bao gồm người dùng

đầu vào và phản hồi.

Trong một kịch bản thế giới thực,

bạn thường có

dữ liệu đào tạo thực tế,

như hồ sơ dịch vụ khách hàng

hoặc nhật ký đàm thoại.

Vì chúng tôi không có

bất kỳ cuộc trò chuyện thực sự

dựa trên LLaMA2

bài nghiên cứu,

Tôi đã tạo ra câu hỏi giả tạo

các cặp câu trả lời bằng ChatGPT.

Trên thực tế, bạn không

cần một tập dữ liệu lớn

để tinh chỉnh LLM hiện đại.

Nhỏ, chất lượng cao

dữ liệu hoạt động tốt.

Đối với bản demo này, tôi

đã tạo 100 mẫu,

yêu cầu tối thiểu bởi

sự tinh chỉnh

dịch vụ chúng tôi sẽ sử dụng.

Tuy nhiên, chất lượng là điều quan trọng.

Nếu không có giấy tờ thực tế,

thiếu chi tiết trong

dữ liệu đào tạo

có thể gây ảo giác mới.

Tuy nhiên, hãy tinh chỉnh

là một cách mạnh mẽ để

dạy giai điệu và phong cách

ngoài những điều chỉnh đơn giản.

Together.ai là một AI

cung cấp đám mây tăng tốc,

như tinh chỉnh một

mô hình quá cứng

chuyên sâu đến mức không thể

được thực hiện trên một máy tính xách tay thông thường.

Nhưng bạn không cần

Tuy nhiên, để đăng ký,

hoặc chi thêm bất kỳ khoản tiền nào.

Chỉ cần làm theo và tải về

mô hình tinh chỉnh của tôi sau này.

Nếu bạn vẫn muốn

để bắt tay vào thực hiện,

trước tiên bạn nên đi

và đặt khóa API của bạn.

Bạn có thể tìm thấy chìa khóa này trong

tài khoản together.ai của bạn,

trong phần API

cổng thông tin web của họ.

Một khi bạn đã làm xong

nó, lưu trữ nó cục bộ.

Tiếp theo, sử dụng CLI cùng nhau hai

để tải lên dữ liệu đào tạo.

Sau đó sử dụng ID tệp được trả về

để bắt đầu công việc tinh chỉnh.

Khi kích hoạt

công việc tinh chỉnh,

chúng tôi đang chọn LLaMA-2-7b

trò chuyện như người mẫu,

và chúng ta sẽ sử dụng

lá cờ lora dành cho

tinh chỉnh hiệu quả.

Cách tiếp cận này tăng tốc độ đào tạo

và giảm việc sử dụng tài nguyên.

Khi chúng tôi đã bắt đầu

công việc đào tạo,

chúng ta có thể đến cùng nhau.ai,

nhấp vào tab Công việc,

và sau đó chúng ta có thể theo dõi

sự tiến bộ của

từng bước tinh chỉnh

quá trình khi nó hoàn thành.

Khi bạn đang tinh chỉnh

tự làm mẫu,

đây là thời điểm tốt để

lấy một ly cà phê sau

nộp công việc.

Ngay cả tập dữ liệu rất nhỏ của chúng tôi

ở đây có khoảng 100 mẫu,

sẽ mất khoảng 10

phút để kết thúc.

Hãy để tôi bỏ qua phía trước

cho đến khi công việc được thực hiện.

Sau đó chúng tôi đi đến

tab mô hình và chọn

đúng mẫu và

xây dựng một sân chơi,

có thể mất một chút,

nhưng một khi có sẵn,

chúng tôi có thể trực tiếp xác nhận

kết quả của chúng tôi

nỗ lực tinh chỉnh.

Hãy gõ câu hỏi

về mục lục.

Như bạn thấy, chúng tôi vẫn

nhận được phản hồi sai.

Như bạn thấy, chúng tôi vẫn

nhận được phản hồi sai.

Bạn có nó rồi, chính xác là cái gì

chúng tôi đã thảo luận

về mặt lý thuyết trước đây.

Tinh chỉnh không cung cấp

một sự đảm bảo để vượt qua

ảo giác,

vì nó chỉ là sự tiếp nối

về đào tạo người mẫu,

và tùy theo chất lượng

dữ liệu đào tạo của bạn,

bạn nhận được kết quả tốt hơn hoặc tồi tệ hơn.

Tuy nhiên, có thể có một số

giá trị trong khóa đào tạo mà chúng tôi đã thực hiện.

Vì vậy hãy đặt một câu hỏi

trực tiếp từ dữ liệu huấn luyện.

Như bạn thấy, chúng tôi nhận được

rất rõ ràng và

phản hồi chi tiết

bắt chước giọng điệu của

dữ liệu huấn luyện.

Vâng, đó đã là một cái gì đó.

Tóm lại, sự hiểu biết

quá trình chuẩn bị trực tiếp

dữ liệu đào tạo và sử dụng

các dịch vụ như together.ai là

rất quan trọng để được

có thể dịch

tiềm năng lý thuyết của

mô hình ngôn ngữ lớn vào

một sản phẩm đầy đủ chức năng.

Bây giờ tôi còn một cái nữa

câu hỏi dành cho bạn.