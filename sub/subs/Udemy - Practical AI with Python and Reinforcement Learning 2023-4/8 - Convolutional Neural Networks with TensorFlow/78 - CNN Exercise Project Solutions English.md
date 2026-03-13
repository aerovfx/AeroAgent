# 78 - Giải pháp dự án bài tập CNN Tiếng Anh

---

Chào mừng trở lại, mọi người.

Trong bài giảng này, chúng ta sẽ tìm hiểu các giải pháp cho mạng nơ ron tích chập, bài tập

câu hỏi, hãy đến sổ ghi chép và bắt đầu.

Được rồi, chúng ta đang ở sổ ghi chép bài tập.

Điều đầu tiên chúng tôi muốn làm là tải tập dữ liệu lên.

Chúng ta có thể làm điều này một cách đơn giản bằng cách chạy ô từ bài tập.

Vì vậy, dữ liệu trọng tâm căng thẳng đặt lệnh ân xá thời trang và chúng tôi muốn sử dụng matplotlib để trực quan hóa dữ liệu.

Điều đó có nghĩa là chúng tôi thực sự cần nhập đường dẫn matplotlib dưới dạng PLT.

Và nếu chúng ta nhìn vào dữ liệu huấn luyện ngay bây giờ, nếu chúng ta nhìn vào hình dạng của nó, thì đó là

sáu mươi nghìn hình ảnh, hai mươi tám x hai mươi tám.

Vì vậy, hãy tiếp tục và lấy một trong những hình ảnh đó.

Vì vậy bây giờ chúng ta có một hình ảnh duy nhất ở đó và sau đó hiển thị nó, chỉ một hình ảnh duy nhất, chúng ta có thể nói là đẹp

IMNSHO và nó sẽ hiển thị hình ảnh.

Và trong trường hợp này, vì mục hình ảnh đầu tiên là một chiếc ủng thực sự.

Được rồi, vậy là chúng ta đã làm được điều đó.

Chúng tôi hiểu rằng chúng tôi có dữ liệu này.

Bây giờ là lúc xử lý dữ liệu.

Thật may mắn cho chúng ta, chúng ta có thể xác nhận rằng giá trị tối đa là hai năm mươi lăm chỉ bằng cách nói rằng Max, tức là

có nghĩa là tôi có thể thực hiện một quá trình tiền xử lý đơn giản.

Bởi nói cực bằng bằng cực, chia cho hai mươi lăm.

Và phép thử X đó bằng phép thử X chia cho 255.

Sau đó, chúng ta có thể định hình lại tia X để bao gồm chiều thứ tư đó.

Vì vậy những gì chúng ta có thể làm ở đây là chúng ta có thể nói.

Extreme tương đương với việc định hình lại tàu X.

Sáu mươi nghìn hai mươi tám x hai mươi tám một để đảm bảo chúng tôi bao gồm kênh màu đó hoặc một số ít

kênh màu, tôi nên nói vậy, và thử nghiệm tiếp theo sẽ là định hình lại thử nghiệm X.

Và trong trường hợp này là mười nghìn điểm.

Vì vậy, nó có kênh 28 x 28 theo một màu.

Vì vậy chúng tôi đã định hình lại nó để bao gồm kênh màu đó.

Và sau đó, chúng tôi cũng muốn đảm bảo rằng chúng tôi chuyển đổi các nhãn thành phân loại để chúng tôi có thể nói từ tensor

luồng mang các tiện ích đó nhập vào phân loại.

Chạy nó và sau đó chúng ta sẽ nói, tại sao không thể huấn luyện bằng cách gọi hai phân loại này và chúng ta có thể nói,

tại sao lại tập luyện?

Nó có thể suy ra rằng có mười lớp, nhưng chúng ta luôn có thể đảm bảo điều đó bằng cách chuyển

nó cũng vào.

Và sau đó chúng ta sẽ nói, tại sao không thể kiểm tra bằng hai loại bài kiểm tra màu trắng.

Và hy vọng điều này có vẻ khá quen thuộc, vì chúng tôi đã thực hiện gần như cùng một quy trình

trên tập dữ liệu M.

Sau đó, đã đến lúc xây dựng mô hình, vì vậy chúng tôi muốn tạo khoảng cách với các nhà cung cấp dịch vụ điện thoại để xây dựng

