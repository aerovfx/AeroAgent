# 49 - Đánh giá và dự đoán mô hình hồi quy Keras

---

Chào mừng mọi người quay trở lại với Phần ba của dự án mã hồi quy Keris của chúng tôi.

Vì vậy, trong bài giảng trước, chúng ta đã kết thúc việc đào tạo mô hình của mình và làm cho phù hợp với tập huấn luyện đó.

Bây giờ là lúc khám phá đánh giá không chỉ về dữ liệu thử nghiệm của chúng tôi mà còn về khả năng dự đoán

giá của một ngôi nhà mới, dựa trên các tính năng của nó.

Hãy bắt đầu.

Được rồi, chúng ta đang ở trong cuốn sổ mà chúng ta đã dừng lại lần trước.

Chúng tôi vừa hoàn thành khóa đào tạo cho 400 kỷ nguyên đó.

Điều tôi sắp làm bây giờ là khám phá lịch sử mô hình của tôi bây giờ trông như thế nào.

Vì vậy, hãy nhớ lại, chúng ta có thể biết được lịch sử của những mất mát đó bằng cách nói mô hình, lịch sử đó, lịch sử đó và

nó trả về từ điển này.

Tuy nhiên, vì chúng ta đã vượt qua nên dữ liệu xác thực sẽ được nhập vào.

Những gì tôi có thể làm bây giờ là muốn chuyển đổi cái này.

Đối với khung dữ liệu, tôi không chỉ bị mất trên tập huấn luyện mà còn nhận được biến khác có tên là

Vall gạch dưới sự mất mát và đây là sự mất mát của tôi trong bài kiểm tra đó với dữ liệu xác thực đó.

Và bây giờ tôi có thể so sánh trực tiếp mức giảm trong quá trình đào tạo với mức giảm trong bài kiểm tra hoặc xác nhận để

xem liệu tôi có trang bị quá mức cho dữ liệu huấn luyện trên mô hình của mình không.

Và cách tốt nhất để làm điều đó là chỉ cần vẽ sơ đồ này.

Vì vậy, tôi sẽ nói tổn thất bằng khung dữ liệu đó và sau đó tôi có thể nói tổn thất theo biểu đồ dấu chấm.

Và tôi có thể so sánh trực tiếp hành vi cốt truyện của lần mất huấn luyện màu xanh lam với lần mất xác nhận màu cam của tôi.

Và đây chính xác là loại tín hiệu mà chúng tôi muốn khi có sự giảm cả về thời gian luyện tập và

sự mất xác nhận.

Và cho đến nay không có sự gia tăng nào trong bộ xác thực.

Và thực ra điều đó có nghĩa là về mặt kỹ thuật, chúng tôi có thể tiếp tục đào tạo.

Bây giờ bạn sẽ nhận thấy rằng về phần cuối, chúng tôi thực sự không cải thiện được nhiều.

Vì vậy sau 400 kỷ nguyên, có vẻ như chúng ta đang lơ lửng quanh giá trị bị mất đặc biệt này

và quá trình giảm đang diễn ra chậm hơn nhiều.

Nhưng vì tổn thất xác thực cũng đang giảm xuống, đó là dấu hiệu cho thấy chúng tôi có thể tiếp tục đào tạo

mà không cần trang bị quá mức cho dữ liệu đào tạo của chúng tôi.

Nếu bạn thấy đường màu cam này bắt đầu tăng đột biến sau một số giai đoạn này, thì nó bắt đầu đi lên và đi lên

trở lên, điều đó có nghĩa là bạn đã trang bị quá mức cho dữ liệu huấn luyện, bởi vì bây giờ bạn có tổn thất lớn hơn nhiều

trên dữ liệu xác nhận của bạn.

Và sau này trong các bài giảng, chúng ta sẽ thấy một ví dụ cho phép chúng ta thực sự triển khai

cái được gọi là dừng sớm.

Trong trường hợp này, đây gần như là hành vi hoàn hảo mà bạn muốn thấy.

Bạn muốn thấy tổn thất đào tạo, mất mát và xác nhận giảm xuống và sau đó tiếp tục giảm cùng nhau.

Vì vậy, không có hiện tượng trang bị quá mức mà chúng ta có thể thấy xảy ra ở đây.

Được rồi, bây giờ hãy thực hiện một số đánh giá về dữ liệu thử nghiệm của chúng ta.

