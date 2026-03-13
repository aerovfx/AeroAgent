# Tóm tắt lỗi cú pháp 001 trong Python

---

Xin chào tất cả mọi người.

Chào mừng trở lại.

Chúng ta hãy tiếp tục bài học này với các lỗi trong Python một cách ngắn gọn.

Lập trình viên mới bắt đầu mắc lỗi khi viết chương trình vì thiếu kinh nghiệm lập trình nói chung

hoặc do không quen với ngôn ngữ lập trình.

Những lập trình viên dày dạn mắc lỗi do bất cẩn hoặc do giải pháp được đề xuất cho một vấn đề

bị lỗi và việc thực hiện đúng một giải pháp không đúng sẽ không tạo ra một chương trình đúng.

Vì vậy, trong Python có ba loại lỗi chung.

Một là lỗi cú pháp.

Và thứ hai là lỗi thời gian chạy.

Và thứ ba là lỗi logic hay lỗi logic.

Chúng ta hãy bắt đầu với một lỗi cú pháp.

Trình thông dịch được thiết kế để thực thi tất cả các chương trình Python hợp lệ.

Trình thông dịch đọc tệp nguồn Python và dịch nó sang dạng thực thi được.

Đây là giai đoạn dịch

Nếu trình thông dịch phát hiện câu lệnh chương trình không hợp lệ trong giai đoạn dịch, nó sẽ chấm dứt

việc thực thi chương trình và báo lỗi.

Những lỗi như vậy là do người lập trình sử dụng sai ngôn ngữ.

Lỗi cú pháp là một lỗi phổ biến mà trình thông dịch có thể phát hiện khi cố gắng dịch một con trăn

câu lệnh sang ngôn ngữ máy.

Ví dụ, ở đây x bằng y cộng hai là hợp lệ.

Biểu thức Python và nó đúng về mặt cú pháp vì nó tuân theo các quy tắc về cấu trúc của

một tuyên bố phân công.

Những gì chúng ta đã thảo luận.

Giả sử nếu chúng ta sửa đổi biểu thức này một chút trong phiên bản khác như thế nào.

Y cộng hai bằng X.

Và lưu ý ở đây rằng chúng tôi đã gặp lỗi ngay lập tức.

Nếu một câu lệnh như thế này xuất hiện trong một chương trình, trình thông dịch sẽ báo lỗi.

Điều này là do.

Đối với biểu thức chúng tôi không thể.

Gán giá trị hoặc biểu thức không thể được coi là một biến.

Được rồi, vậy ở đây nếu bạn nhìn vào biểu thức đầu tiên, X là biến, trong khi Y cũng là một trong

biến.

Nhưng nếu bạn nhìn vào y cộng hai này, nó là một biểu thức.

Vì vậy chúng ta có thể gán biểu thức.

Đối với biến, nhưng chúng ta không thể thực hiện thao tác ngược lại.

Chúng ta có thể gán một biến cho biến khác hoặc biến khác.

Vào thời điểm đó.

Giá trị của một biến sẽ được coi là giá trị của biến kia.

Vì vậy, trong tuyên bố thứ ba này, giá trị của Y.

Sẽ được coi là giá trị của biến x.

Vì vậy giá trị của Y sẽ được đánh giá đầu tiên.

Nếu nó xuất hiện trong chương trình thì giá trị của Y sẽ được gán cho biến x.

Vì vậy, chúng ta có thể thực hiện phép toán ngược lại cho các biến chỉ như y bằng x.

Vì vậy không có lỗi.

Chúng ta có thể gán một giá trị biến cho một giá trị khác.

Giá trị biến hoặc.

Một biến làm giá trị cho một biến khác.

Vì vậy, nếu chúng ta cố gắng thực hiện câu lệnh thứ hai này.

Khi đó chúng ta sẽ gặp lỗi như cú pháp.

Lỗi không thể gán cho người vận hành.

Nó có nghĩa đơn giản là chúng ta có thể nói rằng cú pháp của Python không cho phép biểu thức như Y cộng hai

xuất hiện ở phía bên trái của toán tử gán.

Vì vậy, biểu thức phải luôn xuất hiện ở bên phải của toán tử gán.

Hãy để chúng tôi xem.

Các lỗi cú pháp phổ biến khác phát sinh từ các lỗi đánh máy đơn giản như dấu ngoặc đơn không khớp.

Ví dụ: X bằng.

Thay vì sử dụng.

Dấu ngoặc đơn đầu tiên làm dấu ngoặc đơn mở nếu tôi sử dụng dấu ngoặc đơn đóng rồi mới sử dụng.

Một số giá trị số nguyên.

Giống như hai.

Và cần lưu ý ở đây, trình thông dịch không hiển thị lỗi.

