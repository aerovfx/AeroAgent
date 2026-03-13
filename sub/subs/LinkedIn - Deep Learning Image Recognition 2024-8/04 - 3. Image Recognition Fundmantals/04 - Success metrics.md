# 04 - Thước đo thành công

---

- Vì vậy, chúng tôi đang xây dựng những mô hình học sâu này,

nhưng chúng ta đo lường sự thành công như thế nào?

Vì vậy, trong phiên này,

chúng ta sẽ xem xét các thước đo thành công và chúng đòi hỏi những gì,

loại thông tin họ đang cung cấp cho chúng tôi,

những lợi thế là gì

và nhược điểm của việc chọn thước đo thành công XYZ.

Vì vậy, trước hết, hãy kiểm tra độ chính xác.

Tỷ lệ hình ảnh được phân loại chính xác

tổng số hình ảnh trong bộ thử nghiệm làm cho

độ chính xác của bài kiểm tra.

Tiếp theo là báo cáo phân loại.

Vì vậy, nó cung cấp một bản phân tích chi tiết

về hiệu suất của mô hình cho mỗi lớp.

Nó bao gồm độ chính xác, thu hồi và điểm F1.

Tiếp theo là ma trận nhầm lẫn.

Nó trực quan hóa hiệu suất của mô hình phân loại của chúng tôi.

Mỗi hàng đại diện cho lớp thực sự,

và mỗi cột đại diện cho lớp được dự đoán.

Vậy quá trình tiến hóa diễn ra như thế nào?

Một lần nữa, hãy xem lại các bước của chúng tôi.

Chúng tôi tải mô hình được đào tạo trước,

kiểm tra xem tệp mô hình có tồn tại không và chúng tôi tải nó.

Tiếp theo, chúng tôi đánh giá mô hình.

Chúng tôi đánh giá mô hình trên dữ liệu thử nghiệm để tìm ra sự mất mát

và con số chính xác.

Tiếp theo, chúng tôi tạo ra các dự đoán,

dự đoán các lớp cho dữ liệu thử nghiệm.

Tiếp theo, chúng tôi tạo ra một báo cáo phân loại,

tạo ra một báo cáo phân loại chi tiết,

mà chúng ta sẽ có mã trong giây lát.

Tiếp theo là ma trận nhầm lẫn.

Chúng ta sẽ hình dung ma trận nhầm lẫn bằng bản đồ nhiệt.

Vì vậy, chúng ta sẽ có hai hình dung chính trong phần này.

Một là báo cáo phân loại.

Nó sẽ cung cấp số liệu chi tiết,

như tôi đã nói, đối với mỗi lớp,

điều này sẽ giúp chúng ta hiểu

mô hình hoạt động tốt như thế nào trên các danh mục khác nhau.

Tiếp theo là ma trận nhầm lẫn.

Nó hình dung sự phân loại đúng so với dự đoán,

làm nổi bật bất kỳ lĩnh vực nào mà mô hình đang gặp khó khăn.

Bây giờ để kết luận,

những đánh giá này là rất, rất cần thiết

trong việc phát triển một hệ thống nhận dạng hình ảnh đáng tin cậy.

Chúng giúp đảm bảo mô hình của chúng tôi hoạt động tốt

trên tất cả các danh mục, không chỉ một,

và xác định bất kỳ vấn đề tiềm ẩn nào.

Đánh giá đúng là rất quan trọng để xây dựng vững mạnh

và các mô hình đáng tin cậy.

Vì vậy, chúng tôi không muốn chỉ dựa vào một số liệu.

Chúng tôi muốn sử dụng một hệ thống phức tạp, mạnh mẽ,

và số liệu sâu sắc để nó mang lại cho chúng tôi

sự hiểu biết tổng thể về cách thức hoạt động của mô hình.

Vì vậy, với thông tin này,

hãy tiếp tục và viết mã số liệu thành công của chúng ta.

Như mọi khi, hãy tiếp tục

và tìm 03 _04 file _begin.python.

