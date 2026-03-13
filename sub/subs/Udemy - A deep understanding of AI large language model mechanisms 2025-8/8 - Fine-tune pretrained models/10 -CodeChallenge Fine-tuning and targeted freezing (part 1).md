# 10 -CodeChallenge Tinh chỉnh và đóng băng có mục tiêu (phần 1)

---

Nếu bạn tò mò từ xa về khả năng và tác động của việc tinh chỉnh, thì tôi nghĩ bạn

sẽ thực sự thích thú với thử thách viết mã này.

Chúng tôi sẽ thực hiện việc đóng băng chính xác và đo lường tác động của việc đóng băng đối với quá trình tập luyện

mất mát, tỷ lệ sử dụng mã thông báo phổ biến và thời gian tính toán đào tạo.

Có rất nhiều việc phải làm ở đây, vì vậy hãy bắt đầu.

Và bạn chắc chắn cũng sẽ rất vui khi biết rằng chúng tôi sẽ không hợp tác với Gulliver's

Du hành hoặc với cỗ máy thời gian.

Chúng ta sẽ chuyển sang cuốn sách nổi tiếng Moby Dick.

Điều này có sẵn trên Gutenberg.org.

Bạn có thể dễ dàng tìm thấy nó trên trang web của họ.

Hoặc bạn chỉ có thể kiểm tra tệp trợ giúp hoặc tệp giải pháp để tìm URL trực tiếp.

Khi bạn nhập và mã hóa cuốn sách này, bạn sẽ thấy rằng có khoảng 350.000

mã thông báo, chỉ có 17.000 trong số đó thực sự là mã thông báo duy nhất.

Bản thân điều đó khá thú vị vì nó có nghĩa là

mà cuốn sách thực sự không có

một vốn từ vựng rất lớn.

Dù sao đi nữa, bạn muốn tìm 100 token được sử dụng thường xuyên nhất

trong cuốn sách đó.

Lần cuối cùng chúng tôi làm điều này, chúng tôi cũng đã áp dụng bộ lọc

số mã thông báo cần dài hơn hai ký tự.

Tôi không đưa ràng buộc đó vào đây, mặc dù bạn có thể đưa nó vào nếu muốn.

Ở đây bạn sẽ thấy một vài kết quả trong số đó, và nếu bạn biết chút gì về Moby Dick, bạn sẽ

không ngạc nhiên khi từ cá voi là một trong những từ được sử dụng phổ biến nhất trong cuốn sách.

Vì vậy, phần bài tập 1 này chủ yếu nói về việc nhập và mã hóa văn bản.

Tiếp theo các bạn muốn tạo 2 mô hình GPT, 2 mô hình Neo từ eluthor thì tải về

chính xác cùng một mô hình hai lần với hai biến riêng biệt và bạn chắc chắn muốn đẩy

những thứ này tới GPU.

Bây giờ lý do tại sao bạn muốn có hai mô hình, hoặc thực tế là cùng một mô hình ở hai mô hình khác nhau

biến là chúng ta sẽ đóng băng các phần của một mô hình và rời khỏi hoàn toàn mô hình kia

Và điều đó tạo nên một cách tiếp cận thử nghiệm thực sự thú vị vì các mô hình bắt đầu giống hệt nhau

và họ sẽ được huấn luyện trên dữ liệu giống hệt nhau theo thứ tự giống nhau. Sự khác biệt duy nhất giữa

hai mô hình này sẽ là một mô hình có một số ma trận trọng số bị cố định. Bây giờ là phần cuối cùng

của bài tập một là đếm tỷ lệ mã thông báo được tạo ra

trong mã thông báo Moby Dick thường xuyên nhất. Đây chính xác là ý tưởng tương tự và

cách tiếp cận mà bạn đã sử dụng cho video Alice đấu với Edgar. Và chỉ để bạn thấy

điều này sẽ diễn ra ở đâu, trong bài tập 4 bạn sẽ tạo ra một hình

trông như thế này, hiển thị phần trăm số token

được tạo ra bởi hai mô hình trước và sau khi tinh chỉnh.

Tôi gọi hai mô hình này là đóng băng và đào tạo.

Đó là một chút sai sót

bởi vì chúng tôi cũng đang đào tạo mô hình đóng băng,

