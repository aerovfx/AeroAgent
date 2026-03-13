# 55 - Giải pháp dự án Keras Thiếu dữ liệu Phần một tiếng Anh

---

Chào mừng trở lại, mọi người.

Bây giờ là lúc bắt đầu xử lý trước dữ liệu và chúng ta sẽ bắt đầu bằng cách cố gắng tìm ra cách hoạt động

với dữ liệu còn thiếu trong tập dữ liệu của chúng tôi.

Đây có lẽ là phần khó nhất trong toàn bộ dự án vì nó mang nhiều sắc thái hơn và không có 100%

câu trả lời đúng.

Hãy nhớ rằng, các tùy chọn của chúng tôi là giữ lại dữ liệu bị thiếu, loại bỏ dữ liệu bị thiếu hoặc điền vào phần còn thiếu.

dữ liệu.

Hãy xem lại dữ liệu nào bị thiếu và cách chúng tôi có thể xử lý dữ liệu đó.

Được rồi.

Vì vậy, trong Phần hai về xử lý dữ liệu, chúng ta có một số mục tiêu.

Và ngay bây giờ chúng tôi sẽ tập trung vào việc xóa hoặc điền vào mọi dữ liệu còn thiếu.

Và tế bào đầu tiên này thực sự không phải là một nhiệm vụ.

Nó chỉ là phần đầu của khung dữ liệu mà chúng tôi hiện có.

Vì vậy, chúng ta sẽ chuyển sang dữ liệu còn thiếu.

Và chúng tôi muốn tự hỏi, độ dài của toàn bộ khung dữ liệu là bao nhiêu và điều đó có dễ dàng không?

Câu trả lời chỉ bằng cách nói dựa vào khung dữ liệu, bạn cũng có thể sử dụng thông tin dữ liệu.

Và có vẻ như chúng ta có khoảng 400000 điểm, ít hơn thế một chút.

Vì vậy, tiếp theo, chúng tôi muốn tạo một chuỗi hiển thị tổng số giá trị còn thiếu trên mỗi cột.

Và chúng tôi đã chỉ cho bạn cách thực hiện việc này trước đây.

Bạn đơn giản nói D.F., điều đó là vô giá trị.

Và gọi lại sẽ trả về một khung dữ liệu trông như thế này.

Và chúng ta có thể tính tổng của nó qua các hàng ở đây.

Và sau đó chúng ta nhận được các cột thực tế và số lượng của chúng để biết số điểm bị thiếu.

Vì vậy, có vẻ như chúng tôi còn thiếu khoảng 22 nghìn tiêu đề AMP mà sau này chúng tôi sẽ tìm hiểu

là chức danh việc làm.

Ngoài ra, thời gian làm việc bị thiếu khá nhiều.

Sau đó, chúng tôi thiếu tiêu đề này, chỉ thiếu một số tiêu đề về tính năng cụ thể này.

Chúng ta đang thiếu khá nhiều thông tin về Moort Ach nên chúng ta sẽ phải xem đó là gì.

Và sau đó chúng ta cũng thiếu một cặp đôi trong hồ sơ công khai về các vụ phá sản.

Được rồi, vậy điều thú vị là lấy những con số này theo tỷ lệ phần trăm của tổng số dữ liệu này

frame chỉ để xem mức độ nghiêm trọng của vấn đề.

Vì vậy, tôi muốn thấy nó theo cách này là tôi đang thiếu 5,7% tất cả các chức danh việc làm

hoặc tôi đang thiếu gần 10% số tài khoản thế chấp này.

Vì vậy, hãy tiếp tục và tìm ra cách để làm điều đó.

Một cách để làm điều đó là thu hồi loạt phim trước của chúng tôi đó là D.F. số tiền đó là null.

Và sau đó nếu tôi chỉ cần chia mọi mục ở đó cho độ dài của khung dữ liệu, thì tôi có thể nhân số đó

lên 100 để có tỷ lệ phần trăm và đó là cách chúng ta có thể nhận được kết quả chính xác như vậy.

Vì vậy, một lần nữa, tổng đó gấp một trăm lần DFAS null chia cho độ dài của khung dữ liệu.

