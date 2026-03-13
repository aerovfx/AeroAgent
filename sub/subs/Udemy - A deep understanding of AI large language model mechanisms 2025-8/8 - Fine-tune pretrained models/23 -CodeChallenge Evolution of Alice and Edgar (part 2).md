# 23 -CodeChallenge Sự tiến hóa của Alice và Edgar (phần 2)

---

Video này là phần cuối của thử thách viết mã

mà chúng tôi đã bắt đầu phát triển trong video trước.

Vì vậy, bạn chắc chắn cần phải trải qua

video trước để bắt đầu làm việc với video này.

Bạn sắp huấn luyện mô hình Alice và Edgar

trên các văn bản tương ứng của họ,

như bạn đã làm trước đây trong phần này.

bạn có thể sử dụng 121 mẫu đào tạo

và tỷ lệ học từ 10 đến âm 5.

Vì vậy, đây là một tinh chỉnh rất nhẹ nhàng.

Chúng tôi không muốn đào tạo quá nhanh

và chúng tôi không muốn trang bị quá nhiều cho những văn bản này.

Cứ 10 mẫu, bạn có thể tính toán phân loại BERT

và viết báo cáo.

Nó sẽ trông giống như thế này.

Vì vậy, ở đây chúng tôi in ra những tổn thất

cho mô hình Alice và Edgar,

và đây là độ chính xác của phân loại BERT.

Tất nhiên, độ chính xác bắt đầu vào khoảng 50%,

và câu hỏi là chuyện gì xảy ra

khi chúng ta tiến bộ thông qua học tập?

Bây giờ, về mặt lý thuyết, bạn có thể đánh giá

độ chính xác phân loại BERT

trên mỗi mẫu trong số 121 mẫu huấn luyện.

Vấn đề là việc tạo ra một loạt dữ liệu

và để Bert thực hiện việc phân loại mất khá nhiều thời gian.

Vì vậy, nếu bạn đánh giá thường xuyên hơn,

sau đó toàn bộ vòng đào tạo chỉ bắt đầu

phải mất một thời gian thực sự dài.

Mặt khác, với những thông số mà tôi thiết lập,

toàn bộ vòng huấn luyện này nằm trong tay tôi,

với GPU mà tôi đã sử dụng, khoảng năm phút.

Vì vậy, nó không thực sự khủng khiếp.

Tôi đoán nó phụ thuộc vào mức độ kiên nhẫn của bạn.

Được rồi, sau đó bạn muốn hình dung kết quả

bằng cách hiển thị sự mất mát từ các mô hình sinh eluthor

rằng bạn thực sự đang đào tạo

và hiển thị độ chính xác phân loại BERT

như một chức năng của đợt đào tạo.

Bây giờ, trước khi tôi yêu cầu bạn tạm dừng video,

Tôi muốn nói vài lời về quản lý bộ nhớ

và có ba mô hình cùng rất nhiều dữ liệu

trong phiên Colab của bạn.

Google Colab là một dịch vụ tuyệt vời

và tôi thực sự biết ơn vì chúng tôi có thể truy cập

GPU mạnh mẽ trực tuyến miễn phí hoặc với mức giá khiêm tốn.

Nhưng mặt khác, GPU mà chúng tôi có

không hẳn là siêu đỉnh của dòng.

Các GPU khác nhau có dung lượng RAM khác nhau

nhưng nhìn chung chúng ở đâu đó khoảng 20 đến 40 hợp đồng biểu diễn.

Tôi thấy rằng tôi không thể chạy mã này trên GPU L4

bởi vì cái đó chỉ có 22 GB RAM.

Vì vậy tôi đã sử dụng GPU A100,

vào thời điểm tôi ghi lại, nó có sẵn 40 hợp đồng biểu diễn.

Bạn có thể theo dõi lượng bộ nhớ bạn đang sử dụng

bằng cách nhấp vào biểu tượng này ở trên cùng bên phải

của màn hình CoLab của bạn.

Nếu bạn đang gặp vấn đề về bộ nhớ,

bạn có thể thử xóa các biến không sử dụng,

bạn có thể thử giảm kích thước lô,

và nếu bạn đang viết, kiểm tra và khám phá mã,

thì có lẽ bạn đã tạo ra rất nhiều

nhưng sau đó các biến không được sử dụng trôi nổi xung quanh.

Vì vậy, bạn cũng có thể thử thỉnh thoảng khởi động lại phiên

để xóa tất cả các biến của bạn

mà bạn không sử dụng nữa.

Chỉ cần nhớ rằng khi bạn khởi động lại phiên,

mọi thứ đều bị xóa, mọi thứ đều bị xóa,

vì vậy bạn cần nhập lại các thư viện,

chạy lại mã trước đó, vân vân, vân vân.

Được rồi, tôi hy vọng bạn thích bài tập này,

và tôi hy vọng bạn đang mong chờ

để xem bộ phân loại làm gì với hai mô hình này

vì chúng đang được tinh chỉnh.

Và bây giờ tôi sẽ chuyển sang mã.

Ở đây tôi xác định hai trình tối ưu hóa.

Tất nhiên, đó chính xác là cùng một trình tối ưu hóa,

nhưng đối với mô hình Edgar và mô hình Alice.

Và đây là quá trình đào tạo.

Để tôi xem nào, tôi thực sự đã bắt đầu chạy cái này rồi.

Vậy hãy xem, tất cả những điều bạn đã thấy trước đây,

