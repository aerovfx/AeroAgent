# 3 -CodeChallenge Tỷ lệ học tập của Gulliver

---

Trong video trước, tôi đã nhấn mạnh rằng tốc độ học để tinh chỉnh phải thấp hơn

bởi vì bạn không thực sự muốn thay đổi mô hình cơ sở theo những cách thực sự quan trọng.

Bạn chỉ muốn thúc đẩy nó nhận dạng một bộ tính năng cụ thể trong văn bản.

Vì vậy, mục tiêu của thử thách viết mã này về cơ bản là lặp lại đoạn mã demo trước đó,

sử dụng ba tốc độ học tập khác nhau. Chúng tôi cũng sẽ chỉ sử dụng các biện pháp đào tạo định lượng,

và tôi nghĩ bạn sẽ thấy rằng bản thân các con số mang tính thông tin nhưng thực sự không đủ để

giúp bạn đưa ra quyết định xem đây có phải là một ứng dụng thực sự hay không. Bây giờ nếu bạn chưa xem

video trước đó hoặc đã xem qua đoạn mã đó thì bạn chắc chắn muốn làm điều đó trước khi làm việc

thông qua các bài tập ở đây. Trên thực tế, tôi không nghĩ bạn sẽ gặp nhiều khó khăn

với thử thách mã này. Tôi khuyến khích bạn sao chép và dán từ tệp mã từ phần trước

video và tôi muốn bạn dành nhiều năng lượng trí tuệ hơn ở đây để tập trung vào các khái niệm

và những thách thức trong việc tinh chỉnh thế giới thực chứ không phải chỉ tập trung vào việc làm cho mã hoạt động.

Dù sao, bài tập một liên quan đến việc nhập và mã hóa văn bản sách và tìm 100

token phổ biến nhất.

Sau đó, bạn muốn tạo hai chức năng.

Hàm đầu tiên sẽ tính tỷ lệ token được tạo có trong danh sách

100 token Gulliver's Travels phổ biến nhất.

Chức năng này gần giống hệt như mã trong video trước, nhưng hãy đảm bảo

rằng bạn có thể nhập một mô hình cụ thể vào hàm này vì chúng ta sẽ sử dụng hàm này

để thử nghiệm các mô hình khác nhau trong bài tập sau. Và hàm này sẽ xuất ra tỷ lệ phần trăm của

Các mã thông báo Gulliver's Travels phổ biến xuất hiện trong văn bản được tạo theo mô hình. Chức năng thứ hai

mà bạn nên viết là về đào tạo

và đánh giá mô hình.

Hàm này có hai đầu vào, tốc độ học,

và một tham số cho số lượng mẫu đào tạo.

Bên trong chức năng này, bạn muốn tải xuống một bản sao mới

của mô hình GPT-2, mô hình được đào tạo trước,

bởi vì chúng tôi sẽ tinh chỉnh nó nhiều lần

với tốc độ học tập khác nhau.

Sau đó, bạn muốn gọi hàm đếm mã thông báo kỳ dị này.

Đó là những gì tôi gọi là đánh giá trước chuyến tàu ở đây.

Và sau đó bạn thực hiện quy trình đào tạo điển hình của mình,

như bạn đã biết từ video trước.

Và ở phần cuối của chức năng này,

bạn muốn xuất ra mất tàu

và đánh giá trước đào tạo và đánh giá sau đào tạo.

Một lần nữa, hai biến này ở đây

hoặc đầu ra của hàm này,

mà bạn gọi trước khi bắt đầu tập luyện,

và sau đó bạn gọi lại sau khi đào tạo.

Vì vậy, bạn có thể thấy có một số mã mới để viết,

nhưng cũng có rất nhiều bản sao dán.

Vậy là xong bài tập này.

Tạm dừng video, chuyển sang mã và khi bạn sẵn sàng,

hãy quay lại video và tôi sẽ cho bạn xem mã của tôi

và có một cuộc thảo luận ngắn về một số thay đổi.

Dưới đây là những thư viện mà chúng ta sẽ cần ở đây.

Ở đây tôi đang nhập mã thông báo GPT-2.

Thực ra tôi chưa nhập mô hình này

bởi vì tôi sẽ làm điều đó sau.

Được rồi, đồng thời cũng đang thiết lập lệnh gọi GPU.

Được rồi, đây là văn bản được mã hóa

và chúng tôi nhận được 100 token thường xuyên nhất.

Bạn đã từng thấy mã đó trước đây.

