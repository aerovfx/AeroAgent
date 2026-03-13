## Nội dung

### 00:00:00.000 - 00:00:07.400
Bây giờ, trong bài giảng trước, chúng ta đã tạo mã cho một tập ngẫu nhiên với trò chuyện GPT và

### 00:00:07.400 - 00:00:13.439
trước khi tiếp tục, hãy cố gắng hiểu từng dòng ở đây, từng dòng mã hóa

### 00:00:13.439 - 00:00:19.480
 và chúng ta sẽ bắt đầu ở đây bằng việc tạo môi trường.

### 00:00:19.480 - 00:00:26.440
Vì vậy, trước tiên, chúng ta nhập nasium và sau đó tạo môi trường cho thử thách xe leo núi

### 00:00:26.440 - 00:00:36.439
 và ở đây chúng ta chọn chế độ kết xuất con người và đặt các bước tối đa của tập là 200

### 00:00:36.439 - 00:00:44.840
và ở đây chúng ta đã khởi tạo môi trường rồi lưu một ít các biến quan trọng như tổng số

### 00:00:44.840 - 00:00:53.200
các bước thưởng được thực hiện và cắt bớt và các giá trị ban đầu là 0 0 sai và sai và sau đó chúng ta

### 00:00:53.200 - 00:01:00.760
phải đặt lại trạng thái của môi trường hay nói một cách đơn giản là chúng ta thực sự đặt lại điểm xuất phát

### 00:01:00.760 - 00:01:10.600
 của ô tô và hãy thực hiện việc này ở đây và chúng ta có thể trích xuất trạng thái ở đây sao cho trong một mảng Numpy

### 00:01:10.600 - 00:01:20.480
 vì vậy giá trị đầu tiên thực sự là vị trí của ô tô dọc theo trục x nên từ âm 1,2

### 00:01:20.480 - 00:01:29.960
đó là giá trị tối thiểu đến cộng 0,6 đó là giá trị tối đa và giá trị thứ hai là 0 là vận tốc

### 00:01:29.960 - 00:01:41.159
 của ô tô nên từ âm 0,07 đến cộng 0,07 và thực tế có một khía cạnh ngẫu nhiên trong phương thức đặt lại 

### 00:01:41.159 - 00:01:50.000
 nên bất cứ khi nào chúng ta đặt lại môi trường nhiều lần nên vận tốc vẫn bằng 0 nhưng vị trí bắt đầu trên trục x thay đổi một chút nên bất cứ khi nào chúng ta bắt đầu một tập mới, điểm bắt đầu

### 00:01:50.000 - 00:01:58.920
 luôn khác nhau nên đây là thiết lập trạng thái ban đầu của môi trường của chúng ta và sau đó

### 00:01:58.920 - 00:02:13.120
chúng ta thực hiện hành động và hành động có nghĩa là 0 và tăng tốc sang trái một không tăng tốc và hai tăng tốc sang

### 00:02:13.120 - 00:02:22.120
 bên phải nên cái này là bên trái và cái này ở đây bên phải và chúng ta có thể thực hiện một hành động ngẫu nhiên để 0 1 hoặc 2 với

### 00:02:22.120 - 00:02:31.480
phương thức mẫu nên bây giờ chúng ta có 0 ở bên trái không tăng tốc sang phải không có gì ở bên phải

### 00:02:31.479 - 00:02:44.120
, v.v. vì vậy chúng ta lưu lại hành động và sau đó chúng ta chuyển hành động đó sang phương thức bước và điều này đánh giá trạng thái

### 00:02:44.120 - 00:02:54.639
tiếp theo tùy thuộc vào hiện tại trạng thái và hành động để chúng ta chuyển sang trạng thái tiếp theo về vị trí

### 00:02:54.639 - 00:03:02.839
 của chiếc xe và vận tốc cũng như phần thưởng và miễn là chiếc xe không lên đến đỉnh

### 00:03:02.839 - 00:03:10.439
đỉnh núi thì phần thưởng là âm 1 và nếu không thì là 0 thì ở đây chúng ta có tham số done 

### 00:03:10.439 - 00:03:18.879
 cho biết liệu chúng ta đã đạt được mục tiêu hay không nên thường được thực hiện là sai và sau đó chúng ta đã

### 00:03:18.879 - 00:03:25.799
cắt ngắn và điều này kiểm tra xem chúng ta đã đạt đến tập tối đa bước 200 cuối cùng hay chưa nhưng ít nhất chúng ta có

### 00:03:25.799 - 00:03:34.799
thông tin không liên quan ở đây vì vậy hãy kiểm tra ví dụ của chúng tôi ở đây, chúng tôi bắt đầu ở âm 0,466 và vận tốc

