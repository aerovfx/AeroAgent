# 04 - Ví dụ thực tế về MCP trong Claude

---

- Cách dễ nhất để hiểu điều này

là để xem một ví dụ.

Đây là Claude.

Ở Claude, tôi đã cài đặt hai máy chủ MCP mới.

Cái được gọi là thời tiết do tôi tự tạo ra,

có ba công cụ.

get_current_weather, get_forecast,

và get_hourly_analysis,

và một thứ được gọi là màu sắc,

mà tôi phát hiện ra rằng người khác đã xây dựng

cho phép Claude tương tác với màu sắc.

Đèn trong phòng tôi.

Hãy để tôi chỉ cho bạn cách nó hoạt động.

Ở Claude, tôi sẽ chỉ nói,

"Thời tiết ở Burnaby hiện giờ thế nào?"

Bây giờ, khi tôi gửi yêu cầu này,

thay vì Claude thực hiện tìm kiếm trên web thông tin này

hoặc chỉ ảo giác một số thông tin về thời tiết

hoặc cho tôi số liệu thống kê chung về thời tiết,

nó sẽ nói, "Này, có sẵn một số máy chủ MCP

cho tôi ở đây, vì vậy tôi sẽ sử dụng nó."

Thấy chưa, ở đây ghi get_current_weather, yêu cầu tên Burnaby.

Đây là Claude đang quan sát việc tôi đưa ra yêu cầu về thời tiết,

rằng nó có sẵn các công cụ để nói lên điều gì đó

về việc nhận thông tin về thời tiết.

Và sau đó, nó yêu cầu sự cho phép của tôi,

người dùng sử dụng công cụ này.

Và tôi với tư cách là người dùng bây giờ có thể xem những gì đang xảy ra ở đây.

Vì vậy, nó nói rằng Claude muốn sử dụng công cụ này.

Hàm nó muốn được gọi là get_current_weather,

và thông tin đang được truyền vào

là Burnaby, British Columbia, Canada.

Bây giờ tôi có thể xem lại thông tin này. Đó là tất cả những gì tôi có thể thấy.

Và sau đó tôi sẽ chỉ nói Cho phép luôn hoặc Cho phép một lần.

Vì vậy, Cho phép luôn có nghĩa là đối với phần còn lại của cuộc trò chuyện cụ thể này,

nó sẽ chỉ cho phép nó chạy.

Nếu tôi nói Cho phép một lần, nó sẽ chỉ cho phép

cho trường hợp cụ thể này của cuộc trò chuyện.

Và nếu tôi nói Từ chối,

nó sẽ không thể sử dụng dịch vụ

và nó sẽ rơi trở lại vào thứ khác.

Vì vậy, tôi sẽ nói Cho phép một lần.

Hệ thống lúc này sẽ gửi thông tin cần thiết

tới máy chủ MCP.

Máy chủ MCP trong trường hợp này sẽ chuyển đến Open-Meteo

là API thời tiết nguồn mở,

và lấy ra một loạt thông tin.

Và sau đó, khi thông tin đó được trả về,

máy chủ tóm tắt thông tin cho tôi.

Vì vậy, ở đây bạn có thể thấy phản hồi tôi nhận được.

Có rất nhiều thông tin thời tiết được gói gọn trong đó.

Và thông tin thời tiết này

không phải là tất cả mọi thứ được trả về từ API.

Đó là những gì máy chủ MCP xác định là có liên quan

được chuyển sang API.

Vì vậy, khi tôi xây dựng máy chủ MCP này,

Tôi đã suy nghĩ cẩn thận về những thông tin nào

tôi có thấy hữu ích cho những loại câu hỏi tôi sẽ hỏi không

ở Claude về thời tiết?

Và sau đó, tôi chỉ đưa những thông tin đó vào

trong phản hồi từ dịch vụ thời tiết.

Vì vậy, thay vì xây dựng kết nối API

nơi tôi vừa gửi yêu cầu tới API

và tất cả dữ liệu thời tiết đều quay trở lại,

đó chỉ là một lượng lớn dữ liệu, tôi nói,

"Gửi yêu cầu, tìm hiểu địa điểm và thời gian,

và sau đó chỉ lấy lại được những thông tin này."

