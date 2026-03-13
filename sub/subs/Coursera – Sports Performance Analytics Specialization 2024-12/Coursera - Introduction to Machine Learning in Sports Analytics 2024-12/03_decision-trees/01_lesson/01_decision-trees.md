# 01 cây quyết định

---

Cây quyết định là sơ đồ

của các quy tắc và họ

mô tả cách chúng tôi

phân chia dữ liệu thành các lớp

đưa ra một số tính năng.

Điều tốt đẹp về

cây quyết định

là họ rất

có thể xem xét nội tâm.

Chúng đã được sử dụng khá nhiều trong

tất cả các lĩnh vực khi nó đến

đến học máy.

Với phân tích thể thao

họ đặc biệt tốt bụng

bởi vì chúng dễ dàng

hiểu được bởi những người không phải là chuyên gia,

nên huấn luyện viên, cầu thủ,

giám đốc điều hành, và những người khác

các thành viên trong nhóm của bạn.

Bây giờ, cây quyết định thực sự là

một kỹ thuật rất cũ

trong Học máy,

một trong những

kỹ thuật sớm nhất.

Có rất nhiều thứ khác nhau

các thuật toán để lựa chọn.

ID3 là một trong những cái đầu tiên.

C4.5 là cái mà tôi đã

được sử dụng rất nhiều trong suốt

cuộc sống của tôi khi còn là sinh viên tốt nghiệp

và giảng viên và CART.

Việc phân loại và

cây hồi quy là

cây quyết định chính

thuật toán hiện được sử dụng trong

cả sklearn và

[không nghe được] Bây giờ,

ở mức độ cao, bạn đọc

cây quyết định

bắt đầu từ gốc,

đó là đỉnh của

cây và đi xuống.

Mỗi chi nhánh, vì vậy mỗi

phân chia là nhị phân và

nó dựa trên một số nhất định

tính năng và một số giá trị.

Rồi phần dưới của cây,

chúng được gọi là

lá và những thứ này

là các lớp phân loại của bạn.

Bây giờ cây lớn nhanh

và có rất nhiều cách để

hạn chế sự phát triển của chúng và

cây lớn có xu hướng

quá phù hợp với dữ liệu.

Điều này thực sự dễ dàng hơn nhiều

để giải thích bằng dữ liệu,

đặc biệt nếu bạn

không biết gì cả

về cây như một cấu trúc dữ liệu.

Thay vì đưa

bạn có cả đống

slide để nói về những điều này,

Tôi muốn nhảy thẳng

vào sổ ghi chép

tuần này và đã giải quyết

cây quyết định ở đó.

Chúng ta hãy quay trở lại

dữ liệu quảng cáo chiêu hàng mà chúng tôi

được sử dụng trước đây cho SVM,

nó thực sự tốt

dữ liệu thực sự để

cũng nói về cây cối.

Bạn sẽ thấy tôi chỉ

sẽ mang lại tất cả

hàng nhập khẩu mà chúng tôi

được sử dụng trước đó.

Tôi sẽ đọc vào

tập tin dữ liệu từ

một tập tin zip vào một

DataFrame và làm việc trên

hình dung điều này để xem xét

tốc độ hiệu quả đó so với

tốc độ quay phát hành.

Đó là quan điểm của chúng tôi

đám mây trông như thế nào

Hãy nhớ rằng, đây thực sự là

nhiều loại sân khác nhau.

Tôi muốn xem qua một số

sự chồng chéo giữa

những cú ném đó.

Tôi đang cố gắng xây dựng trên những gì chúng tôi

đã làm lần trước và tôi muốn

mang Matplotlib vào

không gian màu ở đây.

Tôi sẽ tạo ra

một danh sách các màu sắc.

Sau đó ở dòng này ở dưới đây,

Thực ra tôi định giao

mỗi người một màu sắc

một trong những sân.

Điều đó sẽ trở thành một chút

rõ ràng hơn một chút ở đây.

Ở đó chúng ta thấy liên quan đến,

và hãy nhớ đó là

luôn luôn với sự tôn trọng

