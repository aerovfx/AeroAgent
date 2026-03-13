# 5 -Django framework.en Mỹ

---

WEBVTT

Làm.

Vì vậy, đây là phần thứ hai của dự án mà chúng ta sẽ phát triển một trang web sử dụng khung Django.

Vì vậy, Django là đúng, vì vậy Django thực sự là một ứng dụng web mã nguồn mở và miễn phí được viết bằng Python.

Như tôi đã giới thiệu sơ qua cho bạn ở phần giới thiệu.

Giờ đây, cùng với tất cả chức năng mà Django cung cấp, bạn có thể tạo ứng dụng hoặc trang web của mình

từ mã nguồn hiện có thay vì tạo mã hóa từ đầu.

Vì vậy không có trang web.

Ngay cả những cái đơn giản được thiết kế bởi một người vẫn có thể bao gồm các chức năng nâng cao như xác thực,

hỗ trợ, bảng quản trị, hỗ trợ cho các tệp giao diện người dùng, hỗ trợ tải lên và hơn thế nữa.

Nói cách khác, nếu chúng ta tạo một trang web từ đầu, bạn cần xử lý giao diện người dùng

một phần.

Bạn cần xử lý phần phụ trợ.

Bạn sẽ cần xử lý xem cả hai có hoạt động bình thường hay không, có đồng bộ hóa hay không.

Bạn có thể đang sử dụng các phần mềm khác như MySchool hoặc PGA làm Postgres để lưu trữ dữ liệu của mình.

Sau đó, bạn cũng cần xem liệu trang web của bạn có hoạt động bình thường với dữ liệu của bạn hay không.

Nó có thể truy vấn dữ liệu hay không?

Phải.

Nhưng Django có mẫu mẫu.

Xem hệ thống kiến trúc ghi nhớ tất cả những điều đó và giúp bạn đáp ứng yêu cầu về giao diện người dùng

và quản lý cơ sở dữ liệu cho nhà phát triển.

Phải.

Vì vậy, đây là cách mà ngay cả một người cũng có thể xây dựng trang web bằng Django và làm việc đồng thời trong việc quản lý cơ sở dữ liệu

truy vấn hoặc ở giao diện người dùng hoặc hiển thị dữ liệu hoặc truy xuất dữ liệu và xử lý mọi thứ trong phần phụ trợ.

Vì vậy, hãy tiếp tục, trước tiên hãy xem cách khởi tạo dự án Django.

Tôi đã viết ra một số bước mà bạn có thể làm theo, nhưng một số bước chỉ dành cho tình huống

hoặc chỉ trong thời gian bạn thực sự tạo dự án Django của mình.

Vì vậy, vì bạn sẽ chỉ sử dụng mã này nên bạn không phải chạy tất cả các lệnh, nhưng một số lệnh

về các lệnh cụ thể mà tôi sắp nói với bạn.

Vì vậy, trong các bước bạn có thể thấy rằng trong tệp bước, việc đầu tiên là tạo một môi trường ảo.

Bây giờ bạn có thể thấy tôi đã tạo một cái rồi.

Bạn có thể thấy điều đó từ đây.

Nhưng giả sử bạn đang sử dụng ID như PI.

Vì vậy, bạn chỉ cần truy cập vào tập tin.

Bạn chỉ cần nhấp vào cài đặt và sau đó một cửa sổ bật lên sẽ mở ra nơi bạn có thể truy cập dự án.

Thông dịch viên Bên trong dự án của bạn.

Phải.

Bạn có thể nhấp vào Trình thông dịch dự án và sau đó bạn chỉ cần nhấp vào nút cài đặt ở đây để thêm.

Vâng.

Để thêm vào một môi trường ảo mới cho cơ sở mã này, bạn có thể thấy rằng bạn có thể tạo một môi trường mới

hoặc bạn cũng có thể sử dụng một cái hiện có.

Vì vậy, khi bạn tạo môi trường mới, nó sẽ tải.

Sau đó, khi hoặc nếu bạn đang sử dụng các ID khác, bạn có thể phải kích hoạt môi trường của mình từ dòng lệnh,

phải không?

Sau đó, những gì bạn phải làm là bạn phải làm.

