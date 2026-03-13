# 010 Phím tắt con trỏ vi

---

Steven: Trong phần cuối cùng,

chúng tôi đã nói chuyện rất chi tiết

về các toán tử dấu và và dấu sao.

Điều đáng rút ra là nếu chúng ta có một giá trị,

chúng ta có thể biến nó thành địa chỉ bộ nhớ

bằng cách sử dụng giá trị ký hiệu.

Và nếu chúng ta có một địa chỉ hoặc một con trỏ,

chúng ta có thể biến nó thành một giá trị với địa chỉ sao.

Và đó chính xác là những gì chúng tôi đã thấy trong cơ sở mã của mình.

Chúng tôi đã biến biến của mình thành

chỉ vào cấu trúc, jim,

vào một con trỏ hoặc một địa chỉ bộ nhớ

bằng cách sử dụng ký hiệu và ngay tại đây,

và sau đó chúng tôi đã đảo ngược điều đó

thành một giá trị bằng cách sử dụng toán tử ngôi sao.

Một điều rất quan trọng khác cần ghi nhớ,

và một lần nữa, đây là một trong những sự cố lớn nhất

xung quanh các con trỏ trong Go, tôi nghĩ,

đó là bất cứ khi nào bạn nhìn thấy một ngôi sao ở phía trước một loại chữ,

điều đó có nghĩa là chúng tôi đang tìm kiếm

một loại con trỏ tới một người

Nhưng nếu chúng ta nhìn thấy một ngôi sao ở phía trước một con trỏ thực sự,

một biến giống thực tế chứa một con trỏ,

trong trường hợp này, chúng tôi hiểu đây là một toán tử

có nội dung là "Này, tôi muốn xoay con trỏ này

thành một giá trị con người thực tế."

Được rồi, trong phần này,

chúng ta sẽ làm một việc thực sự nhanh chóng.

Đây sẽ là một phần rất ngắn.

Tôi muốn chỉ ra một điều nhỏ xung quanh con trỏ

mà bạn sẽ thấy rất thường xuyên trong mã Go thực tế,

và thậm chí cả mã mà chúng ta viết trong tương lai.

Sau khi chúng ta vượt qua chuyện đó,

sau đó chúng ta sẽ nghỉ ngơi

và sau đó quay lại và nói về một trong những điều có thật,

có vấn đề lớn thực sự xung quanh Go.

Vì vậy, hãy bắt đầu với nó.

Bây giờ, trong đoạn mã mà chúng ta có ngay bây giờ,

bạn sẽ nhận thấy ngay ở đây nơi chúng tôi nói &jim

và sau đó gán nó cho jimPointer,

và chỉ sau đó mới làm

chúng tôi gọi jimPointer.updateName.

Vâng, đây thực sự là một nỗi đau ở phía sau

viết ngay tại đây phải không?

Giống như chúng ta thực sự muốn viết ra đoạn mã này

mỗi lần chúng ta muốn sửa đổi một cấu trúc?

Vâng, có lẽ là không.

Vì vậy Go có một chút phím tắt

về cơ bản thì điều đó làm được

điều tương tự ở đây.

Vì vậy, có một điều trước khi chúng ta nhìn vào lối tắt này,

Tôi muốn làm rõ một điều cực kỳ rõ ràng,

hãy nhớ rằng, khi chúng ta nói &jim,

gán một con trỏ cho một người

tới biến jimPointer.

Vì vậy, nếu tôi di chuột qua phần này trong Mã VS,

ngay cả VS Code cũng nói,

"Đúng, đây là một con trỏ tới một người".

không còn nghi ngờ gì nữa phải không?

Vì vậy khi chúng ta tạo hàm cập nhật tên đó

and we specify its receiver type

như là con trỏ tới người,

hai thứ này rất hợp nhau phải không?

Giống như đây là con trỏ tới người,

đây là loại máy thu của con trỏ tới người.

Vâng, cả hai kết hợp với nhau một cách hoàn hảo.

Họ xếp hàng một trăm phần trăm.

Bây giờ với ý nghĩ đó,

chúng tôi sẽ thực hiện một chút thay đổi đối với mã của mình

nó sẽ trông hơi lạ một chút,

nhưng nó sẽ dẫn đến

rất ít mã được viết trong thực tế.

Vì vậy điều đầu tiên tôi sẽ làm

là tôi sẽ xóa dòng này

nơi chúng tôi lấy được địa chỉ bộ nhớ của Jim,

và sau đó tôi sẽ thay đổi jimPointer

chỉ đơn giản là jim.

Bây giờ tôi sẽ lưu tập tin.

Tôi sẽ quay lại thiết bị đầu cuối của mình,

và tôi sẽ chạy đi chạy chính đi lần nữa,

và bạn sẽ nhận thấy rằng mã của chúng tôi vẫn đang hoạt động.

Vậy là tôi vẫn còn tên Jimmy ở đây.

Nhưng bây giờ bạn sẽ nhận thấy rằng có

thực sự là sự không phù hợp trong các loại máy thu của chúng tôi.

