# 73 - CNN về đọc tệp ảnh thật trong dữ liệu

---

Chào mừng trở lại, mọi người.

Về cơ bản, hãy bắt đầu bằng cách tìm hiểu cách sử dụng mạng nơ-ron tích chập trên các hình ảnh tùy chỉnh

các tệp PMG hoặc JPEG của riêng bạn trong phần một của loạt bài giảng này, chúng ta sẽ chỉ tập trung vào việc hiểu

dữ liệu của chúng tôi trông như thế nào và cách đặt đường dẫn tệp cho dữ liệu của chúng tôi.

Hãy bắt đầu.

Được rồi.

Và bài giảng trước chúng ta đã import OS để thiết lập thư mục dữ liệu.

Và khi gọi thư mục danh sách từ thư mục dữ liệu, bạn sẽ thấy rằng có một bài kiểm tra

thư mục và một thư mục xe lửa.

Vì vậy, điều chúng ta sẽ làm sau đó là chúng ta sẽ khám phá thêm điều này.

Nhưng trước tiên, tôi sẽ sao chép và dán một vài nội dung nhập từ sổ ghi chép của chúng tôi.

Đầu tiên là PD Numpties, ENPI, Sieber, A.S.A. và sau đó là dấu chấm matplotlib dưới dạng Kielty.

Bây giờ, chúng ta đã thấy tất cả những nội dung nhập đó trước đây, nhưng có một nội dung mới mà chúng ta sẽ sử dụng để

thực sự đọc trong các tệp hình ảnh thực và nó được gọi từ matplotlib.

Vì vậy, từ hình ảnh dấu chấm matplotlib, không phải đường dẫn đó.

Hãy tiếp tục và nhập khẩu.

Tôi được đọc.

Vì vậy, điều này sẽ cho phép chúng ta đọc trực tiếp các tập tin hình ảnh.

Vì vậy, chúng tôi đã biết rằng chúng tôi có một bộ kiểm tra và một bộ đào tạo bên trong này.

Hãy tiếp tục và đặt hai biến.

Chúng tôi sẽ gọi một đường dẫn thử nghiệm.

Đó là thư mục dữ liệu của tôi và sau đó tôi sẽ ghép nối.

Là một chuỗi và tôi đang sử dụng dấu gạch chéo ngược kép ở đây vì tôi đang ở trên windows.

Và tôi sẽ thêm vào thư mục kiểm tra đó, sau đó tôi sẽ tạo một lộ trình đào tạo và nêu rõ rằng dữ liệu của tôi

thư mục cộng và trong trường hợp này, một lần nữa, dấu gạch chéo ngược kép ở đây trên chuyến tàu thử nghiệm.

Và rất tiếc, nó sẽ là dữ liệu.

Thư mục, không phải thư mục dữ liệu của tôi.

Được rồi, hoàn hảo.

Vì vậy, nếu chúng ta xem xét Test PAF thì.

Và chạy shift enter, về cơ bản đây là đường dẫn cuối cùng đến tập kiểm tra.

Vì vậy, hãy tiếp tục và liệt kê những tập tin bên trong bằng cách nói, OK, dừng danh mục thư mục và chúng ta sẽ tiếp tục

và vượt qua con đường thử nghiệm của chúng tôi.

Chạy nó và bạn sẽ nhận thấy có ký sinh trùng và không bị nhiễm bệnh.

Và về cơ bản những gì chúng ta đang xem ở đây là một tập dữ liệu chứa hai thư mục.

Ban đầu, nó chứa một thư mục bị nhiễm và một thư mục không bị nhiễm.

Cái này đã được chia nhỏ và kiểm tra cho bạn và nó chứa tổng cộng khoảng hai mươi bảy nghìn

hình ảnh.

Và bộ dữ liệu này được lấy từ kho lưu trữ của chính phủ về bộ dữ liệu sốt rét.

Vì vậy, có Thư viện Y khoa Quốc gia và liên kết có trong sổ ghi chép dành cho bạn trong sổ ghi chép đó

đi cùng bài giảng này.

Nhưng bạn có thể xem toàn bộ ấn phẩm và bộ dữ liệu tại đây.

Họ có hình ảnh của một tế bào.

Thế thôi.

