# 002 ESP-IDF Build System & CMake Tổng quan vi

---

Trước khi thiết lập mẫu dự án, hãy xem lại và làm quen với dự án ESP IDF hoạt động như thế nào

được tổ chức và xây dựng.

Vì vậy, trong bài học này, chúng ta sẽ xem xét các tài liệu ấn tượng và tìm hiểu chi tiết về

các chủ đề sau liên quan đến hệ thống build ESP, IDF.

Nhưng trước tiên, hãy đặt điều này vào bối cảnh bằng cách xem những thành phần nào có thể được đưa vào ESP

Dự án IDF cho một ứng dụng máy chủ web hiển thị độ ẩm.

Trong ví dụ này, bạn có thể có các thư viện cơ sở ESP, IDF, trình điều khiển WiFi, ngăn xếp IP TCP, miễn phí

hệ điều hành của ô tô, máy chủ web và trình điều khiển cho cảm biến độ ẩm và việc buộc mã chính

tất cả cùng nhau.

Vì vậy, các thành phần ESP, IDF có thể được cấu hình và hệ thống xây dựng sẽ biên dịch dự án dựa trên

các cài đặt cấu hình.

Ngoài ra, hệ thống xây dựng cần biết các thành phần tùy chỉnh và mã ứng dụng của bạn nằm ở đâu.

Vì vậy, để tìm hiểu về Hệ thống xây dựng ESP IDF, chúng ta sẽ xem xét các khái niệm hệ thống xây dựng cơ bản và các khái niệm khác nhau.

phương pháp sử dụng hệ thống xây dựng và CMYK.

Sau đó, chúng ta sẽ xem xét một ví dụ, thiết lập dự án và xem xét sâu hơn về dự án,

xem, tạo tệp danh sách và cả cách tạo thành phần tối thiểu.

C Tạo tập tin này.

Được rồi.

Vì vậy, liên kết này cung cấp mô tả về các khái niệm được liệt kê ở đây và điều này có vẻ khá cơ bản đối với

một số, nhưng điều này rất quan trọng.

Thuật ngữ của Dự án ESP IDF.

Vì vậy, dự án là một thư mục chứa tất cả các tệp và cấu hình để xây dựng một ứng dụng hoặc tệp thực thi duy nhất,

cũng như các phần tử hỗ trợ như dữ liệu bảng phân vùng, phân vùng hệ thống tệp và bộ tải khởi động.

Vì vậy thư mục dự án là thư mục cấp cao nhất ở đây.

Và liên quan đến bảng phân vùng, chúng ta sẽ tìm hiểu thêm chi tiết trong phần cập nhật chương trình cơ sở OTA, nhưng

về cơ bản nó là một tệp CSV được lưu trữ trong flash để chỉ định nhiều loại dữ liệu khác nhau cho các phân vùng cụ thể.

Và những bảng này có thể được tìm thấy khi chuỗi công cụ của bạn được cài đặt và của tôi được cài đặt vào đường dẫn ở đây.

Và để cung cấp cho bạn ý tưởng cơ bản, tôi đã sửa đổi bảng phân vùng này để chứa hai phân vùng OTA,

một để cập nhật và một để chạy ứng dụng.

Và nó cũng chứa các phần dành cho dữ liệu OTA lưu trữ không biến đổi mà bộ nạp khởi động cần biết

Ứng dụng OTA nào sẽ thực thi và chống lại dữ liệu init chịu trách nhiệm về lớp mạng vật lý

thông tin liên lạc.

Và một lần nữa, chúng ta sẽ xem xét kỹ hơn vấn đề này trong phần cập nhật OTA.

Vì vậy, chúng tôi cũng có cấu hình dự án được lưu giữ trong một tệp duy nhất gọi là cấu hình SDK.

nằm trong thư mục gốc của dự án.

Tệp cấu hình này được sửa đổi thông qua cấu hình menu py IDF để tùy chỉnh cấu hình của

dự án.

Nhưng để thuận tiện cho chúng ta, thay vì sử dụng cấu hình menu dòng lệnh, chúng ta sẽ sử dụng ID để sửa đổi

tệp cấu hình Sdhc và chúng tôi thực sự sẽ cập nhật tệp này trong quá trình thiết lập mẫu dự án.

