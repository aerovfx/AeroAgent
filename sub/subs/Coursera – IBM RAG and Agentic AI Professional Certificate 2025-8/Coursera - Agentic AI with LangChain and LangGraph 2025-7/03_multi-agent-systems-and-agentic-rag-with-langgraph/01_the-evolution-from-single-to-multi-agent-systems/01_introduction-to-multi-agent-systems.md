# 01 bài giới thiệu về hệ thống đa tác nhân

---

[ÂM NHẠC]

Chào mừng bạn đến với video giới thiệu về Hệ thống đa tác nhân.

Trong video này, bạn sẽ khám phá các hệ thống đa tác nhân và hiểu các thành phần cốt lõi của chúng.

Bạn sẽ khám phá các khái niệm chuyên môn hóa tác nhân và ví dụ về hệ thống đa tác nhân.

Bạn cũng sẽ hiểu rõ hơn về các khuôn khổ điều phối.

Cuối cùng, bạn sẽ xem xét những thách thức liên quan đến việc xây dựng những hệ thống mạnh mẽ này.

Hãy hình dung một nhóm trong đó mỗi thành viên là một tác nhân AI, mỗi người có một vai trò riêng,

cùng nhau giải quyết những thách thức phức tạp.

Đây chính là sức mạnh của hệ thống đa tác nhân, các tác nhân thông minh cộng tác theo thời gian thực.

Trong video này, bạn sẽ khám phá cách các tác nhân này phối hợp, điều chỉnh và tăng hiệu suất

trên mọi thứ từ hỗ trợ khách hàng đến phân tích dữ liệu.

Bây giờ bạn có thể xây dựng các tác nhân AI từ đầu, một trong những bước thú vị nhất tiếp theo là tổ chức

họ thành các nhóm hợp tác chuyên biệt.

Đây là bản chất của thiết kế đa tác nhân.

Các hệ thống đa tác nhân về cơ bản là về sự chuyên môn hóa có tổ chức,

phân công đúng người đại diện vào đúng nhiệm vụ.

Một hệ thống đa tác nhân (hoặc MAS) bao gồm nhiều thực thể hoặc tác nhân tự trị

tương tác trong một môi trường để đạt được mục tiêu cá nhân hoặc tập thể.

Mỗi tác nhân hoạt động độc lập, nhận thức môi trường xung quanh, đưa ra quyết định và thực hiện hành động.

Chúng ta hãy hiểu rõ hơn về các tác nhân này bằng một phép loại suy.

Hãy tưởng tượng một nhóm đầu bếp trong bếp, mỗi người chuyên về một món ăn khác nhau,

mà còn hợp tác để chuẩn bị một bữa ăn hoàn chỉnh.

Cùng nhau, những đầu bếp này có thể đảm nhận những nhiệm vụ quá phức tạp để một đầu bếp có thể xử lý một mình.

Tương tự, sự cộng tác giữa các tác nhân tự trị sẽ giúp giải quyết vấn đề hiệu quả hơn và có thể mở rộng quy mô.

Hãy sử dụng một phép tương tự để hiểu các thành phần chính của hệ thống đa tác nhân.

Hãy tưởng tượng một đội robot kho hàng.

Họ liên tục cập nhật cho nhau về quan điểm và ý định của mình.

Nếu một robot chuẩn bị nhặt một món đồ, nó sẽ báo hiệu cho những robot khác tránh dùng lực quá mức hoặc tránh va chạm.

Đây là sự phối hợp năng động, theo thời gian thực thay vì chỉ tuân theo một kịch bản cố định.

Trong kịch bản này, bản thân robot là tác nhân,

các đơn vị tự trị có khả năng và mục tiêu cụ thể.

Sàn nhà kho và kệ, nơi chúng hoạt động và tương tác, đại diện cho môi trường,

bối cảnh trong đó các tác nhân hoạt động và tương tác.

Và những tín hiệu chúng gửi cho nhau chính là những giao thức truyền thông, những tiêu chuẩn được

cho phép các đại lý chia sẻ thông tin và phối hợp hành động.

Khi thiết kế các tác nhân đa hệ thống, việc hiểu các khái niệm chuyên môn hóa tác nhân là rất quan trọng.

Điều này liên quan đến việc tuân thủ một số nguyên tắc thiết kế cốt lõi.