đến những tính năng mà

chúng tôi đang xem xét

Trong trường hợp này, vì chúng ta có thể

chỉ thực sự nhìn thấy cốt truyện 2D,

chúng tôi đang xem xét tốc độ hiệu quả

trong tốc độ quay phát hành,

nhưng chúng tôi đang xem làm thế nào

các cao độ khác nhau là

phân loại theo màu sắc và

chúng được phân phối như thế nào.

Bạn có thể thấy điều đó nếu

chúng tôi muốn nhìn

giữa màu xanh lá cây và

màu xanh nhạt hoặc

màu tím và màu cam

rằng chúng ta sẽ có thể

tách các lớp đó

khá dễ dàng.

Rằng có rất nhiều

lộn xộn hơn

khi chúng ta bắt đầu

hãy xem xét lớp này,

bất kể màu xanh là gì.

Một số trong số đó

danh mục khá đẹp

khác biệt và một số không quá nhiều.

Bây giờ chúng ta hãy quay trở lại với

hai cú ném ban đầu,

bóng nhanh và thay đổi.

Chúng ta sẽ kéo

chúng ra như loại quảng cáo chiêu hàng của chúng tôi.

Sau đó chúng ta sẽ xem xét

chỉ hai cái đó thôi

nốt nhạc. Bắt đầu nào.

Chúng ta có thể thấy rằng có

một số sự trùng lặp thú vị trong

phần trung tâm của

hình ảnh giữa hai người,

những quả bóng nhanh và những thay đổi

có sự khác biệt ở đâu

trong phân loại.

Vì mục đích giảng dạy,

Tôi thực sự muốn phóng to

vùng dữ liệu đó bởi vì nó

sẽ thú vị hơn

chỉ cho bạn cách

cây quyết định hoạt động.

Tôi đã chơi đùa với

dữ liệu này một chút.

Đó là một chút

bịa đặt bởi vì tôi

anh đào chọn dữ liệu của tôi ở đây

để cho bạn thấy một vài điều,

nhưng hãy giới hạn tốc độ của chúng ta

giữa 85 và 90

dặm một giờ.

Tôi sẽ chỉ lấy

nghìn cú ném đầu tiên

đó là trong không gian đó.

Bây giờ, hãy nhìn này

khu vực trong giây lát.

Chúng tôi chỉ đang xem xét

hai tính năng.

Tốc độ hiệu dụng của

sân và

giải phóng tốc độ quay.

Bóng nhanh của chúng tôi có màu đỏ và

thay đổi có màu vàng.

Cây quyết định phải quyết định

trên một phân chia nhị phân để thực hiện.

Một quy tắc cắt giảm

tốc độ quay phát hành ở đâu đó

hoặc hiệu quả

tốc độ ở đâu đó.

Bây giờ nếu bạn đang đi

để phân chia không gian này,

nếu bạn định

vẽ một đường thẳng

theo chiều ngang hoặc chiều dọc,

đó là hai duy nhất của bạn

tùy chọn trên biểu đồ này.

Bạn sẽ vẽ nó ở đâu?

Được rồi. Con đường

thuật toán CART hoạt động

đó là nó sẽ

tìm cách tách biệt

tập dữ liệu vào

thực tế là hai tập dữ liệu nhỏ hơn,

mỗi cái đó ở đâu

tập dữ liệu nhỏ hơn là thuần túy.

Điều này có nghĩa là đồng nhất

với sự tôn trọng

đến các lớp mà

nó có trong đó.

Nó sẽ cố gắng giữ những thứ đó

tinh khiết đối với kích thước của chúng.

Thuật toán cây sẽ

hãy xem xét hai tính năng của chúng tôi và

cố gắng phân đoạn chúng

dựa trên biện pháp này.

Đây thực sự là

rất khó để làm cho

tập dữ liệu lớn, vì vậy thay vào đó,

phương pháp này nhằm mục đích ước tính

tạp chất thay vì cố gắng

để làm điều đó một cách hoàn hảo.

Bây giờ, chúng tôi chỉ

xem xét một tính năng

