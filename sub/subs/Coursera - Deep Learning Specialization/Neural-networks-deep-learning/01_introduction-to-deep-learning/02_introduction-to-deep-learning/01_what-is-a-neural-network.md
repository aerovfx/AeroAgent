# 01 mạng lưới thần kinh là gì

---

Thuật ngữ Học sâu,

đề cập đến việc đào tạo Mạng lưới thần kinh,

đôi khi Mạng lưới thần kinh rất lớn.

Vậy chính xác thì Mạng nơ-ron là gì?

Trong video này, chúng ta hãy thử đưa ra

cho bạn một số trực giác cơ bản.

Hãy bắt đầu với một

Ví dụ dự đoán giá nhà ở.

Giả sử bạn có một tập dữ liệu có sáu

nhà, để bạn biết kích thước của ngôi nhà

tính bằng feet vuông hoặc mét vuông và bạn

biết giá căn nhà và bạn muốn

để phù hợp với một chức năng để dự đoán giá

của một ngôi nhà theo kích thước của nó.

Vì vậy, nếu bạn quen thuộc với tuyến tính

hồi quy bạn có thể nói, vậy chúng ta hãy

đặt một đường thẳng tới dữ liệu này, vì vậy,

và chúng ta có được một đường thẳng như thế.

Nhưng nói một cách thú vị hơn, bạn có thể

nói, chúng tôi biết rằng giá cả

không bao giờ có thể tiêu cực, phải không?

Vì vậy, thay vì khớp đường thẳng,

mà cuối cùng sẽ trở nên tiêu cực,

hãy uốn cong đường cong ở đây.

Vì vậy, nó chỉ kết thúc bằng 0 ở đây.

Vậy là đường kẻ dày màu xanh này kết thúc

trở thành chức năng của bạn cho

dự đoán giá nhà

như một hàm của kích thước của nó.

Nơi nó bằng 0 ở đây và sau đó có

một đường thẳng phù hợp với bên phải.

Vì vậy, bạn có thể nghĩ về chức năng này

bạn vừa phù hợp với giá nhà ở

như một mạng lưới thần kinh rất đơn giản.

Nó gần như đơn giản nhất

mạng lưới thần kinh có thể.

Hãy để tôi vẽ nó ở đây.

Chúng tôi có đầu vào cho mạng lưới thần kinh

kích thước của một ngôi nhà mà chúng ta gọi là x.

Nó đi vào nút này,

vòng tròn nhỏ này và

sau đó nó đưa ra mức giá mà chúng ta gọi là y.

Vậy vòng tròn nhỏ này, đó là

một nơ-ron đơn lẻ trong mạng lưới thần kinh,

thực hiện chức năng này

mà chúng tôi đã vẽ ở bên trái.

Và tất cả những gì nơ-ron làm là đưa vào

kích thước, tính hàm tuyến tính này,

lấy tối đa bằng 0 và

sau đó đưa ra giá ước tính.

Và nhân tiện, trong mạng lưới thần kinh

văn học, bạn sẽ thấy chức năng này rất nhiều.

Chức năng này đi

đôi khi về 0 và

thì nó sẽ coi như một đường thẳng.

Chức năng này được gọi là ReLU

chức năng đại diện cho

đơn vị tuyến tính được chỉnh lưu.

Vậy là R-E-L-U.

Và

khắc phục chỉ có nghĩa là lấy tối đa 0

đó là lý do tại sao bạn có được một hàm có hình dạng như thế này.

Bạn không cần phải lo lắng

về đơn vị ReLU cho

bây giờ nhưng nó chỉ là thứ gì đó mà bạn

sẽ gặp lại sau trong khóa học này.

Vậy nếu đây là một nơ-ron đơn lẻ,

mạng lưới thần kinh,

thực sự là một mạng lưới thần kinh nhỏ bé,

một mạng lưới thần kinh lớn hơn

sau đó được hình thành bằng cách lấy nhiều

các nơ-ron đơn lẻ và xếp chúng lại với nhau.

Vì vậy, nếu bạn nghĩ về tế bào thần kinh này

giống như một viên gạch Lego duy nhất, sau đó bạn

có được một mạng lưới thần kinh lớn hơn bằng cách xếp chồng

cùng nhiều viên gạch Lego này.

Hãy xem một ví dụ.

Hãy nói rằng thay vì dự đoán

giá của một ngôi nhà chỉ từ kích thước,

bây giờ bạn có các tính năng khác.

Bạn biết những điều khác về ngôi nhà,

chẳng hạn như số lượng phòng ngủ,

mà chúng tôi sẽ viết là "#phòng ngủ",

và bạn có thể nghĩ rằng một trong những điều

điều đó thực sự ảnh hưởng đến giá của

một ngôi nhà có quy mô gia đình, phải không?

Vậy ngôi nhà này có phù hợp với gia đình bạn không?

ba người, hoặc gia đình bốn người, hoặc

gia đình năm người?

Và nó thực sự dựa trên kích thước trong

feet vuông hoặc mét vuông, và

số lượng phòng ngủ

điều đó quyết định có hay không