Được rồi, vậy điều bạn phải làm tiếp theo là nếu bạn muốn sử dụng cơ sở mã hiện có, những mã

Tôi sẽ đưa cho bạn, sau đó điều tiếp theo sẽ thực sự là ta ta, ta ta.

Được rồi.

Vì vậy, có một lệnh mà bạn phải chạy, đó là.

Và Don Dash yêu cầu về việc nhắn tin.

Vì vậy, nếu bạn thực sự đang sử dụng cơ sở mã thì tất cả những gì bạn cần làm chỉ là cài đặt các gói và

các phần phụ thuộc mà mã yêu cầu để chạy.

Và điều tiếp theo bạn phải làm là vào bên trong thư mục của tôi ở đây.

Phải.

Vì vậy, thư mục dự án của tôi nằm ở bên trong, nơi tôi có thư mục trang web của mình ở đây.

Vì vậy, về cơ bản là bên trong đây.

Phải.

Tôi có tất cả các tệp này bên mình, vì vậy chỉ cần gõ lệnh.

Trình quản lý Python di chuyển.

Bây giờ, lệnh này dành riêng cho Django.

Và cái này làm gì?

Có phải khi bạn chạy lệnh này, tất cả các bảng cần được tạo bởi Django hoặc đã được

do bạn xác định bên trong Django.

Tất cả chúng sẽ được khởi tạo và tạo trong cơ sở dữ liệu mà bạn đang sử dụng.

Vì vậy, đó là lý do tại sao bạn cần chạy lệnh di chuyển này.

Nó cũng giúp thay đổi cấu trúc của cơ sở dữ liệu.

Nếu bạn có chuỗi thứ gì đó trong đó, bạn cần chạy lệnh di chuyển để tất cả những thay đổi đó được thực hiện

cũng được phản ánh trong cơ sở dữ liệu của bạn.

Vì vậy lệnh này rất quan trọng.

Và cuối cùng, bạn cần chạy lệnh python được quản lý hoặc thậm chí chạy lệnh máy chủ.

Vì vậy, quá trình này bắt đầu từ đây, máy chủ cục bộ trên máy của bạn.

Và sau đó bạn có thể truy cập và xem trang web hoạt động như thế nào.

Phải.

Bây giờ, nếu bạn định xây dựng một dự án Django từ đầu, bạn sẽ làm gì?

Điều đầu tiên là tôi có thể tạo một môi trường ảo.

Việc tiếp theo là cài đặt Django.

Bất kỳ phiên bản nào bạn muốn viết, bạn muốn sử dụng.

Sau đó, những gì bạn cần làm là chạy một lệnh đó là dự án Django Admin Start và sau đó là tên của

dự án.

Giống như tôi đã đặt tên cho trang web của mình.

Bạn có thể đặt bất kỳ tên nào.

Sau đó, bạn chỉ cần vào bên trong dự án ngay từ dòng lệnh và chạy lệnh Python

được quản lý bởi startup và tên của dự án là gì và ứng dụng là gì.

Tôi sẽ nói rõ điều đó sau, nhưng trước đó, đây là điều bạn cần làm để

cũng tạo một ứng dụng

Sau đó, bạn sẽ cần thiết lập mọi thứ bên trong cài đặt của mình mà tôi sẽ chỉ cho bạn sau một phút.

Và sau đó các dòng còn lại đều giống nhau đối với họ.

Phải.

Vì vậy, đây là trang web của tôi.

Dự án và dự án táo bạo này đã được tạo.

Vì vậy, bạn không cần phải chạy các lệnh đó.

Việc khởi động và ứng dụng dự án phải không?

Ngay cả ứng dụng phiên bản Django, bạn cũng không cần phải làm vậy.

Điều đó sẽ được chỉ định trong văn bản yêu cầu.

Vì vậy, hãy đi đến các cài đặt này theo từng tập tin.

Bây giờ bạn phải định cấu hình dự án Django để nó hoạt động theo mong muốn của bạn.

Nhưng bởi vì Django cung cấp cho bạn một dự án cơ bản nơi bạn có thể thêm mọi thứ vào chức năng xây dựng

mà bạn muốn, nhưng một lần nữa, bạn phải định cấu hình dự án Django để nó hoạt động tương ứng.

