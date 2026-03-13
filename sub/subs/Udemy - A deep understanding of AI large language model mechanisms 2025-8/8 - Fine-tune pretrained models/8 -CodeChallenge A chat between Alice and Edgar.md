# 8 -CodeChallenge Cuộc trò chuyện giữa Alice và Edgar

---

Thử thách viết mã này là phần tiếp theo thú vị của thử thách viết mã trước đó.

Bạn sẽ huấn luyện mô hình Alice và Edgar rồi viết mã để họ nói chuyện

với nhau.

Tôi có thể hứa với bạn rằng đây sẽ không phải là một cuộc trò chuyện hợp lý, nhưng tôi gần như có thể

đảm bảo rằng bạn sẽ vô cùng thích nó và cũng cải thiện kỹ năng và mô hình mã hóa của bạn

kỹ năng tạo và tinh chỉnh trong quá trình thực hiện.

Bài tập một rất đơn giản.

Bạn chỉ cần sao chép mã

từ thử thách viết mã trước đó

và dán nó vào một tập tin mới.

Đừng lo lắng về tần suất mã thông báo

hoặc bất kỳ đánh giá nào.

Tất cả những gì bạn cần làm cho bài tập một ở đây

là nhập mô hình, nhập văn bản,

tạo hai trình tối ưu hóa và sau đó huấn luyện hai mô hình

giống như bạn đã làm trong thử thách viết mã trước đó.

Bây giờ tôi sẽ chuyển sang mã, nhưng chỉ rất ngắn gọn,

chỉ để xem lại những phần quan trọng nhất của mã

từ bài tập trước.

Nhận một số thư viện.

Ở đây tôi đang nhập mã thông báo và các mô hình

và đẩy mọi thứ vào GPU.

Đây là nơi tôi nhận được hai văn bản,

vì vậy qua kính nhìn

và bộ sưu tập của Edgar Allen Poe và mã hóa chúng.

Và bạn có thể thấy rằng tôi không bao gồm bất kỳ thứ gì trong số đó

về việc tìm kiếm các token phổ biến nhất.

Chúng tôi không cần điều đó cho thử thách mã này.

Được rồi, đang thiết lập trình tối ưu hóa, các tham số huấn luyện,

và sau đó thực hiện quá trình đào tạo.

Đây thực sự là bài tập duy nhất trong thử thách viết mã này.

Những gì bạn thấy ở đây là cuộc trò chuyện giữa Alice và Edgar.

Vì vậy, hãy để tôi dành một chút thời gian để giải thích những gì đang xảy ra ở đây.

Tôi bắt đầu với lời gợi ý đầu tiên của Alice rằng:

xin chào, tên tôi là Alice.

Sau đó, tôi mã hóa văn bản đó và đưa nó vào mô hình Edgar

và tạo ra 50 mã thông báo mới.

Vậy đầu ra của mô hình Edgar là 57 token,

bảy cái đầu tiên trong số đó là của Alice, đầu vào,

và 50 tiếp theo được tạo ra bởi mô hình này.

50 token mới được hiển thị ở đây.

Tôi không hiển thị bảy mã thông báo đầu tiên

vì điều đó sẽ trở nên dư thừa.

Nghĩa đen là những token này ở đây.

Được rồi, vậy tôi lấy hết 57 đồng xu đó

và đưa chúng vào mô hình Alice

và yêu cầu mô hình Alice tạo ra 50 mã thông báo mới.

Vì vậy, điều đó có nghĩa là hiện tại chúng tôi có tổng cộng 107 mã thông báo.

Bảy câu đầu tiên là từ lời nhắc ban đầu của Alice.

50 tiếp theo là từ mô hình Edgar.

Và sau đó chúng ta có 50 token mới từ mô hình Alice

để đáp lại những gì mô hình Edgar đã nói.

Và sau đó, bạn có thể thấy tôi vừa trả lại cái này

qua lại.

Điều này diễn ra trong một vòng lặp for.

Vì vậy, đầu ra của mô hình Alice là đầu vào

đến mô hình Edgar, v.v.

