# 07 - Áp dụng chính quy bỏ học vào mô hình học sâu

---

- [Người hướng dẫn] Trong video này, bạn sẽ học cách

để áp dụng chính quy hóa bỏ học vào mô hình học sâu

để giảm việc trang bị quá mức.

Tôi sẽ viết mã trong tệp 02_07e.

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp 02_07b.

Đảm bảo chạy mã đã viết trước đó để nhập

và xử lý trước dữ liệu cũng như xây dựng

và huấn luyện mô hình cơ sở.

Tôi đã làm như vậy rồi.

Nhìn vào xác nhận

và đường cong chỉ số tổn thất đào tạo, chúng ta thấy

rằng mô hình cơ sở quá phù hợp với dữ liệu huấn luyện.

Một dấu hiệu rõ ràng về việc trang bị quá mức là sự khác biệt mà chúng ta thấy

trong các chỉ số tổn thất về đào tạo và xác thực,

có thể nhìn thấy trong các đường cong đào tạo ở trên.

Để giúp giảm thiểu việc trang bị quá mức, hãy thử

để áp dụng chính quy hóa bỏ học cho mô hình cơ sở.

Quá trình chính quy hóa bỏ học sẽ tắt ngẫu nhiên một phần

của các nơ-ron trong quá trình huấn luyện.

Điều này buộc mạng phải tìm hiểu các tính năng mạnh mẽ

không phụ thuộc quá nhiều vào các tế bào thần kinh cụ thể.

Để áp dụng chính quy hóa bỏ học cho mô hình cơ sở,

chúng tôi chỉ cần thêm một lớp bỏ học

sau mỗi lớp ẩn trong mạng của chúng tôi.

Ở đây chúng tôi chỉ định tỷ lệ phần trăm bỏ học là 0,5,

điều đó có nghĩa là 50% số nơ-ron sẽ bị loại bỏ

trong mỗi lần chuyển tiếp.

Để bắt đầu, chúng tôi nhập bỏ học

từ tensorflow.keras.layers.

Sau đó, khi chúng ta xác định cấu trúc của mô hình,

chúng tôi bao gồm một lớp bỏ học ở giữa mỗi lớp

của các lớp dày đặc.

Hãy tiếp tục và chạy mã của chúng tôi.

Tiếp theo, chúng tôi biên dịch mô hình chính quy.

Sau đó, chúng tôi đào tạo mô hình chính quy

chống lại dữ liệu của chúng tôi.

Lưu ý rằng chúng tôi đã chỉ định 15 kỷ nguyên.

Vì vậy, nó sẽ trải qua 15 chu kỳ huấn luyện.

Kích thước lô là 128,

và mức phân chia xác thực là 0,1.

Vì vậy, hãy cho mô hình của chúng ta một chút thời gian để đào tạo.

Vậy chúng ta đang ở kỷ nguyên thứ 13 và thứ 14,

và bây giờ chúng ta đang ở kỷ nguyên cuối cùng, 15.

Bây giờ mô hình đó đã được đào tạo xong,

bây giờ chúng ta có thể vẽ sơ đồ đoàn tàu

và số liệu mất xác thực để xem

việc bỏ học có tác động gì đến mô hình.

Vì vậy lần này chúng ta thấy rằng việc đào tạo

và số liệu về việc mất xác thực bắt đầu hơi khác nhau một chút,

nhưng sau đó bắt đầu hội tụ khi quá trình đào tạo tiếp tục.

Điều này chỉ ra rằng việc chính quy hóa việc bỏ học

đang giúp mô hình khái quát hóa tốt hơn

bằng cách ngăn chặn nó khớp quá mức với dữ liệu huấn luyện.

Công việc tuyệt vời.

Bây giờ bạn đã biết cách sử dụng chính quy bỏ học

để giảm tình trạng trang bị quá mức trong mô hình học sâu bằng Python.