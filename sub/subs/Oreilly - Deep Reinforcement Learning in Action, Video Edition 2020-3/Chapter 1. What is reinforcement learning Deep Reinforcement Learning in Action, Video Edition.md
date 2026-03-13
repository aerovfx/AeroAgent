# Chương 1. Học tăng cường là gì Học tăng cường sâu trong thực tế, Phiên bản video

---

Chương 1 Học tăng cường là gì?

Chương này bao gồm Đánh giá ngắn gọn về học máy

Giới thiệu học tăng cường như một trường con

Khung cơ bản của học tăng cường

Ngôn ngữ máy tính trong tương lai sẽ quan tâm nhiều hơn đến mục tiêu và ít quan tâm hơn đến thủ tục

do người lập trình quy định.

Marvin Minxie, Bài giảng ACM Turing năm 1970

Nếu bạn đang đọc cuốn sách này, có lẽ bạn đã quen với việc mạng lưới thần kinh sâu đến mức nào.

được sử dụng cho những việc như phân loại hoặc dự đoán hình ảnh, còn nếu không, hãy tiếp tục đọc.

Chúng tôi cũng có một khóa học cấp tốc về học sâu trong phần phụ lục.

Học tăng cường sâu (DRL) là một lĩnh vực con của học máy sử dụng học sâu

các mô hình (tức là mạng lưới thần kinh) trong các nhiệm vụ học tăng cường (RL), được xác định trong phần

1.2.

Trong phân loại hình ảnh, chúng ta có một loạt các hình ảnh tương ứng với một tập hợp các ảnh rời rạc.

các danh mục, chẳng hạn như hình ảnh của các loại động vật khác nhau và chúng tôi muốn có một máy học

mô hình để diễn giải một hình ảnh và phân loại loại động vật trong hình ảnh, như trong hình

1.1.

Hình 1.1 Bộ phân loại hình ảnh là một hàm hoặc học tập

thuật toán lấy hình ảnh và trả về nhãn lớp, phân loại hình ảnh thành

một trong số hữu hạn các loại hoặc lớp có thể có

Phần 1.1 Học tập tăng cường sâu

Mô hình học sâu chỉ là một trong nhiều loại mô hình học máy mà chúng ta có thể sử dụng

để phân loại hình ảnh.

Nói chung, chúng ta chỉ cần một số loại hàm nhận hình ảnh và trả về một lớp

nhãn (trong trường hợp này là nhãn xác định loại động vật nào được mô tả trong hình ảnh),

và thông thường chức năng này có một bộ tham số có thể điều chỉnh cố định.

Chúng tôi gọi những loại mô hình này là mô hình tham số.

Chúng ta bắt đầu với một mô hình tham số có các tham số được khởi tạo thành các giá trị ngẫu nhiên.

Điều này sẽ tạo ra các nhãn lớp ngẫu nhiên cho hình ảnh đầu vào.

Sau đó, chúng ta sử dụng quy trình huấn luyện để điều chỉnh các tham số, do đó hàm lặp lại

ngày càng tốt hơn trong việc phân loại hình ảnh một cách chính xác.

Tại một thời điểm nào đó, các tham số sẽ ở mức giá trị tối ưu, nghĩa là mô hình

không thể làm tốt hơn nhiệm vụ phân loại.

Các mô hình tham số cũng có thể được sử dụng để hồi quy, trong đó chúng ta cố gắng khớp mô hình với một tập hợp các giá trị

dữ liệu để chúng tôi có thể đưa ra dự đoán cho dữ liệu chưa nhìn thấy (Hình 1.2).

Một cách tiếp cận phức tạp hơn có thể hoạt động tốt hơn nếu nó có nhiều tham số hơn hoặc

kiến trúc bên trong tốt hơn.

Hình 1.2 Có lẽ mô hình học máy đơn giản nhất

là một hàm tuyến tính đơn giản có dạng f(x) = mx + b, với các tham số m, độ dốc và

b, sự đánh chặn.

Vì nó có các tham số có thể điều chỉnh được nên chúng tôi gọi nó là hàm hoặc mô hình tham số.

Nếu chúng ta có một số dữ liệu hai chiều, chúng ta có thể bắt đầu với một bộ tham số được khởi tạo ngẫu nhiên,

chẳng hạn như m = 3,4, b = 0,3, sau đó sử dụng thuật toán huấn luyện để tối ưu hóa các tham số cho phù hợp

dữ liệu huấn luyện, trong trường hợp đó tập tham số tối ưu gần với m = 2, b = 1.

Mạng lưới thần kinh sâu rất phổ biến vì trong nhiều trường hợp chúng là tham số chính xác nhất

mô hình học máy cho một nhiệm vụ nhất định, như phân loại hình ảnh.

Điều này phần lớn là do cách họ thể hiện dữ liệu.

Mạng lưới thần kinh sâu có nhiều lớp, do đó có độ sâu, tạo ra mô hình học hỏi

biểu diễn lớp của dữ liệu đầu vào.

Biểu diễn theo lớp này là một dạng tổng hợp, nghĩa là một phần dữ liệu phức tạp được biểu diễn

là sự kết hợp của nhiều thành phần cơ bản hơn và những thành phần đó có thể được chia nhỏ hơn nữa

thành các thành phần thậm chí còn đơn giản hơn, v.v., cho đến khi bạn đạt được đơn vị nguyên tử.

Ngôn ngữ của con người có tính cấu tạo (Hình 1.3).

Ví dụ, một cuốn sách bao gồm các chương, các chương bao gồm các đoạn văn, các đoạn văn.

bao gồm các câu, v.v., cho đến khi bạn có được các từ riêng lẻ, đó là

đơn vị ý nghĩa nhỏ nhất.

Tuy nhiên, mỗi cấp độ cá nhân đều truyền tải ý nghĩa.

Toàn bộ cuốn sách nhằm mục đích truyền đạt ý nghĩa, còn các đoạn riêng lẻ trong đó nhằm mục đích truyền tải ý nghĩa.

truyền tải những điểm nhỏ hơn.

Mạng lưới thần kinh sâu cũng có thể học cách biểu diễn thành phần dữ liệu.

Ví dụ: chúng có thể biểu diễn một hình ảnh dưới dạng thành phần của các đường viền nguyên thủy và

kết cấu, được tạo thành các hình dạng cơ bản, v.v., cho đến khi bạn có được kết cấu hoàn chỉnh

hình ảnh phức tạp.

Khả năng xử lý sự phức tạp với các biểu diễn thành phần phần lớn là điều tạo nên sự sâu sắc

học tập rất mạnh mẽ.

Hình 1.3.

Một câu như "John đánh bóng" có thể được chia thành những phần ngày càng đơn giản hơn

cho đến khi chúng ta nhận được các từ riêng lẻ.

Trong trường hợp này, chúng ta có thể phân tách câu, ký hiệu là "s", thành một danh từ chủ ngữ, "n",

và một cụm động từ, "vp".

"Vp" có thể được phân tách thành động từ "hit" và cụm danh từ "np".

Sau đó, "np" có thể được phân tách thành các từ riêng lẻ "the" và "ball".