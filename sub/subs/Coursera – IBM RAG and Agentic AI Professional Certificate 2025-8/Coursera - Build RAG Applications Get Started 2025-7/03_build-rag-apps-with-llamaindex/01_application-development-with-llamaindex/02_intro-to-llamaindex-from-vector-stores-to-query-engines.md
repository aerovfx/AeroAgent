# 02 phần giới thiệu về llamaindex-từ-vector-stores-to-query-engine

---

Chào mừng bạn đến với video giới thiệu này về LlamaIndex bao gồm các chủ đề từ cửa hàng vector

để truy vấn các công cụ.

Sau khi xem video này, bạn sẽ có thể:

Thảo luận về việc nhúng vào các cửa hàng vectơ trong LlamaIndex,

Mô tả cách truy xuất hoạt động trong LlamaIndex với sự hiện diện của kho lưu trữ vectơ,

Thảo luận về việc tăng cường nhanh chóng và truy vấn LLM trong LlamaIndex và

Giải thích cách các công cụ truy vấn mạnh mẽ của LlamaIndex kết hợp nhiều bước RAG vào một đối tượng duy nhất.

Hãy bắt đầu với đánh giá cấp cao về RAG.

Trong Thế hệ tăng cường truy xuất, tài liệu được tải, chia khối,

và nhúng vào các vectơ được lưu trữ trong kho vectơ.

Lời nhắc của người dùng cũng được nhúng và các đoạn tương tự từ tài liệu nguồn được truy xuất

từ cửa hàng vector. Văn bản nhắc nhở và truy xuất được kết hợp và gửi

đến một mô hình ngôn ngữ để tạo ra phản hồi nhận biết ngữ cảnh.

Đến bây giờ, bạn đã quen với việc tải và chia tài liệu thành các nút.

Hãy bắt đầu bằng việc nhúng các nút đó và lưu trữ chúng trong kho lưu trữ vectơ.

Hãy xem cách bạn có thể tạo các phần nhúng.

Để tạo và lưu trữ các phần nhúng, LlamaIndex sử dụng lớp VectorStoreIndex.

Đối với các trường hợp sử dụng đơn giản, các phần nhúng có thể được tạo bằng mô hình mặc định và được lưu trữ

trong bộ nhớ bằng cách chuyển các nút làm tham số duy nhất cho VectorStoreIndex.

Đối với các trường hợp phức tạp hơn yêu cầu mô hình nhúng tùy chỉnh và bộ lưu trữ liên tục,

thủ tục sau đây là cần thiết. Đầu tiên, nhập các thư viện cần thiết.

Trong trường hợp này, bạn đang nhập cơ sở dữ liệu vectơ ChromaDB để lưu trữ các phần nhúng

và một hàm nhập các mô hình nhúng từ HuggingFace.

Sau đó xác định mô hình nhúng. Trong trường hợp này, bạn đang sử dụng mô hình nhúng từ HuggingFace.

Tiếp theo, thiết lập kho lưu trữ vector và ngữ cảnh lưu trữ của bạn. Trong trường hợp này, bạn đang sử dụng ChromaDB và sau đó

chuyển mô hình nhúng và ngữ cảnh lưu trữ vào VectorStoreIndex.

Sau đó chuyển các nút, mô hình nhúng và ngữ cảnh lưu trữ

vào VectorStoreIndex để tạo các phần nhúng bằng mô hình đã chọn

và lưu trữ các vectơ nhúng bên trong bộ lưu trữ liên tục được xác định bởi ngữ cảnh lưu trữ.

Do đó, cho dù bạn lưu trữ các vectơ nhúng trong bộ nhớ hay trong bộ lưu trữ liên tục,

Lớp VectorStoreIndex mạnh mẽ của LlamaIndex xử lý hiệu quả cả hai đoạn văn bản nhúng

và lưu trữ các kết quả nhúng trong kho lưu trữ vectơ.

Với VectorStoreIndex, lời nhắc ban đầu của người dùng, việc nhúng,

và các bước truy xuất có thể được kết hợp trong LlamaIndex bằng quy trình sau.

Đầu tiên, tạo công cụ truy xuất bằng cách gọi phương thức "as_retriever" trên VectorStoreIndex

đối tượng. Sau đó chuyển lời nhắc của người dùng tới phương thức truy xuất của đối tượng truy xuất để lấy

những kết quả có liên quan. Ngoài ra, nếu bạn cần kiểm soát số lượng mục tối đa được truy xuất,