Nó cung cấp cho chúng tôi một khung sườn tốt về những gì chúng tôi đang làm việc,

sau đó chúng tôi sẽ tiếp tục và chèn số liệu thành công của mình vào

và tiêu chí cho tập tin này,

và chúng ta sẽ đi theo con đường của mình

đến 03 _04 _end tập tin python.

Vì vậy, hãy xem bộ xương được cấu trúc như thế nào.

Một lần nữa, nó cung cấp cho chúng tôi các quy trình thông thường,

nhập thư viện, tắt GPU, tải tập dữ liệu,

tập dữ liệu tiền xử lý, đảm bảo thư mục đầu ra tồn tại,

xác định đường dẫn mô hình và tất cả những thứ đó.

Vì vậy, điều chúng ta cần làm tiếp theo là chúng ta sẽ tiếp tục

và tiếp tục mô hình này và đảm bảo

rằng chúng ta đang xác định tất cả các con đường mà chúng ta cần.

Nếu không, chúng tôi sẽ tiếp tục và thêm chúng.

Sau đó, chúng tôi sẽ tiếp tục và thêm các số liệu gây nhầm lẫn của mình

tới mã này.

Vì vậy, hãy bắt đầu.

Vì vậy, trước hết,

Tôi muốn chắc chắn

rằng chúng tôi đang thêm thư mục cốt truyện của mình

vào hệ thống của chúng tôi là tốt.

Vì vậy, sau đường dẫn mô hình,

hãy đảm bảo rằng đường dẫn cốt truyện của chúng ta cũng được xác định

để chúng tôi có thể chèn các số liệu gây nhầm lẫn

vào đúng thư mục.

Vì vậy, bây giờ chúng ta sẽ tiếp tục và tạo một thư mục

rằng nếu chúng ta không có nó,

chúng ta sẽ tiếp tục và tạo ra nó.

Phần tiếp theo thực sự là cốt lõi của buổi học ngày hôm nay của chúng ta.

Vì vậy, cái nào sẽ xác định đường dẫn tệp

đến các số liệu gây nhầm lẫn mà chúng tôi sẽ xây dựng.

Vì vậy, chúng tôi tiếp tục và xác định điều đó.

Tiếp theo, chúng ta tiếp tục,

và chúng tôi xác định tất cả các báo cáo phân loại

và cài đặt chỉ số nhầm lẫn.

Vì vậy, hãy tiếp tục và làm tất cả những điều đó tiếp theo.

Thực ra tôi sẽ đi trước

và di chuyển định nghĩa cốt truyện này sang phải

sau khi kiểm tra đường dẫn cốt truyện,

vì vậy chúng được tổ chức một cách chiến lược về mặt trật tự.

Tiếp theo, chúng tôi kiểm tra xem mô hình đã tồn tại chưa.

Nếu nó đã tồn tại, nó sẽ tải mô hình được đào tạo trước,

và sau đó nó in ra rằng nó đã tải mô hình hiện có.

Bây giờ mô hình hiện có là đủ cho trường hợp của chúng tôi.

Chúng ta có thể tiếp tục và tạo ra tất cả các thước đo thành công này

trên mô hình được đào tạo trước,

đó là một tin tốt

bởi vì theo cách đó chúng ta không có

để chờ đợi tất cả 20 kỷ nguyên đó đến được với họ.

Vì vậy, chúng tôi tiếp tục và đánh giá mô hình

trên dữ liệu thử nghiệm để có được sự mất mát và độ chính xác.

Vì vậy, chúng tôi xác định độ mất kiểm tra và độ chính xác của kiểm tra,

và nó sẽ là model.evaluate, xtest, ytest,

và chúng tôi in điểm chính xác của bài kiểm tra.

Sau đó chúng ta tiếp tục và dự đoán các lớp học

cho dữ liệu thử nghiệm.

Vì vậy, chúng ta hãy tiếp tục và làm điều đó.

Chúng tôi đưa ra dự đoán với y_pred

bằng np.argmax,

