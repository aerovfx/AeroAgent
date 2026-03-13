# 60 - Đánh giá mô hình giải pháp dự án Keras

---

Chào mừng mọi người trở lại, để kết thúc bài giảng về giải pháp, bây giờ chúng ta sẽ đánh giá mô hình

mà chúng ta đã đào tạo ở bài trước.

Hãy bắt đầu.

Được rồi, chúng ta đã đào tạo xong mô hình của mình.

Tùy chọn, bạn có thể tiếp tục và lưu mô hình của mình.

Mã để làm điều đó chỉ đơn giản là nói.

Từ dòng chảy Tenzer, bác sĩ, mô hình suy nghĩ, nhập khẩu thấp, mô hình gạch dưới, và điều đó sẽ cho phép

bạn thực sự tải nó sau.

Nhưng để lưu nó, về mặt kỹ thuật, bạn không cần phải thực hiện thao tác nhập đó.

Bạn chỉ có thể nói mô hình lưu.

Và sau đó chọn bất kỳ mã chuỗi nào, ví dụ như mô hình yêu thích của tôi, H 5 đó rồi lưu mã đó, và nếu bạn

muốn nó tải lại thì bạn chỉ cần chạy mô hình tải.

Vì vậy, điều này là hoàn toàn tùy chọn.

Bạn thực sự không lưu mô hình của mình ở đây nếu bạn không muốn sử dụng lại.

Vì vậy, hãy tập trung vào việc đánh giá khả năng thu hồi hiệu suất của mô hình trong quá trình đào tạo mà chúng tôi đã vượt qua trong cả quá trình xác thực của mình.

tập hợp và tập huấn luyện của chúng tôi.

Hãy tiếp tục và vạch ra những điều đó.

Vì vậy, chúng ta sẽ nói lịch sử mô hình trong suốt lịch sử và điều đó trả về từ điển này của

tổn thất, sau đó chúng tôi có thể dễ dàng chuyển đổi sang khung dữ liệu của gấu trúc và sau đó chúng tôi sẽ đặt dữ liệu đó thành tổn thất.

Hãy chạy nó và chúng ta hãy tiếp tục vẽ biểu đồ này để chúng ta gọi là biểu đồ tổn thất, tuy nhiên, nếu chúng ta xem xét

lúc thua lỗ.

Hiện tại, chúng ta có mất mát và mất xác thực, vì vậy hãy nhớ rằng mất mát này là mất mát đào tạo, mất xác thực này

mất mát là mất mát trong tập kiểm tra của chúng tôi rằng bài kiểm tra X và bài kiểm tra chuyến bay.

Vì vậy, hy vọng khi chúng tôi chạy cái này, chúng tôi sẽ thấy hành vi tương tự.

Và có vẻ như quá trình đào tạo, mất mát và mất xác nhận của chúng tôi đều giảm.

Nhưng cuối cùng thì chúng tôi cũng không thực sự cải thiện được nhiều về mặt xác thực.

Một điều có thể thú vị để khám phá ở đây là thêm điểm dừng sớm và gọi lại và chỉ

luyện tập thêm nhiều kỷ nguyên nữa và xem liệu điều này có tiếp tục giảm hay bạn đã bắt đầu

ngày càng tăng.

Hãy tiếp tục và tiếp tục nhiệm vụ tiếp theo, đó là tạo dự đoán từ bộ kiểm tra và hiển thị

một báo cáo phân loại và ma trận nhầm lẫn cho tập kiểm tra đó.

Cách chúng tôi có thể làm điều đó là từ Escalon, các số liệu sẽ tiếp tục và nhập báo cáo phân loại

và ma trận nhầm lẫn.

Chúng tôi có thể lấy dự đoán của mình bằng cách chỉ cần lấy mô hình của chúng tôi và chạy các lớp dự đoán, sau đó bạn

chỉ cần chuyển một số tính năng như kiểm tra và điều đó sẽ trả về các dự đoán, trong trường hợp đó, một lần

Vậy là xong, chúng tôi có thể in ra một báo cáo phân loại để bạn xem qua.

Rất tiếc, không phải bản in mà là báo cáo phân loại thực tế đưa ra dự đoán y đúng so với Y.

Vì vậy, chúng tôi sẽ chuyển y đúng so với dự đoán của chúng tôi và vì nhiệm vụ phân loại gợi lại nên chúng tôi sẽ

có các vòng lặp khác nhau.

Đây phải là lý do tại sao test.

Và như tôi đã nói, do nhiệm vụ phân loại nên chúng tôi sẽ có những số liệu khác nhau

có thể đánh giá điều này bằng cách sẽ có một thước đo độ chính xác, một sự thu hồi thước đo chính xác.

Và nếu một điểm có độ chính xác cao như vậy thì đó chỉ là phần trăm thực tế mà chúng tôi có được.

Phải.

Vì vậy, nếu bạn thực hiện cùng một vòng trong phần chia, chúng tôi đã thực hiện cùng một mạng.

Chúng tôi đang xem xét độ chính xác khoảng 90 phần trăm.

