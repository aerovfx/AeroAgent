# 04 cách tính khoảng cách khác nhau

---

Chúng ta sẽ thảo luận về vấn đề sau

ba phương pháp tính khoảng cách,

Khoảng cách Manhattan, khoảng cách Euclide,

và khoảng cách Hamming.

Hãy bắt đầu với khoảng cách Manhattan.

Khoảng cách Manhattan

là tổng tuyệt đối

sự khác biệt giữa hai điểm

trên tất cả các kích thước.

Nghe có vẻ phức tạp phải không?

Hãy phá vỡ nó.

Hiện tại,

chúng ta sẽ chỉ xem xét một chiều.

Chúng ta có hai điểm trong chiều này,

A và B có tọa độ p và q.

Bây giờ, bạn nghĩ làm thế nào chúng ta có thể tính toán

khoảng cách giữa A và B?

Chúng ta có thể thấy giá trị của p là 3 và

của q là 8.

Chúng ta sẽ chỉ tính toán tuyệt đối

sự khác biệt giữa hai,

đó là 3-8, bằng 5 đơn vị.

Khá đơn giản phải không?

Hãy thử một ví dụ khác và

trong trường hợp này, chúng ta có hai chiều.

Ta có tọa độ của A là p1,p2 và

tọa độ của B là q1,q2.

Bạn nghĩ chúng ta có thể tính toán như thế nào

khoảng cách tuyệt đối giữa A và B?

Nhìn vào định nghĩa cẩn thận hơn.

Chúng ta có thể thấy rằng đó là tổng của

sự khác biệt tuyệt đối giữa hai

điểm trên tất cả các chiều.

Vì vậy, chúng ta sẽ lấy một chiều tại một thời điểm.

Đầu tiên chúng ta sẽ tính toán sự khác biệt

giữa A và B trong chiều này,

và sau đó ở chiều không gian này.

Vì vậy, ở đây chúng ta có sự khác biệt giữa

A và B trong chiều này là p1-q1.

Và trong chiều này nó sẽ là p2-q2.

Và một lần nữa,

chúng tôi có sự khác biệt tuyệt đối.

Khi chúng ta thế các giá trị vào đây,

chúng ta có nó 5-8 và 5-9.

Vậy khoảng cách sẽ là 7 đơn vị.

Tương tự, nếu chúng ta đưa nó vào n chiều,

chúng ta sẽ tính tổng tuyệt đối

sự khác biệt giữa các điểm

trong tất cả các kích thước.

Vì vậy chúng ta sẽ đưa nó về pn trừ qn,

trong đó n là số thứ nguyên.

Khoảng cách Manhattan được ưu tiên

khi chúng ta có nhiều kích thước hoặc

các đặc tính trong tập dữ liệu.

Nhưng khoảng cách Manhattan thì không

khoảng cách ngắn nhất giữa hai điểm.

Trong mặt phẳng hai chiều của chúng tôi, chúng tôi tính toán

khoảng cách theo hình chữ L.

Vì vậy chúng ta có một kỹ thuật khác

gọi là khoảng cách Euclide,

tính toán ngắn nhất

khoảng cách giữa hai điểm.

Nó là phổ biến nhất

kỹ thuật được sử dụng trong ngành.

Bây giờ, hãy nhớ lại ví dụ chúng ta đã sử dụng cho

tìm khoảng cách Manhattan.

Chúng tôi đã tính khoảng cách theo cách này và

chúng tôi phát hiện ra là 7.

Bây giờ, bạn nghĩ điều gì sẽ là

khoảng cách ngắn nhất trong trường hợp Euclide?

Nó sẽ giống như

dòng hiển thị trên màn hình.

Bạn có thể đoán được công thức tính toán

khoảng cách giữa A và B?

Định lý Pythagoras.

Đó là những gì chúng tôi sẽ sử dụng.

Theo định lý Pythagoras,

khoảng cách này, h,

sẽ bằng gốc của tổng

hình vuông của đường vuông góc và đáy.

Nếu chúng ta thế các giá trị của A và

B về phương vuông góc và đáy,

chúng ta sẽ có được nó như phương trình hiển thị ở đây,

sẽ cho chúng ta khoảng cách 5 đơn vị.

Vì vậy, ngắn nhất hoặc Euclide

khoảng cách giữa A và B là 5 đơn vị.

Tương tự, với n chiều,

công thức cho

khoảng cách Euclide sẽ

trông giống như thế này

Hãy đơn giản hóa việc này bằng cách sử dụng

