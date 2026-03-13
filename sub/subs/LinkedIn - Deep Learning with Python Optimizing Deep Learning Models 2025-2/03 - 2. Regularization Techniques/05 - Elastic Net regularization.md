# 05 - Chính quy hóa lưới đàn hồi

---

- [Người hướng dẫn] Chính quy hóa mạng đàn hồi

kết hợp các hình phạt của cả hai

L một và L hai chính quy

làm cho nó đặc biệt hữu ích khi xử lý dữ liệu

trong đó một số tính năng có mối tương quan cao

hoặc khi cả L one và L two đều không được chính quy hóa

một mình mang lại kết quả tối ưu.

Hàm mất đối với việc chuẩn hóa lại mạng đàn hồi là

được định nghĩa như được hiển thị ở đây nơi điều khiển alpha

sức mạnh tổng thể của việc chính quy hóa

và Rho là tham số trộn giữa

L một và L hai chính quy.

Giá trị của Rho trong khoảng từ 0 đến 1

tạo ra sự kết hợp của cả L một và L hai.

Tuy nhiên, khi Rho bằng 1 thì hiệu ứng sẽ là

giống như quy tắc L one hoặc lasso,

và khi Rho bằng 0 thì hiệu ứng sẽ là

giống như L hai chính quy.

Về cơ bản, mục tiêu chính quy hóa mạng đàn hồi

để tận dụng lợi ích của cả hai

L một và L hai chính quy,

bằng cách khuyến khích sự thưa thớt như L one để lựa chọn tính năng,

đảm bảo rằng mô hình chỉ sử dụng các tính năng phù hợp nhất

và ổn định mô hình như L hai

bằng cách xử phạt các trọng lượng lớn một cách thống nhất

ngăn chặn bất kỳ trọng lượng duy nhất nào chiếm ưu thế.

Điều này cũng làm giảm nguy cơ trang bị quá mức.

Lựa chọn sử dụng chính quy hóa mạng đàn hồi

Việc chính quy hóa L một và L hai phụ thuộc vào đặc điểm cụ thể

yêu cầu của vấn đề đặt ra.

Lưới đàn hồi đặc biệt phù hợp với các tình huống

nơi số lượng tính năng lớn hơn nhiều

hơn số lượng quan sát.

Elastic Net có thể giúp chọn tập hợp con phù hợp nhất

của các đặc điểm mà không hoàn toàn bỏ qua những đặc điểm tương quan.

Nó cũng hữu ích khi tập dữ liệu

có các nhóm đặc điểm tương quan.

L một sự chính quy hóa có thể tùy ý chọn một tính năng từ

một nhóm tương quan có khả năng bỏ qua thông tin hữu ích.

Mặt khác, L hai sự chính quy hóa có xu hướng

để bao gồm tất cả các tính năng, nhưng không thu nhỏ

đối với các trọng số quan trọng về 0.

Lưới đàn hồi cân bằng những hành vi này

cho phép lựa chọn tính năng nhóm

đồng thời vẫn duy trì tình trạng giảm cân.

Tham số vai trò trong lưới đàn hồi cung cấp khả năng kiểm soát tinh chỉnh

trên số dư chính quy,

cho phép kết hợp linh hoạt

về các thuộc tính lựa chọn tính năng của L một

với độ ổn định và phân bố trọng lượng của L2.