bởi vì đây thực sự là

một quá trình đệ quy.

Đối với mỗi

tập dữ liệu nhỏ hơn,

chúng ta sẽ chỉ chạy

lại thuật toán,

chia chúng thành

hai hoặc nhiều tập dữ liệu.

Chúng ta sẽ dừng lại khi một trong hai

tất cả dữ liệu chúng tôi

đã rời khỏi nút

là của một lớp duy nhất,

ví dụ: bóng nhanh hoặc cho đến khi

một số ngưỡng khác

đã bị đánh.

Điều tuyệt vời là chúng tôi

chỉ có thể tận dụng

tất cả kiến thức của chúng ta

về SKLearn.

Chúng ta thực sự không cần phải

làm khác nhiều so với chúng tôi

đã làm trong SVM để bắt đầu

xây dựng các mô hình này.

Chúng ta sẽ tạo X, tập hợp của chúng ta ở đây

các trường hợp đào tạo

hoặc các tính năng của chúng tôi,

df nhỏ, hiệu quả

tốc độ và tốc độ phát hành.

Sau đó chiếc mũ y của chúng ta sẽ biến mất

trở thành kiểu quảng cáo chiêu hàng của chúng tôi.

Sau đó chúng ta phải biến cái này

thành một con số để nó

làm việc với phương pháp mũ

việc đó đang được thực hiện ở đây.

Sau đó chúng ta chỉ cần kéo vào

phân loại cây quyết định

ở đây thay vì SVC.

Ở đây tôi đang sử dụng hai

các thông số khác nhau,

độ sâu tối đa, tôi

đặt nó thành một,

và tất nhiên là tôi đang thiết lập

biến trạng thái ngẫu nhiên đó

một lần nữa để bạn

nên có thể

xem những gì tôi có thể thấy.

Sau đó, tôi muốn tận dụng

Mật mã tuyệt vời của Sebastian,

một lần nữa để xem

vùng quyết định

để chúng ta có thể hình dung được nó.

Chúng ta có thể thấy rằng cây

quyết định chia tay bằng cách sử dụng

tốc độ hiệu quả tại

khoảng 87,5 dặm một giờ.

Chúng ta có thể thấy rằng

độ chính xác ở đầu

biểu đồ này chỉ là 92 phần trăm.

Điều này gần với những gì bạn

lẽ ra đã có thể làm được như vậy

như chia tách dữ liệu?

Bất chấp điều đó,

hình tam giác màu cam trên

bên trái và

hình vuông màu xanh hướng về phía

phía trên đề nghị chúng tôi

có thể đã làm được một chút

tốt hơn nếu chúng ta tái diễn

sâu hơn một chút.

Hãy nhớ rằng

chúng ta sẽ xem xét

mỗi bên của cái này

cây riêng lẻ.

Chúng tôi thực sự có thêm hai

sự chia tách mà chúng ta có thể làm.

Một cho phía bên trái

dưới 87,5 dặm một giờ,

và một cho phía bên tay phải.

Những sự phân chia này

hoàn toàn độc lập,

vì vậy chúng ta có thể chọn hoàn toàn

số khác nhau.

Trên thực tế, trên một trong số chúng,

chúng ta có thể chọn

trục dưới nếu

chúng tôi muốn tiếp tục

chia cắt ở đó,

và mặt khác, chúng tôi

có thể chọn trục y.

Tạm dừng video một lát.

Bạn sẽ chia tay ở đâu

phía bên trái trong

không gian xanh và ở đâu

bạn có muốn chia tay không

phía bên phải

trong không gian màu cam?

Để làm điều đó ở đây,

chúng tôi chỉ tăng

tham số độ sâu tối đa của chúng tôi là hai

và sau đó chúng tôi điều chỉnh dữ liệu

một lần nữa và chúng tôi chạy

âm mưu nữa.

Tuyệt vời. Điều đầu tiên

cần chú ý là

độ chính xác của chúng tôi tăng lên một chút.

Bây giờ chúng tôi đang ở mức 96%.

Chúng ta thấy rằng cái cây đã tách ra

