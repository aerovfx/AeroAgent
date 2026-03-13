# 01 dọn dẹp và chuyển đổi dữ liệu

---

Xin chào và chào mừng trở lại.

Ở bài học trước,

chúng tôi đã giúp PrimeBuy giải quyết một số vấn đề

về sự không nhất quán dữ liệu của họ.

Những lỗi này dễ dàng

hiển thị trong tập dữ liệu.

Tuy nhiên, tập dữ liệu có thể chứa các

những lỗi ẩn hoặc sự không nhất quán.

Rất may, trong Power Query Editor,

chúng tôi có sẵn một số công cụ

như Chất lượng Cột, Hồ sơ Cột và

Phân phối theo cột, giúp chúng tôi

trong việc phát hiện ra những lỗi ẩn này.

Nhiệm vụ thứ ba mà Primebuy

muốn giải quyết là làm sạch và

chuyển đổi dữ liệu để hiểu rõ ràng

mức giảm giá trung bình được cung cấp cho

từng kênh bán hàng trong hoạt động kinh doanh của mình.

Có sẵn các công cụ trong Power

Trình soạn thảo truy vấn, như Chất lượng cột và

Hồ sơ cột đóng vai trò quan trọng

trong việc làm sạch tập dữ liệu của chúng tôi một cách hiệu quả.

Vì vậy, hãy đi sâu vào Power Query Editor

bằng cách nhấp vào biến đổi

tab từ chế độ xem mô hình hoặc

xem báo cáo.

Trong Power Query Editor, hãy chọn dạng xem

tab có sẵn trên Dải băng trên cùng và

kích hoạt chất lượng cột bằng cách

đánh dấu hộp kiểm.

Sau khi hoàn thành bước này, bạn có thể thấy

Power Bi phân tích các cột trong

tập dữ liệu và hiển thị chất lượng khác nhau

số liệu hợp lệ, Lỗi và trống.

Hãy hiểu các thông số này.

Hợp lệ, tham số này bao gồm

phần trăm giá trị hợp lệ trong cột,

nghĩa là, các giá trị xác nhận

lỗi định dạng và kiểu dữ liệu dự kiến.

Tham số này làm nổi bật tỷ lệ phần trăm

của các giá trị trong cột đó

chứa các lỗi như không hợp lệ,

các kiểu dữ liệu và các vấn đề về định dạng.

Trống, tham số này đại diện

tỷ lệ thiếu

các giá trị trong các cột.

Bằng cách làm theo các bước sau và

xem xét các tham số hợp lệ,

lỗi và trống cho mỗi cột,

bạn có thể phân tích một cách hiệu quả

chất lượng cột của tập dữ liệu của bạn.

Bây giờ, hãy ghi nhớ điều này,

tìm kiếm

các lỗi trong cột

của Phiếu đặt hàng bán hàng.

Hãy chọn Bảng đặt hàng bán hàng.

Điều quan trọng cần lưu ý là khi

bạn đang xem bản xem trước dữ liệu trong

Trình soạn thảo Power Query, Power Bi, theo mặc định,

sẽ thực hiện việc lập hồ sơ dữ liệu dựa trên

chỉ trên một nghìn hàng trên cùng.

Khi mục tiêu là thực hiện

kiểm tra chẩn đoán dữ liệu bằng cách sử dụng

Hồ sơ cột, nó được khuyến khích

để thay đổi cài đặt mặc định và

thực hiện hồ sơ cột

dựa trên toàn bộ tập dữ liệu.

Để làm điều này, bấm vào cột

hồ sơ dựa trên toàn bộ tập dữ liệu

từ dưới cùng bên trái vậy

rằng chúng tôi không bỏ lỡ bất kỳ thông tin chi tiết nào.

Bây giờ, nếu bạn cuộn qua các cột,

bạn sẽ quan sát thấy điều đó trong

cột áp dụng giảm giá,

chỉ 99% giá trị là hợp lệ.

Điều này cũng được biểu thị bằng đường màu xanh lá cây,

đó là không đầy đủ.

Một vài hàng trong cột này có giá trị rỗng

các giá trị, như được biểu thị bằng giá trị trống.

Chất lượng cột giúp chúng tôi tìm kiếm

các cột dễ mắc lỗi.

Hãy tiếp tục và thực hiện một số thao tác dọn dẹp