Đầu tiên, ranh giới năng lực.

Mỗi tác nhân nên có một phạm vi được xác định rõ ràng và tập trung.

Ví dụ: tác nhân tóm tắt không nên truy vấn cơ sở dữ liệu.

Đó rõ ràng là công việc của chó săn.

Tiếp theo, hãy xem xét chiều sâu chuyên môn và chiều rộng.

Bạn cần cân bằng giữa các tác nhân có chuyên môn cao với các tác nhân tổng quát.

Những người tổng quát này đóng vai trò là người điều phối, thực hiện nhiệm vụ định tuyến và giám sát tiến độ tổng thể.

Sau đó, tiêu chuẩn hóa giao diện là chìa khóa.

Mỗi tác nhân phải giao tiếp thông qua đầu vào và đầu ra có cấu trúc, thường sử dụng các định dạng như lược đồ JSON.

Tiêu chuẩn hóa này là yếu tố cho phép điều phối hiệu quả

thông qua các framework như LangGraph, CrewAI, BeeAI hoặc AutoGen.

Cuối cùng, thiết lập các mô hình chuyển giao rõ ràng.

Các tổng đài viên nên chuyển giao nhiệm vụ cho các tổng đài viên khác một cách khéo léo khi nhiệm vụ đó nằm ngoài chuyên môn cụ thể của họ.

Một ví dụ phổ biến là tác nhân đọc tài liệu chuyển đầu ra của nó cho tác nhân tóm tắt.

Để minh họa cách các hệ thống đa tác nhân làm việc cùng nhau trong một hệ thống AI duy nhất, hãy

hãy xem một ví dụ thực tế về hệ thống trợ lý nghiên cứu.

Trong hệ thống này, các tác nhân AI khác nhau làm việc cùng nhau, mỗi tác nhân xử lý một phần cụ thể của quy trình nghiên cứu.

Tác nhân truy xuất lấy tất cả các tài liệu liên quan từ nhiều nguồn khác nhau một cách hiệu quả.

Tiếp theo, tác nhân tóm tắt sẽ cô đọng các tài liệu đó, trích xuất và làm nổi bật những thông tin chi tiết quan trọng.

Sau đó, người phê bình sẽ bước vào để đánh giá một cách chặt chẽ

thông tin tóm tắt về bất kỳ sai lệch hoặc khoảng trống tiềm ẩn nào.

Cuối cùng, tác nhân biên dịch lấy tất cả những hiểu biết đã được xử lý này

và tạo ra báo cáo cuối cùng đầy đủ.

Chuyên môn này cho phép mở rộng quy mô hiệu quả trên các lĩnh vực như công nghệ pháp lý, chăm sóc sức khỏe,

và quản lý tri thức doanh nghiệp.

Hệ thống đa tác nhân cung cấp một số lợi thế đáng kể.

Hãy coi nó giống như một nhóm mô-đun nơi các thành viên có thể tham gia hoặc rời đi khi cần thiết, đảm bảo hoạt động liên tục.

Điều này làm nổi bật khả năng mở rộng của họ.

Bạn có thể dễ dàng thêm hoặc bớt tác nhân mà không làm gián đoạn hệ thống.

Chúng cũng mang lại sự linh hoạt to lớn vì các tác nhân có thể thích ứng với những thay đổi trong môi trường hoặc nhiệm vụ của họ.

Và cuối cùng là sự chắc chắn.

Hệ thống có thể tiếp tục hoạt động hiệu quả ngay cả khi một số tác nhân riêng lẻ bị lỗi.

Các tác nhân chủ yếu tương tác với những gì được gọi là hệ thống có cấu trúc biểu đồ,

xác định luồng công việc và giao tiếp.

Một cách phổ biến mà các đại lý cộng tác là thông qua mô hình quy trình.

Ở đây, các tác nhân thực hiện chuyển giao tuần tự,

chuyển trực tiếp đầu ra của họ làm đầu vào cho tác nhân tiếp theo trong dòng.

Một ví dụ điển hình là một tác nhân nghiên cứu thu thập dữ liệu,

sau đó giao cho một tác nhân biên tập để tinh chỉnh đầu ra.

Một phương pháp cộng tác phổ biến khác là mô hình trục và nan hoa.

