# 8 -CodeChallenge HellaSwag evals in two models (phần 1) đã dịch

---

Chào mừng bạn đến với thử thách mã này. Mục tiêu ở đây sẽ là tích hợp điểm chuẩn Helliswag

đánh giá mà bạn đã tìm hiểu về hai video trước bằng phương pháp nhập có độ chính xác thấp,

các mô hình có thông số cao mà bạn đã tìm hiểu ở video trước. Và trên đường đi,

chúng ta sắp gặp một điều gì đó rất khó hiểu, điều này sẽ khiến tôi phải giới thiệu cho bạn một chút

công thức thay thế của ma trận chú ý, cũng như một thủ thuật thông minh được sử dụng trong

thư viện bit và byte. Hãy bắt đầu. Mục tiêu của bài tập một là nhập tham số Zephyr 7B

mô hình bằng cách sử dụng thư viện bit và byte như tôi đã giới thiệu cho bạn trong video trước. Sau đó tôi muốn bạn

in ra mô tả mô hình và xem xét tất cả các thành phần của mô hình để đảm bảo bạn

nhận ra tên và sau đó nghĩ về kích thước mà bạn thấy được báo cáo ở đây. Tiếp theo, hãy đếm

tổng số tham số trong toàn bộ mô hình bằng cách sử dụng thông số hiểu danh sách và tham số dấu chấm của mô hình.

Ở đây tôi chỉ sử dụng M làm cách viết tắt, nhưng điều này sẽ lặp lại tất cả các tham số

trong mô hình để đếm tất cả. Bạn có thể hiển thị kết quả của mình như thế này, đếm tổng số

các tham số và tổng số tham số có thể huấn luyện được cũng như tổng số tham số không thể huấn luyện được

các thông số. Hãy nhớ rằng các tham số có thể huấn luyện được nếu chúng có thuộc tính PyTorch

yêu cầu grad bằng đúng. Bây giờ đằng sau hộp này, tôi liệt kê tổng số tham số bằng cách sử dụng

dấu phẩy sau mỗi ba chữ số rồi ở đây mình đã chia tỷ lệ hai số này cho gần nhất

tỷ với hai số sau dấu thập phân. Và cảnh báo spoiler, bạn sẽ nhận được một con số

ở đây mà bạn có thể không mong đợi để xem. Hãy nhớ rằng số 7 trong 7B trong tên mẫu máy này có nghĩa là có

là 7 tỷ tham số. Vì vậy, về mặt lý thuyết, tổng số tham số ở đây phải ở đâu đó

khoảng 7 tỷ. Và sau đó, như tôi đã đề cập, bạn sẽ nhận được một con số mà bạn có thể không

mong đợi. Vì vậy, để xác nhận điều tôi muốn bạn làm là đếm thủ công số lượng tham số

nên dựa trên những con số trong mô tả này ở đây. Bây giờ đừng lo lắng, tôi không có ý nói rằng bạn

phải in ra tất cả 7 tỷ cái này và đếm từng cái một. Ý tôi là theo

mô tả này, ma trận nhúng là 32.000 x 4.096. Vì vậy tổng số tham số trong

lớp này chỉ là tích của hai số này. Và khi đó chúng ta có ma trận Q là 4.096

bằng 4.096 và có 32 trong số đó. Vì vậy bạn có thể chỉ cần nhìn vào danh sách này, nhân tất cả những con số này

cho các kích thước ma trận và cộng tất cả chúng lại. Và nếu bạn làm điều đó, nếu bạn nhân kích thước lên

và tổng hợp chúng cho tất cả các thành phần được liệt kê trong mô hình này ở đây, mang đến cho bạn một cái nhìn khác

cách đếm tổng số tham số trong mô hình. Và đó chính là dòng cuối cùng ở đây

tương ứng với. Tôi hy vọng bạn thấy bài tập này thú vị và có lẽ cũng khó hiểu. tôi đang đi

