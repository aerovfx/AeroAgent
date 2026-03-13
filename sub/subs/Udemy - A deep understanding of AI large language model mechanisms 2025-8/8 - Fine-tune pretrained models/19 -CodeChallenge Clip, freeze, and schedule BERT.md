# 19 -CodeChallenge Clip, đóng băng và lên lịch BERT

---

Thử thách viết mã này về cơ bản là sự kết hợp của thử thách viết mã trước đó mà bạn đã đào tạo

mô hình BERT để phân loại cảm tính và video trước mà bạn đã tìm hiểu về

cắt gradient và lập lịch tốc độ học tập.

Bạn sẽ thấy trong thử thách viết mã này một lần nữa rằng việc sao chép, dán và sửa đổi mã

Việc thực hiện các kỹ thuật tinh chỉnh không quá khó nhưng biết liệu các kỹ thuật đó có

mà bạn đang nộp đơn thực sự phù hợp thì phức tạp hơn và nó đòi hỏi một số kiến thức chuyên môn,

một số kinh nghiệm và một số hình dung. Và việc xây dựng kiến thức và kinh nghiệm đó là một trong những

mục tiêu chính của tôi dành cho bạn trong video này.

Vậy hãy bắt đầu.

Đối với bài tập một, hãy sao chép tập tin sổ ghi chép

từ thử thách mã trước đó.

Và về cơ bản thử thách mã này

mà bạn đang làm việc ngay bây giờ

là một sửa đổi và mở rộng của cái trước đó.

Vì vậy, khi bạn có một bản sao của cuốn sổ đó,

bạn có thể chạy toàn bộ mọi thứ lên đến và bao gồm

nơi bạn tạo và cố định mô hình.

Tuy nhiên, không chạy mã để tinh chỉnh mô hình.

Chúng ta sẽ làm vài việc trước lúc đó

và thay đổi mã học tập đó một chút.

Vì vậy, đó là nhiệm vụ của bạn bây giờ.

Bạn có thể tạm dừng video và chuyển sang Python

và về cơ bản sao chép và chạy mã.

Tôi thậm chí sẽ không chuyển sang Python

bởi vì tôi không có gì để thảo luận ở bài tập một.

Được rồi, bây giờ đến bài tập thứ hai.

Bây giờ chúng ta đến phần lập lịch tốc độ học tập.

Mục tiêu của bài tập thứ hai là tạo ra

và hình dung một bộ lập lịch tốc độ học tập.

Bây giờ bạn sẽ không thực sự tinh chỉnh mô hình

trong bài tập này.

Đây chỉ là về việc thiết lập các thông số

cho bộ lập lịch tốc độ học tập.

Bạn sẽ đào tạo 300 mẫu dữ liệu

và sử dụng mức khởi động 5%, từ đó bạn có thể giảm tuyến tính xuống còn 450 bước.

Đợi một chút, đó có phải là lỗi đánh máy không? Tôi vừa nói rằng bạn tập luyện 300 bước, nhưng không, đây không phải là

lỗi đánh máy. Hãy nhớ lại video trước, đây thực sự là một cách để xác định các thông số cho

bộ lập lịch tốc độ học tập

để nó không giảm xuống mức 0.

Hãy nhớ rằng vấn đề là,

khi bạn sử dụng bộ lập lịch tuyến tính,

khi bạn chỉ định số bước đào tạo,

tốc độ học tập sẽ giảm xuống bằng không

khi kết thúc các bước đào tạo đó

theo tham số mà bạn chỉ định trong bộ lập lịch.

Nhưng ở đây, tôi không muốn bạn để tốc độ học tập

đi đến tận cùng số không.

Vì vậy, bạn thực sự nói với bộ lập lịch tốc độ học tập

rằng có 450 bước,

để khi kết thúc quá trình luyện tập thực sự với 300 bước,

tốc độ học giảm đi, nhưng vẫn ở trên mức 0.

Được rồi, sau đó bạn có thể hình dung tốc độ học tập

trong 300 bước huấn luyện trong một sơ đồ như thế này.

Bây giờ, hãy nhớ rằng khi bạn xác định trình tối ưu hóa

