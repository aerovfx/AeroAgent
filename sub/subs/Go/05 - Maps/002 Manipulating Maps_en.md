# 002 Thao tác trên bản đồ vi

---

Giáo viên: Ở phần cuối,

chúng tôi lần đầu tiên được nếm trải bản đồ trong cờ vây.

Vì vậy, chúng tôi đã thấy một cú pháp ngay tại đây để khai báo bản đồ

với một số giá trị ban đầu được gán cho nó.

Bây giờ tôi muốn xem qua hai cách khác

rằng chúng ta có thể khai báo một bản đồ.

Vì vậy, tôi sẽ bình luận về khối mã hiện có này ngay tại đây

và chúng tôi sẽ bổ sung thêm hai cách nữa

ngay phía trên nó chỉ để xem cú pháp.

Bây giờ cái đầu tiên sẽ sử dụng

cú pháp var quen thuộc đó

mà chúng ta đã thấy vài lần trước đây.

Vì vậy chúng ta sẽ nói var màu sắc và sau đó chúng ta sẽ khai báo kiểu

của biến mà chúng ta đang khai báo ở đây.

Vậy chúng ta sẽ nói rằng đó là một bản đồ

trong đó tất cả các khóa đều thuộc loại chuỗi

và tất cả các giá trị cũng thuộc loại chuỗi.

Bây giờ chúng ta có thể lưu tệp này, lật lại thiết bị đầu cuối của chúng ta,

chạy lại chương trình và nó sẽ in ra một bản đồ trống.

Vì vậy hãy nhớ rằng bất cứ khi nào chúng ta khai báo một biến mới trong Go,

nếu chúng ta không gán giá trị thực cho nó,

Go sẽ khởi tạo nó với giá trị bằng 0.

Vì vậy, giá trị 0 của bản đồ về cơ bản chỉ là một bản đồ trống

vì vậy nó không có cặp giá trị khóa bên trong nó.

Chúng tôi thường áp dụng cách tiếp cận này ngay tại đây

khai báo bản đồ bằng từ khóa var

nếu sau này chúng ta muốn tìm hiểu xem những giá trị nào

hoặc cặp giá trị khóa nào chúng tôi muốn thêm vào đó.

Bây giờ chúng ta cũng có thể tạo một bản đồ

với cú pháp hơi khác một chút

bằng cách nói màu sắc dấu hai chấm bằng.

Và trong trường hợp này chúng ta sẽ sử dụng một hàm có sẵn

trong Go để tạo bản đồ mới này.

Chúng ta sẽ nói make và sau đó chúng ta sẽ chuyển vào loại

của bản đồ mà chúng tôi muốn tạo.

Vì vậy chúng ta sẽ nói chuỗi chuỗi bản đồ như vậy.

Vậy hai dòng mã ở đây khá đẹp

tương đương nhiều cho mọi ý định và mục đích.

Điều này sẽ tạo ra một bản đồ mới không có giá trị bên trong nó

trong đó tất cả các khóa đều thuộc loại chuỗi

và tất cả các giá trị cũng thuộc loại chuỗi.

Bây giờ nếu vì lý do nào đó chúng ta muốn tạo một bản đồ trống

với một trong những cách tiếp cận này ngay tại đây

và sau đó thêm vào một số giá trị,

điều đó hoàn toàn phù hợp.

Chúng tôi chắc chắn có thể làm điều đó.

Vì vậy, chúng ta có thể thêm các giá trị vào bản đồ hiện có

bằng cách sử dụng cú pháp dấu ngoặc vuông

mà bạn có thể đã thấy với các ngôn ngữ khác.

Vì vậy chúng ta có thể nói ở đây

có lẽ chúng tôi muốn thêm vào một cặp giá trị khóa bổ sung

cho màu trắng vào đối tượng màu sắc của chúng tôi.

Vì vậy chúng ta sẽ đặt tên của bản đồ,

niềng răng vuông của chúng tôi,

bên trong đây chúng ta sẽ đặt chìa khóa mà chúng ta muốn thêm vào.

Vì vậy có lẽ chúng ta sẽ thêm màu trắng

và sau đó chúng ta sẽ nói cái này bằng giá trị

và chúng ta sẽ nhập mã hex cho màu trắng, như vậy.

