# 04 - Mạng lưới thần kinh học như thế nào

---

- [Người hướng dẫn] Tương tự như những người được giám sát khác

mô hình học máy,

chúng tôi đào tạo mạng lưới thần kinh nhân tạo bằng cách sử dụng dữ liệu

bao gồm một tập hợp các biến độc lập

và một biến phụ thuộc.

Mục tiêu là để mạng lưới thần kinh học

bằng cách mô hình hóa mối quan hệ giữa các bộ tín hiệu đầu vào,

các biến độc lập

và các tín hiệu đầu ra tương ứng phụ thuộc vào một biến.

Khi mạng nơ-ron xử lý từng bộ tín hiệu đầu vào,

nó học cách dự đoán chính xác đầu ra liên quan

bằng cách tăng cường hoặc làm suy yếu các kết nối

giữa các tế bào thần kinh dựa trên các mẫu

được quan sát trong dữ liệu huấn luyện.

Để làm điều này, các mạng sử dụng một kỹ thuật gọi là

lan truyền ngược, bao gồm việc điều chỉnh lặp đi lặp lại

trọng số và thành kiến kiểm soát

tín hiệu đi qua mạng như thế nào.

Mỗi chu kỳ huấn luyện lặp đi lặp lại trong quá trình lan truyền ngược đều được biết trước

như một kỷ nguyên và bao gồm một giai đoạn chuyển tiếp

và một giai đoạn lùi lại.

Để minh họa cách hoạt động của lan truyền ngược, hãy đi bộ

thông qua một ví dụ đơn giản về mạng lưới thần kinh học

để dự đoán mức lương hàng năm của nhân viên dựa trên số năm làm việc của họ

kinh nghiệm, trình độ học vấn và ngành nghề.

Mạng lưới thần kinh xử lý dữ liệu bằng số,

vì vậy bất kỳ biến phân loại nào trước tiên phải

được mã hóa bằng số trước khi chúng được đưa vào mạng.

Biến trình độ học vấn có thể được mã hóa

như Trung học bằng 1, Cử nhân bằng 2,

và Masters bằng 3,

và các giá trị cho biến ngành có thể được mã hóa

như Công nghệ bằng 1, Tài chính bằng 2,

và Giáo dục bằng 3.

Sau khi mã hóa dữ liệu đầu vào sẽ như thế này.

Dữ liệu được mã hóa được đưa vào các nút đầu vào của mạng,

với mỗi nút đại diện cho một tính năng trong dữ liệu đầu vào.

Quá trình huấn luyện lan truyền ngược bắt đầu

với một giai đoạn chuyển tiếp

nơi mạng lưới thần kinh đưa ra dự đoán ban đầu

dựa trên dữ liệu đầu vào.

Để đưa ra dự đoán ban đầu,

mạng bắt đầu bằng một bộ

của các trọng số và độ lệch được khởi tạo ngẫu nhiên.

Khi mỗi tín hiệu đầu vào truyền qua mạng,

mạng tính toán tổng trọng số của đầu vào

và đưa ra dự đoán.

Lưu ý rằng vì đây là một vấn đề hồi quy,

mức lương dự đoán chỉ đơn giản là tổng trọng số

cộng với sự thiên vị.

Mặc dù hữu ích cho các vấn đề phân loại,

chức năng kích hoạt thường không được sử dụng

trong lớp đầu ra của mô hình hồi quy.

Bây giờ mạng đã đưa ra dự đoán,

nó kết thúc giai đoạn chuyển tiếp

và chuyển sang giai đoạn lùi lại,

đó là tất cả về việc cải thiện độ chính xác

của những dự đoán trong tương lai.

Trong giai đoạn này, mạng so sánh giá trị dự đoán

là 10.000,13 USD

với giá trị thực tế là 60.000 USD từ dữ liệu huấn luyện,

bằng cách tính toán sai số dựa trên hàm mất mát.

Đối với các vấn đề hồi quy,

hàm mất mát thông thường là sai số bình phương trung bình, hay MSE.

Lỗi lớn cho thấy

rằng dự đoán của mô hình là không chính xác.

Để nâng cao độ chính xác của các dự đoán trong tương lai,

sự lan truyền ngược có ích

của một kỹ thuật tối ưu hóa được gọi là giảm độ dốc

để tìm ra trọng lượng là bao nhiêu

và các thành kiến nên được điều chỉnh trong mạng.

Giả sử các điều chỉnh sau được thực hiện

trong giai đoạn lùi dựa trên lỗi.

Sau khi điều chỉnh trọng số và độ lệch,

giai đoạn lùi kết thúc, kỷ nguyên đầu tiên cũng vậy.

Trong kỷ nguyên thứ hai, mạng sử dụng các trọng số được cập nhật

và thiên vị để đưa ra một dự đoán khác

trong giai đoạn phía trước.

Mặc dù đây là một sự cải thiện so với dự đoán ban đầu

10.000 USD, vẫn còn quá xa so với mức lương thực tế

là 60.000 USD.

Ở pha lùi, mô hình tính toán một lỗi mới

và điều chỉnh trọng số và độ lệch cho phù hợp.

Điều này kết thúc kỷ nguyên 2.

Quá trình lan truyền thuận, tính toán lỗi,

và sự lan truyền ngược sẽ xảy ra qua nhiều thời đại.

Với mỗi thời đại,

mạng sẽ giảm dần lỗi

được tính bằng hàm mất mát.

Sau nhiều kỷ nguyên,

mạng nơ-ron sẽ đạt tới sự hội tụ.

Điều này có nghĩa là các cập nhật về trọng số

và độ lệch sẽ trở nên rất nhỏ,

và dự đoán của mô hình sẽ ổn định.

Tại thời điểm này, mô hình đã học thành công

cách dự đoán mức lương của nhân viên

dựa trên số năm kinh nghiệm, trình độ học vấn,

và loại ngành.

Mạng bây giờ có thể được sử dụng

để dự đoán mức lương của nhân viên mới không tham gia

của tập huấn luyện với độ chính xác cao.