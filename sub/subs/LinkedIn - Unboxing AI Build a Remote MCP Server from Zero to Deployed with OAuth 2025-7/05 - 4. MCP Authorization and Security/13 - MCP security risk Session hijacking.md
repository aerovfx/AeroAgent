# 13 - Rủi ro bảo mật MCP Chiếm quyền điều khiển phiên

---

- Chúng tôi cũng có chiếm quyền điều khiển phiên.

Đó là khi ai đó thực sự nhìn thấy một phiên đang diễn ra

giữa máy chủ MCP được ủy quyền và một số máy chủ khác,

một số dịch vụ bên ngoài và tiếp quản toàn bộ phiên đó.

Điều này có thể xảy ra nếu máy chủ MCP được xây dựng để thực hiện việc đó.

Vì vậy, ai đó có thể xây dựng một máy chủ MCP độc hại

bàn giao phiên cho một số bên thứ ba.

Vì vậy, thông thường, khi bạn làm việc với nó

và bạn đã đăng nhập, mọi thứ đều ổn.

Nhưng rồi ai đó có thể bước vào và nói,

"Không, tôi sẽ tiếp quản phiên họp."

Và rồi đột nhiên, bạn mất quyền kiểm soát dịch vụ

và người khác đang hành động thay mặt bạn

trong dịch vụ.

Đây là điều có thể xảy ra

bởi vì máy chủ MCP đang hoạt động như một nhân viên trung gian

và bởi vì LLM đang thực hiện tương tác

với dịch vụ thay vì bạn.

Nếu ai đó chiếm quyền điều khiển phiên,

có thể bạn chưa biết từ lâu.

Vì vậy có thể có một điều hoàn toàn khác đang xảy ra

ngoài tầm cung cấp của bạn

trong khi LLM của bạn không tương tác với dịch vụ.

Vì vậy, một lần nữa, đây là một rủi ro đáng kể

và đó là điều bạn có thể giảm nhẹ

bằng cách sử dụng hệ thống xác thực chính thức

được xây dựng để bảo vệ chống lại các kiểu tấn công này.