Tôi nhận được một loạt token Alice ngẫu nhiên

từ cuốn sách của Alice, và tôi đang thực hiện chuyển tiếp,

tính toán tổn thất và nhận lại chỗ dựa

cho mô hình Alice.

Mã này ở đây hoàn toàn giống với mã ở trên này,

chỉ thay thế tất cả các biến cho Alice thay vì Edgar.

Và sau đó cứ mỗi mẫu thứ 10,

Tôi tạo một lô cho Berts.

Bạn có thể thấy mũi tên nhỏ màu xanh lá cây này bị kẹt trên dòng này.

Vậy chỉ riêng dòng này thôi, tôi không biết là bao nhiêu giây,

chỉ có vài giây, nhưng nó thực sự bắt đầu cộng lại

bạn càng muốn đánh giá hiệu suất thường xuyên hơn.

Và sau đó tôi sử dụng torch.nograd.

Điều này sẽ giúp giảm thời gian tính toán một chút

bằng cách tắt bất kỳ tính toán độ dốc nào.

Vì vậy, sau đó tôi chạy phân loại

và ở đây tôi chỉ nhận được các nhãn được dự đoán

và độ chính xác.

Bây giờ, trong trường hợp này, tôi thực sự không tính toán

và lưu trữ khoản lỗ từ mô hình Bert.

Tôi có mã để làm điều đó từ bài tập trước.

Nếu bạn muốn bao gồm điều đó

và xem sự mất mát của mô hình Barrett là gì,

thì được thôi, bạn có thể làm được điều đó,

nhưng tôi không làm điều đó ở đây.

Được rồi, sau đó tôi sẽ báo cáo điều đó.

Vậy hãy xem, tôi sẽ tạm dừng ghi âm

và hẹn gặp lại bạn sau giây lát.

Vậy là mất khoảng bốn phút,

và bạn có thể thấy rằng sự phân loại của Barrett

bắt đầu ở mức 50% và tăng lên khoảng 90%.

Chúng ta hãy xem những kết quả này trông như thế nào.

Vì vậy, ở đây chúng ta thấy những tổn thất đối với các mô hình tổng quát.

Và tôi đã đề cập trước đó,

khi chúng tôi làm việc với những mô hình tinh chỉnh này trước đây,

rằng con số ở đây, giá trị này, nó sẽ giảm xuống,

nhưng nó không thực sự rõ ràng

con số sẽ giảm xuống bao nhiêu.

Nếu con số này giảm dần về 0,

thì có lẽ chúng ta đang tập luyện quá mức

trên tập dữ liệu tinh chỉnh,

điều mà chúng ta thường không muốn.

Vì vậy, việc sử dụng bộ phân loại

là một cách tiếp cận thay thế thú vị

để định lượng hiệu suất của hai mô hình này,

những mô hình tinh chỉnh này.

Vì vậy, ý tưởng là nếu mô hình phân loại BERT

có thể dự đoán với độ chính xác 90%,

phong cách nào đang được tạo ra bởi hai mô hình này ở đây,

thì chúng ta có thể coi khóa đào tạo này là một thành công,

bất kể sự mất mát trông như thế nào.

Bây giờ, hãy nhớ rằng bộ phân loại này

được đào tạo về các văn bản thực tế,

vậy nên những cuốn sách thực sự từ Through the Looking Glass

và những bài thơ của Edgar Allan Poe.

Dữ liệu mà nó thực sự đang phân loại

không đến từ những văn bản đó.

Nó được tạo ra bởi hai mô hình này

và hai mô hình này đã được đào tạo về hai cuốn sách đó.

Vì vậy không có gì vòng tròn hay thiên vị cố hữu

về sự đánh giá này, sự định lượng này

về hiệu quả hoạt động của hai mô hình này.

Nó thực sự là một thiết lập thực sự tốt đẹp.

Đó là một cách hay để đánh giá các mô hình tổng quát.

Chà, đó thực sự là một thử thách về mã.

Tôi hy vọng bạn cảm thấy bộ não của mình được mở rộng thêm một chút

từ những bài tập này và từ toàn bộ phần này.

Tôi đã đề cập trước đó

rằng việc đánh giá các mô hình tổng quát thực sự rất khó khăn.

Nghe có vẻ rất hay khi sử dụng mô hình thứ ba

để định lượng hiệu suất tổng hợp của hai mô hình khác.

Và nói chung, đó là một con đường đầy hứa hẹn

của nghiên cứu và ứng dụng.

Nhưng vấn đề là cách tiếp cận như vậy

cũng có thể mang lại cảm giác tự tin sai lầm

khi nó không hoạt động hoàn hảo.

Một ví dụ rõ ràng về điều này là các mô hình ngôn ngữ

được thiết kế để phát hiện liệu, ví dụ,

một báo cáo mà một sinh viên nộp cho một lớp

được viết bởi con người hoặc bởi AI.

Bạn có thể đã từng gặp những cuộc thảo luận như thế này trên mạng,

nhưng về cơ bản những máy dò AI này hoạt động không tốt lắm.

Họ sẽ gắn nhãn văn bản viết bằng AI là con người

và văn bản do con người viết dưới dạng AI.

Vì vậy, việc có một mô hình phân loại văn bản,

nó có thể là một giải pháp tuyệt vời cho một số loại vấn đề,

nhưng nó không phải là một giải pháp phổ biến.