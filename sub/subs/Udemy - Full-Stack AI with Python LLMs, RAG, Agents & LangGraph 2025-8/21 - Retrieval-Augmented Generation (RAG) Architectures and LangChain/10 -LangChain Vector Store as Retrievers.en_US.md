# 10 -LangChain Vector Store dưới dạng Retrievers.en US

---

Được rồi, trong trường hợp đặc biệt này

phần, đặc biệt là phần này

thực sự là giảng bài, chúng ta cần phải làm vậy.

Điều chúng ta cần làm là chúng ta cần

để nói rằng, này, chúng ta cần tạo ra

nhúng vector cho các khối này.

Vì vậy, những gì tôi sẽ làm

để nói, tôi sẽ tìm kiếm

cho một cái gì đó được gọi là

Nhúng LangChain OpenAI.

Được rồi.

Và đi vào.

Vì vậy, OpenAI Embeddings là một gói.

Vậy làm thế nào để thiết lập nó?

Nó rất đơn giản.

Vì vậy, nếu chúng ta cuộn xuống, chúng ta

cần cài đặt pip.

Cài đặt pip LangChain mở AI.

Vậy đây là gói

mà chúng ta cần cài đặt.

Vì vậy, bạn có thể thấy nhanh chóng chúng tôi

đã thực hiện cài đặt.

Nó rất nhanh chóng.

Bây giờ những gì tôi có thể làm, tôi chỉ có thể

nói thế đi, này, từ, được rồi, từ

Nhập khẩu LangChain OpenAI.

Được rồi, tôi muốn nhập

Tích hợp OpenAI.

Vậy điều tôi sắp làm là

Tôi sẽ tạo ra

một mô hình nhúng ở đây.

Vì vậy tôi sẽ chỉ nói nhúng dấu gạch dưới

mô hình tương đương với các phần nhúng OpenAI.

Và ở đây chúng ta cần đưa ra mô hình.

Bạn muốn sử dụng mẫu nào

để thực hiện nhúng?

Được rồi, vậy là bạn có một vài mô hình.

Chúng ta sẽ sử dụng văn bản

nhúng, ba lớn.

Đây là mô hình nhúng của bạn.

Bây giờ hãy xem chúng ta có thể làm gì.

Về mặt kỹ thuật tôi có

mô hình nhúng đã sẵn sàng, phải không?

Nếu bạn có thể thấy, tôi có

mô hình nhúng đã sẵn sàng.

Bây giờ mô hình nhúng này cần

để tạo phần nhúng cho đoạn này

và lưu trữ nó trong db góc phần tư.

Góc phần tư DB là gì

về cơ bản db vector của tôi.

Vì vậy, chúng tôi có

một cái gì đó được gọi là một cây cầu

Được rồi, vậy chúng ta hãy tìm kiếm

cho LangChain,

cơ sở dữ liệu chúng tôi đang sử dụng.

Chúng tôi đang sử dụng vạc db.

Vì vậy, góc phần tư DB và tìm kiếm.

Vì vậy, bạn có thể thấy LangChain thực sự

có hỗ trợ cho db góc phần tư.

Được rồi, vậy chúng ta cần cài đặt pip,

cài đặt góc phần tư LangChain.

Vậy chúng ta hãy quay trở lại

và thứ này ở đâu?

Vâng, tôi chỉ có thể nói pip,

cài đặt góc phần tư LangChain

và chỉ cần nhấn enter.

Vậy chúng ta hãy chờ một lát nhé.

Cài đặt của bạn thành công.

Vì vậy bây giờ những gì chúng ta có thể làm, chúng ta có thể

chỉ cần tạo một cửa hàng vector.

Vì vậy, cửa hàng vector bằng một cái gì đó.

Được rồi, tôi chỉ đang đặt

một cái gì đó ở đây.

Vì vậy, về cơ bản đây là

một kho vector góc phần tư.

Vì vậy tôi sẽ chỉ nói từ

góc phần tư gạch dưới chuỗi lang

nhập cửa hàng vector góc phần tư.

Thế nên tôi sẽ chỉ nói rằng, này, cái này

là một kho lưu trữ vector góc phần tư.

Điều đó thực sự tuyệt vời.

Và điều tôi sắp nói là

đó, này, vector góc phần tư

lưu trữ dấu chấm từ tài liệu.

Được rồi, từ tài liệu.

Vì vậy, trước tiên bạn cần phải vượt qua

của tất cả, tất cả các tài liệu.

Vì vậy, đây là những khối đó.

Này, đây là những khối

mà tôi muốn lưu trữ.

Được rồi, bây giờ bạn có

để cho, nhúng.

Được rồi, vectơ nào

nhúng bạn muốn sử dụng?

Tôi muốn sử dụng điều này làm mô hình của tôi.

Điều đó cũng tuyệt vời.

Bạn phải cung cấp một URL.

Được rồi, bạn cần cung cấp URL

của vectơ góc phần tư DB của bạn.

Vì vậy, URL về cơ bản là HTTP

Dấu hai chấm HTTP, dấu gạch chéo, dấu gạch chéo.

Nó đang chạy trên localhost phải không?

Cơ sở dữ liệu của bạn đang chạy

trên máy chủ cục bộ 6333.

Vậy hãy để tôi mở localhost,

6333, bảng điều khiển.

Bạn thực sự có được giao diện người dùng góc phần tư này.

Nếu tôi vào đây vào bảng điều khiển, xin lỗi,

vào bộ sưu tập nhé bạn

