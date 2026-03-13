# 50 - Phân loại Keras EDA và tiếng Anh tiền xử lý

---

Chào mừng mọi người trở lại, trong loạt bài giảng này, chúng ta sẽ tập trung vào hai điều.

Một là cách thực hiện nhiệm vụ phân loại với dòng tensor.

Thứ hai cũng tập trung vào cách xác định và xử lý Overfitting thông qua việc dừng callback sớm

kỹ thuật, cũng như thêm vào các lớp Drop-Out.

Tất nhiên, việc dừng sớm là điều chúng ta có thể làm để tự động ngừng tập luyện dựa trên tình trạng đã mất,

trên dữ liệu xác thực mà chúng tôi chuyển qua trong mô hình phù hợp với cuộc gọi.

Các lớp thả ra là các lớp có thể được thêm vào để tắt các nơ-ron trong quá trình luyện tập nhằm ngăn chặn tình trạng trang bị quá mức.

Về cơ bản những gì chúng tôi làm là mỗi lớp sẽ loại bỏ hoặc tắt một tỷ lệ phần trăm đơn vị nơ-ron do người dùng xác định trong

lớp trước, từng đợt.

Vì vậy, điều đó có nghĩa là một số tế bào thần kinh nhất định không bị ảnh hưởng về trọng lượng hoặc độ lệch trong một đợt.

Thay vào đó, chúng chỉ bị tắt.

Được rồi, hãy xem tất cả những điều này diễn ra như thế nào bằng cách chuyển sang sổ ghi chép Sao Mộc.

Được rồi.

Tôi đang ở đây với cuốn sổ ghi chép của Jupiter.

Tôi đã tiếp tục nhập số gấu trúc PI, Matplotlib và Seabourne.

Và tập dữ liệu chúng ta sắp làm việc ở đây về cơ bản là một loạt các phép đo khối u

và sau đó phân loại xem chúng là ác tính hay lành tính.

Và hãy tiếp tục tải tập tin này lên.

Chúng ta sẽ nói PD.

Đọc CSFI.

Và sau đó, dưới dữ liệu, chúng tôi sẽ tải tệp lên và nó được gọi là phân loại ung thư, vì vậy bạn

tab có thể tự động hoàn thành từ thư mục dữ liệu.

Và như chúng ta đã biết bên dưới thư mục của Anan, nếu bạn vào sổ ghi chép phân loại của Keri và mở

lên, bạn sẽ có thể cuộn qua phần này và đọc toàn bộ mô tả của tập dữ liệu.

Nó chứa 30 thuộc tính dự đoán số và sau đó là một lớp bổ sung.

Và đó là một tập dữ liệu tương đối nhỏ, khoảng năm trăm sáu mươi chín trường hợp.

Vì vậy, chúng ta sẽ quay lại đây và cùng ra ngoài và thực hiện một chút phân tích dữ liệu thăm dò.

Và sau đó chúng ta sẽ chuyển sang tập trung vào việc dừng các lệnh gọi lại sớm, cũng như thêm vào các lệnh gọi lại đó

các lớp bỏ học.

Vì vậy, điều tôi luôn khuyên bạn nên làm là thực hiện cuộc gọi thông tin nhanh và điều này sẽ giúp bạn thấy

nếu bạn có bất kỳ giá trị null nào ngay lập tức.

Và nếu bạn lướt qua phần này, bạn sẽ nhận thấy tất cả đều là 569.

Vì vậy, không có giá trị nào trong số đó là giá trị rỗng, điều này tốt cho chúng ta.

Và sau đó chúng ta cũng có thể thực hiện lệnh gọi được mô tả để bắt đầu khám phá phân phối thống kê

của các tính năng khác nhau.

Và tôi luôn muốn chuyển đổi nó để dễ đọc hơn một chút với chỉ mục là các tính năng

chính họ.

Được rồi.

Rất nhiều thông tin ở đây chúng ta có thể khám phá.