về tính năng thứ hai,

tốc độ quay phát hành của chúng tôi và

thực sự đã làm điều đó cho

cả bên phải và

các cây con bên trái.

Nhưng điều này đã xảy ra với

các giá trị khác nhau,

khoảng 2.250 cho

phía bên trái

và 2.500 cho

bên tay phải.

Bây giờ chúng ta có bốn lá

các nút trong cây của chúng tôi.

Nhưng những quy định đó là gì

nó thực sự được tạo ra?

Chúng ta thấy điều này như thế nào

ranh giới đã thay đổi.

Chúng tôi thấy những khu vực khác nhau này

và nó trông khá tốt.

Bây giờ, hầu hết các nút màu xanh

đang ở trong màu xanh

không gian và hầu hết

các hình tam giác màu cam là

trong không gian màu cam.

Nhưng thực tế đó là gì

những quy định đã có

được tạo bên dưới bởi

thuật toán GIỎ HÀNG?

SKLearn đã tích hợp sẵn

chức năng để

hiển thị thực tế

chính cây quyết định.

Chúng ta có thể sử dụng cốt truyện

thực sự là cây

tạo ra cái này và sau đó

hiển thị nó trong dòng.

Đây là cây quyết định của chúng tôi.

Đây là cây quyết định của chúng tôi.

Hãy đi qua nó.

Trong mỗi nút, chúng ta thấy quy tắc,

đó là so sánh nhị phân,

lớn hơn hoặc nhỏ hơn

đối với một

tính năng duy nhất.

Tại nút gốc, chúng ta thấy

sự chia rẽ xảy ra vào lúc

87,353 dặm một giờ

về tốc độ hiệu quả.

Ngay dưới đó

là giá trị gini.

Đây là thước đo

tạp chất và chúng ta có thể

kiểm soát thuật toán CART sử dụng.

Mặc định là

hệ số gini.

Bây giờ tôi sẽ không

đi sâu vào vấn đề này hơn,

nhưng bạn có thể đọc về

các lựa chọn của bạn và cách

hệ số Gini là

được tính toán trong tài liệu SKLearn.

Sau đó chúng ta thấy số lượng

các mẫu được xem xét trong

nút trong cây này đó là

chỉ hơn 600 nốt nhạc,

hoặc là thay đổi

up hoặc bóng nhanh.

Bây giờ hãy nhớ rằng chúng ta chỉ

quyết định nhìn vào

một phần nhỏ của

dữ liệu và sau đó chúng tôi lọc

chỉ cho hai lần ném bóng.

Dòng giá trị chứa

giá trị thực sự của chúng tôi cho

quan sát trong sự phân chia này.

Trong trường hợp này có 125

các trường hợp của lớp 0.

Đó là những hình vuông màu xanh và

499 trường hợp của chúng tôi

lớp hoặc hình tam giác màu cam.

Cuối cùng, chúng ta có lớp

giá trị đó sẽ là

được nút này dự đoán cho

các mẫu ở đó.

Điều này luôn luôn chỉ

lớp đa số.

Trong trường hợp này, màu cam của chúng tôi

hình tam giác hoặc một.

Bây giờ chúng ta hãy xem xét

ở nút bên trái.

Đây sẽ là tất cả

điểm dữ liệu mà

không có tốc độ hiệu quả dưới đây

ngưỡng của

87,353 dặm một giờ.

Chúng tôi thấy rằng ở đó

là 156 mẫu

ở đây và sau đó trong số đó,

114 là số 0 hoặc hình vuông màu xanh,

và 42 là hình tam giác màu vàng.

Lớp dự đoán

sẽ bằng không.

Chúng ta cũng thấy rằng sự phân chia ở

vị trí này không tuyệt vời

Rằng khi chúng ta phân đoạn theo

tốc độ quay phát hành

20-42 hệ số Gini

thực tế là gần 0,4

độ tinh khiết tốt hơn nhiều

mặc dù ở lần tiếp theo

mức độ trong cây,

đặc biệt là trên

phía bên phải,

phần lớn là của chúng tôi