Nhưng nếu chúng ta cố gắng đánh giá điều này trong khi đánh giá, chúng ta sẽ gặp lỗi.

Chúng ta hãy thử đánh giá điều này.

Vì vậy, chúng tôi đã gặp lỗi và khớp nó.

Dấu ngoặc đơn cho dấu ngoặc đơn đóng.

Kế tiếp.

Nếu bạn cố gắng sử dụng khác nhau.

Hợp âm trong một chuỗi.

Sau đó chúng ta sẽ nhận được một.

Lỗi cú pháp.

Vì vậy hãy nhìn vào đây.

Trình thông dịch không hiển thị lỗi nhưng nếu chúng tôi cố gắng đánh giá biểu thức này.

Trình thông dịch sẽ đưa ra lỗi.

Vì vậy, chúng tôi đã gặp lỗi cú pháp.

Cuối dòng trong khi quét chuỗi ký tự.

Một loại lỗi khác xuất hiện với lỗi thụt đầu dòng như x bằng.

Hai.

Và nếu tôi sử dụng sai thụt lề như khoảng trắng rồi gõ y bằng ba.

Nhìn ra đây.

Trình thông dịch không hiển thị lỗi.

Ở giai đoạn này trong khi.

Đang chỉnh sửa chương trình, nhưng nó sẽ báo lỗi nếu bạn cố đánh giá dòng thứ hai này trong ô này.

Chúng ta hãy thử đánh giá dòng đầu tiên này bằng cách nhấn F9.

Không có lỗi.

Chúng ta hãy thử đánh giá điều này và xem điều gì sẽ xảy ra.

Chúng tôi đã có.

Không có lỗi.

Vì nó là file script.

Được rồi.

Nếu chúng ta cố gắng thực hiện thao tác tương tự trong.

Cửa sổ bảng điều khiển hoặc trong trình thông dịch trực tiếp.

Chúng tôi có thể gặp lỗi.

Ví dụ: X bằng hai.

Và nếu.

Sử dụng không gian và y bằng ba.

Vì vậy, ở đây chúng tôi cũng không có lỗi.

Vì vậy, điều này là do chúng tôi chưa sử dụng.

Những câu lệnh này có mã màu đen.

Ví dụ: nếu chúng ta sử dụng các câu lệnh này trong một khối mã, chắc chắn chúng ta sẽ gặp lỗi.

Nếu g bằng.

Bằng một.

X bằng hai.

Và Y bằng ba.

Gán X bằng hai và Y bằng ba.

Và cuối cùng là in.

Các giá trị của.

X và Y.

Chúng ta hãy khởi tạo giá trị Z là một.

Bây giờ hãy nhìn vào đây.

Nếu tôi sử dụng.

Lời mời thẳng thắn.

Sau đó trình thông dịch không hiển thị lỗi.

Nhưng nếu chúng ta cố gắng đánh giá điều này.

Nếu có điều kiện thì chúng ta có thể gặp lỗi.

Chúng ta hãy thử chạy ô này.

Vì vậy, chúng tôi đã gặp lỗi.

Thụt lề.

Lỗi.

Vì vậy, bây giờ bạn đã có.

Ý tưởng về cách sửa lỗi thụt lề trong Python.

Vì vậy, hãy nhìn vào những dòng nhỏ.

Đây là mức thụt lề đầu tiên đối với các dòng ban đầu.

Và dòng nhỏ này.

Đang hiển thị.

Việc thụt lề cho.

Tại sao?

Đúng vậy.

Thông báo cho người dùng về việc thụt lề sai.

Dòng nhỏ này bạn có thể quan sát tại đây.

Dưới x.

Được rồi.

Chúng ta hãy thử thay thế.

Thụt lề thứ hạng với thụt lề bên phải.

Vì vậy, bây giờ bạn có thể thấy dòng nhỏ vừa biến mất.

Bởi vì thụt lề chính xác.

Và nếu cố gắng đánh giá ô này, chúng ta sẽ nhận được.

Không có lỗi.

Vì vậy, những ví dụ này chỉ minh họa một số cách mà các lập trình viên có thể viết.

Một mã được hình thành không đúng.

Trình thông dịch phát hiện lỗi cú pháp trước khi bắt đầu chạy chương trình.

Và nó sẽ không thực thi bất kỳ phần nào của chương trình có lỗi cú pháp.

Trong khi chỉnh sửa thông dịch viên có thể.

Thí điểm các lỗi cú pháp.

Nhưng trong khi đánh giá nó chắc chắn sẽ kiểm tra tất cả các lỗi cú pháp.

Nếu tìm thấy thì nó sẽ dừng lại.

Đánh giá các câu lệnh còn lại và báo lỗi cú pháp ở dòng cụ thể đó.