các thao tác trên cột áp dụng chiết khấu.

Power Bi cho phép bạn xử lý

giá trị null theo những cách khác nhau.

Chúng ta có thể loại bỏ

các hàng bằng cách bỏ chọn

các giá trị null từ bộ lọc này hoặc

nhấp vào tùy chọn Xóa trống.

Tuy nhiên, sử dụng phương pháp này

cũng sẽ xóa hàng

giá trị từ các cột khác trong đó

chiết khấu được áp dụng có giá trị rỗng.

Một cách tiếp cận tốt hơn là thay thế null

các giá trị có giá trị thay thế trong

một cách hợp lý.

Thay thế cũng là một lựa chọn tốt nếu

có lỗi trong cột.

Cách tiếp cận này đòi hỏi doanh nghiệp

hiểu biết để lựa chọn phù hợp

các giá trị thay thế.

Quá trình thay thế null này

các giá trị được gọi là tính toán.

Trong cuộc thảo luận với Nhóm PrimeBuy,

hiểu rằng bất cứ nơi nào giảm giá

được áp dụng là 0%, giá trị trong

cột áp dụng giảm giá là rỗng.

Hãy gán các giá trị như

0 khi giá trị là null.

Hãy làm điều đó.

Hãy chọn giảm giá

cột áp dụng và

sau đó nhấp vào Thay thế giá trị

trong tab Chuyển đổi.

Khi bạn nhấp vào nó, một tab mới sẽ xuất hiện,

yêu cầu bạn thay thế

một giá trị với một giá trị khác.

Trong bước tiếp theo, chuyển giá trị rỗng

giá trị trong giá trị cần tìm và

số 0 trong cột Thay thế bằng và

nhấn OK.

Với điều này, chúng tôi đã điền vào phần còn thiếu

giá trị cho cột áp dụng giảm giá.

Hãy xác nhận hoạt động này bằng cách

kiểm tra giá trị phần trăm hợp lệ trong

chất lượng cột.

Tại sao bạn không kiểm tra chất lượng cột trong

tất cả các tờ khác để xác nhận rằng có

không còn giá trị nào bị thiếu nữa?

Khi bạn đã hoàn tất, hãy tiếp tục và

khám phá một công cụ tuyệt vời khác trong

power bi gọi là Column Profile.

Trong khi cố gắng đạt được những hiểu biết sâu sắc và

hiểu các mẫu trong dữ liệu,

bạn có thể gặp những giá trị có vẻ như

khác biệt một cách bất thường so với phần lớn

các điểm dữ liệu.

Đây được gọi là ngoại lệ.

Hồ sơ cột giúp trong

xác định các ngoại lệ.

Nó hỗ trợ việc khám phá dữ liệu bằng cách

cung cấp một cái nhìn tổng quan nhanh chóng về giá trị

phân phối cột,

bao gồm các số liệu thống kê như tối thiểu và

giá trị tối đa và trung bình cho

cột đã chọn.

Hãy điều hướng đến

Phiếu đặt hàng bán hàng và

bấm vào hồ sơ Cột có sẵn trong

phần Ribbon trong tab Xem.

Một lần nữa, hãy đảm bảo cột

hồ sơ được dựa trên tất cả các hàng.

Khi đã xong, hãy kiểm tra cột

hồ sơ của cột Số lượng đặt hàng

trong bảng Đơn đặt hàng bán hàng.

Vì điều đó,

chọn cột Số lượng đặt hàng.

Chỉ với một vài cú nhấp chuột, chúng ta có thể

để xem số liệu thống kê cột và

sự phân phối giá trị

của số lượng đặt hàng.

Nếu chúng ta biết về điều này

lừa trong phiên cuối cùng,

chúng ta có thể sử dụng nó để dễ dàng kiểm tra

các giá trị ngoại lệ trong cột Số lượng đặt hàng.

Bạn có nhớ chúng ta đã tìm thấy thế nào không

ngoại lệ ở bài học trước?

Nếu không, vui lòng tóm tắt nhanh.

Tuyên bố vấn đề của chúng tôi đối với Primebuy là

làm sạch và chuyển đổi dữ liệu để rõ ràng

hiểu mức giảm giá trung bình được cung cấp

cho từng kênh bán hàng trong hoạt động kinh doanh của mình.

Chúng tôi đã dọn dẹp rồi

