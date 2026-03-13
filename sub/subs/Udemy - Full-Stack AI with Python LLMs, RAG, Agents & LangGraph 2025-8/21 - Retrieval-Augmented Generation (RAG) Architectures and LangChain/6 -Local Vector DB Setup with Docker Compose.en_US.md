# 6 -Thiết lập DB Vector cục bộ với Docker Compose.en US

---

Được rồi các bạn, vậy nên trong trường hợp đặc biệt này

video, hãy chuyển sang phần mã hóa

và hãy viết mã cho hệ thống RAG đầu tiên của chúng ta.

Bây giờ như chúng ta đã

đã thảo luận rằng trong RAG chúng tôi

có hai giai đoạn, phải không?

Chúng tôi có một giai đoạn lập chỉ mục

và chúng tôi có một giai đoạn phục hồi.

Vì vậy, trước tiên tôi muốn phục vụ

giai đoạn lập chỉ mục.

Chúng tôi sẽ viết mã lập chỉ mục

giai đoạn, đường dẫn lập chỉ mục này.

Và quan trọng nhất ở chỗ đó

video, chúng ta cần thiết lập,

cơ sở hạ tầng đầu tiên.

Bây giờ như bạn có thể thấy, như một phần

về cơ sở hạ tầng, chúng tôi chỉ

cần thiết lập cơ sở dữ liệu

đó là cơ sở dữ liệu vector.

Hiện nay trên thị trường có rất nhiều

của cơ sở dữ liệu vector.

Ví dụ: nếu tôi tìm kiếm,

ví dụ: có Pinecone db.

Vì vậy, Pinecone DB không phải là nguồn mở.

Đó là một máy chủ tự lưu trữ, nó

một dịch vụ được quản lý trên máy chủ.

Vì vậy, bạn có thể thấy Quả thông,

cơ sở dữ liệu vectơ

Sau đó, bạn có một cái gì đó giống như VV8.

Vì vậy, hãy để tôi tìm kiếm VV8, VV8DB.

Được rồi, vậy là VV8DB.

Vì vậy, đây là VVADB.

Đây thực sự là nguồn mở.

Thế thì bạn cũng có điều gì đó đã biết

vì Chroma DB cũng là một trong số đó.

Vậy là Chroma DB đã có mặt.

Sau đó, bạn thậm chí còn có vector PG.

Tất cả những điều này là gì?

Tất cả đều là cơ sở dữ liệu vector của bạn.

Vậy là bạn có vector PG này

và sau đó bạn có một cái gì đó

được gọi là Quadrant db.

Vậy qdrand, đó là db Góc phần tư này.

Vì thế có rất nhiều và rất nhiều

cơ sở dữ liệu vector có sẵn

trên thị trường và tất cả họ

làm việc gần như giống nhau.

Bây giờ sự khác biệt duy nhất là, đối với

ví dụ, đây không phải là nguồn mở,

đây là những nguồn mở.

cái yêu thích của tôi là

thực ra là Cauldron DB.

Tại sao?

Bởi vì số một, nó rất dễ dàng

để thiết lập QuadrantDB

và nó rất nhẹ, nó

rất nhanh, rất nhẹ.

Vì vậy cá nhân tôi thích

QuadrantDB rất nhiều.

Vì vậy trong loạt bài hướng dẫn cụ thể này

chúng ta sẽ sử dụng QuadrantDB.

Nhưng tất cả kiến thức đều có thể chuyển giao được

bởi vì cuối cùng

trong ngày đây chỉ là cơ sở dữ liệu.

Vì vậy, hãy thiết lập

lên Cauldron DB cục bộ.

Bây giờ để thiết lập

Số QuadrantDB, một cách là khi

bạn bấm vào đây để bắt đầu

nút, bạn thực sự có thể tải xuống

và bạn biết đấy, hãy thiết lập QuadrantDB

tất cả trên đám mây.

Bạn có thể thấy rằng có

một phiên bản đám mây là tốt.

Nhưng cá nhân tôi thích nó được thiết lập hơn

cục bộ bằng cách sử dụng Docker.

Được rồi, điều đó có nghĩa là thiết lập

lên nó tại địa phương bạn cần

để có Docker và bạn cần

có kiến thức về Docker.

Hãy xem, nếu bạn là một nhà phát triển,

không thành vấn đề nếu bạn là một

nhà phát triển phụ trợ, bạn là một

nhà phát triển giao diện người dùng, bạn là một

Docker nhà phát triển ngăn xếp đầy đủ là

