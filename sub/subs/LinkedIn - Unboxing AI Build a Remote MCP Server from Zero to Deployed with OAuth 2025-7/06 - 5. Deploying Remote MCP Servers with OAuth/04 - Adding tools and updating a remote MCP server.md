# 04 - Thêm công cụ và cập nhật máy chủ MCP từ xa

---

- Bây giờ tôi có thể đi và cập nhật máy chủ MCP của mình

và triển khai lại lên Cloudflare cũng như bất kỳ thay đổi nào tôi thực hiện

cũng tự động hiển thị cho người dùng.

Hãy để tôi chỉ cho bạn.

Máy chủ này nằm trong thư mục, máy chủ MCP của tôi.

Đây là một dự án TypeScript,

và bên trong dự án TypeScript

có một thư mục, nguồn, có tệp index.ts,

và đó là nơi mọi thứ đang diễn ra.

Vì vậy nếu tôi nhìn vào đây,

bạn sẽ nhận thấy, mặc dù đó là TypeScript,

cấu trúc giống nhau

như Python mà chúng ta đã xem xét cho đến nay.

Chúng tôi có công cụ máy chủ này

và sau đó chúng ta có mô tả về công cụ này,

đây là những gì AI nhìn thấy.

Sau đó, chúng tôi có chức năng công cụ thực tế,

trong trường hợp này, chỉ cần cộng các số lại với nhau.

Chúng tôi có một cái khác, công cụ máy chủ tính toán,

và chức năng bên dưới đó.

Vậy điều đó có nghĩa là tôi có thể thêm một công cụ mới

chỉ bằng cách sử dụng GitHub Copilot.

Vì vậy, tôi sẽ mở Copilot và nói, index.ts là ngữ cảnh của tôi.

"Thêm một công cụ mới vào máy chủ MCP này

gọi là Ngôn ngữ, Trò chơi chữ.

Khi công cụ này được kích hoạt,

nó tạo ra ba chữ cái ngẫu nhiên.

Tất cả đều phải khác nhau.

Sau đó nó sẽ hướng dẫn người dùng

để nghĩ ra càng nhiều từ càng tốt

có chứa ba chữ cái này trong bất kỳ sự kết hợp nào.

Tuân theo cấu trúc hiện có của máy chủ MCP."

Vì vậy, tôi sẽ chạy nó và bây giờ Copilot

xem xét mã hiện có, khớp với các mẫu,

và xây dựng chức năng mới.

Và bởi vì chúng tôi đang làm việc trên máy chủ MCP ở đây

và nó thực sự chỉ là TypeScript đơn giản,

sự khác biệt duy nhất giữa thiết lập này

và bất cứ thứ gì khác mà bạn xây dựng

có phải người trang trí nhỏ ở trên cùng nói rằng

rằng đây là công cụ

Vì vậy Copilot sẽ làm tốt công việc này

mà không cần tôi thực sự nhập bất kỳ thông tin bổ sung nào.

Khi xong, tôi sẽ bấm giữ.

Tôi có thể đi kiểm tra mã ở đây

nhưng chức năng này thực sự đơn giản,

không cần phải làm bất cứ điều gì cầu kỳ.

Khi việc này hoàn tất, tôi có thể mở lại thiết bị đầu cuối của mình.

Tôi cũng giống như trước đây nên tôi chỉ nói, để xem...

Sau đó tôi có thể triển khai lại nên tôi sẽ chỉ nói npm run triển khai.

Trước tiên tôi chỉ cần chắc chắn rằng mình đang ở trong thư mục đó,

vậy hãy cd máy chủ MCP của tôi, sau đó npm chạy triển khai.

Điều này triển khai phiên bản mới của máy chủ.

Và khi quá trình triển khai kết thúc,

khi tôi quay lại và kết nối lại với máy chủ

sau đó xóa và liệt kê các công cụ,

bạn sẽ thấy có một công cụ mới ở đây tên là Word Game.

Tôi có thể chạy nó, chúng tôi nhận được kết quả Word Game.

Và đó là vấn đề.

Sử dụng máy chủ MCP từ xa,

Bây giờ tôi có thể cập nhật máy chủ MCP đó bất cứ lúc nào tôi muốn.

Và bất kỳ tính năng nào tôi thêm hoặc sửa đổi

tự động hiển thị cho người dùng cuối,

nếu họ đang trỏ vào máy chủ MCP từ xa đó.

Họ không phải quản lý phiên bản.

Nó giống như việc truy cập vào một trang web,

ngoại trừ trang web là máy chủ MCP.