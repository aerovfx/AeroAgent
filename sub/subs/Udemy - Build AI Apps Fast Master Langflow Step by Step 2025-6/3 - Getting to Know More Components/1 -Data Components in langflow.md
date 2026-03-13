# 1 -Thành phần dữ liệu trong langflow được dịch

---

Bây giờ bạn đã biết cách hoạt động của dòng chảy dài và chúng tôi đã giới thiệu về chương trình,

hãy phân tích một số thành phần bạn có thể sử dụng trong các quy trình công việc khác nhau của mình.

Chúng tôi đã xem xét một số thành phần này trước đây, chẳng hạn như những thành phần được tìm thấy trong đầu vào

danh mục, các thành phần trong danh mục đầu ra và cả danh mục tôm.

Tuy nhiên, có những danh mục khác mà chúng ta có thể khám phá để tiếp tục khám phá các thành phần mới.

Hãy bắt đầu với các thành phần được tìm thấy trong phần được gọi là dữ liệu.

Các thành phần này sẽ cho phép chúng ta lấy thông tin từ một nguồn bên ngoài để sử dụng

dữ liệu từ, ví dụ: một số API có sẵn từ một hệ thống, trong số các API khác.

Đầu tiên, chúng ta có thành phần này được gọi là yêu cầu API, cho thấy nó cho phép chúng ta thực hiện các lệnh gọi HTTP

bằng cách sử dụng URL hoặc cũng có thể bằng lệnh Cure.

Cái này hoạt động thế nào?

Về cơ bản, bạn phải nhập vào đây URL bạn muốn gọi.

Trong trường hợp của tôi, tôi đã chuẩn bị sẵn một URL mà tôi đã cho bạn xem bên dưới.

Nếu chúng tôi truy cập URL này, bạn có thể thấy dữ liệu được hiển thị trực tiếp, được định dạng bởi

browser.

URL là một bài kiểm tra rất đơn giản, còn có tên khác là dummyjson.muck.bcptor.com.

Đây là URL và đây là phản hồi mà chúng tôi sẽ nhận được do lệnh gọi API này.

Khi URL được xác định, chúng tôi có một số tùy chọn cấu hình, chẳng hạn như phương thức HTTP để sử dụng.

Trong phần Điều khiển, bạn có thể thấy chúng ta có nhiều thuộc tính hơn mà chúng ta có thể cấu hình.

Nếu API hoặc lệnh gọi API của bạn yêu cầu bất kỳ cấu hình bổ sung nào, chẳng hạn như vị trí tham số,

so với nội dung trong yêu cầu hoặc tiêu đề, bạn có thể thêm các tiêu đề đó để tạo,

ví dụ: một số loại mã thông báo phản chiếu trong số những loại khác.

Tôi sẽ đóng cửa sổ này lại.

Đây là dữ liệu chúng tôi quan tâm.

Để chạy thử nghiệm này, hãy nhấp vào nút để bắt đầu thực thi thành phần và bạn sẽ thấy

rằng mọi thứ đều hoạt động chính xác.

Nếu chúng tôi kiểm tra nút này có nhãn dữ liệu, bạn có thể thấy rằng ở đây nguồn dữ liệu xuất hiện

cùng với kết quả, hiển thị chính xác nội dung mà chúng tôi nhận được khi đưa ra yêu cầu

trực tiếp trong trình duyệt.

Ngoài ra, nếu nhìn vào khung dữ liệu ở đây, chúng ta có thể thấy thông tin tương tự được hiển thị.

Một tính năng khác tôi thấy rất hữu ích trong thành phần này là chúng ta có thể sử dụng lệnh Cure

để thực hiện cuộc gọi dịch vụ.

Ví dụ, ở đây tôi có một lệnh sẽ chỉ cho bạn.

Đó là cái bạn nhìn thấy trên màn hình.

Tiếp theo, đây là lệnh Cure.

Chúng tôi sử dụng tham số trừ V và sau đó là URL.

Nếu có thêm thông số cần điền, chúng sẽ được cấu hình hoặc cấu hình sẵn tự động

trong lệnh này.

Khi chạy lệnh này, bạn có thể thấy tất cả thông tin cần thiết được hoàn thành tự động.

Hãy phân tích dữ liệu.

