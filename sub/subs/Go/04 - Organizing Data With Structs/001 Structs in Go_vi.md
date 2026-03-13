# 001 Struct trong Go vi

---

Chà, đã đến lúc bắt tay vào thực hiện dự án tiếp theo của chúng ta.

Đối với dự án tiếp theo này, chúng tôi sẽ bắt đầu bằng cách quay lại dự án của chúng ta, bộ bài.

Và tôi muốn chỉ ra một điều gì đó trong dự án có thể hơi khó xử lý.

Vì vậy, một cái gì đó có thể sẽ gặp một chút công thức nếu chúng tôi quyết định tiếp

Tiếp tục mở rộng dự án đó.

Sau khi chúng tôi nói về vấn đề đó là gì và chúng tôi hiểu rằng nó có thể là một vấn đề nhỏ như thế

dù sao đi nữa, chúng tôi sẽ nói về một tính năng mới trong GO sẽ giúp chúng tôi giải quyết vấn đề đó.

Và sau đó chúng tôi sẽ bắt đầu công việc trên một chương trình nhỏ để khám phá những tính năng đó nhiều hơn một chút.

Vì vậy, hãy bắt đầu bằng cách nói về những gì có thể gây khó khăn trong việc xử lý Thẻ dự án.

Vì vậy, trong Thẻ dự án, bạn nên nhớ rằng chúng tôi đã làm việc với một đoạn chuỗi và mỗi chuỗi được sử dụng

để đại diện cho một thẻ chơi duy nhất.

Vì vậy, chúng tôi đã có một lá bài như Ace of Spades hoặc hai quân Bich hoặc ba quân tiền.

Bây giờ trong dự án đó, chúng tôi thực sự không bao giờ phải hỏi bất kỳ thẻ cụ thể nào xem nó phù hợp với hoặc giá trị của nó

là bao nhiêu.

Nhưng tôi chắc chắn rằng bạn có thể dễ dàng hình dung ra rằng nếu chúng tôi muốn mở rộng dự án

ở đó và bắt đầu tập hợp một thứ gì đó như, ví dụ như trò chơi poker hoặc trò chơi xì dách hoặc đánh cá hay những thứ tương thích

tự động, vào một thời điểm nào đó, chúng tôi thực sự muốn có thể xem xét một thẻ và rất dễ dàng đặt câu hỏi,

thẻ này phù hợp với điều gì và mệnh giá của thẻ đó là bao nhiêu?

Vì vậy, lý do làm mà nó sẽ rất khó khăn với cách mà chúng tôi đã đặt ra mọi thứ

là để tìm ra những gì phù hợp hoặc có giá trị của bất kỳ thẻ nào nhất.

Chúng tôi sẽ phải thực hiện một chuỗi thao tác nhỏ, vì vậy chúng tôi sẽ

phải lấy chuỗi, chia nó theo từ của nó và sau đó loại ra giá trị và bộ đồ từ đó.

Và vì vậy, bạn biết đấy, điều đó không phải là không thể.

Nó không nằm ngoài khả năng phạm vi.

Nhưng tôi nghĩ rằng điều đó sẽ thực sự khó xử lý nếu kết hợp chương trình của chúng ta theo kiểu đó và

nói rằng mãi mãi, vâng, một tấm thẻ là một chuỗi.

Và như vậy, trong phần này, chúng ta sẽ bắt đầu xem xét một cấu trúc dữ liệu khác và đi đến cái mà chúng

ta có thể sử dụng để đại diện cho một thẻ chơi riêng.

Vì vậy, chúng tôi sẽ bắt đầu bằng cách nói về cấu trúc dữ liệu đó là gì, nó hoạt động như thế nào và sau đó

chúng tôi sẽ bắt đầu thực hiện một dự án nhỏ để khám phá cách thức hoạt động của cấu trúc mới này.

Vì vậy, dữ liệu cấu trúc mà chúng ta sẽ gọi là cấu trúc cấu trúc.

Vì vậy, tôi đã nói hướng dẫn struct ở đây, thực tế một số cấu trúc cấu trúc đã được viết tắt của cấu trúc.

Nó là một dữ liệu cấu trúc đang hoạt động.

Và bạn có thể coi nó giống như một tập hợp các thuộc tính khác nhau có liên quan với nhau bằng cách

bất kỳ mục tiêu nào hoặc có một số loại mục tiêu chung.

Và vì vậy, nếu chúng tôi nghĩ ra ví dụ về một thẻ ở đây, chúng tôi có thể đã tạo một dữ liệu cấu trúc,

cấu trúc của các loại thẻ và sau đó phân bổ các thuộc tính khác nhau cho cấu trúc đó.

Vì vậy, chúng tôi có thể nói rằng cấu trúc loại thẻ có thể có một bộ đồ được chọn là một

string and can may be a value, can be choose a string.

Và sau đó như một sự phát triển khai thực tế hoặc như một ví dụ như một giá trị của các loại thẻ, chúng ta có thể có một bộ

Quân át và một giá trị quân át.

Bây giờ, tôi sẽ nói với bạn ngay bây giờ rằng ngay khi chúng tôi bắt đầu xem xét cấu trúc, if

Bạn có kiến thức cơ bản về JavaScript, bạn có thể nghĩ cấu trúc tương tự như một đối tượng đơn giản.

Và nếu bạn có nền tảng kiến ​​thức về Ruby, hãy nghĩ về một cấu trúc tương tự như hàm băm.

Và nếu bạn có kiến ​​thức nền tảng về Python, hãy nghĩ về nó giống như một cuốn từ điển.

Bây giờ, đó không phải là một định nghĩa thực sự chính xác, hoàn hảo về cấu trúc là gì.

Tôi chỉ nói rằng ngay bây giờ ở cấp độ rất cao, bạn có thể nghĩ về một cấu trúc tương tự như những thứ đó

data config type.

Vì vậy, tôi nghĩ rằng cách tốt nhất là tìm ra cách thức hoạt động chính xác của các cấu trúc đang hoạt động với một mẫu dự án

nhỏ xung quanh nó.

Và vì vậy, dự án này sẽ không phải là một ứng dụng đầy đủ tính năng cho một mục tiêu.

Thay vào đó, chúng tôi sẽ viết một cấu trúc mã nhỏ và sau đó hiểu rõ hơn về cách chúng hoạt động và

chúng ta có thể sử dụng chúng để làm gì.

Vì vậy, hãy bắt đầu dự án đó ngay bây giờ bằng cách tạo và tạo một dự án thư mục mới

một tệp chính mới.

Vì vậy, tôi sẽ chuyển sang trình soạn thảo mã hóa của mình.

Tôi sẽ vào hồ sơ, chúng tôi sẽ mở một thư mục mới.

Vì vậy, tôi sẽ tạo một thư mục mới và tôi sẽ gọi nó đơn giản là cấu trúc.

Chúng tôi sẽ mở thư mục này và sau đó trong thư mục mới, tôi sẽ tạo một tệp mới có tên là Main

Đi.

Vì vậy, chúng tôi nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay trở lại trong phần tiếp theo và chúng ta sẽ bắt đầu làm việc với

một vài ví dụ để hiểu rõ hơn về cấu trúc là gì.

Vì vậy, hãy nhanh chóng nghỉ ngơi và tôi sẽ gặp lại bạn chỉ sau một phút.