chỉ định số lượng mục được truy xuất tối đa bằng cách đặt tương tự_top_k

tham số khi tạo đối tượng truy xuất.

Khi lời nhắc của người dùng được chuyển đến trình truy xuất này, nó sẽ truy xuất k nút nhiều nhất

tương tự như lời nhắc của người dùng từ kho lưu trữ vectơ, trong trường hợp này sẽ là 5 nút. Đã lấy được

các nút được trả về dưới dạng danh sách được xếp hạng với các nút giống nhau nhất ở đầu danh sách.

Bây giờ chúng ta hãy thảo luận về việc tăng cường nhanh chóng, truy vấn LLM và tạo phản hồi.

LlamaIndex có khả năng kết hợp tăng cường nhanh chóng,

Các bước truy vấn LLM và tạo phản hồi RAG bằng cách sử dụng bộ tổng hợp phản hồi.

Với các nút được nhắc và được truy xuất của người dùng, phương pháp tổng hợp của bộ tổng hợp phản hồi

tạo ra phản hồi từ LLM. Lưu ý rằng việc nhúng lời nhắc của người dùng,

tăng cường dấu nhắc và việc chuyển dấu nhắc tăng cường tới LLM được thực hiện trong

nền và người dùng không cần thực hiện thêm bước nào để thực hiện các bước này theo cách thủ công.

Với LlamaIndex, quy trình có thể được đơn giản hóa hơn nữa bằng cách sử dụng công cụ truy vấn.

Công cụ truy vấn của LlamaIndex kết hợp việc nhúng lời nhắc,

các bước truy xuất, tăng cường nhắc nhở, truy vấn LLM và tạo phản hồi,

loại bỏ nhu cầu truy xuất các nút theo cách thủ công và chuyển chúng đến bộ tổng hợp phản hồi.

Với lời nhắc của người dùng, phương thức truy vấn của công cụ truy vấn sẽ tạo ra phản hồi từ LLM.

Lưu ý rằng việc nhúng lời nhắc, truy xuất, tăng cường lời nhắc của người dùng,

và việc chuyển lời nhắc tăng cường tới LLM được thực hiện ở chế độ nền,

và người dùng không cần phải thực hiện thêm bước nào để thực hiện các tác vụ này một cách thủ công.

Kết quả là các công cụ truy vấn của LlamaIndex giảm đáng kể số lượng mã cần phải

được viết khi xây dựng một ứng dụng RAG. Và hãy nhớ những lời khuyên hữu ích này khi

tạo ứng dụng của bạn. Bạn có thể tùy chỉnh LlamaIndex

công cụ truy vấn bằng cách thay đổi LLM mặc định thành một công cụ khác mà bạn chọn,

xác định mẫu lời nhắc tùy chỉnh để tăng cường lời nhắc hoặc bằng cách chỉ định một trình truy xuất tùy chỉnh.

LlamaIndex cung cấp nhiều cách để tùy chỉnh quy trình RAG để phù hợp với nhu cầu của bạn

ứng dụng. Hãy xem lại những gì bạn đã học được. Trong video này, bạn đã học được rằng

LlamaIndex sử dụng lớp VectorStoreIndex để tạo và lưu trữ nhúng.

Bạn tạo công cụ truy xuất bằng cách gọi phương thức "as_retriever" trên

Đối tượng VectorStoreIndex. Sau đó, bạn chuyển lời nhắc của người dùng tới đối tượng truy xuất

phương pháp truy xuất để thu được kết quả phù hợp. Bộ tổng hợp phản hồi trong LlamaIndex kết hợp

tăng cường nhanh chóng, truy vấn LLM và tạo phản hồi trong một bước.

Bộ tổng hợp phản hồi sử dụng dấu nhắc ban đầu và các nút được truy xuất để tạo phản hồi,

tinh chỉnh nó nếu cần với các nút còn sót lại. Bạn có thể tùy chỉnh hành vi tổng hợp phản hồi

sử dụng các LLM hoặc mẫu nhắc nhở khác nhau. Một công cụ truy vấn có thể nén quá trình

hơn nữa bằng cách kết hợp nhúng dấu nhắc, truy xuất, tăng cường dấu nhắc, truy vấn LLM,

và tạo phản hồi RAG bước vào một vài lệnh đơn giản. Và một công cụ truy vấn có thể

được sửa đổi bằng cách thay đổi LLM mặc định, tùy chỉnh mẫu lời nhắc hoặc sửa đổi trình truy xuất.