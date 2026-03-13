# 03 gỡ lỗi trong visual-studio-code

---

Xin chào, đây sẽ là một chương ngắn nơi chúng ta sẽ học cách gỡ lỗi trong Visual

Mã Studio.

Vì vậy, hãy quay lại Visual Studio và trước tiên viết mã giai thừa đơn giản không

hơn 5-6 dòng và sau đó hãy tìm hiểu cách gỡ lỗi nó trong Visual Studio Code.

Được rồi, quay lại Visual Studio Code, đây là cùng một tệp, test.py và đây

trước đó có mã để in hello world, nhưng tôi đã gỡ nó ra để chúng ta có thể viết nó

mã giai thừa từ đầu.

Vì vậy, hãy viết mã giai thừa đơn giản.

Vì vậy, trước tiên, tôi sẽ định nghĩa một hàm gọi là giai thừa và việc này sẽ đòi hỏi một số

đầu vào và sau đó chúng tôi sẽ kiểm tra xem số đầu vào có bằng 0 hay không và nếu đúng như vậy thì

chúng ta sẽ chỉ trả về 1 số khác, nếu không chúng ta sẽ nói, tôi nghĩ chúng ta sẽ trả về số đã nhân

bởi chính hàm đó và đầu vào có giá trị âm 1.

Đó là tất cả những gì chúng ta có và sau khi hoàn thành việc đó, chúng ta sẽ nói in và gọi hàm

và chúng ta sẽ chuyển vào một số nào đó, giả sử là 5, để chúng ta biết rằng nó sẽ in ra 120.

Vì vậy, điều này có một số vấn đề ở đây.

Đầu tiên chúng ta phải quên dấu hai chấm ở đó và mọi thứ khác có vẻ ổn, vì vậy nếu tôi nhìn vào

vấn đề, nó báo là mã thông báo không mong muốn, dòng mới, bạn hiểu rồi, tôi nghĩ là như vậy.

Hãy chạy chương trình này và nó hiển thị 120.

Vậy là nó đã có tác dụng.

Vì vậy, cùng một mã đang hoạt động, không có vấn đề gì ở đó.

Bây giờ chúng ta chỉ cần học cách gỡ lỗi chức năng này.

Vì vậy, chúng ta sẽ thêm các điểm ngắt, giống như khi bạn di chuột dọc theo cạnh này

vùng canvas cụ thể, bạn sẽ thấy rằng bất cứ nơi nào con trỏ chuột của bạn ở đó, chấm màu nâu sẽ xuất hiện ngay

bên dưới đó.

Vì vậy, điều đó ngụ ý rằng bạn có thể thêm một điểm dừng hoặc bạn có thể phá mã tại điểm cụ thể đó

điểm.

Gần như mọi trình biên dịch hiện nay vì đây là Visual Studio nên nó vẫn là một phần của

Visual Studio lớn hơn, nhấn F9 sẽ thêm điểm dừng và nhấn F9 lần nữa, đó là

nút chuyển đổi.

F9 là nút chuyển đổi để thêm điểm dừng và xóa hoặc xóa điểm dừng.

Nhưng tôi sẽ không sử dụng F9 vì điều đó cũng sẽ khiến tôi dừng ghi âm.

Vì vậy, bạn cũng có thể nhấp vào bên cạnh.

Vì vậy, nếu tôi muốn thêm một điểm dừng trong dòng này, nếu n bằng 0, vì vậy nếu người dùng nhập

giai thừa, nếu người dùng nhập n ở đây, số 0 ở đây thay vì năm hoặc bất cứ thứ gì khác, thì

mã này sẽ được thực thi.

Phần mã này sẽ được thực thi phải không?

Vì vậy, nếu tôi muốn xem liệu điều này có thực sự được thực thi hay không, thì tôi có thể thêm số 0 vào đây theo đúng nghĩa đen

và kiểm tra.

Được rồi, nếu tôi nhấn lưu ở đó, bạn cũng có thể nhấn F5 để chạy chương trình và nó báo khi nào

bạn nhấn F5, nó hiện ra và hỏi bạn phải làm gì với nó.

Vì vậy, chúng tôi muốn gỡ lỗi các tệp Python hiện đang hoạt động.

Tôi sẽ chỉ cần nhấp vào đó và bạn thấy đấy, bạn thấy đấy.

Như bạn thấy, nó đang triển khai, ý tôi là nó đang chạy chương trình.

Thế là nó chạy qua hàm rồi đến đây, thực ra nó bắt đầu từ đây.

Nó bắt đầu từ lệnh in và sau đó nó gọi hàm giai thừa và sau đó

nó thấy rằng nó bằng 0 và sau đó điều kiện này được thỏa mãn và sau đó nó nhận ra rằng có

là một điểm dừng.

Hãy dừng lại ở đó và bạn có thể thấy biểu tượng nhỏ xung quanh vòng tròn màu nâu này biểu thị

rằng mã bị phá vỡ ở đó, nhưng nó đã thành công trong việc phá mã ở đó.

Vì vậy, bây giờ chúng tôi có thể kiểm tra theo nghĩa đen những gì bạn muốn làm.

Vì vậy, nếu bạn di chuột qua thứ n ngoài kia, bạn có thể thấy rằng đây bằng không.