và bộ lập lịch để thiết lập và kiểm tra các thông số này,

bạn sẽ cần xác định lại trình tối ưu hóa

và xác định lại lịch trình

sau khi bạn thực hiện hình dung này.

Ngược lại, khi bạn thực hiện tinh chỉnh thực sự

trong bài tập tiếp theo,

bộ lập lịch, nếu bạn sử dụng cùng một bộ lập lịch

mà bạn sử dụng ở đây để hình dung,

người lên lịch đó sẽ nghĩ rằng bạn đang bắt đầu

hoặc tiếp tục với bước 301.

Vì vậy bạn cần xác định lại các biến

sau khi thực hiện hình dung này.

Được rồi, vậy là xong cho lời giải thích này.

Bây giờ bạn có thể tạm dừng video và thực hiện bài tập này.

Và bây giờ tôi thực sự sẽ chuyển sang Python

và chỉ cho bạn giải pháp của tôi.

Mã này ở đây là để xây dựng mô hình đồ chơi rất đơn giản này.

Nó chỉ là một ma trận trọng số tuyến tính 10 x 10

với tốc độ học tập đã đặt và đây là bộ lập lịch.

Bây giờ điều này thực sự phản ánh số lượng mẫu đào tạo

mà chúng tôi muốn sử dụng trong quá trình tinh chỉnh thực sự,

nhưng những thứ này tôi không quan tâm.

Đây chỉ là để thiết lập các thông số và hình dung nó.

Vì vậy, hãy lưu ý rằng tôi đã tạo một trình tối ưu hóa,

Tôi đã tạo một lịch trình,

nhưng đó chỉ là để thiết lập các thông số

Vì vậy, tôi có thể biết tỷ lệ học tập thực sự sẽ được triển khai như thế nào

trong quá trình đào tạo thực sự.

Đó là lý do tại sao ở đây tôi thiết lập tỷ lệ học tập,

hoặc xin lỗi, lại trình tối ưu hóa và lại lên lịch.

Bây giờ các thông số ở đây cũng giống như trên,

nhưng nó có trình tối ưu hóa mới.

Vậy hãy để tôi chạy nó.

Và bây giờ chúng ta đã sẵn sàng cho bài tập thứ ba.

Mục tiêu của bài tập thứ ba là tinh chỉnh mô hình.

Bạn có thể bắt đầu từ mã từ thử thách mã trước đó với việc phân loại cảm tính của các bài đánh giá phim.

Nhưng có một số điều bạn cần thêm vào.

Trước hết, bạn cần thêm bộ lập lịch tốc độ học tập mà bạn đã phát triển trong bài tập trước.

Và ở đây bạn cũng muốn triển khai việc cắt bớt định mức độ dốc,

và đặc biệt là cắt các gradient bằng cách sử dụng ngưỡng một.

Bây giờ bạn đã có mã cho điều đó từ video trước.

Điều tôi muốn bạn thêm vào đây là lưu trữ các chỉ tiêu độ dốc thực tế từ hai lớp của mô hình

trước khi bạn áp dụng thao tác cắt.

Bạn có thể sử dụng khối biến áp 8 và lớp co MLP

và sau đó là chỉ tiêu độ dốc từ lớp phân loại mà chúng tôi đã thêm ở trên cùng.

Vì vậy, bạn sẽ cần phải tìm ra cách xác định hai lớp đó và lưu trữ định mức ma trận trọng số của chúng trước khi thực sự áp dụng việc cắt định mức gradient.

Bạn có thể vẽ biểu đồ tổn thất và độ chính xác như bạn đã làm trước đây trong thử thách mã trước đó.

Và ở đây bạn có thể sử dụng cùng một mã. Tôi không nghĩ bạn sẽ cần phải thay đổi bất cứ điều gì.

Sau đó, bạn cũng muốn tạo một biểu đồ về các chỉ tiêu và độ dốc của hai lớp mà bạn đã trích xuất.

Bạn có thể vẽ chúng dưới dạng biểu đồ phân tán trong quá trình huấn luyện và bạn cũng có thể thêm một đường ngang vào một đường để biểu thị giá trị cắt.

