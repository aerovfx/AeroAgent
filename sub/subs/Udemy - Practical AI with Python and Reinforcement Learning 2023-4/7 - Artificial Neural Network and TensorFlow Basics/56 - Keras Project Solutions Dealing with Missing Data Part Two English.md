# 56 - Giải pháp dự án Keras Xử lý dữ liệu bị thiếu Phần thứ hai Tiếng Anh

---

Chào mừng trở lại, mọi người.

Chúng ta sẽ tiếp tục nơi chúng ta đã dừng lại lần trước về quá trình tiền xử lý dữ liệu đối với dữ liệu bị thiếu.

Hãy quay lại với cuốn sổ đó.

Được rồi, chúng ta quay lại với The Notebook.

Hãy tiếp tục và tiếp tục với các nhiệm vụ.

Đầu tiên, yêu cầu chúng tôi xem lại cột tiêu đề so với cột mục đích và xem liệu đây có phải là thông tin lặp lại hay không,

đó là một gợi ý mạnh mẽ rằng nó có thể là như vậy.

Nhưng chúng ta sẽ ra ngoài và kiểm tra điều này.

Sẽ nói D.F. Mục đích.

Hãy tiếp tục và kiểm tra xem nó thực sự trông như thế nào.

Có vẻ như thông tin này về mục đích của khoản vay, cho dù đó là để đi nghỉ, hợp nhất nợ.

Và chúng ta luôn có thể kiểm tra điều này bằng cách cố ý nói thông tin tính năng, chạy nó.

Và đó sẽ là danh mục do chính người đi vay cung cấp cho yêu cầu vay vốn.

OK, vậy là chúng ta đã có thông tin đó và chúng ta cũng có thể kiểm tra tiêu đề tương tự bằng cách nói tiêu đề.

Dot đã điều hành công việc đó và anh ấy đã được nghỉ phép, hợp nhất nợ, v.v.

Bây giờ chúng ta hãy tiếp tục và kiểm tra thông tin tính năng cho tiêu đề.

Chạy nó và đây là quyền sở hữu khoản vay do người đi vay cung cấp, vì vậy về cơ bản chúng tôi có một danh mục và

một tiêu đề, do đó cột tiêu đề chỉ đơn giản là một chuỗi hoặc mô tả danh mục con về mục đích.

Vì vậy, thật hợp lý khi bỏ đi cột tiêu đề thực tế, bởi vì nếu chúng ta xem xét một số

trong số những ví dụ trên cột tiêu đề, một số trong số đó về cơ bản chỉ có thông tin giống như những gì

đã có mục đích.

Vì vậy chúng ta sẽ tiếp tục và bỏ nó đi.

Will Sadaf tương đương với sự sụt giảm.

tiêu đề.

Dọc theo trục bằng một.

Được rồi, phần tiếp theo ở đây có lẽ là phần khó nhất của dự án vì nó chứa đầy những phần còn thiếu

dữ liệu dựa trên các giá trị của cột khác trong khung dữ liệu.

Vì vậy, một lần nữa, tôi thực sự khuyên bạn nên tham khảo sổ tay Giải pháp nếu bạn gặp khó khăn ở phần này

một, đó là lý do tại sao bạn ở đây.

Nhưng chúng ta hãy tiếp tục và đi qua điều này.

Nhiệm vụ là tìm ra Morts này nhấn mạnh một đặc điểm thể hiện điều gì.

Và nếu bạn chạy thông tin về điều này, thì đó là chức năng thông tin tính năng trên dấu gạch dưới Morts

axi chạy nó và báo cáo lại.

Đây là số lượng tài khoản thế chấp mà mọi người có.

Được rồi, chúng ta hãy vào và tạo một tài khoản giá trị bằng cách nói D.F..

Các tài khoản thế chấp và nói giá trị gạch dưới được tính ở đây, vì vậy bạn chạy nó và chúng tôi sẽ nhận ra ở đây ngay

bây giờ có vẻ như phần lớn mọi người không có tài khoản thế chấp nào khác và có vẻ như đó là

gần 25 phần trăm dữ liệu của chúng tôi và sau đó nó chuyển sang một, hai, v.v.

Và một số trong số này là những loại giá trị cực trị thú vị mà ai đó ở đây trong tập dữ liệu bằng cách nào đó

34 tài khoản thế chấp, nhưng chúng tôi sẽ để chúng ở đó.

Bây giờ, điều chính chúng ta đang cố gắng tìm ra ở đây là chúng ta thực sự làm gì với cột này?

