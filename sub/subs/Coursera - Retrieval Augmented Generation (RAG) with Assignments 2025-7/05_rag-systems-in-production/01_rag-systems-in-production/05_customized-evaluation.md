# 05 đánh giá tùy chỉnh

---

Tạo tập dữ liệu tùy chỉnh về các lời nhắc mà hệ thống của bạn đã nhận được

cho phép bạn hiểu sâu sắc về cách hệ thống của bạn hoạt động trong quá khứ

và sau đó chạy thử nghiệm để xem việc thiết kế lại hệ thống của bạn như thế nào

có thể thay đổi hiệu suất theo lời nhắc trong thế giới thực.

Hãy xem cách xây dựng một trong số đó.

Tập dữ liệu tùy chỉnh chỉ là tập hợp các lời nhắc mà hệ thống của bạn có

được xử lý trước đó, cũng như bất kỳ thông tin nào bạn chọn

thu thập về hành trình của lời nhắc đó trong hệ thống của bạn.

Bạn có thể chọn chỉ lưu lời nhắc ban đầu và phản hồi cuối cùng,

hoặc bạn có thể thêm rất nhiều thông tin vào tập dữ liệu tùy chỉnh của mình,

như những tài liệu mà cơ sở dữ liệu vector của bạn đã truy xuất,

cách các tài liệu đó được xếp hạng trước và sau trình xếp hạng lại của bạn,

đầu ra của trình viết lại truy vấn của bạn, v.v.

Với rất nhiều tính linh hoạt, một quyết định quan trọng khi xây dựng một

tập dữ liệu tùy chỉnh là dữ liệu nào tôi lưu trữ?

Câu trả lời đơn giản là bạn muốn đánh giá điều gì?

Ví dụ: bạn gần như chắc chắn muốn lưu lời nhắc đầu vào

do người dùng gửi và phản hồi cuối cùng do hệ thống RAC của bạn tạo ra.

Hai điểm dữ liệu cơ bản này mang lại cảm giác về hiệu suất hệ thống

và sẽ cho phép bạn theo dõi cách phản hồi thay đổi khi chỉnh sửa lời nhắc.

Tuy nhiên, thông tin đó thực sự chỉ giúp ích cho việc đánh giá toàn diện.

Nếu bạn muốn thực hiện đánh giá ở cấp độ thành phần để biết mức độ

trình truy xuất, trình xếp hạng lại hoặc trình viết lại truy vấn đang thực hiện,

bạn sẽ cần lưu dữ liệu đầu vào và đầu ra được sử dụng bởi từng thành phần đó.

Thông thường, bạn sẽ muốn ghi lại các bước cấp thành phần chi tiết này,

và kết quả là các bảng được sử dụng để ghi nhật ký cuộc gọi đến hệ thống RAC

có thể dễ dàng có hàng tá cột, lưu trữ mọi thứ từ ID

của khách hàng đã thực hiện cuộc gọi, vào phần văn bản, người xếp hạng lại của bạn

được sàng lọc đến đầu ra của mỗi LLM bộ định tuyến trong quy trình làm việc Agentech của bạn.

Việc lưu trữ nhiều loại dữ liệu như thế này cho phép bạn phân tích

từng thành phần của hệ thống riêng lẻ và kiểm tra hiệu suất

trên nhiều chiều.

Ví dụ: nếu bạn đang xây dựng một chatbot dịch vụ khách hàng,

bạn có thể lọc theo chủ đề câu hỏi để phát hiện các câu hỏi về việc hoàn tiền

đang nhận được phản hồi chất lượng cao nhưng có câu hỏi về sự chậm trễ của sản phẩm

không hoạt động tốt chút nào.

Khi bạn đi điều tra lý do tại sao những lời nhắc liên quan đến sự chậm trễ của sản phẩm đó

dẫn đến phản hồi chất lượng thấp, bạn có thể phân tích nhật ký

để phát hiện rằng chó tha mồi của bạn không thể tìm thấy nhiều tài liệu liên quan

cho những lời nhắc đó.

Có thể bạn cần thêm thông tin phù hợp hơn vào kho kiến ​​thức của mình.

Nếu bạn xây dựng hệ thống quan sát phù hợp,

bạn sẽ có thể phát hiện vấn đề, xác định nguồn gốc của chúng,

và cảm thấy tự tin rằng các giải pháp đang có hiệu quả.

Hãy để tôi chia sẻ một ví dụ về điều này từ sự nghiệp của chính tôi.

Tôi đang làm việc trên một hệ thống RAC chuyên dụng có khả năng

để tạo văn bản, hình ảnh cũng như biểu đồ và sơ đồ được hỗ trợ bằng mã

sử dụng Nàng tiên cá.js.

Chúng tôi bắt đầu nhận được những phàn nàn rằng chất lượng của một số sơ đồ

do hệ thống tạo ra khá thấp.

Xem xét ngược lại nhật ký của mình, chúng tôi nhận ra rằng nhiều vấn đề trong số này

nảy sinh khi người dùng yêu cầu hệ thống vẽ sơ đồ.

Mô hình ngôn ngữ của bộ định tuyến đã hiểu sai lời nhắc này

và do đó gửi nó đến mô hình chuyển văn bản thành hình ảnh được sử dụng để tạo hình ảnh.

Những mô hình này khá giỏi trong việc tạo ra hình ảnh của người hoặc vật,

nhưng khá tệ trong việc tạo biểu đồ.

Một khi chúng ta nhận ra nguồn gốc của vấn đề,

chúng tôi đã có thể cập nhật lời nhắc hệ thống cho bộ định tuyến LLM

để những lời nhắc đó tạo ra các biểu đồ được hỗ trợ bằng mã

và không tạo ra hình ảnh.

Nhờ hệ thống giám sát và ghi nhật ký mạnh mẽ,

khi chúng tôi nhận được báo cáo của khách hàng về vấn đề này,

thật đơn giản để truy tìm nguồn gốc của nó

và nhanh chóng đưa bản sửa lỗi vào sản xuất.

Mặc dù đôi khi bạn muốn theo dõi từng lời nhắc hoạt động kém

như thế này, khi bạn ghi lại nhiều dữ liệu,

bạn sẽ thường muốn hình dung nó.

Điều này có thể cho phép bạn xác định các xu hướng cấp cao trong hiệu suất

của toàn bộ hệ thống hoặc của từng bộ phận.

Ví dụ: bạn có thể hình dung tất cả các lời nhắc đầu vào

đi qua hệ thống của bạn và sử dụng một số loại thuật toán phân cụm

để xác định các chủ đề cấp cao mà khách hàng của bạn đang hỏi,

như giới thiệu sản phẩm hoặc các câu hỏi khắc phục sự cố.

Nếu bạn có thể phân biệt được tất cả những lời nhắc khác nhau này,

sau đó bạn có thể chạy đường dẫn đánh giá của mình chỉ trên loại lời nhắc đó

và xem liệu hệ thống của bạn có hoạt động kém đối với một số loại câu hỏi nhất định hay không.

Bộ dữ liệu tùy chỉnh là một công cụ quan trọng để cá nhân hóa ứng dụng RAG của bạn

đối với các yêu cầu đối với quy trình hệ thống của bạn.

Kết hợp chúng vào cách bạn đánh giá hệ thống của mình

là cách tốt nhất để cải thiện cách hệ thống của bạn phản hồi

đến lời nhắc thực tế và các câu hỏi mà người dùng của bạn đang hỏi.