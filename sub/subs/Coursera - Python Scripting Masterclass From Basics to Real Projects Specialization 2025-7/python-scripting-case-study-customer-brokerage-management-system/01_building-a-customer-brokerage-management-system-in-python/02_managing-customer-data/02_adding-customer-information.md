# 02 thêm-thông tin khách hàng

---

Vì vậy, trong bước này, chúng ta sẽ xem cách thêm thông tin khách hàng.

Được rồi.

Thế là ở đây vừa viết thêm khách hàng xong mình sẽ bỏ cái này đi cho đúng

bây giờ.

Bây giờ, điều chúng ta cần ở đây là chúng ta cần lấy thông tin đầu vào.

Vì vậy, giả sử tôi đang lấy tên khách hàng bằng đầu vào, chúng ta cần yêu cầu nhập khách hàng

tên.

Sau đó, chúng tôi cần một số liên lạc.

Vì vậy, giả sử số liên lạc bằng đầu vào, hãy nhập số liên lạc.

Sau đó loại phẳng.

Vì vậy, loại phẳng bằng với đầu vào, trong đó tôi sẽ chỉ nói rằng loại phẳng, giả sử, nhập

loại phẳng trong BHK, nghĩa là bằng số, chẳng hạn như 1BHK, 2BHK, 3BHK hoặc 4BHK.

Sau đó số tiền bằng đầu vào, nhập số tiền.

Vậy bây giờ chúng ta đã có bốn đầu vào này, phải không?

Tên khách hàng, số điện thoại liên lạc, loại căn hộ và số tiền.

Vì vậy, đây là bốn điều chúng tôi cần lấy từ người dùng và sau điều này,

chúng ta cần lưu trữ nó trong đối tượng, phải không?

Vì vậy, tôi cũng sẽ tạo một danh sách.

Vì vậy, giả sử danh sách khách hàng CUST bằng với điều này.

Vậy là chúng ta có tên danh sách là danh sách khách hàng phải không?

Danh sách khách hàng này sẽ lưu trữ rất nhiều dữ liệu của khách hàng.

Vì vậy, điều chúng ta cần làm ở đây là, để lưu trữ dữ liệu, điều đầu tiên,

chúng ta cần kiểm tra số tiền thành gấp đôi hoặc có thể nổi, bất kỳ loại dữ liệu nào.

Vì chúng tôi đang lấy dữ liệu này thành một số float nên chúng tôi có thể tính toán số tiền môi giới

và loại phẳng này cũng phải ở định dạng số nguyên.

Vì dựa vào điều này, chúng ta sẽ biết nó nên đi theo điều kiện nào, đúng không?

Vì vậy, hai điều này, bạn có thể bỏ qua số liên lạc ngay bây giờ, có thể trong thời gian xác thực,

chúng ta có thể thay đổi nó thành số nguyên nhưng hiện tại, chúng ta sẽ chỉ giữ nó dưới dạng chuỗi.

Loại phẳng là số nguyên và số lượng là float.

Vì vậy, điều chúng ta cần làm ở đây là, để có được số tiền môi giới, tôi sẽ nói nếu

loại phẳng bằng 1 tức là loại BHK phải không?

Vì vậy, tại thời điểm đó, số tiền môi giới của chúng tôi sẽ là hoặc có thể số tiền môi giới sẽ là số tiền,

bất kể số tiền ở đó là bao nhiêu.

Bây giờ, hãy xem xét một ví dụ, nếu tôi muốn nhận được 10 phần trăm, tôi sẽ mở một máy tính

ngay bây giờ.

Giả sử, nếu tôi bán một căn hộ trị giá 2 vạn và tôi muốn tìm 10 phần trăm, vậy thành 10

và nếu tôi đưa ra dấu phần trăm, nó sẽ cho tôi 0,1, phải không?

Vậy nó bằng 20.000 phải không?

Vì vậy, hãy xem xét một ví dụ ở đây cũng vậy, số tiền sẽ được nhân với 7 phần trăm

