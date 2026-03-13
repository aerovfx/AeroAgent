# 3 -Khám phá kiến ​​trúc của MCP.en US

---

Được rồi các bạn, vì vậy trong này

video cụ thể hãy cùng xem nhé

MCP từ một tiêu chuẩn là gì

quan điểm tài liệu.

Vậy là MCP đã thực sự được giới thiệu

bởi Anthropic, công ty

đằng sau Claude, mà

lại là một mô hình LLM.

Vậy bạn có thể thấy nó là

thực sự đã ra mắt vào ngày 25

Tháng 11 năm 2024.

Vậy là nó đã ở đó

một lúc.

Vì vậy, hãy hiểu những gì là

Giao thức bối cảnh mô hình?

Mcp.

Được rồi, xem nào

về cơ bản họ nói.

Hôm nay chúng tôi đang mở nguồn cung ứng

Giao thức bối cảnh mô hình,

một tiêu chuẩn mới cho

kết nối hỗ trợ AI

đến nơi dữ liệu tồn tại.

Ý tôi là cách sử dụng thực sự hay,

cách thực sự tốt đẹp để nói công cụ.

Vì vậy, về cơ bản đây là

những công cụ gì.

Được rồi, vậy nơi dữ liệu tồn tại

bao gồm cả nội dung

kho lưu trữ, công cụ kinh doanh

và môi trường phát triển.

Nó nhằm mục đích giúp các mô hình biên giới

LLM của bạn để sản xuất

tốt hơn và phù hợp hơn

phản hồi với tư cách là trợ lý AI

đạt được sự chấp nhận chính thống.

Ngành đã đầu tư

tập trung nhiều vào khả năng của mô hình,

đạt được những tiến bộ nhanh chóng

về lý luận và chất lượng.

Tuy nhiên ngay cả những thứ phức tạp nhất

mô hình bị hạn chế bởi

dạng dữ liệu cô lập của chúng.

Điều đó có nghĩa là họ được đào tạo

trên một hệ thống nào đó.

Mỗi nguồn dữ liệu mới đều yêu cầu

phong tục riêng của nó

việc thực hiện, làm cho nó

thực sự khó khăn, hệ thống

khó mở rộng quy mô, điều đó

về cơ bản nói là C, mặc dù

chúng tôi có những mô hình thực sự đẹp

ngoài kia, bạn vẫn không thể

đào tạo mô hình đó mỗi ngày.

Có dữ liệu mới

nguồn hàng ngày.

Bạn không thể giữ

khi huấn luyện dữ liệu này.

Rất khó để

mở rộng quy mô các loại hệ thống này.

MCP giải quyết thách thức này.

Nó cung cấp một cách mở phổ quát

chuẩn kết nối AI

hệ thống với các nguồn dữ liệu.

Bạn có thể kết nối nó với

Postgres, bạn có thể kết nối

nó vào MongoDB, bạn có thể

kết nối nó với một trang web,

bạn có thể kết nối nó với

Bông tuyết, bạn có thể kết nối

nó tới một số luồng dữ liệu.

Vì vậy, về cơ bản đây là

những gì MCP nói.

Vì vậy, ví dụ như những gì họ

đang nói là bạn có thể

có MCP cho Postgres,

bạn có thể có MCP cho,

cho MongoDB, phải không?

MCP cho MongoDB, bạn có thể có

một MCP có thể lấy dữ liệu

từ Google Tìm kiếm, Google

Tìm kiếm và mcp, phải không?

Bạn có thể có MCP trong khoảng thời gian

đại loại như chúng ta hãy lấy

một ví dụ về Bông tuyết, được chứ?

Hoặc có thể là Kafka,

một cái gì đó như thế

Vì vậy ngay khi tôi

kết nối postgres này.

Ồ, bây giờ là hình mẫu Song Tử của tôi,

mô hình LLM của tôi có quyền truy cập

vào cơ sở dữ liệu postgres của tôi.

Nó có thể truy vấn, nó có thể

lấy lại nếu tôi kết nối cái này

MCP MongoDB cụ thể.

Bây giờ mô hình LLM của tôi có

truy cập vào MongoDB của tôi.

Bây giờ nó thậm chí có thể thực hiện một thao tác Google

tìm kiếm và bây giờ nó thậm chí có thể

thực hiện truy vấn Bông tuyết.

Vì vậy, về cơ bản đây là những gì

ý họ là điều này.

Được rồi?

Giao thức bối cảnh mô hình.

Bây giờ, đây là một nền tảng

về mô hình

giao thức ngữ cảnh.

Hãy đi vào

một tài liệu chuyên dụng.

Được rồi, đây là

một tài liệu chuyên dụng.

Vì vậy, điều này nói lên rằng MCP là

một giao thức mở

chuẩn hóa cách các ứng dụng

cung cấp bối cảnh cho LLM.

Hãy coi MCP giống như cổng USB C

cho các ứng dụng AI.

Cũng như mc.

Giống như USB C cung cấp một

