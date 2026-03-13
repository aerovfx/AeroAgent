# 02 thuật toán gần đúng-gần-gần-nhất-ann

---

Trong khi tìm kiếm từ khóa và ngữ nghĩa tạo thành nền tảng của một công cụ truy xuất sản phẩm,

khi bạn mở rộng quy mô các kỹ thuật này, các vấn đề mới sẽ phát sinh.

Nếu được triển khai một cách đơn giản, việc tìm kiếm vectơ ở các thang đo cụ thể sẽ kém,

đòi hỏi tài nguyên tính toán đáng kể và tăng thêm độ trễ cho hệ thống của bạn.

Hãy xem xét thuật toán tìm kiếm vectơ cơ bản để hiểu nguồn gốc của vấn đề,

và sau đó khám phá cách chúng tôi có thể cải thiện nó.

Hình thức truy xuất vectơ đơn giản nhất được gọi là tìm kiếm k-láng giềng gần nhất,

và đó là điều bạn đã thấy trong suốt khóa học cho đến nay.

Đầu tiên, bạn tạo một vectơ nhúng cho mọi tài liệu trong cơ sở kiến thức của mình,

cũng như lời nhắc của bạn.

Sau đó, bạn tính khoảng cách giữa vectơ nhắc và mọi vectơ tài liệu.

Sau đó, bạn sắp xếp tài liệu dựa trên khoảng cách của chúng với vectơ nhắc.

Sau đó người dùng có thể chọn một số, k,

đó chỉ là số lượng tài liệu lân cận gần nhất cần trả lại.

k-hàng xóm gần nhất rất dễ hiểu và dễ thực hiện.

Vấn đề là nó có quy mô khủng khiếp.

Số phép tính mà mỗi lần tìm kiếm yêu cầu

tăng tuyến tính theo số lượng tài liệu trong cơ sở tri thức.

Nếu bạn có một nghìn tài liệu thì với mỗi lần tìm kiếm, bạn phải tính một nghìn khoảng cách vectơ.

Tuy nhiên, nếu bạn có một tỷ tài liệu, bạn phải tính một tỷ khoảng cách vectơ.

Lần tìm kiếm thứ hai đó sẽ chậm hơn một triệu lần so với lần tìm kiếm đầu tiên.

Nếu muốn chú chó tha mồi của mình hoạt động tốt trên quy mô lớn, bạn sẽ cần một cách tiếp cận tốt hơn.

Để cải thiện k hàng xóm gần nhất,

Những kẻ săn mồi sử dụng một nhóm thuật toán được gọi là những người hàng xóm gần nhất gần đúng hoặc ANN.

Các thuật toán này sử dụng cấu trúc dữ liệu thông minh để cho phép tìm kiếm nhanh hơn đáng kể.

Để làm được điều này, họ phải hy sinh một chút về chất lượng của kết quả,

nghĩa là họ không được đảm bảo tìm được tài liệu gần nhất tuyệt đối trong cơ sở kiến thức,

mặc dù họ vẫn sẽ tìm thấy những cái ở rất gần.

Hãy xem xét một thuật toán ANN điển hình được gọi là thế giới nhỏ có thể điều hướng.

Trước khi thực hiện bất kỳ tìm kiếm nào, thuật toán sẽ tạo ra một cấu trúc dữ liệu được gọi là biểu đồ lân cận.

Để làm điều này, trước tiên, nó tính khoảng cách giữa mỗi vectơ và mọi vectơ khác.

Sau đó, bên trong biểu đồ vùng lân cận này, bạn thêm một nút cho mỗi tài liệu.

Cuối cùng, bạn tạo một cạnh giữa mỗi tài liệu và một số tài liệu khác gần nhất với nó.

Điều này dẫn đến một cấu trúc giống như web.

Bạn có thể tưởng tượng việc duyệt qua biểu đồ vùng lân cận bằng cách chuyển từ một tài liệu sang các tài liệu lân cận gần nhất

dọc theo các cạnh kết nối chúng.

Bây giờ, hãy xem biểu đồ lân cận này tăng tốc tìm kiếm như thế nào.

Khi nhận được lời nhắc, nó sẽ được vector hóa để tạo vectơ truy vấn.

Mục tiêu là tìm các tài liệu nằm gần vectơ truy vấn đó nhất.

Để làm điều đó, thuật toán chọn ngẫu nhiên một điểm vào, được gọi là vectơ ứng cử viên, để bắt đầu với,

đó chỉ là một trong các nút trong biểu đồ lân cận.

Đây là một lựa chọn thực sự ngẫu nhiên, không có giả định rằng nó thậm chí gần với vectơ gợi ý.

Bây giờ, thuật toán bắt đầu duyệt đồ thị.

Nó nhìn vào từng hàng xóm của vectơ ứng cử viên hiện tại

và tính toán cái nào trong số chúng gần nhất với vectơ nhắc.

Vì chỉ có một vài người hàng xóm cần xem xét nên quá trình này diễn ra rất nhanh.

Ai gần nhất sẽ trở thành ứng cử viên mới.

Bây giờ, quá trình lặp lại.

Tại mỗi vectơ ứng viên, thuật toán sẽ tìm xem vectơ lân cận nào được kết nối

gần nhất với vectơ truy vấn và trở thành ứng cử viên mới.