có thể thấy chúng tôi không có bộ sưu tập.

Được rồi.

Vì vậy, về cơ bản nó đang chạy

trên localhost Colon6333.

Đây là nơi cơ sở dữ liệu của tôi đang chạy.

Và bạn cần phải cho

một tên bộ sưu tập.

Vì vậy, tên bộ sưu tập là

về cơ bản là sự phân chia hợp lý.

Vì vậy, tên bộ sưu tập.

Tôi chỉ có thể nói rằng chúng tôi

đang học, rag.

Vì thế tôi chỉ có thể nói là học rag.

Thế thôi.

Và bây giờ chúng ta chỉ có thể nói in.

Được rồi, tôi chỉ có thể nói là in.

Lập chỉ mục các tài liệu, được thực hiện.

Đó là nó.

Vì vậy, hãy xem những gì chúng tôi đã làm,

nó rất đơn giản phải không?

Hãy xem chúng tôi đã làm được gì?

Bạn đọc, bạn lấy một đường dẫn PDF,

bạn tải bản PDF,

bạn chia nó thành nhiều phần

và bạn nhúng vector nó.

Về cơ bản bạn thực hiện nhúng vector

ra khỏi nó và bạn lưu trữ nó

vào cơ sở dữ liệu vectơ.

Đó là nó.

Đó là tất cả.

Xem này, nếu tôi quay lại sơ đồ của mình,

bạn lấy tài liệu, chia nó ra

vào các khối, tạo các phần nhúng

và lưu trữ nó vào cơ sở dữ liệu.

Đó là nó.

Vì vậy bây giờ nếu tôi chạy cái này

mã, thực ra là bạn

sẽ gặp lỗi.

Nhưng hãy để tôi chạy

mã này cho bạn.

Được rồi?

Vì vậy, nếu tôi chạy cái này cụ thể

mã, chỉ cần xem lỗi.

Được rồi, chuyện gì xảy ra?

Vì vậy, bạn có thể thấy nó đang chạy

và chúng tôi đã gặp lỗi.

Lỗi là ở chỗ tôi

không cung cấp khóa API của tôi.

Khóa API OpenAI của tôi chưa được đặt.

Vì vậy, những gì tôi sẽ làm

việc cần làm trước tiên là hãy để tôi chỉ

tạo một tập tin env và tôi cần

để cung cấp env này, khóa API này.

Vậy hãy để tôi nhanh chóng

tạo khóa API bằng cách đi

tới platform.OpenAI.com

và chỉ cho tôi một chút thôi.

Ừ, vậy là tôi có chìa khóa rồi,

Tôi đã dán chìa khóa của mình.

Và chúng tôi cũng cần

để đọc phím này, phải không?

Vậy làm thế nào chúng ta có thể đọc nó?

Vì vậy tôi sẽ chỉ nói từ dấu chấm ENV

phong bì tải nhập khẩu.

Và trước khi chạy vấn đề,

hãy tải chương trình của chúng tôi.

Hãy tải env.

Bây giờ hãy xem điều gì xảy ra nếu tôi,

bạn biết đấy, hãy để tôi xóa cái này

thiết bị đầu cuối và tạo một thiết bị đầu cuối mới.

Chỉ một giây thôi.

Tạo một thiết bị đầu cuối mới

và chạy chương trình này.

Hãy xem điều gì sẽ xảy ra.

Vì vậy bạn có thể thấy nó là, nó

đang làm điều gì đó đúng đắn

Nó đang hoạt động và nó

đang mất một thời gian.

Hãy để tôi quay lại

tới góc phần tư, cái này, cửa hàng, được chứ?

Và hãy để tôi làm mới nhanh chóng.

Ồ, và bạn có thể thấy chúng tôi đã học được

rag như một bộ sưu tập ở đây.

Và có bao nhiêu phân đoạn?

Có bảy phân đoạn, phải không?

192 điểm.

Và nếu tôi nhấp vào, bạn có thể thấy bạn

thực sự có nhúng vector.

Vì vậy, hãy xem, đây là một đoạn.

Bạn biết đấy, đây là một số

thêm thông tin về nó.

Và đây là những vectơ.

Và tôi không muốn sao chép

cái này, đừng sao chép cái này vì

máy tính xách tay sẽ bắt đầu tụt hậu.

Bạn có thể thấy chúng tôi có một số

nhúng vector.

Được rồi?

Và việc nhúng vector chẳng là gì cả.

Đây chỉ là những con số.

Vì vậy, việc nhúng vector là

đã xong và bạn đã thành công

đã lập chỉ mục của bạn.

Vì vậy, hãy xem, mỗi trang đều

bây giờ thành một đoạn.

Vector nhúng ở đây.

Và đây là nội dung trang

mà chúng ta sắp vượt qua.

Và đây là một số siêu dữ liệu.

Siêu dữ liệu về cơ bản có nghĩa là tác giả

ở đó, bạn biết đấy, người sáng tạo ở đó.

Thế là bạn đã có nguồn

nó được đọc từ đâu, thấy không?

Sau đó tổng số trang.

Và đây là từ số trang

ba, nhãn trang bốn.

Vì vậy tất cả siêu dữ liệu và mọi thứ

được lưu trữ trong db góc phần tư của chúng tôi.

Vậy thì xin chúc mừng các bạn, bạn đã có

đã xây dựng thành công của bạn

đường dẫn lập chỉ mục cho Rack.

Từ bài giảng tiếp theo trở đi,

hãy xem chúng ta có thể làm như thế nào

phần truy xuất trong Rack.