mô hình tuần tự này.

Vì vậy, hãy bắt đầu với việc nhập, chúng ta sẽ nói từ luồng Tenzer mang quá trình nhập tuần tự và cả

từ luồng Tenzer mang thông tin nhập của lớp đó.

Và chúng ta sẽ sử dụng phép tích chập cho lớp tổng hợp tối đa.

Đó là hai, ba nữa, và sau đó chúng ta cũng cần tìm ra kết quả trong mô hình của mình

vì vậy chúng tôi đã sẵn sàng để đi.

Chúng ta có thể tạo mô hình của mình và sau đó thêm một tích chập vào đó.

Vì vậy, đó là tích chập của giếng, hãy tiếp tục và đặt các bộ lọc bằng 32.

Đây là một giá trị mà bạn có thể sử dụng, nhưng chúng tôi sẽ đặt các giá trị mặc định mà về cơ bản chúng tôi đã thực hiện lần trước.

Vì vậy, kernel 4 x 4 và sau đó chúng ta cần chỉ định hình dạng đầu vào là 28 x 28

bởi một.

Và chúng ta cũng có thể thử sử dụng chức năng kích hoạt.

Vì vậy, tôi có thể nói kích hoạt bằng để điều chỉnh đơn vị tuyến tính.

Sau khi hoàn thành việc đó, chúng ta sẽ tiếp tục và thêm một lớp tổng hợp.

Vì vậy, đó là nhóm tối đa có kích thước nhóm, mặc định là hai nhân hai.

Vì vậy, tôi có thể để mặc định hoặc tự mình chỉ định nó, nhưng chúng ta sẽ tiếp tục và giữ nguyên nó

tạm biệt OK, tiếp theo chúng ta sẽ nói thêm mô hình và chúng ta sẽ làm phẳng nó.

Bạn có thể thêm nhiều lớp chập hơn nếu muốn, nhưng đối với trường hợp sử dụng thì điều đó là đủ.

Và sau đó chúng ta sẽ thêm một lệnh gọi lớp dày đặc với tính năng không hoạt động.

Lớp cuối cùng của đơn vị Linnear được chỉnh sửa phải là một lớp dày đặc có cùng số lượng nơ-ron như số lượng

của các lớp, vậy đó là 10 nơ-ron.

Và chúng tôi cũng phải đảm bảo rằng đó là softmax vì đây là vấn đề phân loại nhiều lớp.

Và sau đó.

Chúng tôi sẽ biên soạn mô hình này nếu bạn muốn, bạn có thể tiếp tục và bổ sung thêm mọi thứ trong quá trình đào tạo, chẳng hạn như

cơ chế dừng sớm, nhưng hiện tại, hãy giữ mọi thứ đơn giản.

Chúng tôi sẽ nói phân loại.

Entropy chéo.

Chúng ta sẽ tiếp tục và chỉ cần chọn một trình tối ưu hóa nguyên tử, xem nó hoạt động như thế nào và sau đó hãy tiếp tục và

theo dõi độ chính xác là tốt.

Vì vậy, nói độ chính xác là một trong những số liệu của chúng tôi.

Chúng tôi biên soạn cái này.

Chúng tôi có thể xác nhận mô hình lý thuyết này, cuộc gọi tóm tắt.

Bằng cách nói mẫu mà tóm tắt.

Và ở đó chúng ta có thể thấy kết quả.

Được rồi, đã đến lúc huấn luyện mô hình, số lượng kỷ nguyên thực sự tùy thuộc vào bạn.

Chúng ta sẽ có một số kết quả ở đây.

Vì vậy, bạn có thể thấy rằng về cơ bản sau một vài kỷ nguyên, hiệu suất có xu hướng đạt đến điểm chín năm,

thậm chí chỉ sau ba kỷ nguyên.

Vậy chúng ta sẽ đi tiếp.

Giả sử chỉ cần luyện tập trong ba kỷ nguyên ở đây.

Vậy một mô hình vừa vặn trên tàu X, tại sao lại không thể huấn luyện được.

Và như một tùy chọn, bạn cũng có thể truyền dữ liệu vô hiệu.

Hãy tiếp tục và làm điều đó.

Chúng tôi sẽ nói dữ liệu xác thực là thử nghiệm X với thử nghiệm mèo Y.

