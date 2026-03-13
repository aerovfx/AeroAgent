# 010 Phím tắt con trỏ vi

---

Trong phần trước, chúng tôi đã nói rất chi tiết về các dấu và sao toán tử.

Bài học kinh nghiệm lớn là nếu chúng ta có một giá trị, chúng ta có thể biến nó thành một bộ nhớ địa chỉ bằng cách sử dụng ký hiệu giá trị

hiệu và.

Và nếu chúng ta có một địa chỉ hoặc một con trỏ, chúng ta có thể biến nó thành một giá trị với sao địa chỉ.

Và chính xác đó là những gì chúng tôi đã tìm thấy trong cơ sở mã hóa của mình.

Chúng tôi đã biến con trỏ tới struct Jim thành một con trỏ hoặc một bộ nhớ địa chỉ bằng cách sử dụng ký hiệu

và ngay tại đây.

Và sau đó chúng tôi biến nó trở lại thành một giá trị bằng cách sử dụng dấu sao toán tử.

Một điều rất quan trọng khác cần ghi nhớ, và một lần nữa, đây là một trong những vấn đề

lớn nhất xung quanh con trỏ và tôi nghĩ rằng bất cứ khi nào bạn nhìn thấy một ngôi sao phía trước một loại,

điều đó có nghĩa là chúng tôi đang tìm kiếm một loại con trỏ cho một người.

Nhưng nếu họ nhìn thấy một ngôi sao phía trước một con trỏ thực tế hoặc một biến thực tế chứa một con trỏ, trong trường

hợp lý, chúng tôi giải thích đây là một toán tử cho biết, Này, tôi muốn biến con trỏ này thành một giá

người thực tế có giá trị.

Được chứ.

Vì vậy, trong phần này, chúng tôi sẽ thực hiện công việc nhanh chóng.

Đây là một phần rất ngắn.

Tôi muốn chỉ ra một điều nhỏ xung quanh các con trỏ mà bạn sẽ thấy rất thường xuyên trong mã go

thực và ngay trong mã chúng tôi viết trong tương lai.

Sau khi vượt qua điều đó, chúng ta sẽ nghỉ ngơi một chút và sau đó quay lại và nói về một trong những vấn đề

vấn đề thực tế có thật xung quanh.

Đi.

Vì vậy, chúng ta hãy bắt đầu ngay bây giờ.

Trong mã mà chúng tôi có ngay bây giờ, bạn sẽ nhận được ngay tại đây nơi chúng tôi nói ký hiệu và Jim và sau

đó chỉ định nó cho Jim Pointer.

Và chỉ sau đó chúng tôi gọi tên cập nhật Jim Pointer.

Ừ.

Đây là một nỗi đau thực sự ở hậu phương để viết ngay sau đây.

Đúng.

Giống như chúng tôi thực sự muốn viết ra mã này mỗi khi chúng tôi muốn sửa đổi một cấu trúc, chúng tôi có

could not be.

Vì vậy, hãy có một chút đường tắt về cơ bản thực hiện điều chỉnh ngay tại đây.

Vì vậy, một điều trước khi chúng tôi xem xét luận điểm tắt này, tôi muốn làm rõ một điều.

Hãy nhớ rằng, khi chúng tôi nói ký hiệu và Jim, sẽ chỉ định một con trỏ cho một người vào biến.

Jim Pointer Vì vậy, nếu tôi di chuột qua điều này trong mã V, ngay cả mã của V cũng nói, vâng, đây là một con trỏ đến một người, không nghi ngờ

không ngờ nữa.

Đúng?

Vì vậy, khi chúng tôi tạo bản cập nhật tên chức năng đó và sau đó chúng tôi xác định loại người nhận chỉ định

Nó là con trỏ tới người, hai thứ này rất khớp nhau, phải không?

Giống như đây là con trỏ tới người, đây là loại con trỏ tới người nhận.

Đúng.

Hai người đi cùng nhau một cách hoàn hảo.

Họ xếp hàng 100%.

Bây giờ, với suy nghĩ đó, chúng tôi sẽ thực hiện một chút thay đổi đối với mã hóa

chúng tôi đang xem xét những điều lạ, nhưng nó sẽ dẫn đến việc viết mã trong thực tế ít hơn rất nhiều.

Vì vậy, điều đầu tiên tôi sẽ làm là tôi sẽ xóa dòng này nơi chúng tôi nhận

được bộ nhớ địa chỉ của Jim và sau đó tôi sẽ thay đổi Con trỏ Jim thành Jim đơn giản.

Bây giờ tôi sẽ lưu tệp.

Tôi sẽ quay lại thiết bị cuối cùng của mình và tôi sẽ chạy, chạy, chạy, Main, quay lại và bạn sẽ nhận thấy mã đó

chúng tôi vẫn đang hoạt động.

Vì vậy, tôi vẫn còn một cái tên đầu tiên của Jimmy ngay tại đây.

Nhưng bây giờ bạn sẽ thấy rằng thực sự có sự không phù hợp trong các loại bộ máy của chúng tôi.

