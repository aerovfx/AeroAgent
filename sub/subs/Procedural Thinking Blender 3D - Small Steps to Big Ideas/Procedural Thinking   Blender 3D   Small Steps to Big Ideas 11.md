# Máy xay sinh tố tư duy quy trình 3D Những bước nhỏ dẫn đến ý tưởng lớn 11

---

(nhạc sôi động)

Vậy là đủ với hệ thống dây điện,

hãy làm cho mạng nút này thực hiện công việc cho chúng ta.

Chúng tôi sẽ thêm một nút nhóm

tự động tạo ra những quả táo độc đáo

để chúng ta không phải điều chỉnh mọi thứ một cách thủ công.

Hãy bắt đầu.

Bây giờ, điều cuối cùng tôi muốn thêm vào các thông tin đầu vào của nhóm này

trong bảng sửa đổi này là một cách để ngẫu nhiên hóa hình dạng

mỗi lần tôi nhân đôi quả táo này.

Tương tự như cách chúng tôi có phiên bản màu khác

mỗi lần chúng tôi sao chép cái này,

điều gì sẽ xảy ra nếu chúng ta có một tùy chọn, một hộp kiểm sau khi được bật,

mỗi khi chúng ta nhân đôi một quả táo,

nó cho chúng ta một hạt giống ngẫu nhiên của nhiễu hình dạng,

côn và mọi thứ

để mỗi quả táo là duy nhất khi chúng ta nhân bản nó.

Vậy cách chúng tôi chọn ngẫu nhiên màu sắc của quả táo này

đang sử dụng nút thông tin đối tượng, một đầu vào ngẫu nhiên,

Tôi tin rằng chúng tôi đã chèn vào độ bão hòa màu sắc.

Vì vậy, nó đã giúp chúng tôi trộn lẫn giữa hai màu này.

Bây giờ, hãy xem liệu chúng ta có nút thông tin đối tượng không

trong nút hình học.

Có, chúng tôi có nút thông tin đối tượng.

Vì vậy tôi sẽ đi đến phần tiếng ồn hình dạng này

của nút hình học.

Nếu bạn để ý, chúng tôi không có đầu vào ngẫu nhiên

trong nút thông tin đối tượng này.

Đó là một nút khác với những gì chúng ta có trong trình soạn thảo shader.

Vì vậy, chúng ta sẽ phải giải quyết vấn đề này theo cách khác.

Vì vậy, trong kết cấu tiếng ồn này,

Hãy để tôi ngắt kết nối này bây giờ.

Vì vậy, ngay tại đây, tôi cần một giá trị

đó là duy nhất cho mỗi quả táo

để nó tạo ra một biểu mẫu duy nhất cho mỗi bản sao.

Vì vậy, nếu chúng ta tạo nhiều bản sao,

chúng ta có gì độc đáo cho mỗi quả táo?

Đó là vị trí của họ.

Vì vậy chúng ta có thể sử dụng tọa độ vị trí để rút ra bất kỳ tham số nào

và tạo ra những kết quả độc đáo.

Nếu tôi lấy vị trí và đặt giá trị này vào giá trị W,

bây giờ, nếu tôi cố gắng sao chép cái này,

nó sẽ không giúp ích gì

bởi vì trong nút thông tin đối tượng này, chúng ta không có gì cả.

Vì vậy, hãy mang theo một nút tự,

kết nối điều này với đối tượng.

Bây giờ chúng ta hãy thử điều này.

Ngay cả bây giờ nó không hoạt động.

Chúng ta sẽ phải thêm một nút toán học vector

và thay đổi điều này thành chiều dài.

Và bây giờ hãy đặt cái này vào giá trị W.

Bây giờ bạn sẽ chú ý mỗi khi tôi sao chép đối tượng này

và di chuyển nó, kiểu tiếng ồn sẽ thay đổi

dựa trên vị trí.

Về cơ bản nó tính toán độ dài dựa trên vị trí

và sử dụng giá trị đó trong chữ W ngay tại đây.

Nhưng sự khác biệt là không đáng chú ý.

