## Nội dung

### 00:00:00.000 - 00:00:07.000
Bây giờ, trước khi chúng ta tiếp tục chạy hàng trăm, thậm chí hàng nghìn tập mà không có sự kết xuất của con người.

### 00:00:07.000 - 00:00:19.000
Trước hết, chúng ta nên đảm bảo rằng chúng ta đo lường hiệu suất hoặc đánh giá hiệu suất và tỷ lệ thành công của các tập.

### 00:00:19.000 - 00:00:28.000
Vì vậy, sau này khi chúng ta muốn đào tạo một tác nhân và chạy hàng trăm hoặc thậm chí hàng nghìn tập, chúng ta cần đo hiệu suất

### 00:00:28.000 - 00:00:40.000
và trước hết, hãy làm rõ rằng chúng ta đã chọn biến thể mà chúng ta có khởi tạo bên ngoài vòng lặp mùa thu.

### 00:00:40.000 - 00:00:55.000
Vì vậy, chúng ta có thể bắt đầu lại ở đây với dấu nhắc sau. Tôi quyết định tiếp tục với đoạn mã sau chỉ để đảm bảo chúng ta ở trên cùng một trang.

### 00:00:55.000 - 00:00:59.000
Và sau đó chúng ta có thể sử dụng lời nhắc sau.

### 00:00:59.000 - 00:01:10.000
Vì vậy, bây giờ hãy tập trung vào việc đo lường và đánh giá hiệu suất. Tôi muốn đo lường hiệu suất hoặc sự thành công của tác nhân ngẫu nhiên và in hiệu suất khi kết thúc quá trình chạy ngẫu nhiên.

### 00:01:10.000 - 00:01:16.000
Vui lòng đưa ra đề xuất phù hợp với các số liệu khác nhau.

### 00:01:16.000 - 00:01:21.000
Vì vậy, hãy sao chép và dán vào đây theo lời nhắc của chúng tôi.

### 00:01:21.000 - 00:01:26.000
Và hãy xem chúng ta nhận được gì.

### 00:01:26.000 - 00:01:34.000
Vì vậy, để đo lường hiệu suất và sự thành công của tác nhân ngẫu nhiên, chúng ta có thể xem xét các số liệu sau, tổng phần thưởng trung bình.

### 00:01:34.000 - 00:01:47.000
Vậy tổng phần thưởng trung bình thu được qua tất cả các tập. Vì vậy, điều này chắc chắn có ý nghĩa. Sau đó là số bước trung bình cần thực hiện để hoàn thành mỗi tập.

### 00:01:47.000 - 00:01:59.000
Vì vậy, con số này sẽ rất giống với tổng phần thưởng. Sau đó là tỷ lệ thành công, tỷ lệ phần trăm của các tập mà tác nhân đạt được mục tiêu thành công.

### 00:01:59.000 - 00:02:06.000
Vì vậy, trong môi trường ô tô leo núi, thành công có thể được định nghĩa là đạt được lá cờ trên đỉnh núi.

### 00:02:06.000 - 00:02:20.000
Vì vậy, đây là mã và số liệu hiệu suất ban đầu như tổng phần thưởng, danh sách số bước và số lần thành công.

### 00:02:20.000 - 00:02:28.000
Vì vậy, chúng tôi thêm tổng phần thưởng của mỗi tập vào danh sách và chúng tôi cũng làm như vậy với số bước.

### 00:02:28.000 - 00:02:45.000
Và sau đó chúng tôi kiểm tra xem thành công hay đạt được cờ ở trên cùng. Vì vậy, nếu trạng thái ở vị trí một, tức là tham số x lớn hơn hoặc bằng vị trí mục tiêu, chúng ta sẽ tăng số lần thành công lên một.

### 00:02:45.000 - 00:02:57.000
Và cách khác, chúng ta cũng có thể kiểm tra xem tham số done có đúng hay không. Vì vậy, đây có thể là giải pháp thay thế thứ hai và chúng tôi có thể yêu cầu cuộc trò chuyện của bạn là T cho nó.

### 00:02:57.000 - 00:03:04.000
Và cuối cùng, chúng tôi tính toán số liệu hiệu suất và in số liệu hiệu suất.

### 00:03:05.000 - 00:03:23.000
Vì vậy, điều này nghe giống như một kế hoạch, hãy sao chép nó, hãy dán và thử. Vậy là chỉ với năm tập ngẫu nhiên và ở đây chúng ta có thể thấy cửa sổ trò chơi hình bánh. Vậy là chúng ta đã có tập đầu tiên.

### 00:03:23.000 - 00:03:38.000
Có vẻ như tập này không thành công. Sau đó chúng ta có cái thứ hai. Vậy hãy đợi cho đến khi chúng ta đạt được năm tập ngẫu nhiên.

### 00:03:38.000 - 00:03:53.000
Vậy là bây giờ chúng ta có bốn tập không thành công và hãy đợi tập cuối cùng. Vì vậy, đối với tập thứ năm và đây cũng không phải là một thành công.