nhưng sắp tới, mô hình này sẽ chứa

rất nhiều lớp cố định, ma trận trọng số cố định,

và ở đây với mô hình này,

toàn bộ mô hình sẽ được tinh chỉnh.

Được rồi, vậy điều bạn sắp làm bây giờ là tính toán các thanh màu xanh tương ứng ở đây

trước khi đào tạo trước khi chúng ta bắt đầu tinh chỉnh.

Bạn không cần phải tạo đồ họa này ở đây.

Tôi chỉ cho bạn xem để bạn biết chúng ta đang đi đâu.

Được rồi, đó là bài tập một.

Tạm dừng video và thực hiện bài tập này.

Và bây giờ tôi sẽ chuyển sang mã.

Dưới đây là tất cả các thư viện mà chúng tôi sẽ sử dụng, bao gồm một số thư viện mà chúng tôi sẽ sử dụng

sử dụng cho các bài tập sau, nhưng tôi đã đặt chúng ở đây.

Ở đây tôi đang nhập mã thông báo eluthor, như bạn nhớ ở phần trước của khóa học.

Đây chính xác là mã thông báo giống như mã thông báo AI GPT mở.

Tuy nhiên, bản thân các mô hình là khác nhau.

Sau đó, bạn có thể thấy hai dòng mã này giống hệt nhau ngoại trừ biến này ở đây.

Vì vậy, mô hình cố định, có một số lớp cố định và một số lớp có thể huấn luyện được, và mô hình huấn luyện,

điều này hoàn toàn có thể đào tạo được.

Được rồi, vậy hãy nhập cái đó.

Và sau đó tôi đẩy chúng vào GPU ở đây.

Được rồi, bây giờ chúng ta bắt đầu thực hiện một bài tập.

Ở đây tôi đang nhập văn bản Moby Dick và báo cáo tổng số mã thông báo và số duy nhất

mã thông báo.

Và ở đây tôi đang đếm tần số mã thông báo.

Bạn đã từng thấy mã này trước đây.

Được rồi, và như bạn đã thấy trước đây, những token phổ biến nhất hoặc ít nhất là nhiều token

mã thông báo phổ biến nhất, là những mã thông báo thực sự phổ biến mà bạn mong đợi trong bất kỳ văn bản nào.

Vì vậy, các dòng mới, dấu phẩy, dấu chấm, v.v.

Dấu chấm phẩy, dấu chấm than,

rõ ràng có rất nhiều câu cảm thán ẩn chứa trong đó, Moby Dick.

Nhưng chúng ta cũng thấy những từ như cá voi,

và một cho ahab, tôi nghĩ vậy.

Và vâng, đây là nơi ở của ahab.

Và tôi nghĩ con tàu, vâng, con tàu đây.

Vì vậy, bạn biết đấy, c,

có một số token mà bạn có thể không ngờ tới

thấy với tần suất cao như vậy trong rất nhiều văn bản khác.

Đây là mã mà bạn đã thấy trước đây,

mặc dù không hoàn toàn giống nhau,

nhưng đó là mã để tạo mã thông báo

dựa trên các chỉ số bắt đầu ngẫu nhiên.

Sẽ có 10 đợt, mỗi đợt 100 mã thông báo được tạo.

Vậy là bạn đã từng thấy điều này trước đây và vâng,

vậy thì xuống đây tôi đang tính tỷ lệ

trong số các mã thông báo được tạo nằm trong 100 mã thông báo Moby Dick hàng đầu.

Vì vậy, quá trình này mất khoảng một phút để chạy và ở đây chúng tôi tìm thấy ở 40% phía trên, tức là 47 và 44% của

mã thông báo được tạo bởi các mô hình cơ sở được đào tạo trước này là mã thông báo cũng xuất hiện trong

top 100 của cuốn sách Moby Dick.

Và tất nhiên, câu hỏi đặt ra là điều gì xảy ra với những con số này sau khi chúng ta tinh chỉnh

các mô hình?

Bây giờ đến bài tập thứ hai.

Mục tiêu của bài tập này là viết mã để thực hiện việc đóng băng chính xác theo mục tiêu.

Đặc biệt, bạn chỉ muốn tập luyện các trọng số chú ý và chỉ trong máy biến áp

khối sáu và cao hơn.