Nếu chúng ta nhìn lại xem chúng ta có bao nhiêu giá trị còn thiếu trong cột này, gần 10% tổng số

giá trị của chúng tôi còn thiếu thứ gì đó trong số tài khoản thế chấp này.

Vậy điều đó có nghĩa là chúng ta không thể bỏ bông hồng đi.

Nếu không, chúng tôi sẽ mất 10 phần trăm dữ liệu của mình.

Vì vậy, bây giờ tùy chọn khác là chúng ta có loại bỏ tính năng thực tế không?

Vâng, đó là một cuộc tranh luận.

Thực sự không có câu trả lời đúng ở đây.

Việc bỏ nó không phải là không có lý.

Nhưng bạn cũng không thiếu nhiều dữ liệu như vậy.

Bạn chỉ thiếu 10 phần trăm.

Vì vậy, chúng tôi muốn tìm hiểu xem có cách nào để chúng tôi có thể điền dữ liệu này không?

Vì vậy, đây là một trong những điều khó nhất khi xử lý dữ liệu bị thiếu là tìm ra cách hợp lý để thử

để điền vào.

Vì vậy, một cách tiếp cận là cố gắng tìm ra đặc điểm nào trong số những đặc điểm này mà chúng ta có tất cả thông tin

vì có mối tương quan cao với các tài khoản thế chấp này và xem liệu chúng tôi có thể sử dụng tài khoản đó để điền thông tin của mình không

khỏi nó.

Chúng tôi sẽ cuộn xuống và về cơ bản thực hiện theo các nhiệm vụ nhằm hướng dẫn bạn thực hiện.

Vì vậy, theo nhiều cách, chúng tôi có thể giải quyết lượng dữ liệu còn thiếu này hoặc chúng tôi sẽ làm điều đó.

Chúng ta sẽ tiếp tục và xem xét cột nào có mối tương quan cao nhất với cột tài khoản thế chấp của chúng ta.

Vì vậy, chúng tôi muốn kiểm tra mối tương quan của cột tài khoản thế chấp đối với tất cả các số liệu hiện tại của chúng tôi.

cột để thực hiện việc này, chúng tôi chỉ cần nói D.F..

Và sau đó chúng ta sẽ đi vào tương quan điểm và kiểm tra mối tương quan với cột tài khoản thế chấp.

Và tôi sẽ sắp xếp những giá trị này.

Vì vậy, tôi chạy nó và nhận được kết quả ở đây, và tất nhiên, tài khoản thế chấp hoàn toàn tương quan với

tài khoản thế chấp.

Nhưng điều thú vị là họ có cột khác rất giống nhau, tổng số tài khoản.

Và nó không phải là một mối tương quan hoàn hảo, có nghĩa là nó không trùng lặp dữ liệu, nhưng nó có tác động khá tốt

tương quan tích cực.

Vì vậy, bạn có thể thấy từ loạt bài này rằng tính năng tổng tài khoản này có tương quan với khoản thế chấp

tính năng tài khoản.

Và điều đó khá hợp lý về mặt trực giác rằng tổng số tài khoản sẽ tương quan với số lượng

của các tài khoản thế chấp.

Vì vậy, hãy tiếp tục và thử điều này bằng cảm nhận và cách tiếp cận.

Vì vậy, việc chúng ta sắp làm là nhóm khung dữ liệu theo tổng số tài khoản và tính giá trị trung bình

giá trị của các tài khoản thế chấp trên tổng số tài khoản.

Vì vậy, nhận được kết quả trông như thế này dưới đây.

Về cơ bản những gì chúng ta đang làm ở đây là tổng tài khoản.

Chúng ta sẽ nhóm theo nó và tìm ra giá trị trung bình của tài khoản thế chấp là bao nhiêu

cột cho tổng danh mục tài khoản.

Và sau đó chúng ta sẽ sử dụng mức trung bình cụ thể này để điền vào cột tài khoản thế chấp hoặc thiếu

thông tin.

Vì vậy, bây giờ nó hơi phức tạp.

Nhưng bây giờ hãy chia nó thành các bước.

Tôi thiếu dữ liệu trong cột tài khoản thế chấp của mình và điều tôi muốn làm là tìm ra giải pháp hợp lý

cách điền nó dựa trên cột tổng tài khoản này.

Vì vậy, những gì tôi sẽ làm là lấy khung dữ liệu của tôi.

Được nhóm theo cột tổng tài khoản rồi lấy giá trị trung bình.