### 00:03:34.799 - 00:03:44.719
 bằng 0 và sau đó chúng tôi thực hiện một hành động ngẫu nhiên có nghĩa là tăng tốc sang phải và do đó chúng tôi

### 00:03:44.719 - 00:03:53.840
có vận tốc dương và chúng tôi hơi di chuyển sang phải nên đây là giá trị ít âm hơn nên chúng tôi

### 00:03:53.840 - 00:04:02.919
bắt đầu ở đây lái xe sang phải nhưng vẫn chỉ với hành động này là chúng tôi chưa đạt được mục tiêu và

### 00:04:02.919 - 00:04:11.319
do đó phần thưởng là âm 1 và cũng thực hiện là sai và bị cắt ngắn cũng sai nên đây là cách nó

### 00:04:11.319 - 00:04:19.399
hoạt động và sau đó chúng tôi cập nhật tổng phần thưởng cũng như số bước hiện là âm 1 và 1 và cả

### 00:04:19.399 - 00:04:27.719
chúng tôi cập nhật trạng thái là trạng thái tiếp theo và cuối cùng, chúng tôi nên đóng môi trường

### 00:04:27.719 - 00:04:36.759
bây giờ chúng tôi đã tạo các bước biến riêng biệt và chúng tôi đã đếm số bước ở đây theo cách thủ công

### 00:04:36.759 - 00:04:49.399
vì vậy bằng cách tăng dần các bước nhưng cũng có tùy chọn thứ hai để chúng tôi có thể truy cập các bước trôi qua với

### 00:04:49.399 - 00:04:58.920
gạch dưới các bước trôi qua và trong ví dụ này là 1 và do đó chúng tôi có thể sửa đổi và tối ưu hóa một chút

### 00:04:59.240 - 00:05:08.759
ở đây mã của chúng tôi nên hãy sao chép dòng mã hóa này ở đây và chúng tôi có thể gạch bỏ các bước ở đây và còn cái này

### 00:05:08.759 - 00:05:23.800
và ở đây thực sự đủ để đánh giá các bước đã trôi qua trước khi chúng tôi in ra nên đây

### 00:05:24.439 - 00:05:33.560
có thể là mã được tối ưu hóa và bây giờ chúng ta hãy chạy mã ở đây một lần nữa để cho một tập ngẫu nhiên

### 00:05:33.560 - 00:05:42.759
hãy kiểm tra bằng đồ họa ở đây để chúng ta có 200 bước 200 hành động và trạng thái này thay đổi nhưng tôi nghĩ

### 00:05:43.480 - 00:05:56.279
chúng ta sẽ không đạt được mục tiêu như trường hợp này và thực tế là bản in ra ở đây sai nên số lượng

### 00:05:56.279 - 00:06:03.159
bước đã thắng vì chúng ta ở đây chưa điều chỉnh bản in ra nên bây giờ phải có num bước nên hãy thử đi thử lại

### 00:06:03.159 - 00:06:12.279
chúng ta có 200 hành động ngẫu nhiên và sau 200 bước chúng ta đã không đạt được mục tiêu

### 00:06:12.279 - 00:06:25.559
với tổng số từ là âm 200 nên đây thực sự là điều cơ bản nên đây thực sự là

### 00:06:25.559 - 00:06:35.639
những điều cơ bản về môi trường phòng tập thể dục của AI mở nên nó hoạt động khá giống nhau đối với mọi môi trường

### 00:06:35.639 - 00:06:44.680
và nó thực sự khá quan trọng mà ít nhất bạn hiểu ở đây những điều cơ bản nhất nên line for line

### 00:06:45.719 - 00:06:52.599
 và chúng ta cũng có ở đây phương thức ngẫu nhiên ở đây trong trường hợp của chúng ta không quan trọng như chúng ta đã có

### 00:06:53.159 - 00:06:59.319
đã xác định chế độ ngẫu nhiên cho con người nhưng sau này chúng ta sẽ thấy rằng phương pháp ngẫu nhiên cũng có liên quan ở đây

### 00:06:59.319 - 00:07:07.159
nhưng ở đây đối với trường hợp đơn giản này nên một tập ngẫu nhiên đối với kết xuất của con người, chúng ta cũng có thể gạch bỏ nó

### 00:07:07.159 - 00:07:13.560
vì vậy đây là những điều cơ bản và chúng ta sẽ tiếp tục trong bài giảng tiếp theo, cảm ơn vì đã xem và hẹn gặp lại bạn ở đó

### 00:07:14.439 - 00:07:19.879
tạm biệt

### 00:07:19.879 - 00:07:26.039
bye

