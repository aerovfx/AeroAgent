# 11 -CodeChallenge Tinh chỉnh và đóng băng có mục tiêu (phần 2)

---

Đây là phần tiếp theo của thử thách viết mã mà chúng ta đã bắt đầu ở video trước.

Bạn chắc chắn cần phải trải qua những bài tập đó để bắt đầu với video này.

Bây giờ là bài tập thứ tư.

Cái này thú vị hơn vì nó chỉ liên quan đến việc viết nhiều mã Matplotlib để trực quan hóa

kết quả mà bạn đã thu thập được.

Bạn có thể bắt đầu bằng cách vạch ra những tổn thất.

bạn có thể vẽ biểu đồ tổn thất cho mô hình cố định

và mô hình có thể đào tạo đầy đủ.

Và ở đây bên phải, tôi có một biểu đồ phân tán

tổn thất của mô hình cố định trên trục x

so với mô hình có thể huấn luyện hoàn toàn trên trục y.

Bây giờ hãy nhớ rằng hai mô hình này bắt đầu giống hệt nhau

và họ được đào tạo về cùng một dữ liệu

theo đúng thứ tự như vậy.

Vì vậy, thật thú vị khi so sánh trực tiếp tổn thất của họ.

Tiếp theo, bạn có thể vẽ biểu đồ thanh

về tần suất tạo mã thông báo từ hai mô hình này

được lấy mẫu từ các token Moby Dick phổ biến nhất.

Đây chính xác là biểu đồ thanh mà tôi đã trình bày trong bài tập một.

Vì vậy ở đây bên phải chỉ là sự khác biệt

giữa bài trừ đào tạo trước.

bạn có thể thấy cả hai mô hình đều có sự thay đổi tích cực.

Vì vậy tỷ lệ token được chọn lớn hơn

sau khi tinh chỉnh ở cả hai mô hình.

Và câu hỏi đặt ra là mô hình nào trong số này

có tỷ lệ mã thông báo được tạo cao hơn.

Tiếp theo, bạn nên vẽ một biểu đồ thanh

về thời gian tính toán tích lũy của hai mô hình.

Và điều này sẽ rất thú vị để đánh giá

Xem xét khiếu nại của tôi trong video trước

việc đóng băng trọng lượng đôi khi được thực hiện

nhằm mục đích thực tế nhằm đẩy nhanh thời gian đào tạo.

Bây giờ, đồ thị cuối cùng ở đây là chuẩn sai phân ma trận

mà bạn đã tính toán bên trong vòng đào tạo.

Nếu bạn có nền tảng đại số tuyến tính

và bạn đã quen với việc diễn giải các chuẩn mực ma trận,

sau đó tôi muốn bạn đưa ra một giả thuyết

về những mẫu bạn mong đợi thấy ở đây.

Nếu bạn không có nền tảng đại số tuyến tính vững chắc

và khái niệm chuẩn mực không quá quen thuộc với bạn,

thì đừng lo lắng về điều đó.

Chỉ cần lên cốt truyện rồi mình sẽ bàn cách diễn giải

khi tôi chuyển sang mã.

Dù sao bây giờ bạn nên tạm dừng video

và quay lại và xem tôi thảo luận về kết quả của mình.

Vì vậy, đầu tiên, âm mưu của những mất mát.

Đây bạn thấy đấy, hãy để tôi phóng to một chút ở đây.

Điều này khá thú vị.

Vì vậy, chúng ta thấy rằng mô hình có thể huấn luyện đầy đủ

có những khoản lỗ có mức giảm mạnh hơn nhiều

và tổn thất cuối cùng thấp hơn nhiều.

Mô hình đóng băng, không hoàn toàn bị đóng băng,

nhưng chủ yếu là bị đóng băng, nó học được một chút.

Những tổn thất giảm xuống.

Hãy để tôi xem con số thực tế là gì.

Vì vậy, tổn thất giảm từ 3,78 xuống còn 2,65.

Vì vậy, bạn biết đấy, nó có giảm đi một chút,

nhưng gần như không ấn tượng bằng đường màu xanh

đối với mô hình có thể đào tạo đầy đủ.

Tất nhiên điều đó không có gì đáng ngạc nhiên,

nhưng chúng ta có thể đặt câu hỏi quan trọng