Vì vậy, có vẻ như thứ chúng ta sẽ phải thực sự tập trung vào là tài khoản thế chấp này, bởi vì

chúng ta thực sự không thể bỏ đi 10% dữ liệu của mình.

Nhưng một số trong đó rất nhỏ, chẳng hạn như cái này và cái này.

Đây thực sự là ít hơn nửa phần trăm dữ liệu của chúng tôi.

Vì vậy, sẽ ổn nếu bỏ đi một số thứ này.

Vì vậy, chúng ta sẽ làm là chúng ta sẽ bắt đầu từ trên xuống dưới.

Chúng ta sẽ bắt đầu với chức danh việc làm và thời gian làm việc.

Vậy chúng ta hãy cuộn xuống đây.

Vì vậy, trước tiên tôi muốn kiểm tra chức danh công việc này và thời gian làm việc để xem liệu nó có ổn không

thả chúng xuống để chúng ta có thể sử dụng chân dưới thông tin gạch dưới.

Đó là chức năng thông tin tính năng mà chúng tôi thiết lập cho bạn lúc đầu chỉ đơn giản là báo cáo

quay lại đây là gì

Vì vậy, thông tin đặc trưng về chức danh công việc, đó chỉ đơn giản là chức danh công việc do người vay cung cấp

khi đăng ký khoản vay và liên kết việc làm.

Chúng tôi thực sự có nó cho bạn ở đây.

Đó là thời gian làm việc tính bằng năm.

Vì vậy, các giá trị có thể nằm trong khoảng từ 0 đến 10, trong đó 0 có nghĩa là dưới một năm và 10 có nghĩa là 10 hoặc

nhiều năm nữa.

Vì vậy, câu hỏi tiếp theo mà chúng ta muốn bắt đầu nghĩ đến là có bao nhiêu chức danh việc làm duy nhất

có ở đó không?

Bởi vì tôi muốn bắt đầu suy nghĩ, liệu chúng ta sẽ bỏ chức danh việc làm hay điền vào nó bằng thứ gì đó?

Vì vậy, có thể sẽ rất thú vị khi thực sự khám phá chức danh việc làm.

Vì vậy chúng ta sẽ nói D.F..

Chức danh việc làm và hãy xem có bao nhiêu chức danh việc làm độc đáo.

Vì vậy, sau khi chạy nó, bạn sẽ thấy có rất nhiều chức danh việc làm độc đáo, trên thực tế, có

173.000 chức danh việc làm duy nhất, hãy nhớ lại rằng chính tập dữ liệu của chúng tôi đã có từ khoảng

400000.

Vì vậy, có vẻ như gần một nửa trong số đó đều là những chức danh việc làm độc đáo.

Và sau đó chúng ta có thể kiểm tra nó bằng cách đếm giá trị để khám phá thêm điều đó.

Mà tôi muốn giới thiệu.

Mặc dù bạn không phải làm điều này cho dự án, nhưng chúng ta có thể chỉ cần chạy cái này và chúng ta có thể thấy ở đây cái đó

chúng tôi có một số giáo viên, người quản lý, y tá đã đăng ký, v.v. và chúng tôi có rất nhiều chức danh

thực sự chỉ dành riêng cho người cụ thể đó.

Vì vậy, trên thực tế, có quá nhiều tiêu đề để chuyển đổi điều này thành một loại tính năng biến giả nào đó.

Chúng ta không thể thêm vào thêm một trăm bảy mươi ba nghìn cột boolean.

Bây giờ, điều bạn có thể làm là với kỹ thuật tính năng mở rộng, hãy bắt đầu phân loại những thứ có thể

việc làm có thu nhập cao so với việc làm có thu nhập trung bình.

Nhưng một lần nữa, bạn phải đưa ra rất nhiều giả định và phải tìm ra cách thực hiện điều này và lập bản đồ

có tới hơn 173.000 chức danh công việc khác nhau.

Vì vậy, đây chỉ là quá nhiều chức danh công việc độc đáo nên có lẽ nó sẽ không cung cấp nhiều thông tin vì

một nửa số người có một chức danh công việc độc đáo nào đó.

Vì vậy, thay vì làm như vậy, chúng tôi sẽ chỉ xóa tiêu đề đó vì nó không thực tế

