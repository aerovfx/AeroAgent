# 04 ứng dụng tương tác với bên ngoài

---

Trong phần trước,

bạn đã thấy LLM có thể tương tác như thế nào

với các bộ dữ liệu bên ngoài.

Bây giờ chúng ta hãy lấy một

hãy xem họ có thể làm thế nào

tương tác với bên ngoài

ứng dụng.

Để động viên các loại

các vấn đề và trường hợp sử dụng

yêu cầu loại này

tăng cường LLM,

bạn sẽ gặp lại khách hàng

ví dụ về bot dịch vụ

bạn đã thấy trước đó trong khóa học.

Trong lần hướng dẫn này của

một khách hàng

tương tác với ShopBot,

bạn sẽ nhìn vào

tích hợp mà

bạn cần phải cho phép

ứng dụng xử lý việc trả lại hàng

yêu cầu từ đầu đến cuối.

Trong cuộc trò chuyện này,

khách hàng có

bày tỏ rằng họ

muốn quay lại

một số gen mà họ đã mua.

ShopBot trả lời bằng cách hỏi

cho số thứ tự,

mà khách hàng

sau đó cung cấp.

ShopBot sau đó tra cứu

số thứ tự trong

cơ sở dữ liệu giao dịch.

Một cách nó có thể làm

đây là bằng cách sử dụng

một sự thực hiện giẻ rách

thuộc loại bạn

đã thấy trước đó trong

video trước đó.

Trong trường hợp này ở đây,

bạn có thể sẽ lấy

dữ liệu thông qua truy vấn SQL để

một đơn đặt hàng phụ trợ

cơ sở dữ liệu chứ không phải là

lấy dữ liệu từ một

tập tài liệu.

Khi ShopBot đã lấy được

khách hàng đặt hàng,

bước tiếp theo là

xác nhận các mục đó

sẽ được trả lại.

Bot hỏi

khách hàng nếu họ muốn

trả lại bất cứ thứ gì

khác với gen.

Sau khi người dùng

nêu câu trả lời của họ,

bot bắt đầu một yêu cầu để

vận chuyển của công ty

đối tác cho một nhãn trả lại.

Cơ thể sử dụng các chủ hàng

API Python để yêu cầu

nhãn ShopBot sắp hoạt động

gửi email vận chuyển

dán nhãn cho khách hàng.

Nó cũng yêu cầu họ xác nhận

địa chỉ email của họ.

Khách hàng phản hồi bằng

địa chỉ email của họ và bot

bao gồm thông tin này trong

lệnh gọi API tới người gửi hàng.

Sau khi yêu cầu API

đã hoàn thành,

Bartlett là

khách hàng biết điều đó

nhãn đã được

gửi qua email,

và cuộc trò chuyện

đi đến hồi kết.

Ví dụ ngắn này minh họa

chỉ một bộ có thể

tương tác mà bạn có thể cần

một LLM có khả năng

để cung cấp năng lượng và ứng dụng.

Nói chung, việc kết nối LLM với

ứng dụng bên ngoài

cho phép mô hình

để tương tác với

thế giới rộng lớn hơn,

mở rộng tiện ích của họ

ngoài nhiệm vụ ngôn ngữ.

Như cửa hàng đã mua

ví dụ cho thấy,

LLM có thể được sử dụng

để kích hoạt hành động

khi được trao khả năng

để tương tác với các API.

LLM cũng có thể kết nối với

tài nguyên lập trình khác.

Ví dụ, một

Trình thông dịch Python

có thể cho phép các mô hình

kết hợp chính xác

tính toán vào kết quả đầu ra của họ.

Điều quan trọng là phải

lưu ý rằng lời nhắc và

sự hoàn thành đang ở mức rất cao

trọng tâm của các quy trình công việc này.

Các hành động mà ứng dụng

sẽ đáp lại

yêu cầu của người dùng sẽ được

được xác định bởi LLM,

đóng vai trò là

công cụ lý luận của ứng dụng.

Để kích hoạt các hành động,

sự hoàn thành được tạo ra bởi

LLM phải chứa một số

thông tin quan trọng.

Đầu tiên, mô hình cần phải

có thể tạo ra một bộ

hướng dẫn sao cho

ứng dụng

biết phải thực hiện những hành động nào.

Những hướng dẫn này cần phải được

dễ hiểu và tương ứng

đến những hành động được phép

Trong ShopBot

ví dụ chẳng hạn,

các bước quan trọng là;

kiểm tra ID đơn hàng,

yêu cầu nhãn vận chuyển,

xác minh email người dùng,

và gửi nhãn cho người dùng qua email.

Thứ hai, việc hoàn thiện

cần phải được định dạng trong

một cách mà rộng hơn

ứng dụng có thể hiểu được.

Điều này có thể đơn giản như

một câu cụ thể

cấu trúc hoặc như

phức tạp như viết một kịch bản trong

Python hoặc tạo

một lệnh SQL.

Ví dụ, đây là một

Truy vấn SQL sẽ

xác định liệu một đơn đặt hàng có

có trong cơ sở dữ liệu

của tất cả các đơn đặt hàng.

Cuối cùng, mô hình

có thể cần phải thu thập

thông tin cho phép

nó để xác nhận một hành động.

Ví dụ, trong

cuộc trò chuyện của ShopBot,

ứng dụng cần thiết

để xác minh email

địa chỉ khách hàng đã sử dụng

để thực hiện đơn hàng ban đầu.

Bất kỳ thông tin nào

là cần thiết cho

xác nhận cần phải

được lấy từ

người dùng và chứa trong

sự hoàn thành để nó có thể được

được chuyển qua

ứng dụng.

Cấu trúc lời nhắc

theo cách đúng là

quan trọng đối với tất cả

những nhiệm vụ này và có thể thực hiện

một sự khác biệt rất lớn trong

chất lượng của một kế hoạch được tạo ra

hoặc tuân thủ một mong muốn

đặc điểm kỹ thuật định dạng đầu ra