Hãy tiếp tục và thực hiện một chút phân tích dữ liệu khám phá thông qua trực quan hóa để phân loại

nhiệm vụ.

Bạn nên lập biểu đồ đếm nhãn thực tế của mình để xem số lượng phiên bản trên mỗi nhãn

và xem liệu đó có phải là một vấn đề cân bằng hay không.

Vì vậy cột nhãn được gọi.

Dấu gạch dưới lành tính, số 0, dấu gạch dưới, dấu gạch dưới, cũng có thể gạch dưới một.

Về cơ bản, nó chỉ cho biết lành tính là 0 và ác tính là 1.

Vì vậy, đây là tính năng thực tế hoặc xin lỗi, hãy gắn nhãn và sau đó khung dữ liệu của chúng tôi là D.F..

Chúng ta sẽ tiếp tục và chạy nó.

Và điều này có vẻ tương đối cân bằng.

Vì vậy, chúng tôi chắc chắn có nhiều trường hợp khối u ác tính hơn trong bộ dữ liệu cụ thể này.

Nhưng sự khác biệt ở đây không phải là quá lớn.

Sau đó, những gì chúng tôi có thể làm là kiểm tra mối tương quan giữa các tính năng để bạn có thể nói

F.

Sự tương quan và điều này thực sự sẽ tạo ra một mối tương quan ở đây, và đôi khi điều tốt nên làm là

thực ra chỉ cần xem điều này liên quan đến nhãn mà chúng tôi đang cố gắng dự đoán, một lần nữa, đó là liệu nó có

ác tính hoặc lành tính.

Vì vậy, chúng ta có thể chuyển nó vào.

Và điều đó chỉ cho chúng ta điều này ngay tại đây.

Và trong trường hợp đó, chúng ta có thể nói các giá trị sắp xếp và sau đó chúng ta có thể thấy những gì có mối tương quan dương, cao,

cũng như những gì có mối tương quan tiêu cực cao.

Và đôi khi việc vạch ra điều này thực sự dễ dàng hơn.

Và chúng ta có thể làm điều này bằng cách gọi đơn giản là cốt truyện với phần tiếp theo của cốt truyện dạng thanh.

Bạn cũng có thể làm điều này với Seabourne nếu muốn.

Và hãy chú ý rằng cái cuối cùng ở đây chính là nhãn thực tế, có mối tương quan hoàn hảo

tại một.

Vì vậy chúng ta hãy tiếp tục và bỏ cái đó đi.

Vì vậy, chúng ta sẽ tiếp tục và nói về các giá trị sắp xếp.

Và sau này chúng ta sẽ làm như sau.

Chúng tôi sẽ nói lấy mọi thứ trừ cái cuối cùng.

Và về cơ bản, điều đó sẽ loại bỏ cột nhãn đó, nên có vẻ như chúng ta có các giá trị rất tương quan,

nhưng có mối tương quan nghịch rất cao, nên chúng ta có thể có được những dự đoán khá chắc chắn từ điều này

tập dữ liệu chỉ dựa trên phân tích này ở đây.

Và chúng ta cũng có thể thực hiện một phân tích tương tự về mối tương quan giữa chính các biến thực tế bằng cách gọi

một bản đồ nhiệt.

Tuy nhiên, về mối tương quan này và điều này trả về một bản đồ nhiệt, tuy nhiên, điều này cho bạn thấy mối tương quan với mọi

tính năng so với mọi tính năng khác.

Và nếu nó hơi nhỏ, bạn luôn có thể mở rộng điều này bằng cách nói Kielty figure figure size và sau đó

chọn kích thước lớn hơn 12 x 12 hoặc bất cứ kích thước nào bạn thấy phù hợp.

Vì vậy, đó cũng là điều bạn có thể khám phá.

Bạn cũng có thể thay đổi ánh xạ màu để khám phá thêm điều đó.

Nhưng ngay bây giờ, chúng tôi sẽ tiếp tục và đặt phân tích dữ liệu khám phá sang một bên để chúng tôi có thể bắt tay vào công việc của mình