thứ gì đó phải có trong

trạng thái ngày nay.

Được rồi, vậy bạn cần có docker

được cài đặt trên máy của bạn

và bạn cần thiết lập docker.

Vì vậy docker rất quan trọng.

Được rồi, đây là docker.

Vì vậy, bạn phải có docker

đã cài đặt và bạn phải có

docker đang chạy trên máy của bạn.

Vậy là tôi đã cài đặt docker rồi

và tôi vừa chọn, Docker.

Vì vậy bạn có thể thấy rằng

động cơ docker đang khởi động.

Điều đó thực sự tuyệt vời.

Tôi có một vài hình ảnh.

Bạn hoàn toàn có thể bỏ qua chúng.

Được rồi, bây giờ chúng ta hãy quay lại

đến góc phần tư.

Và bây giờ điều chúng ta sắp làm là chúng ta

sẽ thiết lập góc phần tư.

Vì vậy, đây là cơ sở mã của chúng tôi.

Vậy hãy để tôi tạo ra

rag, gạch dưới, chỉ mục.

Được rồi, tôi sẽ chỉ nói là giẻ rách.

Được rồi, thật rách rưới.

Và đây là điều tôi sắp làm

Tôi sẽ tạo một tập tin

đó là docker soạn yml.

Vì vậy, đây là tập tin

bạn phải tạo ra.

Bây giờ trong tập tin soạn thảo docker này,

chúng tôi sẽ chỉ nói dịch vụ.

Được rồi, trong các buổi lễ, tôi

chỉ cần một dịch vụ

đó là cơ sở dữ liệu vector.

Bên trong cơ sở dữ liệu vectơ,

chúng ta nên sử dụng hình ảnh nào?

Chúng ta nên sử dụng Quadrant.

Góc phần tư.

Và chúng ta cần hiển thị một số cổng.

Vì vậy, thực sự góc phần tư

hoạt động trên Cổng 6333.

Đúng.

Vì vậy, bạn có thể thấy rằng tôi đang chạy.

Đây là dịch vụ duy nhất của tôi.

Vì vậy bây giờ hãy mở terminal của bạn.

Bạn có thể thấy rằng tôi

bên trong thiết bị đầu cuối của tôi.

Hãy để CD vào thư mục giẻ rách.

Và bây giờ điều tôi sắp làm là

chỉ cần nói Docker soạn.

Được rồi, Docker soạn, lên và nhập.

Vậy điều bạn sắp chú ý là

rằng bây giờ nó đang kéo vector

DB đó là hình ảnh góc phần tư này.

Và bây giờ sẽ mất một ít

thời gian vì đây là lần đầu tiên

thời gian chúng tôi đang kéo.

Và góc phần tư DB của tôi đã hoạt động.

Thấy chưa, góc phần tư DB của tôi

đang hoạt động.

Vấn đề là nếu tôi làm

điều khiển C, nó thực sự dừng lại

cơ sở dữ liệu đặc biệt này.

Vì vậy, tôi không muốn dừng cơ sở dữ liệu của mình.

Vì vậy tôi chỉ có thể nói gạch nối D, mà

về cơ bản có nghĩa là chế độ tách rời.

Bây giờ nó đang chạy ở chế độ nền.

Vì vậy, bạn có thể thấy của tôi

thiết bị đầu cuối được giải phóng.

Và nếu tôi đi đến đây để trở về với tôi

Docker, bạn có thể thấy miếng giẻ đó

và cơ sở dữ liệu vector đang chạy

và những cổng nào được tiếp xúc?

6333.

Vì vậy, trong một thời gian, ý tôi là nó có thể

thiết lập nó ở chế độ nền.

Vì vậy, sau một thời gian bạn sẽ thấy

Cổng 6333 đó sẽ bị lộ,

lên và có sẵn.

Được rồi, vậy hãy đợi nhé

trong một thời gian ngắn.

Bạn có thể thấy nó là 24 giây,

và nếu tôi chỉ cần nhấp vào đây.

Được rồi.

Vì vậy, bạn có thể xem tất cả các bản ghi.

Bạn có thể thấy nó đang làm

một cái gì đó trong nội bộ.

Không sao đâu.

Nó đang chạy và chạy.

Điều đó thật tuyệt.

Vì vậy, trong video cụ thể tiếp theo,

hãy bắt đầu bằng cách thực sự

cài đặt tất cả các phụ thuộc

và mã hóa giai đoạn lập chỉ mục.