### 00:03:54.000 - 00:04:09.000
Và sau đó chúng ta hãy chờ đợi các chỉ số hiệu suất. Vì vậy, tổng phần thưởng trung bình là âm 200 và số bước trung bình là cộng 200 và tỷ lệ thành công là 0. Vậy là 0 phần trăm.

### 00:04:10.000 - 00:04:24.000
Vì vậy, chúng ta có tỷ lệ thành công là 0 phần trăm, nhưng cũng có thể hợp lý nếu thêm vào đây số tập thành công và tổng số tập ở đây trong ngoặc hoặc bất cứ thứ gì.

### 00:04:24.000 - 00:04:33.000
Vì vậy, hãy tinh chỉnh ở đây hiệu suất được in ra một chút và chúng ta có thể sử dụng lời nhắc sau ở đây.

### 00:04:33.000 - 00:04:51.000
Vì vậy, có vẻ như tổng phần thưởng trung bình và số bước là giống nhau. Vui lòng xóa các bước và cũng vui lòng thêm số tập thành công và tổng số tập vào tỷ lệ thành công, ví dụ: trong ngoặc đơn.

### 00:04:51.000 - 00:05:01.000
Vì vậy, hãy gửi lời nhắc ở đây và hãy tinh chỉnh thêm mã của chúng tôi ở đây.

### 00:05:01.000 - 00:05:18.000
Vì vậy, ở đây chúng tôi có mã cập nhật và bạn xóa số liệu các bước cũng như cập nhật lại tỷ lệ thành công để bao gồm số tập thành công và tổng số tập.

### 00:05:18.000 - 00:05:23.000
Vì vậy, điều này sẽ cung cấp đánh giá rõ ràng.

### 00:05:23.000 - 00:05:31.000
Vì vậy, hãy chỉ sao chép và dán một cái nữa thời gian.

### 00:05:31.000 - 00:05:35.000
Và hãy chạy nó một cách đơn giản.

### 00:05:35.000 - 00:05:43.000
Vì vậy, một lần nữa chúng ta sẽ bắt đầu ở đây với tập một. Vậy chúng ta hãy chờ năm tập.

### 00:05:43.000 - 00:05:53.000
Vậy bây giờ chúng ta hãy chờ tập cuối cùng.

### 00:05:53.000 - 00:06:06.000
Và đây chúng ta có bản in cuối cùng. Vì vậy, tổng phần thưởng trung bình là âm 200 và tỷ lệ thành công là 0. Vậy là không có tập nào trong số năm tập thành công.

### 00:06:06.000 - 00:06:13.000
Vậy là chúng ta đã đạt được mục tiêu. Vì vậy, một số số liệu hiệu suất như tổng phần thưởng trung bình và tỷ lệ thành công.

### 00:06:13.000 - 00:06:22.000
Và cũng ở đây, chúng tôi có thể tinh chỉnh thêm mã và kết quả đầu ra tùy theo sở thích cá nhân của mình.

### 00:06:22.000 - 00:06:26.000
Và chúng tôi có thể tiếp tục ở đây với lời nhắc sau.

### 00:06:26.000 - 00:06:33.000
Vì vậy, chẳng hạn, sẽ hợp lý nếu thêm vào đây cho mỗi phần không bao giờ in ra liệu tập có thành công tiếp theo hay không.

### 00:06:33.000 - 00:06:41.000
Vì vậy, chúng tôi cũng có thể thấy điều này ở đây trong tổng phần thưởng. Tuy nhiên, điều đó thậm chí còn rõ ràng hơn.

### 00:06:41.000 - 00:06:47.000
Vì vậy, chúng ta có thể sử dụng phần thêm vui lòng thêm vào mỗi tập để in ra xem tập đó có thành công hay không.

### 00:06:47.000 - 00:06:57.000
Và cũng để xác định mức độ thành công và tỷ lệ thành công, chúng ta cũng có thể sử dụng tham số done thay vì sử dụng ở đây.

### 00:06:57.000 - 00:07:05.000
Loại mã vị trí mục tiêu cuối cùng. Vì vậy, có vẻ như chúng ta cũng có thể sử dụng ở đây done.

### 00:07:05.000 - 00:07:09.000
Vì vậy, nếu bạn đạt done bằng true thì chúng ta đã thành công.

### 00:07:09.000 - 00:07:16.000
Và đây có thể là lựa chọn tốt hơn. Vì vậy, nó có thể là một vấn đề về hương vị. Nhưng chúng ta hãy hỏi ở đây.

### 00:07:16.000 - 00:07:26.000
Vậy chắc chắn chúng ta có thể sử dụng tham số done. Và hãy xem ở đây mã được cập nhật.

### 00:07:26.000 - 00:07:33.000
Vì vậy, nếu done là đúng, nó chỉ ra rằng tập đã kết thúc do đã đạt được mục tiêu hoặc đã hết bước.

### 00:07:33.000 - 00:07:39.000
Vì vậy, điều đó không hoàn toàn đúng vì hiện tại chúng ta có các tham số bị cắt ngắn.

### 00:07:39.000 - 00:07:45.000
Vì vậy, nếu done là đúng, nó cho biết rằng tập đã kết thúc bằng cách đạt được mục tiêu hoặc do hết số bước.