Một cách khác để nghĩ về điều này hoặc diễn đạt điều này là bạn đang đóng băng toàn bộ mô hình

ngoại trừ các trọng số chú ý trong các khối biến áp sau này.

Vì vậy, đây là một sự tinh chỉnh rất có chọn lọc, rất có mục tiêu.

Bây giờ có một chút khó khăn để triển khai điều này trong mã.

Bạn cần tìm kiếm ma trận trọng số Q, K và V để không bị đóng băng

ma trận W0, là ma trận biến đổi tuyến tính

kết hợp tất cả những khám phá

từ những sự chú ý khác nhau hướng tới nhau

trước khi được gửi đến các lớp MLP.

Được rồi, vậy là bạn không muốn huấn luyện ma trận W0.

Bạn cũng không muốn huấn luyện ma trận trọng số QKV

trong các lớp từ 0 đến 5.

Đây là gợi ý giúp bạn bắt đầu với việc lọc.

Nếu bạn lấy tên tham số và chia nó ra

theo thời gian, sau đó bạn sẽ nhận được một danh sách

với mỗi phần tử danh sách tương ứng

đến một thành phần của tên.

Và từ đây, bạn có thể viết một số mã

để thực hiện một số tìm kiếm và kiểm tra

để xem liệu mỗi thông số

tương ứng với thứ mà bạn muốn đóng băng

hoặc một lớp mà bạn muốn duy trì khả năng huấn luyện.

Tôi khuyên bạn nên in ra danh sách các thông số giống như những gì tôi đã trình bày trong video trước.

Nó sẽ trông giống như thế này.

Vì vậy, ở đây bạn thấy hầu hết các dấu trừ vì hầu hết các lớp trong mô hình này đều bị đóng băng.

Và chúng ta có các dấu cộng chọn lọc chỉ cho các ma trận trọng số K, V và Q, chỉ trong

các khối phụ chú ý và chỉ ở các lớp từ 6 đến 11.

Vì vậy, bạn có thể thấy ở đây rằng chúng tôi thực sự chỉ đang đào tạo một số lượng rất nhỏ trong tổng số

các tham số trong mô hình.

Bây giờ đối với video này, hãy cố gắng đừng suy nghĩ quá nhiều về lý do tại sao chính xác chỉ có những thông số này.

được huấn luyện chứ không phải các tham số khác trong mô hình.

Tôi thiết lập các hướng dẫn ở đây chủ yếu là để cho bạn cơ hội đảm bảo rằng bạn thực sự

biết cách xác định các lớp cụ thể và bật hoặc tắt độ chuyển màu của chúng.

Vậy là xong bài tập này.

Bây giờ bạn nên tạm dừng video và bây giờ tôi sẽ chuyển sang viết mã và thảo luận về giải pháp của mình.

Mã này ở đây chỉ hiển thị ảnh chụp màn hình hoặc mã tạo ảnh chụp màn hình

mà tôi đã trình bày trong các slide.

Ở đây tôi đang lặp lại tất cả các tham số đã đặt tên và chỉ tách chúng ra.

Vì vậy tất nhiên bạn nhận ra tất cả những cái tên này

của các lớp khác nhau.

Điều mới duy nhất ở đây là chúng được chia ra

vào một danh sách với các chuỗi khác nhau

ở giữa các khoảng thời gian dưới dạng các mục danh sách riêng biệt.

Bạn cũng có thể thấy rằng một số trong số này là,

giống như hai lớp này ở đây,

ma trận nhúng mã thông báo và vị trí chỉ là ba.

Chỉ có ba yếu tố trong danh sách này.

trong khi các danh sách khác, tên khác dài hơn.

Và vì vậy tôi có nhiều phần tử danh sách hơn.

Được rồi, ô tiếp theo ở đây chỉ là ô thử nghiệm.

Đây là mã mà tôi đang sử dụng

để khám phá và phát triển bộ lọc của tôi.

Vì vậy hãy chú ý rằng ở đây trong ô này,

Tôi thực sự không thay đổi bất cứ điều gì trong mô hình.

Ví dụ, tôi không viết,

Tôi không thay đổi giá trị của yêu cầu grad.

Vì vậy tất cả những gì tôi đang làm là xem xét mọi yếu tố trong,

