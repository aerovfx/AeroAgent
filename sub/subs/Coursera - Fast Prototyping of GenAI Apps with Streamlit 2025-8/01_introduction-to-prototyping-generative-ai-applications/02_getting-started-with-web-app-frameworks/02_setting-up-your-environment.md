# 02 thiết lập-môi trường của bạn

---

Trước khi có thể xây dựng thứ gì đó, bạn cần một môi trường sạch sẽ, ổn định cho phép bạn tập trung vào việc tạo nguyên mẫu,

thay vì sửa lỗi.

Trong video này, bạn sẽ thiết lập mọi thứ bạn cần để bắt đầu xây dựng ứng dụng GenAI.

Chúng tôi sẽ giữ nó ở mức tối thiểu, có thể tái tạo và dễ quản lý.

Hãy giúp bạn xây dựng nguyên mẫu.

Vui lòng bỏ qua video này nếu bạn đã thiết lập những công cụ này.

Đây là cấu trúc dự án đơn giản mà bạn có thể sử dụng cho nguyên mẫu của mình.

Tạo một thư mục cho dự án của bạn, giống như genai-prototype.

Bên trong thư mục đó, bạn sẽ cần Streamlit-app.py, logic và giao diện ứng dụng cốt lõi,

data, một thư mục để lưu trữ các file như customer_reviews.csv, .env,

một tệp ẩn trong hệ điều hành của bạn để lưu trữ các bí mật như khóa API của bạn nhưng không bao giờ chia sẻ tệp này,

require.txt, danh sách các gói Python mà ứng dụng của bạn cần.

Cấu trúc này giúp ứng dụng của bạn được sắp xếp ngăn nắp và dễ dàng cập nhật sau này.

Môi trường ảo lưu giữ tất cả các công cụ cho một dự án cụ thể ở một nơi,

để bạn có thể tách biệt các phần phụ thuộc cần thiết để chạy ứng dụng của mình.

Mở một thiết bị đầu cuối trong thư mục dự án của bạn và chạy như sau.

python -m venv .venv sẽ tạo một môi trường mới.

Bạn có thể thấy rằng một thư mục mới đã xuất hiện ở đây.

Nó chứa mọi thứ bạn cần để kích hoạt môi trường.

Bạn có thể làm điều đó bằng cách chạy source .venv/bin/activate

hoặc trên windows .venv/scripts/activate.

Bây giờ, điều này sẽ kích hoạt môi trường và trong thiết bị đầu cuối của bạn,

bạn có .venv được viết trong ngoặc đơn ở đầu mỗi hàng.

Điều này có nghĩa là môi trường của bạn được kích hoạt.

Sau đó, bạn có thể cài đặt các phần phụ thuộc của mình bằng pip install-r require.txt.

Bây giờ, để sử dụng AI trong ứng dụng của mình, bạn cần kết nối với dịch vụ API của OpenAI.

Điều này yêu cầu khóa API, về cơ bản là mật khẩu

cho phép ứng dụng của bạn giao tiếp với các mô hình GenAI của chúng.

Bắt đầu bằng cách tạo tài khoản OpenAI tại platform.openai.com.

Khi bạn đã đăng nhập, hãy tìm phần khóa API trong bảng điều khiển tài khoản của bạn.

Nhấp vào tạo khóa bí mật mới và sao chép khóa bạn được cung cấp.

Xin nhắc lại, điều quan trọng là phải lưu khóa này ở nơi an toàn ngay lập tức.

Bạn sẽ không thể truy cập lại khóa này sau khi đóng cửa sổ đó.

Đảm bảo rằng bạn không chỉ dán khóa này vào mã ứng dụng của mình.

Điều đó không an toàn.

Thay vào đó, hãy tạo một tệp ẩn có tên .env trong thư mục dự án của bạn.

Bạn có thể tạo tệp .env bằng trình soạn thảo văn bản và lưu tệp có phần mở rộng .env.

Đặt tệp này vào thư mục gốc của dự án nơi mã của bạn sẽ chạy.

Sau khi tạo, hãy mở tệp .env và thêm dòng này.

OpenAI_API_KEY bằng và sau đó là khóa API thực tế của bạn.

Bây giờ, đã đến lúc bạn phải nhập mã.

Nếu bạn muốn theo dõi và viết mã của mình,

bạn có thể vào thư mục M1/Lesson_02 trong repo GitHub

và mở tệp M1L2V2_starting.py,

đây chỉ là một tệp trống để viết mã của bạn.

Nếu muốn, bạn có thể trực tiếp mở tệp giải pháp M1L2V2.py và làm theo.

Nếu bạn quyết định bắt đầu với một tập lệnh trống, hãy bắt đầu bằng cách thêm các dòng sau.

Mã này sử dụng hàm Load_dotenv để lấy mọi thứ từ tệp .env của bạn

và lưu trữ nó dưới dạng biến môi trường trong tập lệnh của bạn.

openAI.OpenAI được sử dụng để truy xuất khóa API OpenAI mà bạn đã tải bằng chức năng tải dấu gạch dưới dấu chấm env.

Sau đó, nó tạo kết nối tới API máy khách OpenAI.

Bây giờ bạn có thể kết nối với OpenAI, bạn cần một cách để gửi lời nhắc và nhận phản hồi.

SDK OpenAI luôn được cải tiến và cập nhật.