chuyển sang Python để hiển thị giải pháp của tôi và sau đó tôi sẽ giải thích một số điểm khó hiểu

chi tiết hơn khi tôi quay lại các slide. Tôi đã chạy hai dòng mã này và

đã khởi động lại phiên của tôi. Vì vậy, bây giờ tôi chỉ có thể nhập tất cả các thư viện này, bao gồm cả bộ dữ liệu chẳng hạn.

Thư viện này tôi không tin là mình đã từng sử dụng trước đây, TQDM, nó là thanh tiến trình cho bốn vòng.

Nó được sử dụng khá thường xuyên khi bạn phải thực hiện vòng lặp bốn lần để duyệt qua nhiều mục có thể mất một thời gian.

lâu rồi. Vì vậy, phần này sẽ cập nhật thanh tiến trình, tôi sẽ cho bạn thấy nó trông như thế nào và hoạt động như thế nào

trong một khoảnh khắc. Được rồi, ở đây tôi sẽ nhập mô hình Zephyr bằng cách sử dụng chính xác mã mà tôi đã hiển thị

trong video trước. Như vậy là chúng ta đã import thành công mẫu này. Bạn có thể thấy nó khá lớn. Mỗi người

trong số các phần của mô hình này, tất cả các phần riêng lẻ, có dung lượng khoảng hai gigabyte và có

nhiều mảnh đó. Được rồi, hãy chuyển nó sang chế độ đánh giá, đẩy nó vào GPU. Và bây giờ chúng ta cũng có thể

thực ra, hãy để tôi chuyển sang tài nguyên xem ở đây. Bạn có thể thấy rằng tôi đang sử dụng GPU A100 trên

Colab và tôi đã sử dụng 7 trong số 40 gigabyte chỉ để lưu trữ mô hình. Và đây là

Phiên bản lượng tử hóa 4 bit rút gọn của mô hình. Vì vậy, ngay cả phiên bản lấy mẫu xuống cũng khá lớn.

Được rồi, vậy chúng ta thấy gì ở đây? Hãy để tôi làm cho nó lớn hơn một chút. Được rồi, các phần nhúng, bạn đã thấy

trước đây, 32.000 chúng ta có thể suy ra rằng có 32.000 mã thông báo và số chiều nhúng là

4.096. Nó lớn hơn gấp năm lần so với phiên bản nhỏ hơn của GPT2 và lớn hơn gấp bốn lần so với phiên bản GPT2.

phiên bản lớn của GPT2. Vì vậy, bạn có thể thấy rằng những mô hình lớn hơn này sẽ lớn hơn rất nhanh. Và bởi vì

ma trận nhúng này là 4.000, điều đó có nghĩa là ma trận chú ý cũng sẽ là

4.000. Bây giờ đây là lúc mọi thứ bắt đầu trở nên hơi khó hiểu. Bạn đã học được điều đó và bạn đã thấy

rằng trong mô hình GPT2, tất cả các ma trận W này cho thuật toán chú ý đều là hình vuông. Vì thế tất cả họ đều

768 x 768 hoặc 1024 x 1024. Vì vậy, bạn có thể mong đợi rằng cả bốn ma trận này đều bằng 4.096 x

4.096. Nhưng ở đây hóa ra ma trận trọng số K và V không vuông góc. Chúng có hình chữ nhật.

Chúng là những ma trận cao. Họ là 4.096 x 1.024. Vậy chiều rộng bằng một phần tư chiều cao của họ.

Và ở đây trong lớp MLP, chúng ta cũng có một kiến ​​trúc trông hơi khác một chút.

Vì vậy, trong các mô hình GPT, bạn thường chỉ thấy hai ma trận ở đây. Vì vậy, một trong đó mở rộng

chiều và một ma trận thu gọn chiều. Và đó thực chất là những gì

hai ma trận làm được. Vậy chúng ta có 4.096 tăng lên 14.000. Và nếu tôi nhớ không nhầm thì tôi tin điều này

