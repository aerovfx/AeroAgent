# 75 - CNN về Tệp Ảnh Thực Tạo Mô Hình

---

Chào mừng mọi người quay trở lại và bài giảng này chúng ta sẽ tập trung vào việc tạo ra mô hình thực tế cho

mạng nơ-ron tích chập trên những hình ảnh tùy chỉnh này và mô hình sẽ phù hợp với một trình tạo.

Hãy bắt đầu.

Được rồi, chúng ta đang ở trong cuốn sổ mà chúng ta đã dừng lại lần trước.

Hãy bắt đầu tạo mô hình của chúng ta, chúng ta sẽ nói từ dòng tensor, hãy quan tâm đến các mô hình chứng khoán.

Và giống như chúng ta đã làm trước đây, chúng ta sẽ nhập tuần tự.

Và sau đó chúng tôi sẽ nói từ Tenzer flow Doc Harris, tầm quan trọng của lớp đó và chúng tôi sẽ làm là chúng tôi

sẽ nhập một lớp dày đặc.

Đây là điều cuối cùng.

Ngoài ra, chúng ta có thể thêm một số lớp dày đặc sau các lớp chập của chúng ta.

Hãy tiếp tục và nhập các lỗi tích chập xảy ra với những lỗi này.

Và sau đó chúng ta cũng sẽ nhập các lớp kéo của mình.

Vì vậy, có hồ bơi tối đa.

Một điểm gây nhầm lẫn phổ biến cho sinh viên là sự khác biệt giữa nhóm tối đa và nhóm tối đa.

Chúng thực sự giống nhau.

Và bạn có thể kiểm tra điều này.

Nếu bạn vào Trung tâm Tài liệu, bạn sẽ nhận thấy rất nhiều lớp trong số này có các phần phụ được gọi là

bí danh, về cơ bản có nghĩa là có nhiều tên cho cùng một lệnh gọi hàm.

Vì vậy, chỉ cần ghi nhớ điều đó.

Đây là một vấn đề thực sự phổ biến gần giống như một vấn đề xảy ra với dòng tensor do thực tế là nó có quá nhiều phiên bản.

rằng có rất nhiều bí danh cho cùng một thứ, ngay cả trong những thứ như Keris.

Vì vậy, chúng tôi có cả Max Pool và Max kéo hai.

Chúng thực sự giống hệt nhau.

Vì vậy, chúng ta sẽ nói điệu nhảy tích chập đến mức tối đa kéo đến cuối, bởi vì nó sẽ là một

một chút của một mạng lưới lớn hơn.

Hy vọng rằng chúng ta cũng hãy thêm phần thả ra để nó có thể ngăn chặn tình trạng trang bị quá mức.

Chúng ta sẽ nói mô hình tuần tự.

Và bây giờ sẽ là lúc thêm vào các lỗi tích chập.

Vì vậy, những gì tôi sẽ làm là thiết lập một lớp chập cơ sở.

Vì vậy trước tiên chúng ta nói tích chập với và sau đó chúng ta sẽ quyết định có 32 bộ lọc ở đây.

Và tôi sẽ chọn kích thước hạt nhân nhỏ hơn, khoảng ba x ba, sau đó là hình dạng đầu vào và

điều này trở nên rất quan trọng, hình dạng đầu vào phải bằng hình dạng đầu vào mà chúng ta đã xác định trước đó.

Vì vậy, hình dạng đầu vào sẽ bằng với hình dạng hình ảnh mà chúng ta đã xác định.

Vì vậy hãy nhớ lại trước đó, chúng ta xác định hình dạng hình ảnh dựa trên kích thước trung bình của những hình ảnh này và đó là những gì

đã ở trên đây, là 1 x 30, 30 x 3.

Và đây là thứ bạn có thể chơi đùa.

Hãy nhớ rằng, nếu bạn chọn hình dạng hình ảnh quá lớn, đặc biệt nếu bạn đang xử lý các vấn đề cực kỳ khó khăn.

các tập tin lớn, bạn có thể hết bộ nhớ trên máy tính.

Một lần nữa, điều đó phụ thuộc vào phần cứng của bạn.

Được rồi, vậy một 30 x một 30.