trong đó một trong số này là tốt hơn.

Nếu bạn đã nghiên cứu deep learning để phân loại,

để phân loại, thì bạn có thể nói,

ừ, rõ ràng là đường màu xanh tốt hơn

bởi vì tổn thất là rất lớn và chúng tôi muốn giảm thiểu chúng.

Nhưng mặt khác, đối với một mô hình tổng quát,

khi chúng tôi tinh chỉnh, nó không thực sự rõ ràng

rằng giảm thiểu tổn thất nhất thiết phải là cách tốt nhất

để đánh giá mô hình.

Tất nhiên, chúng tôi muốn tổn thất nhỏ

và giảm trong suốt quá trình tinh chỉnh,

nhưng thực sự điều mọi người muốn có những mô hình sáng tạo cho

là tạo ra văn bản.

Và những con số này không cho chúng ta biết về mô hình

tính mạch lạc và nhạy cảm khi tạo ra văn bản.

Ở đây bạn cũng thấy rằng sự mất mát đào tạo

thực sự bắt đầu cao hơn.

Và thực sự ngay từ đầu chúng giống nhau.

Nhưng tổn thất huấn luyện đối với mô hình có thể huấn luyện đầy đủ

đã cao hơn một chút.

Và lý do cho điều đó là toàn bộ mô hình,

mọi tham số trong mô hình,

mọi tham số có thể huấn luyện trong mô hình

đang được điều chỉnh và chuyển dịch và thay đổi và thích nghi.

Và thực ra mô hình này đang thay đổi rất nhiều

ngay từ đầu,

trong khi mô hình đóng băng chỉ thay đổi một chút rất nhỏ

nên lúc đầu tập sẽ ổn định hơn một chút.

Ở đây trong biểu đồ phân tán này, chúng ta có mô hình đóng băng,

mô hình bị đóng băng một phần trên trục X

và mô hình có thể huấn luyện đầy đủ trên trục Y.

Và đường thống nhất ở đây cho chúng ta biết

rằng bất cứ điều gì dọc theo dòng này sẽ giống hệt nhau.

Vì vậy, ví dụ: nếu chúng tôi không đóng băng bất kỳ mô hình nào

và chúng tôi vừa có hai bản sao giống hệt nhau của mô hình,

chúng ta mong đợi tất cả những dấu chấm này nằm trên đường chéo.

Và việc chúng không nằm trên đường chéo cho chúng ta biết

rằng có những động lực khác nhau giữa chúng.

Và đặc biệt, bất cứ thứ gì nằm dưới đường chéo

cho chúng ta biết rằng mô hình đóng băng có tổn thất cao hơn

và bạn thấy ở đây, ví dụ,

khi mô hình đóng băng có mức lỗ là 3,

mô hình xe lửa bị lỗ hai, trên hai một chút.

Vì vậy, đây là mô hình đóng băng nói chung

có tổn thất cao hơn mặc dù dữ liệu huấn luyện

giống hệt nhau.

Và ở đây, những điểm này là nơi mô hình xe lửa,

mô hình có thể huấn luyện hoàn toàn có tổn thất lớn hơn

so với mô hình đóng băng

Và vâng, như tôi đã đề cập,

tương ứng với sự khởi đầu ở đây.

Được rồi, đó là phần thua lỗ.

Đây là mã hoàn thiện ngẫu nhiên,

bắt đầu gieo hạt với số ngẫu nhiên để tạo ra một số mã thông báo.

Bạn sẽ nhớ rằng lúc đầu,

con số này là khoảng 44 và 47%.

Và bây giờ hãy xem họ đang làm gì ở đây.

Được rồi, chúng ta thấy rằng các thanh màu cam trong cả hai trường hợp

lớn hơn các thanh màu xanh.

Và điều đó cho chúng ta biết rằng cả hai mô hình này

thực sự đang chọn nhiều token hơn từ Moby Dick

sau khi tinh chỉnh so với trước đây.

Và thực tế chúng tôi thấy tỷ lệ đó cao hơn

đối với mô hình đông lạnh hơn là mô hình xe lửa

mà bạn cũng thấy ở đây.

Đây thực sự không phải là một kết quả được mong đợi.

