# 43 - Cú pháp Keras Chuẩn bị dữ liệu

---

Chào mừng mọi người quay trở lại, trong bài giảng này, chúng ta sẽ bắt đầu tìm hiểu về những điều cơ bản về Cú pháp

cho API Keris, cho Tenzer Flow.

Hãy đi tới một cuốn sổ tay và bắt đầu.

Được rồi, tôi đang ở sổ ghi chép đây.

Tôi sẽ bắt đầu với một vài hàng nhập khẩu.

Chúng tôi sẽ nhập khẩu Pantazis P.D. Chúng tôi cũng sẽ nhập khoản không phải trả tiền dưới dạng ENPI.

Và vì chúng ta sẽ thực hiện một chút hình dung nên tôi sẽ nhập Seabourne dưới dạng S.A.S.

bây giờ thực sự tập trung vào cú pháp của Charise cho bài giảng cụ thể này.

Chúng ta sẽ sử dụng một tập dữ liệu giả rất đơn giản và trong bài giảng tiếp theo sẽ sử dụng

một tập dữ liệu thực tế.

Và chúng tôi sẽ tập trung nhiều hơn vào kỹ thuật tính năng.

Hãy tiếp tục và đọc trong tập tin này.

Chúng tôi sẽ sử dụng PDF đọc CSFI.

Và bên dưới thư mục dữ liệu của chúng tôi, có một tệp có tên Fake Underscore dành cho hồi quy

CSV.

Và sau đó chúng ta sẽ kiểm tra phần đầu của trạng thái khung.

Vì vậy, khung dữ liệu này rất đơn giản.

Nó chỉ đơn giản là có một mức giá và sau đó là hai tính năng tương ứng.

Vì vậy, chúng ta sẽ coi đây là một vấn đề hồi quy trong đó dựa trên tính năng một và tính năng hai sẽ

cố gắng dự đoán giá

Vì vậy, chúng ta có thể tưởng tượng rằng có thể đây là số đo của một số loại đá quý hiếm mà loại đá quý đó có đặc điểm

một và tính năng hai và chúng tôi đang cố gắng dự đoán giá.

Vì vậy, ở đây chúng ta có thông tin lịch sử, có nghĩa đây là một bài toán học có giám sát.

Mục tiêu chính của chúng tôi là xây dựng một mô hình mà khi chọn một viên đá quý mới từ mặt đất, chúng tôi có thể đo được

các tính năng của nó, tính năng một và tính năng hai và dự đoán mức giá chúng ta nên bán trên thị trường

do thực tế là chúng tôi có thông tin lịch sử về giá bán dựa trên hai đặc điểm này.

Vì vậy, một tập dữ liệu rất đơn giản.

Tôi muốn nhanh chóng chỉ cho bạn cách chúng ta có thể khám phá tập dữ liệu này.

Chúng tôi sẽ nói tạo một cặp âm mưu.

Trong khung dữ liệu, hãy chạy khung dữ liệu đó và sau đó chúng tôi sẽ có thể xem các tính năng so với giá cả và bạn sẽ

Hãy chú ý rằng đặc biệt là tính năng thứ hai, nó dường như có mối tương quan rất cao với giá thực tế.

Vì vậy, đây là một dấu hiệu khác cho thấy đây là dữ liệu giả mạo.

Vì vậy, trong một tập dữ liệu thực tế mà chúng ta sẽ thực hiện trong bài giảng tiếp theo, chúng ta sẽ mất rất nhiều

thời gian khám phá dữ liệu, thực hiện những gì được gọi là phân tích dữ liệu khám phá, thực hiện nhiều hình ảnh trực quan,

cũng như có thể thực hiện một số kỹ thuật tính năng, cố gắng trích xuất các tính năng khác từ các tính năng

mà chúng ta không thể sử dụng được.

Tuy nhiên, hãy thực sự tập trung vào quy trình làm việc chính để sử dụng luồng keris và Tensor cho học sâu.

Vì vậy, bước số một là đọc dữ liệu của bạn.