và chúng tôi đưa ra model.predict, xtest và axis one.

Sau đó chúng tôi cung cấp y _true và p.argmax,

ytest, trục một.

Tiếp theo là báo cáo phân loại.

Vì vậy, đây là cốt lõi của phiên họp của chúng tôi.

Vì vậy, hãy tiếp tục và viết mã này từ đầu.

Vì vậy, chúng tôi nói rằng hãy tạo một báo cáo phân loại ở đây,

và báo cáo phân loại này bao gồm những gì

chúng ta có thể nói báo cáo lớp ở đây bằng nhau

vào báo cáo phân loại,

đó là một chức năng tích hợp.

Bạn nhận thấy rằng nó tự động hoàn thành khi tôi nhấn enter.

Sau vài lá thư,

nó thực sự đã tự động hoàn thành báo cáo phân loại.

Sau đó chúng ta đưa ra dự đoán y đúng, y.

Chúng tôi vừa tạo những thứ đó ở trên.

Sau đó chúng ta nói tên mục tiêu bằng,

và sau đó chúng tôi đặt tên mục tiêu làm lớp học của mình.

Vì vậy, tôi sẽ tiếp tục và sao chép chúng ngay tại đây

để chúng tôi có tất cả sẵn sàng.

Hãy đảm bảo rằng dấu ngoặc đơn của chúng ta thẳng hàng.

Hãy chú ý đến những cái màu đỏ.

Chúng tôi có những cái thừa nên tôi đã tiếp tục và loại bỏ nó.

Vì vậy, đây là cách chúng tôi tạo một báo cáo lớp học.

Chúng tôi gọi chức năng báo cáo phân loại tích hợp là

và chúng tôi đưa ra y đúng từ các lớp dự đoán

và sau đó y pred chúng ta vừa tạo.

So, y pred is the predictions

và y true là giá trị thực,

và sau đó nó tiếp tục

và tạo báo cáo phân loại cho chúng tôi.

Bây giờ là thước đo thành công tiếp theo

chúng ta sẽ đề cập đến trong phần này

là ma trận nhầm lẫn.

Vì vậy, hãy tiếp tục và viết mã đó.

Tạo một ma trận nhầm lẫn.

Vì vậy, trong trường hợp cụ thể này,

chúng tôi nói ma trận nhầm lẫn bằng.

Một lần nữa, hãy sử dụng hàm dựng sẵn ma trận nhầm lẫn.

Nó tự động hoàn thành nó cho tôi.

Chúng tôi tiếp tục và nói y đúng.

Chúng tôi vừa tạo chúng ở trên, y _pred.

Vì vậy, điều này là khá nhiều.

Trên thực tế, nó giúp ích cho chúng ta

thực sự đơn giản để làm

bằng ngôn ngữ lập trình Python

vì những chức năng tích hợp tuyệt vời này.

Và sau đó chúng ta tiếp tục và đưa ra kích thước hình

giả sử là từ 10 đến 8.

Tiếp theo, chúng ta sẽ sử dụng đường biển cho việc đó.

Vì vậy, chúng ta sẽ sử dụng bản đồ nhiệt để xác định

ma trận nhầm lẫn.

Vì vậy, chúng tôi cung cấp cho nó ma trận nhầm lẫn,

và sau đó chúng tôi nói chú thích là đúng,

và sau đó chúng tôi cung cấp tất cả các cài đặt khác

mà chúng tôi muốn về điều này,

và sau đó chúng ta tiếp tục,

và vẽ nhãn và tiêu đề tương ứng

để chúng tôi hiểu chúng tôi đang làm việc với cái gì.

Vì vậy, đây là bản đồ nhiệt của chúng tôi.

Phải mất tất cả 10 nhãn mà chúng tôi đang làm việc.

Máy bay, ô tô, chim, mèo, hươu, v.v.

Và sau đó chúng tôi thực sự gán nhãn x

và nhãn y như dự đoán và đúng,

và sau đó tiêu đề là ma trận nhầm lẫn.