Vì vậy, những gì chúng ta có thể làm là sử dụng nhiều phương pháp khác nhau về vấn đề này.

Bạn có thể nói từ chúng tôi, Kahlan.

Số liệu đó được nhập và chúng tôi có thể nhập những thứ như lỗi bình phương trung bình.

Sai số tuyệt đối trung bình và chúng tôi cũng có thể, ngay cả khi muốn, nhận được điểm phương sai giải thích, vậy thì sao?

điều chúng tôi làm ở đây là lấy dự đoán của mình.

Bằng cách nói mô hình mà dự đoán.

Và chúng ta sẽ dự đoán trên tập thử nghiệm.

Vì vậy, chúng tôi chạy nó và bây giờ nhớ lại, chúng tôi có danh sách dự đoán và chúng tôi sẽ làm chỉ đơn giản là so sánh

những giá trị này mà chúng tôi biết là chính xác để chúng tôi có thể gọi.

Ý tôi là, sai số bình phương hoặc sai số tuyệt đối, chúng ta có thể làm cả hai, và điều chúng ta làm là trước tiên tại sao

đúng.

Vì vậy, hãy nhớ lại lý do tại sao phải kiểm tra và sau đó chúng tôi so sánh điều đó với dự đoán của mình.

Vậy sai số bình phương tổng của chúng ta ở đây là giá trị này.

Đây là một giá trị rất lớn, điều này khá hợp lý vì chúng ta đang xử lý giá nhà.

Vậy chúng ta đang bình phương những cái đó.

Vì vậy, nó phải là một giá trị lớn.

Điều này thực sự khó giải thích.

Vì vậy, những gì chúng ta có thể làm là tính sai số bình phương trung bình gốc bằng cách lấy căn bậc hai của giá trị này

bằng cách chạy căn bậc hai NPU hoặc ENPI.

Đây là sai số căn bậc hai hoặc sai số bình phương trung bình gốc của chúng tôi hoặc chúng tôi cũng có thể nhận được sai số trung bình, tuyệt đối,

vì vậy có nghĩa là lỗi tuyệt đối.

Điều này thực sự dễ hiểu vì về cơ bản, sai số tuyệt đối trung bình của bạn trên tất cả là bao nhiêu?

dự đoán của bạn để chúng tôi có thể nói tại sao phải kiểm tra so với dự đoán?

Và có vẻ như sai số tuyệt đối trung bình của chúng tôi.

Như vậy trung bình chúng ta đang lỗ khoảng một trăm ngàn đô la.

Bây giờ, điều đó tốt hay xấu?

Một lần nữa, chúng ta phải tính đến chính khung dữ liệu thực tế.

Vì vậy, chúng tôi phải tính đến cột giá của lệnh gọi khung dữ liệu ban đầu, mô tả về cột đó và

xem chúng ta thực sự đang xử lý loại giá trị nào.

Hãy nhớ lại rằng giá trị trung bình có vẻ như là 5,4 nhân 10 mũ 5.

Vì vậy, nếu chúng ta thực sự lấy cái này và đặt nó ở đây dưới dạng một con số, nó sẽ báo cáo lại rằng giá trung bình

của ngôi nhà là khoảng năm trăm bốn mươi ngàn đô la.

Trong trường hợp của chúng tôi, sai số tuyệt đối chính của chúng tôi là khoảng một trăm nghìn đô la.

Vì vậy, điều đó không thực sự tuyệt vời.

Hoặc giảm khoảng 20 phần trăm.

Vì vậy, không tuyệt vời.

Cũng không kinh khủng lắm.

Nhưng chúng ta cũng có thể sử dụng và giải thích điểm phương sai để cố gắng hiểu sâu hơn về

số liệu đánh giá ở đây để tôi có thể sử dụng điểm phương sai giải thích.

Và nếu bạn thay đổi thời gian ở đây, về cơ bản họ sẽ giải thích điều gì đang thực sự xảy ra ở đây.

Vì vậy, số điểm tốt nhất có thể là một điểm không.

Và điều này có tác dụng gì, nó cho bạn biết mô hình thực tế của bạn giải thích được bao nhiêu phương sai.

Và bạn hãy xem tài liệu trực tuyến để biết thêm ví dụ về cách thức hoạt động thực sự của nó và

nó thực sự được tính toán như thế nào.

