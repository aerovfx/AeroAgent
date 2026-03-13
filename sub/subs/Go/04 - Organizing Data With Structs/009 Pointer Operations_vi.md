# 009 Các thao tác con trỏ vi

---

Trong phần cuối cùng, chúng tôi đã thực hiện một số thay đổi nhỏ đối với cơ sở mã hóa của mình và kết quả là không mong muốn

bất cứ khi nào chúng tôi gọi hàm cập nhật này bằng một chuỗi Jimmy, có vẻ như Jim đã cập nhật thành công.

Vì vậy, bây giờ chúng tôi sẽ chia nhỏ mã này và nói về chính xác những gì chúng tôi vừa làm.

Vì vậy, điều đầu tiên tôi muốn làm là nói một chút về ký tử tử và ngay tại

đây là gì và dấu sao toán tử hoặc dấu hoa thị ở đây là gì.

Vì vậy, hãy nói về những toán tử đó là gì, và điều đó có thể giúp chúng ta làm

quen hơn một chút với những gì thực sự đang làm ở đây.

Vì vậy, trước tiên, chúng ta sẽ nói về dấu và điều đó.

Dấu vết và là một toán tử.

Chúng tôi đặt ký hiệu và sau đó đặt một số biến tên.

Và chính xác đó là những gì chúng tôi tìm thấy trong cơ sở mã hóa của mình, nơi chúng đặt ký hiệu và sau đó là biến.

Jim Rất tiếc, ký hiệu và, Jim.

Bây giờ khi chúng ta làm điều đó, chúng ta đang nói, hãy nhìn vào biến thể này và cấp cho chúng ta quyền truy cập vào địa chỉ

bộ nhớ duy nhất mà biến này đang trỏ tới.

Vì vậy, nói theo cách khác, nếu chúng có ký hiệu và Jim, Jim đang chỉ vào cấu trúc của chúng đang ở trong bộ nhớ và cấu trúc đó

đang tồn tại tại một số cụ thể địa chỉ.

Vì vậy, khi chúng tôi viết Ampersand, Jim, chúng tôi nói, hãy cho tôi quyền truy cập vào địa chỉ bộ nhớ mà cấu trúc này

đang ở.

Và vì vậy, ví dụ, có thể là, 0001, chúng tôi nhận được giá trị đó và sau đó chúng tôi chỉ định nó cho Jim Pointer.

Vì vậy, hiện tại biến Jim Pointer mà chúng tôi giới thiệu vào ứng dụng của chúng tôi không trỏ đến hoặc nó

không phải là một tham chiếu trực tiếp đến cấu trúc.

Thay vào đó, nó là một tham chiếu đến bộ nhớ địa chỉ mà cấu trúc tồn tại.

Nếu bây giờ chúng ta đang lấy giá trị của Jim Pointer, chúng ta có thể sẽ tìm thấy

một số bộ nhớ địa chỉ loại như 0x0 ABCD 123.

Vì vậy, Jim Pointer hiện đang hiển thị trực tiếp vào không gian này trong bộ nhớ.

Bây giờ với suy nghĩ đó, chúng ta hãy nói về các toán tử khác mà chúng ta vừa thấy.

Vì vậy, đó là toán tử ngôi sao.

Vì vậy, bất cứ khi nào chúng tôi sử dụng ngôi sao toán tử, chúng đều đặt dấu sao và sau đó là bộ nhớ địa chỉ hoặc con trỏ.

Bất cứ khi nào chúng tôi làm điều đó, chúng tôi đang nói, hãy lấy địa chỉ này bộ nhớ và cung cấp cho tôi giá trị tồn tại

at địa chỉ bộ nhớ đó.

Vì vậy, bên cạnh chức năng cập nhật tên của chúng tôi ngay tại đây, chúng tôi đã nói con trỏ sao với từng người.

Con trỏ tới người là địa chỉ bộ nhớ mà Jim tồn tại.

Và vì vậy bằng cách nói con trỏ ngôi sao với người, chúng ta đang nói, đây là con trỏ.

Tôi không muốn nhìn vào bộ nhớ địa chỉ nữa.

Thay vào đó, hãy cho tôi quyền truy cập trực tiếp vào bất kỳ thứ gì này hoặc bất kỳ giá trị nào thực sự đang ở đây.

Và làm được điều đó, ngôi sao Jim Pointer trở thành một mẫu người thực sự.

Vì vậy, với hai toán tử đó trong tâm trí và hiểu chính xác những gì chúng làm, bây giờ chúng ta hãy xem qua mã của chúng ta và

chúng tôi có thể xem dữ liệu để tìm ra chính xác điều gì đang xảy ra hay không.

Vì vậy, ngay tại dòng một, trước tiên họ bắt đầu bằng cách lấy biến Jim.

Hãy nhớ rằng Jim là một tham chiếu đến cấu trúc trong bộ nhớ, giá trị thực tế của cấu trúc.

Chúng tôi sử dụng dấu và toán tử.

