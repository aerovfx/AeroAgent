# 01 mô hình-tối ưu hóa để triển khai

---

Bây giờ bạn đã khám phá

công việc cần thiết để thích nghi và

sắp xếp các mô hình ngôn ngữ lớn cho phù hợp với nhiệm vụ của bạn,

hãy nói về những điều bạn sẽ phải làm

xem xét để tích hợp của bạn

mô hình vào ứng dụng.

Có một số điều quan trọng

những câu hỏi cần đặt ra ở giai đoạn này.

Bộ đầu tiên liên quan đến cách bạn

LLM sẽ hoạt động trong quá trình triển khai.

Vậy bạn cần tốc độ như thế nào

mô hình để tạo ra sự hoàn thành?

Bạn có sẵn ngân sách tính toán nào?

Và bạn có sẵn sàng giao dịch không

tắt hiệu suất mô hình cho

tốc độ suy luận được cải thiện hoặc dung lượng lưu trữ thấp hơn?

Bộ câu hỏi thứ hai là

gắn liền với các nguồn lực bổ sung

mà mô hình của bạn có thể cần.

Bạn có ý định cho mô hình của mình tương tác

với dữ liệu bên ngoài hoặc các ứng dụng khác?

Và nếu vậy,

bạn sẽ kết nối với những tài nguyên đó như thế nào?

Cuối cùng là câu hỏi về

mô hình của bạn sẽ được tiêu thụ như thế nào.

Ứng dụng dự định sẽ là gì hoặc

Giao diện API mà mô hình của bạn sẽ

được tiêu thụ thông qua trông như thế nào?

Hãy bắt đầu bằng cách khám phá một vài phương pháp

có thể được sử dụng để tối ưu hóa mô hình của bạn

trước khi triển khai nó để suy luận.

Mặc dù chúng ta có thể dành một số bài học

về chủ đề này, mục đích của phần này

là để cung cấp cho bạn phần giới thiệu về

kỹ thuật tối ưu hóa quan trọng nhất.

Mô hình ngôn ngữ lớn trình bày suy luận

những thách thức về mặt tính toán và

yêu cầu lưu trữ cũng như đảm bảo

độ trễ thấp cho các ứng dụng tiêu thụ.

Những thách thức này vẫn tồn tại cho dù bạn có

triển khai tại cơ sở hoặc trên đám mây và

thậm chí còn trở thành một vấn đề

khi triển khai tới các thiết bị biên.

Một trong những cách cơ bản để

cải thiện hiệu suất ứng dụng

là giảm kích thước của LLM.

Điều này có thể cho phép tải dữ liệu nhanh hơn

mô hình, làm giảm độ trễ suy luận.

Tuy nhiên, thách thức là làm giảm

kích thước của mô hình trong khi vẫn duy trì

hiệu suất mô hình.

Một số kỹ thuật hoạt động tốt hơn

những cái khác cho các mô hình tổng quát, và

có sự cân bằng giữa độ chính xác và

hiệu suất.

Bạn sẽ tìm hiểu về ba

các kỹ thuật trong phần này.

Quá trình chưng cất sử dụng mô hình lớn hơn,

mô hình giáo viên,

để huấn luyện một mô hình nhỏ hơn,

mẫu sinh viên.

Sau đó bạn sử dụng mô hình nhỏ hơn cho

suy luận để giảm dung lượng lưu trữ của bạn và

tính toán ngân sách.

Tương tự như đào tạo nhận thức lượng tử hóa,

lượng tử hóa sau đào tạo

biến đổi trọng số của mô hình thành

một biểu diễn có độ chính xác thấp hơn,

chẳng hạn như dấu phẩy động 16 bit hoặc

số nguyên tám bit.

Như bạn đã học ở tuần một của khóa học,

điều này làm giảm bộ nhớ

dấu chân của mô hình của bạn.

Kỹ thuật thứ ba, Cắt tỉa mẫu,

loại bỏ mô hình dư thừa

các thông số đóng góp ít

đến hiệu suất của mô hình.

Chúng ta hãy nói qua từng

các tùy chọn này chi tiết hơn.

Mẫu chưng cất là

một kỹ thuật tập trung vào

có một mô hình giáo viên lớn hơn

đào tạo một mô hình sinh viên nhỏ hơn.

Mô hình học sinh học cách thống kê

bắt chước hành vi của giáo viên mẫu,

hoặc chỉ trong lớp dự đoán cuối cùng

hoặc trong các lớp ẩn của mô hình.

Bạn sẽ tập trung vào tùy chọn đầu tiên ở đây.

Bạn bắt đầu với giai điệu tinh tế của bạn

LLM là hình mẫu giáo viên của bạn và

tạo LLM nhỏ hơn cho

hình mẫu sinh viên của bạn.

Bạn đóng băng trọng lượng của mô hình giáo viên và

sử dụng nó để tạo ra sự hoàn thành cho

dữ liệu đào tạo của bạn.

Đồng thời,

bạn tạo ra sự hoàn thành cho

dữ liệu huấn luyện sử dụng

hình mẫu sinh viên của bạn.

Chắt lọc kiến thức giữa

mô hình giáo viên và học sinh đã đạt được

bằng cách giảm thiểu hàm mất mát

gọi là tổn thất chưng cất.

Để tính toán sự hao hụt này, chưng cất

sử dụng phân phối xác suất trên

token được sản xuất bởi

lớp softmax của mô hình giáo viên.

Bây giờ, mẫu giáo viên đã có

tinh chỉnh trên dữ liệu huấn luyện.

Vậy khả năng phân bố xác suất

phù hợp chặt chẽ với dữ liệu thực tế thực tế và

