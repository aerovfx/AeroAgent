# 05 lời giải thích cho việc triển khai được vector hóa

---

Trong video trước,

chúng ta đã thấy các ví dụ đào tạo của bạn được xếp chồng lên nhau theo chiều ngang trong ma trận x như thế nào,

bạn có thể rút ra cách triển khai vector hóa để truyền bá qua mạng thần kinh của mình.

Chúng ta hãy giải thích thêm một chút về lý do tại sao các phương trình chúng ta viết

down là cách triển khai chính xác việc vector hóa trên nhiều ví dụ.

Vì vậy, chúng ta hãy xem qua phần tính toán lan truyền thuận cho một số ví dụ.

Hãy nói rằng đối với ví dụ đào tạo đầu tiên,

bạn kết thúc việc tính toán

x1 cộng b1 và sau đó là ví dụ huấn luyện thứ hai,

cuối cùng bạn tính x2 cộng b1 và

sau đó đối với ví dụ đào tạo thứ ba,

cuối cùng bạn tính được 3 cộng b1.

Vì vậy, để đơn giản hóa việc giải thích trên slide này, tôi sẽ bỏ qua b.

Vì vậy, hãy nói rằng, để đơn giản hóa sự chứng minh này một chút, b bằng 0.

Nhưng lập luận mà chúng ta sắp đưa ra sẽ có tác dụng với

chỉ có một chút thay đổi ngay cả khi b khác 0.

Nó chỉ đơn giản hóa mô tả trên slide một chút.

Bây giờ, w1 sẽ là một ma trận nào đó, phải không?

Vì vậy, tôi có một số hàng trong ma trận này.

Vậy nếu bạn nhìn vào phép tính x1 này,

những gì bạn có là

w1 nhân x1 cho bạn một vectơ cột nào đó mà bạn phải vẽ như thế này.

Và tương tự, nếu bạn nhìn vào vector x2 này,

bạn có điều đó w1 lần

x2 cho một số vectơ cột khác, phải không?

Và điều đó mang lại cho bạn chiếc z12 này.

Và cuối cùng, nếu bạn nhìn vào x3,

bạn có w1 nhân x3,

cung cấp cho bạn một số vectơ cột thứ ba, đó là z13.

Vì vậy bây giờ, nếu bạn xem xét tập huấn luyện X viết hoa,

mà chúng tôi hình thành bằng cách xếp chồng tất cả các ví dụ đào tạo của chúng tôi lại với nhau.

Vì vậy ma trận viết hoa X được hình thành bằng cách lấy vectơ x1 và

xếp nó theo chiều dọc với x2 và sau đó là x3.

Đây là nếu chúng ta chỉ có ba ví dụ huấn luyện.

Nếu bạn có nhiều hơn, bạn biết đấy, chúng sẽ tiếp tục xếp chồng lên nhau theo chiều ngang như vậy.

Nhưng nếu bây giờ bạn lấy ma trận x này và nhân nó với w thì bạn sẽ có,

nếu bạn nghĩ về cách hoạt động của phép nhân ma trận,

bạn kết thúc với cột đầu tiên là

những giá trị tương tự mà tôi đã vẽ ở đó bằng màu tím.

Cột thứ hai sẽ là bốn giá trị tương tự.

Và cột thứ ba sẽ là những giá trị màu cam đó,

hóa ra chúng là gì.

Nhưng tất nhiên điều này chỉ bằng z11 được biểu diễn dưới dạng

vectơ cột theo sau là z12 được biểu thị dưới dạng vectơ cột theo sau là z13,

cũng được biểu diễn dưới dạng vectơ cột.

Và đây là nếu bạn có ba ví dụ huấn luyện.

Bạn nhận được nhiều ví dụ hơn thì sẽ có nhiều cột hơn.

Và vì vậy, đây chỉ là chữ hoa ma trận Z1 của chúng ta.

Vì vậy tôi hy vọng điều này đưa ra lời giải thích cho lý do tại sao chúng tôi đã

trước đây w1 nhân xi bằng

z1i khi chúng ta xem ví dụ huấn luyện đơn lẻ vào thời điểm đó.