Bài tập này không yêu cầu điều này.

Bạn có thể tiếp tục giải quyết vấn đề đó và giả sử là các kỷ nguyên.

Bằng ba nên chúng ta muốn huấn luyện nó nhiều đến mức đó, chúng ta sẽ đạt được kết quả khá tốt ngay cả khi ở mức ba

thời đại và cách chơi chữ của nó, bạn nên bắt đầu thấy nó rèn luyện vì lợi ích của nó.

Tôi chỉ làm ba kỷ nguyên.

Bạn luôn có thể thêm điểm dừng sớm và xem nó hoạt động như thế nào.

Chúng ta có thể thấy ở đây chúng ta đang bắt đầu đạt tới 90%.

Vì vậy, nó có độ chính xác khá tốt và hơn nữa, hy vọng nó hoàn hảo đến 90%.

Nếu chúng ta luyện tập thêm vài giai đoạn nữa, rất có thể chúng ta sẽ đạt được 95%,

Được rồi, làm theo mẫu.

Vì vậy, có rất nhiều cách khác nhau để chúng ta có thể làm điều này.

Ừm, chúng ta sẽ tiếp tục và chỉ làm theo một vài số liệu giống như chúng ta đã làm.

Hãy hỏi số liệu mô hình là gì để chúng ta có thể làm điều này bằng cách nói tên số liệu mô hình ở đây.

kết quả là sự mất mát và độ chính xác.

Có rất nhiều lựa chọn khác nhau mà chúng ta có thể làm.

Tôi có thể nói lịch sử mô hình mà lịch sử đã biến nó thành khung dữ liệu.

Và sau đó nói điều gì đó như số liệu bằng nhau và đảm bảo rằng chúng tôi nhập gấu trúc để thực hiện việc này,

nhập gấu trúc dưới dạng.

Thế đấy.

Và sau đó tôi có thể vạch ra các số liệu của mình.

Vì vậy, không có gì quá điên rồ ở đây, nhưng chúng ta phải đảm bảo rằng chúng ta vẽ ra các số liệu có liên quan với nhau.

Vì vậy, hãy vẽ đồ thị về mất mát và mất xác thực, hãy vẽ ra điều đó.

Có vẻ như cả hai vẫn đang đi xuống.

Chúng ta có lẽ có thể đào tạo hơn ba kỷ nguyên.

Nhưng vì mục đích ghi hình này, họ không muốn lãng phí thời gian chỉ để luyện tập.

Và điều còn lại chúng ta có thể làm là độ chính xác và xác nhận, độ chính xác.

Và hy vọng cả hai đều tiếp tục đi lên.

Và chúng ta bắt đầu.

Vì vậy, rõ ràng là chúng ta có thể đã luyện tập trong nhiều kỷ nguyên hơn, nhưng hãy tiếp tục và xem xét tổng thể chúng ta đã làm như thế nào.

Chúng tôi sẽ nói từ Escalon Metrics nhập một báo cáo phân loại.

Và sau đó những gì chúng ta có thể làm ở đây, chẳng hạn như dự đoán, tương đương với các lớp dự đoán mô hình và chúng tôi sẽ làm điều đó

trên tập thử nghiệm của chúng tôi và sau đó chúng tôi chỉ cần in ra báo cáo phân loại của mình để so sánh lý do.

ĐÚNG VẬY.

Hoặc thực sự, tại sao phải kiểm tra dự đoán của chúng tôi?

Được rồi, dựa trên thực tế là có lẽ chúng ta đã không luyện tập đủ số kỷ nguyên so với mười kỷ nguyên

trong giải pháp, chúng tôi thực sự vẫn đang hoạt động khá tốt.

Chúng tôi có độ chính xác 90%, về cơ bản đó là những gì chúng tôi hướng tới.

Rất nhiều thứ khác chúng ta có thể làm ở đây, như thử nghiệm với các lớp chập, thêm nhiều nơ-ron hơn,

vân vân, chơi đùa với kích thước hạt nhân.

Nhưng hy vọng đây là một bài tập tốt.

Và chỉ cần bạn tuân theo quy trình chung để thiết lập mạng nơ-ron tích chập.

OK, đó là phần này.

Cảm ơn.

Và chúng tôi sẽ gặp bạn ở lần tiếp theo.