Và bạn có thể thấy rằng chúng ta lại nhận được kết quả chính xác một lần nữa, nhưng lần này sử dụng lệnh Cure.

Đó là cách thành phần yêu cầu LPI này hoạt động.

Tôi sẽ xóa nó vì bây giờ tôi muốn bạn xem thành phần tiếp theo có tên là thư mục.

Thành phần này cho phép chúng ta tải các tệp từ một thư mục và đặt đường dẫn, cũng như chọn các tệp cụ thể

tập tin chúng tôi muốn sử dụng.

Có điều gì đó tôi muốn đề cập đến về thành phần này.

Rất có thể nó sẽ sớm bị loại bỏ.

Trên thực tế, vào thời điểm bạn xem video này, thành phần này có thể không còn xuất hiện trong

danh sách chính thức của thành phần giao diện đồ họa vì tôi đã cho bạn xem một URL.

Đây là cuộc trò chuyện trong kho lưu trữ độ dài chính thức và bạn có thể xem phản hồi ở đây

từ máy tính của nhóm, người này chỉ ra rằng thành phần này không hoạt động như mong đợi và

sẽ bị loại bỏ.

Ông cũng đề nghị thay thế nó bằng một thành phần khác, thành phần loại tệp.

Nếu thành phần này không xuất hiện với bạn thì đó là do những gì tôi đã đề cập trước đó.

Trong trường hợp bạn muốn sử dụng chức năng tương tự, hãy thay thế thành phần thư mục bằng tệp

thành phần như bạn có thể thấy trên màn hình.

Chúng tôi đã xem xét ngắn gọn thành phần này trong phần trước.

Như bạn có thể nhớ, nó cho phép chúng tôi tải lên bất kỳ loại tệp nào.

Chúng tôi đã tải tệp PDF lên nhưng làm cách nào bạn có thể sửa đổi hoạt động của thành phần tệp?

Ví dụ: những gì bạn có thể làm là nén các tệp bạn muốn xử lý thành tệp zip.

Tôi đã từng làm điều đó trước đây.

Tôi sẽ chọn nó ở đây như một phần thuộc tính của tệp.

Ở đây tôi có tệp zip của mình.

Tôi sẽ tải nó lên.

Bạn có thể thấy nó hiện đã được tải lên.

Và điều tôi sắp làm là bắt đầu thực thi thành phần này, vì tôi muốn bạn thấy

những gì xuất hiện ở đây trong một đường dẫn.

Bạn có thể thấy ở đây mỗi đường dẫn của tệp chúng tôi đã thêm vào tệp zip đều được hiển thị.

Tại đây, bạn có thể xem tên của từng tệp, cho dù đó là tệp PDF, tệp XT, v.v.

Điều liên quan ở đây là tất cả thông tin từ mỗi bên đều là một phần của quy trình.

tập tin được lấy ở định dạng văn bản, cho phép bạn sử dụng thông tin này trong một trong các

các dòng chảy.

Do đó, đây là một thành phần rất hữu ích nếu bạn cần xử lý các tệp trong luồng của mình.

Và tôi sẽ xóa nó một lần nữa.

Bạn có thể thấy rằng chúng tôi đã tải lên một thành phần khác gọi là nhóm S3, cho phép chúng tôi

để tải tệp lên vùng lưu trữ S3.

Để làm điều này, bạn cần định cấu hình khóa truy cập dịch vụ AWS, khóa bí mật, nhóm

tên và chiến lược tải lên.

Bạn có thể định cấu hình điều này nếu bạn có tài khoản AWS.

Nếu không, bạn có thể tạo một cái.

Tôi tin rằng họ cung cấp một số khoản tín dụng miễn phí để bạn có thể dùng thử dịch vụ một thời gian.

Tiếp theo, bạn có thể thấy rằng chúng tôi có một thành phần được gọi là truy vấn SQL, hiện đang ở giai đoạn thử nghiệm.

Điều quan trọng cần lưu ý, như tôi đã đề cập trước đó, thành phần này hiện đang ở giai đoạn thử nghiệm.

phiên bản.

Có thể khi bạn xem video, thẻ beta này có thể không còn xuất hiện nữa

trên thành phần và hiệu suất của nó có thể hiệu quả hơn.

Tại sao?

Bây giờ tôi sẽ chỉ cho bạn cách thành phần này hoạt động.

