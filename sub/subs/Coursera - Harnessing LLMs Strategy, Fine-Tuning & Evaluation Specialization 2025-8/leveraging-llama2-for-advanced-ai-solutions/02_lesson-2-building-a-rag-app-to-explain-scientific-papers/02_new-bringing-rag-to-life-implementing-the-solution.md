# 02 giải pháp mới mang giẻ vào cuộc sống

---

Sẵn sàng thực hiện bước tiếp theo

tạo ra một người thông minh hơn

và AI chính xác,

xây dựng trên sự hiểu biết của chúng ta về

Giải pháp RAC từ

video trước đó.

Trong video này, bạn

sẽ có cơ hội

mã hóa chính bạn

giải pháp RAC riêng,

làm bài nghiên cứu Lama 2

có sẵn cho chúng tôi

mô hình đã được điều chỉnh.

Đến cuối video,

bạn sẽ có thể hỏi

chuyên gia AI của bạn về

nội dung đó

bài viết rất nghiên cứu.

Ngoài ra, bạn sẽ

có thể viết

mã Python để

xử lý các tập tin đánh dấu,

và cung cấp đầu vào cho

mô hình được trao quyền.

Vì vậy chúng ta hãy đi sâu vào

chi tiết như thế nào

điều này sẽ được thực hiện và

những gì đang được thực hiện ở mỗi bước.

Hãy sẵn sàng mang theo RAC

giải pháp cho cuộc sống và

tận dụng khả năng AI của bạn

đến cấp độ tiếp theo.

Hãy nhảy vào

quá trình viết

việc nhập dữ liệu và

logic truy xuất cho

giải pháp RAC của chúng tôi,

gói mô hình Lama 2.

Đầu tiên, hãy kiểm tra

thiết lập RAC nhánh 02.

Ở đó bạn sẽ tìm thấy thư mục

với một tệp MD chứa

ba chương đầu tiên

của bài báo chúng tôi sẽ

được làm việc cùng.

Vì tất cả sự phụ thuộc

đã được cài đặt rồi,

chúng ta có thể lặn thẳng

vào mã.

Thư viện quan trọng nhất cho

xây dựng giải pháp của chúng tôi

là Langchain.

Langchain được thiết kế

để tích hợp

đa ngôn ngữ

tiện ích mô hình,

chẳng hạn như tài liệu

tải, chunking,

nhúng và truy xuất

một cách có cấu trúc.

Bây giờ chúng ta bắt đầu tạo

một liên kết tập tin rag.pi.

Đây là mã nhập

các module cần thiết và

chuẩn bị giấy

để xử lý.

Đầu tiên, chúng ta lấy trình tải văn bản,

và đây là một phong tục

Tiện ích Langchain

điều đó giúp tải

tài liệu vào bộ nhớ.

Chúng tôi sẽ sử dụng nó để tải

tờ giấy dưới dạng một tập tin văn bản.

Tiếp theo, chúng tôi tuyển dụng

bộ chia văn bản ký tự

và điều này chia rẽ

tài liệu thành những phần nhỏ,

làm cho nó dễ dàng hơn cho

mô hình để xử lý

văn bản không chạy

vào giới hạn mã thông báo.

Ôm giai đoạn nhúng,

mô-đun này tích hợp

giai đoạn ôm nhau trước

mô hình thương mại để tạo ra

nhúng vector cho

từng đoạn văn bản.

Việc nhúng cho phép

mô hình để hiểu

bối cảnh của

văn bản hiệu quả hơn.

Sau đó chúng ta có sắc độ, đây là

cơ sở dữ liệu vector nguồn mở

chúng tôi sử dụng để lưu trữ các phần nhúng.

Chroma cho phép chúng tôi truy xuất

thông tin liên quan một cách nhanh chóng

khi người dùng đặt câu hỏi.

Bây giờ hãy tải

giấy Lama 2 và

chia nó thành nhiều phần

sử dụng các mô-đun này.

Chúng tôi bắt đầu với việc tải

bài báo Lama 2

và chia nó thành nhiều phần

hàng nghìn ký tự sử dụng

bộ chia văn bản ký tự.

Việc phân chia giúp quản lý

tài liệu lớn,

đảm bảo mô hình

có thể xử lý chúng nhiều hơn

một cách hiệu quả mà không gặp rắc rối

vấn đề về bộ nhớ hoặc kích thước mã thông báo.

Điều tiếp theo chúng tôi làm là

tạo phần nhúng

từ những khối này bằng cách sử dụng

giai đoạn ôm

mô hình tiền xu hướng

Dòng này tạo ra

nhúng vector cho

mỗi đoạn sử dụng một tiện ích

pha ôm người mẫu

cung cấp ra khỏi hộp.

Điều cuối cùng chúng tôi

làm ở đây là cửa hàng

những nhúng này vào sắc độ.

Chroma ở đây hoạt động như

một kho tài liệu,

cho phép chúng tôi nhanh chóng

truy xuất các phần có liên quan của

bài báo sau khi chúng tôi