Vì vậy, tổng chiều dài của vectơ mã thông báo tăng

mỗi lần hai người mẫu trò chuyện với nhau.

Và điều này có nghĩa là cửa sổ ngữ cảnh

để họ tạo ra văn bản mới luôn tăng lên.

Bây giờ bạn thực sự không nhìn thấy toàn bộ cửa sổ ngữ cảnh ở đây

bởi vì tôi chỉ in ra các mã thông báo mới được tạo

và không phải tất cả các mã thông báo trước đó.

Được rồi, tôi đã chạy qua vòng lặp này năm lần,

thực ra có nghĩa là 10 thế hệ kiểu mẫu

bởi vì mỗi lần lặp trong vòng lặp for

là một cặp cuộc trò chuyện từ Edgar tới Alice.

Được rồi, tôi hy vọng điều đó có ý nghĩa.

Nếu bạn sử dụng lấy mẫu xác suất,

bạn có thể chạy qua mã nhiều lần

để có được nhiều kết quả khác nhau.

Cái này tôi chọn vì nó rất tuyệt.

Edgar ngay lập tức hỏi, bạn là gì, một chiếc máy tính?

Và ý kiến của bạn về tính chất của bài báo là gì

rằng bạn đã quá nhiệt tình?

Bạn là ai?

Và nó ở đâu, điều này thú vị đây.

Vậy là Edgar đang viết, Asstan đang kinh ngạc ở đâu?

Và đó là sự kết thúc, đó là token thứ 50

mà Edgar đã nói ở đây.

Nhưng sau đó bởi vì tất cả những dòng chữ này

sau đó được nhập trực tiếp vào mô hình Alice,

mô hình Alice thực sự đã hoàn thành từ này.

Vì vậy, astan-ish có nghĩa là.

Vì vậy, đây không hoàn toàn giống như một cuộc trò chuyện

theo nghĩa là hai mô hình này

chưa được đào tạo để hiểu ý nghĩa của trò chuyện

giữa hai cá nhân, hai tác nhân.

Vậy là họ không thực sự trò chuyện với nhau

ví dụ: cách bạn trò chuyện bằng trò chuyện GPT

nhưng đó chỉ là do các mô hình như chat GPT

đã được đào tạo để biết cuộc trò chuyện trông như thế nào,

cuộc trò chuyện diễn ra thế nào, cuộc trò chuyện diễn ra như thế nào.

Và hai mô hình này chưa được đào tạo theo cách đó.

Họ chỉ đơn giản là hoàn thành chuỗi mã thông báo

và tạo chuỗi mã thông báo mới

dựa trên bối cảnh trước đó.

Tôi thực sự rất hứng thú với bài tập này

và tôi hy vọng bạn cũng tìm thấy vài điều thú vị ở đây.

Đi làm cũng hơi khó khăn

đặc biệt là với việc theo dõi tổng số mã thông báo

và chỉ in ra các mã thông báo mới được tạo.

Dù sao bây giờ bạn nên tạm dừng video

và thử làm điều này.

Và bây giờ tôi sẽ chuyển sang viết mã và thảo luận về giải pháp của mình.

Vì vậy, đây là tất cả mã cho bài tập này.

Có lẽ có một số cách đúng

bạn có thể đã thiết lập điều này.

Vì vậy, nếu giải pháp của bạn trông khác với giải pháp của tôi,

điều đó thật tuyệt, điều đó hoàn toàn ổn.

Giải pháp của bạn không cần phải giống của tôi,

giải pháp của bạn chỉ cần hoạt động.

Vì vậy, đây là cách tôi bắt đầu cuộc trò chuyện.

Xin chào, tên tôi là Alice.

Điều này được mã hóa thành mã thông báo và sau đó được in ra.

Và sau đó tôi lấy những token này và nhập chúng vào

vào mô hình Edgar,

vào phương thức generate của mô hình Edgar.

Vì vậy, đây là tất cả các token được đưa vào.

Tôi đang yêu cầu 50 token mới.

Tôi muốn một mẫu và đây chỉ là biểu thị

