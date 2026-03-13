## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong phần này, chúng ta sẽ khám phá tế bào thần kinh nhân tạo là gì và chúng hoạt động như thế nào.

### 00:00:05.000 - 00:00:12.000
Chúng là một cơ chế lấy cảm hứng từ thiết kế và hoạt động của các tế bào thần kinh sinh học.

### 00:00:13.000 - 00:00:19.000
Nếu có bất kỳ nhà sinh vật học nào xem video này, tôi xin lỗi trước vì đã đơn giản hóa quá mức

### 00:00:19.000 - 00:00:20.000
tế bào thần kinh hoạt động như thế nào.

### 00:00:21.000 - 00:00:23.000
Đơn giản hóa rất nhiều.

### 00:00:23.000 - 00:00:29.000
Có thể nói nơ-ron là một tế bào thuộc hệ thần kinh của động vật có khả năng tiếp nhận, xử lý

### 00:00:29.000 - 00:00:32.000
và gửi tín hiệu điện hoặc hóa học.

### 00:00:33.000 - 00:00:36.000
Với các tế bào thần kinh khác mà nó được kết nối.

### 00:00:36.000 - 00:00:40.000
Những kết nối này được gọi là khớp thần kinh.

### 00:00:41.000 - 00:00:47.000
Tế bào thần kinh được kết nối với các tế bào thần kinh khác thông qua các sợi nhánh và sợi trục của nó là các đầu của tế bào.

### 00:00:47.000 - 00:00:54.000
Các sợi nhánh là các kết nối qua đó tế bào thần kinh nhận được các tín hiệu hóa học và điện này.

### 00:00:54.000 - 00:01:01.000
Các tín hiệu nhận được sẽ được tổng hợp và xử lý trong thân tế bào và khi chúng vượt quá một mức nhất định

### 00:01:01.000 - 00:01:07.000
cường độ mạnh, tế bào phát ra các xung điện qua sợi trục đến các tế bào khác.

### 00:01:08.000 - 00:01:14.000
Chúng ta có thể nói rằng đuôi gai là bộ phận của tế bào nhận kích thích và sợi trục là bộ phận

### 00:01:14.000 - 00:01:18.000
một phần của tế bào truyền tín hiệu.

### 00:01:19.000 - 00:01:24.000
Thông qua cơ chế này, tế bào thần kinh có thể tham gia vào các nhiệm vụ vận động và nhận thức.

### 00:01:25.000 - 00:01:32.000
Chà, các nhà nghiên cứu đã phát triển mạng lưới thần kinh đã quan sát cơ chế này và lấy nó làm nguồn cảm hứng

### 00:01:32.000 - 00:01:36.000
để phát triển một mô hình tính toán dựa trên các nơ-ron này.

### 00:01:37.000 - 00:01:41.000
Và mô hình tính toán này được gọi là nơron nhân tạo.

### 00:01:42.000 - 00:01:48.000
Nơ-ron nhân tạo là một hàm toán học lấy các giá trị số đầu vào từ các nơ-ron khác,

### 00:01:48.000 - 00:01:56.000
mỗi trong số chúng có cường độ khác nhau được biểu thị bằng tham số w để đo cường độ của

### 00:01:56.000 - 00:01:59.000
kết nối giữa nơron nguồn và nơron đích.

### 00:02:00.000 - 00:02:08.000
Và sau đó nơ-ron tổng hợp tất cả các tín hiệu thu được từ các nơ-ron nguồn và được tính trọng số bởi chúng.

### 00:02:08.000 - 00:02:14.000
cường độ và nó áp dụng hàm kích hoạt cho giá trị tổng hợp này.

### 00:02:15.000 - 00:02:22.000
Kết quả của hàm kích hoạt này là tín hiệu mà nơ-ron sẽ truyền đến các nơ-ron của

### 00:02:22.000 - 00:02:25.000
lớp tiếp theo mà nó được kết nối.

### 00:02:26.000 - 00:02:32.000
Vậy tóm lại, nơron nhân tạo đơn giản là một hàm toán học tổng hợp và biến đổi

### 00:02:32.000 - 00:02:38.000
tín hiệu nhận được từ các nơ-ron khác và sau đó truyền giá trị được chuyển đổi.

### 00:02:40.000 - 00:02:46.000
Chúng ta có thể sử dụng các hàm kích hoạt khác nhau tùy thuộc vào giá trị mà chúng ta muốn truyền tới

### 00:02:46.000 - 00:02:47.000
các lớp.

