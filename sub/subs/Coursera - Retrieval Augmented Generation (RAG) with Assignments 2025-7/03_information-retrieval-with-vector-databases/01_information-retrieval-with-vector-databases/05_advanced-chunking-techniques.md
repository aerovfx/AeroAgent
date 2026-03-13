# 05 kỹ thuật chunking nâng cao

---

Việc chia nhỏ có nhiều lợi ích, nhưng bằng cách chia tài liệu thành các phần nhỏ hơn,

nó cũng có nguy cơ chia nhỏ văn bản theo cách làm mất đi ngữ cảnh liên quan.

Xét câu,

Đêm đó cô mơ, như cô thường làm, rằng cuối cùng cô đã trở thành nhà vô địch Olympic.

Tùy thuộc vào vị trí của đường phân chia, đoạn này có thể khiến nó trông giống như người mơ mộng của chúng ta.

đã giành được huy chương vàng và thay vào đó không mơ về vinh quang trong tương lai.

Kích thước cố định và phân tách ký tự đệ quy không cung cấp biện pháp bảo vệ chống lại loại vấn đề này.

Vì vậy, hãy xem xét một số kỹ thuật nâng cao hơn nhằm cố gắng xây dựng một cách thông minh

các khối dựa trên ý nghĩa của một đoạn văn bản.

Kỹ thuật đầu tiên chúng ta sẽ khám phá được gọi là phân đoạn ngữ nghĩa,

cố gắng ghép các câu lại với nhau thành từng đoạn nếu chúng có ý nghĩa tương tự nhau.

Thuật toán hoạt động bằng cách di chuyển qua tài liệu từng câu một.

Đối với mỗi câu, nó sẽ quyết định xem nó có đủ giống với các câu trước hay không,

và do đó thuộc cùng một đoạn hoặc khác nhau.

Để làm điều này, cả nội dung của đoạn hiện tại và câu tiếp theo đều được vector hóa.

Nếu hai vectơ nằm cách nhau một khoảng cách dưới một ngưỡng nào đó,

chúng có ý nghĩa tương tự nhau và các câu được thêm vào cùng một đoạn.

Quá trình này tiếp tục cho đến khi đoạn phát triển quá khác so với đoạn sau

câu. Tại thời điểm đó, bạn cắt đoạn đó và bắt đầu lại toàn bộ quá trình từ câu tiếp theo.

Khi bạn vẽ biểu đồ này ra, nó trông giống như biểu đồ này.

Ngưỡng cho khoảng cách vectơ hoặc độ khác nhau có màu đỏ.

Thước đo mức độ khác biệt của đoạn phát triển với câu

theo sau nó được biểu diễn bằng đường đỉnh.

Cuối cùng, khoảng cách giữa đoạn và câu tiếp theo vượt qua ngưỡng,

và một đoạn mới được tạo ra.

Kết quả của quá trình này là các khối có kích thước khác nhau đi theo dòng suy nghĩ của

tác giả. Ví dụ: nếu tác giả đi chệch hướng khái niệm trong một đoạn văn,

hoặc theo đuổi cùng một ý tưởng trong hai đoạn văn liên tiếp,

phân đoạn ngữ nghĩa sẽ đặt các phân chia khối tại các vị trí thích hợp.

Như bạn có thể tưởng tượng, việc phân chia ngữ nghĩa có thể tốn kém về mặt tính toán vì

bạn đang tính toán nhiều lần các vectơ cho mỗi câu trong cơ sở kiến ​​thức của mình.

Tuy nhiên, đổi lại bạn sẽ thường nhận được truy xuất chất lượng cao

được đo bằng các số liệu quen thuộc như độ chính xác và khả năng thu hồi.

Để linh hoạt hơn nữa, bạn có thể thử phân đoạn dựa trên mô hình ngôn ngữ lớn.

Tại đây, bạn đưa tài liệu của mình vào một mô hình ngôn ngữ,

cùng với hướng dẫn về các loại chunk mà bạn muốn tạo.

Ví dụ: bạn yêu cầu nó phân tách các phần dựa trên ý nghĩa,

giữ các khái niệm tương tự lại với nhau trong một đoạn,

