# 03 - Giảm độ dốc ngẫu nhiên (SGD)

---

- [Người hướng dẫn] Giảm độ dốc ngẫu nhiên, hay SGD,

thực hiện một cách tiếp cận khác với việc giảm độ dốc hàng loạt

bằng cách tính toán độ dốc và cập nhật các tham số

cho từng ví dụ đào tạo riêng lẻ

thay vì toàn bộ tập dữ liệu.

Hãy nghĩ về SGD như việc bước những bước nhỏ nhanh chóng xuống đồi,

điều chỉnh đường dẫn của bạn dựa trên môi trường xung quanh ngay lập tức

thay vì xem xét toàn bộ cảnh quan.

Phương pháp này giới thiệu một mức độ ngẫu nhiên hoặc nhiễu

vào quá trình tối ưu hóa.

Một trong những lợi ích chính của việc giảm độ dốc ngẫu nhiên

là mỗi bản cập nhật đều nhanh chóng

bởi vì nó chỉ xử lý một mẫu tại một thời điểm.

Điều này có thể tăng tốc đáng kể quá trình lặp lại,

cho phép mô hình bắt đầu học các mẫu

từ dữ liệu nhanh hơn.

Tính trực tiếp này có thể đặc biệt hữu ích

trong các tình huống học tập trực tuyến

nơi dữ liệu đến trong luồng.

SGD cũng yêu cầu ít bộ nhớ hơn

vì nó chỉ cần lưu trữ một mẫu dữ liệu duy nhất

và gradient tương ứng.

Điều này làm cho nó phù hợp hơn với các tình huống

nơi tài nguyên tính toán bị hạn chế

hoặc khi xử lý các tập dữ liệu cực lớn

không thể tải tất cả vào bộ nhớ cùng một lúc.

Một ưu điểm thú vị của tính ngẫu nhiên trong SGD

là khả năng thoát khỏi cực tiểu địa phương.

Tiếng ồn trong các bản cập nhật

có thể giúp thuật toán thoát khỏi các giải pháp dưới mức tối ưu

và có khả năng tìm thấy mức tối thiểu toàn cầu tốt hơn.

Điều này làm cho SGD đặc biệt hữu ích

trong đào tạo mô hình deep learning

với bề mặt mất mát phức tạp

nơi cực tiểu địa phương là những trở ngại phổ biến.

Tuy nhiên, sự khác biệt lớn trong các bản cập nhật

cũng là một trong những hạn chế đáng kể của SGD.

Bởi vì mỗi bản cập nhật dựa trên một điểm dữ liệu duy nhất,

các bản cập nhật có thể dao động đáng kể.

Điều này có thể dẫn đến đường hội tụ kém ổn định hơn,

làm cho việc dự đoán trở nên khó khăn hơn

khi mô hình đạt đến tổn thất tối thiểu.

Đường dẫn tối ưu hóa có thể giống với hình zigzag,

có khả năng vượt quá mức tối thiểu

và cần nhiều lần lặp hơn để hội tụ.

Một nhược điểm nữa là SGD

có thể yêu cầu nhiều lần lặp hơn để hội tụ

so với phương pháp giảm độ dốc hàng loạt.

Các bản cập nhật ồn ào có thể gây ra quá trình tối ưu hóa

để đi theo một con đường thất thường hơn hướng tới mức tối thiểu,

có khả năng tăng thời gian đào tạo tổng thể.

Điều này có thể không hiệu quả,

đặc biệt khi cần có sự hội tụ chính xác.

Ngoài ra, xử lý từng mẫu một

hạn chế cơ hội cho tính toán song song.

Trong môi trường tính toán hiện đại

trong đó sự song song hóa là chìa khóa cho hiệu quả,

đây có thể là một bất lợi đáng kể.

Không có khả năng tận dụng đòn bẩy

bộ xử lý đa lõi hoặc GPU hiệu quả

có nghĩa là SGD có thể không sử dụng hết

tài nguyên tính toán sẵn có.