Quá trình tiếp tục cho đến khi không có hàng xóm nào gần hơn ứng cử viên hiện tại,

và vectơ ứng cử viên được trả về.

Với những sửa đổi nhỏ, phương pháp này có thể được thực hiện để trả về nhiều tài liệu,

nhưng ý tưởng cốt lõi vẫn giống nhau.

Bạn chỉ cần di chuyển qua biểu đồ khoảng cách, mỗi lần,

chọn bất kỳ người hàng xóm nào đưa bạn đến gần lời nhắc nhất.

Cách tiếp cận này không nhất thiết phải tìm ra vectơ tốt nhất có thể có trong biểu đồ tri thức.

Có thể có một cái ở ngoài đó gần với vectơ gợi ý hơn,

nhưng thuật toán sẽ không thể tiếp cận được,

bởi vì nó không thể chọn đường dẫn tổng thể tối ưu thông qua biểu đồ lân cận.

Chỉ là con đường tốt nhất trong từng thời điểm.

Tuy nhiên, trong thực tế, thuật toán này tìm thấy các vectơ rất gần nhau,

và nhanh hơn nhiều so với k hàng xóm gần nhất.

Mặc dù thuật toán thế giới nhỏ có thể điều hướng này đã hiệu quả hơn KNN, nhưng

một biến thể nhỏ được gọi là thế giới nhỏ có thể điều hướng theo thứ bậc, hay HNSW,

bổ sung thêm cải tiến bằng cách tăng tốc đáng kể các phần đầu của tìm kiếm.

HNSW phụ thuộc vào việc có biểu đồ lân cận phân cấp với nhiều lớp.

Đây là biểu đồ khoảng cách phân cấp có thể trông như thế nào

cho một nền tảng kiến thức với 1.000 tài liệu.

Lớp 1 chứa tất cả 1.000 vectơ,

và bạn tính toán biểu đồ lân cận như bình thường.

Ở lớp 2, bạn loại bỏ ngẫu nhiên tất cả trừ 100 vectơ,

và bạn tạo một biểu đồ lân cận mới chỉ cho 100 vectơ đó.

Cuối cùng, ở lớp 3, bạn loại bỏ ngẫu nhiên tất cả trừ 10 vectơ,

và một lần nữa, tạo biểu đồ lân cận cho 10 số còn lại.

Để tìm kiếm biểu đồ lân cận này, việc tìm kiếm bắt đầu ở lớp 3, lớp trên cùng.

Thuật toán chọn một điểm vào ngẫu nhiên trong lớp này,

và sau đó tìm kiếm như bình thường để tìm ra ứng viên tốt nhất ở lớp 3.

Sau đó, nó rơi xuống lớp 2,

bắt đầu từ ứng cử viên tốt nhất được tìm thấy ở lớp 3.

Vì ở đây có nhiều vectơ hơn,

có thể có một vectơ gần với vectơ gợi ý hơn.

Thuật toán di chuyển qua lớp 2 như bình thường

cho đến khi tìm được ứng viên tốt nhất ở lớp 2.

Tại thời điểm đó, nó rơi xuống lớp 1, mức thấp nhất,

có mọi vectơ trong cơ sở tri thức.

Thuật toán di chuyển qua lớp thấp nhất này như bình thường,

và lần này, ứng cử viên tốt nhất được tìm thấy là ứng cử viên mà thuật toán thực sự trả về.

Cách tiếp cận phân cấp này rất hiệu quả,

bởi vì ở các lớp cao nhất, thuật toán tạo ra những bước nhảy lớn

để đi vào vùng lân cận gần đúng của vectơ nhắc.

Vào thời điểm mọi vectơ có thể được xem xét ở lớp 1,

vectơ ứng cử viên phải rất gần với vectơ nhắc.

Thuật toán HNSW này nhanh hơn đáng kể so với tìm kiếm lân cận gần nhất k.

Khi bạn đi lên theo từng lớp, sẽ có ít vectơ để điều hướng hơn theo cấp số nhân,

và do đó thời gian chạy của HNSW xấp xỉ logarit,

trong khi KNN là tuyến tính.

Đây là điều cho phép tìm kiếm vectơ có quy mô lên tới hàng tỷ vectơ

và vẫn chỉ yêu cầu độ trễ vài trăm mili giây.

Bạn sẽ không cần triển khai các thuật toán ANN như thuật toán này,

nhưng hiểu được một số tính năng chính của chúng vẫn rất quan trọng.

Đầu tiên, chúng nhanh hơn đáng kể so với k hàng xóm gần nhất,

cho phép tìm kiếm vector vẫn có thể thực hiện được ở quy mô lớn.

Thứ hai, trong khi họ có xu hướng tìm các tài liệu gần với vectơ nhắc,

họ không thể đảm bảo rằng họ sẽ tìm thấy những kết quả phù hợp nhất.

Và cuối cùng, toàn bộ quá trình phụ thuộc vào việc xây dựng một biểu đồ lân cận tốt,

một quá trình tính toán khá chuyên sâu

may mắn thay có thể được tính toán trước trước khi nhận được bất kỳ lời nhắc nào.

Đó là một bản tóm tắt hay về cách thuật toán ANN giúp tìm kiếm vectơ trên quy mô lớn.

Vì vậy, bây giờ chúng ta hãy xem những công cụ bạn sẽ sử dụng để thực sự triển khai các thuật toán này.