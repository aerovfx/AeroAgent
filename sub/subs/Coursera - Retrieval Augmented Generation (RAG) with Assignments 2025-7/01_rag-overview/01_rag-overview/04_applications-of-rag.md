# 04 ứng dụng của giẻ lau

---

Như bạn vừa thấy, ý tưởng cốt lõi của RAG là kết hợp LLM có sẵn với kiến thức

cơ sở thông tin mà nó có thể không có quyền truy cập khi được đào tạo.

Nhiều hệ thống được hỗ trợ bởi LLM triển khai mô hình này, vì vậy bây giờ chúng ta hãy khám phá một vài trong số chúng.

Một ứng dụng quan trọng của RAG là tạo mã.

Điều này rất quan trọng vì mặc dù các mô hình ngôn ngữ đã được đào tạo bằng rất nhiều mã,

có thể hình dung mọi kho lưu trữ Git công khai, tạo mã chính xác cho một dự án cụ thể

yêu cầu thông tin chuyên ngành.

LLM cần biết các lớp, chức năng và định nghĩa trong dự án, cũng như

phong cách mã hóa tổng thể đang được sử dụng.

Xây dựng hệ thống RAG sử dụng cơ sở mã của riêng bạn làm cơ sở kiến thức tạo ra thông tin này

có sẵn cho LLM.

Bằng cách truy xuất các lớp, định nghĩa và tệp có liên quan từ kho lưu trữ của bạn, LLM là

có khả năng tạo mã hoặc trả lời các câu hỏi liên quan đến dự án của bạn tốt hơn nhiều.

Một ứng dụng chính khác là tùy chỉnh chatbot cho từng công ty.

Mỗi công ty đều có sản phẩm, chính sách và nguyên tắc truyền thông riêng.

Việc coi các tài liệu doanh nghiệp này như một cơ sở kiến thức cho phép bạn triển khai LLM theo nhiều cách khác nhau

về những cách hữu ích.

Bạn có thể xây dựng một chatbot dịch vụ khách hàng biết thông tin về công ty của bạn

sản phẩm, hàng tồn kho hiện tại hoặc các bước khắc phục sự cố phổ biến.

Bạn có thể triển khai một chatbot nội bộ để trả lời chính xác các câu hỏi về công ty

chính sách hoặc hướng bạn tới tài liệu hữu ích.

Trong cả hai trường hợp, cơ sở kiến thức sẽ giúp đưa ra các phản hồi của LLM phù hợp với nhu cầu cụ thể của công ty bạn.

sản phẩm hoặc chính sách và giúp giảm thiểu các trường hợp LLM tạo ra các sản phẩm hoặc chính sách chung

hoặc phản hồi sai lệch.

RAG có những ứng dụng quan trọng trong lĩnh vực chăm sóc sức khỏe và pháp lý.

Trong những trường hợp này, cơ sở tri thức có thể chứa các tài liệu pháp lý từ một

trường hợp, văn bản từ các tạp chí y khoa được xuất bản gần đây, v.v.

Trong những lĩnh vực như thế này, trong đó độ chính xác là bắt buộc và số lượng thích hợp cũng như tiềm năng

thông tin cá nhân rất rộng lớn, cách tiếp cận dựa trên RAG có thể là cách duy nhất để triển khai hệ thống dựa trên LLM

sản phẩm đủ chính xác và sử dụng thông tin cá nhân.

Một ứng dụng chính khác là tìm kiếm trên web được hỗ trợ bởi AI.

Trong lịch sử, các công cụ tìm kiếm hoạt động giống như một con chó săn.

Đưa ra một truy vấn tìm kiếm, họ trả về các trang web có liên quan.

Ngày nay, các công cụ tìm kiếm sẽ cung cấp bản tóm tắt AI của các kết quả tìm kiếm này để nhanh chóng trình bày

những thông tin hữu ích nhất theo cách có thể đọc lướt được.

Các bản tóm tắt web AI này về cơ bản là một hệ thống RAG có cơ sở kiến thức là toàn bộ

internet.

Mặc dù các hệ thống RAG quy mô lớn có thể mạnh mẽ nhưng điều này cũng đúng đối với các hệ thống được cá nhân hóa cao.

Trợ lý được cá nhân hóa trong tin nhắn văn bản, ứng dụng email, trình xử lý văn bản, lịch và

v.v. hiện có thể giúp bạn gửi tin nhắn, sắp xếp lịch trình, soạn thảo tài liệu và

hoàn thành các công trình lớn nhỏ.

Trong mỗi trường hợp, LLM càng có nhiều bối cảnh về dự án bạn đang thực hiện thì

tốt hơn là họ có thể hỗ trợ công việc đó.

Trong những trường hợp này, cơ sở tri thức có thể tương đối nhỏ.

Ví dụ: tin nhắn văn bản, danh sách liên hệ, email hoặc thư mục tài liệu của bạn.

Những loại tài liệu này dày đặc với bối cảnh quan trọng.

Vì vậy, hệ thống RAG có quyền truy cập vào thông tin cá nhân quy mô nhỏ này có thể hoàn thành các nhiệm vụ trong

một cách phù hợp hơn đáng kể với những gì bạn đang làm.

Như bạn có thể thấy, mô hình RAG có khả năng ứng dụng trong nhiều bối cảnh khác nhau.

Nhiều công ty, tổ chức và thậm chí cả bạn có bộ sưu tập thông tin có thể

được sử dụng để nâng cao chất lượng văn bản do LLM tạo ra.

Bất cứ khi nào bạn có quyền truy cập vào thông tin có thể chưa được sử dụng để đào tạo ngôn ngữ lớn

mô hình, có tiềm năng xây dựng một ứng dụng RAG hữu ích.

Họ thậm chí có thể cho phép sử dụng LLM trong những bối cảnh không thể thực hiện được.

Khi tiếp tục khóa học này, hy vọng bạn sẽ bắt đầu nhìn thấy các cơ hội trong

công việc và cuộc sống mà cách tiếp cận RAG sẽ hữu ích.

Tuy nhiên, hiện tại, hãy cùng tôi xem video tiếp theo và tìm hiểu sâu hơn về kiến trúc

của hệ thống RAG.