Những điều đó không quá tệ, vì vậy chúng ta sẽ tiếp tục và giữ nguyên hình dạng hình ảnh ở đó và hãy chọn một chức năng kích hoạt.

Chúng ta sẽ nói rằng kích hoạt bằng đơn vị tuyến tính được chỉnh lưu và sau đó.

Chúng tôi sẽ thêm vào lớp kéo của mình, vì vậy Max, hãy kéo đến và chúng tôi sẽ tiếp tục và giữ mặc định

kích thước hồ bơi chỉ để chúng ta có thể nhìn thấy nó để chúng ta có thể ghi nhớ nó.

Bây giờ là hai x hai.

Vì vậy, hãy tiếp tục và thêm vào một vài lớp chập nữa.

Kích thước hình ảnh càng lớn và nhiệm vụ bạn đang xử lý càng phức tạp thì càng phức tạp

các lớp mà có lẽ bạn nên có.

Và có một liên kết dành cho bạn trong cuốn sổ.

Vì vậy, nếu bạn xem Sổ tay Học tập Sâu của chúng tôi và cuộn xuống, sẽ có một liên kết ở đây dẫn đến một

bài giải thích về các quy tắc khác nhau để chọn số lượng nơ-ron và số lượng bộ lọc và tích chập

các lớp.

Vì vậy, chắc chắn hãy kiểm tra bài viết giải thích đó.

Được rồi, một điều tôi sẽ chỉnh sửa ở đây là khi chúng ta đi sâu hơn vào mạng lưới này, tôi sẽ tạo

nhiều bộ lọc hơn.

Vì vậy, chúng ta sẽ có hai loại lớp chập bên trong, ẩn bên trong, mỗi lớp có 64 bộ lọc.

Sau đó, chúng ta sẽ làm phẳng cái này, các mô hình của chúng ta sẽ nói, hãy tiếp tục và làm phẳng cái này ra, thêm vào

lớp làm phẳng của chúng tôi và có vẻ như tôi đã quên nhập nó.

Vậy hãy để tôi cũng làm điều đó.

Vì vậy, chúng ta sẽ nói làm phẳng, nhập cái đó.

Và sau đó tôi có thể gọi sự làm phẳng ở đây, để làm phẳng nó cho lớp dày đặc của chúng ta, vì vậy chúng ta sẽ nói mô hình

và thế là có 128 nơ-ron và chúng ta sẽ nói rằng kích hoạt của chúng ta bằng đơn vị tuyến tính được chỉnh lưu.

Tôi muốn chỉ ra điều gì đó và bạn có thể thấy điều này khi khám phá các mô hình phức tạp hơn, phức tạp hơn.

Bạn có thể khám phá trực tuyến rất nhiều để xem cách người khác tấn công các bộ dữ liệu khác nhau bằng

hình ảnh khác nhau có kích cỡ khác nhau.

Bạn có thể thấy một số người thêm vào kích hoạt sau khi kết thúc.

Vì vậy, bạn có thể làm một loại bí danh khác.

Và tôi sẽ quay lại đây để cho bạn thấy nó có trong sổ ghi chép của chúng tôi.

Về cơ bản có một ví dụ về việc thực hiện việc này theo hai bước trong đó bạn thêm các vết lõm rồi thêm

hàm kích hoạt sau lớp dày đặc.

Điều đó hoàn toàn giống với những gì chúng tôi đã làm ở đây, gọi nó là bên trong hang động.

Vì vậy, tùy bạn muốn sử dụng cái nào.

Và sau đó chúng ta cũng sẽ làm ở đây là chúng ta sẽ thêm phần thả ra, chúng ta sẽ tắt.

Một nửa số nơ-ron ngẫu nhiên để ngăn chặn tình trạng trang bị quá mức sau đó, chúng ta có lớp dày đặc cuối cùng, có thể nói như vậy

đó là một rồi nói mô hình và bạn có thể thêm hàm sigmoid vào hoặc chỉ nói ở đây, kích hoạt

bằng sigmoid.

Chúng tôi cũng trình bày phương pháp thay thế ở đây, đó là thêm nó vào sau thực tế.

Một trong hai hoàn toàn ổn.

