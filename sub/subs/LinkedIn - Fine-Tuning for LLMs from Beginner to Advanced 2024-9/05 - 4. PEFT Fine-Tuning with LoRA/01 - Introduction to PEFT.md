# 01 - Giới thiệu về PEFT

---

- Chúng ta đã nói về kỹ thuật nhanh chóng

và chuyển giao việc học để tinh chỉnh.

Bây giờ chúng ta sẽ tìm hiểu

tinh chỉnh tham số hiệu quả hoặc PEFT.

Chúng tôi sẽ giải thích PEFT là gì, nó khác nhau như thế nào

từ việc tinh chỉnh và chuyển giao truyền thống,

và tại sao nó đặc biệt có giá trị khi chúng ta có ít dữ liệu.

Để giữ mọi thứ hấp dẫn,

chúng ta sẽ sử dụng phép so sánh nấu ăn để minh họa những khái niệm này.

Hãy tưởng tượng bạn là một đầu bếp đang làm việc với những nguyên liệu hạn chế.

Bạn cần tạo ra một món ăn ngon

mà không có quyền truy cập vào một phòng đựng thức ăn đầy đủ.

Điều này tương tự như thách thức phải đối mặt trong học máy

khi dữ liệu còn ít.

Tinh chỉnh truyền thống có thể đòi hỏi nhiều tài nguyên,

giống như có một nhà bếp đầy ắp đồ.

Tuy nhiên, PEFT giống như làm chủ nghệ thuật nấu ăn

với những gì bạn có, tối ưu hóa công dụng của từng thành phần.

PEFT tập trung vào việc sửa đổi

một tập hợp con nhỏ các tham số của mô hình

hơn là toàn bộ mô hình.

Phương pháp này mang lại hiệu quả cao nên có thể

để đạt được những cải tiến đáng kể về hiệu suất

mà không cần phải đào tạo lại rộng rãi.

Hãy phá vỡ sự khác biệt.

Trong tinh chỉnh truyền thống, bạn điều chỉnh tất cả các thông số

của một mô hình được đào tạo trước để thích ứng với một nhiệm vụ mới.

Nó giống như làm lại toàn bộ công thức từ đầu.

Học chuyển giao bao gồm việc sử dụng một mô hình được đào tạo trước,

thêm các lớp hoặc đầu mới vào nó,

tương tự như việc thêm một đồ trang trí mới

hoặc nước sốt cho món ăn đã hoàn thành.

Mặt khác, PEFT,

liên quan đến việc thêm các thành phần nhỏ gọi là bộ điều hợp.

Hãy coi bộ điều hợp như các công cụ hoặc kỹ thuật chuyên dụng

giúp nâng tầm món ăn mà không làm thay đổi công thức cốt lõi.

Những bộ điều hợp này cho phép mô hình học các nhiệm vụ mới

sử dụng hiệu quả dữ liệu bổ sung tối thiểu.

Bộ điều hợp là mô-đun nhẹ

được đưa vào mô hình được huấn luyện trước.

Trong quá trình đào tạo, chỉ những bộ điều hợp này mới được cập nhật

trong khi phần còn lại của mô hình vẫn không thay đổi.

Phương pháp này làm giảm đáng kể

các tài nguyên tính toán cần thiết

và làm cho quá trình đào tạo nhanh hơn và hiệu quả hơn.

Ví dụ: nếu bạn đang đào tạo một mô hình ngôn ngữ

để hiểu các văn bản pháp luật, bạn có thể chèn bộ chuyển đổi

chuyên về thuật ngữ và bối cảnh pháp lý.

Những bộ điều hợp này được đào tạo với tập dữ liệu hạn chế của bạn,

điều chỉnh mô hình để thực hiện tốt nhiệm vụ cụ thể này

mà không cần phải đào tạo lại toàn bộ mô hình.

Tại sao PEFT lại quan trọng khi dữ liệu còn ít?

Đó là tất cả về hiệu quả.

Với PEFT, bạn có thể đạt được hiệu suất cao

với ít điểm dữ liệu hơn với sức mạnh tính toán ít hơn.

Điều này đặc biệt có lợi trong các tình huống

nơi thu thập số lượng lớn

dữ liệu được dán nhãn là không thực tế hoặc quá tốn kém.

Tóm lại, tinh chỉnh tham số hiệu quả hoặc PEFT

là một kỹ thuật mạnh mẽ cung cấp một giải pháp thay thế hiệu quả

sang việc tinh chỉnh và chuyển giao học tập truyền thống,

đặc biệt khi xử lý dữ liệu hạn chế.

Bằng cách sử dụng các bộ điều hợp, PEFT tối ưu hóa quá trình học tập,

đảm bảo rằng ngay cả với ít dữ liệu,

bạn vẫn có thể đạt được kết quả xuất sắc.

Điều này làm cho PEFT trở thành một công cụ thiết yếu

trong bộ công cụ AI hiện đại.