hoặc mọi tham số được đặt tên trong mô hình

và in ra những cái phù hợp với bộ lọc

mà tôi muốn sửa đổi.

Vì vậy, ở đây bạn thấy, nếu độ dài của chuỗi phân tách

lớn hơn năm,

và tại sao tôi muốn số này lớn hơn 5?

Đó là bởi vì ở đây tôi sẽ cần truy cập

phần tử thứ sáu trong danh sách.

nhưng một số trong số này không có sáu yếu tố.

Vì vậy, điều đó sẽ gây ra lỗi Python.

Vì vậy, ở đây chúng tôi đã dừng lại nếu độ dài của chuỗi này,

danh sách này quá nhỏ.

Được rồi, sau đó tôi cũng chỉ muốn lọc

trong đó phần tử thứ tư có từ chú ý hoặc ATTN.

Vì vậy, ví dụ ở đây là phần tử số 0, phần tử một, hai, ba.

hai, ba.

Được rồi, đây là MLP không gây được sự chú ý.

Điều đó có nghĩa là phần tử này bị bỏ qua.

Mặt khác, đây là sự chú ý.

Vì vậy, điều đó chuyển sang tuyên bố tiếp theo ở đây.

Vậy thì tôi muốn nói, là yếu tố thứ hai hay thứ ba

trong chỉ số hai tương ứng với con số này ở đây?

Bây giờ, đây không thực sự là một con số, đây là một chuỗi.

Vì vậy, chúng tôi chuyển đổi nó thành một số nguyên

và sau đó xem liệu nó có lớn hơn 5 không.

Và đây là cơ chế mà tôi có thể chọn

chỉ các ma trận trọng số ở khối sáu trở lên.

Và cuối cùng, tôi kiểm tra xem chữ cái đầu tiên

trong phần tử thứ sáu là Q, V hoặc K.

Và về cơ bản điều đó sẽ chuyển những điều này qua

và nó sẽ loại trừ hai tham số này ở đây,

đó là ma trận trộn tuyến tính W0.

Được rồi, sau đó tôi in ra cái tên vừa xác nhận

rằng điều này mang lại cho tôi những thông số mà tôi muốn.

Bây giờ tôi lấy tất cả mã này, sao chép nó,

và dán nó xuống đây,

và sau đó tôi thực sự sửa đổi tham số requireGrad,

rồi in thông báo này ra đây.

Bây giờ, vì giá trị mặc định của require grad là đúng nên bạn thực sự không cần điều này

dòng.

Tuy nhiên, khi tôi viết mã này, tôi muốn thay đổi mọi thứ, thay đổi bộ lọc

qua lại.

Vì vậy, tôi liên tục bật và tắt các nút bật tắt này.

Vì vậy, tôi quyết định để lại điều này ở đây chỉ để chắc chắn một chút.

Được rồi, bây giờ chúng ta thấy hầu hết các dấu hiệu ở đây là dấu trừ, có nghĩa là chúng

Họ bị đóng băng, họ không thể huấn luyện được.

Hiện nay rất ít lớp trong số này thực sự có thể huấn luyện được.

Bài tập ba liên quan đến việc đào tạo các mô hình

và cũng kết hợp mã vào vòng đào tạo

để theo dõi một số tính năng của các mô hình.

Bây giờ chính vòng lặp đào tạo,

bạn hầu như có thể sao chép từ các video trước đó.

Một số thông số giống nhau.

Tôi đã sử dụng 474 kỷ nguyên đào tạo

và tốc độ học là 0,0005.

Cái đó lớn hơn một chút

hơn mức tôi thường sử dụng để tinh chỉnh,

nhưng rất nhiều mô hình này đã được tinh chỉnh hoặc bị đóng băng

rằng việc tinh chỉnh thực sự mang lại lợi ích

có tỷ lệ học tập cao hơn một chút.

Được rồi, ngoài việc tinh chỉnh những mô hình này,

có một vài điều nữa mà bạn cần thêm vào đây.

Một là bạn muốn tính thời gian cho đường chuyền tiến và lùi

cho mỗi lần lặp lại quá trình đào tạo.

Vì vậy, mã vòng lặp đào tạo của bạn sẽ trông giống như thế này.

Cả khu nhà này ở đây,

