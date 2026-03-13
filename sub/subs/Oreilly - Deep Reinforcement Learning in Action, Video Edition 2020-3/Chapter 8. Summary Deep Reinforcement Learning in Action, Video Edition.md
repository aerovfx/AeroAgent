# Chương 8. Tóm tắt Học tập tăng cường sâu trong thực tế, Phiên bản video đã được dịch

---

Bản tóm tắt. Vấn đề về phần thưởng thưa thớt là khi một môi trường hiếm khi tạo ra tín hiệu phần thưởng hữu ích,

điều này thách thức nghiêm trọng cách DRL thông thường cố gắng học hỏi.

Vấn đề Phần thưởng thưa thớt có thể được giải quyết bằng cách tạo ra các tín hiệu phần thưởng tổng hợp mà chúng tôi gọi là Phần thưởng tò mò.

Mô-đun tò mò tạo ra các phần thưởng tổng hợp dựa trên mức độ khó dự đoán của trạng thái tiếp theo của môi trường,

khuyến khích tác nhân khám phá những phần khó đoán hơn của môi trường.

Mô-đun tò mò nội tại, ICM, bao gồm ba mạng thần kinh độc lập,

mô hình dự đoán thuận, mô hình nghịch đảo và bộ mã hóa.

Bộ mã hóa mã hóa các trạng thái chiều cao thành vectơ chiều thấp với các tính năng cấp cao,

giúp loại bỏ tiếng ồn và các tính năng tầm thường.

Mô hình dự đoán chuyển tiếp dự đoán trạng thái được mã hóa tiếp theo và lỗi của nó cung cấp tín hiệu Curiosity.

Mô hình nghịch đảo huấn luyện bộ mã hóa bằng cách lấy hai trạng thái được mã hóa liên tiếp và dự đoán hành động đã được thực hiện.

Trao quyền là một cách tiếp cận có liên quan chặt chẽ nhưng có tính thay thế đối với việc học tập dựa trên trí tò mò.

Trong Trao quyền, tác nhân được khuyến khích học cách tối đa hóa mức độ kiểm soát mà nó có đối với môi trường.