Được rồi, nó nói cho bạn biết theo nghĩa đen.

Bây giờ có rất nhiều thứ bạn có thể làm với nó và bạn có thể thấy, cũng thấy điều đó

trong phần này bạn có biến cục bộ hoặc các biến cục bộ.

Bây giờ đây thực sự là một biến cục bộ vì nó được định nghĩa bên trong đối số hàm

và nó cho bạn biết chính xác giá trị hiện tại của nó.

Vì vậy, tôi có thể, đây là những phím khác nhau, đây là những nút khác nhau mà bạn có thể thực hiện

trong quá trình gỡ lỗi nó.

Vì vậy, nếu bạn nói tiếp tục thì nó sẽ được in ra, vì đây là phần cuối

của chương trình.

Nếu phần cuối bằng 0 thì cái này sẽ trả về một và thế là xong.

Vì vậy, nếu tôi nhấn tiếp tục, nó sẽ chỉ in một cái và chương trình sẽ kết thúc.

Vì vậy, nếu tôi muốn bỏ điểm ngắt ở đây và tôi sẽ chỉ nói năm rồi tôi sẽ thêm

thay vào đó hãy đặt điểm dừng ở đây và sau đó tôi sẽ nhấn F5 lần nữa.

Được rồi.

Hoặc bạn cũng có thể nhấp vào phần chạy này và gỡ lỗi Python và sau đó nếu tôi nhấp vào đó, bạn có thể

xem đầu tiên và năm này.

Được rồi.

Và sau đó nếu tôi nhấn F5 hoặc tiếp tục, hoặc bạn cũng có thể bước qua hoặc bạn có thể bước vào,

bạn có thể bước ra ngoài, bạn có thể khởi động lại toàn bộ quá trình gỡ lỗi hoặc bạn có thể đơn giản dừng lại

nhấn shift F5.

Đây là các phím tắt và nút rất chuẩn trên hầu hết các trình biên dịch.

Ít nhất Visual Studio có tất cả những thứ này.

Vì vậy, ngay cả mã Visual Studio cũng có thể đưa tất cả những thứ đó vào IDE của nó.

Vậy bây giờ là năm.

Nếu tôi nhấn F5, nó sẽ tiếp tục và bạn có thể thấy rằng điều này đang thay đổi theo

mọi F5 vì nó lặp lại, phải không?

Vì vậy, nó là một hàm đệ quy.

Vì vậy, nó phải tự gọi mình thêm bốn hoặc năm lần nữa.

Thế là mỗi lần nó gọi là nó hỏng ở đây.

Mỗi khi hàm này được gọi, toàn bộ hàm này sẽ chạy và sau đó nó sẽ xuất hiện ở đây

và tất cả những điều kiện này đều được thỏa mãn và nó bị phá vỡ liên tục cho đến khi

không bằng 0, cho đến khi n khác 0, cho đến khi nó không đến đây, nó sẽ gãy ở đây.

Vì vậy, hãy làm điều này.

Vì vậy, trong khi chúng ta đang ở điểm dừng, trong khi chúng ta có điểm dừng ở đây, khi n thì không

bằng 0, hãy thêm điểm ngắt vào vị trí mà chúng ta đã có trước đó.

Được rồi.

Vì vậy, nếu tôi tiếp tục nhấn F5 và nếu bạn để ý, nếu bạn để ý đến biến số

n ở đây, điều này cũng sẽ tiếp tục cập nhật với mỗi lần nhấn phím F5.

Vậy là hai và một.

Bây giờ còn một điều nữa phải làm trước khi nó vỡ ở đây chứ không phải ở đây.

Và nếu tôi nhấn F5 lần nữa, bạn sẽ làm được.

Thế nên bây giờ nó hỏng ở đây.

Bây giờ nếu tôi nhấn F5 lần nữa, sẽ không có gì xảy ra vì nó không thực sự bằng 0.

Ý tôi là nó là 120.

Vì đó là thứ cuối cùng phải in.

Được rồi.

Thế là xong.

Và tôi tin rằng không còn gì nữa, không phải ở đây, tôi chỉ muốn xóa màn hình ở đây.

Không còn gì để hiển thị nữa và bạn đã có những điểm dừng này và tôi đã cho bạn xem tất cả

các nút ở đó và F5 là những gì bạn làm, bạn biết đấy, gỡ lỗi mã và sử dụng F9 và F10 để

get into a function and get out of a function or simply skip over this whole break point

thứ.

Hoặc bạn cũng có thể sử dụng shift F5 để ngừng gỡ lỗi hoàn toàn.

Vì vậy, không có gì nhiều để nói về việc gỡ lỗi.

Nếu bạn đến từ các ngôn ngữ lập trình khác, bạn có thể đã biết về

nó và đây cũng là cách nó được thực hiện trong mã studio trực quan.

Và nếu bạn đến từ studio trực quan, thì bạn thực sự không cần phải làm vậy, bạn đã không

thậm chí phải xem cái này, cái video đặc biệt này, dù sao thì bạn cũng có thể bỏ qua nó.

Thế là xong.

Và trong chương tiếp theo, chúng ta sẽ bắt đầu cài đặt Django.