Vì vậy, ngay tại đây, nếu tôi di chuột qua Jim và mã vs, nó nói rất rõ ràng 100%, không nghi ngờ gì nữa.

Jim là một người có kiểu biến thể, vì vậy Jim có giá trị là một cấu trúc.

Ở đây không có bộ nhớ địa chỉ, không có con trỏ và không có gì tương tự.

Nhưng dù bằng cách nào đi nữa, họ vẫn có thể sử dụng chức năng này của một bộ thuộc tính hoàn toàn khác

loại này là con trỏ tới người, phải không?

Con trỏ tới người, đây chỉ là người.

Vì vậy, đây là một đoạn đường tắt để đi cùng.

Nếu chúng tôi xác định bộ thu có kiểu con trỏ tới bất kỳ thứ gì, hãy đưa ra giới hạn như con trỏ trống, bất kỳ kiểu nào mà bạn có thể

Tượng trưng khi chúng ta cố gắng đi gọi hàm này hoặc chúng ta cố gắng đi gọi phương thức

Điều này ngay tại đây, go sẽ cho phép họ gọi hàm này với một con trỏ hoặc với một cốt lõi như kiểu gốc, về cơ bản, con người của bạn trong trường hợp này,

bạn biết không, chúng ta hãy xem sơ đồ sẽ giải quyết nó tốt

hơn là tôi có thể.

Được chứ.

Vì vậy, đây là mã ban đầu mà chúng tôi vừa có.

Đây là những thay đổi mà chúng tôi vừa thực hiện và đây là những chức năng mà chúng tôi đang làm.

Vì vậy, tại thời điểm này, lặp lại nhiều lần đã nói, đã được rồi, Jim Pointer thuộc loại con trỏ tới từng người.

Và sau đó chúng tôi có máy thu của mình, đó là con trỏ.

Vì vậy, hai trường hợp ngay tại đây xếp hàng hoàn hảo.

Nhưng hãy cho phép chúng tôi tắt và nói, điều này, nếu bạn có một biến chỉ là loại người, nhưng sau đó là người

nhận của bạn là con trỏ đến từng người, điều đó hoàn toàn ổn.

Chúng tôi sẽ chỉ giải thích rõ ràng điều đó cho bạn và sẽ tự động biến các loại biến thể của người dùng

bạn thành người gợi ý cho bạn.

Vì vậy, nói theo cách khác, đây chỉ là một phím tắt nhỏ mà chúng ta sẽ sử dụng về

cơ bản mỗi khi chúng tôi sử dụng loại bộ thu ngay tại đây của loại bộ thu là con trỏ.

Vì vậy, chúng tôi thực sự không cần phải lấy địa chỉ bộ nhớ từ Jim ngay tại đây.

Go chỉ là để chăm sóc nó cho chúng tôi.

Bây giờ, tất nhiên, nếu chúng tôi quay lại mã của chúng tôi ở đây và chúng tôi thay đổi con trỏ thành người, quay lại chỉ người, tốt,

Hiện tại mọi thứ sẽ bị hỏng khi chúng tôi sử dụng điểm này ngay tại đây

bởi vì bây giờ chúng tôi sẽ nói, đã được rồi, con người là loại người không có ý kiến gì ở đây cả.

Và vì vậy nếu chúng tôi cố gắng tham khảo con trỏ này đến từng thứ với ngôi sao ngay tại đây thì bây giờ mã của

chúng ta sẽ bị hỏng.

Vì vậy, về cơ bản vào cuối ngày, những gì tôi đang cố gắng đạt được ở đây, chúng tôi có hai lựa chọn.

Chúng tôi có thể lấy bộ nhớ địa chỉ từ Jim và sau đó sử dụng địa chỉ đó để làm bộ nhớ tại đây, hoặc chúng tôi có thể chỉ

use value of main it.

Dù bằng cách nào đi nữa, nó sẽ hoạt động tốt với một con trỏ tới loại của chúng tôi.

Bây giờ một lần nữa, đây có thể là một trong những điều bạn đang nói, Stephen, khác biệt là gì?

Điều khác biệt ở đây là gì?

À, một lần nữa, đây là một trong những thứ mà bạn sẽ phải tự viết một

chút mã và xem một chút nội dung này trong các bài tập trước khi tôi nghĩ rằng nó thực sự sẽ chìm vào.

Vì vậy, với suy nghĩ đó, chúng ta hãy nghỉ ngơi nhanh chóng.

Chúng tôi sẽ tiếp tục trong phần tiếp theo.

Và tôi muốn chỉ ra một điều đó không phải là một cách chơi chữ, nhân tiện, khi tôi nói quan điểm, tôi muốn chỉ ra

một hoặc hai điều nhỏ nhanh chóng và cho rằng đó là những vấn đề thực sự quan trọng xung quanh tất cả những thứ liên quan đến con trỏ này.

Vì vậy, hãy nhanh chóng nghỉ ngơi và tôi sẽ gặp bạn chỉ sau một phút.