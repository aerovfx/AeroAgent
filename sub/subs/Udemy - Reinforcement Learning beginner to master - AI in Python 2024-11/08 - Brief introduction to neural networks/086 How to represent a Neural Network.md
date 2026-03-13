## Nội dung

### 00:00:00.000 - 00:00:06.000
Bây giờ chúng ta đã biết mạng lưới thần kinh là gì và cấu trúc của nó, nhưng chúng ta vẫn cần biết cách thực hiện.

### 00:00:06.000 - 00:00:12.000
chúng ta sẽ trình bày mạng lưới thần kinh trong mã của mình và cách chúng ta sẽ sử dụng nó để ước tính

### 00:00:12.000 - 00:00:13.000
hàm giá trị.

### 00:00:14.000 - 00:00:18.000
Đây là cấu trúc của một mạng lưới thần kinh ba lớp.

### 00:00:18.000 - 00:00:21.000
Như bạn có thể thấy, lớp đầu vào có ba nơ-ron.

### 00:00:22.000 - 00:00:30.000
Lớp ẩn duy nhất mà mạng này có sáu nơ-ron và lớp đầu ra có hai nơ-ron.

### 00:00:31.000 - 00:00:39.000
Nếu chúng ta muốn giải quyết một nhiệm vụ điều khiển trong đó trạng thái có ba chiều và có sẵn hai hành động,

### 00:00:39.000 - 00:00:46.000
mạng nơ-ron này hoàn hảo vì chúng ta có thể huấn luyện nó để ước tính giá trị Q của hai hành động cho

### 00:00:46.000 - 00:00:49.000
mỗi trạng thái mà chúng tôi cung cấp làm đầu vào.

### 00:00:50.000 - 00:00:52.000
Bây giờ chúng ta hãy xem xét mạng lưới thần kinh theo từng phần.

### 00:00:53.000 - 00:00:57.000
Ở đây chúng ta có phần đầu tiên, lớp đầu vào và lớp ẩn.

### 00:00:57.000 - 00:01:04.000
Với các kết nối của chúng, chúng ta sẽ biểu diễn phần này của mạng nơ-ron bằng cách sử dụng vectơ làm đầu vào.

### 00:01:04.000 - 00:01:10.000
Vector x này ở đây và đây là vector có các giá trị đi vào mạng nơ-ron thông qua

### 00:01:10.000 - 00:01:11.000
lớp đầu vào.

### 00:01:12.000 - 00:01:18.000
Trong trường hợp của chúng tôi, nó sẽ là một vectơ có các giá trị cho từng chiều của trạng thái.

### 00:01:18.000 - 00:01:25.000
Mặt khác, chúng tôi sẽ lưu trữ một ma trận biểu thị các kết nối giữa hai lớp và mỗi lớp

### 00:01:25.000 - 00:01:32.000
phần tử bên trong ma trận đó sẽ biểu thị cường độ kết nối giữa một nơ-ron từ

### 00:01:32.000 - 00:01:36.000
lớp đầu vào và một nơ-ron từ lớp ẩn.

### 00:01:36.000 - 00:01:43.000
Chỉ số đầu tiên của mỗi phần tử đại diện cho nơ-ron từ lớp đầu vào mà từ đó kết nối

### 00:01:43.000 - 00:01:52.000
xuất hiện và chỉ mục thứ hai cho mỗi phần tử đại diện cho nơ-ron đích trong lớp ẩn.

### 00:01:53.000 - 00:01:59.000
Như vậy, cột đầu tiên của ma trận kết nối thể hiện cường độ kết nối giữa

### 00:01:59.000 - 00:02:05.000
tất cả các nơ-ron trong lớp đầu vào với nơ-ron đầu tiên từ lớp ẩn.

### 00:02:05.000 - 00:02:12.000
Cột thứ hai biểu thị các kết nối đến nơ-ron thứ hai từ lớp ẩn, v.v.

### 00:02:12.000 - 00:02:15.000
vân vân với tất cả các cột.

### 00:02:15.000 - 00:02:21.000
Ma trận kết nối sẽ có số hàng bằng số nơ-ron trong lớp đầu vào và số lượng

### 00:02:21.000 - 00:02:25.000
cột vì có các nơ-ron trong lớp ẩn.

### 00:02:25.000 - 00:02:33.000
Cuối cùng, chúng ta sẽ có một vectơ tên là H sẽ chứa kết quả xử lý đầu vào cho mỗi nơ-ron.

### 00:02:33.000 - 00:02:40.000
Vectơ này thu được bằng cách tính tích giữa vectơ x và ma trận W1.

### 00:02:40.000 - 00:02:47.000
Phần tử đầu tiên của vectơ này chứa đầu vào tổng hợp nhân với cường độ kết nối của nó

### 00:02:47.000 - 00:02:48.000
cho nơron đầu tiên.

### 00:02:49.000 - 00:02:54.000
Một chức năng kích hoạt được áp dụng cho đầu vào tổng hợp này.

### 00:02:54.000 - 00:03:01.000
Giá trị thứ hai trong vectơ này tương ứng với kết quả của nơron thứ hai xử lý đầu vào

### 00:03:01.000 - 00:03:02.000
từ lớp trước đó.

### 00:03:02.000 - 00:03:09.000
Tất nhiên, nhân nó với cường độ của từng đầu vào rồi áp dụng hàm kích hoạt.

### 00:03:09.000 - 00:03:11.000
Và vân vân và vân vân.

### 00:03:12.000 - 00:03:17.000
Vector sẽ có số phần tử bằng số nơ-ron trong lớp ẩn và nó chứa

