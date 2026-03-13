# 01 thành phần cốt lõi của langgraph

---

Chào mừng bạn đến với video này về các thành phần cốt lõi của LangGraph.

Trong video này, bạn sẽ khám phá cách LangGraph

mô hình hóa quy trình làm việc của tác nhân dưới dạng biểu đồ linh hoạt,

hiểu vai trò cốt lõi của các nút, cạnh và trạng thái.

Bạn sẽ có được kiến thức về khả năng mạnh mẽ của nó

như các tính năng lặp, phân nhánh và con người trong vòng lặp.

Bạn cũng sẽ phân tích lý do tại sao LangGraph lại vượt trội trong các công việc phức tạp.

Tác nhân AI và cách trực quan hóa quy trình làm việc phức tạp của nó.

LangGraph là một framework nâng cao trong

hệ sinh thái LangChain được xây dựng cho

xây dựng các ứng dụng đa tác nhân có trạng thái.

Nó được thiết kế ở mức độ thấp và linh hoạt, mang lại cho bạn

kiểm soát hoàn toàn mà không có sự trừu tượng hạn chế.

LangGraph là một framework mô hình hóa

quy trình làm việc của đại lý dưới dạng biểu đồ trong đó

Các nút giống như các bước hoặc chức năng riêng lẻ

thực hiện tính toán thực tế.

Các cạnh chỉ cho bạn đường dẫn, xác định cách

việc thực thi diễn ra từ bước này sang bước tiếp theo.

Và cuối cùng, trạng thái là cấu trúc dữ liệu được chia sẻ hoặc

bộ nhớ ghi nhớ mọi thứ xuyên suốt

tất cả các nút này, giúp duy trì bối cảnh quy trình làm việc của bạn.

Cấu trúc biểu đồ độc đáo của LangGraph mang lại cho bạn nhiều khả năng.

Bạn có thể có vòng lặp và phân nhánh, có nghĩa là

đại lý của bạn có thể đưa ra quyết định năng động khi họ đi.

Sau đó, có sự bền bỉ của trạng thái, vì vậy AI của bạn có thể

duy trì bối cảnh ngay cả trong những tương tác thực sự dài.

Và bạn thậm chí có thể có chức năng con người trong vòng lặp,

cho phép bạn bước vào khi cần thiết bằng tay.

Cuối cùng, có sự du hành thời gian để tạo điều kiện thuận lợi

gỡ lỗi bằng cách tua lại về trạng thái trước đó.

Bạn có thể tự hỏi, tại sao không chỉ

bám vào vòng lặp for hoặc câu lệnh if?

Vâng, các vòng lặp lập trình truyền thống, như for

hoặc while và các câu lệnh if khá tuyến tính.

Họ chỉ lặp lại một khối mã cho đến khi đạt được một yêu cầu nhất định

điều kiện được đáp ứng hoặc họ đánh giá các điều kiện

để quyết định điều gì xảy ra tiếp theo.

Và mặc dù chúng có hiệu quả đối với những việc lặp đi lặp lại đơn giản

nhiệm vụ, chúng thực sự thiếu sự linh hoạt mà bạn

cần các quy trình làm việc có trạng thái phức tạp.

Mặt khác, LangGraph cung cấp một cách rõ ràng

quản lý trạng thái, cho phép quy trình làm việc

duy trì và sửa đổi bối cảnh trên các nút khác nhau.

Chuyển đổi có điều kiện, cho phép quy trình làm việc

đưa ra quyết định trong thời gian chạy và chi nhánh tương ứng.

Tính mô đun, trong đó mỗi nút có thể được phát triển và

được thử nghiệm độc lập, thúc đẩy các thành phần có thể tái sử dụng.

Cuối cùng, khả năng quan sát nâng cao mang lại sự rõ ràng

hiểu biết sâu sắc về đường dẫn thực thi của quy trình làm việc,

đó là điều vô giá cho việc gỡ lỗi và giám sát.

LangGraph đặc biệt thích hợp cho việc xây dựng

các tác nhân AI phức tạp thực sự cần năng động

khả năng ra quyết định và khả năng thích ứng.

Hãy tưởng tượng bạn đang xây dựng một nhân viên hỗ trợ khách hàng.

Vòng lặp while có thể tiếp tục hỏi người dùng cho đến khi đầu vào hợp lệ

được đưa ra, nhưng nó sẽ không nhớ các chủ đề trong quá khứ.

Mặt khác, quy trình làm việc LangGraph có thể

nhánh, vòng lặp, tạm dừng cho đầu vào của con người và tiếp tục

thực hiện tất cả trong khi vẫn giữ được bộ nhớ đàm thoại đầy đủ.

Đồ thị LangGraph cũng có thể được hiển thị bằng cách sử dụng

sơ đồ nàng tiên cá, giúp bạn hiểu và

gỡ lỗi cấu trúc đồ thị trực quan hơn.

Trong ví dụ này, các nguyên thủy cốt lõi,

các nút và các cạnh được thể hiện rõ ràng.

Những nguyên thủy này cho phép xây dựng phức tạp

quy trình công việc với cấu trúc rõ ràng và có thể bảo trì.

Trong video này, bạn đã học được rằng

LangGraph là một framework nâng cao được thiết kế

để xây dựng các ứng dụng đa tác nhân có trạng thái.

Các nút là các hàm thực hiện tính toán thực tế.

Các cạnh xác định cách thức thực thi từ bước này sang bước tiếp theo.

Trạng thái là bộ nhớ dùng chung ghi nhớ mọi thứ trên các nút.

Các khả năng độc đáo của LangGraph bao gồm lặp

và phân nhánh để đưa ra các quyết định năng động,

trạng thái kiên trì để duy trì bối cảnh trong thời gian dài

tương tác, chức năng con người trong vòng lặp

sự can thiệp kịp thời của con người và thời gian

đi du lịch để tạo điều kiện gỡ lỗi thuận tiện.

LangGraph cung cấp khả năng quản lý trạng thái, cho phép quy trình làm việc

để duy trì và sửa đổi bối cảnh trên các nút khác nhau.

Nó cũng cung cấp các chuyển tiếp có điều kiện, cho phép

quy trình làm việc để đưa ra quyết định trong thời gian chạy

và phân nhánh tương ứng.

Luồng công việc LangGraph có thể phân nhánh, lặp, tạm dừng

cho đầu vào của con người và tiếp tục thực hiện tất cả

trong khi vẫn bảo toàn được bộ nhớ đàm thoại đầy đủ.

Đồ thị LangGraph có thể được hiển thị bằng cách sử dụng nàng tiên cá

sơ đồ với các nguyên thủy cốt lõi, chẳng hạn như các nút

và các cạnh, được thể hiện rõ ràng.