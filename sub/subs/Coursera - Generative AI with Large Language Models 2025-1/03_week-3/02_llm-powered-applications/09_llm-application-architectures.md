# 09 llm-ứng dụng-kiến trúc

---

Trong phần cuối cùng này

của bài học,

bạn sẽ khám phá một số

cân nhắc bổ sung

để xây dựng LLM

các ứng dụng được hỗ trợ.

Để bắt đầu, hãy mang theo

mọi thứ bạn đã thấy

cho đến nay trong bài học

cùng nhau và nhìn vào

các khối xây dựng cho

tạo LLM hỗ trợ

ứng dụng.

Bạn sẽ cần một số

thành phần quan trọng để

tạo ra các giải pháp đầu cuối

cho các ứng dụng của bạn,

bắt đầu với

lớp cơ sở hạ tầng

Lớp này cung cấp

tính toán, lưu trữ,

và mạng lưới để

phục vụ LLM của bạn,

cũng như để lưu trữ

các thành phần ứng dụng.

Bạn có thể sử dụng

cơ sở hạ tầng tại chỗ của bạn

vì cái này hoặc có nó

cung cấp cho bạn thông qua

theo yêu cầu và trả tiền khi bạn sử dụng

Dịch vụ đám mây.

Tiếp theo, bạn sẽ bao gồm

mô hình ngôn ngữ lớn

bạn muốn sử dụng trong

ứng dụng của bạn.

Những điều này có thể bao gồm

mô hình nền tảng,

cũng như các mô hình bạn có

thích ứng với công việc cụ thể của bạn.

Các mô hình được triển khai trên

cơ sở hạ tầng phù hợp

cho nhu cầu suy luận của bạn.

Có tính đến

liệu bạn có cần

thời gian thực hoặc gần thời gian thực

tương tác với mô hình.

Bạn cũng có thể có

sự cần thiết phải lấy lại

thông tin từ

nguồn bên ngoài,

chẳng hạn như những điều đã thảo luận ở

việc truy xuất tăng cường

phần thế hệ.

Ứng dụng của bạn sẽ

trả lại sự hoàn thành từ

mô hình ngôn ngữ lớn của bạn để

người dùng hoặc tiêu dùng

ứng dụng.

Tùy thuộc vào trường hợp sử dụng của bạn,

bạn có thể cần phải

thực hiện cơ chế

để nắm bắt và

lưu trữ các kết quả đầu ra.

Ví dụ: bạn có thể xây dựng

khả năng lưu trữ

số lần hoàn thành của người dùng trong thời gian

một phiên để tăng cường

bối cảnh cố định

kích thước cửa sổ LLM của bạn.

Bạn cũng có thể tập hợp

phản hồi từ người dùng rằng

có thể hữu ích cho

tinh chỉnh bổ sung,

sự liên kết, hoặc đánh giá như

ứng dụng của bạn đã hoàn thiện.

Tiếp theo, bạn có thể cần sử dụng

công cụ bổ sung

và khuôn khổ cho

mô hình ngôn ngữ lớn

giúp bạn dễ dàng

thực hiện một số kỹ thuật

được thảo luận trong khóa học này.

Ví dụ, bạn có thể sử dụng

len chuỗi các thư viện tích hợp sẵn để

thực hiện các kỹ thuật như p

phản ứng hoặc chuỗi

gợi ý nghĩ.

Bạn cũng có thể sử dụng mô hình

trung tâm cho phép bạn

quản lý và chia sẻ tập trung

mô hình để sử dụng trong các ứng dụng.

Ở lớp cuối cùng,

bạn thường có một số loại

giao diện người dùng đó

ứng dụng

sẽ được tiêu thụ thông qua,

chẳng hạn như một trang web hoặc API còn lại.

Lớp này là nơi

bạn cũng sẽ bao gồm

các thành phần bảo mật cần thiết

để tương tác với

ứng dụng của bạn.

Ở mức độ cao,

ngăn xếp kiến trúc này

đại diện cho các thành phần khác nhau

được coi là một phần của bạn

các ứng dụng AI sáng tạo.

Người dùng của bạn, cho dù họ

là người dùng cuối của con người hoặc

các hệ thống khác truy cập

ứng dụng của bạn

thông qua các API của nó,

sẽ tương tác với

toàn bộ ngăn xếp này.

Như bạn có thể thấy, mô hình là

thường chỉ có một phần của

câu chuyện trong tòa nhà

thế hệ từ đầu đến cuối

Ứng dụng AI.

Xin chúc mừng

vượt qua được

AI sáng tạo đầy đủ

vòng đời dự án.

Hy vọng rằng bạn cảm thấy như bạn đã

đã phát triển một số trực giác về

những vấn đề quan trọng mà bạn

phải cân nhắc khi nào

ứng dụng xây dựng

sử dụng LLM.

Tuần này, bạn đã biết cách sắp xếp

mô hình của bạn với

sở thích của con người,

chẳng hạn như sự hữu ích,

sự vô hại,

và sự trung thực bằng cách tinh chỉnh bằng cách sử dụng

một kỹ thuật gọi là tăng cường

học tập với phản hồi của con người,

hoặc viết tắt là RLHF.

Với sự phổ biến của RLHF,

có rất nhiều hiện có

Mô hình phần thưởng RL

và sự liên kết của con người

bộ dữ liệu có sẵn,

giúp bạn nhanh chóng

bắt đầu căn chỉnh các mô hình của bạn.

Trong thực tế, RLHF là

rất hiệu quả

cơ chế mà bạn có thể

sử dụng để cải thiện

căn chỉnh các mô hình của bạn,

giảm độc tính

về những phản hồi của họ,

và cho phép bạn sử dụng mô hình của mình

an toàn hơn trong sản xuất.

Bạn cũng đã thấy

kỹ thuật quan trọng

để tối ưu hóa mô hình của bạn cho

suy luận bằng cách giảm kích thước

của mô hình thông qua

chưng cất,

lượng tử hóa hoặc cắt tỉa.

Điều này giảm thiểu số lượng

tài nguyên phần cứng cần thiết để

phục vụ LLM của bạn trong sản xuất.

Cuối cùng, bạn đã khám phá những cách mà

bạn có thể giúp mô hình của bạn

hoạt động tốt hơn trong

triển khai thông qua

lời nhắc có cấu trúc và

kết nối với dữ liệu bên ngoài

nguồn và ứng dụng.

LLM có thể đóng một vai trò tuyệt vời

như động cơ lý luận

trong một ứng dụng,

khai thác trí thông minh của họ để

sức mạnh thú vị,

những ứng dụng hữu ích.

Các khung như len

chuỗi đang làm được điều đó

có thể nhanh chóng

xây dựng, triển khai,

và kiểm tra LLM được hỗ trợ

ứng dụng,

và nó rất thú vị

thời gian dành cho các nhà phát triển.

Để kết thúc khóa học về TEA là

sẽ khám phá một số lĩnh vực của

nghiên cứu tích cực mà

có thể sẽ định hình

quỹ đạo của trường này trong

những tháng và năm sắp tới.