Nó có sẵn từ NIH.

Vì vậy, bạn có thể kiểm tra chi tiết đầy đủ ở đây.

Nhưng về cơ bản, đó chỉ là hình ảnh cho biết tế bào có bị nhiễm bệnh sốt rét hay không.

Vì vậy, chúng ta sẽ quay lại đây và nhận thấy rằng về cơ bản chúng ta có một thư mục con bên dưới phần kiểm tra hình ảnh

nơi tế bào đã bị nhiễm bệnh và một tế bào không bị nhiễm bệnh.

Và chúng ta có thể làm điều tương tự cho con đường đào tạo.

Và về cơ bản nó sẽ có cùng một bộ danh mục.

Vì vậy, cuối cùng chúng ta sẽ cố gắng xây dựng một mô hình chỉ dựa trên hình ảnh của một ô.

Nó có thể dự đoán liệu nó có bị nhiễm hay không bị nhiễm?

Về lý thuyết, điều này hy vọng có thể giúp các bác sĩ thực sự tiết kiệm được nhiều thời gian chỉ bằng cách chạy hình ảnh vào mô hình của chúng tôi

thay vì phải tự tay nhìn vào những hình ảnh này và xác định.

Vì vậy, những gì chúng ta sẽ làm chỉ là nhìn vào một hình ảnh duy nhất.

Vì vậy, chúng ta sẽ nói, OK, hãy lập thư mục và tiếp tục thực hiện những việc sau.

Chúng tôi sẽ nói từ con đường đào tạo của chúng tôi.

Hãy tiếp tục và nối.

Vâng, chúng ta sẽ xem xét một con có ký sinh trùng.

Vì vậy, nói cộng với điều đó.

Chạy nó và bạn sẽ thấy danh sách tất cả các tệp hình ảnh, vì vậy đây là một ô tệp PMG một sáu hai một sáu,

hai, ba và vân vân.

Vì vậy, có hàng ngàn hình ảnh ở đây.

Chúng ta hãy đi tiếp.

Và về cơ bản, chức năng này chỉ liệt kê tất cả các hình ảnh.

Chúng ta hãy lấy cái đầu tiên trong danh sách này.

Vì vậy, nếu bạn để ý ở đây, bây giờ tôi đã có tệp PJI này và điều tôi cần làm về cơ bản là cho hình ảnh đọc

chức năng.

Tập tin này thực sự ở đâu.

Vì vậy, tế bào ký sinh hoặc tế bào bị nhiễm bệnh này, tôi sẽ nói Paracel bằng và chúng ta sẽ nói train paff plus.

Ký sinh trùng ở đó cộng thêm.

Và sau đó để đảm bảo mọi thứ hoạt động sẽ thêm hai bộ dấu gạch chéo ngược.

Về cơ bản sẽ có sự xung đột giữa tất cả các tên tệp hoặc tất cả các thư mục và sau đó

thêm vào đó.

Vì vậy, nếu tôi xem xét riêng Paracel sau khi chạy chương trình này, tất cả những gì tôi muốn nói là

Paracel này về cơ bản là toàn bộ đường dẫn tệp tới một hình ảnh, có nghĩa là sau đó tôi có thể sử dụng

hình ảnh để hoạt động mà chúng tôi đã nhập.

Vì vậy, hãy tiếp tục, Imrie Paracel và nó sẽ tự động chuyển một tệp thành một mảng cho bạn.

Và nếu chúng ta kiểm tra hình dạng của cái này.

Bạn sẽ nhận thấy rằng hình ảnh cụ thể này là 148 x 1, 42 x 3, có nghĩa là

đó là một hình ảnh màu

Hãy tiếp tục và khám phá xem nó thực sự trông như thế nào.

Vì thế chúng ta sẽ nói có tội.

Và bây giờ tôi có thể nói hình ảnh hiển thị trên hình ảnh này.

Reid gọi chạy đó.

Và đây là hình dạng của tế bào khi nó bị nhiễm trùng, ký sinh trùng.

Và bạn có thể thấy có một khu vực cơ bản bị nhiễm trùng tối màu này.

Hãy tiếp tục và làm tương tự với một ô không bị nhiễm virus và xem nó trông như thế nào.