Và sau khi bạn đã thực hiện xong kỹ thuật tính năng hoặc dữ liệu, khi bạn đã khám phá dữ liệu của mình, bước tiếp theo

bước này là tạo một sự phân chia đoàn tàu thử nghiệm.

Và chúng ta có thể làm điều này.

Từ Saikat học cách lựa chọn mô hình.

Có một train để phân chia chức năng, rất dễ sử dụng.

Vì vậy, điều chúng ta sắp làm là sử dụng chuỗi này để phân chia chức năng, chia dữ liệu của chúng ta thành

một tập huấn luyện và một tập kiểm tra.

Vì vậy, hãy huấn luyện trên tập huấn luyện và sau đó đánh giá hiệu suất của mô hình của chúng tôi trên tập kiểm tra.

Vì vậy, trước tiên, điều chúng tôi muốn làm là nắm bắt các tính năng mà chúng tôi sẽ sử dụng.

Vì vậy, trong trường hợp này, đó sẽ là tính năng một và tính năng hai.

Và do cách thức hoạt động của tensor flow, chúng ta thực sự phải chuyển vào mảng bàn phím số thay vì của Panda

khung dữ liệu hoặc chuỗi Pande, vì vậy tôi có thể chỉ cần thêm giá trị dấu chấm vào cuối chuỗi hoặc khung dữ liệu và

Tôi sẽ trả lại nó dưới dạng một mảng.

Vì vậy điều chúng ta sắp làm là vẽ đồ thị các đặc điểm và đặt nó là X, và theo quy ước, chúng ta

sử dụng chữ X viết hoa vì thông thường ma trận đặc trưng là hai chiều.

Vì vậy, chúng tôi chỉ ra rằng đối với vốn.

Và sau đó là nhãn mà chúng ta sẽ dự đoán lý do tại sao là cột Giá.

Và điều tương tự ở đây sẽ lấy các giá trị theo quy ước, vì giá về cơ bản là một

vectơ chiều, chúng ta có chữ Y viết thường cho điều đó.

Vì vậy, đó là lý do tại sao chúng ta có chữ X viết hoa và chữ thường, tại sao về cơ bản nó bắt nguồn từ cách bạn viết

điều này được ghi lại một cách toán học trên giấy.

Bây giờ chúng ta đã có mảng số thực tế, nếu chúng ta nhìn vào X, nó chỉ là một số của

thông tin tương tự mà chúng tôi có trong khung dữ liệu đó để làm nổi bật một cái.

Đó chỉ là những con số là gấu trúc.

Đã đến lúc chuyến tàu của chúng ta phải tách ra.

Vì vậy, cách tôi muốn làm điều này chỉ đơn giản là gọi train để chia tách.

Và sau khi bạn đã nhập nó, bạn sẽ có thể thực hiện tab shift để xem chuỗi tài liệu được mở rộng

trên đó.

Hãy tiếp tục và cuộn xuống.

Và cuối cùng ở phía dưới bạn sẽ thấy thứ gọi là ví dụ.

Và để tiết kiệm chút thời gian, tôi chỉ muốn sao chép và dán dòng này từ ví dụ

về cơ bản là chỉ cho bạn cách bạn thực sự sử dụng cái này.

Vì vậy, tôi sẽ dán nó vào và đặt tất cả trên một dòng và giải thích cơ bản những gì đang diễn ra

ở đây.

Hãy nhớ lại rằng khi chúng tôi thực hiện phân chia bài kiểm tra tàu, cả hai chúng tôi đều chia các tính năng của mình thành bài kiểm tra X đào tạo tiếp theo

khi nhãn của chúng tôi vào đào tạo Y và chúng tôi kiểm tra.

Đảm bảo bạn xem lại phần học máy của khóa học trong trường hợp bạn có bất kỳ câu hỏi nào về nội dung

bốn tham số hoặc biến này thực sự đại diện.

Sau đó, để phân tách tàu, bạn chuyển tất cả các tính năng của mình dưới dạng X, nhãn của bạn dưới dạng Y và sau đó bạn chọn

một tỷ lệ phần trăm như kích thước thử nghiệm của bạn.

