# 48 - Tiền xử lý dữ liệu hồi quy Keras và tạo mô hình

---

Chào mừng mọi người quay trở lại với phần hai hoặc giai đoạn thứ hai của Dự án Mã hồi quy KARIUS,

bạn đã xem qua các tính năng, sau đó là một chút về kỹ thuật tính năng và thậm chí đã bỏ qua

một số tính năng.

Bây giờ là lúc mở rộng quy mô để phân chia treinta, sau đó tạo mô hình và huấn luyện mô hình đó.

Hãy bắt đầu.

Được rồi, sau khi chúng ta hoàn thành tất cả kỹ thuật tính năng, bước tiếp theo là tách các tính năng của chúng ta khỏi

nhãn.

Và chúng ta có thể làm điều này bằng cách gán X để loại bỏ.

Giá dọc theo trục bằng 1, và điều còn lại chúng ta sẽ làm là nói tại sao lại bằng

giá cả và để đảm bảo không có vấn đề gì giữa kiểu dữ liệu của gấu trúc và số lượng, chúng tôi

cũng có thể chỉ yêu cầu các giá trị.

Vì vậy, nếu bạn nói rằng các giá trị này sẽ trả về Nampara bên dưới các khung dữ liệu thực tế của chuỗi.

Vì vậy, chúng tôi chạy chúng.

Và bây giờ chúng ta đã tách các tính năng khỏi nhãn của mình, đã đến lúc thực hiện phân tách thử nghiệm, chúng ta sẽ nói:

từ Escalon.

Việc lựa chọn mô hình nhập phần tách thử nghiệm tàu.

Chạy cái đó và theo cách tôi thích làm, để tiết kiệm cho mình một chút thời gian gõ phím, tôi chỉ cần lấy

ví dụ từ chuỗi dock rồi sao chép và dán nó vào đây.

Vì vậy, chúng ta sẽ tiếp tục và lấy nó.

Sao chép nó.

Đã dán vào, tôi khuyến khích bạn làm điều tương tự.

Và điều tôi sắp làm là tôi sẽ đặt các địa điểm thử nghiệm của mình chỉ ở mức 30%.

Và tôi cũng sẽ đặt trạng thái ngẫu nhiên của mình là một không một.

Một lần nữa, tùy tiện, không có sự lựa chọn.

Chỉ là chúng tôi nhất quán trên sổ ghi chép.

Vì vậy, hãy tiếp tục và chọn trạng thái ngẫu nhiên giống như tôi làm.

Bằng cách đó bạn có thể so sánh kết quả của mình một cách trực tiếp.

Được rồi, vậy chúng ta sẽ tiếp tục và chạy cái này.

Chúng tôi đã chia tay xong.

Bây giờ là lúc thực sự thực hiện việc chia tỷ lệ.

Hãy nhớ rằng, chúng tôi muốn thực hiện chia tỷ lệ bài đăng.

Bằng cách đó, chúng tôi chỉ phù hợp với tập huấn luyện để tránh rò rỉ dữ liệu từ tập kiểm tra.

Chúng ta sẽ làm điều này giống như chúng ta đã làm trước đây bằng cách nói tìm hiểu rằng quá trình tiền xử lý nhập vô hướng tối thiểu tối thiểu.

Về mặt kỹ thuật, bạn có thể sử dụng bất kỳ tỷ lệ nào bạn thích, nhưng vô hướng tối thiểu tối đa dễ hiểu hơn, vì vậy chúng tôi sử dụng

nó trong trường hợp này.

Giá trị vô hướng tối thiểu tối đa và sau đó chúng tôi sẽ xác định lại tập huấn luyện của mình dưới dạng phiên bản được chia tỷ lệ.

Và tôi có thể tiết kiệm một chút thời gian bằng cách vừa điều chỉnh vừa chuyển đổi tất cả tập huấn luyện của mình chỉ trong một bước,

vì vậy trước đây chúng tôi thấy sự phù hợp và biến đổi theo hai bước.

Nhưng việc chia tỷ lệ thực sự có tính năng tiện lợi là chuyển đổi và điều chỉnh chỉ trong một bước.

Vì vậy, chúng tôi sẽ tiếp tục và làm điều đó.

Và sau đó để thu hồi tập kiểm tra ở đây, chúng ta sẽ chuyển đổi.

Chúng tôi không phù hợp với tập thử nghiệm của mình vì chúng tôi không muốn thừa nhận thông tin trước đó về tập thử nghiệm của mình.