Vậy chúng ta có sigmoid kích hoạt này.

Điều cuối cùng tôi muốn cho bạn thấy là việc biên dịch mô hình sẽ nói là biên dịch mất mô hình.

Đây là một vấn đề phân loại nhị phân.

Vì vậy, nó phải là nhị phân.

Entropy chéo.

Và sau đó là trình tối ưu hóa của chúng tôi.

Chúng tôi sẽ là Adam và nếu muốn kiểm tra số liệu, chúng tôi có thể nói số liệu tương đương với độ chính xác,

chạy nó, đảm bảo chúng tôi không có lỗi.

Được rồi, có vẻ như mô hình của chúng tôi đang hoạt động.

Hãy tiếp tục và kiểm tra bản tóm tắt mô hình.

Vì vậy, hãy gọi cho ai đó trên mô hình của bạn và bạn có thể thấy các lớp khác nhau và bạn có thể thấy các tham số khác nhau

mỗi lớp.

Lưu ý rằng chúng ta có rất nhiều tham số vào thời điểm chúng ta đến lớp dày đặc, vì vậy mô hình này sẽ lấy

mất một thời gian dài để đào tạo để đảm bảo rằng chúng tôi có thể chọn đúng thời điểm để đào tạo cho những gì có thể nói từ

dòng chảy tensor.

Tiến sĩ Lệnh gọi lại iStock nhập dừng sớm rồi tạo, giống như chúng tôi đã làm trước đây khi dừng sớm

gọi lại.

Chúng tôi sẽ làm điều này dựa trên sự giám sát.

Mất xác nhận.

Và chúng ta có thể có bệnh nhân của một hoặc hai kỷ nguyên.

Đó cũng là thứ bạn có thể chơi đùa.

OK, vậy là đang tạo mô hình để huấn luyện mô hình.

Chúng ta phải chọn một kích thước lô.

Vì vậy, chúng ta sẽ tiếp tục và đào tạo về kích thước 16 hình ảnh đó cùng một lúc, vì vậy, một lần nữa, điều này khá điển hình đối với

chọn một cái gì đó trong sức mạnh của hai

Vậy hai lũy thừa của hai là bốn.

Bốn lũy thừa của hai là 16.

Và phần cứng của bạn càng lớn thì kích thước lô càng lớn.

Bạn có thể lựa chọn một cách hợp lý, kích thước lô càng nhỏ thì thời gian chạy tàu càng lâu vì

bạn đang cung cấp ít hình ảnh hơn tại một thời điểm.

Vì vậy điều chúng ta sắp làm là tạo ra hai máy phát điện, giống như chúng ta đã làm trước đây, và

máy phát điện sẽ nói tàu hỏa.

Trình tạo hình ảnh sẽ là một trong số đó, và cái còn lại chúng ta sẽ làm là hình ảnh thử nghiệm

máy phát điện, chúng sẽ rất giống nhau.

Sự khác biệt duy nhất sẽ là nguồn dữ liệu của họ.

Và chúng ta đã trải qua điều này trên luồng từ thư mục.

Rằng chúng ta cần đưa vào lộ trình đào tạo và có một vài thông số khác mà chúng ta sẽ nêu

ở đây, vì vậy chúng tôi cũng phải nêu rõ là nằm ngoài thư mục mà chúng tôi đã có là lộ trình đào tạo

kích thước mục tiêu.

Vậy quy mô mục tiêu của chúng ta là bao nhiêu?

Lưu ý kích thước mục tiêu chỉ quan tâm đến chiều rộng và chiều cao.

Vì vậy, những gì chúng tôi làm là nói rằng kích thước mục tiêu của chúng tôi bằng với hình dạng hình ảnh mà chúng tôi đã xác định trước đó.

Vì vậy, xin nhắc bạn, hình dạng của hình ảnh trước đó là 1 30 x 1, 3 x 3.

Tôi thực sự chỉ quan tâm đến hai chiều đầu tiên đó.

Vậy đó là gọi hai người để có được một 30 x một 30.

Vì vậy, đó là những gì tôi sẽ chuyển vào đây.

Tôi có thể thực hiện việc này một cách thủ công hoặc tôi có thể tắt biến đó.

