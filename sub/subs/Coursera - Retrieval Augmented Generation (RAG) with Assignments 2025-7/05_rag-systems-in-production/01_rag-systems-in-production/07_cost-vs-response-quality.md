# 07 chi phí so với chất lượng đáp ứng

---

Bây giờ là lúc nói về chủ đề yêu thích của mọi kỹ sư, đó là ngân sách.

Khi bạn thiết kế hệ thống RAG đầu tiên của mình, có thể bạn sẽ tập trung vào việc khám phá những gì

có thể và có được một nguyên mẫu hoạt động được.

Khi bạn bắt đầu mở rộng quy mô hệ thống của mình lên hàng trăm, hàng nghìn hoặc thậm chí hàng triệu yêu cầu, chi phí

những cân nhắc ngày càng trở nên quan trọng.

Vì vậy, hãy xem những chiến lược nào có sẵn cho bạn để hạn chế chi phí của hệ thống

trong khi vẫn cung cấp phản hồi chất lượng cao.

Hai chi phí lớn nhất trong một ứng dụng RAG điển hình sẽ là cơ sở dữ liệu vectơ và dung lượng lớn của bạn.

các mô hình ngôn ngữ

Hãy bắt đầu bằng cách xem xét một số cách để quản lý chi phí LLM.

Một cách để giảm chi phí LLM là thử nghiệm sử dụng các mô hình nhỏ hơn.

Cho dù đó là LLM cốt lõi chịu trách nhiệm tạo phản hồi cuối cùng hay LLM của bộ định tuyến

trong một hệ thống tác tử, bạn có thể đạt được chất lượng tổng thể tương tự với chi phí nhỏ hơn

và do đó các mô hình rẻ hơn.

Các mô hình có thể nhỏ hơn vì chúng chứa ít tham số hơn ngay từ đầu hoặc

bởi vì các giá trị của các tham số của chúng đã được lượng tử hóa thành định dạng có độ chính xác thấp hơn

như 8-bit.

Trong cả hai trường hợp, bạn sẽ thường ngạc nhiên một cách thú vị về hiệu quả hoạt động của các mô hình nhỏ hơn,

đặc biệt nếu LLM của bạn sẽ thực hiện một số nhiệm vụ hạn chế.

Việc tinh chỉnh một mô hình nhỏ có thể mang lại kết quả tốt với chi phí thấp.

Cách tiếp cận đơn giản thứ hai là thử nghiệm các cách để hạn chế số lượng đầu vào và

token đầu ra.

Lời nhắc RAG có thể tăng kích thước nhanh chóng, đặc biệt nếu bạn truy xuất nhiều đoạn dài cho mỗi đoạn.

nhắc nhở.

Thử nghiệm lấy ít tài liệu hơn, hay nói cách khác là giảm top-k.

Nhiều LLM có thể dài dòng và hãy nhớ rằng bạn phải trả tiền cho mỗi mã thông báo mà chúng tạo ra.

Cập nhật lời nhắc của hệ thống để khuyến khích phản hồi ngắn gọn hoặc thậm chí đặt giới hạn mã thông báo chắc chắn

là một cách đơn giản khác để giảm chi phí.

Cho dù bạn đang giảm kích thước mô hình hay độ dài lời nhắc, việc có một quy trình có khả năng quan sát mạnh mẽ

tại chỗ sẽ cho phép bạn đánh giá tác động của những thay đổi này và quyết định xem sự đánh đổi

giữa tiết kiệm chi phí và giảm chất lượng phản hồi thực sự đáng giá.

Một cách tiếp cận khả thi khác là lưu trữ LLM trên phần cứng chuyên dụng.

Các nhà cung cấp LLM trên nền tảng đám mây như TogetherAI, AWS và Google cung cấp các điểm cuối suy luận thuận tiện,

và chúng thường có ý nghĩa khi sử dụng khi bạn xây dựng một nguyên mẫu.

Tuy nhiên, nếu dự án của bạn được mở rộng tới hàng nghìn hoặc hàng triệu yêu cầu, bạn có thể muốn

để tiết kiệm tiền bằng cách chạy các mô hình trên phần cứng chuyên dụng được thuê từ chính các công ty đó.

Lợi ích bổ sung của các điểm cuối chuyên dụng là độ tin cậy tốt hơn, vì phần cứng đó

chỉ phục vụ lưu lượng người dùng của bạn và không có gì khác.

Khi sử dụng phần cứng chuyên dụng để lưu trữ mô hình, bạn sẽ trả tiền theo giờ cho GPU cho mô hình của mình