Nhưng nếu bạn tò mò và muốn biết cách gọi cấu hình menu IDF py, bạn có thể truy cập ESP

Dòng lệnh IDF hoặc ESP IDF PowerShell, đi kèm với quá trình cài đặt mà bạn đã hoàn tất.

Và đầu tiên bạn vào thư mục dự án của bạn.

Sau đó sử dụng lệnh cấu hình menu py IDF.

Và đây là cấu hình menu mà bạn có thể sử dụng để cập nhật tệp cấu hình sdhc.

Tiếp theo, chúng tôi có một ứng dụng có thể thực thi được xây dựng bởi ESP, IDF, một dự án duy nhất.

Chúng tôi thường xây dựng hai ứng dụng, một ứng dụng dự án là ứng dụng thực thi chính là chương trình cơ sở tùy chỉnh của bạn

và một ứng dụng bootloader, đây là chương trình bootloader ban đầu khởi chạy ứng dụng dự án.

Ngoài ra, còn có các thành phần là các đoạn mã độc lập theo mô-đun được biên dịch thành tĩnh

thư viện hoặc tập tin và được liên kết vào một ứng dụng.

Một số được cung cấp bởi chính ISP, trong khi một số khác có thể được lấy từ những nơi khác.

Ví dụ: Thư viện cảm biến Libs ESP IDF này ở đây chứa một số thành phần và liệu bạn có

tích hợp các thành phần như thế này vào dự án của bạn hoặc viết mã tùy chỉnh mà bạn muốn chia thành các phần riêng biệt

các thành phần, bạn có thể thực hiện theo cách tương tự như cách thực hiện ở đây và chúng ta sẽ xem cách thực hiện

điều này sau trong bài học.

Và mục tiêu là phần cứng mà ứng dụng được xây dựng.

Trong trường hợp của chúng tôi, đó là ESP 32 và một số thứ không thuộc dự án chính là ESP IDF.

Thay vào đó, nó độc lập và được liên kết với dự án thông qua biến môi trường đường dẫn IDF.

giữ đường dẫn của thư mục ESP IDF.

Điều này cho phép tách khung IDF khỏi dự án của bạn trong đường dẫn cài đặt khung IDF

năm nay và năm nay của bạn có thể giống nhau tùy thuộc vào cách cài đặt của bạn.

Ngoài ra, chuỗi công cụ để biên dịch không phải là một phần của dự án.

Chuỗi công cụ phải được cài đặt trong đường dẫn dòng lệnh của hệ thống được quản lý bởi tất cả

trong một lần cài đặt mà bạn đã hoàn thành ở bài học trước.

Được rồi.

Vì vậy, đây là các phương pháp sử dụng hệ thống xây dựng khác nhau và chúng ta sẽ bắt đầu với IDF.

PY Công cụ dòng lệnh py IDF cung cấp giao diện người dùng để dễ dàng quản lý các bản dựng dự án của bạn và nó quản lý

các công cụ sau đây.

Nó quản lý CMYK để cấu hình dự án sẽ được tích hợp.

Link ở đây sẽ đưa bạn tới trang C make và xem.

Nó có thể dễ dàng là một khóa học khác, nhưng nhìn chung Mark được sử dụng để kiểm soát việc biên dịch phần mềm

và chúng ta sẽ tìm hiểu những điều cơ bản bằng cách sử dụng C tạo danh sách các tệp txt khi chúng ta tiến bộ trong khóa học.

Trong một công cụ khác do EDF Pius Ninja quản lý, công cụ xây dựng dự án và Ninja, đó là một bản dựng nhỏ

hệ thống tập trung vào tốc độ và nó khác với các hệ thống xây dựng khác ở hai khía cạnh chính.

Nó được thiết kế để các tệp đầu vào được tạo bởi hệ thống xây dựng cấp cao hơn và nó được thiết kế để

chạy bản dựng nhanh nhất có thể.

Và vì mục đích của chúng ta trong khóa học này, đó thực sự là tất cả những gì chúng ta cần biết về Ninja.

Và bộ công cụ ESP PY được sử dụng để flash mục tiêu và đó là nền tảng nguồn mở dựa trên python độc lập