Tế bào, nói, tế bào không bị nhiễm bệnh của tôi.

Bằng và trong trường hợp này sẽ nói đường tàu cộng và chúng ta cũng cần nói dấu gạch chéo ngược không bị nhiễm mã độc

và tôi chỉ cần lấy một hình ảnh duy nhất từ ​​đây.

Vì vậy tôi sẽ sử dụng cách tiếp cận tương tự như chúng ta đã làm lần trước.

Chúng ta sẽ nói hệ điều hành.

Hãy thư mục.

Và trong lộ trình đào tạo, hãy tiếp tục và lấy từ những người không bị nhiễm để tôi chỉ có thể nói lấy từ những người không bị nhiễm

ở đây.

Đưa nó vào.

Và hãy để tôi chia nó ra để bạn có thể thấy kết quả của nó là gì, vì vậy hãy nhớ lại một kẻ bị nhiễm bệnh sẽ phải kết thúc

ở đó.

Hãy tiếp tục và chạy nó.

Nó liệt kê tất cả các tệp hình ảnh bên trong thư mục không bị nhiễm virus, trong lộ trình đào tạo của tôi.

Chỉ cần lấy một trong số họ.

Và bây giờ chúng tôi có cái tên đó ngay tại đó.

Vì vậy, hãy lấy cái đó hoặc chỉ lấy cái này rồi dán nó để bạn có thể làm điều đó hoặc chỉ lấy bảng phân công

chính nó.

Nhân tiện, vấn đề này, nó sẽ có cùng một mã, về cơ bản là cùng một chuỗi.

Và bây giờ chúng ta đã có đường dẫn file.

Đến một tế bào không bị nhiễm bệnh.

Vậy đó là đường dẫn tệp hoàn chỉnh sau ô không bị nhiễm.

Hãy tiếp tục và đọc nó phòng trường hợp tôi sẽ cứu được ô không bị nhiễm virus của mình.

Bằng với hình ảnh đọc.

Và sau đó chúng ta sẽ nói ô không bị nhiễm và bây giờ là ô không bị nhiễm, mảng đó có tên PLT Image Show ở đây,

và đây là một tế bào khỏe mạnh không bị nhiễm bệnh.

Sự khác biệt phải khá rõ ràng.

Lưu ý rằng có một dấu hiệu đen tối ở đây về sự lây nhiễm và người không bị nhiễm bệnh.

Nhìn về cơ bản, trích dẫn không trích dẫn, bình thường.

Chúng chỉ có màu hồng như thế này thôi.

Họ không có vết đen này.

Được rồi, phần lớn của việc này chỉ là hiểu đường dẫn tệp trên máy tính của bạn.

Và bạn luôn có thể hiểu được tệp, có lẽ như chúng ta đã thảo luận trong phần gấu trúc, nếu bạn gõ

TWD liệt kê vị trí hiện tại của bạn trên máy tính bên trong sổ ghi chép này.

Được rồi, hãy tiếp tục và kiểm tra xem có bao nhiêu hình ảnh. Có rất nhiều cách khác nhau để chúng ta có thể thực hiện việc này, nhưng

một cách chúng ta có thể nói OS.

Đó là danh sách thư mục lấy lộ trình đào tạo của chúng tôi.

Và sau đó hãy tiếp tục kiểm tra xem chúng ta có bao nhiêu phiên bản ký sinh trùng?

Và sau đó cũng liên tục đảm bảo kiểm tra chính tả của bạn ở đây và sau đó kiểm tra độ dài của nó để

có vẻ như bên trong thư mục đào tạo chúng ta có 12.480 ví dụ về bị nhiễm

tế bào hoặc ký sinh tế bào.

Và rồi độ dài ở đây sẽ nói, hãy cùng thư mục lại trên con đường luyện tập.

Ngoại trừ lần này, hãy nhìn vào trường hợp không bị nhiễm bệnh.

Vì vậy, chúng tôi sẽ nói không bị nhiễm, hãy kiểm tra liên kết ở đó, vì vậy số lượng là như nhau.

Vì vậy, chúng tôi có cùng số lượng hình ảnh giữa các tế bào không bị nhiễm và tế bào ký sinh trong quá trình huấn luyện của chúng tôi,