tổng của bình phương (pi-qi) và

gốc của phép tính tổng.

Ở đây một lần nữa, chúng ta có giá trị n,

đó là số lượng kích thước,

và pi qi sẽ là tọa độ của chúng ta.

Hãy nhìn vào công thức.

Vì vậy, chúng tôi đã đề cập đến hai kỹ thuật

để tính khoảng cách,

khoảng cách Manhattan và

khoảng cách Euclide.

Cả hai kỹ thuật chúng tôi đề cập bây giờ

là tính khoảng cách giữa

các biến liên tục.

Nhưng nếu chúng ta phải tính toán

khoảng cách giữa hai

biến phân loại?

Đối với điều này, chúng tôi có một kỹ thuật khác

gọi là khoảng cách Hamming.

Về cơ bản nó là tổng số

sự khác nhau giữa hai chuỗi

chiều dài giống nhau.

Bây giờ, với độ dài giống hệt nhau, chúng tôi muốn nói

số lượng ký tự trong cả hai

các dây phải giống nhau.

Hãy hiểu điều này với một vài ví dụ.

Chúng tôi có một biến, giới tính và

chúng ta có ba hàng A, B và C.

Chúng tôi đã chuyển đổi biến, giới tính,

nam và nữ thành chuỗi 0 và 1.

Điều quan trọng cần lưu ý là 0 và

1 là chuỗi chứ không phải số.

Vậy là không có mệnh lệnh nào ở đây cả.

Tức là 1 không lớn hơn 0 và

0 không nhỏ hơn 1.

Bây giờ, để tính khoảng cách,

chúng ta sẽ thấy số lượng

sự khác biệt giữa hai chuỗi.

Vì vậy, chúng ta có 0 ở hàng A và 1 ở hàng B.

Vì có sự thay đổi

chỉ trong một ký tự,

khoảng cách giữa hàng A và hàng B là 1.

Tương tự, khoảng cách giữa B và

C lại là 1 vì chỉ có một

ký tự của chuỗi đã thay đổi.

Khoảng cách giữa A và

C sẽ bằng 0 vì có

không có sự thay đổi về nhân vật.

Bây giờ hãy lấy một ví dụ phức tạp hơn.

Trong ví dụ này, chúng ta có ba hàng với

ba đặc điểm phân loại khác nhau.

Bây giờ một lần nữa, chúng ta sẽ chuyển đổi

những đặc điểm này thành số.

Vậy chúng ta có 0 và 1 cho giới tính,

nam và nữ thì chúng ta có 0 và

1 dành cho người đã kết hôn và chưa kết hôn.

Và chúng ta có 1, 2 và 3 cho

tình trạng việc làm.

Như đã đề cập trước đó, những con số này không

có bất kỳ thứ tự nào vì chúng là các chuỗi.

Chúng tôi chỉ xem xét nếu kết hợp

các giá trị đã thay đổi.

Để làm điều này,

chúng tôi sẽ kết hợp tất cả các chuỗi.

Vì vậy, nếu bạn nhìn vào hàng A,

0,0,1 là chuỗi.

Đối với hàng B là 1,0,2,

và đối với C, nó là 0,1,3.

Trong trường hợp này, khi chúng ta so sánh A và B,

có bao nhiêu ký tự trong

chuỗi này đã thay đổi?

Vì vậy, số 0 đã đổi thành 1,

ký tự này không có gì thay đổi

và nhân vật này nữa

đã thay đổi từ 1 thành 2.

Vì hai nhân vật đã thay đổi,

khoảng cách giữa A và B sẽ là 2.

Nếu so sánh A và C thì ta có điểm đầu tiên

ký tự 0 trong cả hai trường hợp,

vì vậy điều này không thay đổi, và

ký tự thứ hai này thay đổi.

Và sau đó chúng ta có thứ ba

ký tự thay đổi từ 1 đến 3.

Vì vậy, một lần nữa, chúng ta có khoảng cách cho

A và C bằng 2.

Bây giờ đến lượt bạn.

Tại sao bạn không thử tính toán Hamming

khoảng cách giữa điểm B và điểm C?

Và điều đó kết thúc video này.

Khá mãnh liệt phải không?

Chúng tôi đã đề cập đến ba kỹ thuật khác nhau để

tính toán khoảng cách giữa các mẫu.

Trong video tiếp theo,

hãy đưa nó đi xa hơn một chút và

hiểu những cạm bẫy của

các thuật toán dựa trên khoảng cách.