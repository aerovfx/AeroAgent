# 01 Advanced-Retriever-in-llamaindex

---

Chào mừng bạn đến với video này, "Công cụ truy xuất nâng cao trong LLAMAIndex."

Sau khi xem video này, bạn sẽ có thể

xác định các loại chỉ mục khác nhau trong LLAMAIndex và biết khi nào nên sử dụng từng loại,

khám phá các công cụ truy xuất cốt lõi và nâng cao hỗ trợ các chiến lược tìm kiếm linh hoạt,

khám phá các kỹ thuật tổng hợp kết hợp kết quả từ nhiều truy vấn,

và hiểu các trường hợp sử dụng phù hợp nhất cho các loại chó tha mồi khác nhau.

Trong video này, bạn sẽ tìm hiểu cách xây dựng quy trình truy xuất thông minh, linh hoạt

bằng cách sử dụng các công cụ và công cụ truy xuất do khung LLAMAIndex cung cấp.

Trước tiên, hãy bắt đầu bằng cách thảo luận về ba loại chỉ mục cốt lõi có sẵn trong LLAMAIndex.

VectorStoreIndex được sử dụng để tìm kiếm ngữ nghĩa dựa trên ý nghĩa.

DocumentSummaryIndex sử dụng các bản tóm tắt được tạo để xác định các tài liệu có liên quan.

Và, KeyTableIndex cho phép kết hợp từ khóa chính xác cho tìm kiếm dựa trên quy tắc hoặc kết hợp.

Hãy thảo luận chi tiết hơn về loại chỉ mục đầu tiên, VectorStoreIndex.

Chỉ mục này lưu trữ các phần nhúng vector cho từng đoạn tài liệu.

Nó phù hợp nhất cho việc truy xuất ngữ nghĩa.

Và nó thường được sử dụng trong các quy trình liên quan đến các mô hình ngôn ngữ lớn.

Tiếp theo là DocumentSummaryIndex.

Chỉ mục này tạo và lưu trữ các bản tóm tắt tài liệu tại thời điểm lập chỉ mục.

Những bản tóm tắt này được sử dụng để lọc tài liệu trước khi lấy ra toàn bộ nội dung.

Loại chỉ mục này đặc biệt hữu ích khi làm việc với các bộ tài liệu lớn và đa dạng

không thể vừa với cửa sổ ngữ cảnh của LLM.

Loại chỉ mục thứ ba là KeyTableIndex.

Loại chỉ mục này trích xuất từ ​​khóa từ tài liệu.

Nó ánh xạ những từ khóa đó tới các khối nội dung cụ thể.

Lý tưởng cho việc kết hợp từ khóa chính xác

và cho các kịch bản tìm kiếm kết hợp hoặc dựa trên quy tắc.

Bây giờ chúng ta hãy nói về công cụ truy xuất, bắt đầu với Công cụ truy xuất chỉ mục Vector.

Công cụ truy xuất này sử dụng các vectơ nhúng để tìm nội dung có liên quan về mặt ngữ nghĩa.

Đó là lý tưởng cho mục đích tìm kiếm chung.

Nó cũng được sử dụng rộng rãi trong thế hệ tăng cường truy xuất, RAG, đường ống.

Trước khi chuyển sang công cụ truy tìm tiếp theo, hãy hiểu về TF-IDF,

Nền tảng của tìm kiếm dựa trên từ khóa.

Tần số thuật ngữ, phần TF trong TF-IDF, đo tần suất một từ xuất hiện trong tài liệu.

Tần số tài liệu nghịch đảo, phần IDF trong TF-IDF, đo mức độ hiếm của từ đó trên tất cả các tài liệu.

Điểm TF-IDF là tích của hai giá trị này,

Làm nổi bật những từ thường xuyên xuất hiện trong một tài liệu nhưng hiếm gặp trong toàn bộ bộ sưu tập.

Bây giờ chúng ta hãy nhìn vào BM25 Retriever

đó là một phương pháp dựa trên từ khóa để xếp hạng tài liệu.

BM25 Retriever truy xuất nội dung dựa trên kết hợp từ khóa chính xác thay vì sự tương đồng về ngữ nghĩa.

