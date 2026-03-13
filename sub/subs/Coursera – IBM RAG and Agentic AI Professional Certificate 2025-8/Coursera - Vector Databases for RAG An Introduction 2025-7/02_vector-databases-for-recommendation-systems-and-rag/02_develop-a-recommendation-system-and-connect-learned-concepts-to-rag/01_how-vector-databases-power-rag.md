# 01-vector-cơ sở dữ liệu-power-rag

---

Chào mừng bạn đến với video này, "Cách cơ sở dữ liệu Vector cung cấp năng lượng cho RAG".

Sau khi xem video này, bạn sẽ có thể

Mô tả RAG là gì và vấn đề nó giải quyết

Mô tả từng bước chính trong quy trình RAG

Giải thích lý do tại sao bạn nên sử dụng cơ sở dữ liệu vectơ để thực hiện nhiều bước trong quy trình RAG

Và mô tả những cạm bẫy cần tránh trong quy trình RAG

Trong video này, chúng ta sẽ khám phá cách cơ sở dữ liệu vectơ không chỉ là một phần của Truy xuất

Thế hệ tăng cường hay RAG, chúng là xương sống của nó.

Vì vậy, hãy cùng tìm hiểu cách cơ sở dữ liệu vectơ cung cấp năng lượng cho đường dẫn RAG.

Nhưng trước tiên, hãy tóm tắt lại RAG là gì.

RAG là một framework giúp nâng cao các mô hình ngôn ngữ bằng cách

Lấy thông tin liên quan từ các nguồn bên ngoài và sử dụng nó để tạo ra thông tin chính xác hơn

phản ứng có căn cứ, và do đó làm giảm số lượng ảo giác tiềm ẩn

có thể xảy ra.

LLM, mặc dù có khả năng xử lý lượng lớn dữ liệu nhưng lại có cửa sổ ngữ cảnh hạn chế, do đó

không thể bao gồm tất cả thông tin trong một lời nhắc.

Hơn nữa, kiến thức của họ bị đóng băng tại thời điểm họ được đào tạo, và họ

có thể ảo giác sự thật.

RAG giải quyết những vấn đề này bằng cách truy xuất và đưa kiến ​​thức liên quan vào lời nhắc.

Chúng ta hãy xem ví dụ về tất cả các bước trong quy trình RAG đầy đủ.

Đầu tiên, các tài liệu nguồn liên quan đến ca sử dụng được cung cấp và có khả năng

chia thành các phần nhỏ hơn.

Tiếp theo, các tài liệu nguồn hoặc các đoạn của chúng sẽ được nhúng vào.

Sau đó, các nguồn này và phần nhúng của chúng được lưu trữ trong cơ sở dữ liệu vectơ, chẳng hạn như Chroma DB.

Tiếp theo, lời nhắc của người dùng được nhận.

Sau đó, lời nhắc của người dùng này được nhúng.

Sau đó, người truy tìm sẽ chọn các khối từ kho vectơ phù hợp nhất với nhu cầu của người dùng.

nhắc nhở.

Tiếp theo, văn bản được truy xuất sẽ được kết hợp với lời nhắc ban đầu của người dùng để tạo ra một

lời nhắc tăng cường.

Và cuối cùng, lời nhắc tăng cường này được chuyển đến LLM để tạo ra phản hồi nhận biết ngữ cảnh.

Cơ sở dữ liệu vectơ đóng vai trò trung tâm trong đường dẫn RAG.

Họ có thể xử lý một số trách nhiệm chính như nhúng cả tài liệu nguồn và

lời nhắc của người dùng, lưu trữ các phần nhúng đó, truy xuất các kết quả phù hợp nhất và cung cấp

truy xuất nội dung để tăng cường nhanh chóng.

Điều này thể hiện đầy đủ khả năng của hầu hết các cơ sở dữ liệu vectơ hiện đại.

Tuy nhiên, một số bước này, chẳng hạn như nhúng tài liệu và lời nhắc (bước 2 và 5),

cũng có thể được thực hiện bên ngoài.

Trong những trường hợp như vậy, cơ sở dữ liệu vectơ được sử dụng chủ yếu để lưu trữ và truy xuất vectơ.

Bây giờ hãy thảo luận lý do tại sao bạn muốn sử dụng cơ sở dữ liệu vectơ để thực hiện hầu hết các bước

bên trong đường ống RAG.

Trước hết, việc sử dụng cơ sở dữ liệu vectơ giúp ngăn ngừa các lỗi nghiêm trọng, chẳng hạn như vô tình sử dụng

các mô hình nhúng khác nhau cho tài liệu nguồn và lời nhắc của người dùng hoặc liên kết các phần nhúng không chính xác

tới các tài liệu nguồn tương ứng của chúng.

Thứ hai, quá trình phát triển trở nên nhanh hơn và rõ ràng hơn khi có nhiều bước hơn được chuyển sang cơ sở dữ liệu vectơ.

Với ít bộ phận chuyển động hơn và ít logic tùy chỉnh hơn, cơ sở mã của bạn sẽ đơn giản và dễ dàng hơn

