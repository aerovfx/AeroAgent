# 42 - Giải thích về TensorFlow và Keras

---

Chào mừng trở lại, mọi người.

Trong bài giảng này, chúng ta sẽ thảo luận về sự khác biệt giữa dòng Tensor và Keris.

Vì vậy, trước khi chúng ta bắt đầu học cách viết mã mạng lưới thần kinh của riêng mình, tôi muốn nhanh chóng làm rõ sự khác biệt

giữa dòng tensor và sóng mang, vì đây là điểm gây nhầm lẫn phổ biến cho học sinh.

Như vậy là chúng ta đã học được tất cả các khía cạnh lý thuyết của mạng lưới thần kinh.

Bây giờ, ngay trước khi chúng ta bắt đầu viết mã, tôi muốn làm rõ một số điều.

Tensor Flow là thư viện deep learning mã nguồn mở được phát triển bởi Google với Tensor Flow 2.0 chính thức được phát hành

được phát hành vào cuối năm 2019.

Dòng Tensor có hệ sinh thái rộng lớn gồm các thành phần liên quan, bao gồm các thư viện như hỗ trợ trực quan hóa,

các tùy chọn triển khai và API sản xuất, cũng như hỗ trợ các ngôn ngữ lập trình khác nhau, không

chỉ là Python.

Caires là một thư viện Python cấp cao có thể sử dụng nhiều thư viện deep learning bên dưới.

nó có thể hoạt động trên các thư viện như Tenzer Flow, CMT hoặc THENO.

Luồng kéo căng một điểm X hoặc bất kỳ phiên bản một điểm nào đều có hệ thống lớp Python phức tạp để xây dựng

mô hình và vì nó phức tạp hơn một chút nên thư viện Keris cuối cùng trở thành một mô hình đơn giản hơn, nhiều hơn

API trừu tượng có thể chạy trên luồng Tensor.

Vì vậy Keris cuối cùng đã trở nên rất nổi tiếng.

Và nó phổ biến đến mức khi các nhà phát triển của Ton's Flow phát hành phiên bản 2.0, họ đã áp dụng

Carus là API chính thức cho Tenzer Flow.

Vì vậy, mặc dù Carus vẫn là một thư viện riêng biệt với luồng Tenzer, nhưng giờ đây nó cũng có thể được chính thức

được nhập thông qua dòng chảy Tenzer.

Vì vậy không cần phải cài đặt thêm Charice Cares giờ đã chính thức là một phần của Tenzer

flow và đó là API chính thức để flow chỉ ra và tiếp tục, vì việc thực hiện sẽ đơn giản hơn

sử dụng hơn hệ thống lớp con phức tạp hơn đã được sử dụng trong các phiên bản X một điểm X của Tenzer.

CPI, thật dễ dàng để sử dụng và xây dựng các mô hình bằng cách thêm các lớp chồng lên nhau thông qua các thao tác đơn giản

cuộc gọi.

Vì vậy, trong bài giảng tiếp theo, chúng ta hãy bắt đầu khám phá những kiến ​​thức cơ bản về Keris API cho Tensor Flow.

Tôi sẽ gặp bạn ở đó.