Tiếp theo, tôi cần đảm bảo chế độ màu của mình là chính xác.

Vì tôi đang xử lý hình ảnh màu, chế độ màu của tôi là đỏ, lục, lam, nếu chúng ta xuống đây,

chúng ta có thể thấy các thông số khác nhau.

Vì vậy, nó sẽ có thang độ xám hoặc đỏ, lục, lam hoặc nếu vì lý do nào đó, bạn sẽ xử lý

với một kênh alpha là tốt.

Alpha là sự minh bạch.

Bạn có thể đồng ý, vậy là có chế độ màu của chúng tôi.

Một vài điều cuối cùng chúng tôi muốn đặt ở đây là kích thước lô.

Vì vậy, kích thước của kích thước lô và sau đó là chế độ lớp sẽ là nhị phân vì đó là phân loại nhị phân.

Về cơ bản tôi sẽ sao chép cái này.

Và sau đó dán nó vào trình tạo hình ảnh thử nghiệm của tôi.

Hãy tiếp tục và chạy máy phát điện đầu tiên.

Cái đó đã sẵn sàng để đi.

Điều tôi cần thay đổi ở đây là đường dẫn thử nghiệm.

Nên dành cho các hình ảnh thử nghiệm và bạn sẽ nhận thấy rằng một trong các thông số ở đây.

Việc xáo trộn này về cơ bản là xáo trộn dữ liệu của bạn trước khi nó tạo ra đợt ngẫu nhiên này

điểm dữ liệu cho bạn trong quá trình đào tạo, bạn nên xáo trộn dữ liệu của mình.

Tuy nhiên, khi bạn đang tạo bài kiểm tra, bạn thực sự không cần phải xáo trộn.

Trên thực tế, bạn không nên xáo trộn.

Nếu không, nhãn của bạn sẽ bị xáo trộn so với các điểm đặc trưng thực tế của bạn.

Vì vậy, chúng tôi muốn nói xáo trộn bằng sai khi chạy trong dữ liệu thử nghiệm.

Được rồi, đó là trình tạo hình ảnh huấn luyện trong trình tạo hình ảnh thử nghiệm của chúng tôi.

Và điều chúng ta có thể làm bây giờ là quan sát những đồ vật này.

Vì vậy, ví dụ, trình tạo hình ảnh đào tạo của chúng tôi và chúng tôi có thể nói các chỉ số lớp và báo cáo lại số 0 đó

thuộc về ký sinh trùng, một thuộc về không bị nhiễm bệnh.

Và điều chúng ta sắp làm ở đây là chúng ta có thể nói.

Mô hình kết quả của tôi hoặc các kết quả tương đương với mô hình phù hợp với trình tạo.

Chúng tôi chuyển vào trình tạo hình ảnh đào tạo của mình, chuyển một số kỷ nguyên, chúng tôi có thể chọn một kỷ nguyên lớn hơn

ở đây vì những gì chúng ta sắp làm là chuyển vào bộ xác thực của chúng ta.

Đó là trình tạo hình ảnh thử nghiệm.

Và sau đó các cuộc gọi lại sẽ tương đương với điểm dừng sớm, vì vậy bạn có thể tiếp tục và chạy nó.

Và sau đó điều đó sẽ được thực hiện trong quá trình đào tạo.

Hãy nhớ rằng, việc này sẽ mất nhiều thời gian để đào tạo.

Vì vậy, điều tôi sắp làm là tôi thực sự sẽ ngắt lời đại tá của mình và chúng tôi thực sự đã có một

tập tin cho bạn bên dưới mạng lưới thần kinh tích chập.

Chúng tôi có máy phát hiện bệnh sốt rét, tệp H5.

Hãy tiếp tục và tải nó lên để tiết kiệm thời gian nếu bạn muốn huấn luyện mô hình của riêng mình, đặc biệt là

nếu nó khác với cái mà chúng tôi đã xác định trong sổ ghi chép của mình hoặc điều bạn có thể làm là nói từ tensor

dòng chảy.

Mô hình dừng tóc, mô hình tải nhập khẩu.