Đối với cột tổng tài khoản.

Hoặc khi tôi lớn lên nhờ điều này, nên tôi có thể thấy số tiền cho vay trung bình trên tổng số tài khoản,

lãi suất bình quân cho tổng số tài khoản tại đây.

Vì vậy, đây là mức trung bình trên các danh mục tổng tài khoản khác nhau.

Vì vậy, điều tôi muốn là tôi thực sự chỉ quan tâm đến việc điền thông tin tài khoản thế chấp của mình, vì vậy

Tôi sẽ lấy cái đó.

Và bây giờ tôi có thể thấy giá trị tài khoản thế chấp trung bình trên tổng số nhóm tài khoản.

Ở đây tôi có thể thấy rằng các tài khoản thế chấp trung bình, nếu bạn chỉ có tổng cộng hai tài khoản, sẽ

bằng không.

Vì vậy, điều hợp lý là nếu tôi có một hàng thiếu thông tin tài khoản thế chấp, tôi sẽ sử dụng

chuỗi này dùng để tra cứu và thay thế giá trị tài khoản thế chấp bị thiếu dựa trên tổng tài khoản

giá trị mà tôi biết không thiếu.

Và tôi điền giá trị trung bình vào đó.

Vì thế điều này không phải là không có lý.

Vì vậy, nó sẽ tiếp tục và tìm ra cách chúng ta có thể làm điều này.

Vì vậy, tôi sẽ đặt giá trị này bằng một biến mà sau đó tôi có thể tham chiếu sẽ cho biết giá trị này bằng tổng

tài khoản gạch dưới, mức trung bình gạch dưới hoặc phương tiện bằng với điều này.

Vì vậy, chúng tôi chạy nó.

Vì vậy, chúng tôi sẽ điền vào các giá trị tài khoản còn thiếu ở đây.

Thực sự có một liên kết hữu ích ở đây về cách thực hiện việc này, nhưng có một cách để thực hiện điều đó là thông qua một hàm

gọi.

Vì vậy tôi sẽ xây dựng một hàm.

Cái đó sẽ được gọi là điền vào tài khoản thế chấp, và nó chứa các giá trị, nó chứa trong tài khoản của người đó.

tổng giá trị tài khoản.

Cũng như giá trị tài khoản thế chấp của người đó.

Và điều tôi sắp làm là tôi sẽ làm như sau nếu.

Và bạn có thể sử dụng ENPI là Nan để kiểm tra xem chúng tôi có thiếu giá trị hay không, nếu tôi thiếu giá trị.

Tôi sẽ trả lại thứ gì đó mà chúng tôi sẽ giữ nguyên cam kết đó ngay bây giờ, tuy nhiên, điều đó dễ dàng hơn

là, nếu tôi không thiếu bất kỳ giá trị thế chấp nào, tôi sẽ chỉ trả lại giá trị tài khoản thế chấp hiện tại.

Vậy nếu tôi thiếu giá trị tài khoản thế chấp này thì tôi muốn làm gì?

Vì vậy, những gì tôi muốn làm ở đây về cơ bản là thực hiện một cuộc gọi tra cứu tổng số trung bình của tài khoản.

Dán cái đó vào rồi tra xem tổng số tài khoản của người đó là bao nhiêu và cái đó sẽ điền vào

phù hợp với giá trị tài khoản thế chấp trung bình này.

Được rồi, đó là những gì chức năng này sẽ làm.

Và sau đó tôi có thể đơn giản áp dụng nó để có thể nói D.F. áp dụng và tôi có thể làm điều này.

Một trong hai hàm gọi biểu thức đất.

Vì vậy, hãy làm điều đó, tiết kiệm một chút không gian gõ.

Nhưng về cơ bản, lamda này, điều chúng ta sắp làm là gọi tài khoản thế chấp của mình và đây thực sự là

trực tiếp gỡ bỏ liên kết hữu ích này.

Vì vậy, nếu bạn xem liên kết hữu ích đó, biểu thức thực tế, nếu bạn cuộn xuống, nó sẽ hiển thị ở đây

thực sự dành cho bạn theo nhiều cách khác nhau.

Nhưng đây là biểu thức chúng tôi đang sử dụng.

Chúng ta sẽ quay lại đây và điền như hình ở đó sẽ có chữ X.

Trong tổng số tài khoản.

Và sau đó là X ở đây.

Của các tài khoản thế chấp.

Và chúng ta đang làm điều này dọc theo trục bằng một.