Mã này ở đây về cơ bản là giống nhau

như những gì tôi đã trình bày ở video trước.

Như tôi đã đề cập, bạn muốn chắc chắn

rằng biến này ở đây xuất phát từ đầu vào.

Vì vậy, chúng tôi muốn có thể nhập vào chức năng này

một mô hình khác vì chúng tôi sẽ đào tạo

ba mô hình khác nhau với ba tốc độ học tập khác nhau.

Đó là lý do vì sao cái này sẽ có tên biến khác

như tên của mô hình.

Và đầu ra là tỷ lệ token được tạo ra

đó cũng có trong văn bản.

Được rồi, hãy chạy mã đó.

Đây là chức năng đào tạo mô hình.

Như tôi đã đề cập, cần có hai đầu vào,

tốc độ học và số lượng mẫu cần huấn luyện.

Đây là nơi tôi tải xuống bản sao mới của GPT-2.

Được rồi, điều này xảy ra lúc đầu

của chức năng đào tạo này.

Sau đó chúng tôi gọi đánh giá.

Bạn có thể thấy tôi đang nhập vào mã thông báo đáng sợ này.

Đó là chức năng ở trên này.

Mô hình này, đây đã được đào tạo trước,

nhưng nó vẫn chưa được tinh chỉnh.

Ở đây tôi tạo trình tối ưu hóa bằng cách sử dụng tốc độ học tập

sẽ được chỉ định làm đầu vào cho hàm này.

Và sau đó, vâng, chỉ cần thiết lập quá trình đào tạo, khởi tạo.

Được rồi, vậy thì đến đây để tập huấn,

thực sự không có gì mới mẻ ở đây.

Về cơ bản tất cả điều này được sao chép và dán từ mã.

Ở video trước mình đã cô đọng lại một chút,

nhưng ngoài ra thì đó chính là mã mà bạn đã thấy trước đây.

Được rồi, sau khi tinh chỉnh xong,

chú ý vết lõm ở đây.

Vì vậy, cái này được thụt vào trong vòng lặp for này

trên tất cả các mẫu huấn luyện.

Và sau đó điều này không được thụt lề,

vì vậy đây là một phần của chức năng.

Dòng này được gọi sau tất cả các tinh chỉnh

đã hoàn tất và sau đó chúng ta có đầu ra.

Vậy hãy chạy dòng mã đó,

và bây giờ chúng ta đã sẵn sàng cho bài tập tiếp theo.

Bài tập hai liên quan đến việc chạy mã mà bạn đã viết cho bài tập một.

Vì vậy, bạn có thể thấy rằng tôi đang sử dụng ba tốc độ học tập khác nhau ở đây.

10 đến trừ bốn, 10 đến trừ năm, và 10 đến trừ sáu.

Vì vậy, bạn muốn lặp lại ba tốc độ học tập khác nhau này,

gọi hàm để tinh chỉnh mô hình và đánh giá nó,

và sau đó lưu trữ kết quả cho từng mô hình này.

Bây giờ, việc chạy vòng lặp này cho 800 mẫu huấn luyện mất khoảng 10 phút.

Vì vậy, đây là một mẹo để thực hiện bài tập này.

Điều tôi khuyên bạn nên làm là đặt số lượng ví dụ huấn luyện thành một con số thực sự nhỏ,

có thể là 20, có thể là 50, để bạn có thể xem nhanh và kiểm tra lỗi.

lỗi. Khi bạn tự tin rằng mã của mình là chính xác, bạn có thể tăng số lượng mẫu lên 800.

Hoặc bạn biết mình có thể làm được nhiều hơn nếu kiên nhẫn hơn. Đừng lo lắng về hình ảnh trực quan cho

bài tập này. Điều đó đến sau. Được rồi, hãy tạm dừng video và bắt đầu làm việc, bây giờ tôi sẽ trình chiếu

giải pháp của tôi. Vậy 3 tốc độ học, 800 mẫu, và đây là vòng lặp. Được rồi, vậy tôi đây

gọi hàm này, huấn luyện mô hình,

với tốc độ học tập đặc biệt này

và số lượng mẫu đào tạo này.

Một lần nữa, tôi hy vọng bạn đặt điều này ở mức rất nhỏ,

chỉ để bạn có thể kiểm tra mã của mình một cách nhanh chóng,

và sau đó bạn có thể tăng nó.

Được rồi, và ba kết quả đầu ra là tổn thất huấn luyện,