Khi chúng tôi làm điều đó, chúng tôi biến Ampersand Jim thành một bộ nhớ địa chỉ hoặc một con trỏ và sau đó chúng tôi chỉ định

giá trị đó cho Jim Pointer.

Tiếp theo, chúng tôi gọi Jim Pointer.

Update name.

Bây giờ hãy chú ý và đây thực sự là một thông báo quan trọng về việc chúng tôi đã thay đổi loại máy thu ở đây thành ngôi sao.

Bạn có thể đọc điều này ngay tại đây như một con trỏ chỉ vào một người.

Bây giờ, một điều tôi muốn chỉ ra và điều này thực sự quan trọng để hiểu và đây

có lẽ là một trong những điều khó hiểu nhất về con trỏ và đi là tôi vừa nói với bạn 2 giây trước rằng bất cứ khi nào

dù họ đặt dấu sao và sau đó quay con trỏ thành một giá trị.

Vì vậy, quyền này ở đây đã được chuyển thành một giá trị, phải không?

Giống như tôi vừa nói điều đó 2 giây trước.

Nhưng bây giờ tôi cũng đang nói chuyện với bạn, ngôi sao ngay ở đây đang nói một kiểu con trỏ chỉ vào

một người.

Và vì vậy đây là một sự phân biệt thực sự quan trọng mà tôi muốn dành nhiều thời gian để thực sự thuê nhà.

Vì vậy, có lẽ đây là ý kiến trúc của tôi, một trong những điều khó hiểu nhất về con trỏ là khi chúng ta

nhìn thấy một ngôi sao ở phía trước của một loại, nó có nghĩa là một cái gì đó hoàn toàn khác nên khi chúng ta nhìn thấy một ngôi sao trước

một con trỏ thực tế.

Vì vậy, chúng tôi hãy chia nhỏ cả hai và tìm ra sự khác biệt giữa hai điều này.

Vì vậy, trong máy thu, chúng tôi đã nói rằng con trỏ tới người là một giá trị của kiểu ngôi sao.

Bất cứ khi nào bạn nhìn thấy một ngôi sao và sau đó là bất cứ thứ gì, về cơ bản là bất kỳ từ nào ở nơi mà một loại có thể

cho là có.

Và hãy nhớ rằng, trong một máy thu, chúng tôi luôn đặt giá trị và sau đó là loại của nó.

Vì vậy, bất cứ khi nào bạn nhìn thấy một ngôi sao ở vị trí của một loại, điều đó có nghĩa rằng đây là mô tả của một loại.

Chúng tôi đang tìm kiếm một con trỏ đến một người.

Vì vậy, trong trường hợp này, ngôi sao ở đây thực sự không nên được coi là một toán tử như chúng

ta đã nói trước đây.

Hãy nhớ rằng, chúng tôi vừa nói 2 giây trước khi Star Pointer là một toán tử nói rằng, hãy chọn tôi giá trị

nơi bộ nhớ địa chỉ này đang trỏ tới.

Nhưng khi họ nhìn thấy ngôi sao ở phía trước của một loại thực tế thì đó là mô tả

loại và không có nghĩa là bản cập nhật tên chức năng này chỉ được gọi bằng bộ nhận dạng con trỏ đến một người.

Vì vậy, tôi hy vọng điều này có ý nghĩa khi tôi đang cố gắng làm rõ rằng đây thực sự là một chủ đề khó hiểu

và hy vọng sự phân biệt giữa hai chủ đề này có ý nghĩa.

Vì vậy, đây là điều xác định rõ ràng rằng chúng tôi muốn có một loại con trỏ đến một người.

Đây là một toán tử thực thi con trỏ này và biến nó thành một giá trị thực tế.

Vì vậy, hãy lấy lại mã của chúng tôi và tiếp tục xem qua.

Vì vậy, chúng tôi có bản cập nhật tên chức năng có thể được gọi với bất kỳ bộ con trỏ kiểu nào đến

Mỗi người, chính xác đó là hàm Jim Pointer.

Vì vậy, chúng tôi gọi bản cập nhật tên Jim Pointer này là Jim Pointer ngay tại đây hoặc địa chỉ bộ nhớ này sau đó

được chuyển vào hàm này dưới dạng con trỏ tới người dùng.

Vì vậy, bạn có thể tưởng tượng Jim Pointer và chỉ một người gốc phun ngay bây giờ.

Vì vậy, bên trong hàm chúng ta nói con trỏ dấu sao cho người dùng.

Vì vậy, hãy nhớ dấu sao và sau đó là một con trỏ thực tế có ý nghĩa gì.

Nó nói rằng hãy đưa ra địa chỉ con trỏ này cho người dùng và biến nó thành một thực tế có giá trị.

Vì vậy, dấu ngoặc nhỏ này chặn ngay tại đây, thứ này ngay tại đây sẽ trở thành con người Jim thực

đang ngồi trong ký ức.

Vì vậy, chúng tôi quay lại cấu trúc này ngay tại đây, nó không còn trong bộ nhớ.

