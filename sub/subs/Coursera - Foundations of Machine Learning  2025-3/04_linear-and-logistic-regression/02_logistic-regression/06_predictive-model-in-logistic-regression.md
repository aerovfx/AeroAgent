# 06 mô hình dự đoán trong logistic-hồi quy

---

Trong video này, chúng tôi sẽ

học cách xây dựng

mô hình dự đoán và

đánh giá nghiêm túc

hiệu suất của nó.

Nói một cách đơn giản hơn,

mục tiêu cuối cùng của chúng tôi là

làm cho chính xác

dự đoán về việc liệu

một sản phẩm sẽ bán

hơn 1.000

đơn vị dựa trên

các yếu tố dự đoán khác nhau.

Hãy bắt đầu bằng cách tạo

một cuốn sổ mới cho

cách tiếp cận mang tính dự đoán.

Hiện giờ chúng ta đã ổn rồi

khi viết mã cơ bản.

Tôi sẽ nhanh chóng thực hiện

tất cả các bước cơ bản

như chúng tôi đã làm trước đó cho một

phương pháp miêu tả.

Điều này sẽ bao gồm việc nhập khẩu

các thư viện,

đang tải tập dữ liệu,

áp dụng một mã hóa nóng,

kiểm tra dữ liệu

các loại dữ liệu,

thả giống nhau

cột và cuối cùng,

kiểm tra hình dạng của dữ liệu

Tương tự như các bước chúng tôi

theo sau trong hồi quy tuyến tính,

hãy chia tập dữ liệu thành

bộ huấn luyện và kiểm tra,

và kiểm tra hình dạng

của cả hai bộ.

Bây giờ dữ liệu

đã bị chia cắt,

hãy xây dựng

mô hình dự báo.

Chúng tôi sử dụng hậu cần

lớp hồi quy từ SQL học,

xây dựng một hệ thống hậu cần

mô hình hồi quy

và huấn luyện nó hoặc tập huấn luyện.

Bây giờ hãy đánh giá

hiệu suất

của mô hình sử dụng điểm F1.

Hãy kiểm tra hiệu suất trên

cả đào tạo và

các bộ thử nghiệm.

Với điểm F1 là 0,77,

cho cả việc đào tạo

và dữ liệu thử nghiệm,

mô hình chứng minh

hiệu suất nhất quán

trong việc xác định sản phẩm có

doanh số bán hàng vượt quá 1.000 đơn vị.

Sự đồng nhất như vậy giữa

điểm đào tạo và kiểm tra,

giảm nhẹ mối lo ngại

của việc trang bị quá mức.

Mặc dù số điểm 0,77 có vẻ

ưu việt ngay từ cái nhìn đầu tiên,

không có điểm chuẩn rõ ràng

hiệu quả vẫn còn tương đối.

Để có cái nhìn toàn diện hơn

đánh giá,

so sánh hiệu suất này với

các thuật toán khác như KNN

có thể cung cấp những hiểu biết sâu sắc hơn.

Đối với vấn đề phân loại này,

phương pháp KNN mang lại

điểm F1 là 0,87.

Sự khác biệt này gợi ý rằng

phương pháp KNN tốt hơn

hồi quy logistic về mặt

cân bằng độ chính xác và thu hồi

cho tập dữ liệu cụ thể này.

Như chúng ta đã thảo luận ở

mô-đun trước đó,

máy phát triển

mô hình học tập

là một quá trình lặp đi lặp lại

đòi hỏi phải cố gắng

một số cách tiếp cận khác nhau

cũng như các mô hình.

Khi chúng ta tiếp tục đi qua

khóa học này và khóa học này

chuyên môn,

chúng tôi sẽ tiếp tục cố gắng

cách tiếp cận khác nhau và

các mô hình cải tiến

hiệu suất

của hệ thống dự đoán của chúng tôi.

Khi mô-đun này kết thúc,

có một phát hiện quan trọng là chúng ta

nên ghi nhớ

trong khi đưa ra quyết định.

Cả hồi quy của chúng tôi

mô hình không thể đánh bại

tương ứng

số liệu hiệu suất

đạt được nhờ các mô hình KNN của chúng tôi.

Điều quan trọng cần lưu ý

rằng trong học máy,

không có một kích thước phù hợp cho tất cả.

Đối với khác nhau

báo cáo vấn đề,

thuật toán khác nhau

có thể hoạt động tốt hơn

Trong mô-đun tiếp theo,

chúng ta sẽ khám phá

thêm một máy được giám sát

thuật toán học tập

khám phá và giải quyết

vấn đề kinh doanh

cho các giải pháp tổng hợp.