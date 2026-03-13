# 2 -Thiết lập công cụ trả phí trong langflow dịch

---

Là một phần của các thành phần trong Lanclow, điều quan trọng cần biết là có sẵn các công cụ trả phí.

Điều này không có nghĩa là bạn phải trả tiền trực tiếp cho Lanclow để sử dụng chúng.

Thay vào đó, trước tiên bạn phải tạo một tài khoản với một dịch vụ bên ngoài cụ thể và lấy chìa khóa để truy cập dịch vụ.

Bạn có thể tìm thấy điều này trong danh mục Công cụ nơi bạn có thể thấy chúng tôi có một số thành phần như Công cụ AstraDB, là API tìm kiếm.

Nếu chúng tôi kéo bất kỳ thứ nào trong số này, thông thường họ sẽ yêu cầu bạn nhập một số loại khóa để có thể sử dụng dịch vụ.

Một số dịch vụ cấp cho bạn tín dụng hàng tháng sau khi bạn đăng ký.

Ví dụ: trong số các thành phần, chúng tôi có một thành phần gọi là API máy chủ Google, có xu hướng...

Thành phần này cho phép chúng tôi thực hiện tìm kiếm các kết quả của Google để lấy URL chẳng hạn và thực hiện nghiên cứu sâu hơn.

Tôi đã tạo một tài khoản trên SetPair.DevSight, liên kết mà bạn có thể nhìn thấy trên màn hình.

Bạn có thể truy cập URL serpair.dev và đăng ký tài khoản.

Khi bạn đã đăng ký và xác minh tài khoản của mình, bạn có thể đi tới phần có tên Khóa API nằm ở phía bên trái.

Một chìa khóa sẽ xuất hiện ở đây. Bấm vào Sao chép để sao chép khóa API.

Sau khi sao chép khóa sản phẩm, hãy quay lại Lanclow và dán khóa của bạn vào trường hoặc thuộc tính có nhãn Khóa API Serpair.

Nếu muốn sử dụng lại dịch vụ nhiều lần, bạn có thể tạo một biến mới.

Đó là những gì tôi sẽ làm.

Mình sẽ đặt tên là Serpair API key rồi dán Product key vào.

Tôi sẽ cho biết rằng tôi muốn lưu biến này để chúng ta có thể sử dụng lại nó nhiều lần nếu cần mà không gặp rủi ro hoặc không cần phải sao chép và dán khóa API.

Bây giờ, bên trong thành phần này, chúng ta thấy một trường đầu vào nơi chúng ta có thể nhập bất kỳ cụm từ tìm kiếm nào, chẳng hạn như Flother và chỉ định, chẳng hạn như chúng ta muốn nhận được ba kết quả.

Hãy chạy thành phần.

Và sau vài giây, chúng ta thấy kết quả.

Ở đây chúng tôi có ba kết quả mà chúng tôi yêu cầu.

Chúng tôi có các đoạn mã cho từng trang và quan trọng nhất là URL mà chúng tôi có thể khám phá sau này, lấy thông tin, tạo bản tóm tắt hoặc thực hiện bất kỳ tác vụ nào chúng tôi cần với dữ liệu chính hãng hoặc đã được xác minh từ các trang web.

Hãy phân tích một thành phần khác.

Trong các công cụ này, chúng ta có một thành phần khác gọi là Pavili, được tìm thấy trong phần này.

Chúng tôi có một thành phần cho phép chúng tôi thực hiện tìm kiếm thông qua API.

Tatili Search là công cụ tìm kiếm được tối ưu hóa cho mô hình LLM hoặc AI và RAC được thiết kế để cung cấp kết quả được tối ưu hóa chỉ chứa thông tin phù hợp nhất từ ​​một trang web, do đó, nó có thể được chuyển sang mô hình AI cho nhiệm vụ cụ thể.

Một lần nữa, bạn có thể truy cập trang web Pavili.com.

Bạn có thể tạo tài khoản trong quá trình đăng ký và sau khi có tài khoản, bạn có thể chuyển đến phần tổng quan.

Bạn sẽ thấy một phần có tên là Khóa API nơi bạn có thể tạo khóa mới.

Sau khi có nó, bạn chỉ cần chọn tùy chọn sao chép nó từ sản phẩm.

Bạn có thể tạo một biến toàn cục mới như một phần của độ dài tải của từ.

Hãy dán giá trị.

Hãy chỉ định rằng tên sẽ là khóa api tabli.

Chúng ta sẽ lưu biến này và có thể sử dụng nó bất cứ khi nào chúng ta cần.

Bây giờ, như một phần của tìm kiếm, chúng ta sẽ sử dụng thuật ngữ langflow và quan sát kết quả nào được trả về khi thành phần này được thực thi.

Chúng tôi đã xem xét dữ liệu và như bạn có thể thấy, lần này chúng tôi thu được nhiều kết quả hơn.

Điều thực sự quan trọng đối với chúng tôi là nội dung.

Lưu ý cách nội dung được tối ưu hóa hoặc bất kỳ mã nào không thuộc về truy vấn văn bản thông thường đều đã bị xóa.

Ví dụ: tất cả mã nguồn và các thành phần khác sẽ không phải là một phần của tìm kiếm tabli.

Vì vậy, chỉ những phần có liên quan nhất mới được trích xuất để gửi trực tiếp đến mô hình AI, cho phép xử lý một số thông tin nhất định hiệu quả hơn mà không cần sử dụng nhiều mã thông báo.

Đôi khi, một trang web có thể trả về nhiều thông tin không liên quan, điều này có thể khiến bạn sử dụng quá nhiều token.

Đây là cách bạn có thể định cấu hình một số nhóm trả phí trong trường hợp bạn quan tâm đến việc sử dụng bất kỳ thành phần nào trong số này như một phần của luồng trong langflow.