hữu ích cho chúng tôi dưới bất kỳ hình thức nào.

Vì vậy chúng ta sẽ nói D.F. sẽ bằng với sự sụt giảm.

Chức danh việc làm.

Và chúng ta cần thực hiện điều này dọc theo trục bằng một và hãy cẩn thận với những câu lệnh loại bỏ này bởi vì

bạn chỉ có thể chạy chúng một lần.

Nếu bạn thử chạy chúng nhiều lần, bạn sẽ gặp lỗi vì bạn đã xóa nó

tính năng.

OK, tiếp theo chúng ta tạo tài khoản cho cột tính năng liên kết việc làm.

Vì vậy, một lần nữa, chúng tôi muốn thử sắp xếp thứ tự của các giá trị.

Vì vậy, một cách để làm điều đó là cố gắng lấy một danh sách ở đây để thực sự nhận được đơn hàng đó.

Vì vậy chúng ta có thể nói cũng như trước đây, D.F. thời gian làm việc phải là dấu gạch dưới.

Hãy tiếp tục và nói.

Bỏ bất kỳ giá trị nào và sau đó, chúng ta sẽ có thể gọi duy nhất nếu chúng ta không bỏ và đôi khi điều đó trả về

một lỗi.

Vì vậy, đây là những tiêu đề thực sự độc đáo và tôi sẽ tiếp tục sắp xếp chúng.

Và bây giờ tôi đã sắp xếp các tiêu đề, và điều này thực sự có vẻ gần như theo thứ tự, ngoại trừ việc xuất sắc

được sắp xếp một năm ngay trước hơn 10 năm này.

Vì vậy, những gì tôi có thể làm chỉ đơn giản là sao chép cái này, đó là những gì tôi đang làm ở dưới đây, dán nó vào ô

và chúng ta sẽ tiếp tục và cho biết thứ tự thời lượng tuyển dụng bằng với danh sách này.

Và sau đó tôi sẽ đơn giản làm điều này bằng cách tóm lấy anh chàng này, dán nó xuống đây.

Hãy tiếp tục và đảm bảo rằng định dạng đó là chính xác.

Và sau đó chúng ta sẽ tóm lấy anh chàng này và dán nó vào đó rồi sửa dấu phẩy.

OK, vậy là sau khi chạy nó, bây giờ chúng ta đã có thứ tự tuyệt vời này.

Xin nhắc lại, đây là tùy chọn về mặt kỹ thuật, nhưng sẽ rất tốt cho biểu đồ đếm mà chúng tôi tạo ngay tại đây

để thực sự có được thứ tự này.

Và bây giờ tôi có thể làm điều này chỉ bằng cách nói S.A.S. ô đếm trong đó X là.

Liên kết việc làm.

Dữ liệu của tôi bằng với khung dữ liệu hiện tại của tôi và đơn hàng của tôi bằng với thứ tự thời lượng việc làm đó.

Vì vậy, nếu bạn đang ở trên đó, bạn sẽ thấy điều này ngay tại đây, chúng tôi sẽ tiếp tục và kéo dài nó ra để chúng tôi không

có được sự chồng chéo đó bằng cách nói hình phạt có kích thước này bằng với đi vào và nói mười hai nhân bốn.

Và chúng ta có được âm mưu hay ho này ở đây.

Vì vậy, có vẻ như phần lớn mọi người đã làm công việc của mình hơn 10 năm,

điều đó có ý nghĩa.

Nếu bạn đang vay tiền, rất có thể bạn sẽ có việc làm.

Bằng không thì làm sao bạn có thể trả lại được?

Vì vậy, hầu hết mọi người đã làm việc được hơn một năm và có vẻ như chúng tôi đã làm sai trật tự ở đây

một năm so với dưới một năm.

Vậy chúng ta hãy tiếp tục và bắt anh chàng này.

Và đặt nó vào đúng nơi nó thuộc về, và điều đó sẽ sắp xếp thứ tự cho chúng ta.

Thế đấy.

Vì vậy, bây giờ chúng ta thấy ít hơn một năm, một năm này sang năm khác, v.v.