Chà, khi bạn nhìn vào những đồ thị này, bạn có thể thấy rằng có sự khác biệt trong phạm vi trục y

đối với hai trọng lượng khác nhau này

ma trận từ lớp phân loại cuối cùng mà chúng tôi đã thêm lên trên và

từ lớp MLP mà chúng tôi đang điều tra. Điều này xuất phát từ mô hình BERT được đào tạo trước.

Vì vậy, tôi muốn bạn suy nghĩ thật kỹ về những lựa chọn

chúng tôi đã thực hiện cắt gradient theo lớp cần cắt và theo giá trị ngưỡng.

Vì vậy hãy suy nghĩ xem liệu bạn có nghĩ rằng đây thực sự là một điều thích hợp để làm hoặc liệu bạn có thể làm

một cái gì đó khác biệt. Tôi hy vọng bạn thích làm việc thông qua bài tập này. Bây giờ bạn nên tạm dừng

quay video và bắt đầu làm việc. Và bây giờ tôi sẽ chuyển sang viết mã, thảo luận về giải pháp mã của mình và sau đó cũng

thảo luận một số khái niệm cấp cao về ý nghĩa của việc cắt giảm độ dốc và khi nào nó phù hợp.

Ở đây tôi đang khởi tạo một loạt các biến để lưu trữ tổn thất và độ chính xác từ

tập huấn luyện và tập kiểm tra cũng như các tiêu chuẩn từ hai lớp đó.

Vì vậy, hãy lặp lại quá trình đào tạo 300 đợt.

Ở đây tôi nhận được một loạt dữ liệu.

Di chuyển nó đến GPU.

Hãy xem nào, vâng, đây đều là những thứ tiêu chuẩn.

Tôi nghĩ rằng tôi không thực sự cần phải thảo luận về điều này.

Tôi muốn thảo luận về điều này.

Được rồi, ở đây tôi đang lấy định mức của model.bert.

Đây là mô hình BERT được đào tạo trước

mà chúng tôi đã chèn vào model.encode.layer7 của mình.

Vậy đây là khối máy biến áp thứ tám.

Và sau đó chúng ta nhận được phần đầu ra của khối đó.

tương ứng với lớp co lại.

Vâng, dày đặc là lớp co lại thực sự.

Sau đó là trọng số và sau đó là độ dốc

liên quan đến các trọng số đó.

Được rồi, và sau đó là mục dấu chấm, như bạn đã biết,

chỉ là lấy nó ra khỏi GPU

và cũng tách nó ra khỏi thông tin gradient khác.

Được rồi, vậy tôi có cùng một torch.norm,

nhưng bây giờ là lớp tuyến tính cuối cùng,

bộ phân loại mà chúng tôi đã thêm ở trên cùng.

Được rồi, đó là trước khi tôi áp dụng tính năng cắt chuyển màu.

Ở đây tôi áp dụng việc cắt gradient

với tất cả các tham số của mô hình,

và tôi chỉ định rằng ngưỡng là một.

Như tôi đã đề cập ở video trước,

không cần thiết phải sử dụng giá trị bằng một,

nhưng đó là một giá trị khá phổ biến thường được sử dụng.

trình tối ưu hóa và vì chúng tôi có bộ lập lịch tốc độ học tập,

điều quan trọng cần nhớ là bạn gọi người lên lịch

ngay lập tức hoặc bước qua lịch trình

ngay sau khi bạn bước qua trình tối ưu hóa.

Được rồi, mã này bạn đã thấy trước đây,

về cơ bản cứ 10 mẫu,

Tôi đã chuyển mô hình sang chế độ đánh giá, đánh giá,

tắt tính toán độ dốc,

và sau đó thực hiện chuyển tiếp qua mô hình,

chạy nó thông qua hàm mất mát,

nhận được tổn thất và có được độ chính xác dự đoán.

Vì vậy tôi sẽ chạy qua đoạn mã đó

việc đó sẽ mất vài phút

và sau đó tôi sẽ cho bạn thấy kết quả trông như thế nào.

Vậy 300 kỷ nguyên mất khoảng 5 phút huấn luyện,

nhìn chung không quá tệ.

Và bây giờ hãy vẽ biểu đồ tổn thất và dự đoán chính xác.