Và tôi nghĩ nó chỉ phản ánh sự thật

rằng có sự ngẫu nhiên nào đó ở đây.

Có lẽ điều này sẽ hơi khác một chút

nếu tôi sử dụng nhiều mã thông báo hơn để tạo.

Hãy thử chạy lại cái này.

Điều này có vẻ khá nhất quán.

Được rồi, đây thực sự không phải là một hướng đi được mong đợi

của hiệu ứng.

Tôi đã mong đợi mô hình có thể đào tạo hoàn toàn

để có token cao hơn từ Moby Dick

so với mô hình đông lạnh một phần.

Có lẽ đó là những gì bạn tìm thấy.

Và vâng, ý tôi là, điều này phản ánh bản chất

lấy mẫu ngẫu nhiên và hoạt động ngẫu nhiên.

Được rồi, vậy hãy xem nào.

Bây giờ chúng ta muốn xem trọng lượng đã thay đổi như thế nào.

Vì vậy, ở đây chúng tôi nhận được hai ô đường

và chúng tôi thấy rằng chúng bắt đầu ở mức rất cao.

Chúng giảm mạnh và đang dần tăng trở lại.

Vậy điều này cho chúng ta biết điều gì?

Điều này cho chúng ta biết rằng ma trận trọng số,

hãy nhớ rằng đây chỉ là một ma trận trọng số

từ một khối chú ý,

nó đang thay đổi rất nhiều ngay từ đầu.

Vì vậy, ngay trong vài lần lặp lại huấn luyện đầu tiên,

ma trận này thực sự đang thay đổi rất nhiều.

Và rồi nó ngừng thay đổi,

hoặc nó không ngừng thay đổi,

nhưng nó thay đổi chậm hơn nhiều,

điều đó có nghĩa là rất nhiều kiến thức chính

đã diễn ra rồi.

Bây giờ, thực tế là đường màu xanh nằm phía trên đường màu cam,

và đường màu xanh tương ứng với mô hình gần như bị đóng băng,

đường màu cam tương ứng với mô hình có thể huấn luyện đầy đủ,

điều này chỉ ra rằng hầu hết những thay đổi trong mô hình

đang diễn ra trong các lớp này và vẫn có thể huấn luyện được.

Điều đó không có gì đáng ngạc nhiên.

Vì vậy, mô hình thực sự cần phải cố gắng điều chỉnh trọng số của nó

để dự đoán tốt nhất các mã thông báo tiếp theo.

Và làm sao nó có thể làm được điều đó?

Vâng, trong mô hình có thể đào tạo hoàn toàn,

có 124 triệu thông số cần huấn luyện,

nhưng trong mô hình gần như bị đóng băng, có,

Tôi không đếm chúng ở đây,

chúng ta sẽ làm điều đó trong bài tập sau,

nhưng có, tôi không biết,

có thể là vài triệu tham số

liên quan đến hàng trăm triệu tham số

điều đó không thể đào tạo được.

Vậy những ma trận chú ý này

thực sự đang làm tất cả những công việc nặng nhọc,

họ thực sự phải điều chỉnh để dự đoán tốt nhất

những token này.

Và cuối cùng, chúng ta có thể nhìn vào thời gian đào tạo.

Chúng tôi không thấy có gì ngạc nhiên ở đây về tổng thời gian đào tạo.

Vì vậy, đây không phải là cho một lần lặp.

Đây là tổng của gần 500 lần lặp.

Đối với mô hình gần như bị đóng băng, thời gian này là khoảng 89 giây,

đại loại như thế, một phút rưỡi.

Và đối với mô hình có thể đào tạo hoàn toàn,

đã gần hai phút rồi.

Vì vậy, chúng tôi thực sự tiết kiệm được rất nhiều thời gian tính toán.

Mặt khác, hãy nhớ rằng rất nhiều

của phép tính, thời gian tính toán liên quan

trong quá trình đào tạo một mô hình ngôn ngữ lớn xuất hiện

từ việc chuyển tiếp, nó xuất phát từ việc tính toán tổn thất

và chỉ có rất nhiều chi phí.

Vì vậy, việc đóng băng rất nhiều mô hình sẽ giúp ích.

Nó làm giảm thời gian tính toán,

nhưng nó không phải là một hiệu ứng lớn.