duy trì, điều này giúp việc triển khai và gỡ lỗi nhanh hơn.

Và cuối cùng, hiệu suất là một lợi thế lớn.

Cơ sở dữ liệu vectơ được xây dựng để tìm kiếm ngữ nghĩa tốc độ cao, có thể mở rộng bằng cách sử dụng

thuật toán lập chỉ mục.

Các lựa chọn thay thế được xây dựng tùy chỉnh thường không thể phù hợp với hiệu suất này nếu không có

nỗ lực tối ưu hóa.

Cơ sở dữ liệu vectơ rất mạnh mẽ, nhưng ngay cả với các công cụ phù hợp, vẫn có những lỗi phổ biến

cần chú ý trong đường ống RAG.

Một số cạm bẫy này có thể tránh được bằng cách sử dụng cơ sở dữ liệu vectơ.

Những người khác yêu cầu sự chú ý cẩn thận hơn.

Ví dụ: sử dụng các mô hình nhúng khác nhau cho tài liệu và truy vấn của bạn có thể làm hỏng quá trình truy xuất

hoàn toàn.

Vì vậy, hãy sử dụng cùng một mô hình nhúng xuyên suốt.

Cơ sở dữ liệu vectơ thường tự động xử lý việc này.

Một cạm bẫy khác là chọn chiến lược phân chia kém, tạo ra các phân đoạn có

quá lớn hoặc quá nhỏ, điều này cũng có thể ảnh hưởng tiêu cực đến hiệu suất.

Do đó, hãy chọn kích thước đoạn đủ dài để bảo toàn ý nghĩa mà không bao gồm

quá nhiều nội dung không liên quan.

Một lỗi phổ biến khác là quên nhúng lại nội dung của bạn sau khi thay đổi dữ liệu, khoảng cách

mô hình số liệu hoặc nhúng.

Đối với một số cơ sở dữ liệu, chẳng hạn như Chroma DB, việc này không thể thực hiện được trên cơ sở dữ liệu hiện có và

có thể cần phải nhân bản bộ sưu tập của bạn.

Và cuối cùng, chỉ vì thứ gì đó được lấy ra không có nghĩa đó là câu trả lời hay nhất.

Do đó, bạn phải luôn kiểm tra kết quả của mình vì một chút điều chỉnh có thể tạo ra sự khác biệt lớn.

Cơ sở dữ liệu vectơ rất cần thiết cho RAG nhưng chúng không làm được mọi thứ.

Một số tác vụ đường ống RAG thường xảy ra bên ngoài cơ sở dữ liệu.

Ví dụ, việc phân đoạn thường được thực hiện trước khi dữ liệu vào cơ sở dữ liệu vectơ.

Logic truy xuất bổ sung, chẳng hạn như lọc và sắp xếp lại, có thể yêu cầu các công cụ bổ sung.

Việc tăng cường nhanh chóng cũng thường được xử lý bên ngoài cơ sở dữ liệu.

Và việc tích hợp với LLM không được tích hợp vào hầu hết các cơ sở dữ liệu vectơ.

Đó là nơi các khung RAG lấp đầy khoảng trống bằng cách kết nối tất cả các phần.

Các công cụ như LangChain và LlamaIndex bao quanh cơ sở dữ liệu vectơ của bạn và giúp quản lý

quy trình từ chuẩn bị tài liệu đến phản hồi cuối cùng.

Các khung này cung cấp cấu trúc bổ sung và đơn giản hóa việc phát triển và triển khai

của ứng dụng RAG của bạn hơn nữa.

Trong video này, bạn đã học được rằng

RAG nâng cao chất lượng phản hồi LLM bằng cách truy xuất thông tin bên ngoài có liên quan, giúp

mô hình tạo ra kết quả đầu ra chính xác hơn và được hỗ trợ tốt hơn.

Cơ sở dữ liệu vectơ là nền tảng giúp cho việc tạo tăng cường truy xuất hoạt động.

Cơ sở dữ liệu vectơ nhiệm vụ có thể thực hiện trong đường dẫn RAG bao gồm:

Nhúng tài liệu nguồn và lời nhắc của người dùng,

lưu trữ các phần nhúng, truy xuất hầu hết các kết quả phù hợp,

và cung cấp nội dung được truy xuất để tăng cường nhanh chóng.

Sử dụng cơ sở dữ liệu vectơ cho tất cả các bước RAG có liên quan giúp ngăn ngừa các lỗi nghiêm trọng, tốc độ

phát triển ứng dụng và tối ưu hóa hiệu suất.

Một số quy trình RAG, chẳng hạn như phân đoạn, logic truy xuất nâng cao, tăng cường nhắc nhở và

Tích hợp LLM, thường xảy ra bên ngoài cơ sở dữ liệu.

Và các khung RAG, chẳng hạn như LangChain và LlamaIndex, có thể bao bọc cơ sở dữ liệu vectơ của bạn

và giúp quản lý toàn bộ quy trình RAG, đơn giản hóa hơn nữa việc phát triển ứng dụng RAG.