đây là để đào tạo mô hình đóng băng.

Và tôi đã chia nó thành hai phần nhỏ

cho đường chuyền về phía trước và chỗ dựa phía sau.

Và bạn có thể thấy dòng đầu tiên trong đoạn mã này

là để có được thời gian đồng hồ hiện tại

và sau đó lưu nó dưới dạng một biến.

Và dòng cuối cùng trước khi chuyển sang mô hình tiếp theo

là lấy lại thời gian trên đồng hồ hiện tại,

trừ đi thời gian bắt đầu,

và đây là tổng thời gian đã trôi qua

giữa dòng mã này,

vì vậy sự bắt đầu của đường chuyền tiếp theo

và phần cuối của backprop và lưu trữ sự mất mát.

Và thời gian trôi qua này được tổng hợp lại,

được tích lũy vào biến thời gian miễn phí này.

Vì vậy tổng thời gian đang được tích lũy,

không chỉ cho một lần lặp, mà cho tất cả các lần lặp,

tất cả 474 lần lặp.

Khi bạn viết mã cho mô hình đóng băng,

bạn chỉ cần sao chép và dán nó xuống đây cho mô hình xe lửa

và chỉ cần siêng năng thay đổi tên biến

đến mô hình tàu hỏa.

Vì vậy, đó là một điều chỉnh cần thực hiện đối với mã đào tạo.

Một điều chỉnh khác cần thực hiện là theo dõi

những thay đổi liên quan đến việc học ở một trong các tham số

có thể huấn luyện được trong cả hai mô hình.

Vì vậy tôi đã chọn ma trận WK từ khối biến áp thứ bảy.

Bây giờ không có gì đặc biệt có ý nghĩa về mặt lý thuyết

về ma trận này ngoại trừ việc nó có thể huấn luyện được

trong cả hai mô hình mà chúng tôi đang làm việc ở đây.

Nhân tiện, đây không phải là địa chỉ đầy đủ

với ma trận trọng số đó, tôi đã rút ngắn nó ở đây

vì vậy nó sẽ in đẹp trong dòng.

Vì vậy, ý tưởng là bạn muốn trừ ma trận trọng số

từ lần lặp hiện tại tương đối

đến lần lặp trước đó trong quá trình huấn luyện.

Điều đó sẽ cung cấp cho bạn một ma trận khác biệt

và bạn có thể tính định mức của sự khác biệt ma trận đó.

Vì vậy, điều này có nghĩa là bạn sẽ cần có cách theo dõi ma trận mỗi khi nó cập nhật trong quá trình tinh chỉnh để thu được ma trận WK ở mỗi lần lặp với cùng ma trận WK từ lần lặp trước đó trong quá trình huấn luyện.

Bây giờ bạn không cần thực hiện bất kỳ hình dung nào cho bài tập này mà chỉ cần thiết lập vòng lặp đào tạo và chạy nó.

Và nhân tiện, như tôi đã đề cập vài lần trước đây,

khi bạn vừa mới thiết lập mã,

Tôi khuyên bạn chỉ nên chạy qua năm,

có thể là 10 mẫu đào tạo dữ liệu.

Và đó là bởi vì khi bạn viết mã

và gỡ lỗi, xử lý và phát triển mã,

bạn muốn có thể lặp lại

và cải thiện nhanh nhất có thể.

Và một khi bạn tự tin rằng mã của mình tốt,

sau đó bạn có thể tăng số lần lặp đào tạo.

Dù sao, chúc may mắn làm việc thông qua điều này.

Và bây giờ tôi sẽ chuyển sang mã và hiển thị giải pháp của mình.

Chúng tôi đang đào tạo hai mô hình khác nhau.

Và vì vậy chúng ta cần hai trình tối ưu hóa khác nhau.

Trên thực tế, nó chính xác là cùng một trình tối ưu hóa,

nhưng tôi nhận được hai trường hợp khác nhau về nó,

một cho mỗi mô hình.

Được rồi, vậy hãy chạy nó.

Dưới đây là một số thông số điển hình.

Và thực ra, bạn biết đấy, chỉ như một lời nhắc nhở nhỏ,

Chúng tôi không chỉ định hàm mất ở đây.

Bạn có thể nếu bạn muốn, nhưng nó thực sự không cần thiết

