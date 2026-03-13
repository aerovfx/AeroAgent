# 04 vectorizing-trên-nhiều-ví dụ

---

Trong video trước, bạn đã biết cách tính

dự đoán trên mạng lưới thần kinh,

đưa ra một ví dụ đào tạo duy nhất.

Trong video này, bạn sẽ thấy cách vector hóa

trên nhiều ví dụ đào tạo.

Và kết quả sẽ khá giống với

những gì bạn đã thấy về hồi quy logistic.

Nhờ đó sắp xếp các khóa đào tạo khác nhau

ví dụ trong các cột khác nhau của

ma trận, bạn có thể lấy

các phương trình bạn đã có từ video trước.

Và với rất ít sửa đổi, thay đổi

chúng để làm cho mạng lưới thần kinh tính toán

kết quả đầu ra trên tất cả các ví dụ trên

khá nhiều tất cả cùng một lúc.

Vậy hãy cùng xem chi tiết

về cách thực hiện điều đó.

Đây là bốn phương trình chúng ta có từ

video trước về cách tính z1,

a1, z2 và a2.

Và họ cho bạn biết làm thế nào,

đưa ra một tính năng đầu vào trở lại x,

bạn có thể sử dụng chúng để tạo mũ a2 = y cho

một ví dụ đào tạo duy nhất

Bây giờ nếu bạn có m ví dụ huấn luyện,

bạn cần lặp lại quá trình này cho

ví dụ đào tạo đầu tiên.

x chỉ số trên (1) để tính

y hat 1 đưa ra dự đoán về

ví dụ đào tạo đầu tiên của bạn.

Sau đó x(2) sử dụng nó để tạo ra

dự đoán y mũ (2).

Và cứ thế giảm xuống x(m) đến

tạo ra một dự đoán y hat (m).

Và vì thế trong tất cả những lần kích hoạt này

ký hiệu chức năng là tốt,

Tôi sẽ viết nó dưới dạng a[2](1).

Và đây là một[2](2),

và a(2)(m), do đó

ký hiệu này a[2](i).

Dấu ngoặc tròn tôi đề cập đến

để đào tạo ví dụ i,

và dấu ngoặc vuông 2

đề cập đến lớp 2, được thôi.

Đó là cách dấu ngoặc vuông và

các chỉ số khung tròn hoạt động.

Và vì vậy để gợi ý rằng nếu bạn có

một triển khai không được kiểm soát và

muốn tính toán dự đoán

trong số tất cả các ví dụ đào tạo của bạn,

bạn cần làm cho i = 1 đến m.

Sau đó về cơ bản thực hiện

bốn phương trình này phải không?

Bạn cần tạo một z[1](i)

= W(1) x(i) + b[1],

a[1](i) = sigma của z[1](1).

z[2](i) = w[2]a[1](i)

+ b[2] vàZ2i bằng w2a1i cộng b2 và

a[2](i) = điểm sigma của z[2](i).

Vì vậy, về cơ bản là bốn phương trình này

trên cùng bằng cách thêm vòng siêu ký tự

ngoặc i vào tất cả các biến mà

phụ thuộc vào ví dụ đào tạo.

Vì vậy việc thêm vòng chỉ số trên này

ngoặc i đến x là z và a,

nếu bạn muốn tính toán tất cả các kết quả đầu ra

trên các ví dụ về đào tạo m của bạn.

Điều chúng tôi muốn làm là vector hóa toàn bộ điều này

tính toán, để loại bỏ điều này cho.

Và nhân tiện, trong trường hợp có vẻ như

Tôi đang nhận được rất nhiều điều khó chịu

đại số tuyến tính, hóa ra là

có thể thực hiện điều này

một cách chính xác là quan trọng trong

kỷ nguyên học sâu

Và chúng tôi thực sự đã chọn ký hiệu

rất cẩn thận cho khóa học này và

thực hiện vector hóa này

bước dễ dàng nhất có thể.

Vì vậy tôi hy vọng rằng việc vượt qua điều này

sự thực tế thực sự sẽ giúp bạn

triển khai chính xác nhanh hơn

các thuật toán này đang hoạt động.

Được rồi, để tôi sao chép toàn bộ cái này

khối mã cho slide tiếp theo và

sau đó chúng ta sẽ xem cách vector hóa cái này.

Vì vậy đây là những gì chúng tôi có được từ

slide trước có for

vòng lặp đi qua các ví dụ đào tạo m của chúng tôi.

Vì vậy hãy nhớ lại rằng chúng ta đã định nghĩa

ma trận x bằng nhau

với các ví dụ đào tạo của chúng tôi được xếp chồng lên nhau

lên trong những cột này như vậy.

Vì vậy hãy lấy các ví dụ đào tạo và

xếp chúng thành cột.