Bài tập năm có thể được thực hiện bằng cách thay đổi theo nghĩa đen

hai đoạn mã nhỏ xíu.

Tất cả những gì bạn cần làm là đảo ngược khả năng huấn luyện

và lọc tham số cố định.

Vì vậy, bây giờ bạn sẽ đào tạo gần như toàn bộ mô hình

và chỉ đóng băng các ma trận chú ý

trong các khối máy biến áp sau này.

Khi bạn thực hiện thay đổi nhỏ đó,

sau đó bạn có thể chạy lại toàn bộ mã

và xem kết quả khác nhau như thế nào ở đây

so với những gì bạn thấy ở bài tập 4.

Vì vậy bây giờ bạn nên tạm dừng video và xem

và bây giờ tôi sẽ chuyển sang mã.

Tất cả những gì chúng ta cần làm cho bài tập năm

thay đổi điều này đúng thành sai

và thay đổi sai này thành đúng.

Bây giờ điều đó rất dễ thực hiện.

Nếu bạn chạy lại mã này,

bạn vẫn sẽ nhận được kết quả khó hiểu

bởi vì tôi thực sự đã không cập nhật văn bản này.

Vì vậy, điều này nói là đông lạnh, mặc dù nó thực sự đúng.

Vì thế đừng để ý tới điều này.

Tôi thậm chí sẽ loại bỏ hoàn toàn điều đó.

Khi bạn đã hoán đổi hai Boolean này,

nó đơn giản như nhấp vào chạy tất cả.

Được rồi, tôi đã chạy lại toàn bộ mã.

Ở đây chúng ta thấy rằng các cấu hình tổn thất trông gần giống nhau.

bạn phải phóng to để thấy rằng thực sự có

ở đây có hai dòng

Và bạn có thể thấy rằng bây giờ gần như tất cả những mất mát này

về cơ bản là trên đường thống nhất,

không chính xác theo nghĩa đen bởi vì vẫn còn một số

sự khác biệt giữa các mô hình,

nhưng chúng hầu như thực sự, thực sự, thực sự giống nhau.

Được rồi, vậy chúng ta mong đợi mọi thứ khác

về cơ bản là giống nhau.

Và vâng, bây giờ đây thực sự là đường màu xanh này

thực sự không còn thú vị nữa để xem xét

bởi vì đây là ma trận trọng số

điều đó bây giờ thực sự đã bị đóng băng.

Vì vậy, thực tế là đường màu xanh hoàn toàn bằng 0

thực chất chỉ là xác nhận

rằng mô hình này thực sự đã bị đóng băng.

Và thời gian tính toán vẫn có một chút khác biệt.

Vì vậy, mặc dù chúng tôi chỉ đào tạo một người đóng băng

một vài lớp trong mô hình,

nó không thực sự thay đổi hiệu suất tổng thể,

ít nhất là về sự mất mát.

Và chúng tôi vẫn lưu, tôi không biết, có lẽ là năm giây.

Một mặt, năm giây không phải là nhiều,

nhưng bạn có thể tưởng tượng việc mở rộng khoản tiết kiệm thời gian đó

cho một mô hình lớn hơn nhiều, và bạn đang đào tạo, bạn biết đấy,

có thể hàng trăm ngàn mẫu dữ liệu

thay vì chỉ vài trăm như chúng tôi đã làm ở đây.

Tôi nghĩ rằng từ việc vượt qua thử thách mã này,

bạn thực sự có thể hiểu ý tôi ở video trước

khi tôi nói rằng việc đóng băng có chủ đích đều thực sự dễ dàng

và rất khó khăn.

Có rất nhiều khả năng và rất nhiều lựa chọn

và nó không thực sự rõ ràng

cách thiết lập giao thức đóng băng.

Mặt khác, có một số hướng dẫn hợp lý

lớp nào sẽ bị đóng băng và tại sao,

và tất cả những hướng dẫn đó đều đến từ nghiên cứu

về khả năng diễn giải cơ học.

Vì vậy tôi nghĩ rằng sự không chắc chắn

với mục tiêu đóng băng và tinh chỉnh

sẽ cải thiện theo thời gian vì có nhiều hơn

nghiên cứu về khả năng diễn giải đang được công bố.