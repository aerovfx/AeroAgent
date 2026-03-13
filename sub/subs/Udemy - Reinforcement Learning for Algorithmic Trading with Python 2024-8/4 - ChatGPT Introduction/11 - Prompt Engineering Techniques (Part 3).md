## Nội dung

### 00:00:00.000 - 00:00:05.940
Được rồi, đây là bài giảng thứ ba và cũng là bài giảng cuối cùng về kỹ thuật nhắc nhở và ở đây chúng ta sẽ

### 00:00:05.940 - 00:00:11.960
đề cập đến các khía cạnh quan trọng như đối tượng mục tiêu, giọng điệu, mức độ chi tiết và hình thức phản hồi

### 00:00:11.960 - 00:00:17.500
. Vì vậy, về cơ bản, chúng tôi có thể hỏi cùng một câu hỏi theo những cách hoàn toàn khác nhau

### 00:00:17.500 - 00:00:23.620
 và nhận được những câu trả lời hoàn toàn khác nhau về mức độ chi tiết,

### 00:00:23.620 - 00:00:31.140
phạm vi, giọng điệu và hình thức và điều này chúng tôi có thể điều chỉnh câu trả lời cho phù hợp với một

### 00:00:31.140 - 00:00:36.260
đối tượng mục tiêu cụ thể. Vì vậy, điều này nghe có vẻ phức tạp nhưng hãy lấy một ví dụ ở đây và

### 00:00:36.260 - 00:00:42.299
hãy bắt đầu với lời nhắc sau. Vì vậy, thông thường, sự khác biệt giữa học có giám sát và học không có giám sát đối với những người mới bắt đầu học về khoa học dữ liệu và máy

### 00:00:42.299 - 00:00:48.780
 không dễ hiểu và chúng ta có thể hỏi ở đây

### 00:00:48.780 - 00:00:55.420
các câu hỏi sau đây để giải thích ngắn gọn sự khác biệt giữa học có giám sát

### 00:00:55.420 - 00:01:00.660
 và học không giám sát cho những người không có kiến ​​thức về khoa học dữ liệu và

### 00:01:00.660 - 00:01:06.180
học máy. Hãy cho một ví dụ minh họa. Vậy hãy xem chúng ta nhận được gì

### 00:01:06.180 - 00:01:13.299
ở đây. Vì vậy, học có giám sát và học không giám sát là hai khái niệm cơ bản trong lĩnh vực học máy

### 00:01:13.299 - 00:01:24.620
 và hãy bắt đầu từ đây với học có giám sát. Vì vậy, trong quá trình học có giám sát

### 00:01:24.620 - 00:01:30.140
, thuật toán được huấn luyện trên tập dữ liệu nhãn và điều này có nghĩa là mỗi

### 00:01:30.140 - 00:01:36.579
ví dụ trong tập dữ liệu được ghép nối với câu trả lời hoặc nhãn đúng. Vì vậy, ví dụ trong

### 00:01:36.579 - 00:01:42.420
bộ dữ liệu Titanic, chúng ta biết liệu hành khách là thú cưng có phải không nên đây là nhãn

### 00:01:42.420 - 00:01:48.099
sống sót hay không sống sót. Vì vậy, mục tiêu của học có giám sát là học cách ánh xạ

### 00:01:48.099 - 00:01:53.659
 từ các biến đầu vào đến các biến đầu ra dựa trên dữ liệu nhãn và nhiệm vụ nhận xét

### 00:01:53.659 - 00:01:58.620
 và học có giám sát bao gồm phân loại để dự đoán

### 00:01:58.620 - 00:02:04.340
 các danh mục như sống sót không tồn tại và hồi quy để dự đoán các giá trị

### 00:02:04.340 - 00:02:10.980
 liên tục và thực sự quay lại bài giảng cuối cùng về sàng lọc lặp lại nên

### 00:02:10.979 - 00:02:17.539
nếu bạn không thực sự hiểu sự khác biệt giữa phân loại và

### 00:02:17.539 - 00:02:21.620
hồi quy, bạn có thể hỏi thêm ở đây để làm rõ hơn vì vậy đây là cách nó

### 00:02:21.620 - 00:02:27.219
hoạt động nhưng bây giờ Hãy quay lại phần học có giám sát và chúng ta có một ví dụ