Vì thế bước nhảy rất từ ​​từ.

Vì vậy, tôi có thể phóng đại hiệu ứng này bằng cách sử dụng nút toán học.

Thay đổi điều này để nhân lên.

Hãy xem cách nó hoạt động bây giờ.

Vì vậy, hiệu quả bây giờ rõ ràng hơn nhiều,

nhưng bây giờ tôi không muốn nhiễu này thay đổi trên mỗi pixel,

về mọi thay đổi nhỏ nhất ở vị trí.

Thay vào đó tôi muốn điều này diễn ra nhanh chóng

khi có sự thay đổi đáng kể về khoảng cách.

Vì vậy, nếu tôi nhân đôi nút nhân này,

nút toán học và thay đổi nút này thành snap,

hãy tăng nó lên 1,5 hoặc gì đó.

Tôi sẽ xóa cái này.

Vì thế bây giờ sự thay đổi nhanh chóng hơn nhiều

khi có chuyển động đáng kể.

Vì vậy, tôi đoán 1,5 là ổn.

Ừ, được rồi.

Vì vậy bây giờ cái này ở đây hoạt động linh hoạt,

nó gần như đang thay đổi hình dạng của Apple một cách năng động

dựa trên vị trí.

Vì vậy, rất nhiều nút này đang giúp chúng tôi thực hiện nhiệm vụ đó,

ngẫu nhiên mẫu nhiễu hoặc tham số

cái này được chèn vào dựa trên vị trí.

Bây giờ chúng tôi sẽ mang đến một nút chuyển đổi,

thay đổi điều này từ hình học sang nổi,

kết nối cái này ngay tại đây

và thay đổi kết nối sang đầu vào thứ hai.

Và cái đầu tiên sẽ là cái này,

cái này, một giá trị cố định, không ngẫu nhiên.

Hạt giống tiếng ồn này định hình, đến từ đầu vào của nhóm.

Nếu bạn đến ngay đây, hãy định hình hạt giống tiếng ồn.

Vì vậy, một khi chúng ta thay đổi điều này,

nó sẽ thay đổi hình dáng của Apple,

nhưng khi chúng ta chuyển đổi nó thành bộ ngẫu nhiên động,

nó sẽ thay đổi hình dạng dựa trên vị trí.

Vì vậy, tôi sẽ cắm cái này ngay tại đây.

Bây giờ, nếu tôi di chuyển cái này, hình dạng sẽ không thay đổi

và thay vào đó hình dạng sẽ thay đổi từ đây,

hạt tiếng ồn.

Nhưng nếu tôi chuyển đổi nó,

bây giờ hình dạng sẽ thay đổi dựa trên vị trí

và điều này sẽ không ảnh hưởng đến nó.

Được rồi.

Vì vậy, bây giờ chúng tôi có một công tắc.

Bây giờ, điều cuối cùng tôi muốn làm là

rằng ngay cả khi cái này được bật lên, hiệu ứng này,

Tôi vẫn muốn có quyền truy cập vào cái này.

Thông số này đây

vẫn có thể điều chỉnh tiếng ồn.

Vì vậy, tôi sẽ đưa ra nút toán học,

đặt cái này ở đây

và thay đổi điều này để nhân thêm.

Vì vậy, giá trị này đến từ bảng điều khiển bên cạnh,

từ đầu vào của nhóm,

giá trị này vẫn sẽ hoạt động,

nhưng hiệu ứng bổ sung trên đó

sẽ là hiệu ứng ngẫu nhiên.

Được rồi.

Hãy đặt cái này vào ổ cắm đầu tiên

và số nhân được đặt thành một.

Vì vậy, bây giờ hiệu ứng không hoạt động,

nhưng khi tôi tắt nó đi,

hiệu ứng ngẫu nhiên sẽ diễn ra,

nhưng sau đó chúng ta vẫn có quyền truy cập để định hình hạt giống tiếng ồn

tham số làm việc từ đây.

Vì vậy, chúng tôi đang sử dụng giá trị này trong nút cộng số nhân.

