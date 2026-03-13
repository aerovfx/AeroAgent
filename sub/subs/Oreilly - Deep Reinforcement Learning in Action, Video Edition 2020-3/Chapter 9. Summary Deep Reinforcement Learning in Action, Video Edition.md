# Chương 9. Tóm tắt Học tập tăng cường sâu trong thực tế, Phiên bản video đã được dịch

---

Bản tóm tắt. Học Q thông thường không hoạt động tốt trong cài đặt nhiều tác nhân vì môi trường trở nên không cố định khi các tác nhân học các chính sách mới.

Một môi trường không cố định có nghĩa là giá trị mong đợi của phần thưởng thay đổi theo thời gian.

Để xử lý tính không cố định này, hàm Q cần có quyền truy cập vào không gian hành động chung của các tác nhân khác.

Nhưng không gian hành động chung này mở rộng theo cấp số nhân theo số lượng tác nhân, điều này trở nên khó giải quyết đối với hầu hết các vấn đề thực tế.

Học tập Q lân cận có thể giảm thiểu quy mô theo cấp số nhân bằng cách chỉ tính toán trên không gian hành động chung của các lân cận trực tiếp của một tác nhân nhất định.

Nhưng thậm chí điều này có thể quá lớn nếu số lượng hàng xóm lớn.

Học tập Q trường trung bình, MFQ, tỷ lệ tuyến tính với số lượng tác nhân bởi vì chúng tôi chỉ tính toán một hành động trung bình chứ không phải là không gian hành động chung đầy đủ.