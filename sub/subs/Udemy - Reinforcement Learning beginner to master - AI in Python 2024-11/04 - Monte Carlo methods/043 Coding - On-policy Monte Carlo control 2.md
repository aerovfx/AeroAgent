## Nội dung

### 00:00:00.000 - 00:00:07.000
Trong video này, chúng ta sẽ triển khai thuật toán đầu tiên học hỏi kinh nghiệm. chúng tôi đang nói chuyện

### 00:00:07.000 - 00:00:10.000
về thuật toán điều khiển Montecarlo theo chính sách.

### 00:00:13.000 - 00:00:20.000
Thuật toán này sẽ cho phép tác nhân đối mặt với môi trường một số lần cụ thể

### 00:00:22.000 - 00:00:24.000
tuân theo chính sách mà chúng tôi đã tạo.

### 00:00:30.000 - 00:00:37.000
Sau khi tác nhân hoàn thành nhiệm vụ, sẽ đến lúc cập nhật bảng giá trị q và ước tính mới

### 00:00:37.000 - 00:00:45.000
của mọi giá trị q mà chúng tôi phải cập nhật sẽ là mức lợi nhuận trung bình mà tác nhân đã quan sát được

### 00:00:45.000 - 00:00:49.000
sau khi thực hiện một hành động ở một trạng thái cụ thể.

### 00:00:52.000 - 00:00:58.000
Vì vậy hãy thực hiện thuật toán. Điều đầu tiên chúng ta sẽ làm là định nghĩa một hàm

### 00:01:00.000 - 00:01:02.000
được gọi là chính sách

### 00:01:03.000 - 00:01:05.000
Kiểm soát Montecarlo.

### 00:01:09.000 - 00:01:16.000
Hãy nhớ rằng chính sách phù hợp có nghĩa là chúng ta đang sử dụng cùng một chính sách để khám phá môi trường và tham gia

### 00:01:16.000 - 00:01:21.000
trong quá trình học và chúng ta sẽ chuyển làm đối số cho hàm này.

### 00:01:22.000 - 00:01:23.000
chính sách,

### 00:01:25.000 - 00:01:26.000
bảng giá trị q,

### 00:01:30.000 - 00:01:36.000
một số tập cụ thể, đó là số lần mà đặc vụ sẽ cố gắng giải quyết nhiệm vụ.

### 00:01:38.000 - 00:01:45.000
Và hệ số chiết khấu, gamma, mà chúng tôi sử dụng để chiết khấu các phần thưởng trong tương lai khi tính toán lợi nhuận

### 00:01:46.000 - 00:01:52.000
và chúng ta cũng sẽ chuyển một đối số khác gọi là epsilon mà chúng ta sẽ khởi tạo 0,2.

### 00:01:53.000 - 00:02:00.000
Và epsilon sẽ là xác suất thực hiện một hành động ngẫu nhiên để khám phá môi trường. Bên trong

### 00:02:00.000 - 00:02:01.000
chức năng

### 00:02:02.000 - 00:02:05.000
điều đầu tiên cần làm là khai báo một từ điển Python

### 00:02:05.000 - 00:02:11.000
nơi chúng tôi sẽ lưu trữ lợi nhuận sẽ nhận được cho từng cặp trạng thái và hành động cụ thể?

### 00:02:18.000 - 00:02:20.000
Tiếp theo, chúng ta vào vòng lặp chính.

### 00:02:23.000 - 00:02:30.000
Hãy viết số tập trong khoảng từ một cho đến số tập cộng một.

### 00:02:32.000 - 00:02:37.000
Vì vậy, số đếm bắt đầu từ 1 thay vì 0.

### 00:02:41.000 - 00:02:48.000
Và điều đầu tiên chúng ta sẽ làm là thiết lập lại môi trường và thu được quan sát trạng thái đầu tiên.

### 00:02:50.000 - 00:02:54.000
Trạng thái này là những gì chúng ta thu được khi gọi phương thức reset trên môi trường.

### 00:02:57.000 - 00:03:03.000
Điều tiếp theo chúng ta cần làm là khai báo một biến mà chúng ta gọi là done. Và thực hiện ý muốn

### 00:03:03.000 - 00:03:05.000
cho chúng tôi biết nhiệm vụ đã kết thúc hay chưa.

### 00:03:06.000 - 00:03:14.000
Khi hoàn tất có giá trị 'Đúng', điều đó có nghĩa là nhiệm vụ đã kết thúc và tác nhân đã tìm thấy lối ra.

### 00:03:17.000 - 00:03:24.000
Điều tiếp theo chúng ta sẽ làm là lập một danh sách với mỗi lần chuyển đổi trạng thái. Mỗi lần đại lý thực hiện

