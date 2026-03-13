# 06 a-note-on-python-numpy-vector

---

Khả năng của python cho phép bạn

sử dụng các hoạt động phát sóng và

tổng quát hơn, tính linh hoạt tuyệt vời của

ngôn ngữ chương trình python numpy là,

Tôi nghĩ, cả sức mạnh lẫn

điểm yếu của ngôn ngữ lập trình.

Tôi nghĩ đó là sức mạnh vì họ

tạo nên tính biểu cảm của ngôn ngữ.

Tính linh hoạt tuyệt vời của ngôn ngữ cho phép

bạn làm được rất nhiều việc dù chỉ với một việc duy nhất

dòng mã.

Nhưng cũng có điểm yếu vì với

phát sóng và số lượng lớn này

linh hoạt, đôi khi có thể

bạn có thể giới thiệu những lỗi rất tinh tế hoặc

những lỗi trông rất lạ, nếu bạn không

quen thuộc với tất cả những điều phức tạp của

phát sóng như thế nào và

cách các tính năng như phát sóng hoạt động.

Ví dụ: nếu bạn lấy một vectơ cột

và thêm nó vào một vectơ hàng, bạn sẽ

mong đợi nó sẽ tạo ra một chiều

không khớp hoặc lỗi gõ hoặc một cái gì đó.

Nhưng bạn thực sự có thể quay trở lại

một ma trận là tổng của một vectơ hàng và

một vectơ cột.

Vì vậy có một logic nội tại để

những hiệu ứng kỳ lạ này của Python.

Nhưng nếu bạn không quen với Python,

Tôi đã thấy một số học sinh có thái độ rất kỳ lạ,

rất khó tìm ra lỗi.

Vì vậy điều tôi muốn làm trong video này là

chia sẻ với bạn một số lời khuyên và

thủ thuật rất hữu ích cho

tôi để loại bỏ hoặc

đơn giản hóa và loại bỏ tất cả những điều lạ lùng

tìm kiếm lỗi trong mã của riêng tôi.

Và tôi hy vọng rằng với những lời khuyên này và

thủ thuật,

bạn cũng sẽ có thể dễ dàng hơn nhiều

viết mã không có lỗi, python và numpy.

Để minh họa một trong những điều ít hơn

hiệu ứng trực quan của Python-Numpy,

đặc biệt là cách bạn xây dựng vectơ trong

Python-Numpy, hãy để tôi làm bản demo nhanh.

Hãy đặt a = np.random.randn(5),

vì vậy điều này tạo ra năm Gaussian ngẫu nhiên

các biến được lưu trữ trong mảng a.

Và vì vậy hãy in(a) và

bây giờ hóa ra là thế

hình dạng của chữ a khi bạn làm điều này

đây là cấu trúc năm màu.

Và vì vậy đây được gọi là thứ hạng

1 mảng trong Python và

nó không phải là một vector hàng cũng không phải

một vectơ cột.

Và điều này dẫn đến nó có một số

hiệu ứng hơi không trực quan.

Vì vậy, ví dụ, nếu tôi in một chuyển vị,

cuối cùng nó trông giống như a.

Vì vậy, một và

một chuyển đổi cuối cùng trông giống nhau.

Và nếu tôi in sản phẩm bên trong giữa

a và một chuyển vị, bạn có thể nghĩ

đôi khi một chuyển vị có thể là bên ngoài

có thể sản phẩm sẽ cung cấp cho bạn ma trận.

Nhưng nếu tôi làm thế,

thay vào đó bạn lấy lại một số.

Vì vậy điều tôi muốn giới thiệu là

khi bạn đang mã hóa các mạng mới,

rằng bạn không sử dụng cấu trúc dữ liệu

trong đó hình dạng là 5 hoặc n, mảng xếp hạng 1.

Thay vào đó, nếu bạn đặt a là thế này, (5,1),

sau đó điều này cam kết một

là (5,1) vectơ cột.

Và trong khi trước đây, a và

một sự chuyển đổi trông giống nhau,

bây giờ nó trở thành một chuyển vị,

bây giờ chuyển vị là một vectơ hàng.

Lưu ý một sự khác biệt tinh tế.

Trong cấu trúc dữ liệu này có hai

dấu ngoặc vuông khi chúng ta in chuyển vị.

Trong khi trước đó,

có một dấu ngoặc vuông.

Vậy đó là sự khác biệt

giữa cái này thực sự là 1 x

5 ma trận so với một trong

các mảng xếp hạng 1 này.

Và nếu bạn in, hãy nói,