Bây giờ chúng ta hãy tiếp tục

và cũng có ma trận nhầm lẫn

được âm mưu

vào thư mục cốt truyện mà chúng tôi đã xác định.

Vì vậy, đây là cách chúng tôi làm điều đó.

Vẽ dấu chấm, lưu hình

và sau đó chúng tôi đưa ra tệp cốt truyện ma trận nhầm lẫn.

Đây là điều chúng tôi đã xác định ở trên,

và sau đó ở đây là tập tin cốt truyện ma trận nhầm lẫn.

Chúng ta sẽ tiếp tục và chèn phần này vào phần cốt truyện.

Bây giờ chúng tôi muốn làm một điều nữa trước khi đóng mã này.

Chúng tôi muốn lưu mô hình được đánh giá

vào thư mục đầu ra là tốt.

(nhấn bàn phím)

Được rồi và chúng ta tiếp tục

và lưu nó vào thư mục đầu ra.

Được rồi tuyệt vời.

Sau đó, nếu không, chúng tôi nói không tìm thấy mô hình.

Hãy đảm bảo mô hình được đào tạo chính xác

để nắm bắt bất kỳ điều kiện nào khác.

Vậy chúng ta hãy tiếp tục và thử sức nhé

và sau đó thực hiện thêm một bản tóm tắt cuối cùng về nó.

Vì vậy, để đơn giản,

hãy bắt kịp lại

từ 03 _04 _end.py.

So sánh mã của bạn với mã bắt đầu.

Xem cái gì giống và cái gì khác.

Nếu không, chúng ta có thể tiếp tục

đến 03 _04 _kết thúc,

và chỉ cần nhấp vào chạy,

và sau đó chúng ta sẽ thấy

rằng những gì chúng tôi đã thêm vào đang thực hiện công việc của nó.

Nó đang tải mô hình hiện có ngay tại đây

bởi vì chúng tôi vừa tạo mô hình hệ thống

ở các phần trước,

và ở đó, chúng ta có báo cáo phân loại

cũng như cốt truyện ma trận nhầm lẫn đã được lưu

đến nơi chúng tôi đã xác định.

Xuất sắc.

Vì vậy, đây chính là thứ chúng tôi đang tìm kiếm,

và trong trường hợp cụ thể này, ví dụ,

báo cáo phân loại này

có điểm thu hồi chính xác và hỗ trợ F1.

Vì vậy, khi nói đến độ chính xác,

nó có nghĩa là tỷ lệ dự đoán tích cực thực sự

với tổng số kết quả tích cực được dự đoán.

Nó đo lường độ chính xác của những dự đoán tích cực.

Vì vậy, đối với máy bay 0,77 là độ chính xác

của những dự đoán tích cực.

Tiếp theo là thu hồi.

Thu hồi là tỷ lệ dự đoán tích cực thực sự

đến những mặt tích cực thực tế.

Nó đo lường khả năng của mô hình

để tìm tất cả các trường hợp có liên quan trong tập dữ liệu.

Và điểm F1 là giá trị trung bình hài hòa của độ chính xác và khả năng thu hồi.

Nó cung cấp một số liệu duy nhất cân bằng cả hai mối quan tâm.

Vì vậy, nếu chúng ta tò mò về độ chính xác

và nhớ lại nhưng chúng tôi chỉ muốn một điểm,

sau đó chúng tôi sử dụng điểm F1.

Hỗ trợ là số lượng phiên bản thực sự cho mỗi lớp.

Trong trường hợp của chúng tôi, tất cả đều bình đẳng.

Vì vậy, chúng ta hãy xem lại một lần nữa

kết quả cho máy bay

Đối với độ chính xác của máy bay là 0,77,

thu hồi là 0,80, điểm F1 là 0,78,

và hỗ trợ là 1 000.

Chúng ta tiếp tục và cuộn xuống,

và chúng tôi tìm thấy sự chính xác ở đây.

Vì vậy, độ chính xác là một trong những thước đo tổng thể,

và độ chính xác là 0,74,