Và những gì chúng ta có thể tiếp tục làm là nói rằng mô hình bằng với mô hình tải và sau đó chuyển vào máy dò sốt rét.

Tôi rất khuyến khích điều này, đặc biệt nếu bạn đang chạy nó trên một loại máy tính có phần cứng đơn giản hơn.

Hãy tiếp tục tải mô hình đó và xác nhận rằng mô hình đó đã hoạt động.

Tóm tắt mô hình tương tự.

Và bạn sẽ thấy thứ gì đó về cơ bản trông giống như thế này, mô hình mà chúng ta vừa tạo.

Ngoại trừ điều tuyệt vời là người mẫu này đã được đào tạo đầy đủ.

Điều cần lưu ý ở đây là nếu bạn quyết định tải mô hình của chúng tôi, những gì sẽ không có sẵn cho

bạn là người mẫu lịch sử đào tạo.

Vì vậy, nếu chúng ta thử lịch sử mô hình, lịch sử, nó sẽ nói rằng nó không thể tìm thấy nó bởi vì nó không thực sự

có nó.

Đó là bởi vì bạn đã tải mô hình và đây chỉ là lưu mô hình, đoàn tàu.

Nó không lưu lịch sử của mô hình đào tạo.

Hãy nhớ rằng, bạn có thể tùy ý lưu lịch sử mô hình nếu bạn thực sự muốn.

Vì vậy, nếu bạn chỉ tìm kiếm trên Google, hãy lưu lịch sử mô hình, Carus.

Về cơ bản hãy nhấn vào liên kết đầu tiên này, có mã ở đây về cách thực sự lưu cái này dưới dạng ảnh

gửi lịch sử thực tế của quá trình đào tạo nhưng lý do chúng tôi không lưu nó là vì chúng tôi thực sự hiển thị

bạn lịch sử của mô hình.

Nếu bạn đến nơi chúng tôi cung cấp một cuốn sổ tay và cuộn xuống, chúng tôi sẽ thực sự cho bạn thấy loại lịch sử

ở đây của âm mưu xác nhận mất mát.

Vì vậy, về cơ bản bạn có thể chỉ cần xem lịch sử đào tạo ở đây.

Và đây là mô hình mà chúng tôi đã lưu cho bạn.

Nếu vì lý do nào đó bạn muốn đánh giá mô hình trên dữ liệu thử nghiệm thì mô hình đó vẫn hoạt động.

Bạn có thể nói mô hình, đánh giá trình tạo và sau đó vượt qua trình tạo hình ảnh thử nghiệm, chạy nó và bạn nên

nhận được kết quả tương tự như những gì chúng ta sắp nhận được.

Hãy nhớ rằng, tùy thuộc vào việc xáo trộn thực tế của dữ liệu huấn luyện và khởi tạo ngẫu nhiên,

cái này có thể trông hơi khác so với những gì chúng ta có ở đây.

Nhưng nhìn chung, bạn sẽ nhận được thứ gì đó trong phạm vi này.

Nếu chúng tôi nói rằng các số liệu được mô hình hóa đặt tên cho độ mất mát và độ chính xác của nó thì độ chính xác của bạn sẽ nằm ở khoảng giữa

như 85 và 95 phần trăm, khá tốt vì độ chính xác cơ bản là 50

phần trăm.

Được rồi, vậy chúng ta sẽ tiếp tục và tải mô hình vì chúng ta không muốn dành toàn bộ thời gian để đào tạo lại

mô hình mà chúng tôi đã cung cấp cho bạn.

Nếu bạn quan tâm đến lịch sử thực tế của tệp HP, bạn có thể kiểm tra nó trong phần thực tế được cung cấp

cuốn sổ ở đây.

Chúng tôi thực sự hiển thị toàn bộ lịch sử của quá trình đào tạo mô hình đó.

Được rồi, vậy là có mẫu dành cho bạn rồi.

Sắp tới tiếp theo.

Về cơ bản, chúng ta sẽ nói nhiều hơn về việc đánh giá mô hình, không chỉ lịch sử mà còn cả việc dự đoán

trên hình ảnh của bạn, báo cáo phân loại, v.v.

Chúng tôi sẽ gặp bạn ở bài giảng tiếp theo.