mà tôi đặt ở đây, tôi thêm nó vào một danh sách ngày càng dài ra,

và sau đó tôi có các đánh giá trước và sau đào tạo,

và tôi đặt chúng vào một ma trận.

Được rồi, tôi sẽ chạy mã này

việc đó sẽ mất vài phút và chúng tôi sẽ quay lại.

Bây giờ là bài tập thứ ba.

Điều này khá đơn giản.

Bạn chỉ cần hình dung kết quả

mà bạn đã tạo ở bài tập trước.

Ở đây bên trái, tôi có những tổn thất khi luyện tập

cho ba tốc độ học tập khác nhau.

Điều này cuối cùng đã trở thành rất nhiều điểm đánh dấu để vẽ

Và vì vậy tôi nghĩ cốt truyện trông có vẻ xấu xí

với 800 lần ba điểm đánh dấu.

Vì vậy tôi chỉ vẽ mỗi điểm 10

chỉ để làm cho nó trông đẹp hơn một chút.

Và ở đây, chúng ta có các ô vạch

hiển thị phần trăm token Gulliver's Travels

được mô hình tạo ra từ lần bắt đầu mã thông báo ngẫu nhiên.

Bây giờ đối với ba tốc độ học tập khác nhau,

chúng tôi cũng có các đánh giá trước và sau mô hình.

Bây giờ là bài tập viết mã để tạo biểu đồ này

là một chuyện, nhưng đến thời điểm này của khóa học,

Tôi không nghĩ đó sẽ là một thử thách thực sự đối với bạn.

Vì vậy tôi muốn bạn dành chút thời gian

suy nghĩ cẩn thận và phê bình về những con số này

mà bạn đang xem ở đây.

Đây có phải là một thước đo hữu ích không?

là số tiền bị mất và phần trăm của 100 token thông thường

thực sự là cách tốt nhất để đánh giá tác động

tinh chỉnh trên các mô hình này?

Và nó có ý nghĩa gì

để một trong những mô hình này là tốt nhất?

Có lẽ bạn có thể nghĩ ra một số cách khác

để đánh giá sự thành công của khóa đào tạo này.

Được rồi, bạn nhìn thấy logo ở đây, bạn biết phải làm gì.

Tạm dừng video và bây giờ tôi sẽ chuyển sang code.

Vì vậy, vòng luyện tập cho bài tập 3 mất khoảng 9 phút.

Không tệ lắm.

Ba tốc độ học tập, khoảng ba phút cho mỗi tốc độ học tập.

Hãy xem nó trông như thế nào.

Được rồi, ở đây tôi có một vòng lặp for trên phạm vi 3, tương ứng với ba phương pháp học

tỷ giá.

Trong phần phụ đầu tiên, tôi sẽ vẽ biểu đồ tổn thất.

Như tôi đã đề cập, tôi đã bỏ qua, tôi nghĩ tôi đã nói trong video rằng tôi bỏ qua 10 cái một lần, nhưng

Bây giờ tôi đang bỏ qua mỗi bảy giờ.

Nhưng vâng, đó chỉ là vì có cách khác

rất nhiều điểm chồng chéo.

Và ở đây tôi có cốt truyện thanh

và tôi đang tạo biểu đồ thanh này một cách riêng biệt

cho từng mức độ học tập.

Vậy hãy xem nó trông như thế nào nhé.

Vì vậy, ở đây chúng ta thấy những tổn thất và tỷ lệ

số mã thông báo được tạo từ văn bản.

Vậy nếu chúng ta nhìn vào biểu đồ này ở đây, tổn thất,

Kết quả này không có gì đáng ngạc nhiên lắm.

Về cơ bản những gì chúng ta thấy là tốc độ học tập càng cao,

đây thực sự vẫn là một tỷ lệ học tập rất nhỏ,

nhưng tỷ lệ học tập tương đối cao hơn,

tổn thất càng nhỏ.

Vậy mô hình này học nhanh nhất,

nó đang học hỏi nhiều nhất, nó đang thích nghi nhiều nhất.

Và sau đó, đúng vậy, mô hình có tốc độ học tập nhỏ nhất

không thay đổi nhiều về tổn thất tàu của nó.

Bây giờ, bạn biết đấy, trong suốt quá trình học sâu,

chúng tôi được dạy rằng thời gian đào tạo ít hơn thì tốt hơn.

Vì vậy, bản năng của bạn có lẽ là

rằng đây là tốc độ học tập tốt nhất,

