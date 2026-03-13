# 06 chương trình-ngôn ngữ-mô hình-pal

---

Như bạn đã thấy trước đó

trong bài học này,

khả năng của LLM để thực hiện

số học và toán học khác

hoạt động còn hạn chế.

Mặc dù bạn có thể thử sử dụng chuỗi

nhắc nhở suy nghĩ

để vượt qua điều này,

nó sẽ chỉ đưa bạn đến nay.

Ngay cả khi mô hình chính xác

lý do thông qua một vấn đề,

nó vẫn có thể có được cá nhân

các phép tính toán sai,

đặc biệt với số lượng lớn hơn

hoặc các hoạt động phức tạp.

Đây là ví dụ

bạn đã thấy trước đó ở đâu

LLM cố gắng hành động như

một máy tính nhưng được

câu trả lời sai.

Hãy nhớ rằng, mô hình không phải

thực sự đang làm bất cứ điều gì

toán học thực sự ở đây.

Nó chỉ đơn giản là cố gắng dự đoán

các token có khả năng xảy ra cao nhất

hoàn thành lời nhắc.

Mô hình nhận được

toán sai có thể có

nhiều hậu quả tiêu cực

tùy thuộc vào trường hợp sử dụng của bạn,

như tính phí cho khách hàng

tổng sai

hoặc lấy số đo

cho một công thức không chính xác.

Bạn có thể khắc phục hạn chế này

bằng cách cho phép mô hình của bạn

tương tác với

ứng dụng bên ngoài

giỏi toán,

giống như một trình thông dịch Python.

Một khuôn khổ thú vị

để tăng cường LLM

theo cách này được gọi là

mô hình ngôn ngữ được chương trình hỗ trợ,

hoặc viết tắt là PAL.

Tác phẩm này lần đầu tiên được trình bày

của Luyu Gao và

cộng tác viên tại Carnegie

Đại học Mellon năm 2022,

ghép nối LLM với

một trình thông dịch mã bên ngoài

để thực hiện các phép tính.

Phương pháp đó sử dụng

chuỗi suy nghĩ nhắc nhở

để tạo ra khả năng thực thi

Các tập lệnh Python.

Những kịch bản đó

mô hình tạo ra

được chuyển đến một

trình thông dịch để thực thi.

Hình ảnh bên phải

ở đây được lấy từ

bài báo và đưa ra một số ví dụ

nhắc nhở và hoàn thiện.

Bạn sẽ đi bộ qua

một ví dụ về

những thứ này trong một giây vì vậy đừng

lo lắng về việc đọc tất cả

các chi tiết ở đây bây giờ.

Chiến lược đằng sau PAL là

để LLM tạo ra

hoàn thành ở đâu

các bước suy luận

được đi cùng

bằng mã máy tính.

Mã này sau đó được chuyển

đến một thông dịch viên để mang theo

ra các tính toán cần thiết

để giải quyết vấn đề.

Bạn chỉ định định dạng đầu ra

cho mô hình bằng cách bao gồm

ví dụ cho một hoặc một vài ngắn

suy luận trong lời nhắc.

Chúng ta hãy xem xét kỹ hơn cách

những lời nhắc ví dụ này

được cấu trúc.

Bạn sẽ tiếp tục làm việc

với câu chuyện của Roger

mua bóng tennis như

ví dụ một lần.

Việc thiết lập ở đây nên

giờ nhìn quen quen.

Đây là một chuỗi

ví dụ suy nghĩ.

Bạn có thể thấy lý do

các bước được viết ra

bằng chữ trên dòng

được đánh dấu bằng màu xanh lam.

Điều gì khác biệt so với

lời nhắc bạn đã thấy trước đây là

sự bao gồm các dòng của

Mã Python hiển thị màu hồng.

Những dòng này dịch

bất kỳ bước lý luận

liên quan đến

tính toán thành mã.

Các biến được khai báo dựa trên

văn bản ở mỗi bước suy luận.

Giá trị của chúng được gán

hoặc trực tiếp,

như trong lần đầu tiên

dòng mã ở đây,

hoặc như tính toán sử dụng

số có mặt trong

văn bản lý luận như bạn thấy

trong dòng Python thứ hai.

Mô hình này cũng có thể hoạt động với

các biến nó tạo ra

ở các bước khác,

như bạn thấy ở dòng thứ ba.

Lưu ý rằng văn bản của

từng bước suy luận

bắt đầu bằng dấu thăng,

do đó dòng

có thể được bỏ qua như

một bình luận của

Trình thông dịch Python.

Lời nhắc ở đây kết thúc bằng

vấn đề mới cần giải quyết.

Trong trường hợp này,

mục tiêu là để

xác định có bao nhiêu ổ bánh mì

bánh mì một tiệm bánh có

còn lại sau một ngày bán hàng và

sau khi ăn vài ổ bánh mì

trở về từ một

đối tác cửa hàng tạp hóa.

Ở bên phải, bạn có thể thấy

sự hoàn thành

do LLM tạo ra.

Một lần nữa, chuỗi suy nghĩ

các bước lập luận được thể hiện

màu xanh lam và Python

mã được hiển thị bằng màu hồng.

