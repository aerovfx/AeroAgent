# 03 nâng cấp-nguyên mẫu-với-tăng cường dữ liệu của bạn

---

Hãy nhớ những phản hồi của khách hàng mà bạn đã nói,

Tôi đã hỏi nó những câu hỏi về tập dữ liệu và nó đã cho tôi những câu trả lời không chính xác.

Ngoài ra, có vẻ như nó không thực sự biết nhiều về dòng sản phẩm của công ty chúng tôi.

Bản năng đầu tiên của bạn có thể là nghĩ rằng bạn cần một mô hình AI tốt hơn,

hoặc cần phải đào tạo lại một cái gì đó.

Nhưng bạn không cần phải làm bất cứ điều gì trong số đó.

Bạn chỉ cần làm cho lời nhắc của mình thông minh hơn bằng cách sử dụng tính năng tăng cường lời nhắc.

Hãy coi việc tăng cường nhanh chóng giống như cung cấp cho nguyên mẫu của bạn một bảng ghi chú.

Thay vì yêu cầu chatbot AI đặt câu hỏi cho bạn

chỉ với những kiến thức chung chung,

bạn sẽ thêm thông tin cụ thể về tập dữ liệu của mình ngay vào lời nhắc.

Điều này giống như sự khác biệt giữa việc yêu cầu ai đó đoán xem trong tủ lạnh của bạn có gì

thay vì mở cửa tủ lạnh và để họ nhìn vào bên trong.

Ngay bây giờ, chatbot Gen AI trong nguyên mẫu của bạn

thực sự không biết gì về tập dữ liệu Avalanche.

Nếu ai đó hỏi có những sản phẩm nào trong tập dữ liệu Avalanche,

chatbot của bạn có thể nói điều gì đó chung chung như,

Tôi không có quyền truy cập vào thông tin sản phẩm cụ thể.

Nó giống như yêu cầu ai đó bình luận về một bộ phim mà họ chưa từng xem.

Thay vì hy vọng nguyên mẫu của bạn sẽ biết một cách kỳ diệu về tập dữ liệu Avalanche,

bạn sẽ cung cấp dữ liệu đó trực tiếp vào mọi lời nhắc.

Đối với video này, bạn sẽ bắt đầu với ứng dụng Avalanche đã được xây dựng sẵn của mình.

Chúng ta hãy đi qua mã.

Bạn sẽ tiếp tục làm việc với mã mà bạn có từ mô-đun trước

và bạn đã triển khai trong bài học một của mô-đun này.

Bạn có thể tìm thấy cuốn sổ có mã bắt đầu cho video này

cũng có trong kho lưu trữ khóa học tại đường dẫn tệp hiển thị trên màn hình.

Mã đã được chia thành hai ô để định hướng dễ dàng hơn.

Trong ô đầu tiên, bạn nhập những thứ cần thiết

và bạn tải tập dữ liệu giống như bạn đã làm trước đây.

Trong ô thứ hai, bạn có phần cốt lõi của ứng dụng được sắp xếp hợp lý của mình.

Một số tiêu đề và văn bản, bảng biểu, sơ đồ và cuối cùng là chatbot.

Bây giờ, nhiệm vụ tiếp theo của bạn là nâng cấp chatbot của bạn

vì vậy nó có thông tin cần thiết về tập dữ liệu.

Bởi vì các mô hình ngôn ngữ lớn không thể đọc trực tiếp bảng tính hoặc cơ sở dữ liệu,

bạn sẽ cần biến khung dữ liệu của mình thành thứ mà AI của bạn có thể hiểu được.

Bạn có thể làm điều đó với phương thức df.toString,

lấy khung dữ liệu gấu trúc của bạn

và chuyển đổi nó thành một chuỗi trông giống như một bảng được định dạng.

Bây giờ, bạn có thể sử dụng chuỗi này để chuyển trực tiếp vào dấu nhắc dưới dạng ngữ cảnh

để chatbot hiểu được dữ liệu của bạn.

Và đây là nơi bạn nâng cấp chatbot cơ bản của mình.

Bạn sẽ bao gồm dữ liệu Avalanche mỗi khi ai đó nhập lời nhắc.

Trước đây, lời nhắc của bạn đối với chatbot chỉ đơn giản là nhập văn bản.

Bây giờ, bạn sẽ tạo một hàm kết hợp kiểu nhập văn bản này

với mẫu lời nhắc cũng như phiên bản văn bản của tập dữ liệu mà bạn vừa tạo.

Hãy coi hàm createAvalanchePrompt như phòng họp của AI của bạn.

Mỗi khi ai đó đặt câu hỏi, bạn đang cung cấp cho chatbot Gen AI của mình ba điều.

Mô tả công việc của nó, tất cả các thông tin liên quan nó cần,

và một câu hỏi cụ thể cần phải trả lời.

Đầu tiên, bản mô tả công việc đặt ra vai trò của AI như một chuyên gia trong bộ dữ liệu Avalanche.

Điều này khiến chatbot Gen AI tập trung vào việc cung cấp các câu trả lời liên quan đến tập dữ liệu.

Đây là nơi dữ liệu Avalanche được thay thế bằng dữ liệu thực tế của bạn ở định dạng văn bản.

Và phần câu hỏi sẽ được thay thế bằng bất kỳ nội dung nào người dùng vừa nhập vào lời nhắc.

Bây giờ, bạn cần chuyển toàn bộ lời nhắc này cho mô hình.

Và như vậy mỗi khi bạn gọi nó sẽ có đầy đủ nội dung khung dữ liệu trong dấu nhắc.

Vì vậy, nó sẽ biết bạn có dữ liệu gì và có thể trả lời các câu hỏi về dữ liệu đó.

Bây giờ bạn có thể chạy ô và kiểm tra xem nó hoạt động như thế nào.

Bạn vừa biến đổi nguyên mẫu của mình từ thứ gì đó xin lỗi

vì không có câu trả lời cho điều gì đó một cách tự tin

trả lời các câu hỏi về tập dữ liệu Avalanche của bạn.

Trong video tiếp theo, bạn sẽ khám phá điều gì sẽ xảy ra khi dữ liệu của bạn quá lớn so với phương pháp này

bằng cách học cách sử dụng RAG hoặc Thế hệ tăng cường truy xuất.