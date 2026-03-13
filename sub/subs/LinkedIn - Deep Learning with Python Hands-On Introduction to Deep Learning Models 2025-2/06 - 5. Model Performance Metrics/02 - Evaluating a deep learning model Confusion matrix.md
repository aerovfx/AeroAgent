# 02 - Đánh giá mô hình deep learning Ma trận nhầm lẫn

---

- [Người hướng dẫn] Trong video này, bạn sẽ học cách tạo

và giải thích ma trận nhầm lẫn của mô hình học sâu.

Tôi sẽ chạy mã trong tệp 05_02e.

Bạn có thể theo dõi

bằng cách hoàn thành các ô mã trống trong tệp 0502 B.

Lưu ý rằng video này là một giây,

trong chuỗi năm video hướng dẫn bạn thực hiện quy trình

đánh giá một mô hình học sâu trong Python.

Nếu chưa hãy xem video trước

để được giải thích chi tiết về mã trước đó.

Trước khi bắt đầu, hãy chạy mã chúng tôi đã tạo trong video đó

để môi trường của chúng ta tăng tốc.

Vì vậy, chúng ta sẽ tiếp tục và nhấp vào ô mã ở đây

và chạy mọi thứ ở trên.

Và tôi sẽ cuộn lên một chút để đảm bảo

rằng mã của chúng tôi đã hoàn tất trước khi chúng tôi tiếp tục.

Được rồi, ma trận nhầm lẫn sẽ cung cấp thêm thông tin chi tiết

vào hiệu suất của một mô hình bằng cách tóm tắt

mô hình thực hiện tốt như thế nào trong việc phân loại từng nhãn.

Điều này có thể giúp chúng tôi chẳng hạn,

xác định xem có chữ số không

thường bị phân loại sai bởi mô hình.

Để tạo một ma trận nhầm lẫn,

chúng ta sẽ sử dụng hàm ma trận nhầm lẫn

từ gói sklearn.metrics.

Vì vậy, chúng tôi bắt đầu bằng cách nhập hàm

và sau khi nhập một hàm, bây giờ chúng ta có thể gọi hàm đó

và chuyển cho nó các lớp thực và các lớp được dự đoán.

Và điều đó trả lại cho chúng ta một đối tượng.

Chúng ta sẽ gọi conf_matrix.

Hãy tiếp tục và chạy nó.

Bây giờ chúng ta có thể hình dung ma trận dưới dạng bản đồ nhiệt.

Vì vậy lần này chúng ta sẽ sử dụng đường biển

và chúng ta sẽ chỉ định chức năng bản đồ nhiệt

và sử dụng nó để hình dung ma trận nhầm lẫn của chúng tôi

để xem chính xác nó trông như thế nào.

Vì vậy, khi chúng tôi chạy nó, chúng tôi có được cảm giác khá tốt

về một cái nhìn toàn cảnh, về hiệu suất của mô hình của chúng tôi

cho mỗi nhãn.

Vì vậy, chúng ta thấy các nhãn thực sự trên trục Y,

và chúng ta thấy các nhãn được dự đoán trên trục X.

Các phần tử đường chéo của ma trận nhầm lẫn,

những cái có màu xanh đậm hơn, đại diện cho số

dự đoán chính xác cho từng nhãn,

trong khi các phần tử đường chéo biểu thị

những sự phân loại sai lầm.

Nhìn chung, khi nhìn vào điều này, chúng ta có thể thấy

rằng mô hình của chúng tôi hoạt động rất tốt

trong việc phân loại hầu hết các hình ảnh.

Tuy nhiên, chúng tôi quan sát thấy

rằng mô hình đôi khi nhầm lẫn bốn.

Đúng vậy, đôi khi có bốn cái ở đây.

Bốn chín, vậy chúng ta thấy số 19 ở đây,

đó là những con số bị phân loại sai.

Vì vậy, và chúng ta cũng thấy

số bảy đó đôi khi thường bị phân loại sai thành số chín.

Vì vậy, chúng tôi thấy những điều đó ở đây.

Mặc dù đây là những lỗi tương đối nhỏ so với

tới 956 hình ảnh được phân loại chính xác

của bốn và bảy.

Có lẽ nó đáng giá

để điều tra điều này thêm một chút

để xác định các lĩnh vực tiềm năng để cải thiện.

Vì vậy, trong video này, chúng tôi đã có thể tạo

và diễn giải ma trận nhầm lẫn cho mô hình học sâu.

Trong video tiếp theo, chúng tôi sẽ tạo

và giải thích độ chính xác cho từng nhãn lớp

để hiểu sâu hơn về hiệu suất của mô hình.

Hẹn gặp bạn ở đó.