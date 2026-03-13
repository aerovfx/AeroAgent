# 1 -Trích xuất thông tin từ tài liệu đã dịch

---

Trong các video trước, chúng ta đã thấy mã lấy thông tin, chẳng hạn như từ một tệp hoặc một trang web,

và xử lý nó bằng mô hình AI.

Tuy nhiên, điều gì sẽ xảy ra nếu chúng ta muốn làm việc với các tài liệu lớn hơn?

Chẳng hạn, điều gì sẽ xảy ra nếu chúng ta muốn có một cơ sở kiến thức được tạo thành từ nhiều tệp PDF hoặc chữ số?

lấy tập tin và vân vân?

Làm cách nào chúng tôi có thể lưu trữ tất cả thông tin đó để khi người dùng thực hiện một truy vấn liên quan, hệ thống

hoặc một số quy trình công việc có thể tự động truy xuất dữ liệu phù hợp nhất và tạo ra một quy trình phù hợp

phản hồi cho người dùng?

Đó là những gì chúng ta sẽ thấy trong phần này, cách tạo một ứng dụng kiểu RAC.

Trước đây chúng tôi đã phân tích rằng chúng tôi có thể thêm một thành phần để thực hiện một số loại xử lý.

Ví dụ: chúng ta có thể thêm một tập hợp tệp bằng thành phần thư mục này.

Chúng tôi cũng có thành phần tệp và thành phần URL, nhưng trong trường hợp này, chúng tôi sẽ kiểm tra bằng cách sử dụng

thành phần URL.

Về cơ bản, những gì chúng ta sẽ làm là phân tích một trang web có nội dung khá phong phú.

Ví dụ, đây là một bài viết từ Hiến pháp Hoa Kỳ.

Bạn có thể thấy chúng ta có khá nhiều văn bản chứa các đoạn thông tin bằng số,

nhưng mục tiêu của chúng tôi là lưu trữ nó thành từng phần trong cơ sở dữ liệu để chúng tôi có thể truy vấn nó sau này.

Bây giờ chúng ta hãy xem làm thế nào để làm điều đó.

Chúng tôi đã có URL ở đây.

Chúng tôi có thành phần URL.

Hãy nhớ rằng trước đó chúng ta đã xem xét một thành phần có tên là Split Text.

Đây rồi, Tách văn bản.

Tôi sẽ kéo nó và lưu ý rằng thành phần này cho phép chúng ta chia nhỏ rất lớn

văn bản thành các phần nhỏ hơn, giúp tránh việc có quá nhiều thông tin trong một bản ghi.

Bằng cách này, chúng ta có thể có được lượng thông tin nhỏ, vì vậy khi truy vấn hoặc sử dụng mô hình AA, chúng ta chỉ

chuyển ngữ cảnh phù hợp nhất liên quan đến việc sử dụng Squery.

Điều này cho phép chúng tôi nhận được câu trả lời chuyên biệt và chính xác hơn cho yêu cầu được đưa ra.

Vì vậy tôi sẽ sao chép URL này như một phần của thành phần URL.

Bạn có thể sử dụng cùng một URL hoặc bất kỳ URL nào khác mà bạn quan tâm.

Việc tôi làm tiếp theo là kết nối nút dữ liệu đầu ra từ URL tới Split Text.

Để khi chạy thành phần Split Text này, bạn có thể thấy nó trả về một tập hợp văn bản

đã được chia thành nhiều phần nhỏ.

Trong cột này gọi là Văn bản, chúng ta có từng phần thông tin liên quan đến một bài viết cụ thể

hoặc một phần của Hiến pháp mà chúng ta đang nói đến.

Bằng cách này, chúng tôi đã chia văn bản thành các phần nhỏ hơn.

Chúng tôi muốn bắt đầu tất cả nội dung trong một bản ghi duy nhất nhưng thay vào đó là những đoạn mã nhỏ.

Đây là phần dùng để thực hiện việc trích xuất thông tin, tài liệu.

Đó là điều rất đơn giản để thực hiện ở Lancthlo.