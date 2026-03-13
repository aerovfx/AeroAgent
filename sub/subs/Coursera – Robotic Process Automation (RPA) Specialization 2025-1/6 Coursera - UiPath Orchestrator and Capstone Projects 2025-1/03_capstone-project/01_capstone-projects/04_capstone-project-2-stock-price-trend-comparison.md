# 04 capstone-dự án-2-so sánh xu hướng giá cổ phiếu

---

Trong video trước,

bạn đã hiểu

yêu cầu của

dự án capstone đầu tiên

gọi là Nhập hóa đơn.

Trong video này, bạn sẽ

hiểu yêu cầu của

dự án capstone thứ hai

gọi là Giá cổ phiếu

So sánh xu hướng.

Trong dự án này, bạn được mong đợi

sử dụng Excel và

tự động hóa email,

trích xuất dữ liệu từ một trang web,

và tạo Excel

báo cáo và gửi email.

Hãy bắt đầu. bạn

dự kiến sẽ xây dựng

một dự án tự động hóa

xu hướng giá cổ phiếu

so sánh đối với một tổ chức

Mỗi ngày,

tổ chức muốn

ghi lại sự tăng giảm

trong giá cổ phiếu của

hai công ty tên là Exxon

RPA Corp và WEX Academy Inc.

So sánh giá của cả hai

các công ty sử dụng biểu đồ.

Nó muốn gửi báo cáo

bao gồm giá cổ phiếu và

đồ thị so sánh

một khách hàng sau khi

thời gian giao dịch đã kết thúc.

Thời gian giao dịch là khi thực tế

giao dịch đang được tiến hành.

Ví dụ, ở Mỹ,

thời gian giao dịch là

trong khoảng thời gian từ 09:30 sáng-04:00 chiều.

Có một số hành động của

dự án nên

đảm nhận việc thực hiện.

Chúng ta sẽ hiểu

tất cả những hành động này trong

chi tiết để bạn có thể tạo

dự án của riêng bạn.

Trước khi bắt đầu với

việc tạo ra dự án,

bạn nên đảm bảo

rằng bạn đã sẵn sàng

với các điều kiện tiên quyết của dự án.

Có một số

điều kiện tiên quyết của dự án.

Điều kiện tiên quyết đầu tiên đó là

máy tính của bạn nên có

UiPath Studio và Microsoft

Đã cài đặt văn phòng.

Bạn có thể tìm thấy phần cứng

và yêu cầu phần mềm

để cài đặt

UiPath Studio trên Uipath

cổng thông tin tài liệu.

Điều kiện tiên quyết thứ hai là

studio nên có tất cả

gói cần thiết.

Các gói này là UiPath

Hoạt động tự động hóa giao diện người dùng,

Hoạt động của hệ thống UiPath,

Hoạt động Uipath Excel,

và Hoạt động Thư UiPath.

Trong Studio, bạn có thể xem

các gói được cài đặt bởi

nhấp vào Quản lý gói

tùy chọn trên dải băng Thiết kế.

Bạn có thể tìm kiếm và

cài đặt gói mới từ

tab Tất cả các gói của

Cửa sổ Quản lý gói.

Điều kiện tiên quyết thứ ba là phải có

một mạng internet đang hoạt động và

một trình duyệt có thể

được sử dụng cho tự động hóa.

Trang web sẽ được sử dụng

để khai thác giá cổ phiếu là

Thị trường chứng khoán RPA trên

rpachallenge.com.

Hãy để chúng tôi có được một cái nhìn tổng quan

của trang web từ

giá cổ phiếu ở đâu

sẽ được trích xuất.

Ở bên trái màn hình,

bạn có thể thấy một hộp thả xuống.

Trong trình đơn thả xuống của nó,

bạn sẽ tìm thấy tên của

một số công ty có cổ phiếu

giá có thể được trích xuất.

Khi bạn chọn một công ty

và nhấp vào biểu tượng Tìm kiếm.

Phần này dưới đây hiển thị

giá cổ phiếu của nó và

biểu đồ liên quan.

Điều kiện tiên quyết thứ tư

là bạn nên có

Outlook được định cấu hình trên

máy có địa chỉ email.

Điều kiện tiên quyết thứ năm

là để tạo ra

một tệp Excel có tên Data.xlsx.

Nó phải có mặt trong

thư mục dự án với

tiêu đề cột như

Ngày hệ thống trong ô A1,

Dấu thời gian trong ô B1,