Và để định cấu hình điều đó, bạn cần thực hiện các thay đổi hoặc thực hiện các thay đổi.

Những thay đổi khác trong cài đặt chưa được xác minh, ít nhất là đối với dự án này.

Phải.

Vì vậy việc đầu tiên là phải có một khóa bí mật.

Khóa bí mật của bạn là thứ có thể được sử dụng để truy cập vào dự án rừng của bạn và có thể là một người và

người bên ngoài.

Nếu anh ta có chìa khóa.

Bạn có thể thực hiện nhiều thay đổi trong dự án của mình.

Sau đó, việc tiếp theo là thiết lập máy chủ được phép để thông báo rằng Django có thể nói chuyện hoặc kết nối

với cái nào với máy nào.

Vì vậy, quyền truy cập được chỉ định ở đây.

Sau đó, bạn có các ứng dụng đã cài đặt, như bạn có thể thấy, có thông báo phiên xác thực quản trị viên.

Vì vậy, đây là những ứng dụng dựng sẵn mà Django cung cấp cho bạn để bạn có thể sử dụng chức năng của nó thay vì

viết mã từ đầu.

Nhưng nếu bạn muốn thứ gì đó không được Django Jean cung cấp, hãy tạo ứng dụng của riêng bạn, phải không?

Như bạn có thể thấy ở đây, tôi đã chỉ định các ứng dụng.

Vì vậy, trong một dự án, bạn sẽ thấy các tệp như các cài đặt này theo từng tệp, tệp WCF và trong các ứng dụng, bạn sẽ

xem các tập tin như thế này

Vì vậy, đây chính là cách bạn triển khai phần phụ trợ của mình, kết nối công việc giao diện người dùng với các mô hình của bạn, tức là một lần nữa

cơ sở dữ liệu, phải không?

Và đây chỉ là để cấu hình toàn bộ dự án của bạn.

Tiếp theo là phần mềm trung gian.

Bây giờ, Django cũng xử lý phần mềm trung gian cho bạn.

Bạn không cần phải mã hóa bất cứ điều gì cụ thể ở đây.

Sau đó chúng ta có các mẫu.

Không có mẫu nào về cơ bản là các tệp HTML và CSS.

Những tệp được phân phối khi bạn nhấn một URL.

Phải.

Vì vậy, đó là tất cả các mẫu của biệt ngữ Django.

Tiếp theo là cơ sở dữ liệu.

Nếu bạn muốn sử dụng cơ sở dữ liệu có sẵn là ba, thì bạn có thể để nó giữ nguyên như cũ.

Nếu bạn có một số cơ sở dữ liệu của bên thứ ba khác hoặc rõ ràng là bên thứ ba như trường học của tôi hoặc Postgres, thì bạn

có thể thiết lập điều đó ở đây bằng cách thêm nhiều khóa hơn như tên người dùng máy chủ, mật khẩu, cả hai, v.v.

Việc này nhằm tạo ra tiền mặt.

Cách cất giữ tiền mặt, Cách lấy lại tiền mặt.

Vì vậy, một lần nữa, điều đó cũng được xử lý bởi Django.

Bạn chỉ cần xác định chính xác nó sẽ được xử lý như thế nào.

Được rồi, phần còn lại bây giờ không quan trọng lắm nên bạn không cần phải đi tìm hiểu

chi tiết đó.

Nhưng nếu muốn, bạn có thể truy cập tài liệu Dự án Django và từ tài liệu bạn có thể nhận được

một bức tranh khá rõ ràng về một số thứ mà tôi đã bỏ qua lúc này.

Được rồi.

Vì vậy, tôi có thể nói rằng điều này cũng đã xảy ra, hãy kiểm tra trong phần cài đặt rằng p y là một tệp được sử dụng

để biết các cấu hình để xử lý cách thức hoạt động của dự án.

Sau đó, việc tiếp theo là đi sâu vào ứng dụng và xem chúng tôi sẽ đưa chức năng đó vào như thế nào

bắt buộc phải ở bên trong trang web mà chúng ta đang xây dựng phải không?

Vì vậy, điều đó sẽ được đề cập trong video tiếp theo.