bạn sẽ nhớ lại một vài video trước đây

rằng tổn thất và độ chính xác khá khác nhau.

Và tôi đã nói rằng có một vài điều khác nhau

bạn có thể cố gắng để việc học ổn định hơn một chút.

Và bây giờ chúng tôi thấy sự ổn định ngày càng tăng trong quá trình học tập.

Vì vậy, sự thay đổi trong tổn thất nhỏ hơn một chút.

Tôi chỉ dựa trên nhãn cầu trực quan này.

Tôi thực sự không định lượng điều này,

Nhưng chắc chắn có vẻ như mức độ tổn thất là nhất quán hơn,

chúng ít thay đổi hơn trong quá trình đào tạo.

Và độ chính xác dự đoán dường như cũng khá ổn định.

Thực tế, sau khoảng 100 đợt đào tạo,

có vẻ như chúng ta đã đạt đến cấp độ gần như cuối cùng

hiệu suất phân loại.

Cũng không còn biến động như trước nữa.

Rất đẹp.

Vì vậy, đó là về hiệu suất mô hình.

Và bây giờ ở đây chúng ta có thể vẽ đồ thị gradient và chuẩn.

Vì vậy hãy để tôi dành một chút thời gian để giải thích điều này

chi tiết hơn một chút.

Vì vậy, ở đây chúng ta lại có mẫu huấn luyện trên trục x.

Trục y thể hiện định mức thực tế

trước khi chúng bị cắt bớt.

Hãy để tôi quay lại mã

để đảm bảo chúng tôi đang trích xuất thực sự rõ ràng

những giá trị này từ.

Đây là hai ma trận trọng số trong lớp MLP

từ mô hình đã được huấn luyện trước.

Vì vậy, điều này đã được đào tạo trước

và bây giờ chúng tôi đang tinh chỉnh nó.

Và sau đó chúng ta có mô hình phân loại

không được đào tạo trước.

Nó bắt đầu như những con số ngẫu nhiên

bởi vì chúng tôi vừa khởi tạo nó trong mô hình mà chúng tôi đã tạo

ngay trước khi thực hiện việc tinh chỉnh này.

Và tôi nhận được những định mức này trước khi áp dụng

việc cắt độ dốc.

Điều đó có nghĩa là khi chúng ta đến giai đoạn tối ưu hóa,

không có ma trận nào trong mô hình này

có chuẩn gradient lớn hơn một.

Vì vậy, tất cả các giá trị này ở đây phản ánh giá trị cắt trước.

Và chúng ta thấy gì ở đây?

Vì vậy, những gì chúng ta thấy là MLP có một vị trí khá,

độ dốc tương đối thấp, và sau đó đào tạo quá mức

khi mô hình ngày càng tốt hơn,

độ dốc đang bắt đầu thay đổi nhiều hơn một chút

và chúng tôi nhận được khá nhiều mẫu đào tạo

trong đó ma trận trọng số có độ dốc

nó khá lớn,

chỉ ra rằng mô hình cần đào tạo rất nhiều,

như cái này ở đây.

Bây giờ, điểm dữ liệu này có gì đặc biệt?

Chuyện gì đã xảy ra ở đây vậy?

Thật không may, ngay bây giờ chúng tôi không thể nói,

chúng tôi thực sự không có quyền truy cập vào dữ liệu,

Nhưng về nguyên tắc, nếu bạn muốn cứu tất cả

của các đợt đào tạo, bạn có thể xem lại

và có lẽ điều đã xảy ra ở đây là họ chỉ

tình cờ lại có một số ví dụ kỳ lạ

trong tập huấn luyện.

Và người mẫu có chút bối rối.

Ví dụ: giả sử ai đó thực sự đã xếp hạng một bộ phim

như đang ở mức thấp.

Vì thế họ nói rằng họ không thích bộ phim

nhưng bản thân bài đánh giá đã có rất nhiều yếu tố tích cực

hoặc có thể ngược lại.

Có lẽ ai đó thực sự thích bộ phim

nhưng đánh giá của họ rất quan trọng.

Vì vậy, điều đó có thể gây nhầm lẫn trong phân loại mô hình.

