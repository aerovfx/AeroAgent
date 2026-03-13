# 05 - Dừng sớm và kiểm tra

---

- [Người hướng dẫn] Dừng sớm là một kỹ thuật điều chỉnh

được thiết kế để tối ưu hóa quá trình đào tạo bằng cách tạm dừng nó

khi hiệu suất của một người mẫu

trên tập dữ liệu xác thực ngừng cải thiện.

Kỹ thuật này hoạt động

bằng cách liên tục đánh giá hiệu suất của mô hình

về số liệu xác nhận,

chẳng hạn như mất xác nhận hoặc độ chính xác

vào cuối mỗi thời đại.

Dừng sớm theo dõi các số liệu này

và tạm dừng quá trình đào tạo

nếu không thấy cải thiện

cho một số kỷ nguyên liên tiếp nhất định

được xác định bởi tham số kiên nhẫn.

Một trong những lợi ích chính của việc dừng sớm

là khả năng ngăn chặn việc trang bị quá mức

bằng cách ngừng đào tạo trước khi mô hình bắt đầu

mất khả năng khái quát hóa dữ liệu chưa nhìn thấy.

Ngoài ra, nó bảo tồn tài nguyên tính toán,

tiết kiệm thời gian và sức mạnh xử lý

bằng cách ngừng đào tạo không cần thiết.

Việc dừng sớm cũng giảm thiểu nhu cầu

để can thiệp thủ công,

vì nó tự động đưa ra quyết định khi nào nên kết thúc đào tạo.

Việc dừng lại sớm không phải là không có thách thức.

Thứ nhất, dừng sớm rất nhạy cảm với tiếng ồn

trong các số liệu xác nhận,

có thể dẫn tới việc dừng xe sớm.

Hơn nữa, hiệu quả của việc dừng sớm

phụ thuộc rất nhiều vào việc thiết lập thông số kiên nhẫn thích hợp,

có thể yêu cầu thử nghiệm

để tối ưu hóa cho một tác vụ hoặc tập dữ liệu cụ thể.

Bất chấp những hạn chế này,

dừng sớm vẫn là một công cụ có giá trị

để cải thiện hiệu suất mô hình

và hiệu quả đào tạo.

Một cách tiếp cận khác để cải thiện hiệu suất mô hình

đang kiểm tra điểm.

Điểm kiểm tra liên quan đến việc lưu các tham số của mô hình

định kỳ trong quá trình đào tạo,

thông thường, khi hiệu suất trên bộ xác thực được cải thiện.

Điều này đảm bảo rằng phiên bản tốt nhất của mô hình

với mức độ mất xác thực thấp nhất

hoặc độ chính xác xác nhận cao nhất được bảo tồn.

Quá trình này rất đơn giản.

Vào cuối mỗi thời đại,

hiệu suất của phiên bản hiện tại của mô hình

được so sánh với cái tốt nhất được lưu cho đến nay.

Nếu số liệu xác thực cho thấy sự cải thiện,

phiên bản mới được lưu vào đĩa,

thay thế phiên bản đã lưu trước đó.

Điều này đảm bảo rằng phiên bản tốt nhất của mô hình

luôn có thể phục hồi được,

bất kể quá trình đào tạo tiến triển như thế nào

hoặc nếu xảy ra sự gián đoạn không lường trước được.

Kiểm tra điểm cung cấp một số lợi thế.

Đầu tiên, nó đảm bảo rằng phiên bản tốt nhất

của mô hình được bảo tồn,

ngay cả khi việc tiếp tục đào tạo dẫn đến việc trang bị quá mức.

Thứ hai, nó cung cấp khả năng chịu lỗi,

hoạt động như một mạng lưới an toàn trong trường hợp hệ thống gặp sự cố

hoặc mất điện.

Thứ ba, nó cho phép sự linh hoạt,

cho phép bạn thử nghiệm các tiêu chí dừng khác nhau,

mà không có nguy cơ mất đi mô hình hoạt động tốt nhất.

Việc kiểm tra điểm mặc dù có một số hạn chế.

Lưu các tham số mô hình yêu cầu lưu trữ bổ sung,

có thể trở thành mối quan tâm đối với các mô hình lớn.

Hơn nữa, việc kiểm tra thường xuyên

chẳng hạn như lưu sau mỗi kỷ nguyên có thể gây ra sự chậm trễ

do hoạt động đầu vào đầu ra tăng lên.

Bất chấp những hạn chế này, việc kiểm tra điểm là một công cụ có giá trị

để duy trì chất lượng mô hình

và đảm bảo khả năng phục hồi đào tạo.