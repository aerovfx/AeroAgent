# 4 -Xây dựng và đào tạo model.en US

---

WEBVTT

Và vì vậy, chúng tôi sẽ bắt đầu bằng việc xác định việc xây dựng mô hình của mình và sau đó đào tạo mô hình của chúng tôi

để xem nó hoạt động tốt như thế nào trên tập dữ liệu mà chúng ta vừa có.

Đầu vào.

Nhưng trước khi tiếp tục và thực sự xác định mô hình, hãy để tôi cung cấp lại cho bạn một số thông tin tóm tắt

mạng.

Vì vậy, tôi đã trình bày một phần nội dung đó trong video giới thiệu và tôi đã nhấn mạnh lý do tại sao chúng tôi sử dụng lithium,

phải không?

Bởi vì nó có kiến trúc phản hồi, kết nối, phản hồi, kết nối giúp đỡ và cho phép các nhóm

để hiểu toàn bộ chuỗi dữ liệu, ghi nhớ toàn bộ chuỗi dữ liệu, một lần nữa,

giúp nâng cao độ chính xác, khả năng dự đoán của mô hình.

Và đối với những tập dữ liệu có nhiều trình tự trong đó, Đúng vậy.

Vì vậy, đó là lý do tại sao, đồng tính nữ đặc biệt giỏi xử lý và không xử lý, nhưng

xử lý chuỗi dữ liệu.

Đó có thể là một văn bản, một bài phát biểu hoặc tập dữ liệu chuỗi thời gian chung.

Mô hình mạng lưới thần kinh chính trị.

Điều xảy ra là khi chúng tôi đưa dữ liệu đầu vào vào lớp đầu tiên và sau đó là độ lệch có trọng số, thì độ lệch có trọng số sẽ

thiên vị, chúng ta nhận được một số đầu ra từ lớp đầu tiên, lớp này sẽ trở thành đầu vào cho lớp tiếp theo.

Phải?

Và đây là điều xảy ra trong mạng nơi đầu ra của lớp đầu tiên trở thành lớp tiếp theo, đầu vào,

và sau đó chúng ta đi đến lớp tiếp theo.

Chúng tôi có đầu ra của nó là đầu vào của lớp tiếp theo cho đến khi chúng tôi đạt đến lớp đầu ra.

Đó là lớp cuối cùng.

Nhưng lớp cuối cùng hiểu rằng trọng lượng là bao nhiêu và độ lệch của lớp đầu tiên là gì.

Không, không phải vậy, phải không?

Nó không.

Vì vậy, hệ thống thực sự có một mạng phản hồi giúp ghi nhớ hoặc giúp hiểu

bên phải, giúp hiểu được.

Nó giúp hiểu được điều đúng.

Nó giúp hiểu rằng lớp đầu ra cũng hiểu những gì đang xảy ra trong năm đầu tiên.

Vì vậy, đó là nhóm của chúng tôi đang làm việc.

Bellevue vừa đưa ra mô hình tuần tự.

Nhưng thực tế thì chúng tôi đang viết phần chúng tôi đang viết phần nhúng và chúng tôi đang thêm phần đầu tiên

lớp sẽ là lớp nhúng sự kiện có kích thước từ vựng.

Một lần nữa, đây là danh sách các từ duy nhất mà chúng tôi có.

Và sau đó là nơ-ron 15 lớp, không phải lớp và độ dài đầu vào, phải không?

Bây giờ lý do chúng ta lật úp ở đây là vì, như tôi đã nói với bạn, khi chúng ta có vectơ dữ liệu 3D, chúng ta có ba

các phần tử bên trong vector của tôi.

Hiện nay.

Uh, điều tôi vừa làm là tạo ra một vectơ từ có độ dài, kích thước từ vựng, có nghĩa là

Tôi có một vector Ở đâu?

Vâng, tôi có một vectơ trong đó, giả sử từ I, tôi có vectơ 10000 cho đến khi chúng ta bị lật úp.

Vậy thì tôi có lời tiếp theo, đó là.

Và sau đó tôi có vectơ từ cho nó là 0 dấu phẩy 10000 cho đến khi chúng ta lật úp.

Bằng cách này, tôi có thể tạo ra các vectơ và độ dài của mỗi vectơ sẽ là độ dài bị lật, phải không?

Bởi vì mỗi vectơ sẽ có giá trị bằng một tại một vị trí duy nhất để xác định một từ duy nhất trong vốn từ vựng của tôi.

Tiếp theo, tôi có A.T.M. mô hình mà tôi đã sử dụng và đưa ra mức độ quan trọng là 50 một lần nữa, tương tự cho lần tiếp theo