Nhưng những gì chúng ta có thể làm ở đây cũng giống như trước đây.

Phần trăm là giá trị của Nhà Trắng so với dự đoán của chúng tôi và chúng tôi nhận được điểm phương sai được giải thích là

đâu đó quanh số 0,8.

Vì vậy, trong trường hợp này, số không điểm bảy chín.

Vì vậy, điều đó chỉ đơn thuần là ổn.

Một lần nữa, nó thực sự phụ thuộc vào bối cảnh.

Chúng ta có mô hình trước đó thực sự hoạt động tốt hơn mô hình này không?

Chúng tôi cũng nhận thấy rằng về mặt kỹ thuật, chúng tôi vẫn có thể tiếp tục tập luyện và tiếp tục giảm tỷ lệ thua này.

Vì vậy, có lẽ việc cố gắng tiếp tục đào tạo về dữ liệu huấn luyện là điều đáng giá vì về mặt kỹ thuật chúng tôi chưa thực sự

vẫn chưa đạt đến mức trang bị quá mức do phân tích của chúng tôi ở đây.

Chà, chúng ta cũng có thể so sánh các dự đoán của mình và có thể vẽ chúng ra sao cho phù hợp hoàn hảo.

Vì vậy, hãy nhớ lại rằng trước đây những gì chúng tôi đã làm, chúng tôi đã thực hiện một biểu đồ phân tán để kiểm tra lý do tại sao.

So với những dự đoán của chúng tôi, chúng tôi có thể thấy chúng phù hợp như thế nào ở đây và điều tôi có thể làm là làm cho điều này trở nên thú vị hơn một chút.

lớn hơn.

Vì vậy, tôi có thể nói rằng kích thước của hình phạt này bằng, giả sử, 12 x 6 để phù hợp với mọi thứ

độc đáo.

Bây giờ trong một thế giới hoàn hảo, đây sẽ là một đường thẳng và chúng ta có thể so sánh bằng cách nói âm mưu PLT và tôi là

chỉ cần đi kiểm tra âm mưu y.

Chống lại bài kiểm tra tại sao?

Và tôi sẽ chỉ nói đây là ranh giới đỏ bằng cách nói, à.

Và bây giờ đường màu đỏ này đại diện cho đường dự đoán tốt nhất hoặc về cơ bản là hoàn hảo.

Bạn sẽ nhận thấy rằng về cơ bản chúng ta đang bị trừng phạt ở đây bởi những ngoại lệ này.

Vì vậy, những ngôi nhà thực sự đắt tiền này thực sự không giỏi trong việc dự đoán mức giá đó, nhưng chúng tôi khá

giỏi dự đoán giá nhà trong khoảng từ 0 đến 2 triệu đô la.

Điều này thực sự không quá tệ.

Rõ ràng ở đây có sự phù hợp tốt giữa các thử nghiệm và dự đoán của chúng tôi.

Và về cơ bản đó chính là điểm phương sai được giải thích đang cố gắng báo cáo lại cho bạn dưới dạng

một số duy nhất.

Điều đáng làm là đào tạo lại mô hình của chúng tôi về 99% số ngôi nhà ở phần dưới cùng đó.

Và vì vậy nếu chúng ta gặp phải tình huống mà giá bán có thể của chúng ta là hơn 3 triệu đô la, chúng ta sẽ

chỉ cần nói xin lỗi, chúng tôi không đủ tốt cho việc này và sẽ chỉ trang bị lại cho 99% dưới cùng đó.

Một lần nữa, nó thực sự phụ thuộc vào ngữ cảnh và những câu hỏi bạn đang cố gắng trả lời cũng như những vấn đề gì

bạn đang cố gắng giải quyết.

Được rồi, cuối cùng, hãy cho bạn thấy cách bạn sử dụng mô hình của mình để dự đoán về một ngôi nhà hoàn toàn mới.

Vì vậy, hãy xem khung dữ liệu ban đầu của chúng tôi.

Chúng ta sẽ tiếp tục và chọn ngôi nhà đầu tiên ở đây.

Vì vậy, hãy nói D.F. và điều chúng tôi sẽ làm là giảm giá căn nhà này.

Giả sử giá giảm dọc trục bằng 1 rồi chỉ cần chộp lấy căn nhà đầu tiên ở đây.

Vì vậy, đây chỉ là những đặc điểm của một ngôi nhà mới trên thị trường.

