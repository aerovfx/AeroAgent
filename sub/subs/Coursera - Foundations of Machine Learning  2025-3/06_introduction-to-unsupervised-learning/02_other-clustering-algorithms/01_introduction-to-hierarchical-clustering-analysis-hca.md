# 01 giới thiệu-phân cấp-phân cụm-hca

---

Ở bài học trước,

chúng tôi đã tạo thành công

không được giám sát

mô hình học máy

để phân cụm

SKUID khác nhau.

Mặc dù K-means là

một thuật toán mạnh mẽ,

bạn vẫn phải xác định

số lượng cụm

sử dụng các phương pháp khác nhau,

chẳng hạn như hình bóng

điểm số và âm mưu khuỷu tay.

Đây là một trong những

nhược điểm lớn

của thuật toán K-means.

Một nhược điểm khác của

Thuật toán K-means là nó

giả định các cụm để

có dạng lồi.

Điều này có thể không phù hợp

cho tất cả các tập dữ liệu.

Tuy nhiên, có những khác

thuật toán để tạo

các cụm mà không cần phải

tìm ra cách tối ưu

số cụm.

Một thuật toán như vậy là

Phân cụm theo cấp bậc

Phân tích, hoặc HCA.

Ví dụ, hãy nói

bạn có sáu cuốn sách

nằm rải rác xung quanh.

Ban đầu, mỗi

cuốn sách được coi là

một cụm duy nhất như vậy

chúng tôi có sáu cụm.

Bây giờ thuật toán sẽ so sánh

mỗi cặp sách dựa trên

các đặc điểm như tác giả,

thể loại và xếp hạng.

Ở đây các cụm giống nhau nhất

là Cụm 1 và Cụm 2.

Cụm 1 là Harry

Hòn đá phù thủy của Potter,

và Cụm 2 là

Phòng chứa Bí mật.

Những thứ này sẽ được kết hợp

bởi vì họ có

cùng một tác giả,

thể loại và xếp hạng rất giống nhau.

Chúng được hợp nhất đầu tiên

để tạo thành một cụm.

Bây giờ cụm được hợp nhất này là

được xử lý như một thực thể duy nhất.

Hãy gọi cụm này là Alpha.

Tương tự, Giết một

Chim nhại và

Trợ giúp được nhóm lại với nhau

để hình thành cụm Beta.

Vì cả hai đều thuộc về

cùng thể loại,

khám phá chủ đề của lớp học,

chủng tộc, vân vân.

Họ cũng có

thậm chí xếp hạng tương tự

mặc dù chúng được viết

của hai tác giả khác nhau.

Kiêu hãnh và định kiến và

Mật mã Da Vinci vẫn còn

tự mình nhóm lại kể từ đó

họ không có gì chung.

Kiêu hãnh và Định kiến hợp nhất

với cụm beta.

Lý do là vì

xếp hạng tương tự

của Kiêu hãnh và Định kiến

cho hai cuốn sách còn lại.

Điều này tạo thành một sự kết hợp mới

cụm. Hãy gọi nó là Gama.

Sau đó thuật toán

sẽ hợp nhất cụm 3,

đó là Mật mã Da Vinci,

với cụm Gama.

Hãy gọi đây là

cụm đồng bằng mới.

Điều này cũng dựa trên

sự tương đồng trong đánh giá,

ngay cả khi chúng khác nhau

thể loại và tác giả.

Cuối cùng,

thuật toán sẽ hợp nhất

cụm alpha với

cụm delta để

tạo một cụm lớn.

Hãy gọi đây là trận chung kết

cụm Epsilon.

Không giống như K-means trong

phân cụm theo thứ bậc,

mỗi mẫu có thể thuộc về

tới nhiều cụm.

Chúng ta cũng không cần

chỉ định số lượng

các cụm lúc đầu.

Tuy nhiên, về mặt tính toán

xây dựng tốn kém,

và cuối cùng,

các cụm được chọn dựa trên

trên sơ đồ phân cấp,

điều đó chỉ khả thi

cho các tập dữ liệu nhỏ.