Và chúng ta sẽ áp dụng điều đó.

Và sau đó chúng ta sẽ đặt nó bằng.

Cột tài khoản thế chấp một lần nữa có lẽ là một trong những điều khó khăn nhất mà chúng ta phải làm trong suốt bài giảng này.

loạt bài về các giải pháp.

Vì vậy, hãy để tôi phá vỡ nó một lần nữa.

Bạn có thể tiếp tục và bỏ qua nếu bạn hiểu chuyện gì đang xảy ra ở đây.

Nhưng điều chúng tôi muốn làm là tìm ra cách bù đắp những giá trị còn thiếu của khoản thế chấp này

cột tài khoản

10 phần trăm mọi người đã bỏ lỡ nó.

Vì vậy chúng ta không thể bỏ những cuộn giấy đó đi.

Và có vẻ như nó đủ quan trọng để thực sự được giữ lại như một tính năng.

Vì vậy, nếu chúng ta quyết định không bỏ cột đó và không bỏ bông hồng đó, chúng ta phải điền dữ liệu.

Vậy làm thế nào chúng ta có thể làm điều đó?

Chà, chúng tôi đã tìm ra những đặc điểm thực tế khác có mối tương quan cao với tài khoản thế chấp.

Có vẻ như tổng số tài khoản có mối tương quan khá tốt.

Vì vậy, hãy tiếp tục và sử dụng nó.

Và sau đó chúng ta sẽ làm dựa trên tổng số tài khoản.

Chúng tôi tiếp tục và nhóm theo tổng số tài khoản và tìm ra giá trị tài khoản thế chấp trung bình cho

các nhóm khác nhau của tổng tài khoản tổng danh mục tài khoản.

Và chúng ta sẽ sử dụng nó để tra cứu.

Sau đó, nếu chúng ta xem xét khung dữ liệu và nhận ra rằng chúng ta đang thiếu giá trị tài khoản thế chấp,

hãy tiếp tục và tra cứu giá trị trung bình của tài khoản thế chấp đó dựa trên tổng tài khoản của họ.

Ngược lại, nếu không thiếu thì chỉ cần trả về giá trị hiện tại.

Và điều đó sau đó được áp dụng ở đây dựa trên thông tin sau khi bổ sung cách áp dụng một chức năng

về cơ bản là chức năng của hai cột và một chốt, khung dữ liệu này.

Vì vậy, đó là những gì bài đăng tràn ngăn xếp đó đang trả lời.

Vì vậy chúng ta sẽ tiếp tục và chạy cái này.

Và tùy thuộc vào máy tính của bạn, việc này thực sự có thể mất một chút thời gian vì nó đang thực hiện các phép tính

cho mỗi hàng trong tập dữ liệu.

Nhưng một khi bạn đã làm điều đó, chúng tôi sẽ có thể xác nhận rằng nó đã được điền bằng cách nói F là

vô giá trị.

Một số chạy đó.

Và bạn nên chú ý rằng cột tài khoản thế chấp hiện ở mức 0.

Điều này khiến chúng ta chỉ còn lại hai dữ liệu còn thiếu, đó là hồ sơ công khai và công dụng của Raval về các vụ phá sản.

Tuy nhiên, đây chỉ là một tỷ lệ phần trăm nhỏ trong tập dữ liệu tổng thể của chúng tôi, nhiều nhất là năm trăm ba mươi lăm

rằng chúng ta có thể bỏ những hàng đó đi.

Chúng ta không cần phải bỏ đi những tính năng này.

Chúng ta có thể bỏ năm trăm này xuống.

Và vì vậy những người đã mất đi sự phá sản hồ sơ công cộng của họ và 270 người này, vì vậy những người đã

thiếu tính năng đặc biệt này.

Vì vậy, để làm điều đó, chúng tôi chỉ cần nói D.F. dù sao cũng bằng với sự sụt giảm.

Và bây giờ nếu bạn đang đi vòng.

Bây giờ là một số.

Bạn sẽ nhận được kết quả là không còn dữ liệu nào bị thiếu nữa, OK, vậy là xong phần còn thiếu

dữ liệu, một phần của quá trình tiền xử lý chắc chắn là một trong những phần khó nhất của dự án này.

Và đây thực chất là những gì chúng ta vừa trải qua.

Tiếp theo, chúng ta sẽ xem cách xử lý các biến phân loại và biến giả.

Được rồi, cảm ơn.

Và tôi sẽ gặp bạn ở đó.