bởi vì với những mô hình được cung cấp này

thông qua khuôn mặt ôm, nếu bạn nhập nhãn bằng

và sau đó sử dụng các mã thông báo tương tự như những gì bạn nhập

ở đầu vào đầu tiên, sau đó mô hình sẽ nội bộ

tính toán tổn thất bằng cách dịch chuyển các token này,

chuyển đổi nhật ký thành nhật ký softmax

và tính toán khả năng ghi nhật ký âm.

Và điều đó xuất hiện trong kết quả đầu ra.loss.

Được rồi, đó chỉ là một lời nhắc nhở nhỏ.

Được rồi, ở đây tôi đang bắt đầu các khoản lỗ

để theo dõi hai mô hình.

Và đây là tiêu chuẩn delta.

Đây là cách tôi sẽ theo dõi,

hoặc lưu trữ định mức của ma trận sai phân

của ma trận trọng số WK đó trong quá trình huấn luyện.

Ở đây tôi đang khởi tạo vectơ thời gian, thời gian tính toán bằng 0 và tại mỗi thời điểm

lặp đi lặp lại trong quá trình đào tạo, tôi sẽ tiếp tục bổ sung thêm ngày càng nhiều thời gian đồng hồ vào phần này.

Vì vậy, điều này sẽ phản ánh tổng thời gian đào tạo chứ không chỉ thời gian đào tạo cho một lần lặp.

Được rồi, tôi đang lấy ma trận WK trước đó.

Tôi quên mất tại sao tôi lại gọi nó là M ở đây, nhưng điều đó không quan trọng.

Đó là từ mô hình này, mô hình đóng băng, máy biến áp,

lớp ẩn thứ sáu, chú ý, chặn ma trận chú ý,

phép chiếu k, vì vậy đây là tuần, và sau đó là trọng số.

Và ở đây tôi tách nó ra.

Được rồi, đó là ma trận tuần trước khi chúng ta bắt đầu

tinh chỉnh.

Tôi sẽ cho bạn thấy điều gì xảy ra với hai biến này

trong một khoảnh khắc.

Ở đây chúng tôi thực hiện đào tạo, lấy một loạt dữ liệu,

Bạn đã nhìn thấy điều này nhiều lần trước đây.

Đây chỉ là một số dữ liệu ngẫu nhiên

từ bất cứ nơi nào trong cuốn sách.

Được rồi, đồng hồ bắt đầu tính giờ rồi,

xóa các gradient trước đó,

thực hiện đường chuyền về phía trước.

Chúng tôi tính toán tổn thất, chúng tôi tính toán ngược lại,

thực hiện điều chỉnh trọng số, lưu trữ tổn thất,

rồi cập nhật thời gian tích lũy.

Vì vậy mà bạn đã thấy trước đây.

Mã này hoàn toàn giống nhau,

nhưng đối với mô hình xe lửa.

Vì vậy, mô hình mà tôi chưa thay đổi

bất kỳ cấp độ nào được yêu cầu, đều yêu cầu tham số cấp độ.

Được rồi, đây cũng là mã mới để lấy định mức ma trận

về sự khác biệt của ma trận trọng số

ở mỗi bước trong quá trình đào tạo.

Vì vậy ở đây tôi viết torch.norm

và có hai ma trận ở đây.

Đầu tiên là địa chỉ rất dài này

để có được chính xác ma trận này ở đây,

WK từ khối chú ý thứ sáu,

trừ đi biến mà tôi đã chỉ định

trước vòng đào tạo.

Và sau đó tôi xác định lại biến đó,

bây giờ nó là cái trước, vâng, chính xác là cái này.

Vì vậy đây là đoạn mã cho phép tôi theo dõi sự thay đổi

trong ma trận trọng số từ lần lặp hiện tại trong quá trình huấn luyện

đến lần lặp trước đó trong quá trình huấn luyện.

Phần 1 của thử thách viết mã này kết thúc ở đây.

Tuy nhiên, còn hai bài tập nữa phải làm.

Tôi cắt video ở đây vì muốn các bạn đứng dậy, duỗi chân, nghỉ ngơi một chút

phá vỡ.

Khi đã sẵn sàng, bạn có thể quay lại và tiếp tục thử thách viết mã này trong video tiếp theo.