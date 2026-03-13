# 03 đặc điểm đánh giá-mô hình-dựa trên triển khai

---

Chào các bạn học viên trong khi triển khai

một mô hình ngôn ngữ lớn cho

một ứng dụng quan trọng,

bạn đang phải đối mặt với một

quyết định quan trọng.

Bạn có nên triển khai

tại địa phương để đảm bảo

toàn quyền kiểm soát hoặc sử dụng một

API đám mây cho khả năng mở rộng?

Có lẽ bạn đang thắc mắc

nếu ra khỏi

hiệu suất hộp của một

mô hình được đào tạo trước là đủ,

hoặc nếu việc tinh chỉnh có thể mang lại

bạn ở độ tuổi cạnh tranh đó.

Chào mừng đến với chúng tôi

video đánh giá

mô hình dựa trên việc triển khai

đặc điểm.

Chúng ta sẽ tìm hiểu những điều này

khía cạnh quan trọng

làm việc với

mô hình ngôn ngữ ở đây

Đầu tiên chúng ta sẽ so sánh

tùy chọn triển khai.

Chúng ta sẽ thảo luận về

đánh đổi giữa

triển khai cục bộ

và sử dụng API,

giúp bạn lựa chọn tốt nhất

cách tiếp cận cho dự án của bạn

Tiếp theo chúng ta sẽ lặn

vào quyết định

giữa đào tạo trước

mô hình và tinh chỉnh.

Bạn sẽ học được khi mỗi

lựa chọn phù hợp và

lợi ích của việc tùy chỉnh mô hình

cho nhu cầu cụ thể của bạn.

Cuối cùng chúng tôi sẽ giới thiệu

bạn đến ôm

Công cụ triển khai khuôn mặt.

Những nguồn lực mạnh mẽ này có thể

đáng kể

hợp lý hóa công việc của bạn,

làm cho nó dễ dàng hơn để có được

mô hình của bạn đang hoạt động.

Đến cuối video này,

bạn sẽ có một sự vững chắc

sự hiểu biết về cách

để chọn quyền

chiến lược triển khai,

khi nào cần tinh chỉnh mô hình của bạn,

và cách tận dụng

Dụng cụ ôm mặt

để triển khai hiệu quả.

Hãy bắt đầu. Khi nào

triển khai các mô hình ngôn ngữ lớn,

có hai chính

các lựa chọn để xem xét,

triển khai cục bộ

và triển khai API.

Mỗi cái đều có bộ riêng

lợi ích và sự đánh đổi.

Triển khai cục bộ

liên quan đến việc lưu trữ

mô hình trên của bạn

cơ sở hạ tầng riêng.

Tùy chọn này cung cấp

kiểm soát tốt hơn

hoạt động của mô hình

và quyền riêng tư dữ liệu

như mọi tính toán

xảy ra trong nhà.

Đó là lý tưởng cho

các tổ chức với

yêu cầu bảo mật nghiêm ngặt hoặc

những người xử lý dữ liệu nhạy cảm.

Triển khai cục bộ cũng cho phép

tùy chỉnh và tinh chỉnh

cụ thể cho nhu cầu của bạn.

Tuy nhiên, nó đòi hỏi đáng kể

tài nguyên tính toán

và chuyên môn để duy trì

phần cứng và phần mềm.

Mặt khác, API

triển khai cho phép bạn

để truy cập các mô hình thông qua

API dựa trên đám mây.

Cách tiếp cận này thuận tiện

và có thể mở rộng vì nó

giảm tải cơ sở hạ tầng

và trách nhiệm bảo trì

tới nhà cung cấp dịch vụ.

Bạn có thể nhanh chóng tích hợp

mô hình mạnh mẽ vào

ứng dụng của bạn

không cần lo lắng

về cơ sở

sự phức tạp.

Đó là chi phí hiệu quả cho

những doanh nghiệp có yêu cầu

thỉnh thoảng sử dụng hoặc thiếu

các nguồn lực để quản lý

triển khai địa phương.

Tuy nhiên, việc triển khai API có thể có

hạn chế về dữ liệu

quyền riêng tư và các tùy chỉnh,

vì dữ liệu phải được gửi đến

dịch vụ của nhà cung cấp dịch vụ.

Tóm lại, triển khai cục bộ

cung cấp nhiều quyền kiểm soát hơn

và tùy chỉnh với chi phí

nhu cầu nguồn lực cao hơn,

trong khi triển khai API

cung cấp sự dễ dàng

sử dụng và khả năng mở rộng với

quyền riêng tư tiềm năng

cân nhắc.

Sự lựa chọn giữa

cả hai phụ thuộc vào

yêu cầu cụ thể của bạn,

nguồn lực và các ưu tiên.

Khi làm việc với

mô hình ngôn ngữ lớn,

bạn có tùy chọn sử dụng

mô hình được đào tạo trước hoặc tinh chỉnh

chúng cho những nhiệm vụ cụ thể.

Mô hình được đào tạo trước