tiện ích để giao tiếp với bộ tải khởi động ROM và chip biểu cảm.

Và sau đó có tùy chọn sử dụng Quake trực tiếp.

Và ở đây đã đề cập rằng IDF dot pie là một lớp bọc xung quanh C tạo sự thuận tiện.

Ví dụ: khi EDF Pi làm điều gì đó, nó sẽ in ra từng lệnh mà nó chạy để dễ dàng tham khảo.

Ví dụ: lệnh build EDF Pi cũng giống như chạy các lệnh này trong bash shell hoặc tương tự

lệnh cho dấu nhắc lệnh của Windows.

Nhưng cách chúng tôi sắp sử dụng hệ thống xây dựng, bao gồm CMYK Ninja và công cụ ESP PY là

chỉ cần sử dụng ID biểu cảm để chúng tôi có thể tạo flash và giám sát ứng dụng trực tiếp

từ ID biểu cảm dựa trên nhật thực.

Và mặc dù ID mang đến cho chúng ta rất nhiều tiện ích nhưng chúng ta vẫn phải thiết lập file C make list

để cho hệ thống xây dựng biết cách xây dựng dự án một cách chính xác.

Tài liệu ở đây hiển thị một ví dụ về cây thư mục dự án, trong đó có chứa

các yếu tố sau, bao gồm một dự án cấp cao nhất c tạo danh sách tệp txt.

Và đây là tệp chính mà C sử dụng để tìm hiểu cách xây dựng dự án và có thể thiết lập dự án

rộng.

C Tạo các biến.

Nó bao gồm dự án tệp mà C tạo để triển khai phần còn lại của hệ thống xây dựng và nó cũng đặt

tên dự án và xác định dự án và tệp cấu hình dự án sdhc config được tạo dấu gạch chéo

được cập nhật khi cấu hình menu py IDF chạy và nó giữ cấu hình cho tất cả các thành phần trong

dự án, bao gồm cả ESP, IDF.

Và như tôi đã đề cập, chúng ta có thể định cấu hình tất cả các thành phần bằng cách truy cập trực tiếp vào cấu hình Sdhc tại đây từ

ID.

Sau đó là thư mục các thành phần tùy chọn chứa các thành phần là một phần của dự án,

và dự án không nhất thiết phải chứa các thành phần tùy chỉnh, nhưng nó có thể hữu ích cho việc cấu trúc các thành phần có thể tái sử dụng

mã hoặc bao gồm các thành phần của bên thứ ba không phải là một phần của ESP ADF.

Và một lần nữa, đây là một ví dụ về điều này trong thư viện ESP ADF Lib Sensors nơi có nhiều thành phần

và trong thư mục BM six Eight, bạn có các tệp nguồn và C tạo tệp này tương tự

cấu trúc theo những gì được hiển thị trong tài liệu ấn tượng.

Và trên thực tế, ở đây đã đề cập rằng mỗi thư mục thành phần đều chứa một danh sách tạo thành phần C,

txt và tệp này chứa các định nghĩa biến để kiểm soát quá trình xây dựng thành phần và

sự tích hợp của nó vào dự án tổng thể.

Chúng ta cũng có thư mục chính, là thành phần đặc biệt chứa mã nguồn của dự án

chính nó.

Và trên thực tế, chúng tôi sẽ thêm hầu hết các tệp mới vào đây và chúng tôi cũng có thư mục bản dựng nơi chứa bản dựng

đầu ra được tạo và thư mục này được tạo bởi RDF.

PY nếu nó chưa tồn tại và Cimatu định cấu hình dự án và tạo các tệp bản dựng tạm thời tại đây,

thì sau khi quá trình xây dựng chính được chạy, nó cũng sẽ chứa các tệp và thư viện đối tượng tạm thời như

cũng như các tập tin đầu ra nhị phân cuối cùng.

Và chỉ nói sơ qua về config project build file, file này cho phép bạn gộp cấu hình

tùy chọn.

Và thay vì đọc nó vì nó có thể hơi khó hiểu, tôi sẽ chỉ cho bạn xem trước

nó được sử dụng như thế nào ở đây.

Chúng tôi có tệp xây dựng dự án bánh và hình với tùy chọn menu được gọi là cấu hình ví dụ.

