# 06 ngữ nghĩa-tìm kiếm-giới thiệu

---

Bây giờ hãy chuyển sự chú ý của chúng ta sang tìm kiếm ngữ nghĩa.

Tìm kiếm ngữ nghĩa có thể khớp tài liệu với lời nhắc

dựa trên ý nghĩa được chia sẻ và có thể nắm bắt được sắc thái

tìm kiếm từ khóa đó bị bỏ lỡ.

Ví dụ: tìm kiếm từ khóa không thể khớp với các từ

hạnh phúc và vui mừng, mặc dù chúng là từ đồng nghĩa,

và sẽ khớp không chính xác với Python, ngôn ngữ lập trình,

và Python, con rắn.

Công nghệ tìm kiếm ngữ nghĩa cơ bản khá đáng chú ý,

vì vậy hãy đi sâu vào để xem nó hoạt động như thế nào.

Ở mức độ rất cao, tìm kiếm ngữ nghĩa hoạt động giống như tìm kiếm từ khóa.

Mọi tài liệu đều được ánh xạ tới một vectơ và lời nhắc cũng vậy.

Sau đó, các vectơ nhắc và vectơ tài liệu

được so sánh để tạo ra điểm số,

và tìm các tài liệu phù hợp nhất với lời nhắc.

Sự khác biệt chính là cách gán vectơ

vào từng tài liệu và lời nhắc.

Trong tìm kiếm từ khóa, bạn chỉ cần đếm tần suất mỗi từ

xuất hiện trong đoạn văn bản.

Tuy nhiên, trong tìm kiếm ngữ nghĩa, bạn tạo ra các vectơ

bằng cách chạy tài liệu hoặc lời nhắc thông qua một chương trình đặc biệt

mô hình toán học được gọi là mô hình nhúng.

Mô hình nhúng ánh xạ các từ tới một vị trí trong không gian.

Vị trí này được biểu diễn bằng một vectơ.

Ví dụ: mô hình nhúng có thể ánh xạ từ pizza

tới vectơ 3, 1, và từ gấu tới vectơ 5, 2.

Trong hai chiều, bạn có thể biểu diễn những điều này

như các điểm trên trục x-y.

Bây giờ đến phần gần giống như phép thuật.

Mô hình nhúng sẽ ánh xạ các từ tương tự về mặt ngữ nghĩa

đến các vị trí lân cận trong không gian.

Ví dụ, từ thực phẩm và ẩm thực

sẽ được gắn chặt hơn với nhau,

và các từ trombone và mèo sẽ được đặt xa nhau hơn.

Ý nghĩa tương tự dẫn đến vị trí tương tự.

Trục x và y ở đây không có bất kỳ cách giải thích đơn giản nào.

Không có trục thực phẩm và trục động vật ở đây,

hoặc ít nhất không phải là thứ dễ nhìn thấy.

Thay vào đó bạn chỉ nên nghĩ về những điểm trôi nổi xung quanh

trên mặt phẳng 2D, với các từ có nghĩa tương tự

cụm lại với nhau.

Vector có nhiều mối quan hệ phức tạp,

và tạo ra các cụm hợp lý theo hai chiều

có lẽ sẽ không hoạt động.

Nếu mỗi vectơ có ba thành phần,

bạn có thể tưởng tượng việc nhúng chúng vào không gian ba chiều.

Bây giờ có nhiều không gian hơn để các nhóm khái niệm liên quan có thể hình thành,

và để nắm bắt các mối quan hệ sắc thái giữa chúng.

Tuy nhiên, trong hầu hết các mô hình nhúng,

những vectơ này có hàng trăm hoặc thậm chí hàng nghìn thành phần,

mang lại sự linh hoạt đáng kinh ngạc

về nơi nhúng từng điểm.

Không thể vẽ đồ thị hoặc thậm chí có thể tưởng tượng

không gian nhiều chiều này,

nhưng về mặt toán học, tất cả các nguyên tắc tương tự đều đúng.

Các vectơ cho tọa độ các vị trí trong không gian đó.

Những khái niệm tương tự được gắn chặt với nhau,

và các khái niệm khác nhau được đặt xa nhau hơn.

Mặc dù ví dụ này tập trung vào các từ riêng lẻ,

mô hình nhúng tồn tại cho nhiều loại dữ liệu đầu vào.

Có các mô hình nhúng cho từng từ riêng lẻ,

câu, và thậm chí toàn bộ tài liệu.

Những mô hình này sử dụng các loại đầu vào khác nhau,

nhưng trong mỗi trường hợp, xuất ra một vectơ duy nhất

xác định một điểm trong không gian.

Cũng giống như với những từ đơn lẻ,

nếu các vectơ gần nhau hơn,

các đoạn văn bản có ý nghĩa tương tự.

Hãy xem xét ba câu.

