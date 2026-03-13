# 11 -Thực thi truy xuất RAG được hỗ trợ bởi LangChain.en US

---

Được rồi các bạn, hãy bắt đầu nào

với phần truy xuất.

Và phần truy xuất thực sự là

khá giống nhau.

Hãy xem điều gì xảy ra?

Người dùng đưa ra một truy vấn, phải không?

Khi người dùng đưa ra một truy vấn,

bạn sử dụng mô hình nhúng để tạo

nhúng của truy vấn này.

Bạn tìm kiếm lần này, bạn tìm kiếm

một cái gì đó vào vector của bạn

cơ sở dữ liệu, bạn mang lại

những phần có liên quan, bạn đưa ra điều đó

chuyển sang mô hình trò chuyện với

truy vấn và bạn trả lời đó là

phần truy xuất của bạn.

Được rồi, điều đó rất đơn giản phải không?

Vì vậy nếu chúng ta đi sâu vào vấn đề cụ thể này

mã, hãy để tôi tạo một tập tin mới.

Bây giờ đó là biểu đồ của bạn py.

Vì vậy, về cơ bản đây là

mã truy xuất của bạn.

Hiện nay.

Bây giờ trong mã truy xuất những gì

đầu tiên chúng ta sẽ làm

trên hết, hãy xem, nó rất đơn giản.

Hãy xem mọi thứ bắt đầu như thế nào.

Được rồi, trước hết tôi cần

mô hình nhúng của tôi.

Vì vậy, một số mã sẽ được

sao chép dán, phải không?

Tôi cần mô hình nhúng của tôi.

Vì vậy, mô hình nhúng về cơ bản là thế này.

Vì vậy, tôi sẽ chỉ sao chép cụ thể này

thứ gì đó, dán nó vào đây.

Đó là mô hình nhúng.

Và tôi cũng cần nhập

mô hình nhúng bởi vì xem,

truy vấn của người dùng cần phải được

được nhúng bằng cách sử dụng cùng một mô hình.

Vì vậy, mô hình tương tự ở đây.

Ngoài ra tôi cần tải env của mình,

chỉ cần sao chép dòng cụ thể này

và gọi hàm env ở đây.

Vì thế hiện tại tôi chưa làm gì cả.

Tôi chỉ đang tạo một kết nối.

Về cơ bản nó giống như

mô hình nhúng của bạn.

Bây giờ bạn cần vector của bạn

cơ sở dữ liệu, phải không?

Bạn cần một kết nối

vào cơ sở dữ liệu vectơ.

Vì vậy, vectơ db.

Bây giờ có một điều

mà chúng tôi sắp làm.

Nếu tôi quay lại chỉ mục PY và sao chép

lần nhập db góc phần tư này

chúng ta sẽ nói từ hiện tại

bộ sưu tập bởi vì bây giờ chúng tôi không muốn

để lưu trữ một cái gì đó vào

bộ sưu tập chúng tôi đang làm từ

bộ sưu tập hiện có.

Được rồi, bộ sưu tập hiện có.

Bây giờ URL vẫn giữ nguyên, phải không?

Tôi sẽ sao chép URL

và tôi sẽ dán URL

và đó là bộ sưu tập

mà chúng tôi muốn truy vấn.

Chúng tôi muốn truy vấn bộ sưu tập này.

Vì vậy, hãy để tôi tìm kiếm và dán nó

ở đây và, và chúng tôi cũng sẽ đi

để cung cấp cho nó một mô hình nhúng.

Vì vậy tôi sẽ sao chép

và tôi sẽ đưa

đó là mô hình nhúng.

Đây là cơ sở dữ liệu vector của bạn

mô hình nhúng kết nối

Mọi thứ đã sẵn sàng.

Bây giờ chúng ta hãy hỏi.

Bây giờ hãy bắt đầu, được rồi,

lấy đầu vào của người dùng.

Vậy để lấy thông tin đầu vào của người dùng, điều gì

bạn làm vậy, về cơ bản bạn nói xin chào,

truy vấn của người dùng bằng với đầu vào.

Được rồi?

Và tôi chỉ có thể nói hỏi điều gì đó.

Được rồi, hỏi cái gì đó.

Vì vậy người dùng sẽ

cung cấp cho bạn một đầu vào.

Bây giờ bạn đã có câu hỏi.

Bạn muốn làm gì từ điều này?

Muốn thực hiện tìm kiếm tương tự.

Bạn muốn thực hiện tìm kiếm tương tự

trên cơ sở dữ liệu vector của bạn.

Vậy nên tôi chỉ có thể nói, này Mr.

Vector DB bạn có thể làm được không

một tìm kiếm tương tự cho tôi?

Truy vấn của bạn là gì?

Vâng, tôi sẽ chỉ, tôi sẽ chỉ

cung cấp cho bạn truy vấn của người dùng.

Đó là nó.

Còn bạn, những gì bạn nhận được, bạn

về cơ bản nhận được kết quả tìm kiếm.

Bây giờ những kết quả tìm kiếm này là gì.

Những kết quả tìm kiếm này về cơ bản

