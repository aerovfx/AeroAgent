# 6 -Xây dựng Trình ghi nhật ký với Decorator.en US

---

Có nhiều trường hợp sử dụng khác nhau

của những người trang trí, và thành thật mà nói, bạn

thực sự tìm hiểu về các trang trí

khi bạn sử dụng chúng nhiều hơn ở Django.

Bạn sẽ sử dụng rất nhiều trong số chúng

trong các thư viện như fastapi.

Thực ra bạn sẽ

sử dụng rất nhiều trong số họ.

Nhưng có một số đồ trang trí nhất định

mà bạn muốn thực hiện chúng trên

sở hữu và đó là cách bạn học chúng.

Vì vậy trong video này chúng ta sẽ đi

để xây dựng một trang trí ghi nhật ký đơn giản.

Đó là một bài tập thú vị.

Bạn, sẽ hoàn toàn thích điều này.

Hãy để tôi chia sẻ màn hình với bạn.

Vậy hãy để tôi đưa bạn trực tiếp

ở phần mã.

Chúng ta không cần bất kỳ lý thuyết nào cho việc này.

Hãy gọi cái này là 02.

Cái này sẽ là

trang trí ghi nhật ký py.

Tất nhiên rồi.

Vậy trình trang trí ghi nhật ký hoạt động như thế nào?

Nó thực sự siêu đơn giản.

Những bước cơ bản đầu tiên

sẽ luôn như cũ.

Vì thế chúng ta sẽ luôn tiếp tục và nói

từ, các công cụ chức năng, bắt đầu nào

về phía trước và nhập các kết thúc tốt đẹp.

Lẽ ra phải như vậy, ồ, tệ quá.

Nó không nên như vậy

nhập khẩu, nên có nguồn gốc từ.

Được rồi, đủ tốt.

Bây giờ hãy nói rằng chúng tôi muốn

gọi cái này là logactvt.

Đó là phần đầu tiên của nó.

Và chúng tôi sẽ coi việc nhập là

một hàm, hãy gọi nó là func.

Hãy thoải mái gọi nó là bất cứ điều gì khác.

Và công việc đầu tiên là đảm nhận việc này

kết thúc tốt đẹp và thực hiện chức năng này để

chúng tôi có tất cả các giá trị được bảo tồn.

Sau đó, chúng tôi xác định hàm bao bọc của mình.

Nó thực sự không cần phải được gọi

làm trình bao bọc, nhưng trình bao bọc có ý nghĩa.

Vậy là chúng ta đã có giấy gói.

Bây giờ đây là phần thú vị.

Chức năng này cũng có thể

chấp nhận một số lý lẽ

hoặc các tham số trong trường hợp đó.

Vì vậy có thể có tranh luận, hoặc

có thể có giá trị chính

đối số hoặc đối số từ khóa.

Tôi không biết cái nào sắp xuất hiện.

Vì vậy, trong trường hợp đó, những gì bạn làm là

bạn lấy cái bọc và bạn

chỉ cần tiếp tục và nói, này,

sao cũng được, tôi không biết

số lượng của nó, bất kể

args đang đến, tôi sẽ

vui vẻ chấp nhận điều đó.

Tôi cũng sẽ tiếp tục và chấp nhận

tất cả các từ khóa tổ chức

điều đó cũng đang đến.

Tôi cũng sẽ lấy chúng.

Và sau đó tôi sẽ đi

tiến lên và xử tử bạn.

tôi sẽ trở lại

một số thứ thú vị nữa.

Nhưng chức năng này sẽ thực thi

và sẽ trả lại cho bạn kết quả.

Vậy nên tôi sẽ tiếp tục và nói,

này, chức năng, chỉ cần thực hiện điều đó.

Và cũng hãy chắc chắn rằng bạn không quên

để lấy thông số của bạn.

Vì vậy tôi sẽ tiếp tục

và nói lập luận như thế.

Và tôi cũng sẽ đi tiếp

và nói hãy lấy từ khóa của bạn.

Thế đấy.

Tất cả đều tốt.

Và cuối cùng chúng ta tiếp tục

và nói trả lại kết quả.

Và đây là kết quả chúng tôi đạt được ở đây.

Và chúng ta cũng tiếp tục nhé

và đừng lo lắng, tôi sẽ chỉ cho bạn

bộ phận làm việc cũng vậy.

Nhưng đây không phải là tất cả

chúng tôi đã làm điều này

Công việc thực sự đã hoàn thành.

Bạn đã thấy từ khóa như thế nào

lập luận có thể được thực hiện bởi vì ở đây

bạn đang thực hiện toàn bộ chức năng

cùng với mọi chi tiết đó

xuất hiện ở đây trong trình bao bọc.

