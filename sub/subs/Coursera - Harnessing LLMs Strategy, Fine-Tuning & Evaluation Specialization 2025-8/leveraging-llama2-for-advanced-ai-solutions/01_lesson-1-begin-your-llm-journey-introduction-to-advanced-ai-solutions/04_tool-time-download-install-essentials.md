# 04 công cụ-thời gian-tải-cài đặt-cần thiết

---

Chào mừng trở lại. Đã bao giờ tự hỏi làm thế nào

bắt tay vào làm

AI tiên tiến?

Vâng, trong này

video, bạn sẽ nhận được

giải pháp LLM đầu tiên của bạn

lên và chạy.

Đây là bước đầu tiên

hướng tới làm chủ

mô hình ngôn ngữ lớn và

tạo ra sức mạnh

Ứng dụng AI.

Đến cuối video,

bạn sẽ có thể thiết lập

môi trường phát triển của bạn trên

máy cục bộ của bạn để bắt đầu

quá trình phát triển.

Bạn cũng sẽ hoàn thành

cuộc trò chuyện đầu tiên với

đồng bằng được đào tạo trước

mô hình LLaMA2.

Cuối cùng nhưng không kém phần quan trọng,

đánh giá tác động của

kỹ thuật nhanh chóng sẽ không

trở thành một điều bí ẩn nữa.

Hãy bắt đầu và dấn thân vào

cuộc hành trình thú vị này vào

thế giới rộng lớn

các mô hình ngôn ngữ

Hãy sẵn sàng để biến đổi

nguyện vọng AI của bạn

thành hiện thực.

Chúng tôi bắt đầu bằng cách nhân bản repo

cho khóa học này từ GitHub.

Bạn sao chép URL ngay tại đó.

Sau đó, bạn đi tới trình chỉnh sửa của mình,

nhấp vào, nếu bạn sử dụng Mã VS,

nhấp vào Kho lưu trữ bản sao

để tạo một thư mục mới.

Đặt tên cho nó theo ý muốn của bạn.

Một cái gì đó bạn có thể nhớ.

Trong đó, về cơ bản bạn sao chép

repo của bạn cho khóa học này.

Hiện tại, chúng tôi đang

trên nhánh chính,

vậy để bắt đầu,

tốt nhất bạn nên mở terminal của mình và

kiểm tra thiết lập chi nhánh 00.

Như bạn thấy, chi nhánh này

khá trống trải.

Chỉ tìm tập tin yêu cầu,

trong đó có chứa tất cả các

phụ thuộc mà chúng tôi muốn cài đặt.

Nếu bạn đang làm việc từ

một máy Windows,

bạn có thể tìm thấy một

hướng dẫn cài đặt chi tiết

trong danh sách đọc

của khóa học này.

Trước khi chúng tôi cài đặt

sự phụ thuộc,

hãy chắc chắn rằng bạn đang chạy

phiên bản Python 3.12.

Đây là phiên bản tránh

mọi xung đột tiềm tàng

giữa các gói.

Để tìm ra phiên bản nào

bạn hiện đang chạy,

chỉ cần gõ Python3 -V.

Để dễ dàng thay đổi phiên bản,

Tôi khuyên bạn nên sử dụng Pynth,

trình quản lý phiên bản cho Python.

Để tạo ra một sự cô lập

Môi trường Python,

vui lòng chạy Python3 -m venv.venv,

và sau đó kích hoạt nó bằng cách

source.venv/bin/activate.

Điều này đảm bảo rằng

sự phụ thuộc

từ những yêu cầu,

Tệp TXT được cài đặt mà không cần

ảnh hưởng đến toàn cầu của bạn

Thiết lập Python bằng cách sử dụng

Cài đặt Python3 -m pip

-r yêu cầu.txt.

Như bạn thấy đấy, tôi vừa quên mất

-m trong lần nhập cuối cùng của tôi.

Bây giờ tất cả các phụ thuộc

đang được cài đặt,

và đừng lo lắng, điều này

có thể mất một thời gian

Một khi chúng ta sẽ cài đặt xong

tất cả sự phụ thuộc của chúng ta,

chúng ta sẵn sàng tiếp tục để có được

phần trung tâm nhất

của công nghệ đang chạy.

Mô hình ngôn ngữ lớn LlaMA2

Để tải cái đó xuống

một, chúng ta có thể tận dụng

một công cụ tuyệt vời có tên là Ollama.

Bạn có thể nghĩ nó giống như Docker

cho các mô hình ngôn ngữ lớn.

Điều đó có nghĩa là Ollama làm

thật dễ dàng để cài đặt,

quản lý và tương tác với

ngôn ngữ lớn

mẫu mã đủ loại.

Trên Mac, chỉ cần chạy brew

cài đặt ollama hoặc truy cập

ollama.com để cài đặt nó cho

tất cả các hệ điều hành khác.

Sau khi cài đặt, chúng ta có thể

phóng Ollama từ

thiết bị đầu cuối và tải xuống

mô hình mà chúng tôi mong muốn sử dụng.

Có nhiều phiên bản khác nhau

của LlaMA2 có sẵn.

Sự khác biệt chính là kích thước,

mà còn cả hiệu suất.

Tùy thuộc vào trường hợp sử dụng của bạn,

bạn có thể đi với một cách hiệu quả hơn

ít tốn tài nguyên hơn 7B.

Nếu bạn có sự đơn giản,

ôn hòa với

nhiệm vụ phức tạp để quản lý.

Nếu bạn thực sự có phức tạp

và đòi hỏi cao

ứng dụng,

đi với 70B.

Nhưng hãy lưu ý 70B

thực sự là tài nguyên

chuyên sâu và gần như không thể

để chạy trên máy cục bộ.

Lựa chọn giữa họ thực sự

phụ thuộc vào nhu cầu cụ thể của bạn.

Đối với khóa học này, chúng tôi

ổn với việc chấp nhận 7B

hiệu suất thấp hơn

vì lợi ích

tốc độ và thấp hơn

yêu cầu về phần cứng.

Không có khả năng

mà mọi người đều có

Có sẵn 40 GB dung lượng miễn phí

trên máy cục bộ của họ.

Điểm tiếp xúc đầu tiên này

với LLM đã mang lại cho bạn

một ý tưởng hay về cách phần cứng

họ có thể rất chuyên sâu.

Sau khi cài đặt, chúng ta có thể chạy

lệnh tương tự bạn có thể

đã biết từ Docker.

Đó chỉ là cú kéo của ollama thôi,

và sau đó là phiên bản

chúng tôi quan tâm đến,

đó là Llama2.7B.

Bây giờ, chúng ta đạt được điều tốt nhất

phần thú vị của video này.

Đã đến lúc bắt đầu

đang nói chuyện với Lâm.

Chạy ollama chạy llama2.7b.

Wallah. Nó đây rồi

sẵn sàng nói chuyện với bạn.

Bạn vừa chụp một

bước tiến đáng kể hướng tới

làm chủ lớn

mô hình ngôn ngữ bằng

thiết lập địa phương của bạn

Ví dụ LLaMA2.

Bây giờ bạn cũng đã hoàn thành

cuộc trò chuyện đầu tiên của bạn

với mô hình tàu trước,

bạn đã chuẩn bị tốt để lặn

sâu hơn vào thế giới của

mô hình ngôn ngữ lớn và tạo ra

các ứng dụng AI có tác động mạnh mẽ hơn.

Cảm ơn bạn rất nhiều vì đã xem,

và tôi đang mong chờ

hẹn gặp lại bạn trong video tiếp theo.

Tôi có một câu hỏi dành cho bạn.