Được rồi, có lẽ tôi cũng muốn xem tính năng này hữu ích như thế nào dựa trên những gì

chúng tôi đang cố gắng dự đoán.

Hãy nhớ lại rằng chúng ta đang cố gắng dự đoán liệu ai đó có thực sự trả được khoản vay của mình hay không.

Vậy tình trạng cho vay của họ là gì?

Chúng tôi điều hành nó.

Và thực sự điều tôi quan tâm ở đây là mối quan hệ giữa thanh toán đầy đủ và tính phí

theo thời gian làm việc.

Nếu có sự khác biệt lớn giữa một trong các loại khoản thanh toán đầy đủ và khoản thanh toán đã tính phí, ví dụ:

Ví dụ: có thể nếu bạn làm việc chưa đầy một năm, mọi người ở đó không tính phí khoản vay của họ không trả được

hồi đó.

Đó là một tính năng rất quan trọng.

Nếu tỷ lệ của thanh màu xanh này với thanh màu cam này về cơ bản là giống nhau trên tất cả các việc làm này

các danh mục thì đây không phải là một tính năng có nhiều thông tin.

Vì vậy, điều tôi muốn làm là tôi thực sự muốn tìm ra tỷ lệ giữa số tiền được thanh toán đầy đủ so với số tiền phải trả

tắt người cho mỗi loại liên kết việc làm.

Và đó là nhiệm vụ sau này chúng ta vừa hoàn thành, nhiệm vụ này ở dưới đây, nhiệm vụ này chúng ta đang ở đây, đó là

về cơ bản nó đang mô tả điều gì.

Vì vậy, điều đó không thực sự thông báo cho chúng tôi.

Điều chúng tôi thực sự muốn biết là tỷ lệ phần trăm giảm giá cho mỗi danh mục thời gian làm việc.

Được rồi, vậy làm thế nào chúng ta thực sự có thể làm được điều này?

Đây là một nhiệm vụ hơi khó khăn, nhưng nếu bạn nghĩ về nó một cách hợp lý từng bước một, đặc biệt là

khi bạn đang sử dụng gấu trúc, việc này sẽ khá đơn giản.

Vì vậy, điều tôi muốn làm về cơ bản là tôi muốn xây dựng một chuỗi trông giống như thế này,

phần trăm số người không trả lại khoản vay của họ theo loại việc làm.

Vậy điều tôi sắp làm là tôi sẽ nói.

Hãy tiếp tục và lấy tập hợp con của khung dữ liệu chứa trạng thái khoản vay của tôi.

Bằng.

Bị tính phí, vì vậy đây là những người không trả được khoản vay của họ và tôi sẽ sao chép và dán

ở dưới này vì chúng ta sẽ làm điều tương tự với những người chưa trả hết khoản vay của họ.

Vì vậy, hiện tại tôi có một khung dữ liệu trong đó mọi người không trả lại khoản vay của họ và một khung dữ liệu trong đó

họ đã thanh toán đầy đủ.

Và điều tôi sắp làm là tôi quan tâm đến việc nhóm nó theo loại thời gian làm việc này.

Vì vậy tôi sẽ nói nhóm theo.

Độ dài gạch dưới của việc làm và tôi sẽ làm điều đó cho cả hai trường hợp.

Và tiếp theo, điều tôi muốn làm là tôi thực sự muốn lấy số đếm của từng cái, tôi muốn tính

xem thực tế có bao nhiêu người ở thanh màu xanh này và có bao nhiêu người ở thanh màu cam này.

Vì vậy, đây là tôi chỉ đang cố gắng tính toán đằng sau những song sắt này.

Vì vậy, họ tính tiền cho mọi người, nhóm họ theo thời gian làm việc.

Hãy tiếp tục và đếm ở đó.

Về cơ bản bây giờ đó là chuyên mục của Quận Cam.

Và để có được cột thẻ xanh, chúng tôi sẽ chỉ thực hiện điều đó trên các trạng thái đã thanh toán đầy đủ.

Và trong trường hợp này, tôi thực sự chỉ quan tâm đến cột trạng thái khoản vay cho từng khoản này.

Vì vậy, thay vì chỉ chạy cái này và nhận số tiền, nó sẽ giống nhau đối với tất cả những thứ này.