Tập đoàn Exxon RPA ở ô C1,

và WEX Academy Inc tại

ô D1 trong một trang tính.

Biểu đồ đường đôi nên

cũng được tạo ra trong

cùng một tờ,

điều này sẽ cho thấy những thay đổi trong

giá cổ phiếu theo thời gian.

Ban đầu, biểu đồ

nên trống rỗng,

cái nào sẽ được xây dựng

như dữ liệu

đã tải lên trong tập tin

trong quá trình này.

Đảm bảo rằng Excel này

tập tin trống và

chỉ có tiêu đề trước

chạy quá trình.

Sẽ tốt nhất nếu bạn cũng

vô hiệu hóa tính năng lưu tự động

tùy chọn của Excel.

Một tệp Data.xlsx mẫu

đã được cung cấp cùng

với khóa học này.

Điều kiện tiên quyết thứ sáu

là để tạo ra

một tập tin Excel

được gọi là Config.xlsx.

Nó nên có mặt

trong thư mục dự án.

Tại cột A của trang tính,

nhập địa chỉ email của người nhận,

nội dung thư và chủ đề thư.

Ở liền kề

các ô của cột B,

nhập khách hàng

địa chỉ email.

Một tin nhắn mà bạn muốn trong

thân thư và

báo cáo giá cổ phiếu.

Một tệp Config.xlsx mẫu

đã được cung cấp cùng

với khóa học này.

Điều kiện tiên quyết thứ bảy

là bạn nên đảm bảo

máy tính của bạn vẫn bật

trong khi dự án đang chạy.

Dự án dự kiến sẽ chạy

cứ 30 phút một lần cho đến 04:00 chiều.

Bạn có thể điều chỉnh việc thực hiện nó

tần số như mong muốn.

Bây giờ chúng ta hãy hiểu

những hành động mà

dự án nên thực hiện.

Hành động đầu tiên mà

dự án nên thực hiện là để kiểm tra

liệu thời điểm hiện tại

là thời gian giao dịch hợp lệ,

tức là nó ít hơn

hơn 04 giờ chiều.

Nếu việc giao dịch

thời gian không hợp lệ,

dự án nên

ngừng thực hiện.

Nếu thời gian giao dịch hợp lệ,

dự án nên tính toán

tổng tần suất thực hiện của nó hoặc

số lần nó

có thể chạy đến 04:00 chiều.

Nếu bạn muốn chạy dự án

cứ sau 30 phút và bắt đầu

nó được thực hiện vào lúc 02:00 chiều,

dự án sẽ

thực hiện bốn lần.

Sau khi tính toán

tần suất thực hiện,

dự án nên trích xuất

ngày và dấu thời gian của hệ thống.

Sau khi giải nén

ngày và dấu thời gian của hệ thống,

dự án nên mở

trang web thị trường chứng khoán

trên rpachallenge.com.

Sau khi mở trang web,

dự án nên trích xuất

giá cổ phiếu của

Tập đoàn Exxon RPA và

Học viện WEX,

và đóng trang web.

Sau khi đóng trang web,

dự án nên lưu trữ

ngày trích xuất,

dấu thời gian và giá cổ phiếu

trong tệp Data.xlsx.

Sau khi lưu trữ dữ liệu

trong tệp Excel,

các dự án nên được tính

tần suất thực hiện hiện tại

hoặc số lượng

lần nó đã chạy.

Sau khi tính toán

tần suất thực hiện hiện tại,

dự án nên

kiểm tra xem nó có phải không

ít hơn tổng số

tần suất thực hiện

Nếu hiện tại

tần số thực hiện là

ít hơn tổng số

tần suất thực hiện,

dự án nên

đợi trong 30 phút.

Sau 30 phút,

dự án nên

trích xuất lặp lại

ngày, dấu thời gian,

và giá cổ phiếu của

các công ty và

lưu trữ chúng trong

Tệp dữ liệu.xlsx.

Nếu hiện tại

tần số thực hiện là

không ít hơn tổng

tần suất thực hiện,

dự án nên tạo ra một

biểu diễn đồ họa của

dữ liệu được thu thập trong

tệp Excel và

gửi email cho khách hàng.

Địa chỉ email, chủ đề,

và thông điệp cơ thể nên được thực hiện

từ tệp Config.xlsx.

Sau khi gửi email,

dự án nên

ngừng thực hiện.

Đó là tất cả cho video này.

Cảm ơn đã xem.