cột Giảm giá được áp dụng, vì vậy

hãy thử hình dung mức trung bình

chiết khấu cho từng kênh bán hàng.

Hãy đóng và áp dụng để lưu các thay đổi.

Bây giờ, để giải quyết vấn đề này,

biểu đồ cột nhóm là

biểu đồ phù hợp nhất.

Hãy nhanh chóng chuyển sang chế độ xem báo cáo và

tạo nó trên một khung báo cáo trống.

Bấm vào biểu đồ cột được nhóm lại.

Bây giờ kéo giảm giá

cột được áp dụng trong trục y.

Vì nó là một cột giá trị số,

Power Bi theo mặc định

tổng hợp nó thành tổng.

Ngoài ra, Primebuy muốn hiểu

chiết khấu trung bình cho

mỗi kênh bán hàng, vì vậy

hãy thay đổi tổng hợp thành Trung bình.

Bây giờ kéo kênh bán hàng từ

bảng Đơn đặt hàng bán hàng theo trục x tới

được giảm giá trung bình cho

từng kênh bán hàng.

Vụ chính tả khét tiếng

phương sai gây ra sự hỗn loạn dữ liệu.

Bạn có để ý thấy có nhiều biến thể

cách viết cho các kênh bán hàng giống nhau?

Ví dụ: thuật ngữ Instore là

được đề cập hai lần với định dạng khác nhau.

Đầu tiên, nó được thể hiện bằng dấu gạch nối,

và thứ hai,

nó xuất hiện với một khoảng trống ở giữa.

Một sự xuất hiện tương tự được ghi nhận cho

cụm từ kênh bán hàng trực tuyến.

Sau khi quan sát cẩn thận,

có vẻ như chúng ta chỉ có bốn điểm riêng biệt

các kênh bán hàng trực tuyến tại cửa hàng,

Nhà phân phối, bán buôn.

Được rồi, bây giờ chúng ta có

lại tìm thấy một vấn đề,

chúng ta cần khắc phục nó

bằng cách sử dụng Power Query Editor.

Hãy làm điều đó.

Bấm vào biến đổi

dữ liệu từ Ribbon trên cùng.

Bây giờ hãy điều hướng đến bảng Đơn đặt hàng bán hàng và

chọn cột Kênh bán hàng.

Bây giờ hãy sửa những lỗi chính tả này

từng cái một bằng cách nhấp vào Thay thế

các giá trị trong tab Chuyển đổi.

Bây giờ trong menu Giá trị thay thế,

chúng tôi sẽ giải quyết vấn đề cho Instore.

Hãy chuyển Instore dưới dạng Giá trị được xác định và

chuyển vào cửa hàng có dấu gạch nối

ở giữa là Thay thế

với Giá trị và nhấp vào OK.

Tương tự, chúng tôi sẽ khắc phục vấn đề

với kênh bán hàng trực tuyến.

Với điều đó, chúng tôi đã thực hiện với những thay đổi.

Hãy đóng và áp dụng và

xem liệu điều đó có khắc phục được biểu đồ của chúng tôi không.

Vâng, nó đã làm được.

Tuyệt vời.

Biểu đồ làm mới chứng minh rằng

không có sự khác biệt đáng kể trong

mức giảm giá trung bình được cung cấp

tới các kênh khác nhau.

Kênh bán hàng trực tuyến bị ảnh hưởng nhẹ

chiết khấu trung bình cao hơn ở mức 12%,

trong khi mức giảm giá trung bình được cung cấp bởi

tất cả các kênh bán hàng khác đều đứng ở mức 11%.

Như chúng tôi đã quan sát ở đây,

đôi khi chúng ta có thể tìm thấy sự mâu thuẫn

trong dữ liệu bằng cách trực quan hóa dữ liệu.

Vậy là xong, chúng ta hãy kết thúc video này tại đây.

Bây giờ chúng ta hiểu những cách khác nhau

trong đó dữ liệu có thể được làm sạch bằng cách sử dụng

Trình soạn thảo Power Query.

Power Query Editor là một công cụ rộng lớn

với rất nhiều khả năng.

Hãy dành chút thời gian để khám phá

các tính năng khác nhau mà nó cung cấp.

Hãy tiếp tục giúp đỡ Primebuy

trong phát biểu vấn đề tiếp theo của nó.