Trong thiết lập này, điều phối viên trung tâm sẽ phân công nhiệm vụ cho các đại lý chuyên môn khác nhau.

Ví dụ: tác nhân quản lý nội dung có thể chỉ định các nhiệm vụ cụ thể cho người viết,

một người kiểm tra thực tế và một tác nhân tối ưu hóa SEO.

Đây chỉ là hai ví dụ và bạn sẽ tìm thấy nhiều mẫu tương tác mạnh mẽ hơn

có sẵn để thiết kế các hệ thống đa tác nhân phức tạp.

Giao tiếp hiệu quả là rất quan trọng đối với các hệ thống đa tác nhân.

Hai giao thức đáng chú ý tạo điều kiện thuận lợi cho việc này.

Giao thức bối cảnh mô hình (hoặc MCP) tiêu chuẩn hóa cách các mô hình AI truy cập và chia sẻ bối cảnh với

các công cụ và nguồn dữ liệu bên ngoài, hoạt động như một trình kết nối phổ quát cho các ứng dụng AI.

Giao thức truyền thông đại lý (hoặc ACP) được IBM phát triển và cung cấp một phương pháp tiêu chuẩn hóa

để các tác nhân AI giao tiếp và cộng tác, cho phép tích hợp và phối hợp liền mạch

trên các hệ thống khác nhau.

Các khung điều phối được sử dụng để quản lý các tương tác phức tạp giữa các tác nhân AI.

Dưới đây là một số ví dụ đáng chú ý.

Đầu tiên là LangGraph, một khung cho phép bạn xác định quy trình làm việc của nhiều tác nhân tùy chỉnh,

cung cấp cho bạn quyền kiểm soát rõ ràng về cách các đại lý của bạn tương tác.

Sau đó, bạn có CrewAI, một khung Python nguồn mở được thiết kế đặc biệt để phát triển

và quản lý các hệ thống AI đa tác nhân, giúp việc xây dựng các nhóm cộng tác gồm các tác nhân AI trở nên dễ dàng hơn.

Tiếp theo là AutoGen, một framework do Microsoft phát triển giúp tạo ra AI đa tác nhân

các ứng dụng thông qua giao diện đàm thoại, do đó các tổng đài viên có thể cộng tác hiệu quả hơn nữa.

Và cuối cùng là IBM BeeAI framework, một framework mã nguồn mở của IBM để xây dựng

và triển khai các tác nhân AI, hỗ trợ điều phối nhiều tác nhân có thể mở rộng.

Mặc dù cực kỳ mạnh mẽ nhưng các hệ thống đa tác nhân cũng đặt ra một số thách thức chính.

Đầu tiên, có sự phức tạp trong phối hợp.

Việc đảm bảo tất cả các đại lý của bạn hoạt động hài hòa có thể khá phức tạp.

Sau đó, bạn có thể gặp phải chi phí liên lạc.

Sự tương tác thường xuyên giữa các tác nhân đôi khi có thể làm cạn kiệt tài nguyên hệ thống của bạn.

Và cuối cùng, mối quan tâm về an ninh là rất quan trọng.

Bảo vệ toàn bộ hệ thống khỏi bất kỳ tác nhân độc hại nào là vô cùng quan trọng.

Trong video này, bạn đã học được rằng

Hệ thống đa tác nhân về cơ bản là về chuyên môn hóa có tổ chức.

Phân công đúng người đại diện vào đúng nhiệm vụ.

Các hệ thống này bao gồm nhiều tác nhân tự trị tương tác với một môi trường.

Các khung điều phối, chẳng hạn như khung LangGraph, CrewAI, AutoGen và IBM BeeAI

được sử dụng để quản lý các tương tác phức tạp giữa các tác nhân AI.

Giao thức bối cảnh mô hình (hoặc MCP) tiêu chuẩn hóa cách các mô hình AI truy cập và chia sẻ bối cảnh với

các công cụ và nguồn dữ liệu bên ngoài.

Giao thức truyền thông đại lý (hoặc ACP)

cung cấp một phương pháp tiêu chuẩn hóa để các tác nhân AI giao tiếp và cộng tác.

Những thách thức trong việc xây dựng hệ thống đa tác nhân bao gồm sự phức tạp trong việc phối hợp,

chi phí liên lạc và mối quan tâm về an ninh.

[ÂM NHẠC]