# 03 - Học chuyển tiếp là gì

---

- [Giảng viên] Học chuyển tiếp

là một kỹ thuật học máy trong đó một mô hình được đào tạo

trên một tập dữ liệu lớn, có mục đích chung

được điều chỉnh cho một nhiệm vụ liên quan, thường chuyên biệt hơn.

Hãy xem xét một đầu bếp

người đã thành thạo các kỹ thuật nấu ăn cơ bản,

chẳng hạn như kỹ năng dùng dao, cân bằng hương vị và mạ.

Nếu đầu bếp này quyết định chuyên về ẩm thực Pháp,

họ không cần phải học lại những điều cơ bản về nấu ăn,

mà thay vào đó là trau dồi kiến thức chuyên môn của họ

bằng cách kết hợp các công thức nấu ăn mới

và các kỹ thuật đặc trưng của ẩm thực Pháp.

Tương tự, thay vì đào tạo một mô hình từ đầu,

học chuyển tiếp cho phép chúng tôi áp dụng mô hình được đào tạo trước

đã học cách biểu diễn

từ một tập dữ liệu lớn, đa dạng đến một nhiệm vụ liên quan mới,

giảm nhu cầu đào tạo mở rộng

trên một tập dữ liệu chuyên biệt nhỏ hơn.

Học chuyển tiếp đã trở thành nền tảng

của xử lý ngôn ngữ tự nhiên hiện đại.

Ví dụ, một dự án có quy mô lớn,

mô hình ngôn ngữ lớn được đào tạo trước như BERT, GPT và T5,

được đào tạo ban đầu hoặc kho văn bản lớn,

học các mẫu ngôn ngữ chung như ngữ pháp,

ngữ nghĩa và ngữ cảnh.

Tuy nhiên, chúng ta có thể điều chỉnh chúng cho phù hợp với những nhiệm vụ mới và cụ thể,

chẳng hạn như phân tích tình cảm, trả lời câu hỏi,

hoặc tóm tắt văn bản.

Chúng ta chỉ cần tinh chỉnh chúng

với một tập dữ liệu nhãn tương đối nhỏ.

Học chuyển giao rất quan trọng trong học sâu

vì một số lý do.

Đào tạo mạng lưới thần kinh sâu từ đầu

trên các tập dữ liệu lớn có thể tốn kém về mặt tính toán

và tốn thời gian.

Bằng cách bắt đầu với một mô hình được đào tạo trước,

bạn thường có thể đạt được hiệu suất tốt sau một phần nhỏ

của các lần lặp lại đào tạo, tiết kiệm cả thời gian

và tài nguyên.

Trong nhiều tình huống thực tế, việc thu thập

và gắn nhãn cho một tập dữ liệu khổng lồ cho một nhiệm vụ mới

là thách thức hoặc không thể.

Học chuyển giao giúp khắc phục tình trạng khan hiếm dữ liệu

bằng cách sử dụng các biểu diễn tính năng phong phú đã học

từ một tập dữ liệu phong phú hơn.

Những cách trình bày này mang lại cho mô hình mới một khởi đầu thuận lợi,

cho phép hiệu suất mạnh mẽ hơn trên dữ liệu hạn chế.

Các mô hình được đào tạo trước thường nắm bắt các tính năng chung, có thể sử dụng lại,

chẳng hạn như các cạnh và hình dạng trong hình ảnh

hoặc cấu trúc cú pháp và ngữ nghĩa trong văn bản.

Những tính năng này có thể được tinh chỉnh cho một vấn đề mới liên quan,

dẫn đến sự khái quát hóa mạnh mẽ.

Nếu không học chuyển giao, mô hình có thể quá phù hợp

hoặc đấu tranh để tìm hiểu các mẫu phức tạp khi dữ liệu thưa thớt.

Trong khi học chuyển giao ban đầu đã đạt được sự nổi bật

trong thị giác máy tính, nó hiện được sử dụng rộng rãi trong các lĩnh vực

như xử lý ngôn ngữ tự nhiên, xử lý âm thanh,

phân tích chuỗi thời gian và hơn thế nữa.

Bất cứ khi nào bạn có một tập dữ liệu nguồn lớn, mang tính đại diện

và một tập dữ liệu mục tiêu nhỏ hơn có liên quan,

học chuyển giao có thể là một chiến lược mạnh mẽ.

Trong nghiên cứu học sâu, học chuyển giao

đã xúc tác cho những đột phá bằng cách cho phép các nhà nghiên cứu

để xây dựng dựa trên các mô hình có hiệu suất cao đã được thiết lập.

Thực hành này tăng tốc độ thử nghiệm

và thúc đẩy sự đổi mới trong các lĩnh vực mới nổi

nơi thu thập lượng dữ liệu khổng lồ

vẫn chưa khả thi.

Trong phần tiếp theo của khóa học, chúng ta sẽ chuyển trọng tâm

chuyển giao việc học vào thực tiễn

bằng cách sử dụng các mô hình được đào tạo trước từ thư viện Ôm mặt.

Những mô hình này đang ở đỉnh cao

xử lý ngôn ngữ tự nhiên,

đã được đào tạo về kho văn bản lớn.

Thay vì xây dựng một mô hình từ đầu,

chúng ta có thể khai thác sự hiểu biết ngôn ngữ phong phú

những mô hình này đã sở hữu và điều chỉnh chúng

cho các nhiệm vụ chuyên biệt với chi phí tối thiểu.