Tuy nhiên, nó cải thiện TF-IDF bằng cách giải quyết một số hạn chế của nó.

Cụ thể, BM25 làm giảm tác động của các thuật ngữ lặp lại bằng cách sử dụng độ bão hòa tần số của thuật ngữ.

Nó cũng điều chỉnh độ dài tài liệu, giúp việc tìm kiếm dựa trên từ khóa trở nên hiệu quả hơn.

Tiếp theo, chúng ta sẽ thảo luận về Công cụ truy xuất chỉ mục tóm tắt tài liệu.

Những loại công cụ truy xuất này sử dụng tóm tắt tài liệu thay vì tài liệu thực tế để tìm nội dung liên quan

Có hai phiên bản của chú chó tha mồi này,

với một phiên bản sử dụng mô hình ngôn ngữ lớn hoặc LLM để tìm nội dung phù hợp nhất.

Tuy nhiên, sử dụng LLM để tìm dữ liệu liên quan có thể tốn nhiều thời gian và tốn kém hơn các tùy chọn khác.

Phiên bản còn lại sử dụng sự tương đồng về ngữ nghĩa giữa truy vấn và phần nhúng tóm tắt để tìm nội dung phù hợp nhất.

Phiên bản này hiệu quả hơn cho các bộ sưu tập lớn.

Bất kể phiên bản nào được sử dụng, Trình truy xuất chỉ mục tóm tắt tài liệu sẽ trả về các tài liệu gốc chứ không phải bản tóm tắt của chúng.

Tiếp theo là Auto Merge Retriever

Công cụ truy xuất này được thiết kế để bảo tồn ngữ cảnh trong các tài liệu dài bằng cấu trúc phân cấp.

Nó sử dụng phân đoạn phân cấp để chia tài liệu thành các nút cha và nút con.

Nếu đủ các nút con từ cùng một nút cha được lấy ra, thì trình truy xuất sẽ trả về nút cha thay thế.

Điều này giúp củng cố nội dung liên quan và duy trì bối cảnh rộng hơn.

Hãy xem xét Công cụ truy xuất đệ quy.

Công cụ truy xuất này được thiết kế để theo dõi mối quan hệ giữa các nút bằng cách sử dụng các tham chiếu.

Nó có thể theo dõi các tham chiếu từ nút này sang nút khác, chẳng hạn như các trích dẫn trong một bài báo học thuật hoặc các liên kết siêu dữ liệu khác.

Nó hỗ trợ cả tham chiếu chunk và tham chiếu siêu dữ liệu.

Điều này cho phép Công cụ truy xuất đệ quy truy xuất nội dung liên quan trên các tài liệu hoặc các lớp trừu tượng.

Cuối cùng, chúng ta sẽ khám phá Query Fusion Retriever.

Công cụ truy xuất này được sử dụng để kết hợp các kết quả từ các công cụ truy xuất khác nhau, chẳng hạn như các phương pháp dựa trên vectơ và dựa trên từ khóa.

Nó cũng tùy chọn tạo ra nhiều biến thể của truy vấn bằng cách sử dụng LLM để cải thiện phạm vi bao phủ.

Các kết quả được hợp nhất bằng cách sử dụng các chiến lược tổng hợp như tổng hợp thứ hạng đối ứng hoặc tổng hợp điểm tương đối để cải thiện khả năng thu hồi.

Hãy cùng thảo luận về một số chiến lược hợp nhất được Query Fusion Retriever của LLAMAIndex hỗ trợ.

Kết hợp xếp hạng đối ứng kết hợp các danh sách được xếp hạng bằng cách gán điểm cao hơn cho các tài liệu xuất hiện gần đầu bất kỳ danh sách nào.

Nó mạnh mẽ và không phụ thuộc vào cường độ điểm số.

Tổng hợp điểm tương đối chuẩn hóa điểm số trong mỗi bộ kết quả bằng cách chia điểm tối đa.

Điều này bảo toàn sự tự tin tương đối của mỗi chú chó săn.

Sự kết hợp dựa trên phân phối sử dụng các kỹ thuật thống kê như chuẩn hóa điểm z hoặc xếp hạng phần trăm để kết hợp các kết quả, khiến nó trở nên lý tưởng để xử lý sự biến đổi của điểm số.