### 00:02:48.000 - 00:02:52.000
Lớp kích hoạt đơn giản nhất được gọi là hàm nhận dạng.

### 00:02:52.000 - 00:03:00.000
Hàm này không thực hiện bất kỳ thay đổi nào đối với giá trị được tổng hợp từ đầu vào nhận được từ các nơ-ron khác.

### 00:03:01.000 - 00:03:06.000
Nó chỉ đơn giản là truyền giá trị đó đến lớp tiếp theo mà không sửa đổi nó.

### 00:03:07.000 - 00:03:13.000
Mạng nơ-ron có chức năng kích hoạt này ở tất cả các lớp sẽ học rất hiệu quả nhưng không

### 00:03:13.000 - 00:03:17.000
có khả năng xấp xỉ chính xác các hàm rất phức tạp.

### 00:03:18.000 - 00:03:23.000
Chúng tôi sẽ chỉ sử dụng chức năng nhận dạng này trong lớp đầu ra.

### 00:03:24.000 - 00:03:30.000
Ở các lớp bên trong, chúng ta sẽ sử dụng các hàm phi tuyến đặc biệt ở các lớp ẩn.

### 00:03:30.000 - 00:03:35.000
Đó là các lớp không có liên hệ với bên ngoài mạng lưới thần kinh.

### 00:03:36.000 - 00:03:41.000
Chúng ta sẽ sử dụng một hàm kích hoạt được gọi là hàm chỉnh lưu.

### 00:03:42.000 - 00:03:50.000
Hàm kích hoạt này chuyển đổi giá trị tổng hợp từ đầu vào của các nơ-ron khác thành 0 nếu

### 00:03:50.000 - 00:03:52.000
giá trị tổng hợp là âm.

### 00:03:53.000 - 00:03:58.000
Và mặt khác, nó không thực hiện bất kỳ sửa đổi nào đối với giá trị tổng hợp.

### 00:03:59.000 - 00:04:03.000
Nghĩa là, nếu giá trị tổng hợp từ các nơ-ron khác là năm.

### 00:04:03.000 - 00:04:07.000
Chức năng chỉnh lưu sẽ để nguyên như vậy.

### 00:04:08.000 - 00:04:12.000
Và nơron sẽ truyền giá trị 5 tới lớp tiếp theo.

### 00:04:13.000 - 00:04:20.000
Tuy nhiên, nếu giá trị tổng hợp là âm 5 thì hàm chỉnh lưu sẽ chuyển đổi nó thành

### 00:04:20.000 - 00:04:23.000
0 trước khi truyền nó sang lớp tiếp theo.

### 00:04:24.000 - 00:04:31.000
Chức năng này được sử dụng như một chức năng kích hoạt trong các lớp ẩn vì nó tăng tốc và tạo điều kiện thuận lợi cho việc

### 00:04:31.000 - 00:04:38.000
quá trình học của mạng nơ-ron, đặc biệt khi mạng có nhiều lớp ẩn.

### 00:04:38.000 - 00:04:43.000
Ngoài ra, nó cho phép mạng nơ-ron xấp xỉ các hàm phức tạp hơn.

### 00:04:44.000 - 00:04:52.000
Một nơron sử dụng chức năng kích hoạt này được gọi là đơn vị tuyến tính được chỉnh lưu Relu.

### 00:04:53.000 - 00:04:58.000
Một ví dụ khác về hàm kích hoạt tuyến tính là hàm sigmoid.

### 00:04:58.000 - 00:05:05.000
Hàm kích hoạt này nén các giá trị được tổng hợp từ các nơ-ron khác vào phạm vi giá trị

### 00:05:05.000 - 00:05:07.000
giữa 0 và 1.

### 00:05:07.000 - 00:05:09.000
Trước khi truyền bá giá trị đó.

### 00:05:11.000 - 00:05:17.000
Hàm này thường được sử dụng ở lớp cuối cùng của mạng nơron khi chúng ta muốn tính toán đầu ra

### 00:05:17.000 - 00:05:25.000
bởi mạng lưới thần kinh là một giá trị xác suất vì tất nhiên xác suất luôn nằm trong khoảng 0

### 00:05:25.000 - 00:05:26.000
và 1.

### 00:05:27.000 - 00:05:33.000
Tuy nhiên, chức năng kích hoạt này không được sử dụng ở các lớp bên trong của mạng nơ-ron vì nó

### 00:05:33.000 - 00:05:37.000
làm chậm và cản trở quá trình học tập.

