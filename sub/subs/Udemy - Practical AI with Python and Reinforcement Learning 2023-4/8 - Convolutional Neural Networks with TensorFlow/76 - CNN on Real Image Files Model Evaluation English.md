# 76 - CNN về Đánh giá mô hình tệp ảnh thực

---

Được rồi, vậy chúng ta quay lại sổ ghi chép, chúng ta có mô hình mà chúng ta sắp làm là mô hình dấu chấm

và chúng ta sẽ làm là nói dự đoán, gạch dưới.

Generator và chúng ta sẽ chuyển qua trình tạo hình ảnh thử nghiệm của mình, sau đó hãy tiếp tục và gọi

màu đỏ này để dự đoán, hãy tiếp tục và chạy nó.

Hãy nhớ rằng, việc này thường mất nhiều thời gian hơn so với dự đoán thông thường vì trình tạo phải

thực sự đi vào máy tính của bạn, đọc và mở các tệp hình ảnh này rồi đưa chúng trở lại mô hình của bạn.

Vì vậy, nếu chúng ta nhìn vào kết quả ở đây của Pred, chúng ta sẽ thấy có vẻ hơi lạ, nhưng

về cơ bản bạn sẽ nhận thấy giá trị của chúng nằm trong khoảng từ 0 đến 1.

Vì vậy, nó thực sự không trả lại các cuộc gọi thẳng.

Thay vào đó, nó trả về xác suất.

Vì vậy, bạn biết đấy, ví dụ cuối cùng này là 0,97.

Vì thế chín mươi bảy phần trăm chắc chắn nó thuộc loại một.

Vì vậy, chúng tôi thực sự cần phải làm một bộ.

Dự đoán bằng mức chênh lệch lớn hơn 0,5.

Và điều tuyệt vời ở đây là nếu bạn nhìn lại, những dự đoán của bạn bây giờ, điều này về cơ bản là đúng

và các câu lệnh sai nên các câu lệnh đúng và sai được coi là số không và số một trong trường hợp có nhiều số nguyên.

Vì vậy, chúng tôi có thể thực hiện việc này một cách trực tiếp, chuyển thông tin này vào báo cáo nhầm lẫn, ma trận và phân loại của chúng tôi.

Vì vậy, một lần nữa, hãy nhớ rằng Pred, mặc dù có vẻ như một số trong số đó chỉ là những cuộc gọi đẳng cấp như

0 và 1, chúng thực sự là các giá trị xác suất.

Vì vậy, hãy ghi nhớ điều đó.

OK, và nếu chúng ta xem xét độ dài của thông báo màu đỏ cho toàn bộ tập kiểm tra.

OK, vậy điều chúng ta sắp làm ở đây chỉ đơn giản là nói từ Escalon rằng Matrix nhập một báo cáo phân loại

cũng như một ma trận nhầm lẫn.

Chạy nó rồi tiếp tục in báo cáo phân loại so sánh các câu trả lời đúng của chúng tôi.

nếu bạn muốn có được các lớp thực tế, bạn có thể nói trình tạo hình ảnh thử nghiệm đã lấy các lớp thực tế

và trả về một mảng của các lớp đó.

Vì vậy, đó là lý do tại sao chúng tôi chuyển các giá trị thử nghiệm đó vào và so sánh chúng với dự đoán của chúng tôi.

Việc thu hồi nào là phiên bản được lọc của xác suất dự đoán thực tế?

Vì vậy, chúng tôi sẽ lấy dự đoán của chúng tôi ở đây.

Và đặt chúng vào, để chúng tôi in báo cáo phân loại của mình và bạn sẽ nhận được khoảng 90

phần trăm, có thể ít hơn một chút, nhưng chúng ta có thể thấy ACSI tổng thể của chúng tôi là 87 hoặc thu hồi độ chính xác khá tốt

Nhìn chung, F1 đạt điểm khá gần 90%.

Hãy nhớ rằng, giá trị mặc định sẽ có độ chính xác 50%.

Và thực tế là việc tiết kiệm rất nhiều thời gian thực sự có ích.

Và điều thú vị ở mô hình này là nó mang lại xác suất dự đoán chẳng hạn

bạn muốn triển khai mô hình này trong đời thực và thực sự có được nó.

Tám bác sĩ cho đến nay.