Và từ cấu hình sdhc, chúng tôi có sẵn những định nghĩa này để có thể sử dụng từ nguồn

mã và bạn sẽ thấy cách thức hoạt động trong phần tích hợp thư viện cảm biến.

Được rồi.

Vì vậy, chúng ta hãy quay lại tệp Project Chemicals.

Nếu chúng tôi nhớ lại tệp danh sách tạo cấp cao nhất C này chứa các cài đặt bản dựng cho toàn bộ dự án.

Và tối thiểu, tệp này phải chứa những phần bắt buộc này.

Lệnh C tạo phiên bản yêu cầu tối thiểu yêu cầu c tạo phiên bản tối thiểu cần thiết để xây dựng

dự án.

Tệp PDF được thiết kế để hoạt động với C make 3.16 hoặc mới hơn và dòng này phải là dòng đầu tiên trong c

lập danh sách.

tập tin TXT.

Sau đó, có dự án include tại dòng c make kéo phần còn lại của chức năng C, make

để định cấu hình dự án và khám phá tất cả các thành phần, v.v. và chúng tôi cũng có lệnh dự án trong

lệnh này tự tạo dự án và chỉ định tên dự án và tên dự án được sử dụng

đối với các tệp đầu ra nhị phân cuối cùng của ứng dụng là tệp Elf và Bin.

Trong ví dụ này ở đây, lệnh dự án lấy ID dự án, được lấy từ các lệnh này,

cung cấp cho chúng tôi tên dự án ở đây vì ID dự án trong hành động này chỉ định tên của dự án cuối cùng

tập tin đầu ra nhị phân.

Như đã đề cập trong tài liệu, bạn cũng có các biến dự án tùy chọn và nếu bạn quan tâm,

bạn có thể xem việc thực hiện từng điều này.

Nhưng cái mà chúng ta thực sự sẽ sử dụng trong khóa học là bộ phận chuyển thành phần bổ sung và biến dự án này

cung cấp một danh sách tùy chọn các thư mục bổ sung để tìm kiếm các thành phần và đường dẫn có thể tương đối

vào thư mục dự án hoặc tuyệt đối.

Ví dụ: trong phần Tích hợp Thư viện Cảm biến sắp tới sẽ bao gồm thư viện sử dụng

đặt lệnh vào thư mục Thành phần Slash ESP Lib với đường dẫn tương ứng với thư mục dự án.

Và tài liệu khuyến nghị rằng các lệnh set nên được đặt sau dòng C tạo ra mức tối thiểu, nhưng

trước dòng bao gồm như được hiển thị ở đây.

Đối với danh sách của chúng tôi.

File trong main, chúng ta sẽ sử dụng một thành phần tối thiểu để tạo tệp danh sách và cung cấp cho bạn ngữ cảnh.

Đây là một ví dụ.

Cảnh này tạo danh sách tệp txt trong miền được sử dụng để đăng ký tệp nguồn hoặc tệp c và bao gồm

được biên soạn.

Vì vậy, tệp danh sách tạo thành phần C tối thiểu này chỉ cần đăng ký thành phần đó vào hệ thống xây dựng bằng cách sử dụng

Thanh ghi thành phần EDF và tài liệu cung cấp định nghĩa cho các đối số này.

Sau nguồn, chúng tôi sẽ thêm các tệp nguồn trong suốt khóa học.

Sau đó, đối với các thư mục bao gồm, chúng tôi sẽ sử dụng để bao gồm và yêu cầu.

Chúng tôi sẽ không sử dụng, ít nhất là chưa.

Và không bắt buộc phải sử dụng cái này, nhưng thường phải khai báo những thành phần nào khác

thành phần sẽ sử dụng.

Và bạn có thể theo liên kết này ở đây để tìm hiểu thêm.

Và đừng lo lắng nếu tất cả điều này có vẻ khó hiểu.

Bây giờ, khi chúng ta cập nhật tệp danh sách tạo và cấu hình dự án trong suốt khóa học, nó sẽ

tất cả đều đến với nhau.

Vì vậy chúng ta hãy tiếp tục bài học tiếp theo và thiết lập mẫu dự án.