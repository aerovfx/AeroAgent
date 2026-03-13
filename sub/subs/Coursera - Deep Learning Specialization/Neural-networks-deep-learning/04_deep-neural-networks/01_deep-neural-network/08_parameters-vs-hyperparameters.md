# 08 tham số-vs-siêu tham số

---

Có hiệu quả trong việc phát triển chiều sâu của bạn

Mạng lưới thần kinh yêu cầu bạn không chỉ

tổ chức tốt các thông số của bạn nhưng cũng

siêu thông số của bạn. Vậy siêu là gì

thông số? chúng ta hãy xem! Vì vậy

tham số mô hình của bạn là W và B và

có những điều khác bạn cần nói

thuật toán học tập của bạn, chẳng hạn như

tỷ lệ học tập alpha, bởi vì chúng ta cần

để đặt alpha và điều đó sẽ

xác định các thông số của bạn phát triển như thế nào hoặc

có lẽ số lần lặp của

việc giảm độ dốc mà bạn thực hiện. của bạn

thuật toán học tập có oth

những con số mà bạn cần đặt chẳng hạn như

số lớp ẩn nên chúng tôi gọi đó là

chữ L viết hoa hoặc số đơn vị ẩn,

chẳng hạn như 0 và 1 và 2 và

vân vân. Sau đó, bạn cũng có quyền lựa chọn

của hàm kích hoạt. bạn có muốn không

sử dụng RELU, hoặc tiếp tuyến hoặc sigmoid

hoạt động đặc biệt trong

các lớp ẩn. Vậy tất cả những điều này

là những điều bạn cần nói với bạn

thuật toán học tập và vì vậy đây là

các thông số kiểm soát cuối cùng

tham số W và B và vì vậy chúng tôi gọi tất cả

những điều này dưới các thông số siêu.

Bởi vì những thứ như alpha,

tốc độ học tập, số lần lặp lại,

số lớp ẩn, v.v., những lớp này

đều là các tham số điều khiển W và B.

Vì vậy chúng tôi gọi những thứ này là siêu tham số,

bởi vì chính các siêu tham số đó

bằng cách nào đó xác định cuối cùng

giá trị của tham số W và B mà bạn

kết thúc với. Trên thực tế, học sâu có một

rất nhiều siêu tham số khác nhau.

Trong khóa học sau, chúng ta sẽ thấy những điều khác

siêu tham số cũng như

thời hạn động lượng, kích thước lô nhỏ,

các hình thức chính quy khác nhau

các tham số, v.v. Nếu không có

những thuật ngữ ở phía dưới vẫn có ý nghĩa,

đừng lo lắng về nó! Chúng ta sẽ nói về

chúng trong khóa học thứ hai. Bởi vì sâu sắc

học tập có rất nhiều thông số siêu trong

tương phản với các lỗi trước đó của máy

học tập, tôi sẽ cố gắng trở thành

nhất quán trong việc gọi tốc độ học tập

alpha một siêu tham số chứ không phải

gọi tham số. Tôi nghĩ trước đó

kỷ nguyên của máy học khi chúng ta không

có rất nhiều thông số siêu cao, hầu hết chúng ta

ở đây thường hơi chậm và chỉ

gọi alpha là một tham số. Về mặt kỹ thuật,

alpha là một tham số, nhưng là một tham số

xác định các tham số thực. tôi sẽ

cố gắng nhất quán trong việc gọi những điều này

những thứ như alpha, số lượng

lặp lại, v.v. trên các siêu tham số. Vì vậy

khi bạn đang huấn luyện một mạng lưới sâu cho

ứng dụng riêng mà bạn thấy rằng có thể có

có rất nhiều cài đặt có thể có cho

siêu tham số mà bạn cần chỉ

thử. Vì vậy việc áp dụng deep learning ngày nay là

một quá trình rất phức tạp mà bạn thường xuyên

có thể có một ý tưởng Ví dụ, bạn có thể

có ý tưởng về giá trị tốt nhất cho

tốc độ học tập. Bạn có thể nói, cũng có thể

alpha bằng 0,01 Tôi muốn thử điều đó.

Sau đó bạn thực hiện, dùng thử và sau đó

hãy xem nó hoạt động như thế nào Dựa trên

kết quả đó bạn có thể nói, bạn biết không?

Tôi đã thay đổi trực tuyến, tôi muốn tăng

tỷ lệ học tập đến 0,05. Vì vậy, nếu

bạn không chắc chắn giá trị tốt nhất là gì

để sử dụng tỷ lệ học tập. Bạn có thể

thử một giá trị của tỷ lệ học tập alpha

và thấy hàm chi phí j của họ giảm xuống

như thế này thì bạn có thể thử cái lớn hơn

giá trị cho tỷ lệ học tập alpha và

xem hàm chi phí bùng nổ và

phân kỳ. Sau đó, bạn có thể thử cái khác

phiên bản và thấy nó đi xuống rất nhanh.

nó nghịch đảo với giá trị cao hơn. Bạn có thể

thử phiên bản khác và

xem hàm chi phí J làm điều đó nhé.

Tôi sẽ cố gắng thiết lập các giá trị. Vì vậy bạn có thể