### 00:07:45.000 - 00:07:49.000
Vì vậy, điều này không hoàn toàn đúng trong phiên bản gần đây nhất.

### 00:07:49.000 - 00:08:00.000
Vì vậy, trước đây điều này là đúng, nhưng bây giờ với việc giới thiệu tham số bị cắt ngắn, điều này không hoàn toàn đúng.

### 00:08:00.000 - 00:08:05.000
Nhưng chúng tôi có thể xác định xem tập phim có thành công hay không bằng đoạn mã sau.

### 00:08:05.000 - 00:08:09.000
Vì vậy, nếu thực hiện là đúng và không bị cắt bớt.

### 00:08:09.000 - 00:08:18.000
Vì vậy, điều này có hiệu quả trong mọi trường hợp ngoại trừ trường hợp chúng tôi thành công ở bước cuối cùng.

### 00:08:18.000 - 00:08:23.000
Sau đó, chúng tôi sẽ gặp sự cố với bạn. Vì vậy, chúng ta cũng có thể thảo luận thêm về vấn đề này tại đây.

### 00:08:23.000 - 00:08:29.000
Vì vậy, nếu thành công thì chúng ta sẽ tăng số lần thành công này lên một.

### 00:08:29.000 - 00:08:33.000
Nhưng bây giờ, hãy làm rõ điểm này một cách đơn giản.

### 00:08:33.000 - 00:08:42.000
Vậy còn nếu bạn đạt được mục tiêu ở bước cuối cùng có thể là 200 thì đây không phải là thành công theo mã của bạn?

### 00:08:42.000 - 00:08:47.000
Bạn nói đúng nếu tác nhân đạt được mục tiêu ở bước cuối cùng có thể.

### 00:08:47.000 - 00:08:51.000
Xong sẽ đúng, nhưng bị cắt bớt cũng sẽ đúng.

### 00:08:51.000 - 00:08:58.000
Vì vậy, đây là một ví dụ điển hình ở đây cần có sự giám sát và can thiệp của con người.

### 00:08:58.000 - 00:09:01.000
Vì vậy, chatgpt không hoàn hảo.

### 00:09:01.000 - 00:09:08.000
Và để xử lý trường hợp này, chúng ta cần điều chỉnh logic để xem xét vị trí của đặc vụ ở cuối tập.

### 00:09:08.000 - 00:09:10.000
Vì vậy, hãy kiểm tra điều này ở đây.

### 00:09:10.000 - 00:09:14.000
Và có vẻ như chatgpt quay trở lại giải pháp trước đó.

### 00:09:14.000 - 00:09:23.000
Vì vậy, vị trí mục tiêu, không sao, nhưng chúng ta cũng có thể chỉ tập trung vào tham số done.

### 00:09:23.000 - 00:09:30.000
Vì vậy, nếu thực hiện đúng, thì đây sẽ là một thành công.

### 00:09:30.000 - 00:09:34.000
Nhưng hãy để nguyên như vậy. đây.

### 00:09:34.000 - 00:09:41.000
Vì vậy, hãy sao chép lại mã cuối cùng.

### 00:09:41.000 - 00:09:48.000
Và hãy chạy thêm một lần nữa.

### 00:09:48.000 - 00:09:53.000
Với năm tập.

### 00:09:53.000 - 00:10:00.000
Và bây giờ chúng tôi đã thêm vào đây dù nó có thành công hay không. Vậy là bạn đã biết.

### 00:10:00.000 - 00:10:04.000
Và bây giờ, ở đây chúng tôi cũng có năm tập không thành công.

### 00:10:04.000 - 00:10:10.000
Vì vậy, tổng phần thưởng trung bình là âm 200 và tỷ lệ thành công là 0%.

### 00:10:10.000 - 00:10:17.000
Vì vậy, chúng tôi đã xây dựng những kiến ​​thức cơ bản để phân tích sâu hơn và đào tạo đại lý của mình.

### 00:10:17.000 - 00:10:24.000
Vì vậy, bây giờ trong bước tiếp theo, chúng ta thực sự nên điều hành đại lý và đào tạo đại lý không chỉ năm lần,

### 00:10:24.000 - 00:10:27.000
nhưng hàng trăm thậm chí hàng nghìn lần.

### 00:10:27.000 - 00:10:30.000
Và để làm được điều này, chúng ta cần tăng tốc quá trình.

### 00:10:30.000 - 00:10:34.000
Vì vậy, chúng ta không cần chế độ kết xuất của con người nữa.

### 00:10:34.000 - 00:10:37.000
Vì vậy, bây giờ chúng ta đã hiểu môi trường hoạt động như thế nào.

### 00:10:37.000 - 00:10:45.000
Vì vậy, nó chỉ là việc lên đến đỉnh núi với xếp hạng hầm từ trái sang phải và không làm gì cả.

### 00:10:45.000 - 00:10:48.000
Và chúng ta sẽ tiếp tục ở đây trong các bài giảng tiếp theo.

### 00:10:48.000 - 00:10:51.000
Cảm ơn bạn đã theo dõi và hẹn gặp lại bạn ở đó. Tạm biệt.