### 00:03:24.000 - 00:03:32.000
một hành động, chúng tôi sẽ giữ một thực thể trong danh sách này với trạng thái nơi hành động được thực hiện, hành động

### 00:03:32.000 - 00:03:37.000
mà chúng tôi đã nhận và phần thưởng mà chúng tôi nhận được sau khi thực hiện hành động đó.

### 00:03:38.000 - 00:03:47.000
Bây giờ, chúng tôi sẽ yêu cầu đặc vụ phải đối mặt với nhiệm vụ trong toàn bộ tập phim theo chính sách của chúng tôi.

### 00:03:47.000 - 00:03:58.000
Vì vậy, chúng ta khai báo một vòng lặp bên trong ghi, trong khi chưa hoàn thành, nghĩa là trong khi tác vụ chưa hoàn thành, và bên trong

### 00:03:58.000 - 00:04:07.000
vòng lặp đó, chúng tôi sẽ chọn một hành động bằng cách chuyển trạng thái mà tác nhân tham gia vào chính sách cũng như một giá trị

### 00:04:07.000 - 00:04:13.000
cho epsilon, để đôi khi nó sẽ thực hiện những hành động ngẫu nhiên cho phép chúng ta khám phá môi trường.

### 00:04:14.000 - 00:04:18.000
Điều tiếp theo chúng ta sẽ làm là thực thi hành động đó trong môi trường.

### 00:04:19.000 - 00:04:23.000
Hãy nhớ rằng trong phần trước chúng ta đã mô phỏng việc thực hiện các hành động.

### 00:04:24.000 - 00:04:30.000
Bây giờ, thay vì làm vậy, chúng ta sẽ yêu cầu người đại diện thực sự thực hiện các hành động và đối mặt với hậu quả.

### 00:04:31.000 - 00:04:38.000
Và sau khi thực hiện hành động đó, cái chúng ta sẽ nhận được là trạng thái tiếp theo, phần thưởng ngay lập tức mà chúng ta

### 00:04:38.000 - 00:04:45.000
nhận được sau khi thực hiện hành động đó, một giá trị mới cho biến done, giá trị này sẽ cho chúng ta biết liệu tác nhân có

### 00:04:45.000 - 00:04:52.000
có tìm thấy lối ra hay không và một từ điển Python trống với thông tin bổ sung mà chúng ta sẽ không cần trong

### 00:04:52.000 - 00:04:52.000
trường hợp này.

### 00:04:52.000 - 00:04:58.000
Và tất cả những điều này chúng ta có được bằng cách gọi phương thức step, truyền hành động mà chúng ta muốn thực hiện.

### 00:04:59.000 - 00:05:04.000
Việc tiếp theo chúng ta cần làm là lưu trữ vào danh sách chuyển tiếp và nhập

### 00:05:08.000 - 00:05:13.000
với trạng thái hiện tại của chúng ta, hành động được thực hiện và phần thưởng đạt được.

### 00:05:20.000 - 00:05:20.000
Xong.

### 00:05:22.000 - 00:05:29.000
Và điều cuối cùng, đơn giản chỉ là cập nhật biến trạng thái thành trạng thái tiếp theo sau khi thực hiện

### 00:05:29.000 - 00:05:35.000
hành động để trong lần lặp tiếp theo của vòng lặp sẽ lặp lại toàn bộ quá trình này với trạng thái mới.

### 00:05:39.000 - 00:05:45.000
Và vòng lặp này sẽ được thực hiện cho đến hết tập phim. Như bạn có thể thấy ở đây, một khi tập phim

### 00:05:45.000 - 00:05:46.000
đã kết thúc.

### 00:05:46.000 - 00:05:50.000
Những gì chúng tôi làm là khởi tạo kết quả trả về là 0.

### 00:05:51.000 - 00:05:58.000
Và thay vì tính toán lợi nhuận, mong đợi một số phần thưởng trong tương lai sẽ được chiết khấu,

### 00:05:59.000 - 00:06:01.000
chúng ta sẽ tính toán ngược lại.

### 00:06:02.000 - 00:06:06.000
Điều này sẽ cho chúng ta kết quả chính xác tương tự, nhưng nó sẽ hiệu quả hơn.

### 00:06:07.000 - 00:06:12.000
Vì vậy, bây giờ là lúc lặp lại các chuyển đổi trạng thái mà chúng tôi đã lưu trữ trong danh sách trên.

### 00:06:12.000 - 00:06:20.000
Nhưng chúng ta sẽ lặp lại từ cái cuối cùng cho đến cái đầu tiên theo thứ tự nghịch đảo. Từ trạng thái cuối cùng đã truy cập

### 00:06:21.000 - 00:06:23.000
và hành động cuối cùng được thực hiện cho đến hành động đầu tiên.

