# 4 -Tạo công cụ dịch tùy chỉnh

---

Hình ảnh của Lancelot chắc chắn sẽ rất hữu ích với bạn đó là khả năng tạo các công cụ tùy chỉnh bằng mã Python.

Ví dụ: giả sử chúng ta muốn làm việc với hình ảnh thông qua dịch vụ OpenAI hoặc nền tảng tương tự.

Chúng tôi có thể sử dụng một thành phần mà chúng tôi đã thấy trước đây được gọi là yêu cầu API.

Tuy nhiên, đã có những thư viện được thiết lập tốt cung cấp thông tin chính xác cho những gì chúng ta cần.

Vì vậy, chúng tôi có thể thắc mắc tại sao lại sử dụng yêu cầu API.

Tương tự như vậy, việc sử dụng yêu cầu API cho các dịch vụ này không trực quan lắm đối với các đại lý.

Chúng tôi sẽ đề cập đến chủ đề này trong các video sau, đặc biệt khi có các thông số tùy chỉnh khác nhau.

Vậy làm thế nào chúng ta có thể tạo một thành phần tùy chỉnh?

Tôi sẽ xóa thành phần mà tôi đã thêm trước đó và thay vào đó chúng ta có thể kéo bất kỳ thành phần nào chúng ta muốn.

Điều khiến chúng tôi quan tâm là đi đến phần mã của thành phần nơi chứa mã nguồn được sử dụng riêng cho thành phần này.

Tôi sẽ xóa nội dung này và chúng ta sẽ tạo một thành phần từ đầu.

Điều đầu tiên chúng ta cần làm là sử dụng những hàng nhập khẩu cần thiết.

Trong trường hợp này, chúng tôi sử dụng các nội dung nhập khác nhau từ Lancelot và chúng tôi cũng sử dụng thư viện OpenAI để truy cập các dịch vụ của nó một cách liền mạch.

Bước tiếp theo là tạo một lớp bao gồm thành phần lớp cơ sở.

Hãy làm điều đó.

Lưu ý ở đây chúng ta có định nghĩa lớp này.

Trong trường hợp này, nó được gọi là thành phần E-Mash.

Chúng tôi đang sử dụng thành phần cơ bản được gọi là thành phần và ở đây chúng tôi xác định các thuộc tính khác nhau.

Ví dụ: display name sẽ là tên hiển thị cho người dùng.

Trong trường hợp này, đó là văn bản bạn nhìn thấy trên màn hình.

Chúng tôi cũng có phần mô tả cho phép người dùng hiểu cụ thể nội dung của thành phần này.

Chúng tôi cũng có một biểu tượng và tên nội bộ mà chúng tôi có thể sử dụng lại sau này trong cùng một mã nguồn.

Nếu chúng tôi lưu những thay đổi này, bạn có thể thấy rằng thành phần đó đã sửa đổi hoàn toàn hình thức trực quan của nó,

và bây giờ chúng tôi có một thành phần chức năng mà chúng tôi thậm chí có thể thực thi.

Đúng như mong đợi, chúng ta không nhận được kết quả vì thành phần này chưa thực hiện bất kỳ hành động nào,

nhưng giao diện đồ họa đã được tích hợp vào thành phần.

Tiếp theo, là một phần của mã, chúng ta phải xác định trường đầu vào sẽ là gì để cho phép người dùng định cấu hình thành phần này hoặc xác định cách thức hoạt động của nó.

Điều này được thực hiện thông qua một mảng, như bạn có thể thấy ở đây.

Ở đây chúng ta có phần đầu vào.

Chúng tôi xác định một vài đầu vào ở đây.

Đầu tiên là kiểu nhập văn bản tin nhắn, cho phép người dùng nhập văn bản vào hộp văn bản.

Chúng tôi có tên nội bộ được gọi là nhắc nhở và trong trường hợp cụ thể này, thuộc tính này là nhắc nhở.

Chúng tôi cũng thấy tên hiển thị sẽ hiển thị cho người dùng, cho phép họ nhập lời nhắc của mình.

Ngoài ra còn có thông tin được cung cấp để người dùng có thể tìm hiểu thêm về thành phần này,

cụ thể là chức năng của các hộp văn bản này.

Chúng tôi đang chỉ ra rằng nên nhập mô tả của hình ảnh vào đây và nếu có lỗi, bạn có thể đặt mô tả hình ảnh mới nếu muốn.

Trong trường hợp này, đó là mô tả về hình ảnh mà chúng ta muốn tạo và cuối cùng, chúng ta có một thuộc tính được gọi là chế độ công cụ,

cho phép chúng tôi chỉ ra liệu thành phần này có thể hoạt động như một công cụ cho một tác nhân hay không.

Chúng ta sẽ xem xét điều này sau để hiểu chính xác chế độ công cụ dùng để làm gì.

Ngoài ra, với tư cách là tham số thứ hai, chúng tôi chỉ định rằng chúng tôi muốn một đầu vào hoặc hộp văn bản thuộc loại đầu vào este bí mật.

Điều này có nghĩa là gì?

Chúng ta sẽ có thể nhập mật khẩu, chẳng hạn như khóa chúng ta cần để sử dụng dịch vụ bên ngoài, giống như chúng ta đã làm trong video trước.

Chúng tôi chỉ định tên, tên hiển thị và rất quan trọng là chúng tôi cũng cho biết liệu người dùng có bắt buộc phải nhập thông tin này trước khi sử dụng thành phần hay không.