để phân chia và nhân rộng dữ liệu.

Và sau đó trong phần hai sẽ tập trung vào việc tạo mô hình để xử lý tình trạng trang bị quá mức có thể xảy ra.

Vì vậy, trước tiên, hãy thực hiện bài kiểm tra huấn luyện, phân tách các đặc điểm X, chúng ta sẽ nói F, bỏ đi phần lành tính

cột.

Trên thực tế, họ vẫn nên dán bản sao đó vào đó.

Và sau đó dọc theo trục bằng một.

Và chúng ta sẽ lấy những giá trị đó để nó là trọng tài và sau đó tại sao nó sẽ bằng DF.

Và trong trường hợp này, nó chỉ là cột đó và chúng tôi sẽ lấy những giá trị đó, vì vậy chúng tôi sẽ nói từ Escalon

lựa chọn mô hình và điều này có vẻ rất quen thuộc với bạn bây giờ, tàu đã tách bến.

Đó là cuộc gọi tàu để chia tay.

Hãy tiếp tục và mở rộng chuỗi tài liệu để bạn có thể cuộn xuống đây và lấy ví dụ này.

Hãy sao chép và dán nó ở đây.

Và điều chúng ta sắp làm là thay đổi kích thước thử nghiệm thành kích thước nhỏ hơn một chút vì

chúng tôi không có nhiều điểm như vậy

Chúng tôi sẽ tiếp tục và thay đổi thành chỉ 25% dữ liệu của chúng tôi.

Và để giữ mọi thứ nhất quán, tôi sẽ đặt trạng thái ngẫu nhiên của mình thành một không một.

Tất nhiên đó chỉ là sự lựa chọn tùy ý.

Nhưng nếu bạn muốn nhận được phần chia tương tự, tôi sẽ tiếp tục và chọn cùng một giá trị mà chúng tôi chạy để nhận được

chia tay.

Và cuối cùng, hãy mở rộng quy mô dữ liệu.

Chúng tôi sẽ thực hiện việc này bằng cách sử dụng tính năng tiền xử lý từ Saikat Learn.

Và sau đó chúng tôi sẽ nhập vô hướng tối thiểu tối đa.

Tạo một phiên bản của bộ chia tỷ lệ và chúng tôi sẽ làm như vậy.

Phù hợp, biến đổi.

Dữ liệu huấn luyện của chúng tôi, vì vậy chúng tôi sẽ vào và nói tàu X bằng với việc biến đổi tàu X và chúng tôi sẽ thực hiện

tương tự cho dữ liệu thử nghiệm của chúng tôi.

Rất vô hướng.

Thu hồi thử nghiệm Transform X, chúng tôi không thực sự muốn phù hợp với dữ liệu thử nghiệm, chúng tôi chỉ muốn phù hợp với

dữ liệu đào tạo để ngăn chặn rò rỉ dữ liệu.

Được rồi, chúng tôi đã thực hiện một chút phân tích dữ liệu thăm dò.

Chắc chắn còn rất nhiều điều bạn có thể làm.

Vì vậy, hãy thoải mái tạo các biểu đồ phân tán, các biểu đồ phân phối, v.v., bất cứ điều gì bạn quan tâm.

Và quan trọng hơn, chúng tôi đã tiến hành phân chia thử nghiệm tàu cũng như tiền xử lý để

mở rộng quy mô dữ liệu.

Vì vậy, phần tiếp theo chúng ta sẽ tập trung vào việc tạo mô hình và sau đó chỉ cho bạn cách ngăn chặn việc trang bị quá mức

và làm cách nào để đảm bảo rằng bạn không thực sự sử dụng quá nhiều tập dữ liệu huấn luyện và cuối cùng gặp phải kết quả kém

phù hợp với tập dữ liệu thử nghiệm của bạn.

Vì vậy, chúng tôi cũng sẽ đề cập đến tất cả những điều đó một phần.

Tôi sẽ gặp bạn ở đó.