Cuối cùng, hãy đề cập đến một số đề xuất về việc nên sử dụng Công cụ truy xuất LLAMAIndex nào trong các trường hợp sử dụng cụ thể.

Đối với câu hỏi và câu trả lời chung, hãy sử dụng Công cụ truy xuất chỉ mục Vector, có thể kết hợp với Công cụ truy xuất BM25.

Sự kết hợp của công cụ tìm kiếm này kết hợp mức độ liên quan về mặt ngữ nghĩa với việc kết hợp từ khóa.

Đối với các tài liệu kỹ thuật, đặc biệt là những tài liệu cần ưu tiên các thuật ngữ chính xác, hãy cân nhắc đặt BM25 làm công cụ truy xuất chính của bạn,

với Vector Index Retriever bổ sung tính linh hoạt theo ngữ cảnh như một công cụ truy xuất phụ.

Đối với các tài liệu dài, Auto Merging Retriever là một lựa chọn tuyệt vời vì nó sẽ chỉ truy xuất các phiên bản gốc dài hơn nếu truy xuất đủ các phiên bản con ngắn hơn.

Đối với các tài liệu nghiên cứu, hãy sử dụng Công cụ truy xuất đệ quy để truy xuất nội dung liên quan từ các tài liệu được trích dẫn.

Đối với các bộ tài liệu lớn, hãy cân nhắc sử dụng Công cụ truy xuất chỉ mục tóm tắt tài liệu để thu hẹp số lượng tài liệu có liên quan,

tiếp theo là Tìm kiếm Vector trong tập hợp con còn lại để truy xuất nội dung phù hợp nhất.

Trong video này, bạn đã học được rằng

Các loại LLAMAIndex cốt lõi là VectorStoreIndex, DocumentSummaryIndex và KeyTableIndex.

VectorStoreIndex lưu trữ các phần nhúng vectơ cho từng đoạn tài liệu, phù hợp nhất cho việc truy xuất ngữ nghĩa,

và thường được sử dụng trong các quy trình liên quan đến các mô hình ngôn ngữ lớn.

DocumentSummaryIndex tạo và lưu trữ các bản tóm tắt tài liệu,

được sử dụng để lọc tài liệu trước khi truy xuất toàn bộ nội dung và rất hữu ích khi làm việc với các bộ tài liệu lớn và đa dạng.

KeyTableIndex trích xuất từ ​​khóa từ tài liệu và ánh xạ chúng tới các khối nội dung cụ thể và rất hữu ích trong các tình huống tìm kiếm kết hợp hoặc dựa trên quy tắc.

VectorIndexRetriever sử dụng các phần nhúng vectơ để tìm nội dung có liên quan về mặt ngữ nghĩa và lý tưởng cho các đường dẫn RAG và tìm kiếm có mục đích chung.

BM25 Retriever là một phương pháp dựa trên từ khóa để xếp hạng tài liệu và nó truy xuất nội dung dựa trên kết quả khớp từ khóa chính xác thay vì sự giống nhau về ngữ nghĩa.

Trình truy xuất chỉ mục tóm tắt tài liệu sử dụng tóm tắt tài liệu thay vì tài liệu thực tế để tìm nội dung liên quan.

Có hai phiên bản của Công cụ truy xuất chỉ mục tóm tắt tài liệu, một phiên bản sử dụng LLM và phiên bản còn lại sử dụng tính tương tự về ngữ nghĩa.

Auto Merge Retriever bảo toàn ngữ cảnh trong các tài liệu dài bằng cách sử dụng cấu trúc phân cấp

và sử dụng phân đoạn theo cấp bậc để chia tài liệu thành các nút cha và nút con.

Recursive Retriever tuân theo mối quan hệ giữa các nút và sử dụng các tham chiếu như trích dẫn trong các bài báo học thuật hoặc liên kết siêu dữ liệu.

Trình truy xuất kết hợp truy vấn kết hợp các kết quả từ các trình truy xuất khác nhau bằng cách sử dụng các chiến lược tổng hợp.

Và các chiến lược hợp nhất được Query Fusion Retriever hỗ trợ là

Hợp nhất thứ hạng đối ứng, hợp nhất điểm tương đối và hợp nhất dựa trên phân phối