và tách văn bản thành nhiều phần khi thảo luận về chủ đề mới.

Sau đó, mô hình ngôn ngữ sẽ tạo ra đoạn đầu ra giống như cách nó có thể tạo ra bất kỳ văn bản nào khác.

Mặc dù về bản chất là một cách tiếp cận hộp đen,

đây thực sự là một chiến lược chunking có hiệu suất rất cao.

Và khi chi phí mô hình ngôn ngữ giảm,

Phân đoạn dựa trên LLM thậm chí còn trở nên khả thi hơn về mặt kinh tế.

Cải tiến cuối cùng cho bất kỳ chiến lược chunking nào

là sử dụng mô hình ngôn ngữ để thêm ngữ cảnh vào từng đoạn.

Ví dụ: bạn có thể yêu cầu mô hình ngôn ngữ tạo các đoạn từ một tài liệu,

mà còn thêm văn bản tóm tắt vào đoạn giải thích ngữ cảnh của nó trong tài liệu rộng hơn.

Một tác giả có thể kết thúc một bài đăng trên blog bằng cách cảm ơn một danh sách những người ủng hộ và đóng góp.

Điều đó có nghĩa là sẽ có một đoạn ở gần cuối bài viết blog

đó chỉ là một danh sách dài các tên, khiến cho phần đó khó diễn giải riêng lẻ.

LLM có thể thêm văn bản vào đoạn giải thích ngữ cảnh của nó trong bài đăng blog rộng hơn.

Văn bản được thêm này có sẵn cả khi đoạn được vector hóa,

giúp thúc đẩy mức độ liên quan tìm kiếm lớn hơn,

và khi đoạn đó được lấy ra,

cuối cùng giúp LLM hiểu được ý nghĩa tổng thể của đoạn.

Phân đoạn nhận biết ngữ cảnh yêu cầu tiền xử lý tốn kém về mặt tính toán

vì LLM cần phải xem xét toàn bộ nền tảng kiến thức của bạn,

một tài liệu và chia nhỏ từng phần để thêm ngữ cảnh.

Tuy nhiên, lợi ích là những tìm kiếm phù hợp hơn

và về cơ bản không ảnh hưởng đến tốc độ tìm kiếm.

Hầu hết các hệ thống RAG sẽ thực hiện một số kiểu phân đoạn.

Tuy nhiên, việc sử dụng cách tiếp cận phức tạp đến mức nào sẽ phụ thuộc vào ngữ cảnh.

Phân tách ký tự có kích thước cố định hoặc đệ quy thường là điểm khởi đầu tốt

khi tạo nguyên mẫu một hệ thống và là những cách tiếp cận mặc định tốt.

Phân đoạn ngữ nghĩa và dựa trên LLM có thể dẫn đến hiệu suất cao hơn,

nhưng chúng tốn kém về mặt tính toán và có thể khó điều chỉnh, bảo trì hoặc kiểm tra.

Sẽ có ý nghĩa hơn khi thử nghiệm với một tập hợp con nhỏ dữ liệu của bạn

và xem liệu những kỹ thuật tiên tiến hơn này có

đang thực sự dẫn đến những cải tiến về mức độ liên quan của tìm kiếm.

Vì việc phân chia theo ngữ cảnh có thể được áp dụng trên bất kỳ chiến lược phân chia nào

và có thể cải thiện cả mức độ liên quan của tìm kiếm và thế hệ tiếp theo,

nó thường có thể là một cải tiến tốt đầu tiên để khám phá ngoài các kỹ thuật có chiều rộng cố định.

Là nhà thiết kế hệ thống RAG,

mục tiêu không phải là triển khai kỹ thuật phân chia tiên tiến nhất trên thị trường.

Đó là để hiểu những tùy chọn nào có sẵn, mức độ phù hợp của chúng với dữ liệu của bạn,

và liệu chi phí và lợi ích có đáng để triển khai trong hệ thống của bạn hay không.

Hy vọng rằng, cuộc khảo sát nhanh về kỹ thuật chunking này

cung cấp cho bạn một nền tảng vững chắc để đưa ra những quyết định đó.