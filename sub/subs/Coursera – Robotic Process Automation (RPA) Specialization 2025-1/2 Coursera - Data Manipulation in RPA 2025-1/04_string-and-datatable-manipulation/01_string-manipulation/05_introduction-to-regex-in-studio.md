# 05 giới thiệu về biểu thức chính quy trong studio

---

Trong video trước,

bạn đã hiểu phương pháp và

các hoạt động thao tác với chuỗi.

Trong video này, bạn sẽ hiểu

biểu thức chính quy và

trình hướng dẫn xây dựng biểu thức chính quy và

studio.

Vì vậy, hãy bắt đầu.

Biểu thức chính quy hoặc

RegEx là một mẫu tìm kiếm cụ thể

có thể được sử dụng để dễ dàng phù hợp,

định vị và quản lý văn bản.

Studio chứa trình tạo RegEx

giúp đơn giản hóa việc tạo thông thường

biểu thức.

Khả năng tìm kiếm RegEx và

bộ chọn cho phép người dùng xác định

nhiều yếu tố mục tiêu với

một lần thực hiện tìm kiếm duy nhất.

RegEx có thể được sử dụng cho

xác thực đầu vào, phân tích chuỗi,

cạo dữ liệu và thao tác chuỗi.

RegEx có thể được sử dụng để lấy các mảnh

của văn bản tuân theo một khuôn mẫu nhất định,

chẳng hạn như một địa chỉ email.

Bây giờ chúng ta cùng tìm hiểu về hoạt động

đã tích hợp trình tạo RegEx

với họ.

Đây là những trận đấu đầu tiên.

Hoạt động này tìm kiếm một chuỗi đầu vào cho

mọi sự việc xảy ra và

trả về tất cả các kết quả phù hợp thành công cho

biểu thức đã cho.

Hoạt động này có thể được sử dụng để truy xuất

tất cả các mục và sử dụng chúng hơn nữa.

Thứ hai, là sự phù hợp.

Hoạt động này cho biết liệu

biểu thức chính quy được chỉ định tìm thấy

một sự trùng khớp trong chuỗi đầu vào được chỉ định và

chỉ trả về giá trị đúng hoặc sai.

Hoạt động này có thể là điều kiện để

một hoạt động khác.

Và thứ ba, Thay thế.

Hoạt động này thay thế chuỗi

khớp với một biểu thức chính quy

mẫu có quy định

chuỗi thay thế.

Hoạt động này có thể được sử dụng để

mục đích chất lượng dữ liệu.

Như bạn đã biết hiện nay về các hoạt động

sử dụng trình tạo RegEx,

chúng ta hãy nhìn vào

trình hướng dẫn xây dựng RegEx.

Wizard giúp dễ dàng

quá trình xây dựng và

kiểm tra biểu thức chính quy

tiêu chí tìm kiếm.

Trình hướng dẫn RegEx có thể

mở ra từ cơ thể của

bất kỳ hoạt động nào trong số này phù hợp,

là phù hợp hoặc thay thế.

Hãy kéo một hoạt động phù hợp.

Và nhấp vào cấu hình thường xuyên

nút biểu thức để mở RegEx

người xây dựng.

Giao diện người dùng của phiên bản thông thường

builder có ba phần.

Chúng là văn bản kiểm tra, giá trị loại và

định lượng IRS, biểu hiện đầy đủ.

Trong trường văn bản kiểm tra,

người dùng có thể kiểm tra tìm kiếm đã chọn

tiêu chí so với văn bản

trên đó RegEx được áp dụng.

Trước trình soạn thảo văn bản, người dùng có thể

chọn loại biểu thức RegEx,

giá trị và định lượng.

Làm như vậy, làm nổi bật những phát hiện

trong trình soạn thảo văn bản thử nghiệm.

Nó đơn giản hóa việc xây dựng các biểu thức chính quy

bằng cách cho phép cấu hình loại,

giá trị và định lượng.

Khi một điều kiện được hoàn thành,

một cái khác có thể được thêm vào.

Nếu có nhiều hơn một điều kiện,

thứ tự áp dụng chúng

cũng có thể được cấu hình.

Chúng ta hãy nhìn vào loại,

giá trị và định lượng ngay bây giờ.

Kiểu thả xuống cho phép tìm kiếm

một văn bản nhất định hoặc một biểu thức từ nhiều.

Nó có thể được cấu hình để chỉ tìm kiếm

ở đầu hoặc ở cuối.

Và cũng cung cấp các biểu thức dựng sẵn cho

email,

URL Các tiểu bang của Hoa Kỳ hoặc Số điện thoại của Hoa Kỳ.

Điều này rất hữu ích trong

trường hợp dữ liệu được chuẩn hóa.

Một số ví dụ là, chữ, chữ số, một trong,

không phải một trong, bất cứ thứ gì, bất kỳ ký tự từ nào,

khoảng trắng, bắt đầu bằng.

Trường giá trị chứa chính xác

văn bản cần lấy.

Danh sách thả xuống bộ định lượng cho phép

người dùng chọn loại kết quả

nên được hiển thị.

Trình đơn thả xuống có các tùy chọn sau.

Đầu tiên, chính xác là như vậy

chọn một số tiền chính xác

số lần xuất hiện liên tiếp

người dùng muốn tìm.

Ví dụ, nếu văn bản đang

được tìm kiếm là Xin chào và

số lượng ở đó được đặt chính xác là hai,

trình hướng dẫn sẽ tìm thấy bất kỳ lần xuất hiện nào của Hello,

Xin chào trong hộp văn bản kiểm tra.

Thứ hai, bất kỳ số 0 hoặc

nhiều hơn nữa làm nổi bật bất kỳ số lượng

kết quả tìm thấy liên tiếp

bắt đầu từ số không.

Thứ ba, ít nhất một, một hoặc

nhiều hơn nữa làm nổi bật bất kỳ số lượng

kết quả tìm thấy liên tiếp

bắt đầu từ một, thứ tư.

Không hoặc một cái chỉ làm nổi bật một

sự xuất hiện liên tiếp của thuật ngữ.

Thứ năm, giữa X&Y lần

làm nổi bật số

số lần xuất hiện liên tiếp được chọn.

Ví dụ, tìm kiếm

Xin chào và lựa chọn giữa hai và

ba lần chỉ nổi bật Xin chào,

Xin chào và xin chào, xin chào, xin chào.

Hộp văn bản biểu thức đầy đủ

ở cuối trình hướng dẫn,

hiển thị RegEx hiện tại

biểu hiện ở dạng thô.

Và đó là tất cả cho video này.

Tiếp theo trong bài học này là phần minh họa

video về cách sử dụng trình tạo RegEx.

Và một bài tập thực hành khác

về thao tác chuỗi.

Cảm ơn đã xem.

[ÂM NHẠC]