Hệ số nhân được đặt thành một.

Điều đó có nghĩa là hiệu ứng đã hoạt động hoàn toàn

và trong giá trị gia tăng, giá trị bổ sung,

chúng tôi có bộ ngẫu nhiên động dựa trên vị trí này,

mà chúng tôi đã thực hiện ngay tại đây.

Vì vậy, hiệu quả bây giờ là ngược lại.

Khi tôi bật nó lên, nó sẽ được chọn ngẫu nhiên.

Vì vậy, tôi sẽ chỉ kéo cái này sang cái thứ hai.

Bây giờ nó sẽ hoạt động bình thường.

Vì vậy tôi sẽ lấy tất cả các nút này

và nhấn control G và tạo một nhóm.

Nhấn tab.

Bây giờ chúng ta có nhóm nút này.

Thay vì tất cả các nút đó chiếm quá nhiều không gian,

hãy lấy nhóm nút này

và gọi đây là bộ ngẫu nhiên động.

Tôi sẽ cho nó màu sắc sống động

chỉ để dễ dàng nhận biết.

Bây giờ tôi sẽ chọn nhóm nút này,

nhấn tab để nhảy vào và nhập vào nhóm,

Tôi sẽ kéo giá trị chuyển đổi này.

Nhấn tab lần nữa để thoát.

Vì vậy, chúng tôi có quyền truy cập chuyển đổi ngay tại đây.

Tôi sẽ lấy công tắc này và đặt nó vào nút nhóm.

Vâng, vì lý do nào đó nó lại xuất hiện ở đầu danh sách.

Tôi nghĩ đó là do các tấm nền, nhưng không sao cả.

Chúng tôi có công tắc này.

Hãy đổi tên bộ ngẫu nhiên động này

và sau đó chúng ta có thể kéo bộ ngẫu nhiên động này

vào các tính năng bổ sung.

Vì vậy, chúng tôi có bộ ngẫu nhiên động ở đây.

(nhấn bàn phím)

Hãy nhân đôi điều này.

Vâng, nó đang hoạt động.

Nếu tôi tắt tính năng này, nó sẽ ngừng hoạt động.

Bây giờ hãy xem tất cả những gì chúng ta có thể sử dụng nó để làm gì.

Chúng ta có bộ ngẫu nhiên động để xác định nhiễu hình dạng ở đâu?

Hình dạng tiếng ồn.

Bây giờ hãy nhân đôi điều này.

Và ngay tại đây chúng ta có giá trị W của kết cấu Voronoi.

Cái này.

Điều gì sẽ xảy ra nếu chúng ta chèn nó vào giá trị W này?

Bây giờ chúng ta hãy lấy cái công tắc này và đặt cái này

vào bộ ngẫu nhiên động.

Vì vậy, bộ ngẫu nhiên động hiện đang hoạt động trên cả hai thứ này.

Chúng ta cũng có thể sử dụng điều tương tự cho hiệu ứng taper.

Vậy trong phần côn, chúng ta có thang đo côn này,

độ bền côn, được nối ngay tại đây.

Vậy nếu chúng ta lấy cái này và đặt nó ở dạng côn,

điều đang xảy ra là nó sẽ không giúp chúng ta chọn ngẫu nhiên nó

vì giá trị này không giống tham số W đó

trong kết cấu tiếng ồn.

Vì vậy, nó không thực sự mang lại cho chúng ta một kết cấu khác.

Nó không giống như một giá trị hạt giống.

Nó sẽ tăng quy mô lên và xuống

dựa trên vị trí.

Vì vậy, chúng tôi không muốn điều đó.

Vì vậy, thay vì có một giá trị cố định,

đầu tiên hãy để tôi chỉ cho bạn tác dụng của việc này.

Nếu tôi đặt cái này ở đây,

vì vậy nó sẽ tăng giảm kích thước quả táo

dựa trên vị trí.

Vì vậy, sự thay đổi nhỏ nhất về vị trí đang thu nhỏ quả táo này