Vì vậy, những gì bạn thấy là, vâng, chỉ là những ví dụ này

nơi độ dốc thực sự đã bị cắt bớt

ở giá trị bằng một.

Vì vậy, tất cả những độ lớn gradient này thực sự không bao giờ

đã được sử dụng trong buổi tập huấn.

Thay vào đó, tất cả các giá trị này được chuyển xuống một,

nhưng hầu hết các độ dốc đều ở dưới một.

Nhưng bây giờ chúng ta có được một bức tranh hơi khác

khi chúng ta nhìn vào lớp phân loại ở đây.

Trong lớp phân loại,

bạn có thể thấy điều đó đặc biệt trong giai đoạn đầu đào tạo,

có rất nhiều giá trị,

rất nhiều đợt đào tạo

trong đó giá trị gradient cao hơn đáng kể so với một.

Và điều đó có nghĩa là rất nhiều thông tin

có thể được sử dụng để huấn luyện lớp phân loại

nhanh hơn và hiệu quả hơn thực sự đã bị mất.

Nó không có tác động khủng khiếp như vậy,

mà bạn có thể thấy ở đây,

độ chính xác nhìn chung vẫn khá tốt.

Và cuối cùng độ dốc đã giảm xuống khá ổn định

dưới 0, trên một vài điểm, xin lỗi, một,

một vài mẫu ở đây và ở trên một,

nhưng chủ yếu là dưới một.

Vậy là kết quả cuối cùng cũng không tệ lắm,

nhưng đó là một câu hỏi thú vị

về việc liệu điều này có phù hợp hay không,

chuẩn hóa gradient này là phù hợp

để đặt những trọng lượng ngẫu nhiên này quá sớm trong quá trình tập luyện

nơi trọng lượng thực sự cần phải thay đổi rất nhiều

bởi vì chúng được khởi tạo là ngẫu nhiên.

Bây giờ, một điều bạn có thể làm,

không phải là một phần của bài tập này hoặc thử thách mã này,

nhưng nó không khó để thực hiện,

là bao gồm một ngưỡng.

Vì vậy, ví dụ: giả sử bạn áp dụng

việc cắt định mức độ dốc chỉ khi bạn theo sau,

chỉ sau khi đã thực hiện được 10 hoặc 20% thời gian đào tạo đầu tiên.

đào tạo. Một cái gì đó như thế sẽ cho phép những thông tin cường độ gradient này

tăng tốc độ đào tạo và sau đó khi bạn bắt đầu áp dụng việc cắt bỏ định mức gradient

ở đây có thể ở giá trị 60 nếu bạn muốn thực hiện 20% thì bạn có thể sử dụng phần cắt để đảm bảo rằng

tinh chỉnh ổn định hơn. Chỉ là một suy nghĩ thôi. Vấn đề về LLM là

chúng to lớn, phức tạp và phức tạp. Mỗi bước bổ sung mà bạn học được là, tôi

không biết có nên dùng từ đơn giản không, nhưng ít nhất cũng có thể nắm bắt được như chính nó

chút kiến thức kỹ thuật. Nhưng bạn bắt đầu đặt tất cả những thứ này

cùng nhau và sự phức tạp trở nên quá sức và đáng sợ. Và để làm

vấn đề tệ hơn, phát triển LLM vẫn là một lĩnh vực mới mà chúng tôi không thực sự biết chính xác

điều tốt nhất nên làm trong các tình huống khác nhau với các loại dữ liệu khác nhau và

kiến trúc mô hình khác nhau và như vậy. Tất nhiên, điều đó không có nghĩa và tôi không có ý

để ám chỉ rằng chúng ta chỉ đang loay hoay trong bóng tối. Có một số hướng dẫn tốt về những gì cần làm

làm và tại sao phải làm điều đó, nhưng không có quy trình thực sự nghiêm ngặt nào được thiết lập. Vậy điều đó có nghĩa là

nếu bạn muốn làm việc với LLM, để nghiên cứu hoặc ứng dụng, bạn cần cân nhắc cẩn thận

không chỉ tất cả các lựa chọn riêng lẻ mà còn cả cách các lựa chọn này tương tác với nhau như thế nào.