Vậy là có một tập huấn luyện và một tập kiểm tra. Bây giờ chúng đã được mở rộng quy mô, tiếp theo, chúng ta sẽ bắt đầu

việc cần làm thực sự là tạo ra mô hình.

Vì vậy, chúng tôi sẽ thực hiện những điều sau đây, chúng tôi sẽ nói từ Tensor Flow Daycare rằng các mô hình sẽ được nhập tuần tự.

Và tôi cũng sẽ nói từ luồng Tenzer rằng các lớp Carus sẽ nhập và chúng tôi sẽ nhập lớp đó.

Vì vậy, chúng ta chạy nó và tạo mô hình của mình.

Vì vậy, chúng tôi tạo ra một mô hình tuần tự, và thông thường những gì chúng tôi làm là cố gắng căn cứ vào số lượng tế bào thần kinh hoặc

đơn vị trong các lớp của chúng tôi từ kích thước của dữ liệu tính năng thực tế.

Vì vậy, chúng ta hãy xem nhanh hình dạng dữ liệu của chúng tôi.

Vì vậy, có vẻ như chúng ta có 19 tính năng sắp ra mắt và đó có lẽ là một phạm vi phù hợp để có 19 nơ-ron

trong lớp của chúng tôi.

Vì vậy, cùng một mô hình thêm.

Từ ngày 19 đến nay, chúng ta cũng sẽ nói rằng lớp kích hoạt.

Sẽ là một đơn vị linnear chỉnh lưu.

Bây giờ, hãy đảm bảo rằng chúng ta thực sự đánh vần đúng thứ tự này, điều mà chúng ta sắp làm

khám phá sau này là để xem chúng ta có thể sử dụng cách dừng sớm để cố gắng chọn đúng số

kỷ nguyên để đào tạo mà còn cố gắng chọn đúng số lớp để đào tạo.

Tuy nhiên, bây giờ tôi chỉ định sao chép và dán dòng này một vài lần để thêm vào và tạo

đây là một mạng lưới học tập sâu.

Bây giờ, điều này có thể là quá mức cần thiết và cuối cùng chúng ta có thể sẽ trang bị quá mức một chút cho dữ liệu huấn luyện, nhưng chúng ta sẽ có thể

để khám phá xem điều đó có xảy ra hay không bằng cách chuyển dữ liệu xác thực vào quá trình đào tạo.

Vì vậy, những gì tôi sẽ làm ở đây là thêm một lớp cuối cùng nữa.

Và chữ cái cuối cùng cuối cùng này, cô ấy sẽ có một nơ-ron làm đầu ra, vì đó sẽ là

trực tiếp xuất ra hoặc dự đoán giá, sau đó chúng tôi sẽ biên soạn mô hình này.

Và trước đó, trong phần lý thuyết của các bài giảng này, chúng ta đã nói về Adam Optimizer

là một trình tối ưu hóa tốt, vì vậy chúng tôi sẽ chọn nó bằng cách chuyển mã chuỗi.

Adam Anson là một bài toán hồi quy trong đó việc chọn một nhãn liên tục như Giá sẽ tiếp tục và

chọn số liệu tổn thất của chúng tôi làm sai số bình phương trung bình.

Được rồi, chúng ta tiếp tục chạy nó và bây giờ là lúc huấn luyện mô hình, chúng ta sẽ nói mô hình phù hợp.

Và thứ tôi sắp chuyển qua đây là dữ liệu huấn luyện của tôi, giống như chúng ta đã làm trước đây.

Thế là X đào tạo rồi.

Tại sao phải đào tạo và điều tiếp theo tôi sẽ làm cũng là về dữ liệu xác thực, chúng tôi nhấn shift ở đây.

Bạn sẽ nhận thấy rằng bạn có thể truyền dữ liệu để đào tạo về X và Y, đồng thời bạn cũng có thể chuyển dữ liệu sang quá trình xác thực

dữ liệu.

Và điều đó có nghĩa là sau mỗi epoc huấn luyện, dữ liệu huấn luyện sẽ chạy nhanh dữ liệu thử nghiệm

và kiểm tra sự mất mát của chúng tôi trên dữ liệu thử nghiệm.

Vì vậy, bằng cách đó, chúng tôi có thể theo dõi mức độ hoạt động tốt không chỉ trên dữ liệu đào tạo của mình mà còn trên

dữ liệu thử nghiệm của chúng tôi.

Hãy nhớ rằng, dữ liệu thử nghiệm này sẽ không thực sự ảnh hưởng đến trọng số hoặc độ lệch của mạng của chúng tôi.