Đó là những gì tôi nhận lại được. Thật gọn gàng phải không?

Nào, hãy xem thứ gì đó

thực tế hơn một chút trong thế giới thực.

Bạn sẽ nhận thấy phía sau tôi có ánh sáng màu xanh lam, phải không?

Ánh sáng xanh phía sau màn hình đây.

Đó là bóng đèn màu.

Vì vậy, tôi có thể vào đây vì tôi có công cụ tạo màu này.

Tôi sẽ nói, "Đèn nào hiện đang bật?"

Đó là một câu hỏi kỳ lạ để hỏi, phải không?

Nhưng vì tôi đã cài đặt màu sắc

và một trong những công cụ bên trong mô tả rằng,

rằng nó có thể tìm thấy ánh sáng.

Nó nói: "Này, bạn có muốn sử dụng đèn get-light không?"

Tôi nói Cho phép một lần.

Bây giờ nó sẽ cho tôi danh sách tất cả các đèn có sẵn.

Vì vậy, hãy xem ở đây.

Chúng tôi có phòng ăn, văn phòng của Morten, phòng ngủ.

Và hãy xem, điểm màu sắc 1.

Tôi nghĩ là cái này, đèn bàn màu.

Vì vậy, tôi sẽ gõ vào đây,

"đổi đèn bàn sang màu đỏ."

Vậy bạn có thấy bây giờ nó có màu xanh không? Vâng.

Tôi sẽ chạy lệnh này.

Và nếu mọi thứ hoạt động tốt,

nó sẽ nói,

"Bạn có muốn thay đổi màu đèn bàn từ,

bật nó lên và đặt nó thành màu đỏ?"

Vâng, tôi sẽ cho phép một lần.

Tada!

Bạn có thấy tại sao điều này lại quan trọng bây giờ không?

Làm cách nào bây giờ tôi có thể kiểm soát thế giới bằng bot trò chuyện AI của mình?

Và bắt đầu nghĩ xem điều gì có thể xảy ra khi điều này có thể thực hiện được?

Và sau đó nhận ra rằng MCP là một giao thức

có thể được kết nối với bất cứ điều gì.

Có nghĩa là bạn có thể làm tất cả những điều kỳ lạ với nó.

Vì vậy, đây là cách nó hoạt động.

Khách hàng MCP của tôi, trong trường hợp này là Claude,

kết nối với máy chủ MCP.

Máy chủ MCP chứa bên trong nó các công cụ và tài nguyên,

và có thể là những gợi ý, gợi ý và những thứ khác.

Và trong trường hợp này, công cụ có trong máy chủ MCP

là một công cụ định vị giúp tìm ra, khi tôi nói Burnaby,

điều đó thực sự có nghĩa là gì?

Và sau đó, nó hiển thị thông tin về những vị trí đó

sau đó có thể được chuyển đến máy chủ thời tiết.

Sau đó, nếu tôi nói, "Thời tiết hiện tại thế nào?"

Tôi sử dụng get current_function

nó đi và nhận được thời tiết hiện tại.

Nếu tôi nói, "Thời tiết thế nào

sẽ mất khoảng một tuần kể từ bây giờ phải không?"

Sau đó, nó sẽ sử dụng hàm get_forecast,

nhận thông tin ngày tháng.

Nếu tôi nói, "Thời tiết vào thứ Sáu tuần trước thế nào?"

Nó sẽ quay trở lại lịch sử và gửi một lệnh khác.

Và nếu tôi nói get_stats, nó sẽ nhận được nhiều chỉ số hơn bình thường

bởi vì sau đó chúng ta có thể vẽ đồ thị và các thứ khác.

Và sau đó, máy chủ MCP

kết nối với dịch vụ bên ngoài thông qua API.

Đây chính là điều tôi muốn nói khi nói đó là một công nhân trung gian.

Điều này có một số ý nghĩa quan trọng

bởi vì điều đó có nghĩa là nếu bất kỳ dịch vụ nào có khả năng

để kết nối với nó như một API

hoặc đang chạy trên hệ thống hiện tại của bạn,

sau đó bạn có thể xây dựng một máy chủ MCP

cho phép một tác nhân trò chuyện nói chuyện với hệ thống đó,

điều đó làm cho những điều thực sự thú vị có thể xảy ra.