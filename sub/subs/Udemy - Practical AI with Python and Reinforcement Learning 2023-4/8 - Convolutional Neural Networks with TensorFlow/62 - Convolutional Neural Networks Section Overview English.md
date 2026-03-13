# 62 - Tổng quan về phần Mạng thần kinh chuyển đổi bằng tiếng Anh

---

Chào mừng mọi người đến với phần này về mạng nơ ron tích chập.

Vì vậy, mạng nơ-ron tích chập là một kiến trúc cụ thể của mạng nơ-ron cực kỳ hiệu quả

trong việc xử lý dữ liệu hình ảnh.

Và bài giảng này, tôi chỉ muốn ôn lại nhanh những gì chúng ta sẽ học trong phần này

của khóa học.

Chúng ta sẽ bắt đầu bằng cách cố gắng tìm hiểu lý thuyết đằng sau mạng lưới thần kinh tích chập và

điều gì khiến chúng khác biệt với mạng lưới thần kinh nhân tạo.

Chúng ta sẽ nói về Col của hình ảnh và các bộ lọc tích chập cũng như việc kéo các lớp khi chúng ta hiểu được

lý thuyết đằng sau mạng lưới thần kinh tích chập.

Chúng ta sẽ tiếp tục và giải quyết hai bộ dữ liệu thực sự nổi tiếng.

Tập dữ liệu M này đang học cách áp dụng mạng nơ ron tích chập cho hình ảnh thang độ xám.

Và sau đó chúng ta sẽ chuyển sang hình ảnh màu chẳng hạn như tập dữ liệu Saffar 10, về cơ bản là mở rộng nó ra

với ba kênh màu đỏ, lục và lam.

Khi chúng tôi hiểu cách làm việc với các tập dữ liệu cơ bản đó, chúng tôi sẽ mở rộng sang làm việc với hình ảnh thực.

các tập tin, thứ gì đó bạn sẽ gặp trong thế giới thực.

Các tệp JPEG hoặc tệp PMG, v.v. như thế nào?

Vì vậy, chúng tôi cũng sẽ sử dụng mạng lưới thần kinh tích chập để phân tích những thứ như hình ảnh bệnh sốt rét, máu

phân loại tế bào.

Vì vậy chúng ta sẽ có nhiều hình ảnh khác nhau.

Một số tế bào máu sẽ bị nhiễm bệnh sốt rét, số khác thì không.

Và chúng tôi sẽ xây dựng một mạng tích chập có thể thực sự phát hiện được chỉ dựa trên hình ảnh

tế bào máu có bị nhiễm trùng hay không.

Sau đó, chúng ta sẽ tiếp tục và kiểm tra các kỹ năng mới bằng bài tập mạng nơ ron tích chập theo kiểu

tập dữ liệu hình ảnh.

Được rồi, chúng ta hãy bắt đầu bằng việc tìm hiểu về lý thuyết.

Tôi sẽ gặp bạn ở đó.