Bất kể giá trị nào đang được thông qua

trên thực tế có thể được nhập lên đây.

Bởi vì chức năng này thực sự

có liên kết trực tiếp.

Và khi bạn gọi hàm

bạn đang ở cuối dòng

truyền những giá trị này vào đây.

Quá đơn giản, siêu dễ dàng.

Nhưng điều duy nhất mà chúng ta chưa

xong là chúng ta chưa nói cái nào

chức năng đang gọi và cái nào

chức năng đã gọi xong.

Vì vậy, ngay trước khi nó gọi, hãy thêm

một tuyên bố in và bản in

câu lệnh sẽ là một công cụ định dạng

chuỗi sẽ nói đang gọi.

Và sau đó chúng ta sẽ sử dụng tên hàm.

Vậy tên chức năng của chúng tôi là gì?

Siêu dễ dàng.

Chúng ta chỉ có thể gọi đây là func

dấu gạch dưới, tên gạch dưới,

gạch dưới, gạch dưới hoặc

trong ngắn hạn.

Vì vậy, chức năng này, bất kể là gì

ở đó, nó thực sự xuất hiện.

Chúng tôi chỉ đơn giản gọi như vậy.

Hãy tiếp tục và nói lần này

cái này sẽ được hoàn thành.

Và thư viện của chúng tôi là

thực sự thú vị.

Vì vậy, nó thực sự bao gồm một số.

Đánh dấu cũng vậy, không cào.

Thế đấy.

Vì vậy, nó thực sự sử dụng một đánh dấu

này, gọi xong rồi

chức năng và một khi nó

cuộc gọi hãy sử dụng một số khác.

Vì vậy, cái này có vẻ tốt.

Vậy thực ra tên lửa đang kêu gọi

ít nhất làm cho nó thú vị.

Vậy chúng ta sẽ sử dụng như thế nào

cái này, cái kia thú vị.

Bạn chỉ cần tiếp tục

và nói logactivity.

Đó là nó.

Bây giờ bạn có thể xác định hàm.

Hãy nói rằng chức năng của chúng tôi là

pha chai.

Bạn nghĩ chúng tôi sẽ đi

rời khỏi chai?

Không, hoàn toàn không.

Và chúng tôi chỉ đơn giản là tiếp tục và vượt qua

trên bất kỳ loại nào chúng tôi đang nhận được.

Có lẽ chúng ta có thể tranh luận nhiều hơn.

Không có vấn đề gì ở đó.

Tôi sẽ tiếp tục và in

với một định dạng

tuyên bố nói rằng sản xuất bia.

Đáng lẽ phải viết chính xác.

Sản xuất bia.

Và sau đó bất kể loại nào,

bạn cho tôi chai.

Được rồi, đủ tốt.

Và đừng quên

gọi cái này là brew chai.

Và chúng ta sẽ gọi masala chai.

Được rồi, khá thú vị.

Và hy vọng bạn đã học được điều gì đó

về từ khóa này.

Điều này ban đầu có chút khó xử,

nhưng cuối cùng bạn sẽ có thói quen

rằng đây là cách tôi viết nó.

Hãy tiếp tục và chạy cái này.

Đây sẽ là Python 3, chúng tôi sẽ

đang sử dụng 02 và thế là xong.

Vì vậy hãy chú ý ở đây bất kỳ chức năng nào bạn

chuyển sang cái này với

bất kể kiểu dữ liệu thực sự là gì

hãy tiếp tục và làm việc với điều đó.

Vì vậy hãy chú ý ở đây nó gọi là brewchai

và chúng tôi đã thiết kế một

đăng nhập khá tùy chỉnh cho chúng tôi.

Bây giờ lợi thế của việc này nếu

Tôi thay đổi cái này nhé

nói thay vì loại tôi

cũng cứ nói sữa đi.

Giá trị mặc định sẽ là

một chuỗi đơn giản nói không

và tôi có thể truyền đạt nhiều hơn

giá trị của nó pha chai và

tình trạng sữa và sau đó chúng ta đi

phía trước và chỉ cần in ra

sữa đây.

Vì vậy, hãy chú ý ở đây chúng tôi đã thay đổi

hoạt động mà không phải lo lắng về tôi

không thực sự quan tâm đến giấy gói của tôi là gì

có, tôi chỉ tập trung vào việc xây dựng

tự hoạt động và chúng tôi chỉ đơn giản là

bây giờ chấp nhận nhiều tham số hơn ngay cả

đối số từ khóa Khá

thú vị phải không?

Điều này thực sự rất vui

và đây là cách nói chung bạn

xây dựng các logger trong trang trí.

Hy vọng bạn thích điều này.

Hãy đánh giá chúng tôi và hãy nắm bắt

lên trong video tiếp theo.