và chúng tôi có thể có cái nhìn tương tự cho đường dẫn thử nghiệm của mình.

Vậy là có 1.300 hình ảnh của các tế bào ký sinh trong bộ thử nghiệm.

Và nếu chúng ta cũng xem xét bài kiểm tra.

Có một nghìn ba trăm người không bị nhiễm, được rồi, vậy là chúng ta có cùng số lượng phiên bản cho mỗi lớp,

điều đó thật tuyệt, vì vậy chúng ta có thể tiếp tục và thực hiện những điều này ngay bây giờ và hãy tiếp tục và cuối cùng tìm ra

hình dạng trung bình của một trong những hình ảnh này.

Điều cần lưu ý ở đây là vì đây là những tệp hình ảnh thực nên không chắc tất cả chúng đều sẽ

có hình dạng giống hệt trước đây.

Chúng ta không phải lo lắng về điều đó vì chúng ta đã đọc và các tập dữ liệu như tập dữ liệu đại chúng,

Tập dữ liệu chú ý SSAFA và mọi hình ảnh đều có cùng kích thước.

Hình ảnh ngoài đời thực sẽ không như vậy.

Chúng sẽ có kích thước khác nhau.

Vì thế.

Có rất nhiều cách khác nhau để chúng ta có thể thực hiện việc này, nhưng có một cách là thiết lập hai danh sách, gọi một yêu cầu cho bốn và

cái kia cũng vậy.

Vì vậy, điều đó đề cập đến một và hai và một điều tôi sẽ làm là lệnh sau.

Tôi sẽ nói bốn hình ảnh.

Tên tập tin.

Trong và tôi sẽ xem xét, giả sử các hình ảnh thử nghiệm của chúng tôi sẽ có trong thư mục danh sách hệ điều hành.

Bên dưới bồn tắm thử, hãy quan sát những người không bị nhiễm bệnh.

Vì vậy, hãy lấy những hình ảnh không bị nhiễm virus đó rồi tiếp tục và đọc trong tệp đó dưới dạng một mảng, giả sử các hình ảnh bằng nhau

để đọc hình ảnh và trong trường hợp này sẽ nói đường dẫn kiểm tra.

Thêm vào đó.

Không bị nhiễm trùng.

Hãy chắc chắn rằng bạn đánh vần đúng.

Dấu gạch chéo ngược, dấu gạch chéo ngược, cộng với tên tệp hình ảnh thực tế.

Vì vậy, hãy nhớ lại rằng thư mục kiểm tra thiếu suy nghĩ PAF không bị nhiễm, nếu tôi xem xét những gì trả về, về cơ bản

những gì tôi thực sự đang duyệt qua, tôi đang lặp qua từng tệp này, vì vậy hãy tiếp tục và lấy

tập tin đó.

Nhưng để thực sự tạo ra hình ảnh, tôi cần chuyển tên tệp đầy đủ, OK, điều đó cho phép điều này

cell để chạy từ bất kỳ thư mục nào bất kể bạn đang ở đâu trên máy tính.

Tôi đang đọc tất cả những tập tin này, tôi đang đọc và tất cả những hình ảnh này.

Và điều tôi sắp làm là kiểm tra hình dạng của hình ảnh, nhớ lại rằng hình dạng của hình ảnh là một bộ dữ liệu,

ba chiều, kích thước của nó, một chiều cho chiều rộng và chiều cao, sau đó là kích thước màu sắc,

đó sẽ là ba cho tất cả chúng.

Có ba kênh màu cho tất cả chúng.

Vì vậy, bây giờ tôi sẽ nói rằng thứ nguyên một sẽ nối giá trị D và thứ nguyên sẽ nối D vào giá trị.

Hãy chắc chắn rằng loại bỏ nó ở đó.

Vì vậy, tất cả những gì tôi đang làm là duyệt qua từng tệp và tình cờ đường dẫn thử nghiệm không bị nhiễm virus.

Vậy đó sẽ là 1300 tập tin.

Sau đó, tôi sẽ kiểm tra hình dạng của từng cái và lưu chiều thứ nhất và chiều thứ hai của chúng.

chiều kích.

Hãy tiếp tục và chạy cái này.