Khi bạn lấy các ví dụ đào tạo khác nhau và xếp chúng vào các cột khác nhau,

thì kết quả tương ứng là bạn kết thúc

với chữ z cũng được xếp chồng lên nhau ở các cột.

Và tôi sẽ không xuất hiện nhưng bạn có thể tự thuyết phục mình nếu bạn muốn điều đó với tính năng phát sóng Python,

nếu bạn thêm lại vào,

các giá trị này của b đến các giá trị vẫn đúng.

Và điều thực sự xảy ra là bạn kết thúc với việc phát sóng bằng Python,

cuối cùng bạn sẽ có bi riêng lẻ cho từng cột của ma trận này.

Vì vậy, trên slide này, tôi chỉ chứng minh rằng z1 bằng

w1x cộng b1 là

một vector hóa chính xác của

bước đầu tiên trong bốn bước chúng ta có ở slide trước,

nhưng hóa ra một phân tích tương tự cho phép bạn

cho thấy các bước khác cũng có tác dụng khi sử dụng

một logic rất giống nhau trong đó nếu bạn xếp các đầu vào theo cột thì sau phương trình,

bạn nhận được kết quả đầu ra tương ứng cũng được xếp chồng lên nhau theo cột.

Cuối cùng, hãy tóm tắt lại mọi thứ chúng ta đã nói trong video này.

Nếu đây là mạng lưới thần kinh của bạn,

chúng tôi đã nói rằng đây là điều bạn cần làm nếu bạn muốn triển khai để nhân giống,

mỗi lần một ví dụ huấn luyện đi từ i bằng 1 đến m. Và sau đó chúng tôi nói,

Hãy sắp xếp các ví dụ huấn luyện thành các cột như vậy và với mỗi giá trị z1 này,

a1, z2, a2 hãy xếp các cột tương ứng như sau.

Vì vậy, đây là ví dụ cho a1 nhưng điều này đúng với z1,

a1, z2 và a2.

Sau đó, những gì chúng tôi trình bày trên slide trước đó là

dòng này cho phép bạn vector hóa nó trên tất cả m ví dụ cùng một lúc.

Và hóa ra với lý luận tương tự,

bạn có thể chỉ ra rằng tất cả các dòng khác là

vector hóa chính xác của cả bốn dòng mã này.

Và như một lời nhắc nhở,

vì x cũng bằng a0 vì hãy nhớ rằng

vectơ đặc tính đầu vào x bằng a0, vì vậy xi bằng a0i.

Vậy thì thực sự có một sự đối xứng nhất định đối với

những phương trình này trong đó phương trình đầu tiên này cũng có thể là

viết z1 = w1 a0 + b1.

Và vì vậy, bạn thấy rằng cặp phương trình này và cặp phương trình này

các phương trình thực sự trông rất giống nhau nhưng chỉ là tất cả các chỉ số đều tăng lên một.

Vì vậy, điều này cho thấy rằng các lớp khác nhau của mạng lưới thần kinh được

đại khái là làm cùng một việc hoặc chỉ làm đi làm lại cùng một phép tính.

Và ở đây chúng ta có mạng lưới thần kinh hai lớp nơi chúng ta đi đến

một mạng lưới thần kinh sâu hơn nhiều trong các video của tuần tới.

Bạn thấy rằng thậm chí các mạng lưới thần kinh sâu hơn về cơ bản đang sử dụng

hai bước này và thực hiện chúng nhiều lần hơn những gì bạn thấy ở đây.

Vì vậy, đó là cách bạn có thể vector hóa mạng lưới thần kinh của mình qua nhiều ví dụ đào tạo.

Tiếp theo, cho đến nay chúng ta vẫn đang sử dụng các hàm sigmoid trên toàn bộ mạng lưới thần kinh của mình.

Hóa ra đó thực sự không phải là sự lựa chọn tốt nhất.

Trong video tiếp theo, chúng ta cùng tìm hiểu một chút nhé

sâu hơn về cách bạn có thể sử dụng những cách khác nhau, cái được gọi là,

các hàm kích hoạt trong đó hàm sigmoid chỉ là một lựa chọn khả thi.