tích giữa a và chuyển vị,

sau đó cái này mang lại cho bạn cái bên ngoài

tích của một vectơ phải không?

Và như vậy, sản phẩm bên ngoài của

một vectơ cung cấp cho bạn một ma trận.

Vì vậy, hãy xem xét chi tiết hơn

với những gì chúng ta vừa thấy ở đây.

Lệnh đầu tiên chúng tôi chạy,

vừa rồi, là thế này.

Và điều này đã tạo ra một cấu trúc dữ liệu với

a.shape là điều buồn cười (5,) vì vậy

đây được gọi là mảng xếp hạng 1.

Và đây là một cấu trúc dữ liệu rất buồn cười.

Nó cũng không hoạt động nhất quán như

vectơ hàng cũng như vectơ cột,

điều này làm cho một số của nó

hiệu ứng không trực quan.

Vì vậy điều tôi muốn giới thiệu là

khi bạn đang lập trình

bài tập, hoặc thực tế là khi bạn

thực hiện hồi quy logistic hoặc

mạng lưới thần kinh mà bạn vừa

không sử dụng các mảng xếp hạng 1 này.

Thay vào đó, nếu mỗi lần

bạn tạo một mảng,

bạn cam kết thực hiện nó

hoặc là một vectơ cột, vì vậy

điều này tạo ra một vectơ (5,1), hoặc

cam kết biến nó thành một vectơ hàng,

sau đó hành vi của vectơ của bạn

có thể dễ hiểu hơn.

Vì vậy trong trường hợp này,

a.shape sẽ bằng 5,1.

Và vì vậy điều này hoạt động rất giống một, nhưng

thực ra đây là một vectơ cột.

Và đó là lý do tại sao bạn có thể coi đây là

(5,1) ma trận, trong đó là vectơ cột.

Và ở đây a.shape sẽ là 1,5,

và điều này hoạt động nhất quán

dưới dạng một vectơ hàng.

Vì vậy, khi bạn cần một vectơ,

Tôi sẽ nói sử dụng cái này hoặc cái này, nhưng

không phải là mảng xếp hạng 1.

Một điều nữa mà tôi làm rất nhiều trong

mã là nếu tôi không hoàn toàn chắc chắn những gì

kích thước của một trong các vectơ của tôi,

Tôi thường đưa ra một tuyên bố khẳng định

như thế này, để đảm bảo, trong trường hợp này,

rằng đây là một vectơ (5,1).

Vậy đây là một vectơ cột.

Những khẳng định này thực sự

không tốn kém để thực hiện, và

họ cũng giúp phục vụ như

tài liệu cho mã của bạn.

Vì thế đừng ngần ngại khẳng định

những câu nói như thế này bất cứ khi nào bạn

cảm thấy thích.

Và cuối cùng, nếu vì lý do nào đó

bạn kết thúc với một mảng xếp hạng 1,

Bạn có thể định hình lại cái này, bằng a.reshape

nói một mảng (5,1) hoặc một mảng (1,5)

rằng nó hoạt động nhất quán hơn như

vectơ cột hoặc vectơ hàng.

Vì thế đôi khi tôi thấy học sinh

kết thúc rất khó theo dõi

bởi vì đó là những thứ không trực quan

tác dụng của mảng hạng 1.

Bằng cách loại bỏ mảng xếp hạng 1 trong cũ của tôi

mã, tôi nghĩ mã của tôi đã trở nên đơn giản hơn.

Và tôi thực sự đã không tìm thấy nó

hạn chế về những thứ tôi có thể

thể hiện bằng mã.

Tôi chưa bao giờ sử dụng mảng xếp hạng 1.

Và những điều cần rút ra sẽ đơn giản hóa

mã của bạn, không sử dụng mảng xếp hạng 1.

Luôn sử dụng ma trận n x một,

về cơ bản các vectơ cột, hoặc từng vectơ một

n ma trận, hay về cơ bản là vectơ hàng.

Hãy thoải mái ném thật nhiều

câu lệnh chèn, vì vậy

kiểm tra lại kích thước

của ma trận và mảng của bạn.

Ngoài ra, đừng ngại gọi điện cho

định hình lại hoạt động để đảm bảo rằng

ma trận hoặc vectơ của bạn

là kích thước mà bạn cần.

Vì vậy,

Tôi hy vọng rằng bộ gợi ý này

giúp bạn loại bỏ nguyên nhân gây ra lỗi

từ mã Python và gây ra sự cố

bài tập dễ dàng hơn để bạn hoàn thành.