Vì vậy Keris sẽ không cập nhật mô hình của bạn dựa trên dữ liệu thử nghiệm hoặc dữ liệu xác thực.

Thay vào đó, họ sẽ chỉ sử dụng dữ liệu huấn luyện khi nó đang cập nhật trọng số và độ lệch rồi tiếp tục

về cơ bản là kiểm tra xem nó hoạt động tốt như thế nào không chỉ trong việc đào tạo dữ liệu mà còn cả dữ liệu xác thực.

Và cách chúng tôi chuyển dữ liệu này vào là nói rằng dữ liệu xác thực bằng và sau đó chúng tôi chuyển các giá trị của mình vào

ở đây.

Vì vậy chúng ta sẽ nói.

kiểm tra X.

Và sau đó tại sao phải kiểm tra và chúng tôi muốn đảm bảo rằng chúng tôi thực sự xem xét các giá trị ở đây, vì vậy có điều gì đó

điều cần đảm bảo là bạn đã gọi các giá trị ở đây vì Tensas Flow có thể phàn nàn nếu bạn không chuyển vào

Mỹ vì nó không thể hoạt động tốt với chuỗi hoặc khung dữ liệu này.

Vì vậy hãy chắc chắn rằng bạn đã thực hiện các giá trị.

Và một lần nữa, điều chúng tôi đang làm ở đây là chúng tôi đang tập luyện trên chuyến tàu X Train Y.

Nhưng trong quá trình thực hiện, chúng tôi muốn kiểm tra bộ thử nghiệm của mình và điều đó sẽ cho chúng tôi một số đồ thị đẹp

về cơ bản là nhận ra liệu chúng ta có trang bị quá mức hay không.

Vì vậy, hãy thêm vào dữ liệu xác nhận.

Và cuối cùng, vì đây là tập dữ liệu lớn hơn nên chúng tôi sẽ cung cấp dữ liệu của mình theo đợt.

Và chúng ta sẽ gọi kích thước lô.

Trong số 128, việc tính kích thước lô và lũy thừa của 2 là điều rất điển hình, vì vậy 64, 128,

256, kích thước lô càng nhỏ thì thời gian đào tạo sẽ càng lâu.

Nhưng bạn càng ít có khả năng khớp quá mức với dữ liệu của mình vì bạn không vượt qua toàn bộ khóa đào tạo của mình

thiết lập cùng một lúc.

Thay vào đó, bạn đang tập trung vào những đợt nhỏ hơn này.

Và cuối cùng, hãy tiếp tục và chọn một số lượng lớn các kỷ nguyên tùy ý.

Vậy là 400, chúng ta chưa có cơ chế dừng sớm nào.

Chúng ta sẽ tìm hiểu về những điều đó sau trong khóa học.

Nhưng ngay bây giờ chúng tôi sẽ làm được bốn trăm.

Bằng cách đó, tôi có thể nhìn thấy những đường cong đẹp mắt đó và cũng có thể so sánh hiệu suất tập luyện với hiệu suất kiểm tra của mình.

Vì vậy, hãy tiếp tục và chạy cái này.

Và hy vọng nếu bạn đã làm mọi thứ một cách chính xác, bạn sẽ thấy được kết quả.

Nếu bạn nhận được một số loại mã lỗi ở đây, hãy đảm bảo bạn tham khảo sổ ghi chép của chúng tôi và bạn có thể tiếp tục

và chạy trực tiếp sổ ghi chép của chúng tôi để ngăn chặn bất kỳ lỗi đánh máy đơn giản nào.

Được rồi, hiện tại đây đang là chương trình đào tạo về tập dữ liệu của chúng ta.

Trong bài giảng tiếp theo, chúng ta sẽ tiếp tục hoàn thành phần đào tạo của anh ấy.

Vì vậy, hãy tua nhanh phần này và sau đó chúng tôi sẽ bắt đầu đánh giá trên tập dữ liệu thử nghiệm của mình cũng như

dự đoán về dữ liệu hoàn toàn mới.

Vì vậy, một lần nữa, tất cả những gì chúng ta làm trong bài giảng này là chúng ta đã mở rộng quy mô dữ liệu sau khi thực hiện phân chia bài kiểm tra tàu,

đã tạo ra mô hình của chúng tôi.

Và sau đó, điều mới mà chúng tôi thấy ở đây là bổ sung thêm dữ liệu xác thực trong quá trình lắp đặt

như việc chọn một kích thước lô.

Được rồi, cảm ơn.

Và tôi sẽ gặp bạn ở bài giảng tiếp theo.