Tôi sẽ không chuyển qua cột trạng thái khoản vay và nhận được những con số đó.

Vì vậy, ở đây tôi có thể thấy trạng thái khoản vay được tính theo danh mục việc làm.

Và nếu tôi làm điều này với anh chàng này, tôi sẽ nhận được điều tương tự.

Nhưng đối với những người đã trả hết khoản vay của họ và tôi sẽ chuyển nhượng những khoản này.

Bằng cách nói việc làm hoặc gạch dưới MP, chúng ta sẽ tiếp tục và nói CEO là người bị sa thải, vì vậy đó là một chuỗi

và sau đó chúng tôi sẽ nói MP gạch dưới FNP để thanh toán đầy đủ.

Và tất cả những gì tôi quan tâm là tỷ lệ giữa chúng.

Vì vậy, đó sẽ là.

Chiều dài nhân viên cho những người đã tính phí, chia cho.

Khoản thanh toán đầy đủ để chúng tôi có thể chạy những thứ này và bây giờ tôi có thể thấy phần trăm số người đã tính phí so với

được thanh toán đầy đủ.

Hãy nhớ rằng, đây là tỷ lệ trực tiếp, nếu tôi thực sự muốn biết phần trăm, tôi có thể nói.

Giám đốc điều hành AMP, cộng với AMP, FNP, điều hành nó và đây là phần trăm thực tế cho mỗi danh mục thay vì

tỷ lệ trực tiếp, và chúng ta có thể thấy ở đây rằng xét về mọi mặt thì nó trông cực kỳ giống nhau.

Vậy tôi có thể thấy không điểm một chín không điểm một tám.

Hầu hết trong số này là 0,9 so với mức tối đa là 0,2.

Vì vậy, có vẻ như đặc điểm cụ thể này của thời gian làm việc thực sự không có một số khác biệt lớn

về mức phí giảm giá.

Vì vậy, có vẻ như bất kể thời gian làm việc thực tế của bạn là bao nhiêu, nếu bạn chọn một ai đó

khoảng 20 phần trăm trong số họ, khoảng từ 19 phần trăm đến 19,9,9 và 20 phần trăm

sẽ không trả được khoản vay của họ.

Và chúng ta có thể minh họa thêm điều này bằng cách nói độ dài gạch dưới việc làm, tôi thực sự có thể làm cho

một âm mưu thanh cho việc này.

Theo cùng một âm mưu, loại bằng thanh chạy đó và tôi có thể thấy tỷ lệ phần trăm hoặc tỷ lệ, về cơ bản

thông tin giống nhau, thực sự điều tôi đang tìm kiếm ở đây là thực tế là vì tất cả các thanh này gần như

cùng chiều cao, thực sự không có nhiều thông tin hoặc sự khác biệt giữa việc làm

cột cuộc sống, điều này thật đáng ngạc nhiên.

Nhưng chúng ta có thể thấy ở đây sự khác biệt chính là những người làm việc trong 10 năm có thu nhập nhỏ hơn một chút.

giảm giá so với những người làm việc ít hơn một năm hoặc ít hơn một năm.

Nhưng sự khác biệt không đủ lớn để thực sự xác nhận việc giữ tính năng này.

Vì chúng cực kỳ giống nhau trong tất cả các công việc, nhưng chúng ta sẽ tiếp tục và chỉ bỏ qua

cột đó sẽ nói D.F. bằng với mức giảm DFG.

Thời gian làm việc.

X bằng một, vì vậy hãy chạy nó và tiếp theo hãy xem lại khung dữ liệu để xem những cột trong tương lai vẫn có những cột nào

dữ liệu bị thiếu.

Vì vậy Sadaf không phải là một số người cứ tiếp tục và chạy thì bạn sẽ lấy lại được bộ truyện này và có vẻ như chúng ta vẫn

có quyền sở hữu, Reville Util này, tài khoản thế chấp này và hồ sơ phá sản công khai.

Vì vậy, chúng tôi sẽ tiếp tục xử lý các tính năng còn thiếu này và tiếp tục

bài giảng này.

Tôi sẽ gặp bạn ở đó.