cách kết nối được tiêu chuẩn hóa

thiết bị của bạn khác nhau

thiết bị ngoại vi và phụ kiện,

MCP cung cấp một

được tiêu chuẩn hóa, tôi đang tập trung

trên một từ, theo cách tiêu chuẩn hóa

để kết nối các mô hình AI với

nguồn dữ liệu khác nhau.

Vì vậy, về cơ bản đây là

MCP của bạn hoạt động như thế nào.

Được rồi, bây giờ chúng ta hãy

chỉ cần làm một điều

Hãy để chúng tôi hiểu

khái niệm cốt lõi, làm thế nào

MCP về cơ bản hoạt động.

Được rồi?

chủ yếu có

ba thành phần.

Máy chủ MCP, Máy khách MCP,

và máy chủ MCP.

Nếu tôi phải nói với bạn

một định nghĩa chỉ trong một lần

Máy chủ MCP về cơ bản là gì

ứng dụng AI của bạn,

bạn là chủ nhà.

Ví dụ: nếu tôi đang sử dụng

id này, bạn có thấy nó không

Tôi có đại lý này đang chạy?

Đây là máy chủ MCP.

Được rồi, IDE này là thứ

máy chủ MCP, sau đó là MCP

khách hàng, một thành phần

duy trì kết nối

tới máy chủ MCP.

Bây giờ, trong máy chủ MCP này, trong

IDE mà tôi đang chạy, ở đó

là cài đặt cho mcp phải không?

Nếu tôi chỉ tìm kiếm mcp,

điều bạn sắp chú ý là

đó, vâng, tôi có một mcp.

Nếu tôi thêm một máy chủ,

Tôi thậm chí có thể thêm một máy chủ,

duyệt các máy chủ MCP.

Vậy đây là máy khách MCP.

Vậy điều đó có nghĩa là bên trong ide của tôi,

IDE của tôi là máy chủ MCP.

Bên trong máy chủ của tôi, một MCP

khách hàng đang chạy.

Được rồi, một khách hàng MCP là

về cơ bản là chạy bên trong tôi

ID này và Máy chủ MCP.

Giả sử tôi muốn kết nối

đến một số máy chủ từ xa.

Giống như, nó có thể là của Google

Máy chủ MCP, nó có thể

Máy chủ MCP của Twitter.

Nó có thể là bất kỳ máy chủ MCP nào

mà tôi muốn kết nối tới.

Về cơ bản mọi chuyện diễn ra như thế.

Vì vậy, ví dụ, nếu tôi nhấp vào

trên máy chủ MCP duyệt này,

bạn có thể thấy chúng tôi có

danh sách các máy chủ MCP.

Bạn có GitHub, bạn có

ôm mặt, bạn có figma,

bạn có nhà viết kịch.

Vậy bạn có thể thấy rằng bạn có

thực sự có rất nhiều máy chủ MCP.

Bạn có máy chủ MCP tuyến tính.

Ý niệm có đó.

Bạn có thể thấy tất cả điều đó

các công ty đang

về cơ bản bây giờ đang phơi bày

máy chủ MCP của họ.

Vì vậy, những gì bạn có thể làm,

bạn chỉ có thể kéo một cái

Máy chủ MCP từ đây.

Ví dụ như bạn

muốn wiki sâu, bạn

có khuôn mặt ôm sát.

Bất cứ điều gì bạn muốn, chỉ cần

chọn, bạn chỉ cần cài đặt

nó và thế thôi.

Ví dụ: nếu bạn cài đặt

MCP của GitHub, bạn

có quyền truy cập vào GitHub

Máy chủ MCP phải không?

Bạn có thể thấy yêu cầu kéo của mình,

bạn có thể thấy vấn đề của mình

Vì vậy, đại lý của bạn về cơ bản có thể

truy cập thông tin này.

Vì vậy, về cơ bản đây là

MCP hoạt động như thế nào.

Được rồi.

Vì vậy nếu chúng ta quay trở lại

đến kiến trúc và nếu chúng ta

chỉ cần đi xuống một chút.

Vậy là có một cái rất đẹp

sơ đồ được thực hiện bởi những người này.

Tôi nghĩ nó đã được cập nhật

nhưng không sao đâu.

Vì vậy hãy sử dụng mcp.

Là đây, kiến trúc

tổng quan tôi nghĩ.

Vâng, sơ đồ là

thực sự đã thay đổi.

Vì vậy trước đây điều này không phải

sơ đồ nhưng vâng.

Máy chủ MCP vì vậy hãy nói rằng bạn

có ứng dụng AI,

bạn có MCP Client 1, MCP

Khách hàng 2, Khách hàng MCP 3.

Và nó có thể duy trì một

trên một kết nối với

nhiều máy chủ MCP.

Ví dụ: có MCP

máy chủ vệ sinh,

có một máy chủ MCP cho

hệ thống tập tin, có MCP

máy chủ cho cơ sở dữ liệu.

Vì vậy, về cơ bản đây là

những gì MCP làm.