lên xuống và nó không thực sự chọn một số ngẫu nhiên.

Nó không ngẫu nhiên hóa quy mô.

Vì vậy, đây không phải là những gì chúng tôi muốn.

Chúng ta cần phải tìm ra một cái gì đó khác.

Vì vậy chúng ta cần thay đổi giá trị tỷ lệ này

đến một dãy số mà từ đó chúng ta có thể chọn ngẫu nhiên

bất kỳ số lượng, bất kỳ quy mô.

Thay vào đó, chúng tôi sẽ xác định một phạm vi quy mô

sử dụng một nút giá trị ngẫu nhiên.

Hãy lấy cái này.

Hãy cắt cái này đi.

Vì vậy, hiện tại tỷ lệ của quả táo là âm 0,2 hay gì đó,

về cơ bản côn này.

Vì vậy tôi sẽ sao chép giá trị này ở đây.

Được rồi.

Bây giờ tôi sẽ kéo cái này xuống và chọn một phạm vi,

như mức độ côn nhỏ nhất có thể là bao nhiêu

nhìn bề ngoài thì có vẻ tốt, chừng này.

Vì vậy tôi sẽ sao chép cái này ở đây

và sau đó tôi sẽ chọn một phiên bản có độ côn lớn nhất,

nhiều thế này.

Ý tôi là, điều này có thể chấp nhận được.

Apple có thể hoàn toàn tròn trịa.

Hãy đặt cái này ở đây.

Vâng.

Và sau đó tôi sẽ chèn nút giá trị ngẫu nhiên này vào đây.

Nhưng hiện tại sự ngẫu nhiên này đang diễn ra ở mọi điểm

và chúng tôi không muốn điều đó.

Thay vào đó, chúng tôi sẽ mang một nút chỉ mục

và kéo một nút so sánh ra khỏi điểm bằng này

và đưa cái này vào ID.

Được rồi.

Vì vậy, bây giờ hiệu ứng này đang hoạt động.

Nếu bạn kéo hạt giống,

bạn sẽ có được một biến thể khác của độ côn

mỗi khi bạn kéo cái này.

Vậy là bây giờ chúng ta đã có hạt giống.

Đây là những gì chúng ta sẽ kéo

vào đầu vào nhóm cường độ côn

và ngắt kết nối cái này.

Vậy hãy để tôi dọn dẹp chỗ này một chút.

Và bây giờ trong mạng lưới hạt giống này,

bạn có thể kéo bộ ngẫu nhiên này

và công tắc có thể được kết nối với bộ ngẫu nhiên động.

Vì vậy bây giờ tính năng ngẫu nhiên động đã được bật.

Bây giờ khi tôi sao chép cái này,

nó sẽ mang lại cho chúng ta một độ thuôn khác

cùng với tất cả những kết cấu lạ mắt đang diễn ra ở đây.

Vì vậy, hãy xem nó trông như thế nào trong kết xuất.

Vâng.

Vì vậy, có thể giá trị độ côn tối thiểu có thể hơi cao một chút,

ừ, chừng này.

Được rồi.

Vì vậy, điều này đang hoạt động.

Vì vậy, chúng tôi có một bộ ngẫu nhiên trong mẫu tiếng ồn,

ngẫu nhiên trong phần côn

và ngẫu nhiên hóa các chỗ phình ra và mọi thứ.

Vì vậy chúng ta có thể tiếp tục bổ sung thêm nếu muốn

và ngẫu nhiên hóa hầu hết mọi thứ,

nhưng điều đó có thể là quá nhiều.

Và tôi không nghĩ chúng ta cần điều đó vào lúc này.

Vì vậy ngay bây giờ, khi chúng tôi ngẫu nhiên hóa điều này,

chúng ta thấy sự thay đổi về màu sắc.

Điều gì sẽ xảy ra nếu chúng ta cũng muốn ngẫu nhiên hóa sự thay đổi màu sắc này?

Miếng vá, miếng vá xanh mà chúng tôi đã làm ở đây,

sự thay đổi nhỏ về màu sắc của quả táo,