### 00:02:27.219 - 00:02:32.139
ở đây, giả sử bạn có một tập dữ liệu gồm các email trong đó mỗi email được gắn nhãn là

### 00:02:32.139 - 00:02:37.259
thư rác hoặc không phải thư rác để chúng tôi biết email đó là thư rác hay không phải thư rác thì trong

### 00:02:37.259 - 00:02:43.579
học có giám sát, thuật toán học từ dữ liệu nhãn này để phân loại các email mới

### 00:02:43.579 - 00:02:50.340
 là thư rác hoặc không phải thư rác nên đây là học có giám sát và ngược lại

### 00:02:50.340 - 00:02:56.219
chúng ta học không giám sát nên ở đây thuật toán được đưa ra

### 00:02:56.219 - 00:03:01.379
tập dữ liệu không được gắn nhãn và do đó, thuật toán phải tự tìm cấu trúc hoặc mẫu

### 00:03:01.379 - 00:03:07.019
 bên trong nó và không có câu trả lời hoặc nhãn chính xác được xác định trước

### 00:03:07.020 - 00:03:12.900
 và học tập không giám sát và điều này thường được sử dụng cho các nhiệm vụ như phân cụm để

### 00:03:12.900 - 00:03:18.980
nhóm các điểm dữ liệu tương tự lại với nhau và giảm kích thước và

### 00:03:18.980 - 00:03:25.379
 làm ví dụ. Vì vậy, hãy xem xét tập dữ liệu chứa thông tin về khách hàng của

### 00:03:25.379 - 00:03:29.420
một nhà bán lẻ trực tuyến như lịch sử theo đuổi của họ và hơn thế nữa và trong

### 00:03:29.420 - 00:03:35.340
học tập không giám sát, thuật toán có thể xác định các nhóm khách hàng ai

### 00:03:35.340 - 00:03:40.740
 thể hiện các hành vi rượt đuổi tương tự mà không được thông báo trước những nhóm

### 00:03:40.740 - 00:03:46.140
 đó có thể là gì nên đây tóm lại là sự khác biệt giữa học có giám sát

### 00:03:46.140 - 00:03:51.620
và học không có giám sát. một số học có giám sát tóm tắt liên quan đến

### 00:03:51.620 - 00:03:55.780
học từ dữ liệu nhãn với các câu trả lời đúng được xác định trước trong khi không có giám sát

### 00:03:55.780 - 00:04:01.500
học liên quan đến việc tìm kiếm các mẫu hoặc cấu trúc và dữ liệu không được gắn nhãn nên đây là

### 00:04:01.500 - 00:04:09.460
câu trả lời cho những người mới bắt đầu hoàn toàn rất đơn giản và không quá kỹ thuật và bây giờ

### 00:04:09.460 - 00:04:16.259
hãy tiếp tục với một đối tượng mục tiêu hoàn toàn khác để trải nghiệm dữ liệu

### 00:04:16.259 - 00:04:21.980
các nhà khoa học và chúng ta hãy chuyển đổi định dạng để ở đây chúng ta có các dấu đầu dòng và chúng ta

### 00:04:21.980 - 00:04:30.220
Ví dụ: có thể chuyển sang định dạng bảng và hãy thử ở đây theo lời nhắc

### 00:04:30.220 - 00:04:35.820
sau đây để giải thích chi tiết sự khác biệt giữa học có giám sát và

### 00:04:35.820 - 00:04:40.980
học không giám sát để trải nghiệm các nhà khoa học dữ liệu và so sánh cả hai trong một

### 00:04:40.980 - 00:04:47.140
định dạng bảng nêu bật những điểm tương đồng và khác biệt nên về cơ bản đây là

### 00:04:47.140 - 00:04:53.260
cùng một câu hỏi. học có giám sát

### 00:04:53.260 - 00:04:57.060
học có giám sát và học không giám sát theo định dạng bảng nên ở đây chúng ta có nhiều

### 00:04:57.060 - 00:05:03.139
các khía cạnh khác nhau như dữ liệu huấn luyện và như chúng ta đã học trước đây nên ở đây chúng ta có