đây là tỷ lệ học tập tốt nhất tiếp theo,

và đây là tỷ lệ học tập tồi tệ nhất,

bởi vì hãy nhìn xem những sai số này vẫn còn cao đến mức nào,

sự mất mát đào tạo.

Mặt khác, đặc biệt là để tinh chỉnh,

đó không hẳn là một điều xấu.

Chúng tôi không nhất thiết muốn tổn thất tàu hỏa về 0.

Và lý do là nếu tổn thất tàu về 0

hoặc gần bằng không.

Điều đó có nghĩa là rất nhiều kiến thức được đào tạo trước

và nhận dạng mẫu được nhúng bên trong GPT-2,

GPT-2 được đào tạo trước, hiện đã bị xóa.

Nó đã bị ghi đè bởi các mẫu duy nhất

đến những chuyến du hành của Gulliver, tới một văn bản cụ thể đó.

Bây giờ, nếu bạn thực sự, thực sự chỉ muốn một mô hình

chỉ có thể chuyên về đúng một cuốn sách,

thì đó có lẽ là một điều tốt.

Nhưng nếu bạn muốn một mô hình có mục đích chung

có rất nhiều kiến thức về chuyến đi của Gulliver

hoặc viết theo phong cách của Jonathan Swift,

thì đây có lẽ không phải là điều tốt.

Điều này có lẽ là quá nhiều

về việc nhúng cuốn sách này vào mô hình này một cách triệt để.

Vì vậy, trong trường hợp đó, bạn có thể nghĩ rằng tốc độ học tập này

tốt hơn, nhẹ nhàng hơn, tốc độ học tập nhỏ hơn.

Được rồi, sau đó chúng ta có thể nhìn qua đây.

Chúng tôi thấy cùng một mô hình cho cả ba

của những tỷ lệ học tập này, hộp nào sẽ tăng lên.

Và điều đó có nghĩa là gì?

Điều đó có nghĩa là tỷ lệ token

mà mô hình tạo ra đã tăng lên

sau khi được tinh chỉnh trên cuốn sách.

Và tất cả đều bắt đầu gần giống như chúng ta mong đợi.

Và tất cả đều tăng, nhưng không có gì đáng ngạc nhiên,

mô hình có tốc độ học tập nhỏ hơn đã tăng lên,

nó trông giống như 60, 61%.

Và ở đây với tốc độ học tập nhỏ nhất,

nó có thể lên đến 52 phần trăm hay gì đó.

Một lần nữa, kết quả tốt nhất ở đây là gì?

Như tôi đã đề cập trong cuộc thảo luận này ở đây,

chúng tôi không nhất thiết muốn có một mô hình

điều đó đã được đào tạo rất khắt khe trong cuốn sách này

rằng cuốn sách đó đã ghi đè lên tất cả cú pháp khác

và kiến thức thế giới mà mô hình đã tích lũy được

qua rất nhiều khóa đào tạo.

Vì vậy, những con số này rất quan trọng.

Chắc chắn họ sẽ nói với bạn rằng việc đào tạo có hiệu quả,

việc tinh chỉnh đã thành công,

nhưng để thực sự có thể xác định

tỷ lệ học tập nào trong số này là tốt nhất,

chúng tôi sẽ cần một số đánh giá bổ sung,

có lẽ một số đánh giá định tính hơn

nơi chúng tôi tạo văn bản theo mô hình,

Và giả sử chúng tôi và một nhóm người khác

sẽ đọc văn bản và đánh giá tính mạch lạc của nó,

vì kiến thức, vì sự liên quan,

cho bất kỳ ứng dụng nào chúng tôi đang tìm kiếm.

Các mô hình sáng tạo rất khó đánh giá.

Nó không giống như việc đánh giá một mô hình phân loại

độ chính xác phân loại ở đâu

về cơ bản là biện pháp quan trọng nhất.

và điều đó rất dễ dàng để định lượng và giải thích.

Các mô hình sáng tạo khó đánh giá hơn nhiều

và tôi nghĩ đó là điều bạn thực sự sẽ làm

để đánh giá cao trong phần này và trong phần tiếp theo.

Điều đó nói rằng, nói chung,

tinh chỉnh liên quan đến việc sử dụng tỷ lệ học tập nhỏ hơn

và lý do là bạn không muốn

để thay đổi hoàn toàn mô hình cơ sở,

bạn chỉ muốn chỉnh sửa nó một chút

vì vậy nó có một sở thích học được

cho tập huấn luyện Fine Tune.