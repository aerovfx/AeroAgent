# 03 - Dữ liệu thô lộn xộn

---

- [Người hướng dẫn] Tại sao việc xử lý trước dữ liệu lại quan trọng đến vậy?

Bằng cách xử lý trước dữ liệu, chúng tôi đảm bảo chất lượng của nó.

Dữ liệu chất lượng cao này cho phép mô hình AI

để học một cách hiệu quả,

dẫn đến kết quả đầu ra chính xác và đáng tin cậy hơn.

Nó thậm chí có thể tăng tốc quá trình đào tạo

bằng cách làm cho dữ liệu dễ dàng hơn để mô hình làm việc.

Chúng ta hãy xem xét các vấn đề

dữ liệu thô hoặc chưa được xử lý.

Dữ liệu thô là thông tin chưa được xử lý

được thu thập từ nhiều nguồn khác nhau.

Chúng tôi đã thu thập thô từ nguồn dữ liệu

mà không cần làm sạch hoặc cấu trúc,

để lại tất cả các thuộc tính dữ liệu gốc

và các giá trị tại chỗ.

Ví dụ: loại tệp dữ liệu

xác định định dạng dữ liệu được lưu trữ,

.txt cho văn bản thuần túy, .jpg cho hình ảnh,

.wav cho âm thanh, v.v.

Mọi giá trị dữ liệu được lưu trữ trong các tệp này

vẫn ở trạng thái ban đầu

khi chúng được kéo từ các hệ thống khác nhau.

Các hệ thống như cơ sở dữ liệu,

hệ thống quản lý quan hệ khách hàng,

hoặc nền tảng lưu trữ đám mây lưu trữ, sắp xếp,

quản lý và truy cập các loại tệp dữ liệu khác nhau.

Chúng hoạt động như thư viện hoặc tủ đựng hồ sơ cho dữ liệu của bạn.

Khi bạn đã trích xuất và tải dữ liệu của mình

từ nhiều hệ thống khác nhau để phân tích,

bạn có thể sẽ gặp phải vấn đề.

Các vấn đề thường gặp bao gồm thiếu giá trị,

hồ sơ trùng lặp, định dạng không nhất quán,

các ngoại lệ, lỗi và thông tin không liên quan.

Chúng ta hãy xem một vài ví dụ

sử dụng tập dữ liệu viễn thông của chúng tôi.

Các giá trị bị thiếu là phổ biến trong dữ liệu thô

trong đó một số mục nhập dữ liệu không đầy đủ.

Điều này có thể dẫn đến kết quả không chính xác

nếu bạn không xử lý chúng đúng cách.

Ví dụ bao gồm các trường trống hoặc không có giá trị trong tập dữ liệu.

Trong ví dụ này, tính năng hợp đồng hoặc cột

thiếu giá trị ở hàng bốn, năm và sáu.

Chúng tôi không thể biết liệu hợp đồng của những khách hàng này có

là hàng tháng hoặc một năm.

Bản ghi trùng lặp là mục nhập dữ liệu dư thừa

có thể làm sai lệch phân tích và kết quả.

Một ví dụ là các bản ghi khách hàng lặp lại trong một tập dữ liệu,

có thể làm tăng số liệu và làm sai lệch thông tin chi tiết.

Trong ví dụ này, ID khách hàng 7590-VHVEG

được lặp lại hai lần.

Các định dạng dữ liệu không nhất quán đề cập đến tính biến đổi

trong cách dữ liệu được trình bày,

điều này tạo ra khó khăn trong việc xử lý và phân tích.

Ví dụ bao gồm các định dạng ngày khác nhau

hoặc các đơn vị đo lường khác nhau.

Trong ví dụ này, ngày thu được

được định dạng khác với ngày rời bỏ.

Điều này sẽ gây nhầm lẫn vì nó xuất hiện

rằng hai ngày này là từ các nguồn khác nhau.

Phù.

Bạn vừa thấy ba ví dụ về dữ liệu bẩn.

Dữ liệu bẩn hay còn gọi là dữ liệu không sạch hoặc dữ liệu lộn xộn.

đề cập đến thông tin trong một tập dữ liệu

điều đó không chính xác, không đầy đủ,

không nhất quán hoặc có định dạng không đúng.

Vậy làm cách nào để khắc phục hoặc làm sạch dữ liệu bẩn này?

Chúng ta cần xử lý trước dữ liệu.

Khi kết thúc quá trình tiền xử lý dữ liệu

dữ liệu thô của bạn được chuyển đổi

từ một khối thô sơ, vô tổ chức

thành các khối xây dựng rõ ràng, được định dạng

mà các mô hình AI có thể dễ dàng sử dụng để đào tạo.

Dữ liệu được xử lý đã được làm sạch này

cho phép mô hình học hiệu quả hơn,

dẫn đến kết quả đầu ra chính xác và đáng tin cậy hơn.

Hãy nghĩ đến việc xử lý trước dữ liệu

như chuẩn bị nguyên liệu cho một bữa ăn ngon.