Như bạn có thể thấy,

mô hình tạo ra

một số biến để

theo dõi các ổ bánh nướng,

những ổ bánh mì được bán ở

mỗi thời điểm trong ngày,

và những ổ bánh mì quay trở lại

bởi cửa hàng tạp hóa.

Thì câu trả lời là

tính bằng cách mang

ra các phép tính số học

về các biến này.

Mô hình xác định chính xác

liệu các điều khoản có nên

được cộng hoặc trừ vào

đạt được tổng số chính xác.

Bây giờ bạn đã biết cách

ví dụ về cấu trúc

điều đó sẽ nói

LLM để viết

Các tập lệnh Python dựa trên

các bước suy luận của nó,

chúng ta hãy xem xét làm thế nào

Khung PAL cho phép

một LLM để tương tác với

một thông dịch viên bên ngoài.

Để chuẩn bị cho

suy luận với PAL,

bạn sẽ định dạng lời nhắc của mình thành

chứa một hoặc nhiều ví dụ.

Mỗi ví dụ nên chứa

một câu hỏi theo sau

các bước suy luận theo dòng

Mã Python đó

giải quyết vấn đề.

Tiếp theo, bạn sẽ nối thêm

câu hỏi mới đó

bạn muốn trả lời

mẫu nhắc nhở.

PAL kết quả của bạn

lời nhắc được định dạng ngay bây giờ

chứa cả ví dụ

và vấn đề cần giải quyết.

Tiếp theo, bạn sẽ vượt qua điều này

lời nhắc kết hợp tới LLM của bạn,

sau đó tạo ra sự hoàn thành

đó là ở dạng

một tập lệnh Python

đã học được cách

định dạng đầu ra dựa trên

ví dụ trong lời nhắc.

Bây giờ bạn có thể bàn giao kịch bản

tới trình thông dịch Python,

mà bạn sẽ sử dụng để chạy

mã và tạo ra một câu trả lời.

Đối với kịch bản ví dụ về tiệm bánh

bạn đã thấy ở slide trước,

câu trả lời là 74.

Bây giờ bạn sẽ nối thêm văn bản

chứa câu trả lời,

mà bạn biết là

chính xác bởi vì

sự tính toán

đã được thực hiện trong

Python sang định dạng PAL

nhắc bạn bắt đầu.

Đến thời điểm này bạn có

một lời nhắc bao gồm

câu trả lời đúng trong ngữ cảnh.

Bây giờ khi bạn vượt qua

đã cập nhật lời nhắc cho LLM,

nó tạo ra một sự hoàn thành

chứa câu trả lời đúng.

Với phép toán tương đối đơn giản

trong vấn đề bánh mỳ,

rất có thể là mô hình

có thể đã nhận được câu trả lời

đúng chỉ với chuỗi

của sự thúc đẩy suy nghĩ.

Nhưng đối với những phép toán phức tạp hơn,

bao gồm cả số học

với số lượng lớn,

lượng giác hoặc phép tính,

PAL là một kỹ thuật mạnh mẽ

điều đó cho phép bạn đảm bảo rằng

mọi tính toán được thực hiện bởi

ứng dụng của bạn là

chính xác và đáng tin cậy.

Bạn có thể tự hỏi làm thế nào để

tự động hóa việc này

xử lý để bạn

không cần phải truyền thông tin

qua lại giữa LLM,

và người phiên dịch bằng tay.

Đây là nơi người điều phối dàn nhạc

mà bạn đã thấy trước đó bước vào.

Người điều phối dàn nhạc được hiển thị ở đây là

hộp màu vàng là

một thành phần kỹ thuật

có thể quản lý dòng chảy

của thông tin và

sự khởi đầu của

cuộc gọi đến dữ liệu bên ngoài

nguồn hoặc ứng dụng.

Nó cũng có thể quyết định những gì

hành động cần thực hiện dựa trên

về thông tin chứa đựng

trong đầu ra của LLM.

Hãy nhớ rằng, LLM là của bạn

công cụ lý luận của ứng dụng.

Cuối cùng, nó

tạo ra kế hoạch đó

người điều phối dàn nhạc sẽ

diễn giải và thực hiện.

Trong PAL chỉ có một

hành động cần thực hiện,

việc thực thi mã Python.

LLM thực sự không có

để quyết định chạy mã,

nó chỉ cần viết

kịch bản đó

người điều phối sau đó chuyển sang

trình thông dịch bên ngoài để chạy.

Tuy nhiên, hầu hết thế giới thực

các ứng dụng có khả năng

phức tạp hơn

kiến trúc PAL đơn giản.

Trường hợp sử dụng của bạn có thể yêu cầu

tương tác với một số

nguồn dữ liệu bên ngoài.

Như bạn đã thấy trong

ví dụ mua cửa hàng,

bạn có thể cần phải quản lý

nhiều điểm quyết định,

hành động xác thực và cuộc gọi

đến các ứng dụng bên ngoài.

Làm thế nào bạn có thể sử dụng LLM để

sức mạnh phức tạp hơn

ứng dụng?

Hãy cùng khám phá một chiến lược

trong video tiếp theo.