### 00:06:24.000 - 00:06:32.000
Chúng ta sẽ tạo một vòng lặp cho trạng thái tại thời điểm 't', hành động tại thời điểm 't' và phần thưởng tại thời điểm 't'

### 00:06:35.000 - 00:06:43.000
và 't' sẽ thay đổi từ thời điểm cuối cùng cho đến khi bắt đầu tập phim và ngược lại

### 00:06:43.000 - 00:06:50.000
danh sách các chuyển đổi, chúng tôi gọi hàm đảo ngược, điều này sẽ cho phép chúng tôi có quyền truy cập vào danh sách

### 00:06:50.000 - 00:06:52.000
chuyển tiếp theo thứ tự nghịch đảo.

### 00:06:55.000 - 00:06:58.000
Hãy cuộn một chút và

### 00:07:00.000 - 00:07:06.000
Bây giờ, câu hỏi mà chúng ta tự hỏi mình là, sự trở lại vào thời điểm cuối cùng là bao nhiêu?

### 00:07:07.000 - 00:07:15.000
Chà, đó sẽ là phần thưởng mà chúng tôi nhận được sau khi thực hiện hành động cuối cùng, cộng với gamma nhân với

### 00:07:15.000 - 00:07:16.000
sự trở lại đang chạy.

### 00:07:18.000 - 00:07:23.000
Đó là sự trở lại của thời gian vào giây phút cuối cùng. Bây giờ trong từ điển

### 00:07:23.000 - 00:07:24.000
nơi chúng tôi lưu trữ

### 00:07:24.000 - 00:07:26.000
Lợi nhuận mà đại lý quan sát được

### 00:07:26.000 - 00:07:31.000
chúng ta sẽ lưu trữ kết quả trả về mà chúng ta vừa tính toán.

### 00:07:32.000 - 00:07:36.000
Nếu chúng ta không có mục nào trong từ điển cho trạng thái 't' và hành động 't',

### 00:07:46.000 - 00:07:48.000
chúng ta sẽ tạo một cái mới.

### 00:07:55.000 - 00:08:01.000
Chúng tôi sẽ viết rằng chúng tôi muốn có một danh sách trống trong đó chúng tôi muốn lưu trữ kết quả trả về mà chúng tôi quan sát được cho việc này

### 00:08:01.000 - 00:08:02.000
trạng thái và hành động.

### 00:08:08.000 - 00:08:13.000
Và chúng tôi sẽ lưu trữ kết quả trả về mà chúng tôi vừa tính toán trong danh sách đó.

### 00:08:19.000 - 00:08:25.000
Như bạn có thể thấy, chúng tôi sử dụng cặp trạng thái và hành động làm chỉ mục để định vị danh sách phù hợp bên trong từ điển.

### 00:08:28.000 - 00:08:31.000
Và đó là nơi ít nhất chúng ta sẽ lưu trữ kết quả trả về 'G'.

### 00:08:38.000 - 00:08:46.000
Sau đó, chúng ta sẽ tra cứu trong bảng giá trị q hành động 't' và trạng thái 't' và chúng ta sẽ tìm

### 00:08:46.000 - 00:08:49.000
cập nhật ước tính giá trị q của trạng thái đó đang hoạt động.

### 00:08:54.000 - 00:09:00.000
Ước tính mới sẽ là mức lợi nhuận trung bình mà chúng tôi quan sát được đối với cặp đó, tức là

### 00:09:00.000 - 00:09:03.000
lý do tại sao chúng tôi giữ từ điển.

### 00:09:14.000 - 00:09:20.000
Như bạn có thể thấy, ước tính mới của giá trị q sẽ là mức lợi nhuận trung bình mà chúng tôi đã quan sát được

### 00:09:21.000 - 00:09:22.000
đối với trạng thái và hành động đó.

### 00:09:27.000 - 00:09:31.000
Và thế là xong, chúng ta có thuật toán của mình.

### 00:09:34.000 - 00:09:42.000
Bây giờ chúng ta sẽ kiểm tra nó bằng cách gọi hàm kiểm soát Montecarlo theo chính sách và chuyển chính sách,

### 00:09:43.000 - 00:09:48.000
bảng giá trị q và chúng tôi sẽ cung cấp cho nó 10000 tập.

### 00:09:58.000 - 00:10:05.000
Hãy chạy ô này ở đây mà trước đây chúng ta chưa thực thi và bây giờ chúng ta đã sẵn sàng thực thi thuật toán.

### 00:10:13.000 - 00:10:16.000
Sẵn sàng. trong video tiếp theo chúng ta sẽ thấy kết quả.

### 00:10:17.000 - 00:10:18.000
Tôi sẽ gặp bạn ở đó.