Chúng tôi đang nói rằng nếu chúng tôi chắc chắn hơn 50% rằng dự đoán của chúng tôi bị ảnh hưởng, hãy tiếp tục và

dán nhãn nó là đúng.

Nó bị nhiễm trùng.

Thực ra, chúng ta phải nhìn lại đây và kiểm tra xem cái nào không bị nhiễm thực sự là một.

Vì vậy, các giá trị đi từ 0 đến 1 và không bị nhiễm là một, có nghĩa là nếu nó đúng thì đó là một.

Chúng tôi tin rằng nó không bị nhiễm bệnh.

Vậy điều chúng ta đang nói ở đây là nếu chúng ta nói với xác suất lớn hơn 50 phần trăm thì

nó không bị nhiễm virus, cứ tiếp tục và nói rằng nó không bị nhiễm virus.

Nhưng thực sự, điều này sẽ đóng vai trò như một mô hình hỗ trợ bác sĩ để chúng tôi thực sự có thể thiết lập

ngưỡng cao hơn nếu chúng ta muốn.

Và đây là nơi về cơ bản bạn có thể thực hiện kiểu cân bằng thu hồi chính xác của riêng mình.

Vì vậy bạn có thể nói, được rồi, tôi chỉ muốn báo cho bác sĩ nếu chúng ta chắc chắn 80% hay gì đó

như thế và nhờ bác sĩ tự tay xem xét mọi thứ khác.

Vì vậy, đây là thứ bạn chắc chắn có thể thử.

Và đó là khía cạnh quan trọng cần xem xét trong cuộc sống thực, đặc biệt khi chúng ta nói về những thứ như

quan trọng hơn, lỗi loại một hoặc lỗi loại hai hoặc âm tính giả hoặc dương tính giả.

Và chúng tôi đã thảo luận về tất cả những điều đó cũng như việc học máy trong một phần của khóa học.

Vì vậy, hãy ghi nhớ điều đó.

Dòng này ngay tại đây, mặc dù trông có vẻ vô hại và chỉ là một khoảnh khắc rất ngắn ngủi, nhưng thực ra đây là

có lẽ là một trong những dòng quan trọng nhất trong toàn bộ dự án này vì nó trực tiếp quyết định

đánh đổi việc thu hồi chính xác.

Phải?

Được rồi, vậy là chúng ta có một báo cáo phân loại và chúng ta cũng có thể thực hiện một ma trận nhầm lẫn nếu muốn, chúng ta

về cơ bản có thể nói ma trận nhầm lẫn trong bộ dữ liệu này ngay tại đây.

Hãy tiếp tục.

Chỉ cần sao chép và dán nó và chúng ta có thể thấy có bao nhiêu phân loại sai.

Được rồi, sau khi chúng ta thực sự xem xét điều đó, hãy tiếp tục và chỉ cho bạn cách dự đoán trên một

hình ảnh.

Nếu chúng ta nhìn vào Paracel, đây chỉ là một hình ảnh duy nhất và tôi thực sự có thể cho bạn xem hình ảnh đó bằng cách tải lên

từ quá trình tiền xử lý Keris, chúng ta có thể nói từ luồng cảm biến mang đến việc dừng tiền xử lý hình ảnh quan trọng

chức năng.

Và điều thú vị ở đây là chức năng hình ảnh thấp thực sự được tích hợp vào

lều trước đây chúng tôi sử dụng matplotlib, nhưng chúng tôi thực sự có thể làm điều này với PARACEL này vì vậy chúng tôi

có thể nói hình ảnh tải hình ảnh và nó thực sự hiển thị một hình ảnh.

Và nếu chúng ta kiểm tra loại kết quả này sẽ trả về.

Nó đang quay trở lại loại tệp hình ảnh pelo đặc biệt, vì vậy hãy ghi nhớ điều đó, thực tế không phải vậy

một mảng, nó chỉ là một loại tệp hình ảnh chuyên dụng.

Chà, chúng ta sắp làm ở đây điều thú vị về việc hạ thấp.

Hình ảnh không chỉ giúp chúng tôi cung cấp đường dẫn mà còn có thể cho biết kích thước mục tiêu của tôi là bao nhiêu?

Và trong trường hợp này, tôi có thể định hình lại.

Bằng cách nói rằng kích thước mục tiêu của tôi bằng với hình dạng hình ảnh ban đầu đó, tôi xác định 30 x 1, 30 x 3,