sẽ không có nhiều biến thể về mã thông báo.

Đó là lý do tại sao chưng cất

áp dụng một mẹo nhỏ để thêm

một tham số nhiệt độ

đến hàm softmax.

Như bạn đã học ở bài 1,

nhiệt độ cao hơn tăng

sự sáng tạo của ngôn ngữ

mô hình tạo ra.

Với nhiệt độ

tham số lớn hơn một,

phân phối xác suất trở thành

rộng hơn và đạt đỉnh ít mạnh hơn.

Sự phân phối nhẹ nhàng hơn này cung cấp

bạn với một bộ mã thông báo

tương tự như các mã thông báo sự thật cơ bản.

Trong bối cảnh của quá trình chưng cất,

đầu ra của mô hình giáo viên thường được tham khảo

như nhãn mềm và sinh viên

dự đoán của mô hình là dự đoán mềm.

Song song đó bạn huấn luyện mô hình sinh viên

để tạo ra những dự đoán chính xác

dựa trên dữ liệu đào tạo thực tế cơ bản của bạn.

Ở đây, bạn không thay đổi

cài đặt nhiệt độ và

thay vào đó hãy sử dụng hàm softmax tiêu chuẩn.

Chưng cất đề cập đến mô hình sinh viên

kết quả đầu ra như những dự đoán cứng và

nhãn cứng.

Sự mất mát giữa những

hai là sự mất mát của sinh viên.

Sự chưng cất kết hợp và sinh viên

tổn thất được sử dụng để cập nhật trọng số

của mô hình sinh viên thông qua lan truyền ngược.

Lợi ích chính của phương pháp chưng cất

đó là mô hình sinh viên nhỏ hơn

có thể được sử dụng để suy luận trong việc triển khai

thay vì mô hình giáo viên.

Trong thực tế, việc chưng cất không phải là

hiệu quả cho các mô hình giải mã tổng quát.

Nó thường hiệu quả hơn đối với

mô hình chỉ có bộ mã hóa,

chẳng hạn như Burt có rất nhiều

về sự dư thừa đại diện.

Lưu ý rằng với quá trình chưng cất,

bạn đang luyện tập một giây,

mô hình nhỏ hơn để sử dụng trong quá trình suy luận.

Bạn không giảm kích thước mô hình

của LLM ban đầu dưới bất kỳ hình thức nào.

Chúng ta hãy xem mô hình tiếp theo

kỹ thuật tối ưu hóa thực sự

làm giảm kích thước LLM của bạn.

Bạn đã được giới thiệu phương pháp thứ hai,

lượng tử hóa,

trở lại vào tuần một trong

bối cảnh đào tạo.

Cụ thể là đào tạo nhận thức lượng tử hóa,

hay gọi tắt là QAT.

Tuy nhiên, sau khi một mô hình được đào tạo, bạn

có thể thực hiện lượng tử hóa sau đào tạo,

hoặc viết tắt là PTQ để tối ưu hóa nó cho

triển khai.

PTQ chuyển đổi trọng số của mô hình thành

một biểu diễn có độ chính xác thấp hơn,

chẳng hạn như dấu phẩy động 16-bit hoặc

số nguyên 8 bit.

Để giảm kích thước mô hình và

dấu chân bộ nhớ,

cũng như các tài nguyên tính toán cần thiết

để phục vụ mô hình, lượng tử hóa có thể

chỉ được áp dụng cho trọng lượng mô hình hoặc

cho cả trọng lượng và lớp kích hoạt.

Nhìn chung, các phương pháp lượng tử hóa

bao gồm các kích hoạt có thể

có tác động cao hơn đến hiệu suất của mô hình.

Lượng tử hóa cũng yêu cầu thêm

bước hiệu chuẩn để thống kê

nắm bắt phạm vi năng động của

các giá trị tham số ban đầu.

Giống như các phương pháp khác, có sự đánh đổi

bởi vì đôi khi lượng tử hóa

dẫn đến một tỷ lệ nhỏ

giảm số liệu đánh giá mô hình.

Tuy nhiên, sự giảm thiểu đó thường có giá trị

tiết kiệm chi phí và tăng hiệu suất.

Tối ưu hóa mô hình cuối cùng

kỹ thuật là cắt tỉa.

Ở mức độ cao, mục tiêu là giảm

kích thước mô hình để suy luận bằng cách loại bỏ

trọng lượng không đóng góp

nhiều đến hiệu suất tổng thể của mô hình.

Đây là các trọng số có giá trị

rất gần hoặc bằng 0.

Lưu ý rằng một số phương pháp cắt tỉa yêu cầu

đào tạo lại toàn bộ mô hình, đồng thời

những người khác rơi vào loại tham số

tinh chỉnh hiệu quả, chẳng hạn như LoRA.

Ngoài ra còn có những phương pháp

tập trung vào việc cắt tỉa sau đào tạo.

Về lý thuyết, điều này làm giảm kích thước của

mô hình và cải thiện hiệu suất.

Tuy nhiên, trong thực tế có thể có

không ảnh hưởng nhiều đến kích thước và

hiệu suất nếu chỉ một tỷ lệ nhỏ

trọng số của mô hình gần bằng 0.

Lượng tử hóa, chưng cất và

Cắt tỉa tất cả nhằm mục đích giảm kích thước mô hình xuống

cải thiện hiệu suất mô hình trong quá trình

suy luận mà không ảnh hưởng đến độ chính xác.

Tối ưu hóa mô hình của bạn để triển khai

sẽ giúp đảm bảo rằng ứng dụng của bạn

hoạt động tốt và cung cấp cho người dùng của bạn

với cảm giác trải nghiệm tốt nhất có thể.