Ý tưởng chính là có thể thực hiện các truy vấn trên cơ sở dữ liệu mà chúng tôi có quyền truy cập.

Bạn có thể mô phỏng điều này bằng cách truy cập một dịch vụ.

Trong trường hợp này, tôi đã tạo một tài khoản giả chỉ nhằm mục đích minh họa.

Dịch vụ này cho phép bạn sử dụng hoặc tạo cơ sở dữ liệu miễn phí, mặc dù có một số hạn chế nhất định.

Trong trường hợp của tôi, tôi đã tạo cơ sở dữ liệu SQL của mình và một cơ sở dữ liệu SQL hậu xử lý khác, nếu bạn có thể

nhìn thấy trên màn hình.

Bởi vì tôi đã tạo ra những cơ sở dữ liệu này nên tôi đã có sẵn thông tin ở đây về cách

kết nối với cơ sở dữ liệu cụ thể này.

Ở đây, tôi có URI kết nối, cho phép tôi kết nối với dịch vụ.

Vì vậy, quay lại truy vấn SQL hoặc trong thành phần này, tôi sẽ dán thông tin cơ sở dữ liệu của mình.

Tôi có thể để lại thông tin này như nó được.

Nếu tôi quay lại dịch vụ của mình và chúng tôi truy cập ứng dụng cho phép chúng tôi chạy truy vấn.

Tôi chạy truy vấn dựa trên cơ sở dữ liệu và thông tin tôi đã nhập trước đó cho việc này

bảng được hiển thị ở đây.

Tuy nhiên, nếu chúng ta quay lại thành phần, tôi sẽ dán cùng một truy vấn mà tôi đã sử dụng

trước đó.

Tôi sẽ thực thi thành phần đó và bạn sẽ thấy rằng không có vấn đề gì.

Kết nối là chính xác.

Ở đây, nếu chúng tôi phân tích văn bản, bạn có thể thấy rằng chúng tôi không nhận được bất kỳ phản hồi nào.

Nghĩa là, có vẻ như không có kết nối thành công vì lý do nào đó, mặc dù chúng tôi đã

xác nhận thông tin có tồn tại

Vì vậy, có thể là do thành phần này hiện ở định dạng tốt hơn.

Đó có thể là lý do tại sao chúng tôi không nhận được kết quả, nhưng về cơ bản đây là cách bạn sử dụng

thành phần.

Tôi sẽ xóa nó và tiếp theo chúng ta có thành phần URL mà tôi thấy rất thú vị

bởi vì nó cho phép chúng tôi lấy thông tin từ trang web của chúng tôi cũng như trích xuất văn bản từ

trang.

Ví dụ: hãy nhập trang web tài liệu tải độ dài chính thức và chạy thành phần.

Bạn có thể thấy rằng thông tin đã được xử lý.

Chúng tôi chọn biểu tượng này cho biết dữ liệu.

Bạn có thể thấy ở đây chúng ta đã có văn bản được trích xuất từ ​​​​thông tin.

Đó là một thành phần xử lý thông tin rất nhanh chóng.

Ở đây, chúng tôi có tin nhắn.

Trong trường hợp bạn chỉ cần văn bản để sử dụng nó trong một thành phần, ví dụ như từ OpenAI trong số

những người khác.

Vì vậy, đây là một thành phần rất hữu ích nếu bạn cần trích xuất thông tin

từ trang web của chúng tôi.

Thành phần này cũng sẽ hữu ích nếu bạn cần lấy thông tin từ các phần phụ trợ

có thể tồn tại trong URL này.

Bạn có thể xác định những điều này thông qua thuộc tính có tên MaxDeb.

Cuối cùng, chúng ta có thành phần có tên WebHook, cho phép chúng ta kết nối với một trong các

các thành phần sử dụng điểm cuối này được hiển thị trên màn hình.

Chúng tôi có thể kết nối từ một ứng dụng, dịch vụ hoặc trang web bên ngoài và bắt đầu thực hiện quy trình làm việc

đang xử lý thông tin, ví dụ như từ dữ liệu nhận được từ một bảng hoặc từ bên ngoài

máy chủ.

Điều này sẽ bắt đầu xử lý một luồng mà chúng tôi đã tạo trước đó.

Đây là các thành phần khác nhau được tìm thấy trong danh mục dữ liệu, rất hữu ích.