có nghĩa là 74% số hình ảnh

được phân loại chính xác cho mô hình này.

Trung bình vĩ mô là trung bình của việc thu hồi chính xác

và điểm F1 cho tất cả các lớp.

Mặt khác, bình quân gia quyền,

là mức thu hồi chính xác trung bình

và điểm F1 cho tất cả các lớp,

được tính theo số lượng trường hợp thực sự

cho mỗi lớp.

Tiếp theo, chúng ta có thể cuộn lên,

và dưới phần cốt truyện,

chúng ta hãy tiếp tục

và tìm 03 _04_confusion _matrix

mà chúng tôi vừa tạo bằng mã này

mà chúng ta đã xác định.

Vì vậy, đây là một bảng được sử dụng

để mô tả hiệu suất của một mô hình phân loại.

Vì vậy, nó hiển thị sự phân loại thực tế so với dự đoán,

với các lớp thực tế được liệt kê trên các hàng

và các lớp dự đoán được liệt kê trên các cột.

Vì vậy, làm thế nào để chúng ta đọc ma trận nhầm lẫn này?

Vâng, các phần tử đường chéo mà chúng ta đang tìm kiếm

at đại diện cho các dự đoán chính xác cho mỗi lớp.

Ví dụ: đối với máy bay có 797 dự đoán đúng.

Các phần tử nằm ngoài đường chéo thể hiện sự phân loại sai.

Vì vậy, 45 trong số những người ở hạng máy bay

bị phân loại sai thành chim.

26 hình ảnh máy bay bị phân loại sai thành một con mèo,

chẳng hạn.

Vì vậy, để tóm tắt nhanh chóng,

từ ma trận nhầm lẫn cho lớp máy bay,

chúng ta có 797 kết quả dương tính thực sự,

có nghĩa là được phân loại chính xác là máy bay.

Còn những kết quả dương tính giả thì sao?

Vâng, chúng ta có 11 cộng 45 cộng 26 cộng 18 cộng

5 cộng 6 cộng 13 cộng 51 cộng 28,

được phân loại sai như các lớp khác,

và chúng ta có thể nhìn xuống

và xem những gì được phân loại sai.

Như chúng tôi đã ghé thăm trước đây, số 11 là ô tô,

45 là chim, 26 là mèo, v.v.

Tổng số âm thực của tất cả

các phần tử đường chéo khác được phân loại chính xác

như các lớp khác.

Và âm tính giả là tổng của tất cả các yếu tố khác

trong hàng máy bay bị phân loại sai là máy bay.

Vì vậy, hãy quay lại báo cáo phân loại

và đưa ra một số giải thích về báo cáo này.

Vì vậy, độ chính xác cao và thu hồi cho ô tô.

Mô hình thực hiện tốt việc phân loại hình ảnh ô tô,

với độ chính xác là 0,89 và thu hồi là 0,81.

Vâng, còn con mèo thì sao?

Độ chính xác và thu hồi đối với mèo cũng thấp hơn.

Người mẫu nỗ lực nhiều hơn

với hình ảnh con mèo cho thấy độ chính xác thấp hơn 0,54

và thu hồi 0,52.

Còn hiệu suất tổng thể thì sao?

Vâng, mô hình có độ chính xác cân bằng là 0,74,

cho thấy nó hoạt động khá tốt,

nhưng nó vẫn còn chỗ để cải thiện ở một số lớp nhất định.

Tóm lại, báo cáo phân loại

và ma trận nhầm lẫn với nhau

cung cấp sự hiểu biết toàn diện

về hiệu suất của mô hình.

Chúng giúp xác định lớp nào

mô hình đang hoạt động tốt,

và lớp nào cần chú ý hơn một chút.

Những chỉ số này rất quan trọng để đánh giá,

và cải tiến mô hình.

Hãy nhớ rằng, chúng tôi cũng đã chạy tất cả những thứ này trong CPU không có GPU,

và nó hỗ trợ rằng chúng tôi đã xây dựng được một mô hình vững chắc.