Anh ấy nói chuyện nhẹ nhàng trong lớp.

Anh thì thầm lặng lẽ trong giờ học.

Con gái bà đã làm bừng sáng ngày u ám.

Khi chiếu vào không gian vectơ,

các vectơ cho hai câu đầu tiên

sẽ gần nhau hơn

trong khi câu thứ ba sẽ khác xa với hai câu còn lại.

Để lượng hóa sự giống nhau

của các đoạn văn bản khác nhau,

bạn có thể đo khoảng cách giữa các vectơ của chúng.

Có một số cách để làm điều này.

Ví dụ: khoảng cách Euclide

bạn có thể nhớ từ lớp hình học

chỉ đo khoảng cách giữa hai vectơ

bằng cách vẽ một đường thẳng từ vectơ này sang vectơ kia,

khoảng cách ngắn nhất có thể giữa chúng.

Công thức tính toán này

về cơ bản là định lý Pythagore,

nhưng được mở rộng trên nhiều chiều hơn.

Tuy nhiên, trong không gian rất cao chiều,

mọi điểm có xu hướng khá xa

từ mọi điểm khác.

Một thước đo khoảng cách được sử dụng phổ biến hơn nhiều

là độ tương đồng cosin,

đo lường độ tương tự theo hướng của hai vectơ,

bất kể chúng có ở gần nhau trong không gian hay không.

Vectơ 10, 10 và 100, 100

không phải gần nhau đến thế sao,

nhưng họ nhìn về cùng một hướng.

Cosin tương tự nằm trong khoảng từ 1,

khi các vectơ hướng về cùng một hướng,

đến âm 1,

khi họ đối mặt hoàn toàn trái ngược với nhau.

Thỉnh thoảng bạn cũng sẽ thấy tích chấm,

đo độ dài hình chiếu của một vectơ

lên cái khác.

Nếu hai vectơ có độ dài và hướng giống nhau thì

hình chiếu sẽ lớn hơn.

Nếu chúng ở góc 90 độ,

chiều dài hình chiếu sẽ bằng không.

Nếu họ quay mặt về hướng ngược nhau,

tích số chấm sẽ âm.

Nếu toán học không phải là sở trường của bạn, đừng lo lắng.

Bạn có thể sẽ không bao giờ cần thực hiện các biện pháp đo khoảng cách này,

nhưng biết cách chúng hoạt động là hữu ích.

Ví dụ: đối với cả tích số chấm và độ tương tự cosine,

giá trị cao hơn phản ánh các vectơ gần hơn,

mà cuối cùng phản ánh nhiều khái niệm tương tự hơn.

Độ tương tự cosine dao động từ âm 1 đến 1,

và tích chấm có thể nhận bất kỳ giá trị nào

giữa âm và dương vô cùng.

Hãy xem cách đo khoảng cách này được sử dụng để hỗ trợ tìm kiếm ngữ nghĩa.

Đầu tiên, tất cả tài liệu được chiếu vào không gian vectơ

bằng mô hình nhúng.

Nhờ vào cách thiết kế mô hình nhúng,

các tài liệu có ý nghĩa tương tự sẽ gần nhau hơn,

và các tài liệu có ý nghĩa khác nhau sẽ cách xa nhau hơn.

Tiếp theo, bạn nhúng lời nhắc để có được một vectơ riêng.

Bây giờ, bạn có thể đo khoảng cách giữa vectơ nhắc

và vectơ của từng tài liệu.

Nhờ vào cách thiết kế mô hình nhúng,

tài liệu nào gần nhất cũng sẽ có ý nghĩa giống nhau nhất.

Tại thời điểm này, việc xếp hạng tài liệu rất dễ dàng.

Bạn chỉ cần sắp xếp tài liệu theo khoảng cách từ dấu nhắc

và trả lại những tài liệu có khoảng cách ngắn nhất.

Nhờ vào cách thức hoạt động của mô hình nhúng,

bạn vừa tìm thấy những tài liệu có ý nghĩa gần giống nhất với lời nhắc của bạn.

Tìm kiếm ngữ nghĩa khá đơn giản

nếu bạn cho rằng mô hình nhúng hoạt động bình thường.

Các khái niệm tương tự cuối cùng được ánh xạ tới các vị trí lân cận,

và do đó bạn có thể định lượng mức độ liên quan bằng khoảng cách giữa các vectơ.

Tìm hiểu sâu hơn một chút về cách đào tạo các mô hình nhúng

và cách họ gần như biết cách đặt những khái niệm tương tự một cách kỳ diệu

gần nhau hơn có thể giúp bạn hiểu sâu hơn

tìm kiếm ngữ nghĩa nói chung.

Vì vậy, hãy tham gia cùng tôi trong video tiếp theo để tìm hiểu sâu hơn một chút

về thành phần quan trọng này để tìm kiếm ngữ nghĩa.