nhưng nếu tôi lấy tỷ lệ phần trăm ở đây, tôi sẽ giả định điều gì mà bạn không thể

lấy phần trăm, phải không?

Vì vậy, nếu tôi muốn lấy tỷ lệ phần trăm, có thể, giả sử, tôi sẽ lại mở máy tính,

có lẽ là số tiền hai vạn, trong đó tôi muốn lấy 10, nên nhân với 10 chia

bằng 100.

Tuy nhiên, tôi vẫn nhận được kết quả, vì vậy khi tôi lấy số bảy này sẽ chia cho 100, vì vậy tôi sẽ

nhận số tiền của tôi ngay bây giờ, số tiền môi giới từ đây, đó là 7 phần trăm, phải không?

Nhưng nếu tức là loại phẳng bằng 2BHK thì số tiền môi giới sẽ là

bằng số tiền thành 10 chia cho 100, vì vậy nó sẽ là 10 phần trăm số tiền môi giới.

Và nếu loại phẳng bằng 3 nghĩa là nếu nó về thứ 3 thì nhà môi giới

số tiền sẽ là 12 chia cho 100 và nếu, loại phẳng bằng 4, tại

lúc đó số tiền môi giới bằng số tiền là 15 chia cho 100.

Vì vậy, đây đều là loại căn hộ của chúng tôi và nhờ đó, tôi sẽ nhận được số tiền môi giới của mình, phải không?

Vậy bây giờ điều chúng ta cần làm là chúng ta đã có danh sách khách hàng phải không?

Và để thêm phần này, chúng tôi sẽ chỉ gọi danh sách khách hàng của mình là dấu chấm nối thêm và trong phần nối thêm này

method, I will be creating object of customer, that's the customer and we will store all

dữ liệu, tức là tên khách hàng, số điện thoại liên hệ, sau đó chúng ta có kiểu phẳng và sau đó chúng ta

có số tiền và sau đó chúng tôi có số tiền môi giới.

Vì vậy, đây là năm điều chúng ta cần thêm vào danh sách và sau đó, chúng ta sẽ

chỉ cần nhắn là in ra, khách hàng đã thêm thành công rồi phải không?

Vì vậy, giả sử, tôi sẽ thử chạy mã này trước và thử thêm một mã, tôi sẽ nhận được khách hàng

tên, giả sử, tên khách hàng là Tracy, số liên lạc của khách hàng là thế này, giả sử,

khách hàng Tracy đang mua căn hộ 2BHK và số tiền là 2 vạn.

Bây giờ tôi có tùy chọn khi khách hàng được thêm thành công, được chứ?

Tôi sẽ không in được dữ liệu này phải không?

Bởi vì tôi vừa mới nói ở đây, đã lấy bao nhiêu này rồi.

Bây giờ tôi sẽ chỉ làm một việc, hiện tại tôi sẽ chỉ in danh sách CUST, tôi sẽ chỉ in

Danh sách CUST sau này, được chứ?

Vì vậy, chỉ để cho bạn biết liệu việc thêm dữ liệu này có khả thi hay không, Tracy, 9876543210,

có thể căn hộ là 2BHK, số tiền và bạn có thể thấy, tôi đang nhận được đối tượng khách hàng chính.

Tại sao tôi nhận được một đối tượng khách hàng?

Vì hiện tại mình vừa in ra biến có đối tượng.

Vì vậy, điều tôi phải làm ở đây là, danh sách khách hàng chấm, tôi phải gọi đối tượng đó, tôi phải

tạo một đối tượng cho nó.

Vì vậy, việc này chúng ta sẽ thực hiện một phần sau.

Điều đó có nghĩa là ngay bây giờ chúng ta có thể giả định rằng khách hàng của chúng ta đang thêm vào đây

thành công rồi phải không?

Vì vậy, đây là điều chúng ta cần làm để thêm khách hàng.