là 3,5 lần. Vì vậy, nó không hẳn là một bản mở rộng gấp 4 lần. Đó là một bản mở rộng 3,5 lần. Bạn có thể kiểm tra số học của tôi

trên đó. Tôi có thể sai. Và sau đó chúng ta có lớp co lại từ 14.000 trở lại 4.000.

Và vấn đề với ma trận trọng lượng cổng này là gì? Tại sao chúng ta có lên xuống rồi có cổng?

Chà, hóa ra kiến trúc này từ Mistral, nó là một cách thay thế hơi khác

thiết lập lớp MLP. Vì vậy, họ có điều này lên xuống. Và ở giữa có sự phi tuyến tính.

Đó là hàm C-LU có thể so sánh với GALU, nhưng hơi khác một chút. Nó chỉ khác

hàm kích hoạt phi tuyến. Và ý tưởng là hình chiếu cổng này thực sự có tỷ lệ

tính phi tuyến sau cái này. Vì vậy chúng ta đi lên và sau đó có một sự phi tuyến kết hợp lại

với đầu ra của sự chú ý. Vì vậy, đầu ra của ma trận trộn tuyến tính này ở đây, mà họ gọi là

O cho đầu ra. Trước đây tôi đã gọi nó là W0 hoặc ma trận trộn tuyến tính. Và sau đó điều đó được

được chiếu lên và biến đổi phi tuyến. Và sau đó nó được kết hợp với một phiên bản khác của

cái này, được chia tỷ lệ tuyến tính theo cùng một chiều mở rộng, nhưng không được biến đổi phi tuyến tính.

Được rồi, tôi hy vọng điều đó có ý nghĩa. Tôi không đi sâu vào loại kiến trúc này ở phần trước của khóa học

bởi vì nó chỉ là một biến thể của thứ bạn đã thấy trước đây. Được rồi, và tất nhiên là chúng tôi

có một định mức lớp và như vậy. Vì vậy, bây giờ chúng ta hãy đếm tất cả các tham số. Vậy ở đây tôi có tổng

trên nummL cho p trong các tham số dấu chấm của mô hình zephyr. Vì vậy việc lặp lại tất cả các tham số trong mô hình

và sau đó đếm tất cả các phần tử trong mỗi ma trận này, từng ma trận tham số.

Vì vậy, đó là tổng số tham số. Và ở đây tôi có số lượng tham số có thể huấn luyện được

đó chính xác là cách hiểu danh sách giống như tôi có ở đây, ngoại trừ việc tôi thêm một phần bổ sung

yêu cầu cho biết nếu yêu cầu grad bằng đúng. Vậy điều đó có nghĩa là số đếm này ở đây sẽ là một

tập hợp con của số này ở đây. Vì vậy, điều đó mang lại cho chúng ta tổng số có thể huấn luyện được, tổng số tham số, tổng số

các tham số có thể huấn luyện được và các tham số không thể huấn luyện được chỉ là sự khác biệt giữa hai tham số đó.

Được rồi, để chuyển sang tỷ, chúng ta chỉ cần chia cho 10 lũy thừa chín. Vì thế điều đó mang lại cho tôi

tham số tỷ. Được rồi, bây giờ chúng ta nhận được kết quả đáng ngạc nhiên này, không có gì đáng ngạc nhiên cho lắm

kết quả là có vẻ như chỉ có 3,7 tỷ tham số trong mô hình này. Bây giờ trên một

tay, 3,75 tỷ vẫn còn rất nhiều thông số cần đào tạo. Mặt khác, mô hình được quảng cáo là

là bảy tỷ thông số. Vậy thỏa thuận ở đây là gì? Sao hình như chỉ có một nửa

có bao nhiêu thông số cần có? Hơn nữa, khi chúng tôi đếm các tham số có thể huấn luyện được, ở đây chúng tôi tìm thấy

rằng chỉ có ít hơn 10% tham số thực sự có thể huấn luyện được và hầu hết tất cả các tham số,