mô hình.

Sau đó, chúng ta có mô hình dày đặc, mô hình dày đặc, hiểu kích thước đầu vào là bao nhiêu và sử dụng

hàm kích hoạt, có giá trị tự tối đa, một lần nữa được sử dụng để phân loại.

Bây giờ chúng ta đang phân loại ở đây phải không?

Cách chúng tôi phân loại.

Chúng tôi đang lấy biến đầu vào và xem hoặc phân loại các từ duy nhất.

Từ nào sẽ là dự đoán.

Về cơ bản những gì chúng tôi đang làm là giả sử có Lớp A, Lớp B, nhưng ngoài ra, chúng tôi có

từ A đó là A và sẽ là như vậy.

Vì vậy, tôi đang cố gắng dự đoán xem từ tiếp theo có phải là a hay không.

Đó là cách phân loại đang hoạt động ở đây.

Và sau đó chúng tôi vừa biên dịch mô hình bằng trình tối ưu hóa.

Adam Và độ chính xác làm thước đo.

Phải.

Và khi lắp, chúng ta thấy điều đó.

Độ chính xác đạt chỉ đạt 27% trong 50 kỷ nguyên.

Đó không phải là ít hơn, nhưng đó cũng không phải là lớn.

Steichen.

Vì vậy, có hai lý do cho điều đó.

Thứ nhất, như bạn có thể thấy, mô hình đã tăng độ chính xác lên từng chút một và bạn có thể thấy điều đó

mức lỗ cũng giảm dần.

Vì vậy, nếu tôi thực hiện nhiều chu kỳ hơn hoặc nhiều kỷ nguyên hơn thì tôi sẽ nhận được kết quả tốt hơn.

Điều thứ hai là, như tôi đã nói với bạn, tôi chỉ lấy dữ liệu như một phần của tập dữ liệu 700 đầu tiên

câu trong số 6000.

Vì vậy, nếu bạn đang sử dụng nhiều dữ liệu hơn, mô hình của bạn sẽ được xây dựng trên các trọng số phức tạp hơn và nó sẽ cung cấp

bạn với độ chính xác tốt hơn.

Phải.

Vì vậy, bạn có thể thử bằng cách tăng kích thước của tập dữ liệu và xem độ chính xác có tăng hay không,

mặc dù không có lựa chọn nào về việc nó có tăng hay không.

Điều tiếp theo là điều tôi đã làm là lưu mô hình của mình, phải không, vì tôi sẽ sử dụng lại mô hình đó.

Nhưng tôi cũng đã lưu đối tượng được mã hóa của mình vì nó phù hợp với tập dữ liệu và nó hiểu liệu

Tôi có một số dữ liệu mới, tôi sẽ chuyển đổi dữ liệu mới hoặc dữ liệu văn bản đó thành các vectơ như thế nào.

Lấy làm tiếc.

Đó là chủ nghĩa tokenism.

Vì thế.

Hãy dành thời gian để mã hóa dữ liệu.

Ờ, được rồi.

Vâng.

Vì vậy, hàm tôi vừa tạo này để dự đoán xem liệu mô hình của tôi có hoạt động tốt hay không,

và nếu tôi dự đoán kết quả sẽ như thế nào.

Nhưng nó lại lấy mô hình giá trị bởi tôi sẽ chuyển mô hình này ở đây mà tôi đã lưu ở đây.

Sau đó là người tổ chức mà tôi đã lưu ở đây.

Vì vậy, độ dài chuỗi, đó là độ dài tôi đã sử dụng để xác định biến đầu vào của mình, lại là 50.

Sau đó, nhắn tin văn bản thực tế mà chúng ta sẽ xử lý để xem chuỗi từ tiếp theo là gì

sẽ như vậy.

Phải?

Chúng tôi có dữ liệu này làm dữ liệu đầu vào của chúng tôi.

Sau đó, chúng tôi sẽ sử dụng điều này để dự đoán chuỗi mã tiếp theo.

Và cuối cùng, bạn muốn bao nhiêu từ.

Bạn muốn có 12 từ được dự đoán sau văn bản hoặc 20 từ tương tự.

Vậy điều tôi đang làm là tôi đang dự đoán Ethan.

Vì vậy, những gì đang xảy ra trong chu kỳ này, tôi dự đoán một từ.

Tôi nối thêm từ đó và chúng tôi thiết lập chỉ mục rồi dự đoán từ tiếp theo, nối từ đó vào từ hiện có

lập chỉ mục, sau đó xây dựng và gửi lại vào đây để dự đoán từ tiếp theo.