trả về cho bạn những phần có liên quan.

Các đoạn có liên quan từ vectơ db.

Vì vậy, điều đó có nghĩa là ngay cả khi bạn có

hàng nghìn khối trong db vector của bạn,

bạn chỉ nhận được những phần có liên quan

dựa trên những gì người dùng đang yêu cầu.

Điều đó thực sự tốt đẹp.

Bây giờ hãy xem tôi có thể làm gì.

Bạn đã có những phần có liên quan.

Bây giờ hãy để tôi tạo

một lời nhắc hệ thống.

Được rồi, vậy lời nhắc hệ thống của tôi là

sẽ rất đơn giản.

Vì vậy, lời nhắc hệ thống của tôi nói rằng

bạn là một trợ lý hữu ích.

Được rồi, hãy đọc cái này đi

bạn là một trợ lý hữu ích.

Hãy để tôi chuyển đổi gói từ.

Trợ lý AI hữu ích

câu trả lời Chính tả là

câu trả lời sai truy vấn của người dùng.

Dựa trên bối cảnh có sẵn.

Được rồi, ngữ cảnh có sẵn

lấy từ một tập tin PDF.

Lấy từ tập tin PDF.

Cùng với nội dung trang

và số trang.

Bạn chỉ nên trả lời

vì vậy tôi có một lời nhắc bằng văn bản.

Bạn chỉ nên trả lời dựa trên người dùng

trong bối cảnh sau

và điều hướng người dùng để mở

số trang phù hợp để biết thêm.

Được rồi, sau đó chúng ta cần

để cung cấp tìm kiếm có liên quan

kết quả ở đây từ đây.

Vậy điều tôi sắp làm là tôi chỉ

sẽ tạo một biến nội dung

đây, đó là điều tôi sẽ chỉ

nói này, đó là một mảng, được chứ?

Đó là một mảng

về những gì chúng ta sẽ lặp lại.

Chúng tôi sẽ lặp lại nó.

Vì vậy, hãy để tôi sao chép một số, mượn

một số mã từ đây để bạn có thể

hãy xem chúng tôi đang làm gì ở đây.

Chúng tôi chỉ nói vậy thôi, này,

Tôi đang tạo một chuỗi ngay tại đây.

Vậy điều đó có nghĩa là chúng ta đang lặp lại

trên kết quả tìm kiếm.

Bạn có thể xem kết quả

trong kết quả tìm kiếm cho mọi

kết quả tìm kiếm, những gì chúng tôi đang làm,

chúng tôi đang nói nội dung trang.

Đây là nội dung trang.

Sau đó chúng tôi sẽ đưa ra

số trang, được chứ?

Và sau đó chúng tôi sẽ đưa ra

vị trí tập tin.

Đó là nó.

Vì vậy, đây là một chuỗi.

Và bây giờ bối cảnh này có thể

được đưa ra ngay tại đây.

Vì vậy, đây là những gì chúng tôi đang làm ở đây.

Nếu bạn nhớ phần đặc biệt này.

Lời nhắc hệ thống của tôi ở đâu?

Chính xác?

Hãy xem chúng tôi đã đưa ra một hệ thống

nhanh chóng và chúng tôi chỉ

đưa ra các dữ liệu có sẵn.

Vì vậy, đây là dữ liệu có sẵn.

Bây giờ những gì chúng ta có thể làm, giống như bạn

biết cách thực hiện lệnh gọi API phải không?

Bạn đã biết cách làm

các loại lệnh gọi API này.

Chúng tôi cũng đang đi

để thực hiện cuộc gọi API.

Vậy để tôi mang theo vài thứ nhé.

Vì vậy tôi sẽ chỉ nói từ OpenAI

Nhập OpenAI.

Điều đó khá tuyệt.

Tôi sẽ tạo ra

một khách hàng OpenAI.

Vì vậy, hãy gạch dưới OpenAI

khách hàng tương đương với OpenAI.

Đó là nó.

Bây giờ hãy xem chúng ta có thể làm gì.

Tôi sẽ chỉ cuộn xuống đây.

Tôi sẽ chỉ nói OpenAI

chat.completions.create.

bạn muốn sử dụng mô hình nào?

Tôi muốn sử dụng GPT5.

Đây là mẫu mới nhất

mà chúng tôi muốn sử dụng.

Được rồi, vậy chúng ta cần

để đưa ra những thông điệp.

Bây giờ làm thế nào để đưa ra các tin nhắn?

Tất nhiên là họ đang đi

có hai tin nhắn, phải không?

Vì vậy tin nhắn đầu tiên sẽ có

một vai trò của những gì hệ thống nhắc nhở.

Vai trò là hệ thống và chúng tôi

sẽ cung cấp nội dung

là lời nhắc của hệ thống.

Vì vậy, lời nhắc hệ thống này tạo ra

có một số hướng dẫn ban đầu

và bối cảnh có liên quan.

Phải?

Vì vậy, điều này xảy ra với hệ thống

nhắc và sau đó chúng ta sẽ đi

có vai trò là người dùng.