Vậy cái này trở thành n, hoặc

có lẽ nx by m làm giảm ma trận.

Tôi chỉ định đưa ra câu kết

và cho bạn biết những gì bạn cần thực hiện trong

để có một vector hóa

thực hiện vòng lặp for này.

Hóa ra những gì bạn

việc cần làm là tính toán

Z[1] = W[1] X + b[1],

A[1]= điểm sig của z[1].

Khi đó Z[2] = w[2]

A[1] + b[2] và

thì A[2] = điểm sig của Z[2].

Vì vậy, nếu bạn muốn sự tương tự là

chúng tôi đã đi từ vector chữ thường xs

thành ma trận X viết hoa bằng cách xếp chồng

viết chữ xs thường vào các cột khác nhau.

Nếu bạn làm điều tương tự cho

zs, ví dụ như,

nếu bạn lấy z[1](i), z[1](2), v.v.

trên và đây đều là các vectơ cột,

lên tới z[1](m), phải.

Vì vậy, đó là số lượng đầu tiên mà tất cả

m trong số chúng và xếp chúng thành cột.

Sau đó chỉ cung cấp cho bạn ma trận z[1].

Và tương tự như vậy bạn nhìn

có thể nói số lượng này và

lấy a[1](1), a[1](2), v.v. và

a[1](m) và xếp chúng thành cột.

Sau đó, điều này, giống như chúng tôi đã đi từ

chữ x thường thành chữ hoa X và

chữ z viết thường thành chữ hoa Z.

Điều này bắt nguồn từ chữ thường a,

là các vectơ tới chữ hoa A[1] này,

nó ở đằng kia và

tương tự với z[2] và a[2].

Đúng là họ cũng có được

bằng cách lấy các vectơ này và

xếp chúng theo chiều ngang.

Và lấy những vectơ này và

xếp chúng theo chiều ngang,

để có được Z[2] và E[2].

Một trong những tài sản này

ký hiệu có thể giúp ích

bạn hãy nghĩ về điều đó là

ma trận này nói Z và A,

theo chiều ngang chúng ta sẽ

chỉ mục trên các ví dụ đào tạo.

Đó là lý do tại sao chỉ số ngang

tương ứng với ví dụ đào tạo khác nhau,

khi bạn quét từ trái sang phải bạn

quét qua các ô huấn luyện.

Và theo chiều dọc chỉ số dọc này

tương ứng với các nút khác nhau trong

mạng lưới thần kinh.

Vì vậy, ví dụ, nút này,

giá trị này ở trên cùng,

góc trên cùng bên trái của giá trị trung bình

tương ứng với kích hoạt

của đơn vị tiêu đề đầu tiên trên

ví dụ đào tạo đầu tiên.

Giảm một giá trị tương ứng với

kích hoạt ở đơn vị ẩn thứ hai trên

ví dụ đào tạo đầu tiên,

sau đó là đơn vị tiêu đề thứ ba trên

mẫu đào tạo đầu tiên, v.v.

Vì vậy, khi bạn quét xuống đây là của bạn

lập chỉ mục cho số đơn vị ẩn.

Trong khi đó nếu bạn di chuyển theo chiều ngang thì

bạn sẽ đi từ đơn vị ẩn đầu tiên.

Và ví dụ đào tạo đầu tiên

đến bây giờ là đơn vị ẩn đầu tiên và

mẫu đào tạo thứ hai,

ví dụ đào tạo thứ ba.

Và cứ như vậy cho đến khi nút này ở đây tương ứng

để kích hoạt lần đầu tiên

đơn vị ẩn trong ví dụ chuyến tàu cuối cùng và

ví dụ đào tạo thứ n.

Được rồi, ma trận theo chiều ngang

A xem xét các ví dụ đào tạo khác nhau.

Và theo chiều dọc thì khác nhau

chỉ số trong ma trận

A tương ứng với các đơn vị ẩn khác nhau.

Và trực giác tương tự cũng đúng với

ma trận Z cũng như đối với

X tương ứng theo chiều ngang

với các ví dụ đào tạo khác nhau.

Và theo chiều dọc nó tương ứng với

các tính năng đầu vào khác nhau mà

thực sự khác biệt so với những

lớp đầu vào của mạng nơ-ron.

Vậy trong những phương trình này, bây giờ bạn đã biết

cách triển khai trong mạng của bạn

với vector hóa, đó là

vector hóa trên nhiều ví dụ.

Trong video tiếp theo tôi muốn cho bạn thấy

thêm một chút biện minh về lý do tại sao

đây là một thực hiện đúng

của kiểu vector hóa này.

Hóa ra lời biện minh sẽ là

tương tự như những gì bạn đã thấy trong hồi quy logistic.

Chúng ta hãy chuyển sang video tiếp theo.