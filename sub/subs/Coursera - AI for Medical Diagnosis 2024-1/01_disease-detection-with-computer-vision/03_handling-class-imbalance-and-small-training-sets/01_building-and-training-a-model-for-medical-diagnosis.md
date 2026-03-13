# 01 xây dựng và đào tạo mô hình chẩn đoán y khoa

---

Bây giờ bạn đã thấy một số

ứng dụng tiên tiến của học sâu vào hình ảnh y tế

vấn đề phân loại,

chúng ta sẽ xem xét cách bạn có thể xây dựng khả năng học sâu của riêng mình

mô hình cho

nhiệm vụ hình ảnh y tế của

sử dụng ngực

X-quang để phát hiện nhiều

bệnh tật với một mô hình duy nhất.

Chúng ta sẽ đi qua quá trình đào tạo

một mô hình giải thích X-quang ngực,

và nhìn vào những thách thức chính mà

bạn sẽ phải đối mặt trong quá trình này, và

làm thế nào bạn có thể giải quyết thành công.

Chúng ta sẽ bắt đầu bằng việc xem xét nhiệm vụ

giải thích X-quang ngực.

Chụp X-quang ngực là một trong những phương pháp quan trọng nhất

thủ tục chẩn đoán hình ảnh thông thường

trong y học với khoảng 2 tỷ rương

X-quang được thực hiện trong một năm.

Giải thích X-quang ngực là rất quan trọng đối với

phát hiện nhiều bệnh

bao gồm cả viêm phổi

và ung thư phổi ảnh hưởng đến hàng triệu người

của người dân trên toàn thế giới mỗi năm.

Bây giờ là một bác sĩ X quang được đào tạo về

giải thích hình ảnh chụp X-quang ngực

khi chụp X-quang ngực,

nhìn vào phổi, tim,

và các khu vực khác để tìm kiếm

manh mối có thể gợi ý

nếu bệnh nhân bị viêm phổi hoặc

ung thư phổi hoặc tình trạng khác.

Hãy nhìn vào một điều bất thường bình thường,

gọi là khối lượng, hình như thế.

Và tôi sẽ không làm điều đầu tiên

định nghĩa khối lượng là gì

nhưng hãy nhìn vào ba cái rương

Tia X có chứa một

khối và 3 phim X-quang ngực đều bình thường.

Sau đó tôi có thể cho bạn xem một cái mới

chụp X-quang ngực đây

và yêu cầu bạn xác định

có khối lượng hay không.

Bạn có thể xác định chính xác

rằng tấm X-quang ngực này có chứa một khối.

Và đây là khối lượng có thể trông như thế này

tương tự như những thứ bạn thấy

trong những hình ảnh này, nhưng không giống với

bất cứ điều gì bạn nhìn thấy trong những hình ảnh này.

Cách bạn học rất giống nhau

về cách chúng ta sẽ dạy một thuật toán

để phát hiện khối lượng.

Để chúng ta tham khảo, khối lượng là

được định nghĩa là một tổn thương, hay nói cách khác

tổn thương mô, nhìn thấy trên X-quang ngực như

đường kính lớn hơn 3cm.

Hãy xem chúng ta có thể rèn luyện chúng ta như thế nào

thuật toán xác định khối lượng.