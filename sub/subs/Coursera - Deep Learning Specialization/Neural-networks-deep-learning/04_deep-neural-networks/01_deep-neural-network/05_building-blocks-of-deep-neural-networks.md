# 05 khối xây dựng của mạng lưới thần kinh sâu

---

Trong các video đầu tuần này,

cũng như từ các video

từ nhiều tuần qua,

bạn đã thấy tòa nhà cơ bản

khối lan truyền về phía trước và

lan truyền ngược, các thành phần chính bạn

cần phải triển khai một mạng lưới thần kinh sâu.

Hãy xem cách bạn có thể đặt các thành phần này

cùng nhau xây dựng mạng lưới sâu của bạn.

Đây là một mạng lưới gồm một vài lớp.

Hãy chọn một lớp.

Và xem xét các tính toán

bây giờ chỉ tập trung vào lớp đó.

Vì vậy, đối với lớp L,

bạn có một số tham số wl và

bl và đối với chỗ dựa về phía trước, bạn sẽ nhập

kích hoạt a l-1

từ lớp trước của bạn và

xuất ra một l.

Vì vậy, cách chúng tôi đã làm điều này

trước đây bạn đã tính z l =

w l nhân al - 1 + b l.

Và khi đó al = g của z l.

Được rồi.

Vì vậy, đó là cách bạn đi từ đầu vào

al trừ một cho đầu ra al.

Và hóa ra là để sử dụng sau này, nó sẽ

cũng hữu ích khi lưu trữ giá trị zl.

Vì vậy, hãy để tôi đưa cái này vào bộ đệm như

tốt vì lưu trữ giá trị zl

sẽ hữu ích cho việc lạc hậu, vì

bước lan truyền ngược sau này.

Và sau đó cho bước lùi hoặc cho

bước lan truyền ngược, một lần nữa,

tập trung vào tính toán cho lớp này l,

bạn sắp thực hiện

một hàm nhập da(l).

Và xuất ra da(l-1), và

chỉ để xác thực các chi tiết,

đầu vào thực sự là da(l),

cũng như bộ nhớ đệm vậy

bạn có sẵn cho bạn giá trị

của zl mà bạn đã tính toán và

ngoài ra, xuất ra da(l)

trừ 1 bạn mang đầu ra hoặc

độ dốc bạn muốn theo thứ tự

để thực hiện giảm độ dốc cho

học tập, được chứ?

Vì vậy đây là cấu trúc cơ bản của

cách bạn thực hiện bước tiến này,

cái mà chúng ta gọi là hàm chuyển tiếp

cũng như bước lùi này,

mà chúng ta sẽ gọi là hàm lùi.

Tóm lại, trong lớp l,

bạn sẽ có bước tiến về phía trước hoặc

chỗ dựa phía trước của hàm chuyển tiếp.

Đầu vào al-1 và đầu ra, al, và

để thực hiện phép tính này

bạn cần sử dụng wl và bl.

Và cũng xuất ra một bộ đệm,

có chứa zl phải không?

Và sau đó là chức năng lùi,

sử dụng bước chống đỡ phía sau,

sẽ là một chức năng khác bây giờ

đầu vào da(l) và đầu ra da(l-1).

Vì vậy, nó cho bạn biết, với các đạo hàm

tôn trọng những kích hoạt này,

đó là da(l), đạo hàm là gì?

Tôi ước bao nhiêu?

Bạn biết đấy, al-1 thay đổi kết quả tính toán

các dẫn xuất liên quan đến việc hủy kích hoạt

từ lớp trước đó.

Trong hộp này phải không?

Bạn cần sử dụng wl và bl, và

hóa ra trên con đường bạn kết thúc

tính toán dzl, và hộp này,

chức năng lùi này

cũng có thể xuất dwl và

dbl, nhưng đôi khi tôi sử dụng mũi tên màu đỏ

để biểu thị sự lặp lại ngược.

Vì vậy, nếu bạn thích,

chúng ta có thể vẽ những mũi tên này bằng màu đỏ.

Vì vậy nếu bạn có thể thực hiện

hai chức năng này

thì phép tính cơ bản của

mạng lưới thần kinh sẽ như sau.

Bạn sẽ lấy đầu vào

có tính năng a0, đưa nó vào và

điều đó sẽ tính toán kích hoạt của

lớp đầu tiên, hãy gọi đó là a1 và

để làm điều đó, bạn cần có w1 và

b1 và sau đó cũng sẽ,

bạn biết đấy, nhớ cache z1 đi phải không?