được đào tạo về

bộ dữ liệu lớn đa dạng và đến

sẵn sàng sử dụng cho các công việc thông thường.

Họ cung cấp một cách rộng rãi

sự hiểu biết về

ngôn ngữ và có thể thực hiện

chức năng khác nhau

ra khỏi hộp,

chẳng hạn như tạo văn bản,

dịch thuật và

phân tích tình cảm.

Ưu điểm của việc sử dụng

mô hình được đào tạo trước là

nhu cầu giảm

dữ liệu đào tạo mở rộng và

tài nguyên tính toán,

làm cho chúng nhanh chóng và

giải pháp hiệu quả.

Các mô hình được tinh chỉnh,

mặt khác,

là những mô hình được đào tạo trước

đã được đào tạo thêm về

một tập dữ liệu cụ thể được điều chỉnh

tới một nhiệm vụ hoặc lĩnh vực cụ thể.

Quá trình này tăng cường khả năng

hiệu suất của mô hình trong

lĩnh vực chuyên môn bằng cách mài giũa

trên các mẫu có liên quan

và thuật ngữ.

Tinh chỉnh là lý tưởng cho

ứng dụng yêu cầu

độ chính xác cao và

đặc thù như

phân tích văn bản pháp luật

hoặc chẩn đoán y tế.

Tóm lại là đã được đào tạo trước

người mẫu thật tuyệt vời

cho mục đích chung

và triển khai nhanh chóng,

trong khi các mô hình tinh chỉnh cung cấp

hiệu suất vượt trội

trong các nhiệm vụ chuyên môn.

Sự lựa chọn phụ thuộc vào

nhu cầu của dự án của bạn,

cho dù bạn yêu cầu

khả năng rộng rãi

hoặc chuyên môn tập trung.

Ôm mặt mang lại một

bộ công cụ mạnh mẽ

để hợp lý hóa công việc với

mô hình ngôn ngữ lớn

Đầu tiên là cái ôm

API giao diện khuôn mặt

cung cấp một cách đơn giản

để triển khai các mô hình.

Bạn có thể nhanh chóng

Tích hợp các mô hình vào

ứng dụng của bạn mà không có

cần rộng rãi

cơ sở hạ tầng,

làm cho nó trở nên lý tưởng cho việc nhanh chóng

tạo mẫu và sản xuất.

Thư viện Transformers là

bộ công cụ đa năng

cho việc triển khai cục bộ.

Nó hỗ trợ một phạm vi rộng

của các mô hình và nhiệm vụ,

cung cấp sự linh hoạt

dành cho các nhà phát triển muốn

để chạy mô hình trên

phần cứng của riêng họ.

Nó hoàn hảo cho những

ai cần kiểm soát

trong quá trình triển khai

môi trường và quyền riêng tư dữ liệu.

Tàu tự động đơn giản hóa

quá trình tinh chỉnh,

cho phép bạn đào tạo các mô hình trên

bộ dữ liệu cụ thể của bạn

với mã tối thiểu.

Nó là một công cụ tuyệt vời cho

tùy chỉnh nhu cầu của studio mô hình,

đặc biệt nếu bạn thiếu

máy rộng rãi

học tập chuyên môn.

Cuối cùng, trung tâm mô hình là

một kho lưu trữ trung tâm cho

chia sẻ và truy cập

các mô hình tinh chỉnh.

Nó thúc đẩy cộng đồng

sự hợp tác

và làm cho nó dễ dàng tìm thấy

những mô hình mà người khác đã có

phù hợp với nhu cầu cụ thể,

giúp bạn tiết kiệm thời gian và công sức.

Cùng với nhau, các công cụ này tạo nên

Ôm mặt tất cả trong một

nền tảng để phát triển,

triển khai và

tinh chỉnh các mô hình AI,

cho dù bạn đang tìm kiếm sự dễ dàng

sử dụng hoặc tùy biến sâu.

Trong video này, bạn đã khám phá

những cân nhắc quan trọng

để triển khai

ngôn ngữ lớn

các mô hình một cách hiệu quả.

Bạn đã học được cách

cân nhắc sự đánh đổi giữa

triển khai cục bộ và

sử dụng API đám mây,

giúp bạn lựa chọn tốt nhất

cách tiếp cận cho dự án của bạn

Bây giờ bạn đã hiểu khi nào nên

sử dụng các mô hình được đào tạo trước so với

tinh chỉnh và cách

tùy chỉnh mô hình cho

hiệu suất tối ưu.

Ngoài ra, bạn đã

giới thiệu về Ôm

Công cụ triển khai khuôn mặt,

có thể hợp lý hóa

quy trình làm việc của bạn.

Với những hiểu biết này, bạn

đang chuẩn bị tốt để thực hiện

quyết định sáng suốt và triển khai

mô hình của bạn một cách tự tin.

Làm tốt lắm, và tôi sẽ thấy

bạn trong bài học tiếp theo.

Bây giờ tôi có một câu hỏi dành cho bạn.