### 00:05:03.139 - 00:05:12.540
nhãn dữ liệu và học không giám sát, dữ liệu không được gắn nhãn và mục tiêu học

### 00:05:12.540 - 00:05:17.019
ở đây là tìm hiểu cách ánh xạ từ các biến đầu vào đến các biến đầu ra và một

### 00:05:17.019 - 00:05:22.259
học không giám sát để tìm các mẫu hoặc cấu trúc ẩn trong dữ liệu và ở đây

### 00:05:22.259 - 00:05:28.980
các loại nhiệm vụ thường trong học có giám sát mà chúng ta có thể phân biệt

### 00:05:28.980 - 00:05:34.219
 phân loại để dự đoán các danh mục hoặc lớp và hồi quy

### 00:05:34.219 - 00:05:40.420
dự đoán các giá trị liên tục và trong học tập không giám sát, chúng tôi có ví dụ

### 00:05:40.420 - 00:05:44.620
phân cụm để nhóm các điểm dữ liệu tương tự lại với nhau hoặc giảm kích thước

### 00:05:44.620 - 00:05:50.259
 và sau đó chúng tôi có các đánh giá hiệu suất ở đây, vậy làm cách nào chúng tôi có thể đánh giá

### 00:05:50.259 - 00:05:56.139
hiệu suất của một mô hình và điều này thường được thực hiện chẳng hạn với độ chính xác

### 00:05:56.139 - 00:06:02.019
độ chính xác và điểm f1 để phân loại hoặc sai số bình phương trung bình cho một hồi quy

### 00:06:02.019 - 00:06:07.300
dự án và so với dự án đó đối với việc học không giám sát, nó chủ quan hơn và

### 00:06:07.300 - 00:06:13.819
ví dụ: ở đây chúng tôi có các số liệu như điểm bóng và hơn thế nữa và

### 00:06:13.819 - 00:06:20.579
thực sự đối với việc học có giám sát, chúng tôi cần dữ liệu nhãn và Ngược lại với

### 00:06:20.579 - 00:06:25.939
dữ liệu không được gắn nhãn đó chỉ phù hợp cho việc học không giám sát và sau đó chúng tôi có ở đây các

### 00:06:25.939 - 00:06:32.180
ví dụ để phát hiện email hoặc phân khúc khách hàng thì chúng tôi có

### 00:06:32.180 - 00:06:39.860
sự phức tạp của các trường hợp sử dụng thuật toán và các thuật toán ví dụ như cây quyết định

### 00:06:39.860 - 00:06:44.860
hỗ trợ mạng lưới thần kinh vectơ so với phân cụm k-means hoặc PCA nên đây là một

### 00:06:44.860 - 00:06:52.120
so sánh hay dành cho những người đã biết khá nhiều về học máy

### 00:06:52.120 - 00:06:58.420
và học có giám sát và học không giám sát nên tóm lại là trong khi cả

### 00:06:58.420 - 00:07:06.020
học có giám sát và không giám sát đều là các nhánh cơ bản của học máy

### 00:07:06.019 - 00:07:13.459
chúng khác nhau và các phản hồi ở đây từ trò chuyện GPT cũng khác nhau ngay cả khi

### 00:07:13.459 - 00:07:18.859
câu hỏi thực sự giống nhau nhưng nó được điều chỉnh cho phù hợp với đối tượng mục tiêu

### 00:07:18.859 - 00:07:22.939
và với điều này, chúng tôi đã đề cập đến các kỹ thuật nhắc nhở quan trọng nhất mà chúng tôi

### 00:07:22.939 - 00:07:29.779
cũng sẽ sử dụng trong các bài giảng và phần tiếp theo, vì vậy đây là những điều cơ bản và

### 00:07:29.779 - 00:07:36.859
chúng tôi sẽ áp dụng những điều cơ bản và kỹ thuật này trong khóa học sắp tới, cảm ơn vì

### 00:07:36.859 - 00:07:42.539
đã xem và rất mong được gặp bạn ở đó, tạm biệt

### 00:07:42.539 - 00:07:48.979
will use also in the next lectures and sections so these were the basics and

### 00:07:48.979 - 00:07:57.339
we will apply these basics and techniques in the upcoming course thanks for

### 00:07:57.339 - 00:08:02.139
watching and looking forward to seeing you there bye