Vì vậy, thông thường bạn có thể sử dụng khoảng 30 phần trăm dữ liệu của mình.

Vì vậy, nếu tôi nói 0 phẩy 3, thì sẽ có 30% tổng dữ liệu của tôi sẽ được sử dụng cho

bộ thử nghiệm.

Và bạn luôn có thể làm nhỏ hơn nếu bạn có tập dữ liệu thực sự lớn.

Và sau đó là trạng thái ngẫu nhiên.

Vì vậy đoàn tàu cần phân chia sẽ thực hiện việc phân chia này một cách ngẫu nhiên.

Vì vậy, nó sẽ lấy các hàng ngẫu nhiên và sau đó chia chúng thành bên huấn luyện và bên kiểm tra.

Nếu bạn muốn lặp lại kết quả thực tế của phép chia mỗi lần, thì bạn sẽ đặt ngẫu nhiên

chuyển sang một số cụ thể.

Bản thân con số chỉ là sự lựa chọn tùy tiện, tùy tiện.

Bạn phải đảm bảo chọn cùng một thứ mỗi lần.

Vì vậy, hãy tiếp tục và lựa chọn.

Trạng thái ngẫu nhiên bằng 42 và bằng cách đó bạn sẽ nhận được sự phân chia ngẫu nhiên giống như tôi.

Vì vậy chúng ta sẽ tiếp tục và chạy cái này.

Và bây giờ chúng ta đã chia dữ liệu ra và chúng ta thực sự có thể kiểm tra điều này bằng cách kiểm tra hình dạng của nó.

Vì vậy hãy chú ý đến chuyến tàu X.

Hình dáng đó bây giờ là bảy trăm nhân hai tính năng X thử nghiệm.

Hình dạng đó là 300 bởi hai tính năng.

Vì vậy, đây là 70 phần trăm dữ liệu của chúng tôi dưới dạng tập tàu và 30 phần trăm dưới dạng tập thử nghiệm, vì tổng kích thước của chúng tôi

dữ liệu gốc là một nghìn hàng, được chứ?

Thông thường, bây giờ, bước tiếp theo là thực sự chuẩn hóa hoặc mở rộng quy mô dữ liệu của bạn vì chúng tôi đang làm việc với

trọng số và độ lệch bên trong mạng lưới thần kinh.

Nếu chúng tôi có các giá trị thực sự lớn trong bộ tính năng của mình, điều đó có thể gây ra lỗi về trọng số.

Và sau này chúng ta sẽ nói về độ dốc biến mất và bùng nổ.

Đó có thể là một vấn đề.

Nhưng một cách để cố gắng tránh bất kỳ sự cố nào khi đào tạo mạng của bạn là bình thường hóa và mở rộng quy mô tính năng của bạn

dữ liệu.

Vì vậy, tôi có thể học được rằng thực sự cho phép chúng tôi thực hiện điều này khá đơn giản bằng cách nói từ Escalon rằng quá trình tiền xử lý

import và thực tế có rất nhiều cách khác nhau để bạn có thể chuẩn hóa hoặc mở rộng quy mô dữ liệu của mình.

Một cách đơn giản là sử dụng cái được gọi là chia tỷ lệ tối đa tối thiểu.

Vì vậy, chúng tôi sẽ tiếp tục và nhập vô hướng tối thiểu tối đa.

Và nếu bạn gọi trợ giúp theo số vô hướng tối thiểu tối thiểu, nó sẽ thực sự mô tả những gì nó đang làm.

Vì vậy, về cơ bản, nó cũng sẽ chuyển đổi dữ liệu của bạn dựa trên độ lệch chuẩn của dữ liệu của bạn

như những người đàn ông và các giá trị tối đa.

Vì vậy, chúng ta có thể thấy ở đây công thức thực tế mà nó đang áp dụng cho chúng ta.

Vì vậy, điều chúng tôi sắp làm là chỉ cho bạn cách bạn có thể mở rộng quy mô dữ liệu, điều rất điển hình trong quy trình làm việc của bạn,

để xử lý mạng lưới thần kinh.

Bây giờ, bạn thực sự không cần phải mở rộng nhãn.