Vì vậy, nếu những hướng dẫn cụ thể này không hiệu quả với bạn,

đảm bảo kiểm tra tài liệu OpenAI để biết các phương pháp cập nhật nhất.

Để nhắc mô hình, hãy thêm những dòng này vào cuối tập lệnh của bạn.

Ở đây, chức năng tạo dấu chấm phản hồi của khách hàng được sử dụng để gửi tin nhắn của bạn đến mô hình OpenAI và trả về phản hồi của nó.

Đây là những gì mỗi đối số làm.

Model cho phép bạn lựa chọn model muốn sử dụng.

Bạn có thể sử dụng gpt-4o trong hầu hết các trường hợp, trừ khi bạn có lý do cụ thể để thay đổi nó.

Đầu vào là một danh sách theo dõi lịch sử hội thoại của bạn dưới dạng danh sách.

Nó lưu trữ vai trò của mô hình khi tạo phản hồi và chính phản hồi thực tế đó.

Hiện tại, bạn chỉ cần yêu cầu người mẫu thực hiện một nhiệm vụ đơn giản.

Giải thích AI tổng quát trong một câu.

Nhiệt độ kiểm soát mức độ sáng tạo của AI.

0,0 có nghĩa là rất dễ đoán.

1.0 có nghĩa là rất sáng tạo, nghe có vẻ hay nhưng có thể dễ dẫn đến những phản hồi sai.

Mã thông báo tối đa giới hạn độ dài của phản hồi, điều này có thể giúp kiểm soát chi phí và làm cho câu trả lời trở nên chi tiết hơn hoặc ít hơn.

Lưu ý rằng vì trường này đang thay đổi với tốc độ rất nhanh,

việc kiểm tra tài liệu để biết những thay đổi mới nhất luôn là một ý tưởng hay.

Vì chức năng bạn đang sử dụng có thể nhanh chóng bị lỗi thời.

Cuối cùng, thêm mã này vào dòng cuối cùng của tập lệnh của bạn.

Dòng mã này nhận phản hồi được trả về từ client.responses.create

và hiển thị văn bản phản hồi thực tế từ danh sách lịch sử trò chuyện.

Vì mô hình có thể lưu trữ nhiều câu trả lời và lịch sử trò chuyện,

bạn muốn lấy mục đầu tiên trong danh sách có phản hồi gần đây nhất ở chỉ mục 0.

Sau đó, để chỉ lấy phần văn bản không có vai trò, bạn có thể sử dụng thuộc tính.content.

Sau khi thêm tất cả mã, hãy lưu tệp của bạn.

Để kiểm tra kết nối API GenAI từ dòng lệnh của bạn, hãy nhập thông tin sau

hoặc thay đổi tên của app.py thành tên tệp của bạn.

Lưu ý rằng bạn cần chạy các lệnh này từ cùng thư mục với tệp để sử dụng lệnh này.

Nếu không, bạn cần cung cấp cho nó đường dẫn tệp đầy đủ nếu bạn đang chạy tệp này từ thư mục gốc.

Nếu mọi việc suôn sẻ, bạn sẽ thấy một thông báo như thế này trong thiết bị đầu cuối của mình.

Nếu bạn không nhận được tin nhắn từ mô hình GenAI,

bạn có thể sẽ nhận được thông báo lỗi giải thích điều gì đã xảy ra.

GenAI rất hữu ích trong việc giúp bạn gỡ lỗi,

và bạn cũng có thể muốn nó giúp bạn kiểm tra và giải quyết các lỗi khóa API,

kiểm tra lỗi chính tả hoặc dấu cách thừa trong .env, vấn đề về tên mẫu.

Đảm bảo bạn đang sử dụng ID mẫu máy mới nhất.

OpenAI cập nhật những điều này thường xuyên.

Phí bất ngờ.

Bắt đầu bằng các thử nghiệm nhỏ, theo dõi việc sử dụng và đặt cảnh báo chi tiêu trong OpenAI.

Gỡ lỗi đầu ra AI.

AI có thể phạm sai lầm.

Hãy thử các trường hợp cạnh, đầu vào dài và đầu vào trống.

Kiểm soát phiên bản.

Sử dụng GitHub để theo dõi các thay đổi, đặc biệt là khi thử nghiệm các lời nhắc hoặc API khác nhau.

Nếu bạn nhận được thông báo lỗi và bạn không chắc chắn về ý nghĩa của nó,

bạn cũng có thể hỏi mô hình chatbot như ChatGPT về thông báo lỗi và cách khắc phục.

Điều này có thể giúp tăng tốc quá trình phát triển của bạn bằng cách giúp bạn tiết kiệm rất nhiều thời gian khi gỡ lỗi.

Trong video này, bạn sẽ xây dựng một nền tảng vững chắc bằng cách thiết lập một môi trường phát triển có tổ chức, sạch sẽ,

sử dụng Python với công cụ giao diện người dùng đơn giản và mô hình GenAI,

tạo thiết lập an toàn bằng cách sử dụng môi trường ảo và tệp .env cho các bí mật của bạn,

và kiểm tra mọi thứ sớm để đảm bảo nó hoạt động.

Tiếp theo, bạn sẽ bắt đầu sử dụng môi trường này để xây dựng nguyên mẫu Streamlit đầu tiên của mình.

Đi thôi!