Nhưng hãy nhớ lại điều đó ở phần đầu của cuốn sổ này.

Vì vậy, ở phần trên cùng, điều chúng tôi đã làm là trước tiên chúng tôi phân tích nhãn thực tế và nhớ lại rằng

đó là một nhãn mất cân bằng.

Vì vậy, số tiền được thanh toán đầy đủ nhiều hơn số tiền phải trả cho các khoản vay.

Và trên thực tế, nếu chúng ta xem xét một mô hình đơn giản thu hồi bất kỳ khoản vay nào là hoàn toàn

được trả tiền, nó thực sự vẫn khá chính xác.

Vì vậy chúng ta sẽ cuộn xuống đây.

Và chỉ để cho bạn thấy điều tôi muốn nói là gì, nếu chúng ta nhìn vào khung dữ liệu ban đầu và

chúng ta biết liệu khoản vay của chúng ta đã được hoàn trả hay chưa hay chúng ta sẽ làm là hãy tính một số giá trị ở đây.

Và chúng tôi đã hoàn trả được nhiều khoản vay này.

Vì vậy, hãy tiếp tục lấy số đó và chia cho độ dài thực tế của khung dữ liệu đó.

Và chạy nó, vì vậy hãy lưu ý ở đây rằng điều này cho thấy rằng 80 phần trăm số điểm của tôi đã được

được dự đoán là khoản vay được hoàn trả, có nghĩa là nếu tôi tạo một mô hình rất đơn giản chỉ đơn giản là bất kỳ khoản vay nào

sẽ được hoàn trả, tôi sẽ chính xác 80%.

Vì vậy, đừng để bị lừa bởi một mô hình có độ chính xác 80%, bởi vì theo mặc định, một mô hình

chỉ cần luôn báo cáo lại khoản vay sẽ tự hoàn trả, sẽ chính xác 80%, ít nhiều

trên tập dữ liệu thử nghiệm tình dục.

Vì vậy, chúng ta nên xem xét ngưỡng dưới cùng là 80 phần trăm, nghĩa là 89 phần trăm của chúng tôi

độ chính xác ở đây là ổn.

Nhưng nó không hoàn toàn tuyệt vời vì tập dữ liệu không cân bằng của chúng tôi, như đã đề cập trong Machine Learning

Bài giảng về số liệu, số liệu thực tế.

Chúng tôi muốn xem xét khả năng thu hồi chính xác và điểm F1 của chúng tôi, và có vẻ như tùy thuộc vào hạng

chúng tôi thực hiện kém hơn một chút.

Vì vậy, lớp thực sự mà chúng ta nên xem xét ở đây là lớp có biểu diễn thấp hơn, bằng 0.

Vì vậy, bây giờ chúng ta có ít trường hợp bằng 0 hơn.

Ở đây chúng tôi khá giỏi về độ chính xác, nhưng thực sự điều chúng tôi gặp khó khăn là việc thu hồi và chúng tôi có thể nhận được

Điểm F1, gợi lại mức trung bình hài hòa giữa độ chính xác và khả năng thu hồi.

Vì vậy, thực sự, thông báo thực sự về việc liệu mô hình này có hoạt động tốt hay không là điểm F1 trên

lớp không.

Vì vậy, điều tôi khuyến khích bạn làm là xem liệu bạn có thể thử các tham số siêu mô hình hay không, có thể

thêm vào nhiều lớp hơn, thêm nhiều nơ-ron hơn, có thể thử xoay quanh tỷ lệ bỏ học để xem liệu bạn có thể cải thiện không

ngoài điểm 0 cơ bản sáu một điểm F1.

Được rồi, vậy điều này tốt hay xấu?

Chà, điều đó thực sự phụ thuộc vào toàn bộ bối cảnh của tình huống, liệu chúng ta có một mô hình đã

cố gắng dự đoán điều này và điểm F1 của nó.

Vì vậy, chúng tôi cần nhiều bối cảnh hơn để quyết định liệu việc thu hồi điểm F1 này có đủ tốt hay không.

Chà, chúng ta không thể nói ngay rằng độ chính xác này tốt hơn chỉ là một kiểu phỏng đoán mặc định,

đó sẽ là 80 phần trăm.

Vì vậy, mô hình này chắc chắn tốt hơn là chỉ đoán ngẫu nhiên hoặc đoán thẳng.

Vì vậy, chúng tôi đang hoạt động tốt hơn nhiều.

Một sự đoán ngẫu nhiên.

Chúng tôi sẽ nhận được độ chính xác 50 phần trăm.

Một phỏng đoán thẳng thắn về việc luôn được hoàn trả với độ chính xác 80% trong mô hình của chúng tôi là nhận được 89

độ chính xác phần trăm.

Vì vậy, chúng tôi đang hoạt động tốt hơn cả dự đoán ngẫu nhiên và khoản hoàn trả khoản vay thẳng.

OK, vậy về tổng thể, chúng ta có thể thấy rằng mô hình của chúng ta đang học được điều gì đó từ tập dữ liệu này và sau đó chúng ta có thể thấy

ma trận nhầm lẫn là tốt.