Và nếu bạn xem sổ ghi chép A của chúng tôi, chúng tôi có một liên kết giải thích lý do tại sao chúng tôi không cần mở rộng quy mô

nhãn.

Chúng tôi thực sự chỉ cần mở rộng quy mô các tính năng vì về cơ bản đó là những gì được truyền qua

mạng thực tế.

Nhãn cuối cùng chỉ là sự so sánh được thực hiện ở cuối.

Vì vậy, để sử dụng đại lượng vô hướng với Saikat learn, điều đầu tiên chúng tôi làm là tạo một phiên bản của nó rồi chọn

một số tên biến, thường là vô hướng, sau đó chúng tôi tạo một thể hiện của vô hướng tối đa tối thiểu mở đóng

dấu ngoặc đơn.

Bây giờ tôi có ví dụ về đại lượng vô hướng này và điều tôi sắp làm là tôi cần phải khớp với đại lượng vô hướng này

vào dữ liệu đào tạo của tôi.

Vì vậy tôi sẽ nói phù hợp trên chuyến tàu X.

Và những gì nó làm chỉ đơn giản là tính toán các tham số cần thiết để thực hiện việc chia tỷ lệ thực tế sau này

trên.

Vì vậy, nếu chúng ta nhớ lại từ việc gợi ý trợ giúp về đại lượng vô hướng tối thiểu tối thiểu, thì đại lượng vô hướng tối thiểu tối thiểu phụ thuộc vào tiêu chuẩn

độ lệch, giá trị tối thiểu và giá trị tối đa trong tập dữ liệu cụ thể đó.

Vì vậy, những gì nó làm về cơ bản là tính toán độ lệch chuẩn, nam giới và Max.

Vì vậy, đó là những gì nó làm.

Vì vậy, bạn chạy fit trên tập huấn luyện của chúng tôi và lý do chúng tôi chỉ chạy nó trên tập huấn luyện là vì chúng tôi

muốn ngăn chặn hiện tượng rò rỉ dữ liệu khỏi tập thử nghiệm.

Chúng tôi không muốn cho rằng chúng tôi có thông tin trước về bộ thử nghiệm.

Vì vậy, chúng tôi chỉ điều chỉnh đại số vô hướng của mình cho tập huấn luyện để không cố gắng gian lận và nhìn vào tập kiểm tra.

Vậy thì chúng ta cần phải làm gì.

Biến đổi if.

Dữ liệu huấn luyện của chúng tôi, vì vậy chúng tôi sẽ nói rằng đoàn tàu X bây giờ bằng với đại lượng vô hướng biến đổi trên đoàn tàu X mà thực tế

thực hiện một phép chuyển đổi.

Vì vậy, về cơ bản chúng ta thực hiện hai bước ở đây, đó là tính toán những gì cần thiết cho phép chuyển đổi

xảy ra và sau đó chúng tôi thực sự thực hiện phép biến đổi và chúng tôi cũng sẽ làm như vậy.

Đối với bộ thử nghiệm.

Vì vậy chúng ta sẽ nói vô hướng.

Chuyển đổi trong thử nghiệm và bây giờ nếu chúng ta xem xét các giá trị này cho extranet, bạn sẽ nhận thấy chúng có

đã được thu nhỏ.

Vì vậy, nếu chúng ta xem xét giá trị tối đa trên tàu X là bao nhiêu thì bây giờ nó là một.

Và sau đó.

Giá trị tối thiểu bây giờ là 0, vì vậy mọi thứ đã được điều chỉnh tỷ lệ từ 0 đến 1.

Và một lần nữa, chúng tôi chỉ điều chỉnh tập huấn luyện để không xác định thông tin từ TSA vì

đó thực chất là gian lận.

ĐƯỢC RỒI.

Vì vậy, bây giờ chúng ta đã mở rộng quy mô dữ liệu, đã đến lúc chỉ cho bạn cách tạo mạng lưới thần kinh của mình,

vì vậy trong phần hai của bài giảng này chúng ta sẽ bắt đầu tạo mạng lưới thần kinh.

Tôi sẽ gặp bạn ở đó.