hơn 90% tham số trong mô hình này không thể huấn luyện được. Một lần nữa, điều đó có vẻ thực sự kỳ lạ. Vì vậy

có gì đó thực sự kỳ lạ ở đây phải không? Vì vậy tôi hy vọng bạn có cảm giác bối rối và lo lắng. Nếu bạn

đã làm được thì thật tuyệt. Điều đó có nghĩa là bạn đang tìm hiểu về các kiến ​​trúc LLM này. Được rồi, nhưng sau đó tiếp tục

mặt khác, một điều kỳ lạ xảy ra khi chúng ta cố gắng đếm thủ công tất cả các tham số này, điều này

là chúng ta nhận được một số thông số. Chúng tôi nhận được một số liệu trên thực tế rất phù hợp với những gì

công ty báo cáo rằng mô hình của họ thực sự có, là 7,24 tỷ, ít hơn một nửa

của con số này. Và làm thế nào tôi có được con số này? 7,2 tỷ. Điều đó xuất phát từ, như tôi đã nói, trong các slide,

theo nghĩa đen chỉ cần nhìn qua mô hình và viết nội dung này ra. Vì vậy, kích thước của nhúng là

32.000 x 4.096. Và sau đó chúng ta có lớp chú ý có diện tích 4.000 bình phương cộng 4.000 nhân 1.000. Và

nó đến từ ma trận K ở đây và vân vân cho tất cả những thứ đó. Và đây là dành cho MLP

lớp và ma trận của phần tách nhúng. Và sau đó tôi thực sự chỉ tổng hợp chúng. Ở đây tôi thêm sự chú ý

trong MLP và nhân số đó với 32, vì có 32 khối máy biến áp trong mô hình này. Vì vậy, một cái gì đó

kỳ lạ đang diễn ra. Hãy điều tra điều này thêm một chút. Vì vậy nếu chúng ta bắt đầu nhìn vào

mô hình này, ở đây tôi chỉ đang xem xét một trong những khối chú ý. Và hãy xem, chúng ta có thể phóng to một

thêm một chút nữa, hãy nhìn vào một trong những khối chú ý và phóng to hơn một chút. Hãy chỉ

tập trung vào ma trận Q-proge này. Vì vậy, ở đây chúng ta thấy nó phải là 4.000 x 4.000, đó là một con số lớn. Hãy

xem 4.096 bình phương là bao nhiêu. Đúng rồi, khoảng 16 triệu. Vậy chắc phải có 16 triệu

thông số ở đây Nhưng hãy để tôi đồng ý trước khi tôi làm điều này. Hãy để tôi nói torched.numl và đếm

số lượng tham số ở đây. Bây giờ, bạn có thể nói đây rõ ràng không phải là con số giống nhau

như thế. Hãy xem điều gì xảy ra khi tôi viết số này chia cho số đó. Ở đây chúng tôi nhận được một chính xác

số hai. Vậy thỏa thuận ở đây là gì? Tất cả những thông số bổ sung này ở đâu? Được rồi, chúng ta hãy đi đến

bây giờ tôi sẽ nhìn vào hình dạng của cái này. Được rồi, hãy nhớ ma trận trọng số này. Rất tiếc, thực ra là khi

Tôi muốn cho bạn thấy điều này đầu tiên. Được rồi, vậy đây sẽ là 4.000 x 4.000. Nhưng bây giờ khi chúng ta thực sự

nhìn vào nó, chúng ta thấy rằng nó là một tham số chứa và nó trông giống như một danh sách. Vì vậy chúng ta hãy nhìn vào

hình dạng hoặc mảng một chiều. Vậy ở đây chúng ta thấy rằng đây là 88 triệu một. Vậy đây chỉ là

một vector cột thực sự dài. Và thỏa thuận ở đây là gì? Chúng ta hãy nhìn vào điều này một lần nữa. Và cũng