Nếu chúng tôi quan tâm đến điều đó, chúng tôi có thể tìm hiểu lý do tại sao các thử nghiệm so với dự đoán lại chạy điều đó và chúng tôi sẽ thấy

ma trận nhầm lẫn này.

Và một lần nữa, bạn có thể thấy hoặc phân loại sai rất nhiều điểm 0, điều này gây ra loại điểm thấp này.

nhớ lại.

Được rồi, với nhiệm vụ cuối cùng, giao cho khách hàng bên dưới, bạn có thể cung cấp cho riêng người này những gì chúng tôi đang làm không?

việc cần làm ở đây về cơ bản là sử dụng mô hình của chúng tôi để chạy trên một người nên chúng tôi sẽ chỉ nhập ngẫu nhiên

Seed, đặt thành từng cái một, sau đó chúng ta sẽ tạo một chỉ mục ngẫu nhiên bằng cách sử dụng cái này.

Sau đó, tắt chỉ mục ngẫu nhiên này, chúng tôi sẽ thu hút một số khách hàng mới và sau đó hiển thị các đặc điểm thực tế của họ.

Vì vậy, hãy tiếp tục và chạy cái này.

Và nếu bạn thực hiện mọi thứ theo cùng một cách, bạn sẽ có được cùng một khách hàng ngẫu nhiên mà chúng tôi có và bạn có thể chơi

rời khỏi ghế nếu bạn muốn một khách hàng ngẫu nhiên khác.

Và cách thực sự có thể dự đoán được khách hàng này trước tiên là chúng ta phải đảm bảo rằng điều này không xảy ra.

một loạt bảng điều khiển dài hơn nhưng thực chất là một con số.

Vì vậy, đây là phần khó nhất là đảm bảo dữ liệu của bạn ở đúng hình dạng.

Vì vậy, một khách hàng mới.

Bây giờ nó là một loạt phim.

Những gì tôi cần làm là lấy các giá trị trả về các giá trị tính năng này.

Và sau đó, tôi cần định hình lại nó để có hình dạng giống với dữ liệu huấn luyện mà mô hình

đã được đào tạo, trong trường hợp của chúng tôi là 1/78.

Và về cơ bản, điều đó bổ sung thêm một chút lệnh gọi khung ở đó, đó là điều mà mô hình của chúng tôi mong đợi và

thì chúng ta sẽ tiếp tục và đảm bảo rằng chúng ta chia tỷ lệ dữ liệu này để dự đoán đúng lớp.

Bởi vì việc thu hồi, mô hình của chúng tôi đã học về dữ liệu được chia tỷ lệ, vì vậy chúng tôi sẽ sử dụng công cụ chia tỷ lệ và chúng tôi sẽ làm như vậy.

Biến đổi.

Dữ liệu này và thiết lập dữ liệu đó cho khách hàng mới của chúng tôi, khách hàng của bạn cũng vậy.

Chạy nó, hãy tiếp tục và kiểm tra khách hàng mới của chúng tôi, vì vậy bây giờ chúng tôi có phiên bản thu nhỏ của khách hàng mới này

khách hàng và hãy chuyển thông tin này vào mô hình, chẳng hạn như mô hình, dự đoán các lớp trên khách hàng mới này chạy

trong mô hình của chúng tôi dự đoán rằng đó là tám giờ một.

Vì vậy, bây giờ chúng ta hãy thực sự kiểm tra xem người này có thực sự trả lại khoản vay của họ hay không.

Vì vậy, những gì chúng ta sắp làm ở đây về cơ bản là chạy lệnh tương tự ở đây.

Nhưng chúng tôi sẽ không thực sự bỏ nó.

Chúng tôi chỉ muốn cột thực tế đó ở đó, chạy nó và nếu chúng tôi nhìn vào phần dưới cùng hoặc chúng tôi chỉ có thể gọi

bản thân chúng ta, chúng ta muốn xem liệu khoản vay có được hoàn trả hay không và nó đã được hoàn trả một cách ngẫu nhiên.

Vì vậy, có vẻ như trong trường hợp cụ thể này, chúng tôi đã làm đúng.

Được rồi.

Vậy là xong cho dự án này.

Lưu ý, đó là một dự án rất lớn, nhưng phần lớn của nó thực sự là kỹ thuật tính năng và sự hiểu biết

dữ liệu.

Thông thường, khi thực sự đào tạo mô hình, đó là một nhiệm vụ đơn giản hơn nhiều vì

mô hình đang thực hiện hầu hết công việc.

Tất cả những gì bạn cần quyết định là có bao nhiêu lớp và bao nhiêu nơ-ron trên mỗi lớp.

Vì vậy, có rất nhiều lựa chọn để chơi ở đây.

Và tôi khuyến khích bạn thử nghiệm các mô hình của riêng bạn và xem liệu bạn có thể trở thành người biểu diễn của chúng tôi không

chúng tôi đã trình bày ở đây với mô hình đơn giản hơn này.

Cảm ơn.

Và tôi sẽ gặp bạn ở bài giảng tiếp theo.