Bây giờ chúng ta sẽ lưu cái này, lật lại terminal,

chạy lại và chắc chắn rồi,

chúng tôi đã thêm cặp giá trị chính của mình.

Bây giờ, một cú pháp mà chúng ta đã thấy cách đây ít lâu

với cấu trúc là cú pháp dấu chấm.

Vì vậy, khi chúng tôi sử dụng cấu trúc,

chúng tôi thấy rằng chúng tôi có thể làm điều gì đó như stuctName dot,

Tôi không biết, màu trắng.

Vì vậy, chúng tôi không nhận được loại cú pháp này với bản đồ.

Nếu chúng ta muốn truy cập một khóa riêng lẻ

chúng ta phải sử dụng những dấu ngoặc vuông này

rồi điền tên thật vào

hoặc giá trị thích hợp của khóa ngay tại đây.

Lý do cho điều này là tất cả các phím

bên trong bản đồ của chúng tôi được gõ.

Và vì vậy khi chúng ta đặt dấu ngoặc vuông ở đây

chìa khóa mà chúng tôi cung cấp ngay tại đây

phải thuộc loại thích hợp.

Vì vậy, nếu vì lý do nào đó,

thay vì nói rằng chúng tôi có bản đồ với tất cả các phím

thuộc loại chuỗi,

nếu chúng ta nói rằng chúng ta có một bản đồ với những chiếc chìa khóa

thuộc loại int như vậy,

vậy thì khi chúng ta sử dụng cú pháp dấu ngoặc vuông ngay tại đây

thay vào đó chúng ta sẽ nói điều gì đó giống như bất kỳ int hợp lệ nào,

nên có lẽ là 10.

Và vì vậy bạn có thể tưởng tượng

bằng cách sử dụng cú pháp dấu chấm ngay tại đây

sẽ không ổn lắm

bởi vì khi đó chúng ta sẽ phải làm điều gì đó như thế,

điều này không có nhiều ý nghĩa với bản đồ.

Vì vậy, chúng tôi luôn đảm bảo rằng chúng tôi sử dụng

cú pháp dấu ngoặc vuông với bản đồ.

Bây giờ, chỉ để kiểm tra điều này

và xem nó hoạt động như thế nào với int,

hãy lưu nó và chạy lại.

Vậy nên tôi sẽ tiết kiệm. Và chúng ta bắt đầu.

Vậy bây giờ chúng ta đã có 10 là chỉ ra giá trị fff.

Bây giờ điều cuối cùng tôi muốn chỉ cho bạn là cách xóa chìa khóa

và các giá trị trên bản đồ hiện có.

Vì vậy, chúng ta có thể sử dụng một chức năng tích hợp khác cho việc này.

Và chức năng tích hợp này được gọi là chức năng xóa.

Vì vậy, chúng tôi có thể chuyển bản đồ của mình và sau đó là chìa khóa

rằng chúng tôi muốn xóa bản đồ.

Vì vậy, chúng tôi sẽ vượt qua trong bản đồ của chúng tôi

và sau đó có lẽ chúng ta muốn xóa cặp giá trị khóa

với phím số 10.

Vì vậy, với đối số thứ hai, chúng ta sẽ chuyển vào 10 như vậy.

Bây giờ hãy lưu nó và chạy lại.

Và khi chúng tôi làm như vậy chúng tôi thấy rằng chúng tôi đã trở lại

đến một bản đồ hoàn toàn trống rỗng, giống như trước đây.

Được rồi, còn hai điều nữa tôi muốn cho bạn thấy trong video tiếp theo.

Tôi muốn dành một chút thời gian

để cho bạn thấy chính xác cách chúng tôi có thể lặp lại trên bản đồ.

Và sau đó tôi cũng muốn cho bạn thấy một chút

về sự khác biệt giữa bản đồ và cấu trúc

bởi vì tôi chắc chắn vào thời điểm này

đó là một trong những câu hỏi lớn mà bạn có.

Chúng ta sẽ sử dụng bản đồ ở đâu so với struct.

Vậy chúng ta hãy nghỉ ngơi nhanh thôi,

quay lại phần tiếp theo

và tìm ra cách lặp lại trên bản đồ.