phát ra từ kết cấu tiếng ồn này

được điều khiển bởi thuộc tính dịch chuyển màu sắc này.

Để ngẫu nhiên hóa điều này, chúng tôi sẽ sao chép bộ ngẫu nhiên này.

Hãy sao chép cái này

và đặt cái này ngay tại đây trước thuộc tính dịch chuyển màu sắc.

Vì vậy bây giờ khi chúng ta tạo bản sao,

bộ ngẫu nhiên cũng đang thay đổi hình thức

nó cũng đang thay đổi vị trí của kết cấu nhiễu này,

đang thay đổi màu sắc của nó

để chúng ta có thể thấy bản vá này ở nhiều nơi khác nhau,

điều này thể hiện rõ hơn nhiều ở táo đỏ và táo sẫm màu.

Vì vậy, dựa trên vị trí, kết cấu này hiện cũng đang thay đổi.

Hiện tại các biến thể đang tạo ra quả táo đỏ,

táo xanh và một số ở giữa các màu.

Vì vậy nếu bạn muốn hạn chế những điều này,

bạn luôn có thể quay lại trình chỉnh sửa shader

và ngay sau nút ngẫu nhiên, chúng ta có một phạm vi bản đồ.

Tôi sẽ tạo một bản sao để sao lưu.

Vì vậy, bạn có thể thắt chặt các giá trị này một chút.

Được rồi, đại loại như thế này,

để ở giữa không quá nhiều.

Chúng ta đang nhìn thấy một số màu đỏ, một ít màu xanh lá cây, điều đó không sao cả.

Vâng, tôi nghĩ điều này ổn.

Vì vậy nếu tôi sao chép cái này bây giờ,

thậm chí bây giờ có rất ít rau xanh.

Vì vậy hãy để tôi cân bằng tỷ lệ này.

Vâng.

Hãy để tôi loại bỏ những thứ này.

Hãy nhân đôi một lần nữa.

Màu xanh lá cây, màu xanh lá cây, màu đỏ, trộn, màu đỏ, màu xanh lá cây,

có thể là một chút màu hơi vàng, cỡ này.

Vâng, những thứ này ổn.

Bây giờ chúng ta hãy loại bỏ những thứ này.

Nên hình dáng là ngẫu nhiên, màu sắc là ngẫu nhiên.

Chúng ta có thể làm một điều nữa.

Chúng ta có thể chọn ngẫu nhiên gốc.

Vì vậy trong phần thân cây,

chúng tôi có một tham số hạt giống khác ngay tại đây.

Vậy nếu tôi chèn bộ ngẫu nhiên này vào,

bây giờ chúng ta cũng sẽ thấy một biến thể trong thân cây.

Về cơ bản hướng của nó sẽ thay đổi

cũng dựa trên vị trí.

Ở độ cao của quả táo,

chúng ta có tham số tỷ lệ này.

Ở đây chúng ta cũng có thể thực hiện ngẫu nhiên,

nhưng vấn đề là không có giá trị hạt giống.

Vì vậy chúng ta sẽ phải coi nó như hình côn.

Tôi sẽ sao chép ba nút này,

đẩy cái này ra khỏi khung này bằng cách xóa khỏi khung,

từ nhấp chuột phải, đặt cái này vào tỷ lệ

và sử dụng hạt giống này theo chiều dọc.

Đặt cái này vào tỉ lệ và như thế này.

Được rồi, bây giờ chúng ta có thể ngẫu nhiên hóa điều này,

chèn cái này vào dây hạt giống.

Bây giờ đối với giá trị tối thiểu và tối đa,

0,2 là mặc định theo chiều dọc mà chúng tôi đang sử dụng.

Vì vậy tôi sẽ sử dụng giá trị nhỏ hơn 0,2 một chút,

0,15 và 0,25 cho chiều cao tối đa.

Vì vậy, chúng ta sẽ thấy những quả táo cao hơn một chút, một vài quả táo nhỏ hơn,

chiều cao tối đa có thể 0,2 là ổn.

Được rồi, thế thôi.