yêu cầu.

Tuy nhiên, ở quy mô lớn, việc tiết kiệm chi phí bằng cách trả tiền theo giờ so với trả tiền cho mỗi mã thông báo có thể rất lớn.

đáng kể.

Khi tìm cách tiết kiệm tiền trên cơ sở dữ liệu vectơ của bạn, điều quan trọng cần biết là hầu hết

cơ sở dữ liệu cung cấp cho bạn nhiều loại bộ nhớ.

Thông thường, có ba loại bộ nhớ cần xem xét ở đây - RAM, bộ nhớ đĩa và

lưu trữ đối tượng đám mây.

RAM là nhanh nhất nhưng đắt nhất.

Lưu trữ đối tượng trên đám mây là chậm nhất nhưng rẻ nhất.

Và bộ nhớ đĩa nằm ở đâu đó ở giữa.

RAM thường đắt hơn nhiều lần trên mỗi gigabyte so với bộ nhớ đĩa, bản thân nó cũng vậy.

đắt hơn nhiều lần so với lưu trữ đám mây.

Nếu bạn muốn tiết kiệm tiền thì bạn muốn đảm bảo rằng bạn chỉ trả tiền để lưu giữ thông tin

trong bộ lưu trữ nhanh và đắt tiền nếu nó thực sự mang lại lợi ích cho hiệu suất hệ thống của bạn.

Ví dụ: chỉ mục HNSW phải được giữ trong RAM để đảm bảo tìm kiếm vectơ chạy nhanh nhất

càng tốt.

Tuy nhiên, nội dung tài liệu của bạn có thể không cần được lưu trữ trong RAM.

Sau đó, bạn có thể quyết định đặt các tài liệu được truy cập thường xuyên nhất của mình vào bộ nhớ đĩa và

các đối tượng hiếm khi được truy cập trong bộ lưu trữ đối tượng trên đám mây.

Nhiều cơ sở dữ liệu vectơ bao gồm các tính năng giúp bạn theo dõi sự cân bằng này và thậm chí có thể

giúp di chuyển dữ liệu một cách linh hoạt vào các loại bộ nhớ khác nhau dựa trên ứng dụng của bạn

nhu cầu.

Một ví dụ điển hình của phương pháp này là multi-tenancy, có nghĩa là chia tất cả các tài liệu thành

cơ sở dữ liệu vectơ của bạn theo người dùng hoặc tổ chức mà họ thuộc về.

Ví dụ: bạn có thể có một triệu tài liệu trong cơ sở dữ liệu vectơ của mình, thuộc sở hữu của một nghìn

người dùng khác nhau.

Mỗi người dùng chỉ có thể truy cập tài liệu của riêng mình, vì vậy mỗi người dùng sẽ thực sự

có chỉ mục HNSW riêng cho các tài liệu liên quan đến chúng.

Hệ thống này giúp dễ dàng tải nhanh dữ liệu của người thuê vào bộ nhớ nhanh và đắt tiền

chỉ khi cần thiết.

Ví dụ: bạn có thể đợi cho đến khi khách hàng thực sự đăng nhập vào trang web của bạn để tải

vectơ vào RAM hoặc bạn có thể mặc định giữ dữ liệu của người thuê châu Âu

được bảo quản chậm hơn vào ban đêm ở Châu Âu.

Trong cả hai trường hợp, bạn chỉ di chuyển dữ liệu vào và ra khỏi bộ nhớ đắt tiền nhưng sắp xếp

thông tin của người thuê giúp thực hiện nhiệm vụ này một cách hiệu quả dễ dàng hơn.

Ý tưởng cốt lõi của tất cả những tối ưu hóa này là với tư cách là một kỹ sư, bạn cần hiểu

nguồn chi phí của bạn và đảm bảo chúng được chứng minh bằng hiệu quả hoạt động.

Đối với LLM, mô hình nhỏ hơn và lời nhắc ngắn hơn thường là giải pháp.

Đối với cơ sở dữ liệu vectơ, việc lưu trữ lượng dữ liệu nhỏ hơn trong bộ lưu trữ đắt tiền và di chuyển giữa

RAM, đĩa và lưu trữ đối tượng là những cách chính để tiết kiệm chi phí.

Việc thử nghiệm và giám sát tác động hiệu suất của những thay đổi này sẽ cho phép bạn

quyết định xem khoản tiết kiệm chi phí họ mang lại có xứng đáng hay không.