### 00:03:17.000 - 00:03:22.000
các giá trị mà lớp nơ-ron này sẽ truyền sang lớp tiếp theo.

### 00:03:24.000 - 00:03:29.000
Bây giờ chúng ta hãy xem phần thứ hai của mạng lưới thần kinh, nơi chúng ta sẽ kết nối lớp ẩn với

### 00:03:29.000 - 00:03:31.000
lớp đầu ra.

### 00:03:31.000 - 00:03:37.000
Vì có sáu nơ-ron ở lớp ẩn và hai nơ-ron ở lớp đầu ra nên ma trận kết nối

### 00:03:37.000 - 00:03:41.000
sẽ có sáu hàng và hai cột.

### 00:03:41.000 - 00:03:47.000
Cột đầu tiên biểu thị cường độ kết nối giữa các nơ-ron trong lớp ẩn

### 00:03:47.000 - 00:03:50.000
và nơ-ron đầu tiên trên lớp đầu ra.

### 00:03:51.000 - 00:03:56.000
Cột thứ hai sẽ biểu thị cường độ kết nối giữa các tế bào thần kinh trong vùng ẩn.

### 00:03:56.000 - 00:03:59.000
lớp và nơron đầu ra thứ hai.

### 00:03:59.000 - 00:04:07.000
Do đó, vectơ đầu vào của lớp đầu ra bây giờ sẽ là vectơ h sẽ được xử lý

### 00:04:07.000 - 00:04:13.000
đầu vào là các giá trị mà lớp ẩn sẽ truyền đến lớp đầu ra.

### 00:04:14.000 - 00:04:21.000
Vectơ đầu ra sẽ là kết quả của việc tổng hợp và xử lý các đầu vào theo lớp đầu ra,

### 00:04:22.000 - 00:04:29.000
và trong trường hợp này nó sẽ bao gồm một vectơ có hai giá trị vì chúng ta có hai nơ-ron.

### 00:04:30.000 - 00:04:37.000
Vectơ này thu được bằng cách nhân vectơ h với ma trận kết nối w hai.

### 00:04:38.000 - 00:04:44.000
Bây giờ chúng ta hãy xem xét toàn bộ mạng lưới thần kinh và đi theo đường dẫn của các giá trị được nhập làm đầu vào cho đến khi

### 00:04:44.000 - 00:04:46.000
họ để lại như đầu ra.

### 00:04:48.000 - 00:04:56.000
Vectơ x đi qua lớp đầu vào và được nhân với ma trận kết nối W1.

### 00:04:57.000 - 00:05:00.000
Kết quả là một vectơ gồm sáu phần tử.

### 00:05:00.000 - 00:05:09.000
Chúng tôi áp dụng chức năng kích hoạt của lớp ẩn và do đó chúng tôi thu được vectơ h.

### 00:05:09.000 - 00:05:16.000
Sau đó, các giá trị của vectơ này được truyền đến lớp đầu ra bằng cách nhân chúng với ma trận

### 00:05:16.000 - 00:05:17.000
của các kết nối w.

### 00:05:20.000 - 00:05:25.000
Và sau đó chức năng kích hoạt của lớp đầu ra sẽ được áp dụng cho kết quả.

### 00:05:26.000 - 00:05:30.000
Và đó là những kết quả đầu ra từ mạng lưới thần kinh.

### 00:05:31.000 - 00:05:38.000
Nếu bạn để ý, mạng lưới thần kinh không gì khác hơn là một hàm, một hàm có các tham số w

### 00:05:38.000 - 00:05:43.000
có thể được điều chỉnh để sửa đổi kết quả đầu ra mà chúng tạo ra.

### 00:05:44.000 - 00:05:50.000
Do đó, mạng nơ-ron có thể được sử dụng để tính gần đúng các hàm và như các hàm xấp xỉ hàm, chúng

### 00:05:50.000 - 00:05:53.000
rất linh hoạt và rất mạnh mẽ.

### 00:05:53.000 - 00:06:00.000
Mạng lưới thần kinh càng có nhiều lớp ẩn thì các hàm phức tạp càng có thể xấp xỉ chính xác,

### 00:06:00.000 - 00:06:05.000
mặc dù nó sẽ đòi hỏi nhiều tính toán và trí nhớ hơn trong quá trình học tập.

### 00:06:06.000 - 00:06:12.000
Trong các bài tập viết mã, chúng ta sẽ sử dụng thư viện PyTorch để xây dựng mạng lưới thần kinh của mình.

### 00:06:13.000 - 00:06:20.000
Và chúng ta sẽ thực hiện điều đó bằng cách sử dụng một lớp có tên là Tuần tự, lớp này cho phép chúng ta xây dựng mạng lưới thần kinh áp dụng các phép toán

### 00:06:20.000 - 00:06:26.000
đến đầu vào theo cách tuần tự mà đầu vào của chúng ta đi qua lớp đầu vào.

### 00:06:26.000 - 00:06:29.000
Sau đó chúng được nhân với ma trận kết nối.

### 00:06:29.000 - 00:06:32.000
Sau đó, chức năng kích hoạt từ lớp ẩn sẽ được áp dụng.

### 00:06:33.000 - 00:06:33.000
Vân vân.

### 00:06:33.000 - 00:06:34.000
Vân vân.

### 00:06:34.000 - 00:06:41.000
Vì vậy, bên trong lớp tuần tự này, chúng ta có thể truyền một tập hợp các thao tác sẽ được áp dụng tuần tự

### 00:06:41.000 - 00:06:43.000
đến đầu vào của mạng nơ-ron.

