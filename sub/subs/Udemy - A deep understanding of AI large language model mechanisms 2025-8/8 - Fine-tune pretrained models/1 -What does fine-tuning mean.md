# 1 -Tinh chỉnh nghĩa là gì

---

Chào mừng bạn đến với phần này về tinh chỉnh LLM. Ở phần đầu của phần trước,

Tôi đã thảo luận ngắn gọn về ý nghĩa của việc tinh chỉnh các mô hình và điều đó khác với đào tạo trước như thế nào.

Vì vậy, trong video này, tôi sẽ nhắc lại sự khác biệt đó và chỉ ra một số thách thức trong việc tinh chỉnh

mà bạn sẽ khám phá trong phần này.

Đây là bảng tóm tắt mà bạn đã thấy

ở phần đầu của phần trước,

và ở đây tôi sẽ chỉ nhắc nhở bạn một cách ngắn gọn

ý tưởng của các mô hình tinh chỉnh.

Khi bạn tinh chỉnh LLM,

bạn không bắt đầu từ trọng số ngẫu nhiên ban đầu.

Thay vào đó, bạn tải xuống trọng lượng mà các tổ chức khác

đã dành nhiều tháng đào tạo về một kho văn bản khổng lồ.

Vì vậy, mô hình nền tảng đó đã có thể hiểu và sản xuất được ngữ pháp và

văn bản hợp lý về mặt cú pháp.

Những gì bạn sẽ làm khi tinh chỉnh là điều chỉnh và điều chỉnh mô hình cho phù hợp với một số nhiệm vụ cụ thể.

Và chính xác thì điều gì liên quan đến việc tinh chỉnh, nói một cách thực tế?

Vâng, bạn bắt đầu bằng việc tìm một mô hình cơ sở phù hợp với ứng dụng của mình.

Vì vậy, không chỉ có GPT-2 từ OpenAI.

Có hàng trăm mẫu cơ bản mà các nhóm hoặc công ty khác nhau đã sản xuất và chế tạo

có sẵn.

Một số trong số chúng nhỏ hơn, một số trong số chúng lớn hơn.

Trong phần này và phần tiếp theo, tôi sẽ giới thiệu cho bạn một số mô hình

chúng tôi có thể tải về.

Tiếp theo bạn nhận được một tập dữ liệu.

Vì vậy, để làm cho điều này cụ thể hơn một chút, giả sử bạn đang làm việc

cho một tổ chức phi lợi nhuận tập trung vào việc nâng cao kiến thức tài chính ở các nước đang phát triển.

Bạn có thể tham gia GPT được đào tạo trước và thu thập nhiều văn bản về lời khuyên để hiểu biết về tài chính

đó là thông lệ dành cho người dân ở các nước đang phát triển.

Có thể đó là văn bản được công bố rộng rãi trên mạng,

hoặc có thể bạn liên hệ với các chuyên gia trong lĩnh vực này

và yêu cầu họ viết những lời khuyên cụ thể

mà bạn có thể sử dụng cho tập huấn luyện.

Nói cách khác, tập dữ liệu mà bạn sử dụng để tinh chỉnh

được quản lý và tên miền cụ thể.

Điều đó cũng có nghĩa là bạn có ít dữ liệu hơn,

điều đó có nghĩa là thay vì đào tạo hàng tháng

trên các cụm GPU cực kỳ đắt tiền,

bạn có thể tinh chỉnh một mô hình được đào tạo trước

có thể trong vài ngày nữa,

có thể là vài tuần nếu đó là một mô hình thực sự lớn

và bạn có rất nhiều dữ liệu,

nhưng cũng có thể chỉ là vài giờ.

Vấn đề là khi bạn có mô hình cơ sở

và bạn có một tập dữ liệu,

sau đó bạn tiếp tục huấn luyện mô hình bằng cách sử dụng phương pháp giảm độ dốc

chính xác giống như cách tôi đã chỉ cho bạn

cách đào tạo mô hình từ đầu ở phần trước.

Toán học giống nhau, mã giống nhau.

Có một vài điểm khác biệt mà bạn sẽ thấy trong phần này.

Ví dụ: bạn muốn sử dụng tỷ lệ học tập nhỏ hơn

để tinh chỉnh và bạn thường áp dụng

một số điều chỉnh bổ sung như đóng băng một số lớp.

Về cơ bản, bạn không muốn ghi đè hoặc đào tạo lại

bất kỳ cú pháp cơ bản hoặc kiến thức thế giới nào mà mô hình đã học được trong quá trình đào tạo trước.

Và vì vậy việc tinh chỉnh sẽ tinh tế hơn một chút và có mục tiêu rõ ràng hơn. Như bạn sẽ học trong phần này

phần này, có rất nhiều cách để điều chỉnh quy trình đào tạo. Và không phải lúc nào cũng rõ ràng

các tham số cần chọn, giao thức nào sẽ sử dụng và điều gì sẽ thành công. Vì vậy trong thực tế,

Tinh chỉnh bao gồm rất nhiều thử nghiệm, thử nghiệm,

khám phá, đánh giá và làm lại từ đầu.

Đúng vậy, tinh chỉnh có nghĩa là lấy một mô hình

rằng người khác đã dành rất nhiều thời gian

nỗ lực và nguồn lực để phát triển,

và sau đó bạn cải thiện nó cho nhu cầu cụ thể của riêng bạn.

Một trong những điểm tôi sẽ nhấn mạnh trong phần này

là việc tinh chỉnh vừa rất dễ vừa rất khó.

Nó rất dễ thực hiện nhưng thật khó để biết đâu là lựa chọn tối ưu để đạt được kết quả tốt nhất.