Vì vậy, giả sử một ngôi nhà mới sắp được rao bán trên thị trường và bạn muốn bán nó vào ngày 21 tháng 10.

Và bạn biết đấy, những đặc điểm khác nhau của ngôi nhà, bạn biết nó có bao nhiêu cựu chiến binh, bạn biết làm thế nào

nó có nhiều phòng tắm, vân vân, bạn biết đấy, tình trạng của nó, dù nó có ven sông hay không, vân vân.

Vì vậy, chúng tôi có tất cả những đặc điểm này cho một ngôi nhà mới sắp tung ra thị trường.

Bây giờ, bước tiếp theo là mở rộng quy mô dữ liệu của từng ngôi nhà này.

Hãy nhớ lại rằng mô hình của chúng tôi được đào tạo trên các phiên bản thu nhỏ của các tính năng, điều đó có nghĩa là chúng tôi thực sự có thể vượt qua

trong các tính năng này thô.

Và thay vào đó điều chúng ta cần làm là nói ngôi nhà đơn lẻ.

Lấy những giá trị đó, nên bây giờ nó là Nampara, nhưng hình dạng thực sự không được chú ý chỉ có một bộ

của dấu ngoặc nhọn hoặc dấu ngoặc ở đó.

Tôi cần định hình lại cái này thành âm một vào 19.

Và bây giờ bạn sẽ nhận thấy rằng về cơ bản sẽ thêm bộ dấu ngoặc bổ sung vào đó, đó là hình dạng mong đợi.

Tiêu cực về cơ bản chỉ có nghĩa là giữ các kích thước cũ đó dọc theo trục.

Vì vậy, bây giờ tôi đã có hình dạng chính xác, tôi có thể nói vô hướng.

Sự biến đổi đó.

Về điều này và bây giờ chúng tôi có các phiên bản chuyên nghiệp của mọi thứ và bây giờ chúng tôi sẽ đặt lại phiên bản này thành phiên bản duy nhất của chúng tôi

nhà, vậy bây giờ tôi có căn nhà riêng rồi, tôi sẽ nói mẫu mà dự đoán.

Trên ngôi nhà duy nhất của tôi, hãy chạy cái này và bây giờ tôi có mức giá dự đoán mà nó sẽ bán và nếu tôi mua

nhìn vào.

Fed, món hàng đầu tiên ở đó, chỉ hiển thị một cái, giá thật mà nó bán là hai trăm

21.000 đô la và tôi dự đoán nó sẽ được bán với giá 288.000 đô la.

Vì vậy, có vẻ như chúng ta đang vượt quá giới hạn ở đây.

Và một lần nữa, đó có thể là một vấn đề khi chúng ta đang cố gắng phù hợp với những giá trị cực đoan này.

Vì vậy, bước thú vị tiếp theo cần thực hiện là đào tạo lại mô hình của bạn bằng cách có thể bỏ học.

giá trị một hoặc hai phần trăm cao nhất và xem liệu điều đó có thể làm giảm sai số bình phương trung bình trên tập dữ liệu của bạn hay không.

Nhưng hiện tại, tôi có thể nói rằng chúng tôi đã hoàn thành khá nhiều việc với dự án này.

Chúng tôi có thể thực hiện một chút kỹ thuật, thực hiện một chút phân tích dữ liệu mang tính khám phá, tạo ra

và huấn luyện một mô hình rồi lấy lại một mô hình tương đối hợp lý để dự đoán giá của

những ngôi nhà.

Không phải là chúng ta đang dự đoán hai tỷ đô la cho một ngôi nhà lớn có hai trăm đô la.

Thay vào đó, chúng tôi tương đối nằm trong khoảng giá mà một ngôi nhà có thể bán được.

Và có vẻ như chúng ta ít nhiều đang giải thích khá nhiều phương sai, lên tới 80% phương sai

trong việc định giá.

OK, vậy là xong bài giảng này.

Tiếp theo, chúng ta sẽ bắt đầu tìm hiểu sâu hơn về nhiều chủ đề này dựa trên những thứ như

kích thước dơi và điểm dừng sớm trong mô hình của chúng tôi.

Và chúng ta sẽ làm điều đó bằng cách xem xét các nhiệm vụ phân loại thông qua luồng Tenzer.

Tôi sẽ gặp bạn ở bài giảng tiếp theo.