Và tôi cứ làm như vậy cho đến khi hoàn thành đủ số từ mà tôi muốn dự đoán.

Đó là những gì đã và đang xảy ra ở đây.

Điều này ở đây là một chức năng mới.

Bạn cũng có thể đã thấy điều đó trong đoạn mã trên.

Vì vậy, về cơ bản đây là một chức năng đệm.

Nhưng điều xảy ra là giả sử rằng tôi đã tạo một vectơ từ, nhưng nó không có nó không

có nhiều như vậy.

Chiều dài của chiều dài của vectơ từ mà tôi đã tạo không dài như tôi yêu cầu.

Vì vậy, những gì tôi đang làm là tôi đang đệm nó.

Vì vậy, giả sử tôi muốn học cách lên sáu, nhưng tôi chỉ đạt được năm ở đây, vì vậy nó sẽ thêm số 0 vào

ở cuối để tạo thành chiều dài sáu.

Nhưng giả sử tôi có một vectơ từ có độ dài bảy, nhưng tôi chỉ mới sáu tuổi.

Vì vậy, nó sẽ cắt ngắn.

Điều đó có nghĩa là nó sẽ đẩy nó trở lại hoặc loại bỏ các phần tử để nó trở lại độ dài bằng 6 như tôi

chỉ là dự đoán thôi.

Và từ đó được dự đoán là một lần nữa.

Hãy chuyển đổi nó ra rồi đặt nó ra với bề ngoài rồi thêm vào kết quả.

Và cuối cùng, kết quả là như nhau.

Ngay cả ở đây, chỉ từng từ một sẽ chết.

Vì vậy, bạn có mã thông báo bên trong.

Đó không phải là câu thực tế.

Họ phải nối các từ của bạn và tạo ra một câu từ đó để chúng tôi chỉ có thể trả lại văn bản.

Như bạn có thể thấy, tôi vừa ừ, vậy nên việc tôi vừa làm là tôi vừa tạo ra. Tôi vừa có một dòng đó là

Dài 50 token phải không?

Bởi vì chúng ta đã chuyển đổi nên chúng ta có dãy số là 50.

Bắt đầu với chuỗi dưới dạng vectơ có độ dài 50, sau đó chỉ cần tải mô hình, tải trình tổ chức, gửi

tất cả dữ liệu đó vào hàm tạo SEQ của tôi.

Và như bạn có thể thấy ở đây.

Vì vậy, đây là những gì tôi đã đưa ra làm đầu vào cho văn bản này.

Và đây bạn có thể thấy đây là dự đoán.

Được rồi, sau nhiều thời đại, điều mà ít nhà văn vĩ đại nào có thể đoán trước được, họ

không nhận thức được nhu cầu kết nối trong bài viết của chính họ hoặc những lỗ hổng trong hệ thống của họ, blah, blah,

bla.

Và cuối cùng, bạn nhận được kết quả tốt nhất là Cộng hòa không được coi là hiện thân.

Không có.

Nhưng cho đi không phải hai lần.

Đó là vì nó đã tiên đoán sẽ không đến hai lần.

Một lần nữa, mô hình không phải là mô hình tốt nhất, nhưng bạn có thể thấy chuỗi từ tiếp theo rất đẹp

nhiều thứ được đưa ra ngay lập tức bởi mô hình xe lửa và chức năng mà chúng tôi đã tạo ra.

Phải?

Bạn thậm chí có thể bỏ ghi chú dòng này và xem điều gì đang xảy ra ở đây, nhưng lưu ý rằng tôi có dữ liệu đầu vào

và không phải một chuỗi 50 thẻ hay 50 từ, mà là một chuỗi tôi nghĩ là 1617 từ.

Phải?

Vì vậy, nếu bạn nhập thông tin này, nó sẽ báo lỗi vì dữ liệu đầu vào của bạn khi bạn đang đào tạo

mô hình của bạn là một câu gồm 50 từ hoặc 50 thẻ.

Đó là một lần nữa.

Chuyển đổi nó thành vectơ.

Vì vậy, bạn sẽ cần một chuỗi từ dài 50 làm đầu vào.

Bạn chỉ có thể thay đổi mã đó trong đoạn mã trên và biến nó thành số 10 hoặc 15.

Phải.

Nhưng với điều này chúng ta đã hoàn thành phần đầu tiên là xây dựng và huấn luyện mô hình.

Sau đó, phần tiếp theo chúng ta sẽ tiến về phía trước và hiểu cách chúng ta sẽ làm việc với Django

khuôn khổ.