mã thông báo đệm.

Chúng tôi thực sự không quan tâm nhiều đến điều này,

nhưng về cơ bản điều này chỉ ngăn cản những mô hình này

gửi cho chúng tôi những thông điệp cảnh báo.

Được rồi, bây giờ phần này đã dễ dàng rồi,

tính tổng số token.

Và ở đây tôi muốn nói để giải mã

không phải tất cả các token, nhưng nó sẽ ở đây,

nếu tôi làm điều này, nó sẽ trả lại cho tôi tất cả số token,

bao gồm toàn bộ lịch sử của cuộc trò chuyện

giữa Alice và Edgar.

Nhưng đó không phải là những gì tôi muốn in ra.

Vì vậy, những gì tôi muốn in ra là

dù chuỗi mã thông báo này dài bao nhiêu,

rồi cứ thế cho đến hết.

Và điều đó sẽ mang lại cho tôi tất cả các token mới.

Bây giờ đầu ra của cái này được gọi là Edgar.

Và sau khi in cái này,

nó trở thành đầu vào của mô hình Alice.

Bây giờ hãy chú ý những gì tôi không làm ở đây.

Những gì tôi không làm ở đây là những việc như thế này.

Nếu tôi coi đây là đầu vào,

thì Alice chỉ nhìn thấy câu trả lời của Edgar.

Vì vậy, điều này rút ngắn cửa sổ ngữ cảnh.

Nếu tôi để nó như thế này,

Điều này có nghĩa là mô hình Alice không chỉ nhìn thấy câu trả lời của Edgar

mà còn cả lời nhắc ban đầu của Alice,

xin chào, tên tôi là Alice.

Vì vậy, cửa sổ ngữ cảnh mã thông báo,

trình tự ngày càng dài hơn,

điều đó có nghĩa là những mô hình này ngày càng có nhiều bối cảnh hơn

trong đó để tạo ra một câu trả lời.

Và đó là cách chúng ta có được giọng điệu trò chuyện nhiều hơn.

Được rồi, tôi hy vọng tất cả đều có ý nghĩa.

Vì vậy, đầu ra của Edgar lại là đầu vào của Alice,

nhưng ở lần chạy thứ hai trong quá trình lặp lại này,

nó không còn là chuỗi mã thông báo ban đầu này nữa,

đó là chuỗi mã thông báo do mô hình này xuất ra,

trong đó bao gồm tất cả các cuộc trò chuyện trước đó.

Được rồi, mọi chuyện bắt đầu hơi kỳ lạ rồi đây.

Nhà của những người đó sẽ không được hoàn trả.

Được rồi, nhưng để xem nào.

Xin chào, tên tôi là Alice.

Nhưng điều gì sẽ xảy ra nếu đây chỉ là một bóng ma hoặc một sự mâu thuẫn,

điều mà tôi nghi ngờ.

Tôi cho rằng đó là một số biến thể trong tính cách của,

sau đó Alice nói,

hình dung bạn khó có thể nghĩ về nó như bất cứ điều gì hơn

hơn một số Python.

Tôi không biết Python là gì,

nhưng nó chắc chắn giống như thứ bạn sẽ đọc

trong Alice qua tấm gương soi.

Những gì bạn lập trình ở đây rất gần với cách mọi thứ hoạt động

với các bot trò chuyện như trò chuyện GBT.

Có nhiều token đặc biệt hơn khi trò chuyện

cho phép bot trò chuyện nhận ra

và phân biệt đầu vào của người dùng với đầu vào của chính nó.

Và bạn sẽ tìm hiểu thêm về những loại chi tiết đó

trong phần tiếp theo về điều chỉnh lệnh.

Nhưng những gì bạn làm ở đây về cơ bản là những gì đang diễn ra

hậu trường khi bạn trò chuyện với bot trò chuyện.

Và vâng, nếu bạn nhận được bất kỳ cuộc trò chuyện thực sự thú vị nào

giữa Alice và Edgar, vui lòng chụp ảnh màn hình

và đăng chúng lên phần hỏi đáp.