Hãy nhớ rằng bạn nên kiểm tra kỹ các phần của tệp ở đây và đảm bảo mọi thứ đều chính xác.

Và sau đó, bạn sẽ có thể kiểm tra một trong những thứ này và nó có rất nhiều kích thước trong đó.

Lưu ý rằng tất cả chúng đều khác nhau.

Vì vậy, đây là những tệp hình ảnh thực, có nghĩa là chúng sẽ không có cùng kích thước.

Chúng đều có hình dạng giống nhau, bốn chiều giống nhau và về cơ bản để xem biểu đồ của cả hai.

Chúng ta có thể nói S.A.S. âm mưu chung.

Tôi cũng đã đề cập đến một chiều và chúng tôi có được thứ trông như thế này để tôi có thể thấy các chiều khác nhau

kích thước, chúng ta có một hình ảnh rất nhỏ khoảng 50 x 60 và một hình ảnh rất lớn ở đây.

Đó là khoảng hai trăm nhân hai trăm.

Được rồi, vậy tại sao điều này lại quan trọng?

Chà, mạng lưới thần kinh tích chập sẽ không thể đào tạo trên các hình ảnh có kích thước khác nhau.

Vì vậy, điều tôi cần làm là đảm bảo rằng tôi sẽ thay đổi kích thước tất cả các hình ảnh này cho giống nhau

kích thước.

Vì vậy, tôi phải chọn kích thước thực tế mà tôi nên thay đổi kích thước mọi thứ.

Và những gì bạn nên chọn về cơ bản là mức trung bình của cả hai chiều.

Và điều này cho bạn thấy sự phân bố thực tế của hình ảnh.

Và tất cả chúng đều tập trung vào khoảng 1 30 x 1 30.

Và bạn có thể xác nhận điều này bằng cách kiểm tra các giá trị trung bình trong thứ nguyên của mình.

Vì vậy, bạn có thể nói ý nghĩa của chúng một và ý nghĩa của chúng nữa.

Vì vậy, điều tôi sắp làm là tôi sẽ nói hình dạng hình ảnh cuối cùng mà tôi sẽ cung cấp trong phép tính tích chập của mình

mạng lưới thần kinh là một 30 x một, 30 x ba.

Hãy tiếp tục và chạy nó, sau đó, chúng ta sẽ thực sự chuẩn bị dữ liệu cho mô hình, tôi sẽ thay đổi kích thước

mọi thứ theo những kích thước này.

Vì vậy, nếu đó là một bức ảnh nhỏ hơn, về cơ bản tôi có thể thêm phần đệm để nó đạt được các kích thước này.

Và nếu đó là một bức ảnh lớn hơn, tôi có thể cắt hoặc thu nhỏ nó lại.

OK, phần lớn việc hiểu đường dẫn tệp của Lexa này.

Vui lòng đảm bảo xem lại các bài giảng đầu vào và đầu ra, empanadas, nếu bạn vẫn còn bối rối trong hồ sơ

các bộ phận trên máy tính của bạn.

Và một lần nữa, hãy ghi nhớ nếu bạn đăng câu hỏi về đường dẫn tệp của mình, tôi sẽ không

có quyền truy cập vào máy tính của bạn.

Vì vậy, tôi thực sự không thể biết bạn đang lưu tập tin ở đâu.

Chà, bạn có thể làm điều đó khi bạn thực sự thiết lập dòng thư mục dữ liệu này, bạn nên

có thể chạy sổ ghi chép của chúng tôi và mọi thứ sẽ hoạt động.

Điều duy nhất bạn thực sự cần chỉnh sửa là dòng đơn lẻ này ngay tại đây.

Một lần nữa, của bạn sẽ không giống của tôi vì bạn không có trên máy tính của tôi.

Được rồi.

Vì vậy, rất nhiều phần của tệp ở đây và có thể đọc được dữ liệu hình ảnh thực.

Đó là tất cả những gì chúng ta cần trình bày cho bài giảng này.

Tiếp theo, chúng tôi sẽ chỉ cho bạn cách sử dụng trình tạo dữ liệu hình ảnh để thực hiện thao tác hình ảnh

và sau đó tạo các lô từ các tệp hình ảnh thực.

Tôi sẽ gặp bạn ở đó.