Đây là nơi chúng ta sẽ đến

để đưa ra truy vấn ban đầu.

Truy vấn người dùng này.

Được rồi, đây là những gì

người dùng đang yêu cầu.

Điều này sẽ cho tôi một phản hồi.

Vì vậy tôi sẽ chỉ nói phản hồi

và cuối cùng khi chúng tôi nhận được phản hồi

Tôi chỉ có thể nói này, bạn biết đấy tôi

chỉ muốn có một biểu tượng bot.

Vì vậy tôi sẽ lấy một con bot

biểu tượng ở đây và tôi sẽ đi

để nói reply.choices@ah0.um

nội dung tin nhắn.

Vì vậy, đây là những gì chúng tôi nhận được như một câu trả lời.

Điều đó thật tuyệt.

Đúng vậy, đây là những gì chúng tôi đã làm.

Hãy để tôi thử chạy cái này

tập tin cụ thể đó là trò chuyện.

Được rồi, bạn có thể thấy

nó đang hoạt động.

Bây giờ hãy để tôi mở cái này

tập tin PDF một lần nữa.

Được rồi, tệp PDF này

một lần nữa cho bạn.

Ở đây chúng tôi có tệp PDF.

Bây giờ tôi sẽ hỏi nó

giả sử như đang gỡ lỗi.

Được rồi, vậy hãy nói rằng tôi muốn

để yêu cầu nó gỡ lỗi.

Và bạn có thể thấy việc gỡ lỗi đó

có phần ở trang số 23.

Bạn có thể giúp tôi hiểu được không

gỡ lỗi trong Node JS?

Đây là truy vấn người dùng của tôi và nhập.

Vì thế nó sẽ đi, bạn biết đấy, nó sẽ

tạo các phần nhúng vector, đi vào

cơ sở dữ liệu, tìm kiếm nó, đến

trở lại và sau đó thực hiện việc truy xuất.

Hãy xem.

Vì vậy chúng ta đang hỏi điều gì đó, nó

mất một chút thời gian, được thôi.

Và chúng ta hãy đợi một lát

và ở đây chúng tôi đã có câu trả lời.

Vì vậy, hãy xem những gì đã xảy ra.

Dưới đây là một cái nhìn tổng quan nhanh

dựa trên hướng dẫn.

Bạn có thể thấy nó đang cho

cho tôi một số ví dụ.

Bạn có thấy nó đang cho không

cho tôi một số ví dụ.

Những ví dụ này là

tất cả được lấy từ đây.

Và nó nói rằng bạn cũng có thể

xem trang số 23 và 24.

Bạn có thể thấy điều này?

Mở trang 23 để bắt đầu.

Vì vậy, bạn có thể thấy nếu tôi mở

trang số 23.

Vâng, nó nói, bạn biết đấy, nhận được,

gỡ lỗi nút js.

Và bạn có thể thấy vào ngày 24

cũng có một bản gỡ lỗi.

Hãy để tôi thử một lần nữa.

Được rồi, vậy hãy nói rằng tôi muốn

để đọc về các hàm mũi tên.

Vì vậy, nó ở trang số 20.

Vì vậy, nếu tôi chạy cái này cụ thể

chương trình lại, nó đang chạy.

Bạn có thể giúp tôi hiểu được không

khái niệm về chức năng mũi tên?

Và đi vào.

Vậy là chúng ta đã có câu trả lời.

Bạn có thể thấy đây là

nơi tôi hỏi, phải không?

Bạn có thể giúp tôi hiểu được không

khái niệm về hàm mũi tên?

Đây là hướng dẫn nhanh,

tất cả những thứ đó

Bạn có thể đọc cái này và trang

số 20 và 21.

Vì vậy, bạn có thể thấy điều đó trên trang

số 20 và vâng, trên trang

số 21 chúng tôi thực sự là

nhận được các chức năng mũi tên.

Và bạn có thể thấy đó là ví dụ

rằng nó đã mang lại cho tôi nó

thực sự từ cuốn sách.

Vì vậy bạn có thể thấy rằng,

trong thực tế đây là một cuốn sách rất lớn.

Bạn không thể nhập tất cả dữ liệu này vào

AI, vào bối cảnh hệ thống.

Chúng tôi chỉ đưa nó

các đoạn có liên quan.

Vậy đây là toàn bộ đường ống, phải không?

Tôi đã đưa ra sơ đồ rồi.

Lấy truy vấn của người dùng, tạo vector

nhúng, thực hiện tìm kiếm tương tự

bây giờ, cùng với các phần có liên quan.

Xin lỗi, lỗi của tôi.

Cùng với các nội dung liên quan

khối bạn gọi là một mô hình.

Và bạn làm công việc trò chuyện.

Đây là cách bạn tạo ra miếng giẻ trên,

các tập tin lớn, dữ liệu lớn và bất cứ thứ gì.

Và một điều rất quan trọng,

điều đó không cần thiết

tập tin của bạn luôn là PDF.

Nó có thể là bất kỳ loại dữ liệu nào.

Bất kỳ loại dữ liệu nào, được chứ?