không một ngôi nhà nào có thể phù hợp với bạn

quy mô gia đình của gia đình.

Và có thể bạn biết mã vùng,

ở các quốc gia khác nhau, nó

gọi là mã bưu điện của một ngôi nhà.

Và mã zip có thể là một tính năng cho bạn biết, khả năng đi bộ?

Vậy khu phố này có dễ đi bộ không?

Nghĩ rằng chỉ cần đi bộ đến cửa hàng tạp hóa?

Đi bộ đến trường?

Bạn có cần lái xe không?

Và một số người rất thích

khu dân cư có thể đi bộ được.

Và sau đó là mã zip cũng như

sự giàu có có thể cho bạn biết, đúng không.

Chắc chắn là ở Hoa Kỳ nhưng

một số nước khác nữa.

Cho bạn biết chất lượng trường học tốt như thế nào.

Vì vậy, mỗi vòng tròn nhỏ này tôi

bản vẽ, có thể là một trong những ReLU đó,

đơn vị tuyến tính được chỉnh lưu hoặc

một số hàm hơi phi tuyến tính khác.

Vì vậy, dựa trên kích thước và

số phòng ngủ,

bạn có thể ước tính quy mô gia đình,

mã zip của họ, dựa trên khả năng đi bộ,

dựa trên mã zip và

sự giàu có có thể ước tính chất lượng trường học.

Và rồi cuối cùng bạn có thể nghĩ tốt về điều đó

cách mọi người quyết định số tiền họ có

sẵn sàng trả tiền cho một ngôi nhà, họ có xem xét

những điều thực sự quan trọng với họ.

Trong trường hợp này quy mô gia đình,

khả năng đi bộ, chất lượng trường học và

giúp bạn dự đoán giá.

Vậy trong ví dụ x là

tất cả bốn đầu vào này.

Và y là giá bạn

đang cố gắng dự đoán.

Và do đó, bằng cách xếp chồng một số

nơ-ron đơn lẻ hoặc các yếu tố dự đoán đơn giản

chúng ta có từ slide trước, bây giờ chúng ta

có mạng lưới thần kinh lớn hơn một chút.

Cách bạn quản lý mạng lưới thần kinh

đó là khi bạn triển khai nó,

bạn chỉ cần cung cấp cho nó đầu vào x và

đầu ra y cho một số

ví dụ trong tập huấn luyện của bạn và

tất cả những thứ này ở giữa,

họ sẽ tự tìm ra.

Vì vậy, những gì bạn thực sự thực hiện là thế này.

Ở đâu, ở đây, bạn có một dây thần kinh

mạng có 4 đầu vào.

Vì vậy, các tính năng đầu vào có thể là kích thước,

số phòng ngủ,

mã zip hoặc mã bưu chính, và

sự giàu có của khu phố.

Và do đó, với những tính năng đầu vào này,

công việc của mạng lưới thần kinh

sẽ dự đoán giá y.

Và cũng lưu ý rằng mỗi vòng tròn này,

chúng được gọi là các đơn vị ẩn trong

mạng lưới thần kinh, mỗi mạng trong số chúng

lấy đầu vào của nó cả bốn tính năng đầu vào.

Vì vậy, ví dụ, thay vì nói điều này

nút đầu tiên đại diện cho quy mô gia đình và

quy mô gia đình chỉ phụ thuộc

về đặc tính X1 và X2.

Thay vào đó, chúng ta sẽ nói,

mạng lưới thần kinh tốt,

bạn quyết định bất cứ điều gì bạn

muốn nút này được.

Và chúng tôi sẽ cung cấp cho bạn tất cả bốn tính năng nhập liệu

để tính toán bất cứ điều gì bạn muốn.

Vì vậy, chúng tôi nói rằng lớp đó

đây là lớp đầu vào và

lớp này ở giữa thần kinh

mạng lưới được kết nối dày đặc.

Bởi vì mọi tính năng đầu vào

được kết nối với mọi người

của những vòng tròn này ở giữa.

Và điều đáng chú ý về thần kinh

mạng là như vậy, được cung cấp đủ dữ liệu về

x và y, đã cho đủ ví dụ huấn luyện

với cả x và y, mạng lưới thần kinh

đặc biệt giỏi trong việc tìm ra

các hàm ánh xạ chính xác từ x đến y.

Vì vậy, đó là một mạng lưới thần kinh cơ bản.

Hóa ra là khi bạn xây dựng

ra mạng lưới thần kinh của riêng bạn,

bạn có thể sẽ thấy chúng hữu ích nhất,

mạnh mẽ nhất

trong khuyến khích học tập có giám sát, nghĩa là

rằng bạn đang cố lấy đầu vào x và

ánh xạ nó tới một số đầu ra y, như chúng ta vừa thấy

trong ví dụ dự đoán giá nhà đất.

Trong video tiếp theo chúng ta hãy điểm qua một số

thêm ví dụ về học tập có giám sát và

một số ví dụ về nơi bạn có thể tìm thấy

mạng cực kỳ hữu ích cho

ứng dụng của bạn nữa.