sân lớp màu xanh.

Đó là cách quyết định

Phương pháp cây hoạt động

ở mức độ cao và

như bạn có thể thấy,

giải thích của

mô hình khá trực quan,

nhưng không phải lúc nào cũng vậy

rất đẹp và sạch sẽ.

Hãy đi xuống một lần nữa

cấp độ trong cây này.

Điều đó thật dễ dàng để làm. Chúng tôi vừa đặt

tốc độ sâu tối đa của chúng tôi để

ba và chạy lại.

Bây giờ cây này thực sự

trông không khác gì

cái trước và cái của chúng tôi

độ chính xác cũng như nhau.

Vì vậy, những gì mang lại? Hãy lấy

nhìn vào cốt truyện của các quy tắc.

Chúng ta hãy dành thời gian của chúng tôi vào

phía bên trái đó.

Chúng tôi thấy cả hai nút bị chia cắt

trên một giá trị khác của

giải phóng tốc độ quay.

Nhưng nó không thay đổi chút nào

phân loại của chúng tôi.

Cả hai cây con đều

một hoặc không và nó không

có vẻ như có gì mới

thông tin đã thu được.

Đây không thực sự là

hoàn toàn đúng.

Còn nhiều nữa

sự phân chia đang diễn ra,

nhưng ranh giới quyết định

không gian vẫn như cũ.

Tức là chúng ta không thể nhìn thấy

sự chia rẽ bởi vì chúng ta

vẫn dự đoán

kết quả lớp giống nhau.

Cây đó không còn hữu ích nữa

để dự đoán hơn lần trước.

Bây giờ, nếu bạn nhìn vào

Tài liệu SKLearn,

bạn sẽ thấy điều đó

có một tham số để

kiểm soát việc cắt tỉa

của cây hoặc

chỉ loại bỏ phân nhánh

như thế này được gọi là CCP Alpha.

Theo mặc định không có

việc cắt tỉa đang được thực hiện,

vì vậy giỏ hàng cứ tiếp tục

phân chia dựa trên

sự thuần khiết của sự lựa chọn phân chia

cho đến khi bạn nhận được Gini bằng 0,

một lớp hoàn toàn đồng nhất.

Thực tế chúng ta có thể thấy rằng điều này

đã xảy ra ở bên phải

bên thân cây.

Chuyện gì sẽ xảy ra nếu

chúng tôi quyết định tiếp tục tái sử dụng

xuống cái cây này.

Chúng ta hãy xem xét.

Wow, trông không kỳ lạ sao?

Bạn thấy cấp độ trước đó

thiết lập cấp độ này để phân chia

thông minh hơn một chút và

độ chính xác của chúng tôi đã tăng lên.

Chúng ta có thể thấy rằng có

một dòng rất nhỏ

màu cam ở phía bên trái

bên nào nắm bắt

có thể là bốn hình tam giác và chúng tôi cũng vậy

có độ chi tiết hơn một chút

trên đường chéo,

trông có vẻ hơi nhỏ

hơi giống một bộ

các bước và điều này thực sự

chứng minh điều gì đó

thực sự quan trọng

về cây quyết định

so với nói SVM.

Cây quyết định rất nhạy cảm với

việc xoay các điểm dữ liệu của chúng tôi.

Sự chia tách luôn luôn

một tính năng duy nhất,

x hoặc y trong trường hợp này.

Trong khi tuyến tính

SVM chẳng hạn

là một đường thẳng

theo bất kỳ hướng nào,

nếu bạn biết bạn là

dữ liệu được tách ra

theo đường chéo như trong trường hợp này,

thì tốt hơn là nên sử dụng

một SVM hoặc để chuyển đổi

dữ liệu của bạn bằng cách xoay

nó nếu bạn muốn

sử dụng cây quyết định.

Đây chỉ là những điều cơ bản về cách

cây quyết định hoạt động và

chúng ta sẽ lặn trong một

sâu hơn một chút và

hãy nhìn cách họ làm việc

nhiều lớp

tình huống và cách chúng tôi

cũng có thể hồi quy

với cây quyết định.