Tôi nghĩ chúng ta đã xong tất cả chuyện này.

Chúng tôi có quyền truy cập nhanh vào mọi thứ

trong bảng sửa đổi nút hình học.

Vì vậy nếu bạn thấy tất cả những điều này quá lộn xộn,

những gì bạn có thể làm là chọn tất cả những thứ này và nhấn Control + H.

Điều này sẽ xảy ra nếu bạn nhấn lại lần nữa,

bất kể ổ cắm không được sử dụng là gì,

những thứ đó sẽ ẩn nếu bạn nhấn Control + H.

Vì thế cách nhìn này trở nên gọn gàng và gọn gàng hơn rất nhiều.

Vì vậy tôi sẽ dành một chút thời gian

và sắp xếp lại tất cả các nút này.

Chỉ là làm cho nó sạch sẽ hơn một chút thôi.

Mặc dù chúng tôi đã làm công việc khá tốt

trong việc giữ mọi thứ ngăn nắp,

giống như chúng ta có một khung bao quanh mọi phần.

Hãy tưởng tượng nếu chúng ta không có tất cả những thứ đó.

Vì vậy việc điều hướng qua tất cả các nút này

sẽ thực sự đau đớn,

nhưng hãy cố gắng sửa chữa mọi thứ trong thùng chứa,

những khung hình này ngay sau khi hoàn thành,

tạo các phần khác nhau, lên kế hoạch bố cục hợp lý

để khi bạn xem lại tập tin của mình,

bạn sẽ không phải phỏng đoán và điều đó sẽ tiết kiệm thời gian.

Bạn cũng có thể tô màu các thứ dựa trên vật liệu

hoặc các bộ phận của đồ vật mà bạn đang tạo ra,

như phần thân có thể có màu nâu, phần táo có thể có màu đỏ.

Và điều đó tùy thuộc vào bạn.

Chỉ cần tùy chỉnh quy trình làm việc theo cách bạn muốn,

theo cách bạn thấy thuận tiện cho mình, thế thôi.

Được rồi, đây là toàn bộ mạng lưới

và chúng ta hãy thử nó.

Hãy xem liệu nó có hoạt động tốt hay không.

Và táo châu Á, táo cắt lát, cắt góc.

Vì vậy, mọi thứ đang hoạt động.

Chỉ là sự kéo dài theo chiều dọc, chiều cao của quả táo.

Vì vậy, hiện tại tính năng kéo dài theo chiều dọc không hoạt động như trước

bởi vì hiện tại chúng tôi đang sử dụng công cụ ngẫu nhiên.

Vì vậy, ở đây cũng vậy, tôi sẽ chỉ mang theo một nút toán học

và nhân thêm

và sử dụng phần kéo dài theo chiều dọc vào giá trị

và cái này trong hiệu ứng bổ trợ.

Vì vậy bây giờ bộ ngẫu nhiên cũng đang hoạt động,

nhưng chúng tôi vẫn có quyền truy cập vào thông số chiều cao này

từ bảng sửa đổi này.

Vì vậy, chúng ta cũng có thể điều chỉnh nó theo cách thủ công

trên hết hiệu ứng hiện có đó.

Được rồi, chúng ta đã hoàn thành toàn bộ tài sản,

nhưng còn một điều cuối cùng cần thêm vào.

Trong chương tiếp theo, chúng tôi sẽ giới thiệu các thiết bị,

cho phép chúng tôi kiểm soát tất cả các thông số này

trực tiếp từ trong khung nhìn

thay vì đào bới bảng sửa đổi này.

Điều này làm cho toàn bộ quá trình trở nên tương tác và thú vị hơn.

Tinh chỉnh mọi thứ trong thời gian thực ngay trong khung nhìn

với mặt số và mũi tên là trải nghiệm tốt hơn nhiều

hơn là cuộn số.

Vì vậy, hãy làm điều đó trong chương tiếp theo và tôi sẽ gặp bạn ở đó.

(nhạc nhẹ nhàng)

(nhạc nhẹ nhàng)