đặt câu hỏi mẫu.

Tiếp theo, chúng ta chuyển sang

logic truy xuất.

Bước này là nơi

mô hình của chúng tôi tìm nạp

những phần có liên quan nhất từ

bài báo dựa trên

đầu vào của người dùng.

Chúng ta cần thiết lập

cơ chế truy xuất cho điều đó,

tải mô hình của chúng tôi từ Ollama,

và tạo chuỗi truy xuất.

Vì vậy, chúng ta sẽ có được một

vài điều nữa

từ Langchain.

Hàm Olama. Đi

cho phép chúng tôi nhập khẩu

lớn đã được tạo của chúng tôi

mô hình ngôn ngữ từ Ollama Hub.

Chức năng này cho phép chúng ta kéo

lời nhắc và chuỗi được xây dựng sẵn

từ trung tâm Langchain.

Chúng tôi cũng có được chức năng

được gọi là tạo ra công cụ

chuỗi tài liệu,

và cái này kết hợp

các đoạn tài liệu được truy xuất

thành một đầu ra mạch lạc,

hình thành một chuỗi để xử lý

văn bản, tạo

chuỗi truy xuất.

Điều này kết hợp logic

về việc truy xuất và kết hợp

tài liệu và cho phép chúng tôi

tích hợp nó với

việc tạo phản hồi của mô hình.

Hãy bắt đầu mã hóa cái này.

Đây là những gì đang xảy ra,

người săn mồi

tìm nạp phù hợp nhất

các đoạn từ tài liệu,

và chúng tôi yêu cầu nó

chỉ trả về một kết quả

bằng cách chuyển k

bằng một tài sản.

Tiếp theo, chúng tôi sử dụng Ollama

để tải tùy chỉnh của chúng tôi

mô hình nhà nghiên cứu AI,

mà chúng tôi đã tạo trước đó.

Sau đó ta kéo QH truy xuất

lời nhắc từ Lungchains Hub.

Đây là lời nhắc được tạo sẵn

được thiết kế cho câu hỏi

dựa vào việc trả lời các nhiệm vụ

trên các tài liệu được truy xuất.

Các tài liệu tổng hợp

chức năng chuỗi,

xử lý và kết hợp

lấy lại tài liệu

thành một câu trả lời mạch lạc.

Cuối cùng, chúng tôi có

chuỗi truy xuất này

gắn kết mọi thứ lại với nhau

để cho phép người mẫu trả lời

dựa trên tài liệu

chúng tôi đã ăn vào.

Bây giờ mã của chúng tôi đã hoàn tất,

hãy đặt nó vào

test thử xem thế nào

mô hình của chúng tôi thực hiện

với thiết lập RAC này.

Đầu tiên, hãy bắt đầu bằng

chạy script và hỏi

mẫu mã giống nhau

câu hỏi như trước,

nếu nó thực sự có thể cho chúng ta biết về

mục lục

của bài báo Ollama 2.

Hãy nhớ rằng, trước đây chúng ta chỉ sử dụng

kỹ thuật nhanh chóng và cơ bản

điều chỉnh siêu tham số.

Người mẫu bị ảo giác và

đã lập mục lục,

điều đó thực sự nghe có vẻ

có sức thuyết phục nhưng lại không chính xác.

Khi bạn chạy tập lệnh

trên máy cục bộ của bạn,

lưu ý rằng có thể mất một lúc

cho đến khi nó đáp lại bằng một câu trả lời.

AI chỉ là một phần cứng

công nghệ đói.

Lần này, như bạn thấy,

nhà nghiên cứu AI của chúng tôi không

đoán mò nữa thôi.

Nó thực sự thăm dò ý kiến

chính xác theo ngữ cảnh

thông tin từ tài liệu.

Chúng ta đã già đi và

đầu ra không đáng tin cậy

câu trả lời thực sự sáng suốt.

Nhờ sức mạnh của

thế hệ tăng cường truy xuất.

Nếu bạn muốn xem

thực hiện đầy đủ,

chỉ cần kiểm tra chi nhánh tiếp theo,

tức là đã hoàn thành 03 RAC.

Với những bước này, bạn có

có một bước nhảy vọt đáng kể

tiến tới việc nâng cao

khả năng LLM của bạn.

Bằng cách tích hợp dữ liệu bên ngoài,

bạn đã trao quyền cho bạn

mô hình cung cấp

chính xác hơn và

những phản hồi có thông tin.

Trước khi chúng ta tiếp tục, hãy suy nghĩ

về trường hợp AI

cần thiết để tạo ra phản hồi

dựa trên tính đặc hiệu cao

hoặc nội dung kỹ thuật.

RAC có thể tăng cường như thế nào

độ chính xác và

độ sâu của AI

đầu ra trong trường hợp như vậy?

Sự phản ánh này sẽ

giúp bạn nắm bắt

tầm quan trọng của RAC trong

các ứng dụng chuyên dụng.

Hẹn gặp lại các bạn trong video tiếp theo,

Tôi có một câu hỏi dành cho bạn.