vì vậy chúng ta sẽ tiếp tục và nói đây là hình ảnh của tôi.

Và nếu chúng ta nhìn vào hình ảnh của tôi, cuốn sổ thực sự hiển thị nó, vì vậy chúng ta nghĩ về điều này

tình hình thế giới, những gì đang thực sự xảy ra.

Về cơ bản, bác sĩ sẽ gửi email cho chúng tôi tập tin này.

Chúng ta sẽ tiếp tục huấn luyện mô hình của mình hoặc tải lên mô hình đã tồn tại.

Và bây giờ chúng tôi đã nhận được email của tệp PMG này.

Chúng tôi sẽ tải nó với hình ảnh lệnh này.

Hình ảnh tải đó sẽ kiểm tra kích thước mục tiêu của chúng ta, hình dạng hình ảnh.

Và chúng tôi luôn có thể nói nếu chúng tôi muốn lập mô hình tóm tắt đó, hãy chạy nó và chúng tôi có thể kiểm tra mô hình

mà chúng tôi đang làm việc ở đây.

Và sau đó điều chúng ta sẽ làm là đọc hình ảnh này và chuyển nó cho mô hình, vậy làm thế nào

chúng ta có thực sự làm điều này không?

Tốt.

Nếu chúng ta nói.

Hình ảnh có một IMG thành mảng thực sự biến đổi hình ảnh, đối tượng chuyên biệt này thành một mảng.

Vì vậy, tôi sẽ nói mảng hình ảnh của mình và bây giờ tôi có hình ảnh gốc của mình, trông khá rõ ràng là nó bị nhiễm virus

đưa ra thiết kế và bây giờ nó thực sự là lấy.

Mảng hình ảnh của tôi và chúng ta đã có nó rồi, chúng ta sẽ tiếp tục và kiểm tra

hình dạng.

Tôi nhận thấy nó là 1 30 x 1, 3 x 3, vì vậy điều tôi sắp làm ở đây chỉ đơn giản là thay đổi kích thước cái này theo

chiều không và tôi có thể làm điều đó bằng nhiều cách.

Tôi có thể định hình lại hoặc điều tôi có thể làm là tôi có thể nói không.

Và nó có chức năng kích thước mở rộng này về cơ bản có nghĩa là lấy hình ảnh hiện tại và

mở rộng nó để nó có một hình ảnh mới dọc theo trục bằng 0.

Mục đầu tiên đó, bởi vì thực sự những gì tôi muốn hình dạng này trông giống như từng hình một, 30 x

một, ba kênh màu ba vì mô hình mong đợi hàng loạt hình ảnh.

Ngay cả khi đó chỉ là một hình ảnh, nó cũng cần biết rằng đó là một loạt hình ảnh.

Vì vậy, hãy tiếp tục và đọc phần phạt có nội dung mảng hình ảnh của tôi.

ngang bằng với anh chàng này.

Bây giờ chúng tôi kiểm tra hình ảnh của tôi, kiểm tra hình dạng của nó, từng cái một, 30 cái một, ba cái ba.

Bây giờ nó đã sẵn sàng để một mô hình dự đoán.

Chúng tôi đang dự đoán dựa trên một hình ảnh duy nhất chứ không phải từ một trình tạo.

Vì vậy, bây giờ tôi chỉ có thể thấy dự đoán mô hình chạy hình ảnh của mình và nó dự đoán nó bằng 0.

Việc thu hồi nào?

Nếu chúng ta xem lại các chỉ số lớp, chúng ta có thể thực hiện việc này bằng cách sử dụng trình tạo hoặc kiểm tra hình ảnh tàu hỏa

chúng dưới dạng chỉ mục lớp cuộc gọi của trình tạo, nó tin rằng đây là một tế bào ký sinh.

Và rõ ràng là như vậy.

Trên thực tế, đó là hình ảnh đầu tiên chúng ta nhìn thấy trước đây.

Được rồi, vậy là xong cho dự án này.

Tôi hy vọng bạn đã có rất nhiều niềm vui.

Và tôi hy vọng bây giờ bạn khám phá bộ dữ liệu hình ảnh của riêng mình và bắt đầu huấn luyện nó để phân loại của riêng bạn

vấn đề.

Cảm ơn.

Và tôi sẽ gặp bạn ở phần tiếp theo của khóa học.