Nếu chúng tôi kiểm tra và lưu các thay đổi, hai trường mà chúng tôi định cấu hình đã xuất hiện.

Bạn có thể xem về văn bản hoặc giá trị mặc định của lời nhắc cũng như tùy chọn chỉ định khóa nào bạn muốn sử dụng.

Trong trường hợp này, bạn đã lưu một biến toàn cục cho dịch vụ này.

Trong trường hợp của tôi, tôi sẽ sử dụng khóa OpenAI.

Một lần nữa, chúng ta chưa triển khai chức năng cho thành phần này nên nó sẽ chưa làm được gì cả.

Hãy quay lại phần mã và phần tiếp theo chúng ta cần khai báo là mảng đầu ra, mảng này sẽ xác định những giá trị nào mà thành phần sẽ trả về sau khi thực thi.

Vì vậy, tôi sẽ sao chép và dán một số mã mà tôi đã xác định trước đó, đây là mảng đầu ra.

Bạn có thể thấy ở đây một đầu ra đã được xác định, cho biết tên phát này sẽ là URL hình ảnh.

Chúng ta cũng có tên gọi là đầu ra và một loại, tương ứng với loại đầu ra của hàm này.

Trong trường hợp này, nó sẽ là một loại langflow cụ thể, là dữ liệu, để trả về mảng hoặc thông tin liên quan từ quá trình tạo hình ảnh.

Cuối cùng, chúng tôi chỉ định một phương thức đóng vai trò là con trỏ tới thủ tục, chúng tôi sẽ thực thi để tạo đầu ra này.

Phương pháp này thực sự sẽ là đặc tả chức năng của thành phần.

Ví dụ: một định nghĩa rất đơn giản có thể là định nghĩa tôi sẽ trình bày tiếp theo.

Bạn có thể thấy rằng một phương thức được gọi là đầu ra xây dựng đã được xác định và về cơ bản, phương thức này trả về một thông báo có văn bản, chính là lời nhắc thứ ba của người dùng.

Tôi đang làm điều này chỉ nhằm mục đích trình diễn.

Điều tôi muốn bạn quan sát là phương thức này đề cập đến hàm mà chúng ta đã xác định, hàm này chỉ trả về một đối tượng thông báo có văn bản do người dùng cung cấp trong dấu nhắc.

Chúng tôi lưu các thay đổi, bạn có thể thấy rằng không có lỗi nào xuất hiện.

Hãy chạy thành phần này và vì chúng tôi đã có chức năng cụ thể nên nếu chúng tôi kiểm tra kết quả đầu ra, bạn sẽ nhận thấy nó hiển thị cùng một văn bản đầu vào, người dùng đã nhập,

và phần đầu ra này được gọi là URL hình ảnh mà chúng tôi đã xác định trước đó.

Bây giờ, là một phần của dịch vụ OpenAI trong phần tạo hình ảnh, bạn có thể thấy mã nguồn mẫu đó được hiển thị ở đây bằng các ngôn ngữ lập trình khác nhau.

Chúng tôi sẽ tập trung vào Python.

Tại đây, bạn có thể xem đoạn mã sẽ sử dụng để tạo hình ảnh này một cách dễ dàng.

Vì vậy, chúng ta có thể sao chép mã nguồn này và chuyển nó sang langflow trong phần mã.

Tôi đã mã hóa trước chức năng này và tôi có nó trong phần này, đồng thời tôi sẽ xóa định nghĩa đầu tiên khỏi đầu ra của bản dựng ban đầu và thay vào đó, tôi đã có định nghĩa cuối cùng cho phép chúng tôi tạo một đối tượng dữ liệu.

Bạn có thể thấy rằng chúng tôi có một số định nghĩa biến cho phép chúng tôi hoàn thành lời nhắc, phù hợp với lời nhắc của người dùng.

Chúng tôi cũng đã truy xuất khóa API từ dịch vụ mà người dùng đã nhập trước đó như một phần của thành phần.

Chúng tôi cũng có định nghĩa cho ứng dụng khách OpenAI, trong đó khóa sản phẩm được chỉ định và cuối cùng, phương thức được tạo từ hình ảnh sẽ được sử dụng để tạo hình ảnh.

Trong trường hợp cụ thể này, chúng tôi sử dụng mô hình then-e3, chỉ định lời nhắc, cho biết chúng tôi chỉ muốn tạo một hình ảnh và chọn định dạng ngang cho kích thước.

Cuối cùng, chúng tôi xác định rằng chúng tôi chỉ quan tâm đến việc lấy URL hình ảnh.

Vì vậy, đây là dữ liệu sẽ được trả về như một phần của chức năng này.

Chúng tôi lưu các thay đổi và chạy lại thành phần này, giờ đây với chức năng thực sự tạo ra hình ảnh bằng dịch vụ OpenAI.

Sau vài giây, bạn có thể xác nhận rằng không có lỗi nào xuất hiện.

Hãy kiểm tra kết quả. Ở đây chúng ta có thể thấy một URL đã được tạo. Tôi dán nó vào trình duyệt.

Bạn có thể thấy rằng ở đây chúng tôi có một hình ảnh được tạo bằng Đạt Lai Lạt Ma theo định dạng mà chúng tôi đã chỉ định, vì đó là những thông số đầu vào mà chúng tôi đã đặt.

Nhóc, cháu có thể sửa đổi lời nhắc và sử dụng bất cứ thứ gì cháu thích.

Chúng tôi sẽ sử dụng lại thành phần này sau trong khóa học.