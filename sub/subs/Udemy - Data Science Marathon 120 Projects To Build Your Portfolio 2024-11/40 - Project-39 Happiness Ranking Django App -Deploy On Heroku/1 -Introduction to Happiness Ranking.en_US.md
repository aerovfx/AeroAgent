# 1 -Giới thiệu về Happiness Xếp hạng.en US

---

WEBVTT

Xin chào.

Trong dự án này, chúng tôi sẽ dự đoán thứ hạng của các quốc gia về chủ đề hạnh phúc.

Đó là lý do tại sao chúng tôi sẽ xây dựng mô hình học máy trên tập dữ liệu có niềm vui.

Xếp hạng theo chỉ số hạnh phúc.

Vì vậy, với tôi, tôi có một bộ dữ liệu về chỉ số hạnh phúc.

Và cùng với đó, chúng tôi sẽ đào tạo mô hình của mình và dự đoán chỉ số.

Tiến về phía trước.

Chỉ số hạnh phúc là gì?

Đó là chỉ số về mức độ hạnh phúc dựa trên kết quả khảo sát lần đầu tiên được sử dụng trong Báo cáo Hạnh phúc Thế giới năm 2012

Báo cáo.

Trong cuộc khảo sát, những người tham gia được yêu cầu đánh giá mức độ hạnh phúc của họ theo thang điểm từ 0 đến 10.

Chỉ số hạnh phúc được tính bằng cách lấy trung bình kết quả khảo sát của người trả lời.

Hiện nay.

Nó thực sự bắt nguồn từ đâu?

Và bạn có thể hỏi tại sao nó thực sự cần thiết.

Vì vậy, chỉ số Định nghĩa Hạnh phúc bắt nguồn từ Chỉ số Hạnh phúc Quốc gia GROSS của Bhutan.

Vâng, điều này có thể làm bạn ngạc nhiên, nhưng vào năm 1972, Bhutan bắt đầu ưu tiên hạnh phúc hơn các yếu tố khác,

chẳng hạn như sự giàu có được trao và tăng trưởng kinh tế.

Điều này đã truyền cảm hứng cho hạnh phúc.

Hội đồng đưa ra định nghĩa riêng về chỉ số hạnh phúc, được đưa ra trong Báo cáo Hạnh phúc Thế giới 2012

Báo cáo.

Không có thông tin chi tiết về dự án

Bây giờ dự án được chia thành ba phần.

Phần đầu tiên là xây dựng mô hình machine learning để dự đoán thứ hạng mức độ hạnh phúc hoặc mức độ hạnh phúc

chỉ số.

Cả hai đều giống nhau khi tôi nói với bạn hoặc trong bối cảnh tôi đang sử dụng.

Thứ hai, chúng tôi xây dựng một ứng dụng web hoặc ứng dụng web trên Django để gắn kết mô hình dự đoán.

Phần thứ ba hoặc phần cuối cùng là chúng tôi đã triển khai Dự án Django trên Heroku bằng cách sử dụng hoặc thông qua GitHub.

Vì vậy, mô hình học máy.

Vì vậy, chúng tôi bắt đầu bằng việc xây dựng mô hình học máy bằng mô hình hồi quy tuyến tính đơn giản và huấn luyện

mô hình đó bằng cách sử dụng tập dữ liệu chỉ số hạnh phúc.

Để hỗ trợ dự án này.

Chúng ta cũng sẽ thấy quy mô tiêu chuẩn đang hoạt động.

Nhưng tôi muốn nói rằng chúng tôi sẽ sử dụng bộ chia tỷ lệ tiêu chuẩn để chuẩn hóa tập dữ liệu của mình nhằm xử lý thêm.

Và cùng với đó, tôi cũng sẽ cho bạn biết lý do tại sao tôi cũng thực hiện nó.

Nhưng phần thứ hai là xây dựng ứng dụng Web Django.

Đây là phần thứ hai của khóa học nơi chúng ta sẽ xây dựng ứng dụng web bằng Django

khuôn khổ.

Chúng tôi gắn mô hình mà chúng tôi xây dựng ở phần trước hoặc phần đầu tiên trong phần này của khóa học hoặc dự án

chính nó.

Cuối cùng, phần cuối của khóa học sẽ triển khai ứng dụng Django trên Heroku bằng cách sử dụng

các kết nối tới GitHub.

Vì vậy, bây giờ chúng ta hãy chuyển sang phần đầu tiên của dự án này.