Sau đó, chúng tôi tham chiếu thuộc tính tên của nó và chúng tôi cập nhật thuộc tính tên của nó thành Jimmy hoặc

bất kỳ tên mới nào là OC.

Vì vậy, đó là một cuộc dạo chơi số một ở đây.

Và nếu nó khó hiểu, tôi phải nói với bạn, điều đó hoàn toàn là OC Không ai từng học các con trỏ mà không nghe về chúng trước đây

và giống như lần đầu tiên họ được nghe về chúng.

Không ai đã từng hiểu con trỏ ngay từ đầu.

Và nếu bạn có thì xin chúc mừng bạn, tôi mong đợi đó là điều tốt nhất tôi có thể nói.

Vì vậy, điều này là khó hiểu.

Điều đó hoàn toàn ổn định.

Và chúng tôi sẽ có rất nhiều bài tập để thực hiện khai thác tại nhà.

Chính xác những gì đang xảy ra ở đây.

Bây giờ, trước khi chúng tôi tiếp tục, có một số điểm mà tôi thực sự muốn nhấn mạnh.

Được chứ.

Vì vậy, đây là số một.

Trước đó, khi chúng tôi nghĩ về các biến thể của chúng tôi ở đây và mọi thứ đang diễn ra với

cấu trúc đó ngay bây giờ, chúng tôi thực sự đang làm việc với hai loại biến khác nhau.

Một biến chứa con trỏ thứ đến một địa chỉ.

Vì vậy, nó sẽ giống như con trỏ thực tế của chúng tôi, Jim Pointer của chúng tôi ngay tại đây.

Đây là một bộ nhớ địa chỉ.

Và các mặt khác, chúng có các biến tạo ra giá trị thực tế.

Và điều đó sẽ giống như Jim ngay tại đây.

Vì vậy, Jim là một người có giá trị.

Bây giờ chúng ta bắt đầu nghĩ về các địa chỉ và cách chúng liên quan đến các giá trị mà chúng chứa

Bên trong, hãy nhớ rằng đó là lý do tại sao chúng ta đang sử dụng dấu và dấu phẩy toán tử.

Vì vậy, đây là quy tắc.

Đây là quy tắc cần thực thi nếu bạn có địa chỉ.

Vì vậy, nếu bạn có một địa chỉ, bạn có thể biến địa chỉ đó thành một giá trị bằng cách nói dấu sao rồi đến địa chỉ

hoặc con trỏ.

Nếu bạn có một giá trị, bạn có thể biến nó thành một địa chỉ bằng cách viết ký hiệu và giá trị.

Và chính xác đó là những gì chúng tôi thấy trong đoạn mã của mình ngay tại đây.

Ngay tại đây.

Chúng tôi có một giá trị.

Chúng tôi biến nó thành một bộ nhớ địa chỉ hoặc một con trỏ bằng cách viết ký hiệu và.

Jim Và sau đó, đây là cùng một con trỏ chính xác hoặc cùng một địa chỉ chính xác của bộ nhớ và chúng tôi chuyển nó trở lại

thành một giá trị bằng cách viết dấu sao và sau đó là con trỏ.

Vì vậy, đó là một số lượng nhắc nhở lớn.

Và thứ hai lớn của nhắc nhở được hiểu là khác biệt giữa thời điểm chúng ta sử dụng dấu

sao đó trước một loại hoặc trước một bộ nhớ địa chỉ.

Vì vậy, một lần nữa, bất cứ khi nào bạn nhìn thấy ngôi sao ở một vị trí mà thông tin chúng tôi sẽ chỉ định

một loại, điều đó có nghĩa là, này, chúng tôi đang tìm kiếm một loại là con trỏ tới cái này tới một người, một con trỏ tới một người.

Đó là những gì đang hiển thị cho người này.

Vì vậy, trong trường hợp này, ngôi sao thực sự không nên coi là một nhà điều hành.

Chỉ khi chúng ta có một bộ nhớ địa chỉ thực tế hoặc một con trỏ thực tế ngay tại đây

thì toán tử ngôi sao biến nó trở lại thành một giá trị OC Vì vậy, với tất cả những điều đó, giống như số vòng lặp

một con trỏ.

Hy vọng rằng nó không quá tệ vì tôi có rất nhiều điều xấu.

Điều này giống như một bản sửa đổi một trong những con trỏ và thực tế không thể, thực sự có một số trường hợp nguy hiểm

Rủi ro mà chúng tôi thực sự, thực sự, thực sự cần thiết phải lưu ý.

Vì vậy, chúng tôi nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay lại trong phần tiếp theo.

Chúng tôi sẽ thực hiện một chút việc dọn dẹp mã hóa ở đây.

Và tôi muốn nói về một số loại bổ sung nhỏ một hoặc hai, và sau đó chúng sẽ nhanh chóng nói về một

trong những trường hợp lợi thế xung quanh con trỏ và cách chúng được xử lý trong quá trình thực hiện.

Vì vậy, hãy nhanh chóng nghỉ ngơi và chúng tôi sẽ theo dõi trong phần tiếp theo.