Bây giờ đã làm xong việc đó, bạn cho nó ăn

lớp thứ hai và sau đó sử dụng w2 và b2,

bạn sẽ tính toán việc hủy kích hoạt

ở lớp tiếp theo a2, v.v.

Cho đến cuối cùng, bạn kết thúc việc xuất ra

a l bằng y hat.

Và trên đường đi,

chúng tôi đã lưu trữ tất cả các giá trị z này vào bộ nhớ đệm.

Vì vậy, đó là bước lan truyền về phía trước.

Bây giờ, đối với bước lan truyền ngược,

chúng ta sẽ làm gì

sẽ là một chuỗi lặp ngược

trong đó bạn đang đi lùi và

tính toán độ dốc như vậy.

Vậy bạn sẽ cho gì vào đây,

da(l) và

thì hộp này sẽ cho chúng ta da(l- 1) và

cứ như vậy cho đến khi được da(2) da(1).

Bạn thực sự có thể có thêm một cái nữa

xuất ra để tính da(0) nhưng

điều này là phái sinh đối với bạn

các tính năng đầu vào, đó là

ít nhất là không hữu ích cho

rèn luyện sức nặng của những thứ này

mạng lưới thần kinh được giám sát.

Vì vậy, bạn chỉ có thể dừng nó ở đó. Nhưng

trên đường đi,

back prop cũng xuất ra dwl,

dbl.

Tôi chỉ sử dụng dấu nhắc là wl và bl.

Điều này sẽ xuất ra dw3, db3, v.v.

Vì vậy, bạn kết thúc việc tính toán tất cả

các dẫn xuất bạn cần.

Và vì vậy chỉ để có thể điền vào

cấu trúc của cái này nhiều hơn một chút,

những hộp này sẽ sử dụng

những thông số đó nữa.

wl, bl và hóa ra là thế

sau này chúng ta sẽ thấy điều đó bên trong những chiếc hộp này

cuối cùng chúng tôi cũng tính toán dz.

Vì vậy, một lần lặp lại đào tạo thông qua

một mạng lưới thần kinh bao gồm: bắt đầu bằng

a(0) là x và

đi qua chỗ dựa phía trước như sau.

Tính toán y mũ và

sau đó sử dụng nó để tính toán cái này và

sau đó lùi lại, phải, làm điều đó và

bây giờ bạn có tất cả những dẫn xuất này

các điều khoản và như vậy, bạn biết đấy,

w sẽ được cập nhật dưới dạng w1 =

tốc độ học nhân với dw, phải không?

Đối với mỗi lớp và

tương tự cho tỷ lệ b.

Bây giờ phần chống lưng được tính toán

có tất cả các dẫn xuất này.

Đó là một lần lặp của gradient

đi xuống cho mạng lưới thần kinh của bạn.

Bây giờ trước khi tiếp tục,

chỉ là một chi tiết thông tin nữa.

Về mặt khái niệm, nó sẽ hữu ích

nghĩ về bộ nhớ đệm ở đây như

lưu trữ giá trị của z cho

các chức năng lùi.

Nhưng khi bạn thực hiện điều này, và

bạn thấy điều này trong bài tập lập trình,

Khi bạn thực hiện điều này,

bạn thấy rằng bộ đệm có thể

một cách thuận tiện để đạt được điều này

giá trị của các tham số w1, b1,

vào chức năng lùi là tốt.

Vì vậy đối với

bài tập này bạn thực sự lưu trữ trong

bộ nhớ cache vào z cũng như w

và b. Vì vậy, cái này lưu trữ z2, w2, b2.

Nhưng ở góc độ thực hiện,

Tôi chỉ thấy đó là một cách thuận tiện

chỉ để lấy các thông số,

sao chép vào nơi bạn cần sử dụng chúng sau này

khi bạn đang tính toán lan truyền ngược.

Vì vậy đó chỉ là một cách thực hiện

chi tiết mà bạn nhìn thấy khi

bạn thực hiện bài tập lập trình.

Vậy bây giờ bạn đã thấy những gì

là những khối xây dựng cơ bản cho

thực hiện một mạng lưới thần kinh sâu.

Trong mỗi lớp có

một bước lan truyền về phía trước và

có một cái tương ứng

bước lan truyền ngược.

Và có một bộ đệm để vượt qua

thông tin từ cái này sang cái khác.

Trong video tiếp theo,

chúng ta sẽ nói về cách bạn thực sự có thể

thực hiện các khối xây dựng này.

Chúng ta hãy chuyển sang video tiếp theo.