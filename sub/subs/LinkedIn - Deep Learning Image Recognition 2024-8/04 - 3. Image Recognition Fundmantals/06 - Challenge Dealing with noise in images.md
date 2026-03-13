# 06 - Thử thách Xử lý nhiễu trong ảnh

---

(nhạc sôi động tươi sáng)

- Trong khi chúng ta nói về những thách thức trong Nhận dạng Hình ảnh,

chẳng hạn như điều kiện ánh sáng khác nhau,

sự tắc nghẽn, sự thay đổi về quy mô,

giải quyết sự mất cân bằng giữa các lớp, sự tương đồng giữa các lớp,

nhưng còn một điều nữa chúng ta chưa nói tới,

và đó là việc xử lý tiếng ồn.

Vì vậy, Giới thiệu về tiếng ồn.

Vì vậy, trước hết hãy xem tiếng ồn là gì.

Tiếng ồn trong hình ảnh có thể được nghĩ đến

như các biến thể ngẫu nhiên về độ sáng hoặc thông tin màu sắc.

Tiếng ồn có thể đến từ nhiều nguồn khác nhau,

như những hạn chế của cảm biến, điều kiện môi trường,

hoặc thậm chí trong quá trình truyền hình ảnh

chúng tôi có thể giới thiệu tiếng ồn.

Trong ngữ cảnh của chúng tôi, nhiễu xuất hiện dưới dạng thông số kỹ thuật hoặc biến thể ngẫu nhiên

làm che khuất các chi tiết thực sự của hình ảnh.

Chà, tại sao đây lại là vấn đề đối với chúng ta khi học sâu?

Đối với các mô hình của chúng tôi, tiếng ồn có thể là vấn đề đặc biệt.

Các mô hình được đào tạo về dữ liệu sạch, không có tiếng ồn

thực sự có thể gặp khó khăn trong việc nhận ra các mẫu hoặc đồ vật

khi tiếng ồn được đưa vào.

Điều này là do tiếng ồn có thể làm biến dạng các tính năng quan trọng

mà mô hình dựa vào để đưa ra dự đoán chính xác.

Làm thế nào chúng ta có thể mô phỏng nhiễu trong hình ảnh?

Vâng, để chuẩn bị cho mô hình của chúng ta về tiếng ồn,

điều kiện thực tế,

chúng ta có thể mô phỏng tiếng ồn trong quá trình đào tạo.

Bằng cách thêm nhiễu vào hình ảnh đào tạo của chúng tôi,

chúng ta có thể dạy các mô hình của mình trở nên mạnh mẽ hơn,

và để xử lý tốt hơn các điều kiện ồn ào

khi họ gặp chúng trong các ứng dụng thực tế.

Bây giờ, hãy tiếp tục và xem thử thách của chúng tôi.

Vì vậy, trong thử thách đặc biệt này,

tất cả những gì chúng ta cần làm là thêm phần tử thứ sáu vào đây,

xử lý nhiễu trong ảnh.

Vì vậy, hãy mở tệp Python 03_06_challenge,

và thách thức của chúng tôi trong phiên này là thêm yếu tố thứ sáu

vào danh sách thách thức của chúng tôi,

đó là xử lý nhiễu trong hình ảnh.

Vì vậy, hãy tiếp tục và bắt đầu nhập hàm,

xác định add_noise,

và nó sẽ chụp một hình ảnh

và sau đó nó sẽ lấy hệ số nhiễu,

và sau đó nó sẽ thực hiện thêm một số chức năng ở đây.

Bây giờ đến lượt bạn đọc sách

và thực hiện một số tìm kiếm sơ bộ về điều này

về cách chúng tôi có thể thêm nhiễu vào hình ảnh,

và tôi sẽ gặp bạn trong video giải pháp.