Vì vậy, ngay tại đây, nếu tôi di chuột qua jim trong Mã VS,

nó nói rất rõ ràng

một trăm phần trăm, không nghi ngờ gì về điều đó,

jim là một biến kiểu người.

Vậy jim có giá trị là một cấu trúc.

Không có địa chỉ bộ nhớ ở đây,

không có con trỏ,

không có gì giống như thế cả,

nhưng bằng cách nào đó chúng ta vẫn có thể

để sử dụng chức năng này

có một loại máy thu hoàn toàn khác,

vì kiểu này là con trỏ tới người, phải không?

Con trỏ tới người.

Đây chỉ là người thôi.

Vì vậy, đây là một chút phím tắt với Go.

Với Go, nếu chúng ta xác định một người nhận

với một loại con trỏ tới bất cứ thứ gì,

giống như con trỏ trống,

bất kỳ loại nào bạn có thể tưởng tượng,

khi chúng tôi cố gắng gọi hàm này

hoặc chúng tôi cố gắng gọi phương thức này ngay tại đây,

Go sẽ cho phép chúng tôi gọi

chức năng này với một con trỏ

hoặc với lõi, giống như kiểu gốc ở đây,

người đó trong trường hợp này.

Về cơ bản, bạn biết không,

chúng ta hãy nhìn vào sơ đồ chết tiệt.

Điều đó sẽ giải thích nó tốt hơn tôi có thể.

Được rồi, đây là mã gốc mà chúng ta vừa có,

đây là thay đổi mà chúng tôi vừa thực hiện

và đây là chức năng mà chúng tôi đang làm việc.

Vì vậy vào thời điểm này,

lần lặp lại số một đã nói,

"Được rồi jimPointer thuộc loại con trỏ tới người".

Và sau đó chúng tôi đã có ống nghe,

đó là con trỏ tới người.

Vậy hai trường hợp ở đây xếp hàng một cách hoàn hảo.

Nhưng Go cho phép chúng tôi đi theo lối tắt này và nói,

"Này, nếu bạn có một biến thì đó chỉ là

loại người nhưng sau đó là người nhận của bạn

là con trỏ tới người, điều đó hoàn toàn ổn".

Chúng tôi sẽ chỉ che đậy sự thật đó cho bạn

và Go sẽ tự động chuyển lượt của bạn

biến kiểu người thành

người gợi ý cho bạn.

Vậy nói cách khác,

đây chỉ là một chút phím tắt

về cơ bản chúng ta sẽ sử dụng

mỗi lần chúng ta sử dụng

một loại máy thu ngay tại đây

loại máy thu của một con trỏ.

Vì vậy, chúng ta không cần phải thực sự dỗ dành

địa chỉ bộ nhớ của Jim ngay tại đây.

Đi chỉ là đi đến loại

hãy chăm sóc nó cho chúng tôi.

Tất nhiên là bây giờ nếu chúng ta quay lại mã của mình ở đây

và chúng tôi đã thay đổi con trỏ thành người,

trở lại với con người,

giờ thì mọi thứ sẽ tan vỡ,

cụ thể, bạn biết đấy, khi chúng tôi sử dụng

con trỏ này ngay tại đây.

Bởi vì bây giờ Go sắp nói,

"Ồ được rồi, con người thuộc loại người.

Không có con trỏ nào ở đây cả".

Và vì vậy nếu chúng ta cố gắng loại bỏ tham chiếu

con trỏ này tới con người

với một ngôi sao ở ngay đây,

bây giờ mã của chúng ta sắp bị hỏng.

Vì vậy, về cơ bản vào cuối ngày,

điều tôi đang cố gắng đạt được ở đây,

chúng tôi có hai lựa chọn.

Chúng ta có thể lấy địa chỉ bộ nhớ từ Jim

và sau đó sử dụng nó làm máy thu ngay tại đây

hoặc chúng ta có thể chỉ sử dụng giá trị đó.

Dù bằng cách nào nó sẽ hoạt động tốt

với một con trỏ tới kiểu của chúng tôi.

Bây giờ một lần nữa,

đây có thể là một trong số đó

những điều bạn đang nói,

"Steven, có gì khác biệt vậy?"

"Sự khác biệt ở đây là gì"?

Vâng một lần nữa,

đây là một trong những thứ mà

bạn sẽ phải viết

một chút mã cho chính mình

và xem một số thứ

trong bài tập trước khi tôi nghĩ

nó thực sự sẽ chìm xuống.

Vì vậy, với ý nghĩ đó,

chúng ta hãy nghỉ ngơi nhanh chóng.

Chúng ta sẽ tiếp tục ở phần tiếp theo

và tôi muốn chỉ ra một điều,

Nhân tiện, đó không phải là một cách chơi chữ,

khi tôi nói điểm,

Tôi muốn chỉ ra một hoặc hai điều nhanh chóng

những điều nhỏ nhặt trong Go thực sự là những vấn đề lớn

xung quanh tất cả những thứ con trỏ này.

Vậy nên hãy nghỉ ngơi nhanh và tôi sẽ gặp bạn sau một phút nữa.