nói, được rồi, có vẻ như đây là giá trị của

alpha. Nó giúp tôi học hỏi khá nhanh

và cho phép tôi hội tụ đến mức thấp hơn

hàm chi phí j và vì vậy tôi sẽ sử dụng

giá trị này của alpha. Bạn đã thấy trong một

slide trước có rất nhiều

các thông số lai khác nhau. Nó quay

nhận ra rằng khi bạn bắt đầu làm việc mới

ứng dụng, bạn sẽ thấy nó rất

khó biết trước chính xác

giá trị tốt nhất của siêu là gì

các thông số. Vì vậy, điều thường xảy ra là bạn

chỉ cần thử nhiều cách khác nhau

giá trị và đi vòng quanh chu kỳ này

thử một số giá trị, thực sự thử năm giá trị ẩn

các lớp. Với số lượng ẩn này

các đơn vị thực hiện việc đó, xem nó có hiệu quả không và

sau đó lặp lại. Vì vậy tiêu đề của slide này

là việc áp dụng học sâu là một điều rất

quá trình thực nghiệm và quá trình thực nghiệm

có lẽ là một cách nói hoa mỹ để nói rằng bạn chỉ

phải thử rất nhiều thứ và xem những gì

hoạt động. Một hiệu ứng khác tôi đã thấy là

học sâu ngày nay được áp dụng cho

nhiều vấn đề khác nhau, từ máy tính

tầm nhìn, nhận dạng giọng nói, tự nhiên

xử lý ngôn ngữ cho rất nhiều

các ứng dụng dữ liệu có cấu trúc như

có thể là quảng cáo trực tuyến hoặc tìm kiếm trên web,

hoặc đề xuất sản phẩm, v.v.

Điều tôi thấy đầu tiên là tôi đã thấy

các nhà nghiên cứu từ một ngành, bất kỳ ngành nào

trong số này và cố gắng chuyển sang một cái khác.

Và đôi khi trực giác về siêu

các tham số được chuyển tiếp và đôi khi nó

không, nên tôi thường khuyên mọi người,

đặc biệt là khi bắt đầu một công việc mới

vấn đề, chỉ cần thử một loạt

giá trị và xem những gì w. Trong phần tiếp theo

tất nhiên chúng tôi sẽ

xem một số cách có hệ thống để thử

một loạt các giá trị. Thứ hai,

ngay cả khi bạn đang làm việc trên một

ứng dụng trong một thời gian dài, bạn biết đấy

có thể bạn đang làm việc trực tuyến

quảng cáo, khi bạn đạt được tiến bộ trên

vấn đề rất có thể là tốt nhất

giá trị cho tỷ lệ học tập, một số

các đơn vị ẩn, v.v. có thể thay đổi. Vì vậy

ngay cả khi bạn điều chỉnh hệ thống của mình ở mức tốt nhất

giá trị của siêu tham số ngày nay

có thể bạn sẽ thấy rằng giá trị tốt nhất

có thể thay đổi một năm nữa kể từ bây giờ có lẽ

bởi vì cơ sở hạ tầng máy tính,

có thể bạn biết CPU hoặc loại GPU

đang chạy hoặc có gì đó đã thay đổi.

Vì vậy có lẽ một nguyên tắc nhỏ là

thỉnh thoảng, có thể vài lần

tháng, nếu bạn đang giải quyết một vấn đề

trong một thời gian dài đối với nhiều người

năm chỉ cần thử một vài giá trị cho

siêu tham số và kiểm tra kỹ xem

có một giá trị tốt hơn cho siêu

các thông số. Khi bạn làm như vậy, bạn từ từ

cũng có được trực giác về siêu

thông số phù hợp nhất với bạn

vấn đề.

Tôi biết rằng điều này có vẻ giống như một

phần không thỏa mãn của việc học sâu

bạn chỉ cần thử tất cả các giá trị

đối với các siêu tham số này, nhưng có lẽ

đây là một lĩnh vực mà học sâu

nghiên cứu vẫn đang tiến triển, và có thể

theo thời gian chúng tôi sẽ có thể cung cấp tốt hơn

hướng dẫn các thông số siêu tốt nhất

để sử dụng. Cũng có thể là

bởi vì CPU, GPU, mạng và

tất cả các tập dữ liệu đều thay đổi và đó là

có thể hướng dẫn sẽ không

hội tụ một thời gian. Bạn chỉ cần

để tiếp tục thử những giá trị khác nhau và

tạm dừng đánh giá chúng

bộ xác thực chéo hoặc một cái gì đó và

chọn giá trị phù hợp với bạn

vấn đề. Đó là một cuộc thảo luận ngắn gọn

của siêu tham số. Trong khóa học thứ hai,

chúng tôi cũng sẽ đưa ra một số gợi ý về cách

để khám phá một cách có hệ thống không gian của

siêu thông số nhưng bây giờ bạn thực sự

có khá nhiều công cụ bạn cần

để làm bài tập lập trình trước

bạn làm điều đó điều chỉnh hoặc chia sẻ xem một

nhiều ý tưởng hơn mà tôi thường hỏi

học sâu có tác dụng gì

bộ não con người?