rằng đây là những số nguyên. Đây không phải là số dấu phẩy động. Vậy điều này có liên quan đến cách dữ liệu

được lượng tử hóa. Làm thế nào các ma trận trọng số này được lượng tử hóa để có được các trọng số

được biểu diễn dưới dạng số bốn bit. Và phải đủ nhỏ gọn để kích thước cuối cùng trở nên khá nhỏ.

Vì vậy tôi sẽ nói về vấn đề này nhiều hơn một chút trong các slide. Tôi cũng muốn cho bạn thấy

yêu cầu bằng cấp, chờ đã, xin lỗi, đúng vậy, nó phụ thuộc vào trọng lượng. Vì vậy, prog.weight..

Điều đó đòi hỏi phải tốt nghiệp. Và điều đó thực sự tương đương với sai. Vì vậy, lớp này, tập hợp các trọng số này thực sự là

về mặt kỹ thuật được phân loại là một lớp không thể đào tạo được. Điều đó không có nghĩa là những thông số này chưa bao giờ

được đào tạo. Tất nhiên, họ đã được đào tạo. Nhưng hiện tại chúng được liệt kê là không thể đào tạo được vì

lượng tử hóa. Điều cuối cùng mà tôi định nói lúc đầu là về việc chia cái này,

đó là điều tương tự mà tôi đã trình bày ở đây. Để tôi xem, không yêu cầu bằng cấp. Ừ, vậy đó chỉ là

nghịch đảo của điều này. Vì vậy, tôi định giải thích rằng đây hóa ra là tỷ lệ một nửa cho

số lượng số trong ma trận này so với kích thước dự kiến. Được rồi, bây giờ thêm một chút chi tiết

về một số điều khó hiểu mà chúng tôi đã phát hiện ra trong kiến trúc mô hình.

Trước đó trong khóa học, bạn đã tìm hiểu về thuật toán chú ý và cách tính ba ma trận trọng số

đều là hình vuông. Vậy wq, wk và wv. Bây giờ hóa ra chúng vuông không phải do sự cần thiết về mặt toán học,

nhưng theo quy ước. Chúng không cần phải vuông vắn. Nhóm đã tạo ra mô hình Zeffer,

mistral.ai, sử dụng một cách khác để tổ chức các ma trận chú ý,

dựa trên ý tưởng được phát triển tại Google Research. Vì vậy, ở đây bạn có thể xem tài liệu tham khảo

cho tờ giấy đó. Kỹ thuật này được gọi là chú ý truy vấn nhóm hoặc gqa. Vì vậy, ý tưởng là trong một

cơ chế chú ý nhiều đầu điển hình, có nhiều phần truy vấn, khóa và giá trị

tất cả đều xử lý các mã thông báo độc lập với nhau. Và sau đó thông tin của họ được kết hợp

bằng ma trận trộn tuyến tính w0. Tuy nhiên, các ma trận khóa và giá trị cũng có thể

để chia sẻ nhiều vectơ truy vấn. Vì vậy, nó trông giống như thế này. Vậy bây giờ bạn có bốn nhóm

thay vì tám cái đầu. Và đây là một kỹ thuật có ít tham số hơn. Và nó trở nên xinh đẹp

hiệu suất có thể so sánh được. Bây giờ tôi sẽ không thảo luận chi tiết hơn về phương pháp này.

Bạn có thể đọc thêm về các chi tiết ở đây trong bài viết này hoặc trong các bài viết khác nếu bạn quan tâm đến

các chi tiết kỹ thuật. Chà, đó là rất nhiều thông tin cần tiêu hóa cho một bài tập. Có hai

nhiều bài tập hơn trong thử thách viết mã này, nhưng tôi khuyên bạn nên tạm dừng ở đây, nghỉ ngơi một lát,

giãn cơ, uống chút nước, tiêu hóa tất cả thông tin đó. Và khi bạn cảm thấy sảng khoái,

quay lại để hoàn thành thử thách mã này.